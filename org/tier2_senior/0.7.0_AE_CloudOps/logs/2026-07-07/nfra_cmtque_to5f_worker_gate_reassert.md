# 0.7.0_AE_CloudOps~B -- NFRA_CMTQUE TO-5F: worker-side commit-gate re-assert, all 4 reqs live-exercised

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Window: ~1610Z -> ~1635Z, continuing COO's DRIVE GO Wave-1 sequence (TO-4 -> ADHC_COMMITGATE
-> TO-5F).

## Summary

The commit-worker's own commit path only trusted the ENQUEUING AGENT's pre-run of
commit-gate.sh -- its own header comment called this out as "AGENT-SIDE fail-fast." A caller
that skipped its own pre-check (bug, or an enqueue path that doesn't follow convention) would
land non-compiling/undefined-name code with nothing structurally catching it, since git itself
has no opinion on Python syntax. Added a worker-side re-assert (step F2 in `cw_process`, after
the sensitive-leak gate, before the actual `git commit`) that reruns the same gate on the
request's own in-scope files. A gate failure classifies as a normal DETERMINISTIC rejection
(same class as sensitive-leak/owned-paths), never DLQ.

**Scope clarification (before touching anything):** requirement 4 ("legacy apparatus removed
from the queue path") is ambiguous between (a) delete safe-commit.sh's active mkdir-mutex/
contamination code NOW, while it's still the live default for 100% of traffic
(`SAFE_COMMIT_USE_QUEUE=0` until TO-6R's cutover), or (b) confirm the worker's OWN commit logic
never had that apparatus (D5, already retired). Asked COO before writing any code (Rule 22
grounding) -- confirmed (b). This commit does not touch `safe-commit.sh`.

## All 4 requirements -- exercised live, not asserted

1. **`--selftest` case-2 green.** Ran twice (before and after the change): round-trip +
   R4-attribution + msg-fidelity + sensitive-fail-closed + singleton + crash-recovery, all PASS.
2. **Owned-paths-lane rejection, exercised in the worker path.** Enqueued a `.github/workflows/`
   file as AE (BASE_EXEC lane) directly via `cq_enqueue`. The REAL git pre-commit hook (not a
   mock) rejected it: `ERROR: owned-paths lane violation(s) detected (block mode): ...
   lane=BASE_EXEC`. File correctly left staged (git's own default post-hook-failure behavior,
   not a worker concern) -- manually cleaned up.
3. **Non-compiling `.py` rejection, exercised in the worker path.** Enqueued a genuinely broken
   file directly (bypassing any agent-side pre-check). **First attempt caught a real bug**: the
   running daemon was the PRE-EDIT process (bash doesn't hot-reload a running script's body) --
   it committed the broken file (`63b98eda1`, later removed in `e0f9e5b4b`). Restarted the
   worker, re-ran with a fresh filename -> correctly REJECTED with `commit-gate blocked: ...
   SyntaxError: invalid syntax ...`. **That same exercise surfaced a second real gap**: the
   rejected file stayed staged in the index (no unstage-on-reject, unlike the existing
   sensitive-leak gate's `git reset -q HEAD --` pattern) -- fixed, re-verified clean (file
   correctly left unstaged after rejection).
4. **Legacy apparatus removed from the queue path.** Per COO's clarification: the worker's own
   commit logic (`cw_process`) never ported the mkdir-mutex + BASELINE/contamination detection
   in the first place -- confirmed by re-reading the D5 comment at the top of
   `.tools/commit-worker.sh` ("a single index-writer means `git diff --cached` can only ever
   show THIS worker's own in-scope stage -> the baseline/contamination apparatus is dead weight
   and is NOT ported"). `safe-commit.sh`'s legacy path (lines 196-339) is untouched -- it remains
   the live default until TO-6R's cutover.

**Bonus exercise (objective's own "prove... in the worker" language, the 07-02 near-miss
class):** a `session.har` under a `workflows/**/sources/` path (the exact directory-pathspec-
sweep shape `.owned-paths.yaml`'s workflows/** GOTCHA warns about) enqueued directly -> the
worker's sensitive-leak gate (shared `cg_sensitive_hits`, TO-5) correctly fail-closed:
`sensitive-leak blocked (1 file(s)): workflows/_to5f_exercise/sources/session.har`.

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `.tools/commit-gate.sh` (dogfood, ADHC_COMMITGATE's own new tool) | pre-commit gate on the edited commit-worker.sh | `OK: comp-shell scan clean (1 file(s) scanned, 0 findings)` + `OK: pre-commit gate clean for 1 file(s)` |
| `commit-worker.sh --selftest` | before/after regression | PASS both times (6 sub-checks each) |
| `comp-which/rail` | native Read/Grep for source reading (safe-commit.sh, commit-worker.sh, owned-paths.yaml); native aws/git for the live exercises | rail respected -- no comp-tool covers "read this shell script" or "enqueue a live commit-queue request" |

## Files Modified

- `.tools/commit-worker.sh` -- step (F2) worker-side commit-gate re-assert + unstage-on-reject.

## Blockers

None. Both real bugs found by the exercises (stale-daemon-code, unstage-on-reject gap) were
fixed and re-verified in this same window.

## Current State (zero-context handoff)

Worker daemon restarted + running the new code (confirmed via the exercises above, all four
running against the LIVE main-repo worker, not a throwaway). `SAFE_COMMIT_USE_QUEUE` is still 0
(dormant) -- this TO's work is real but not yet on the hot path; it activates when TO-6R flips
the cutover. All exercise artifacts (test files, dirs) cleaned up; only the intended
`commit-worker.sh` diff is committed (`fce73ef08`).

## Next Steps

- [2.0.0_SA_COO] TO-5F ready for close -- all 4 requirements + the objective's own workflows/
  near-miss re-proof, exercised live. RAVC incoming.
- Per the DRIVE sequence: NFRA_CMTQUE.TO-6R's load-test can proceed once COO schedules the
  quiet window (ADHC_COMMITGATE's precondition is already clear per the earlier RAVC).
