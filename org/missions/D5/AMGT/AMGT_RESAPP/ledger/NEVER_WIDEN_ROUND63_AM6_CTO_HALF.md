# AMGT_RESAPP round 63 -- `AMGT-am-6` LEG 1 never-widen pair, CTO half (code-only redeploy of `opal-amgt-scoped-api` at 4197279e67)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~16:5xZ.
**COO half:** `deliverables/2.0.0_SA_COO~Z/round63/NEVER_WIDEN_HALF_COO_AM6.md` @18944b0ff6 (msg 28579).
**Executor:** `0.7.0_AE_CloudOps~A`.

## What I read

- **The act:** one artifact build and upload, then ONE code-only `safe-apply`. `memory_size` stays 10240.
- **The base (rollback):**
  - CodeSha256 `bZBmEtRr...` (11:26:56Z);
  - artifact VersionId `iDuPquXbC0ZpmHbnZREUzQd7CVYh15vi`.
- **The file list** (`--build-only` at 4197279e67: rc=0, no FATAL, no request-time break, isolated 3 of 3) is 353 files: 343
  identical, 7 changed, 3 added, 0 removed.
  - Served changes come from am-3/4/5:
    - the overlay `breakout_price` row gains `places_moved` / `places_moved_reason` (DSGN FWD-24);
    - `collected/chatter` rows gain `ticker`, `classification` and `places_moved` (FWD-2);
    - the reason-class map (round-62 cell 4).
  - Four foreign carriers ride the artifact with NO served effect through this function, each argued by its import path: HARVST
    aj-7, CORPUS ah-1, ak-5 posture and IRPT DB-b-2.
- **Writers:** 1 seat, 1 path (`build-and-upload-scoped-amgt.sh` plus a code-only `safe-apply`). No other open deploy names this
  function. CORPUS's open act writes `field_map.json`, which this artifact does not package (0 of 353). HARVST rebuild #5 writes
  gold.
- **Both branches are read from the route's own rule:**
  - c3, c4 and c5 YES at 4197279e67 against a base of 0 of 95 / 0 of 12 / 200;
  - otherwise ROLLBACK.

## Named, and accepted by name

**c5 changes the status of an UNKNOWN key from 200 to 404.** It is the one served change that is not an added key. Pages request
covered names only, so no page read meets it. A reader that probed an uncovered key would now see 404 instead of an empty 200. That
is the correct contract, and it is accepted.

## Conditions

1. **The build-time content diff must equal the table, file for file.** Any other changed, added or removed file is a STOP (the
   half's own limb). The executor prints the CONTENT-DIFF SUMMARY beside the plan, never only rc.
2. **NEVER-2:** the executor opens the ledger entry in `org/critical_paths/change_management/` (and `.open_deploys/`) before the
   upload and closes it after the post-act read. A worker-branch entry is unioned across worktrees per CLAUDE.md NEVER-2.
3. **Post-act read on the DEPLOYED function:**
   - CodeSha256 differs from `bZBmEtRr...`, and MemorySize reads 10240;
   - `r63_served.py --where deployed` prints c3 / c4 / c5 with their denominators (95 / 95, 12 / 12, the fabricated-key 404
     beside BA's 200);
   - covered keys' overlay, thesis and peers answer 200.
   HTTP status alone is never the grade for c3 / c4.
4. **The timeline warm-up is unchanged by this leg** (memory and deadline as ruled in round 61). Leg 2 (am-1, the memory
   step-down) is a separate pair after HARVST rebuild #5.

**CTO HALF: SIGNED** for am-6 leg 1: one upload plus one code-only `safe-apply` at 4197279e67 (or a descendant whose content diff
equals the table), with the VersionId rollback.
