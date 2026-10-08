"""NFRA_TRNSPT round 5 -- the issuer's mechanical checks (2.0.0_SA_COO~T2), one subcommand per criterion.

  a5-file    TR5-a5-AC1  the meeting allowlist file lists the Monday meeting series FIRST; every row's identifier equals
                         the one series.json carries for that series, and every row's source is a path:line that exists
  a5-test    TR5-a5-AC2  the allowlist test file passes, and it holds a test that a row with no identifier, and a row with
                         no source, is rejected
  c5-record  TR5-c5-AC1  the deployed-vs-HEAD record names the manifest's deployed commit and a verdict for mail_route.py,
                         with a positive-control line
  c5-census  TR5-c5-AC2  the listing census test file passes (counts only; a planted sender address never in its output)

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
SERIES = Path("data/transcripts/scripts/teams/series.json")
ALLOWLIST = Path("data/transcripts/scripts/teams/meeting_allowlist.json")
RECORD = Path("org/missions/D9/NFRA/NFRA_TRNSPT/deliverables/0.9.0_WK_NFRA_TRNSPT~2/R5_MAIL_ROUTE_DEPLOYED_VS_HEAD.md")


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
    m = re.fullmatch(r"(\S+):(\d+)", str(src).strip().strip("`"))
    if not m:
        return False
    p = Path(m.group(1))
    if not p.is_file():
        return False
    with p.open(encoding="utf-8", errors="replace") as f:
        return 1 <= int(m.group(2)) <= sum(1 for _ in f)


def a5_file():
    if not ALLOWLIST.exists():
        return False, "absent: %s" % ALLOWLIST.as_posix()
    doc = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    rows = doc.get("meetings") if isinstance(doc, dict) else None
    if not isinstance(rows, list) or not rows:
        return False, "no meetings list"
    known = {s["table"]: s["online_meeting_id"] for s in json.loads(SERIES.read_text(encoding="utf-8"))["series"]}
    if rows[0].get("series") != "monday_meeting":
        return False, "first row is %r, not monday_meeting" % rows[0].get("series")
    for i, row in enumerate(rows):
        sid = row.get("series")
        if sid not in known:
            return False, "row %d series %r is not in series.json" % (i, sid)
        if row.get("online_meeting_id") != known[sid]:
            return False, "row %d (%s) identifier differs from series.json" % (i, sid)
        if not _source_ok(row.get("source", "")):
            return False, "row %d (%s) source is not a path:line that exists" % (i, sid)
    return True, "rows=%d first=monday_meeting" % len(rows)


def a5_test():
    path = TESTS / "test_meeting_allowlist.py"
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    text = path.read_text(encoding="utf-8")
    for need in ("def test_reject_row_without_identifier", "def test_reject_row_without_source"):
        if need not in text:
            return False, "missing %s" % need
    return _pytest(path)


def c5_record():
    if not RECORD.exists():
        return False, "absent: %s" % RECORD.as_posix()
    text = RECORD.read_text(encoding="utf-8")
    m = re.search(r"^MAIL_ROUTE: deployed@([0-9a-f]{10,40}) (SAME-AS-HEAD|DIFFERS) SOURCE: (\S+)\s*$", text, re.M)
    ctl = re.search(r"^POSITIVE_CONTROL: (\S+) (DIFFERS|SAME-AS-HEAD)\s*$", text, re.M)
    if not m or not ctl:
        return False, "missing line(s): MAIL_ROUTE=%s POSITIVE_CONTROL=%s" % (bool(m), bool(ctl))
    if not _source_ok(m.group(3)):
        return False, "source not found at a real line: %s" % m.group(3)
    return True, "deployed=%s verdict=%s" % (m.group(1)[:10], m.group(2))


def c5_census():
    path = TESTS / "test_listing_census.py"
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    if "def test_no_sender_address_in_output" not in path.read_text(encoding="utf-8"):
        return False, "missing test_no_sender_address_in_output"
    return _pytest(path)


CHECKS = {
    "a5-file": ("R5-A5-FILE", a5_file),
    "a5-test": ("R5-A5-TEST", a5_test),
    "c5-record": ("R5-C5-RECORD", c5_record),
    "c5-census": ("R5-C5-CENSUS", c5_census),
}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r5_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
