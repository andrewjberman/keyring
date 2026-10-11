# IRPT_ANLREQ round 4, workstream Y -- L9 read

**From:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T11:55:28Z. Rows IRPT_ANLREQ-D2-S47 and IRPT_ANLREQ-D2-S48.
**Input:** `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND4_Y_L8_COMPILE_20261011.md @5eb0889c73 (msg 4855)`. No judgment criterion. The packet asks two things of a reviewer; both are answered below.

## 1. Can "exercised" stand for release 5?

**For the service, yes. For the outcome, no.** Nine after-reads read the function's new fields and they held. The thing a person
uses is the page, and the page's reader on PROD refuses a history answer with any key beyond the two it knows. This seat read that
reader: it admits a page only when its keys are exactly `items` and `next_cursor`. So for 61 minutes the release served an answer
its one consumer could not accept. A release is exercised when its consumer has read it. This one was exercised at the wrong end.

## 2. The two inferred statements

| statement | what this seat read | standing |
|---|---|---|
| The history view was refused for 61 minutes | The PROD reader's code refuses the three-key page; the release's own read R3 shows the page carried the third key | **The mechanism is confirmed in source. The event is still not observed**: nobody looked at a page, and nobody counted history requests in the window |
| It answers again | Live is revision 6 (read at this compile); the relayed read shows a two-key page | **Sound for the service.** Not observed on a page either |

**What is still unknown and matters:** whether any user opened Investor Reporting history between 10:25Z and 11:27Z. That page is on
PROD. The function's request log for the history route in that window would say. Row IRPT_ANLREQ-D2-S48.

## 3. Checked, and it holds

- The map hazard is disarmed on this tree: the three history members are pinned at the pre-release commit and the map records the
  live digest. It is disarmed only on a tree that contains that pin, as the packet says.
- The tolerant reader is on portal DEV and not on PROD. The re-release waits on a PROD push that changes a client-facing page, which
  is Andrew's word.

## 4. A correction to this seat's own row D2-S38

That row worried that the opened report prints a decimal fraction beside "percent". The packet's unit read answers part of it: of
513 served sections with unit `pct`, 425 carry a value of 1 or more. So served values are mostly percentage points and the fixture's
shape (0.0712 beside "percent") is not the served shape. 88 sections read below 1, zeros included; those are not told apart.
