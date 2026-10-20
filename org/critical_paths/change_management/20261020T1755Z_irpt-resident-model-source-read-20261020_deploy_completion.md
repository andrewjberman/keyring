# Deploy Completion Record
**Date opened:** 2026-10-20T17:55:27.373528+00:00
**Status:** CLOSED -- STOPPED AT C, NOTHING APPLIED (terraform fmt -check resident.tf rc 3 at the pin 50f7c709af2: three misaligned lines in the added statement; the live policy is unchanged) -- closed 20261020T180550Z
**Deploy:** IRPT_ANLREQ TO-APPLY-MODELGRANT: one-statement IAM grant (s3:GetObject on two exact keys of opal-data-portal-v2) on aws_iam_role_policy.runner_resident for the resident host role
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R0 | verify | before-reads: live policy sid list and sha256, four baseline simulations | R0 baseline implicitDeny on all four | R0 baseline implicitDeny on all four at 2026-10-20T17:57Z: 14 Sids, ReadTheModelReturnSeriesAndPositioning absent; GetObject on both keys and a third key, PutObject on the first key all implicitDeny; control: PutObject on a ycharts_opal_reports key allowed (the simulator can say allowed); open-deploys denominator 52 worktrees, 145 distinct entries, no open entry on the ycharts stack, the role or its policy (one HELD-SOVEREIGN-GATED a18 read-evidence reference) | CLOSED 20261020T180026Z |
| C | verify | scoped plan at the pin 50f7c709af2 reads 0 to add 1 to change 0 to destroy with exactly one added statement | plan output and diff read | C STOPPED, not green: terraform fmt -check resident.tf rc 3 at the pin 50f7c709af2 (three misaligned lines in the added statement, whitespace only; parent passes); an informational scoped plan read 0 to add 1 to change 0 to destroy with exactly one added statement; order step 3 says STOP, nothing applied | CLOSED 20261020T180550Z |
| A | activation | safe-apply of the saved plan | Apply complete 0 added 1 changed 0 destroyed | NOT-RUN: nothing applied (stopped at step 3); live policy sha256 7038867f... re-read equal to R0 | CLOSED 20261020T180550Z |
| V | verify | after-reads G1 to G4: byte-equal other statements, simulation, replan No changes, host-role reads of both objects | G1 G2 G3 G4 lines | NOT-RUN: nothing applied, so no after-reads G1 to G4 | CLOSED 20261020T180550Z |

## Log

- 20261020T175527Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T180026Z LEG R0 closed: R0 baseline implicitDeny on all four at 2026-10-20T17:57Z: 14 Sids, ReadTheModelReturnSeriesAndPositioning absent; GetOb
- 20261020T180550Z LEG C closed: C STOPPED, not green: terraform fmt -check resident.tf rc 3 at the pin 50f7c709af2 (three misaligned lines in the added 
- 20261020T180550Z LEG A closed: NOT-RUN: nothing applied (stopped at step 3); live policy sha256 7038867f... re-read equal to R0
- 20261020T180550Z LEG V closed: NOT-RUN: nothing applied, so no after-reads G1 to G4
- 20261020T180550Z CLOSED -- all 4 legs proven
