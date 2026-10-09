"""NFRA_TRNSPT round 14 (keep-driving on an empty tick) -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  l14   TR14-l14-AC1  the commentary Lambda's handler test passes and holds, by name: the full faked path lands a ticket (done), and
                      with no vendor word the model is never called and no ticket is written
  l14n  TR14-l14-AC2  data/transcripts/scripts/commentary/NAMES.json equals lib/opal_naming.py name() output for every row
  h14   TR14-h14-AC1  the entry test file holds and passes the holdings-category derivation test by name
  x14   TR14-x14-AC1  the exception-list test file passes and holds, by name: Apple survives as an issuer, and "Apple" as a person
                      name in a name context is still wiped

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")


def _pytest(path, names):
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    text = path.read_text(encoding="utf-8")
    missing = [n for n in names if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    r = subprocess.run([sys.executable, "-m", "pytest", str(path), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(names)), tail


def l14():
    return _pytest(TESTS / "test_commentary_lambda.py",
                   ["test_full_path_lands_ticket", "test_no_vendor_word_never_calls_model"])


def l14n():
    p = Path("data/transcripts/scripts/commentary/NAMES.json")
    if not p.exists():
        return False, "absent: %s" % p.as_posix()
    sys.path.insert(0, str(Path.cwd()))
    from lib import opal_naming  # noqa: E402
    rows = json.loads(p.read_text(encoding="utf-8"))
    bad = []
    for key, row in rows.items():
        if key.startswith("_"):
            continue
        built = opal_naming.name(row["system"], row["scope"], row["function"], row["kind"], row.get("qualifier"))
        if built != row.get("name"):
            bad.append("%s: %r != %r" % (key, row.get("name"), built))
    if not rows or bad:
        return False, "; ".join(bad) or "no rows"
    return True, "rows=%d all equal name()" % len([k for k in rows if not k.startswith("_")])


def h14():
    return _pytest(TESTS / "test_commentary_entry.py", ["test_holdings_categories_from_normalized_input"])


def x14():
    return _pytest(TESTS / "test_securities_exceptions.py",
                   ["test_apple_survives_as_issuer", "test_apple_as_person_name_still_wiped"])


CHECKS = {"l14": ("R14-L14", l14), "l14n": ("R14-L14N", l14n), "h14": ("R14-H14", h14), "x14": ("R14-X14", x14)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r14_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
