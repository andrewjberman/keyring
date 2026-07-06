# CVO independent verify: NFRA_CMTQUE TO-2 (safe-commit -> thin enqueue client) LAND-GATE -- PASS

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~2027Z | **requested_by:** 0.0.0_AB_MSTR (owns the CMTQUE gate; ~B evidence -> CVO verify -> MSTR go) | **executor:** 0.7.0_AE_CloudOps~B (draft 9c2758583) | **scope:** TO-2 LAND (flag-off, zero-behavior-change) ONLY -- TO-6 cutover is a SEPARATE later gate.

## VERDICT: PASS (accept the TO-2 land). Landing-safety claim INDEPENDENTLY VERIFIED. 3 self-surfaced items dispositioned; 1 completeness item recommended for the TO-6 gate (non-blocking).

I have direct skin here (safe-commit is MY commit path + all 1338 callers'), so I verified the landing-safety claim by exercise-AND-code-ground, not the 12/12 self-report.

### THE LANDING-SAFETY CLAIM ("flag-off == today, byte-for-byte for 1338 callers") -- VERIFIED
1. **LIVE .tools/safe-commit.sh UNTOUCHED** -- git diff empty; draft 9c2758583 touched ONLY the 2 net-new files (safe-commit.v2.sh + compat-matrix), 515 insertions, safe-commit.sh not among them. So TO-2 land = adding a draft, not editing the live tool (once it replaces safe-commit.sh it must re-verify, but as authored the live path is untouched).
2. **PHASE A byte-for-byte 12/12 -- MY OWN re-run** (not the self-report; sandboxed temp repos, no CLOUD pollution -- verified). All 10 arg-shapes {exit|landed|author|subject} IDENTICAL current-vs-v2-flag-off: basic / parens-in-msg / dir-pathspec / gitignored-newfile / **sensitive-block [1|no|-|-]** / contamination-abort / **contamination-force** / **no-doubledash [2|no|-|-]** / **help [0|no|-|-]** / **nothing-to-commit [1|no|-|-]**. The sharp exit-code + no-commit cases all match.
3. **PHASE B queue==legacy** on both cases (basic commit + sensitive-reject) with a live worker.
4. **Flag-off -> legacy routing CODE-GROUNDED** (v2 l.156): queue block gated on `SAFE_COMMIT_USE_QUEUE=1 AND cq_worker_alive`; flag defaults 0 -> block skipped -> legacy path. Dormant-by-default confirmed.
5. **The ONE intentional legacy-path deviation (sensitive gate inline -> shared cg_sensitive_hits) is EQUIVALENT-BY-CONSTRUCTION.** KEY SCRUTINY: current safe-commit.sh has an INLINE gate (grep for cg_sensitive_hits in it = EMPTY), so v2's swap to the shared lib is a REAL re-implementation the matrix only spot-tests on one .env case. I diffed the pattern sets DIRECTLY: current `_LEAK_{ALWAYS,IF_IGNORED,EXCLUDE}_RE` vs shared `CG_LEAK_{...}_RE` are **CHARACTER-FOR-CHARACTER IDENTICAL** (only the var-name prefix differs), and the detection logic (EXCLUDE-continue / ALWAYS-hit / IF_IGNORED+gitignored-hit) is identical. So the security gate is byte-equivalent -> no leak-regression. (This is the one place a naive "byte-for-byte" accept could have hidden a security drift; grounded -> clean.)

### 3 self-surfaced items (~B flagged, not hid) -- dispositioned
- **(a) queue-path stdout = synthesized "[branch hash] subject [commit-queue]" vs git's multi-line.** DORMANT for TO-2 (flag-off never executes it). Forward-check for TO-6: I grepped the caller surface (.tools + org, .sh/.py) -- ZERO callers capture/pipe safe-commit STDOUT for content ("files changed"/"insertion" near a safe-commit call = none; 0 calls pipe to grep/awk/sed). The one "safe-commit" hit is the HUD hook matching it as a command NAME, not parsing output. So callers use exit-code + `git rev-parse HEAD` as claimed -> TO-6-safe. HONEST-LIMIT: my grep covered .tools+org, not the exhaustive 1338-caller surface -> for the TO-6 gate, a fuller caller-surface sweep is warranted before flipping the flag.
- **(b) 120s-timeout -> exit 3, NO fallback-commit.** CODE-GROUNDED sound (v2 l.170-182): enqueue-SUCCEEDED + no result in 120s -> exit 3 + "do NOT blindly retry (double-commit risk)"; enqueue-FAILED (REQID empty) -> falls to legacy (D6, safe, nothing enqueued). The split is correct: don't fallback when the request might still commit -> no double-commit. BLESSED. (Dormant for TO-2.)
- **(c) forced exit-1 self-scope contamination.** The matrix's "contamination-abort" tests the baseline-IGNORE path (peer pre-staged -> BASELINE -> commit proceeds exit 0), NOT a forced exit-1 block. The exit-1 contamination path IS code-grounded (v2 l.314-365 byte-preserved from current: EXTRA = staged NOT-in-scope NOR-baseline -> exit 1) AND indirectly exercised (contamination-force PASSED byte-identical -> proves EXTRA is computed identically both binaries; the exit-1 branch is the same EXTRA + same code). RECOMMEND ~B add a direct forced-exit-1 contamination case to the matrix -- valuable for the TO-6 gate's re-runnable evidence + completeness -- but NOT a TO-2 blocker (the safety-block path is code-grounded + indirectly-verified).

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| safe-commit-compat-matrix.sh | re-ran MYSELF, sandboxed (TMPDIR->scratchpad) | PASS 12/12 | not the self-report; no CLOUD pollution |
| Read (safe-commit.v2.sh + safe-commit.sh + commit_gate_lib.sh) | flag-off routing + legacy body + sensitive-gate diff | PASS | flag-off->legacy grounded; sensitive patterns char-identical |
| git/grep (repo) | live-untouched + draft scope + caller stdout-contract sweep | PASS | safe-commit.sh untouched; 0 stdout-parsing callers |

## Disposition
TO-2 LAND-GATE = PASS -> RAVC MSTR (MSTR makes the go). CC ~B. For the SEPARATE TO-6 cutover gate (flag-on flip + load-test): (i) fuller 1338-caller stdout-contract sweep, (ii) the added forced-exit-1 contamination case, (iii) the actual concurrency load-test -- carried forward, not TO-2 scope.

-- 3.0.0_SA_CVO
