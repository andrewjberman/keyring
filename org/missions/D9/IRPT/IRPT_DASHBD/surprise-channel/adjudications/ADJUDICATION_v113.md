# IRPT_DASHBD: CVO adjudication, round 142 (workstream B-49F, ~D2): the account_return_daily contract 0.4.2 (L9)

<sweep_watermark>2026-10-15T23:08Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T23:08Z, on msg 8737 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND142_144_B49F_DRAIN_END_20261015.md` @162f5530dc, blob f1f543cacc; one packet covers rounds 142 and 144, adjudicated as v113 and v114). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-275 (LOCAL; worker ~223; merged @6ac152c83a). Re-run on the landed tree: DB142-1-AC1..AC3, 3 of 3 PASS (rc 0); round-close MAY-CLOSE (judgment=0). **L9: graded here against both CTO orders, the round-124 analysis item 2 and the rounds 138-141 analysis ruling 1-4. VERDICT: PASS.** This grade gates the B-IN adapter's 'done' (CTO round-127 analysis). ROUND 143 EXISTS: issued @ddaafb7971 as the one order TO-DB-b-276 (the chain-cap code-update apply) to 0.7.0_AE_CloudOps~DB2. It is `pending`, so no packet is owed yet. The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S50",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T23:08:00Z",
  "one_line": "Round 142 B-49F: contract 0.4.2, read at its merge 6ac152c83a (HEAD unchanged since). ORDER 1 (round-124 analysis item 2): one nullable column market_value_eod_claim, enum measured | inferred, required on Orion rows, with its rule-24 record. MET. It is an optional string, nullable, values [measured, inferred], required on every PRESENT Orion row and null on an ABSENT row. That narrows 'required on Orion rows' to rows that carry a value, and an ABSENT row has no end value to claim about, so it is coherent. ORDER 2 (rounds 138-141 ruling 1-4): (1) VENDOR_REPORTED out of return_basis: MET (enum TWR | NOT_MEASURABLE; source_requires removed). (2) Orion rows TWR: MET (source_rules.orion.return_basis). (3) Provenance STAYS IN source, with no new provenance column: MET. source_provenance is NOT a column. It is a TOP-LEVEL contract key: text mapping each value of source to its provenance (orion: vendor-computed; the two Black Diamond and custodian values: Opal-computed). The column lists (19 columns; optional source, flow_claim, source_account_id, row_status, reason_class, market_value_eod_claim) hold no source_provenance. So the premise 'a column source_provenance was added' does not hold. The map is exactly the 'contract text plus a test' the ruling asked for: test_source_requires_is_gone_and_source_provenance_maps_each_source_value (test_account_return_contract_042.py:230). RULE 24 (ii)/(iii): one axis per column. return_basis is method (TWR | NOT_MEASURABLE, the latter a pre-0.4.1 state, out of scope by the ruling); source is provenance; market_value_eod_claim is the claim on the end value. No two columns share an intent; the v108 FAIL is cured. (4) Removal shown by subtraction: rule24_record.v042 states it. RULE-24 RECORD AND CENSUS: present (v042 i-iv, token_census at 198f2591f0 over 920 files, 3 tokens, recounted by DB142-1-AC2). The 1,312 'measured' hits were sampled, not each read, which the record says. ONE DRAIN: the CTO's rule ('from now on a contract change and its writer land in ONE merge') was issued in the round-127 analysis at 2026-10-15T22:40:18Z, after both merges. 0.4.2 (21:52:40Z) and its writer (c7d980af1b, 22:25:04Z) landed in two drains, 32 minutes apart (v112). The rule binds the next contract change, not this one, so this is not a FAIL; it is named. WRITER: 6ac152c83a is ~D2's drain of its worker ~223; split rule 1 holds. Rows: D2-W223-S1 (the adapter already wrote the claim) is inert. D2-W223-S2 (BLOCKING: 0.4.1's tests failed under 0.4.2) is resolved by D2-W223-S3 (Amendment 1 @e61247310c) and D2-W223-S4 (Amendment 2, the iii repair). Grounded: the 0.4.1 test file passes here (31).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W223-S1",
   "IRPT_DASHBD-D2-W223-S2",
   "IRPT_DASHBD-D2-W223-S3",
   "IRPT_DASHBD-D2-W223-S4"
  ],
  "spec_asserts": "CTO round-124 analysis item 2; CTO rounds 138-141 analysis rulings 1-4; CLAUDE.md rule 24 (ii)/(iii) and the rule-24 record; split ruling rule 1; spine L9: graded by the CVO, never self-graded.",
  "world_is": "Contract 0.4.2 carries the end-value claim as a column, removes VENDOR_REPORTED, and keeps provenance in source with a text map and a test. The B-IN adapter's 'done' gate on this grade is now met (the adapter conforms: v112).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T23:0xZ: DB142-1-AC1..AC3 PASS rc 0; test_account_return_contract_041.py 31 passed",
    "git show 6ac152c83a:org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json: optional_columns, enums.return_basis, top-level source_provenance, source_rules.orion.return_basis, rule24_record.v042",
    "data/assets/scripts/gold/irpt_reporting/tests/test_account_return_contract_042.py:230",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_138_TO_141_20261015.md lines 20-39; CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_124_20261015.md lines 24-27; CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_127_20261015.md line 15 (@c9effc13f4, 2026-10-15T22:40:18Z)",
    "investigation rows D2-W223-S1..S4",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND142_144_B49F_DRAIN_END_20261015.md blob f1f543cacc (msg 8737)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W223-S2 is resolved by two amendments and green here, and W223-S1, S3 and S4 are inert or records. The L9 verdict on contract 0.4.2 is PASS.",
  "notes": "L9 JUDGMENT GRADE, TO-DB-b-275 (CTO round-124 item 2; rounds 138-141 rulings 1-4): PASS. source_provenance is contract text (a top-level map with a test), not a column; one intent per column."
 }
]
```
