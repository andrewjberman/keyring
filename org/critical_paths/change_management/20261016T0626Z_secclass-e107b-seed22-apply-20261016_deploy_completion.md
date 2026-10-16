# Deploy Completion Record
**Date opened:** 2026-10-16T06:26:49.838912+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-107 (TO-SC-e107b): seed22.py apply writes 13 NEW keys into etf-classifications by conditional put (never overwrites); 9 held-out not written. Pair: CTO half @7b166cf360 SIGNED, COO half SIGNED, request sha256 737e43a0. Rollback: delete exactly the 13 keys with ConditionExpression source_table = 'bd-securities'. Leg G is the issuer's.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | dynamodb etf-classifications (us-east-1) 13 new keys | SEED22-APPLY written=13 refused=0 |  | OPEN |
| B | verify | e107_seeded_check.py and the 200-key census | E107-SEEDED ok=True present=13/13 absent_ok=9/9 and no last_updated moved |  | OPEN |

## Log

- 20261016T062649Z OPENED by 0.7.0_AE_CloudOps~SC1 with 2 leg(s)
