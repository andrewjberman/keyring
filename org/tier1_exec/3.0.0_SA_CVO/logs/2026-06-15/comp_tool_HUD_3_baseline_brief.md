# comp-tool HUD #3 — blind-grep-where-a-tool-exists BASELINE + buried-tool ranking + #1/#2 seed (CVO measurement arm)

**archetype:** VALIDATE
**secondary_archetypes:** TRACE
**Andrew-direct via CTO (215810Z + 215929Z amend).** #3 = the data arm that targets + validates CTO's #1 (PreToolUse intercept hook) + #2 (`comp-which` router). Ground-truthed against **425 ajb_workspace session transcripts** (`~/.claude/projects/...`, full tool-call args) over the window **2026-05-20 → 2026-06-15**. Method + reproducibility: `org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/hud3_classify.py`.

## Data-reachability (what's exact vs estimated)
- **Transcripts (425, arg-level) = the gold source** — every Grep `pattern`, Bash `command`, Glob `pattern`, Read `file_path`. The classification below is computed on these, EXACT counts.
- agent telemetry (66.8k, 46 files) = frequency-only (no args) — corroborates volume, can't classify.
- comp-tools-log (6,026, arg-level) = the comp-tool USAGE side (what's already used) — the #2-router question→tool seed.
- The ONE judgment layer = classifying a search as "comp-answerable" (the regexes); precision-tuned below, residual noise flagged.

## BASELINE — blind-search-where-a-comp-tool-exists

Searches split by intervention-confidence (a comp-tool use / `git` / `ps` / `safe-commit` is EXCLUDED from both num+denom — it's not a bypass):

| Tier | what | ops | comp-answerable | rate |
|---|---|---|---|---|
| **TIER-1** | Grep/Glob/bash `grep`/`find` = REPO **relationship** search (the clean bypass signal) | 8,801 | 1,765 | **~20%** |
| AWS-CLI | `aws s3/lambda/cw...` | 2,869 | 2,828 (98.6%) | **mostly LEGIT** — F5-verify-own-change against served (per the never-trust-rc=0 rule) or census; NOT a comp-bypass. Excluded from the headline. |
| TIER-2 | Read/`cat` file-view | 17,855 | 1,632 | ~9% (softer — reading source to edit is legit; lower-confidence as "blind") |

**Headline: ~1 in 5 clean repo-relationship-searches (Grep/grep/find) target something a comp-* tool answers deterministically.** Precision caveat (honest): residual noise remains — some matches are greps OF a specific gold-script's SOURCE for its internal config/env (comp-pipescript io gives the I/O contract, not a script's internals), so the TRUE high-confidence bypass band is **~15-18%**. The SHAPE (which tools, which patterns) is solid regardless of the last point.

## BURIED-TOOL ranking (TIER-1 — which comp tool was bypassed, by volume)
1. **comp-pipescript** (io/--resource 453 + io/feeds/consumers 302 = **755**) — the MOST buried; S3-key + gold-script-id reference searches.
2. **comp-transform / comp-routes (645)** — portal-component / endpoint / scoped-route searches.
3. **comp-iam / comp-aws (333)** — lambda-name searches.
4. comp-iam (33) — IAM role/policy.
=> CTO's #1 hook should prioritize comp-pipescript + portal-tools redirects (they cover ~80% of the bypass volume).

## TARGET PATTERNS for #1 (the intercept hook) — precision-over-recall

Fire the advisory ONLY when ALL hold: (a) the op is a Grep/Glob/bash-grep/find (NOT a Read of a file being edited, NOT an `aws`-against-live verify, NOT a comp-tool use); (b) the search TARGET matches a class below; (c) NEGATIVE-FILTER: the command does not already contain `comp-`/`pipescript`/`git `/`safe-commit` (else it's a tool-use/archaeology, not a bypass).

| # | target regex (high-confidence) | -> comp call |
|---|---|---|
| 1 | gold-script id `(?<![\w])(INF_)?[A-DIS]_\d{2}[a-z]?(?![\w])` | `comp-pipescript io/feeds/consumers <id>` |
| 2 | S3 served key `s3://opal-` / `opal-data-\w+` / `/(gold\|platinum\|silver)/` / `\.parquet` (when the SEARCH is for references, not viewing one file) | `comp-pipescript io` / `pipescript --resource <key>` |
| 3 | lambda name `opal-[a-z-]+` / `(inf\|bd)-[a-z-]+-(trigger\|runner\|publisher\|daily)` / `yang-generate-*` / `causality-*` | `comp-iam service <fn>` / `comp-aws` / `pipescript --resource` |
| 4 | portal component/route `portal/src/` / `\.tsx` / `/api/(scoped\|general)/` / `getAdvisor*` | `comp-transform schema-check` / `comp-routes behaviors` |
| 5 | IAM role/policy `iam[_-]?role` / `:role/` / `aws_iam_policy` | `comp-iam` |

NEGATIVE patterns (do NOT fire — keeps the advisory non-noise): a grep WITHIN a single named source file for its internal vars (`grep X data/.../foo.py`), any `aws s3 cp/head` verifying own served output (F5-legit), any command already invoking a comp tool.

## QUESTION→TOOL MAP for #2 (`comp-which` router) — ranked by bypass frequency
1. "what produces/consumes this S3 key / who reads this artifact?" -> `comp-pipescript io` / `pipescript --resource` (453+ obs)
2. "which producer/endpoint feeds this portal component / what's the scoped route?" -> `comp-transform` / `comp-routes` (645)
3. "what does <gold-id> read/write / who consumes it?" -> `comp-pipescript io/feeds/consumers` (302)
4. "what does this lambda do / its IAM / its thread?" -> `comp-iam service` / `comp-aws` / `pipescript --resource` (333)
5. "what AWS resources exist / which thread owns them?" -> `comp-aws` / `comp-pipescript deployed` / `pipescript <name>`
6. "what perms does this role have / is it a real grant?" -> `comp-iam` (mind the Deny-guardrail FP class)
(comp-tools-log corroborates demand: comp-pipescript 4165 runs, comp-transform 263, comp-routes 187, comp-iam 233, comp-kuzu 423 — the high-traffic question classes #2 covers first.)

## BEFORE/AFTER (intervention proof)
This is the BEFORE. Re-run `org/tier1_exec/3.0.0_SA_CVO/logs/2026-06-15/hud3_classify.py` post-#1-hook over the new-transcript window: a working hook drives the TIER-1 comp-answerable rate DOWN (agents redirect to the comp call) — if it stays flat, the advisory is ignorable noise -> kill or re-tune. The per-class breakdown is the tuning signal (which redirect agents accept vs ignore).

— 3.0.0_SA_CVO
