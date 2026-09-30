"""R24 ~Y cell IB-yr-241 check: a correction-bearing status offers CORRECT with WORDS, from an enumerated mapping.

Why (walk-2 W2-06, CTO 103026: "~Y: ... W2-06 correction words on the status wire"). The page has nothing to show:
`ProspectJobStatus.tsx:61-76` renders the state word plus `publicReasonCode`, and `OwnedRequestHistory.tsx:110` adds
"Open it to see what to change" to every non-READY row because nothing on the wire says WHAT to change.

The wire already has the home, so this cell adds NO field and changes NO contract (decomp R24 amendment 2):
`StatusEnvelope.schema.json` is `additionalProperties: false`, and `public_reason_code` is documented as "a code,
never a message" -- `build_envelope` enforces that itself. But `actions[]` items are `{action, safe, description}`,
all required, the `action` enum already contains `CORRECT`, and `description` is documented as "what the action does".
So a correction-bearing state offers `{"action": "CORRECT", "safe": true, "description": "<the words>"}`.

The words come from an ENUMERATED server-side mapping keyed by the public reason code -- never free text, never an
exception body. One mapping is load-bearing and measured: `RESOLVE_RETRY_EXHAUSTED` must NOT advise replacing the
file, because rows IRPT_BCKEND-S206 and IRPT_BCKEND-S215 measured that the file is not the cause (the same upload
normalized in 1 s solo and exhausted in 203 s while another generation was in flight).

Run from the repo root:
    python -m pytest -q -p no:cacheprovider org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/R24_CHECKS/test_r24_y1_correction_words.py::<test>

- offers_correct_with_words:  a NEEDS_CORRECTION envelope carries a CORRECT action with a non-empty description.
                              FAILS at the base -- today nothing adds one.
- retry_exhausted_words_do_not_blame_the_file: that description must not advise replacing/re-uploading the file
                              (S206/S215). FAILS at the base for want of any words at all.
- contract_unchanged:         CONTROL. The envelope still has exactly the contract's 7 properties, still validates,
                              and `public_reason_code` still refuses a message. PASSES at the base and must keep
                              passing -- a cell that changed the contract fails its own control.
"""
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[6]
IR = ROOT / "infra/aws/lambda/investor-reporting"
OPS = IR / "ops"
CONTRACTS = IR / "_contracts"
# ops/status.py's package pulls prospect_dates -> submission, which lives in the generate tree; the
# lambda bundles them side by side, so the check puts the same siblings on the path.
sys.path[:0] = [str(OPS), str(IR / "ycharts/generate"), str(IR / "_scope"), str(IR / "_authz"), str(IR / "intake")]

import status as ops_status  # noqa: E402

CORRECTION_STATE = "NEEDS_CORRECTION"
# the code W22/W24 actually served on a stopped normalization, three times
RETRY_EXHAUSTED = "RESOLVE_RETRY_EXHAUSTED"


def _envelope(reason_code, state=CORRECTION_STATE, actions=None):
    return ops_status.build_envelope(
        "analysis-status", "read", "REQ-" + "a" * 24, state, "2026-09-29",
        actions=actions, public_reason_code=reason_code)


def _correct_actions(env):
    return [a for a in env.get("actions", []) if a.get("action") == "CORRECT"]


def test_offers_correct_with_words():
    """A correction-bearing state offers CORRECT, and its description is not empty."""
    env = _envelope(RETRY_EXHAUSTED)
    got = _correct_actions(env)
    assert got, ("a %s envelope with reason %s offered no CORRECT action, so the page has nothing to show and falls "
                 "back to 'Open it to see what to change'. actions were: %r"
                 % (CORRECTION_STATE, RETRY_EXHAUSTED, env.get("actions")))
    assert got[0].get("safe") is True, "the offered action must be safe: %r" % got[0]
    words = (got[0].get("description") or "").strip()
    assert len(words) >= 10, "the CORRECT action must carry WORDS, not an empty description: %r" % got[0]


def test_retry_exhausted_words_do_not_blame_the_file():
    """RESOLVE_RETRY_EXHAUSTED must not advise replacing the file -- S206/S215 measured that as the wrong remedy."""
    env = _envelope(RETRY_EXHAUSTED)
    got = _correct_actions(env)
    assert got, "no CORRECT action to inspect; see test_offers_correct_with_words"
    words = (got[0].get("description") or "").lower()
    for blamed in ("replace the file", "replace your file", "re-upload", "reupload", "upload a different",
                   "fix the file", "correct the file"):
        assert blamed not in words, (
            "the words for %s advise %r, but rows IRPT_BCKEND-S206 and S215 measured the file is NOT the cause: the "
            "same upload normalized in 1 s solo and exhausted in 203 s while another generation was in flight. "
            "words were: %r" % (RETRY_EXHAUSTED, blamed, got[0].get("description")))


def test_contract_unchanged():
    """CONTROL: the envelope keeps exactly the contract's shape, and a message is still refused as a reason code."""
    schema = json.loads((CONTRACTS / "StatusEnvelope.schema.json").read_text(encoding="utf-8"))
    expected = set(schema["properties"])
    assert schema.get("additionalProperties") is False, "the contract stopped being closed"

    env = _envelope(RETRY_EXHAUSTED)
    assert set(env) <= expected, "the envelope grew a key the contract forbids: %r" % (set(env) - expected)
    for req in schema["required"]:
        assert req in env, "required property %r is missing" % req

    # every action still matches the contract's closed item shape
    for a in env.get("actions", []):
        assert set(a) == {"action", "safe", "description"}, "action item shape changed: %r" % a
        assert a["action"] in ops_status.ACTIONS, "action outside the enum: %r" % a

    # "a code, never a message" still holds
    with pytest.raises(ops_status.EnvelopeRefused):
        _envelope("this is a sentence, not a code")
