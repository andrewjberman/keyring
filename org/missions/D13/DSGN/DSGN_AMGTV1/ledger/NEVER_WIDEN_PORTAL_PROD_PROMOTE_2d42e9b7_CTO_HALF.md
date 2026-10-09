# NEVER-WIDEN CO-SIGN -- CTO HALF. Portal PROD promote `f73f9ab0 -> 2d42e9b7` (DSGN_AMGTV1 FWD-1's PROD walk)

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-09 ~05:3xZ. **Ruling:** `ledger/ROUND_ANALYSIS.round57.md` @fa37dc1b8a, R1. **Measured set**
(`4.0.0_SA_CRO~DELL1`, UB-20261009T045815Z-2f7a): 25 commits and 40 files in four page families (SecurityAnalysis, Freshness,
InvestorReporting, TicketCenter) and three API modules. Every route is `ProtectedRoute requireInternal`. **Other owners:** laptop
`1.0.0_SA_CTO` answered XB-20261009T052023Z-bf16. IRPT_BCKEND, IRPT_YCDGEN and TCKT_VNEXT are PROD-ready at `2d42e9b7`, every changed
page is internal, and the custody-print output does not trigger law d92d08c448's client-facing clause. Record
`CROSSBOX_ANSWER_XB-20261009T052023Z-bf16_PORTAL_PROD_PROMOTE_READINESS.md` (box/laptop).

## VERDICT: SIGNED for one promote of portal PROD to exactly `2d42e9b7`. Four conditions.

- **Blast radius:** portal PROD's ref, moving from `f73f9ab0` to `2d42e9b7`, and the PROD build it triggers. Nothing else: no backend, no
  Lambda, no S3 data key.
- **Rollback, one key:** PROD back to `f73f9ab0`, in the same session, by the `/prod-deploy` owner.
- **No word from Andrew is owed** (law d92d08c448): no page a client or partner-firm login can open changes. The push receipt names each
  changed page and its class (internal).

## Conditions

1. **Bound to `2d42e9b7`.** Immediately before the promote, `git ls-remote` reads DEV. If DEV is not `2d42e9b7`, the set is re-read and
   this half does not cover the difference.
2. **The `/prod-deploy` skill as updated by d92d08c448** (CLOUD a50603983c) is live at the promote seat, and its own checks stand.
3. **The COO half is `2.0.0_SA_COO~D1`'s,** for the DSGN and CORPUS commits. The other three projects' readiness rests on the laptop
   answer above.
4. **After the promote:** one signed-in read of `/security-analysis/AMD` on PROD loads every tab. Then FWD-1's walk is Andrew's act.

**SIGNED** (conditions 1-4) -- `1.0.0_SA_CTO~DELL1`.
