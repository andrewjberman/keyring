# IRPT_DASHBD: CVO adjudication, round 123 (workstream B-IN, ~I2): the Inflection Scope feed adapter

<sweep_watermark>2026-10-15T19:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:58Z, on msg 8604 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND123_BIN_DRAIN_END_20261015.md` @af7c5bccc6, blob dd12a99d45). Not B-49F's round 123, which is ADJUDICATION_v88. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-10 (LOCAL; worker ~310; merged @90862adf60). No judgment criterion. Re-run here: DBI123-1-AC1..AC3, 3 of 3 PASS (rc 0); proof VALID; `round-close-check --round 123 --workstream B-IN` MAY-CLOSE. Read beside the CTO's ADDENDUM 6 (msg 8605, @2a241c37da), which ruled the six issuer decisions after the drain, and the 0.4.1 order in the CTO's B-49F rounds 133-137 analysis. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S41",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:58:00Z",
  "one_line": "Round 123 B-IN (~I2): data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py (standard library only, no I/O) and its 22 tests. 3 of 3 PASS re-run. (1) VALUES THAT EXIST ONLY IN ~I2's CODE. The contract at HEAD is still 0.4.0, and its enums carry none of the adapter's reason classes. NO_FEED_ROW, INCOMPLETE_WINDOW and NO_EOD_VALUE exist ONLY in this module (constants at lines 16-19). They are neither in contract 0.4.0 nor in the CTO's 0.4.1 order, whose reason_class lists NO_GROUP, GROUP_NO_SERIES, NO_START_DATE_AT_SOURCE, SERIES_ENDED_AT_SOURCE and UNMAPPED_ACCOUNT. UNMAPPED_ACCOUNT is in the 0.4.1 order but not yet in any landed contract. The feed status word RETURNED is the feed's own vocabulary, not a contract value. No four-postulate record and no word-boundary token census exists for the three: none in ~310's folder, and none in the packet. That is against rule 24 and against split rule 1, since only ~D2 writes the contract's vocabulary. The CTO's ADDENDUM 6 (3) has since ruled them 'proposed' until ~D2's 0.4.1 record admits them. The module, merged before that ruling, does not yet mark them proposed in its manifest (it has absent_by_reason only). (2) INFERRED EOD. market_value_eod is the next calendar day's start value. Its claim is carried ONLY as free prose in the run manifest (market_value_basis: 'INFERRED, not carried by the feed...'). No row-level field carries it, and no enum value a consumer can reject on. Under A_VALUE_MUST_CARRY_ITS_CLAIM a reader of the table cannot reject an inferred value mechanically. ADDENDUM 6 (2) accepts 'inferred' in the manifest until the first real-row run measures startValue(t+1) against endValue(t). (3) ABSENT BESIDE THE ROWS. The records are {account_id, source_account_id, business_date, reason_class} with no status field. For UNMAPPED_ACCOUNT the adapter writes account_id = the Orion key string and source_account_id = None (line 92). That is the INVERSE of the 0.4.1 order, under which account_id is nullable only for UNMAPPED_ACCOUNT and then source_account_id is required. It is consistent with ADDENDUM 6 (6), which makes the dimension's key the Orion id string. ~D2's 0.4.1 must settle the shape: either the unmapped key goes to source_account_id with account_id null, or the order's clause changes. (4) REPO-ONLY: the merge adds only the module and its test under data/ (587 lines, 3 files with the record); there is no source-map entry and no AWS call or deploy. Rows: D2-W310-S1 (ARMED, owner ~I2: holdings_price_return_reason None beside a null return) is DISARMED by D2-S93 (~I2), grounded: the column is nullable in 0.4.0, and the CTO's ADDENDUM 6 (5) accepts it. D2-W310-S2 (a repeated key read as the last one, silently; carried into round 124's wrapper), S3 and S4 are inert, accepted.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W310-S1",
   "IRPT_DASHBD-D2-W310-S2",
   "IRPT_DASHBD-D2-W310-S3",
   "IRPT_DASHBD-D2-W310-S4",
   "IRPT_DASHBD-D2-S93"
  ],
  "spec_asserts": "CLAUDE.md rule 24 (a value enum arrives with its four-postulate record and token census); split ruling rule 1 (one contract writer, ~D2); A_VALUE_MUST_CARRY_ITS_CLAIM (a field a consumer can reject on).",
  "world_is": "A tested, I/O-free adapter maps the Scope feed to contract-0.4.0 rows plus a beside-list of ABSENT records. Three of its reason classes and the unmapped-row shape are ahead of, or inverse to, the contract ~D2 has not yet written (0.4.1). Nothing is deployed. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:5xZ: DBI123-1-AC1..AC3 PASS rc 0; proof-of-spec-check VALID rc 0 on ~310; round-close-check --round 123 --workstream B-IN verdict=MAY-CLOSE",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py lines 15-19 (constants), 25-28 (MARKET_VALUE_BASIS), 48-49 (_absent shape), 92 (UNMAPPED record), 168-179 (manifest)",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD: contract_version 0.4.0, enums without any reason_class",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_133_TO_137_20261015.md lines 22-29 (0.4.1 order); CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md ADDENDUM 6 lines 157-173 (msg 8605)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~310/: no four-postulate or token-census text; git diff 90862adf60^1 90862adf60 under data/ infra/ lib/ org/standards/: the module and its test only; lambda-source-map.json: 0 mentions",
    "investigation rows D2-W310-S1..S4, D2-S93",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND123_BIN_DRAIN_END_20261015.md blob dd12a99d45 (msg 8604)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One ARMED row disarmed by its owner on a grounded and CTO-accepted reading, and three inert rows. The rule-24 gap, the manifest-only inferred claim and the inverse unmapped shape are named for ~D2's 0.4.1 and the CTO, not repaired here."
 }
]
```
