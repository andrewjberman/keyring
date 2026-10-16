# OG-en-7 -- SmartX cross-firm count (0.7.0_AE_CloudOps~Z, 2026-10-16)

- Order msg 34967 item 2, commit e08686be6a. Read-only; one SSM command, run once.
- Live commit read from the deployed artifact's S3 git-ref: 1bc2df0b13 (moved from 3d5c9c8bf1 by 0.7.0_AE_CloudOps~MI at 11:30Z); equal before and after the read.
- Host program W/en7_host.py uses client_adapter_smartx's own _firm_allocations, _account_map and _candidates_by_account and ctx.firm_roster(); no copy of their logic.
- Result: 6010 candidates over 4528 distinct last4 values, 0 mapping to another firm, 0 unmapped, 0 on a shared account; the served tool agreed with the module on 6 of 6 last4 values.
- Bound named in the record: 75 of 10268 roster rows carry an advisor name the map does not hold; the adapter drops them.
- en7.AC1 PASS. No advisor name, e-mail, account reference or long digit run in any repo file.
