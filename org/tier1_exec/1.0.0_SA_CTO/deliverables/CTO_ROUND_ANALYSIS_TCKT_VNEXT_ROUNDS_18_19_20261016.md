# CTO ROUNDS 18-19 ANALYSIS -- TCKT_VNEXT (~V2): meeting request, trade-form routes, cross-firm narrowing (2026-10-16 ~21:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~DELL2` ADJUDICATION_v8 (`org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/adjudications/ADJUDICATION_v8.md`
@a08573509a, msg 9895). Nine criteria are MET and two PARTIAL (R18P1 and R18P2). FWD-11 is PARTIAL on DEV and NOT REALIZED. FWD-10 is not run.
round-close-check reads MAY-CLOSE for both rounds. **No PRD addendum:** every gap below is served by an existing FWD.

## Rulings

1. **Rounds 18 and 19 CLOSE.** The four R19 narrowings (client notice recipient, intake list, profile scope, the two environment values) are
   MET live, including the two old fail-open paths, which are now closed.
2. **R18P1 (meeting form, PARTIAL):** two gaps.
   - The render-and-read is owed: a screenshot of the served page, read by a seat that did not build it.
   - The coordinator's two actions render only for a viewer in the ticket's `routing.primary`. Every other viewer sees the outcome line
     and no control. The 403 sentence stays as the server's guard.
3. **R18P2 (trade-form page, PARTIAL) stays HELD** under Andrew's hold on the Trade Request type, quoted: "we should not push this til we
   actually have a functioning channel for that". Nothing is owed until he lifts it. FWD-10 PART 2 also waits for the 5174 handover after his
   Performance-tab smoke.
4. **FWD-11 is NOT REALIZED on two counts:**
   - The filer's read was never exercised.
   - The outcome line hides once the ticket completes (`status !== 'completed'`), so a filer whose meeting completed cannot read it.

   Ruling: the outcome line shows on the ticket in every status that carries a `meeting` outcome. The exercise is one synthetic filer
   principal reading its own ticket after the confirm and again after completion, in the rendered page. Then PROD runs by 2026-10-24, as
   the DONE WHEN reads.
5. **D2-C-S2 (latent, INERT): closed now, cheaply.** `attachment_open_ticket` fences and presigns on the SAME member. It refuses a ticket
   whose `requester.firm` differs from `answers.firm`, and it presigns from the fenced member. There is one test per side.

## Enrichment list (round 20, ~V2)

1. The FWD-11 outcome line in every status that carries a `meeting` outcome, plus the filer's rendered read before and after completion (on
   DEV, then PROD).
2. The coordinator controls only for `routing.primary`, plus the render-and-read of the meeting form.
3. The open-route same-member fence (D2-C-S2).
4. FWD-10 / R18P2: HELD (Andrew's hold; the 5174 handover).

-- 1.0.0_SA_CTO~DELL2
