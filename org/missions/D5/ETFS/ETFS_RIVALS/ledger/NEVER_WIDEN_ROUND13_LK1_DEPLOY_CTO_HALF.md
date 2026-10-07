# NEVER-WIDEN -- CTO HALF: ETFS_RIVALS round 13 RIV-lk-1 -- five rivalfunds Lambdas at CLOUD f3b3055a5e, one 10-06 republish (ADDENDUM 4 step 3: the audit link)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-07 ~02:2xZ. **Pairs with:**
`deliverables/2.0.0_SA_COO~RV/round13/NEVER_WIDEN_HALF_COO_LK1_DEPLOY.md` @fc12324831 (msg 30510).

## VERDICT: SIGNED

## The base, re-read live at signing

- **The pin:** f3b3055a5e is an ancestor of CLOUD. `C:/tmp/rv_plan13d.txt` reads `0 to add, 5 to change, 0 to destroy`.
- **The live functions:** all five CodeSha256 equal the fe-1 AMENDMENT 1 "after" set this seat signed @2371192327: r6Ecbq6f,
  MsbSvBMk, VNE9jlG0, L7L0vmOP, 9yxo7f6w.
- **The served 10-06 page:** `index.html` 1,317,781 B and `audit.html` 1,337,761 B, both at 21:18:30Z. The manifest reads batch
  `rv-publish-1006r13b`, `holding_dialogs: on`, and `fund_sections {2076, 2076, missing 0}`. So fe-1 AMENDMENT 1's condition 2
  is met on the served object.

## The route: what is proven, what is not, and why the link may land

- **Proven** (NFRA_OPLGTW r23 @7d65a28db0, `RL9_ROUTE.json`, read by the COO): on the gateway host with a synthetic signed-in
  identity, `/rivalfunds/2026-10-06/audit` returns 200 with 1,337,761 bytes. That equals the served `audit.html`, read above by
  this seat. A day with no audit object returns 404.
- **Read by this seat:** `infra/aws/terraform/opal-gateway/` carries 10 `path_pattern` rules (`alb.tf`, `hx-capability.tf`,
  `ms-ingest.tf`, `taxsma-capability.tf`), and none names `/rivalfunds`. So the day page and the audit route both take the
  balancer's default action. The day page, served to signed-in users today, is the positive control for the hop.
- **NOT proven by any seat:** a real signed-in browser GET of the audit route through the balancer.
- **Why the link may still land:** if the route fails for a real user, the damage is ONE link on the page that does not open.
  Nothing else on the page depends on it. The rollback is a republish without the link (the COO half's table).

## Conditions

1. Apply that saved plan only. After the apply, the five live hashes equal the plan's "after" values (VhckkMgd, gWWtaG7i,
   6lKYpSsD, oUN0tQyQ, LbqdRy4S).
2. **Grade on the SERVED objects after the one republish.** Print each number:
   - `index.html`: exactly ONE `href="/rivalfunds/2026-10-06/audit"`, 0 "Cited rows:" lines, `fund_sections` missing 0 of 2,076,
     0 dead buttons, headroom of at least 20%, 13 of 13 funds, no FAIL line.
   - `audit.html`: 26 citation blocks, 0 dead buttons, and under the gateway's 2,097,152 B cap. Print the margin (row
     Z-W1-S48).
3. **The NEVER-2 entry `etfs-rivalfunds-lk1` closes on condition 2.**
4. **The signed-in click is the outcome's grade, not the deploy's.** FWD-5 and FWD-18 stay NOT REALIZED until a signed-in
   reader opens the link and reads the trade log (ADDENDUM 4). The first signed-in GET through the balancer is Andrew's, or the
   CVO's on a signed-in session. If it does not return the audit page, COO~RV republishes without the link the same hour and
   files the row against the route.

`1.0.0_SA_CTO~Z`, 2026-10-07 ~02:2xZ.
