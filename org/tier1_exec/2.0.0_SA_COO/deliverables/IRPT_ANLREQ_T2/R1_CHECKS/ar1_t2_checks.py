"""IRPT_ANLREQ round 1, workstream ~T (commentary) -- the issuer's mechanical checks (2.0.0_SA_COO~T2).

  t11   AR11-t-AC1  the I3 test file passes and holds, by name: a READY queue message rebuilt byte-equal is admitted and becomes ONE
                    entry record; a malformed or extra-field message is refused; commentary.tf subscribes the commentary Lambda to the
                    analysis_ready queue (batch size 1) by builder name
  t12   AR12-t-AC1  the composition-port test file passes and holds, by name: the live port invokes IRPT's read Lambda with
                    {tenant, request_ref} only; owner is never read; a persisted DRAFT is followed by exactly one commentary_ready message;
                    and commentary.tf no longer holds DecryptWithTheIrptKey
  t13   AR13-t-AC1  the IRPT store test file passes and holds, by name, the CTO ruling's four refusals (ca645f8410): another
                    service subject, another family, a second put on the same request_id, a body-supplied tenant

Prints <TOKEN>-OK or <TOKEN>-FAIL <reason> and exits 0 / 1. Run from the repo root (or the worker's worktree root).
"""
import re
import subprocess
import sys
from pathlib import Path

TF = Path("infra/aws/terraform/transcripts/commentary.tf")
SPEC = {
    "t11": (Path("data/transcripts/scripts/tests/test_commentary_ready_queue.py"),
            ["test_ready_message_admitted_once", "test_malformed_or_extra_field_refused", "test_tf_subscribes_lambda_to_ready_queue"]),
    "t13": (Path("infra/aws/lambda/investor-reporting/reports/tests/test_commentary_draft_store.py"),
            ["test_other_service_subject_refused", "test_other_family_refused", "test_second_put_same_request_refused",
             "test_body_tenant_ignored"]),
    "t12": (Path("data/transcripts/scripts/tests/test_commentary_composition_port.py"),
            ["test_live_port_invokes_irpt_reader_with_tenant_and_request_ref", "test_owner_never_read",
             "test_draft_persisted_then_one_commentary_ready"]),
}


def _run(key):
    test, names = SPEC[key]
    if not test.exists():
        return False, "absent: %s" % test.as_posix()
    text = test.read_text(encoding="utf-8")
    missing = [n for n in names if "def %s(" % n not in text]
    if missing:
        return False, "missing %s" % ", ".join(missing)
    if key == "t12" and "DecryptWithTheIrptKey" in TF.read_text(encoding="utf-8"):
        return False, "commentary.tf still holds DecryptWithTheIrptKey"
    r = subprocess.run([sys.executable, "-m", "pytest", str(test), "-q", "-p", "no:cacheprovider"],
                       capture_output=True, text=True, timeout=110)
    tail = re.sub(r"\x1b\[[0-9;]*m", "", ([ln for ln in (r.stdout + r.stderr).splitlines() if ln.strip()] or [""])[-1])
    passed = int((re.search(r"(\d+) passed", tail) or [0, 0])[1])
    return (r.returncode == 0 and passed >= len(names)), tail


TOKENS = {"t11": "AR1-T11", "t12": "AR1-T12", "t13": "AR1-T13"}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in SPEC:
        print("usage: ar1_t2_checks.py {%s}" % "|".join(SPEC))
        sys.exit(2)
    ok, why = _run(sys.argv[1])
    print("%s-%s %s" % (TOKENS[sys.argv[1]], "OK" if ok else "FAIL", why))
    sys.exit(0 if ok else 1)
