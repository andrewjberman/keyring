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
| L1 | git | tree commit and the sha256 of each file in the packet's section 2; packet blob, sha256 and both halves; marker scan; live absence reads; the layer read | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip line equals the packet's 8pQOR3TN...; import smoke; then upload the key's FIRST object version; built==landed | build line, VersionId |  | OPEN |
| L3 | activation | fmt, init, validate, saved plan EXACTLY 7/0/0 on the seven addresses, naming gate 0 REFUSE; then ONE safe-apply; read-backs; replan No changes | plan line, apply line, read-backs |  | OPEN |
| L4 | activation | ONE synchronous DRY-RUN event {day 2026-10-14, dry_run true}, no retry; after-read: the filled prefix still 0 objects | the REPORT line, the body, the LIST |  | OPEN |
| L5 | activation | backfill: the {} events one at a time with an after-read each until NOTHING_OWED | per-event records, final LIST |  | OPEN |

## Log

- 20261015T195408Z OPENED by 0.7.0_AE_CloudOps~DB2 with 5 leg(s)
