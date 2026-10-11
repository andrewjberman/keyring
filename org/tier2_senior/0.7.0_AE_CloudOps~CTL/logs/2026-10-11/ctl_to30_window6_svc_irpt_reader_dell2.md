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

## Window 7 (same session, same terms, no start hold)

**archetype:** DEPLOY

Consent `CTO_CONSENT_SVC_IRPT_READER_WINDOW7_DELL2_20261011.md`, GO msg 108221. Ledger
`svc-irpt-served-read-w7-laptop-20261011` opened 05:25Z. Live == BEFORE at 05:25:51Z and 05:26:00Z.
ADD put 05:26:00-05:26:01Z, read back set-equal to ADD 05:26:03Z, PUT TIME to MSTR 05:26:09Z (6 s after the
read-back). Simulated with the live policy attached: dell2 allowed, dell1 explicitDeny, walker allowed.
G2 R done 05:29:50Z (one GET, HTTP 200). REMOVE put 05:31:09-05:31:11Z on CTO 108225, read back set-equal to
BEFORE 05:31:13Z, dell2 and dell1 explicitDeny, walker allowed, AC1 present. Window open 5 min 10 s. Ledger
closed. REMOVE time sent to MSTR (108226) and the CTO (108227). No GetSecretValue by this seat.
Next: `[2.0.0_SA_COO~C]` record windows 6 and 7 on TO-APPLY-30's closure block.

## Window 8 (same terms, no start hold, ONE GET: 257-section census through the served read)

**archetype:** DEPLOY

Consent `CTO_CONSENT_SVC_IRPT_READER_WINDOW8_DELL2_20261011.md`, GO msg 108237. Ledger
`svc-irpt-served-read-w8-laptop-20261011` opened 07:07Z. Live == BEFORE at 07:08:17Z and 07:08:26Z.
ADD put 07:08:26-07:08:28Z, read back set-equal to ADD 07:08:30Z, PUT TIME to MSTR 07:08:35Z (5 s after the
read-back). Simulated with the live policy attached: dell2 allowed, dell1 explicitDeny, walker allowed.
G2 R done 07:13:59Z. REMOVE put 07:16:18-07:16:19Z on the CTO R-DONE (108242), read back set-equal to BEFORE
07:16:21Z, dell2 and dell1 explicitDeny, walker allowed, AC1 present. Window open 7 min 51 s. Ledger closed.
REMOVE time sent to MSTR (108244) and the CTO (108245). No GetSecretValue by this seat.
Next: `[2.0.0_SA_COO~C]` record windows 6, 7 and 8 on TO-APPLY-30's closure block.
