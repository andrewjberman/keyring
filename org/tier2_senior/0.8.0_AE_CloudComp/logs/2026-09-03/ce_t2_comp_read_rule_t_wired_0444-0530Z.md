# TO-CE-T-2 -- comp-read Rule T wiring, the s.4 audit deliverable, and the 4.3 four-case test -- 0.8.0_AE_CloudComp~A

**Date:** 2026-09-03
**Task Order:** NFRA_COMPEFFICACY.TO-CE-T-2.comp-read-s4-audit
**Status:** COMPLETE (pending CVO grade + MSTR push)

---

## Objective

Deliver the s.4 per-tool audit for `comp-read` (row T-2, cell CE-t-2), the 4.3 four-case test
against the ratified answer-state enum, and the one code change this cell owed: wire the shared
`.tools/_compbudget.py` carrier onto comp-read's one timeout-carrying subprocess (the self-report
telemetry sink, `:1027ish`, hard-coded `timeout=20`), mirroring the reference application
(`.tools/comp-find`, CE-t-1).

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-read | `.tools/comp-read --for "where a caller's ceiling would enter..."` + `--enumerate 'timeout=\|subprocess\.run\|PAGE '` (before write, and again post-edit) | PASS | 4 hits at cut (per the TO's own measurement); 9 hits after -- the growth is the new Rule T code + docstring, located exactly |
| commit-gate.sh | on `.tools/comp-read`, `.tools/tests/test_comp_read_enumerate.py` | PASS | clean, 2 of 2 files, twice (before and after the Clock-placement refinement) |
| comp-passcraft | `recon comp-read` | PASS | MOVES 1-3 auto-observed; 4-8 hand-run in the deliverable |
| comp-schedule | preflight (per the TO's own `<preflight>` block) | RUN | 0 armed gates named this project/tool at cut |
| comp-system | regenerate `06_current_state` (a commit-gate dependency, `comp-system-gate` blocked on stale state) | PASS | regenerated + staged alongside the code commit |
| proof-of-spec-check.py | on this instance | see below | validated before the `complete` flip |

**What worked:** comp-find's own T-1 rework was a precise template -- the `--budget`/env/default
carrier, the disclosure-line helpers, and the error-message wording all transplanted onto
comp-read's single-subprocess case with only the unit concept (`telemetry_call`, N=1) needing to
be reasoned through fresh.

**What failed, found, and fixed BEFORE commit (both caught by this seat's own exercise, not by a
reviewer):**
1. **Clock placement.** The first draft created the `Clock` inside `_self_report()`, adjacent to
   its own `remaining()` check -- this makes the pre-flight SKIP branch structurally unreachable
   (remaining() checked immediately after `Clock()` is always still ~budget_s). Moved the Clock
   into `main()`, started before any read/enumerate/hud work, so `remaining()` at self-report time
   reflects the whole run's elapsed time. Verified both BUDGET REACHED sub-branches now fire on
   the real binary (fast read -> subprocess TimeoutExpired; slower read -> pre-flight SKIP).
2. **`--hud` silence regression.** `--hud`'s own docstring is explicit that a silent run must emit
   ZERO bytes. An unconditional trailing Rule T print from `_self_report()` (which fires for every
   mode, since it runs in `__main__` after `main()` returns regardless of which branch fired)
   broke that: measured 0 -> 85 bytes on a genuinely clean fixture. Fixed by suppressing the
   PRINTED line (not the underlying budgeted subprocess call) whenever `hud_mode` was set,
   tracked via `_BUDGET_STATE["quiet"]`. Re-measured 0 bytes after the fix.

**Gap found, not fixed (BOUNDS: read semantics do not change under this TO):** comp-read has no
NOT_APPLICABLE voice for `--at LINE` beyond the file's own line range -- silently indistinguishable
from omitting `--at` entirely (F1 in the deliverable). Carried forward, not this cell's fix.

---

## Work Completed

### 1. Rule T wiring, commit `f4eb799c2b`

`--budget` CLI flag (carrier: flag > env `COMP_BUDGET_S` > default 90s via `.tools/_compbudget.py`,
consumed not edited); the self-report subprocess's `:1030` `timeout=20` now derives from
`clock.remaining()`; `--help` discloses the carrier and the non-application (no corpus-width loop,
so BUDGET REACHED needs a deliberately tiny `--budget` to reach); the pre-Rule-T fixed 20s ceiling
is kept as the declared fallback for the one path that never resolves a budget (`--help`/`-h`,
zero read-work). Regenerated `infra/system/06_current_state.{md,json}` (commit-gate's
`comp-system-gate` blocked the first attempt on stale state; not a rule-bank touch, so the regen
path applied, no override needed) and staged them into the same commit.

### 2. Battery: two new arms, exceeding the one owed

`.tools/tests/test_comp_read_enumerate.py`: the pre-existing 8 arms are byte-for-byte unchanged
(confirmed direct and under `pytest -q`, twice, across this cell's edits, including
CONSUMER-INTACT -- `comp-adversary --self-test` still `PASS 5/5` with comp-read's new trailing
Rule T line embedded verbatim in its stage-4 packet). Added BUDGET-CARRIER (the real production
binary: default budget -> WITHIN BUDGET, `--budget 0.001` -> BUDGET REACHED, no mutant needed) and
MUTANT-BUDGET (a build whose `_compbudget.resolve_budget(budget_flag)` call is neutered to
`resolve_budget(None)` goes RED against BUDGET-CARRIER's own predicate). 10/10 PASS, direct and
under pytest. Directory-grain collection unchanged: still aborts at
`test_fabric_check_classify.py:76` (CTO's F6, not this cell's), 25 tests collected before the
abort.

### 3. Deliverable + proof instance

`org/missions/D11/NFRA/NFRA_COMPEFFICACY/deliverables/0.8.0_AE_CloudComp~A/comp-read.result.md`
(the T-16/T-1 shape, all 31 s.4 fields present or explicitly ABSENT with a reason) and its proof
instance, validated against `PROOF_OF_SPEC.schema.json` and `.tools/proof-of-spec-check.py` before
the `<status>` complete flip, which this seat commits itself.

---

## Acceptance (summary; full evidence in the deliverable + proof instance)

T2-AC1 (parses, 4.1 from the engine) PASS · T2-AC2 (four distinguishable planted cases, one
finding F1) PASS · T2-AC3 (Rule T form, side-by-side pair, non-application stated) PASS ·
T2-AC4 (battery 10/10, both grains stated) PASS · T2-AC5 (the `--enumerate`-writes-no-rail-row
finding carried, owner named) PASS · T2-AC6 (push state measured at report, not asserted).

---

## Push State

Measured in the commit report to `2.0.0_SA_COO`, not asserted here.
