# Backfill defect fixed and deployed -- raw-title slots now get real headlines -- 0.1.0_DS_MarketIntelligence

**archetype:** IMPLEMENT
**secondary_archetypes:** DEPLOY, DIAGNOSE

**Date:** 2026-09-11
**Task Order:** ad-hoc, Andrew-direct at this terminal ("just fix the pre-existing defect, we have time it looks like"); delta on the session-close log `session_close_1150-1900Z.md`
**Status:** COMPLETE -- live, rehearsed, ledger CLOSED 5 of 5
**Workspace CLOUD commits:** `d6913f1e9b` (the fix) -> `3b091aaf3c` (ledger OPEN sentinel) -> `b762afef56` (ledger CLOSE + amended close log)

---

## Objective

Fix the pre-existing defect surfaced by the morning's work: when `detect_and_merge_duplicates`
collapses topics sharing an `original_keyword` bucket, `backfill_from_layer2` refills the slots
with RAW ARTICLE TITLES -- 78-char strings on a 45-char panel, with only the mechanical
sports/crypto/source gates applied and never the selection pass's judgement rejections (an
advice column had reached a bearish slot this way). Fix it minimally, rehearse it on a throwaway
partition, deploy it before the 21:15Z scheduled fire.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| render_check.py (mine, scratchpad) | build the curation prompt from the REAL L2 report, measure | PASS | regression guard on the untouched selection prompt: 98,405 chars, 65 of 65 SORT EVIDENCE lines -- the check that caught the morning's regression, now standing |
| offline exercise (mine, inline) | `backfill_from_layer2(needed=3, gpt_client=None)` + `_cap_headline` cases + rendered `write_headline=True` prompt | PASS | 3 returned, all <=45; the two 78-char offenders cap to 43/44; duty block + both fields + rules 8-9 present, JSON balanced; the `write_headline=False` prompt byte-unchanged |
| commit-gate.sh | `.tools/commit-gate.sh <lambda>` | PASS | clean (19 pre-existing non-ASCII WARNs, none mine) |
| deploy_ledger.py | `open` / `close-leg` x5 / `close` | PASS | third ledger of the day; L1's proof carries the two-attempt deploy honestly |
| safe-apply.sh | 2 applies on `infra/aws/terraform/news-pipeline` | PASS (tool) / FAIL (my chain, 1st) | the tool did exactly what it was told both times; the FIRST time it was told to ship the previous bytes -- see Postmortem |
| git show `<pinned-hash>:<path>` | build input for the zip | PASS | replaced `HEAD~1` after the first attempt built the wrong commit |
| .tools/aws (shim) | s3api put/head-object, lambda get-function-configuration/invoke, logs get-log-events, dynamodb query/delete | PASS | with `PYTHONIOENCODING=utf-8` set throughout (the morning's truncation trap) |

Role minimum (DS: `comp-pipescript io` per gold script touched): SKIPPED with reason -- no gold
script touched; the surface is a Lambda under `infra/aws/lambda/`.

**What worked:** the offline exercise of the new path with `gpt_client=None` (it proved the loop,
the lead-carrying fallback and the cap without a vendor call); `deploy_ledger` forcing a proof per
leg, which is where the wrong-bytes deploy became visible; the repository-verified commit check.
**What failed:** my own deploy chain, once -- a `grep` guard that matched the failure line let it
run past a failed commit, and a `HEAD~1` build ref shipped the previous commit's bytes.
**Gap found:** the estate has no tool that asserts "the artefact I am about to upload was built
from THIS hash and hashes to THIS expected value" -- I did it by hand in the chain; it belongs in
a build-and-upload helper for this Lambda.

---

## Work Completed

### 1. The fix (`d6913f1e9b`, +~120/-40 in `infra/aws/lambda/news_layer3_curation/lambda_function.py`)
- `generate_single_topic_analysis(..., write_headline=False)`: opt-in duty. When True the prompt
  adds a BACKFILL block, two JSON fields (`"headline"` <=45 chars from a CARRYING article;
  `"financially_relevant"`) and rules 8-9 naming the SAME rejection classes the selection pass
  applies (sports, entertainment, local crime, advice columns, stock picks). `financially_relevant`
  defaults True on any parse hiccup or failed call, so nothing is rejected by accident; only an
  explicit false removes a candidate. Both selection-path call sites unchanged (verified: the
  rendered `write_headline=False` prompt carries no backfill duty).
- `backfill_from_layer2`: walks candidates in trend order until `needed` are ACCEPTED (a relevance
  false skips to the next), attempts bounded at `max(4*needed, 8)`; the raw-title fallback is now
  the lead CARRYING article via `_carrying_articles` (the old sort keyed on `quality_score`, a field
  Layer 2 articles do not carry -- it was a no-op picking whichever came first); GPT headline if
  written, else the fallback; `_cap_headline` (word-boundary cut at `HEADLINE_MAX_CHARS = 45`)
  either way; `BACKFILL_SHORT` warned if the target is not reached.
- Deliberately NOT changed: `detect_and_merge_duplicates` (changing it changes which topics
  appear); the prompt's top-3 anti-concentration rule (16 keyword buckets only -- one-per-bucket
  pool-wide would starve a 10-slot pool).

### 2. Verified offline BEFORE deploy (real L2 report at `.runtmp/l2_latest.json`)
render check PASS; `_cap_headline` on the two 78-char offenders -> 43/44; `backfill_from_layer2`
with no client returns 3 capped headlines from lead carrying titles; the backfill prompt renders
with the duty and balanced JSON; the selection prompt is byte-unchanged; commit-gate clean.

### 3. Deploy -- two attempts (see Postmortem); the second is the real one
Ledger `20260911T1925Z_news-layer3-backfill-headline`: L1 `d6913f1e9b` + sentinel `3b091aaf3c`;
L2 S3 version `a3tIkpIz9gUHzIo5KeGiwjWYY_T9oPCG`, content-sha256
`bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=` built from `git show d6913f1e9b:<path>` and
asserted equal to an expected value computed in a separate step BEFORE upload; L3 apply
`0 added, 1 changed, 0 destroyed`, only `source_code_hash` (`DA8R9O..` -> `bWvoG+..`) and
`s3_object_version`; L4 triple equality against the EXPECTED constant; L5 rehearsal 6.

### 4. Rehearsal 6 (`2099-01-06`, live bytes)
Curation 29,540 prompt tokens, 10+10 selected; merge bullish 10->7 / bearish 10->8 (same
pre-existing step as rehearsal 4); 5 backfills, EVERY one a GPT-written headline:
`ecb interest rates` -> "European Banks Lift Lending Income Outlook" (42);
`iceland us relations` -> "EU Pledges Greenland Investment Boost" (37);
`currency trading warning` -> "Bessent Warns Traders Against Yen Bets" (38);
`trump voter payout` -> "Republicans Fear Trump Is Campaign Toxic" (40);
`market outlook` -> "Micron Left Behind as Peers Outperform" (38).
20 rows, 0 over 45, max 42; NO_SUPPORTING_NARRATIVE 0; TOPLINE_SOURCE warnings 0; tracebacks 0;
china slot `bullish-3` "OPEC Sees Oil Demand Growth Surge" still a true carrying topline.
HONEST LIMITS: `BLOCKED: RELEVANCE` fired 0 (no advice-column candidate this run) and
`HEADLINE_CAPPED` fired 0 (GPT wrote all five under 45) -- both proven by the rendered prompt and
the offline exercise, not by a live rejection yet. Rehearsal 5 (`2099-01-05`) ran on the OLD bytes
during the first attempt and is NOT evidence; its 20 rows were deleted unread.

### 5. Closeout
Ledger CLOSED 5 of 5; `2099-01-05` and `2099-01-06` deleted (0 rows remain); live `2026-09-11`
untouched at 19 rows; `news-trending-analysis-daily` ENABLED for 21:15Z; the session-close log
amended (Status, Current State, Next Step 5) and committed with the closure; two memories written
and indexed.

---

## Postmortem

**What broke:** my first deploy chain re-applied the PREVIOUS commit's bytes and every check read
green. Nothing wrong was ever served -- the previous build was the one already live -- but the fix
was committed and not deployed, and I would have read rehearsal 5 as proof of it.

| Cause | Mechanism |
|---|---|
| sentinel commit failed (rc=128) | its `-F` message file had been written by an inline `python -c` using a shell-interpolated `/cygdrive` path native Python cannot open -- exactly the case CLAUDE.md 14a's "non-shell writer" rule exists for |
| chain continued past the failure | the guard was `... \| grep -E "^\[CLOUD\|REFUSED\|ERROR" \| head -2 && next` -- grep matched the ERROR line, exited 0 |
| wrong bytes built | the build ref was `HEAD~1`, written assuming the sentinel would be HEAD; with it absent, and another seat's commit (`130599b2c5`) having landed between steps, `HEAD~1` was the previous lambda commit |
| triple equality passed anyway | local zip == S3 == live, all three the same wrong artefact -- DISCRIMINATION inside a wrong GRAIN (CLAUDE.md Rule 22) |

**Caught by:** hashing HEAD's blob (`bWvoG+..`, 144,267 bytes, contains `write_headline`) against
HEAD~1's (`DA8R9O..`, 140,690 bytes, does not) and the live CodeSha256.
**Resolution:** message file via the Write tool; commit verified by `git log -1 --format=%s`
(the repository answering, not the tool's prose); build from the PINNED hash; built sha asserted
against an independently computed EXPECTED value before upload; triple equality against that
constant. Recorded in the ledger's L1 and in memory
`feedback_never_guard_a_deploy_chain_with_a_grep_that_matches_the_failure_line_and_pin_the_build_ref_by_hash.md`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Put the headline + relevance duty on the per-topic call backfill already makes | zero extra requests; the call already sees the cluster's carrying/counterpoint split |
| `financially_relevant` defaults True; only an explicit false rejects | a parse hiccup or a failed call must never remove a topic; a skip is cheap (next candidate), a false drop is not |
| Bound backfill attempts at `max(4*needed, 8)` | a run of rejections must not become an unbounded OpenAI bill |
| Raw-title fallback = lead CARRYING article | the sort is given; the old `quality_score` sort was a no-op on Layer 2's article shape |
| Mechanical 45-char cap on the backfill path only | the selection prompt already carries the rule and its 13 headlines in rehearsal 4 were all <=45; widening the cap is a separate safe follow-up |
| Merge step and top-3 rule untouched | changing merge changes which topics appear; 16 buckets cannot support one-per-bucket across a 10-slot pool |
| Discard rehearsal 5 unread | it ran on the old bytes; reading it as evidence would have repeated the false-green |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/news_layer3_curation/lambda_function.py` | see commit message `d6913f1e9b` | Yes -- `d6913f1e9b`, LIVE |
| `org/critical_paths/change_management/20260911T1925Z_news-layer3-backfill-headline_deploy_completion.md` + `.open_deploys/news-layer3-backfill-headline.json` | third ledger, OPEN then CLOSED (sentinel removed) | Yes -- `3b091aaf3c` open, `b762afef56` close |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-09-11/session_close_1150-1900Z.md` | Status, Current State, Next Step 5 amended to the live state | Yes -- `b762afef56` |
| memory: `feedback_never_guard_a_deploy_chain_...md` + MEMORY.md index line | the chain-guard / pinned-ref lesson | agent memory dir |
| scratchpad: `patch_backfill.py`, `commitmsg9.txt`, `cm10.txt`, `cm11.txt` | the instruments | No -- session scratchpad |

---

## Blockers

None. Push to origin is integrator-only (`0.0.0_AB_MSTR`), not a blocker: 5 of this seat's
commits local at `b762afef56` vs origin `aa484f6b62` (ls-remote 19:44Z).

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| none -- the durable artefacts are the two memories, `render_check.py` (scratchpad, still uncommitted) and this log | -- | -- |

---

## Current State

The full handoff is the amended `session_close_1150-1900Z.md` Current State; this is the delta.
`opal-news-layer3-curation` is LIVE on `d6913f1e9b` (CodeSha256
`bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=`, S3 version `a3tIkpIz9gUHzIo5KeGiwjWYY_T9oPCG`,
applied ~19:31Z), env `GPT_MODEL` and `ANALYSIS_GPT_MODEL` both `gpt-5.6-sol`, terraform 0-diff.
Backfilled slots now carry GPT-written <=45-char headlines from their lead carrying article and
pass the selection pass's relevance rejections; the mechanical cap and the relevance reject are
proven offline and by the rendered prompt but have not yet fired live. All three of today's deploy
ledgers are CLOSED 5 of 5. All test partitions (`2099-01-01`..`06`) are deleted. The live
`2026-09-11` partition is untouched at 19 rows and still carries the pre-fix china row; the
scheduled 21:15Z fire of `news-trending-analysis-daily` (ENABLED) regenerates it on the finished
code and is the acceptance read. Proven rollback: rebuild from `494b80e867` (sha `HXl8Hh..`) and
`safe-apply` -- under 3 minutes, done once today.

---

## Next Steps

1. **[0.1.0_DS_MarketIntelligence] Read the 21:15Z scheduled run** -- the acceptance: `2026-09-11`
   regenerated, china slot a true carrying topline, 20 rows all <=45 chars, `OPENAI_USAGE prompt=`
   on the curation call ~26-30k, and note whether `BLOCKED: RELEVANCE` / `HEADLINE_CAPPED` fire
   for the first time.
2. **[0.1.0_DS_MarketIntelligence] Commit `render_check.py` beside the Lambda, and fold the
   pinned-hash build + expected-sha assertion into a build-and-upload helper** -- the two checks
   that caught today's two regressions live only in a scratchpad and a shell chain.
3. **[0.1.0_DS_MarketIntelligence] Persist backfill provenance** -- `backfilled=True` and
   `topline_source_check` are not written to the DynamoDB row; the log is the only evidence of
   which slots were backfilled.
4. **[0.0.0_AB_MSTR] Publish `d6913f1e9b`..`b762afef56`** -- integrator-only push.
5. **[Andrew's call] Upstream fix in `news-trending-analysis`** -- unchanged from the close log:
   label fidelity 44.1% under-half, 40.9% self-contradicting clusters; measured, not started.
