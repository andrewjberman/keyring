# Never-widen sign-off packet -- WINDOW 13: the Analysis chain, fifth attempt, on resident cw (the W11 fixes)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~13:5xZ.
**Walker:** `2.0.0_SA_COO~Y` (live_chain.py). **Ledger (opened before any write):** `irpt-ui-walk-principal-w13-20260927`.
**Asked by:** ~Y 101895; named WINDOW 13 by CTO 101897.

This packet is window 11's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W11_ANALYSIS_20260927.md`, blob 9ee0c7c5, signed CTO
@1e5b0a08af and CRO @8253c62327) with only the deltas below. Every unnamed section reads as window 11's, including:
- window 7's keys and radius, the route audit, and D2 (the principal stays until every job is terminal, cap 120 min);
- W11-2's start condition: Andrew's "yes you can run as many analysis attempts as needed" (@460e2ae8cb); ONE upload
  and ONE Overview submission, with no retry;
- W11-3's bounds: at most 6 status GETs 15 s apart, and ONE host re-capture on a read WAF challenge (its two kept
  writes named there);
- the signing conditions: the bounds are counted from the resident journal, a re-capture keeps the prior secret
  version as AWSPREVIOUS, an overrun is a BLOCKING row the same tick (CTO 101875), and the ledger prints the running
  re-capture total (CRO 101877; 0 completed after window 11).

## W13-1 -- why a fifth attempt

Window 11's REQ-717c91a5 went ATTENTION VENDOR_READ_BACK_REFUSED on two defects that ~Y diagnosed
(LIVE_WINDOW11_EVIDENCE_20260927.md @647f229b23):
- the re-capture failed LEASE_NOT_HELD because the resident PYTHONPATH crashed the runner's aws CLI. The fix is
  `capture_env`, which strips PYTHON*;
- the read-back compared the STATUS body, which carries no settings. It now reads the SAVED portfolio once after
  `available`.

Both fixes are SERVED in resident `fe64236bbb-cw` since 13:51:07Z (backend b6739556ea; ledger
irpt-resident-capture-env-20260927 @45c9ac981e).

## W13-2 -- the served code, re-read at create

As W11-1, with hops 5-7 on `/opt/irpt-resident/fe64236bbb-cw`. If any differs, the window does not open.

## W13-3 -- K5's added YCharts call (CTO 101897)

ONE `GET /model_portfolios/fixed/{id}` after the status reads `available`: the saved portfolio's settings read-back,
the research worker's proven read. Every other W11-3 bound is unchanged.

## What the halves sign against

This file's committed blob; window 11's text (9ee0c7c5) and its signing conditions, as amended here; the one added
saved-portfolio GET; resident cw.
