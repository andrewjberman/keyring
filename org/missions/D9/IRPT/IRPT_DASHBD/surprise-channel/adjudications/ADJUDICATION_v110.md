# IRPT_DASHBD: CVO adjudication, round 125 (workstream B-IN, ~I2): the adapter and wrapper on contract 0.4.1

<sweep_watermark>2026-10-15T21:35Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T21:35Z, on msg 8677 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND125_BIN_DRAIN_END_20261015.md` @63cbe51c57, blob b552fdb66b). Not B-49F's round 125, which is ADJUDICATION_v89. Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-i-12 (LOCAL; worker ~312; merged @7a8a2f681f). No judgment criterion. Graded on the LANDED tree (HEAD 06f471310e, contract 0.4.1): DBI125-1-AC1..AC3, 3 of 3 PASS (rc 0); the three test files (adapter, wrapper, contract 0.4.1) 93 passed; proof VALID; round-close MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S47",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T21:35:00Z",
  "one_line": "Round 125 B-IN (~I2): the Scope adapter and run wrapper moved to contract 0.4.1, green on trunk. THE CTO'S CONDITION FOR ROUND 124 (msg 8656: B-IN round 124 closes only when round 125 lands green on trunk) IS MET: 3 of 3 PASS and 93 tests green at HEAD. v105's round can close on that condition. Round 124's own criteria do not pass on trunk: DBI124-1-AC1..AC3 now read FAIL, all three, since they grade the 0.4.0 shapes. They are superseded by checks/r125, not repaired, as the packet discloses; the round closes on the CTO's condition, not on its own criteria. THE CTO'S THREE ROUND-125 ADDITIONS ARE ALL PRESENT. (a) The stale 'proposed' marks are removed: 0 occurrences of 'proposed' in the adapter or the wrapper. (b) market_value_eod_claim is present: each adapter row carries it (adapter:188; ABSENT rows None at :60), and the wrapper places it in the run record as claim_placement RUN_RECORD with market_value_eod_claim_counts until the contract declares it, then TABLE (run.py:26, :166-168). (c) W311-S1's disarm is a criterion: p125_run041.py requires trading_days_unaccounted == 0 on both edge-day fixtures (:221) and on the chain fixture (:265), and it passes here; D2-S97 (~I2) records the disarm and is GROUNDED. TWR vs VENDOR_REPORTED is a SEQUENCING FACT, NOT A DEFECT. Contract 0.4.1 at HEAD still sets source_requires {orion: {return_basis: VENDOR_REPORTED}}, so the module writes VENDOR_REPORTED and is correct for the file that exists. The CTO's msg 8674/8675 moves Orion rows to TWR with source orion in contract 0.4.2, which has not landed. The module OWES A FLIP to TWR, and the claim into the table, when 0.4.2 lands. D2-W221-S3 stays ARMED (owner ~I2), its premise reversing with 0.4.2. W311-S2..S6 STILL HAVE NO OWNER and no disposition row. Their substance is answered in code at HEAD: S4 (dimension keys refused, duplicate or non-canonical: run.py:101), S5 (partition keys refused when a row names another pull date: :112), S6 (a non-empty or non-directory out_dir refused: :82, :86) and S2 (repeated keys refused with a count: :120). S3 (account counts omit an account whose every row was dropped) is only partly answered: W312-S4 records that the adapter still counts feed-row accounts only. This seat dismisses S2, S4, S5 and S6 on that code evidence, and leaves S3 open; it is inert with no owner. Worker rows W312-S1..S4 are inert, accepted. Nothing is deployed: repo modules only, with no source-map entry (v105).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W311-S1",
   "IRPT_DASHBD-D2-S97",
   "IRPT_DASHBD-D2-W311-S2",
   "IRPT_DASHBD-D2-W311-S4",
   "IRPT_DASHBD-D2-W311-S5",
   "IRPT_DASHBD-D2-W311-S6",
   "IRPT_DASHBD-D2-W312-S1",
   "IRPT_DASHBD-D2-W312-S2",
   "IRPT_DASHBD-D2-W312-S3",
   "IRPT_DASHBD-D2-W312-S4"
  ],
  "spec_asserts": "Spine L9/L10: a round is graded on the landed tree; a disarm is graded on its evidence; a hazard row carries an owner or a disposition.",
  "world_is": "The Inflection adapter and wrapper are green on trunk against contract 0.4.1, with ABSENT rows in the table and no edge-day loss. A flip to TWR is owed when 0.4.2 lands. Nothing is deployed and no real-row run has happened. FWD-2 for Inflection is not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run on the landed tree 2026-10-15T21:3xZ (HEAD 06f471310e): DBI125-1-AC1..AC3 PASS rc 0; pytest adapter, wrapper and contract-041 tests: 93 passed; DBI124-1-AC1..AC3 FAIL (superseded)",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py:60, :188; inflection_scope_feed_run.py:26, :82, :86, :101, :112, :120, :166-168 (0 occurrences of 'proposed')",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r125/p125_run041.py:144, :221, :265",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD: 0.4.1, source_requires orion VENDOR_REPORTED",
    "investigation rows D2-W311-S1..S6, D2-W312-S1..S4, D2-S97, D2-W221-S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/IRPT_DASHBD_ROUND125_BIN_DRAIN_END_20261015.md blob b552fdb66b (msg 8677)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W311-S1 is disarmed by a passing criterion. W311-S2, S4, S5 and S6 are answered by refusals in the code at HEAD, and W312-S1..S4 are inert. W311-S3 stays open (inert, partly answered), and W221-S3 stays ARMED for the 0.4.2 flip."
 }
]
```
