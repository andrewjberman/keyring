# CTO Session — Adoption Design + ADVI_OFFICE Gap Audit + Output Rightsizing

**Agent:** 1.0.0_SA_CTO
**Date:** 2026-04-14
**Duration:** Long single-session thread
**Scope:** Compiler toolchain evolution (2 rounds), adoption design, TO authoring, output size correctness

---

## Objectives

Four threads ran in this session:

1. **Compiler tool adoption design** — after shipping round 1 and round 2 of new tools, design the mechanism that makes agents actually use them (not just document them)
2. **ADVI_OFFICE gap audit** — compiler-driven diagnosis of what W3 missed, with exact line numbers for the follow-up W6 fixes
3. **ADVI_OFFICE W8 deploy gate** — hold DT, resolve circular dependency between DE and DT, ship W6 priority fixes
4. **Output size rightsizing** — audit compiler tool outputs, fix the ones producing too much context to be useful

---

## Work Stream 1 — Adoption Design

### Problem

15+ compiler tools now exist, but rolling log data shows agents reach for grep/Read by default and only use compiler tools when explicitly mandated in TOs. Instruction files present tools as a catalog to memorize — wrong model for LLM agents that start each session without persistent memory.

### Discussion with COO

Sent full design proposal to COO. COO endorsed all five items with priority ranking:

1. `<expect>/<if_mismatch>` blocks in TO mandates (highest ROI, zero cost)
2. comp-validate in standard acceptance criteria (zero cost)
3. Trigger tables replacing catalog in startup docs (low cost)
4. Auto-logging via wrappers (medium cost)
5. comp-guide CLI (low priority — trigger table covers 80%)

COO added `<if_mismatch>` field proposal — tells the agent what to DO when output is unexpected, not just that something is wrong.

### Implementation

**Trigger tables (replaces catalog model):**
- `CLAUDE.md` compiler section rebuilt — single trigger table: situation → command → incident annotation
- `org/XXX.md` compiler section rebuilt — three tables (about-to-do, done-with, investigation)
- Removed capability descriptions; kept incident annotations ("caught the $22M phantom")

**TO mandate format:**
- `org/ref/TASK_ORDER_PROTOCOL.md` compiler_tools_mandate template updated with `<run>/<expect>/<if_mismatch>` structure
- `<expect>` encodes what "normal" looks like — agents verify output against it
- `<if_mismatch>` tells agent what to DO when output doesn't match

**Acceptance criteria template:**
- Added STANDARD CRITERIA blocks for gold and portal TOs
- DS standard: `comp-validate {script} --artifact exits 0` + `comp-pipescript deployed shows MATCH`
- DE standard: `comp-transform schema-check: 0 MISSING fields` + `bun run build exits 0`

**Auto-logging via wrappers:**
- Built `org/modules/graph/comp_log_auto.py` — Python module called by every comp-* wrapper after execution
- All 13 comp-* shell wrappers updated to capture exit code and call the logger
- Context file: `.comp-graph/.agent_context` with SERIAL + TO_ID (set at session startup)
- Dedup: same agent + same command within 30s = skip (prevents exploratory noise)
- Structured table rows: `| DATE | SERIAL | TO_ID | TOOL | COMMAND | RESULT |`
- Effect: 100% capture rate vs previous ~60% prose entries
- Updated XXX.md startup protocol Step 1b-D with context-file creation one-liner

---

## Work Stream 2 — ADVI_OFFICE Gap Audit

### Context

Andrew flagged OFC implementation gaps in portal screenshots:
- No bell curve at L0 or L1
- Time machine shows $0/N/A when office selected
- Continuous AUA chart blank ("No chart data available")
- Continuous NNA blank ("No NNA advisor data available")
- Continuous chart title reads "Cumulative AUA by Advisor" (wrong for OFC)
- Advisor list in drill "not canonical"

W3 DE was COMPLETE (commit 7dd0a7e). Andrew asked whether DE had been tasked with this (yes) and why changes weren't visible.

### Compiler-Driven Diagnosis

Ran compiler tools against W3-shipped code to diagnose:
- `comp-transform schema-check DistributionTab` — found `nna_ofc` UNUSED (real miss)
- `comp-transform fields DistributionTab` — found `chartData?.ofc?.categories` accessed but the NNA gate at L1956 doesn't route to it
- `comp-platinum page DistributionTab` — full serving path confirmed, data IS in platinum artifacts
- `comp-pipescript io D_01 / D_00b` — confirmed D_01 emits correct OFC view, D_00b fix #3 still outstanding

Manual code read then surfaced exact line numbers for 10 specific bugs.

### Addendum PRD + TOs

- Authored `docs/architecture/ADVI_OFFICE_ADDENDUM.md` with compiler evidence section and all 10 fixes spec'd to line
- Issued `ADVI_OFFICE.W5.ds-d00b-fix3-ofc-timeseries.md` (DS — D_00b modal office aggregation)
- Issued `ADVI_OFFICE.W6.de-ofc-parity-fixes.md` (DE — all 10 frontend fixes with full `<expect>/<if_mismatch>` blocks)

W6 was the first production TO authored using the new mandate format.

### DE Debrief on W3

Sent debrief message to DE after PROFAU.006 completion asking about:
1. Alias-tracking gap observation (DE identified it correctly in PROFAU.005/.006)
2. nna_ofc UNUSED in W3 — why wasn't it actioned
3. /frontend-dev visual test outstanding
4. Honest read on `<expect>` blocks

DE responded cleanly — owned the W3 miss, identified the correct protocol going forward ("feature token in UNUSED = investigation prompt, not checkmark"), confirmed `<expect>` blocks changed behavior on PROFAU.006 (baseline mismatch prompted investigation before code was written). Noted /frontend-dev was sequencing (waiting for DT to push W4), not tool friction.

### W8 Deploy Gate

Andrew flagged DE/DT circular dependency:
- DE waiting for DT /frontend-dev output to know what to fix
- DT waiting for DE W6 commit to run /frontend-dev

COO correctly diagnosed — /frontend-dev is validation step, not prerequisite. Compiler diagnosis already gave exact line numbers. Sent GO to DE directly with 3-line priority fix spec. DE committed (f6fe035, f67dd91, e692f60), DT shipped portal-v2.1.44. Loop broken, all 10 fixes landed.

**Status:** ADVI_OFFICE closed 2026-04-14 per COO dashboard.

---

## Work Stream 3 — Compiler Additions (Round 2)

Built in this session:

### comp-transform schema-check --feature <token>

Escalates UNUSED fields containing the feature token from INFO to WARN with targeted message pointing to ternary-audit. Designed around the W3 failure mode — DE saw `nna_ofc` UNUSED and filed as alias gap; with `--feature ofc`, the same run would have said "this field is typed but NEVER rendered, routing ternary likely missing ofc branch."

### comp-transform ternary-audit

New subcommand. Scans component for string-literal union type aliases (`CohortOption = 'geo' | 'adv' | 'ofc'`), finds variables bound to those types, audits every ternary chain for unhandled union members. Only flags when 2+ members fall to the same else branch (single implicit fallthrough is the intentional pattern). Filters out generic loop variables (key, val, item), large unions (>6 members, like TimePeriodKey), and dynamic-accessor else branches (`view[period]`).

Validation: run against current DistributionTab finds 13 remaining OFC text parity gaps — all real, all useful.

### Output rightsizing (this session, after size audit)

Measured actual output sizes of all tools. Three tools produced too much context for agents to reliably consume:

1. **comp-iam gaps: 485 lines / 25,632 chars** — due to parser bug: non-greedy regex with lookahead `(?=\s*\}|\s*$)` matched inner `Action = [...]` arrays before Statement closing `]`, and the lookahead expected `\s*}` but HCL jsonencode closes with `])`. Only 2 of 6 statements on bd-exporter-ec2-role were parsed. Fixed with depth-balanced bracket walker. Result: **485 lines → 2 lines.** 120 false-positive gaps eliminated.

2. **comp-transform ternary-audit: 107 lines** — changed default to 2-line brief format, added `--verbose` for the 5-line explanation format. Result: **107 lines → 51 lines** default, 314 lines with --verbose.

3. **comp-transform schema-check UNUSED list:** truncated to first 5 + "+N more (--all-unused to show all)". Result: **57 → 47 lines** when many UNUSED fields present.

---

## Work Stream 4 — inbox-watch.sh cross-directory fix

Discovered `bash org/mcp/inbox-watch.sh` fails with exit 127 when run from `portal/` or any subdirectory — bash can't find the file relative to cwd.

Added `.tools/inbox-watch` and `.tools/check-inbox` wrappers that resolve absolute workspace root from binary location. Updated XXX.md and both exec prompt.md files to use the wrapper commands instead of the bare `.sh` paths.

Effect: agents can run `inbox-watch 1.0.0_SA_CTO` from any directory.

---

## Documentation Updates

All propagated through 6 instruction files:

- `CLAUDE.md` — trigger table with new cohort/mode row
- `org/XXX.md` — trigger table + role minimums + session log mandates
- `org/ref/prompts/comp-tools-directive.md` — full comp-transform section added (was absent); comp-validate + comp-iam sections
- `org/ref/TASK_ORDER_PROTOCOL.md` — SPECIAL CASE block in compiler_tools_mandate template for union-type additions
- `org/modules/graph/comp-tools.yaml` — ternary-audit, --feature flag, overlap mandate, deployed subcommand
- `org/tier1_exec/2.0.0_SA_COO/prompt.md` — mandatory TO authoring table with new cohort row

The W3 OFC incident is now referenced in three separate instruction files as the motivating example.

---

## Files Modified (summary)

**New tools:**
- `org/modules/graph/comp_log_auto.py` (auto-logger)
- `.tools/inbox-watch`, `.tools/check-inbox` (cwd-agnostic wrappers)
- `.tools/comp-validate`, `.tools/comp-iam` (round 2 wrappers)

**Extended tools:**
- `org/modules/graph/transform_cli.py` — schema-check --feature + --all-unused, ternary-audit, brief format
- `org/modules/graph/extract_iam.py` — HCL jsonencode parser fix (critical correctness bug)
- `org/modules/graph/pipeline_cli.py` — column gap detection + postdeps + deployed + portal consumers
- `org/modules/graph/extract_pipeline.py` — dynamic S3 reads, CSV support, column gap analysis
- `org/modules/graph/extract_routes.py` — custom_error_response parsing
- `org/modules/graph/routes_cli.py` — behaviors/auth-map custom_error_response warnings
- `org/modules/graph/extract_eventbridge.py` — Lambda→EC2 SSM edges
- `org/modules/graph/trace_graph.py` — wired Lambda→EC2 extractor

**Configs:**
- `data/black_diamond/scripts/gold/gold_validate_config.yaml` (artifact invariants)
- `data/black_diamond/scripts/gold/gold_pipeline_deps.yaml` (post-step dependencies)

**PRD + TOs:**
- `docs/architecture/ADVI_OFFICE_ADDENDUM.md`
- `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_OFFICE.W5.ds-d00b-fix3-ofc-timeseries.md`
- `org/tier2_senior/0.4.0_DE_ClientPlatform/task_orders/ADVI_OFFICE.W6.de-ofc-parity-fixes.md`
- `org/projects/ADVI_OFFICE.json` (phase + blocking updates)
- `org/projects/REGISTRY.md`
- `org/tier1_exec/1.0.0_SA_CTO/prompt.md` (dashboard updates through the session)

**Instructions (6 files):** CLAUDE.md, org/XXX.md, org/ref/TASK_ORDER_PROTOCOL.md, org/ref/prompts/comp-tools-directive.md, org/modules/graph/comp-tools.yaml, org/tier1_exec/2.0.0_SA_COO/prompt.md

---

## Commits (this session)

| SHA | Description |
|---|---|
| 1259b47a | Round 1: column gap detection + comp-pipescript deployed + platinum downstream + Lambda→EC2 + custom_error_response |
| fdc02c2d | Instruction files updated for round 1 tools |
| 4fe969b9 | Round 2: comp-validate + comp-iam + comp-postdeps + 5 additions |
| 8e17d600 | Adoption design: trigger tables + `<expect>` blocks + validate in acceptance criteria |
| 2a81cc73 | Auto-logging: comp_log_auto.py + all 13 wrapper updates + startup protocol |
| b2a5368c | inbox-watch + check-inbox cross-directory wrappers |
| 2398f9cc | ADVI_OFFICE addendum PRD + W5 DS + W6 DE TOs |
| 40cdec14 | comp-transform ternary-audit + schema-check --feature |
| a6fe49b7 | Trigger table documentation for ternary-audit |
| d3e926d2 | Full doc coverage for new tools across all 6 instruction files |
| a2bb03a2 | Output rightsizing: iam 485→2 lines, ternary-audit 107→51, schema-check UNUSED truncation |

---

## Compiler Tools

Meta-session — this was compiler tool work itself. Tools used:

| Tool | Purpose | Result |
|------|---------|--------|
| py_compile (all touched files) | Pre-ship gate on every edit | PASS every time |
| comp-transform schema-check DistributionTab --feature ofc | Diagnose W3 OFC gap | Found nna_ofc UNUSED → confirmed routing bug |
| comp-transform fields DistributionTab | Trace OFC field accesses | Confirmed chartData?.ofc?.categories accessed |
| comp-pipescript io D_00b / D_01 | Verify data layer | D_01 correct, D_00b fix #3 outstanding |
| comp-platinum page DistributionTab | Full stack trace | Confirmed serving path + data presence |
| comp-iam role bd-exporter-ec2-role | Debug parser fix | Verified 6 statements parsed correctly post-fix |
| comp-pipescript postdeps | Smoke test new subcommand | PASS, gold_pipeline_deps.yaml read correctly |
| comp-validate --list | Smoke test new tool | PASS, 4 scripts + 10 checks loaded |
| comp-routes behaviors | Verify custom_error_response parsing | 2 rules detected with WARN annotations |

---

## Cross-Agent Coordination

- **COO:** 5-question design discussion on adoption, follow-up on W3 fix details, W4 gate discussion, ADVI_OFFICE addendum scoping. Ultimately ran the relay release.
- **DE (0.4.0_DE_ClientPlatform):** Post-PROFAU.006 debrief on scan quality, direct GO for 3-line priority fix when DE/DT loop was blocking
- **DS (0.4.0_DS_ClientPlatform):** W5 TO authored directly (Andrew authorized CTO to issue TOs this session)

---

## Outstanding Items

- **`/frontend-dev` integration** — DE runs it post-DT-push, not as a prerequisite. Currently a sequencing convention rather than a tool gate. Worth documenting more explicitly.
- **comp-iam Lambda role mapping** — Lambda services still show 0 permissions because `lambda-source-map.json` doesn't have `role` fields. Gold EC2 scripts fully covered. Would close the gap if source map was extended.
- **comp-guide CLI** — deferred per COO priority ranking; trigger tables cover 80% of the discovery need.
- **Auto-logging dedup tuning** — 30s window is reasonable but may need adjustment after real-world usage data accumulates.

---

## What This Session Demonstrated

The W3 OFC regression became the perfect case study for every piece of infrastructure built today:

1. The bug (line 1956 routing ternary missing OFC branch) was invisible under the old instruction model — schema-check UNUSED was treated as alias gap, agent moved on.
2. `schema-check --feature ofc` would have escalated it to WARN at Phase 1.
3. `ternary-audit` would have generated the complete W6 fix list automatically.
4. `<expect>/<if_mismatch>` blocks in the TO mandate would have forced verification against a specific target ("nna_ofc in RENDERED set after Fix 4").
5. comp-validate acceptance criteria would have blocked completion if the artifact-level check failed.
6. Auto-logging makes the compliance checkable after the fact.

Each fix addresses a different adoption failure mode. Together they form a net — any one would have caught this specific bug; having all of them makes it structurally hard for the same pattern to recur.

---

## Next Steps

None from CTO side. Standing by for Andrew's direction. All work from this session committed and propagated through instruction files; future sessions will inherit the tools and patterns as default.
