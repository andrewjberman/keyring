# NFRA_OPLGTW -- adjudication v11 (site Z): round 19's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T05:55:00Z. Trigger: `2.0.0_SA_COO~O` msg 29923 (round 19 TERMINAL, 2 of 2:
OG-rl-7 under R22 and OG-ts-2; r19b `cf4b036e62` LIVE at 05:31:52Z; last commit 40fa4f6d8e).

**Terminality.** Both round-19 orders are complete per the issuer. Round 19 carries no judgment criterion, so this round
has no L9 grade.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 355 investigation items, 30 adjudication rows, 76
remediation rows. 6 rows read OPEN and 1 reads ARMED (Z-W13-S5, standing). The issuer's Z-S56 already resolves Z-W15-S52,
S53, S57 and S59. This file adjudicates the 6:
- **DISMISSED_WITH_REASON (5), C-S31:** Z-W15-S54, Z-W15-S55, Z-W15-S56, Z-W15-S60, Z-W25-S4.
- **GRADUATED (1), C-S32:** Z-W15-S58 (a flaky test that makes every baseline comparison ambiguous).
- **C-S33** records the r19b never-widen guards V1-V3 read on the deployed host, and the in-place advances of Z-W22-S10
  and Z-W25-S3.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S31",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T05:55:00Z",
    "one_line": "Round 19 L8: 5 INERT rows are DISMISSED_WITH_REASON -- a docstring-only file this seat AST-checked, a stale test ts-2 fixed, a vacuous pre-act anchor the pre-GO exercise caught, the V2 record this seat compared, and a lane block ts-2's A1 resolved.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W15-S54: envelope.py's release diff is docstring-only; this seat's ast.dump comparison (docstrings stripped) reads equal for both r19 and r19b. Z-W15-S55: test_schwab_host_inputs.py's build_package pairing failure on the release tree; ts-2 (ba9a6db154) aligned the file, and this seat ran it on CLOUD: 9 passed. Z-W15-S56: rl7.AC1 anchored to the manifest, which is vacuous before the act; the issuer named it in Phase A, so the pre-GO exercise (RELEASE_ORDER_FORM step 7, the remedy of REMEDIATED Z-W15-S51) caught it before GO, as designed. Z-W15-S60: V2's arm lived in a separate recorder, not in r19b_verify.sh; this seat compared r19b_phaseB_login_before.out with r19b_phaseB_login_after.out, 23 normalised lines, equal except the SSM command id, with the non-configured verified identity reaching consent (307) on both, exactly as live. Z-W25-S4: the ts-2 re-hand could not commit against a complete order; ts-2 A1 landed it (ea7ebece14, tests/proc_tmp_root.py on CLOUD).",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W15-S54",
      "NFRA_OPLGTW-Z-W15-S55",
      "NFRA_OPLGTW-Z-W15-S56",
      "NFRA_OPLGTW-Z-W15-S60",
      "NFRA_OPLGTW-Z-W25-S4"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ast.dump comparison of envelope.py at 37be3485db vs 619e8ddfd6 and vs cf4b036e62: equal (this seat, 2026-10-06 ~04:3xZ and ~05:1xZ)",
        "python -m pytest tests/test_schwab_host_inputs.py on CLOUD: 9 passed (this seat, ~05:4xZ)",
        "deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md step 7; remediations/REMEDIATION_v5.md#NFRA_OPLGTW-Z-W15-S51 (REMEDIATED)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r19b_phaseB_login_before.out vs r19b_phaseB_login_after.out (this seat's diff)",
        "git log ea7ebece14 -- infra/aws/ec2/opal-gateway/tests/proc_tmp_root.py"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each row is either corroborated harmless by this seat's own read (S54, S60), resolved on CLOUD (S55, W25-S4), or the designed catch of an already-REMEDIATED remedy (S56)."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S32",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T05:55:00Z",
    "one_line": "Round 19 L8: Z-W15-S58 GRADUATES OPEN for the issuer -- test_schwab_export_stream.py::test_ogx2_ac01 flips on both live and release bytes, so a baseline reads 7 or 8 failing ids by chance and a one-id difference cannot be graded.",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "test_ogx2_ac01 failed then passed on identical re-runs of live 37be3485db, and passed then failed on the release tree (job_failed in the export stream). Every release-vs-baseline test comparison since carries a one-id ambiguity, which the worker had to name so a half would not read it as a regression.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W15-S58"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S58",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r19b_tests_baseline.out, r19b_tests_release.out",
        "remediations/REMEDIATION_v7.md"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S33",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T05:55:00Z",
    "one_line": "Record: this seat's r19b never-widen guards V1-V3 all held on the deployed host, and Z-W22-S10 and Z-W25-S3 are advanced to REMEDIATED on this seat's own test runs. The r19 half was WITHDRAWN (@06502d7020) after concurring with the CTO's refusal.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A never-widen half's guards are read on the deployed host by the CVO, not taken from the drain summary; the CVO advances remediation clocks only on its own corroborating read.",
    "world_is": "V1: r19b_phaseB_step9_live_md5.out reads MD5 listed 96, identical 96, mismatch 0 before the act. V2: r19b_phaseB_verify_after.out reads VERIFY PASS 7 of 7 -- shipped md5 96 of 96, 65 tools before and after, .env 51 names with 51 of 51 value hashes equal, the refusals listing's sender fields args-borne when present and null when absent (3 of 3 arms on the installed code) -- and the /login record is equal before and after (C-S31). V3: git diff --stat cf4b036e62 CLOUD -- infra/aws/ec2/opal-gateway reads empty, so CLOUD equals the deployed release. Z-W22-S10: ts-2 (ba9a6db154) classified /yearinreview in ROUTE_CLASS and aligned host-inputs to 51 keys and CLOUD's build_package; this seat ran tests/test_principal_cutover.py (11 passed) and tests/test_schwab_host_inputs.py (9 passed) on CLOUD, each in its own process. Z-W25-S3: ts-2 A1 (ea7ebece14) gives each process its own temp root (tests/proc_tmp_root.py); this seat ran deliverables/2.0.0_SA_COO~O/r19/checks/ts2.AC2.sh: concurrent export runs passed 30, failures beyond baseline 0, FileNotFoundError 0, RESULT PASS. The r19 half (619e8ddfd6) was signed on the wrong test for /login and withdrawn; the CTO's refusal held, and R22's re-cut shipped without the narrowing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/r19b_phaseB_step9_live_md5.out, r19b_phaseB_verify_after.out, r19b_phaseB_login_before.out, r19b_phaseB_login_after.out",
        "git diff --stat cf4b036e62 CLOUD -- infra/aws/ec2/opal-gateway: empty (this seat, ~05:4xZ)",
        "pytest runs on CLOUD by this seat: test_principal_cutover.py 11 passed; test_schwab_host_inputs.py 9 passed",
        "ts2.AC2.sh run by this seat ~05:5xZ: concurrent export runs passed 30, FileNotFoundError 0, RESULT PASS",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-7_HALF_20261006.md (WITHDRAWN @06502d7020), cvoO_NEVER_WIDEN_OG-rl-7B_HALF_20261006.md (@e79b976d9b)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
