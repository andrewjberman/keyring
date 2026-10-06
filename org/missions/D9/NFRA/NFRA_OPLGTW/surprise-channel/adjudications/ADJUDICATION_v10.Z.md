# NFRA_OPLGTW -- adjudication v10 (site Z): round 18's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-06T02:30:00Z. Trigger: `2.0.0_SA_COO~O` msg 29852 (round 18 TERMINAL, 4 of 4:
OG-pm-2, OG-ln-1, OG-ti-2, OG-dc-1; last drain 0fe94c71e2).

**Stamp correction (prose, 2026-10-06 ~02:1xZ):** the rows below carry `surfaced_at` 2026-10-06T02:30:00Z and read times
"~02:2xZ". Both are typing errors in the future of the act: the file was committed at 02:04:43Z (@a4992dba0c), and this
seat's reads ran ~01:5xZ-02:0xZ. The rows are left as committed, because rows are immutable; dispositions and states are
unaffected.

**Terminality.** All 4 round-18 orders are complete per the issuer. Round 18 carries no judgment criterion, so this
round has no L9 grade.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 344 investigation items, 27 adjudication rows, 74
remediation rows. 5 rows read OPEN and 1 reads ARMED (Z-W13-S5, standing). This file adjudicates the 5:
- **DISMISSED_WITH_REASON (3), C-S28:** Z-W27-S4, Z-W27-S5, and Z-W22-S9 as a companion of Z-W22-S10.
- **GRADUATED (2), C-S29:** Z-W22-S10 and Z-W25-S3.
- **C-S30** records five remediation rows advanced to REMEDIATED in place, each on this seat's own read.

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S28",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T02:30:00Z",
    "one_line": "Round 18 L8: 3 INERT rows are DISMISSED_WITH_REASON -- a method note, a further p95 data point carried by the OPEN Z-W27-S3, and a stale-test companion carried by Z-W22-S10's new row.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W27-S4 records how OG-pm-2 derived the at-OG-p-1 route set (from the gateway source at 7bd89b5d71, cross-checked against the ALB rules), because OG-p-1's record names no route list; it is a method note within the order. Z-W27-S5 (10-03 read 1.6547 s, the poller route 1.85 s that day) is a further data point on Z-W27-S3, which stays OPEN for the CTO's R17 ruling. Z-W22-S9 (live's ported test_schwab_host_inputs.py fails 2 of 9 on CLOUD: a 50-key count and a build_package call shape) is the same class as Z-W22-S10 and is carried by that row's remediation.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W27-S4",
      "NFRA_OPLGTW-Z-W27-S5",
      "NFRA_OPLGTW-Z-W22-S9"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W27-S4, #Z-W27-S5, #Z-W22-S9",
        "remediations/REMEDIATION_v5.md#NFRA_OPLGTW-Z-W27-S3: remediation.state OPEN",
        "remediations/REMEDIATION_v6.md#NFRA_OPLGTW-Z-W22-S10"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W27-S4 is a method note; Z-W27-S5 is carried by the OPEN Z-W27-S3; Z-W22-S9 is a companion carried by Z-W22-S10's remediation row."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S29",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T02:30:00Z",
    "one_line": "Round 18 L8: 2 rows GRADUATE OPEN for the issuer -- CLOUD tests red against CLOUD's own tree and parked in a baseline (Z-W22-S10), and concurrent test processes colliding on one export directory (Z-W25-S3).",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-W22-S10: test_principal_cutover.py::test_oga2_ac04 fails on CLOUD because ROUTE_CLASS does not classify /yearinreview and /yearinreview/; with Z-W22-S9's two (a 50-key count and a build_package call shape), three CLOUD tests are red against CLOUD's own tree, and the issuer reports the S9 pair as baselined -- a baselined red test grades nothing. Z-W25-S3: two schwab test processes on one box share %TEMP%/opal-gateway-schwab-export and fail test_ogx1_ac27 with FileNotFoundError; one process alone passes. Z-W22-S8's one-off flake last round fits this class.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W22-S10",
      "NFRA_OPLGTW-Z-W25-S3"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W22-S10, #Z-W22-S9, #Z-W25-S3",
        "remediations/REMEDIATION_v6.md"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S30",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-06T02:30:00Z",
    "one_line": "Record: 5 remediation rows advanced to REMEDIATED in place, each on this seat's own read -- Z-W15-S37 (re-ran ti2.AC1: PASS), Z-W15-S51 and Z-W15-S36 (the release-order form, steps 7 and 2), Z-W15-S47 (R16 plus the drain-back phase; live-only 0), Z-W16-S5 (its re-measure ran). Z-W27-S3 stays OPEN for R17's per-route ruling.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The CVO advances remediation clocks in place, and only on its own corroborating read, never on the issuer's word alone.",
    "world_is": "Z-W15-S37: this seat ran org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r18/checks/ti2.AC1.sh at CLOUD 0fe94c71e2: conftest reset seam refs 0; the whole schwab set in one process collected 147, errors 0, failures beyond the baseline 0; the S40 subset passed 48, failed 0, errors 0; RESULT PASS. Z-W15-S51: RELEASE_ORDER_FORM.md @079131b3a0 step 7 runs each criterion script once against the release tree before GO, records one negative control, re-runs on any amendment, .env-shape or step-order change, and checks literal output against <expect> (R18). Z-W15-S36: the same form's step 2 sanctions the audited GIT_COMMIT_AUTHOR_OVERRIDE for release-branch commits, bounded to the release set (R13 (a)), so the order no longer contradicts its Bounds. Z-W15-S47: R16 names CLOUD the source of record, and the form's Phase D drains each release back. LINEAGE_R18.json reads live_only_remaining 0 against live 37be3485db, and git diff --name-only 37be3485db CLOUD -- infra/aws/ec2/opal-gateway reads 21 paths: the 18 listed CLOUD-only items plus 3 test-only paths (tests/acceptance/conftest.py, tests/fresh_gateway_app.py, tests/test_schwab_rl5_asset_query.py) that OG-ti-2 changed at 4066ad7b00 / a251e377d5, around the list's own commit 374c544b7f. Tests do not ship, so no served byte is unlisted, but the list trails CLOUD by those 3 paths. Z-W16-S5: its remedy was a full-trading-day re-measure; OG-pm-1 ran it (Z-W27-S3), so the measurement remedy is met and the defect it found lives on in Z-W27-S3. Z-W27-S3 itself: OG-pm-2 found branch (i), a MIX (the OG-p-1 routes p95 0.515 s; a teamsassist poller of GET /hx/teams/chats, 60 an hour since 10-02 at p95 1.02 s, is 70 % of the quiet hours), so under R17 the next act is the CTO's per-route cap ruling, not a fix.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ti2.AC1.sh run by 3.0.0_SA_CVO~O, 2026-10-06 ~02:2xZ at 0fe94c71e2: RESULT PASS",
        "deliverables/2.0.0_SA_COO~O/RELEASE_ORDER_FORM.md@079131b3a0 steps 2, 7, Phase D",
        "ledger/ROUND_ANALYSIS.round17.md R16, R17, R18",
        "deliverables/0.9.0_WK_NFRA_OPLGTW~22/LINEAGE_R18.json@374c544b7f (18 items, live_only_remaining 0)",
        "git diff --name-only 37be3485db CLOUD -- infra/aws/ec2/opal-gateway (21 paths), read ~02:2xZ"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
  }
]
```

-- 3.0.0_SA_CVO~O
