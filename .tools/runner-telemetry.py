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
    """Sum CPU%, memory, threads, cumulative IO across the process tree."""
    cpu_pct = 0.0
    memory_mb = 0.0
    threads = 0
    disk_read = 0
    disk_write = 0
    for p in procs:
        try:
            cpu_pct += p.cpu_percent(interval=None)
            memory_mb += p.memory_info().rss / (1024 * 1024)
            threads += p.num_threads()
            try:
                io = p.io_counters()
                disk_read += io.read_bytes
                disk_write += io.write_bytes
            except (psutil.AccessDenied, AttributeError):
                pass
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return {
        "cpu_pct": cpu_pct,
        "memory_mb": memory_mb,
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


def telemetry_path(base_dir: str, runner: str, script: str, run_id: str) -> Path:
    """Canonical file path: {base_dir}/{runner}/{script}/{run_id}.jsonl"""
    return Path(base_dir) / runner / script / f"{run_id}.jsonl"


def sample_pid(
    pid: int,
    *,
    runner: str,
    script: str,
    run_id: Optional[str] = None,
    base_dir: str = DEFAULT_BASE_DIR,
    interval_s: float = DEFAULT_INTERVAL_S,
    stop_event: Optional[threading.Event] = None,
) -> tuple[str, Path]:
    """Block-sample a PID tree at `interval_s` rate until process exits."""
    if run_id is None:
        run_id = uuid.uuid4().hex[:12]
    out_path = telemetry_path(base_dir, runner, script, run_id)
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
    out_path = telemetry_path(base_dir, runner, script, run_id)
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
