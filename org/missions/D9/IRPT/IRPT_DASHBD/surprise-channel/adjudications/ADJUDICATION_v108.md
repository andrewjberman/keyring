# IRPT_DASHBD: CVO adjudication, round 140 (workstream B-49F, ~D2): the account_return_daily contract 0.4.1 (L9)

<sweep_watermark>2026-10-15T21:20Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T21:20Z, on msg 8662 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md` @90ac6e0037, blob 55a406ca98; one packet covers rounds 138-141, adjudicated as v106-v109, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). One order, TO-DB-b-273 (LOCAL; worker ~221; merged @754702eb15), plus ~D2's own rule-text fix @ef1c8ccaf2. Re-run here: DB140-1-AC1..AC3, 3 of 3 PASS (rc 0); round-close MAY-CLOSE (judgment=0). **L9: the order's prose says the CVO grades it (line 18), and there is no JUDGMENT <criterion>. This seat grades 0.4.1 at HEAD against the CTO's 0.4.1 order (rounds 133-137 analysis item 1) and rule 24. VERDICT: FAIL on rule 24 (iii) only.** The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S45",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T21:20:00Z",
  "one_line": "Round 140 B-49F: contract 0.4.1 graded at L9 against each element of the CTO's order. (1) row_status PRESENT | ABSENT: MET (optional column and enum; a null reads PRESENT for older writers). (2) reason_class: MET. Eight values: the order's five plus NO_FEED_ROW, INCOMPLETE_WINDOW and NO_EOD_VALUE, admitted under ADDENDUM 6 (3). Required when ABSENT, null otherwise, with one printed precedence. (3) account_id nullable ONLY for UNMAPPED_ACCOUNT (nullable_when) and source_account_id then REQUIRED: MET after ~D2's rule-text fix @ef1c8ccaf2, which removed the contradiction D2-W221-S1 found; market value and flows nullable on an ABSENT row (nullable_when_absent): MET. (4) Orion rows VENDOR_REPORTED: present, via source_requires {orion: {return_basis: VENDOR_REPORTED}}. (5) The rule-24 record with four postulates and a word-boundary token census: PRESENT, and the checker recounts 13 tokens over 915 files at ca3e3ded9a. (6) 0.3.0 writers still validate: MET (19 columns and schema_hash unmoved; 64 earlier contract-reading tests and 31 new pass). RULE 24 (iii) INTENT COHERENCE: FAIL on ~D2's one decision. The column's own meaning, unchanged in 0.4.1, is 'which arithmetic produced total_return_daily': a METHOD axis, with TWR as its value. VENDOR_REPORTED answers a different question, WHO computed it, which is PROVENANCE. The record's iii text quietly re-reads the column as 'whose arithmetic' to fit. The two are not exclusive: Orion's Scope figure is a chained daily factor, a time-weighted return computed by the vendor, so a vendor-reported TWR has no single correct value in this column. Once VENDOR_REPORTED is present, the column no longer says the method of an Orion row. Provenance is also already carried by source (orion), and source_requires makes VENDOR_REPORTED a pure function of source, so it adds no information while displacing the method. The enum's older NOT_MEASURABLE is a third intent, a measurability state; that predates 0.4.1 and is named, not graded here. Remedy for ~D2: keep return_basis as method (an Orion row reads TWR, or a method value the vendor states). Carry provenance in source, which already exists, or in a separate return_method column if the CTO wants a named one. The CTO's own term 'return_method: VENDOR_REPORTED' named a separate field, and that reading is the coherent one. WRITER: 969e41a3e7 is ~D2's worker under ~D2's order and ef1c8ccaf2 is ~D2, so rule 1 holds. ROWS: D2-W219-S1 was disposed resolved in v103 and is not re-disposed. D2-W221-S1 is RESOLVED: ef1c8ccaf2's text now matches required_when. D2-W221-S2 is RESOLVED in code: at HEAD the Scope adapter's ABSENT record carries row_status ABSENT, and an UNMAPPED_ACCOUNT record has account_id None and source_account_id set (inflection_scope_feed_adapter.py:48-51, :94; v105). The records still sit beside the table, which ADDENDUM 6 (1) says must end once 0.4.1 lands; that is carried by ~I2's round 125. D2-W221-S3 (ARMED, owner ~I2: the adapter writes TWR on Orion rows against source_requires) is HELD. The adapter still writes TWR at HEAD, and the right fix depends on the CTO's ruling on (iii) above.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W221-S1",
   "IRPT_DASHBD-D2-W221-S2"
  ],
  "spec_asserts": "CTO 0.4.1 order (CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUNDS_133_TO_137_20261015.md item 1); CLAUDE.md rule 24 (iii) one axis, one intent; split ruling rule 1; spine L9: a judgment is graded by the CVO, never self-graded.",
  "world_is": "Contract 0.4.1 can express ABSENT and UNMAPPED_ACCOUNT rows and carries the rule-24 record. Its return_basis column now mixes method and provenance for Orion rows. ~I2's adapter writes the method value TWR, which 0.4.1 forbids for Orion.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T21:0xZ: DB140-1-AC1..AC3 PASS rc 0",
    "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json at HEAD (0.4.1): columns account_id, market_value_eod, external_flow, income_received, return_basis (meaning 'which arithmetic produced total_return_daily'); optional row_status, reason_class, source_account_id; enums; source_requires; rule24_record.v041.iii_intent_coherence",
    "git show ef1c8ccaf2 (source_account_id rule text, +1/-1); git log on the contract: 969e41a3e7 (~221), ef1c8ccaf2 (~D2)",
    "data/assets/scripts/gold/irpt_reporting/adapters/inflection_scope_feed_adapter.py:48-51, :94 (ADJUDICATION_v105)",
    "ADJUDICATION_v103 (W219-S1 disposed resolved)",
    "investigation rows D2-W221-S1..S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND138_141_B49F_DRAIN_END_20261015.md blob 55a406ca98 (msg 8662)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "W221-S1 and W221-S2 are resolved on the evidence cited. W221-S3 stays ARMED with ~I2. The L9 verdict on contract 0.4.1 is FAIL on rule 24 (iii) alone, with every other element of the CTO's order met.",
  "notes": "L9 JUDGMENT GRADE, TO-DB-b-273 (order line 18; CTO 0.4.1 order item 1): FAIL on rule 24 (iii). return_basis now carries method (TWR) and provenance (VENDOR_REPORTED) on one axis; NOT_MEASURABLE (a state) predates 0.4.1. Every other element is met."
 }
]
```
