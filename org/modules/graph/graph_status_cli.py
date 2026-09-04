#!/usr/bin/env python3
"""
comp-graph -- freshness/status view across every dependency graph (NFRA_GRAPHS D3).

`comp-graph status` answers, in one place, "which graphs exist, how fresh is each,
and when was it last derived" -- the missing operational complement to the
query-vs-rebuild doctrine catalogued in org/modules/graph/graph-call-manifest.yaml.
It reports both the local trace-layer caches (.comp-graph/) and the cloud/
cross-layer artifacts (infra/aws/globgrph/), each with its freshness verdict, age,
TTL, canonical query tool, and rebuild command.

`comp-graph clear [name|all]` drops a local trace-layer cache so the next call
rebuilds it (gitignored cache only -- never touches the cloud artifacts).

Freshness contract -- THREE states (CTO GO 20260709T201214Z):
  - (default) serve the cache iff that tool's freshness PREDICATE says fresh.
  - --check   REPORT staleness, never rebuild.  0 = fresh | 2 = stale | 1 = tool error.
  - --force   always re-derive.
  - --fresh   DEPRECATED no-op alias of default (warns; removed next cycle).

There is no single universal predicate, and this tool must not invent one: the trace graph binds
per-node CONTENT-SHA drift (age is never evaluated on the default path), while graph_cache binds a
stat-only fingerprint AND a TTL. `status` prints each tool's ACTUAL predicate, and takes the trace
verdict by CALLING the enforcer (`cli.trace_freshness`) rather than re-modelling it.

Usage:
    comp-graph status                # freshness table for every graph
    comp-graph status --json         # machine-readable
    comp-graph clear platinum        # drop the comp-platinum caches
    comp-graph clear trace           # drop the trace graph cache
    comp-graph clear all             # drop all local trace-layer caches
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent

sys.path.insert(0, str(_WORKSPACE))

from org.modules.graph import graph_cache as gc  # noqa: E402

_CACHE_DIR = _WORKSPACE / ".comp-graph"

# CG-s-7 (R4): the cloud group used to stat two LOCAL files under infra/aws/globgrph/ that are the
# wrong artifacts (brief F6) -- neither is the served projection. It now reads the projection
# pointer's own manifest (PROJECTION_CONTRACT.md, the CG-s-3 contract) via the straddle rule below.
_DEFAULT_POINTER_URI = "s3://opal-313476888478-globgrph/projection/current.json"
_NIGHTLY_BOUNDARY_HOUR = 2  # cron(0 2 * * ? *): infra/aws/terraform/globgrph/item2a.tf:439
_NIGHTLY_WINDOW_HOURS = 6
_MAX_WINDOW_GETS = 12
_MAX_FALLBACK_GETS = 12

# `_TRACE_TTL = 300` USED TO LIVE HERE. It was a hand-copied second expression modelling a predicate
# the enforcing code does not use: `cli.py::_get_graph`'s default path binds per-node content-SHA
# drift and NEVER evaluates age (the TTL `elif` hangs off `if check_freshness:`). Exercised at
# (age=4000s, drift=0) the old verdict said "STALE (next call rebuilds)" while `_get_graph` SERVED
# the cache -- wrong in both directions. We now CALL the enforcer (`cli.trace_freshness`) and print
# what it returns. MSTR 20260709T200348Z, ratified: a control's reported value and its enforcing
# value must be the SAME EXPRESSION, not two expressions that agree today.
# CTO GO 20260709T201214Z; 0.7.0_AE_CloudOps (tool owner) co-signed 20260709T205010Z.

# The freshness contract's POPULATION, derived from each tool's actual capability -- never inherited
# from the manifest's `rebuild-when-query` token list, which under-collected (it named one launcher
# for a cli.py that backs five) and mis-collected (`comp-aws derive` has no cached read at all).
# Silence about the classes recreates the false-uniformity claim one category over, so status names
# all three (CTO ruling; 0.7.0's framing).
_CONTRACT_TOOLS = ["comp-trace", "comp-blast", "comp-diff", "comp-xref", "comp-platinum",
                   "comp-system"]
_REBUILD_VERB = ["comp-build"]          # default IS the rebuild; --check probes. No warm cached read.
_PURE_PRODUCERS = ["comp-aws derive", "comp-stitch-refresh"]
_QUERY_ONLY = ["comp-kuzu"]


def _fmt_age(seconds) -> str:
    """Human-readable age (e.g. '42s', '7m', '3h', '5d')."""
    if seconds is None:
        return "-"
    s = int(seconds)
    if s < 90:
        return f"{s}s"
    if s < 5400:
        return f"{s // 60}m"
    if s < 172800:
        return f"{s // 3600}h"
    return f"{s // 86400}d"


def _json_built_at(path: Path):
    """Cheaply read a leading `"built_at": <num>` from a graph JSON head."""
    try:
        head = path.read_bytes()[:512].decode("utf-8", errors="replace")
        m = re.search(r'"built_at"\s*:\s*([0-9.]+)', head)
        if m:
            return float(m.group(1))
    except Exception:
        pass
    return None


def _now() -> float:
    return time.time()


def _trace_cli():
    """Import the ENFORCER. Lazy: cli.py pulls the trace-graph machinery, and `comp-graph clear`
    must not pay for it."""
    from org.modules.graph import cli as _cli
    return _cli


def _trace_freshness():
    """Call the enforcing predicate. Fail-closed: if we cannot ASK the enforcer, we do not invent a
    verdict -- an unevaluable status is UNVERIFIABLE, never FRESH."""
    try:
        return _trace_cli().trace_freshness()
    except Exception as e:  # noqa: BLE001
        return "UNVERIFIABLE", f"cannot reach the enforcer ({type(e).__name__}: {e})", 0, []


def _trace_predicate() -> str:
    try:
        return _trace_cli().TRACE_PREDICATE
    except Exception:  # noqa: BLE001
        return "UNKNOWN (enforcer unreachable)"


#: comp-platinum's predicate, named from graph_cache's own contract rather than restated here.
_GC_PREDICATE = f"stat-only (max-mtime, file-count) fingerprint AND age < {gc.DEFAULT_TTL}s TTL"


def _ttl_verdict(exists: bool, age, ttl) -> str:
    if not exists:
        return "MISSING"
    if age is None:
        return "PRESENT"
    return "FRESH" if age < ttl else "STALE"


def _present_verdict(exists: bool) -> str:
    return "PRESENT" if exists else "MISSING"


# --- Projection pointer reader (CG-s-7 R4 repoint) --------------------------------------------
# begin at projection/current.json, apply the reader straddle rule (PROJECTION_CONTRACT.md s.6),
# and report the manifest's own field set. A PULL read only: no write, no rebuild, no engine call.

def _pointer_base():
    """Resolve COMP_GRAPH_POINTER_URI (default: the live pointer) into a (scheme, location) base
    plus the pointer's own key/name. `s3://bucket/key` reads AWS; anything else (a bare path or
    `file://`) is a local fixture -- the plant's own directory stands in for the bucket root, and
    a `projection/` prefix inside a key is stripped when resolved against it."""
    uri = os.environ.get("COMP_GRAPH_POINTER_URI", _DEFAULT_POINTER_URI)
    if uri.startswith("s3://"):
        rest = uri[len("s3://"):]
        bucket, _, key = rest.partition("/")
        return ("s3", bucket), key, uri
    local_uri = uri[len("file://"):] if uri.startswith("file://") else uri
    p = Path(local_uri)
    if not p.is_absolute():
        p = _WORKSPACE / p
    return ("file", str(p.parent)), p.name, uri


def _get_s3_object(bucket, key):
    """GET one S3 object's bytes. boto3 if importable, else `.tools/aws s3 cp ... -` via
    subprocess (the method actually used is returned so callers can state which)."""
    boto3_err = None
    try:
        import boto3
        client = boto3.client("s3")
        try:
            body = client.get_object(Bucket=bucket, Key=key)["Body"].read()
            return body, "boto3", None
        except Exception as e:  # noqa: BLE001
            boto3_err = f"{type(e).__name__}: {e}"
    except ImportError:
        boto3_err = "boto3 not importable"
    aws_bin = _WORKSPACE / ".tools" / "aws"
    try:
        proc = subprocess.run(
            ["bash", str(aws_bin), "s3", "cp", f"s3://{bucket}/{key}", "-"],
            capture_output=True, timeout=30,
        )
        if proc.returncode == 0 and proc.stdout:
            return proc.stdout, "aws-cli-subprocess", None
        detail = proc.stderr.decode("utf-8", "replace").strip() or f"rc={proc.returncode}"
        return None, "aws-cli-subprocess", f"{detail} [boto3: {boto3_err}]"
    except Exception as e:  # noqa: BLE001
        return None, "aws-cli-subprocess", f"{type(e).__name__}: {e} [boto3: {boto3_err}]"


def _get_local_object(directory, key):
    rel = key[len("projection/"):] if key.startswith("projection/") else key
    # Windows forbids ':' in a path component; an ISO-8601 vintage carries three. The plant fixture
    # stores vintage directories with ':' -> '_' (reversed on listing in _list_local_vintages); this
    # is a local-fixture-only detour and never touches an S3 key, which allows ':' natively.
    rel = rel.replace(":", "_")
    path = Path(directory) / rel
    try:
        return path.read_bytes(), "local-file", None
    except Exception as e:  # noqa: BLE001
        return None, "local-file", f"{type(e).__name__}: {e}"


def _get_object_bytes(base, key):
    scheme, loc = base
    if scheme == "s3":
        return _get_s3_object(loc, key)
    return _get_local_object(loc, key)


def _list_s3_vintages(bucket):
    boto3_err = None
    try:
        import boto3
        client = boto3.client("s3")
        try:
            resp = client.list_objects_v2(Bucket=bucket, Prefix="projection/", Delimiter="/")
            prefixes = [p["Prefix"] for p in resp.get("CommonPrefixes", [])]
            vintages = sorted(p[len("projection/"):].rstrip("/") for p in prefixes)
            return vintages, None
        except Exception as e:  # noqa: BLE001
            boto3_err = f"{type(e).__name__}: {e}"
    except ImportError:
        boto3_err = "boto3 not importable"
    aws_bin = _WORKSPACE / ".tools" / "aws"
    try:
        proc = subprocess.run(
            ["bash", str(aws_bin), "s3api", "list-objects-v2", "--bucket", bucket,
             "--prefix", "projection/", "--delimiter", "/",
             "--query", "CommonPrefixes[].Prefix", "--output", "json"],
            capture_output=True, timeout=30,
        )
        if proc.returncode == 0:
            data = json.loads(proc.stdout.decode("utf-8") or "[]") or []
            vintages = sorted(p[len("projection/"):].rstrip("/") for p in data)
            return vintages, None
        detail = proc.stderr.decode("utf-8", "replace").strip() or f"rc={proc.returncode}"
        return [], f"{detail} [boto3: {boto3_err}]"
    except Exception as e:  # noqa: BLE001
        return [], f"{type(e).__name__}: {e} [boto3: {boto3_err}]"


def _list_local_vintages(directory):
    try:
        d = Path(directory)
        # Reverse the ':' -> '_' fixture escape (see _get_local_object) to report the true vintage.
        return sorted(x.name.replace("_", ":") for x in d.iterdir() if x.is_dir()), None
    except Exception as e:  # noqa: BLE001
        return [], f"{type(e).__name__}: {e}"


def _list_projection_vintages(base):
    scheme, loc = base
    if scheme == "s3":
        return _list_s3_vintages(loc)
    return _list_local_vintages(loc)


def _read_pointer(base, key):
    raw, method, err = _get_object_bytes(base, key)
    if raw is None:
        return None, method, err
    try:
        return json.loads(raw.decode("utf-8")), method, None
    except Exception as e:  # noqa: BLE001
        return None, method, f"pointer JSON parse failed: {type(e).__name__}: {e}"


def _read_manifest_verified(base, manifest_key, expected_sha256):
    if not manifest_key:
        return None, "n/a", "pointer carries no manifest_key"
    raw, method, err = _get_object_bytes(base, manifest_key)
    if raw is None:
        return None, method, err
    actual = hashlib.sha256(raw).hexdigest()
    if expected_sha256 and actual != expected_sha256:
        return None, method, (
            f"manifest_sha256 mismatch (pointer: {expected_sha256}, object: {actual})"
        )
    try:
        return json.loads(raw.decode("utf-8")), method, None
    except Exception as e:  # noqa: BLE001
        return None, method, f"manifest JSON parse failed: {type(e).__name__}: {e}"


def _straddle_read(base, pointer_key, max_repeats=4):
    """PROJECTION_CONTRACT.md s.6: GET P1, GET+verify its manifest, GET P2; if P1 != P2 (vintage +
    manifest SHA-256) discard and repeat from P2. Never combines a manifest/artifact from two
    vintages."""
    p1, method, err = _read_pointer(base, pointer_key)
    if p1 is None:
        return None, None, method, err
    for _ in range(max_repeats):
        manifest, mmethod, merr = _read_manifest_verified(
            base, p1.get("manifest_key") or "", p1.get("manifest_sha256")
        )
        if manifest is None:
            return None, None, mmethod, merr
        p2, method2, err2 = _read_pointer(base, pointer_key)
        if p2 is None:
            return None, None, method2, err2
        if (p2.get("vintage") == p1.get("vintage")
                and p2.get("manifest_sha256") == p1.get("manifest_sha256")):
            return p1, manifest, method2, None
        p1 = p2
    return None, None, method, "straddle read did not converge after %d repeats" % max_repeats


def _parse_iso_dt(v):
    try:
        return datetime.fromisoformat(v)
    except Exception:  # noqa: BLE001
        return None


def _last_full_before_boundary(base, now):
    """'Last night' is a DEFINITION, not a feeling: the most recent 02:00Z boundary before now.
    The night RAN if a producer.mode == 'full' manifest with writer_id == 'derive_runner' exists
    whose vintage falls inside [boundary, boundary + 6h) -- bounded to at most 12 manifest GETs.
    A night that did NOT run reports the newest full manifest's built_at before the boundary
    (also bounded), never a default YES."""
    boundary = now.replace(hour=_NIGHTLY_BOUNDARY_HOUR, minute=0, second=0, microsecond=0)
    if now < boundary:
        boundary -= timedelta(days=1)
    window_end = boundary + timedelta(hours=_NIGHTLY_WINDOW_HOURS)

    vintages, list_err = _list_projection_vintages(base)
    if list_err and not vintages:
        return {"ran": None, "boundary": boundary.isoformat(), "error": list_err,
                "checked": 0, "built_at": None, "vintage": None}

    parsed = [(dt, v) for v, dt in ((v, _parse_iso_dt(v)) for v in vintages) if dt is not None]
    parsed.sort()
    in_window = [(dt, v) for dt, v in parsed if boundary <= dt < window_end]
    before_boundary = sorted(((dt, v) for dt, v in parsed if dt < boundary), reverse=True)

    checked = 0
    for _dt, v in in_window:
        if checked >= _MAX_WINDOW_GETS:
            break
        m, _method, _err = _get_object_bytes(base, f"projection/{v}/_build_manifest.json")
        checked += 1
        if m is None:
            continue
        try:
            manifest = json.loads(m.decode("utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if (manifest.get("producer") or {}).get("mode") == "full" and manifest.get("writer_id") == "derive_runner":
            return {"ran": True, "boundary": boundary.isoformat(), "built_at": manifest.get("built_at"),
                    "vintage": v, "checked": checked, "error": None}

    for _dt, v in before_boundary:
        if checked >= _MAX_WINDOW_GETS + _MAX_FALLBACK_GETS:
            break
        m, _method, _err = _get_object_bytes(base, f"projection/{v}/_build_manifest.json")
        checked += 1
        if m is None:
            continue
        try:
            manifest = json.loads(m.decode("utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if (manifest.get("producer") or {}).get("mode") == "full":
            return {"ran": False, "boundary": boundary.isoformat(), "built_at": manifest.get("built_at"),
                    "vintage": v, "checked": checked, "error": None}

    return {"ran": False, "boundary": boundary.isoformat(), "built_at": None, "vintage": None,
            "checked": checked, "error": None}


def _band_status(artifact):
    band = (artifact or {}).get("expected_publish_set_size_band_bytes")
    total = (artifact or {}).get("total_size_bytes")
    if not band or total is None:
        return "NO-BAND"
    lo, hi = band.get("minimum"), band.get("maximum")
    if lo is None or hi is None:
        return "NO-BAND"
    return "IN-BAND" if lo <= total <= hi else "OUT-OF-BAND"


def _projection_rows(now):
    base, pointer_key, uri = _pointer_base()
    p1, manifest, method, err = _straddle_read(base, pointer_key)

    if p1 is None or manifest is None:
        reason = err or "unknown error"
        current = {
            "group": "cloud", "name": "projection.current",
            "desc": "cloud Kuzu projection (projection/current.json, straddle-verified)",
            "path": uri,
            "exists": False, "built_at": None, "age": None,
            "ttl": None, "verdict": "UNVERIFIABLE",
            "detail": f"cannot reach the pointer/manifest ({reason})",
            "query": "comp-kuzu", "rebuild": "none -- the estate refreshes itself (FWD-2)",
            "read_method": method,
            "vintage": None, "age_line": None, "writer_id": None, "producer_mode": None,
            "producer_source_commit": None, "nessie_commit_hash": None,
            "nodes_snapshot_id": None, "edges_snapshot_id": None, "node_count": None,
            "edge_count": None, "edges_skipped_missing_endpoint": None,
            "artifact_bytes": None, "band_status": "NO-BAND",
        }
        last_night = {
            "group": "cloud", "name": "projection.last_night",
            "desc": f"REFRESHED LAST NIGHT: UNVERIFIABLE ({reason})",
            "path": uri,
            "exists": False, "built_at": None, "age": None,
            "ttl": None, "verdict": "UNVERIFIABLE",
            "detail": f"pointer/manifest unreachable ({reason})",
            "query": "comp-kuzu", "rebuild": "none -- the estate refreshes itself (FWD-2)",
            "refreshed_last_night": None, "vintage": None,
        }
        return current, last_night

    artifact = manifest.get("artifact") or {}
    producer = manifest.get("producer") or {}
    band_status = _band_status(artifact)
    built_at_iso = manifest.get("built_at")
    built_dt = _parse_iso_dt(built_at_iso) if built_at_iso else None
    age = (now - built_dt).total_seconds() if built_dt is not None else None

    current = {
        "group": "cloud", "name": "projection.current",
        "desc": "cloud Kuzu projection (projection/current.json, straddle-verified)",
        "path": uri,
        "exists": True, "built_at": built_at_iso, "age": age,
        "ttl": None, "verdict": "PRESENT",
        "query": "comp-kuzu", "rebuild": "none -- the estate refreshes itself (FWD-2)",
        "read_method": method,
        "vintage": manifest.get("vintage"),
        "age_line": manifest.get("age_line"),
        "writer_id": manifest.get("writer_id"),
        "producer_mode": producer.get("mode"),
        "producer_source_commit": producer.get("source_commit"),
        "nessie_commit_hash": manifest.get("nessie_commit_hash"),
        "nodes_snapshot_id": manifest.get("nodes_snapshot_id"),
        "edges_snapshot_id": manifest.get("edges_snapshot_id"),
        "node_count": manifest.get("node_count"),
        "edge_count": manifest.get("edge_count"),
        "edges_skipped_missing_endpoint": manifest.get("edges_skipped_missing_endpoint"),
        "artifact_bytes": artifact.get("total_size_bytes"),
        "band_status": band_status,
    }
    current["extra_fields"] = [
        ("vintage", current["vintage"]),
        ("age_line", current["age_line"]),
        ("built_at", current["built_at"]),
        ("nessie_commit_hash", current["nessie_commit_hash"]),
        ("nodes_snapshot_id", current["nodes_snapshot_id"]),
        ("edges_snapshot_id", current["edges_snapshot_id"]),
        ("writer_id", current["writer_id"]),
        ("producer.mode", current["producer_mode"]),
        ("producer.source_commit", current["producer_source_commit"]),
        ("node_count", current["node_count"]),
        ("edge_count", current["edge_count"]),
        ("edges_skipped_missing_endpoint", current["edges_skipped_missing_endpoint"]),
        ("artifact_bytes", current["artifact_bytes"]),
        ("band_status", current["band_status"]),
        ("read_method", current["read_method"]),
    ]

    result = _last_full_before_boundary(base, now)
    if result["ran"] is True:
        desc = f"REFRESHED LAST NIGHT: YES at {result['built_at']}"
        verdict = "YES"
    elif result["ran"] is False:
        last_full = result.get("built_at") or "none found"
        desc = f"REFRESHED LAST NIGHT: NO (last full: {last_full})"
        verdict = "NO"
    else:
        desc = f"REFRESHED LAST NIGHT: UNVERIFIABLE ({result.get('error')})"
        verdict = "UNVERIFIABLE"

    last_night = {
        "group": "cloud", "name": "projection.last_night",
        "desc": desc,
        "path": uri,
        "exists": result["ran"] is not None, "built_at": result.get("built_at"), "age": None,
        "ttl": None, "verdict": verdict,
        "detail": f"boundary {result['boundary']} (+{_NIGHTLY_WINDOW_HOURS}h window); checked {result['checked']} manifest(s)",
        "query": "comp-kuzu", "rebuild": "none -- the estate refreshes itself (FWD-2)",
        "refreshed_last_night": result["ran"],
        "vintage": result.get("vintage"),
        "extra_fields": [
            ("boundary", result["boundary"]),
            ("checked_manifests", result["checked"]),
            ("vintage", result.get("vintage")),
        ],
    }
    return current, last_night


def _collect():
    """Return the ordered list of graph status records."""
    records = []
    now = _now()

    # --- Local trace layer (.comp-graph/) -----------------------------------
    # Trace graph (comp-trace / comp-blast / comp-diff / comp-xref).
    # VERDICT COMES FROM THE ENFORCER, not from a TTL we keep a copy of. See the _TRACE_TTL note.
    gpath = _CACHE_DIR / "graph.json"
    ba = _json_built_at(gpath) if gpath.exists() else None
    age = (now - ba) if ba else None
    verdict, detail, _n, _drift = _trace_freshness()
    records.append({
        "group": "local", "name": "graph",
        "desc": "trace graph (comp-trace/comp-blast/comp-diff/comp-xref)",
        "path": str(gpath.relative_to(_WORKSPACE)),
        "exists": gpath.exists(), "built_at": ba, "age": age,
        "ttl": None, "verdict": verdict, "detail": detail,
        "predicate": _trace_predicate(),
        "query": "comp-trace / comp-blast", "rebuild": "comp-build",
    })

    # xref baseline (snapshot; no TTL).
    bpath = _CACHE_DIR / "baseline.json"
    bba = _json_built_at(bpath) if bpath.exists() else None
    records.append({
        "group": "local", "name": "baseline",
        "desc": "xref baseline snapshot (comp-xref)",
        "path": str(bpath.relative_to(_WORKSPACE)),
        "exists": bpath.exists(), "built_at": bba,
        "age": (now - bba) if bba else None,
        "ttl": None, "verdict": _present_verdict(bpath.exists()),
        "query": "comp-xref", "rebuild": "comp-xref --save",
    })

    # comp-platinum caches (NFRA_GRAPHS D2) -- discover all platinum.*.cache.
    plat = sorted(_CACHE_DIR.glob("platinum.*.cache")) if _CACHE_DIR.exists() else []
    plat_descs = {
        "platinum.routing": "comp-platinum routing table",
        "platinum.dataflows": "comp-platinum component dataflows",
    }
    for cf in plat:
        name = cf.name[:-len(".cache")]  # strip suffix
        if name.startswith("platinum.dag."):
            firm = name[len("platinum.dag."):]
            desc = f"comp-platinum gold DAG [firm={firm}]"
        else:
            desc = plat_descs.get(name, f"comp-platinum cache ({name})")
        meta = gc.cache_meta(name)
        age = meta.get("age")
        records.append({
            "group": "local", "name": name, "desc": desc,
            "path": str(cf.relative_to(_WORKSPACE)),
            "exists": True, "built_at": meta.get("built_at"), "age": age,
            "ttl": gc.DEFAULT_TTL,
            "verdict": _ttl_verdict(True, age, gc.DEFAULT_TTL),
            "predicate": _GC_PREDICATE,
            "query": "comp-platinum", "rebuild": "comp-platinum ... --force",
        })
    if not plat:
        records.append({
            "group": "local", "name": "platinum.*",
            "desc": "comp-platinum caches (per-firm, keyed by --firm)",
            "path": ".comp-graph/platinum.*.cache",
            "exists": False, "built_at": None, "age": None,
            "ttl": gc.DEFAULT_TTL, "verdict": "MISSING",
            "query": "comp-platinum", "rebuild": "comp-platinum page <C> --firm <F>",
        })

    # --- Cloud / cross-layer (projection pointer) ----------------------------
    # CG-s-7 R4: begin at projection/current.json, apply the reader straddle rule, and report the
    # manifest's own field set (PROJECTION_CONTRACT.md s.6, s.8). PULL READ ONLY.
    now_dt = datetime.fromtimestamp(now, tz=timezone.utc)
    proj_current, proj_last_night = _projection_rows(now_dt)
    records.append(proj_current)
    records.append(proj_last_night)

    return records


def cmd_status(args):
    records = _collect()

    for r in records:
        r["path"] = r["path"].replace("\\", "/")

    if getattr(args, "json", False):
        print(json.dumps({
            "generated_at": _now(),
            "contract": "org/modules/graph/graph-call-manifest.yaml",
            "graphs": records,
        }, indent=2, default=str))
        return

    print("COMP-GRAPH STATUS  (query-vs-rebuild freshness)")
    print("  contract: org/modules/graph/graph-call-manifest.yaml")
    print()

    groups = [("local", "LOCAL TRACE LAYER (.comp-graph/)"),
              ("cloud", "CLOUD / CROSS-LAYER (projection/current.json, straddle-verified)")]
    for gkey, gtitle in groups:
        rows = [r for r in records if r["group"] == gkey]
        if not rows:
            continue
        print(gtitle)
        for r in rows:
            verdict = r["verdict"]
            age = _fmt_age(r["age"]) if r["exists"] and r["age"] is not None else "-"
            ttl = f"TTL {r['ttl']}s" if r["ttl"] else "no-TTL"
            note = ""
            if verdict == "STALE":
                note = f"  (next call rebuilds: {r['rebuild']})"
            elif verdict == "MISSING":
                note = f"  (build: {r['rebuild']})"
            elif verdict == "UNVERIFIABLE":
                note = "  (could not evaluate -- NOT a pass)"
            print(f"  {r['name']:<20} {verdict:<12} {('built ' + age + ' ago') if r['exists'] and r['age'] is not None else ('present' if r['exists'] else 'absent'):<18} {ttl:<9} {r['desc']}{note}")
            # State the PREDICATE and the DENOMINATOR the verdict came from. A verdict whose basis
            # is invisible is a verdict a reader cannot check -- and this row's old verdict was
            # computed from a TTL its own tool never evaluates.
            if r.get("predicate"):
                print(f"  {'':<20} predicate: {r['predicate']}")
            if r.get("detail"):
                print(f"  {'':<20} evaluated: {r['detail']}")
            for label, value in r.get("extra_fields", []):
                print(f"  {'':<20} {label}: {value}")
        print()

    # The contract states the CONTRACT. It does NOT state a universal ("cached within TTL") that is
    # false for both of its members: the trace graph binds content-SHA drift and never reads age;
    # graph_cache binds a stat-only fingerprint AND a TTL. Each tool's ACTUAL predicate is printed
    # per-row above. CTO 20260709T201214Z.
    print("FRESHNESS CONTRACT (3 states):")
    print("  (default)  serve the cache iff that tool's freshness PREDICATE says fresh")
    print("  --check    REPORT staleness, never rebuild.   0 = fresh | 2 = stale | 1 = tool error")
    print("  --force    always re-derive")
    print("  --fresh    DEPRECATED no-op alias of default (warns; removed next cycle) -- the")
    print("             NFRA_GRAPHUNI P2/D2 head-pin made default honor the fingerprint and")
    print("             collapsed FRESH into DEFAULT. Proven no-op, with a control.")
    print()
    # Naming the classes IS the denominator rule applied to a status surface: a page that lists
    # "rebuild-capable graph tools" while silently omitting the pure producers asserts a universal
    # over a set it never states.
    print("POPULATION (derived from each tool's actual capability, not a token list):")
    print("  contract tools  (warm cached read + rebuild; default/--check/--force):")
    print("     %s" % ", ".join(_CONTRACT_TOOLS))
    print("  rebuild+probe verb (no warm cached read -- its DEFAULT is the rebuild; --check probes):")
    print("     %s" % ", ".join(_REBUILD_VERB))
    print("  pure producers  (always re-derive; no cached query path -- --force/--fresh collapse):")
    print("     %s" % ", ".join(_PURE_PRODUCERS))
    print("  query-only      (no rebuild path of its own; cannot own a --force):")
    print("     %s" % ", ".join(_QUERY_ONLY))


def cmd_clear(args):
    target = args.target
    cleared = []
    if target in ("platinum", "all"):
        for cf in sorted(_CACHE_DIR.glob("platinum.*.cache")):
            cf.unlink()
            cleared.append(cf.name)
    if target in ("trace", "all"):
        gpath = _CACHE_DIR / "graph.json"
        if gpath.exists():
            gpath.unlink()
            cleared.append(gpath.name)
    if target not in ("platinum", "trace", "all"):
        print(f"comp-graph clear: unknown target '{target}' (use: platinum | trace | all)",
              file=sys.stderr)
        sys.exit(2)
    if cleared:
        print(f"Cleared {len(cleared)} cache file(s): {', '.join(cleared)}")
        print("Next call to the affected tool will rebuild + re-cache.")
    else:
        print("Nothing to clear (no matching cache files present).")


def main():
    parser = argparse.ArgumentParser(
        prog="comp-graph",
        description="Freshness/status view across every dependency graph (NFRA_GRAPHS D3).",
    )
    sub = parser.add_subparsers(dest="command")

    p_status = sub.add_parser("status", help="Freshness table for every graph")
    p_status.add_argument("--json", action="store_true", help="Machine-readable output")

    p_clear = sub.add_parser("clear", help="Drop a local trace-layer cache (forces next-call rebuild)")
    p_clear.add_argument("target", choices=["platinum", "trace", "all"],
                         help="Which cache(s) to clear")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(0)

    {"status": cmd_status, "clear": cmd_clear}[args.command](args)


if __name__ == "__main__":
    main()
