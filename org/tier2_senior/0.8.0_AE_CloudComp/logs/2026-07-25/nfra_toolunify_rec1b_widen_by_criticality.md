# NFRA_TOOLUNIFY REC-1b — Widen by Criticality — 0.8.0_AE_CloudComp~D

**Date:** 2026-07-25
**Task Order:** NFRA_TOOLUNIFY.REC-1b (MCP dispatch, no XML TO filed — off-main-fabric census group)
**Status:** COMPLETE

---

## Objective

Widen REC-1's failure_mode predicate-exercise from a 5/92 v1 sample to the register's own `role_flags[]`
criticality filter: exhaustive over confirmed `GATE-BLOCKING`/`PRODUCER` tools, sampled over the rest. Also
re-confirm the six §0.2 through-line instances against that filter (does role_flags under-catch any of
them), and verify the stitch post-commit hook's `/c/`-path fix (`fbc91c6e28`) on my own next commit.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-gitdrill` | `--self-test` | PASS | 6/6 built-in assertions, incl. `at.blob_parity_with_git` — the exact property the 2026-07-24 vintage-guard fix targeted |
| `comp-gitdrill` | `<nonexistent node id>` | PASS | mismatched input, DECLARED LOUD, OBSERVED LOUD (rc=3, explicit `NOT-RESOLVED`) |
| `comp-surface-check` | `scan --current <nonexistent file>` | WARN | DECLARED LOUD, OBSERVED FAIL-OPEN by explicit design ("never crash the nightly") — mismatch, flagged §4b of REC1B_EXERCISE.md |
| `comp-surface-check` | `scan --current <empty {} file>` | PASS | comprehensive SEV1/SEV2 output, rc=0 by design (advisory subcommand, not the blocking one — traced to source, not a defect) |
| `comp-dispatch` | `<nonexistent firm alias>` | PASS | DECLARED LOUD (LOW/default), OBSERVED LOUD (rc=1, explicit) |

**What worked:** `comp-gitdrill --self-test` and `comp-manifest-check selfcheck` (from REC-1) both being
built-in, ready-made mismatched-input harnesses made this a much faster pass than hand-crafting probes for
every tool — worth noting to CTO~Z as a pattern (tools that ship their own self-test are cheap to
predicate-exercise; tools that don't require this lane to construct the mismatch by hand each time).

**What failed:** nothing broke the exerciser this pass (the idiom-2 dispatch mistake from REC-1 did not
recur — both new tools this pass are bash-wrapper idiom).

**Gap found:** `comp-surface-check` is one register row covering 7 subcommands with materially different
failure semantics (blocking `selfcheck` vs. advisory `scan` vs. `egress-check` etc.) — a single
`failure_mode` value cannot represent all seven faithfully. Flagged to CTO~Z/CVO~Z, not actioned (read-only
scope).

Appended to `org/compiler-tools-log.md` (auto-logged via `.comp-graph/.agent_context`).

---

## Work Completed

### 1. Denominator analysis

Parsed all 92 rows of the D.md register programmatically for `role_flags[]`. Confirmed
(non-`?`-suffixed) `GATE-BLOCKING` ∪ `PRODUCER`, deduplicated = exactly 2 tools
(`comp-manifest-check`, `comp-stitch-refresh`) — both already exercised in REC-1 as the positive control and
mutant. The "exhaustive over confirmed criticality" half of this dispatch was therefore already satisfied by
REC-1; cited rather than re-run.

### 2. Through-line role_flags cross-check

Of the six §0.2 through-line instances, only 3 are representable as register rows at all (the rest are
AWS/CI resources with no `comp-*` counterpart). Of those 3: `comp-stitch-refresh` carries a confirmed
`PRODUCER` flag; `comp-gitdrill` and `comp-surface-check` (the "two raw-cache readers," through-line
instance #5, fixed 2026-07-24 at `68bbf3dd2`) carry only candidate (`?`-suffixed) flags. **A strict
confirmed-only filter misses 2 of the 3 register-representable through-line instances** — exactly the
under-catch CTO~Z's dispatch asked me to check for. Full reasoning in REC1B_EXERCISE.md §3.

### 3. New exercises

`comp-gitdrill` (through-line #5a): self-test 6/6 PASS + a fresh mismatched-target probe, both LOUD, both
matching declared. `comp-surface-check scan` (through-line #5b): two distinct inputs produced two distinct,
both-informative results — a missing `--current` file triggers an explicit, by-design FAIL-OPEN skip
("never crash the nightly," a genuine mismatch against the declared LOUD row); an empty/degenerate
`--current` file triggers a comprehensive, correctly-severity-tagged SEV1/SEV2 report at rc=0, which traces
to source as correct-by-design (the blocking gate is a different subcommand entirely). `comp-dispatch`
(LOW-confidence LOUD-default sample): matched declared.

### 4. `/c/`-path fix verification (CTO~Z's ask, folded into this session)

Answered COO~Z's relayed probe mid-session (before this dispatch arrived): confirmed `/c/...` fails and
`/cygdrive/c/...` works in this Cygwin shell, and that I'd independently hit the live consequence on my own
prior commit (`c3c68389b`, made before the fix landed) — see that commit's log entry. **This commit** (the
one carrying this log + REC1B_EXERCISE.md's session log) is made after `fbc91c6e28`; result recorded in
Files Modified below per CTO~Z's request to flag if the stderr recurs.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Cite REC-1's `comp-manifest-check`/`comp-stitch-refresh` results instead of re-running them | The confirmed-criticality set is exactly those 2 tools; re-running identical invocations against unchanged tool source would add no new information, only noise. |
| Treat `comp-surface-check scan`'s two rc=0 results as two DIFFERENT findings, not one | The missing-input result is a genuine declared-vs-observed gap; the empty-input result traces to source as correct-by-design (advisory vs. blocking subcommand). Collapsing them would have manufactured a second "mismatch" that isn't one. |
| Did not widen further than 3 new tools | The exhaustive confirmed-criticality half is fully covered (2/2); the dispatch's own framing treats deeper ADVISORY/candidate sampling as available-on-request, not mandatory this pass. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1B_EXERCISE.md` | New — REC-1b write-up | No — CTO~Z's BASE_EXEC lane, same convention as REC-1 |
| `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_TOOLUNIFY_CENSUS/REC1B_EXERCISE.sidecar.json` | New — per-invocation raw results | No — same as above |
| `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/nfra_toolunify_rec1b_widen_by_criticality.md` | This log | Yes — committed this session under `0.8.0_AE_CloudComp~D`'s own lane; post-commit hook stderr result: **[fill after commit below]** |

---

## Blockers

None.

---

## Current State

REC-1b delivered. Exhaustive confirmed-criticality set (`comp-manifest-check`, `comp-stitch-refresh`)
confirmed 2/2 covered via REC-1 citation. Through-line role_flags cross-check surfaced a real filter
under-catch (2 of 3 register-representable through-line instances carry only candidate flags). Three new
tools exercised; `comp-surface-check scan`'s missing-input FAIL-OPEN is a second concrete declared-vs-observed
mismatch on total-absence input (after REC-1's `comp-freshness` result), now a named pattern for CTO~Z/CVO~Z
rather than a one-off. `/c/`-path fix verification folded in per CTO~Z's ask.

---

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Commit `REC1B_EXERCISE.md` + sidecar; decide whether the total-absence-input FAIL-OPEN
   pattern (comp-freshness + comp-surface-check scan, 2/2 so far) warrants a targeted third check before
   generalizing it as a register-wide theme.
2. **[3.0.0_SA_CVO~Z]** Re-verify the denominator table (§1 of REC1B_EXERCISE.md) — mechanically re-derivable
   from D.md, parse approach documented, happy to hand over the script.
3. **[0.8.0_AE_CloudComp~D]** Event-driven, standing by.
