# Daily Cloud drilldown: why keywords served the "evolving" card, and the fix -- keyword-intelligence-generator after BOTH daily runs -- 0.1.0_DS_MarketIntelligence

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, DEPLOY, VALIDATE

**Date:** 2026-09-15 (UTC; window ~03:10Z -> ~04:55Z, which is 2026-09-14 ~11:10 PM -> ~12:55 AM ET)
**Task Order:** none -- Andrew-direct at this terminal, three lines, recorded verbatim in
`org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/ANDREW_DIRECT_20260915_031xZ_DAILY_CLOUD_ANALYSIS_FOR_ALL_ITEMS.md`
(`35981f7456`, follow-ups `c7719c062b`) and broadcast (96881-96883, 96890-96892: `1.0.0_SA_CTO` and
`0.0.0_AB_MSTR` DELIVERED; `2.0.0_SA_COO` QUEUED both times -- no live base session)
**Status:** COMPLETE -- tonight's served cloud 20 of 20 visible keywords FULL; the gate change APPLIED and
proven read by the deployed bytes; ledger `news-kig-evening-bypass` CLOSED 5 of 5. The gate's own exercised
proof is the 2026-09-15 21:15Z fire (Next Step 1).
**Workspace CLOUD commits:** `35981f7456` (record) -> `c7719c062b` (record follow-ups + ledger OPEN) ->
`e2d9f703e9` (terraform env, audited lane override `CLOUD_OPS_OR_ETL`) -> this commit (ledger CLOSE + this
log). Push state: all LOCAL at commit time; origin not re-read inside this window.

---

## Objective

Andrew: *"I need you to look into why we surface the following in the Daily Cloud drilldown modal:
ukraine train strike ... Sentiment is evolving quickly ... We should have analysis for all items that appear
in the Daily Cloud."* Then *"Bypass cost gate"* and *"everything it displays there should have full data."*

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | "what depends on the news-trending-analysis lambda before I change its environment variables" | PASS | routed to comp-blast (tie with comp-kuzu, comp-pulse; read the descriptions) |
| comp-blast | `news-trending-analysis` | PASS | Rule 20 graph check: 29 downstream nodes (LOWER BOUND), served graph vintage 2026-09-15T03:31Z; the relevant node is `opal-keyword-intelligence` |
| .tools/aws (shim) | s3api get-object (+`--version-id`), list-object-versions, head-object; dynamodb query/scan; lambda get-function(-configuration), invoke; logs describe-log-streams, filter-log-events | PASS | `PYTHONIOENCODING=utf-8` throughout; the `/aws/lambda/...` log-group args passed literal by the shim |
| terraform plan | x3 on `infra/aws/terraform/news-pipeline` | PASS | 0 add / 1 change / 0 destroy, env-only; saved plan file; re-plan after apply "No changes" |
| safe-apply.sh | the saved plan | PASS | comp-tagauthz PASSED, tombstone-gate CLEAN, "Apply complete! Resources: 0 added, 1 changed, 0 destroyed." |
| deploy_ledger.py | open, close-leg x5, close | PASS | opened before the terraform commit and the apply; each leg carries its proof |
| safe-commit.sh | 4 commits | FAIL then PASS | one refusal on a foreign `index.lock` (`2.0.0_SA_COO~D` mid-commit, 41 s earlier); retried clean. My own first read of that refusal grepped the log and missed the reason -- re-read in full |
| commit-gate (inside safe-commit) | `lambdas.tf` | PASS | clean 1 of 1 |
| comp-pulse risk reflex (inside safe-commit) | diff | PARTIAL | danger map ~92h STALE -> NOT-DECIDABLE every time |

Role minimum (DS: `comp-pipescript io` per gold script touched): SKIPPED with reason -- no gold script
touched; the surfaces are Lambdas under `infra/aws/lambda/` and one Terraform env line.

**What worked:** S3 versioning on the cloud file let the generator's exact input be re-read (the 20-of-20
mechanism check); downloading the LIVE zip and hash-matching it to CodeSha256 proved an env-only change was
sufficient before any apply.
**What failed:** nothing on the change path. Instrument note: my first article-title field guess (`title`)
read None -- the cache rows use `headline`.
**Gap found:** documentation drift, noted not fixed -- the trending invoke log line still reads "(async,
morning run)" on every run; `keyword_intelligence_generator/lambda_function.py:8,26` and `eventbridge.tf:176-186`
describe schedules that are not the live ones.

---

## Work Completed

### 1. The chain, from source
Modal (`portal/src/components/market-performance/KeywordSentimentModal.tsx:191-234`) -> POST
`/v1/sentiment/keyword-intelligence` -> `portal_data_proxy.get_keyword_intelligence`: exact lowercase keyword,
`generated_date` = today UTC, then 1..7 days back (`lambda_function.py:1469-1501`); on a miss it returns
`_evolving_keyword_card` (`:1401-1437`, returned at `:1675`; introduced `09f361593c` 2026-06-10) -- no model call.
The cache `opal-keyword-intelligence` is written only by `keyword-intelligence-generator`, which processes
`keywords[:MAX_KEYWORDS]` (20, matching `TopicCloud.tsx:135` `.slice(0, 20)`) of
`s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json`, skipping keywords already written today.

### 2. Root cause, measured
- `news-trending-analysis` rewrites the cloud file at BOTH runs (bucket versions 11:16Z and 21:16Z daily)
  but invokes the generator only when `hour_utc < KIG_MORNING_CUTOFF_UTC` (default 17 -- `903fbe9a8d`,
  "gate keyword-intelligence-generator to MORNING run only (Andrew 2026-06-11)"). Live log 2026-09-13 and
  09-14 21:16Z: "SKIP: keyword-intelligence-generator not invoked (evening run hour=21 >= cutoff 17 UTC)".
- Generator runs, 7 of 7 days 09-08..09-14: one per day at 11:16Z, 20 keywords each (140 rows).
- 2026-09-14: the MORNING file's first 20 == that day's 20 cache rows (20 of 20). The EVENING run
  re-clustered and relabelled: 6 of its visible 20 were morning labels, 7 of 20 had any cache row in the
  proxy's lookback -> **13 of 20 visible keywords served the pending card from 21:16Z to the next morning.**
- "ukraine train strike": evening label (cloud count 23, sentiment -0.6073); 0 cache rows ever; the morning
  label for that cluster was "russia-ukraine conflict".

### 3. Andrew's rulings
"Bypass cost gate" answered this seat's three-option question; read narrowly as option (1). It supersedes the
2026-06-11 morning-only ruling for `keyword-intelligence-generator` only.

### 4. The fix (ledger `news-kig-evening-bypass`, CLOSED 5 of 5)
| Leg | Proof |
|---|---|
| L1 git | `e2d9f703e9` (the env line) + `c7719c062b` (OPEN sentinel), both before the apply |
| L2 apply | safe-apply of the saved plan: 0 added / 1 changed / 0 destroyed, ONLY `aws_lambda_function.trending_analysis`, ONLY `+ KIG_MORNING_CUTOFF_UTC = "24"` |
| L3 live | env `KIG_MORNING_CUTOFF_UTC = "24"`; CodeSha256 `veHir0Ww..` unchanged; Active / Successful; re-plan "No changes" |
| L4 bytes | live zip 43,066 bytes hash-matches CodeSha256; LIVE `lambda_function.py:1594-1595` reads the env inside the handler |
| L5 fill | ad-hoc generator run 04:23:46Z-04:28:48Z: total 20, written 20, errors 0; 20 of 20 visible keywords FULL (summary 395-540 chars, 2-4 drivers, not pending), "ukraine train strike" 472 chars / 4 drivers / confidence high |

### 5. Residuals, surfaced not fixed
- **A ~4-5 minute pending window after every cloud publish.** The generator runs async AFTER the cloud file
  is written (20 keywords took 5m02s; the evening pass does only new labels, ~14 on 09-14).
- **The modal header's "N articles" is the carried sample, not the cloud's count** -- **11 of the 20 visible
  keywords** show fewer articles in the modal than their cloud count, every one at exactly 10 (samples capped
  at 10 by `news_trending_analysis/lambda_function.py:1495`); e.g. "ukraine train strike" cloud count 23, modal
  "10 articles"; "oil pipeline attack" cloud count 96, modal 10. The other 9 have <= 10 and match.
- Keywords beyond the visible 20 (23 of 43 in the evening file) get no analysis -- not displayed, so outside
  "everything it displays".

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Env override, not a code change | the gate reads `KIG_MORNING_CUTOFF_UTC` per run (proven in the LIVE bytes); build ladder rung "native feature" -- no zip, no rebuild |
| Asked before changing anything live | lifting the gate reverses his own 2026-06-11 cost ruling (+~70% generator spend); his answer is the authority |
| Read "Bypass cost gate" narrowly | the question named one gate; nothing wider is touched |
| Filled tonight's cloud with one ad-hoc generator run | "everything it displays there should have full data" -- the next scheduled evening fire was ~17h away; the generator is idempotent per day |
| Apply the SAVED plan | applies exactly what was reviewed |
| Did not fix the residuals | the pending window needs a sequencing change in the trending Lambda; the header count is a product choice -- both put to Andrew |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/deliverables/ANDREW_DIRECT_20260915_031xZ_DAILY_CLOUD_ANALYSIS_FOR_ALL_ITEMS.md` | verbatim record + two follow-ups | `35981f7456`, `c7719c062b` |
| `infra/aws/terraform/news-pipeline/lambdas.tf` | `+ KIG_MORNING_CUTOFF_UTC = "24"` with its reason | `e2d9f703e9` (audited override `CLOUD_OPS_OR_ETL`) |
| `org/critical_paths/change_management/20260915T0419Z_news-kig-evening-bypass_deploy_completion.md` + `.open_deploys/news-kig-evening-bypass.json` | ledger OPEN, then CLOSED (sentinel removed) | `c7719c062b`, this commit |
| this log | -- | this commit |

---

## Blockers

None.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| none -- the record, the ledger and this log carry it | -- | -- |

---

## Current State

`news-trending-analysis` (Lambda) now invokes `keyword-intelligence-generator` after EVERY run: live env
`KIG_MORNING_CUTOFF_UTC = "24"` (Terraform `infra/aws/terraform/news-pipeline/lambdas.tf`, `e2d9f703e9`),
code unchanged (CodeSha256 `veHir0WwfMuw0kE2A63LSXzVKJA0HqfzVLFHydU/t44=`). The Daily Cloud shows the first
20 keywords of `s3://opal-data-portal-v2/json/sentiment/keyword-sentiments.json`; the served version
(`XPbEJFWXYx7h..`, generated 2026-09-14T21:16:41Z) has 20 of 20 visible keywords with a full 2026-09-15
analysis in `opal-keyword-intelligence`, so the drilldown modal serves analysis, not the pending card, for
all of them. The next cloud rewrite is the 2026-09-15 11:15Z run (7:15 AM ET); from then on the generator
follows both rewrites. Rollback: delete the env line and `safe-apply` (the default 17 restores morning-only).

---

## Next Steps

1. **[0.1.0_DS_MarketIntelligence] Read the 2026-09-15 21:15Z fire (5:15 PM ET), the first run past the
   old cutoff** -- the gate's exercised proof: `news-trending-analysis` log at ~21:16Z reads "OK:
   keyword-intelligence-generator invoked" (not "SKIP ... evening run"); a generator log stream opens at
   ~21:16Z; the evening cloud's visible 20 are 20 of 20 FULL a few minutes later. Essential wait, stated:
   only a run at hour >= 17 discriminates, and an ad-hoc trending run would also rewrite the served cloud
   and the trending panel.
2. **[Andrew's call] Close the ~4-5 minute window** -- run the generator on the new keyword list BEFORE the
   cloud file is published (a sequencing change in `news-trending-analysis`).
3. **[Andrew's call] The modal's "N articles"** -- show the cluster count (e.g. "10 of 23 articles") or carry
   more samples; today it reads as if 10 were all.
4. **[0.0.0_AB_MSTR] Publish `35981f7456`, `c7719c062b`, `e2d9f703e9` and this commit** -- integrator-only push.
5. **[1.0.0_SA_CTO] Documentation drift** -- the generator docstring (`:8`, `:26`), `eventbridge.tf:176-186`
   and the trending invoke log text still describe the old schedules.
