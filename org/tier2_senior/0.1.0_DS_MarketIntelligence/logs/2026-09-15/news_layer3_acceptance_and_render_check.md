# Trending Topics: acceptance read of the 2026-09-11 deploy PASSES; render_check.py landed; an advice-column gap in the SELECTION pass -- 0.1.0_DS_MarketIntelligence

**archetype:** VALIDATE
**secondary_archetypes:** IMPLEMENT

**Date:** 2026-09-15 (UTC; window ~02:15Z -> ~03:00Z, which is Andrew's 2026-09-14 evening ET)
**Task Order:** none -- this seat's own Next Steps 1 and 2 from `logs/2026-09-11/`; no dispatch, inbox empty, `to-check --all` 0 active of 2,668 faces scanned, `get_delivery_state` since 2026-09-11T19:00Z 0 rows
**Status:** COMPLETE -- acceptance PASS; `render_check.py` committed; one call surfaced to Andrew (not fixed: it moves served output)
**Workspace CLOUD commits:** `f23d4d3839` (render_check.py) + this log's commit. Push state: `f23d4d3839` LOCAL, origin CLOUD `6a5b276f8b` (ls-remote read 02:59Z; positive control `b762afef56` on origin)

---

## Objective

Close the acceptance read the 2026-09-11 session left open (the 21:15Z fire and every fire since, read
from the served table and the function's own logs), and land the prompt-render check that caught that
day's regression, which had lived only in a scratchpad that did not survive.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | PATH exercise "how do I grep the repo" | PASS | 104 of 104 comp-tools resolve bare; the forwarder RAN |
| audit-archive-invoker.py | startup A.2 | PASS | 0 findings; snapshot not due (baseline 10.3h < 12.0h) |
| to-check.py | `--all --assignee 0.1.0_DS_MarketIntelligence` | PASS | 0 active of 2,668 scanned |
| .tools/aws (shim) | `lambda get-function-configuration`, `events describe-rule`, `dynamodb query` x5, `logs filter-log-events` | PASS | `PYTHONIOENCODING=utf-8` throughout (the 2026-09-11 truncation trap); every output strict-parsed |
| render_check.py (new) | 4 arms, see Work Completed 3 | PASS | DISCRIMINATES: refuses the real broken build, passes its correction |
| commit-gate.sh | `render_check.py` | PASS | clean 1 of 1 |
| safe-commit.sh | 2 runs, same pathspec | FAIL then PASS | 1st refused CORRECTLY: a foreign `index.lock` plus 6 files another seat had staged mid-drain; retried after `2.0.0_SA_COO~G`'s drain merged (`e65ae0366b`); never unstaged or forced their files |
| comp-pulse risk reflex (inside safe-commit) | `diff` | PARTIAL | danger map 90.7h STALE -> NOT-DECIDABLE; "could not check" is not "checked clean" |
| naming-gate (inside safe-commit) | -- | WARN | 2 RAISEs on `opal-data-news-v2` and its key template, graded "rule or registry defect, not a refusal"; a legacy-named bucket, the D14 repoint census, not a finding |
| Glob | `org/critical_paths/.open_deploys/news*` | FAIL | ripgrep timed out at 20s; `ls` answered (no news-layer3 sentinel open) |

Role minimum (DS: `comp-pipescript io` per gold script touched): SKIPPED with reason -- no gold script
touched; the surface is a Lambda under `infra/aws/lambda/`, outside comp-pipescript's domain.

**What worked:** reading the served table and the function's own log markers instead of any report
about them; the four-arm exercise with the real broken build as the negative arm.
**What failed:** my own first marker census counted one `Expected` hit as the "Expected 10 bullish + 10
bearish" warning; it was an article title ("Mamdani Expected to Announce..."). Caught by reading the
line, before it reached any claim. Also my first rejection-class grep (`local crime`) missed the
selection prompt's "Local news (crime, ...)" wording; caught by reading `:1655-1685`.
**Gap found:** the inbox Monitor EXPIRES AT 30 MINUTES. `/watcher` and `org/XXX.md` Step 1b-C prescribe
`timeout_ms: 3600000` and a stream that "never exits"; the Monitor tool caps any deadline at 1,800,000 ms,
and task `biqqfke6e` expired "after 30m with no events delivered". A seat that does not act on that
notification is deaf from minute 30. Re-armed here (`bdm0kq2er`, orphan check first: none).

---

## Work Completed

### 1. The deployed state is still this seat's build (DESIRED = APPLIED)
`opal-news-layer3-curation`: CodeSha256 `bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=` (the `d6913f1e9b`
build), LastModified 2026-09-11T19:31:57Z, `GPT_MODEL` and `ANALYSIS_GPT_MODEL` both `gpt-5.6-sol`. No
commit has touched `infra/aws/lambda/news_layer3_curation/` or `infra/aws/terraform/news-pipeline/` since
`d6913f1e9b`. Rule `news-trending-analysis-daily` ENABLED, `cron(15 11,21 * * ? *)`. `d6913f1e9b`,
`3b091aaf3c`, `b762afef56` all on origin/CLOUD. No `news-layer3*` deploy sentinel open.

### 2. Every fire since the deploy, from the function's own logs (EXERCISED)
7 of 7 scheduled fires (2026-09-11 21:16Z through 2026-09-14 21:16Z), each with START and REPORT:

| Fire (UTC) | Duration | Curation `prompt=` | BLOCKED: RELEVANCE (backfill) |
|---|---|---|---|
| 09-11 21:16 | 269 s | 29,917 | 0 |
| 09-12 11:16 | 220 s | 24,905 | 1 |
| 09-12 21:16 | 385 s | 23,573 | 8 |
| 09-13 11:16 | 265 s | 23,971 | 0 |
| 09-13 21:16 | 347 s | 24,675 | 0 |
| 09-14 11:16 | 372 s | 23,093 | 2 |
| 09-14 21:16 | 379 s | 26,452 | 2 |

Across all 7: 0 Traceback, 0 ERROR, 0 "Expected 10 bullish + 10 bearish" warnings, 0
NO_SUPPORTING_NARRATIVE drops, 0 TOPLINE_SOURCE warnings, 0 BACKFILL_SHORT, 0 HEADLINE_CAPPED; max memory
155 MB of 10,240 MB; longest run 385 s of the 900 s timeout. The curation prompt sits at 23-30k tokens
every run (the broken build sent 2,715). **`BLOCKED: RELEVANCE (backfill)` fired LIVE for the first time,
13 times in 4 runs** -- cricket, box office, a murder trial, an FT charts quiz, reader-letter columns --
the path proven only offline on 2026-09-11. HEADLINE_CAPPED has still never fired (the model writes
under 45 every time).

### 3. The served rows (the acceptance proper)
`opal-news-trending-daily`, 4 partitions, each Count 20 = 10 bullish + 10 bearish, **0 of 80 headlines over
45 chars** (max 43). `2026-09-11` was regenerated by the acceptance fire at 21:20:47-21:21:01Z; the
inverted "China Oil Demand Growth Anticipated" row is gone and no China/Sinopec row remains in that set.
`2026-09-15` empty at read time (next fire 11:15Z) -- expected.

### 4. `render_check.py` rebuilt and committed (`f23d4d3839`)
Beside the Lambda (deploy.sh zips `lambda_function.py` by name, so it never ships). Runs the handler's own
steps -- `load_latest_trending_report` (or `--report`), `prefilter_topics_by_finbert`,
`build_curation_prompt` -- no model, no secret, no write. Grades one `SORT EVIDENCE` line per candidate
topic and every candidate keyword present; every run also grades a planted mutant and refuses if it passes.
`--source` renders any candidate file, e.g. the pinned bytes about to be zipped.

| Arm | rc | Rendered |
|---|---|---|
| HEAD + saved report 2026-09-11T11:16Z (`.runtmp/l2_latest.json`) | 0 | 98,405 chars, 65 of 65 -- the 2026-09-11 scratchpad numbers exactly |
| HEAD + live report 2026-09-14T21:16Z | 0 | 88,496 chars, 57 of 57; ~26.6k tokens inferred beside that fire's measured 26,452 |
| `3e83049fe0` (the broken build) + saved report | **1** | 10,145 chars, **0 of 65** -- REFUSED |
| `06b6cef383` (its correction) + saved report | 0 | 98,405 chars, 65 of 65 |

### 5. FINDING (pre-existing, selection path; NOT fixed -- it moves served output)
MarketWatch reader-letter advice columns reach the panel through the SELECTION pass via the `consumer`
keyword bucket, while the BACKFILL relevance check refuses the identical articles:

| Served | Row | Carrying articles (sample) | Backfill on the same article |
|---|---|---|---|
| 09-11 bearish-2 | "Inherited Homes Spark Twin Tax Dispute" | "'It's not fair': My twin brother and I were left houses by our parents..." ; "I'm a single 58-year-old veteran... Can I retire?" | REFUSED 09-12 11:19Z and 21:22Z |
| 09-13 bearish-1 | "Couple Fears Financial Exploitation" | "'We fear financial exploitation': Who will manage our finances if my wife and I become incapacitated?" | REFUSED 09-14 11:21Z |
| 09-13 bullish-5 | "Support Gaps Widen for Aging Seniors" | the same "58-year-old veteran" letters; one Housing Wire piece at FinBERT +0.9269 carried the sort | -- |
| 09-14 bearish-8 | "Americans Fear Working Until They Die" | "The future of retirement? Work until you die." x4 ; "10 biggest retirement fears - and what you can do" | -- |

Mechanism, read from source (the inference is labelled as one): no selection-side text names advice
columns (whole-file census for `advice|personal finance`: 2 hits, both the backfill prompt, `:2145`, `:2159`),
and the curation SYSTEM message (`:1979-1990`) reads "ONLY REJECT topics that are: SPORTS / Entertainment /
Spam / Crypto ... ALL other topics are FINANCIAL and should be SELECTED" -- which contradicts the USER prompt's
own wider list (`:1666-1673`: stock picks "ALWAYS REJECT", local news, political scandals). The same
contradiction plausibly explains two Seeking Alpha single-stock pieces served on the stock-pick class the
user prompt names: "OMAH Touted With Berkshire in Bear Market" (09-11 bullish-2) and "Agree Realty Retains
Cost-of-Capital Edge" (09-13 bullish-1). Many `consumer`-bucket articles carry FinBERT 0.0 (unscored), so one
scored article decides the direction -- which is how the same letters served bearish on one day and bullish on
another.

**CORRECTION of this seat's own record:** `logs/2026-09-11/backfill_fix_1910-1945Z.md` Work Completed 1 says
the backfill rules 8-9 name "the SAME rejection classes the selection pass applies (sports, entertainment,
local crime, advice columns, stock picks)". The selection pass does not name advice columns, and its system
message says to reject only four classes. The backfill list is WIDER than the selection pass's, and the
measured consequence is the table above.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT fix the selection prompt | it removes rows from the served panel = moves served output; the 2026-09-11 authority ("just fix the pre-existing defect") was scoped to the backfill defect. Surfaced as a call with a rec |
| Did NOT persist backfill provenance (old Next Step 3) | adds fields to served rows -- same gate |
| Retried safe-commit in the shared tree rather than a worktree | the contamination was another seat's in-flight drain; once it merged, the index was clean and this was a one-file commit (Rule 14b non-application) |
| Did not unstage or `--force` past the foreign staged files | they were `2.0.0_SA_COO~G`'s live work |
| Did not file the naming-gate RAISEs | legacy-named bucket; the gate grades them as registry defects itself; the D14 repoint census, not a finding |
| Negative arm = the real broken build, not a synthetic one | a check that has only seen synthetic mutants has not been shown to catch the defect it exists for |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `infra/aws/lambda/news_layer3_curation/render_check.py` | new, see commit message | Yes -- `f23d4d3839` (LOCAL) |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-09-15/news_layer3_acceptance_and_render_check.md` | this log | Yes -- this commit |
| `org/mcp/sessions/d2a7b357-7407-41d6-ad83-043404c6b0c6.serial` | session serial (halt gate) | No -- local, session-scoped |
| scratchpad: `accept_parse.py`, `ddb_2026-09-1{1..5}.json`, `l3_logs.json`, `logs_summary.txt`, `l3_cfg.json` | the instruments behind every number above | No -- session scratchpad |

---

## Blockers

None. The selection-prompt fix is a call at Andrew, not a blocker on anything this seat holds.
Push to origin is integrator-only (`0.0.0_AB_MSTR`).

---

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| none -- the durable artefacts are `render_check.py` (`f23d4d3839`) and this log | -- | -- |

---

## Current State

`opal-news-layer3-curation` (Lambda, us-east-1) is LIVE on the `d6913f1e9b` build, CodeSha256
`bWvoG+WeKBa/b/S1NPHV2W1G2p16kZMZr+jXt9nrw1M=`, both model env vars `gpt-5.6-sol`, fired 7 of 7 times since
the 2026-09-11 deploy with no errors; its table `opal-news-trending-daily` serves 20 well-formed rows per day
(10+10, all <=45 chars). The acceptance read of that deploy is CLOSED: PASS. The one open quality defect is
pre-existing and in the SELECTION pass: the curation system message (`lambda_function.py:1975-1995`) tells the
model to reject only sports/entertainment/spam/crypto and select everything else, and nothing on the selection
side names advice columns, so MarketWatch reader-letter columns in the `consumer` bucket reach the panel (4 rows
in 4 days) while the backfill path refuses the same articles. `infra/aws/lambda/news_layer3_curation/render_check.py`
(`f23d4d3839`, LOCAL) is the pre-deploy check for any prompt edit: `python
infra/aws/lambda/news_layer3_curation/render_check.py [--report <l2.json>] [--source <candidate.py>]`, exit 0
OK / 1 refused / 2 could not render. A saved Layer 2 report sits at `.runtmp/l2_latest.json` (2026-09-11T11:16Z).
Proven rollback for the function is unchanged: rebuild from `494b80e867` (sha `HXl8Hh..`) and `safe-apply`.

---

## Next Steps

1. **[Andrew's call] Close the selection-pass gap.** Rec: in `curate_topics_with_gpt`'s system message, replace
   "ONLY REJECT ... ALL other topics are FINANCIAL and should be SELECTED" with the same rejection list the backfill
   prompt uses (sports, entertainment, local crime, personal-finance advice columns, stock picks, crypto), and add
   advice columns to the user prompt's SKIP list. Removes rows from the served panel, so it needs his word.
2. **[0.1.0_DS_MarketIntelligence] On that word:** edit; `render_check.py --source <pinned build>` before upload;
   rehearse on a throwaway `2099-01-NN` partition; ledger; `safe-apply`; read the next scheduled fire.
3. **[0.1.0_DS_MarketIntelligence] Persist backfill provenance to the row** (`backfilled`, `topline_source_check`)
   -- carried; same served-output gate.
4. **[0.0.0_AB_MSTR] Publish `f23d4d3839` and this log's commit** -- integrator-only push.
5. **[Andrew's call] Upstream label fidelity in `news-trending-analysis`** -- carried from 2026-09-11 (44.1% of
   labels describe under half their cluster); the `consumer` bucket being mostly reader letters is one more data point.
6. **[1.0.0_SA_CTO] `/watcher` and `org/XXX.md` Step 1b-C prescribe `timeout_ms: 3600000` and a stream that never
   exits; the Monitor tool caps at 30 minutes** (measured: `biqqfke6e` expired at 30m). Recorded here, not messaged.
