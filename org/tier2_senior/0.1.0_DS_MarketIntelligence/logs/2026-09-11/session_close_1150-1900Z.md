# Trending Topics false-headline: found, measured, fixed at source, deployed -- 0.1.0_DS_MarketIntelligence

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, IMPLEMENT, DEPLOY, VALIDATE

**Date:** 2026-09-11
**Task Order:** ad-hoc, Andrew-direct at this terminal (no TO; no registered project code -- the news-pipeline Lambda `opal-news-layer3-curation`)
**Status:** COMPLETE -- code LIVE and verified end to end; THREE deploy ledgers CLOSED 5 of 5 (the third, `news-layer3-backfill-headline`, fixes the pre-existing backfill defect on Andrew's word after the first close); the 21:15Z scheduled fire is the acceptance read
**Workspace CLOUD commits:** `bc7514c173` -> `76dcff5718` -> `494b80e867` -> `b98f9a493a` (merge) -> `d8bb3ce2d5` -> `3e83049fe0` (SUPERSEDED, broken) -> `aa484f6b62` -> `06b6cef383` (LIVE)

---

## Objective

Andrew reported the Market Overview "Trending Topics" panel serving "China Oil Demand Growth
Anticipated" as bullish-2 while both articles beneath it said China's oil demand was FALLING 8.9%.
Find the story, find the AI responsible, restructure its prompt so a contemplated headline is
tested against its sources rather than asserted from a clustering artefact, raise the model, and
deploy -- all Andrew-direct this session.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `comp-find "opal-news-trending-daily" --files \| head` | FAIL | rail-gated on the `\| head` receiver (correct); re-run without a pipe timed out at 120s and went to background -- Glob answered first |
| comp-find | `comp-find "build_curation_prompt" --limit 20` | FAIL | 120s timeout, backgrounded; Glob `**/*layer3*curation*/**` resolved the 3 candidate sources in seconds |
| comp-iam | `comp-iam service opal-news-ai-sentiment` | PARTIAL | resolved the source path (`tools/news_scanner/lambda/layer2_finbert_scoring/`) but is the Terraform/DESIRED plane and says so -- cannot enumerate live invokers; `lambda get-policy` (audited `# rail-checked`) + CloudWatch last-event was the instrument |
| commit-gate.sh | `.tools/commit-gate.sh <lambda>` | PASS | CAUGHT A REAL BUG py_compile could not: an undefined name after a variable rebind (`sample_articles` -> `all_samples`). Then correctly blocked on 25 PRE-EXISTING ruff errors (25 at HEAD, 25 on my change, delta 0) |
| deploy_ledger.py | `open / close-leg x5 / close` x2 ledgers | PASS | contract tool for the NEVER-half-landed law; both entries opened BEFORE the act, sentinel committed first |
| safe-apply.sh | 4 applies on `infra/aws/terraform/news-pipeline` | PASS | halt-gate needed the session `.serial` file (fail-closed on a bad one -- caught my own `printf %s\\n` escaping slip that appended an `n`); comp-tagauthz gate broke ONLY when I wrongly set `MSYS_NO_PATHCONV=1` (CLAUDE.md says never for safe-apply -- my error) |
| safe-merge.sh | `safe-merge.sh ds-mi-layer3-flagnotdrop` | PASS | drained the isolated worktree back; author resolved as `0.1.0_DS_MarketPerformance` (launch-prompt typo serial) -- cosmetic, underlying commits correct |
| render_check.py (mine, scratchpad) | build the curation prompt from the REAL L2 report and measure | PASS | THE CHECK THAT WOULD HAVE CAUGHT 3e83049fe0: 98,405 chars / 65 of 65 SORT EVIDENCE lines / 237 CARRIES tags. Belongs beside the Lambda -- not yet committed |
| .tools/aws (shim) | 14x `dynamodb query --output json > file` | FAIL then PASS | TRUNCATED two files mid-value on `‐` / `₹` via the cp1252 console, rc=0; fixed with `PYTHONIOENCODING=utf-8`; strict-parse validation added. Memory written |
| .tools/aws (shim) | `s3 cp s3://... /cygdrive/c/.../x.json` | FAIL | destination mangled to `..\..\..\..\cygdrive\c\...`, reported success, file not where named. Relative `.runtmp/` path worked |

Role minimum (DS: `comp-pipescript io` per gold script touched): SKIPPED with reason -- no gold script
was touched; the surface is a Lambda under `infra/aws/lambda/`, outside comp-pipescript's domain.

**What worked:** commit-gate (a real catch), deploy_ledger (kept 4 applies honest across a rollback),
safe-apply's halt-gate (fail-closed on my own corrupted serial file), Glob for source discovery.
**What failed:** comp-find on this corpus (timeouts); the aws shim's console encoding (silent
truncation, silent mis-path); my own span-bounded prompt edit (see Postmortem).
**Gap found:** no estate tool renders a Lambda's prompt from real input and measures it before
deploy. That is exactly the check that caught today's regression, and it lives only in my scratchpad.

---

## Work Completed

### 1. The story, and the fault, from the served record (not the README)
DynamoDB `opal-news-trending-daily`, `date=2026-09-11`, `topic_rank=bullish-2`:
headline "China Oil Demand Growth Anticipated"; rationale "Sinopec forecasts rising future demand";
subtext "China's oil consumption on the rise". top_articles: two Sinopec pieces at FinBERT -0.974 /
-0.975 titled "Sinopec Sees China Oil Demand Falling 8.9% in 2026", plus OPEC global demand
(+0.874), US natgas (+0.947), EIA US output (+0.950). Mean = +0.16438 -> stored `sentiment.finbert`
0.1644 -> BULLISH pool. The rationale attributes to Sinopec the inverse of what Sinopec said; the
sentence is in no article.

### 2. The chain, grounded on the live plane (the two READMEs describe a table and a lambda tree that do not exist)
- Writer identified by CONTENT, not filename: `infra/aws/lambda/news_layer3_curation/lambda_function.py`
  matched the deployed zip byte-for-byte (118,238 bytes, LF-normalised sha 48d055f79764afae). Two
  Lambdas write the table; `news-trending-analysis` owns none of the row's fields.
- Chronology, measured from CloudWatch: EventBridge `news-trending-analysis-daily` cron(15 11,21 UTC)
  -> `news-trending-analysis` (L2: text-embedding-3-small 256d + gpt-4o-mini cluster LABELLER) ->
  async `lambda.invoke` at `:1621` -> `opal-news-layer3-curation` (L3) 35s later; its own rule
  `layer3-gpt-curation-daily` is DISABLED by design. Row `created_at` 11:17:08Z == L3 log event.
- `opal-news-ai-sentiment` (ProsusAI/finbert) LIVE daily 14:10Z, invoked directly by the ingestion
  role (no rule, no resource policy). `news-semantic-clustering` DEAD since 2026-02-24 (199 days),
  no consumer; L3's `cluster_similarities` come from L2's own report (`:2738`).
- All `trending-topics-portal-publisher-*` rules DISABLED; the portal reads the table via
  `opal-portal-data-proxy` (`portal/src/api/endpoints/trending.ts` -> `portal-proxy.ts`).

### 3. Three compounding defects
(a) direction = sign of an UNWEIGHTED MEAN FinBERT over every keyword-matched article
(`prefilter_topics_by_finbert :656`), blind to on-topic-ness; (b) `build_curation_prompt` allowed
rejection only for sports/entertainment/crypto/stock-picks and forbade reordering; (c)
`generate_single_topic_analysis` asserted direction AND headline as PREMISES with no dissent field,
on gpt-4o-mini at temperature 0.7. The estate had already diagnosed this shape for earnings
transcripts (`_validate_outcome_assertions`) and scoped the cure one cluster-type too narrowly.

### 4. Iteration 1 -- DIRECTION-CONSISTENCY GATE (`bc7514c173`)
On-topic token matching + deterministic drop + prompt gate + `direction_check` field + analysis
prompt reframed as a claim under test. Exercised on 19 real rows, then WIDENED TO 14 DAYS / 279 ROWS
(Option 1 of /next-steps): at strict-majority 5 flagged, hand-adjudicated ONE true inversion; every
false positive had support=1, the true catch support=0 -> unanimity rule -> 1 of 279, zero false
positives. Two over-fires closed on the way ("oil prices rise": a DIRECTION word was selecting the
EVIDENCE, 1 of 50 matched; "copper tariffs": a genuine 4-4 split -> MIXED, not dropped).

### 5. Models (Andrew: "4o mini is much too small, i would recommend 5.6-sol")
`gpt-5.6-sol` taken from the estate, not recall: ruled by Andrew 2026-09-10 ~22:1xZ, in service at
`daily_sprint_generator/lambda_function.py:66`. Its reference call (`:253-257`) sends ONLY
model/messages/response_format -- so `_accepts_sampling_controls()` attaches temperature / token
caps BY FAMILY; a naive swap would have 400'd nightly. `ANALYSIS_GPT_MODEL` env (was hardcoded
gpt-4o-mini at the call site). /open-calls CALL 1 approved: `GPT_MODEL` (step 5, the headline
writer) also -> gpt-5.6-sol, which REQUIRED a terraform env change (`76dcff5718`) because the env
var beats the code default. CALL 2 approved: run the analyzer on every topic, not tiered.

### 6. Deploy 1 + smoke test 1 -> found the model's self-verdict noisy and the drop path harmful
Ledger `20260911T1712Z_news-layer3-direction-gate`, 5 legs CLOSED. Live rehearsal on throwaway
`date=2099-01-01`: the model flagged six topics, several citing an article that SUPPORTED the
headline; each DROP was refilled by `backfill_from_layer2` from a RAW ARTICLE TITLE (no 45-char
rule, no relevance filter) -- an advice column reached a bearish slot. Fix `494b80e867`: model flag
only, deterministic gate the sole dropper. Rehearsal 2 (`2099-01-02`): gate fired once (china,
support=0), backfills 6 -> 1. For the same cluster gpt-5.6-sol wrote "Sinopec Sees China Oil Demand
Falling" -- the true direction -- where 4o-mini had written the inversion. Root cause fixed at source.

### 7. Andrew's model (the actual remediation): THE SORT IS GIVEN
Andrew: the sort is a majority verdict; the writer must find the narrative IN the cluster that
CARRIES it; minority views are counterpoint. PREMISE TESTED on 279 rows before implementing: carrying
articles are the strict majority 271 (97.1%), tied 8 (2.9%, all exact ties), ZERO carrying 0 --
writable 279 of 279. THE RECONCILIATION: my gate judged the sort on the LABEL-matched subset (2
Sinopec pieces -> support 0 -> drop); the sort was computed over the WHOLE cluster (3 carrying).
The on-topic filter is label-fidelity metadata, not a basis for judging the sort -- I had applied it
at the wrong stage. Implemented: `_carrying_articles()` (whole-cluster split), `_direction_evidence()`
now CONSISTENT | MINORITY_SUPPORT | EVENLY_SPLIT | NO_SUPPORTING_NARRATIVE (only the last drops; 0 of
279), `format_topic` tags CARRIES THE SORT / COUNTERPOINT, both prompts reframed, and the model
CITES `topline_source` (verified by `_verify_topline_source`) instead of judging its own work.

### 8. Deploy 2 -> REGRESSION -> rollback -> corrected deploy 3 (see Postmortem)
`3e83049fe0` deployed (sha `slOjgb...`); rehearsal `2099-01-04`... no: `2099-01-03` read
"Expected 10 bullish + 10 bearish, got 0 + 0", curation prompt 2,715 tokens. ROLLED BACK to
`494b80e867` (sha `HXl8Hh...`) within minutes. Cause found by two instruments; corrected as
`06b6cef383` (sha `DA8R9OMHOhYTxI9Nc76SH1lcNsNoPTylQYSLv2RkPms=`), render-checked BEFORE deploy,
deployed, triple equality 3 of 3, rehearsal fired 18:56:25Z to `2099-01-04`. At log time the
rehearsal's curation call read prompt=29,540 tokens, 10 bullish + 10 bearish selected; per-topic
analysis calls in flight.

### 9. Findings recorded, not fixed (all pre-existing)
- `backfill_from_layer2` emits raw article titles as headlines (unbounded, unfiltered); reachable
  whenever the selected set is short. MEASURED TRIGGER (rehearsal 4): `detect_and_merge_duplicates`
  collapses topics sharing an `original_keyword` bucket ('ai', 'tech', 'war') across the WHOLE pool
  (bullish 10->7, bearish 10->6 = 7 merges = 7 raw titles), while the curation prompt's
  ANTI-CONCENTRATION rule constrains only the TOP 3 -- the two disagree on scope, so the model
  legitimately selects what the merge then removes. Every merge costs a raw-title row. Fix belongs
  together: either widen the prompt rule to one-per-bucket pool-wide, or make backfill write
  through the same headline/relevance path as selection.
- Upstream (Option 4, measured not started): a label describes UNDER HALF its cluster in 123/279
  (44.1%; the 15.8% zero bucket is inflated by exact-token matching, 44.1% is the honest figure);
  40.9% of clusters contain articles that disagree. Lives in `news-trending-analysis` (step 2
  embeddings are sentiment-blind; step 3 labeller sees titles only).
- `news-semantic-clustering` orphaned 199 days.
- Two aws-shim traps (truncation on console encoding; s3 cp cygdrive dest mangled).

---

## Postmortem

**Root cause of the `3e83049fe0` regression:** the curation-prompt edit was a text span from the gate
heading to the `LAYER2_KEYWORD` heading. Those two headings live in DIFFERENT `"""` literals; between
them sits the Python that renders the candidate pools (`bullish_pool = ...`, the `format_topic` loops,
the similarity table). The span deleted it.

| Check | Read on the broken build | Why it did not catch it |
|---|---|---|
| py_compile | PASS | the file is valid Python with the pools missing |
| ds-precommit-check / ruff | PASS | no undefined names, no lint delta |
| triple equality | 3 of 3 | proves the bytes shipped, says nothing about behaviour |
| terraform 0-diff | No changes | infra matched the (wrong) code |
| live rehearsal on a throwaway date | `got 0 + 0`, prompt=2,715 tokens | THE ONLY CHECK THAT CAUGHT IT |

**Resolution:** span re-bounded at the closing quote of the SAME literal, with a guard that refuses
unless the pool code is the next thing after it; `render_check.py` built and run BEFORE deploy
(98,405 chars, 65/65 topics, 237 CARRIES tags); rehearsal 4 confirms 29,540 prompt tokens, 10+10.
The scheduled 21:15Z run was never exposed. Memory written:
`feedback_render_the_prompt_from_real_input_and_measure_it_before_deploying_any_prompt_edit.md`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Rehearse every deploy on a throwaway partition (`2099-01-NN`, `force_refresh`) | `clear_existing_topics` runs BEFORE the GPT call; a failed live-date run empties the served panel until the next scheduled fire. Cost: ~20 OpenAI calls. It caught two regressions today |
| The deterministic gate DROPS; the model's self-verdict only FLAGS (iteration 2) | measured on the deployed function: model flags cited SUPPORTING articles as contradictions; each drop backfills a raw title |
| Adopt Andrew's write-from-the-sort model; retire the on-topic filter as a JUDGE, keep it as METADATA | premise holds 279/279 writable; my filter judged the sort on a narrower set than the sort was computed on |
| Ask the model to CITE (`topline_source`), not to JUDGE (`direction_check`) | a citation is verifiable against the cluster; a verdict is not, and was measured noisy |
| DROP only on NO_SUPPORTING_NARRATIVE | 0 of 279 in 14 days -- a tripwire, and no drops means no raw-title backfill |
| Roll back FIRST, diagnose second, on `got 0 + 0` | 21:15Z scheduled run was ~2h out; the proven build was one upload away |
| Audited lane override on the terraform commit only | `infra/aws/terraform` is AE lane; the env change was REQUIRED for the approved model raise; authority Andrew-direct "just commit/deploy" -- flagged, not buried |
| Did NOT override the integrator-only push | a push republishes every other seat's local commits |
| Cleared 25 pre-existing ruff errors in the Lambda | Andrew's word "commit/deploy" after I had declined to touch them unasked; all pre-existing, 20 autofixed, 5 by hand, behaviour-neutral |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | see commit messages: `bc7514c173`, `494b80e867`, `3e83049fe0` (superseded), `06b6cef383` | Yes -- `06b6cef383` LIVE |
| `infra/aws/terraform/news-pipeline/lambdas.tf` | `GPT_MODEL` gpt-4o -> gpt-5.6-sol; `ANALYSIS_GPT_MODEL` added; comment block | Yes -- `76dcff5718` (audited lane override) |
| `org/critical_paths/change_management/20260911T1712Z_news-layer3-direction-gate_deploy_completion.md` | ledger 1, 5 legs CLOSED | Yes -- `76dcff5718` open, `d8bb3ce2d5` close |
| `org/critical_paths/change_management/20260911T1839Z_news-layer3-topline-narrative_deploy_completion.md` + `.open_deploys/news-layer3-topline-narrative.json` | ledger 2, L1-L4 closed, L5 OPEN | Yes -- `aa484f6b62` (sentinel) |
| `org/mcp/sessions/fa918d94-c564-4e52-856e-390211e52bb2.serial` | session serial for the halt-gate | No -- local, session-scoped |
| `.runtmp/l2_latest.json` | Layer 2 report snapshot (07:16Z) for the render check | No -- runtime scratch |
| scratchpad: `render_check.py`, `widen_evidence.py`, `premise_test.py`, `upstream_diagnosis.py`, `exercise_gate.py` | the instruments behind every number in this log | No -- session scratchpad, will not survive |
| memory: `reference_the_aws_shim_truncates_its_json_output_midwrite_...md`, `feedback_render_the_prompt_from_real_input_and_measure_it_...md` + MEMORY.md index lines | two instrument traps | agent memory dir (not the repo) |

---

## Blockers

None BLOCKED. Two lanes, not blockers: (1) push to origin is integrator-only -- `0.0.0_AB_MSTR` has
already carried everything through `aa484f6b62`; only `06b6cef383` is local at log time (ls-remote
read 18:59Z). (2) Ledger L5 awaits a row-read of the in-flight rehearsal; the deploy itself is fully
landed (triple equality 3 of 3), so this is not a half-landed deploy -- it is a proof leg, 0.4h into
a 4h window.

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| none -- the durable artefacts are the two memories and `render_check.py` (scratchpad, uncommitted) | -- | -- |

---

## Current State

`opal-news-layer3-curation` is LIVE on `d6913f1e9b` (CodeSha256 `bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=`,
S3 version `a3tIkpIz9gUHzIo5KeGiwjWYY_T9oPCG`, applied ~19:31Z; supersedes `06b6cef383` / `DA8R9O..`),
env `GPT_MODEL` and `ANALYSIS_GPT_MODEL` both `gpt-5.6-sol`, terraform 0-diff. `d6913f1e9b` adds the
BACKFILL FIX (Andrew-direct "just fix the pre-existing defect"): backfilled topics get a GPT-written
<=45-char headline from their lead CARRYING article plus the selection pass's relevance rejections,
on the per-topic call backfill already made; a mechanical 45-char cap backstops it. Rehearsal 6
(`2099-01-06`) proved it: same merge (10->7 / 10->8), 5 backfills, ALL with real headlines (max 42
chars) where rehearsal 4's were 78-char raw titles; 0 drops, 0 citation warnings, 0 tracebacks.
Deploying it took two attempts -- the first re-applied the previous bytes because a grep guard let
the chain run past a failed sentinel commit and the build used HEAD~1; caught by comparing HEAD's blob
sha to the live CodeSha256, redone with a hash-pinned build asserted against an independently computed
expected sha (memory written). Ledger `news-layer3-backfill-headline` CLOSED 5 of 5. It implements Andrew's write-from-the-sort
model: the direction is given, the headline is built from an article tagged CARRIES THE SORT and cited
in `topline_source`, counterpoint goes in the body, and only NO_SUPPORTING_NARRATIVE (0 of 279 in 14
days) can drop a topic. Rehearsal 4 on throwaway `date=2099-01-04` (log stream
`2026/09/11/[$LATEST]27909bf18dc5490aa2e90925090e9ac1`) is COMPLETE and proves it: curation prompt
29,540 tokens, 10+10 selected, 0 drops, 0 citation warnings, 0 tracebacks, 312s, and the china
cluster serves bullish-3 "OPEC Sees Oil Demand Growth Explode in 2027" -- the true bullish topline,
Sinopec as counterpoint. Both ledgers CLOSED (5 of 5 legs each); all four `2099-01-0N` test
partitions deleted (0 rows remain). The live `2026-09-11` partition (19 rows, still carrying the
pre-fix bullish-2) is untouched; the scheduled 21:15Z fire of `news-trending-analysis-daily`
(ENABLED) is the acceptance and regenerates it on the live code. ONE CAVEAT, pre-existing and not
from this change: 7 of the rehearsal's 20 rows are raw article titles because
`detect_and_merge_duplicates` collapses topics sharing an `original_keyword` bucket (bullish 10->7,
bearish 10->6) and `backfill_from_layer2` refills with raw titles; the prompt's anti-concentration
rule guards only the top 3 while the merge sweeps the whole pool. Proven rollback if ever needed:
upload the zip rebuilt from `494b80e867` (sha `HXl8HhPKq7CXFNX8KUkdfreYpj5quXBrg31cLMaoR7I=`) and
`safe-apply` -- done once today in under 3 min.

---

## Next Steps

1. **[0.1.0_DS_MarketIntelligence] Read the 21:15Z scheduled run** -- the acceptance. Confirm
   `2026-09-11` regenerates with a true headline in the china slot, 20 well-formed rows, no advice
   columns; read `OPENAI_USAGE prompt=` on the curation call (~26-30k).
3. **[0.1.0_DS_MarketIntelligence] Commit `render_check.py` beside the Lambda** -- the check that
   caught today's regression must not live only in a scratchpad.
4. **[0.0.0_AB_MSTR] Publish `06b6cef383`** -- integrator-only push; everything earlier is already on origin.
5. **[0.1.0_DS_MarketIntelligence] Persist backfill provenance to the row** -- the wrapped topic's
   `backfilled=True` and `topline_source_check` are not written to DynamoDB (the enrich step builds
   the row from a fixed key set), so the LOG, not the row, is the evidence of which slots were
   backfilled. Small follow-up; the backfill defect itself is FIXED (`d6913f1e9b`, see Current State).
   Also unexercised live so far: `BLOCKED: RELEVANCE` and `HEADLINE_CAPPED` -- proven by the rendered
   prompt and offline tests, watch for their first live firing.
6. **[Andrew's call] Upstream fix in `news-trending-analysis`** -- label fidelity 44.1% under-half,
   40.9% self-contradicting clusters; multi-session, different Lambda, measured not started.
7. **[0.1.0_DS_MarketIntelligence] Watch one week** -- the `MINORITY_SUPPORT` / `EVENLY_SPLIT` / `TOPLINE_SOURCE`
   log lines are the new signal; decide on tiering the analyzer only on that evidence (CALL 2 rec).
