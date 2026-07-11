"""NFRA_TOOLPASS: comp-tagauthz is EXEMPLARY (prints the swept denominator, names its gaps,
advisory-vs-verdict explicit). The load-bearing branch is the exit-2 COLLISION VERDICT -- it must
BITE on a real endangered managed resource and stay clean otherwise. There was NO committed test of
that path; this adds it (CTO front-pass directive). Deterministic + synthetic -- mocks the aws calls
(no IAM/EC2 hit), so it is bd-safe and hermetic.

Verdict logic (cmd_check): a candidate is DANGER (rc=2) iff it carries a tag whose KEY is in the
tree's default_tags AND that (key,value) grants authorization (key in authz and value in authz[key]).

# rail-checked: assurance oracle for comp-tagauthz under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib.util
import io
import os
from contextlib import redirect_stdout
from types import SimpleNamespace

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_TOOL = os.path.join(_WS, ".tools", "comp-tagauthz.py")

_spec = importlib.util.spec_from_file_location("comp_tagauthz", _TOOL)
ta = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ta)


def _verdict(instance_tags: dict):
    """Run cmd_check with all aws-touching helpers mocked; return (rc, stdout)."""
    saved = (ta.sh, ta.collect_conditions, ta.banner, ta.is_ours, ta.default_tag_keys, ta.ec2_tagged)
    ta.sh = lambda cmd: "{}"
    # one customer-managed (ours) policy whose Condition ties access to tag System=CottonwoodPipeline
    ta.collect_conditions = lambda aad: [{"source": "customer/MyAuthPolicy",
                                          "pairs": {"System": ["CottonwoodPipeline"]}}]
    ta.banner = lambda *a, **k: None
    ta.is_ours = lambda source: True
    ta.default_tag_keys = lambda tree: (["System", "Project"], True)   # System collides with the authz key
    ta.ec2_tagged = lambda: [{"id": "i-TEST", "state": "stopped", "tags": instance_tags}]
    args = SimpleNamespace(candidate=["i-TEST"], default_tags_tree="synthetic-tree",
                           from_state=False, from_plan=None)
    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            rc = ta.cmd_check(args)
    finally:
        (ta.sh, ta.collect_conditions, ta.banner, ta.is_ours, ta.default_tag_keys, ta.ec2_tagged) = saved
    return rc, buf.getvalue()


def test_exit2_verdict_bites_on_endangered_candidate():
    # candidate tag-authorized on the colliding key (System) -> tree's default_tags would overwrite -> rc=2
    rc, out = _verdict({"System": "CottonwoodPipeline"})
    assert rc == 2, f"exit-2 COLLISION verdict MUST fire on an endangered managed candidate; got rc={rc}\n{out}"
    assert "WOULD OVERWRITE" in out or "MUST NOT apply" in out, f"verdict output missing: {out!r}"


def test_verdict_clean_when_candidate_not_tag_authorized():
    # same colliding key, but the candidate's value is NOT an authz value -> not endangered -> rc=0
    rc, out = _verdict({"System": "SomethingUnauthorized"})
    assert rc == 0, f"a non-tag-authorized candidate must be CLEAN rc=0; got rc={rc}\n{out}"


if __name__ == "__main__":
    rc_bad, _ = _verdict({"System": "CottonwoodPipeline"})
    rc_ok, _ = _verdict({"System": "SomethingUnauthorized"})
    print(f"[endangered candidate]     rc={rc_bad} (expect 2)")
    print(f"[not-tag-authorized]       rc={rc_ok} (expect 0)")
    test_exit2_verdict_bites_on_endangered_candidate()
    test_verdict_clean_when_candidate_not_tag_authorized()
    print("=== comp-tagauthz exit-2 verdict: BITES on danger, CLEAN otherwise -- ALL PASS ===")
