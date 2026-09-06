#!/usr/bin/env python3
"""S3 -- the MS WRITE-HEAT INDEX over the MS slice of the canonical globgrph (NFRA_MSGRAPH.S3 /
NFRA_GRAPHFEED TO-5, LD-0299).

REUSE, NOT REBUILD (TO scope #1 + CTO invariant #4): this is a DOMAIN ENGINE over DS's S0 pure
lib -- heat_map.HeatParams/score_item score each MS node's write-recency (last_modified_dt), and
object_locality.aggregate_tree rolls the heat up the MS FOLDER TREE (the containment hierarchy
IS the locality structure: "a cold SUBTREE is a stronger signal than scattered cold items").
Zero changes to the shared engine; parameterization only (DS consult sent 213321Z; building
against OBJECT defaults, corrections fold before close).

THE SIGNAL (locked invariant #1): write-heat = the lastModifiedDateTime TIMESTAMP carried on the
MS nodes by the S2 extract -- NEVER file content, NEVER comms. This module reads the canonical
estate graph (the S2 cert-clean substrate) from the SERVED projection and computes ages; it makes
no MICROSOFT GRAPH call, reads no file body, and takes nothing beyond node metadata already in the
graph. (Its one network call is the opal-globgrph projection gateway, which serves those same
nodes -- the invariant is about the MS side, and it is unchanged.)

THE INDEX (TO scope #3, S4-consumption-grounded): one JSON artifact --
  { generated_at, graph_vintage{...}, params{...}, denominators{...},
    dimensions: { write_heat: { nodes: [ {node_id, path, node_type, age_days, score, band,
                                          cluster, size, file_type, owner_upn} ... ranked ],
                                clusters: { dir -> {n, n_cold, cold_frac, oldest_age_days,
                                                    mean_score, depth} } },
                  read_heat: null } }          <- S5 /insights lands HERE, additive (invariant #3)
S4's findability tools do heat-ranked retrieval: nodes[] is pre-sorted score-desc, clusters
carry the rollups -- a rank/filter read, no recompute, no refactor.

SNAPSHOTS (TO scope #2): every non-dry run writes the index to the LATEST key + appends a dated
snapshot under warehouse/ms_heat/snapshots/. Retention is a NAMED, AUDITABLE sizing call:
~5.5k nodes -> ~1.5MB/snapshot; the store is bounded by an S3 LIFECYCLE rule (60-day expiry on
the snapshots/ prefix -- proposed as an additive aws_s3_bucket_lifecycle_configuration, CTO
apply-gated; declared policy, NO code-side deletes: deleting S3 objects stays a human/TF-declared
verb, never an engine side-effect). Cadence: the engine is CADENCE-AGNOSTIC (whatever invokes it
appends one snapshot); the standing schedule (post-derive nightly vs Andrew's "maybe hourly") is
a sizing RAVC to COO/CTO -- the honest math: the MS lastModified data refreshes NIGHTLY (the S2
extract is derive-folded), so hourly snapshots of a nightly signal capture only deterministic
decay drift (24x rows, zero information); post-derive-nightly matches the data vintage.

VINTAGE DISCIPLINE (NFRA_CLDGRPH R7, TO-CG-D-7): the nodes come from the SERVED cloud graph over
one HTTPS /graph/cypher call -- no local database, no local rebuild, no fallback. The service
installs one generation atomically, so the served pointer IS the pin; the graph vintage
(served vintage + manifest sha + marker committed_at) rides the artifact.

Usage:
  python ms_heat_index.py                 # compute + write local index + S3 latest + snapshot
  python ms_heat_index.py --local-only    # compute + write local index only (no S3)
  python ms_heat_index.py --dry-run       # compute + print summary, write NOTHING
  python ms_heat_index.py --self-test     # pure-logic self-test (no kuzu, no S3)

Author: 0.8.0_AE_CloudComp~Z   TO: NFRA_MSGRAPH.S3 (COO GO 18:4xZ) / NFRA_GRAPHFEED TO-5   2026-07-15
Engine: org/modules/heatmap/heat_map.py + object_locality.py (DS-owned, reused unmodified).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
sys.path.insert(0, _HERE)
from heat_map import HeatParams, score_item  # noqa: E402  (DS S0 pure lib, unmodified)
from object_locality import aggregate_tree  # noqa: E402  (DS O2 rollup, unmodified)

GLOBGRPH_DIR = os.path.join(_WS, "infra", "aws", "globgrph")
LOCAL_INDEX = os.path.join(_HERE, "ms_heat_index.json")
S3_BUCKET = "opal-313476888478-globgrph"
S3_LATEST_KEY = "warehouse/ms_heat/ms_heat_index.json"
S3_SNAPSHOT_PREFIX = "warehouse/ms_heat/snapshots/"

MS_NODE_TYPES = ("MS_FILE", "MS_FOLDER")

# DS-consult defaults (message 213321Z): OBJECT-domain knobs -- SharePoint doc write cadence is
# repo-like; freq_weight stays 0 (ONE lastModified per node; no frequency series until S5).
DEFAULT_PARAMS = HeatParams(half_life_days=30.0, hot_days=7.0, warm_days=30.0, freq_weight=0.0)


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------------------------------------
# Graph read (SERVED cloud graph, read-only, one HTTPS round trip)
# ---------------------------------------------------------------------------------------------
def read_ms_nodes() -> tuple[list, dict]:
    """MS_FILE + MS_FOLDER rows from the SERVED cloud graph (NFRA_CLDGRPH TO-CG-D-7 / R7).
    Returns (rows, graph_vintage). Each row: {node_id, node_type, props(dict)}.

    WHAT MOVED AND WHY THE VINTAGE DISCIPLINE IS UNCHANGED. This used to open the local
    kuzu_nessie_db after calling _canonical.ensure_fresh, which could trigger a local rebuild
    on the caller's machine. Both are retired: the graph is BUILT in the cloud and installed by
    the service at a pointer swapped atomically, so the vintage the caller is handed IS the
    installed generation. There is no state in which this reader gets one generation while a
    fresher one is withheld, which is exactly the condition ensure_fresh existed to remove --
    so the refresh call is not replaced by a poll, it is unnecessary. An UNREACHABLE service
    RAISES (ProjectionClientError) rather than computing heat over a stale local copy: a
    VISIBLE gap, never a silent old answer."""
    sys.path.insert(0, GLOBGRPH_DIR)
    import projection_client  # noqa: E402
    import _provenance  # noqa: E402

    conn = projection_client.connect()
    q = conn.execute(
        "MATCH (n:CloudNode) WHERE n.node_type IN ['MS_FILE','MS_FOLDER'] "
        "RETURN n.node_id, n.node_type, n.props")
    rows = []
    while q.has_next():
        nid, ntype, props = q.get_next()
        try:
            props = json.loads(props) if isinstance(props, str) else (props or {})
        except ValueError:
            props = {"_unparseable_props": True}
        rows.append({"node_id": nid, "node_type": ntype, "props": props})

    # The served pointer IS the pin: vintage + manifest identify the generation these rows came
    # from, and they replace the old db_path_basename (which named a file, not a generation).
    vintage = {
        "source": "served cloud graph (opal-globgrph projection)",
        "served_vintage": conn.vintage,
        "served_manifest": conn.manifest_sha256,
        "served_artifact": conn.artifact_prefix,
        "transport": "HTTPS /graph/cypher -- no local database, no cache, no fallback",
    }
    try:
        marker = _provenance.read_branch_head_marker(S3_BUCKET) or {}
        tm = marker.get("table_metadata") or {}
        vintage.update({
            "marker_committed_at": marker.get("committed_at_iso"),
            "marker_writer": marker.get("writer_id"),
            "graph_nodes_snapshot": (tm.get("graph_nodes") or {}).get("snapshot_id"),
            "graph_nodes_last_write": (tm.get("graph_nodes") or {}).get("last_write_iso"),
        })
    except Exception as e:  # noqa: BLE001 -- vintage read is disclosure, not the computation
        vintage["marker_error"] = f"{type(e).__name__}: {e}"
    return rows, vintage


# ---------------------------------------------------------------------------------------------
# Scoring (pure -- unit-testable without kuzu/S3)
# ---------------------------------------------------------------------------------------------
def build_index(rows: list, params: HeatParams, now: datetime) -> dict:
    """Rows -> the S4-consumable index dict. Pure. Denominators printed-in-artifact: scored vs
    skipped_no_ts vs unparseable are all counted -- a node the signal cannot see is DISCLOSED,
    never silently dropped (LAW: silence is not success)."""
    scores = []
    node_meta = {}
    skipped_no_ts, unparseable = 0, 0
    n_by_type = {t: 0 for t in MS_NODE_TYPES}
    for r in rows:
        p = r["props"]
        n_by_type[r["node_type"]] = n_by_type.get(r["node_type"], 0) + 1
        if p.get("_unparseable_props"):
            unparseable += 1
            continue
        ts = p.get("last_modified_dt")
        path = p.get("path") or r["node_id"]
        if not ts:
            skipped_no_ts += 1
            continue
        try:
            lm = datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
        except ValueError:
            skipped_no_ts += 1
            continue
        age_days = max(0.0, (now - lm).total_seconds() / 86400.0)
        s = score_item(path, age_days, frequency=1, p=params)
        scores.append(s)
        node_meta[path] = {"node_id": r["node_id"], "node_type": r["node_type"],
                           "size": p.get("size"), "file_type": p.get("file_type"),
                           "owner_upn": p.get("owner_upn")}

    clusters = aggregate_tree(scores)
    # DS fix 262cda2e8 (root-locus + disclosed coverage): TreeAgg carries clustered_n/total_n.
    # Print UNCONDITIONALLY (a disclosure that only prints when bad is invisible on every good
    # day -- how the 82 stayed hidden). getattr-guarded for pre-fix lib compat.
    clustered_n = getattr(clusters, "clustered_n", None)
    total_n = getattr(clusters, "total_n", None)
    if clustered_n is not None:
        verdict = "OK" if clustered_n == total_n else "WARN"
        print(f"{verdict}: CLUSTER_COVERAGE clustered_n={clustered_n} total_n={total_n}"
              + ("" if clustered_n == total_n else
                 " -- ROLLUP UNDER-COVERS (the slash-less drop class has returned; ping DS)"))
    else:
        print("WARN: CLUSTER_COVERAGE_UNDISCLOSED (pre-262cda2e8 object_locality in use -- "
              "the rollup denominator is unverifiable; pull the lib fix)")

    def _cluster_of(path: str) -> str:
        parts = path.replace("\\", "/").split("/")[:-1]
        return "/".join(parts) if parts else ""

    nodes = []
    for s in sorted(scores, key=lambda x: x.score, reverse=True):
        m = node_meta.get(s.item_id, {})
        nodes.append({"node_id": m.get("node_id"), "path": s.item_id,
                      "node_type": m.get("node_type"), "age_days": round(s.age_days, 2),
                      "score": round(s.score, 6), "band": s.band,
                      "cluster": _cluster_of(s.item_id), "size": m.get("size"),
                      "file_type": m.get("file_type"), "owner_upn": m.get("owner_upn")})

    bands = {"hot": 0, "warm": 0, "cold": 0}
    for s in scores:
        bands[s.band] += 1

    return {
        "generated_at": _iso(now),
        "params": {"half_life_days": params.half_life_days, "hot_days": params.hot_days,
                   "warm_days": params.warm_days, "freq_weight": params.freq_weight,
                   "signal": "write_heat: props.last_modified_dt (S2 metadata; content/comms NEVER read)"},
        "denominators": {"rows_read": len(rows), **{f"n_{k.lower()}": v for k, v in n_by_type.items()},
                         "scored": len(scores), "skipped_no_last_modified": skipped_no_ts,
                         "unparseable_props": unparseable, "bands": bands,
                         "cluster_coverage": {"clustered_n": clustered_n, "total_n": total_n}},
        "dimensions": {
            "write_heat": {"nodes": nodes, "clusters": clusters},
            # S5 lands /insights read-heat + /permissions access HERE, additively (invariant #3).
            "read_heat": None,
            "access": None,
        },
    }


# ---------------------------------------------------------------------------------------------
# TO-7 P1: the DELTA-SIBLING projection (ms_heat_snap rows, staged for the in-VPC ingest)
# ---------------------------------------------------------------------------------------------
SNAP_PENDING_PREFIX = "warehouse/snap_ingest/pending/ms_heat_snap/"


def sibling_rows(index: dict) -> list:
    """Project the index's write_heat nodes into ms_heat_snap rows (the 4 standard convention
    columns + the payload; snap_store.py's SURFACES registry is the schema of record). Pure."""
    gen = index["generated_at"]
    snapshot_date = gen[:10]
    computed_at = int(datetime.fromisoformat(gen.replace("Z", "+00:00")).timestamp() * 1000)
    marker = (index.get("graph_vintage") or {}).get("marker_committed_at") or ""
    producer_ref = f"ms_heat_index-{gen}"
    out = []
    for n in index["dimensions"]["write_heat"]["nodes"]:
        out.append({"snapshot_date": snapshot_date, "computed_at": computed_at,
                    "producer_ref": producer_ref, "marker_head": str(marker),
                    "node_id": n.get("node_id"), "path": n.get("path"),
                    "node_type": n.get("node_type"), "age_days": n.get("age_days"),
                    "score": n.get("score"), "band": n.get("band"),
                    "cluster": n.get("cluster"), "size": n.get("size"),
                    "file_type": n.get("file_type"), "owner_upn": n.get("owner_upn")})
    return out


def stage_sibling(index: dict) -> None:
    """STAGE-THEN-INGEST (TO-7 rider R2): the dev box cannot reach Nessie, so the sibling batch
    stages as JSONL under warehouse/snap_ingest/pending/ms_heat_snap/; the in-VPC snap_store
    --ingest-pending leg appends it + writes the R1 twin heartbeat. Best-effort: a staging
    failure never fails the index write (the twin ages toward alarm -- the designed catch)."""
    rows = sibling_rows(index)
    key = f"{SNAP_PENDING_PREFIX}{index['generated_at'].replace(':', '').replace('-', '')}.jsonl"
    try:
        import boto3
        body = "".join(json.dumps(r, default=str) + "\n" for r in rows).encode()
        boto3.client("s3", region_name="us-east-1").put_object(
            Bucket=S3_BUCKET, Key=key, Body=body, ContentType="application/json")
        print(f"OK: SIBLING_STAGED s3://{S3_BUCKET}/{key} rows={len(rows)} "
              "(in-VPC snap_store --ingest-pending appends it; twin heartbeat on land)")
    except Exception as e:  # noqa: BLE001
        print(f"WARN: SIBLING_STAGE_FAIL err={type(e).__name__}: {e} -- index unaffected; "
              "the ms_heat_snap twin will age toward alarm until a batch lands")


# ---------------------------------------------------------------------------------------------
# Persistence (latest + dated snapshot; retention = declared S3 lifecycle, never a code delete)
# ---------------------------------------------------------------------------------------------
def persist(index: dict, local_only: bool) -> None:
    with open(LOCAL_INDEX, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=1, default=str)
    print(f"OK: LOCAL_INDEX_WRITTEN {os.path.relpath(LOCAL_INDEX, _WS)} "
          f"nodes={len(index['dimensions']['write_heat']['nodes'])}")
    if local_only:
        print("INFO: S3_SKIPPED (--local-only)")
        return
    try:
        import boto3
        s3 = boto3.client("s3", region_name="us-east-1")
        body = json.dumps(index, default=str).encode()
        s3.put_object(Bucket=S3_BUCKET, Key=S3_LATEST_KEY, Body=body,
                      ContentType="application/json")
        snap_key = f"{S3_SNAPSHOT_PREFIX}{index['generated_at'].replace(':', '').replace('-', '')}.json"
        s3.put_object(Bucket=S3_BUCKET, Key=snap_key, Body=body, ContentType="application/json")
        print(f"OK: S3_WRITTEN latest=s3://{S3_BUCKET}/{S3_LATEST_KEY} snapshot={snap_key} "
              f"({len(body)} bytes; retention = declared lifecycle on {S3_SNAPSHOT_PREFIX}, "
              "no code-side delete)")
    except Exception as e:  # noqa: BLE001 -- local index landed; S3 mirror is disclosed-degraded
        print(f"WARN: S3_WRITE_FAIL err={type(e).__name__}: {e} (local index landed)")


# ---------------------------------------------------------------------------------------------
# Self-test (pure logic -- no kuzu, no S3)
# ---------------------------------------------------------------------------------------------
def _self_test() -> bool:
    results = []

    def check(name, cond, detail=""):
        results.append(bool(cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  -> {detail}" if detail and not cond else ""))

    print("=== ms_heat_index self-test (pure: scoring / clusters / denominators / S5-shape) ===")
    now = datetime(2026, 7, 15, 21, 0, 0, tzinfo=timezone.utc)

    def row(nid, ntype, path, ts, **extra):
        p = {"path": path, "last_modified_dt": ts}
        p.update(extra)
        return {"node_id": nid, "node_type": ntype, "props": p}

    rows = [
        row("f1", "MS_FILE", "A/B/hot.docx", "2026-07-14T21:00:00Z", size=10, owner_upn="x@o.com"),
        row("f2", "MS_FILE", "A/B/warm.xlsx", "2026-06-30T21:00:00Z"),
        row("f3", "MS_FILE", "A/C/cold1.pdf", "2025-07-15T21:00:00Z"),
        row("f4", "MS_FILE", "A/C/cold2.pdf", "2025-06-15T21:00:00Z"),
        {"node_id": "f5", "node_type": "MS_FILE", "props": {"path": "A/nots.txt"}},        # no ts
        {"node_id": "f6", "node_type": "MS_FOLDER", "props": {"_unparseable_props": True}},  # bad props
    ]
    idx = build_index(rows, DEFAULT_PARAMS, now)
    d = idx["denominators"]

    check("1  denominators: read=6 scored=4 skipped_no_ts=1 unparseable=1 (nothing silent)",
          d["rows_read"] == 6 and d["scored"] == 4
          and d["skipped_no_last_modified"] == 1 and d["unparseable_props"] == 1, str(d))

    nodes = idx["dimensions"]["write_heat"]["nodes"]
    check("2  bands: 1 hot / 1 warm / 2 cold at the OBJECT thresholds",
          d["bands"] == {"hot": 1, "warm": 1, "cold": 2}, str(d["bands"]))

    check("3  nodes ranked score-desc (heat-ranked retrieval = a plain read for S4)",
          [n["path"] for n in nodes][:2] == ["A/B/hot.docx", "A/B/warm.xlsx"]
          and nodes[0]["score"] >= nodes[-1]["score"])

    cl = idx["dimensions"]["write_heat"]["clusters"]
    check("4  cluster rollup: A/C is a maximal-cold subtree (n=2, cold_frac=1.0) via DS's aggregate_tree",
          cl.get("A/C", {}).get("n") == 2 and cl.get("A/C", {}).get("cold_frac") == 1.0, str(cl.get("A/C")))
    check("5  cluster rollup: A sees the whole subtree (n=4, cold_frac=0.5)",
          cl.get("A", {}).get("n") == 4 and abs(cl.get("A", {}).get("cold_frac", 0) - 0.5) < 1e-9)

    check("6  S5 interface-ready: read_heat + access present-and-null (additive later, no refactor)",
          "read_heat" in idx["dimensions"] and idx["dimensions"]["read_heat"] is None
          and "access" in idx["dimensions"] and idx["dimensions"]["access"] is None)

    check("7  node rows carry the S4 retrieval fields (node_id/path/band/score/cluster/owner)",
          all(k in nodes[0] for k in ("node_id", "path", "band", "score", "cluster", "owner_upn")))

    check("8  guardrail: params.signal names the timestamp-only source (content/comms never read)",
          "content/comms NEVER read" in idx["params"]["signal"])

    # 9: TO-7 P1 sibling projection -- pure, 4 standard cols populated, 1 row per node
    idx["graph_vintage"] = {"marker_committed_at": "2026-07-16T03:33:01Z"}
    srows = sibling_rows(idx)
    check("9  sibling_rows: 1:1 with nodes, snapshot_date/computed_at/producer_ref/marker_head set",
          len(srows) == len(idx["dimensions"]["write_heat"]["nodes"])
          and srows[0]["snapshot_date"] == "2026-07-15"
          and srows[0]["computed_at"] > 0
          and srows[0]["producer_ref"].startswith("ms_heat_index-")
          and srows[0]["marker_head"] == "2026-07-16T03:33:01Z")

    total, passed = len(results), sum(results)
    print(f"=== {passed}/{total} PASS ===")
    return passed == total


def main() -> int:
    ap = argparse.ArgumentParser(description="MS write-heat index over the canonical globgrph MS slice")
    ap.add_argument("--half-life", type=float, default=DEFAULT_PARAMS.half_life_days)
    ap.add_argument("--hot-days", type=float, default=DEFAULT_PARAMS.hot_days)
    ap.add_argument("--warm-days", type=float, default=DEFAULT_PARAMS.warm_days)
    ap.add_argument("--local-only", action="store_true", help="write local index only (no S3)")
    ap.add_argument("--emit-sibling", action="store_true",
                    help="TO-7 P1: also stage the ms_heat_snap sibling batch (JSONL to the "
                         "snap_ingest pending lane; the in-VPC leg appends it)")
    ap.add_argument("--dry-run", action="store_true", help="compute + summary, write NOTHING")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return 0 if _self_test() else 1

    params = HeatParams(half_life_days=args.half_life, hot_days=args.hot_days,
                        warm_days=args.warm_days, freq_weight=0.0)
    rows, vintage = read_ms_nodes()
    idx = build_index(rows, params, _now())
    idx["graph_vintage"] = vintage
    d = idx["denominators"]
    print(f"OK: MS_HEAT_COMPUTED scored={d['scored']}/{d['rows_read']} bands={d['bands']} "
          f"clusters={len(idx['dimensions']['write_heat']['clusters'])} "
          f"vintage={vintage.get('graph_nodes_last_write') or vintage}")
    if args.dry_run:
        print("OK: DRY_RUN (0 writes)")
        return 0
    persist(idx, local_only=args.local_only)
    if args.emit_sibling and not args.local_only:
        stage_sibling(idx)
    # DS RAVC-step-4 finding (141751Z): a printed WARN is not a guard on an unattended run
    # ("a guard nothing invokes == no guard"). Warn-and-ship is kept (the write already
    # happened -- per-node rows are correct, halting the emit would be disproportionate), BUT
    # the coverage gap now reaches the emit's RETURN SIGNAL: exit 2 so an eventual scheduled
    # wrapper's exit-status is the consumer that outlives a reader's attention. clustered_n/
    # total_n also ride the served denominators (a durable surface, not stdout-only).
    cov = (idx.get("denominators") or {}).get("cluster_coverage") or {}
    cn, tn = cov.get("clustered_n"), cov.get("total_n")
    if cn is not None and tn is not None and cn != tn:
        print(f"WARN: CLUSTER_COVERAGE_GAP_ON_WRITE clustered_n={cn} total_n={tn} -- index/"
              "sibling WRITTEN (warn-and-ship) but exiting 2 so an unattended run signals the "
              "gap (the slash-less drop class; ping 0.4.0_DS_ClientPlatform)")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
