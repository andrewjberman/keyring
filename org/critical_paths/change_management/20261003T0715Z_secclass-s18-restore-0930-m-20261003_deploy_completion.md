# Deploy Completion Record
**Date opened:** 2026-10-03T07:15:22.422417+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS-S18 disarm: BD served state back to as_of 09-30 (CTO batch 213 item 1; CTO half CTO_HALF_S18_RESTORE_0930_SERVED_20261003.md @5ec7db4eea; next fire ruled batch 219: (a) hold + (b) watermark reset)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| 0 | verify | runner stopped; no BD gold fire during the act | describe-instances + rule schedules | 07:1xZ: runner i-01003b035d2988dfb stopped (describe-instances); the BD gold fires are bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) and bd-canonical-prices-daily cron(0 4 * * ? *) (both target bd-gold-trigger, list-rule-names-by-target; the monthly rule is DISABLED), so no fire runs before 23:00Z. | CLOSED 20261003T071628Z |
| C | s3-prefix | copy-object of 23,542 served keys to their pre-04:00Z VersionIds (S18_RESTORE_SET_20261003.tsv), read back per key; 36 run-created keys left | restore result counts + read-back |  | OPEN |
| V | verify | served read: platinum/firm/mix_summary.json data_as_of 2026-09-30 at 1,843,114,311.70; one 335-set account's served AUA at its 09-30 value | served key reads |  | OPEN |
| H | activation | disable bd-gold-nightly-fallback and bd-canonical-prices-daily before 23:00Z; read back State DISABLED | describe-rule x2 | 07:17Z aws events disable-rule, read back by describe-rule: bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) State DISABLED; bd-canonical-prices-daily cron(0 4 * * ? *) State DISABLED (both target bd-gold-trigger; the monthly rule was already DISABLED). Done by CLI as an operational hold: the Terraform state of these rules now differs from live until leg R re-enables them -- no apply of their root before leg R. | CLOSED 20261003T071810Z |
| R | activation | when the class cell lands: watermarks to 09-30 and the two rules re-enabled before Monday 04:00Z (else report by Sunday 18:00Z) | watermark reads + describe-rule x2 |  | OPEN |

## Log

- 20261003T071522Z OPENED by 2.0.0_SA_COO~M with 5 leg(s)
- 20261003T071628Z LEG 0 closed: 07:1xZ: runner i-01003b035d2988dfb stopped (describe-instances); the BD gold fires are bd-gold-nightly-fallback cron(0 2
- 20261003T071810Z LEG H closed: 07:17Z aws events disable-rule, read back by describe-rule: bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) State DISA
