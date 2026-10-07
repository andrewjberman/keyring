"""NFRA_TRNSPT round 4 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  w4-spans   TR4-w4-AC1  a 120-day window is listed as spans of at most 31 days covering every day once; a known row skipped
  w4-bounds  TR4-w4-AC2  WINDOW_DAYS over 120 or under 1 raises before any gateway call
  l4-line    TR4-l4-AC1  ONE MAIL-PULL-FIRE line per fire, exact field set; a planted sender address never in stdout
  r4-record  TR4-r4-AC1  the route record names /hx/transcripts state and G-TEAMS-TX state, each with a path:line source
                         that exists at HEAD

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
RECORD = Path("org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R4_TRANSCRIPTS_ROUTE_RECORD.md")


def _pytest(path, k=None):
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    cmd = [sys.executable, "-m", "pytest", str(path), "-q", "-p", "no:cacheprovider"]
    if k:
        cmd += ["-k", k]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=110)
    lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()]
    tail = re.sub(r"\x1b\[[0-9;]*m", "", lines[-1] if lines else "")
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    if r.returncode != 0 or passed == 0:
        return False, "rc=%d %s" % (r.returncode, tail)
    return True, "passed=%d" % passed


def _source_ok(src):
    m = re.fullmatch(r"(\S+):(\d+)", src.strip().strip("`"))
    if not m:
        return False
    p = Path(m.group(1))
    if not p.is_file():
        return False
    with p.open(encoding="utf-8", errors="replace") as f:
        return int(m.group(2)) <= sum(1 for _ in f)


def r4_record():
    if not RECORD.exists():
        return False, "absent: %s" % RECORD.as_posix()
    text = RECORD.read_text(encoding="utf-8")
    route = re.search(r"^ROUTE: (released@[0-9a-f]{7,40}|not-released) SOURCE: (\S+)\s*$", text, re.M)
    gate = re.search(r"^G-TEAMS-TX: (\S+) SOURCE: (\S+)\s*$", text, re.M)
    if not route or not gate:
        return False, "missing line(s): ROUTE=%s G-TEAMS-TX=%s" % (bool(route), bool(gate))
    bad = [s for s in (route.group(2), gate.group(2)) if not _source_ok(s)]
    if bad:
        return False, "source not found at a real line: %s" % ", ".join(bad)
    return True, "route=%s gate=%s" % (route.group(1), gate.group(1))


CHECKS = {
    "w4-spans": ("R4-W4-SPANS", lambda: _pytest(TESTS / "test_mail_window_spans.py", "spans")),
    "w4-bounds": ("R4-W4-BOUNDS", lambda: _pytest(TESTS / "test_mail_window_spans.py", "bounds")),
    "l4-line": ("R4-L4-LINE", lambda: _pytest(TESTS / "test_mail_fire_line.py")),
    "r4-record": ("R4-R4-RECORD", r4_record),
}


def main(argv):
    if len(argv) != 1 or argv[0] not in CHECKS:
        print("usage: r4_checks.py {%s}" % "|".join(CHECKS))
        return 2
    token, fn = CHECKS[argv[0]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
