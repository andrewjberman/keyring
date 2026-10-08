"""NFRA_TRNSPT round 12 (FWD-10, the AI commentary thread) -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  e12   TR12-e12-AC1  H2: test_entry.py passes and holds, by name, the abstract-request test and the no-client-identity test;
                      the READY-event contract file parses and names its fields
  d12   TR12-d12-AC1  H3+H4: test_drafter.py passes and holds, by name, the gate-refusal, no-precedent and no-identity-in-prompt tests
  t12   TR12-t12-AC1  H6: test_commentary_ticket_client.py passes and holds, by name, the ticket-write and never-blocks tests (the
                      contract is ~V2's v0.1 @a8410fcca3; no contract file of ours)

Each prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

TESTS = Path("data/transcripts/scripts/tests")
STD = Path("org/standards")


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


def _contract(path, need):
    if not path.exists():
        return False, "absent: %s" % path.as_posix()
    doc = json.loads(path.read_text(encoding="utf-8"))
    fields = doc.get("fields")
    if not isinstance(fields, dict) or not fields:
        return False, "%s: no fields map" % path.name
    missing = [k for k in need if k not in doc]
    if missing:
        return False, "%s: missing %s" % (path.name, ", ".join(missing))
    return True, "%s fields=%d" % (path.name, len(fields))


def _both(a, b):
    ok1, w1 = a
    ok2, w2 = b
    return ok1 and ok2, "%s | %s" % (w1, w2)


def e12():
    return _both(_contract(STD / "NFRA_TRNSPT_READY_EVENT_CONTRACT.json", ["producer", "consumer", "version"]),
                 _pytest(TESTS / "test_commentary_entry.py",
                         ["test_ready_event_to_abstract_request", "test_abstract_request_carries_no_client_identity"]))


def d12():
    return _pytest(TESTS / "test_commentary_drafter.py",
                   ["test_refuses_until_wipe_gate_passed", "test_no_precedent_draft_says_so",
                    "test_prompt_carries_no_client_identity"])


def t12():
    return _pytest(TESTS / "test_commentary_ticket_client.py",
                   ["test_writes_analysis_request_ticket", "test_failure_never_raises_into_report_path"])


CHECKS = {"e12": ("R12-E12", e12), "d12": ("R12-D12", d12), "t12": ("R12-T12", t12)}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in CHECKS:
        print("usage: r12_checks.py {%s}" % "|".join(CHECKS))
        sys.exit(2)
    token, fn = CHECKS[sys.argv[1]]
    ok, why = fn()
    print("%s-%s %s" % (token, "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
