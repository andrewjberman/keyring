# AMGT_RESAPP round 65 -- ao-2, the code redeploy, and the two STOPs that preceded it -- 0.7.0_AE_CloudOps~A

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

**Date:** 2026-10-03
**Task Order:** AMGT_RESAPP.TO-AMGT-ao-2 sections 1 and 6 (AMENDMENT 1)
**Status:** COMPLETE -- AC1 and AC2 PASS, 5 of 5 regression cells unchanged and YES, rollback not taken.

Session start, so no prior-log delta. First act of session 87228929.

## Objective

One code-only redeploy of `opal-amgt-scoped-api` carrying `AMGT-ao-1` (FWD-38 (b) title case)
and, as it turned out, the ft publisher-quarantine mechanism deletion. Memory stays 1769.

Also: answer the relayed Andrew-direct asking every seat to release any quarantine it holds.

## Compiler Tools

| Tool | Result |
|------|--------|
| `build-and-upload-scoped-amgt.sh --build-only` x2 | PASS, and the FIRST run is what caught STOP 1. At the then-HEAD: `355/352/3`, the third file off both halves' lists. At the pin in a detached worktree: `355/352/3` with the amended list, file for file. |
| `build-and-upload-scoped-amgt.sh` (real) | PASS. Reproduced the build-only diff AND size exactly; VERIFY 75 of 75 modules, cold-start FATAL `[]`, request-time break `[]`, VERIFY-DATA 15 of 15 and 8 of 8, ISOLATED 3 of 3; upload read back with matching `content-sha256`. |
| `terraform plan` / `show -json` / `safe-apply` / `plan -detailed-exitcode` | PASS. 49 `resource_changes`, 1 non-no-op, exactly 3 attributes, `memory_size` 1769 -> 1769, no delete or replace; re-plan 0-diff, exitcode 0. `SAFE_APPLY_TERRAFORM` had to be set -- `.tools/terraform.exe` is absent on this device. |
| `.tools/deploy_ledger.py` open / close-leg x3 / close / check | PASS. Entry opened AND COMMITTED (`4922fbb96f`) before the upload, so the sentinel landed; closed 3 of 3. Final `check`: 27 of 27 sentinels scanned, nothing of mine open. |
| `r65_served.py c17`, `r64_served.py c12 c9 c10 c11 c13 c14` | PASS. Base arms captured on the deployed function BEFORE the apply; `--where local` pre-flight read YES before any upload. |
| `comp-find` / `comp-read --enumerate` | PASS. Denominators printed (4802 of 109620 repo-wide; 101 of 416 on this seat's surfaces). `comp-read --enumerate` on the CTO half is what exposed AMENDMENT 1 present in the FILE while git showed it UNCOMMITTED. |
| `git worktree` + `sparse-checkout` | PASS. A sparse cone (`lib infra org tests .tools`) gave an exact-pin build root without the full-checkout memory risk banked for this device. |

**What worked:** measuring the build point instead of trusting the halves' sentence about it. Both
halves asserted "HEAD equals 9a8cbd2c97 on both packaged files"; that was true when written and false
by the time I built. The `--build-only` gate is cheap and it caught both drifts.

**What failed:** nothing in the act. Two process notes below.

**Gap found:** `r65_served.py --where deployed` grades deployed names with a LOCAL predicate (row
Z-S342).

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | base re-read live | `KQSA62c3...`, 1769, 41,149,311 B -- UNMOVED from the halves |
| 2 | base identity control | downloaded the artifact at the rollback VersionId; its sha256 base64 EQUALS the deployed CodeSha256 |
| 3 | `--build-only` at the then-HEAD | `355/352/3` -- **STOP 1**, `finbert_sentiment.py` off both lists |
| 4 | STOP surfaced, not adjudicated | msgs 28947 + 28949; recommended amending rather than taking the compliant-looking pin arm |
| 5 | ruling 28960, halves amended | COO `b5f723dbdf`, CTO `2c758d373c` |
| 6 | tip re-tested, not assumed | `rolling_windows.py` moved -- **STOP 2**, a tip build would read CHANGED 4 |
| 7 | detached sparse worktree at `19cb3df089` | `--build-only` read `355/352/3` exactly |
| 8 | entry opened + COMMITTED | `4922fbb96f`, before the upload |
| 9 | real build + upload | VersionId `5xO0vR9UWlx.XI59G0KNLJyAsjMKOes4`, `lPTMo20T...` |
| 10 | plan read from JSON, then `safe-apply` | 1 non-no-op of 49, 3 attributes, memory unchanged |
| 11 | deployed read + re-plan | `lPTMo20T...`, 1769, Active/Successful; re-plan 0-diff |
| 12 | AC1, AC2, regressions | all PASS from the pin checkout; zero FAIL lines |
| 13 | entry CLOSED, instance committed | `76c5170831`; worktree removed, scratch branch deleted |

## Verification

AC1 on the deployed function, graded from the pin checkout:

```
PASS C1 breakout/price serves 0 all-caps names status 200 names 94 all-caps 0; e.g. []
PASS C2 price serves Mitsubishi UFJ Financial Group whole served ['Mitsubishi UFJ Financial Group']
PASS C1 collected/chatter serves 0 all-caps names status 200 names 95 all-caps 0; e.g. []
PASS C2 chatter serves Mitsubishi UFJ Financial Group whole served ['Mitsubishi UFJ Financial Group']
R65 C17 SERVED: YES
```

Against the base arm I measured on the same function before the apply: all-caps 55 of 94 and 56 of
95, `MITSUBISHI UFJ FINANCIAL GRO` on both routes. The denominators 94 and 95 are IDENTICAL
base-to-after, which is the control that no row moved -- only the casing did.

The regression set is UNCHANGED, not merely passing: every printed window, count and reason string
in c9, c10, c11, c12, c13 and c14 is byte-identical to the base capture.

## Decisions Made

1. **Stopped on CHANGED 3 instead of reading it as "close enough".** The count differed from the
   halves' by one file, and the extra file was a real source change neither half had read. The
   order's words are "any CHANGED file not on the halves' list is a STOP", so this was mechanical,
   not a judgment.
2. **Did NOT take the pin arm even though I had PROVEN it compliant.** The original pin yielded
   exactly CHANGED 2 and would have passed every gate. But it still CONTAINED the ak-4 mechanism
   that Andrew's ~18:xxZ record orders deleted, so shipping it would have satisfied the halves while
   contradicting a live Andrew-direct. I surfaced both facts and recommended the half amendment. The
   mechanically-available arm was the wrong one.
3. **Re-tested the tip after the re-pin rather than inheriting "ships the repo as it stands".** That
   sentence was the issuer's intent, but intent is not a measurement: `rolling_windows.py` had moved
   and a tip build would have read CHANGED 4. Caught before the build, not after.
4. **Read the plan from `show -json`, not from the human plan.** The human output says "28 unchanged
   attributes hidden", which is not evidence that `memory_size` held. The JSON gives before 1769 /
   after 1769 explicitly, plus the proof that no action shape is delete or replace.
5. **Did not reverse `ad-2`'s `held_no_span` when asked to release quarantine.** The word "hold" is
   in its name, so I named it deliberately rather than letting a term census silently miss it. It is
   a COO-issued product field the deployed adapter reads -- ad-2's own AC2 proved the served
   `/thesis` text reads the hold off the object -- so reversing it would MOVE served text and would
   itself be the unauthorised data-engineering change the same directive forbids. Surfaced to the
   issuer; adjudicated neither way.
6. **Reported the base-figure discrepancy as an INSTRUMENT finding, not a spec error.** The halves say
   60 of 94 and 61 of 95; I measured 55 and 56 on unchanged bytes. The identical denominators ruled
   out the world having moved, and reading the script showed why: the acronym set is imported from the
   local tree outside the `--where` branch. Row Z-S342.
7. **Corrected my own "CTO half uncommitted" message within the hour.** It was true when measured --
   `git show HEAD:<file>` carried zero `RE-SIGNED` lines while the worktree file had them -- and it
   landed at `2c758d373c` while I was still measuring. I said so plainly rather than letting a stale
   ask stand.

## Files Modified

See `19cb3df089` (quarantine answer), `326e271887` (row Z-S342), `4922fbb96f` (ledger open),
`76c5170831` (instance + ledger close). No terraform file changed -- the act is code-only and
`memory_size = 1769` stands as previously committed.

## Blockers

**None owed by this seat.**

## Current State

`opal-amgt-scoped-api` runs `CodeSha256 lPTMo20TWOn9GxEyMPa4EausVvWKpvyGQTeZcVFZlW0=` at
`MemorySize 1769`, artifact VersionId `5xO0vR9UWlx.XI59G0KNLJyAsjMKOes4`. The ak-4 publisher-quarantine
mechanism is now ABSENT from the deployed bytes, not merely inert. Package headroom 8,418,337 B spare
at 96.8%.

Round 65 served state: c17 YES for the first time; c9, c10, c11, c12, c13, c14 unchanged and YES.

## Next Steps

1. **[`2.0.0_SA_COO~Z`]** The `<status>` flip on ao-2 -- `task-orders/` is not in this order's `<paths>`.
2. **[`2.0.0_SA_COO~Z`]** `lib/research/api/rolling_windows.py` (`c20fd8cc98`) is deployed-stale by one
   commit and rides the next act, per GO 28969.
3. **[`2.0.0_SA_COO~Z`]** Row Z-S342: if `r65_served.py` stays a round-65 instrument, moving the
   acronym read inside the `--where` branch would make its base arm reproducible.
4. **[`2.0.0_SA_COO~Z`]** `ad-2`'s `held_no_span` is surfaced for a ruling under the ~17:3xZ direct;
   this seat took no action on it either way.
5. **[`0.0.0_AB_MSTR~Z`]** The push. All four commits from this seat are LOCAL on this device
   (origin/CLOUD read `a714df4d7f` by `git ls-remote` at report time).
