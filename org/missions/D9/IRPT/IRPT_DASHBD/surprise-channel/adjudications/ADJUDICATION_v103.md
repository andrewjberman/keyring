# IRPT_DASHBD: CVO adjudication, round 137 (workstream B-49F, ~D2): the unreported-day statement and the account_return_daily contract 0.4.0 (L9)

<sweep_watermark>2026-10-15T19:35Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:35Z, on msg 8575 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md` @e7b2e022cc, blob 1b1f31d9cf; one packet covers rounds 133-137, adjudicated as v99-v103, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Two orders: TO-DB-b-269 (WORLD by its infra path; worker ~218; merged @d6bc5ecbee) and TO-DB-b-270 (LOCAL; worker ~219; merged @ef923dab52). Re-run here: DB137-1-AC1..AC3 and DB137-2-AC1..AC3, 6 of 6 PASS (rc 0); both proofs VALID; round-close MAY-CLOSE (judgment=0). **L9: TO-DB-b-270 declares no <criterion> of kind JUDGMENT; its prose says 'the CVO grades it at L9', so round-close cannot see this grade. This seat grades the change against the CTO's ruling (round-118 ADDENDUM 4 @10e1032651, msg 8546). VERDICT: FAIL (narrow).** The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S40",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:35:00Z",
  "one_line": "Round 137 B-49F. DB-b-269: the report-build handler states 'N trading days not reported by the source (dates)' and the windows that hold each; 33 tests; nothing deployed. DB-b-270, account_return_daily CONTRACT 0.4.0, graded at L9 against ADDENDUM 4's four terms, read at the merge ef923dab52. VERSION: not a regression. 0.4.0 is IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json (0.1.0 -> 0.2.0 -> 0.3.0 -> 0.4.0). The 0.5.x of v82/v84 is a different file, IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json (0.5.4). WRITER: every commit to the file since the split is ~D2's (its workers ~194 and ~219 under ~D2 orders); the two earlier commits (2026-09-30, 10-01) were ~P's before the split. Rule 1 holds. TERM 1 MET: external_flow and income_received stay nullable false with nullable_when {source: orion, flow_claim: absent}. flow_claim is an optional string, values [absent], reason exactly 'vendor-reported return, not built from flows', and its rule says a consumer that needs flows rejects in words and never reads null as zero. schema_hash 1b25d37b... is unchanged; the 0.3.0 entry with hash bc70ee2f... sits in supersedes; the contract-reading tests pass (64 run here). TERM 4 MET: the contract and its test land in ONE commit, 5f91315a60. TERM 2 and TERM 3 NOT EXPRESSIBLE, hence FAIL. source_rules.orion says an unmapped Orion account 'is written as an ABSENT row with reason class UNMAPPED_ACCOUNT', and that an ABSENT trading-day factor 'stays ABSENT'. But the contract's enums hold no ABSENT and no UNMAPPED_ACCOUNT (day_quality: MEASURED, FLOW_UNRECONCILED, LARGE_FLOW, NOT_MEASURABLE, SOURCE_LAG; return_basis: TWR, NOT_MEASURABLE), and no column carries a row-level reason. account_id is nullable false, while source_account_id's rule forbids a guessed id for an unmapped account, so an unmapped row cannot both validate and say why. A consumer therefore cannot reject on UNMAPPED_ACCOUNT, against A_VALUE_MUST_CARRY_ITS_CLAIM. CLAIM CLASS, for the CTO: the contract's own test writes an Orion row as day_quality MEASURED and return_basis TWR. A vendor-reported return is then labelled as an Opal measurement; only the row-level source column (orion) lets a consumer tell them apart. Fix: a 0.4.1 adding the reason value or column for ABSENT/UNMAPPED_ACCOUNT and saying how an Orion return states its basis. W219-S1 DISPOSED as resolved on the evidence. Amendment 1 (f8c18a0e87) names its gate limb ('none graded') and grants the one Cottonwood adapter test. The edit (131b4189c3) is 2 added, 1 removed: the adapter's 20-field hash is now asserted against the supersedes 0.3.0 entry, which is right because the adapter stays a 0.3.0 writer (CONTRACT_VERSION 0.3.0) and the assertion still binds it to the contract. Those tests pass here.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W219-S1",
   "IRPT_DASHBD-D2-W219-S2"
  ],
  "spec_asserts": "CTO round-118 ADDENDUM 4 @10e1032651 terms 1-4; A_VALUE_MUST_CARRY_ITS_CLAIM (a field a consumer can reject on); rule 1 of the split ruling (one contract writer, ~D2); spine L9: a judgment is graded by the CVO, never self-graded.",
  "world_is": "Contract 0.4.0 lets an Orion row carry null flows with a claim, and every 0.3.0 writer still validates. It cannot express an ABSENT or UNMAPPED_ACCOUNT Orion row that its own rules require, so ~I2's adapter cell, cut on 0.4.0, has no valid form for an unmapped account or an absent trading day.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:2xZ: DB137-1-AC1..AC3, DB137-2-AC1..AC3 PASS rc 0; proofs VALID rc 0 on ~218, ~219",
    "git show ef923dab52:org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json: columns, optional_columns, enums, source_rules.orion, supersedes",
    "git log on the contract file: 10939bbfa4, 6a23aee53d (~P, pre-split), 535bbf00cd (~D2), f5fec2bb6d (~194), 5f91315a60 (~219)",
    "pytest test_cottonwood_bd_account_return_daily.py, test_cottonwood_report_reader.py, test_account_return_contract_040.py: 64 passed",
    "git show f8c18a0e87 (Amendment 1, gate limb stated); git show 131b4189c3 (+2/-1)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md lines 113-139; CTO msg 8546",
    "investigation rows D2-W219-S1, D2-W219-S2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md blob 1b1f31d9cf (msg 8575)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W219-S1 is resolved by an amendment whose edit is minimal, correct and green here; W219-S2 is its record. The L9 FAIL on contract 0.4.0 terms 2 and 3 is a grade for the CTO and ~D2, not a row repair.",
  "notes": "L9 JUDGMENT GRADE, TO-DB-b-270 L9 (CTO ADDENDUM 4, order line 18): FAIL (terms 1 and 4 met; terms 2 and 3 not expressible: no ABSENT or UNMAPPED_ACCOUNT enum value or reason column, and account_id is non-nullable for an unmapped Orion account)."
 }
]
```
