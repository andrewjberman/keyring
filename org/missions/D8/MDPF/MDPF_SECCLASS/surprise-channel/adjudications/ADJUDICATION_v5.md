# MDPF_SECCLASS -- FAST interval L8/L9 adjudication (rows S6, S7, S8)

<sweep_watermark>2026-10-02T02:10Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-02 ~02:1xZ. No drain-end packet: the project is FAST since 2026-10-01T05:39Z and its gate reads 0 open orders of 21. The investigation file at HEAD holds 38 rows, the last S8 (surfaced 2026-10-01T11:10Z, commit aee59866b7); no row was added after it. 3 undispositioned rows: 1 dismissed by the row below (S6, into the graduated row W10-S3), 2 graduated in remediations/REMEDIATION_v5.md (S7 ARMED, S8 INERT). Carried unchanged: every row of REMEDIATION_v1 to v4 that is not closed.

```json
[
  {
    "id": "MDPF_SECCLASS-C-S12",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-02T02:10:00Z",
    "one_line": "S6 is the cause split of the hazard already graduated as W10-S3 (OPEN, owner 1.0.0_SA_CTO, REMEDIATION_v4): the same seven failing tests of .tools/test_safe_deploy.py, now traced to the 2026-08-30 index-blob change. It adds evidence, not a second hazard.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-S6"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; one hazard is carried on one remediation row.",
    "world_is": "The test file still reads 7 failed, 7 passed at CLOUD HEAD, the same seven names S6 lists. The failure cause depends on where the copy runs: in this seat's scratch copy all seven raise TypeError 'Strings must be encoded before hashing', where S6's copy split them four INDEX_MISSING and three TypeError. The tool changed again after S6 was written (47e510a186, 2026-10-01 13:20Z, a shipped-files entry) and the seven stayed red, so S6's own un-park condition ('the tool next changes') passed once without a repair.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show HEAD:.tools/safe_deploy_core.py and HEAD:.tools/test_safe_deploy.py into one scratch folder, python -m pytest (this seat, 2026-10-02 02:0xZ): 7 failed, 7 passed; failing: test_pass_gold_deploy, test_fail_nodeploy, test_fail_partial, test_fail_sha_mismatch, test_serve_release_authorized_with_ack, test_author_enumeration_notice, test_no_regression_clean_deploy",
        "git log --since 2026-10-01 on .tools/safe_deploy_core.py and .tools/test_safe_deploy.py: one commit, 47e510a186 (2.0.0_SA_COO~M), safe_deploy_core.py +16 lines; the test file unchanged",
        "remediations/REMEDIATION_v4.md row MDPF_SECCLASS-W10-S3: OPEN, owner 1.0.0_SA_CTO, remedy 'the owner of .tools/safe_deploy_core.py repairs or retires the seven failing cases ... placement is the CTO's'",
        "investigation row MDPF_SECCLASS-S6 (2.0.0_SA_COO~M), notes: 'supersedes the count-only row MDPF_SECCLASS-W10-S3'"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Duplicate of the graduated, open row MDPF_SECCLASS-W10-S3. Its new facts (origin 3d9eb2931d of 2026-08-30; the tool changed at 47e510a186 with the seven still red) belong to W10-S3's owner, 1.0.0_SA_CTO, who places the repair."
  }
]
```
