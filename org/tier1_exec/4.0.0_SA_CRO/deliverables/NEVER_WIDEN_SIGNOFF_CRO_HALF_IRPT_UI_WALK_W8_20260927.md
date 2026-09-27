# NEVER-WIDEN SIGN-OFF (4.0.0_SA_CRO half) -- WINDOW 8: INF's ONE Orion read (plan 7f64b166) + an optional third Analysis attempt

**Packet:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W8_20260927.md`
blob `e246200462e85ae97d29c26b3b7cae095d52e657` @`1282a22bf5`. The blob is the same at HEAD and on disk (read
2026-09-27 ~03:5xZ).
**Asked by:** 2.0.0_SA_COO~P msg 101773. This seat is not in the act.

## VERDICT: SIGNED on blob e2462004, with one condition

- **W8-1 is this seat's INF addendum 3, as asked:**
  - the plan's end is READ at build from the served INF holdings answer (`source_dates.business_date` 2026-09-22 on
    sel_366d4891..) and printed with its source;
  - the account is still the rule's pick;
  - the pre-check runs with the arm off;
  - the arm is on 3a68bb2d's terms (0/1/0, two env keys, readback of sha 7f64b166);
  - there is ONE matching read, then the disarm;
  - the audit counts exactly ONE Orion call across Andrew's call 2 in total (window 7's 0 plus this 1), and INF
    REPORT# goes from 0 to at most 1, traced to K11's HAR.
- **W8-2 is gated where it must be:** it runs only on Andrew's word at the ~Y terminal. Window 7's go was call 1, and
  it does not carry. The 12 `model_portfolios/{id}/status` polls are named (CTO 101763). Any vendor objects it creates
  are kept and named, like window 7's two (the holdings upload and portfolio 2363504).
- **Carried from window 7:**
  - K1-CRED is deleted once the walkers have logged in;
  - the 120-minute hard cap;
  - K9's REPORT# pre-read and HAR trace;
  - W8-3's pin re-read gate;
  - this seat's named item 1 (no ui-walker arm through the audit close).

## CONDITION -- the arm-OFF pre-check compares the WHOLE request to the plan, not only its end

Window 7 missed on the window's end. The next miss can be the start or the account:
- a YTD preset that begins on the first trading day (2026-01-02) instead of 2026-01-01;
- the account id;
- the requested scope.

All of them cost the same: a refused read, and an arm spent in time rather than in calls, with 12:00Z the expiry. So
the pre-check reads, from the URL or HAR, the request's **account, start and end**, and they must equal the plan's
`acc_5510a..`, 2026-01-01 and 2026-09-22.
- If any of the three differs, nothing arms.
- If only the start differs because of how the page defines YTD, the plan is re-cut to the page's start, read from
  the HAR, under this half without a fresh read, and the pre-check runs again.

Not measured by this seat: the plan file and its sha, the served pins, and the resident rb fix (the packet's).
