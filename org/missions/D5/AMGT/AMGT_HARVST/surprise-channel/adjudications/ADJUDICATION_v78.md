# AMGT_HARVST -- Z-S118 disposition (dell1)

<sweep_watermark>2026-10-13T19:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T19:45:00Z. Asked by 2.0.0_SA_COO~W1 msg 5122. Z-S118 dismissed: an instrument defect, fixed without weakening the check. Round 84 not terminal (bz-7 issued): no slug.

```json
[
  {
    "id": "AMGT_HARVST-D1-C-S39",
    "project": "AMGT_HARVST",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-13T19:45:00Z",
    "one_line": "Z-S118 (BLOCKING, INERT) dismissed: the failure was the GRADING INSTRUMENT's, not the world's. bz-6's AC1/AC2 ran deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py by path, which puts the script's directory (never the repo root) on sys.path[0], so its 'from lib.opal_data_harvest' import raised. This seat reproduced it on dell1: the by-path form prints ModuleNotFoundError: No module named 'lib.opal_data_harvest'. The issuer's amendment @f11e5a062f changes ONLY the two invocations (python -c + runpy.run_path of the same path, run_name __main__); the two <expect> strings are byte-equal before and after (this seat's diff), and the script is unedited by it (its last edit 154e2ff047 precedes the amendment), so what is checked did not weaken. ~ZW's re-run @53aa581851 on site Z: AC1 'STATE wsj present=True subscriber=True network_auth_corroborated=True ... VALID=True' rc 0; AC2 the same for barrons; NEGATIVE CONTROL against C:/nonexistent-runtime-root-bz6-control reads VALID=False for both. The amended form on dell1 against a nonexistent root reads VALID=False rc 0 on this seat's run. GATE LIMB: the amendment commit says the commit-time to-pipeline-gate graded it; that gate's LIMB 6 does not fire on a modification (only GATE viii, placeholders, which this order does not declare), so in substance NO limb graded the amendment's content; this seat's diff is the read. NOT PROVED: that the sessions survive a cycle; bz-7 reads that, and bz-7 is still issued, so round 84 is not terminal and no slug is sent.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_HARVST-Z-S118"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and an issuer's amendment of its own criteria states which gate limb graded it.",
    "world_is": "Z-S118 (BLOCKING, INERT) dismissed: the failure was the GRADING INSTRUMENT's, not the world's. bz-6's AC1/AC2 ran deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py by path, which puts the script's directory (never the repo root) on sys.path[0], so its 'from lib.opal_data_harvest' import raised. This seat reproduced it on dell1: the by-path form prints ModuleNotFoundError: No module named 'lib.opal_data_harvest'. The issuer's amendment @f11e5a062f changes ONLY the two invocations (python -c + runpy.run_path of the same path, run_name __main__); the two <expect> strings are byte-equal before and after (this seat's diff), and the script is unedited by it (its last edit 154e2ff047 precedes the amendment), so what is checked did not weaken. ~ZW's re-run @53aa581851 on site Z: AC1 'STATE wsj present=True subscriber=True network_auth_corroborated=True ... VALID=True' rc 0; AC2 the same for barrons; NEGATIVE CONTROL against C:/nonexistent-runtime-root-bz6-control reads VALID=False for both. The amended form on dell1 against a nonexistent root reads VALID=False rc 0 on this seat's run. GATE LIMB: the amendment commit says the commit-time to-pipeline-gate graded it; that gate's LIMB 6 does not fire on a modification (only GATE viii, placeholders, which this order does not declare), so in substance NO limb graded the amendment's content; this seat's diff is the read. NOT PROVED: that the sessions survive a cycle; bz-7 reads that, and bz-7 is still issued, so round 84 is not terminal and no slug is sent.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show f11e5a062f (order AMGT_HARVST.TO-HVST-bz-6 AC1/AC2 invocations only; expects byte-equal)",
        "deliverables/0.7.0_AE_CloudOps~ZW/round84/bz6_ac1_wsj_runpy.out, bz6_ac2_barrons_runpy.out, bz6_negative_control_runpy.out (@53aa581851)",
        "3.0.0_SA_CVO on dell1: by-path form ModuleNotFoundError; amended form vs a nonexistent root VALID=False rc 0",
        "order AMGT_HARVST.TO-HVST-bz-7 <status>issued</status> at HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S118 (BLOCKING, INERT) dismissed: the failure was the GRADING INSTRUMENT's, not the world's. bz-6's AC1/AC2 ran deliverables/2.0.0_SA_COO_W1/round84/bz6_session_state.py by path, which puts the script's directory (never the repo root) on sys.path[0], so its 'from lib.opal_data_harvest' import raised. This seat reproduced it on dell1: the by-path form prints ModuleNotFoundError: No module named 'lib.opal_data_harvest'. The issuer's amendment @f11e5a062f changes ONLY the two invocations (python -c + runpy.run_path of the same path, run_name __main__); the two <expect> strings are byte-equal before and after (this seat's diff), and the script is unedited by it (its last edit 154e2ff047 precedes the amendment), so what is checked did not weaken. ~ZW's re-run @53aa581851 on site Z: AC1 'STATE wsj present=True subscriber=True network_auth_corroborated=True ... VALID=True' rc 0; AC2 the same for barrons; NEGATIVE CONTROL against C:/nonexistent-runtime-root-bz6-control reads VALID=False for both. The amended form on dell1 against a nonexistent root reads VALID=False rc 0 on this seat's run. GATE LIMB: the amendment commit says the commit-time to-pipeline-gate graded it; that gate's LIMB 6 does not fire on a modification (only GATE viii, placeholders, which this order does not declare), so in substance NO limb graded the amendment's content; this seat's diff is the read. NOT PROVED: that the sessions survive a cycle; bz-7 reads that, and bz-7 is still issued, so round 84 is not terminal and no slug is sent."
  }
]
```
