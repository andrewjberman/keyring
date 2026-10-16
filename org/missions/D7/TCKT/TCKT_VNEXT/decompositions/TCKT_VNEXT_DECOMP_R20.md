# TCKT_VNEXT round 20 -- the FWD-11 outcome stays readable, the coordinator's controls show only to the coordinator, the open route fences and presigns on ONE member (`2.0.0_SA_COO~V2`, dell2, 2026-10-16)

**Authority:** the CTO's rounds 18-19 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUNDS_18_19_20261016.md` (msg 9895 context; its rulings 2, 4 and 5 and its round-20 enrichment list), answering the CVO's `ADJUDICATION_v8` @a08573509a (nine MET, `R18P1-AC4J` and `R18P2-AC4J` PARTIAL; FWD-11 PARTIAL on DEV, NOT REALIZED; FWD-10 not run). **No PRD addendum.** Rows: `TCKT_VNEXT-D2-S57` (the outcome line hides once a meeting ticket completes), `TCKT_VNEXT-C-S11` (the open route fences on `requester.firm` and presigns on `answers.firm`).

## Enrichment list (the CTO's), and what each item becomes

| # | the CTO's item | cell | kind | write surface | risk |
|---|---|---|---|---|---|
| 1 and 2 (code) | the FWD-11 outcome line in every status that carries a `meeting` outcome; the coordinator's controls only for a viewer in `routing.primary` | `R20-pt-1` | BUILD (one worker, portal) | `portal/src/pages/TicketCenter/TicketCenter.tsx`, `portal/src/pages/TicketCenter/MeetingRequestParts.tsx`, one new test file under `__tests__/` | LOCAL (a portal change landing on DEV only through the approval row) |
| 3 | the open-route same-member fence (`TCKT_VNEXT-C-S11`) | `R20-lm-2` | BUILD (one worker, Lambda source and tests only; nothing deployed) | `infra/aws/lambda/ticket_center/lambda_function.py`, `infra/aws/lambda/ticket_center/tests/` | WORLD (a Lambda source path; the worker deploys nothing) |
| 1 and 2 (the exercise) | the filer's RENDERED read of one meeting ticket before and after completion, and the render-and-read of the meeting form (`R18P1-AC4J`) | `R20-rv-3` | RUN (the applier `0.7.0_AE_CloudOps~TV2`, STAGED) | users row, one meeting ticket, the routing window, a rendered page on the 5174 server | WORLD |
| 4 | FWD-10 / `R18P2-AC4J` | none | HELD (Andrew's hold on the Trade Request type; the CTO's 5174 handover) | `TO-R18-RUN-P2` stays staged | -- |

## What each cell does

- **`R20-pt-1` (portal).** (a) The board mounts `MeetingOutcomeLine` for a `meeting_request` ticket in EVERY status that carries a `meeting` outcome: today `TicketCenter.tsx` mounts it only when `t.status !== 'completed'` (lines near 909 to 915), so a completed ticket shows no outcome. After the change the line shows for a `meeting_request` ticket when `t.status !== 'completed'` OR `t.meeting` is present; a completed ticket with NO `meeting` outcome shows nothing (never the "waiting" words on a closed ticket). (b) `MeetingOutcomeControls` (the coordinator's two actions) render only for a viewer whose email is in `t.routing.primary` (case-insensitive), still never on a completed ticket; every other viewer sees the outcome line and no control. The viewer's email is `auth.user?.email` (`useAuth()`, as `InvestorReporting/index.tsx:75` reads it); the server's 403 sentence stays as the guard. No new route, write, principal or colour.
- **`R20-lm-2` (Lambda source).** `attachment_open_ticket` (lines near 2105 to 2135) fences on `requester.firm` (`_in_profile_scope`) but builds the bucket and key prefix from `answers.firm`. After the change it refuses (the same 404 body as "carries no attachment") a ticket whose `requester.firm` and `answers.firm` are not the same plain firm, and presigns from that one fenced member. One test per side. Nothing is deployed: the release is a later ticket-service release.
- **`R20-rv-3` (the live exercise, STAGED).** After `R20-pt-1` is on DEV and the CTO hands the 5174 server over carrying it: one synthetic filer principal files ONE meeting ticket and reads its own ticket in the RENDERED page after the coordinator's confirm and again after completion (two screenshots, read by a seat that did not build it); the meeting form is rendered and read (a third screenshot); the routing window, the identities and the removal are the run pair's. Run under a NEW amendment of the run pair, which the CTO signs.

## Chains and fan-out

**M = 2 independent chains:** {`R20-pt-1`}, {`R20-lm-2`}; `R20-rv-3` depends on `R20-pt-1` landing on DEV and the handover. **Fan-out: 2 of 2 chains, cap 4, reason:** two workers with disjoint write sets (portal; Lambda source), one applier order staged.

## Rule 24 record

- **MECE over the states of one meeting ticket as drawn:** (status completed / not completed) x (`meeting` outcome present / absent) x (viewer in `routing.primary` / not). The outcome line shows for (not completed, any, any) and for (completed, present, any); it is absent only for (completed, absent, any). The controls show only for (not completed, any, in `routing.primary`). Eight cells, each named by a test.
- **Same grain:** one ticket, one viewer, one board row. **State coherence:** drawing the outcome never changes the ticket; the controls' absence never changes what the server admits (its 403 stands).
- **A name this round does not choose:** none.

## Battery

comp-blast, comp-schedule, comp-iam, comp-routes: DECLARED-NOT-APPLICABLE for the two build cells (source and tests; nothing deployed). comp-adversary: the lens is the outcome line showing "waiting" on a completed ticket, a control shown to a non-coordinator, an email compare that is case-sensitive, a same-member fence that refuses a legitimate ticket (requester firm and answers firm are equal on every ticket the create path writes) and a presign from the wrong member.
