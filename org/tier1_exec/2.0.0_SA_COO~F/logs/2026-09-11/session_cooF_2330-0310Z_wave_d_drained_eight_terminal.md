# IRPT_FNTEND round 1: wave D drained, eight of eleven terminal, every tab on DEV -- 2.0.0_SA_COO~F

**Date:** 2026-09-11
**Task Order:** IRPT_FNTEND L7 drains (FE-s-8, FE-s-3, FE-s-6, FE-s-7, FE-s-5); FE-s-9 in flight
**Status:** IN PROGRESS
**archetype:** COORDINATE
**Workspace CLOUD commits (LOCAL):** `5fe38acee7` `b3faaeb599` `b435858a61` `7f61c1a102` `883bfdff53` `99a12674be` `37bc4e36b7` `332f10e458` `e13fa64e11`
**Portal DEV commits (LOCAL):** `4fbbd1c4` `65a37017` `8fb4f15a` `d161a071` `5b959f63`

---

## Objective

Drain five more terminal orders, act as disarm owner on every ARMED row they filed, keep three parallel slots fed through the round's widest wave, and carry each cut defect of this seat's own faces as an amendment to the next order in the same slot.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | re-run by this seat on five instances | PASS | VALID rc=0 each |
| bun test / typecheck | re-run by this seat in each worker's portal worktree | PASS | 8/8, 19/19 (+1 skip), 19/19, 32/32, 20/20; the FE-s-3 set under the alias mapping read 16 pass 2 fail, the regression W1-S7 names |
| bun test (DEV whole set) | after each portal drain | PARTIAL | 164/164 at d161a071; 184 tests, 2 fail at 5b959f63 (dropdown-class under real alias resolution; repair granted to FE-s-9) |
| safe-merge | workspace x5, portal x5 | PASS | three channel conflicts resolved as the ordered union by `union_channel.py` (existing rows byte-identical, new rows appended); two refusals were correct: another seat's staged ledger files, then another seat's open merge |
| never-rules gate | one compound call | BLOCKED (correct) | a `-m` subject and a `$( )` in the same call; split into calls with no substitution beside a subject |
| Get-CimInstance Win32_Process | vite processes under removed worktrees | PASS | found and stopped 17632 (FE-s-4) and 23456 (FE-s-7); a `netstat | findstr` with a colon pattern had reported none -- the process list by command line is the instrument that sees them |

**What worked:** re-running the estate's checker and two or three criteria per order from the worker's own worktree before any merge; the union resolver as a file rather than an inline heredoc; committing a two-file amendment through `--only` while foreign files stayed staged.
**What failed:** an early inline heredoc failed the shell parser; a `-m` beside `$( )` tripped the never-rules gate for the whole call; the FE-s-3 face said each tab body is a mount point and the worker built a shell with no seam, so two later tabs were unreachable.
**Gap found:** the tab shell had no mount seam; the root tsconfig carried no path alias for Bun; the export bundle contract carries references, not payloads; recharts renders empty under static markup; `CategoryViewTree` is bound to the AUM contract and drops non-positive amounts. Each is a row with a named disarm act or an L10 carry.

---

## Work Completed

### 1. Drains
FE-s-8 (ws `5fe38acee7`, portal `4fbbd1c4`), FE-s-3 (`b435858a61`, `65a37017`), FE-s-6 (`883bfdff53`, `8fb4f15a`), FE-s-7 (`99a12674be`, `d161a071`), FE-s-5 (`37bc4e36b7`, `5b959f63`). Eight of eleven orders terminal. Every tab, the render package, the narrative page and the alias mapping are on portal DEV.

### 2. Rows and disarm acts (channel: 27 rows)
- W2-S6 (narrative page unmounted; slot owner outside FE-s-8's grant) -> FE-s-9 mounts it behind `includeNarrative` (F9-AC10); seat row S6.
- W1-S5 (Bun ignores the referenced tsconfig's paths) -> FE-s-5 added the mapping to the root tsconfig (F5-AC9 PASS); seat row S7.
- W1-S6 (stale dev servers) -> swept at every drain by command line; seat row S8.
- W3-S1, W4-S1 (tab shell has no mount seam; Analysis and Holdings tabs unreachable) -> FE-s-10 mounts both (F10-AC10); seat row S9.
- W1-S7 (the alias mapping regresses FE-s-3's dropdown test) -> FE-s-9 removes the mock workaround and asserts the real markup (F9-AC11); seat row S10.
- INERT and carried to L10: W3-S2, W4-S2 (contract fields and the CategoryViewTree reuse finding), W2-S5, W1-S3, W2-S1.

### 3. FE-s-9 spawned
Slot ~1, `/c/tmp/wk-irpt_fntend-1-5-fe-s-9`, from ws `e31ad6b8a1` and portal `5b959f63`, with the three amendments (bundle resolution, narrative wiring, dropdown test repair) in its face. Spawned before the three wave-D record drains landed, because the hold was a foreign seat's staged files on the shared index and every dependency was terminal with a valid instance and its code on DEV.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Mounting the two unreachable tabs goes to FE-s-10, not FE-s-9 | FE-s-10 already holds `tabs/` and depends on every tab cell; FE-s-9 does not depend on FE-s-7 |
| The dropdown-test repair goes to FE-s-9 | the next order on the same slot; DEV stays red for one order rather than a hotfix commit outside any order |
| FE-s-9 spawned ahead of its dependencies' record drains | the hold was on the record side only and belonged to another seat; the code and the valid instances were in place |
| Stale-server sweep by process command line, never by port | the port-keyed check missed three live servers |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../task-orders/IRPT_FNTEND.TO-FE-s-9.export-options-preview.md` | amendments: bundle resolution, narrative wiring, dropdown test repair | `b3faaeb599`, `332f10e458` |
| `.../task-orders/IRPT_FNTEND.TO-FE-s-10.global-view.md` | amendment: mount both tabs | `332f10e458` |
| `.../task-orders/IRPT_FNTEND.TO-FE-s-5.reporting-tab.md`, `TO-FE-s-8.*` | amendments per W1-S5, W2-S4 | `7f61c1a102`, `531ff06aab` |
| `.../surprise-channel/investigations/INVESTIGATION_v1.md` | 27 rows | through `e13fa64e11` |
| `portal/src/App.tsx` (portal) | marker repair after a mis-resolved merge | `b86e6aa2` |

---

## Blockers

None at this seat. FE-s-9 is executing; FE-s-10 and FE-s-11 follow on the same slot.

---

## Current State

IRPT_FNTEND: 8 of 11 orders terminal and drained in both repos; FE-s-9 executing on slot ~1; FE-s-10 (Global view, plus mounting the Analysis and Holdings tabs) and FE-s-11 (census) remain. Portal DEV `5b959f63` typechecks; its Investor Reporting test set reads 184 tests with the 2 dropdown-class failures FE-s-9 repairs. Channel 27 rows; ARMED rows each carry a granted disarm act, and W2-S3 (Lato) is a pending input for Andrew. All commits LOCAL in both repos; the workspace `portal` gitlink still points at `5907cbca`.

---

## Next Steps

1. **Drain FE-s-9**, then cut and spawn FE-s-10 (tab mounting + Global view), then FE-s-11 (census).
2. **L10** -- ONE message to `1.0.0_SA_CTO` after FE-s-11: the CVO watermark against 27+ rows; W2-S3 as an open call (Lato font); W2-S2, W2-S6, W3-S2 as contract-inventory questions for the counterpart (ExportBundle payloads, NarrativePacket fields, AnalysisRequest/ReportSection fields); W2-S4 (browser runtime) for the counterpart's worker cell; W4-S2 (CategoryViewTree not fit for holdings) and W2-S5 (ui-smoke query-string LOC) as reuse and instrument notes; the gitlink pointer.
