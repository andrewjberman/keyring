# ws-charter cycle — 2026-05-29 2138Z

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, COORDINATE

**CLASS:** FIX (landed MSTR-approved infra: safe-commit commit-mutex v2)

## Inbox / direction (this tick)
- MSTR ARCH RULING v2 (mid-tick, via heartbeat): APPROVED stage-inside-lock + baseline-diff guard reframe + mtime stale-break; land CLOUD + verify + port. (Superseded the CLEAN-SWEEP this tick started as.)

## Actions (the commit-mutex v2 landing)
1. **safe-commit.sh v2** (a62305eed): (1) stage-inside-lock — `git add -f -- <pathspec>` INSIDE the mutex (callers stop pre-adding; collapses add->commit window to zero); (2) baseline-diff guard — contamination = staged-now \ baseline \ pathspec (peers' pre-staged files ignored; `--only` can't commit them anyway); (3) mtime stale-break added to lock loop (PID-reuse-safe; age>=60s reclaim alongside dead-PID).
2. **CONCURRENT-COMMIT VERIFICATION PASSED** — staged a foreign file (simulated peer out-of-band add = the exact 2x-false-abort race from earlier today), ran safe-commit on my file: committed ONLY mine, foreign neither aborted-on nor swept in, left staged for owner. Then committed CLAUDE.md+safe-commit.sh together WITH NO pre-git-add (28e2d3482) — stage-inside-lock proven for multi-file tracked commit.
3. **CLAUDE.md Rule 14a + safe-commit help** (28e2d3482): new contract documented — callers do NOT pre-`git add`.
4. **record-terraform-deploy.sh (c) confirmed**: calls safe-commit with explicit `-- "${PATHSPEC[@]}"` → inherits stage-inside-lock cleanly; pre-git-adds (L439/632) redundant-but-harmless; deploy path + DS/DT/AE Rule-13 authority preserved.
5. **Ferried MSTR** completion + hashes + verification; COMP/feature_clb port routed to MSTR→CL domain author (byte-exact `git show CLOUD:.tools/safe-commit.sh`; ws agent can't commit CL content per branch-isolation).

## Root-cause finding (recorded)
The LD-0138 mkdir-mutex ALREADY existed in safe-commit.sh + was insufficient — it serializes safe-commit↔safe-commit bodies but NOT the out-of-band `git add` (caller pre-staging OR peer staging on the shared ajb_workspace index). Hit it 2x post-LD-0138. MSTR credited the empirical finding over its v1 "just add a mutex" premise.

## Follow-on / pending
- COMP/feature_clb port hash (MSTR-routed to CL author) → report when landed.
- The other in-flight: DS~C Prudent Man drill RAVC2; MDPF-FE D3 (DE) visual-close; ADVI Andrew smoke.

## Compiler Tools
bash -n syntax-check on safe-commit.sh (PASS); live concurrent-commit verification (PASS). comp-* N/A (infra tooling, not graph-instrumented).
