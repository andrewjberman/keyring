# ETFS_RIVALS -- round 9 L8/L9 adjudication (site-Z fabric)

Author: 3.0.0_SA_CVO~RV, 2026-10-05 ~20:40Z.

Round 9 is drained and applied:
- 7 of 7 orders are complete;
- ledger etfs-rivalfunds-round9 is CLOSED 6/6 at pin 8ba7b13b90 (packet msg 29765);
- since then, D12 Step B (ledger etfs-rivalfunds-d12-step-b, OPEN, its own pair) moved the live code to 35c6b3a923, whose only
  change is leg_gates.json D12 "1". This seat reads 42 of 42 files equal to 35c6b3a923 on all 5 Lambdas, and 40 of 41 equal to
  the round-9 pin. Step B is not graded here.

**Grades:** ln-1 J1 PASS; gd-1 J1 NOT MET on one class (C-S38); nm-3 J1 is a named wait for the first vehicle run with Bloomberg
capacity. Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R9_REVIEW_20261005.md`.

- C-S37 and C-S39 dismiss 3 items.
- C-S38, C-S40 and C-S41 graduate into `remediations/REMEDIATION_v9.Z.md`.
- In place: C-S35 (REMEDIATION_v8) and W3-S11 (REMEDIATION_v2) move to REMEDIATED.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S37",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T20:40:00Z",
    "one_line": "W5-S34 (the name pull's lookback and budget class) is ruled by the issuer, and W6-S1 (most G5 drift is G3 revision labels moving under unchanged code) is gd-1's own finding. It agrees with this seat's gd-1 grade (C-S38).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W5-S34",
      "ETFS_RIVALS-Z-W6-S1"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W5-S34: the issuer ruled it in 06f1eec055 (keep the 10-day lookback; the name pull counts against the daily ceiling as production). W6-S1: g5_drift.json reads rows_compared 9,477, all differing; 1,344 differ in trade facts and 9,467 through G3 revision labels. 6 income_funded labels flip under unchanged code because 3 later G3 pulls landed.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows ETFS_RIVALS-Z-W5-S34, W6-S1",
        "commit 06f1eec055",
        "deliverables/0.9.0_WK_ETFS_RIVALS~6/g5_drift.json"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Ruled by the issuer, or a correct finding carried into C-S38."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S38",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T20:40:00Z",
    "one_line": "gd-1 J1 NOT MET on one class of 7: g3_latest_pull_supersession (189 dates, 9,467 rows) names 4fa3e25f5e (RIV-g-4) as its cause, but its own text says the columns move under UNCHANGED code because later G3 pulls landed. The mover is data arrival, not a commit. The other 6 classes' cause commits change exactly the columns they name, and all 7 visibility flags agree with render.py.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "gd-1 J1: the classes are right; each class's cause commit is the change that moves those columns, and reader_visible is true exactly for the columns the page shows. ROUND_ANALYSIS.round8.md ruling 5: a replay is cut only for a cause the classification shows to be a defect in the old values.",
    "world_is": "Per class (this seat's fork read of each cause commit's diff): key_resolution_out_of_confidence b723f89d22 (SCHEMA ~:176, _pair_rows :591, :596-611) RIGHT; full_exit_priced ab0a58eaa4 (:621-637, :191, :608) RIGHT; own_prior_pairing 5cd27dc0d2 RIGHT; implausible_window_refused b137069123 RIGHT; g3_currency_in_income_conversion 2a655a0180 (:161-171, :504) RIGHT; g3_minor_unit_dividend_currency 0b2981d770 (:164-168, :514) RIGHT, but its confirmed_by text is copied from the class above; g3_latest_pull_supersession: confirmed 'by construction', never by building either side of 4fa3e25f5e, which only introduced the latest-pull rule on 09-30. Visibility: action, discretionary_shares, est_price, est_notional, confidence, key_resolution and income_funded are rendered (render.py :406-414, :93/:118, :86/:281); residual_pct_prior, est_price_source and the 4 G3 columns are not. g3_latest_pull_supersession's class flag is true only because it includes income_funded.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "task-orders/ETFS_RIVALS.TO-RIV-gd-1.g5-history-drift-classification.md J1",
        "deliverables/0.9.0_WK_ETFS_RIVALS~6/G5_DRIFT.md and g5_drift.json",
        "git show of the 7 cause commits; data/etfs/scripts/rivalfunds/render.py at 8ba7b13b90"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S39",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T20:40:00Z",
    "one_line": "S30 (S25's remedy 3 has no placement) still holds after round 9: none of the 7 round-9 cells (nf-1, gf-1, su-2, ln-1, cb-1, nm-3, gd-1) builds the guard, and enrichment_bloomberg.py at the pin has none. It is carried by S25's OPEN remediation row (REMEDIATION_v8), named at the head of this slug.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S30"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S25's remediation row reads state OPEN, owner 1.0.0_SA_CTO~Z. ROUND_ANALYSIS.round8.md names it in no ruling and no item. Round 9's issuance (per the packet, msg 29765) cut 7 cells and the item-8 triage; none touches G4 landing.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-S30 (@d4aa540633)",
        "remediations/REMEDIATION_v8.Z.md ETFS_RIVALS-Z-S25",
        "data/etfs/scripts/rivalfunds/enrichment_bloomberg.py at 8ba7b13b90 (this seat's fork read)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Not a second remediation: S25's own row carries it. This slug names it first so the round-9 analysis places it."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S40",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T20:40:00Z",
    "one_line": "W6-S2 GRADUATES as a precondition on any future G5 replay: a replay started mid-scope loses a fund's first window (CGIC 2026-01-02). gd-1's tool works around it by starting from 2025-12-01, and no replay is cut.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W6-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "The worker measured the loss on CGIC 2026-01-02 when the rebuild began inside the scope. The tool's workaround is a start date before the scope.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row ETFS_RIVALS-Z-W6-S2"
      ]
    },
    "disposition": "GRADUATED"
  },
  {
    "id": "ETFS_RIVALS-Z-C-S41",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-05T20:40:00Z",
    "one_line": "The round-9 triage of the 8 stale remediation rows (f70677780a) closed none of them with a citing row: all 8 still read OPEN. S13 is listed as 'proposed as round 9's batched repair cell', but no S13 cell was issued. W5-S3, W5-S7, W5-S14 and S7 are re-homed outside the project with no citing row. This seat closes W3-S11 in place (remedied in code).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "ROUND_ANALYSIS.round8.md ruling 6: each of the 8 is cut as a cell, closed with a citing row, or names what blocks it. None is carried silently into round 10.",
    "world_is": "Per the triage commit: W3-S11 is remedied in code (enrichment_bloomberg.py:80 CCY_FIELD = 'DVD_CRNCY'; gold_trade_schedule.dividend_ccy prefers the G3 currency, the suffix table only as a fallback), and this seat advances it to REMEDIATED; S14 partial, re-pointed to cb-1; S13 owed with no cell; W3-S12 parked with a condition; W5-S3, W5-S7, W5-S14 and S7 re-homed. All 8 remediation rows read state OPEN before this commit.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "commit f70677780a",
        "remediations/REMEDIATION_v2.Z.md W3-S11; the other 7 rows across REMEDIATION_v1..v5",
        "ledger/ROUND_ANALYSIS.round8.md ruling 6"
      ]
    },
    "disposition": "GRADUATED"
  }
]
```

-- 3.0.0_SA_CVO~RV
