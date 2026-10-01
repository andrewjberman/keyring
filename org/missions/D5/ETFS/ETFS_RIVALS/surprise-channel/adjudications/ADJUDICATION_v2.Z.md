# ETFS_RIVALS -- round 2 L8/L9 adjudication (site-Z fabric)

<sweep_watermark>2026-10-01T05:09Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01 ~05:5xZ. L8 packet: 2.0.0_SA_COO~RV msg 27541 (acked), `deliverables/2.0.0_SA_COO~RV/round2/DRAIN_END_READ_ROUND2.md` @d152231e55. Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md` (co-committed).

Round 2: 9 of 9 orders terminal. Round-1 rows are compiled in ADJUDICATION_v1.Z.md. Round 2's rows are the 37 surfaced after 2026-09-30T15:35Z, through Z-S3 at 05:09Z (66 in the channel minus 29). Disposition: 29 dismissed by the 4 rows below, 8 graduated in `remediations/REMEDIATION_v2.Z.md` (W2-S4 still ARMED, W1-S8, W1-S11, W3-S11, W3-S12, W5-S21, W5-S28, S2). This commit and the CTO message that cites it are the round's L10 slug.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S6",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T05:50:00Z",
    "one_line": "Three of the round's four ARMED rows are disarmed, re-read by this seat: W5-S24 (silver retains, no delete; markers on the new code), W5-S26 (the test asserts retain; package 189 passed), W3-S13 (the enrichment gate holds G5).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W5-S24",
      "ETFS_RIVALS-Z-W5-S25",
      "ETFS_RIVALS-Z-W5-S26",
      "ETFS_RIVALS-Z-S3",
      "ETFS_RIVALS-Z-W3-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W5-S24: data/etfs/scripts/rivalfunds/silver_bloomberg.py at HEAD holds no delete call (its one match, :13, is the docstring 'silver object is RETAINED'). state/build_bloomberg_silver/ holds import-r2-07 (04:16:06Z) and import-r2-08 (04:20:54Z), written after the 04:10Z apply. Residue, not a hazard: import-r2-04 and -05 carry no silver marker under date=2026-09-30, while their canonical_shape, trade_schedule and page markers exist (driven by replay). run_dag (sweep.py:282-343) walks only its own day's partition, so no later sweep revisits them. W5-S26/S3: this seat ran `pytest test_b1_bloomberg_channel.py -k latest_capture_wins` (1 passed) and the package (189 passed, 2 skipped, 0 failed). W3-S13: enrichment_gate at sweep.py:232, applied to GATED stages in run_dag :324-328.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W5-S24, W5-S25, W5-S26, S3, W3-S13",
        "this seat's list-objects-v2 of rivalfunds/etfs/state/{build_bloomberg_silver,build_canonical_shape,build_trade_schedule,publish_page}/ ~05:4xZ",
        "ledger 20261001T0043Z_etfs-rivalfunds-round2_deploy_completion.md: CLOSED (packet :20)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard is gone at HEAD and in the bucket. The fourth ARMED row, W2-S4, is NOT disarmed and graduates ARMED."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S7",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T05:50:00Z",
    "one_line": "Eight order-versus-estate mismatches were resolved in round and leave nothing open: W2-S2, W5-S22 (leg codes 90-97, disjoint from the price leg), W2-S3 (PY_AWS fallback), W5-S19 (the two red tests are green), W5-S27 (five hashes inside key 6), W5-S18 (937 captures), W5-S20 (act order), W3-S8 (all 13 unmapped dividend types ruled).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S2",
      "ETFS_RIVALS-Z-W5-S22",
      "ETFS_RIVALS-Z-W2-S3",
      "ETFS_RIVALS-Z-W5-S19",
      "ETFS_RIVALS-Z-W5-S27",
      "ETFS_RIVALS-Z-W5-S18",
      "ETFS_RIVALS-Z-W5-S20",
      "ETFS_RIVALS-Z-W3-S8"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "RIV-b-1 merged with the vehicle leg on codes 90-97 (3ac5a8666e message: 'the vehicle leg gated OFF with codes 90-97 (W2-S2)'), so the 80-83 collision W2-S2 named never shipped, and W5-S22 is the order text naming the old code. W2-S3's `if not defined PY_AWS` fallback is measured in the row. W5-S19's two red tests: this seat's package run reads 0 failed. W5-S27: five source_code_hash updates, one shared package, inside the signed key 6. W5-S18 and W5-S20 record a count and an act order that met the pair's stated constraints. W3-S8: issuer amendment ef6e9eb88d ruled every one of the 13 unmapped raw types before RIV-g-4 spawned (9 INCOME, Warrant SHARE-CHANGING, 3 IGNORED, any new type counted and filed), and g-4 merged with AC1-AC3 PASS.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S2, W5-S22, W2-S3, W5-S19, W5-S27, W5-S18, W5-S20, W3-S8",
        "git show ef6e9eb88d (TO-RIV-g-4 amendment 1: the W3-S8 type table)",
        "git show 3ac5a8666e (RIV-b-1 merge message)",
        "this seat's `python -m pytest data/etfs/scripts/rivalfunds/tests -q`: 189 passed, 2 skipped",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by the issuer's amendments or the merge; no live or forward residue."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S8",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T05:50:00Z",
    "one_line": "Fourteen documented build-time choices inside the grant, each with a consumer note and no open hazard: W2-S5, W3-S6, W3-S7, W3-S10, W3-S14, W1-S6, W1-S7, W1-S9, W1-S10, W1-S12, W1-S13, W1-S14, W1-S16, W5-S23.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S5",
      "ETFS_RIVALS-Z-W3-S6",
      "ETFS_RIVALS-Z-W3-S7",
      "ETFS_RIVALS-Z-W3-S10",
      "ETFS_RIVALS-Z-W3-S14",
      "ETFS_RIVALS-Z-W1-S6",
      "ETFS_RIVALS-Z-W1-S7",
      "ETFS_RIVALS-Z-W1-S9",
      "ETFS_RIVALS-Z-W1-S10",
      "ETFS_RIVALS-Z-W1-S12",
      "ETFS_RIVALS-Z-W1-S13",
      "ETFS_RIVALS-Z-W1-S14",
      "ETFS_RIVALS-Z-W1-S16",
      "ETFS_RIVALS-Z-W5-S23"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Each choice is documented in its module and row: modal report-date partition with per-row report_date (W2-S5); date_anomalies kept (W3-S6); the 9996651D cash class closed by W1-S10's rule (W3-S7); a split applied only where the holding moved (W3-S10, the 9 real JP splits); four G5/G6 constants (W3-S14); a single-fund page replaced by RIV-p-2 (W1-S6); fund_ticker as the shared key (W1-S7); suffixed position_id repeats (W1-S9); a selected-row rule (W1-S13); a periodic rule unexercised on real data (W1-S14); the page wrapper (W1-S16); bronze sidecars read for re-publication (W1-S12). W5-S23: the W3-S13 gate builds no new G5 for ANY fund, BASG included, on a morning with no pull-enrichment marker. This is the pair's accepted Branch B, not a regression.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S5, W3-S6, W3-S7, W3-S10, W3-S14, W1-S6, W1-S7, W1-S9, W1-S10, W1-S12, W1-S13, W1-S14, W1-S16, W5-S23",
        "DRAIN_END_READ_ROUND2.md:6-18 (every carrying order terminal, issuer re-run PASS)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R2_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Legal and recorded. Three carry a forward proof owed to real data, named in the review, not here: W3-S10's later-window branch, W1-S14's periodic rule on PFOE, and W5-S23's consequence that the 08:03 leg's sign-in gates every fund's daily G5."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S9",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T05:50:00Z",
    "one_line": "Two round-2 rows are the same items round 1 graduated: W3-S9 is W1-S4 (identity coverage) and W1-S15 is W1-S5 (the status of a published not-updated page).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W3-S9",
      "ETFS_RIVALS-Z-W1-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "remediations/REMEDIATION_v1.Z.md carries ETFS_RIVALS-Z-W1-S4 and ETFS_RIVALS-Z-W1-S5 OPEN with owner 1.0.0_SA_CTO~Z, and each cites its round-2 recurrence as evidence.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W3-S9, W1-S15",
        "remediations/REMEDIATION_v1.Z.md @7d90d0bfd8"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Carried by the open round-1 remediation rows; a second row would double-count one item."
  }
]
```
