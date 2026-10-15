# IRPT_DASHBD: CVO adjudication, round 127 (workstream B-IN, ~I2): the Scope feed module on contract 0.4.2

<sweep_watermark>2026-10-15T22:36Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T22:36Z, on msg 8727 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND127_BIN_DRAIN_END_20261015.md` @7f45aff1dc, blob f7407dae15). Not B-49F's round 127, which is ADJUDICATION_v91. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-14 (LOCAL; worker ~314; merged @c7d980af1b): the TWR-flip cell the CTO's msg 8696 named. No judgment criterion. Graded on the LANDED tree (HEAD 74b2e2ee0e, contract 0.4.2): DBI127-1-AC1..AC3, 3 of 3 PASS (rc 0); adapter, wrapper and contract-042 tests 90 passed; proof VALID. Contract 0.4.2 itself is ~D2's and is NOT graded here; only the module's conformance to it is. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S49",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T22:36:00Z",
  "one_line": "Round 127 B-IN (~I2): the Scope adapter and wrapper conform to contract 0.4.2. 3 of 3 PASS and 90 tests green on trunk. THE CTO'S FOUR ITEMS: (1) return_basis TWR with source orion: MET. 0 occurrences of VENDOR_REPORTED in either module; the adapter writes TWR on PRESENT rows (adapter:20, :194) and NOT_MEASURABLE on ABSENT rows (:65). Contract 0.4.2's return_basis enum is now TWR | NOT_MEASURABLE, with source_requires gone and provenance stated in source_provenance (orion: vendor-computed). That is the method/provenance split v108 asked for. (2) market_value_eod_claim as a contract column: MET. It is declared in 0.4.2's optional columns, and the module writes it in the table, inferred or measured on PRESENT rows and null on ABSENT rows. (3) contract_version 0.4.2: MET, read from the contract file, not typed. (4) W311-S3 count fix: MET. The new test test_an_account_seen_only_on_a_dropped_day_is_still_counted passes; this closes the S3 that v110 left open. THE 93 -> 90: no module test was lost. Round 125's 93 were the adapter, the wrapper and test_account_return_contract_041.py (31); round 127's 90 are the adapter, the wrapper and test_account_return_contract_042.py (27). The module's own tests went from 62 to 63. Removed and replaced: test_present_row_carries_vendor_reported_and_row_status_present becomes ..._twr_..., and test_mapped_absent_row_takes_the_full_0_4_1_shape becomes ..._0_4_2_shape. The two run-record claim tests (test_the_claim_sits_in_the_run_record_while..., test_the_claim_sits_in_the_table_when...) become three: the claim as a declared column, a contract copy without the claim refused, and the W311-S3 count. test_account_return_contract_041.py still exists and still passes (31). No r127 criterion relied on a removed test, so coverage is not lowered. THE RED GAP: contract 0.4.2 merged at 6ac152c83a (2026-10-15T21:52:40Z) and the module merged at c7d980af1b (22:25:04Z). Trunk carried the 4 red module tests for 32 minutes 24 seconds, across about 20 first-parent commits by other seats. Nothing deployed runs the module: there is no source-map entry and the Inflection gold prefix is empty (v105). The only round graded in that window, round 126 (DB-i-13), reads silver and the saved bodies, not the module. Round 125's own criteria were already superseded by checks/r127. Rows: D2-S98 (~I2) disarms D2-W221-S3 (ARMED: TWR against VENDOR_REPORTED). GROUNDED: the module writes TWR and 0.4.2 no longer holds VENDOR_REPORTED. W311-S3 (inert, open in v110) is closed by its test. Correction to v111's slug: v111 @a7c4ed69e5 was LOCAL at send, not on origin (re-read here).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W221-S3",
   "IRPT_DASHBD-D2-S98",
   "IRPT_DASHBD-D2-W311-S3"
  ],
  "spec_asserts": "Spine L9/L10: a round is graded on the landed tree; a disarm is graded on its evidence; a test count change is explained by name, never by total.",
  "world_is": "The Inflection Scope module writes contract-0.4.2 rows (TWR, provenance in source, the claim in the table) and is green on trunk. Nothing is deployed and no real-row run has happened; it waits on ~P2's feed apply. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run on the landed tree 2026-10-15T22:3xZ (HEAD 74b2e2ee0e): DBI127-1-AC1..AC3 PASS rc 0; pytest adapter + wrapper + contract-042: 90 passed; contract-041: 31 passed; proof-of-spec-check VALID rc 0 on ~314",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py:20, :65, :194; grep VENDOR_REPORTED in both modules: 0",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD: 0.4.2; return_basis [TWR, NOT_MEASURABLE]; optional market_value_eod_claim; source_requires absent; source_provenance present",
    "test lists at 7a8a2f681f vs HEAD (def names): adapter 34 -> 34 (2 renamed), wrapper 24 -> 25 (2 replaced by 3)",
    "git log: 6ac152c83a 2026-10-15T21:52:40Z; c7d980af1b 2026-10-15T22:25:04Z",
    "investigation rows D2-W221-S3, D2-S98, D2-W311-S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND127_BIN_DRAIN_END_20261015.md blob f7407dae15 (msg 8727)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W221-S3 is disarmed by S98 on grounded evidence, and W311-S3 is closed by its new passing test. The 32-minute red gap ran nothing deployed and is named."
 }
]
```
