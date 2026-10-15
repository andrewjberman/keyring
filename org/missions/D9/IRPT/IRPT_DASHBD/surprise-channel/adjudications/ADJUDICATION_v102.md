# IRPT_DASHBD: CVO adjudication, round 136 (workstream B-49F, ~D2): the read of the three source-absent days

<sweep_watermark>2026-10-15T19:35Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T19:35Z, on msg 8575 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md` @e7b2e022cc, blob 1b1f31d9cf; one packet covers rounds 133-137, adjudicated as v99-v103, one per round). Graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Round 136 is the issuer's direct LOCAL act (record RD_COT_ABSENT_DAYS_READ_R136.json @b9af37d608; no task order; round-close reads 0 orders, MAY-CLOSE). Re-run here: DB136-1-AC1, DB136-1-AC2, 2 of 2 PASS (rc 0). The struck DB118-3-AC3 still FAILS (rc 1), unmet. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S39",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T19:35:00Z",
  "one_line": "Round 136 B-49F: the three source-absent days. 2 of 2 PASS re-run; the fresh clause recounts the silver presence, next-day rows and measured-return counts. 2026-08-19, 2026-09-24 and 2026-09-25 each have a fact_allocations partition and no fact_transactions partition; this seat confirmed that independently in v96, with controls. Each absent day's own return is missing; the next present day's return is measured (2026-08-20: 783 of 814 rows MEASURED), because the adapter derives it from the previous trading day's silver value. The record states that as inferred, not proven by a flow reconciliation. A sidecar prefix irpt/cottonwood/gold/account_return_daily_blank_reasons/ holds 1 file that the landing function does not write; it is the Commonwealth-era mint's (D2-W166-S4). Per the CTO's ADDENDUM 1 (msg 8524), no sidecar write is made and the handler states the gap (round 137). D2-S92 is held, as in v100: a window compounding across an absent day lacks that day's return.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S92"
  ],
  "spec_asserts": "CLAUDE.md trading-calendar law: a gap is counted in trading days; a value carries its claim (the next-day return is inferred).",
  "world_is": "Three trading days in the Black Diamond era have no Cottonwood return; the report-build handler names them (v103). No AWS write.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T19:2xZ: DB136-1-AC1, AC2 PASS rc 0",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/RD_COT_ABSENT_DAYS_READ_R136.json @b9af37d608 (per_day, sidecar)",
    "ADJUDICATION_v96 silver presence read with controls",
    "investigation rows D2-W166-S4, D2-S92",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND133_137_B49F_DRAIN_END_20261015.md blob 1b1f31d9cf (msg 8575)"
   ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "notes": "D2-S92 is named to HOLD it (ARMED, owner ~D2), not to dismiss it; the round's read is graded above."
 }
]
```
