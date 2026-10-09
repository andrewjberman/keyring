# IRPT_BCKEND PRD v0.31 @6fd48e6630 -- ratified-text half review (L4-R)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-09 ~06:0xZ, on `1.0.0_SA_CTO~DELL2` msgs 2636 and 2638. The change: FWD-14 is
added to ENDPOINT. CONTRACTS is unchanged, apart from one surface-manifest row.

## Against Andrew's word

Record `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261009_060xZ_HOLDINGS_NO_WORSE_PUBLISH_GATE_TO_P2.md` @f8e7d992dd. His
words: "Yes I like that idea, run that over to CTO for fold in for ~P2 workstream", where "that idea" is the CRO's publish gate.
FWD-14 carries it faithfully:
- the gate sits in the producer's publish step, before the index moves;
- the four Branch A conditions;
- per-firm independence;
- new unclassified positions are listed, not refused;
- a first publication passes on the absolute conditions only;
- the seat-driven two-arm QA proof;
- it is a gate, not a monitor.

The record left the two extra conditions as "Optional, Andrew's call". The CTO ruled them in under self-drive discretion. That is
within the seat's discretion, but one of the two is written so that it can freeze a firm for good.

## Verdict: REFUSE, on one clause

**"an account present at the prior and absent now" is WORSE, with no exception for an account that legitimately leaves.**

Accounts close and terminate in the normal course of business. IRPT_BCKEND's own directory work carries terminated entries (IB-pr-380,
-381, -384). Followed through:
1. On the first fire after a real closure, the firm's candidate lacks the account, so it is refused.
2. On WORSE "the firm keeps its last good publication". That publication still holds the closed account.
3. Every later candidate is compared against that same prior, still lacks the account, and is refused again.

The firm's holdings stop updating permanently, through ordinary business with no regression. Nothing in the text lets it recover except
a manual re-point, which this gate exists to retire (S392).

**Fix (one clause):** "an account present at the prior and absent now, unless the firm's source records it closed or terminated (that
account is listed, never refused)". Better still, state the source field that says closed. On those bytes this seat signs.

## Notes, not grounds

- The stale-frontier condition is sound as written, because `lib/trading_calendar.py` keeps a Friday from reading stale on a Monday.
- FWD-14's OWNER line names a seat serial ("workstream 2.0.0_SA_COO~P2") inside ENDPOINT. Every other FWD's OWNER names a project only.
  "IRPT_BCKEND" alone would match.

## Re-review on v0.32 @97826891e9 (~06:1xZ, msgs 2650 and 2651): SIGN

FWD-14's account-lost condition now carries this seat's fix verbatim: "unless the firm's source records it closed or terminated (listed,
never refused)". No other ENDPOINT or CONTRACTS bytes changed. Signed on these bytes. The OWNER-line note stands as a note.
