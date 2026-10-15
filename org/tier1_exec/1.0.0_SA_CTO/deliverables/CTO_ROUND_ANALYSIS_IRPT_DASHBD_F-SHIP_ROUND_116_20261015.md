# CTO ROUND-116 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2) -- the candidate must pass its own criterion at the head that is registered (2026-10-15 ~04:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s L10 slug for round 115 (msg 8057,
`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v80.md` @995d426630): AC1-AC3 PASS at the worker's head
`476f8388`, MAY-CLOSE, no judgment criterion. **No PRD addendum.** Issuer: `2.0.0_SA_COO~F2`.

## Rulings

1. **AC3 is graded at the candidate head `506a2302`,** the head that gets registered for Andrew's approval. It is not graded at the worker's
   head. `~F2` amends AC3 so its grant covers the issuer's own `index.tsx` hookup, its own act under rule 27. The amendment commit names the
   gate limb that graded it. AC3 is then re-run at `506a2302`, and the result goes in the next packet. A candidate that fails its own criterion
   is never registered.
2. **W503-S1 is accepted as ruled:** the export reads the served report and does not re-scope it on the client (`reportRead.ts:107`,
   `ExportButton.tsx:161/236`). Its ground, the route's scope rule, becomes code in IB-pr-554, together with the export freeze fix this seat ruled
   in `~P2`'s round-3 analysis (@a4718eab10). The row's grounding is re-read when IB-pr-554 is built.
3. **No new build cell.** F-SHIP's tab and export are built. The next F-SHIP act is the candidate's registration (client-facing, Andrew),
   once the route serves a 49 Financial sample on DEV (round-114 analysis ruling 3). Until then, this workstream's only act is the AC3
   amendment above.

-- 1.0.0_SA_CTO~DELL2
