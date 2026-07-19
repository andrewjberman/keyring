"""
Integration test for .tools/audit-archive-invoker.py -- exercises the finding MATRIX (clauses 1-4 +
coverage) against synthetic temp workspaces via AUDIT_INVOKER_WS, in --dry-run (no commit, so it is
independent of the GOVERNANCE_AUDIT lane / the A-vs-B commit-path decision).

A verification instrument must itself be verified: this asserts each clause FIRES on the condition it
targets AND does NOT fire on the look-alike that must be tolerated (growth-conditioning's false-Monday
negative, death-without-churn). Run: python .tools/tests/test_audit_archive_invoker.py  (exit 0 = all pass).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
INVOKER = REPO / ".tools" / "audit-archive-invoker.py"
REAL_ARCHIVE = REPO / "org" / "audit" / "archive"
S1, S2 = "2026-07-13T144931Z", "2026-07-16T175907Z"
GAO = "org_git-author-override-audit.log"          # flattened archive name
GAO_REL = "org/git-author-override-audit.log"      # live path
NOW_LATE = "2026-07-19T18:00:00"                    # 72h after S2 -> stale window
NOW_EARLY = "2026-07-16T20:00:00"                   # 2h after S2 -> fresh window

PASS = FAIL = 0


def run_invoker(ws: Path, now: str) -> tuple[int, dict]:
    env = dict(os.environ, AUDIT_INVOKER_WS=str(ws))
    r = subprocess.run([sys.executable, str(INVOKER), "--dry-run", "--json", "--now", now],
                       capture_output=True, text=True, env=env)
    try:
        return r.returncode, json.loads(r.stdout)
    except json.JSONDecodeError:
        return r.returncode, {"findings": [], "_stdout": r.stdout, "_stderr": r.stderr}


def verdicts(rep: dict) -> set:
    return {(f["clause"], f["verdict"]) for f in rep.get("findings", [])}


def make_ws(tmp: Path, *, live_bytes: bytes | None = None, manifest=(GAO_REL,),
            baseline=S2, keep_s2=True, heartbeat: dict | None = None) -> Path:
    """Minimal realistic WS: real S1 (+ optional S2) gao copies, a live gao, manifest, baseline."""
    arch = tmp / "org" / "audit" / "archive"
    arch.mkdir(parents=True)
    (arch / S1).mkdir()
    shutil.copy2(REAL_ARCHIVE / S1 / GAO, arch / S1 / GAO)
    if keep_s2:
        (arch / S2).mkdir()
        shutil.copy2(REAL_ARCHIVE / S2 / GAO, arch / S2 / GAO)
    if live_bytes is None:
        live_bytes = (REAL_ARCHIVE / S2 / GAO).read_bytes()   # == baseline -> clean, no growth
    (tmp / GAO_REL).parent.mkdir(parents=True, exist_ok=True)
    (tmp / GAO_REL).write_bytes(live_bytes)
    (arch / "MANIFEST.txt").write_text("\n".join(manifest) + "\n", encoding="utf-8")
    if baseline:
        (arch / ".baseline").write_text(baseline + "\n", encoding="utf-8")
    if heartbeat is not None:
        (arch / ".invoker-heartbeat.json").write_text(json.dumps(heartbeat), encoding="utf-8")
    return tmp


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS  {name}")
    else:
        FAIL += 1
        print(f"  FAIL  {name}  {detail}")


def scenario(idx: int, name: str):
    print(f"\n[{idx}] {name}")


if __name__ == "__main__":
    import tempfile
    S2_BYTES = (REAL_ARCHIVE / S2 / GAO).read_bytes()

    with tempfile.TemporaryDirectory() as td:
        ws = make_ws(Path(td) / "clean")  # live == baseline (no growth)
        scenario(1, "clean append-only (stale baseline, NO growth) -> must NOT fire liveness (false-Monday)")
        rc, rep = run_invoker(ws, NOW_LATE)
        v = verdicts(rep)
        check("no LIVENESS fire on stale-but-complete", ("LIVENESS", "STALE-BASELINE") not in v, str(v))
        check("integrity clean (no NON-APPEND)", not any(c == "INTEGRITY" for c, _ in v), str(v))

    with tempfile.TemporaryDirectory() as td:
        ws = make_ws(Path(td) / "grow", live_bytes=S2_BYTES + b"2026-07-19T00:00:00Z appended line\n")
        scenario(2, "stale baseline + growth -> LIVENESS fire")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("LIVENESS/STALE-BASELINE fires", ("LIVENESS", "STALE-BASELINE") in verdicts(rep), str(verdicts(rep)))

    with tempfile.TemporaryDirectory() as td:
        mutated = bytearray(S2_BYTES)
        mutated[len(mutated) // 2] ^= 0x20         # flip a mid-file byte -> non-append
        ws = make_ws(Path(td) / "tamper", live_bytes=bytes(mutated))
        scenario(3, "mid-file edit (live diverges from baseline) -> INTEGRITY NON-APPEND fire + withhold")
        rc, rep = run_invoker(ws, NOW_LATE)
        v = verdicts(rep)
        check("INTEGRITY/NON-APPEND-EDIT fires", ("INTEGRITY", "NON-APPEND-EDIT") in v, str(v))
        check("snapshot withheld (not minted)", "minted" not in str(rep.get("snapshot", "")), str(rep.get("snapshot")))

    with tempfile.TemporaryDirectory() as td:
        ws = make_ws(Path(td) / "nobase", keep_s2=False, baseline=None)
        scenario(4, "no baseline snapshot -> INTEGRITY NO-BASELINE fire")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("INTEGRITY/NO-BASELINE fires", ("INTEGRITY", "NO-BASELINE") in verdicts(rep), str(verdicts(rep)))

    with tempfile.TemporaryDirectory() as td:
        ws = make_ws(Path(td) / "gap")
        (ws / "org" / "rogue-audit.log").write_bytes(b"x\n")   # matches org/*-audit.log, not in manifest
        scenario(5, "audit-log-shaped file not in manifest -> COVERAGE UNCOVERED fire")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("COVERAGE/UNCOVERED-AUDIT-LOG fires", ("COVERAGE", "UNCOVERED-AUDIT-LOG") in verdicts(rep), str(verdicts(rep)))

    with tempfile.TemporaryDirectory() as td:
        ws = make_ws(Path(td) / "missing", manifest=(GAO_REL, "org/ghost-audit.log"))
        scenario(6, "manifest entry with no live file -> COVERAGE MANIFEST-ENTRY-MISSING-LIVE fire")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("COVERAGE/MANIFEST-ENTRY-MISSING-LIVE fires",
              ("COVERAGE", "MANIFEST-ENTRY-MISSING-LIVE") in verdicts(rep), str(verdicts(rep)))

    with tempfile.TemporaryDirectory() as td:
        base_lines = S2_BYTES.count(b"\n")
        ws = make_ws(Path(td) / "death", live_bytes=S2_BYTES + b"new churn line\n",
                     heartbeat={"last_run": "2026-07-17T000000Z", "per_log_lines": {GAO_REL: base_lines},
                                "last_snapshot_outcome": "minted"})
        scenario(7, "invoker silent >48h AND churn since -> DEATH fire")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("DEATH/INVOKER-SILENT-WITH-CHURN fires", ("DEATH", "INVOKER-SILENT-WITH-CHURN") in verdicts(rep), str(verdicts(rep)))

    with tempfile.TemporaryDirectory() as td:
        base_lines = S2_BYTES.count(b"\n")
        ws = make_ws(Path(td) / "idle", live_bytes=S2_BYTES,   # no growth
                     heartbeat={"last_run": "2026-07-17T000000Z", "per_log_lines": {GAO_REL: base_lines},
                                "last_snapshot_outcome": "minted"})
        scenario(8, "invoker silent >48h but NO churn -> DEATH must NOT fire (correct idle)")
        rc, rep = run_invoker(ws, NOW_LATE)
        check("no DEATH on silent-but-idle", ("DEATH", "INVOKER-SILENT-WITH-CHURN") not in verdicts(rep), str(verdicts(rep)))

    # --- commit-path control: the exact bug CTO's exec run caught (python -> WSL /bin/bash). ---
    # The dry-run matrix above NEVER runs the real commit, so it passed 10/10 while the live commit was
    # dead. This asserts the invoker resolves an ACTUAL runnable Git Bash, not the System32 WSL stub.
    import importlib.util
    spec = importlib.util.spec_from_file_location("inv", str(INVOKER))
    inv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inv)
    gb = inv.git_bash()
    scenario(9, "commit-path bash resolves to Git Bash (not the WSL stub) and actually executes")
    check("git_bash() found a real bash file", bool(gb) and Path(gb).is_file(), str(gb))
    check("resolved bash is NOT the System32 WSL stub", bool(gb) and "system32" not in gb.lower(), str(gb))
    rb = subprocess.run([gb, "-c", "echo ok"], capture_output=True, text=True) if gb else None
    check("resolved bash executes a command", bool(rb) and rb.returncode == 0 and "ok" in rb.stdout,
          (rb.stderr if rb else "no bash resolved"))

    print(f"\n==== {PASS} passed, {FAIL} failed ====")
    sys.exit(1 if FAIL else 0)
