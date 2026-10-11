# Deploy Completion Record
**Date opened:** 2026-10-09T17:26:50.024420+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T174139Z
**Deploy:** IRPT_DASHBD DB-b-112: gold Lambda irpt-49f-reporting-gold-lambda memory_size 2048 -> 3008, the setting only, signed against packet sha256 f1cc6068e9fc1fcd1daef3ce1a0fede9c30501b2b486c900f9f1a19940ed0ec8 (COO half @ca40177794, CTO half msg 3789); code oNgy4rnr unchanged; one targeted apply, one dry run as after-proof, rollback to 2048 on OVER
**Authored by:** 0.9.0_WK_IRPT_DASHBD~87
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P1 | verify | before read (CodeSha256 oNgy4rnr, MemorySize 2048) and targeted plan on lambda.tf line 59 | Plan: 0 to add, 1 to change, 0 to destroy with memory_size the only changed attribute | before read 2026-10-09 CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= MemorySize 2048 Timeout 900 Active/Successful; lambda.tf line 59 set to 3008; targeted plan 'Plan: 0 to add, 1 to change, 0 to destroy.' with memory_size 2048 -> 3008 the only changed attribute (plan text MEMSTEP_PLAN_OUTPUT.txt) | CLOSED 20261009T172917Z |
| A1 | activation | one safe-apply of the saved plan, infra/aws/terraform/investor-reporting/reporting-gold | Apply complete, 1 changed | SAFE_APPLY_TERRAFORM=main terraform.exe HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/reporting-gold apply memstep.tfplan: rc 0, 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' at 2026-10-09T17:32:02Z | CLOSED 20261009T173255Z |
| V1 | verify | readback MemorySize 3008, CodeSha256 oNgy4rnr, post-apply plan No changes | get-function-configuration plus No changes | get-function-configuration MemorySize 3008, CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= unchanged, Active/Successful; post-apply targeted plan 'No changes. Your infrastructure matches the configuration.' | CLOSED 20261009T173255Z |
| R1 | verify | ONE dry-run 2026-10-08 under 3008 against 85pct lines 765000 ms and 2556.8 MB, written objects 0 | REPORT line Duration and Max Memory Used, 0 objects written | ONE dry-run 2026-10-08 under 3008 on live oNgy4rnr (request ecfbecbd-79d6-48d6-92d0-8ea726e8b11d, 7620 accounts, 0 objects written of 2873 listed, positive control 23): REPORT Duration 277355.56 ms vs 765000 ms line (30.8 pct of 900 s), Max Memory Used 1672 MB vs 2556.8 MB line (55.6 pct of 3008 MB) -> UNDER both | CLOSED 20261009T174139Z |

## Log

- 20261009T172650Z OPENED by 0.9.0_WK_IRPT_DASHBD~87 with 4 leg(s)
- 20261009T172917Z LEG P1 closed: before read 2026-10-09 CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= MemorySize 2048 Timeout 900 Active/Succes
- 20261009T173255Z LEG A1 closed: SAFE_APPLY_TERRAFORM=main terraform.exe HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/re
- 20261009T173255Z LEG V1 closed: get-function-configuration MemorySize 3008, CodeSha256 oNgy4rnrduvN9N2axhsHBfe9izZKd8dZGeFGXAIh+cM= unchanged, Active/Su
- 20261009T174139Z LEG R1 closed: ONE dry-run 2026-10-08 under 3008 on live oNgy4rnr (request ecfbecbd-79d6-48d6-92d0-8ea726e8b11d, 7620 accounts, 0 objec
- 20261009T174139Z CLOSED -- all 4 legs proven
