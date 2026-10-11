# The packager token is minted, stored as one secret and readable by the resident host's role only -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-11
**Task Order:** crossbox ORDER XB-20261011T163203Z-3fc2 (IRPT_ANLREQ attach cell 2b)
**Status:** COMPLETE

---

## Objective

Under dell2's never-widen pair and the laptop CTO's consent, grant `irpt-ycharts-runner-role` one `secretsmanager:GetSecretValue` on one secret, mint one RS256 service token for `svc-irpt-packager` (no firm claim, 90 days), store it as `opal/ticketing/svc-irpt-packager`, and show by six simulates who can read it.

## What was done

- Acked the order; matched all four pins (ask `2b8683578c`, COO half `5a202040cd`, CTO half `88debba439`, consent `84beb91165`).
- BEFORE: three simulates, implicitDeny on the runner role, the drafter role and `agentbus-alyssa01-fleet-andrew-role`. `user/Andrew_Berman` read allowed (an administrator); it was not used as the agent identity and is filed as row `IRPT_ANLREQ-S1`.
- Opened the NEVER-2 ledger `irpt-packager-mint-20261011`; baseline plan in the `ycharts` root: No changes.
- GRANT: `resident.tf` gains Sid `ReadThePackagerServiceToken`, commit `b7c67d3ac8`; plan 0 add, 1 change, 0 destroy; `.tools/safe-apply.sh` with the saved plan; post-apply plan No changes; live policy holds the statement.
- MINT and SECRET: `pk_mint/mint_packager.py --go`; claim names `aud exp iat iss name sub tier userType`; exp 2027-01-09T16:43:55Z; the token was never printed or written. Secret ARN suffix `JEkpSP`.
- AFTER: on the real ARN, allowed on the runner role only; the pattern string with a literal `*` reads implicitDeny for all three (a false deny of the instrument, recorded in the return).
- Ledger closed with all five legs proven. Return: `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/PACKAGER_MINT_RETURN_XB-20261011T163203Z-3fc2.md`.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | none | SKIPPED | the order names iam simulate-principal-policy as its instrument; no new boto3 call in a Lambda |
| iam simulate-principal-policy | six simulates, one resource per call, plus an admin control | PASS | read the real ARN after the secret existed |
| terraform plan / safe-apply | `ycharts` root | PASS | 0 add, 1 change, 0 destroy; then No changes |

**What worked:** simulating the real ARN after creation, paired with a describe-secret of that exact name.
**What failed:** the `-*` pattern ARN reads implicitDeny against a `-??????` policy resource, so it cannot show the grant.
**Gap found:** the laptop's agent sessions run as an administrator user, so "no agent can read the secret" is not checkable by a role simulate alone (row `IRPT_ANLREQ-S1`).
