# Andrew-direct ~15:0xZ 2026-09-18 -- Lead Panel: three cards decided, one card not recognised, message cut off

**Recorded by:** `4.0.0_SA_CRO~Z`, at this terminal, the same minutes the words arrived.
**Context:** the Lead Panel brief (`BRIEF_LEAD_PANEL_CURRENT_TO_DESIRED_20260918.md` @`d07d76b1ea`, corrected
@`7705cdc34c`), section 2, four cards A-D.

## Verbatim (the message arrived truncated; nothing after "On the" was received)

> Yes this is exatly why I wanted you to actually deep dive here and find the gaps. Please update your brief with
> your updated findings as the gaps are discovered. Then, On the four decisions: 1, Yes we should just get prices as
> of prior day on the existing BBG job. 2, go with your rec here. 3, Card 5 I still don't know what that refrs to.
> 4, the Promote can wait. On the

## Reading, narrow

1. **Card A, price cadence: YES.** Prices as of the PRIOR trading day, as a leg of the EXISTING Bloomberg daily job
   (`integrations/bloomberg/pipeline/scheduled_daily_pull.cmd`, task `OPAL_BBGTML_daily_pull`). Not a new job, not a
   new schedule. This opens card A; it is relayed to `1.0.0_SA_CTO~Z` to sequence and does not by itself name who
   edits the file.
2. **Card B, price Breakout floor: this seat's recommendation, adopted.** The recommendation is stated in the brief
   at the moment of adoption so the words cover a specific rule: a price Breakout requires a POSITIVE move of AT
   LEAST +5% above the trailing 30-day mean; smaller or negative moves are excluded, and a day where nothing clears
   it is an honest EMPTY. It lands in `lib/research/metrics/movement_gate.py` as the price entry of
   `MIN_ABSOLUTE_JUMP`, with `MIN_ABSOLUTE_JUMP_BASIS` moving from ABSENT_NOT_RATIFIED to RATIFIED citing this record.
3. **Card 5: NOT RECOGNISED.** Andrew does not know what "Card 5" refers to. `2.0.0_SA_COO~Z` recorded a "yes do it"
   at 13:09Z as his answer to CARD 5 (@`ad2d1253be`) and `AMGT-rk-22` began producing on it. **That answer's scope is
   now in question and is put back to him in plain words; this seat does not treat it as confirmed or as
   withdrawn.** Relayed to `2.0.0_SA_COO~Z` and `1.0.0_SA_CTO~Z` the same turn.
4. **Card D, promote: DEFERRED** by his word. Nothing is prepared toward it.
5. **The brief is to be updated as gaps are discovered** -- a standing instruction for this panel series, not a
   one-off.

Not a canonical-flow project and no new gate.

## Follow-on, ~15:3xZ -- CARD 5 CONFIRMED in plain words

Put back to him in plain words -- the 13:09Z question as `2.0.0_SA_COO~Z` actually asked it, "Run the
management/posture producers over the full 33-name keyed population?", with the result (management 5 -> 14 names,
posture 2 -> 33, low single-digit dollars). His answer, verbatim:

> yes that's what I meant, make sure that your brief is updated as needed, and then let's move on to the next panel,
> THESIS

Reading: the 13:09Z approval stands as given; the scope question raised at ~15:0xZ is CLOSED. The label "CARD 5" did
not land, the act did. `2.0.0_SA_COO~Z` was holding round 13's L10 slug on this answer (msg 23682) and is told the
same turn. Next in the panel series: THESIS.
