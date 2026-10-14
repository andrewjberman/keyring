#!/usr/bin/env python3
"""test_unblock_owed_call_foreign.py -- `unblock.py tick --owed-call` reads a FOREIGN box's open call through the freshest
source (NFRA_CTLPLN CT-ac-6, routed from NFRA_DEVPLN round-7 analysis section 2; the reader is open-calls.py approval_read,
NFRA_DEVPLN DP-e-2). Standard library only; temporary directories only; no network; no real git ref.

Seams: AGENTBUS_DEVICE pins this box to `laptop`; OPAL_STATE_ROOT holds the working-tree copies (<state>/<box>/open_calls.json);
OPAL_CLOUD_READ_LOCAL holds the cluster copy (<seam>/box=<box>/open_calls.json) and origin/box/<box> (<seam>/git=<box>/...).

    python .tools/tests/test_unblock_owed_call_foreign.py      LAST line  UNBLOCK-OWED-FOREIGN cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
FOREIGN = "dell2"
FOREIGN_CALL = "dell2-20261013T221411Z-3635"
OWN_CALL = "laptop-20261013T221411Z-0001"
THIS_BOX = "laptop"
SERIAL = "2.0.0_SA_COO~C"
PROJECT = "NFRA_CTLPLN"


def load_unblock():
    spec = importlib.util.spec_from_file_location("unblock_owed_call_under_test", os.path.join(ROOT, ".tools", "unblock.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def list_doc(box: str, written_at: str, rows: list) -> dict:
    return {"schema": "open-calls/1", "device": box, "written_at": written_at, "written_by": "test", "rows": rows}


def call_row(call_id: str, state: str) -> dict:
    """A row in the open-calls/1 schema. The schema's states are OPEN and CLOSED only (open-calls.py STATES; validate_doc refuses
    any other). A call HELD for Andrew is an OPEN row carrying escalation.to=andrew, so state "HELD" is written as that."""
    row = {"id": call_id, "project": PROJECT, "subject": "test call", "asked_by": "test", "source": "test",
           "state": "OPEN" if state == "HELD" else state, "opened_at": "2026-10-13T22:14:11Z", "scope": {}}
    if state == "HELD":
        row["escalation"] = {"to": "andrew", "ref": None, "at": "2026-10-13T22:20:00Z", "by": "test", "reason": "test hold"}
    if state == "CLOSED":
        row["closed"] = {"at": "2026-10-13T22:40:00Z", "by": "andrew"}
    return row


def put(path: str, payload) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        if isinstance(payload, str):
            fh.write(payload)
        else:
            json.dump(payload, fh)


def pinned_env(base: str) -> dict:
    return {
        "AGENTBUS_DEVICE": THIS_BOX,
        "OPAL_STATE_ROOT": os.path.join(base, "state"),
        "OPAL_CLOUD_READ_LOCAL": os.path.join(base, "seam"),
        "OPAL_OPEN_CALLS_STATE_ROOT": os.path.join(base, "own"),
        "OPAL_XADJ_LOCAL": os.path.join(base, "xadj"),
        "OPAL_UNBLOCK_TICKS": os.path.join(base, "ticks"),
        "OPAL_UNBLOCK_RECORD_ROOT": os.path.join(base, "rec"),
    }


def run_tick(unblock, call_id: str) -> str:
    """The one OWED-CALL line the tick printed (the verdict is read from the line, never from a return value)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
        unblock.main(["tick", "--serial", SERIAL, "--project", PROJECT, "--result", "nothing", "--owed-call", call_id])
    lines = [ln for ln in buf.getvalue().splitlines() if ln.startswith("OWED-CALL:")]
    return lines[-1] if lines else "<no OWED-CALL line>"


def case(unblock, name: str, call_id: str, expect: str, arrange) -> bool:
    """Arrange the copies in a fresh temporary tree, run one tick under the pinned seams, compare the OWED-CALL line."""
    keep = {}
    with tempfile.TemporaryDirectory(prefix="owed_call_foreign_") as base:
        env = pinned_env(base)
        for k, v in env.items():
            keep[k] = os.environ.get(k)
            os.environ[k] = v
        try:
            arrange(base)
            got = run_tick(unblock, call_id)
        finally:
            for k, v in keep.items():
                if v is None:
                    os.environ.pop(k, None)
                else:
                    os.environ[k] = v
    ok = got == expect
    print("%s %s" % ("PASS" if ok else "FAIL", name))
    if not ok:
        print("     expected: %s" % expect)
        print("          got: %s" % got)
    return ok


def arrange_freshest_only(state_row: str):
    def arrange(base: str) -> None:
        # working tree stale and lacking the row; the git copy older still; the cluster copy newest and holding it
        put(os.path.join(base, "state", FOREIGN, "open_calls.json"), list_doc(FOREIGN, "2026-10-13T20:00:00Z", []))
        put(os.path.join(base, "seam", "git=%s" % FOREIGN, "open_calls.json"),
            list_doc(FOREIGN, "2026-10-13T21:00:00Z", []))
        put(os.path.join(base, "seam", "box=%s" % FOREIGN, "open_calls.json"),
            list_doc(FOREIGN, "2026-10-13T22:30:00Z", [call_row(FOREIGN_CALL, state_row)]))
    return arrange


def arrange_unreadable(base: str) -> None:
    # the working-tree copy is present but not JSON; the cluster and git copies are absent: no readable source
    put(os.path.join(base, "state", FOREIGN, "open_calls.json"), "{not json")


def arrange_own_box(base: str) -> None:
    # this box's own call reads the working tree as before; the cluster copy of this box is newer and says CLOSED, and is ignored
    put(os.path.join(base, "own", THIS_BOX, "open_calls.json"),
        list_doc(THIS_BOX, "2026-10-13T20:00:00Z", [call_row(OWN_CALL, "OPEN")]))
    put(os.path.join(base, "seam", "box=%s" % THIS_BOX, "open_calls.json"),
        list_doc(THIS_BOX, "2026-10-13T23:00:00Z", [call_row(OWN_CALL, "CLOSED")]))


def arrange_working_tree_newer(base: str) -> None:
    # the working-tree copy is the newest and holds the row OPEN; the cluster copy is older and says CLOSED
    put(os.path.join(base, "state", FOREIGN, "open_calls.json"),
        list_doc(FOREIGN, "2026-10-13T23:10:00Z", [call_row(FOREIGN_CALL, "OPEN")]))
    put(os.path.join(base, "seam", "box=%s" % FOREIGN, "open_calls.json"),
        list_doc(FOREIGN, "2026-10-13T22:30:00Z", [call_row(FOREIGN_CALL, "CLOSED")]))


def main() -> int:
    unblock = load_unblock()
    results = [
        case(unblock, "a-foreign-open-only-in-freshest-source-waits-with-source-named", FOREIGN_CALL,
             "OWED-CALL: id=%s counts=WAITING state=OPEN source=cluster" % FOREIGN_CALL,
             arrange_freshest_only("OPEN")),
        case(unblock, "b-foreign-held-for-andrew-in-freshest-source-waits", FOREIGN_CALL,
             "OWED-CALL: id=%s counts=WAITING state=OPEN source=cluster" % FOREIGN_CALL,
             arrange_freshest_only("HELD")),
        case(unblock, "c-foreign-closed-in-freshest-source-counts-empty", FOREIGN_CALL,
             "OWED-CALL: id=%s counts=EMPTY reason=call-closed source=cluster" % FOREIGN_CALL,
             arrange_freshest_only("CLOSED")),
        case(unblock, "d-foreign-no-readable-source-counts-empty-unreadable", FOREIGN_CALL,
             "OWED-CALL: id=%s counts=EMPTY reason=call-unreadable" % FOREIGN_CALL,
             arrange_unreadable),
        case(unblock, "e-own-box-call-still-reads-the-working-tree", OWN_CALL,
             "OWED-CALL: id=%s counts=WAITING state=OPEN source=own" % OWN_CALL,
             arrange_own_box),
        case(unblock, "f-working-tree-newer-than-cluster-wins", FOREIGN_CALL,
             "OWED-CALL: id=%s counts=WAITING state=OPEN source=working-tree" % FOREIGN_CALL,
             arrange_working_tree_newer),
    ]
    k, n = sum(results), len(results)
    ok = all(results)
    print("UNBLOCK-OWED-FOREIGN cases=%d/%d ok=%s" % (k, n, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
