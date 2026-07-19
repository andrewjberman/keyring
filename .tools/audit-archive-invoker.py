"""
audit-archive-invoker -- automated durability + tamper-evidence for the untracked audit logs.

WHY: org/audit/archive/ is the ONLY durability substrate for the high-churn, gitignored audit
logs (git-author-override ~589 L/day, comp-which-rail, ledger-hook, ...). The manual snapshot
practice expires 2026-07-23; after that, absence of an automated invoker is itself a finding
(RV-0052 F-008 / F-A). Spec: docs/briefs/audit-archive-invoker-spec-20260716.md (4 clauses).

WHAT (every run, cheap):
  self-test   the closure-bar controls (S1-fires / mutant-fires / append-doesn't / stale-absent-
              fires / stale-no-growth-doesn't); FAIL-CLOSED (refuse to run) if any misbehaves.
              A check that cannot fail is not a check -- and one that fires for the WRONG reason is
              not one either, so each control asserts a SPECIFIC 3-way status {APPEND_OK, NON_APPEND,
              ERROR}, never merely "not-ok".
  clause 2    INTEGRITY -- per covered log, the baseline snapshot must be a byte-exact PREFIX of live
              (append-only). A non-append edit FIRES; the snapshot is WITHHELD and the baseline does
              NOT advance (the divergence is adjudicated by a human -- clause 3 -- before re-base).
              Clause 2 owns edits AND truncation/shrink (a shrunk live undershoots its baseline).
  clause 1    LIVENESS -- the baseline is current only if it covers all live content. FIRES when the
              baseline is older than AGE_THRESHOLD_H *and* an uncaptured tail exists (a covered log
              grew beyond the baseline). Old-but-complete = NOT a finding (T-1 / NEVER#1 false-Monday).
  clause 4    DEATH -- the invoker's own corpse. FIRES when the last-run marker is older than
              DEATH_THRESHOLD_H *and* a covered log grew during the silence (uncaptured churn). Idle-
              silent with zero growth is correct idle, not a corpse. "ran but snapshot-commit failed"
              is a distinct SNAPSHOT-FAILURE finding, not death.
  clause 3    finding TEXT detects the EDIT and states NO opinion about authority (no editor
              allowlist -- that is the surface that can be argued into a PASS).
  archive     when the baseline is >= SNAPSHOT_INTERVAL_H old AND a covered log grew AND integrity is
              clean, mint a new snapshot (concurrent-double-snapshot guarded) and advance the baseline.

>> THE GROWTH INTERLOCK (CTO-required, 2026-07-19 -- what makes growth-conditioning SOUND, not a
   blind spot): the growth signal for clauses 1 and 4 is derived from the SAME live read that
   prefix_test performs -- the exact path the S1 positive control exercises. So a broken live-reader
   does not silently report "no growth"; it makes the S1 positive control fail to fire, the self-test
   fail, and the whole instrument FAIL-CLOSED. Growth is never "silently no": a per-log read error
   returns ERROR (a fail-closed integrity finding), never a bogus zero-growth. <<

>> COMMIT AUTHORIZATION -- Option B (CTO-ruled 2026-07-19): org/audit/archive/** is the GOVERNANCE_AUDIT
   tamper-evidence lane, writable ONLY by MSTR + execs; that restriction IS the control. So the invoker
   commits the snapshot as the RUNNING session's serial (LD-0290 sessions/<sid>.serial): an EXEC startup's
   commit lands; a NON-EXEC startup DEFERS the commit gracefully ("deferred (lane)", not a failure) while
   STILL running detection (findings to stdout + the gitignored heartbeat). Detection is universal; only the
   tamper-lane WRITE is exec-gated. Corpse-resistance rides frequent exec sessions. NO owned-paths change. <<

Findings -> org/audit/archive/FINDINGS.md (append-only) + exit code. NO SES/SNS/CloudWatch (Andrew
07-17 alert-suspension; CTO-confirmed 2026-07-19: a local verifiability instrument, not an alert
system). Owner: 0.7.0_AE_CloudOps. Gate: 1.0.0_SA_CTO.

Exit: 0 clean | 1 finding(s) emitted | 2 self-test failed (instrument broken, fail-closed).
CLI: [--self-test] [--dry-run] [--json] [--now ISO8601]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # .tools/ so the shared resolver imports
from git_bash_resolver import git_bash  # noqa: E402  canonical python->bash resolver (.tools/git_bash_resolver.py)

# workspace root: two parents up (portable across shells). AUDIT_INVOKER_WS overrides it for tests.
WS = (Path(os.environ["AUDIT_INVOKER_WS"]).resolve()
      if os.environ.get("AUDIT_INVOKER_WS") else Path(__file__).resolve().parent.parent)
ARCHIVE = WS / "org" / "audit" / "archive"
MANIFEST = ARCHIVE / "MANIFEST.txt"
BASELINE_PTR = ARCHIVE / ".baseline"
FINDINGS = ARCHIVE / "FINDINGS.md"
HEARTBEAT = ARCHIVE / ".invoker-heartbeat.json"   # gitignored: single-host operational state
LOCKDIR = ARCHIVE / ".snapshot.lock"

S1_TS = "2026-07-13T144931Z"   # KNOWN-DIVERGENT pre-redaction baseline -- permanent positive control; NEVER a baseline
S2_TS = "2026-07-16T175907Z"   # first CLEAN baseline; the chain starts here
TS_FMT = "%Y-%m-%dT%H%M%SZ"

AGE_THRESHOLD_H = 24.0
SNAPSHOT_INTERVAL_H = 12.0
DEATH_THRESHOLD_H = 48.0
LOCK_STALE_MIN = 15.0

APPEND_OK, NON_APPEND, ERROR = "APPEND_OK", "NON_APPEND", "ERROR"


# ---------------- primitives ----------------
def parse_ts(name: str) -> datetime:
    return datetime.strptime(name, TS_FMT).replace(tzinfo=timezone.utc)


def fmt_ts(dt: datetime) -> str:
    return dt.strftime(TS_FMT)


def snapshots() -> list[tuple[datetime, Path]]:
    out: list[tuple[datetime, Path]] = []
    if ARCHIVE.is_dir():
        for d in ARCHIVE.iterdir():
            if d.is_dir():
                try:
                    out.append((parse_ts(d.name), d))
                except ValueError:
                    continue
    return sorted(out)


def flatten(live_rel: str) -> str:
    return live_rel.replace("/", "_")


def manifest_paths() -> list[str]:
    if not MANIFEST.is_file():
        return []
    paths = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            paths.append(line.replace("\\", "/"))
    return paths


def _head_n_lines(data: bytes, n: int) -> bytes:
    """Emulate `head -n n`: bytes up to and including the n-th newline (whole data if fewer)."""
    idx = count = 0
    while count < n:
        nl = data.find(b"\n", idx)
        if nl == -1:
            return data
        idx = nl + 1
        count += 1
    return data[:idx]


def prefix_test(live: Path, baseline_copy: Path) -> tuple[str, str, int, int]:
    """
    Byte-faithful pure-Python equivalent of the ratified instrument
        head -n <archive_line_count> <live> | cmp -s - <archive_copy>
    Returns (status, detail, live_lines, base_lines). live_lines/base_lines are newline counts
    read from the SAME bytes the comparison uses -- this is the growth interlock (see header):
    the growth signal shares prefix_test's read path, so a broken live-reader fails the S1
    positive control rather than silently reporting no-growth. ERROR fails-closed to FIRE in
    production; the self-test treats ERROR as instrument-broken, never a genuine detection.
    """
    if not baseline_copy.is_file():
        return (ERROR, f"baseline missing: {baseline_copy}", -1, -1)
    if not live.is_file():
        return (ERROR, f"live missing: {live}", -1, -1)
    try:
        base = baseline_copy.read_bytes()
        live_bytes = live.read_bytes()
        base_nl = base.count(b"\n")
        live_nl = live_bytes.count(b"\n")
        base_head = _head_n_lines(base, base_nl)     # baseline minus any trailing partial line
        live_head = _head_n_lines(live_bytes, base_nl)
        if live_head == base_head:
            return (APPEND_OK, f"append-only OK ({base_nl} baseline lines are a byte-exact prefix of live)",
                    live_nl, base_nl)
        lim = min(len(base_head), len(live_head))
        pos = next((i for i in range(lim) if base_head[i] != live_head[i]), lim)
        upto = base_head[:pos]
        line_no = upto.count(b"\n") + 1
        col = pos - (upto.rfind(b"\n") + 1) + 1
        return (NON_APPEND, f"non-append edit: first divergence at line {line_no}, col {col} "
                            f"(baseline {len(base_head)}B / live-head {len(live_head)}B)", live_nl, base_nl)
    except Exception as e:  # fail-closed
        return (ERROR, f"prefix-test exception (fail-closed to FIRE): {e}", -1, -1)


def age_hours(dt: datetime, now: datetime) -> float:
    return (now - dt).total_seconds() / 3600.0


def baseline_dir() -> Path | None:
    ts = None
    if BASELINE_PTR.is_file():
        ts = BASELINE_PTR.read_text(encoding="utf-8").strip()
    elif (ARCHIVE / S2_TS).is_dir():
        ts = S2_TS  # bootstrap: chain starts at S2, never S1
    if not ts:
        return None
    d = ARCHIVE / ts
    return d if d.is_dir() else None


# ---------------- clause-1 predicate (isolated for control testing) ----------------
def liveness_fires(now: datetime, threshold_h: float, snaps: list, uncaptured: bool) -> bool:
    """Growth-conditioned (NEVER#1): stale AND uncaptured tail. Old-but-complete does not fire."""
    if not snaps:
        return uncaptured
    return age_hours(snaps[-1][0], now) > threshold_h and uncaptured


# ---------------- closure-bar controls ----------------
def self_test() -> tuple[bool, list[str]]:
    log: list[str] = []
    ok = True

    def want(name: str, got: str, expect: str, detail: str) -> None:
        nonlocal ok
        if got == expect:
            log.append(f"CONTROL-{name} OK: {got} (expected). {detail}")
        else:
            ok = False
            log.append(f"CONTROL-{name} BROKEN: {got}, expected {expect} -- {detail}")

    # (A) REAL positive control: S1 -> live git-author-override MUST be a genuine NON_APPEND detection.
    #     This exercises prefix_test's live-read path -- the growth interlock (header) leans on it.
    live_gao = WS / "org" / "git-author-override-audit.log"
    s1 = ARCHIVE / S1_TS / "org_git-author-override-audit.log"
    st, d, _, _ = prefix_test(live_gao, s1)
    want("A(S1-redaction)", st, NON_APPEND, d)

    # (B) GENERATED instrument controls: a mid-file byte change MUST fire; a pure append MUST NOT.
    with tempfile.TemporaryDirectory() as td:
        tdp = Path(td)
        base = tdp / "b.log"
        base.write_bytes(b"a\nb\nc\nd\n")
        mut = tdp / "m.log"
        mut.write_bytes(b"a\nX\nc\nd\ne\n")
        app = tdp / "a.log"
        app.write_bytes(b"a\nb\nc\nd\ne\nf\n")
        st, d, _, _ = prefix_test(mut, base)
        want("B1(mutant)", st, NON_APPEND, d)
        st, d, lnl, bnl = prefix_test(app, base)
        want("B2(append)", st, APPEND_OK, d)
        want("B3(growth-signal)", "GREW" if lnl > bnl else "FLAT", "GREW",
             f"append read live_nl={lnl} > base_nl={bnl} via same path")

    # (C) LIVENESS controls: stale+growth fires; stale+no-growth does NOT (false-Monday guard).
    now = datetime(2026, 7, 19, tzinfo=timezone.utc)
    old = [(datetime(2026, 7, 1, tzinfo=timezone.utc), ARCHIVE / "2026-07-01T000000Z")]
    want("C1(absent+growth)", "FIRE" if liveness_fires(now, AGE_THRESHOLD_H, [], True) else "OK", "FIRE", "no snapshot + uncaptured tail")
    want("C2(stale+growth)", "FIRE" if liveness_fires(now, AGE_THRESHOLD_H, old, True) else "OK", "FIRE", "432h-old + uncaptured tail")
    want("C3(stale-no-growth)", "FIRE" if liveness_fires(now, AGE_THRESHOLD_H, old, False) else "OK", "OK", "stale but complete = correct idle")

    return ok, log


# ---------------- findings (append-only + IDEMPOTENT) ----------------
def _finding_sig(e: dict) -> str:
    """Normalized signature: volatile numbers (ages, line/col, byte counts) -> '#' so a re-run of the
    same unresolved condition does NOT duplicate the entry (CTO-required 2026-07-19)."""
    raw = f"{e['clause']}|{e['verdict']}|{e.get('log', '')}|{e.get('detail', '')}"
    return re.sub(r"\d+", "#", raw)


def emit(entries: list[dict], now: datetime, dry: bool) -> bool:
    """Append findings whose normalized signature is not already present. Returns True if anything wrote."""
    if not entries or dry:
        return False
    existing = FINDINGS.read_text(encoding="utf-8") if FINDINGS.is_file() else ""
    seen = set(re.findall(r"<!-- sig: (.*?) -->", existing))
    blocks = []
    for e in entries:
        sig = _finding_sig(e)
        if sig in seen:
            continue
        seen.add(sig)
        block = [f"\n## {fmt_ts(now)} -- {e['clause']} -- {e['verdict']}", f"<!-- sig: {sig} -->"]
        block += [f"- {k}: {v}" for k, v in e.items() if k not in ("clause", "verdict")]
        blocks.append("\n".join(block))
    if not blocks:
        return False
    with FINDINGS.open("a", encoding="utf-8") as fh:
        fh.write("\n".join(blocks) + "\n")
    return True


def persist_findings(report: dict, now: datetime, dry: bool) -> None:
    """Write findings (idempotent) and, on an exec run, durably commit FINDINGS.md."""
    if emit(report["findings"], now, dry) and not dry:
        serial = running_serial()
        if governance_permitted(serial):
            safe_commit(serial, ["org/audit/archive/FINDINGS.md"],
                        f"findings({fmt_ts(now)}): audit-archive-invoker durable findings")


# ---------------- Option B: running identity + tamper-lane permission ----------------
def running_serial() -> str | None:
    """The RUNNING session's serial via the LD-0290 file. This -- not a hardcode -- is the commit author."""
    sid = os.environ.get("CLAUDE_CODE_SESSION_ID")
    if sid:
        p = WS / "org" / "mcp" / "sessions" / f"{sid}.serial"
        if p.is_file():
            s = p.read_text(encoding="utf-8").strip()
            if s:
                return s
    return None


def governance_permitted(serial: str | None) -> bool | None:
    """Best-effort: is serial's BASE in GOVERNANCE_AUDIT permitted_agents? None = couldn't determine
    (then we ATTEMPT the commit and let the owned-paths gate be the source of truth)."""
    if not serial:
        return None
    base = serial.split("~")[0]
    op = WS / ".owned-paths.yaml"
    if not op.is_file():
        return None
    try:
        in_block = in_perm = False
        permitted: list[str] = []
        for ln in op.read_text(encoding="utf-8").splitlines():
            s = ln.strip()
            if s.startswith("GOVERNANCE_AUDIT:"):
                in_block = True
                continue
            if in_block and s.startswith("permitted_agents:"):
                in_perm = True
                continue
            if in_perm:
                if s.startswith("- "):
                    permitted.append(s[2:].strip())
                else:
                    break
        return (base in permitted) if permitted else None
    except OSError:
        return None


# ---------------- snapshot (concurrent-double-snapshot guarded; exec-gated commit) ----------------
def take_snapshot(now: datetime, paths: list[str], dry: bool) -> tuple[str, str]:
    serial = running_serial()
    if governance_permitted(serial) is False:                         # non-exec: defer, no snapshot I/O
        return ("deferred", f"lane: {serial} not GOVERNANCE_AUDIT-permitted -- an exec startup will archive")
    snaps = snapshots()
    if snaps and age_hours(snaps[-1][0], now) < SNAPSHOT_INTERVAL_H:   # guard 1: pre-commit age re-check
        return ("skip", f"newest {snaps[-1][1].name} is < {SNAPSHOT_INTERVAL_H}h old")
    if dry:
        return ("dry", f"would mint {fmt_ts(now)} covering {len(paths)} logs as author={serial or 'UNKNOWN'}")
    if not serial:
        return ("deferred", "no running serial (LD-0290 file) -- cannot attribute a tamper-lane commit")
    try:                                                              # guard 2: atomic mkdir lock
        LOCKDIR.mkdir()
    except FileExistsError:
        try:
            lock_age_min = age_hours(datetime.fromtimestamp(LOCKDIR.stat().st_mtime, timezone.utc), now) * 60
        except OSError:
            lock_age_min = 0.0
        if lock_age_min < LOCK_STALE_MIN:
            return ("skip", "another snapshot in progress (lock held)")
        try:
            LOCKDIR.rmdir()
            LOCKDIR.mkdir()
        except OSError:
            return ("skip", "lock contended")
    ts = fmt_ts(now)
    dest = ARCHIVE / ts
    try:
        if dest.exists():                                             # guard 3: unique-second collision
            return ("skip", f"{ts} already exists (concurrent)")
        dest.mkdir(parents=True)
        copied = [rel for rel in paths if (WS / rel).is_file()
                  and (shutil.copy2(WS / rel, dest / flatten(rel)) or True)]
        rc, out = safe_commit(serial, [f"org/audit/archive/{ts}"],
                              f"snapshot({ts}): audit-archive-invoker automated snapshot ({len(copied)} logs)")
        if rc == 0:
            BASELINE_PTR.write_text(ts + "\n", encoding="utf-8")
            safe_commit(serial, ["org/audit/archive/.baseline"], f"baseline({ts}): advance clean baseline pointer")
            return ("minted", f"{ts} minted + baseline advanced ({len(copied)} logs) by {serial}")
        shutil.rmtree(dest, ignore_errors=True)                       # roll back the created dir
        if "not in permitted_agents" in out or "owned-paths lane violation" in out:
            return ("deferred", f"lane: commit by {serial} denied by owned-paths gate -- an exec will archive")
        return ("commit-fail", f"safe-commit rc={rc} (non-lane): {out[-300:]}")
    finally:
        try:
            LOCKDIR.rmdir()
        except OSError:
            pass


def safe_commit(author_serial: str, pathspec: list[str], msg: str) -> tuple[int, str]:
    bash = git_bash()  # shared resolver -- absolute Git Bash, never the System32 WSL stub
    if not bash:
        return (127, "no Git Bash found (bare 'bash' would Windows-resolve to the WSL stub) -- cannot run safe-commit.sh")
    author = f"{author_serial} <{author_serial}@opal.agent>"
    cmd = [bash, str(WS / ".tools" / "safe-commit.sh"), "--author", author, "-m", msg, "--"] + pathspec
    r = subprocess.run(cmd, cwd=str(WS), capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# ---------------- heartbeat (clause-4 death substrate; single-host, gitignored) ----------------
def read_heartbeat() -> dict:
    if HEARTBEAT.is_file():
        try:
            return json.loads(HEARTBEAT.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def write_heartbeat(now: datetime, per_log: dict, snapshot_outcome: str) -> None:
    HEARTBEAT.write_text(json.dumps({
        "last_run": fmt_ts(now),
        "per_log_lines": per_log,
        "last_snapshot_outcome": snapshot_outcome,
    }, indent=2), encoding="utf-8")


# ---------------- main pass ----------------
def run(now: datetime, dry: bool) -> tuple[int, dict]:
    report: dict = {"now": fmt_ts(now), "findings": []}

    ok, stlog = self_test()
    report["self_test"] = {"ok": ok, "log": stlog}
    if not ok:
        report["findings"].append({"clause": "SELF-TEST", "verdict": "INSTRUMENT-BROKEN",
                                   "detail": "; ".join(s for s in stlog if "BROKEN" in s)})
        persist_findings(report, now, dry)
        return 2, report

    paths = manifest_paths()
    if not paths:
        report["findings"].append({"clause": "MANIFEST", "verdict": "MISSING", "detail": f"{MANIFEST} absent or empty"})
        persist_findings(report, now, dry)
        return 1, report

    # coverage-gap (print-the-denominator): missing-live entries + audit-log-shaped files not covered.
    for rel in paths:
        if not (WS / rel).is_file():
            report["findings"].append({"clause": "COVERAGE", "verdict": "MANIFEST-ENTRY-MISSING-LIVE",
                                       "log": rel, "detail": "listed in manifest but no live file"})
    manifest_set = set(paths)
    candidates: set[str] = set()
    for pat in ("org/*-audit.log", "org/*-override*.log", "org/mcp/*-audit.log",
                "org/mcp/*-override*.log", "org/mcp/*-rail.log", "org/tier0/audit/*-audit.log"):
        for p in WS.glob(pat):
            candidates.add(p.relative_to(WS).as_posix())
    for rel in sorted(candidates - manifest_set):
        report["findings"].append({"clause": "COVERAGE", "verdict": "UNCOVERED-AUDIT-LOG",
                                   "log": rel, "detail": "audit-log-shaped file not in MANIFEST -- review + add or exclude"})

    # clause 2 (integrity) -- and, via the SAME read, the growth signal (interlock).
    base = baseline_dir()
    integrity_clean = True
    uncaptured_tail = False
    live_nl_map: dict[str, int] = {}
    if base is None:
        report["findings"].append({"clause": "INTEGRITY", "verdict": "NO-BASELINE",
                                   "detail": "no baseline snapshot; cannot verify -- mint bootstrap"})
        integrity_clean = False
    else:
        report["baseline"] = base.name
        for rel in paths:
            st, d, live_nl, base_nl = prefix_test(WS / rel, base / flatten(rel))
            if st == APPEND_OK:
                live_nl_map[rel] = live_nl
                if live_nl > base_nl:
                    uncaptured_tail = True
            elif st == NON_APPEND:
                integrity_clean = False
                report["findings"].append({"clause": "INTEGRITY", "verdict": "NON-APPEND-EDIT", "log": rel, "detail": d,
                                           "action": "snapshot WITHHELD; baseline NOT advanced; needs human authority ruling (clause 3)"})
            else:  # ERROR -> fail-closed, never a silent no-growth
                integrity_clean = False
                report["findings"].append({"clause": "INTEGRITY", "verdict": "ERROR-FAILCLOSED", "log": rel, "detail": d})

    # clause 1 (liveness, growth-conditioned).
    if base is not None:
        base_dt = parse_ts(base.name)
        if liveness_fires(now, AGE_THRESHOLD_H, [(base_dt, base)], uncaptured_tail):
            report["findings"].append({"clause": "LIVENESS", "verdict": "STALE-BASELINE",
                                       "detail": f"baseline {base.name} is {age_hours(base_dt, now):.1f}h old (>{AGE_THRESHOLD_H}h) AND uncaptured tail exists",
                                       "action": "minting fresh snapshot below" if integrity_clean else "snapshot withheld (integrity not clean)"})

    # clause 4 (death, growth-in-window; distinct from snapshot-failure). Growth via interlocked map.
    hb = read_heartbeat()
    if hb.get("last_run"):
        silent_h = age_hours(parse_ts(hb["last_run"]), now)
        prior = hb.get("per_log_lines", {})
        grew = any(live_nl_map.get(rel, -1) > prior.get(rel, 0) for rel in live_nl_map)
        if silent_h > DEATH_THRESHOLD_H and grew:
            report["findings"].append({"clause": "DEATH", "verdict": "INVOKER-SILENT-WITH-CHURN",
                                       "detail": f"last run {hb['last_run']} ({silent_h:.1f}h ago) and covered logs grew since -- uncaptured churn",
                                       "prior_outcome": hb.get("last_snapshot_outcome", "?")})

    # archive: mint if stale-enough AND growth AND integrity clean.
    snapshot_outcome = "not-due"
    if base is not None and integrity_clean and uncaptured_tail and age_hours(parse_ts(base.name), now) >= SNAPSHOT_INTERVAL_H:
        status, detail = take_snapshot(now, paths, dry)
        snapshot_outcome = f"{status}: {detail}"
        report["snapshot"] = snapshot_outcome
        if status == "commit-fail":
            report["findings"].append({"clause": "SNAPSHOT-FAILURE", "verdict": "COMMIT-FAILED", "detail": detail,
                                       "note": "distinct from DEATH: the invoker RAN, the commit failed"})

    if not dry:
        write_heartbeat(now, live_nl_map, snapshot_outcome)
    persist_findings(report, now, dry)
    return (1 if report["findings"] else 0), report


def main() -> int:
    ap = argparse.ArgumentParser(description="audit-archive-invoker")
    ap.add_argument("--self-test", action="store_true", help="run only the closure-bar controls")
    ap.add_argument("--dry-run", action="store_true", help="verify + report, mint/commit nothing")
    ap.add_argument("--json", action="store_true", help="machine-readable report to stdout")
    ap.add_argument("--now", default=None, help="override now (ISO8601 UTC) for testing")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    if args.now:
        now = datetime.fromisoformat(args.now).replace(tzinfo=timezone.utc)

    if args.self_test:
        ok, log = self_test()
        for line in log:
            print(line)
        print(f"SELF-TEST: {'PASS' if ok else 'FAIL-CLOSED'}")
        return 0 if ok else 2

    try:
        rc, report = run(now, args.dry_run)
    except Exception as e:  # never crash the caller (session startup)
        print(f"audit-archive-invoker ERROR (fail-closed): {e}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"audit-archive-invoker {report['now']}: rc={rc}, {len(report['findings'])} finding(s), "
              f"baseline={report.get('baseline', 'NONE')}, snapshot={report.get('snapshot', 'not-due')}")
        for f in report["findings"]:
            print(f"  [{f['clause']}/{f['verdict']}] {f.get('log', '')} {f.get('detail', '')}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
