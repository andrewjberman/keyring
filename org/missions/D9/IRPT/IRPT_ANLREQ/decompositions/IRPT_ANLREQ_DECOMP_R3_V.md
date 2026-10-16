# IRPT_ANLREQ round 3, workstream TICKET (`2.0.0_SA_COO~V2`) -- the ticket page READS a hop failure (FWD-4, C-HOP-FAILURE v0.21)

**Issuer:** `2.0.0_SA_COO~V2` (dell2), 2026-10-16. Workstream `TICKET` (C-ABSORB e: the Analysis Request parts of the ticket page); rounds 1 and 2 of this workstream were `TO-AR-v11` to `v13` and `v21`. Each workstream issues only into its own scope (rule 27).

**Authority:** the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_ANLREQ_FWD4_HOP_FAILURE_READ_NOT_WRITE_20261016.md` (msg 8908): "`~V2`: the ticket page read, `AnalysisRequestParts.tsx`. Opal-internal, so this seat approves the portal candidate." PRD `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` v0.21, contract C-HOP-FAILURE clauses (1) and (5); both halves SIGNED (`prd-signoff.py status`, read 2026-10-16). No PRD change: the ENDPOINT is unchanged.

## The wire shape this cell reads (from `~G2`, msg 9053, merged `766ec706ee`, LOCAL; the Lambda carries it only at its own later release)

- No new envelope field. **code** = the status value's `public_reason_code`: the closed set `READY_SIGNAL_SEND_FAILED`, `COMMENTARY_DRAFT_FAILED`, `COMMENTARY_DRAFT_REFUSED`, `PACKAGER_REFUSED`, `PACKAGER_FAILED`, or the unchanged `ANALYSIS_*` reason when the hop code is unknown.
- **words** = the `description` of the LAST entry of `actions` when that entry's wire action is `NONE` (fixed strings from `status.FAILURE_WORDS` / `FAILURE_STEP_WORDS`). The step is named in the words' first sentence; there is no separate hop field. A FAILED or ATTENTION job also carries one `NONE` action (generate-step words) with its usual reason code. State and dates do not change on a hop failure.
- **Portal side, measured:** `InvestorReportingClient.getJobStatus(jobId, selectedTenant)` (`src/api/endpoints/investor-reporting.ts:1496`) returns `StatusEnvelope`; `adaptStatusEnvelope` (`contracts/adapt.ts:578`) carries `publicReasonCode: string | null` and maps each wire action to `safeActions[]` with `label = action.description`; `NONE` is a valid wire action (`wire/StatusEnvelope.ts:40`).

## CONTRACT of the cell (fixed by the issuer; the order cites it)

1. The ticket page calls `getJobStatus(ticket.report_ref.request_id, <the ticket's firm>)` ONCE when an analysis-request ticket is opened and once on the existing refresh; no timer, no polling.
2. It shows the failure (the step and what happens next, i.e. the `NONE` action's words) ONLY while the request is unfinished: `ticket.package` absent. A ticket whose package is attached shows its completion and no failure (clause 5). The stored `hop_failure` stays on the job row as history; the page never reads it directly.
3. No call is made for a ticket with no `report_ref.request_id`.
4. A failed status call shows nothing extra and never breaks the ticket page (existing error idiom of the file).
5. No new route, no new principal, no ticket write, no engine call, no new colour (white panel, navy ink, the existing panel classes; DESIGN.md C3/C5.8/C12). Opal-internal page only (the Ticket Center is `requireInternal`).

## Cells

| cell | builds | FWD | write surface | risk | depends on |
|---|---|---|---|---|---|
| `AR-v-31` | the ticket page's hop-failure read in `AnalysisRequestParts.tsx` + the new test file | FWD-4 | `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`, `portal/src/pages/TicketCenter/TicketCenter.tsx` (a prop pass-through ONLY, if the real client is not already handed to the block), `portal/src/pages/TicketCenter/__tests__/hop-failure-read.test.tsx` (new) | LOCAL (portal DEV only; a product file, Opal-internal) | none to build; the live arm waits for `~G2`'s release |

**Chains (M = 1):** {AR-v-31}. **Fan-out: 1 of 1 chain, cap 4, reason:** one cell, one portal worker.

## Acceptance

Mechanical: the six named tests (the issuer's `ar_v_checks.py v31-failure`), the portal typecheck (`portal-tsc`), and a mutant that fires. Judgment (the CVO): the page names the failed step and what happens next only while no package is attached.
**The LIVE arm is not this cell's:** each failure driven on purpose against the released status route (the PRD's DONE WHEN) belongs to FWD-4's run after `~G2`'s release and `~T2`'s cells; this cell is exercised against a stubbed client and rendered once.

## Rule 24 record

- **MECE over the clause-5 states of one ticket:** (request id absent) x (package attached / absent) x (status carries NONE words / carries none / call failed). The six tests are one per distinguishable outcome: words shown (no package, words present); nothing (package attached); the call is made with request id and firm; no call (no request id); nothing extra (no words); nothing and no break (call failed).
- **Same grain, one axis:** one page, one read. **State coherence:** a hop failure never changes the ticket's state, and a recovered hop never reads as failed because the package is the one completion signal.
- **A name this round does not choose:** none (no S3 address, no resource name).

## Battery

comp-schedule, comp-iam, comp-routes, comp-blast: DECLARED-NOT-APPLICABLE (a portal page change under the viewer's own session; no route, role or schedule). comp-adversary: the lens is a failure shown on a FINISHED request (clause 5), a status call for a ticket that has no request, and a thrown error that blanks the ticket page. BLIND to: the deployed status route (not yet released with the failure code).
