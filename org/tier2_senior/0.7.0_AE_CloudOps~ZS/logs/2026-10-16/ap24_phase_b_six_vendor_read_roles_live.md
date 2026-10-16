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
