# Andrew-direct 2026-10-05 ~14:1xZ at the 2.0.0_SA_COO~M terminal -- FWD-10's silver read: R20 YES, PERMANENT

**The call** (`/open-calls` CALL 1 of 1, 2.0.0_SA_COO~M, 2026-10-05 14:0xZ): "Acknowledge the exception that lets the
new-stock producer (FWD-10) read the old Opal ETF holdings location? (yes/no)". The REC was yes, CONDITIONAL until the
etfs-netassets pipeline moves to a builder address.

**Andrew's word, VERBATIM:**

> "Yes it should absolutely be able to that. As long as the scripts invovled are only reading/corroborating
> ticker/security-name data to see if there are new ones not yet in the table, then it shouldnt even need to be
> temporary/conditional grant."

## What it rules

- **R20: GRANTED, PERMANENT** (he rejected the REC's CONDITIONAL). The grant is for MDPF_SECCLASS `new-security-classifier`
  (FWD-10) reading the legacy key prefix `opal-data-etfs/silver/holdings/`, written by `etfs-netassets-daily`, which has no
  `address()` home.
- **Scope, in his words:** the scripts "only reading/corroborating ticker/security-name data to see if there are new ones not
  yet in the table".
- **The scope, measured at HEAD @1e701e1b52:**
  - `infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py:73` reads exactly
    `SILVER_COLUMNS = ("fund_ticker", "holding_ticker", "cusip", "security_name", "is_cash")`. That is identifier and name
    data only: no weight, quantity or value column.
  - The role's grant on that prefix is `s3:GetObject` only (`infra/aws/terraform/mdpf-secclass/new-security-classifier/iam.tf`).
  - Nothing is written under it.
  - A later change that reads another column, or writes there, is outside this grant and needs his word again.

## Where it goes

- **The register entry** (`infra/logic/06_CONFORMANCE_LEDGER.md` section 6, next id X13) is written by the register's lane,
  `4.0.0_SA_CRO`, on this record. That is the same route as X9 and X11.
- **The FWD-10 apply half**
  (`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD10_APPLY_20261005.md`)
  cites this record. Its COO half is signed on it; the CTO half is asked.

Recorded by `2.0.0_SA_COO~M`, 2026-10-05 14:1xZ.
