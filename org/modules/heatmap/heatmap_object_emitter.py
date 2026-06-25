#!/usr/bin/env python3
"""
O1 producer/emitter -- the cadence + snapshot-EMIT half of HEATMAP_OBJECT (NFRA_HEATMAP
Strand-C). 0.5.0_AE_OpalETL's leg (COO converge-GO 20260625T2149Z: "your producer imports
[DS's build()], no re-walk").

SEPARATION OF CONCERNS (one engine, one home):
  - ENGINE (DS, object_freshness.build + heat_map S0): does the ONE git pass + scoring +
    clustering. Authoritative. This producer IMPORTS it; it NEVER re-walks the tree.
  - PRODUCER (here): runs build() on a CADENCE, assembles the DS-pinned snapshot schema,
    and SHIPS it to a configured SINK. No scoring logic, no second git walk, no engine edit.

The snapshot schema reproduced below is DS's pinned object_freshness --json contract
(generated_ts/root/half_life_days/summary/paths/cold_subtrees). It lives here too because the
EMIT FORMAT is the producer's responsibility; if DS later factors a `snapshot()` helper out of
object_freshness.main(), this switches to importing it (tracked: README "snapshot helper").

SINKS (the open Q2 emit-target -- coordinate the PIN with COO/Andrew at producer-stage;
ALL THREE work today so the pin is a --sink flag, never a rewrite):
  - stdout  : print the snapshot JSON (DEFAULT -- zero infra commitment; safe to run anywhere).
  - file    : write a rolling snapshot file (option a -- a repo/disk file; --out PATH).
  - s3      : write a date-keyed time-series object (option b, RECOMMENDED -- durable history;
              --bucket B --prefix P -> s3://B/P/object-freshness/{YYYY-MM-DD}.json + latest.json).
  (option c "derived-on-demand" = just run object_freshness.py --json directly; no producer.)

ADVISORY ONLY (inherited, NFRA_DEBTSCAN chain): emits SCORES + a cold-cluster view. It NEVER
recommends, archives, or deletes -- that is O3, behind never-auto-delete + verify-before-recommend.

Cadence: invoked by the cloud half (EventBridge -> the shared transient-EC2/Lambda vehicle, the
same one the month-end ETFS report rides). The SCHEDULE + IAM are a separate infra leg; this
script is the unit of work it runs. Locally: `python heatmap_object_emitter.py [--sink ...]`.

ASCII only. stdlib + (for --sink s3 only) boto3.

Usage:
    python heatmap_object_emitter.py                                  # stdout, default knobs
    python heatmap_object_emitter.py --sink file --out snap.json
    python heatmap_object_emitter.py --sink s3 --bucket B --prefix heatmap
Author: 0.5.0_AE_OpalETL (NFRA_HEATMAP Strand-C, O1 producer/emitter). 2026-06-25.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heat_map import HeatParams, cluster_by_locality, summarize  # noqa: E402
from object_freshness import build  # noqa: E402  (DS's engine -- the ONE git pass lives here)


def assemble_snapshot(root: str, p: HeatParams, now_ts: float) -> dict:
    """Run DS's engine (build = the single git pass + scoring) and shape its output into the
    DS-pinned snapshot schema. NO re-walk: build() owns the tree traversal; this only formats
    its (scores, src) into the emit contract (identical to object_freshness.main --json)."""
    scores, src = build(root, p, now_ts)
    summ = summarize(scores)
    clusters = cluster_by_locality(scores, lambda path: os.path.dirname(path) or ".")
    cold_dirs = sorted(
        ((k, v) for k, v in clusters.items() if v["n"] >= 3 and v["cold_frac"] >= 0.8),
        key=lambda kv: (-kv[1]["n_cold"], -kv[1]["oldest_age_days"]),
    )
    return {
        "generated_ts": int(now_ts),
        "root": root,
        "half_life_days": p.half_life_days,
        "summary": summ,
        "paths": [
            {"path": s.item_id, "age_days": round(s.age_days, 2),
             "score": round(s.score, 6), "band": s.band, "source": src.get(s.item_id, "?")}
            for s in scores
        ],
        "cold_subtrees": [{"dir": k, **v} for k, v in cold_dirs],
    }


def _emit_stdout(snap: dict) -> str:
    json.dump(snap, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return "stdout"


def _emit_file(snap: dict, out_path: str) -> str:
    out_path = os.path.abspath(out_path)
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, indent=2)
    return out_path


def _emit_s3(snap: dict, bucket: str, prefix: str) -> str:
    """Date-keyed time-series + a stable latest.json pointer. The cold-subtree history IS the
    value of a durable store (a dir going cold OVER TIME is the archive signal O2 wants)."""
    import boto3  # local import: only --sink s3 needs the dep (keeps stdout/file stdlib-only)
    from datetime import datetime, timezone

    s3 = boto3.client("s3")
    day = datetime.fromtimestamp(snap["generated_ts"], tz=timezone.utc).strftime("%Y-%m-%d")
    base = "%s/object-freshness" % prefix.strip("/")
    body = json.dumps(snap, indent=2).encode("utf-8")
    dated_key = "%s/%s.json" % (base, day)
    latest_key = "%s/latest.json" % base
    for key in (dated_key, latest_key):
        s3.put_object(Bucket=bucket, Key=key, Body=body, ContentType="application/json")
    return "s3://%s/%s (+ latest.json)" % (bucket, dated_key)


def main() -> int:
    ap = argparse.ArgumentParser(description="O1 write-freshness producer/emitter (wraps DS build())")
    ap.add_argument("--root", default=".", help="repo root (default cwd)")
    ap.add_argument("--half-life", type=float, default=30.0, help="decay half-life in days")
    ap.add_argument("--sink", choices=("stdout", "file", "s3"), default="stdout",
                    help="emit target (Q2 pin: stdout=default, file=option a, s3=option b)")
    ap.add_argument("--out", default="", help="--sink file: output path")
    ap.add_argument("--bucket", default=os.environ.get("HEATMAP_BUCKET", ""),
                    help="--sink s3: target bucket (or HEATMAP_BUCKET env)")
    ap.add_argument("--prefix", default=os.environ.get("HEATMAP_PREFIX", "heatmap"),
                    help="--sink s3: key prefix (default 'heatmap', or HEATMAP_PREFIX env)")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    p = HeatParams(half_life_days=args.half_life)
    now_ts = time.time()
    snap = assemble_snapshot(root, p, now_ts)

    if args.sink == "stdout":
        where = _emit_stdout(snap)
    elif args.sink == "file":
        if not args.out:
            print("ERROR: --sink file requires --out PATH", file=sys.stderr)
            return 2
        where = _emit_file(snap, args.out)
    else:  # s3
        if not args.bucket:
            print("ERROR: --sink s3 requires --bucket (or HEATMAP_BUCKET env)", file=sys.stderr)
            return 2
        where = _emit_s3(snap, args.bucket, args.prefix)

    summ = snap["summary"]
    print("OK: emitted O1 snapshot -- %d paths (hot=%d warm=%d cold=%d, cold_frac=%.2f), "
          "%d cold subtrees -> %s"
          % (summ["n"], summ["bands"]["hot"], summ["bands"]["warm"], summ["bands"]["cold"],
             summ["cold_frac"], len(snap["cold_subtrees"]), where),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
