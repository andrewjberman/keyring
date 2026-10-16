# Deploy Completion Record
**Date opened:** 2026-10-16T06:26:49.838912+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T062825Z
**Deploy:** MDPF_SECCLASS SC-e-107 (TO-SC-e107b): seed22.py apply writes 13 NEW keys into etf-classifications by conditional put (never overwrites); 9 held-out not written. Pair: CTO half @7b166cf360 SIGNED, COO half SIGNED, request sha256 737e43a0. Rollback: delete exactly the 13 keys with ConditionExpression source_table = 'bd-securities'. Leg G is the issuer's.
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A | verify | dynamodb etf-classifications (us-east-1) 13 new keys | SEED22-APPLY written=13 refused=0 | E107_ACT_20261016.out: SEED22-APPLY written=13 refused=0 at 06:27:08Z (seed22.py sha256 84e77caf.., plan sha256 5337b6ba.., pair = CTO half SIGNED); window read in the same shell: bd-gold-layer-runner pending/running/stopping=0, gold/trigger-pending.json ABSENT | CLOSED 20261016T062824Z |
| B | verify | e107_seeded_check.py and the 200-key census | E107-SEEDED ok=True present=13/13 absent_ok=9/9 and no last_updated moved | E107_ACT_20261016.out: e107_seeded_check.py E107-SEEDED ok=True present=13/13 absent_ok=9/9 problems=[]; get_item of each of the 200 pre-act census keys: 0 missing, 0 last_updated moved; scan 11362 -> 11375; served mix summaries' VersionIds unchanged | CLOSED 20261016T062825Z |

## Log

- 20261016T062649Z OPENED by 0.7.0_AE_CloudOps~SC1 with 2 leg(s)
- 20261016T062824Z LEG A closed: E107_ACT_20261016.out: SEED22-APPLY written=13 refused=0 at 06:27:08Z (seed22.py sha256 84e77caf.., plan sha256 5337b6ba
- 20261016T062825Z LEG B closed: E107_ACT_20261016.out: e107_seeded_check.py E107-SEEDED ok=True present=13/13 absent_ok=9/9 problems=[]; get_item of eac
- 20261016T062825Z CLOSED -- all 2 legs proven
