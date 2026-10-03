# Deploy Completion Record
**Date opened:** 2026-10-03T20:41:33.437259+00:00
**Status:** OPEN
**Deploy:** OG-tf-2: two owner keys into gateway/principals/rosters (values from the live grant writer env, hash-compared), then the opal-gateway root plans clean from a fresh worktree
**Authored by:** 0.9.0_WK_NFRA_OPLGTW~17
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gateway/principals/rosters: mcportal_owner_key + mcportal_owner_key_claim added; sha256 equal to the live function env; the three pre-existing keys per-key sha256 unchanged | per-key hash comparison output (booleans, no value) |  | OPEN |
| L2 | verify | opal-gateway root untargeted plan from a fresh sparse worktree, no TF_VAR_* | plan rc=0, errors 0, No changes (tf2.AC1) |  | OPEN |

## Log

- 20261003T204133Z OPENED by 0.9.0_WK_NFRA_OPLGTW~17 with 2 leg(s)
