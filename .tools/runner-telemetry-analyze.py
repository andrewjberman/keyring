#!/usr/bin/env python3
"""runner-telemetry-analyze — distributional summary of JSONL telemetry.

Reads JSONL files written by `.tools/runner-telemetry.py` and emits:
  1. Per-script distribution: ticks, wall_s, min/max/mean/median/p95 of
     cpu_pct / memory_mb / threads / disk_read_mbs / disk_write_mbs,
     totals for disk read/write
  2. Full-run aggregate: total wall_s (sum), total ticks, peak/mean across
     all scripts, total disk read/write MB

USAGE:
    # Summarize everything under default root
    python .tools/runner-telemetry-analyze.py

    # Single file or specific subtree
    python .tools/runner-telemetry-analyze.py .runtmp/telemetry/inf-gold-layer-runner/
    python .tools/runner-telemetry-analyze.py path/to/run_id.jsonl

    # JSON output for programmatic consumption
    python .tools/runner-telemetry-analyze.py --json
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterator

DEFAULT_ROOT = ".runtmp/telemetry"
VECTORS = ("cpu_pct", "memory_mb", "threads", "disk_read_mbs", "disk_write_mbs")


def _iter_jsonl(path: Path) -> Iterator[Path]:
    if path.is_file():
        yield path
        return
    if path.is_dir():
        yield from sorted(path.rglob("*.jsonl"))


def _parse_ts(s: str) -> datetime:
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return datetime.fromisoformat(s)


def _percentile(values: list[float], pct: float) -> float:
    """p in [0, 100]. Returns 0 for empty list. Linear interpolation."""
    if not values:
        return 0.0
    sv = sorted(values)
    if len(sv) == 1:
        return sv[0]
    k = (pct / 100.0) * (len(sv) - 1)
    lo, hi = int(k), int(k) + 1
    if hi >= len(sv):
        return sv[-1]
    return sv[lo] + (sv[hi] - sv[lo]) * (k - lo)


def _dist_stats(values: list[float]) -> dict[str, float]:
    if not values:
        return {"min": 0.0, "max": 0.0, "mean": 0.0, "median": 0.0, "p95": 0.0}
    return {
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "mean": round(statistics.fmean(values), 2),
        "median": round(statistics.median(values), 2),
        "p95": round(_percentile(values, 95.0), 2),
    }


def _summarize_file(path: Path) -> dict | None:
    """Read one JSONL file; compute per-vector distribution stats."""
    rows = []
    with path.open(encoding="utf-8") as fp:
        for line in fp:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    if not rows:
        return None

    first = _parse_ts(rows[0]["ts"])
    last = _parse_ts(rows[-1]["ts"])
    wall_s = round((last - first).total_seconds(), 1)
    interval_s = wall_s / max(1, len(rows) - 1) if len(rows) > 1 else 1.0

    summary = {
        "runner": rows[0].get("runner", "?"),
        "script": rows[0].get("script", "?"),
        "run_id": rows[0].get("run_id", "?"),
        "ticks": len(rows),
        "wall_s": wall_s,
    }
    for v in VECTORS:
        vals = [float(r.get(v, 0.0)) for r in rows]
        summary[v] = _dist_stats(vals)
    # Cumulative IO totals (MB) — disk_*_mbs is rate, integrate over interval
    summary["tot_read_mb"] = round(sum(float(r.get("disk_read_mbs", 0.0)) for r in rows) * interval_s, 2)
    summary["tot_write_mb"] = round(sum(float(r.get("disk_write_mbs", 0.0)) for r in rows) * interval_s, 2)
    return summary


def _aggregate(summaries: list[dict]) -> dict:
    """Aggregate multi-script run summary."""
    if not summaries:
        return {}
    total_ticks = sum(s["ticks"] for s in summaries)
    total_wall = round(sum(s["wall_s"] for s in summaries), 1)
    total_read = round(sum(s["tot_read_mb"] for s in summaries), 2)
    total_write = round(sum(s["tot_write_mb"] for s in summaries), 2)
    agg = {
        "n_scripts": len(summaries),
        "total_ticks": total_ticks,
        "total_wall_s": total_wall,
        "total_wall_min": round(total_wall / 60.0, 1),
        "total_read_mb": total_read,
        "total_write_mb": total_write,
    }
    for v in VECTORS:
        # Across-runs: peak-of-peaks, mean-of-means
        peaks = [s[v]["max"] for s in summaries]
        means = [s[v]["mean"] for s in summaries]
        agg[f"{v}_peak"] = round(max(peaks), 2)
        agg[f"{v}_mean"] = round(statistics.fmean(means), 2)
    return agg


def _print_per_script(summaries: list[dict]) -> None:
    """Compact per-script table — wall + key vector p50/max."""
    if not summaries:
        print("(no telemetry rows)")
        return
    cols = [
        ("script", "script"),
        ("ticks", "ticks"),
        ("wall_s", "wall_s"),
        ("cpu_max", "cpu_pct.max"),
        ("cpu_p50", "cpu_pct.median"),
        ("cpu_mean", "cpu_pct.mean"),
        ("mem_max", "memory_mb.max"),
        ("mem_p50", "memory_mb.median"),
        ("mem_mean", "memory_mb.mean"),
        ("th_max", "threads.max"),
        ("rd_p95", "disk_read_mbs.p95"),
        ("rd_total", "tot_read_mb"),
        ("wr_p95", "disk_write_mbs.p95"),
        ("wr_total", "tot_write_mb"),
    ]
    rows = []
    for s in summaries:
        row = {}
        for label, key in cols:
            if "." in key:
                outer, inner = key.split(".")
                row[label] = s[outer].get(inner, 0)
            else:
                row[label] = s.get(key, 0)
        rows.append(row)

    widths = {label: max(len(label), max(len(str(r[label])) for r in rows)) for label, _ in cols}
    header = "  ".join(label.ljust(widths[label]) for label, _ in cols)
    print(header)
    print("  ".join("-" * widths[label] for label, _ in cols))
    for r in rows:
        print("  ".join(str(r[label]).ljust(widths[label]) for label, _ in cols))


def _print_dist_per_script(summary: dict) -> None:
    """Full per-vector distribution for a single script."""
    print(f"\n=== {summary['runner']}/{summary['script']}/{summary['run_id']} "
          f"({summary['ticks']} ticks, {summary['wall_s']}s) ===")
    rows = []
    for v in VECTORS:
        d = summary[v]
        rows.append({
            "vector": v,
            "min": d["min"],
            "max": d["max"],
            "mean": d["mean"],
            "median": d["median"],
            "p95": d["p95"],
        })
    cols = ["vector", "min", "max", "mean", "median", "p95"]
    widths = {c: max(len(c), max(len(str(r[c])) for r in rows)) for c in cols}
    print("  ".join(c.ljust(widths[c]) for c in cols))
    print("  ".join("-" * widths[c] for c in cols))
    for r in rows:
        print("  ".join(str(r[c]).ljust(widths[c]) for c in cols))
    print(f"tot_read_mb={summary['tot_read_mb']}  tot_write_mb={summary['tot_write_mb']}")


def _print_aggregate(agg: dict) -> None:
    if not agg:
        return
    print("\n" + "=" * 70)
    print("FULL-RUN AGGREGATE")
    print("=" * 70)
    print(f"  n_scripts:        {agg['n_scripts']}")
    print(f"  total_ticks:      {agg['total_ticks']:,}")
    print(f"  total_wall:       {agg['total_wall_s']}s ({agg['total_wall_min']} min)")
    print(f"  total_read_mb:    {agg['total_read_mb']}")
    print(f"  total_write_mb:   {agg['total_write_mb']}")
    print()
    print(f"  {'vector':<18}  {'peak-of-peaks':>14}  {'mean-of-means':>14}")
    print(f"  {'-' * 18}  {'-' * 14}  {'-' * 14}")
    for v in VECTORS:
        print(f"  {v:<18}  {agg[v + '_peak']:>14}  {agg[v + '_mean']:>14}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", nargs="?", default=DEFAULT_ROOT,
                   help=f"file or dir (default: {DEFAULT_ROOT})")
    p.add_argument("--detail", action="store_true",
                   help="emit full per-vector distribution table per script (vs compact summary)")
    p.add_argument("--json", action="store_true", help="emit JSON instead of tables")
    p.add_argument("--sort", default="wall_s", help="sort key for per-script table (default: wall_s)")
    p.add_argument("--ascending", action="store_true", help="ascending sort (default: descending)")
    args = p.parse_args(argv)

    root = Path(args.path)
    if not root.exists():
        print(f"path not found: {root}", file=sys.stderr)
        return 1

    summaries = []
    for jf in _iter_jsonl(root):
        s = _summarize_file(jf)
        if s is not None:
            summaries.append(s)

    if not summaries:
        print("(no telemetry files found)")
        return 0

    # Sort
    summaries.sort(key=lambda r: r.get(args.sort, 0), reverse=not args.ascending)

    agg = _aggregate(summaries)

    if args.json:
        print(json.dumps({"per_script": summaries, "aggregate": agg}, indent=2))
        return 0

    print(f"runner-telemetry-analyze | {len(summaries)} run(s) | path={root}")
    print()
    _print_per_script(summaries)

    if args.detail:
        for s in summaries:
            _print_dist_per_script(s)

    _print_aggregate(agg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
