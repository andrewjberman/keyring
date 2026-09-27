# Window 8, W8-2 (the Analysis chain, third attempt): the read-back poll ran live, and YCharts' WAF challenged the 3rd status poll

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~04:1xZ.

Packet: `IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_UI_WALK_W8_20260927.md`, blob `e2462004`. The CTO half is c42d47163d
and the CRO half 1dbf46c36b.

Go: Andrew, verbatim at the ~Y terminal, 04:01Z: "yes, run the Analysis window". The principal was
`irpt-uiwalk-1790481488`.

## What ~Y did: one login and exactly two POSTs (`live_walk/live_chain.py`)

| Time | Act | Answer |
|---|---|---|
| 04:02:03Z | login | 200 |
| 04:02:41Z | the password read absent | K4 released |
| 04:02:44Z | **K4** `POST /analysis/inputs` | RESOLVING, then **NORMALIZED** at 04:02:46Z, input `portfolio_acddb08c..` |
| 04:02:50Z | **K5** `POST /analysis` (Overview) | 200 **QUEUED**, `REQ-a8e81b8eccc800b2f3a00c8c` |

The log is `LIVE_CHAIN_1203_20260927_W8.json` (scrubbed).

## What the resident did (resident `fe64236bbb-rb`, which has the read-back poll)

- The holdings upload and the portfolio create succeeded: `model_portfolio_id` **2363801** (intents at 04:02:53Z and
  04:02:55Z).
- The read-back then ended **ATTENTION `VENDOR_READ_BACK_REFUSED`**. The journal, via the new closed-token line, gives
  the reason:
  ```
  04:03:10Z IRPT_RESIDENT_STEP_REFUSED step=read_back status=202 portfolio_status=- polls=3
            drifted=benchmark,level_as_of_type,management_fee,rebalance_frequency,reinvest_dividends,start_of_series,tax_status
  ```
- Reading that line:
  - polls 1 and 2 were healthy `calculating` answers, which the fix waited out;
  - poll 3 (about 10 s after the create) was a **202 whose body carries no status**;
  - that is the WAF challenge shape measured before (`decision_branches.json` `WAF_REFRESH_REQUIRED`, and the
    research README: "202 with `x-amzn-waf-action: challenge` during calculation polling, after three successful
    `calculating` responses").
- The broker classifies a WAF challenge on a read as `BROWSER_ATTENTION / WAF_CHALLENGE` (`controller.py:35-37`).
  `eviction_verdict` refreshes only on `EVICTED` or `SIGNED_OUT` (`broker.py:319`). So by design no re-sign-in
  happened, and the job stopped.
- There was no validate, report or PDF. The upload and portfolio 2363801 are kept.

## What is known and what is not

- **Known:** both live polling sequences at 5 s spacing (the research run and this one) were challenged by the WAF at
  about the 3rd status poll. A single read (window 7) was not challenged.
- **Recovery that worked before:** the research run recovered with ONE browser re-capture of the session, which earned
  a fresh WAF token, then resumed at the checkpoint with no second portfolio POST. "All successful variant runs
  reused this generation."
- **Not known:**
  - whether the trigger is request rate on the status route or the age of the session's WAF token (captured 02:02Z,
    two hours earlier);
  - the session bundle records the `aws-waf-token` cookie with no expiry, so token age cannot be read offline.

## Decision for 1.0.0_SA_CTO (the recovery policy is a design rule, not ~Y's to change alone)

- (a) **A WAF challenge on a status READ spends the job's ONE refresh:** a browser re-capture that earns a fresh
  token, then a resume at the read-back checkpoint. No mutation replays; the upload and portfolio are checkpointed.
  This matches the research's proven recovery.
- (b) **Gentler polling only**, for example 15 s spacing with a transport-lease renew between polls. This is unproven
  against the WAF.
- (c) **Both.**

**REC: (c).** (a) is the only recovery with live evidence, and (b) lowers how often it is needed. Either way the next
window's packet names the re-sign-in as a vendor act.

## RULED (c), bounded (CTO 101792) -- built and proved offline (04:5xZ)

Fix: Y branch `4aaeaea3d5`, `P_READ_BACK_WAF_REFRESH_20260927.patch`. The patch is cut against P's deployed `rb` files
(`07f1982ab9`) and applies cleanly (apply-check rc=0) to P's deploy tree `irpt-smoke-p-backend-20260923`. Its runtime
files are content-identical to the overlay proved below.

1. **The poll backs off:** 6 polls, 15 s apart, with the operation lease renewed between polls. A WAF answer ends the
   loop at once. The result carries `polls`, `wall_s` and `waf_action`, and a successful read-back prints
   `IRPT_RESIDENT_READ_BACK_DONE ... wall_s=`.
2. **A WAF challenge on a status READ** (`broker.waf_read_verdict`: only a `status_poll` observation classified
   `BROWSER_ATTENTION/WAF_CHALLENGE`) prints `IRPT_RESIDENT_STEP_WAF_REFRESH` and spends the job's ONE
   `session_refresh` intent. It then re-runs the read. A challenge on a mutation stays reconciliation.
3. **A second challenge** finds the intent used and goes ATTENTION `SESSION_REFRESH_ALREADY_USED`.

Proof at the real entry point (`resident_job_preflight.py`): the served `rb` content plus overlays, the real Overview
PDF and the production census, and `--capture-stub` standing in for the Linux-only host browser capture.

| Run | Result |
|---|---|
| window 8's live shape (2 calculating, then a 202 challenge with no body status), deployed `rb` | ATTENTION `VENDOR_READ_BACK_REFUSED`; journal `step=read_back status=202 portfolio_status=- polls=3 drifted=<7>`, **identical to the live line** |
| the same, with the fix | `STEP_WAF_REFRESH ... polls=3 wall_s=31.6`, 1 capture, `READ_BACK_DONE ... available polls=1`, **READY**, 1 REPORT# |
| the research shape (decision_branches `WAF_REFRESH_REQUIRED`), with the fix | READY, 1 capture |

Tests: `test_read_back_poll.py` 6/6. In `test_resident_worker.py` the WAF arms pass 2/2: one challenge gives one
capture and READY with one upload and one portfolio POST; a second challenge gives ATTENTION
`SESSION_REFRESH_ALREADY_USED`. The eviction arms still pass, and the resident suites have 46 passed and 8 skipped.

Instrument limit: the pre-flight's DynamoDB double records the `session_refresh` claim's condition but does not
evaluate it, so its two-challenge arm refreshed twice. Bound 3 is proved by the unit test, which evaluates the claim.

For the next packet (ruling item 4), the K5 vendor calls add:
- up to 6 status GETs 15 s apart;
- on a WAF challenge, ONE host session re-capture (the S151 wrapper: a form sign-in) and then the read again.
