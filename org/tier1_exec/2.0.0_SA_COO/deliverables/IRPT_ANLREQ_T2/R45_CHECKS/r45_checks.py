"""IRPT_ANLREQ round 45, workstream TX -- the issuer's mechanical check for a cited-line READ record (2.0.0_SA_COO~T2).

  rec <record.md> [min_rows]   the record is a markdown table `| surface | path:line | verdict | evidence |` plus one line
                               `DENOMINATOR: <n> <what was enumerated and how>`. The check is mechanical:
                                 - n equals the number of table rows and is at least min_rows (default 3);
                                 - every citation `path:line` names a repository file that exists and a line inside it;
                                 - every evidence cell holds a backticked quote that occurs within 5 lines of the cited line;
                                 - every verdict is in the closed set below.
  --self-test                  green record, then four mutants (bad path, bad quote, bad verdict, wrong denominator); each must fail.

Prints R45-REC-OK rows=<n> or R45-REC-FAIL <reason> and exits 0 / 1. Run from the repo root (or a worktree root).
"""
import os
import re
import sys
import tempfile
from pathlib import Path

VERDICTS = {"REFUSES-TESTED", "REFUSES-UNTESTED", "ADMITS", "SURFACES-ON-TICKET", "SILENT", "NOT-APPLICABLE", "UNREAD"}
CITE = re.compile(r"^`?([^`:\s|]+):(\d+)`?$")
QUOTE = re.compile(r"`([^`]+)`")
DENOM = re.compile(r"DENOMINATOR:\s*(\d+)\b")


def check(record, min_rows=3, root=Path(".")):
    p = Path(record)
    if not p.exists():
        return False, "absent: %s" % p.as_posix()
    text = p.read_text(encoding="utf-8")
    m = DENOM.search(text)
    if not m:
        return False, "no DENOMINATOR line"
    n = int(m.group(1))
    rows = []
    for ln in text.splitlines():
        if not ln.startswith("|"):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cells) != 4 or set(cells[0]) <= set("-: ") or cells[0].lower() == "surface":
            continue
        rows.append(cells)
    if len(rows) != n:
        return False, "denominator %d but %d table rows" % (n, len(rows))
    if n < min_rows:
        return False, "only %d rows, need at least %d" % (n, min_rows)
    for surface, cite, verdict, evidence in rows:
        if verdict not in VERDICTS:
            return False, "row '%s': verdict '%s' not in the closed set" % (surface[:40], verdict)
        c = CITE.match(cite)
        if not c:
            return False, "row '%s': citation '%s' is not path:line" % (surface[:40], cite)
        target = root / c.group(1)
        if not target.is_file():
            return False, "row '%s': %s is not a file" % (surface[:40], c.group(1))
        lines = target.read_text(encoding="utf-8", errors="replace").splitlines()
        line = int(c.group(2))
        if not 1 <= line <= len(lines):
            return False, "row '%s': line %d outside %s (%d lines)" % (surface[:40], line, c.group(1), len(lines))
        q = QUOTE.search(evidence)
        if not q:
            return False, "row '%s': evidence holds no backticked quote" % surface[:40]
        window = "\n".join(lines[max(0, line - 6):line + 5])
        if q.group(1) not in window:
            return False, "row '%s': quote '%s' not within 5 lines of %s:%d" % (surface[:40], q.group(1)[:40], c.group(1), line)
    return True, "rows=%d" % n


def self_test():
    me = os.path.relpath(__file__).replace(os.sep, "/")
    good = ("| surface | path:line | verdict | evidence |\n|---|---|---|---|\n"
            "| a | %s:%d | ADMITS | `VERDICTS` |\n| b | %s:%d | UNREAD | `CITE` |\n| c | %s:%d | SILENT | `DENOM` |\n"
            "DENOMINATOR: 3 rows of the self-test\n") % (me, 24, me, 25, me, 27)
    lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    def at(token):
        return next(i + 1 for i, ln in enumerate(lines) if ln.startswith(token))
    good = good.replace(":24 ", ":%d " % at("VERDICTS =")).replace(":25 ", ":%d " % at("CITE =")).replace(":27 ", ":%d " % at("DENOM ="))
    cases = {
        "green": (good, True),
        "bad path": (good.replace(me, "no/such/file.py", 1), False),
        "bad quote": (good.replace("`VERDICTS`", "`NOT_IN_THE_FILE`"), False),
        "bad verdict": (good.replace("ADMITS", "PROBABLY-FINE"), False),
        "wrong denominator": (good.replace("DENOMINATOR: 3", "DENOMINATOR: 4"), False),
    }
    for name, (body, want) in cases.items():
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "rec.md"
            f.write_text(body, encoding="utf-8")
            ok, why = check(f)
        if ok != want:
            print("R45-SELFTEST-FAIL %s: got ok=%s (%s)" % (name, ok, why))
            return 1
    print("R45-SELFTEST-OK green plus four mutants refused")
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--self-test":
        sys.exit(self_test())
    if len(sys.argv) < 3 or sys.argv[1] != "rec":
        print("usage: r45_checks.py rec <record.md> [min_rows] | --self-test")
        sys.exit(2)
    ok, why = check(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 3)
    print("R45-REC-%s %s" % ("OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
