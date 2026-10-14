# IRPT_DASHBD: CVO adjudication, round 97

<sweep_watermark>2026-10-14T00:45:02Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T00:45:02Z. Input: msg 7384 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND97_B_DRAIN_END_20261014.md @a425b45bee`; one LOCAL order, DB-b-182). No judgment
criterion. This seat re-ran DB94-1-AC1, DB94-6-AC1 and DB97-1-AC1: all PASS. 3 rows dismissed below; round 96's rows wait for its packet.

```json
[
 {
  "id": "IRPT_DASHBD-C-S70",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T00:45:02Z",
  "one_line": "Round 97, no judgment criterion. Dismissed: D2-W148-S1 (BLOCKING, ARMED: DB94-1 and DB94-6 failed at the gap-table binding after contract 0.3.0; the issuer's checker amendment ac24632028 accepts a lineage version, and this seat re-ran both checks and DB97-1-AC1: all PASS, so the hazard no longer holds); D2-W148-S2 (chart series reshaped to {name, points}, no chart member measured on this household) and -S3 (BREAK also covers a SOURCE_LAG opening anchor), readings stated in the record. Round 96's rows (D2-W146-S1 to -S3, D2-W147-S1 to -S3) wait for round 96's packet: DB-b-180 is active.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W148-S1",
   "IRPT_DASHBD-D2-W148-S2",
   "IRPT_DASHBD-D2-W148-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "DB-b-182 is complete; the report contract is 0.3.0 and states the filled-report shape; the private sample was rebuilt for the same household. S3 reads only; no served byte moved. Round 96 (DB-b-180) is non-terminal, so no remediation row is written this compile.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W148-S1, D2-W148-S2, D2-W148-S3",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND97_B_DRAIN_END_20261014.md @a425b45bee (msg 7384)",
    "this seat's run 2026-10-14T00:45 of the three criterion invocations from their task orders on the shared tree: DB94-1-AC1 PASS (117 members, 8 sections, bound by hash), DB94-6-AC1 PASS (contract 0.3.0, 36 window members re-sourced), DB97-1-AC1 PASS (3 accounts, 44 filled, 30 identity checks; the private sample conforms); checker amendment ac24632028 on HEAD"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An ARMED check failure this seat re-ran to PASS after the amendment, and two readings."
 }
]
```
