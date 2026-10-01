# L4-R REVIEW -- DSGN_AMGTV1 PRD v0.6 @b8c93f6342, ratified-text half -- SIGN

**Reviewer:** `3.0.0_SA_CVO~Z`. **Delivery:** `1.0.0_SA_CTO~Z` msg 27502 (half_hash cf69f765260d). **Prior signed:** v0.5
@bf3a6f5614 (ENDPOINT hash ca5c501ab4d6). **Diff read:** `git diff bf3a6f5614 b8c93f6342 -- prd/DSGN_AMGTV1_PRD.md`.
**Pins read:** Andrew 2026-10-01 03:4xZ verbatim (`4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261001_034xZ_AMGT_SECURITY_ANALYSIS_DEMO_FRIDAY.md`);
CTO~Z placement rulings R3-R6, R10, R11 (`CTO_PLACEMENT_20261001_043xZ_AMGT_FRIDAY_DEMO_RESTRUCTURE.md` @e18d3a4e6a);
shared CONTRACT (`AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` @b8c93f6342).

## Verbatim against Andrew's words

| outcome | Andrew | PRD | verdict |
|---|---|---|---|
| FWD-21 | "a bubble chart by size to see what is being talked about the most"; "cursors to flip between periods like this month, month -1, month -2 ... watch the bubbles change in size based on what we collected"; "chatter is always that bubble chart form" | one bubble per security, area = collected count in the calendar month; cursor this month, M-1, M-2; one size changes between two steps on served data; no other chatter view | MATCH (the "collected" label is R4, narrower in wording only, faithful to "what we collected") |
| FWD-22 | "horizontal bars widest ones in 1st position and then descending vertically"; "price is always those horizontal bars" | horizontal bars, longest first, descending; 0 line charts, 0 toggles | MATCH. Measure (30-day return, signed) is R3, which fills a value Andrew left open |
| FWD-23 | "Lead Panel header fixtures ... looks nothing like the rest of the panels"; "keep going with" the /philosophy fixture cards | header + selected-name header from the /philosophy card face; chartColors; shared Segmented | MATCH |
| FWD-24 | "We still arent displaying anything in most views when it comes to breakout and price" | 0 "not served" for a field the payload carries, beside a positive control | MATCH; positive arm present |
| FWD-3 RETIRED | "these lines with normalized y-axis percentile ranks are not very interesting"; "No other views" | line history, sparkline, highlight chart removed | MATCH (R5, R10) |

Every operative constraint in Andrew's DSGN paragraph is carried. Each new DONE WHEN has a positive arm: a size that
changes (FWD-21), a DOM census (FWD-22), a before/after render (FWD-23), and a field the payload truly lacks (FWD-24).

## CONTRACTS against the counterpart

C-FRIDAY (1)-(3) agrees with CONTRACT sections 1 (monthly route, RESAPP the writer), 2 (`return_30d_pct` signed percent;
breakout `*_pct`, never rescaled), 3 (server-side date fallback; the page computes no date) and 6 (fixtures of the exact
shape, swapped with no shape change). The two C-ASKS rows name AMGT_RESAPP as owner, which matches CONTRACT section 0.
Agreement with AMGT_RESAPP v0.31 is graded in that half's review.

## Recorded, not blocking

1. **P1 -- FWD-2 carries two DONE WHENs.** The v0.5 DONE WHEN/ACCEPT ("all four lead-panel lists", "laid out like the
   Positioning page's holdings breakdown") stands unstruck above the v0.6 restatement that retires the list form.
   **Binding reading at L9:** FWD-2 is graded on the v0.6 restated DONE WHEN only (identity on 3 bubbles and 3 bars). The
   CTO strikes the superseded lines at the next bump.
2. **P1 -- Breakout leaves the demo by ruling, not by his word.** FWD-18's v0.6 note (R6) removes the Trending/Breakout
   control because Breakout x Chatter has served empty for 16 days. Andrew named breakout among what is not displaying
   and sent it to RESAPP and backfill. Hiding it is a legitimate driver ruling. It still changes what he will see on
   Friday, so it belongs on his 09:00 ET list as a fact, not a call.
3. **P2 -- annotation hygiene.** The ENDPOINT section now holds history and seat names ("v0.6 RESTATED (CTO~Z placement
   ruling R5 ...)", "RETIRED v0.6 (CTO~Z ...)", the "===== v0.6, 2026-10-01" header, the `4.0.0_SA_CRO~Z` path), and
   FWD-1's ACCEPT still reads "out of the list". None changes what is graded beyond item 1. Accepted under proportionate
   sign-off and the 18:00 ET freeze; the move to PROVENANCE goes with the next ENDPOINT change, never alone.

## Verdict

**SIGN** the ratified-text half at b8c93f6342.

## What you should have asked but did not

Whether FWD-21 can pass on Friday at all. Its DONE WHEN needs the *served* monthly route ("on served data"), and the
route is an open C-ASK on AMGT_RESAPP. A fixture-built bubble chart fails FWD-21 by its own text. If the route misses the
18:00 ET freeze, the demo's lead view ships ungraded, so the route belongs at the head of RESAPP's critical path.

-- 3.0.0_SA_CVO~Z
