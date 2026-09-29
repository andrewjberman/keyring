"""R22 ~Y cell IB-yr-221 check: a resolve_upload RETRY never reaches the DLQ (CTO condition 102655, ~P 102659).

The live irpt-generation RedrivePolicy is maxReceiveCount 5 (infra core/sqs.tf:42). With the 60 s RETRY re-offer
(IB-yr-211), a resolve that keeps failing would be dead-lettered after about 5 minutes, leaving its NORMALIZATION row
RESOLVING and its message stuck in the DLQ. The bound: on a RETRY whose ApproximateReceiveCount has reached
RESOLVE_MAX_RECEIVES (below 5), poll_once gives up on THAT message by name: it deletes it and prints
'IRPT_RESIDENT_RESOLVE state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED', and the NORMALIZATION row ends in its existing
terminal NEEDS_CORRECTION state with reason RESOLVE_RETRY_EXHAUSTED (amendment 1: the job ends, the redrive stops).

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R22_CHECKS/test_r22_y1_resolve_bounded.py::<test>

- fourth:     (amendment 1, CTO 102688) receive count RESOLVE_MAX_RECEIVES plus a provider outage deletes the message,
              prints 'state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED', and moves the row to NEEDS_CORRECTION with that
              reason, so the client's redrive stops. Superseded the first form (GAVE_UP, row left RESOLVING).
- asks_count: poll_once asks SQS for ApproximateReceiveCount on every receive. At the base it does not.
- early:      the control. Receive count 1 plus an outage keeps the message with the 60 s re-offer (IB-yr-211, unchanged).
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


class CountedQueue(base.Queue):
    """The suite's Queue, plus SQS's ApproximateReceiveCount attribute and a record of what poll_once asked for."""
    def __init__(self, bodies, receive_count):
        super().__init__(bodies)
        self.receive_count, self.visibility, self.asked = receive_count, [], []

    def receive_message(self, **kw):
        self.asked.append(kw.get("AttributeNames") or kw.get("MessageSystemAttributeNames") or [])
        got = super().receive_message(**kw)
        for m in got.get("Messages", []):
            m["Attributes"] = {"ApproximateReceiveCount": str(self.receive_count)}
        return got

    def change_message_visibility(self, **kw):
        super().change_message_visibility(**kw)
        self.visibility.append(kw["VisibilityTimeout"])


def _outage(case, count):
    deferred.post(case, deferred.payload())
    _, _, _, _, calls, _, _, resolver = broker_world.world({"status": 503, "body": []})
    sent = list(case.sent)
    queue = CountedQueue(case.sent, count)
    poll_once(sqs=queue, queue_url="offline-queue", assembly=base.assembly(case, resolver))
    return queue, sent[0]


def _row_state(case, message):
    """The NORMALIZATION row's state, read as the resident reads it (tenant, upload, revision from the message)."""
    import json
    from upload_resolution import normalization_key, read_resolution_message
    tenant, upload_id, revision = read_resolution_message(json.loads(message))
    row = case.service.artifacts.index.get(tenant, normalization_key(upload_id, revision))
    return None if row is None else row.get("state")


def _row(case, message):
    import json
    from upload_resolution import normalization_key, read_resolution_message
    tenant, upload_id, revision = read_resolution_message(json.loads(message))
    return case.service.artifacts.index.get(tenant, normalization_key(upload_id, revision))


def test_fourth_retry_ends_attention_by_name(case, capsys):
    """Amendment 1 (CTO 102688 on CRO 102684): the bound ENDS the job. The row leaves RESOLVING for the
    existing terminal NEEDS_CORRECTION with reason RESOLVE_RETRY_EXHAUSTED, so the client's redrive stops."""
    limit = getattr(resident_worker, "RESOLVE_MAX_RECEIVES", None)
    assert limit is not None and 1 < limit < 5
    queue, message = _outage(case, limit)
    out = capsys.readouterr().out
    assert queue.deleted == ["rh-1"]
    assert "IRPT_RESIDENT_RESOLVE state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED" in out
    row = _row(case, message)
    assert row is not None and row.get("state") == "NEEDS_CORRECTION"
    assert row.get("reason") == "RESOLVE_RETRY_EXHAUSTED"
    assert [f.get("code") for f in row.get("findings") or []] == ["RESOLVE_RETRY_EXHAUSTED"]


def test_asks_sqs_for_the_receive_count(case):
    queue, _ = _outage(case, 1)
    assert queue.asked and all("ApproximateReceiveCount" in (a or []) or "All" in (a or []) for a in queue.asked)


def test_early_retry_is_kept_and_reoffered(case):
    queue, message = _outage(case, 1)
    assert _row_state(case, message) == "RESOLVING"
    assert queue.deleted == [] and len(queue.bodies) == 1
    assert queue.visibility and queue.visibility[-1] == resident_worker.RESOLVE_RETRY_VISIBILITY_S
