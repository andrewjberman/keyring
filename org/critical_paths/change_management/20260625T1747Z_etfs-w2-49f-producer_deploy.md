# Deploy-Completion Ledger -- ETFS_SETUP W2: bd-49f-etf-ownership-daily Lambda

**Opened:** 2026-06-25T17:47Z | **Agent:** 0.5.0_AE_OpalETL | **Authority:** COO GO (174526Z, with self-proposed guardrails)
**Status:** CLOSED -- COMPLETE + live-verified 2026-06-25T17:55Z. Tag bd-v2.39.0.
**Change:** Deploy the 49F daily ETF-ownership producer Lambda (`bd-49f-etf-ownership-daily`) + its least-priv write-out IAM role, via Terraform. NEVER#1 write-out model (read own-firm opal-data-bd/schwab/silver/rps + write opal-data-etfs/daily/49financial only; no cross-firm read).

## Plan (COO-sequenced)
1. [x] comp-iam scope (READ opal-data-bd/schwab own-firm + WRITE opal-data-etfs/daily/49financial only; cot/inf Denies = foreign-bucket policies, no grant from this role; clean-by-design).
2. [x] OPEN this ledger.
3. [ ] Author TF: `infra/aws/terraform/bd-pipeline/bd-49f-etf-ownership-daily.tf` (role + policy + yang-lambda module; NO eventbridge trigger -- monthly batch, S-D2 no-cron) + lambda-source-map entry.
4. [ ] safe-apply (HALTGT checkpoint) -> 0-diff plan -> apply.
5. [ ] VERIFY LIVE: get-role-policy shows doc-scoped grant (read-own-firm + write-49financial-only, no cross-firm); real handler invoke writes a fresh slice.
6. [ ] CLOSE ledger; tag + push --follow-tags.
7. [ ] CTO-flag: register opal-data-bd/schwab/silver/rps as the pipescript canonical thread (CTO-owned per PRD Sec 8 -- author/flag, do not self-register).

## Rollback
If apply partially lands or live-verify fails: `terraform destroy -target` the new resources (the role + lambda are net-new, no existing dependency), confirm no opal-data-etfs/daily/49financial write-path is half-granted, escalate to COO. The producer CODE + the 34 proven slices are already committed/landed independently (e03c73cf9) -- the deploy only adds the durable Lambda+role; a rollback loses nothing of the W2 data goal (already HIT day-0).

## Log
- 17:47Z opened. comp-iam scoped clean. Authoring TF next.
- 17:50Z TF + source-map committed (349c91e35); build-and-upload OK (sha mkSBC9...), committed (cc5471620).
- 17:52Z plan: 6 to add / 0 change / 0 destroy. safe-apply (HALTGT pass) -> Apply complete 6 added. 0-diff plan: "No changes".
- 17:54Z LIVE verify: deployed-Lambda invoke StatusCode 200 -> wrote daily/49financial/2026-06-18.json total $519.49M (== local-prove to the cent). Live get-role-policy: READ opal-data-bd/schwab/silver/rps/* + opal-data-etfs/config/* + WRITE opal-data-etfs/daily/49financial/* + scoped List; ZERO opal-data-inf/opal-data-cot grants (no cross-firm read, no Deny-widen; NEVER#1 intact). comp-iam service: all 4 ops GRANTED clean.
- 17:55Z record-terraform-deploy (a071e2e85) + tag bd-v2.39.0 + push --follow-tags. CLOSED.
- REMAINING (not deploy-scope; routed): Sec-8 canonical-thread registration -> CTO (flagged); AVGCAP 49F leg -> DS folded + shipped (3-partner monthly live).
