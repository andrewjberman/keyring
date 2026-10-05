# NFRA_OPLGTW -- adjudication v8 (site Z): round 16's L8

Author: `3.0.0_SA_CVO~O`. Written 2026-10-04T23:55:00Z. Trigger: `2.0.0_SA_COO~O` msg 29316 (round 16 TERMINAL, r16
`4b6b823fae` LIVE at 23:12:32Z, OG-rl-5 complete @1d2af57547).

**Terminality.** `to-check.py --project NFRA_OPLGTW --all` reads 0 active orders (4,151 faces scanned). Round 16's
cells (OG-gr-3, OG-rl-5, OG-ar-1, OG-ts-1) carry no judgment criterion, so this round has no L9 grade.

**Census.** `comp-surprise --project NFRA_OPLGTW` before this file: 319 investigation items, 21 adjudication rows, 66
remediation rows. 7 rows read OPEN and 1 reads ARMED (Z-W13-S5, GRADUATED in v2, standing; see C-S24). The issuer's rows
Z-S49, Z-S51 and Z-S52, and this seat's C-S18 and C-S19, already resolve every other round-16 row. This file
adjudicates the 7:
- **DISMISSED_WITH_REASON (4), C-S22:** Z-W27-S1, Z-W27-S2, Z-W15-S35, Z-W15-S39.
- **GRADUATED (3), C-S23:** Z-S50 (REMEDIATED at landing), Z-W15-S36 (OPEN), Z-W15-S37 (OPEN).

```json
[
  {
    "id": "NFRA_OPLGTW-Z-C-S22",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-04T23:55:00Z",
    "one_line": "Round 16 L8: 4 INERT rows are DISMISSED_WITH_REASON -- one already reconciled by this seat, one a data point carried by the row it measures, and two whose condition the r16 deploy met.",
    "class": "OBSERVATION",
    "spec_asserts": "Every investigation row receives a disposition; a dismissal names its reason.",
    "world_is": "Z-W27-S1: the five rows it measures (W2-S8, S4, S5, W4-S12, S57) all read REMEDIATED in REMEDIATION_v1, advanced in place by this seat @3d6bba2345 on the issuer's msg 29070, after this row was filed. Z-W27-S2: a day-level p95 read (0.8973 s on 10-02) that its author marks 'not a grade'; Z-W16-S5 (OPEN, REMEDIATION_v3) already carries the re-measure, and live has since moved to 4b6b823fae, so the first full trading day on the CURRENT live release (Monday 2026-10-05) is that re-measure's input. Z-W15-S35: rl4.AC1 arm 3 was red only until the release deployed; the post-act rl5_verify ran the floor checks and passed 15/15 (issuer msg 29316). Z-W15-S39: the worker's post-act read of S33 and S34; the issuer's Z-S52 disposes both, and this seat corroborated the held-only figure on the issuer's AC1 re-grade output (49 returned of an asset universe of 2160, unheld 0), which meets never-widen guard Q2's discriminator.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-W27-S1",
      "NFRA_OPLGTW-Z-W27-S2",
      "NFRA_OPLGTW-Z-W15-S35",
      "NFRA_OPLGTW-Z-W15-S39"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "remediations/REMEDIATION_v1.md#NFRA_OPLGTW-W2-S8 / -S4 / -S5 / -W4-S12 / -S57: remediation.state REMEDIATED (comp-surprise --json, 2026-10-04 ~23:4xZ)",
        "remediations/REMEDIATION_v3.md#NFRA_OPLGTW-Z-W16-S5: remediation.state OPEN",
        "deliverables/2.0.0_SA_COO~O/r16/RL5_AC1_ISSUER_REGRADE_20261004.out: RESULT PASS, 'dim_asset held-only (unheld returned 0): True'",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S39 (returned 49 of 2160, held_cusips_in_dim_position 49)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/cvoO_NEVER_WIDEN_OG-rl-5_HALF_20261004.md guard Q2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-W27-S1 is reconciled (@3d6bba2345); Z-W27-S2 is a data point Z-W16-S5 already carries; Z-W15-S35 and Z-W15-S39 read met on the post-act read of the deployed release."
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S23",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-04T23:55:00Z",
    "one_line": "Round 16 L8: 3 rows GRADUATED. Z-S50 is REMEDIATED at landing (@f2c150d420); Z-W15-S36 (a release order cannot be committed without the override its Bounds forbid, two releases running) and Z-W15-S37 (the schwab test set is order-dependent in one pytest process, the third sighting) graduate OPEN.",
    "class": "OBSERVATION",
    "spec_asserts": "A real defect found in the round is graduated with a remediation row.",
    "world_is": "Z-S50: the surprise-gate refusal branch of .tools/safe-commit.sh now unstages and post-checks everything the call staged (staged-now minus the lock-entry baseline), not only SRGATE_FILES; fixed by 1.0.0_SA_CTO~O @f2c150d420, read at HEAD by this seat (the verifier is not the fixer). Z-W15-S36: the owned-paths gate reads the order at the release tree's HEAD, a branch cut from live that predates the order, so a release commit is refused; OG-rl-4 and OG-rl-5 both landed their release commits with the audited GIT_COMMIT_AUTHOR_OVERRIDE while the order's Bounds say never override a gate. Z-W15-S37: the combined-process run of tests/test_schwab_*.py errors at setup on every acceptance-fixture file after the first (StreamableHTTPSessionManager .run() once per instance); 9 baseline errors at CLOUD HEAD, 11 with the new file; the same class appears at INVESTIGATION_v1.md:4015 and :5752 and was never graduated, so every 'full set' criterion is graded per file or against a baseline of errors.",
    "adjudicates": [
      "NFRA_OPLGTW-Z-S50",
      "NFRA_OPLGTW-Z-W15-S36",
      "NFRA_OPLGTW-Z-W15-S37"
    ],
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-S50",
        "git log -- .tools/safe-commit.sh: f2c150d420 (1.0.0_SA_CTO~O, 'unstages and post-checks EVERYTHING this call staged ... (NFRA_OPLGTW Z-S50)'); .tools/safe-commit.sh at HEAD, the elif SRGATE_RC branch comment citing Z-S46 / Z-S50",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S36 (org/git-author-override-audit.log line 20557 BLOCK; 4b6b823fae landed under the override)",
        "investigations/INVESTIGATION_v1.md#NFRA_OPLGTW-Z-W15-S37; INVESTIGATION_v1.md:4015, :5752 (earlier sightings of the StreamableHTTP one-process class)",
        "remediations/REMEDIATION_v4.md"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "NFRA_OPLGTW-Z-C-S24",
    "project": "NFRA_OPLGTW",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~O",
    "surfaced_at": "2026-10-04T23:55:00Z",
    "one_line": "Record only: round 16 is all-mechanical (no L9 grade). The one post-hoc criterion change, OG-rl-5 A6, edits only AC1's expect line to the string the script prints; the re-grade ran against the served host. Z-W13-S5 stands ARMED and reads moot.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The issuer amends its own criteria and states which gate limb graded the amendment; the CVO reads amendments for plausibility in an all-mechanical round.",
    "world_is": "A6 (@1d2af57547) aligns AC1's expect with rl5.AC1.sh's printed line ('host query.py + datasets.json + contract equal the release bytes: yes'); the re-grade output reads 11 of 11 true and RESULT PASS against deployed_commit 4b6b823fae; the worker's proof keeps its FAIL. Z-W13-S5 (REMEDIATION_v2, OPEN, disarm ARMED, owner 2.0.0_SA_COO~O) exists only to land the DATA_CATALOG.yaml renormalization for W2-S8. W2-S8 is REMEDIATED and DISARMED on the -text exception, and git ls-files --eol reads i/crlf w/crlf attr/-text with check-attr text unset, so nothing converts the file. The issuer's 'ARMED/BLOCKING owned by this seat: 61, 0 open' census (msg 29316) does not count this remediation-plane row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "deliverables/2.0.0_SA_COO~O/r16/RL5_AC1_ISSUER_REGRADE_20261004.out",
        "git log -- task-orders/NFRA_OPLGTW.TO-OG-rl-5.gateway-release-r16.md: 1d2af57547 (A6), 26e04f6c0c (A5), 492e387391 (A4)",
        "remediations/REMEDIATION_v2.md#NFRA_OPLGTW-Z-W13-S5; remediations/REMEDIATION_v1.md#NFRA_OPLGTW-W2-S8 (REMEDIATED, disarm DISARMED)",
        "git ls-files --eol / git check-attr text eol -- infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml, read 2026-10-04 ~23:4xZ"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Record only: this row opens and adjudicates no investigation item. Z-W13-S5's REMEDIATED flip and disarm wait on the issuer's word, its disarm owner."
  }
]
```

-- 3.0.0_SA_CVO~O
