# Never-widen sign-off packet -- WINDOW 15: the Analysis chain, sixth attempt, on resident lt (release-and-resume + level tolerated)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~15:5xZ.
**Walker:** `2.0.0_SA_COO~Y` (live_chain.py). **Ledger (opened before any write):** `irpt-ui-walk-principal-w15-20260927`.
**Asked by:** ~Y 101927/101938; named WINDOW 15 by CTO 101929.

This packet is window 13's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W13_ANALYSIS_20260927.md`, blob 49ee40b0, signed CTO
@99311001d3 and CRO @ce115a43f1, itself window 11's 9ee0c7c5) with the deltas below. Every unnamed section reads as
window 13's, including:
- the keys and radius, and the route audit;
- D2: the principal stays until every job is terminal, cap 120 min;
- the start condition: Andrew's "yes you can run as many analysis attempts as needed" (@460e2ae8cb), with ONE upload
  and ONE Overview, no retry;
- the signing conditions: bounds counted from the resident journal, an overrun is a BLOCKING row the same tick, and
  the running re-capture total is printed (1 attempted, 0 completed after window 13).

## W15-1 -- the served code, re-read at create

Hops 5-7 run on `/opt/irpt-resident/fe64236bbb-lt` (since 15:51:47Z):
- cw: the W11 fixes (b6739556ea);
- dx: the W13 diagnostics (ec5804f6e0);
- rs: the read-back release-and-resume (38ee23deaa, CTO 101929);
- lt: level_as_of_type tolerated (49b85eacd2).
Each landed on its own ledger, with a census and a rollback root. Generate `G/TqLPdL..` and irpt-status `bMMJ/bQ+5..`
also re-read. If any differs, the window does not open.

## W15-2 -- K5's YCharts calls (CTO 101929, replacing W11-3's read-back bounds)

- as window 6's list: the identity and template reads, the holdings upload, the portfolio create; validate, the report
  create and ONE PDF download;
- the read-back: at most **2** `model_portfolios/{id}/status` GETs per receive, for at most **5** receives. A
  `calculating` answer or a read WAF challenge raises ReadBackPending: the message is retained for redelivery (about 900 s
  later), not ATTENTION;
- **0** host re-captures on a read challenge (the release replaces the re-capture);
- ONE `GET /model_portfolios/fixed/{id}` (the saved read) after `available`;
- the principal's life fits inside the 120-min cap (5 x 900 s = 75 min of releases, plus the work).

## W15-3 -- level_as_of_type (CTO 101929 item 2), verbatim from ~Y 101938

"The resident compares level_as_of_type on the saved portfolio and RECORDS the stored value (journal
tolerated=level_as_of_type=<stored>) without refusing on it. The recipe sends prior_close, which is what the advisor's
own YCharts form sends in all 5 HAR creates. It is a level-display basis, not a returns input; the other six settings
match live, and the certifier reads every as-of date off the PDF. An absent value, or any other drift, still refuses."

## W15-4 -- the audit adds

- per receive, the status GET count and each release;
- the saved GET and the `tolerated=` line with its stored value;
- the terminal state; on READY, the REPORT# row and its PDF (hop 7, certified) traced to the job.

## What the halves sign against

This file's committed blob; window 13's text (49ee40b0) and its conditions, as amended here; resident lt; K5's bounds in
W15-2; the level_as_of_type tolerance in W15-3.
