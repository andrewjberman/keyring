#!/usr/bin/env python3
"""model-census.py -- MEASURED model per seat and per worker on THIS box, graded against org/ref/MODEL_POLICY.json.

Read-only. The instrument is the Claude Code transcript, never a session's own claim: every assistant message in
~/.claude/projects/<project>/<session>.jsonl carries "model", and every subagent transcript sits beside it in
<session>/subagents/agent-*.jsonl with its agentType in agent-*.meta.json. org/mcp/sessions/<session>.serial maps a
session to its serial.

    python .tools/model-census.py                  # sessions active in the last 24h
    python .tools/model-census.py --hours 168      # wider window
    python .tools/model-census.py --since 2026-10-10T23:00:00Z

Per row: serial, role, expected model (policy, or CONTROL on a control device), measured model(s) with message counts,
and a verdict OK / MISMATCH / CONTROL / NO-POLICY-ROLE. The denominators are printed: sessions in the window, sessions
with no serial file, and subagent transcripts read. A session with no serial file is counted, never dropped. A model
seen in a minority of a session's messages (an explicit /model switch mid-session) is printed, not hidden.
Record: org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261010_23xxZ_MODEL_POLICY_BY_ROLE_AND_TEST_PLAN.md
"""
import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True,
                           cwd=Path(__file__).resolve().parent).stdout.strip() or Path(__file__).resolve().parents[1])
POLICY = ROOT / "org" / "ref" / "MODEL_POLICY.json"
SESSIONS = ROOT / "org" / "mcp" / "sessions"
PROJECTS = Path.home() / ".claude" / "projects"


def device():
    d = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if not d and sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                d = str(winreg.QueryValueEx(k, "AGENTBUS_DEVICE")[0]).strip()
        except OSError:
            d = ""
    return d


def models_in(path):
    c = Counter()
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"model"' not in line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                m = (rec.get("message") or {}).get("model") if isinstance(rec.get("message"), dict) else None
                if m and m != "<synthetic>":
                    c[m] += 1
    except OSError:
        pass
    return c


def fmt(c):
    return ", ".join("%s x%d" % (m, n) for m, n in c.most_common()) or "(no assistant message)"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--hours", type=float, default=24.0)
    ap.add_argument("--since", default="")
    ap.add_argument("--projects-dir", default="",
                    help="the Claude Code projects dir to read (default ~/.claude/projects, or $CLAUDE_CONFIG_DIR/projects); "
                         "a box whose seats run under another profile or config dir passes it here")
    a = ap.parse_args()
    global PROJECTS
    if a.projects_dir:
        PROJECTS = Path(a.projects_dir)
    elif os.environ.get("CLAUDE_CONFIG_DIR"):
        PROJECTS = Path(os.environ["CLAUDE_CONFIG_DIR"]) / "projects"
    since = (datetime.strptime(a.since, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc) if a.since
             else datetime.now(timezone.utc) - timedelta(hours=a.hours))
    pol = json.loads(POLICY.read_text(encoding="utf-8"))
    dev = device()
    treated = dev in pol.get("treatment_devices", [])
    wk = pol["worker"]
    print("MODEL-CENSUS policy=%s device=%s arm=%s since=%s" % (
        pol["policy_id"], dev or "UNSET", "TREATMENT" if treated else "CONTROL", since.strftime("%Y-%m-%dT%H:%M:%SZ")))

    all_transcripts = list(PROJECTS.glob("*/*.jsonl"))
    transcripts = [p for p in all_transcripts
                   if datetime.fromtimestamp(p.stat().st_mtime, timezone.utc) >= since]
    newest = max((p.stat().st_mtime for p in all_transcripts), default=0)
    print("PROJECTS-DIR %s exists=%s session transcripts total=%d newest=%s" % (
        PROJECTS, PROJECTS.exists(), len(all_transcripts),
        datetime.fromtimestamp(newest, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if newest else "none"))
    rows, no_serial, sub_read, mism = [], 0, 0, 0
    for t in sorted(transcripts, key=lambda p: p.stat().st_mtime):
        sid = t.stem
        sf = SESSIONS / (sid + ".serial")
        serial = sf.read_text(encoding="utf-8", errors="replace").strip() if sf.exists() else ""
        if not serial:
            no_serial += 1
        base = re.sub(r"~[A-Za-z0-9]+$", "", serial)
        role = next((r for r in pol["roles"] if serial and re.search(r["serial_regex"], base)), None)
        got = models_in(t)
        top = got.most_common(1)[0][0] if got else ""
        if not treated:
            exp, verdict = "CONTROL", "CONTROL"
        elif not role:
            exp, verdict = "-", "NO-POLICY-ROLE"
        else:
            exp = role["model"]
            verdict = "OK" if top == exp else "MISMATCH"
        mism += verdict == "MISMATCH"
        rows.append(("SESSION", serial or "(no serial file)", role["role"] if role else "-", exp, fmt(got), verdict, sid))
        for meta in sorted((t.parent / sid / "subagents").glob("agent-*.meta.json")):
            try:
                at = json.loads(meta.read_text(encoding="utf-8")).get("agentType", "?")
            except (OSError, ValueError):
                at = "?"
            sj = meta.with_name(meta.name.replace(".meta.json", ".jsonl"))
            if not sj.exists() or datetime.fromtimestamp(sj.stat().st_mtime, timezone.utc) < since:
                continue
            sub_read += 1
            sg = models_in(sj)
            stop = sg.most_common(1)[0][0] if sg else ""
            if at not in wk["agent_types"]:
                sexp, sv = "-", "NOT-A-WORKER"
            elif not treated:
                sexp, sv = "CONTROL", "CONTROL"
            else:
                sexp = wk["expected_model"]
                sv = "OK" if stop == sexp else "MISMATCH"
            mism += sv == "MISMATCH"
            rows.append(("  SUBAGENT", at, "worker" if at in wk["agent_types"] else "-", sexp, fmt(sg), sv,
                         sid[:8] + "/" + meta.name.split(".")[0]))
    for r in rows:
        print("%-10s %-34s %-16s %-18s %-8s %s | %s" % (r[0], r[1][:34], r[2], r[3], r[5], r[4], r[6]))
    print("DENOMINATOR: %d session transcript(s) in window, %d with no serial file, %d subagent transcript(s) read; "
          "%d MISMATCH" % (len(transcripts), no_serial, sub_read, mism))
    procs = live_claude_processes()
    if procs is not None:
        # A spawned seat can run with no main transcript on disk (laptop and site Z, 2026-10-14), so the transcript count
        # undercounts live seats. The command line is the second instrument: it shows the REQUESTED model, not the served one.
        for pid, created, model in procs:
            print("PROCESS    pid=%-7s started=%s requested_model=%s (claim: requested, from the command line)" % (
                pid, created, model or "(no --model flag: claude default)"))
        print("PROCESS-DENOMINATOR: %d live claude.exe process(es) vs %d session transcript(s) in window" % (
            len(procs), len(transcripts)))
    return 1 if mism else 0


def live_claude_processes():
    """(pid, created, --model value) per live claude.exe on Windows; None where the process table cannot be read."""
    if sys.platform != "win32":
        return None
    ps = ("Get-CimInstance Win32_Process -Filter \"Name='claude.exe'\" | ForEach-Object { "
          "'{0}|{1}|{2}' -f $_.ProcessId, $_.CreationDate.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ'), $_.CommandLine }")
    try:
        out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True,
                             timeout=60).stdout
    except (OSError, subprocess.SubprocessError):
        return None
    rows = []
    for line in out.splitlines():
        parts = line.split("|", 2)
        if len(parts) != 3:
            continue
        m = re.search(r"--model[ =]+\"?([^\s\"]+)", parts[2])
        rows.append((parts[0], parts[1], m.group(1) if m else ""))
    return rows


if __name__ == "__main__":
    sys.exit(main())
