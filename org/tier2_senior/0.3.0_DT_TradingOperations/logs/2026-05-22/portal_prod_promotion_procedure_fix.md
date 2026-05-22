# Portal PROD-Promotion Procedure Fix — stranded-tree defect

**Agent:** 0.3.0_DT_TradingOperations
**Date:** 2026-05-22
**Trigger:** Process-defect report from 0.3.0_DE_TradingOperations (msg 20260522T193909Z), Andrew-escalated.

## Current State

- **Defect confirmed.** The portal cherry-pick PROD-promotion mechanism
  (SSCN_DIVDEF.006 Phase 1, used for the .001-.011 set + the SSCN_UNVREV set)
  runs `git checkout PROD && git pull origin PROD` in the **shared portal main
  working tree** with **no terminating `git checkout DEV`**. The main tree is
  abandoned on PROD. Verified two ways:
  - `git -C portal branch --show-current` -> `PROD` (stranded right now).
  - SSCN_DIVDEF.006 TO Phase 1 text literally specifies the bare `git checkout
    PROD` in the main tree.
  - portal reflog: `4f8502e6 2026-05-20 14:39 checkout: moving from DEV to PROD`
    is the only branch switch in the window — no matching return to DEV. Found
    stranded twice (2026-05-20, 2026-05-22).
- **Fix adopted + documented.** New canonical procedure: portal PROD promotion
  runs in an **ephemeral `git worktree add` on PROD**; the main tree never moves
  off DEV. Documented as a `<portal_prod_promotion>` section in the DT core
  document `deployment_map.xml` — defect history, 9-step procedure, invariant.
- **RAVC:** ACK sent to 0.3.0_DE (20260522T195104Z). 0.3.0_DE will mandate the
  worktree form in future SSCN promotion TOs — fix is structural on both ends
  (TO authoring + DT core-doc reference).
- **Stranded tree NOT yet restored.** The portal main tree cannot be returned to
  DEV until 0.4.0_DE_ClientPlatform commits their MDPF_ASSETS.033 WIP (aum.ts,
  portal-proxy.ts, ModelPortfolios.tsx) — those uncommitted files straddle the
  branch boundary and `git checkout DEV` would be refused.

## Compiler Tools

| Tool | Result |
|------|--------|
| (none) | Procedure-documentation + core-doc edit only — no script, Lambda, route, or schema change. No comp-* tool applies. |

## Next Steps

1. **[0.4.0_DE_ClientPlatform]** Commit/stash MDPF_ASSETS.033 WIP (aum.ts,
   portal-proxy.ts, ModelPortfolios.tsx) — straddles the DEV/PROD boundary.
2. **[0.3.0_DT]** Once that tree is clean: run `git checkout DEV` in the portal
   main tree to restore it (no cherry-pick — just the branch restore). Ping
   from 0.3.0_DE or 0.4.0_DE expected.
3. **[0.3.0_DE]** Mandate the ephemeral-worktree promotion form in every future
   SSCN portal PROD-promotion TO.
4. DT lane otherwise idle — reachable via the tracked watcher.

## Deployment Tags

No deploy this session — documentation/procedure fix only.
