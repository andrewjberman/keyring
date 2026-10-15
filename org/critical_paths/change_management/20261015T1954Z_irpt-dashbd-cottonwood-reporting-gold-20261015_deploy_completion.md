# Deploy Completion Record
**Date opened:** 2026-10-15T19:54:08.033083+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-272: APPLY the signed Cottonwood report-build pair revision 2 (packet a9cdd5b207fe): build + upload the bundle for irpt-cot-reporting-gold-lambda, ONE safe-apply creating the function, 2 roles, DISABLED schedule irpt-cot-reporting-gold-daily (plan 7/0/0), ONE dry-run event, then the backfill of the filled report values one event at a time; schedule stays DISABLED, ledger stays OPEN
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each file in the packet's section 2; packet blob, sha256 and both halves; marker scan; live absence reads; the layer read | the printed reads | tree HEAD dc6a56af94 (carries pin f25b913caf, ancestor OK; order @97f9a36e55 on box/dell2); packet git blob a7f5afe2a245bd98a896b667706ca7578e6d1949 equals the blob in the COO half's tree @7eb94ae629, sha256 a9cdd5b207fe2f856570ec2a5899da50202caa3d71555e979a2f5fc609438d3d (REVISION 2); COO half SIGNED, CTO half R2 SIGNED at it; marker scan over 37 live worktrees (denominator 37): 0 open markers name reporting-gold-iso, irpt-cot-reporting-gold, reporting-gold or filled_report_values; live: function, execution role, scheduler role, schedule irpt-cot-reporting-gold-daily and log group /aws/lambda/irpt-cot-reporting-gold-lambda ABSENT, artifact key investor-reporting/irpt-cot-reporting-gold-lambda.zip has 0 versions, filled prefix irpt/cottonwood/gold/filled_report_values/ holds 0 objects; layer irpt-performance-native-layer latest version 1 lists python3.12, its zip holds python/pyarrow/__init__.py (pyarrow 14.0.2) and it is the version irpt-cot-account-dim-lambda runs | CLOSED 20261015T195438Z |
| L2 | s3-prefix | BUILD_ONLY zip line equals the packet's 8pQOR3TN...; import smoke; then upload the key's FIRST object version; built==landed | build line, VersionId | BUILD_ONLY line 8pQOR3TN3iicEFV53N7Cs0yeensgZhPDd7zEwTZO3Z4= EQUALS the packet's value; hex sha256 f2940e4774cdde289c105579dcdec2b34c9e7a7b206613c377bcc4c1364edd9e; 19 members incl. handler.py; import smoke from a fresh directory rc 0 (negative control: the bundle without filled_report_values.py, a top-level import of the handler, fails rc 1; removing a lazily imported adapter does not, so the smoke only proves the top-level imports); UPLOAD: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-cot-reporting-gold-lambda.zip FIRST object VersionId QuNKXE7y26o9iJuLTcD.bjXcGZvAlTEl size 182268, landed bytes sha256 equals the built zip (built_equals_landed true); source map change is the entry's artifact_sha256 only | CLOSED 20261015T195719Z |
| L3 | activation | fmt, init, validate, saved plan EXACTLY 7/0/0 on the seven addresses, naming gate 0 REFUSE; then ONE safe-apply; read-backs; replan No changes | plan line, apply line, read-backs |  | OPEN |
| L4 | activation | ONE synchronous DRY-RUN event {day 2026-10-14, dry_run true}, no retry; after-read: the filled prefix still 0 objects | the REPORT line, the body, the LIST |  | OPEN |
| L5 | activation | backfill: the {} events one at a time with an after-read each until NOTHING_OWED | per-event records, final LIST |  | OPEN |

## Log

- 20261015T195408Z OPENED by 0.7.0_AE_CloudOps~DB2 with 5 leg(s)
- 20261015T195438Z LEG L1 closed: tree HEAD dc6a56af94 (carries pin f25b913caf, ancestor OK; order @97f9a36e55 on box/dell2); packet git blob a7f5afe2a245
- 20261015T195719Z LEG L2 closed: BUILD_ONLY line 8pQOR3TN3iicEFV53N7Cs0yeensgZhPDd7zEwTZO3Z4= EQUALS the packet's value; hex sha256 f2940e4774cdde289c105
