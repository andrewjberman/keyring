# Deploy Completion Record
**Date opened:** 2026-10-03T05:38:41.838078+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T055336Z
**Deploy:** Y-4 enrichment, re-packet (CTO batch 208): the runner's Kimi read narrowed at its ONE carrier (both statements) and the resident st17 -> st18 (gate total 240 s); U2 reused from irpt-y4e-20261003
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D3 | activation | ONE targeted safe-apply of aws_iam_role_policy.runner and aws_iam_role_policy.runner_resident (local.kimi_secret_arn -> api-key-??????) | both policies read back; IAM simulation with MatchedStatements: exact secret allowed, sibling implicitDeny | CTO half batch 209 (msg 104554) on blob 157d88794d; before-read 05:47:31Z; re-plan 2 to change, 2 values; safe-apply rc=0; both policies read back astn/kimi/api-key-?????? (login/session unchanged); simulation 05:51:23Z: estate secret allowed matched by irpt-ycharts-runner AND irpt-ycharts-runner-resident-policy, sibling implicitDeny matched none (Y4E/IAM_SIMULATION_REPACKET_AFTER_20261003.txt) | CLOSED 20261003T055204Z |
| D2 | activation | resident install via SSM (root a6f6e7165e-st18, U2 of irpt-y4e-20261003) | running root, digests equal git, unit active, queue 0/0 | head-object script g6Lx_XPK..; Y4E/install_fetch_and_run.sh over SSM rc=0 at 05:52:45Z; running root /opt/irpt-resident/a6f6e7165e-st18; unit active since 05:52:20Z, NRestarts=0; queue 0/0; SSM sha256 of resolution_kimi, upload_suggestions, resident_worker, ops/entry, ops/owned_requests equal git a6f6e7165e 5 of 5 (Y4E/D2_DIGESTS_VS_GIT_Y4E2_20261003.txt) | CLOSED 20261003T055335Z |
| V1 | verify | journal field and IAM after D3+D2 | installed worker carries unasked/elapsed_s; the live typo run rides irpt-y4-20261003 V1 after option A | installed worker carries the journal field (unasked= mentions 1) and TOTAL_SUGGEST_SECONDS = 240 [1]; KIMI_DEADLINE_INVALID [1]; IAM stop met (estate allowed by both policies, sibling implicitDeny). The live typo run and the gate's elapsed seconds ride irpt-y4-20261003 V1 after option A | CLOSED 20261003T055335Z |

## Log

- 20261003T053841Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261003T055204Z LEG D3 closed: CTO half batch 209 (msg 104554) on blob 157d88794d; before-read 05:47:31Z; re-plan 2 to change, 2 values; safe-apply rc=
- 20261003T055335Z LEG D2 closed: head-object script g6Lx_XPK..; Y4E/install_fetch_and_run.sh over SSM rc=0 at 05:52:45Z; running root /opt/irpt-resident/
- 20261003T055335Z LEG V1 closed: installed worker carries the journal field (unasked= mentions 1) and TOTAL_SUGGEST_SECONDS = 240 [1]; KIMI_DEADLINE_INVA
- 20261003T055336Z CLOSED -- all 3 legs proven
