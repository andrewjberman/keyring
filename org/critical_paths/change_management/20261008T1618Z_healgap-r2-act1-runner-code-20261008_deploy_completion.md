# Deploy Completion Record
**Date opened:** 2026-10-08T16:18:06.104084+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP R2 act 1: cot-rebalancer-runner code (HG-t-3 per-feed result + PartialDay + drop-feed induce) at CLOUD 1fdab25b2b; halves COO ab41a7d1d8, CTO d2b90c937d. Branch B history: rebalancer_model_detail missing 2026-08-31..09-10 (11 of 80 dates); under this code each would read PARTIAL, no stamp, no silver. Rollback: artifact version uNNJvohJ8HVjIlEcIjEmpouzIRxLROD8, CodeSha256 QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=
**Authored by:** 2.0.0_SA_COO~G1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | build-and-upload opal-assets cot-rebalancer-runner | artifact sha256 equals BUILD_ONLY NFG8dbEL..; new artifact version id |  | OPEN |
| L2 | activation | safe-apply -target=module.cot_rebalancer_runner | plan code hash only; Apply complete 0/1/0 |  | OPEN |
| L3 | verify | get-function-configuration | CodeSha256 equals build sha, LastUpdateStatus Successful |  | OPEN |
| L4 | verify | 2026-10-09 06:00Z fire + 07:00Z satellites | meta/2026-10-09-result.json COMPLETE, stamp, silver fired, satellites as_of 2026-10-09 |  | OPEN |

## Log

- 20261008T161806Z OPENED by 2.0.0_SA_COO~G1 with 4 leg(s)
