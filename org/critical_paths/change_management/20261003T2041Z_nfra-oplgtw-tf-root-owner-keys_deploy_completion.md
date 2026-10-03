# Deploy Completion Record
**Date opened:** 2026-10-03T20:41:33.437259+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T210156Z
**Deploy:** OG-tf-2: two owner keys into gateway/principals/rosters (values from the live grant writer env, hash-compared), then the opal-gateway root plans clean from a fresh worktree
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gateway/principals/rosters: mcportal_owner_key + mcportal_owner_key_claim added; sha256 equal to the live function env; the three pre-existing keys per-key sha256 unchanged | per-key hash comparison output (booleans, no value) | write_keys.py (in memory, no value printed): rosters secret 3 -> 5 keys; previous VersionId e018dce9 (AWSPREVIOUS, rollback), new 2b1dc776; per-key sha256 of master_admin, write_capable, taxsma_workbook_identity unchanged (True x3); owner_key and owner_key_claim sha256 equal to the live mcportal-grant-writer-lambda env (True, True); tf2.AC2 RESULT: PASS | CLOSED 20261003T210156Z |
| L2 | verify | opal-gateway root untargeted plan from a fresh sparse worktree, no TF_VAR_* | plan rc=0, errors 0, No changes (tf2.AC1) | tf2.AC1 at df3e0e2c06: plan rc=0; errors 0; missing required variables 0; No changes. Your infrastructure matches the configuration.; untargeted plan reads No changes: yes (the helper's own RESULT line reads FAIL by its grep -c \|\| echo 0 defect, row Z-W17-S7) | CLOSED 20261003T210156Z |

## Log

- 20261003T204133Z OPENED by 0.9.0_WK_NFRA_OPLGTW~17 with 2 leg(s)
- 20261003T210156Z LEG L1 closed: write_keys.py (in memory, no value printed): rosters secret 3 -> 5 keys; previous VersionId e018dce9 (AWSPREVIOUS, rollb
- 20261003T210156Z LEG L2 closed: tf2.AC1 at df3e0e2c06: plan rc=0; errors 0; missing required variables 0; No changes. Your infrastructure matches the co
- 20261003T210156Z CLOSED -- all 2 legs proven
