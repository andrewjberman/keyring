#!/usr/bin/env python3
"""comp-iam LIVE-PRIMARY plane: the real estate is the population; Terraform is an overlay.

Andrew-direct 2026-07-22: "Instead of keying off terraform resources as primary, it keys off the real
state as primary, which should all be discoverable via kuzu anyway."

WHY THE FLIP IS CORRECT -- and it is a stronger reason than "the terraform doesn't exist yet"
------------------------------------------------------------------------------------------------
comp-iam's DESIRED->APPLIED join is exact string equality on RoleName. Terraform source is a TEMPLATE:
names, ARNs and ids are resolved at APPLY time. So `iam_cli` holds a parsed role literally named

    opal-assets-silver-${each.key}-role

-- one template row that can never equal any of the six real roles it produces. THE UNJOINABLE CLASS
IS NOT A PARSER GAP; IT IS A CATEGORY ERROR. A template has no name, so it cannot be joined by name,
and no amount of better parsing fixes that. Keying off live state is not merely "more logical": it is
the only plane on which identifiers are actually identifiers.

FEDERATE, DO NOT BUILD
----------------------
The live-vs-declared reconciliation ALREADY EXISTS and is already correct. `comp-aws derive` is
0.7.0's certed live-boto3 + TF reconciler (oracle-scored), and `infra/aws/globgrph/fedobs/
fedobs_emit.py:200-218` states the principle verbatim: "FEDERATE-NOT-BUILD ... this adapter READS its
derive JSON only, never calls AWS itself." Its output is what kuzu's `drift_class` is built from.

Crucially, the derive joins on ARN IDENTITY and carries the TF ADDRESS as provenance
(`tf_module` / `tf_resource` / `tf_type`), not the rendered name -- which is exactly why it gets the
interpolated fleet right where comp-iam and a literal grep both got it wrong. Verified 2026-07-22:
all six opal-assets-silver-* roles and all three opal-*-served-guard roles come back DECLARED with a
real tf_resource address.

So this module does NOT re-derive drift. It CONSUMES the certed derive, applies the vintage discipline
the derive artifact lacks, and reports live-primary with stated denominators.

THE VINTAGE PROBLEM IS NOT SOLVED BY THE FLIP -- IT MOVES
---------------------------------------------------------
The derive artifact is a file on disk with no self-declared vintage, exactly like the 2026-06-03
census. Measured 2026-07-22: the on-disk IAM derive reported live=183 while a fresh
get-account-authorization-details returned 205. Twenty-two live roles had appeared since it was
written, and nothing in the artifact says so.

    A LIVE-PRIMARY TOOL READING A STALE SNAPSHOT OF "LIVE" IS NOT LIVE-PRIMARY. It is
    Terraform-primary's failure mode wearing the other plane's clothes -- and it fails in the
    same direction, reporting a smaller population than exists, so MISSING reads as ABSENT.

Hence: the same fail-closed gate built for the census applies here, keyed on the derive's own mtime
(the honest observed_at that fedobs already uses) and cross-checked against a fresh census population
when one is supplied. A population delta is reported as a STALENESS finding, not silently absorbed.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

_HERE = Path(__file__).resolve().parent
WORKSPACE = _HERE.parent.parent.parent

# Where comp-aws derive writes, and where fedobs reads it from. Same default, same env override --
# if these ever diverge, the two tools are reading different estates and neither would say so.
DERIVE_DIR = Path(os.environ.get("FEDOBS_LIVE_AWS_DERIVE_DIR",
                                 str(WORKSPACE / ".fedobs_tmp" / "live_aws")))

DEFAULT_DERIVE_TTL_HOURS = 24


def load_iam_derive(derive_dir: Path | None = None):
    """Load comp-aws derive's IAM class. Returns (payload, path, observed_at) or (None, path, None).

    observed_at is the FILE MTIME, which is what fedobs_emit calls the "honest vintage -- when the
    observer actually saw the estate". Using mtime is legitimate HERE and illegitimate for the census:
    the derive artifact has no internal stamp and mtime is the only observation time available, so it
    is a declared best-effort; the census DOES stamp itself at read time, so falling back to mtime
    there would replace a real measurement with a proxy. Different artifacts, different honest answer.
    """
    ddir = derive_dir or DERIVE_DIR
    path = ddir / "comp_aws_derive_iam.json"
    if not path.exists():
        return None, path, None
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None, path, None
    iam = ((doc.get("classes_data") or {}).get("iam")) or None
    if iam is None:
        return None, path, None
    observed = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    iam = dict(iam)
    iam["_account"] = ((doc.get("meta") or {}).get("account"))
    return iam, path, observed


def derive_age_hours(observed_at, now=None) -> float | None:
    if observed_at is None:
        return None
    return ((now or datetime.now(timezone.utc)) - observed_at).total_seconds() / 3600.0


def population_delta(derive_iam: dict, census: dict | None):
    """Cross-check the derive's live population against a freshly-read census population.

    This is the staleness DETECTOR the derive cannot perform on itself. Two independent reads of the
    same estate; a difference means the older one is under-enumerating, and under-enumeration is the
    dangerous direction -- every role the snapshot lacks reads as a role that does not exist.

    Returns None when no census is supplied (the check is UNAVAILABLE, which is reported as such and
    never as agreement -- two sources cannot agree when only one is present).
    """
    if not census:
        return None
    derive_names = {str(n.get("id") or n.get("name")) for n in (derive_iam.get("nodes") or [])}
    census_names = {str(r.get("role_name")) for r in (census.get("roles") or [])}
    return {
        "derive_population": len(derive_names),
        "census_population": len(census_names),
        "in_census_not_in_derive": sorted(census_names - derive_names),
        "in_derive_not_in_census": sorted(derive_names - census_names),
    }


def classify(derive_iam: dict) -> dict:
    """Live-primary partition of the derive's nodes. No re-derivation -- the drift_class is the
    certed reconciler's verdict and is reported, not recomputed."""
    nodes = derive_iam.get("nodes") or []
    out = {"DECLARED": [], "LIVE-no-DECLARED": [], "OTHER": []}
    for n in nodes:
        dc = str(n.get("drift_class") or "OTHER")
        out.setdefault(dc, out["OTHER"] if dc not in out else out[dc])
        (out[dc] if dc in ("DECLARED", "LIVE-no-DECLARED") else out["OTHER"]).append(n)
    return out


def service_linked(node: dict) -> bool:
    """AWS-managed service-linked roles, identified on the STRUCTURED /aws-service-role/ ARN path
    segment -- not a name-prefix heuristic. They are live and undeclared BY DESIGN; counting them as
    ungoverned findings is how a real signal gets buried under expected noise."""
    return "/aws-service-role/" in str(node.get("arn") or "")


# ---------------------------------------------------------------------------
# D1/D5 (Andrew design GO 2026-07-22): COHORT VINTAGE, read from the ROWS.
#
# The graph's write path is a UNION of two cadences:
#   A  ECS derive-runner, cron(0 2 * * ? *)  -- full re-derive, one snapshot_ts for every node
#   B  Lambda incremental-updater, CloudTrail-mutating -> SQS -> ESM (120s debounce) -- changed nodes
#
# So FRESHNESS IS A PROPERTY OF THE ROW, NOT THE TABLE. A node stamped 02:00Z is not stale; it is
# CURRENT, because had it changed, path B would have re-observed it within ~2 minutes. The honest
# claim is "current as of the last full derive, PLUS every CloudTrail-observed mutation since."
#
# The existing provenance header reads `last_write_iso` off the branch-head marker -- the TABLE's
# write time. Measured 2026-07-22: 14,708 full-derive nodes at 02:00:31Z (17.1h) and TWO incremental
# nodes at 14:37Z, and the header reported "graph_nodes: last-write 4.5h ago (< 6h cadence)" -- a PASS
# rendered against a clock the data does not live on. Against the cohort it names: 17.1h > 6h = FAIL.
#
# A LAST-WRITE TIMESTAMP IS A PROPERTY OF THE CONTAINER, NOT THE CONTENTS. One row written now makes a
# corpus of any age report as current -- and it is monotonic the wrong way: a finer-grained incremental
# updater makes the staleness signal WORSE, because smaller writes keep refreshing a clock most of the
# data is not on.
# ---------------------------------------------------------------------------

# TO-CG-D-7 (R7): the graph is SERVED. There is no local database constant here any more; the one
# transport is infra/aws/globgrph/projection_client.py.
GLOBGRPH = WORKSPACE / "infra" / "aws" / "globgrph"


def kuzu_iam_rows(db_path=None):
    """Read IAM_ROLE nodes from the SERVED cloud graph. Returns [] if the service is unavailable.

    Read-only, no AWS call, no local database (TO-CG-D-7 / R7 retired it). Returns [] rather than
    raising so the caller degrades to the derive artifact and SAYS SO, instead of erroring out of a
    plane that has a working fallback -- the degradation is DISCLOSED by the caller, which is why an
    empty list is safe here and a silent local-copy read would not have been.

    `db_path` is accepted for signature compatibility and ignored except to refuse: naming a local
    path asks for a surface that no longer exists."""
    if db_path:
        return []
    try:
        if str(GLOBGRPH) not in sys.path:
            sys.path.insert(0, str(GLOBGRPH))
        import projection_client
    except Exception:   # noqa: BLE001
        return []
    try:
        res = projection_client.connect().execute(
            "MATCH (n:CloudNode) WHERE n.node_type = 'IAM_ROLE' "
            "RETURN n.name, n.arn, n.drift_class, n.source, n.snapshot_ts")
        out = []
        while res.has_next():
            name, arn, dc, src, ts = res.get_next()
            out.append({"id": name, "name": name, "arn": arn,
                        "drift_class": dc, "source": src, "snapshot_ts": ts})
        return out
    except Exception:   # noqa: BLE001
        return []


def cohort_vintage(rows, now=None):
    """Per-SOURCE observation vintage -- the number the header should carry.

    Returns {source: {n, newest_iso, oldest_iso, newest_age_h, oldest_age_h}}. Reporting per cohort
    is the whole fix: a single table-write figure cannot express a corpus written by two producers on
    two cadences, and collapsing them lets the smaller, fresher cohort speak for the larger, older one.
    """
    now = now or datetime.now(timezone.utc)
    by = {}
    for r in rows:
        ts = r.get("snapshot_ts")
        if ts is None:
            by.setdefault(r.get("source") or "UNSTAMPED", {"n": 0, "ts": []})["n"] += 1
            continue
        b = by.setdefault(r.get("source") or "UNSTAMPED", {"n": 0, "ts": []})
        b["n"] += 1
        b["ts"].append(int(ts))
    out = {}
    for src, b in by.items():
        if not b["ts"]:
            out[src] = {"n": b["n"], "newest_iso": None, "oldest_iso": None,
                        "newest_age_h": None, "oldest_age_h": None}
            continue
        newest, oldest = max(b["ts"]), min(b["ts"])
        def _iso(ms):
            return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        def _age(ms):
            return (now - datetime.fromtimestamp(ms / 1000, tz=timezone.utc)).total_seconds() / 3600
        out[src] = {"n": b["n"], "newest_iso": _iso(newest), "oldest_iso": _iso(oldest),
                    "newest_age_h": _age(newest), "oldest_age_h": _age(oldest)}
    return out


# Cadence per PRODUCER, not per table -- each cohort is judged against the schedule that writes it.
# full-derive: cron(0 2 * * ? *) => a 24h SLA. incremental: event-driven, so it HAS NO CADENCE and
# must never be judged against one; its health is a property of the PIPE (invocations / DLQ), which
# node rows cannot express. See D3.
COHORT_CADENCE_HOURS = {"full-derive": 24.0}


def cohort_lines(rows, now=None):
    """The D1 header block: per-cohort vintage, each judged against its own producer's cadence."""
    cv = cohort_vintage(rows, now=now)
    if not cv:
        return ["  cohort vintage: UNAVAILABLE (no rows read from the materialized graph)"]
    lines = ["  cohort vintage (observation time carried by the ROWS, not the table write):"]
    for src in sorted(cv, key=lambda s: -cv[s]["n"]):
        c = cv[src]
        if c["newest_iso"] is None:
            lines.append(f"    {src}: {c['n']} node(s), NO snapshot_ts -- vintage UNMEASURED")
            continue
        cad = COHORT_CADENCE_HOURS.get(src)
        if cad is None:
            verdict = "no cadence -- event-driven; health is a PIPE property, see `comp-iam live --pipe`"
        else:
            verdict = (f"[STALE > {cad:.0f}h cadence]" if c["oldest_age_h"] > cad
                       else f"(< {cad:.0f}h cadence)")
        span = ("" if c["newest_iso"] == c["oldest_iso"]
                else f", oldest {c['oldest_age_h']:.1f}h")
        lines.append(f"    {src}: {c['n']} node(s), newest {c['newest_iso']} "
                     f"(age {c['newest_age_h']:.1f}h{span}) {verdict}")
    full = cv.get("full-derive")
    if full and full["newest_iso"]:
        lines.append(f"  => EFFECTIVE: current as of {full['newest_iso']} (last full derive) PLUS every "
                     f"CloudTrail-observed mutation since -- IF the incremental pipe is alive.")
    return lines


# ---------------------------------------------------------------------------
# D3: path-B liveness read FROM THE PIPE, never from node counts.
#
# The incremental cohort's SIZE cannot distinguish a quiescent estate from a dead pipe -- and
# measurement 2026-07-22 proved the hypothesis space was itself too small: the pipe is ALIVE
# (2,492 SQS sends, 114 invocations, 0 errors, 0 DLQ, depth 0) and writes almost nothing
# (`BATCH_END processed_arns=0 nodes_written=0`). Neither quiescent nor dead: ALIVE-AND-YIELDING-
# NOTHING, a third state. Node counts express none of the three.
#
# So liveness is asserted on signals that exist even when nothing changed: invocations, errors,
# DLQ depth, and SQS sends. All read-only.
# ---------------------------------------------------------------------------

LAMBDA_NAME = "opal-globgrph-incremental-updater"
QUEUE_NAME = "opal-globgrph-incremental-events"
DLQ_NAME = "opal-globgrph-incremental-events-dlq"


def _aws(args):
    import shutil
    import subprocess
    exe = shutil.which("aws") or shutil.which("aws.cmd")
    if not exe:
        return None
    p = subprocess.run([exe] + args, capture_output=True, text=True)
    return p.stdout.strip() if p.returncode == 0 else None


def pipe_liveness(hours=24):
    """Return the incremental pipe's health from CloudWatch/SQS, or None per-limb when unreadable.

    A limb that cannot be read returns None and is REPORTED as UNREADABLE -- never as 0. A zero and
    an unmeasured limb are the same shape downstream and only one of them means 'nothing happened'."""
    import datetime
    now = datetime.datetime.now(datetime.timezone.utc)
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    start, end = (now - datetime.timedelta(hours=hours)).strftime(fmt), now.strftime(fmt)

    def metric(ns, name, dim_name, dim_val):
        out = _aws(["cloudwatch", "get-metric-statistics", "--namespace", ns, "--metric-name", name,
                    "--dimensions", f"Name={dim_name},Value={dim_val}", "--start-time", start,
                    "--end-time", end, "--period", str(hours * 3600), "--statistics", "Sum",
                    "--query", "Datapoints[0].Sum", "--output", "text"])
        if out is None or out == "":
            return None
        if out == "None":
            return 0.0
        try:
            return float(out)
        except ValueError:
            return None

    def depth(q):
        out = _aws(["sqs", "get-queue-url", "--queue-name", q, "--query", "QueueUrl", "--output", "text"])
        if not out or out == "None":
            return None
        d = _aws(["sqs", "get-queue-attributes", "--queue-url", out, "--attribute-names",
                  "ApproximateNumberOfMessages", "--query",
                  "Attributes.ApproximateNumberOfMessages", "--output", "text"])
        try:
            return int(d)
        except (TypeError, ValueError):
            return None

    return {
        "window_hours": hours,
        "invocations": metric("AWS/Lambda", "Invocations", "FunctionName", LAMBDA_NAME),
        "errors": metric("AWS/Lambda", "Errors", "FunctionName", LAMBDA_NAME),
        "sqs_sent": metric("AWS/SQS", "NumberOfMessagesSent", "QueueName", QUEUE_NAME),
        "queue_depth": depth(QUEUE_NAME),
        "dlq_depth": depth(DLQ_NAME),
    }


def pipe_lines(pl):
    """Render the pipe verdict. UNREADABLE limbs stay UNREADABLE; they never round to healthy."""
    if pl is None:
        return ["  incremental pipe: UNREADABLE (no AWS access) -- liveness UNKNOWN, not OK"]
    def fmt(v):
        return "UNREADABLE" if v is None else (f"{v:.0f}" if isinstance(v, float) else str(v))
    lines = [f"  incremental pipe ({pl['window_hours']}h): invocations={fmt(pl['invocations'])} "
             f"errors={fmt(pl['errors'])} sqs_sent={fmt(pl['sqs_sent'])} "
             f"queue_depth={fmt(pl['queue_depth'])} dlq_depth={fmt(pl['dlq_depth'])}"]
    inv, err, dlq = pl["invocations"], pl["errors"], pl["dlq_depth"]
    if inv is None:
        lines.append("    verdict: UNKNOWN -- the pipe was not measurable; do NOT read this as healthy")
    elif inv == 0:
        lines.append("    verdict: NO INVOCATIONS -- quiescent estate OR dead pipe, INDISTINGUISHABLE "
                     "from this signal alone")
    elif err and err > 0:
        lines.append(f"    verdict: DEGRADED -- {err:.0f} error(s) in window")
    elif dlq:
        lines.append(f"    verdict: DEGRADED -- DLQ depth {dlq} (events arriving and FAILING, which "
                     "looks exactly like quiescence from the node side)")
    else:
        lines.append("    verdict: ALIVE (invoked, no errors, DLQ empty). NOTE: alive does NOT imply "
                     "it is WRITING -- yield is a separate question the node cohort answers.")
    return lines


# ---------------------------------------------------------------------------
# D4: the RECONCILIATION ORACLE -- attribute every gap to the producer that should have caught it.
#
# The graph has two producers with different obligations:
#   A  full derive, 02:00Z  -- must contain everything that existed AT 02:00Z
#   B  incremental, ~2 min  -- must contain everything created SINCE 02:00Z
#
# So a role that is live but absent from the graph is not one finding, it is TWO DIFFERENT findings,
# and CreateDate separates them:
#
#   created AFTER  the last full derive  -> B should have caught it   => INCREMENTAL MISS
#   created BEFORE the last full derive  -> A should have caught it   => FULL-DERIVE MISS
#
# This is the self-check the design called for, and it is computable locally from data both sides
# already have. Without it "12 roles missing" is a number with no owner; with it, each row names the
# producer whose obligation was not met -- or names neither, which is itself informative (a role
# created before the derive AND excluded by both is a SCOPE decision, not a miss).
# ---------------------------------------------------------------------------

def reconcile_oracle(rows, census, now=None):
    """Attribute each live-but-absent-from-graph role to the producer that should have ingested it.

    Returns {full_derive_ts_iso, incremental_miss[], full_derive_miss[], undatable[]} or None when the
    inputs cannot support the attribution. Returning None rather than an empty result matters: an
    oracle that cannot run must not look like an oracle that ran and found nothing."""
    if not census or not rows:
        return None
    cv = cohort_vintage(rows, now=now)
    fd = cv.get("full-derive") or {}
    fd_iso = fd.get("newest_iso")
    if not fd_iso:
        return None
    fd_dt = datetime.strptime(fd_iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)

    in_graph = {str(r.get("name")) for r in rows}
    inc, full, undatable = [], [], []
    for r in (census.get("roles") or []):
        name = str(r.get("role_name"))
        if name in in_graph:
            continue
        cd = r.get("create_date")
        if not cd:
            undatable.append({"name": name, "why": "census carries no create_date"})
            continue
        try:
            cdt = datetime.strptime(str(cd).replace("+00:00", "Z"), "%Y-%m-%dT%H:%M:%SZ")
            cdt = cdt.replace(tzinfo=timezone.utc)
        except ValueError:
            undatable.append({"name": name, "why": f"unparseable create_date {cd!r}"})
            continue
        rec = {"name": name, "created": cdt.strftime("%Y-%m-%dT%H:%M:%SZ"),
               "service_linked": service_linked(r if r.get("arn") else {"arn": r.get("arn")})
               or "/aws-service-role/" in str(r.get("arn") or "")}
        (inc if cdt > fd_dt else full).append(rec)

    # A gap that pre-dates the derive AND is an AWS service-linked role is not a MISS, it is a SCOPE
    # EXCLUSION: AWS creates and owns those, they are consistently absent across every run, and they
    # are not governable by our IaC. Reporting 12 expected exclusions as misses every run is how a
    # real signal gets buried -- the same crying-wolf failure the service-linked split fixed upstream.
    # The distinction is evidence-based, not cosmetic: MISS means an obligation was not met;
    # EXCLUSION means no obligation existed.
    scope_excluded = [r for r in full if r["service_linked"]]
    genuine_full_miss = [r for r in full if not r["service_linked"]]
    return {"full_derive_ts_iso": fd_iso, "incremental_miss": inc,
            "full_derive_miss": genuine_full_miss, "scope_excluded": scope_excluded,
            "undatable": undatable}


def oracle_lines(o):
    if o is None:
        return ["  reconciliation oracle: UNAVAILABLE (needs a census WITH create_date + a "
                "full-derive cohort) -- NOT a clean result"]
    lines = [f"  reconciliation oracle (vs last full derive {o['full_derive_ts_iso']}):"]
    inc, full, und = o["incremental_miss"], o["full_derive_miss"], o["undatable"]
    exc = o.get("scope_excluded") or []
    if not inc and not full and not und:
        detail = (f" ({len(exc)} AWS service-linked role(s) excluded by scope -- not a miss; "
                  f"AWS owns them and they are not IaC-governable)" if exc else "")
        lines.append(f"    NO ATTRIBUTABLE GAPS -- both producers met their obligation{detail}")
        return lines
    if inc:
        lines.append(f"    INCREMENTAL MISS ({len(inc)}) -- created AFTER the last full derive, so "
                     f"the ~2-min CloudTrail path should have ingested them and did not:")
        for r in inc[:10]:
            lines.append(f"       !! {r['name']}  created {r['created']}")
        if len(inc) > 10:
            lines.append(f"       ... and {len(inc) - 10} more")
    if full:
        lines.append(f"    FULL-DERIVE MISS ({len(full)}) -- existed BEFORE the last full derive, so "
                     f"the 02:00Z re-derive should have contained them and did not:")
        for r in full[:10]:
            lines.append(f"       !! {r['name']}  created {r['created']}")
        if len(full) > 10:
            lines.append(f"       ... and {len(full) - 10} more")
    if exc:
        lines.append(f"    scope-excluded ({len(exc)}): AWS service-linked, absent by design, "
                     f"NOT counted as a miss")
    if und:
        lines.append(f"    UNATTRIBUTABLE ({len(und)}) -- gap is real but the producer cannot be "
                     f"named: {und[0]['why']}")
    return lines
