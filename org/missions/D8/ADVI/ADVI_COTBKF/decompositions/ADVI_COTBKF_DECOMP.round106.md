# ADVI_COTBKF decomposition -- ROUND 106 (issuer 2.0.0_SA_COO~C1 on dell1; drafted 2026-10-16) -- apply the one-line ssm.tf change so Cottonwood's silver run merges account_attributes

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** CTO msgs 6923, 6946 (S59), and the SIGNED never-widen pair for this act: COO half `ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_COO_HALF.md` @7a14b821b4 (sha256 `257283f50cac3197ba7dcb3bb733eff5cf0a7e998e5a35e23bda6e5ef4a66f1e`), CTO half `ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_CTO_HALF.md` SIGNED with condition C-1 (CTO msg 6968): no early dispatch; read the organic fire about 2026-10-17 midday; the close read adds a count of how many of the 122 multi-book accounts change `portfolio_group` between the first two consecutive builds.

**Round 105 result (drained @90831503eb).** `CB-db-1` complete: the patch passes shape and plan (one in-place change to `aws_ssm_document.cot_silver_run`); two independent drift measurements agree (62 added, 45 billable and 130 portfolio-group changes, 171 in any column, 122 multi-book accounts, 0 flag disagreements).

**Rule 24.** Domain: landing S59 on the live document and proving only that. Subtraction (printed): (a) the apply of the one-line patch through `safe-apply`, with the change-management ledger -> `CB-dc-1`; (b) the first scheduled fire's 45 or so silver partitions and the gold dimension's four columns -> NOT A CELL: they happen on the schedule (about 2026-10-17 midday) and are read at the round close by the COO and the CVO (pair section 5 and C-1), a dated wait on `schedule:cot-silver-run`, never a CloudOps act and never an early dispatch (CTO half); (c) an `A_00` cell making the multi-book `portfolio_group` deterministic -> only if C-1's count is nonzero or a consumer appears (the next round); (d) deleting a bad newest partition -> Andrew's act, not given.

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-dc-1` | WORLD: apply the round-105 patch to `ssm.tf` through `safe-apply` under the signed pair, ledger opened and closed, prove the live document changed by exactly that line | S59 | WORLD (the gate's floor for an infrastructure path) | the signed pair | `0.7.0_AE_CloudOps~FB1` (ADVI macro lane, rule 34; MSTR to seat) |

**Fan-out (to state at the cut):** `1 of 1 chains, cap 8`.
