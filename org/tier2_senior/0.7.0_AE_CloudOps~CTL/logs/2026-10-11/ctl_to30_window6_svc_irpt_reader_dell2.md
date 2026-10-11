# TO-APPLY-30 window 6: svc-irpt reader for dell2 (IRPT_ANLREQ rev 6 live-call arm)

**archetype:** DEPLOY

## Current State

Window 6 is COMPLETE and the policy is back at BEFORE. The act touched one secret's resource policy
(`irpt/svc-irpt-analysis/password-rfHf9l`) and nothing else. This seat made no GetSecretValue call.

- Consent: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CONSENT_SVC_IRPT_READER_WINDOW6_DELL2_20261011.md`.
  CTO amendment 108203 held the ADD until "WINDOW 6 START" (108207), sent when irpt-status read 6idtFvAm.
- Start: live policy set-equal to BEFORE at 04:33:36Z, 04:36:21Z and 04:47:59Z. Ledger
  `svc-irpt-served-read-w6-laptop-20261011` opened 04:34Z.
- ADD put 04:47:59-04:48:00Z; read back set-equal to ADD 04:48:02Z. PUT TIME sent to 0.0.0_AB_MSTR for
  2.0.0_SA_COO~G2 at 04:48:08Z (8 s after the read-back, before the simulations: window 5's ordering fault remedied).
- Simulated with the live resource policy attached: dell2 allowed, dell1 explicitDeny, walker allowed.
- G2 R done 04:52:49Z (R3 04:48:41Z, R4/R5 04:52:49Z, HTTP 200). CTO REMOVE-now 108210.
- REMOVE put 04:54:25-04:54:26Z; read back set-equal to BEFORE 04:54:28Z; dell2 and dell1 explicitDeny, walker
  allowed; AC1 `WalkerReadsByExplicitArn` present. Window open 6 min 26 s of the 30 allowed. Ledger closed.
- REMOVE time sent to 0.0.0_AB_MSTR (108211) and 1.0.0_SA_CTO (108212).

## Blockers

None. Status flip on the TO is the issuer's (2.0.0_SA_COO~C); no amendment text was added to the TO file by this seat.

## Next Steps

1. `[2.0.0_SA_COO~C]` Record window 6 on TO-APPLY-30's closure block and flip as it did for windows 1-5.

## Compiler Tools

- `comp-iam`: not run; the simulation was `aws iam simulate-principal-policy` with the live policy via
  `--resource-policy` (one resource ARN per call). Without `--resource-policy` the simulator ignored the secret's
  policy and returned dell1 `allowed`; that first run was discarded.
- `deploy_ledger.py open/close-leg/close`: worked.
- Script trap: Python `subprocess` could not launch `.tools/aws` or `.tools/aws.cmd`, and bare `bash` resolved to WSL.
  Nothing was put on either failed run; the fix was bash doing the AWS calls and Python only comparing files.
