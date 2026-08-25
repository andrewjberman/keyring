# Deploy Completion Record
**Date opened:** 2026-07-24T13:39:02.499124+00:00
**Status:** CLOSED 2026-08-25T03:55:21Z -- all legs proven, nothing stranded
**Deploy:** Stage the CTO-decided NNA excusals manifest @8ba56144e to the inf gold runner prefix (committed 07-23, never staged; runner carried the 1-account 2026-07-17 manifest). DECIDING AUTHORITY: 1.0.0_SA_CTO per the 150205Z ruled path exit (i), Andrew-direct raw-fact grounding 2026-07-23 (vendor cancelDate/isActive=false/currentValue=0.0 on all four accounts). GO: CTO 133738Z option (a), five conditions. Executes an already-recorded decision; no tolerance widened.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | s3://opal-data-inf/code/gold/lib/nna_coverage_excusals.json | POST-CP landed-bytes re-read: s3api head-object ETag+ContentLength == local md5 234d6cc4a8aeb8f30c18836e0b721cca / 4593 B (CTO condition 2: rc=0 and --quiet are NOT proof; aws-shim silent-hang class) | LANDED + VERIFIED 2026-07-24T13:39:36Z. Pre-cp control: old object still ETag 5c60c95231dd51fa9b82d21ca49bae70 / 769 B / 2026-07-17T17:24:57Z (nothing changed under me). Post-cp s3api head-object: ETag 234d6cc4a8aeb8f30c18836e0b721cca / ContentLength 4593 / 2026-07-24T13:39:36Z == local md5+size EXACTLY. Independent re-download + diff vs repo HEAD: BYTE-IDENTICAL (not an ETag-only inference; rc=0 and --quiet were NOT relied on, per CTO condition 2 / aws-shim silent-hang class). Semantic read of the LANDED body: excused_accounts = 237,560,609,703,1225 (five), every entry decided_by 1.0.0_SA_CTO (237 dated 2026-07-17; the four new dated 2026-07-23). Landed BEFORE the gold stage window (~14:0x-14:5xZ). No ad-hoc run triggered (NEVER#4). | CLOSED 20260724T134056Z |
| L2 | verify | INF_C_01 behavior on TODAY'S SCHEDULED gold run (no ad-hoc trigger, NEVER#4) | EXERCISED evidence (Rule 22a): gold/meta/pipeline-complete.json advances off its 2026-07-18T14:59:10Z freeze, vs pipeline-failed.json advancing instead. A staged file is DESIRED-state only. | MEASURED 2026-08-25T03:55Z by 0.7.0_AE_CloudOps~Z, against THIS LEG'S OWN STATED REQUIREMENT. gold/meta/pipeline-complete.json LastModified 2026-08-24T12:43:33Z, 135 B -- ADVANCED off the 2026-07-18T14:59:10Z freeze by 37 days. The rival this leg named (pipeline-failed.json advancing INSTEAD) is FALSIFIED: failed.json LastModified 2026-08-11T06:18:42Z, 14 days STALE, i.e. not advancing. NEVER#1 APPLIED BEFORE THE VERDICT: expected_last_trading_day at 2026-08-25T03:55Z is 2026-08-25; complete.json at 2026-08-24 is T-1 = HEALTHY, not stale. The staged excusals manifest took effect and INF_C_01 behaved. DESIRED (L1, staged+byte-verified 07-24) is now matched by EXERCISED (L2, the scheduled pipeline recovering). | CLOSED 20260825T035521Z |

## Log

- 20260724T133902Z OPENED by 0.7.0_AE_CloudOps with 2 leg(s)
- 20260724T134056Z LEG L1 closed: LANDED + VERIFIED 2026-07-24T13:39:36Z. Pre-cp control: old object still ETag 5c60c95231dd51fa9b82d21ca49bae70 / 769 B /
- 20260825T035521Z LEG L2 closed by 0.7.0_AE_CloudOps~Z: MEASURED 2026-08-25T03:55Z by 0.7.0_AE_CloudOps~Z, against THIS LEG'S OWN STATED REQUIREMENT. gold/meta/pipeline-complete.json LastModified 2026-08-24T12:43:33Z, 135 B -- ADVANCED off the 2026-07-18T14:59:10Z freeze by 37 days. The rival this leg named (pipeline-failed.json advancing INSTEAD) is FALSIFIED: failed.json LastModified 2026-08-11T06:18:42Z, 14 days STALE, i.e. not advancing. NEVER#1 APPLIED BEFORE THE VERDICT: expected_last_trading_day at 2026-08-25T03:55Z is 2026-08-25; complete.json at 2026-08-24 is T-1 = HEALTHY, not stale. The staged excusals manifest took effect and INF_C_01 behaved. DESIRED (L1, staged+byte-verified 07-24) is now matched by EXERCISED (L2, the scheduled pipeline recovering).
- 20260825T035521Z LEDGER CLOSED. Found during a full-corpus census (536 files) after retracting a FALSE open-ledger report about a different ledger of mine. L1 was closed 07-24; L2 sat OPEN 32 days past a 6.0h window with its RED alarm never firing -- the entry is hand-authored and therefore outside the tool index that would have swept it. THE DEPLOY WAS COMPLETE IN SUBSTANCE ON 07-24 AND THE RECORD DID NOT SAY SO.
