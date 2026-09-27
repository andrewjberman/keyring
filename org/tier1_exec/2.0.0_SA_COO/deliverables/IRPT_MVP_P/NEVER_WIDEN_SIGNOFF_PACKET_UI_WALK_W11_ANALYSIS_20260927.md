# Never-widen sign-off packet -- WINDOW 11: the Analysis chain, fourth attempt, on resident wf (the read-back WAF refresh)

**For:** `1.0.0_SA_CTO` and `4.0.0_SA_CRO`. **Operator of create and delete:** `2.0.0_SA_COO~P`, 2026-09-27 ~12:5xZ.
**Walker:** `2.0.0_SA_COO~Y` (live_chain.py). **Ledger (opened before any write):** `irpt-ui-walk-principal-w11-20260927`.
**Asked by:** ~Y 101866.

This packet is window 7's (`NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W7_20260927.md`, blob 3ab51a52, itself window 6's
fffdca65 + D1-D5) with only the deltas below. Every unnamed section reads as window 7's, including:
- the keys K1-K5 and K10, and K5's measured write set;
- the superadmin radius and the route audit;
- D2: the principal stays until EVERY job the window started is terminal, with a hard cap of 120 min, and a same-tick
  signed amendment for a non-terminal job at the cap;
- K1-CRED deleted as soon as the walker has logged in.

## Why a fourth attempt

Window 8's W8-2 reached the portfolio create, then YCharts' WAF challenged the 3rd read-back status poll and the job went
ATTENTION VENDOR_READ_BACK_REFUSED (~Y 101791). CTO 101792 ruled (c). ~Y built and proved the fix offline (101809), and
it is SERVED in the resident as `fe64236bbb-wf` (ledger irpt-resident-waf-refresh-20260927, @85b4dedb9e).

## W11-1 -- the served code, re-read at create

| Hop | What serves it |
|---|---|
| 1-3 | irpt-ycharts-generate `G/TqLPdL..` |
| 5-7 | resident `/opt/irpt-resident/fe64236bbb-wf`: rb + the read-back WAF refresh (e2fdd01015: recipe, resident_worker, session/broker) |
| 8-9 | irpt-status `bMMJ/bQ+5..` |
| Performance | adapter `bOefL9nx..` with NO plan (not used in this window) |

If any differs, the window does not open.

## W11-2 -- start condition

- P creates on both halves at HEAD.
- Andrew's word at the ~Y terminal is given, verbatim: "yes you can run as many analysis attempts as needed" (~Y record
  ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md @460e2ae8cb). This window is ONE attempt: ONE upload
  (K4) and ONE Overview submission (K5), with no retry inside the window.

## W11-3 -- K5's named YCharts calls (CTO 101792 (c), ~Y 101809/101866)

- the identity and template reads, the holdings upload and the portfolio create, as window 6's list;
- the read-back: up to **6** `model_portfolios/{id}/status` GETs, 15 s apart, with the operation lease renewed between
  polls (this replaces CTO 101763's "up to 12, 5 s apart");
- on a WAF challenge to a status READ: ONE host session re-capture (the S151 wrapper, a form sign-in) through the job's
  ONE `session_refresh` intent, then the read again. A second challenge goes ATTENTION
  SESSION_REFRESH_ALREADY_USED, with no further capture;
- validate, the report create and ONE PDF download.

**Writes this adds to K5's set:** on a challenge, the `session_refresh` intent row and a new version of the YCharts
session secret written by the capture (the existing secret, AWSCURRENT moves). Both are KEPT, as on the research run.

## W11-4 -- K10

The request-list route is served (GET .../analysis/requests on irpt-status, owner-scoped; P 101848), but the portal's
LiveClient still refuses it (DSGN_IRPTV1-S18/E9). So K10 is the resident journal, ~Y's status reads (hops 8-9) and
read-only table reads. A page read by ~D is not part of this window.

## W11-5 -- the audit adds

- the resident journal lines `IRPT_RESIDENT_READ_BACK_DONE ... polls= wall_s=` and any
  `IRPT_RESIDENT_STEP_WAF_REFRESH` or `retained_for_retry class=.. code=..` lines, named if they appear;
- the count of YCharts status GETs and re-captures, each against W11-3's bounds;
- the kept vendor objects (the portfolio and the upload) listed by id, as windows 6-8.

## What the halves sign against

This file's committed blob; window 7's text (3ab51a52) as amended here; K5's YCharts calls as bounded in W11-3, with
the challenge's two added writes; and the 120-min cap with the terminal-job rule.
