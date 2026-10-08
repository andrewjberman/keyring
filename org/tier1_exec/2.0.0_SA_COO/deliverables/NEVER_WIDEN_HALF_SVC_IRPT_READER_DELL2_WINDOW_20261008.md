# COO never-widen half -- dell2 reads `irpt/svc-irpt-analysis/password` for one ledger window (ADD at V1, REMOVE at X1)

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~18:4xZ. **Counterpart owed:** a CTO half (its consent is msg 107091).
**Authority:** `1.0.0_SA_CTO` msg 107091 (consent to dell2's ledger `irpt-ycdgen-f1-svc-20261008`, verbatim in
`org/mcp/inbox/0.0.0_AB_MSTR/read/20261008T182218Z_1.0.0_SA_CTO_re_107088__carry_to_1.0.0_SA_CTO_DELL2__.md`) and msg
107099 to this seat; dell2 `2.0.0_SA_COO~G2` msgs 1397/1399 (relay
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_DELL2_SVC_IRPT_READER_CORRECTION_20261008_1824Z.md`): a Dell cannot write the
policy (`secretsmanager:PutResourcePolicy` implicitDeny, measured on dell2 18:2xZ).

## The act, two legs, one property

The property is ONE secret's resource policy (`arn:aws:secretsmanager:us-east-1:313476888478:secret:irpt/svc-irpt-analysis/password-rfHf9l`).
**Writers: N = 1, by hand** -- no Terraform declares it (comp-find over `infra/`: zero declaring hits, 4 test-file mentions);
read live by this seat ~18:4xZ. Default key (`KmsKeyId` null). Census class PLATFORM-KEY, GRANTED in step E.

| leg | when | document (exact bytes, in this folder) |
|---|---|---|
| ADD | dell2 `2.0.0_SA_COO~G2` says leg V1 closed | `SVC_IRPT_READER_POLICY_ADD_dell2_window_20261008.json` -- the walker's principal AND `cloudops-dell2-agent-user` in the Allow's Principal and in the Deny's `ArnNotEquals` list |
| REMOVE | dell2 says leg X1 reached | `SVC_IRPT_READER_POLICY_BEFORE_restore_20261008.json` -- the policy as it is now (semantically equal to the live read, measured) |

## Blast radius

One principal, `cloudops-dell2-agent-user` (every agent seat on dell2), gains `GetSecretValue` on one secret for one
window. Since step E (18:00:17Z) its own IAM policy already allows the read; today only the secret's explicit Deny
(`NobodyElseReadsTheValue`) refuses it, so the ADD's effect is exactly that Deny's exception. In plain words: dell2 can read
the password of the firm's own IRPT Analysis service principal while the window is open, and so act as that service.
`DescribeSecret` is added beside it in the Allow (as the walker's statement reads). Nothing else: no other principal, no other
action, no key policy, no other secret. dell1 is not in either document.

## Expected outcome, BOTH branches, per leg

- **ADD, A:** `put-resource-policy` returns the ARN; `get-resource-policy` reads back equal to the ADD file; simulation
  (`simulate-principal-policy` with the resource policy passed as `--resource-policy`, caller dell2) reads `allowed`; the same
  for `cloudops-dell1-agent-user` reads `explicitDeny`. **ADD, B:** any other read-back -> put the BEFORE file back at once,
  read it back, report.
- **REMOVE, A:** read-back equal to the BEFORE file; dell2 simulated `explicitDeny`; the walker (`Andrew_Berman`) `allowed`.
  **REMOVE, B:** any other read-back -> retry the put once, then report to the CTO and dell2 at once; the window stays open
  only as long as that report takes.

## Rollback per key

The single key is the policy document: put the BEFORE file. That IS the REMOVE leg; it is also each leg's rollback. A value dell2
read during the window cannot be un-read: if the window ever needs undoing for exposure, the service principal's password is
rotated (dell2's ledger names the owner).

## Conditions

1. The applier reads NO secret value (no `GetSecretValue`), only the policy and simulations.
2. Before the ADD, the live policy reads equal to the BEFORE file; if not, STOP (someone else wrote it).
3. Each leg is logged in dell2's ledger by dell2 from the applier's report (the CTO's condition 1), and the laptop applier
   opens and closes its own NEVER-2 entry per leg.
4. The REMOVE is not optional: if dell2 has not called X1 by 2026-10-09T06:00Z, the applier asks this seat, which asks dell2
   and the CTO; the window does not stay open by silence.

**SIGNED** -- `2.0.0_SA_COO~C`
