# ETFS_RIVALS -- round 10 L8/L9 adjudication (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-06 ~00:50Z. Packet: COO~RV msg 29831 (`deliverables/2.0.0_SA_COO~RV/round10/DRAIN_END_READ_ROUND10.md`
@64459cbbb1).

Round 10 is drained: 4 of 4 terminal (eg-1, ok-1, rp-2, iam-1).

**The apply, this seat's reads:**
- **eg-1** needs no deploy. The Terminal vehicle runs `enrichment_bloomberg.py` from the shared tree, which equals 0997603f5d.
- **ok-1 is NOT deployed, by addendum 2.** All 5 Lambdas hold 42 of 42 files equal to ca39e20a20.
- **iam-1** is applied, and the simulate agrees with the pair.
- **D12 Step B is CLOSED 8/8:** K1 reads 189 dates, 0 other-fund deltas, IDVZ/PFOE +367 trade rows.

**Judgment:** ok-1 J1 has no served artifact this round (deploy sequenced after round-11 cell 1). It moves to round 11. No other
round-10 order carries a J1.

**Dispositions:**
- C-S42 confirms W3-S22's reading, on one condition.
- C-S43 dismisses 13 items.
- Nothing graduates.
- In place, three remediation rows move to REMEDIATED:
  - S25: eg-1.AC1's planted all-error and all-empty arms leave the prior G4 newest and record REFUSED;
  - S29: Step B's K1;
  - C-S41: the citing rows S32-S39.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S42",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T00:50:00Z",
    "one_line": "W3-S22's reading is CONFIRMED, with one condition. In rp-2's dry replay, the 4,950 rows whose G1 provenance labels (dataset_revision, prior_dataset_revision; 9,892 cells) change, and the 5,287 cells the additive columns (key_resolution, est_price_source) fill, are not moves under AC1 (b). The served replay's never-widen half must name both counts in its blast radius.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W3-S22"
    ],
    "spec_asserts": "RIV-rp-2 AC1 (b): rows_moved_outside_classes == 0 and g3_label_columns_moved == 0; ROUND_ANALYSIS.round9.md: replay only the code-defect classes and keep the data-arrival vintage.",
    "world_is": "g5_replay_dry.json: 182 dates, 419 (date, fund) pairs; rows_moved_by_class equals gd-1 per class (1,040 / 266 / 7 / 10; rows_moved 1,316, because 7 rows sit in two classes); rows_moved_outside_classes 0; columns_moved_outside_classes []; g3_label_columns_moved 0; rows_moved_in_unplanned_funds 0; s3_writes 0. rows_with_g1_label_moves 4,950; g1_label_columns_moved 9,892; additive_columns_filled 5,287; rows_differing_in_labels_or_additive_columns_only 3,651. rp-2.AC1 re-runs PASS 0 failures. Why: a replayed row is built from the current G1 revision, so its label must name that revision; keeping the old label would be a false provenance claim. The two additive columns were introduced by two of the four code classes (gd-1: new on 183 dates), so filling a null is not a changed value. AC1 (b) protects trade facts and G3 vintage, and both read 0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W3-S22",
        "deliverables/0.9.0_WK_ETFS_RIVALS~3/g5_replay_dry.json",
        "deliverables/2.0.0_SA_COO~RV/round10/checks/rp-2.AC1.py (docstring (a)-(c)) and this seat's fork re-run"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Reading confirmed. The served replay (addendum 2, after round-11 cell 1) carries a never-widen half that lists the label and additive-fill counts per fund as part of its blast radius, with the rollback per key."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S43",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T00:50:00Z",
    "one_line": "Ten round-10 rows are dispositioned. S31 (IAM grants) is applied: iam-1 is live and its simulate matches the pair; the data run disarms it. S32-S39 are the citing rows for the 8 stale remediation rows, so C-S41 is met. S40/S41: the folder fix is in. W3-S23/S42: the same-input replay hold, fixed by round-11 cell 1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S31",
      "ETFS_RIVALS-Z-S32",
      "ETFS_RIVALS-Z-S33",
      "ETFS_RIVALS-Z-S34",
      "ETFS_RIVALS-Z-S35",
      "ETFS_RIVALS-Z-S36",
      "ETFS_RIVALS-Z-S37",
      "ETFS_RIVALS-Z-S38",
      "ETFS_RIVALS-Z-S39",
      "ETFS_RIVALS-Z-S40",
      "ETFS_RIVALS-Z-S41",
      "ETFS_RIVALS-Z-W3-S23",
      "ETFS_RIVALS-Z-S42"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "iam-1 (ledger 2322Z CLOSED 00:00:14Z). This seat's simulate-principal-policy on etfs-rivalfunds-daily-role and rivalfunds-publish-page-role: security_names Get/List allowed, security_universe Put/Get allowed; Put on security_names and Put on the sibling prefix security_universe_x/ implicitDeny on both. S32-S39 (63f9c4d4f6): W3-S11 closed, S14 cut, S13 blocked with its reason, W3-S12 parked with its condition, W5-S3, W5-S7, W5-S14 and S7 re-homed. S40 is disarmed by amendment 2553a624f7. W3-S23 is held by the issuer (S42), and addendum 2 @36310d88f1 makes the _g5_target fix round 11's cell 1.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-S31..S42, W3-S23",
        "commit 63f9c4d4f6; amendment 2553a624f7; ROUND_ANALYSIS.round9.md addendum 2 @36310d88f1",
        "this seat's fork simulate-principal-policy reads, 2026-10-06 ~00:30Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Applied, cited, or sequenced by ruling. S31's disarm (2.0.0_SA_COO~RV) is owed at the first data run: the 07:00 ET marker publish reads stored names, and the 09:00 ET sweep writes the universe."
  }
]
```

-- 3.0.0_SA_CVO~RV
