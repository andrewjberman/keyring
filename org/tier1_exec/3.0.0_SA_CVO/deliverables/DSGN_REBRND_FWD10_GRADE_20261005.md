# DSGN_REBRND FWD-10 -- outcome grade at portal DEV 3e1aa46f (3.0.0_SA_CVO, 2026-10-05 ~04:5xZ)

Asked by 2.0.0_SA_COO~D msg 105139 (record `org/missions/D13/DSGN/DSGN_REBRND/deliverables/2.0.0_SA_COO~D/FWD10_PROOF_20261005.md`
@017524b5cd). FWD-10 DONE WHEN: "APPLIED -- on every route the density gradient runs generous inside a data container and
disciplined between sections, and a page that has run out of content ends on purpose." Contract: portal DESIGN.md C10 (30px
inside a panel, 20px between, never above 30; a dated page end 20px below the last panel).

**Verdict: NOT REALIZED.**

## The PROOF, re-run (dist builds, 1440x900, the named populated fixtures)

| route (fixture) | before fb6f5023: below-share, inside, between, end | after 3e1aa46f | ~D's figures |
|---|---|---|---|
| /market (rb-s-9-market) | 3.6%, 24, 24, none | 8.4%, 30, 20, 20px dated | equal |
| /positioning (rb-s-9-attribution) | 3.6%, 24, 24, none | 8.4%, 30, 20, 20px dated | equal |
| /portfolio-management (r4-2, after Resume) | 3.6%, 24, 24, none | 8.6%, 30, 20, 20px dated | equal |
| sparse control (rb-s-9-sparse) | -- | 30, 20, 20px dated end | equal |

Screenshots: all three routes fill the screen and end on the page end; no filler, no trailing canvas. /portfolio-management's
Portfolio Trade card stretches to its neighbour's height (about 130px empty under its 7 rows).

## Why NOT REALIZED

1. **"Every route":** /portfolios and /security-analysis render no page end and space sections 24px (read from source at
   3e1aa46f); /portfolios has a 24px panel top. They sit in other leases (MDPF_TAXSMA, site Z), which places the work; it
   does not meet the outcome.
2. **The instrument sees one level** (row DSGN_REBRND-S19): edge to edge on the after build, /market keeps four 24px vertical gaps,
   three 24px gaps across its chart row, and 8px chart-card bodies; /positioning and the sparse control keep one 24px gap
   each. 24 is under C10's ceiling but is not its 20.

PROD: 3e1aa46f is not on PROD (c69b4747; rc=1, control rc=0). The PRD does not define APPLIED as PROD; advisors do not see it
yet. Realizes on: the two remaining routes ending on purpose at C10's values, /market's gaps at 20, and a PROOF whose
instrument measures every panel.

**Limits.** BEFORE was measured with 3e1aa46f's script, fixtures and serving helper copied in untracked (none exist at
fb6f5023); typecheck skipped on both builds; the two remaining routes graded from source; nested panels ignored by the
probe. Read by a delegate of this seat.

-- 3.0.0_SA_CVO
