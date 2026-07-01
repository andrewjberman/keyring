#!/usr/bin/env python3
"""
_trino_fed -- reusable query capability over the LIVE Trino federation (NFRA heat/analytics
federation; S5 served-wiring). Tool-HOME-agnostic: this is the MODULE the consumable surface
imports -- whether that surface is a `comp-heat federated` subcommand (option A, pending CTO
rule on their tool) or a sibling `comp-fed` CLI (option B). The query mechanism + canonical
queries live here; the CLI wrapper is thin and added once CTO rules the tool-home.

TRANSPORT (COO-endorsed v0, 2026-06-29): the Trino coordinator (trino.opal-globgrph.local:8080)
is IN-VPC ONLY (private Cloud Map DNS, SG ingress from the VPC CIDR) and session-manager-plugin
is not installed locally -- so a query runs as an in-VPC one-shot Fargate task on the
opal-globgrph cluster that curls the Trino REST API, with the result read back from CloudWatch.
~3-4 min/call (image pull + query) -- an ANALYTICAL surface, not interactive. ZERO new attack
surface (no public endpoint). A persistent authenticated endpoint (sub-second) is the
SCTY-GATED follow-on (option 2) -- HELD, not built, per COO (it reads the whole estate graph).

Federation surface (memory/project_trino_federation_layer_live.md):
  iceberg.globgrph.{graph_nodes,graph_edges,graph_contracts}   (Nessie-backed iceberg)
  code_heat.globgrph.code_heat                                  (git code-heat, Glue over parquet)
  JOIN key: substr(graph_nodes.node_id,8) = code_heat.graph_path   (node_id='module:<wspath>',
            file-grain node_type='Module'; path also in props['path'])

Author: 0.8.0_AE_CloudComp. 2026-06-29. (S5 query-module; tool-home pending CTO A-vs-B rule.)
"""
from __future__ import annotations

import json
import re
import sys

CLUSTER = "opal-globgrph"
TASK_DEF = "globgrph-trino"
SUBNET = "subnet-023db8cbfd99ffff2"
SG = "sg-0715c43654a151f69"
LOG_GROUP = "/ecs/globgrph/trino"
REGION = "us-east-1"

_SQLMARK = "@@CHQ@@"
_DONEMARK = "@@CHDONE@@"

# --- canonical federated queries (the net-new value: GRAPH x CODE-HEAT, not git-local heat) ---
Q_CODE_BANDS = (
    "SELECT ch.heat_band, count(*) AS n_files, round(avg(ch.heat_score),3) AS avg_score "
    "FROM iceberg.globgrph.graph_nodes g "
    "JOIN code_heat.globgrph.code_heat ch ON substr(g.node_id,8) = ch.graph_path "
    "WHERE g.node_id LIKE 'module:%' GROUP BY ch.heat_band ORDER BY n_files DESC"
)
Q_CODE_COLDEST = (
    "SELECT substr(g.node_id,8) AS file, ch.heat_band, ch.heat_score "
    "FROM iceberg.globgrph.graph_nodes g "
    "JOIN code_heat.globgrph.code_heat ch ON substr(g.node_id,8) = ch.graph_path "
    "WHERE g.node_id LIKE 'module:%' ORDER BY ch.heat_score ASC LIMIT {top}"
)
Q_TABLES = "SHOW TABLES FROM iceberg.globgrph"


def _runtime_script(sqls: list[str]) -> str:
    """Bash that curls the Trino REST API for each SQL, following nextUri, echoing each JSON page.
    Each SQL is passed as one bash arg wrapped in single quotes; any single quote INSIDE the SQL
    (e.g. the LIKE 'module:%' literal in the canonical queries) is bash-escaped -- close the quote,
    add an escaped literal quote, reopen -- so it transports intact. (M4 fix: the v0 guard used to
    RAISE on a bare single quote, which crashed comp-heat federated on its OWN default query.)"""
    parts = [
        "B=http://trino.opal-globgrph.local:8080",
        ("q(){ echo \"" + _SQLMARK + " $1\"; "
         "r=$(curl -s -XPOST \"$B/v1/statement\" -H 'X-Trino-User: comp-heat' --data \"$1\"); echo \"$r\"; "
         "n=$(echo \"$r\" | grep -o '\"nextUri\":\"[^\"]*\"' | head -1 | sed 's/.*\"nextUri\":\"//;s/\"$//'); "
         "i=0; while [ -n \"$n\" ] && [ $i -lt 90 ]; do i=$((i+1)); r=$(curl -s \"$n\"); echo \"$r\"; "
         "n=$(echo \"$r\" | grep -o '\"nextUri\":\"[^\"]*\"' | head -1 | sed 's/.*\"nextUri\":\"//;s/\"$//'); "
         "sleep 1; done; }"),
    ]
    for sql in sqls:
        # Bash single-quote escaping (' -> '\'' : end-quote, escaped literal quote, reopen-quote) so
        # a SQL with single quotes -- the LIKE 'module:%' in the canonical queries -- transports intact
        # instead of crashing. (M4 fix: replaced the guard that RAISED on the default query.)
        esc = sql.replace("'", "'\\''")
        parts.append("q '" + esc + "'")
    parts.append("echo " + _DONEMARK)
    return "; ".join(parts)


def run_federated_query(sqls: list[str], *, delay: int = 15, max_attempts: int = 40) -> list[dict]:
    """Run SQLs in one in-VPC Fargate task; return [{sql, columns, rows}] per query.
    Requires boto3 + AWS creds with ecs:RunTask on the globgrph-trino task-def + logs:GetLogEvents."""
    import boto3  # lazy: importing the module must not require boto3 just to read the constants

    ecs = boto3.client("ecs", region_name=REGION)
    logs = boto3.client("logs", region_name=REGION)
    overrides = {"containerOverrides": [{"name": "trino", "command": [_runtime_script(sqls)]}]}
    netcfg = {"awsvpcConfiguration": {"subnets": [SUBNET], "securityGroups": [SG],
                                      "assignPublicIp": "ENABLED"}}
    print("comp-heat/federated: launching in-VPC Trino query task (~3-4 min)...", file=sys.stderr)
    resp = ecs.run_task(cluster=CLUSTER, taskDefinition=TASK_DEF, launchType="FARGATE",
                        networkConfiguration=netcfg, overrides=overrides)
    if not resp.get("tasks"):
        raise RuntimeError(f"run_task failed: {resp.get('failures')}")
    task_arn = resp["tasks"][0]["taskArn"]
    task_id = task_arn.rsplit("/", 1)[-1]
    ecs.get_waiter("tasks_stopped").wait(
        cluster=CLUSTER, tasks=[task_arn],
        WaiterConfig={"Delay": delay, "MaxAttempts": max_attempts})
    events = logs.get_log_events(logGroupName=LOG_GROUP, logStreamName=f"trino/trino/{task_id}",
                                 limit=500, startFromHead=True)
    blob = " ".join(e["message"] for e in events["events"])
    return parse_results(blob)


def parse_results(blob: str) -> list[dict]:
    """Pull columns+rows for each query from the concatenated Trino REST JSON pages."""
    results: list[dict] = []
    for chunk in blob.split(_SQLMARK)[1:]:
        m_cols = re.search(r'"columns":\[(.*?)\],"(?:data|stats)"', chunk)
        cols = re.findall(r'"name":"([^"]+)"', m_cols.group(1)) if m_cols else []
        rows: list = []
        for m in re.finditer(r'"data":(\[.*?\]),"stats":\{"state":"\w+"', chunk):
            try:
                rows.extend(json.loads(m.group(1)))
            except json.JSONDecodeError:
                continue
        err = re.search(r'"errorName":"([^"]+)"', chunk)
        results.append({"sql": chunk.strip().split("\n", 1)[0].strip(),
                        "columns": cols, "rows": rows,
                        "error": err.group(1) if err else None})
    return results


def render_table(res: dict) -> str:
    cols, rows = res["columns"], res["rows"]
    if res.get("error"):
        return f"ERROR: {res['error']}"
    if not cols:
        return "\n".join(str(r) for r in rows)
    srows = [[str(v) for v in r] for r in rows]
    widths = [len(c) for c in cols]
    for r in srows:
        for i, v in enumerate(r[:len(widths)]):
            widths[i] = max(widths[i], len(v))
    out = ["  ".join(c.ljust(widths[i]) for i, c in enumerate(cols)),
           "  ".join("-" * w for w in widths)]
    out += ["  ".join(v.ljust(widths[i]) for i, v in enumerate(r[:len(widths)])) for r in srows]
    return "\n".join(out)


if __name__ == "__main__":
    # Smoke path: `python _trino_fed.py [code|tables]` -- runs a live federated query.
    mode = sys.argv[1] if len(sys.argv) > 1 else "code"
    qs = {"code": [Q_CODE_BANDS], "tables": [Q_TABLES]}.get(mode, [Q_CODE_BANDS])
    for r in run_federated_query(qs):
        print(f"\n# {r['sql'][:90]}")
        print(render_table(r))
