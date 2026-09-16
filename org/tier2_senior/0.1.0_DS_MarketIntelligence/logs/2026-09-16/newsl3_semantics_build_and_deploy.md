# News scanner semantics: four fixes built, deployed and exercised on Andrew's word -- 0.1.0_DS_MarketIntelligence

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Date:** 2026-09-16 (UTC), window 03:0xZ-04:2xZ
**Task Order:** ad-hoc / Andrew-direct ("do it", ~03:5xZ) on the deep-dive recommendations
**Status:** COMPLETE -- ledger `news-scanner-semantics-20260916` CLOSED, 5 of 5 legs with proof

---

## Objective

Land Andrew's rulings on the deep dive (`NEWS_SCANNER_DEEP_DIVE_20260916.md` Section 6): fix
recency and remove the quality score; gap-fill what FinBERT could not score (gpt-4o-mini,
flagged); decide cluster direction by a market judgment call (gpt-4o-mini, flagged); tie the
modal's card to the cloud's inputs. Then deploy all four Lambdas and prove the new code
EXERCISED on served artifacts.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| .tools/commit-gate.sh | on every edited .py | PASS | caught 6+1 pre-existing ruff findings at HEAD (cleared) and one dead var of mine |
| .tools/safe-commit.sh | 7 commits, DS author; 1 under audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` | PASS | the override was for the AE-lane source map + record script only |
| build-and-upload.sh news-pipeline <fn> x4 | S3 artifact + content-sha256 | PASS (1 refusal, correct) | ADHC_DRIFTD.002 refused L3 until `render_check.py` was declared in files[] |
| terraform plan/apply via .tools/safe-apply.sh | news-pipeline | PASS | baseline No changes -> 0/4/0 -> re-plan No changes; HALTGT silent pass, comp-tagauthz PASS |
| .tools/deploy_ledger.py | open / close-leg x5 / close | PASS | rollback rows carried pre-act S3 VersionIds |
| record-terraform-deploy.sh --function | source map rows | PASS after 2 fixes | see Gap found |
| scratch harnesses x4 (mocked OpenAI client/table) | c1-c4 | PASS 0 failures | no vendor call from this box |
| comp-find --corpus aws | live sha before build | PASS | L3 live sha == 09-11 deploy record |

**What worked:** every gate that refused was right -- the parity gate caught an undeclared
file, the owned-paths lane caught a DS seat writing the AE deploy record (resolved by the
audited override the law names, not `--force`), and reading artifacts back (head-object,
get-function-configuration, the served JSON) rather than trusting tool prose caught two
silent non-commits my own `sed` filters had hidden.

**What failed:** my output filters twice hid a refusal (`safe-commit` on the map, the
record script's `Unknown argument`) and I read "no output" as success until `git log`
said otherwise -- the repository answers, the tool describes itself.

**Gap found:** three, all real. (1) `record-terraform-deploy.sh:511` ran `$SCOPE_PY`
unquoted; on site Z python's path carries a space, so bash executed `/c/Users/Opal`
("Is a directory") -- quoted, committed `7c640c8a5f`. (2) `record-deploy-scope.py`
serialises `lambda-source-map.json` with raw non-ASCII (51 bytes incl. `0x9d`) while the
record script reads it in default cp1252 -- the generator re-introduces the byte its own
consumer cannot read; I re-ASCII'd the file before committing but the generator is
unfixed (surfaced, not chased). (3) `--function` takes ONE string; space-separated
word-splits inside unquoted `$SCOPE_ARGS`, comma-separated works -- the help says
"comma/space" and only comma is true through the shell wrapper.

---

## Work Completed

### 1. Four commits (each harnessed against a mocked client; details in the commit bodies)

| Commit | Change | Replaces |
|---|---|---|
| `29892baeaa` | ISO publish dates at ingest (`published_raw` kept); `_parse_published` accepts RFC-822; decay WARNs on fallback; quality score removed from L2 + L3; samples newest-first | deep-dive F1, F6 |
| `a0f555d501` | FinBERT gap-fill on gpt-4o-mini, once per article, written back as `sentiment_gpt*`; effective = finbert non-zero else gpt non-zero else None; `sentiment_source` everywhere; `GPT_GAPFILL_*` flags | F2 (Andrew's way) |
| `29d74204ba` | cluster direction judge at L2 (`judge_cluster_directions`); override = sign(judge) x abs(mean) via `effective_sentiment`; not_market dropped; mixed excluded from L3 pools; `ed1a036b2b` regex removed; `DIRECTION_JUDGE_*` flags | F3, F4, F10 |
| `c3804b3db5` | KIG card keyed to `inputs_fingerprint` (URL set + bucket); parsed-time article sort; `KIG_REFRESH_ON_CHANGE` | F5, F6 |

### 2. Deploy (ledger `news-scanner-semantics-20260916`, opened `1eb2bc2f7a` before the first act)

- L1 git: the four commits, LOCAL (origin/SITEZ `a8f204882b`; push integrator-only).
- L2 artifacts: four zips read back by `head-object`: ingestion `P.fxqND_...` sha `pfv7ue...`;
  trending `QorjHRzb...` `JmNhOC...`; layer3 `BtRIB.u3...` `CMPXj3...`; kig `LDH.xTpE...`
  `0+XaAe...`. Pre-act versions recorded in the ledger for rollback.
- L3 apply: baseline plan "No changes"; saved plan 0 add / 4 change / 0 destroy; `safe-apply`
  -> "Apply complete! Resources: 0 added, 4 changed, 0 destroyed."
- L4 verify: `get-function-configuration CodeSha256` == artifact sha on 4 of 4, all Active /
  Successful at 04:00:49Z; unscoped re-plan "No changes".
- Record: `7c640c8a5f` (`last_deployed_commit` per function = last commit touching its
  source_dir; `deploy_ledger` linked).

### 3. Exercise (L5) -- ad-hoc invoke 04:03:46Z, complete ~04:08Z, chain complete 04:12:55Z

| Measurement | Before (deep dive) | After |
|---|---|---|
| clusters at `avg_time_decay == 0.500` | 18 of 100 | **0 of 90** |
| voters/members median | 0.40 | **0.67** |
| clusters with <50% members voting | 53 of 100 | 28 of 90 |
| gap-fill | -- | 1500 scored (744 non-zero, 756 neutral), 60 calls, 0 errors, 1750 deferred |
| judge | -- | 100 judged: 12 bull / 33 bear / 19 mixed / **36 not_market dropped**, 2 overrides |
| cloud fields | none | 43/43 carry `sentiment_raw`, `voters`, `direction_judged`; 1 override |
| Layer 3 rows 2026-09-16 | -- | 20 at 04:11-04:12Z; 5 MIXED clusters kept out of both pools |
| KIG rows 2026-09-16 | -- | 20/20 with `inputs_fingerprint` + `cloud_generated_at` |

The flip Andrew asked for, end to end: cluster `mortgage rates rise` FinBERT mean **+0.652**
-> judge **bearish** ("higher borrowing costs") -> served cloud **-0.652** -> Layer 3
**bearish-10 "30-Year Mortgage Rate Jumps to 7.17%"** with the raw +0.652 preserved on the row.
`BOJ Rate-Hike Plans Stir Yield Fears` bearish-7. Every energy/yield keyword in the cloud is
bearish or mixed with a stated mechanism.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Execute the deploy from the DS seat | Andrew-direct "do it"; the infra lane is normally AE -- stated in the ledger title and the override commit |
| Audited `GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL` for the source-map commit | CLAUDE.md 14a: the lane escape is the override, never `--force`; singular, one lane, two files |
| Register `render_check.py` in files[] rather than `BAU_PARITY_SKIP=1` | the parity gate's own instruction; the file is committed and not imported by the handler |
| Ad-hoc invoke as L5 rather than waiting for 11:15Z | CLAUDE.md: waiting for the schedule is the coast-failure; the ad-hoc run is the same producer on the same path, blast radius stated in the ledger |
| Re-ASCII the source map by hand, leave the generator | the deploy record needed a readable file now; the generator defect is surfaced in Gap found for the hygiene pass, not chased mid-deploy |

---

## Files Modified

See commit messages: `29892baeaa`, `a0f555d501`, `29d74204ba`, `c3804b3db5`, `a9abfb490d`
(deep-dive Section 6), `1eb2bc2f7a` (ledger open), `7c640c8a5f` (record + script fix),
plus the ledger close commit that follows this log.

---

## Briefs Written

None -- Andrew directed the design in conversation; the four commit bodies and the ledger
carry the rationale and evidence for any successor.

---

## Blockers

None. Push to origin is integrator-only on site Z (`0.0.0_AB_MSTR~Z` holds a site-Z push
question at Andrew); every commit here is LOCAL on SITEZ.

---

## Current State

`news-ingestion-scheduler`, `news-trending-analysis`, `opal-news-layer3-curation` and
`keyword-intelligence-generator` are live on the bytes of SITEZ `c3804b3db5` (artifact shas
above; `lambda-source-map.json` records per-function `last_deployed_commit`). The 11:15Z
and 21:15Z trending runs will each gap-fill up to 1500 more of the 1750 deferred articles
(then ~500-600 new per day), judge ~100 clusters at ~10 gpt-4o-mini calls, and chain Layer 3
+ KIG as before. Flags to revert any piece without a redeploy: `GPT_GAPFILL_ENABLED`,
`DIRECTION_JUDGE_ENABLED`, `KIG_REFRESH_ON_CHANGE` (all default true, on
news-trending-analysis / keyword-intelligence-generator env). Cost review = grep CloudWatch
for `OPENAI_USAGE ... purpose=gapfill|direction_judge` and the one-line `GAPFILL:` /
`JUDGE:` summaries per run. Ledger `news-scanner-semantics-20260916` CLOSED. Not done, by
Andrew's ruling: neutral stays out of the denominator (4.3 rejected). Open hygiene from the
deep dive (4.5): Yahoo Finance ingested then blocked; dead L3 idempotency scan; vestigial row
fields; stale `TOP_20_KEYWORDS`; `dynamic_stopwords.json` frozen since April; the semantic
Lambdas; and the source-map serializer defect above.

---

## Next Steps

1. **[Andrew] Read the cost after 2-3 days** -- `OPENAI_USAGE purpose=gapfill` (~25-60
   calls/run) and `purpose=direction_judge` (~10/run) on gpt-4o-mini; flip the flag if it
   is not worth it.
2. **[0.1.0_DS_MarketIntelligence] Read the 11:15Z run** -- expect `GAPFILL deferred` to
   fall to ~250, then 0 by 21:15Z; expect `JUDGE not_market_dropped` in the 20-40 range
   and the cloud to hold fewer sports/entertainment words.
3. **[0.1.0_DS_MarketIntelligence] Hygiene pass (deep dive 4.5)** on Andrew's word, one
   commit per item; first the `record-deploy-scope.py` serializer (`ensure_ascii=True`) so
   the next recorder does not re-mint the `0x9d` byte.
4. **[0.0.0_AB_MSTR~Z] Carry the SITEZ commits** `29892baeaa`..`7c640c8a5f` + ledger close
   when the site-Z push question clears.
