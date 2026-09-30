# ANDREW-DIRECT 2026-09-30 ~12:5xZ -- /open-calls at `1.0.0_SA_CTO~Z`: all five RECs approved; trust tokens and backoff

**Terminal:** `1.0.0_SA_CTO~Z`, site Z. **Answers:** this seat's `/open-calls` frame (5 cards, ~13:0xZ), including the same-turn
correction to card 1 (push only after DSGN round-13 cell 1 lands).

## VERBATIM

> recs approved for all + we have credentials for everything in AWS Secrets. Furthermore, you most likely should just use existing
> trust tokens secured from past runs. Crawling is only necessary if existing trust tokens are not working. Important to not
> confuse rate limit for trust token expiry. Also recommend a retry backoff for the REST API hits with that in mind. Regarding
> Never-2 edit, want to know what the suggested edit is.

## WHAT EACH APPROVAL IS (scope read from the card, never wider)

| card | approved REC, as carded | routed to |
|---|---|---|
| 1 | Merge origin/DEV into site-Z portal DEV (pull-merge, never a rebase), re-run tsc and the 16 harnesses, push DEV only. **Only AFTER DSGN_AMGTV1 round-13 cell 1 (the no-dossier reader) lands**, per this seat's correction. PROD is a separate word. | `0.0.0_AB_MSTR~Z` |
| 2 | Remove the drained worktrees LISTED, with branches kept: DSGN `/c/tmp/wk-dsgn-amgtv1-18..48`, the `C:/tmp/cood-r*-root` scratch roots and `C:/tmp/dsgn-r12-dist`; HARVST `wk-hvst-r24..r28`. **No other worktree is covered.** | `2.0.0_SA_COO~D` (DSGN), `2.0.0_SA_COO~H` (HARVST) |
| 3 | Re-arm the harvest collection schedule AFTER backfill batch 1, daily, for the names batch 1 reached. | `2.0.0_SA_COO~H` |
| 4 | barrons B1: yes. ft F2: hold until the kept 403 body is read. **Superseded in mechanism by his added words:** the credentials are in AWS Secrets, and existing trust tokens come first (below). | `2.0.0_SA_COO~H` |
| 5 | NOT approved as an edit. **He asked to see the suggested text first.** This seat shows it in its reply; the edit waits on his word after reading it. | -- |

## HIS ADDED DIRECTION (binding on AMGT_HARVST collection; lands as PRD CONTRACTS `C-HV-TRUST-TOKEN`)

1. **Credentials:** "we have credentials for everything in AWS Secrets". A collector reads its publisher credentials from AWS Secrets
   Manager. No credential is asked of Andrew, typed, or harvested by an agent.
2. **Trust tokens first:** "use existing trust tokens secured from past runs". A run starts from the stored session/trust token of a
   prior successful run.
3. **Crawl last:** "Crawling is only necessary if existing trust tokens are not working". A fresh sign-in or crawl happens only when
   the stored token is shown not to work.
4. **Rate limit is not expiry:** "Important to not confuse rate limit for trust token expiry". A 429 or throttle response is a RATE
   LIMIT: back off and retry, and keep the token. Only an auth failure that persists after backoff (401, or a 403 whose kept body
   says the session is invalid) marks the token expired.
5. **Backoff:** "recommend a retry backoff for the REST API hits with that in mind". Every REST call retries with exponential
   backoff and jitter on rate-limit responses, bounded. Each attempt's status and wait is written to the run record.

**Effect on the act list:** "the barrons B1 run and the ft F2 credentials [R-21 call 1]" is REMOVED from the acts listed for Andrew.
Both become collection work under his word, scripted (R-21).
