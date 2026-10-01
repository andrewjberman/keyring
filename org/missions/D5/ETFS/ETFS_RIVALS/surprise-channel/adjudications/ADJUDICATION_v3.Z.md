# ETFS_RIVALS -- round 3 L8/L9 adjudication (site-Z fabric)

<sweep_watermark>2026-10-01T11:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO~RV, 2026-10-01 ~12:1xZ. L8 packet: 2.0.0_SA_COO~RV msg 27797 (acked), `deliverables/2.0.0_SA_COO~RV/round3/DRAIN_END_READ_ROUND3.md` @058d094e4a. Source: 1.0.0_SA_CTO~Z round-2 analysis @01114ae8a8 (and its amendment 1 to ruling 1). Review: `org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md` (co-committed).

Round 3: 6 of 6 orders terminal; ledger `etfs-rivalfunds-round3` CLOSED. Round 3's rows are the 28 surfaced after 2026-10-01T05:09Z, through 11:25Z (94 in the channel minus 66). Disposition: 21 dismissed by the 4 rows below, 7 graduated in `remediations/REMEDIATION_v3.Z.md` (W1-S27, W4-S2, W4-S5, W3-S15, S6, S7, W4-S1). In the same commit, five earlier remediation rows advance their own clocks in place (REMEDIATED; W2-S4 also DISARMED): v1 S1 and W1-S5, v2 W2-S4, W1-S8 and W5-S28. Ruling 9 of the round-2 analysis remains the disarm record for v1 W5-S12.

```json
[
  {
    "id": "ETFS_RIVALS-Z-C-S10",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T12:10:00Z",
    "one_line": "Every round-3 ARMED or BLOCKING hazard is disarmed, re-read by this seat: S8 (identity moved BASG trades; served delta now 0/0), W1-S17 (runtime parse replaced by constants and a drift test), W2-S8 (held funds read 'Trades held'), and S4 (the W2-S4 premise, retracted).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-S8",
      "ETFS_RIVALS-Z-W1-S26",
      "ETFS_RIVALS-Z-W1-S17",
      "ETFS_RIVALS-Z-W1-S21",
      "ETFS_RIVALS-Z-W2-S8",
      "ETFS_RIVALS-Z-W2-S10",
      "ETFS_RIVALS-Z-S4"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S8/W1-S26: deliverables/0.9.0_WK_ETFS_RIVALS~4/d4_live.json gates.1 reads 'PASS: served_delta_r3.py ... BASG and CGIC ETFT INEQ PCLG SCHY TXUE 0/0, BIDD 2/1, TSEL 0/6, WCMG 0/1, IDVZ 0/33 and PFOE 0/18 (home) -- 12 of 12 funds inside the COO half's table'. The BASG delta that read 1489 added / 322 removed before the fix now reads 0/0. W1-S17/W1-S21 and W2-S8/W2-S10: this seat's run of `python -m pytest data/etfs/scripts/rivalfunds/tests -q` reads 249 passed, 2 skipped, 0 failed; the served manifest names no held fund today. S4: silver_issuer.py at HEAD retains a superseded object (:240-247 mark it retained; no delete call; the one DeleteObject match is the comment at :240), and d-4's live AC2 control re-captured BASG 2026-09-29 with both silver objects retained and marker OK.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-S8, W1-S26, W1-S17, W1-S21, W2-S8, W2-S10, S4",
        "d4_live.json gates.1 (read by this seat)",
        "this seat's package run: 249 passed, 2 skipped, 0 failed",
        "this seat's get of s3://opal-data-etfs/rivalfunds/etfs/platinum/page/date=2026-10-01/manifest.json: status published, generated_at 2026-10-01T11:16:08Z, funds_total 13, funds_updated 12, not-updated ['PFOE/GQGU']",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each hazard is closed at HEAD and in the bucket. W1-S27 (TSEL 0/6, WCMG 0/1 in the same delta) is a separate cause and graduates."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S11",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T12:10:00Z",
    "one_line": "Six in-round repairs leave nothing open: three issuer check defects fixed with expectations unchanged (W2-S6, W4-S3, W4-S4), two stale tests replaced by a drift test (W1-S22, W1-S24), and freshness computed in publish_page (W2-S7).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S6",
      "ETFS_RIVALS-Z-W4-S3",
      "ETFS_RIVALS-Z-W4-S4",
      "ETFS_RIVALS-Z-W1-S22",
      "ETFS_RIVALS-Z-W1-S24",
      "ETFS_RIVALS-Z-W2-S7"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Packet :10, :15, :54: r-3.AC2 (W2-S6), d-4.AC1 (W4-S4) and d-4.AC2 (W4-S3) were fixed in the issuer's own instruments with expectations unchanged, and each re-ran PASS. W1-S24 records the two obsolete hp-1 tests deleted under g-6 amendment 1, and the suite is green (this seat: 249 passed). W2-S7: publish_page carries the per-source trading-day freshness; guardrails.report_date_freshness no longer reaches a fund's page result.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S6, W4-S3, W4-S4, W1-S22, W1-S24, W2-S7",
        "DRAIN_END_READ_ROUND3.md:8-17, :54-55",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Repaired in round. W2-S7 leaves a dead path (the guardrails function and its 0 config value); the review names it P2, but it is not a hazard."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S12",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T12:10:00Z",
    "one_line": "Four recorded decisions inside the grant: W2-S9 (the hold is share-changing actions only), W1-S18 (landing folder date is not the report date, handled), W1-S23 (distinct-id candidate counting), W4-S6 (scheduled producers inside the act window).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W2-S9",
      "ETFS_RIVALS-Z-W1-S18",
      "ETFS_RIVALS-Z-W1-S23",
      "ETFS_RIVALS-Z-W4-S6"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W2-S9 matches the round-2 analysis's ruling 2 ('a corporate action that needs the pull's enrichment'): income events move only the income label and never a share count, so holding on them would hold nearly every fund daily (4781 G3 events). W1-S18: G1 reads each row's own report date, and the 27-landing replay gives 23 report dates. W1-S23: two counting choices, measured 1.0 on the real window. W4-S6: the 07:00 ET fetch and the 11:13Z Bloomberg leg wrote inside the act window as declared writers; the last publish marker (d4-publish-r3b) names only GQGU.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W2-S9, W1-S18, W1-S23, W4-S6",
        "ledger/ROUND_ANALYSIS.round2.md ruling 2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ETFS_RIVALS_R3_REVIEW_20261001.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Legal and recorded; W2-S9's reading agrees with the ruling's own words."
  },
  {
    "id": "ETFS_RIVALS-Z-C-S13",
    "project": "ETFS_RIVALS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~RV",
    "surfaced_at": "2026-10-01T12:10:00Z",
    "one_line": "Four rows are carried by graduated items rather than graduated twice: W1-S20 (home rows resolve 0.0) by W4-S2, W1-S19 and W1-S25 (revision ordering) by v2 W1-S11 and W4-S5, and S5 (GQGU has no reader) by its own correction S6.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "ETFS_RIVALS-Z-W1-S20",
      "ETFS_RIVALS-Z-W1-S19",
      "ETFS_RIVALS-Z-W1-S25",
      "ETFS_RIVALS-Z-S5"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "remediations/REMEDIATION_v3.Z.md carries W4-S2 (identity floor, citing W1-S20) and W4-S5 (G4 newest-by-name, citing W1-S19/W1-S25), and REMEDIATION_v2.Z.md carries W1-S11 (revision ties) OPEN for round 4 per analysis ruling 7. S6 corrects S5's premise (GQGU HAS a measured issuer route) and graduates.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) ETFS_RIVALS-Z-W1-S20, W1-S19, W1-S25, S5",
        "remediations/REMEDIATION_v3.Z.md (co-committed); REMEDIATION_v2.Z.md @98b3262aa2"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "One item, one remediation row."
  }
]
```
