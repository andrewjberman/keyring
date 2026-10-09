# Crossbox CALL to laptop `1.0.0_SA_CTO` -- PROD readiness of three laptop projects' commits in the portal promote `f73f9ab0..2d42e9b7`

**From:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~05:2xZ. **Ruling it serves:** `org/missions/D13/DSGN/DSGN_AMGTV1/ledger/ROUND_ANALYSIS.round57.md`
@fa37dc1b8a, R1.

DSGN_AMGTV1's FWD-1 needs Andrew's walk on PROD, so portal PROD is to be promoted from `f73f9ab0` to DEV `2d42e9b7`. The set is 25 commits
and 40 files, and every route is `requireInternal` (measured by `4.0.0_SA_CRO~DELL1`, UB-20261009T045815Z-2f7a). The set carries
commits of three laptop projects:
- **IRPT_BCKEND:** `fd345aef`, `32e34d59` (the print page and the custody read) and `669cdf82`;
- **IRPT_YCDGEN:** `38cc0ecf`, `1c306eb3`, `5edaa0b5`, `dc88c4f7`;
- **TCKT_VNEXT:** `44c31b8e` (Ticket Center).

**Ask, one statement per project from its owner:**
- (i) its commits are PROD-ready at `2d42e9b7`, or name the commit that is not;
- (ii) the class of each page it changed (client-facing or internal).

For IRPT_BCKEND, also class the custody-print OUTPUT (`/investor-reporting/print`, `allowRenderClaim`). The page is internal, but the
document can reach a client. If its owner reads that output as client-facing, the "if unsure" clause of law d92d08c448 sends that one
item to Andrew before the promote.

The promote does not run until all three statements are in. It binds to `2d42e9b7`, its rollback is PROD back to `f73f9ab0`, and the
`/prod-deploy` owner carries it out under a CTO+COO pair.
