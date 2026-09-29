"""R20 ~Y cell IB-yr-202 check: a resolve_upload RETRY is logged with its code and re-offered soon, not after the
900 s generation lease (row S193: window 21's Y4 upload resolved exactly 15 min late).

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R20_CHECKS/test_r20_y2_resolve_retry.py::<test>

- retry:   a provider outage (503) on resolve keeps the message, and the LAST visibility change poll_once makes for it
           is resident_worker.RESOLVE_RETRY_VISIBILITY_S, at most 120 s. The same run prints one line
           'IRPT_RESIDENT_RESOLVE state=RETRY code=<code>'. At the base the message keeps the 900 s lease and nothing
           is printed.
- ready:   a resolve that succeeds still deletes its message (the suite's own success test, re-run) AND prints
           'IRPT_RESIDENT_RESOLVE state=READY'. At the base the delete holds and the line is missing.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
GEN = ROOT / "infra/aws/lambda/investor-reporting/ycharts/generate"
sys.path[:0] = [str(GEN / "tests"), str(GEN)]

import test_resident_worker  # noqa: E402,F401  (first: it sets the suite's sys.path)
import test_resolve_upload as base  # noqa: E402  (the resolve fixtures and Queue fake)
import resident_worker  # noqa: E402
from resident_worker import poll_once  # noqa: E402

case = base.case
deferred, broker_world = base.deferred, base.broker_world


class VisibilityQueue(base.Queue):
    def __init__(self, bodies):
        super().__init__(bodies)
        self.visibility = []

    def change_message_visibility(self, **kw):
        super().change_message_visibility(**kw)
        self.visibility.append(kw["VisibilityTimeout"])


def test_retry_is_logged_and_reoffered_soon(case, capsys):
    deferred.post(case, deferred.payload())
    _, _, _, _, calls, _, _, resolver = broker_world.world({"status": 503, "body": []})
    queue = VisibilityQueue(case.sent)
    poll_once(sqs=queue, queue_url="offline-queue", assembly=base.assembly(case, resolver))
    out = capsys.readouterr().out
    assert queue.deleted == [] and len(queue.bodies) == 1 and len(calls) == 1
    short = getattr(resident_worker, "RESOLVE_RETRY_VISIBILITY_S", None)
    assert short is not None and short <= 120
    assert queue.visibility and queue.visibility[-1] == short
    assert [line for line in out.splitlines() if line.startswith("IRPT_RESIDENT_RESOLVE state=RETRY code=")]


def test_ready_still_deletes_and_is_logged(case, capsys):
    base.test_poll_resolves_deletes_and_the_next_post_reads_normalized(case)  # asserts the delete itself
    assert "IRPT_RESIDENT_RESOLVE state=READY" in capsys.readouterr().out
