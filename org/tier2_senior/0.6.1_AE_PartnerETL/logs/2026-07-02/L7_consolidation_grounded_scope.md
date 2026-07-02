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

## Next
RAVC 1.0.0_SA_CTO with this scope + Q-A/Q-B; on his arch-gate, build the additive-9ET-trigger
safe-apply plan first (non-destructive), N-nightly-verify, THEN the staged cron/Lambda delete.
