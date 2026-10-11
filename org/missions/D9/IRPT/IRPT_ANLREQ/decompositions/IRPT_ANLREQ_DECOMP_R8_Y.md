# IRPT_ANLREQ -- decomposition, round 8, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 5133 (2026-10-11 ~14:3xZ), on this seat's read
`deliverables/2.0.0_SA_COO~Y2/trace/COMMENTARY_READY_WHAT_IT_READS_20261011.md` (@0a2b5da8af): "On the product path only the resident
sends analysis_ready, and only for a READY job, so the drafter trusting the message is the design. The gap is that a hand-built invoke
bypasses it. One cell, not urgent: the drafter refuses a request whose job does not read READY. It lands before the analysis-ready
binding does." No round analysis for rounds 5 to 7 is in hand at this cut (the CVO compiled at 14:22Z); this round is that one ruled
cell. No PRD addendum; the endpoint is unchanged.

**Thread:** FWD-1 is not live. This round hardens hop 10 of the map (the commentary drafter) before hop 9 is bound (workstream G's
attach release, cell 4).

## Cells

| cell | source | what is built | write set | risk |
|---|---|---|---|---|
| `AR-y-81` | CTO msg 5133 | A request whose job does not read READY gets no commentary draft and no `commentary_ready` message, on any path into the drafter. The gate is placed where the job's state can be read with NO new permission if such a place exists (the composition read the drafter already calls holds a jobs-table port; the cell reads whether its role may read that table and says so) | `infra/aws/lambda/investor-reporting/reports/` (the composition read) and/or `data/transcripts/scripts/commentary/` (the drafter), their tests, one design record | WORLD by the gate's floor (`infra/`); nothing is built into a zip, uploaded or applied by the cell |

## Interfaces

- I14: when the gate refuses, the drafter's record lands `failed` at an existing stage with ONE typed reason; no draft is stored and
  nothing is sent. The reason names no job state and no identifier beyond the request id the caller sent.

## Edges and chains

- One cell. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one cell.

## Release

Two deployed functions may be touched (`irpt-commentary-composition-read-lambda`, `outlook-global-commentary-draft-lambda`). Their
release is a pair of its own, cut after the drain with a census of each function's moved members and of every caller of the gated
read. It must be LIVE before workstream G binds the analysis-ready queue (CTO msg 4972, cell 4; msg 5133).
