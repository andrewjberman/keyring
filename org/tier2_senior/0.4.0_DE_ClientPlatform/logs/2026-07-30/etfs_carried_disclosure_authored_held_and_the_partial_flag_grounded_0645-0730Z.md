# The disclosure was the easy half: `partial` detects a late start and nothing else — 0.4.0_DE_ClientPlatform

**archetype:** MIXED (DIAGNOSE + IMPLEMENT + VALIDATE)
**Date:** 2026-07-30 (0645-0730Z)
**Task Order:** ad-hoc — COO dispatch `20260730T064748Z` (ETFS AUG-1 clock)
**Status:** IN PROGRESS — remedy READY BUT UNLANDED, held pending Andrew
**Workspace CLOUD commits:** `75c66b8733` (patch backup) -> `7d7af02155` (finding record)
**Portal DEV commits:** none — no portal work this session

---

## Objective

Author and exercise a per-partner, computed-at-run-time carried-forward disclosure line in
`data/etfs/scripts/presentation/render_month_end.py`, so the per-partner CSVs attached to the
2026-08-01 14:00Z month-end email stop being silently authoritative about carried days on the
ETFS_AVGCAP partner-rebate basis. Selected by git truth (10 of 11 commits on that file are mine).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-grep | `comp-grep "opaletfs_"` | PASS | 19 matches / 10 files, **scanned 24415 of 26410 in scope**. Found the only real consumer (`etfs-reports-orchestrator`) plus ~A's staged rehearsal. Replaced what would have been a blind raw grep. |
| comp-grep | `comp-grep "partial" data/etfs` | PASS | 12 matches / 1 file, scanned 7 of 7. Located `avgcap_monthly_average.py` as the sole `partial` producer — this is what let me ground the mechanism instead of repeating it from memory. |
| comp-glob | `comp-glob "**/*avgcap*"` | PASS | 11 files; confirmed the gold producer + the PRD/brief set around it. |
| commit-gate | `.tools/commit-gate.sh <file>` | PASS | py_compile + ds-precommit + ruff, clean on the edited renderer. |
| safe-commit | `safe-commit.sh --author ... -- <path>` x2 | PASS | surface-check OK (6 surfaces, no critical touched); risk-reflex CLEAN, **denominator printed: 1 file vs 1484 danger nodes**. |
| comp-transform / comp-blast / comp-cache | — | SKIPPED | The DE role minimums are portal-component-scoped. This session touched **zero** portal files: the work was a python renderer in `data/etfs/`, and its only consumer is a Lambda that attaches bytes without parsing. `comp-blast` was not run because nothing was deleted. |

**What worked:** `comp-grep`'s printed denominator is the reason I trusted the consumer census — "19 in 10
files, scanned 24415 of 26410" is a claim I can size; a bare grep hit-list is not. Its SYSTEMS CONTEXT
footer pointed me at the orchestrator as a *lambda source* rather than a text match, which is what made me
go read the attach path instead of assuming it.

**What failed:** nothing produced a wrong answer.

**Gap found:** none in the tools. **One stale record:** `org/ref/SESSION_LOG_STANDARD.md:36` still says
*"Append one line to org/compiler-tools-log.md after writing this section."* That auto-append was RETIRED
Andrew-direct 2026-07-29 and CLAUDE.md/XXX.md both now say **do not append to or commit that file**. I did
not append. Flagging rather than editing — it is not my document.

---

## Work Completed

### 1. The dispatch's stated mechanism was false, and I caught it independently

COO's dispatch said *"`_month_cap` computes each partner's last real in-month date (`in_month[-1]`)"* and
to read `cap`. Source says otherwise (`render_month_end.py:164-175`): for a COMPLETE month it early-returns
`m_end` **unconditionally**, never computing `in_month` at all.

Exercised rather than argued, using June (already complete, so the real branch runs today):

```
CASE A: COMPLETE month (m_end < today) -- THE BRANCH THAT RUNS 2026-08-01
  inflection-like (holds m_end)   in_month[-1]=2026-06-30   _month_cap -> 2026-06-30   MATCH
  cottonwood-like (1 short)       in_month[-1]=2026-06-29   _month_cap -> 2026-06-30   *** MISMATCH ***
  49F-like (3 short)              in_month[-1]=2026-06-27   _month_cap -> 2026-06-30   *** MISMATCH ***
CASE B: IN-PROGRESS month  (positive control)
  in-progress, 2 days short       in_month[-1]=2026-07-28   _month_cap -> 2026-07-28   MATCH
```

CASE B is load-bearing: it proves the harness *can* print MATCH, so the CASE-A mismatches are a real branch
difference rather than a comparison that cannot pass. A disclosure built on `cap` would have printed
"data through 2026-07-31" for a partner whose tail is carried — **certifying carried days as real** on a
payment basis. COO sent a self-correction 12 minutes after the dispatch; I had the result before it landed.

### 2. The change (UNLANDED)

`_carried_disclosure(in_month, cap, m_start)` — derived from `in_month[-1]`, never `cap`. Emits the last
real slice date, the carried tail span, **and** the interior carry count. Appended behind a blank row after
the ETF rows so rows 2..5 stay the grid and Excel `AVERAGE()` still reproduces the deck average.

**Fail-safe by construction.** `main():644` calls `write_month_csvs` unconditionally, no try/except,
upstream of every S3 upload, under `set -e` — so a raise here loses the PDF too. Wrapped so it degrades
but cannot throw. Hazard identified by `0.7.0_AE_CloudOps~A`.

### 3. Exercised — three runs plus a mutant

Zero S3 writes **enforced**, not inferred: `put_object`/`upload_file`/`upload_fileobj`/`copy_object`/
`delete_object` replaced with raising stubs and the guard **self-tested** before any run.

RUN-A (July, clock forced to 2026-08-01 — the Saturday branch), real data:

```
49financial  last_real=2026-07-28  cap=2026-07-31  -> "Dates 2026-07-29 through 2026-07-31 ... 12 of 31"
inflection   last_real=2026-07-29  cap=2026-07-31  -> "Dates 2026-07-30 through 2026-07-31 ... 16 of 31"
cottonwood   last_real=2026-07-27  cap=2026-07-31  -> "Dates 2026-07-28 through 2026-07-31 ... 14 of 31"
```

**MUTANT:** injected a `ValueError` into `_carried_disclosure`; all 3 CSVs still wrote with `Date` header
and DIVZ/IDVZ/PFDE/PFOE rows at full column counts, rc=0. Reverted, confirmed the line returns — so the
test distinguishes the two states. A guard never exercised under its own fault is not a guard.

**CSV bytes verified by parse-back** (I had asserted the shape structurally, then went and looked):
7 rows; rows 0-4 = 31 cells each; row 5 blank; row 6 exactly 1 properly-quoted cell.

### 4. I broke COO's acceptance gate with my own negative control

COO's gate: *"three different outcomes = pass; all three identical = the bug."* I built a negative control
expecting to **confirm** it and hardcoded that prediction. The harness printed `>>> UNEXPECTED: not all
identical` — the masked in-progress branch produced **three distinct sentences** and would have PASSED.

They differ on the leading date and my interior count; **the tail clause is byte-identical across all
three**. My own enrichment was half the reason the gate passed. Replacement gate, adopted by COO:
(1) the complete-month branch was actually taken; (2) the **tail clause** differs and at least one partner
has `cap != last_real`.

I corrected COO's write-up of this: they had recorded it as foresight and propagated that to ~C and MSTR.
The truthful version is that I wrote down a falsifiable prediction and the instrument contradicted me —
which is teachable, where foresight is not.

### 5. The interior-coverage finding, and grounding it made it worse

Census of July no-slice dates surfaced **inflection missing 10 weekdays**, including contiguous runs
07-13/14/15 and 07-20/21/22/23. ~A independently re-derived on a trading-day predicate (12/20 = 60%,
worst of three) and retracted their own "12/12 HIGH CONFIDENCE".

Then I grounded the mechanism at source rather than repeating the received wording
(`avgcap_monthly_average.py:187-205`): `carried` appends one entry per **calendar** day from
`first_written` onward, real or carried, so `covered_days` is a function of `first_written` alone and

> **`partial == (first_written > window_start)`. It detects a LATE START and nothing else.**

**Production artifact `monthly/2026-06.json`, 49financial DIVZ: `written_days=17`,
`calendar_days_covered=30`, `partial=FALSE`.** Seventeen real days in a thirty-day billing window, already
shipped, flagged complete. Cottonwood's June `window.partial=True` is a trap — it trips the onboarding-clock
disjunct at `:219`, not coverage.

**So interior and tail are ONE defect, not two:** a dead tail also leaves `first_written` untouched.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Disclose from `in_month[-1]`, never `cap` | `cap` is the billing window end and carries no information about real data on a complete month. |
| Include the interior carry count | A tail-only line is TRUE AND MISLEADING: it would say "no dates at the end are carried" for inflection while ~9 interior days carry in the same document. COO ruled KEEP. |
| Flag the widened spec instead of shipping it silently | It was COO's spec; a one-line revert was offered. Widening a payment-basis artifact unasked is not mine to do. |
| Wrap the disclosure so it cannot throw | Non-delivery of the month-end report is worse than a missing disclosure line. |
| Report the gate defect rather than the true "3 distinct = PASS" | The passing result was correct and meaningless. |
| Do NOT chase the cause of inflection's gaps | Producer-side, outside dispatch. Recorded as NOT established. |
| Commit the patch backup, not the remedy | Protects a payment-basis diff in a shared worktree without touching the hold. |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `data/etfs/scripts/presentation/render_month_end.py` | `_carried_disclosure()` + fail-safe emission in `write_month_csvs` | **No — HELD UNLANDED**, ` M` unstaged, by COO constraint 2 |
| `org/.../deliverables/carried_disclosure_20260730.patch` | Patch backup of the above | Yes — `75c66b8733` |
| `org/.../deliverables/ETFS_AVGCAP_INTERIOR_COVERAGE_FINDING_20260730.md` | Standing record for Andrew question (b) | Yes — `7d7af02155` |

`_month_cap` **untouched** — verifiable on the diff; it contains no change at or near `:164-175`.

---

## Blockers

- **BLOCKED on `2.0.0_SA_COO`** (carrying `1.0.0_SA_CTO~C`): land/no-land word on the held disclosure diff.
  Ship/no-ship is Andrew's — it is his billing convention and it is dollar-bearing.
  **Evidence:** COO `20260730T070105Z` — *"STILL UNLANDED. Ship/no-ship is Andrew's ... Hold."*
  Not assumption-based: explicit, evidence-cited, named owner.

---

## Current State

The remedy is complete and idle, not in progress: `_carried_disclosure()` sits **unstaged** in
`data/etfs/scripts/presentation/render_month_end.py`, backed up as a reverse-apply-verified patch at
`75c66b8733`, gate-clean, exercised against real data on the actual Aug-1 branch with a self-tested
zero-S3-write guard, and mutant-proven against the one failure mode that could cost Saturday's PDF.
`_month_cap` is untouched. The larger open item is `7d7af02155`: AVGCAP's `partial` flag reduces to
`first_written > window_start`, which means it never reported 49financial's already-shipped June artifact
at 17 real days in a 30-day window — the interior and the recorded carried-tail defect are the same defect.
Inflection projects 45-52% of its Aug-1 billing window carried against a 29% floor; that magnitude is with
COO for ~C ahead of the 14:00Z fire.

---

## Next Steps

1. **[2.0.0_SA_COO / 1.0.0_SA_CTO~C]** land/no-land on the held diff — on GO it goes via `safe-commit.sh`
   under my author line in one motion; the patch is the recovery path if the tree is swept.
2. **[Andrew]** question (b): whether a ~40-50%-carried month is a valid rebate basis at all, disclosed or
   not. Evidence base is `7d7af02155`. **No remedy proposed — deliberately.**
3. **[0.7.0_AE_CloudOps~A]** 49F watch `bbfrc8wl9` verdict — narrows the printed span only; does not gate.
4. **[0.4.0_DE_ClientPlatform]** on GO: land, then re-exercise post-land to confirm the committed bytes
   behave as the working-tree bytes did. **A landed change is not a verified change.**
5. **[0.4.0_DE_ClientPlatform]** flag to whoever owns `org/ref/SESSION_LOG_STANDARD.md`: line 36 still
   directs agents to append to the retired `org/compiler-tools-log.md`.
