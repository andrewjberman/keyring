# ANDREW-DIRECT 2026-09-24 ~15:3xZ (~11:3x AM ET) -- report 2: all seven /open-calls recs approved; a question on Tier-1 process load

**Channel:** the `4.0.0_SA_CRO~A` terminal, in reply to this seat's `/open-calls` output (seven cards, ~15:2xZ).
**Recorded by:** `4.0.0_SA_CRO~A`, same turn. **Report:** RCN-0017,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/REPORT2_CANONICAL_AND_CLOSER_FLOWS_SPEED_MODE_AND_SWITCH_20260924.md`
@`6273825a91`.

## Verbatim

> All of these recs are approved. However something I want more clarity on is what are the tier1 seats doing that is so process intensive? That seems to be the place where the most adjustments need to happen but I dont see any comments from you on that surface

## What is now his word (each REC at exactly the scope it was written; nothing wider)

1. **GO for `1.0.0_SA_CTO` to build report 2's changes C1-C9**, first run on DSGN_IRPTV1. C4, C5, C6, C8 and C9 are
   text edits that take effect at the next issuance; C1 and C2 are `/drive-mode` and `/closer-drive`.
2. **While a FAST lease is live, the seat lands PRODUCT changes on portal DEV itself**, with no CTO go-ahead and no
   MSTR push, CI (VALGATE) running. DEV only; PROD stays gated. This is the scoped change to the shared-branch push
   hold for portal DEV under a live FAST lease, and nothing else.
3. **In FAST mode the CVO grades each change after it lands;** nothing waits on the grade. A CVO FAIL becomes the
   seat's next item.
4. **At a switch back to canonical, the COO cuts the next round straight from the fast seat's STATUS.md**, with no CTO
   round analysis for that one cut. The CTO's analysis resumes at the end of that round.
5. **Lease: (a) 2 hours by default, plus a one-line prompt hook** that stamps a presence timestamp and extends a live
   lease while he is typing, so fast mode ends about 30 minutes after he stops. The hook writes a timestamp only; it
   is not a monitor or an alert.
6. **Arming a FAST lease also stands down the comp-tool search rail (`/freeform` semantics) for that seat for the
   lease's life.** Every safety gate stays armed.
7. **A one-round trial of a lighter worker type (Sonnet 5, effort medium)** on task orders of 100 product lines or
   fewer, graded on minutes per order and check defects per order against the previous same-sized round. Not Opus at
   low effort.

## Not covered by this word

- Nothing here moves served output, promotes to PROD, calls a vendor, or changes any other standing hold.
- The report's section 5.3 "never relaxed" list stands unchanged.

## The question (this seat's next act)

"What are the tier1 seats doing that is so process intensive?" -- answered by this seat as an addendum to RCN-0017,
measured from the Tier-1 seats' own commits, messages and files, and read against `4.0.0_SA_CRO~B`'s RCN-0016 (report
3, @`2d1bf5528a`) so that nothing it already measured is re-measured.
