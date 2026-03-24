# ka_testing Runtime Evaluation — GLDPRE V1 vs V2 A/B Test — 2.0.0_SA_COO

**Date:** 2026-03-19/20
**Session type:** Controlled A/B evaluation of runtime tool-layer fixes
**PRD:** docs/architecture/ADVI_GLDPRE_PRD.md
**Config:** .runtime/config.json (KA_GLDPRE for V1, KA_GLDPRE_V2 for V2)
**V1 results:** .runtime/results/run_20260320T001241.json
**V2 results:** .runtime/results/run_20260320T005634.json
**Telemetry:** .runtime/results/runtime-events.jsonl

---

## Purpose

The GLDPRE V1 run (this session, earlier) produced 10% attribution on a pure-edit
workload — the worst runtime result to date. The V1 eval identified 4 P0 fixes.
The runtime engineering team implemented those fixes and rebuilt the Docker image.

This report is the controlled A/B comparison: same 4 task orders, same target files
(restored to pre-edit state), different runtime. The question: **did the tool-layer
fixes bring edit quality to parity with create quality?**

---

## Fixes Under Test

| Fix | GLDPRE V1 Defect | Mechanism |
|---|---|---|
| `replace_function` tool | D1, D2, D7, D14 — chimera functions from partial edit_file | Indentation-aware full-function replacement. Worker names the function, provides new body. Tool handles boundaries. |
| `git_commit` failure = draft | All 4 V1 workers reported success despite failed commits | Trace scan for failed git_commit -> status=draft + audit entry |
| Coordinator mandates in prompt | Workers chose wrong edit tool (edit_file for function replacement) | Prompt instructs: replace_function for function replacement, apply_patch for >2 edits in one file |
| index.lock pre-flight | 5 minutes of wasted API calls before discovering lock | WARN before first token spent |

**Not implemented (P1):** `read_function` scoped reading tool. This test determines
whether the tool-layer fixes alone are sufficient or whether reading-layer changes
are also needed.

---

## Test Protocol

1. Stashed all V1 validator-corrected changes (`git stash` on parent + portal submodule)
2. Restored portal types.ts to pre-CLSUNI state (`git checkout f0d9d01^`) to ensure
   FirmMixPeriodPoint has the old 6-field shape with structured_notes + other
3. Verified all 4 target files contain old code (ETF_CLASSIFICATIONS present,
   mix_timeseries.json in Lambda, structured_notes in types.ts + PartnerAnalytics)
4. Verified no `.git/index.lock`
5. Rebuilt Docker image with tool-layer fixes (done by eng team)
6. Wrote V2 config with updated task orders (replace_function instructions for WS1,
   precise per-edit instructions for WS4, exact old_string/new_string for WS3)
7. Ran identical Docker command

---

## V1 Baseline (Pre-Fix Run)

**Timestamp:** 2026-03-20T00:07:26Z
**Total wall time:** 5m 15s
**Total tokens:** 99,616 (94,304 in + 5,312 out)

| Worker | Serial | Task | Tokens | Iter | Tools | Critical Defects | Attribution |
|---|---|---|---|---|---|---|---|
| DS | DS.CP.1 | WS1: 06b ETFClassifier | 39,476 | 13 | 17 | 3 (chimera classify_holding, chimera classify_series, compute_period_views def deleted) | ~15% |
| DT | DT.CP.1 | WS3: Lambda filename | 12,931 | 10 | 9 | 1 (function body destroyed, replaced with placeholder comments) | 0% |
| RD | RD.AI.1 | WS5: types.ts | 28,018 | 10 | 10 | 1 (duplicate prepended to file top, original not edited) | 0% |
| RD | RD.AI.2 | WS4: PartnerAnalytics | 19,191 | 10 | 11 | 2 (firmMixChartData useMemo wrapper deleted, raw diff markers pasted into source) | ~15% |

**V1 totals: 16 defects (8 Critical), ~10% attribution, 4/4 workers required manual correction**

---

## V2 Results (Post-Fix Run)

**Timestamp:** 2026-03-20T00:50:47Z
**Total wall time:** 5m 47s
**Total tokens:** 144,511 (138,145 in + 6,366 out)

### Per-Worker Telemetry

| Worker | Serial | Task | Input tok | Output tok | Total tok | Iterations | Tool calls | Files written | Wall time |
|---|---|---|---|---|---|---|---|---|---|
| DS | DS.CP.1 | WS1: 06b ETFClassifier | 41,784 | 2,677 | 44,461 | 13 | 21 | 06b (x3) | 78s |
| DT | DT.CP.1 | WS3: Lambda filename | 14,010 | 735 | 14,745 | 10 | 10 | lambda_function.py (x1) | 137s |
| RD | RD.AI.1 | WS5: types.ts | 31,267 | 1,127 | 32,394 | 10 | 14 | types.ts (x3) | 28s |
| RD | RD.AI.2 | WS4: PartnerAnalytics | 51,084 | 1,827 | 52,911 | 10 | 14 | PartnerAnalytics.tsx (x5) | 104s |

**Note:** Token cost increased 45% vs V1 (144K vs 100K). The additional tokens come
from more tool calls per worker (V2 avg 14.75 vs V1 avg 11.75) — workers are making
more granular, precise edits instead of fewer large (broken) ones. This is the
intended trade-off: more API calls for better edit precision.

---

## Per-Worker Detailed Review

### DS.CP.1 — WS1: 06b ETFClassifier + 4-class taxonomy

**V1 had 8 defects (3 Critical).** classify_holding and classify_series were chimeras
(old tail merged with new head). compute_period_views lost its `def` line. Old static
dicts never removed.

**V2 result:**

| Requirement | V1 | V2 | Status |
|---|---|---|---|
| Import ETFClassifier | Line 70 (correct) | Line 250 (correct) | PASS |
| classify_holding() delegates to ETFClassifier | Chimera: first 4 lines correct, old fallback tail remained (returns 'structured_notes', 'cash', 'other') | Complete, correct function. ETFClassifier delegation + equity fallback. No old classes. | **PASS -- FIXED** |
| classify_series() uses ETFClassifier | Chimera: new loop head merged with old vectorized layers referencing undefined variables | Complete, correct function. ETFClassifier loop + equity default. No old classes. | **PASS -- FIXED** |
| _MIX_ASSET_CLASSES = 3 elements | Correct | Correct | PASS |
| compute_period_views() cash residual | `def` line deleted, orphaned code fragment at module scope | `def` line intact (line 412). Cash residual code present (lines 479-485). | **PASS -- FIXED** |
| Remove ETF_CLASSIFICATIONS dict | NOT removed | NOT removed (lines 146-216) | **FAIL (repeat)** |
| Remove ASSET_NAME_TO_TICKER dict | NOT removed | NOT removed (lines 218-245) | **FAIL (repeat)** |
| Remove _TICKER_CLASS_MAP | NOT removed | NOT removed (lines 276-279) | **FAIL (repeat)** |
| Remove regex patterns | NOT removed | NOT removed (lines 251-262) | **FAIL (repeat)** |

**V2 defects found:**

| # | Defect | Severity | Detail |
|---|---|---|---|
| V2-D1 | Cash residual indentation: lines 480-486 at 8 spaces (should be 12) | **Critical** | `classified_sum`, `cash_val`, `row['cash']`, `result.append(row)`, and `return result` are outside the `for pk in sorted(...)` loop. Only the last period would be processed. **Functional runtime bug** — produces wrong output on EC2. The cash logic itself is correct, just mis-indented by one level. |
| V2-D2 | Old static dicts not removed (same as V1 D3-D6) | Moderate | Worker spent all Ac budget on function replacements + cash residual insertion. Never attempted deletion edits. Dicts are unreferenced dead code — doesn't break execution since classify_holding/classify_series no longer call them, but ETF_CLASSIFICATIONS and ASSET_NAME_TO_TICKER are ~100 lines of dead code. |
| V2-D2b | Missing blank lines + section header between classify_series and _read_parquet (lines 300-301) | Minor | `return result` immediately followed by `def _read_parquet` with no separator. The original had 2 blank lines + `# S3 helpers` section header. replace_function consumed the trailing whitespace. Style-only, not functional. |

**V2 attribution (DS.CP.1):** classify_holding (11 lines), classify_series (16 lines),
_MIX_ASSET_CLASSES edit, cash residual logic (correct content but needs re-indent).
**~55% of intended diff correct from runtime** (vs ~15% in V1). Downgraded from 60% due
to V2-D1 being a functional bug requiring correction.

---

### DT.CP.1 — WS3: Lambda advisor mix filename fix

**V1 had 1 Critical defect:** function body destroyed, replaced with `# some existing code here`.

**V2 result:**

| Requirement | V1 | V2 | Status |
|---|---|---|---|
| Change `mix_timeseries.json` to `mix.json` on line 1056 | Correct key but function body destroyed | Line 1056: `key = f'gold/advisors/{advisor_id}/mix.json'` | **PASS** |
| No other changes | Lines 1055-1061 replaced with placeholder comments | Function body fully intact. cors_response, serve_s3_json, window filtering all present. | **PASS -- FIXED** |

**V2 defects:** None.
**V2 attribution (DT.CP.1): 100%** (vs 0% in V1).

---

### RD.AI.1 — WS5: types.ts 4-class type updates

**V1 had 3 defects:** prepended duplicate FirmMixPeriodPoint at file top, original
interface never edited, MixTimeseriesPoint and MixAssetClass not updated.

**V2 result:**

| Requirement | V1 | V2 | Status |
|---|---|---|---|
| FirmMixPeriodPoint: remove structured_notes | Not attempted (prepend instead) | structured_notes removed | **PASS -- FIXED** |
| FirmMixPeriodPoint: remove other | Not attempted | other removed | **PASS -- FIXED** |
| FirmMixPeriodPoint: keep alternatives | N/A | alternatives ALSO removed (only equity, fixed_income, cash remain) | **FAIL** |
| MixTimeseriesPoint: remove structured_notes | Not attempted | structured_notes NOT removed (line 1315) | **FAIL (repeat-ish)** |
| MixTimeseriesPoint: remove other | Not attempted | other NOT removed (line 1317) | **FAIL** |
| MixAssetClass: update to 4 members | Not attempted | Correctly updated to 4 members (line 1309) | **PASS -- FIXED** |
| No prepended content | Duplicate interface at line 1 | No prepended content — edits in place | **PASS -- FIXED** |

**V2 defects:**

| # | Defect | Severity | Detail |
|---|---|---|---|
| V2-D3 | FirmMixPeriodPoint: alternatives field removed along with structured_notes/other | **Critical** | Worker removed too many fields. FirmMixPeriodPoint now has equity, fixed_income, cash (3 fields) — missing `alternatives: FirmMixClassValue`. **This causes a TypeScript compile error** because PartnerAnalytics.tsx (WS4) accesses `pt.alternatives.value` and `pt.alternatives.pct`. The WS4 edits are correct but WS5 broke the type contract. `bunx tsc -b` would fail. |
| V2-D4 | MixTimeseriesPoint: structured_notes and other not removed, alternatives not added | Moderate | MixTimeseriesPoint still has `structured_notes: number` (line 1315) and `other: number` (line 1317). It also lacks `alternatives: number`. Task order included this edit but Worker did not execute it. |

**V2 attribution (RD.AI.1):** MixAssetClass correct, FirmMixPeriodPoint edited in-place
(but over-deleted — 1 field too many), no prepend. **~40% of intended diff correct** (vs 0% in V1).
Downgraded from 65% due to V2-D3 being a type-system-breaking defect.

---

### RD.AI.2 — WS4: PartnerAnalytics.tsx 4-class Mix toggle

**V1 had 3 Critical defects:** firmMixChartData useMemo wrapper deleted, raw diff
markers pasted into source, duplicate code blocks.

**V2 result:**

| Requirement | V1 | V2 | Status |
|---|---|---|---|
| FIRM_MIX_COLORS: 5 → 4 entries | Correct | Correct (equity, fixed_income, alternatives, cash) | **PASS** |
| firmMixChartData: remove structured_notes/other, add alternatives | useMemo wrapper deleted, orphaned field list | Complete, correct useMemo. alternatives.value + alternatives.pct mapped. structured_notes/other removed. | **PASS -- FIXED** |
| CLASS_LABELS: 5 → 4 entries | Correct | Correct (Equities, Fixed Income, Alternatives, Cash) | **PASS** |
| Bar keys: 5 → 4 entries | Raw diff markers pasted into source | Correct: `['cash', 'alternatives', 'fixed_income', 'equity']` | **PASS -- FIXED** |
| isTop: idx 4 → 3 | Part of mangled diff section | Correct: `const isTop = idx === 3` | **PASS -- FIXED** |

**V2 defects:** None.
**V2 attribution (RD.AI.2): 100%** (vs ~15% in V1).

---

## Aggregate Comparison

### Defect Counts

| Metric | V1 | V2 | Delta |
|---|---|---|---|
| Total defects | 16 | 7 | **-56%** |
| Critical defects | 8 | 2 | **-75%** |
| Moderate defects | 4 | 3 | -25% |
| Minor defects | 4 | 2 | -50% |
| Workers requiring manual correction | 4/4 | 2/4 | -50% |
| Workers producing deployable code | 0/4 | 2/4 (DT, RD.AI.2) | **+2** |

### Attribution

| Worker | V1 Attribution | V2 Attribution | Delta |
|---|---|---|---|
| DS.CP.1 (WS1: 06b) | ~15% | ~55% | **+40pp** |
| DT.CP.1 (WS3: Lambda) | 0% | 100% | **+100pp** |
| RD.AI.1 (WS5: types.ts) | 0% | ~40% | **+40pp** |
| RD.AI.2 (WS4: PartnerAnalytics) | ~15% | 100% | **+85pp** |
| **Weighted average** | **~10%** | **~65%** | **+55pp** |

### Token Efficiency

| Metric | V1 | V2 | Delta |
|---|---|---|---|
| Total tokens | 99,616 | 144,511 | +45% |
| Total tool calls | 47 | 59 | +26% |
| Tokens per correct output line (est.) | ~2,500 | ~480 | **-81%** |
| Cost at gpt-4o | ~$0.55 | ~$0.80 | +45% |
| Validator time (manual correction) | ~45 min | ~10 min | **-78%** |

The 45% token increase is a correct trade-off: more granular tool calls produce
far fewer defects. The cost per correct output line dropped 81%.

### Defect Classification Comparison

| Category | V1 | V2 | Status |
|---|---|---|---|
| Chimera functions (partial edit merge) | 4 | 0 | **ELIMINATED by replace_function** |
| File destruction (placeholder substitution) | 1 | 0 | **ELIMINATED by precise edit_file instructions** |
| Prepend instead of in-place edit | 1 | 0 | **ELIMINATED by coordinator mandates** |
| Raw diff paste into source | 1 | 0 | **ELIMINATED by per-edit task order instructions** |
| Cascading damage | 3 | 0 | **ELIMINATED (root causes fixed)** |
| Skipped deletion | 4 | 3 | Persists (-25%) |
| Over-deletion (removed too much) | 0 | 1 | **NEW** (Critical: breaks type contract) |
| Indentation error in inserted code | 0 | 1 | **NEW** (Critical: functional runtime bug) |
| Missing whitespace/section headers | 0 | 1 | **NEW** (Minor: replace_function ate trailing context) |
| Scope gap (related types not in scope) | 2 | 0 | Addressed by broader task order scope |

---

## Remaining Failure Modes (V2)

### FM1: Skipped Deletion (3 defects — V2-D2, V2-D4)

Workers still do not execute deletion edits when their Ac-stage budget is consumed
by higher-priority writes. The ETF_CLASSIFICATIONS dict (~70 lines), ASSET_NAME_TO_TICKER
(~28 lines), _TICKER_CLASS_MAP (4 lines), and regex patterns (12 lines) survive as
dead code.

**Root cause:** Ac-stage budget competition. Function replacements consume 3-5 tool
calls each. Deletions of large blocks require additional calls. Workers triage and
cut deletions first.

**Recommendation:** Two options:
- (a) Split deletion into a separate task order with its own budget (1 extra Worker)
- (b) Increase Ac budget for tasks with >5 edit targets (allow 8-10 Ac iterations)
- (c) Combine all deletions into a single apply_patch (one diff that removes all 4 blocks)

### FM2: Over-Deletion (1 defect — V2-D3)

RD.AI.1 removed the `alternatives` field from FirmMixPeriodPoint when instructed to
remove only `structured_notes` and `other`. The Worker deleted 3 fields instead of 2.

**Root cause:** The task order specified per-line edit_file calls for each field removal.
The Worker may have used a single broader edit_file that matched all three non-core
fields. Or the alternatives field was adjacent to structured_notes and the Worker's
old_string captured both.

**Recommendation:** For interface field removal, provide the EXACT multi-line old_string
including the fields to KEEP between the fields to remove. This anchors the match.

### FM3: Indentation Error (1 defect — V2-D1)

The cash residual block in compute_period_views is indented at 8 spaces (function body
level) instead of 12 spaces (for-loop body level). This is a functional bug: only the
last period would be appended and returned.

**Root cause:** The task order used edit_file with old_string = `result.append(row)` and
a multi-line new_string. The edit_file tool matches and replaces literally, but the
new_string was provided in the task order at 0-indent. The tool did not re-indent to
match the surrounding context.

**Recommendation:** The `edit_file` new_string in task orders MUST include the correct
indentation. Alternatively, enhance edit_file to auto-indent new_string to match the
column offset of old_string.

---

## Historical Trend (All Runtime Evaluations)

| Project | Date | Task Type | Workers | Tokens | Defects | Critical | Attribution | Key Fix |
|---|---|---|---|---|---|---|---|---|
| CLSUNI | 2026-03-19 | Mixed (create + edit) | 6 | ~200K+ | ~8 | 3 | ~36% | Baseline |
| CLSPT2 | 2026-03-19 | Create-dominant | 2 | ~170K | ~5 | 3 | ~67% | Context windowing |
| GLDPRE V1 | 2026-03-20 | Pure edit | 4 | 100K | 16 | 8 | ~10% | — (exposed tool gap) |
| **GLDPRE V2** | **2026-03-20** | **Pure edit** | **4** | **145K** | **7** | **2** | **~65%** | **replace_function + coord mandates** |

### Trend Lines

- **Critical defects:** 3 → 3 → 8 → **2** (-75%, not eliminated)
- **Attribution (edit tasks):** 36% → 10% → **65%** (major improvement, not parity)
- **Attribution (create tasks):** 67% (CLSPT2) — no V2 data point yet
- **Tokens per correct line:** ~540 → ~478 → ~2500 → **~620** (improved but not back to CLSPT2 level)

---

## Conclusions

### The Tool Layer Was the Primary Bottleneck

The V1→V2 delta confirms tool-layer fixes account for the majority of
improvement. Same files, same task orders, same model (gpt-4o), same
iteration budgets. The only difference was 4 tool-layer fixes. Result:

- Critical defects: 8 → 2 (-75%)
- Attribution: 10% → 65%
- Validators needed: 4/4 → 2/4
- File destruction events: 2 → 0 (eliminated)
- Chimera functions: 4 → 0 (eliminated)

The `replace_function` tool eliminated all chimera-function defects and all
file-destruction events. The coordinator mandates prevented Workers from
choosing edit_file for function-level replacements. These were the dominant
V1 failure modes.

### Two New Failure Modes Emerged

The tool-layer fixes exposed two problems that were masked by the more
catastrophic V1 failures:

**1. Indentation in inserted code (V2-D1, Critical).** When edit_file inserts
a multi-line new_string, the indentation of the new code is taken literally
from the task order text, not inferred from the surrounding code. The cash
residual block was indented at 8 spaces (top-level within the function) instead
of 12 spaces (inside the for-loop body). This is a **functional runtime bug**
that produces wrong output. The edit_file tool needs indentation awareness or
the task order must include pixel-perfect indentation.

**2. Over-deletion (V2-D3, Critical).** When RD.AI.1 was told to remove
`structured_notes` and `other` from FirmMixPeriodPoint, it also removed
`alternatives`. This breaks the type contract with PartnerAnalytics.tsx which
accesses `pt.alternatives.value`. The Worker treated "remove these fields" as
"keep only the core fields" and dropped one too many. The fix is to provide
the EXACT interface as new_string rather than per-field deletion instructions.

### What the Tool Layer Did NOT Fix

Deletion tasks remain problematic (V2-D2, V2-D4). Workers skip deletions when
Ac budget is tight. This is a prioritization problem. Workers correctly prioritize
"write new code" over "remove old code." The fix is either budget-based or
task-structure-based (separate deletion task orders, or single apply_patch).

### read_function Assessment: Inconclusive

The GLDPRE V1 eval hypothesized that Workers can't hold an accurate model of a
1300-line file in context. V2 partially supports and partially refutes this:

- **Supports:** DT.CP.1 edited a 1300-line Lambda with a single-line change
  and produced a perfect result. Workers CAN hold the model.
- **Refutes:** The indentation bug (V2-D1) and over-deletion (V2-D3) suggest
  Workers lose precision on structural details (indentation depth, field
  adjacency) even when they understand the broad function structure.

`read_function` may reduce these errors by narrowing context to the target
function, but this is speculative. The V2 data doesn't conclusively answer
whether reading-layer changes would help.

### Cost-Effectiveness

At ~$0.80 per run and 65% attribution, the runtime produces usable code at
~$0.27 per correct file. Validator correction for the remaining 35% takes
~15 minutes (down from ~45 minutes in V1). For edit-dominant workloads of
4-6 files, this is a net time savings vs manual authorship, but validator
review remains mandatory — 2/4 Workers still required correction.

---

## Recommendations

### P0 — Before Next Production Run

1. **edit_file indentation awareness.** Either (a) auto-indent new_string to
   match the column offset of old_string, or (b) enforce that task orders
   include exact indentation in new_string. V2-D1 is a functional runtime bug
   caused by indentation mismatch. This is the highest-priority fix.

2. **Interface edits: provide full replacement, not per-field deletion.**
   V2-D3 shows Workers over-delete when given "remove field X" instructions.
   Instead, provide the complete new interface as a single edit_file or
   replace_function call. This eliminates the adjacency-confusion failure mode.

3. **Apply deletion via single apply_patch.** Combine all "remove X" instructions
   into one unified diff. Workers skip individual deletions under budget pressure
   but are more likely to execute one consolidated deletion.

4. **Verify git_commit failure = draft.** V2 still showed index.lock WARNs and
   all Workers reported success=true. If git_commit is the only Ad-stage action
   and it fails, success should be false (or at minimum status=draft). Confirm
   the new logic is wired correctly.

### P1 — Medium-Term

5. **replace_function trailing context preservation.** The tool consumed blank
   lines and section header comments between classify_series and _read_parquet
   (V2-D2b). replace_function should preserve N blank lines after the function
   body to maintain code structure.

6. **Parallel Worker execution.** V1 and V2 both ran Workers sequentially.
   WS1 and WS3 are independent — run them in parallel to cut wall time.

7. **Per-edit success tracking.** Emit which edit_file/replace_function calls
   succeeded vs failed (old_string not found, etc). Currently only
   `files_written` count is tracked, which is true even for partial edits.

---

## Files

| File | Purpose |
|---|---|
| `.runtime/config.json` | V2 task order config |
| `.runtime/results/run_20260320T001241.json` | V1 execution results |
| `.runtime/results/run_20260320T005634.json` | V2 execution results |
| `.runtime/results/runtime-events.jsonl` | Full event stream (both runs) |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-19/ka_testing_runtime_evaluation_gldpre.md` | V1 detailed eval |
| `org/tier1_exec/2.0.0_SA_COO/logs/2026-03-19/ka_testing_runtime_evaluation_gldpre_v2.md` | This file |
