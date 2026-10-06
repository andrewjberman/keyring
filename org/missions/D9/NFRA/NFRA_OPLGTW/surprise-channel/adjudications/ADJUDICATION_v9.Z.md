# NFRA_OPLGTW -- adjudication v9 (site Z): round 17's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T00:55:00Z. Trigger: `2.0.0_SA_COO~O` msg 29837 (round 17 TERMINAL, 6 of
6; r17 `e91819e281` and r17c `37be3485db` LIVE; last drain 65c8fe6bac).

**Terminality.** All 6 round-17 orders are complete per the issuer. Round 17 carries no judgment criterion
(OG-rl-6, OG-q-7, OG-gr-4, OG-pm-1 and the rest), so this round has no L9 grade.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 339 investigation items, 24 adjudication rows, 69
remediation rows. 15 rows read OPEN and 1 reads ARMED (Z-W13-S5, standing; C-S27). The issuer's Z-S53 and Z-S54 already
resolve Z-W15-S42, S46 and S50. This file adjudicates the 15:
- **DISMISSED_WITH_REASON (10), C-S25:** Z-W25-S2, Z-W22-S8, Z-W15-S40, Z-W15-S43, Z-W15-S48, Z-W15-S49, plus four
  companions whose substance a C-S26 row carries: Z-W15-S44 (in Z-W15-S47), and Z-W15-S45, Z-W22-S6 and Z-W22-S7 (in
  Z-W15-S51).
- **GRADUATED (5), C-S26:**
  - Z-W27-S3 (the p95 regression);
  - Z-W15-S41 (FWD-4 unexercised by any real principal);
  - Z-W15-S47 (CLOUD's gateway source and live have diverged);
  - Z-W15-S51 (a check graded against an anchor it cannot read);
  - Z-S55 (the onboarding kit points colleagues at the June local setup).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S25",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T00:55:00Z",
    "one_line": "Round 17 L8: 10 INERT rows are DISMISSED_WITH_REASON -- three are further sightings carried by the OPEN test-isolation row Z-W15-S37, two are CRLF warnings the shipped bytes falsify, one is egress the never-widen ask already bounded, and four are companions whose substance a C-S26 remediation row carries.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W25-S2 (the integration caches the first service built in a process; fixed in tests only), Z-W22-S8 (test_ogq1_ac04 failed once while a second pytest process ran, then passed alone) and Z-W15-S40 (the one-process run of the release's named targets fails on CLOUD too, beyond ti-1's fix) are the same class as Z-W15-S37, which stays OPEN with the issuer; none touches shipped bytes. Z-W15-S43 and Z-W15-S48 warn that the kit's index.html is CRLF on disk, but the shipped r17c page measures 48,022 bytes with 0 CR both on disk in /c/tmp/og-rel13 and in blob 37be3485db, as the r17b release did (48,022 bytes, 0 non-ASCII, this seat's read @0366ca3748). Z-W15-S49 (the planted-identity check makes the host fetch the ELB public key from AWS) is the egress the never-widen ask @f6fdd4047b names as Opal's own AWS identity path, which this seat's half @9c23533619 accepted. Companions: Z-W15-S44 (CLOUD and live server.py differ by OA-e-10's /login) is carried by Z-W15-S47's remediation row; Z-W15-S45, Z-W22-S6 and Z-W22-S7 (three checks unable to grade their property) are carried by Z-W15-S51's.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W25-S2",
      "NFRA_OPLGTW-Z-W22-S8",
      "NFRA_OPLGTW-Z-W15-S40",
      "NFRA_OPLGTW-Z-W15-S43",
      "NFRA_OPLGTW-Z-W15-S48",
      "NFRA_OPLGTW-Z-W15-S49",
      "NFRA_OPLGTW-Z-W15-S44",
      "NFRA_OPLGTW-Z-W15-S45",
      "NFRA_OPLGTW-Z-W22-S6",
      "NFRA_OPLGTW-Z-W22-S7"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v4.md#NFRA_OPLGTW-Z-W15-S37: remediation.state OPEN",
        "C:/tmp/og-rel13 app/static/yearinreview/index.html and git show 37be3485db:<same>: 48,022 bytes, CR 0 (read 2026-10-06 ~00:5xZ)",
        "deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6-C2_20261005.md@f6fdd4047b section 2 'Egress (row Z-W15-S49)'",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-6-C2_HALF_20261005.md@9c23533619"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W25-S2, Z-W22-S8 and Z-W15-S40 are carried by the OPEN Z-W15-S37; Z-W15-S43 and Z-W15-S48 are falsified by the shipped bytes (0 CR); Z-W15-S49 is egress the signed ask bounded; Z-W15-S44, Z-W15-S45, Z-W22-S6 and Z-W22-S7 are companions carried by the remediation rows Z-W15-S47 and Z-W15-S51."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S26",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T00:55:00Z",
    "one_line": "Round 17 L8: 5 rows GRADUATE OPEN -- the p95 regression (Z-W27-S3), FWD-4 unexercised by a real principal (Z-W15-S41), CLOUD source diverged from live (Z-W15-S47), checks graded against anchors they cannot read (Z-W15-S51), and the stale onboarding kit (Z-S55).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W27-S3: the full-day 2026-10-05 p95 is 0.9473 s over 3,328 requests, +71.1 % against OG-p-1's 0.5535 s and above the 0.6642 s cap on all three served releases; this is the re-measure Z-W16-S5 asked for, and it confirms the regression. Z-W15-S41: the one live grant naming dim_asset lacks download_filtered, so the r17 download opens for no real principal; only the synthetic grant exercised it. Z-W15-S47 / S44: CLOUD's gateway source and live have diverged both ways -- CLOUD carries OA-e-10's /login change that live lacks, and live carries template lines CLOUD's deploy-to-ec2.sh lacks -- because releases are cut on live and their branches are not drained back. Z-W15-S51 / S45 / Z-W22-S6 / S7: four checks could not grade the property they name (a manifest anchor that does not exist until a later step; a before-state that no longer exists; a one-line PASS parse that a capsys print splits; a grep count of call sites that a single helper defeats); with the issuer's own S38, S42 and S50, seven such rows in two rounds. Z-S55: .tools/m365-mcp-kit/ still installs the June local Lokka server under the old 'm365' name.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W27-S3",
      "NFRA_OPLGTW-Z-W15-S41",
      "NFRA_OPLGTW-Z-W15-S47",
      "NFRA_OPLGTW-Z-W15-S51",
      "NFRA_OPLGTW-Z-S55"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W27-S3, #Z-W15-S41, #Z-W15-S47, #Z-W15-S44, #Z-W15-S51, #Z-W15-S45, #Z-W22-S6, #Z-W22-S7, #Z-S55",
        "remediations/REMEDIATION_v3.md#NFRA_OPLGTW-Z-W16-S5 (the re-measure remedy this round executed)",
        "remediations/REMEDIATION_v5.md"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S27",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T00:55:00Z",
    "one_line": "Record only: round 17 has no L9 grade; this seat's three never-widen halves of the round each held on the deployed host; Z-W13-S5 still stands ARMED and moot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "A never-widen half names guards the after-read must meet; the CVO reads that after-read, not the drain summary.",
    "world_is": "r17 (OG-rl-6, half @9c7fa957a3, guards R1-R2): verify 12/12, the download held-check 49 of a 2,160 universe with 0 unheld, and the empty-holdings refusal, at drain daa5f5ef70. r17b (@0366ca3748) LAPSED under S2 on Andrew's owner-only word (@1760ccc363) and never shipped. r17c (half @9c23533619 for C2, guards T1-T2): rl9_step18_live_reread.out reads live 94 of 94 equal before the act (T1); rl9_phaseB_verify_after.out reads the four arms on the deployed host (owner path 5 of 5, empty roster 3 of 3, missing roster 3 of 3), the public 302, and .env 51 names with 50 of 50 prior value hashes equal (T2). The owner's real 200 stays UNEXERCISED until Andrew opens the page. Z-W13-S5 (REMEDIATION_v2, disarm ARMED, owner 2.0.0_SA_COO~O) still reads moot under DATA_CATALOG.yaml's -text exception and still waits on the issuer's disarm.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git show daa5f5ef70 (r17 drain message)",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/rl9_step18_live_reread.out",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~15/rl9_phaseB_verify_after.out lines 2-32, 53-54, 64-69",
        "remediations/REMEDIATION_v2.md#NFRA_OPLGTW-Z-W13-S5"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
