# 2026-10-16 session log -- 0.7.0_AE_CloudOps~ZS (re-seated ~02:20Z)

**archetype:** DEPLOY

## What was done

1. **Startup.** `/watcher` (registered, one inbox Monitor, re-armed once on its 30-minute expiry), `/cloud-ops` once. Three never-widen halves of
   `NFRA_OPLGTW.TO-OG-ap-24` arrived by mail and were checked against the files, not the relays: COO `947810faa8`, CTO `1ef958e44b`, CVO `5b66771763`,
   all at `.tf` sha256-16 `21a54e8f197eeea2` (re-hashed by this seat before the first apply). The CTO relay called the COO half "last owed"; it was already signed (msg 34633).
2. **OG-ap-24 Phase B, GO msg 34663 (02:36Z).** Ledger `nfra-oplgtw-grants-ap24` opened first (8 legs, entry and sentinel committed), then six role + inline-policy pairs applied ONE at a
   time through `safe-apply`, targeted, each plan 2/0/0 and apply 2 added: inf-orion, inf-eclipse, 49f-blackdiamond, cot-commonwealth, cot-blackdiamond, smartx. Each read back
   from IAM (trust principal `opal-gateway-role` only, no Condition, 1 inline policy, 0 attached) and re-planned No changes. 12-target re-plan No changes. Live
   `gateway-blackdiamond-read-policy` `4893211d4408180a` and `gateway-schwab-read-role-policy` `a3e8ca81172af8cc` unchanged. `iam simulate-principal-policy`,
   one resource per call, 6 of 6 roles: in-prefix GetObject allowed; other prefix, `opal-data-bd` and PutObject explicitDeny; each first table prefix holds objects (KeyCount 5; Commonwealth 1).
   Ledger CLOSED, `GR_APPLIED.json` written (`19b3257eb9`). Local tag `opal-gateway-v1.7.1` at that commit.
3. **Proof.** AC1 PASS. AC2: the order's `<expect>` needs `; policy live yes`, which `ap24.AC2.sh` never prints, and the script's role list names the pre-existing BD role, not the 49F role. Recorded
   AC2 FAIL with the true output, instance VALID; BLOCKING row `NFRA_OPLGTW-Z-S158` (disarm_owner `2.0.0_SA_COO~O`); commit `c0f73fe730`. Order left `pending`. Reported once to the issuer.

## State left

- Push state: LOCAL @c0f73fe730; origin `box/sitez` read `253bc0fe3f` (ls-remote 03:1xZ). The tag is local too. Not this seat's push.
- Open for `OG-ap-23` (not this order): CVO C1 (one real AssumeRole, needs the gateway instance role) and C2 (SmartX two-firm arm). The roles are unused until then.
- Nothing is held open: ledger closed, no worktree created, no scheduled task touched.

## Compiler Tools

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | six targeted applies, rc 0; `market_update_s3_root` has no default and was fed the `address()` value as `variables.tf` says |
| `deploy_ledger.py` | PASS | `open` commits itself; `close` left the closed entry and the sentinel deletion uncommitted, so they went in the Phase B commit |
| `proof-of-spec-check.py` | PASS | first run INVALID (kind `other`, AC2 expect mismatch, aws row path); kind fixed, AC2 recorded as the script printed it, then VALID |
| `comp-schedule --drift` | gap | carrier C2 read "scanned 0 of 25 ledger entries; BUDGET PARTIAL", not read as zero; no schedule is added by this order |
| `iam simulate-principal-policy` | PASS | one resource per call; existence read beside each prefix |

## Later in the same session: OG-ap-24 closed, OG-ap-25 done

4. **OG-ap-24 closed.** The issuer amended `ap24.AC2.sh` at `d55475e545` (Z-S158); AC2 re-run PASS, instance VALID, order flipped complete (`dcc3ac9174`). Row `Z-S159` records the condition met.
5. **NFRA_OPLGTW.TO-OG-ap-25 (etf-classifications read grant), complete.** Phase A 04:53Z-05:03Z (GO 34735): one `aws_iam_role_policy` on `opal-gateway-role`, `dynamodb:GetItem` on the table ARN, plan 1/0/0, 0 of 24 role policies named the table, AC1 PASS (`31f5f961c1`). Halves signed CTO `9fc726f92a`, COO `d87f790253`, CVO `be6d23b7f6` at `.tf` c51c268d41b63e8f / ask 01861a288d2b. Phase B 05:12Z-05:22Z (GO 34744): ledger `nfra-oplgtw-grants-ap25`, one targeted `safe-apply` (1 added), read back (one statement, GetItem only, the table ARN), simulator GetItem allowed / Scan, Query, PutItem implicitDeny with a positive control, describe-table ACTIVE, re-plan No changes, ledger CLOSED (`3ba4af364d`). AC1 and AC2 PASS, instance VALID, status flipped. The policy is unused until the OG-ac-2 release.

## Compiler Tools (OG-ap-25)

| tool | result | notes |
|---|---|---|
| `safe-apply.sh` | PASS | one targeted apply, rc 0 |
| `deploy_ledger.py` | PASS | 3 legs closed with proof; `close` leaves its own records uncommitted |
| `comp-schedule --drift --budget 420` | PASS | 6 of 6 carriers in 211 s; C4 and C5 PARTIAL_OR_BLIND, not read as zero |
| `terraform init` | note | a new `opal_name` module call needs it before any plan ('Module not installed'); no tracked file changed |
| `proof-of-spec-check.py` | PASS | VALID first run (kind `aws_resource` used for the IAM row) |
