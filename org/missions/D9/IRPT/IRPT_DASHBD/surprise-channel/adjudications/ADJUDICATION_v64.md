# IRPT_DASHBD: CVO adjudication, round 104

<sweep_watermark>2026-10-14T12:05Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T12:05Z, on msg 7566 / 7570 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND104_B_DRAIN_END_20261014.md`, blob 02d3d6ccbe @8a1b544b3e). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_104_L9_GRADE_20261014.md`): DB104-1-J1 FAIL on the plain-words clause (orientation met). Round 103's two defects are fixed; three new ones misinform: absent cells claim 'needs more history' for figures the same report prints; an account note contradicts its table; template slot names and a pointer to an absent disclosure page print as client lines. DB104-1-AC1..5-AC1 re-run here: 5 of 5 PASS. 9 rows dismissed below. Held with their owners: W164-S1..S3, W165-S1, S2, W166-S2, S4 (round 105's applies); W158-S1, S4, S6 and W155-S10 (ARMED). Round 98's rows wait. No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T12:05:00Z",
  "one_line": "Round 104. L9: DB104-1-J1 FAIL on its plain-words clause, orientation MET. Fixed since round 103: the unheld classes print the dash (3 of 3), the chart title is honest, and the kind notes name their figures. Not met: (1) p.5 and p.6 say the household's and accounts' last-12-month Beginning Value and Net Gain 'need more history', while p.3, p.4 and pp.8-10 print them; (2) p.8's note says the last-12-month return is not available, above an account that prints it; (3) slot names print as client rows, an asterisk points to no footnote, and every footer points to a disclosure page that reads 'Not available yet'. Dismissed (9): D2-W162-S1, -S2 (render readings), D2-W162-S3 (BLOCKING; the issuer's checker amended @478180115b, AC1 PASS re-run here), D2-W163-S1, -S2, -S3 (a premise count, a gitlink census note, two token collisions carried into the absent_kind proposal under W158-S4), D2-W160-S5 with its answer D2-W166-S1 (the 2026-10-11 manifests were CREATED by the CB-al-2 mint, writer 0.7.0_AE_CloudOps~CB2), and D2-W166-S3 (a UTC label). HELD: D2-W164-S1, -S2, -S3 (three questions to the CTO before the model-series apply), D2-W165-S1, -S2 (the account_dim apply order must add an upload path and take the as-of date as an argument), D2-W166-S2 (rollback by deletion is Andrew's), D2-W166-S4 (a resume through the mint path reaches the sidecar and method-row keys); ARMED with their owners: D2-W158-S1 (remedy in DB-b-198 @564d657082, LOCAL; the CTO's disarm read owed), D2-W158-S4 (the CTO's absent_kind ruling), D2-W158-S6 (remedy in DB-b-197, on an unpushed portal branch), D2-W155-S10 (2.0.0_SA_COO~P2: the resume is blocked, Cottonwood silver stops at 2026-06-23). Wait for round 98's packet: D2-S24, D2-W149-S1 to -S3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W162-S1",
   "IRPT_DASHBD-D2-W162-S2",
   "IRPT_DASHBD-D2-W162-S3",
   "IRPT_DASHBD-D2-W163-S1",
   "IRPT_DASHBD-D2-W163-S2",
   "IRPT_DASHBD-D2-W163-S3",
   "IRPT_DASHBD-D2-W160-S5",
   "IRPT_DASHBD-D2-W166-S1",
   "IRPT_DASHBD-D2-W166-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, every BLOCKING item before the slug, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All five round-104 orders complete (DB-b-197..201 drained on HEAD). Everything LOCAL: renders private, portal branches unpushed, nothing written to AWS. The one BLOCKING round row (W162-S3) is resolved by the issuer's own checker amendment. The round's three packets (model series, account_dim, Cottonwood resume) are inputs to round 105, with three CTO questions open on the model series and the resume blocked on silver that stops at 2026-06-23. Round 98 is not terminal (DB-b-183 held on dell1's ledger SC-e-97), so no remediation row is written this compile.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W162-S1..S3, D2-W163-S1..S3, D2-W164-S1..S3, D2-W165-S1..S2, D2-W166-S1..S4, D2-W160-S5, D2-W158-S1, -S4, -S6, D2-W155-S10 (INVESTIGATION_v1.md)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND104_B_DRAIN_END_20261014.md blob 02d3d6ccbe (msg 7566, 7570)",
    "this seat's re-run 2026-10-14T12:0xZ: p104_round104.py DB104-1-AC1..DB104-5-AC1 -> 5 of 5 PASS",
    "this seat's read of 14 of 14 pages, fwd21_sample_r104/pages/r104_final/ (private; no figure copied)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_104_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Render readings fixed in the round's cells, a BLOCKING checker defect closed by the issuer's own amendment and re-run here, census and premise notes carried into the proposal the CTO rules on, an open writer question answered by its own round's cell, and a time-label reading. Apply-shaping rows and ARMED rows are held with their owners."
 }
]
```
