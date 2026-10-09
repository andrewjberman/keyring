# Deploy Completion Record
**Date opened:** 2026-10-09T14:43:45.881414+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-401 (AMENDMENT 3): irpt-narrative ONLY -- IB-pr-409, a no-row Opal caller classes UNKNOWN as live, the TypeError fix and the opal-capital binding kept. PIN STATED (ccbe8b8be1): pin b8a49eee0e580ebb9a80949a1e5469af7663e0e4, packet blob 0558530f80. BUILT SHA256: iEwSFL34JQJbihTmChB79GkjXwJaEl9WzMJY2sBEs4k= (built twice byte-identical, 19 packaged .py). live_before es/S9azussVLY2DfTj6hRjV1pqhZ8EaVCnaVcELqhPc=; Branch B is S3 version ELQQZdHYUJHbDZSOxC2AAKQ_nXFqApoJ, whose content-sha256 IS that live value. The stopped IB-pr-399 build QiNRKpaC is VOID. Pair: COO @e4227621a6, CTO @28563e702c. Supersedes the IB-pr-399 attempt that stopped on row D2-S48.
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-upload reads, including the W264-S1 enforcer-scope arm recorded here before any write (AMENDMENT 1) | live irpt-narrative equals the order live_before; the built sha256 equals the packet twice; the 16 replay arms match the packet arm for arm; and no_row_internal_enforcer_scope reads IDENTICAL with BOTH sets recorded, its negative control firing |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-narrative.zip | head-object content-sha256 equals the built sha256 and the prior version ELQQZdHYUJHbDZSOxC2AAKQ_nXFqApoJ is retained as the Branch B rollback source |  | OPEN |
| L3 | activation | infra/aws/terraform/investor-reporting/narrative via .tools/safe-apply.sh | the plan printed LINE BY LINE against the half; any line for another resource or release is a STOP (CTO msg 2862); live CodeSha256 read back equal to built; re-plan 0-diff |  | OPEN |
| L4 | verify | the narrative census row and the criteria | the census row for narrative reads ONE (27/27, CTO condition 4), releasing the FWD-1 seat-run hold for this host; IB103-1-AC1, AC2 and AC3 PASS |  | OPEN |
| irpt-narrative | tf-lambda | module.irpt_narrative.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T144345Z OPENED by 0.7.0_AE_CloudOps~IB2 with 5 leg(s)
