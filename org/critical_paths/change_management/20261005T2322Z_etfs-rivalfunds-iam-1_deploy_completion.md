# Deploy Completion Record
**Date opened:** 2026-10-05T23:22:54.491135+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T000014Z
**Deploy:** ETFS_RIVALS RIV-iam-1 (row Z-S31): grant gold/security_names READ + gold/security_universe READ/WRITE to etfs-rivalfunds-daily-role and rivalfunds-publish-page-role
**Authored by:** 0.7.0_AE_CloudOps~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the gen_policies.py + two regenerated role-policy JSONs committed on branch ae-rv10-iam1 (drains to CLOUD) | commit hash | commit 762a984992 on branch ae-rv10-iam1 (gen_policies.py + both regenerated role-policy JSONs + this entry's sentinel, 5 files); CLOUD merged in at fec8fb400b to carry the order amendment 2553a624f7; the branch drains to CLOUD in the same act as this close, per the CTO half condition 4 | CLOSED 20261006T000014Z |
| L2 | activation | safe-apply of the saved plan C:/tmp/rv-iam1.tfplan -- 2 aws_iam_role_policy.stage updates, 0 add, 0 destroy | apply output + aws iam get-role-policy showing both prefixes | safe-apply of the signed saved plan C:/tmp/rv-iam1.tfplan from the pin worktree: comp-tagauthz GATE PASSED (0 candidates overwrite an access-granting tag), tombstone-gate CLEAN (0 creates vs 7 tombstones), then 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed' -- aws_iam_role_policy.stage[etfs-rivalfunds-daily-lambda] and [rivalfunds-publish-page-lambda] Modifications complete. CONDITION 1 held: the re-plan immediately before the apply carried the IDENTICAL moving set (2 updates, 45 resource_changes) | CLOSED 20261006T000014Z |
| L3 | verify | iam-1.AC1 simulate on both live roles reads PASS 0 failures, and a re-plan reads 0-diff | AC1 RESULT line + plan text | AC1 RESULT: PASS 0 failures on both roles -- (a) names list+get allowed, (b) universe put+get allowed, (c) the security_names-put and sibling-prefix controls still implicitDeny, (d) holding_contribution positive control allowed; base read was FAIL 4 on the same calls. Re-plan post-apply: 'No changes. Your infrastructure matches the configuration', detailed-exitcode 0, 45 resource_changes / 0 non-no-op. Live readback: get-role-policy on both roles equals the AFTER documents key-sorted (10/10 and 5/5 statements), ADDED 4 REMOVED 0 per role. Controls: accessanalyzer validate-policy 0 findings on both live documents with a planted bogus action returning INVALID_ACTION; AC1 re-run gave identical verdicts | CLOSED 20261006T000014Z |

## Log

- 20261005T232254Z OPENED by 0.7.0_AE_CloudOps~RV with 3 leg(s)
- 20261006T000014Z LEG L1 closed: commit 762a984992 on branch ae-rv10-iam1 (gen_policies.py + both regenerated role-policy JSONs + this entry's sentinel, 
- 20261006T000014Z LEG L2 closed: safe-apply of the signed saved plan C:/tmp/rv-iam1.tfplan from the pin worktree: comp-tagauthz GATE PASSED (0 candidates
- 20261006T000014Z LEG L3 closed: AC1 RESULT: PASS 0 failures on both roles -- (a) names list+get allowed, (b) universe put+get allowed, (c) the security_
- 20261006T000014Z CLOSED -- all 3 legs proven
