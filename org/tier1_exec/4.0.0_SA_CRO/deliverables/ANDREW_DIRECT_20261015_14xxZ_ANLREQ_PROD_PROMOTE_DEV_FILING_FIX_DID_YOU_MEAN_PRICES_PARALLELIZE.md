# ANDREW_DIRECT 2026-10-15 ~14:xxZ -- Analysis Request: fix DEV filing and promote with the staff filer; "Did you mean" at filing; prices Yahoo then YCharts; parallelize to a full end-to-end system

**Channel:** Claude Code terminal, dell2, to `4.0.0_SA_CRO~DELL2A`. **Recorded by:** `4.0.0_SA_CRO~DELL2A`, same turn.
Andrew was answering the stage-by-stage status `4.0.0_SA_CRO~DELL2A` gave at ~14:1xZ. That status was a re-measure of
`TICKET_CENTER_ANALYSIS_REQUEST_END_TO_END_GAP_BRIEF_20261014.md` against HEAD, the release-31 records and portal DEV/PROD.

**Andrew, verbatim:**

> "1.) Yes we can promote that fix to PROD for the staff filer. We need to get that DEV filing fixed, maybe we can get both the
> staff filer issue and the filing issue fixed on DEV now and they both go out with the promote. We do need to sort out the "Did You
> Mean" at the Request filing point. The swaps can be handled later in the backend process, because swaps are not up to the filer.
> 2.) I can test these whenever ready. 3.) Price source should be handled via the Yahoo finance calls + YCharts Fallback, as
> discussed. Do we need more agents online working on this? The rest of the items seem relatively trivial and can be handled in
> sequence. Let's keep this moving and let me know if there are ways to increase parallelization so that we can get a full end to
> end system done."

## What it sets (surfaced, not adjudicated)

1. **PROD promote, approved by Andrew.** Two fixes ship together:
   - the staff filer (J7, portal AR-y-325, on DEV);
   - the DEV filing fix.

   Today every DEV filing is refused: the portal always sends `commentary_requested` (AR-y-317, merged to DEV 10-14 18:23Z), and
   the live `irpt-ycharts-generate` refuses the member until IB-pr-456 is applied. The promote also carries the PROD list-load
   defect (row D2-S118) if it shares the cause.
2. **"Did you mean" at the filing point.** This is the filer-facing typo hint on the Ticket Center form. **Swaps are NOT the
   filer's;** they happen later, in the backend (C-SWAP, ruled 10-14 with the longest-history qualifier).
3. **Andrew will test** (the stage-2/5 package and the Open-tab attachments) "whenever ready".
4. **Prices:** Yahoo first, YCharts as fallback, as already recorded
   (`ANDREW_DIRECT_20261014_175xZ_PRICE_ORDER_YAHOO_THEN_YCHARTS_THEN_REPLACEMENT.md`; CTO prices addendum 2 @ac60268494). No build
   order is cut on it yet.
5. **Parallelize** toward a full end-to-end system. The other items run in sequence.

## The CRO's lane proposal (for the CTO's ruling)

**Measured 14:2xZ:** IRPT_ANLREQ has 0 open orders and IRPT_YCDGEN has 0. The seats that can carry this work are live and idle or
waiting:
- `2.0.0_SA_COO~Y2` (IRPT_ANLREQ);
- `~G2` (IRPT_YCDGEN; it was waiting on f61b, now withdrawn);
- `~T2` (the commentary workstream, 0 open);
- `~P2` (IRPT_BCKEND, which owns IB-pr-456);
- `0.7.0_AE_CloudOps~AQ2`, `~YC2` and `~CA2`.

**No new seats are needed. The gain is cutting four lanes at once on disjoint surfaces:**

| lane | seat | surface | cells, in order |
|---|---|---|---|
| UNBLOCK | `~P2` + an AE applier | `irpt-ycharts-generate` | IB-pr-456 applied now (f61b withdrawn; addendum 1 signed both halves). This alone reopens DEV filing. |
| FILING + PROMOTE | `~Y2` | portal `TicketCenter/`, the PROD promote | DEV filing re-proved after IB-pr-456; "Did you mean" at the form; then ONE PROD promote of J7 + filing + the D2-S118 list fix; then TO-RUN-FWD1 and Andrew's test |
| REPORT ENGINE | `~G2` | `ycharts/research/` (Opal producer), `producer_for` | C-PRICES (estate stores, Yahoo, YCharts per symbol, then report without the security, named); C-SWITCH by ticket-confirmed `ticket_id`; C-SWAP step 2 (backend replacement); Comparison/Multi-Comp variants |
| COMMENTARY | `~T2` | `data/transcripts/scripts/commentary/` | the drafter reads the produced report's figures and a non-empty transcript source |

**Shared hazards:**
- The resident release is ONE artifact. `~G2`'s and `~Y2`'s resident changes ride one release under one pair; they are not
  applied separately.
- The CVO's grading load grows. The four-lane CVO rule from the IRPT_DASHBD split applies.
