# PROPOSAL: Mandatory test-build PREFLIGHT gate (Andrew-direct 2026-07-01)

**Author:** 0.4.0_DS_ClientPlatform~A · **Routed to:** 1.0.0_SA_CTO + 2.0.0_SA_COO (ratify + gate)
**Trigger incident:** ADVI_INFREF v3 rebuild (SSM 29629fb9) failed 3x in one night; the 3rd death was a
**2-hour SSM ExecutionTimedOut** on a job whose STEP2a alone is a known 87.5-min task. Recoverable
condition (idempotent + `--resume`) turned FATAL + un-watched. Full diagnosis: `org/tier2_senior/
0.4.0_DS_ClientPlatform/logs/2026-07-01/seams_0352Z_infref-v3-rebuild-chain.md`.

## Andrew directive (verbatim intent)
Run a preflight on **every** test build, every time, as a **prerequisite** for firing. A core function
of that preflight is **timeout assessment** -- "killing our shit over a timeout" on a knowable, recoverable
job is a preventable, self-inflicted failure.

## The gate: 3 blocking checks before any test/rebuild fires (SSM/EC2/long batch)

### 1. TIMEOUT / RUNTIME BUDGET  (first-class, the one that burned us)
- Compute `est_runtime` from the last run's elapsed (STEP2a logged `elapsed=5250.0s`) or date-range x per-task cost.
- Compare to the command's execution ceiling. **BLOCK if `est_runtime` (with headroom, >=1.5x) > ceiling.**
- Default long-build ceiling = GENEROUS (hours, or the SSM max 172800s), never the inherited 3600/7200 default.
  (Mirrors deploy-rule #5 "size resources deliberately" -- extended from Lambda mem/timeout to SSM command timeouts.)
- **PREFERRED structural resolution (makes timeout non-fatal by construction):** long jobs run **DETACHED**
  on the box (`setsid`/`nohup`/`systemd-run` -- SSM fires-and-returns), write their own progress + terminal
  sentinel, and are polled via the sentinel. The RunCommand execution ceiling then does not gate the job at all.
  Combined with the existing idempotent skip-converted + `--resume`, a slow run is just slow, never a kill.

### 2. MECHANICAL SEAM PREFLIGHT  (`/seams <build> --axis mechanical`, scoped)
Catches the code-level "dumb bugs" at the desk instead of on the box:
- Driver's call args vs the callee's argparse `choices` (killed attempt #1: `--dims transactions` invalid choice).
- Reader format vs the actual bronze format on disk (killed attempt #2: `read_parquet` on `.jsonl.gz`).
- Path / script-ref resolution (the classic "bad path").
- `bash -n` clean + `comp-pipescript deployed` MATCH on every script the build syncs.

### 3. WATCHER TERMINAL-COVERAGE  (the reason it stayed invisible)
- The build's completion-watcher MUST fire on **terminal-FAILURE** states (`TimedOut`/`Failed`/`Cancelled`),
  not only the success sentinel. `InProgress` != healthy; "no sentinel yet" != "still running."
- Anchor: three agents "believed riding" because watchers keyed only on sentinel-appears; the death was
  caught only by a watch armed on **SSM-terminal OR sentinel**. Make that the standard watch shape.

## Gate mechanism (so it teaches at violation time, not as prose agents forget)
- A wrapper -- candidate `safe-ec2-run.sh` / `comp-preflight` -- that (a) runs the 3 checks, (b) logs a
  preflight record (like the deploy-completion ledger), (c) **REFUSES to fire an unbudgeted / unchecked build**
  (override audited, like `safe-apply` HALT_OVERRIDE). A test-build fired without a logged preflight = a gate miss.
- Ownership: CTO/COO to ratify + pick the wrapper home (likely alongside `safe-ec2-deploy.sh`). DS/AE consume it.

## Why not "just run full /seams every build"
The full 3-axis /seams is post-hoc integration QA -- valuable AFTER a build, but a *pre-build* /seams cannot
observe a timeout (the build hasn't run). The timeout is a **capacity** check (#1), not a seam defect. So the
prerequisite = the fast mechanical seam subset (#2) + the runtime-budget check (#1) + watcher coverage (#3),
not the heavy full-3-axis pass on every build.

## Immediate (does not wait on ratification)
- INFREF re-fire (0.6.1/AE lane): bump ceiling to 4-6h OR split STEP2a/2b/3 OR run detached; STEP2a silver is
  already converted this session so a re-fire fast-skips it. Confirm the interrupted-STEP2b partial live-silver
  is value-consistent before the next nightly gold consumes it.
