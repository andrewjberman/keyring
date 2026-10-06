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

**Part B (2026-10-06 ~14:00Z), the 10-06 reads:** C-S44 -- D12 leg, iam-1 data and sweep PASS; nm-3 NOT MET (2 holdings);
eg-1 live refusal and S24 backfill proof NOT EXERCISED; new rows S47 (dialogs OFF on the page) and S48 (enrichment hangs on an
unreachable DAPI).

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
  },
  {
    "id": "ETFS_RIVALS-Z-C-S44",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-06T14:00:00Z",
    "one_line": "The 2026-10-06 reads (ROUND_ANALYSIS.round9.md ruling 6; CTO~Z msg 30024: graded from the post-sign-in re-run, with the 11:00Z fire as one cause, the Terminal down). PASS: the D12 daily leg, iam-1's data run (S31 disarm verified) and the organic sweep. NOT MET: nm-3 (2 holdings still ticker-form with no reason). NOT EXERCISED: eg-1's live refusal arm (S48) and S24's backfill-night proof. New: the page's dialogs are OFF (S47).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S44",
      "ETFS_RIVALS-Z-S45",
      "ETFS_RIVALS-Z-S46"
    ],
    "spec_asserts": "The first-act block of logs/2026-10-05/session_cvoRV_20261005T1320Z-2020Z.md (commits 6b5941834e, 2b31efc634): nm-3 J1, S24, eg-1 live, the D12 daily leg, iam-1's first data run, S31.",
    "world_is": "Cause: the Terminal was down 03:09Z-12:22Z (S44/S45: a sign-in script clicking at stale screen coordinates, per 0.0.3_BG_BBGTerminal msg 30019). Re-run bbg_tplus1_20261006_082454.log, rc 0.\n- **eg-1:** G4 date=2026-10-05 market-20261006T123301Z-b6602b19fad6 (12:33:51Z): status OK, 582 securities, 0 errors, px_close 578 / gics 575 of 582. The refusal arm was not exercised live (S48); it stays proven offline (C-S43 / S25).\n- **S24:** ledger bbg_budget_2026-10-06.jsonl, 17 entries, 935 of 150,000 rows (daily 751, names 134, probe 50); 0 'Daily Capacity' in 751 capture rows. No backfill night ran, so the remedy's own proof (a backfill night, then a clean 07:00 ET pull) is unexercised and S24 stays OPEN.\n- **D12:** IDVZ 44 and PFOE 24 rows, of 751 in the capture and of 403 in G1 holdings-20261006T123244Z.\n- **nm-3:** the names stage ran (PARTIAL: 134 asked, 128 named; gold/security_names date=2026-10-06 12:33:59Z). On the served 10-06 page (ai-2026-10-06-517fd371, 13 of 13, 13:07:38Z), visible holding ticker forms read 3 occurrences of 2 holdings, against 28 of 22 on 10-05: 8053 JP Equity x2 and 9433 JP Equity in INEQ, with no reason shown. Of the 22 control keys, ATD_CN, MSCI_US, BABA_US, NOVN_SW and TCEHY_US now read company names; 'GQG US Equity' is the fund label, not a holding.\n- **iam-1:** 0 AccessDenied on etfs-rivalfunds-daily-lambda and rivalfunds-publish-page-lambda since 10:00Z. gold/security_universe date=2026-10-05 universe-20261006T130739Z written 13:07:40Z. S46's disarm of S31 is consistent.\n- **Sweep:** REPORT de6ac4f0 447.3 s, 0 timeouts; AI attempt OK, scheduled, 20261006T130020Z-ai.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "this seat's playwright read of platinum/page/date=2026-10-06/index.html and its manifest",
        "this seat's fork reads: the two vehicle logs, the budget ledger, G1/G4/security_names/security_universe objects, CloudWatch for both Lambdas",
        "investigation rows ETFS_RIVALS-Z-S44, S45, S46, S47, S48"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade record. S44/S45 are the environment cause (Terminal down; the sign-in script belongs to 0.0.3_BG_BBGTerminal). S46's disarm of S31 is verified. C-S36 (nm-3) and S24 stay OPEN. S47 and S48 go to round 11's compile."
  }
]
```

-- 3.0.0_SA_CVO~RV
