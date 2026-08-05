# Deploy Completion Record
**Date opened:** 2026-07-24T13:39:02.499124+00:00
**Status:** OPEN
**Deploy:** Stage the CTO-decided NNA excusals manifest @8ba56144e to the inf gold runner prefix (committed 07-23, never staged; runner carried the 1-account 2026-07-17 manifest). DECIDING AUTHORITY: 1.0.0_SA_CTO per the 150205Z ruled path exit (i), Andrew-direct raw-fact grounding 2026-07-23 (vendor cancelDate/isActive=false/currentValue=0.0 on all four accounts). GO: CTO 133738Z option (a), five conditions. Executes an already-recorded decision; no tolerance widened.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json | POST-CP landed-bytes re-read: s3api head-object ETag+ContentLength == local md5 234d6cc4a8aeb8f30c18836e0b721cca / 4593 B (CTO condition 2: rc=0 and --quiet are NOT proof; aws-shim silent-hang class) | LANDED + VERIFIED 2026-07-24T13:39:36Z. Pre-cp control: old object still ETag 5c60c95231dd51fa9b82d21ca49bae70 / 769 B / 2026-07-17T17:24:57Z (nothing changed under me). Post-cp s3api head-object: ETag 234d6cc4a8aeb8f30c18836e0b721cca / ContentLength 4593 / 2026-07-24T13:39:36Z == local md5+size EXACTLY. Independent re-download + diff vs repo HEAD: BYTE-IDENTICAL (not an ETag-only inference; rc=0 and --quiet were NOT relied on, per CTO condition 2 / aws-shim silent-hang class). Semantic read of the LANDED body: excused_accounts = 237,560,609,703,1225 (five), every entry decided_by 1.0.0_SA_CTO (237 dated 2026-07-17; the four new dated 2026-07-23). Landed BEFORE the gold stage window (~14:0x-14:5xZ). No ad-hoc run triggered (NEVER#4). | CLOSED 20260724T134056Z |
| L2 | verify | INF_C_01 behavior on TODAY'S SCHEDULED gold run (no ad-hoc trigger, NEVER#4) | EXERCISED evidence (Rule 22a): gold/meta/pipeline-complete.json advances off its 2026-07-18T14:59:10Z freeze, vs pipeline-failed.json advancing instead. A staged file is DESIRED-state only. |  | OPEN |

## Log

- 20260724T133902Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260724T134056Z LEG L1 closed: LANDED + VERIFIED 2026-07-24T13:39:36Z. Pre-cp control: old object still ETag 5c60c95231dd51fa9b82d21ca49bae70 / 769 B /
