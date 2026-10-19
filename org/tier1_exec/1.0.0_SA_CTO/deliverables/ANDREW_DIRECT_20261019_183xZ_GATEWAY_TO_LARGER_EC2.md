# ANDREW-DIRECT 2026-10-19 ~18:3xZ -- the gateway moves to a larger EC2

Given at the laptop 1.0.0_SA_CTO terminal, in answer to this seat's report of the opal-gateway outage (Z-S420, from ~17:30Z; site Z restart
ledger `nfra-oplgtw-gateway-restart-20261019` opened 18:22Z). VERBATIM:

> "Dont mind the gateway, we need to get it up to a larger EC2 because it's choking on large requests on small."

## Reading, kept to his words

- **Cause, his:** the gateway's instance is too small for large requests. This supersedes this seat's two INFERENCES (the 17:41Z tool audit;
  the 17:23Z OG-ap-50 release) as the working cause.
- **Act:** move the gateway (`i-07dccb1615503ac99`) to a larger EC2 instance type. The size is not named; the owner proposes it.
- **Owner:** NFRA_OPLGTW on site Z (1.0.0_SA_CTO~Z rules, 2.0.0_SA_COO~O issues, site Z CloudOps applies under the deploy ledger and its
  never-widen pair). Relayed by bus the same turn. The laptop applies nothing.
- **"Dont mind the gateway"** is this seat's instruction: the laptop stops tracking the outage.

-- 1.0.0_SA_CTO (laptop)
