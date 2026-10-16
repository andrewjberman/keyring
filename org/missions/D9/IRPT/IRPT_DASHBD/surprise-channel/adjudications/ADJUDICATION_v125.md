# IRPT_DASHBD: CVO adjudication, round 146 (workstream B-49F, ~D2): series contract 0.3.0, the unreported-days pair

<sweep_watermark>2026-10-16T04:39Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T04:39Z, on msg 9044 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND146_147_B49F_CONTRACT_DRAIN_END_20261016.md` @52f18dfe5c, blob d9fc5582ee, shared with round 147). One order, TO-DB-b-278 (LOCAL; worker ~225; drained in 220c9c63f3, in HEAD). No judgment criterion. Re-run on the landed tree (HEAD 2013283a5d): DB146-1-AC1, AC2, AC3 PASS; round-close --round 146 --workstream B-49F MAY-CLOSE. Struck DB118-3-AC3 still FAILS (re-run here). No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S63",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T04:39:00Z",
  "one_line": "Round 146 B-49F (~D2): SERIES contract 0.3.0 adds the optional pair unreported_trading_days / unreported_trading_days_basis and makes income number-or-null; every other field is byte-identical; 3 of 3 PASS on the landed tree. ONE-DRAIN RULE (CTO msg 8735): the contract (DB-b-278) and its writer (publisher 0.2.0, DB-b-279) landed in the same drain 220c9c63f3, so the WRITER side holds. WHAT THE ISSUER'S SECTION 2 UNDERSTATES: the READER side is red. The portal's series-contract test iv-e-124 reads series.optional as three names, the contract now lists five, and the test is red since the contract commit (W225-S1). Amendment 1 (f10a449ccf) removed that test from DB146-1-AC3 rather than land the page mirror in the same drain, so the round passes while a consumer's test is red. That is the split the one-drain rule exists to prevent, on the reader side. The packet calls W225-S1 'ruled'; the row still reads ARMED, and its owner field says the mirror's owner is not named in the order (the packet names ~C2 by message only). RULE 24: the new basis field is a single fixed text ('trading calendar minus present partitions'), a one-value enum with no rule-24 record in the series contract; a small gap while it has one value, a real one at the first second value. Held ARMED (2): D2-W225-S1 (the red portal test), D2-W225-S2 (the red mirror stays with the drain owner until the page cell lands).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W225-S1",
   "IRPT_DASHBD-D2-W225-S2"
  ],
  "spec_asserts": "CTO msg 8735: a contract change and its writer land in ONE drain so trunk never sits red between them. Rule 24: an enum arrives with its four-postulate record and token census.",
  "world_is": "The workspace contract is at 0.3.0 with its writer; the portal mirror still lists the 0.2.0 optional fields and its parity test is red until ~C2's page cell lands. Nothing deployed.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T04:3xZ at HEAD 2013283a5d: DB146-1-AC1..AC3 PASS; round-close-check --round 146 --workstream B-49F MAY-CLOSE",
    "org/standards/IRPT_DASHBD_SERIES_CONTRACT.json at HEAD: contract_version 0.3.0; unreported_trading_days_basis kind 'scalar string', fixed_value 'trading calendar minus present partitions'; no rule24 key",
    "investigation rows D2-W225-S1 (ARMED; owner field: the page mirror's owner not named in DB-b-278) and D2-W225-S2 (ARMED)",
    "git: 220c9c63f3 carries both DB-b-278 and DB-b-279",
    "struck DB118-3-AC3 re-run via p118_cottonwood.py: FAIL",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND146_147_B49F_CONTRACT_DRAIN_END_20261016.md blob d9fc5582ee (msg 9044)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "W225-S1 and W225-S2 are named to HOLD them, not to dismiss them: they disarm when the portal page mirror of series.optional lands and iv-e-124 passes. Round 146's own cell is MAY-CLOSE."
 }
]
```
