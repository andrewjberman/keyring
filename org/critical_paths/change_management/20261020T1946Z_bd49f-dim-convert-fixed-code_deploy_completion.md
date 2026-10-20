# Deploy Completion Record
**Date opened:** 2026-10-20T19:46:41.533219+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T195646Z
**Deploy:** bd49f dim-convert fixed-code deploy, SCD2 schema-typed comparison, no invoke (NFRA_CTLPLN TO-APPLY-35)
**Authored by:** 0.7.0_AE_CloudOps~NFRA2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-assets-bd49f-dim-convert | tf-lambda | module.bd49f_convert.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | artifact version e1QAG_MImQG4spPuHu8kmBA4ZjMIByAD (sha Iosob5...) -> 38_BbBXe67zW2t.11apDUB6_.W619ln0 (sha blu8AGfkLFODrFvcNY7MKpk5INoT6LnyKG96pg7F1P8=); safe-apply -target 0 added 1 changed 0 destroyed; targeted replan No changes; CodeSha256 after = zip sha; MemorySize 3008 Timeout 900; deployed bd49f_dim_conversion.py sha256 bc3019570d49ac1ee10d7cd7668dfdc23a09e938d14dece7abd7c662cf00d503 equals pin, mutant unequal; seam probe on deployed bytes newly_closed=0 of 5338, control 1; prior bytes 5338; record d5b8527acb tag opal-assets-v0.52.0 LOCAL | CLOSED 20261020T195646Z |

## Log

- 20261020T194641Z OPENED by 0.7.0_AE_CloudOps~NFRA2 with 1 leg(s)
- 20261020T195646Z LEG opal-assets-bd49f-dim-convert closed: artifact version e1QAG_MImQG4spPuHu8kmBA4ZjMIByAD (sha Iosob5...) -> 38_BbBXe67zW2t.11apDUB6_.W619ln0 (sha blu8AGfkLFODr
- 20261020T195646Z CLOSED -- all 1 legs proven
