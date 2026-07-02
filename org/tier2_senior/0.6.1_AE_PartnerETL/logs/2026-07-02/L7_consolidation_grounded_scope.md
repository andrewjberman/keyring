# L7 Consolidation -- GROUNDED SCOPE (for CTO arch-gate)

**archetype:** TRACE
**author:** 0.6.1_AE_PartnerETL
**date:** 2026-07-02
**status:** grounding-complete; RAVC'd to 1.0.0_SA_CTO for arch-gate. NOTHING deleted.

## Question (CTO re-scope 184211Z)
Does `--chain full` self-run bronze (Q3), or rely on `opal-inf-bronze-runner`? Which interim
9ET crons are TRULY redundant vs DEPENDENCIES? Then RAVC the grounded scope + safe-apply plan.

## Q3 -- ANSWER: YES, `--chain full` self-pulls bronze AND silver in-process.
`data/inf/scripts/gold/orion-gold-dispatch.sh:334` `CHAIN_PULL` = the front-of-chain stage,
run in the SAME process before CHAIN_COMPUTE. It contains all REST pulls + their silver
converters: `INF_API_PULL_{UNIFIED,REPS,ASSETS_V2,NEW_PORTFOLIO,TXN,PERF,POSITIONS_DAILY,TAX,
BILLING,PERF_DIM}` + matching `INF_API_SILVER_*`. `CHAIN_FULL = CHAIN_PULL + CHAIN_COMPUTE`
(L337). So one `--chain full` invocation self-produces every REST-pull bronze+silver, then
computes gold -- no reliance on the interim crons for the DATA.

## Dependency-vs-redundant split (grounded)

### STAYS -- hard dependencies (NOT candidates)
- **`opal-inf-bronze-runner`** (eventbridge.tf:51 `opal-inf-bronze-runner-cron` cron(30 13)=9:30ET).
  Path-X `orchestrator.py` pulls Orion-API CSV **dims** -> `bronze/orion-api/{date}/{dim}.csv`
  -> `_BRONZE_COMPLETE.json`. **Gold READS this**: `INF_B_00.canonical_holdings`, `INF_D_04`,
  `INF_D_08`, `convert_orion_api_to_silver`. CHAIN_PULL does NOT produce `bronze/orion-api/`.
  => genuinely separate producer. STAYS.
- **`opal-inf-jwt-fetch`** (eventbridge.tf:16 cron(0 13)=9:00ET). Refreshes `secretsmanager-jwt`
  consumed by every pull (interim crons AND CHAIN_PULL). STAYS.
- **`inf-canonical-prices-daily`** (eventbridge.tf:117 cron(47 14)=10:47ET). Produces INF_S_00
  canonical prices (post-open market data; runs separately, before the freshness gate per
  dispatch L315) AND is a full-chain trigger. STAYS (role in new design = arch question below).
- **`inf-silver-aggregator`** + its s3-notification (s3-notifications.tf:29 `silver/_silver_complete/`).
  See trigger-topology finding -- currently load-bearing; becomes vestigial after decommission
  (decommission-in-same-pass is an arch question).
- **`inf-etf-ownership-on-gold-complete`**, **`inf-assets-trigger-bronze-complete`** -- event-driven,
  fire AFTER/on completion sentinels. STAYS.

### CANDIDATE decommission -- the 9 interim REST-pull crons (all 1:1 with a CHAIN_PULL stage)
| Cron rule | Schedule (ET) | CHAIN_PULL equivalent |
|---|---|---|
| inf-api-reps-daily | cron(17 13) 9:17 | INF_API_PULL_REPS (+SILVER_REPS/HHREP) |
| inf-accounts-v2-daily | cron(22 13) 9:22 | INF_API_PULL_NEW_PORTFOLIO+SILVER_ACCOUNTS_V2 |
| inf-unified-account-dim-daily | cron(27 13) 9:27 | INF_API_PULL_UNIFIED |
| inf-api-assets-v2-daily | cron(32 13) 9:32 | INF_API_PULL_ASSETS_V2+SILVER_ASSETS_V2 |
| inf-api-positions-daily | cron(37 13) 9:37 | INF_API_PULL_POSITIONS_DAILY+SILVER_POSITIONS_MV |
| inf-tax-daily | cron(42 13) 9:42 | INF_API_PULL_TAX+SILVER_TAX |
| inf-api-txn-daily | cron(47 13) 9:47 | INF_API_PULL_TXN+SILVER_TXN |
| inf-billing-daily | cron(22 14) 10:22 | INF_API_PULL_BILLING+SILVER_BILLING |
| inf-performance-daily | cron(27 14) 10:27 | INF_API_PULL_PERF+SILVER_PERF |

## CRITICAL finding -- the interim crons are the EARLY GOLD TRIGGER, not redundant pulls
Each interim-cron Lambda BUNDLES its silver converter and writes a per-dim sentinel:
- `inf-api-positions/lambda_function.py:94` -> `silver/_silver_complete/{date}/positions_daily.json`
- `inf-api-txn/lambda_function.py:118` -> `silver/_silver_complete/{date}/transactions.json`
`s3-notifications.tf:29`: `silver/_silver_complete/` ObjectCreated -> `inf-silver-aggregator`,
which "counts existing sentinels and fires gold trigger when N/N reached" (:24).

=> The 9 crons DRIVE the early gold fire (~10:27ET when the last dim's sentinel lands) via the
aggregator N/N fan-in. inf-canonical-prices-daily (10:47ET) is the separate/backstop trigger.
The single-runner CHAIN_PULL writes NO `_silver_complete` sentinels (grep-empty) => after
decommission the aggregator has no writers and never fires => **the early trigger is removed,
not merely a duplicate pull.** This is why the naive "delete 9 redundant crons" is WRONG and
CTO's dedicated-9ET-`--chain full`-trigger lean is the correct shape.

## Proposed safe-apply plan shape (for CTO arch-gate -- NOT yet executed)
1. ADD `aws_cloudwatch_event_rule` cron(0 13)=9:00ET -> `inf-gold-trigger` (mode=full). Replaces
   the aggregator-fan-in early trigger; self-pulls all bronze+silver in-process at 9ET (matches
   old timing). No re-entrant aggregator fire (single-runner writes no sentinels).
2. KEEP inf-canonical-prices-daily (10:47ET) for INF_S_00. **ARCH Q-A:** with the new 9ET
   full-chain trigger, does canonical-prices' full-chain fire become a SECOND daily run? Options:
   (i) 9ET trigger owns full-chain, canonical becomes compute-from-canonical only; (ii) rely on
   the dispatch-lock to dedup; (iii) INF_S_00 ordering means 9ET chain needs canonical -> keep
   canonical as the trigger and move the 9ET carry elsewhere. Needs your ruling.
3. DELETE the 9 interim REST-pull crons (rules + Lambdas + IAM + s3-notifications) -- STAGED,
   after >=N nightlies prove the new 9ET trigger produces gold cleanly.
4. **ARCH Q-B:** decommission `inf-silver-aggregator` + its s3-notification in the same pass
   (vestigial once no cron writes sentinels), or leave dormant?
5. jwt-fetch + bronze-runner + canonical-prices UNTOUCHED.

## Verification gate before ANY delete
N-nightly-verify: the new 9ET trigger fires inf-gold-trigger -> single-runner --chain full ->
served header_metrics advances to run-date, per-dim silver all fresh, AUA parity -- for >=N
consecutive nightlies BEFORE removing the interim crons. Destructive TF delete is COO/human-gated
(cron+Lambda removal), staged separately from the additive 9ET trigger.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Read/grep (source) | CHAIN_PULL defs, sentinel writers, s3-notifications, eventbridge | PASS -- topology grounded from source (Rule-22 mechanism, not inference) |
Rule-20 note: read-only grounding pass, no infra change made; the implementing safe-apply TO
will carry comp-aws/comp-iam checks at execution time.

## Q-A/Q-B RESOLUTION (grounded round 2, post CTO arch-gate 201756Z)

### Q-B gate PASSES -- aggregator is truly writer-less once the 9 crons are gone.
Full-estate grep of `silver/_silver_complete/` writers = EXACTLY the 9 interim crons (one dim
sentinel each: accounts_v2/assets_v2/positions_daily/representatives/transactions/billing/
performance/tax/unified_account_dim) + inf-silver-aggregator's OWN `_AGGREGATOR_FIRED.json`
idempotency marker (the consumer, retires WITH them). The single-runner writes ZERO. => safe to
decommission the aggregator + s3-notification IN Stage-3 WITH the crons (not before, not dormant).

### Q-A = OPTION (i) grounded-viable: --chain full SELF-PRODUCES INF_S_00; no post-open dep.
- `INF_S_00 = INF_build_canonical_prices.py`. Dispatch AUTO-RUNS it as a pre-gate step at the
  front of every `--chain full` (orion-gold-dispatch.sh:1394-1422: "auto-run INF_S_00 before the
  freshness gate ... aborts the full chain if it fails"). It does NOT read INF_S_00 from a
  separate producer -> the chain SELF-PRODUCES canonical prices in-process. This is the single
  fact CTO said "picks the option."
- INF_S_00 INPUTS (INF_build_canonical_prices.py:9-14,48-50): T1 transaction_observed =
  `silver/transactions/` (the SAME pre-open Orion txn silver CHAIN_PULL produces; ties to the
  forward-label seal) + T2 yahoo_finance = `silver/historical_prices.parquet` (separate daily EOD
  producer, FALLBACK tier) + T3 interpolation + T4 carry_forward. **NO post-open live market
  feed.** => the 10:47ET schedule is NOT price-driven; it is merely the chosen trigger cadence.
- => inf-canonical-prices-daily (10:47ET) is JUST a trigger, redundant with a 9ET --chain-full
  trigger; under option (i) it RETIRES too (add to Stage-3 delete). ONE full pull+compute/day at
  9ET, INF_S_00 self-produced fresh at the front. No double-run, no ordering issue.
- SECONDARY input-timing note (N-nightly verify item, NOT a blocker): T2
  `silver/historical_prices.parquet` is produced by the separate historical-prices pipeline
  (infra/aws/ec2/historical-prices/). Confirm it lands before the 9ET chain consumes it; T2 is a
  FALLBACK tier (T1 transaction_observed primary + T4 carry_forward), so a one-day-late T2
  degrades gracefully, not fatally. The INF_S_00 pre-gate/CHAIN_PULL internal ordering is
  UNCHANGED by moving the trigger time (pre-existing behavior, orthogonal to L7).

### Updated Stage-3 delete set (on CTO option-(i) arch-sign)
9 interim REST-pull crons + inf-silver-aggregator + its s3-notification + inf-canonical-prices-daily
(the 10:47 trigger) -- ALL redundant under a single 9ET --chain-full trigger. jwt-fetch +
opal-inf-bronze-runner UNTOUCHED (hard deps). Human-gated (COO + Andrew) on the specific resources.

## STAGE-1 BUILD (post CTO arch-sign option (i) 202800Z + A/B->OPTION B via COO 211327Z)

CTO ruled the A/B trigger-design fork = OPTION B (event-on-_BRONZE_COMPLETE) -- eliminates the
cron(0 13)=9ET-races-bronze-runner(9:30ET) ordering bug I caught pre-encode; fires after
Orion-settle; no magic offset. COO relayed + attached 2 requirements: (a) reliable sentinel to
key on; (b) confirm after-Orion-settle across N-nightly.

BUILT (commit d0bcfb876, infra/aws/terraform/inf-pipeline/eventbridge.tf, terraform validate PASS,
NOT applied): additive `inf_gold_full_on_bronze_complete` EventBridge rule (event_pattern
source=aws.s3 / Object Created / key bronze/orion-api/*/_BRONZE_COMPLETE.json) -> target
module.inf_gold_trigger constant input {mode:full,source:bronze-complete}, DLQ + retry(0) +
lambda_permission mirror inf_canonical_prices_daily_target; rule ARN added to the DLQ queue-policy
SourceArn. Non-destructive (runs ALONGSIDE aggregator+canonical through parity); dispatch-lock
(mode=full TTL5400) 409-dedups concurrent fires.

REQ(a) SATISFIED (grounded): orchestrator.py write_sentinel (L202-249) emits
bronze/orion-api/{date}/_BRONZE_COMPLETE.json EVERY run, completeness-contract-gated (BRONZE-FIX #2
hardened). No sentinel to add. NUANCE: body carries overall=success|failure|incomplete (not
success-only); EventBridge can't filter body, so the rule fires on EXISTENCE (mirrors
inf-assets-trigger, which does not overall-gate). Overall-gate = flagged OPTIONAL hardening
(handler would need EventBridge-S3-format parse + sentinel read); RAVC'd CTO 212249Z to rule
DEFER(my lean; served-guard+CVO parity are the backstops) vs ADD-now.

REQ(b): folded into the N-nightly verify checklist.

GROUNDING (Rule 22a): desired=validate PASS (now); applied+exercised=post-apply (aws events
describe-rule/list-targets live + first real bronze-complete fire) -- NOT asserting GREEN until
exercised.

## STAGE-1 DEPLOYED + VERIFIED + LEDGER CLOSED (CTO ACK 220637Z)

CTO arch-signed (212626Z), 2 apply-reqs delivered, DEPLOYED + applied-layer verified, ledger
CLOSED (advi-infref-l7-stage1-bronzecomplete-trigger, 5 legs proven, no half-deploy). CTO ACK
220637Z: "clean, complete Stage-1 -- all reqs met."
- LIVE: inf-gold-full-on-bronze-complete rule ENABLED -> inf-gold-trigger {mode:full,source:
  bronze-complete} on bronze/orion-api/*/_BRONZE_COMPLETE.json; inf-gold-trigger-dlq-depth alarm;
  source-map sibling removed. safe-apply 4add/1change/0destroy RC=0, 0-diff re-plan, live
  describe-rule/list-targets/describe-alarms confirmed (Rule 22a applied-layer).
- Commits d0bcfb876 + 6659e0110 + 854f20848 + close on origin/CLOUD.

## FIRST-EXERCISE CHECKLIST (the gate before Stage-3 -- RAVC CTO on the first fire)

Event-driven on the next scheduled bronze-complete (~13:30Z/9:30ET, 07-03). NEVER ad-hoc -- verify
on the SCHEDULED nightly's artifacts. Do NOT assert behavioral GREEN until ALL confirmed:
1. RULE FIRED: aws events / CloudWatch -- inf-gold-full-on-bronze-complete Invocations>=1 on the
   07-03 bronze-complete; inf-gold-trigger invoked with source=bronze-complete (dispatch-lock
   run_id, NOT a 409-reject-from-a-competing-trigger -- confirm the bronze-complete fire is the
   one that WON the lock, or that a win/409 both leave gold correctly produced).
2. CHAIN RAN + SERVED ADVANCED: gold/meta/pipeline-complete.json 07-03; platinum/firm/
   header_metrics.json generated_at advances; per-dim silver fresh; AUA parity.
3. AFTER ORION-SETTLE (req b): the fire + chain land after bronze/orion-api is complete (the whole
   point of the bronze-complete trigger) -- confirm timing.
4. T2 CADENCE: silver/historical_prices.parquet (separate historical-prices EC2 pipeline) landed
   BEFORE the chain consumed it (INF_S_00 T2 fallback tier; graceful if one-day-late but watch).
5. JULY-4-OBSERVED HOLIDAY EDGE (CTO 220637Z bonus): 07-03 is July-4-observed (in
   NYSE_CLOSED_DATES). The as_of-normalization must map served data_as_of to the PRIOR trading day
   07-02, NOT 07-03. Confirm the served data_as_of across the holiday -- exercises BOTH the L7
   trigger AND the as_of holiday-handling in one window. DLQ stays empty (else the alarm fires).

On {all 5 GREEN across N nightlies} + the human gate (COO+Andrew): Stage-3 delete proceeds under
NFRA_PPLINF decommission. Overall-gate = deferred hardening follow-on. jwt-fetch + bronze-runner
UNTOUCHED. Nothing applied/deleted beyond the additive Stage-1.
