# Window 7 (the Analysis chain, second attempt): live through the YCharts portfolio create; the read-back refused a `calculating` portfolio -- diagnosed, fixed, proved offline

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~03:3xZ.

Packet: `IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W7_20260927.md` @74e9998d9c, blob `3ab51a52`. The CTO half is
c226ade7a3 and the CRO half d9b4142aa6.

Go: Andrew, "yes to all three" at ~P, @6039c2f680. The principal was `irpt-uiwalk-1790477665`.

## What ~Y did: one login and exactly two POSTs, in the CRO's order (`live_walk/live_chain.py`)

| Time | Act | Answer |
|---|---|---|
| 02:58:17Z | login (after ~D's at 02:56:29Z) | 200; the token was held in memory |
| 02:59:54Z | the password parameter read absent (P deleted it) | K4 released |
| 02:59:57Z | **K4** `POST /analysis/inputs` | 200 RESOLVING; then **NORMALIZED** at 02:59:58Z, input `portfolio_65bfe6d9..` |
| 03:00:01Z | **K5** `POST /analysis` (Overview, null title) | 200 **QUEUED**, `REQ-e2fc5dd5dc2e050cc82a57e4` |

The log is `LIVE_CHAIN_1203_20260927_W7.json`: 3 calls, 0 password values, 0 tokens.

## What the resident did (read-only observation)

Terminal at 03:00:10Z, `handled=1`, queue 0/0. The job went **ATTENTION `VENDOR_READ_BACK_REFUSED`**.
- The vendor session was valid: the fresh S151 session, fence 13. No capture was needed.
- **Holdings upload**: `checkpoint_upload` ok, 2 rows, Dollars, `upload_record_id` 779765.
- **Portfolio create**: `checkpoint_portfolio`, `model_portfolio_id` 2363504.
- Then the 7-setting read-back refused. There was no validate, no report create and no PDF.
- The two YCharts objects (the upload and the portfolio) are kept and named in P's ledger.

## Cause

- `recipe.step_read_back` GETs `/model_portfolios/<id>/status` **once**, about 2 s after the create.
- YCharts answers a new portfolio `calculating` before it is `available`. That answer is a 200, or a 202 during
  calculation polling, and its body carries **only** `status`. This was measured on an earlier live run:
  `fixtures/har/decision_branches.json`, "after three healthy `calculating` responses".
- So all 7 setting fields compared as absent.
- The offline pre-flight replayed `status_ok.json`, which is `available`, and so could not see it.

Recipe values, checked: `intake/settings.json` maps exactly to the vendor values in `status_ok.json` (0.003,
quarterly, no dividend reinvestment, oldest, prior_close, non_qualified, ^SPXTR), so the values themselves are not
the defect.

## Fix (`P_READ_BACK_POLL_20260927.patch`; Y branch `edac4aa42f`)

- `step_read_back` waits out a healthy `calculating` answer: bounded at 12 polls, 5 s apart. It compares the first
  answer that is not calculating.
- Any other answer (available, an eviction or an error) returns at once, so the eviction and refresh rule is unchanged.
- A refused vendor step now prints `IRPT_RESIDENT_STEP_REFUSED` with the step, status, portfolio_status, polls and
  the drifted setting names. These are closed tokens only.

The patch applies cleanly (apply-check rc=0) to CLOUD and to P's tree.

## Proof (the real resident entry point, offline)

Setup:
- The resident package with overlays equal to the served `fe64236bbb-xv` content.
- The real Overview PDF and the production census.
- YCharts answering `calculating` 3 times.
- `resident_job_preflight.py --status-calculating N` (the instrument now never overlays `fixtures/`).

| Run | Result |
|---|---|
| served content, no fix | **ATTENTION** after the upload and create, 1 status GET: window 7's exact shape (the same checkpoints and intents) |
| + fix | **READY**, 4 status GETs, 1 REPORT# published, checkpoint_publication set |
| + fix, 20 calculating (past the bound) | ATTENTION with `IRPT_RESIDENT_STEP_REFUSED step=read_back status=200 portfolio_status=calculating polls=12 drifted=<the 7 setting names>` |

Tests: `test_read_back_poll.py` 5/5. The resident suites have 38 passed and 8 skipped, the same as before; a first
draft that polled through a 403 broke the two eviction tests and was corrected.

## Limits

- Twelve polls at 5 s give about 60 s. A portfolio that calculates longer is refused with its status named, not
  compared.
- The live answer after `available` is not yet seen for these holdings.
