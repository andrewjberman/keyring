# Session log — safe-commit `-F` override read: self-test, and the premise the TO got wrong

**archetype:** VALIDATE
**Agent:** `0.8.0_AE_CloudComp` (base) · 2026-07-25

## Current State

Picked up while idle after respawn: `safe-commit-F-read-override-fix`, the one TO in my folder issued to
**base** and carrying `<status>pending</status>` (= active). P1, issued by `2.0.0_SA_COO` 2026-07-21, with a
`hard_gate` reading "ANDREW BROUGHT 0.8.0 ONLINE TO BUILD THIS NOW." It had been sitting four days.
**I committed nothing to the gate.** Phase-2 verification only, then reported.

### 1. The fix was already built, and uncommitted

`.tools/safe-commit.sh` already carried the additive `-F`/`--file` read at `:541-569` — a separate loop with
its own `_cf*` vars, inserted between a **byte-unchanged** `-m` loop and a **byte-unchanged** `CS_OVR`
extract, plus a normalization so a `# system-current-override:` line (the codebase's `# <marker>:`
convention, cf. `# never-override:` / `# rail-checked:`) is read identically to a plain trailer. It matches
the TO's scope. A prior session built it and was killed before verifying it.

### 2. THE FINDING — the TO's hard_gate premise is false

The TO says the change "goes LIVE only on CVO-confirm ... CTO gates the apply (**the live commit** of the
modified safe-commit.sh)." That treats *committing* as what makes it live. **It is not.**

Agents invoke `.tools/safe-commit.sh` — a path into the **working tree**. Bash reads the file from disk.
**The on-disk copy is the executing artifact; committing changes only whether it is RECORDED.**

Measured, with a positive control so a zero cannot be a broken retrieval:

| Probe | Result |
|---|---|
| `git show HEAD:.tools/safe-commit.sh \| grep -c '_cfk'` | **0** — committed copy has no fix |
| `grep -c '_cfk' .tools/safe-commit.sh` | **9** — on-disk copy has it |
| positive control: `CS_OVR` in the HEAD copy | **4** (579 lines) — retrieval works, so the 0 is a true absence |
| working-tree mtime | **2026-07-21T23:35:01Z** (~93h before this session) |

243 commits landed on 07-25 alone across 8 authors, every one through the on-disk file.

**Bounded honestly, because the alarming version is not the true one:** the *behavioral* delta only
materializes inside the `rc=2` branch — the `:530` trigger must match **and** `comp-system` must report
genuine drift. I checked: the gate returns **rc=0** right now, so the override read has most likely never
fired. The real four-day exposure was never "a wrong override got honored"; it is that a syntax error or a
`set -e` trip anywhere in those 29 added lines would have **wedged every agent's commit path**, and the
thing everyone believed was holding that risk — not committing — was holding nothing.

**Inverted: holding the commit did not reduce the risk, it removed the REVIEWABILITY while the code ran
anyway.** An uncommitted core-gate edit is the worst of both — live in effect, invisible in git, absent
from every reviewer's diff. Same shape as the deployed-vs-repo class, one layer down: here the working tree
*is* the deployment.

`org/modules/graph/boundary_report.py` sits in this same state right now (~E's edit, on disk, awaiting
CTO~Z's commit) — and `org/modules/graph/` is itself a trigger path for this very gate. Flagged to CTO~Z,
not adjudicated by me.

### 3. What I refused to do

Reaching the `rc=2` branch for real requires making `06_current_state` stale. That would arm a **blocking**
gate against every agent committing right now. I did not do it, and I would not have gained much: it tests
the trigger, not the read. Stated as a residual rather than quietly skipped.

## Blockers

None at me. Two dependencies are other people's: **CVO verify** before the change is recorded, and the
**CTO apply gate**. Routing question open — the TO names `3.0.0_SA_CVO` (main), who is not live; `CVO~Z` is.
I did not reassign it; asked CTO~Z and sent CVO~Z the package in parallel so no time is lost.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Apply gate + the routing call. My recommendation, stated as a recommendation: commit
   it promptly — framed as *making running code visible*, not *putting a change live*, since the current
   state is strictly worse than either alternative.
2. **[3.0.0_SA_CVO~Z or 3.0.0_SA_CVO]** Independent verify. Re-run the harness; do not accept my numbers.
   Attack M1 specifically — a coarse whole-loop mutant is the weakest part of my suite.
3. **[0.8.0_AE_CloudComp base]** Not touching the gate further. IDLE, event-driven.

## Compiler Tools

| Tool | Purpose this session | Result |
|---|---|---|
| `comp-system --gate --changed org/modules/graph/boundary_report.py` | Establish the gate's live rc before reasoning about the override branch | **rc=0** — "no comp-system _SOURCE in the changeset (gate n/a, open)". Confirms the override path is not naturally reachable, which is *why* the self-test could not use the real rc=2 branch |
| `fread_selftest.sh` (built this session, now at `deliverables/safe_commit_f_read/`) | The Phase-2 self-test | **13/13 PASS**, incl. mutant + injection controls |
| F-010 PreToolUse commit gate | Acceptance #2 third limb, "still denies -m with `$(`" | **CONFIRMED LIVE — it fired on me.** Unplanned but a genuine exercise |

**Secondary observation on F-010, surfaced not adjudicated:** it fired on a **`grep`**, not a commit — my
command was a read-only search whose *pattern* contained the literal substring. So the matcher fires on
**mentions**, which is the LD-0274 shape CLAUDE.md explicitly contrasts F-010 against. Bounded: it fails
**closed** and cost one retry, so it is friction, not a hole. CTO~Z's to price; I did not touch it.

### The self-test, and why it is shaped this way

Exercises the **real shipped bytes** — the block is extracted from the live file by **anchor** (`grep -n` on
two stable markers), never by hardcoded line numbers, which drift, and never retyped, which would test my
transcription instead of the gate.

| # | Case | Result |
|---|---|---|
| T1 | `-F` body with `# system-current-override:` | PASS — honored |
| T2 | `-F` body with a plain trailer (parity with `-m`) | PASS |
| T3 | `-F` body with **no** trailer | PASS — empty; commit still BLOCKs, exactly as today |
| T4 | `-m` trailer (**regression check**) | PASS — `-m` path unchanged |
| T5 | `-m` and `-F` together | PASS |
| T6 / T7 | `--file=<f>` and `--file <f>` forms | PASS |
| T8 | `-F <missing file>` | PASS — no crash, empty |
| T9 | `-F -` (stdin) skipped | PASS |
| T10 | `-F` body containing `$( )` | PASS — read literally |
| T11 | filesystem control: did it execute? | PASS — **no execution**; the "zero injection surface" claim exercised, not assumed |
| M1 | **MUTANT** with the `-F` loop surgically removed | PASS — does **not** read the override |
| M2 | MUTANT: `-m` still works | PASS — proves the fix is additive |

**M1 is the load-bearing one.** Without it, twelve green lines are unfalsifiable — an instrument that cannot
fail is not an instrument. M1 proves the suite discriminates, so T1 measures the fix rather than measuring
my optimism. I also flagged its weakness to CVO~Z unprompted: it deletes the *whole* loop, where a subtler
mutation (breaking only the comment-marker `sed`, or only the `--file=` form) would probe harder.

**Coverage denominator, stated rather than left to be discovered:** covers the `-m` loop, the `-F` loop, and
the `CS_OVR` extract. Does **not** cover the `:530` trigger predicate, the `rc=2` branch, the audit-log
write, or the reset/exit-1 block path.

A note on the harness's own hygiene: its first draft wrote scratch **inside** the repo, and `mktemp -d`
fails here because `/tmp` is not writable under the Cygwin harness (the same reason an earlier `-F` commit
attempt resolved to `C:/Program Files/Git/tmp/`). It now writes to a self-cleaning script-adjacent dir under
an `EXIT` trap; verified the tree is clean after a run. When the temp path broke, the harness printed
`FATAL: real block lacks the -F loop` and exited 9 rather than reporting green — it **fails closed**.

## Files Modified

- `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/safe_commit_f_read/fread_selftest.sh` (new, this lane's
  ownpath — re-runnable; resolves the repo root at run time via `git rev-parse --show-toplevel`, cf. the
  `fbc91c6e28` install-time-path lesson)
- `org/tier2_senior/0.8.0_AE_CloudComp/logs/2026-07-25/safe_commit_f_read_override_selftest.md` (this log)

**`.tools/safe-commit.sh` is NOT modified by me and NOT committed by me** — it remains as I found it, and
the apply is CTO~Z's gate.
