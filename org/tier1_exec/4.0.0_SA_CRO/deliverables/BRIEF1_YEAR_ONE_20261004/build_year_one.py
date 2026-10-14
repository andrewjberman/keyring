#!/usr/bin/env python
"""build_year_one.py -- Brief #1 one-pager: a year of commits, with the events that mattered.

Usage: python build_year_one.py [--out PATH] [--until YYYY-MM-DD]

Andrew-direct 2026-10-04 ~19:4xZ (record: ../ANDREW_DIRECT_20261004_194xZ_BRIEF1_WHERE_WEVE_BEEN_ONE_YEAR_SCALE_ONE_PAGER.md):
a one-page view led by a large area chart of commit volume since the ajb_workspace and portal
repos began, with lines for key events (partners onboarded, pages built, pipelines built).
Template: the Opal Daily Operating Report (/sprint), daily_reports/templates/daily_report_template.html.

Population: BOTH repos (this workspace and the portal submodule), ALL refs, NO merges -- the same
frame as daily_reports/scripts/commit_census.py, whose classify() is reused unchanged, so a week
here and a day on /sprint are two views of one measurement. A commit reachable from both repos is
impossible (separate histories); a commit seen on several refs of one repo is counted once.

Claims: commit counts are MEASURED (git). The kind of work is INFERRED (path rules, commit_census).
Each event in events.json carries its own claim and evidence. Nothing here reads mail.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import html
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                      cwd=HERE).stdout.strip()
sys.path.insert(0, os.path.join(ROOT, "daily_reports", "scripts"))
from commit_census import classify  # noqa: E402  (reuse the estate's kind-of-work rules)

# Andrew-direct 2026-10-14 ~21:3xZ: coordination over product IS product ("an essential part of product creation");
# split only what is directly product-focused from audit, and audit is "just logs and doc creation". So two bands
# plus the named residual. The kinds still come from commit_census.classify (shared with /sprint, unchanged); only
# GOVERNANCE is split here, by path: a GOVERNANCE commit is AUDIT only when every governance-family file it touches is
# a RECORD (a ledger, a surprise-channel investigation row, the tier-0 ledger); project deliverables, task orders,
# decompositions, PRDs, registers and rules files under the same family are product work and stay product.
GROUPS = [
    ("product", "Product", "Code, data, design, testing, deliverables, and the task orders and decompositions that coordinate them",
     {"FRONTEND", "BACKEND", "DATA", "PLANNING", "VERIFICATION", "DELIVERABLES", "COORDINATION", "TOOLING", "GOVERNANCE"}),
    ("audit", "Audit", "Session logs, deploy and project ledgers, investigation records",
     {"AUDIT"}),
    ("other", "Unclassified", "Paths no rule claims (named residual)", {"UNATTRIBUTED"}),
]
KIND2GROUP = {k: g[0] for g in GROUPS for k in g[3]}
GOVERNANCE_FAMILY = re.compile(r"^org/(tier0|missions|standards|ref|projects|surprise_channel|critical_paths)/"
                               r"|^CLAUDE\.md|^org/XXX\.md")
RECORD_PATHS = re.compile(r"^org/missions/[^/]+/[^/]+/[^/]+/(surprise-channel|ledger)/"
                          r"|^org/(critical_paths|surprise_channel|tier0)/")


def group_of(kind, files):
    """The page band of one commit: its commit_census kind, with GOVERNANCE split into record-keeping vs product."""
    if kind == "GOVERNANCE":
        gov = [f for f in files if GOVERNANCE_FAMILY.search(f)]
        if gov and all(RECORD_PATHS.search(f) for f in gov):
            return "audit"
    return KIND2GROUP[kind]
AGENT_DOMAINS = ("opal.agent", "runtime.agent")


def git_rows(repo_dir, prefix):
    out = subprocess.run(["git", "-C", repo_dir, "log", "--all", "--no-merges", "--no-renames",
                          "--format=@@%H|%aI|%an|%ae", "--name-only"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    if out.returncode != 0:
        raise SystemExit("ERROR: git log failed in %s: %s" % (repo_dir, out.stderr.strip()))
    rows, cur = [], None
    for line in out.stdout.splitlines():
        if line.startswith("@@"):
            h, ad, an, ae = line[2:].split("|", 3)
            cur = {"h": h, "ad": ad, "an": an, "ae": ae, "files": []}
            rows.append(cur)
        elif line.strip() and cur is not None:
            cur["files"].append(prefix + line.strip())
    return rows


def monday(d):
    return d - dt.timedelta(days=d.weekday())


def census(until):
    # PORTAL FIRST: some workspace refs also reach portal history (measured 2026-10-04: 254 portal
    # commits are reachable from a workspace ref). Whichever repo is read first owns a shared hash,
    # and only the portal read carries the portal/ prefix the kind rules need.
    repos = [("portal", os.path.join(ROOT, "portal"), "portal/"), ("workspace", ROOT, "")]
    seen, commits = set(), []
    for name, path, prefix in repos:
        for r in git_rows(path, prefix):
            if r["h"] in seen:
                continue
            seen.add(r["h"])
            r["repo"] = name
            r["date"] = dt.datetime.fromisoformat(r["ad"]).date()
            if r["date"] > until:
                continue
            r["group"] = group_of(classify(r["an"], r["files"]), r["files"])
            r["agent"] = r["ae"].split("@")[-1] in AGENT_DOMAINS
            commits.append(r)
    start = min(c["date"] for c in commits)
    weeks, w = [], monday(start)
    while w <= until:
        weeks.append(w)
        w += dt.timedelta(days=7)
    widx = {w: i for i, w in enumerate(weeks)}
    gkeys = [g[0] for g in GROUPS]
    series = {g: [0] * len(weeks) for g in gkeys}
    month = collections.defaultdict(lambda: {"total": 0, "workspace": 0, "portal": 0, "human": 0,
                                             "agent": 0, **{g: 0 for g in gkeys},
                                             "seats": set(), "identities": set()})
    for c in commits:
        series[c["group"]][widx[monday(c["date"])]] += 1
        m = month[c["date"].strftime("%Y-%m")]
        m["total"] += 1
        m[c["repo"]] += 1
        m[c["group"]] += 1
        m["agent" if c["agent"] else "human"] += 1
        if c["agent"]:
            m["identities"].add(c["an"])
            base = c["an"].split("~")[0]
            if not base.startswith("0.9.0_WK"):
                m["seats"].add(base)
    months = []
    for k in sorted(month):
        m = month[k]
        months.append({"month": k, **{x: m[x] for x in ("total", "workspace", "portal", "human", "agent", *gkeys)},
                       "seats": len(m["seats"]), "identities": len(m["identities"])})
    totals = [sum(series[g][i] for g in gkeys) for i in range(len(weeks))]
    peak = max(range(len(weeks)), key=lambda i: totals[i])
    first_agent = min((c for c in commits if c["agent"]), key=lambda c: c["ad"])
    return {
        "weeks": [w.isoformat() for w in weeks],
        "series": [[g, series[g]] for g in gkeys],
        "months": months,
        "total": len(commits),
        "by_repo": {r: sum(1 for c in commits if c["repo"] == r) for r in ("workspace", "portal")},
        "by_group": {g: sum(series[g]) for g in gkeys},
        "peak_week": {"week": weeks[peak].isoformat(), "commits": totals[peak]},
        "first_commit": {"workspace": min(c["ad"] for c in commits if c["repo"] == "workspace"),
                         "portal": min(c["ad"] for c in commits if c["repo"] == "portal")},
        "first_agent_commit": {"date": first_agent["ad"], "author": first_agent["an"],
                               "commit": first_agent["h"][:10]},
        "until": until.isoformat(),
        "method": "both repos, all refs, merges excluded; kind of work from the files each commit touched "
                  "(daily_reports/scripts/commit_census.py rules), grouped into product and audit plus a named residual",
        "claim": {"counts": "measured", "kind": "inferred"},
    }


def page_numbers(data):
    m = {r["month"]: r for r in data["months"]}

    def span(*months):
        return sum(m[x]["total"] for x in months if x in m)

    dec, sep = m["2025-12"], m["2026-09"]
    return {
        "total": "{:,}".format(data["total"]),
        "dec": "{:,}".format(dec["total"]),
        "sep": "{:,}".format(sep["total"]),
        "multiple": "{:,}".format(round(sep["total"] / dec["total"])),
        "dec_product": "{:,}".format(dec["product"]),
        "sep_product": "{:,}".format(sep["product"]),
        "product_multiple": "{:,}".format(round(sep["product"] / dec["product"])),
        "peak_week": "{:,}".format(data["peak_week"]["commits"]),
        "p1": "{:,}".format(span("2025-11", "2025-12", "2026-01", "2026-02")),
        "p2": "{:,}".format(span("2026-03", "2026-04")),
        "p3": "{:,}".format(span("2026-05", "2026-06", "2026-07")),
        "p4": "{:,}".format(span("2026-08", "2026-09", "2026-10")),
        "apr_seats": str(m["2026-04"]["seats"]),
        "sep_identities": "{:,}".format(sep["identities"]),
        "audit_share": str(round(100 * data["by_group"]["audit"] / data["total"])),
    }


def fill_tokens(obj, nums):
    """Replace {{name}} in every string of the page block; an unknown token fails LOUD."""
    if isinstance(obj, str):
        out = obj
        for k, v in nums.items():
            out = out.replace("{{%s}}" % k, v)
        if "{{" in out:
            raise SystemExit("ERROR: unfilled token in page text: %s" % out)
        return out
    if isinstance(obj, list):
        return [fill_tokens(x, nums) for x in obj]
    if isinstance(obj, dict):
        return {k: fill_tokens(v, nums) for k, v in obj.items()}
    return obj


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=os.path.join(HERE, "YEAR_ONE_ONE_PAGER.html"))
    ap.add_argument("--until", default=dt.date.today().isoformat())
    ap.add_argument("--data-out", default=os.path.join(HERE, "year_one_data.json"))
    a = ap.parse_args()
    data = census(dt.date.fromisoformat(a.until))
    with open(os.path.join(HERE, "events.json"), encoding="utf-8") as f:
        ev = json.load(f)
    # An event past --until would sit beyond the chart's last week: the page stops at one date everywhere.
    data["events"] = [e for e in ev["events"] if e["date"] <= data["until"]]
    # Every number the page's prose states is computed HERE from the same census the chart draws,
    # never typed into events.json: a re-run on a later day moves the chart and the words together.
    data["page"] = fill_tokens(ev["page"], page_numbers(data))
    data["groups"] = [[g[0], g[1], g[2]] for g in GROUPS]
    with open(a.data_out, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1)
    with open(os.path.join(HERE, "year_one_template.html"), encoding="utf-8") as f:
        tpl = f.read()
    payload = json.dumps(data, ensure_ascii=True).replace("</", "<\\/")
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(tpl.replace("__DATA__", payload))
    print("OK: wrote %s" % a.out)
    print("  commits %d (workspace %d, portal %d); weeks %d; events %d; peak week %s = %d"
          % (data["total"], data["by_repo"]["workspace"], data["by_repo"]["portal"], len(data["weeks"]),
             len(data["events"]), data["peak_week"]["week"], data["peak_week"]["commits"]))
    print("  claim: counts measured, kind inferred; escaped title check: %s"
          % html.escape(data["page"].get("headline", ""))[:80])


if __name__ == "__main__":
    main()
