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
