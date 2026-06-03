#!/usr/bin/env python3
"""runner-telemetry — 1Hz process telemetry shared lib.

Wrap any command and capture per-second CPU/memory/IO/threads for the wrapped
process tree. Output: JSONL one record per tick to a local file. Optional
post-run S3 upload for cross-machine analysis.

USAGE:
    python .tools/runner-telemetry.py \\
        --runner inf-gold-layer-runner \\
        --script INF_C_01.canonical_nna \\
        -- python data/orion/scripts/gold/INF_C_01.canonical_nna.py --upload

OUTPUT:
    {base-dir}/{runner}/{script}/{run_id}.jsonl
    (default base-dir: .runtmp/telemetry)

OPTIONAL S3 UPLOAD:
    --s3-bucket opal-data-inf --s3-prefix telemetry
    -> s3://opal-data-inf/telemetry/{runner}/{script}/{run_id}.jsonl

DESIGN RATIONALE (Andrew 2026-05-08):
- CW Custom Metrics path rejected (~$1500/mo at full cardinality)
- CW Logs path rejected (~$1-2/mo: still recurring API cost)
- This implementation: local JSONL writes, $0 cost, no rate limits, fully
  grep/jq-able, optional S3 archive for cross-machine review (~$0.001/mo)

CW alarms can be added later via S3 → CW metric extraction if needed.
"""
from __future__ import annotations

import argparse
import contextlib
import json
import logging
import subprocess
import sys
import threading
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional, TextIO

import psutil

LOG = logging.getLogger("runner-telemetry")

DEFAULT_INTERVAL_S = 1.0
DEFAULT_BASE_DIR = ".runtmp/telemetry"


# ---------------------------------------------------------------------------
# Sampler core
# ---------------------------------------------------------------------------

def _refresh_process_tree(pid: int, cache: dict[int, psutil.Process]) -> list:
    """Return [root + descendants], reusing cached Process objects.

    psutil.Process.cpu_percent(interval=None) tracks usage *since the last
    call on the same Process instance*. Recreating instances each tick
    discards history → always 0%. Cache + reuse instances; prime cpu_percent
    on first add.
    """
    if pid not in cache:
        try:
            cache[pid] = psutil.Process(pid)
        except psutil.NoSuchProcess:
            return []
    root = cache[pid]
    if not root.is_running():
        cache.pop(pid, None)
        return []
    procs = [root]
    try:
        for child in root.children(recursive=True):
            cpid = child.pid
            if cpid not in cache:
                try:
                    child.cpu_percent(interval=None)  # prime
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
                cache[cpid] = child
            procs.append(cache[cpid])
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
    dead = [k for k, v in cache.items() if not v.is_running()]
    for k in dead:
        cache.pop(k, None)
    return procs


def _aggregate_sample(procs: list) -> dict[str, float]:
    """Sum CPU%, memory, threads, cumulative IO across the process tree.

    MEMORY (NFRA telemetry-fix 2026-06-03): the primary `memory_mb` is now
    tree-summed **PSS** (proportional set size), not RSS. Forked multiprocessing
    workers share the parent's data via copy-on-write; RSS counts those shared
    pages in EVERY worker, so summed-RSS over-reports physical memory many-fold
    (the phantom "TB peaks" on a 128 GB box). PSS counts each physical page once,
    split proportionally among sharers — so tree-summed PSS is the true physical
    footprint of the script's process tree. RSS retained as `memory_rss_mb` for
    comparison; system-wide used is captured as `sys_mem_*` (the instance-level
    right-sizing number). PSS needs Linux + /proc access (root on the runners);
    falls back to RSS where unavailable.
    """
    cpu_pct = 0.0
    mem_pss = 0.0
    mem_rss = 0.0
    pss_ok = False
    threads = 0
    disk_read = 0
    disk_write = 0
    for p in procs:
        try:
            cpu_pct += p.cpu_percent(interval=None)
            try:
                fi = p.memory_full_info()
                _pss = getattr(fi, "pss", 0) or 0
                mem_pss += _pss / (1024 * 1024)
                mem_rss += fi.rss / (1024 * 1024)
                if _pss:
                    pss_ok = True
            except (psutil.AccessDenied, AttributeError, OSError):
                mem_rss += p.memory_info().rss / (1024 * 1024)
            threads += p.num_threads()
            try:
                io = p.io_counters()
                disk_read += io.read_bytes
                disk_write += io.write_bytes
            except (psutil.AccessDenied, AttributeError):
                pass
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    try:
        vm = psutil.virtual_memory()
        sys_used_mb = vm.used / (1024 * 1024)
        sys_pct = vm.percent
    except Exception:
        sys_used_mb = 0.0
        sys_pct = 0.0
    return {
        "cpu_pct": cpu_pct,
        # primary memory metric = true physical (PSS); rss fallback if PSS absent
        "memory_mb": mem_pss if pss_ok else mem_rss,
        "memory_pss_mb": mem_pss,
        "memory_rss_mb": mem_rss,
        "pss_available": 1.0 if pss_ok else 0.0,
        "sys_mem_used_mb": sys_used_mb,
        "sys_mem_pct": sys_pct,
        "threads": float(threads),
        "disk_read_bytes": float(disk_read),
        "disk_write_bytes": float(disk_write),
    }


def _make_log_record(
    sample: dict[str, float],
    prev: Optional[dict[str, float]],
    interval_s: float,
    runner: str,
    script: str,
    run_id: str,
    timestamp: datetime,
) -> dict:
    rec = {
        "ts": timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z",
        "runner": runner,
        "script": script,
        "run_id": run_id,
        "cpu_pct": round(sample["cpu_pct"], 2),
        "memory_mb": round(sample["memory_mb"], 1),
        "memory_pss_mb": round(sample.get("memory_pss_mb", 0.0), 1),
        "memory_rss_mb": round(sample.get("memory_rss_mb", 0.0), 1),
        "sys_mem_used_mb": round(sample.get("sys_mem_used_mb", 0.0), 1),
        "sys_mem_pct": round(sample.get("sys_mem_pct", 0.0), 2),
        "threads": int(sample["threads"]),
    }
    if prev is not None and interval_s > 0:
        rec["disk_read_mbs"] = round(
            max(0.0, sample["disk_read_bytes"] - prev["disk_read_bytes"]) / interval_s / (1024 * 1024),
            3,
        )
        rec["disk_write_mbs"] = round(
            max(0.0, sample["disk_write_bytes"] - prev["disk_write_bytes"]) / interval_s / (1024 * 1024),
            3,
        )
    return rec


def _next_serial(day_root: Path) -> int:
    """Count existing .jsonl files under the day's telemetry root + 1.

    Race condition exists for parallel runs (no locking) — acceptable for
    cascade dispatch where scripts run sequentially. If two parallel runs
    both compute serial=N at the same instant, both will pick the same
    serial; the run_id (UUID) in the filename still uniquely identifies them.
    """
    if not day_root.exists():
        return 1
    return sum(1 for _ in day_root.rglob("*.jsonl")) + 1


def telemetry_path(
    base_dir: str,
    runner: str,
    script: str,
    run_id: str,
    started_at: datetime | None = None,
) -> Path:
    """Canonical path with daily folder + timestamp + version serial.

    Layout: {base_dir}/{YYYY-MM-DD}/{runner}/{script}/v{NNN}-{HHMMSSZ}-{run_id}.jsonl

    - YYYY-MM-DD: UTC date the run STARTED (folder for the day per Andrew directive)
    - v{NNN}: monotone serial across all telemetry files in that day's tree;
      zero-padded to 3 digits ("v001", "v002", ...)
    - HHMMSSZ: UTC time HH:MM:SS the run started, compact format
    - run_id: existing UUID12 disambiguator

    Andrew direct 2026-05-08T19:18Z: "every run is tagged with a timestamp and
    version serial and is output to some folder for the day that it ran."
    """
    started_at = started_at or datetime.now(timezone.utc)
    day = started_at.strftime("%Y-%m-%d")
    hhmmss = started_at.strftime("%H%M%SZ")
    day_root = Path(base_dir) / day
    serial = _next_serial(day_root)
    fname = f"v{serial:03d}-{hhmmss}-{run_id}.jsonl"
    return day_root / runner / script / fname


def sample_pid(
    pid: int,
    *,
    runner: str,
    script: str,
    run_id: Optional[str] = None,
    base_dir: str = DEFAULT_BASE_DIR,
    interval_s: float = DEFAULT_INTERVAL_S,
    stop_event: Optional[threading.Event] = None,
    out_path: Optional[Path] = None,
    started_at: Optional[datetime] = None,
) -> tuple[str, Path]:
    """Block-sample a PID tree at `interval_s` rate until process exits.

    If `out_path` is not supplied, it's computed via telemetry_path() using
    `started_at` (defaults to now). Pass `out_path` from sample_subprocess to
    avoid path-recomputation race when the subprocess wrapper has already
    yielded the path to its caller.
    """
    if run_id is None:
        run_id = uuid.uuid4().hex[:12]
    if out_path is None:
        out_path = telemetry_path(base_dir, runner, script, run_id, started_at)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    LOG.info("start pid=%s runner=%s script=%s run_id=%s -> %s",
             pid, runner, script, run_id, out_path)

    proc_cache: dict[int, psutil.Process] = {}
    initial = _refresh_process_tree(pid, proc_cache)
    for p in initial:
        try:
            p.cpu_percent(interval=None)  # prime
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    time.sleep(interval_s)

    prev: Optional[dict[str, float]] = None
    ticks = 0
    fp: TextIO
    with out_path.open("a", encoding="utf-8") as fp:
        while True:
            if stop_event is not None and stop_event.is_set():
                break
            procs = _refresh_process_tree(pid, proc_cache)
            if not procs:
                break
            sample = _aggregate_sample(procs)
            ts = datetime.now(timezone.utc)
            rec = _make_log_record(sample, prev, interval_s, runner, script, run_id, ts)
            fp.write(json.dumps(rec) + "\n")
            fp.flush()
            prev = sample
            ticks += 1
            time.sleep(interval_s)

    LOG.info("stop pid=%s ticks=%d run_id=%s file=%s", pid, ticks, run_id, out_path)
    return run_id, out_path


@contextlib.contextmanager
def sample_subprocess(
    pid: int,
    *,
    runner: str,
    script: str,
    run_id: Optional[str] = None,
    base_dir: str = DEFAULT_BASE_DIR,
    interval_s: float = DEFAULT_INTERVAL_S,
) -> Iterator[tuple[str, Path]]:
    """Spawn a daemon sampler thread; yield (run_id, out_path); join on exit."""
    if run_id is None:
        run_id = uuid.uuid4().hex[:12]
    started_at = datetime.now(timezone.utc)
    out_path = telemetry_path(base_dir, runner, script, run_id, started_at)
    stop_event = threading.Event()

    def _run() -> None:
        sample_pid(
            pid,
            runner=runner,
            script=script,
            run_id=run_id,
            base_dir=base_dir,
            interval_s=interval_s,
            stop_event=stop_event,
            out_path=out_path,
            started_at=started_at,
        )

    t = threading.Thread(target=_run, daemon=True, name=f"telemetry-{run_id}")
    t.start()
    try:
        yield run_id, out_path
    finally:
        stop_event.set()
        t.join(timeout=interval_s * 3)


# ---------------------------------------------------------------------------
# CLI launcher
# ---------------------------------------------------------------------------

def _maybe_upload_to_s3(
    local_path: Path,
    bucket: Optional[str],
    prefix: str,
    runner: str,
    script: str,
    run_id: str,
) -> None:
    if not bucket:
        return
    if not local_path.exists():
        LOG.warning("local file missing, skipping S3 upload: %s", local_path)
        return
    try:
        import boto3
    except ImportError:
        LOG.warning("boto3 unavailable, skipping S3 upload")
        return
    key = f"{prefix.rstrip('/')}/{runner}/{script}/{run_id}.jsonl"
    s3 = boto3.client("s3")
    s3.upload_file(str(local_path), bucket, key)
    LOG.info("uploaded -> s3://%s/%s", bucket, key)


def main(argv: Optional[list[str]] = None) -> int:
    p = argparse.ArgumentParser(
        prog="runner-telemetry",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--runner", required=True,
                   help="logical runner name (e.g. inf-gold-layer-runner)")
    p.add_argument("--script", required=True,
                   help="logical script name (e.g. INF_C_01.canonical_nna)")
    p.add_argument("--run-id", default=None, help="explicit run id; default uuid4()[:12]")
    p.add_argument("--base-dir", default=DEFAULT_BASE_DIR,
                   help=f"local telemetry root dir (default: {DEFAULT_BASE_DIR})")
    p.add_argument("--interval", type=float, default=DEFAULT_INTERVAL_S,
                   help=f"sampler interval seconds (default: {DEFAULT_INTERVAL_S})")
    p.add_argument("--s3-bucket", default=None,
                   help="if set, upload JSONL to s3 after wrapped command exits")
    p.add_argument("--s3-prefix", default="telemetry", help="S3 key prefix")
    p.add_argument("--log-level", default="INFO")
    p.add_argument("cmd", nargs=argparse.REMAINDER, help="-- followed by the command to wrap")
    args = p.parse_args(argv)

    logging.basicConfig(
        level=getattr(logging, args.log_level.upper(), logging.INFO),
        format="[%(asctime)s] [telemetry] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )

    cmd = args.cmd
    if cmd and cmd[0] == "--":
        cmd = cmd[1:]
    if not cmd:
        p.error("no wrapped command supplied (use -- <cmd>)")

    run_id = args.run_id or uuid.uuid4().hex[:12]
    proc = subprocess.Popen(cmd)
    with sample_subprocess(
        proc.pid,
        runner=args.runner,
        script=args.script,
        run_id=run_id,
        base_dir=args.base_dir,
        interval_s=args.interval,
    ) as (rid, out_path):
        rc = proc.wait()

    _maybe_upload_to_s3(out_path, args.s3_bucket, args.s3_prefix,
                        args.runner, args.script, run_id)
    return rc


if __name__ == "__main__":
    sys.exit(main())
