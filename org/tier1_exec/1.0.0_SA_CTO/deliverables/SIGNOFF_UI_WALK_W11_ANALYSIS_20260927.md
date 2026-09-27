# CTO half -- UI walk WINDOW 11: the Analysis chain, fourth attempt, on resident wf (packet blob 9ee0c7c5) -- SIGNED

**Seat:** `1.0.0_SA_CTO`, 2026-09-27 ~12:5xZ. **Request:** 2.0.0_SA_COO~P msg 101868 (on ~Y 101866).

**Packet:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W11_ANALYSIS_20260927.md`
@`7aad982d3e`, blob `9ee0c7c5`. Read at HEAD: `git hash-object` equals `git rev-parse 7aad982d3e:<path>`.

**The base text:** window 7, blob `3ab51a52` (CTO half @`c226ade7a3`), with D2 (the principal kept until every job is
terminal, a 120-min cap) carried.

## What was read

- **Start condition (W11-2):** Andrew at ~Y, verbatim: "yes you can run as many analysis attempts as needed"
  (@`460e2ae8cb`). This window is ONE attempt: ONE upload (K4) and ONE Overview (K5), with no retry.
- **Served code (W11-1):**
  - resident `fe64236bbb-wf` carries the read-back WAF refresh ruled at CTO 101792 (c);
  - ~Y proved it offline (101809), and it is served content-identical (~Y 05:56Z status, ledger @`85b4dedb9e`);
  - the pins are re-read at create, and there is no window if any differs.
- **K5's YCharts calls (W11-3) are exactly the (c) bounds:**
  - at most 6 status GETs, 15 s apart, with the lease renewed;
  - ONE re-capture through the job's ONE `session_refresh` intent on a read WAF challenge;
  - a second challenge goes ATTENTION, with no further capture.
- **The two added kept writes:** the intent row, and a new session-secret version (AWSCURRENT moves). Both are the same
  shape as the S151 run Andrew authorized.
- **K10 (W11-4):** journal and table reads only; the page cannot list the job yet (S18/E9).

## Named item (a condition of this half)

**The audit reads the bounds from the resident journal, not from the walker's log:**
- the count of `model_portfolios/{id}/status` GETs must be 6 or fewer;
- the count of host re-captures must be 1 or fewer.

If a re-capture ran, the prior session-secret version stays as AWSPREVIOUS; it is not deleted. An overrun of either
bound is a BLOCKING row the same tick.

**CTO half: SIGNED on blob 9ee0c7c5.** The CRO half is separate.
