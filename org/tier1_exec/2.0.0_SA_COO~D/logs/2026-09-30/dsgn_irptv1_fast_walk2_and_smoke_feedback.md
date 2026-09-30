# DSGN_IRPTV1 FAST drive: PROD colours, canonical-table front half, walk-2, two rounds of Andrew smoke feedback -- 2.0.0_SA_COO~D

**archetype:** IMPLEMENT
**secondary_archetypes:** COORDINATE, VALIDATE, DEPLOY

**Date:** 2026-09-29 to 2026-09-30 06:10Z
**Task Order:** DSGN_IRPTV1 under a FAST lease (/closer-drive), Andrew-direct design items; no numbered TO
**Status:** IN PROGRESS (DEV 44fd5f42 at Andrew's re-smoke; PROD promote at Andrew)

---

## Objective

Drive DSGN_IRPTV1 (Investor Reporting UI) under a FAST lease: land Andrew-direct design fixes on portal DEV, promote on
his word, and route the backend halves to their owning seats.

## Work Done

Hour-by-hour detail lives in the committed drive logs (`org/tier1_exec/2.0.0_SA_COO~D/drive_log_20260929T21Z.md`
through `drive_log_20260930T05Z.md`). Summary:

1. **Asset-class colours restored in PROD** (Andrew-direct): Fixed Income green500, Equity blue500, Commodities
   yellow500, Alternatives a new light vermilion `#ff4f1f`; Positioning Holdings Breakdown header without source/date.
   `/prod-deploy` run on Andrew's word: PROD ba8e971f, tag portal-v2.1.191.
2. **Canonical security table:** Andrew's words recorded (@099316efdd); portal half on DEV 5068973b (served sub-asset,
   single stocks after the last ETF class); producer move placed with 2.0.0_SA_COO~M (MDPF_SECCLASS / IB-mr-251..).
3. **Search ranking fix:** full-name, then prefix, then the rest (22cccf87; "anna theiss" ranks Thiessen, Anna first).
4. **Walk-2 brief (22 items):** state table @f80d019a6c; front-end batches 1-2 on DEV (W2-02/03/06/08/09/10/17/18/21/22
   partial); CategoryViewTree unblocked by narrowing MDPF_TAXSMA TO-TX-c-2 as the base COO's delegate (@ebeed86711,
   CTO 103063); worktree-wipe edict applied (MSTR 103044).
5. **Andrew design feedback #1 (~01:4xZ):** pie contrast, Client grey, top-10 map with multi-select chips, account
   picker removed, name without ticker -> DEV 5c7eead8.
6. **Andrew smoke feedback #2 (~05:0xZ):** Securities table folded per Sleeve/Account view (Andrew's word = the F7-AC4
   exception), map tooltip name-only + 'Other Securities' + Client chip + no 'All securities' chip, cash-first class
   order, account dialog sleeves by value with collapsible buckets -> DEV 44fd5f42 (three builders, disjoint files).
7. **PHYS class (Andrew, third time):** CTO 103168 admits a narrowed release (table-first, bd-securities fallback,
   four conditions); relayed to 2.0.0_SA_COO~M, who owns the act.
8. Surprise row DSGN_IRPTV1-S40: 13 IR suite failures from workspace @53bbae9c4f (GET /analysis/comparisons in
   routes.json, portal half absent) -- not this lane's change.

## Compiler Tools

| Tool | Command | Result | Notes |
|---|---|---|---|
| comp-find (rail) | raw grep denied twice, routed to Grep tool | PASS | native Grep/Glob used for code census |
| typecheck | `bun run typecheck` | PASS | 0 errors at 5c7eead8 and 44fd5f42 |
| IR suite | `timeout 580 bun test ./src/pages/InvestorReporting` | PARTIAL | 920 pass / 18 fail = known five + S40's 13 |

**What worked:** builders on disjoint files in the main tree, the full suite run once by the issuer at the end.
**What failed:** nothing new; a shared-tree merge by another seat delayed one log commit (safe-commit refused, retried).
**Gap found:** none new.

## Deployment Sequence + Verification

- PROD: `/prod-deploy` ba8e971f (portal-v2.1.191), Andrew-directed, earlier in the window.
- DEV pushes (lease seat): 5c7eead8, 44fd5f42 -- `git ls-remote origin refs/heads/DEV` read 44fd5f42e7c0 after push.

## MCP Traffic (significant)

CTO 103063 (TX-c-2 delegate), 103071 (worktree edict home), 103168 (narrowed class release); ~P 103156 (Analysis
resident stopped) acked; ~D -> ~M relay of 103168.

## Blockers

None on this lane. Dependencies on other seats: PHYS/GLD/VXX class (~M, CTO 103168 conditions); walk-2 W2-19 (UIC-14),
W2-20 (re-mint), server halves (~M/~Y/~P).

## Current State

- portal PROD ba8e971f (v2.1.191); portal DEV 44fd5f42 (on origin). localhost:5174 runs `bun run dev:live` from the
  main portal tree (log `portal/.runtmp/vite-smoke.log`).
- FAST lease DSGN_IRPTV1 (presence-extended) over portal/src/pages/InvestorReporting, Positioning HoldingsTab,
  components/holdings, components/CategoryViewTree.tsx, lib/chartColors.ts.
- Workspace log commits local on CLOUD (latest c45edc420e); CLOUD push is the integrator's.

## Next Steps

- [Andrew] Re-smoke DEV 44fd5f42 on localhost:5174; call PROD promote; say whether FCASH folds into the Cash row.
- [2.0.0_SA_COO~M] Cut the narrowed class release under CTO 103168; tell ~D when served.
- [IRPT_BCKEND ~Y] Portal half of GET /analysis/comparisons (row DSGN_IRPTV1-S40).
