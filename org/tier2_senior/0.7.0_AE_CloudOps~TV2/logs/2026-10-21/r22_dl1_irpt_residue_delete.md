# TCKT_VNEXT TO-R22-DL1 -- the 42 opal-data-irpt synthetic residue versions deleted (0.7.0_AE_CloudOps~TV2)
**archetype:** DEPLOY

Result: RUN-OK (residuedelete). AMENDMENT 6 (V2 GO 11702, CTO ruling 11699; release 11717 after IB2 reported run 7f). Ledger `tckt-vnext-r22-dl1-20261020` CLOSED, 6 of 6 legs.

- First attempt (AMENDMENT 5, 00:58-01:03Z): STOPPED at the first delete, 0 of 46: the `opal-data-cottonwood` bucket policy `DenyForeignFirmPrincipals` blocks the throwaway role. Roles destroyed; record `stop_at_delete_step.md`. The CTO re-cut the pair to the 42 irpt entries; the 4 cottonwood objects stay as residue.
- This pass (01:27-01:32Z): plan 8 to add, apply 01:28:26Z; role 0 assumed 900 s, FIRST entry deleted (204) and read ABSENT, then the rest: 42 of 42 each 204 and ABSENT (404 only, key lists no version or marker); roles 1-3 likewise. `-target` destroy of exactly the 8 resources (0/0/8), roles read ABSENT 01:31:54Z. Deny v7 intact; control object (a 7F residue key, not in the 42) PRESENT; Andrew's ticket TCK-20261020-b1d61f80 and the two protected tickets present; the ticket-center root shows only the 8 pending adds.
- Check blob 9b192b70ef: R22-RESIDUEDELETE-SELFTEST-OK beside RUN-OK (residuedelete).
- Mistakes: the first stop-and-destroy planned a whole-root `plan -destroy` once (never applied, planfile deleted); and my watcher was deaf for hours until fix 9fe08639a3, which cost five late reads.

## Compiler Tools
- `deploy_ledger.py` open, close-leg x4, close, hold/release: worked. `naming-gate.py --diff --enforce`: PASS 8 graded. `safe-commit.sh`, `safe-apply.sh`, `terraform plan -destroy -target`: worked. `r22_residue_delete_check.py` and `--self-test`: worked. Gaps: the pair did not read the cottonwood bucket policy (first attempt); `plan -destroy` without `-target` is a footgun, the pair now says so.
