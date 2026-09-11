# ANDREW-DIRECT 2026-09-11 ~05:0xZ -- TWO CALLS RULED: USE THE EXISTING GITHUB TOKEN (SPRINT LAMBDA TOO); APPLY THE STATE-BUCKET LIFECYCLE RULE

**Terminal:** `1.0.0_SA_CTO`. **Recorded by:** `1.0.0_SA_CTO`, same turn. Answers the two cards of `/open-calls` at 05:0xZ.

## VERBATIM AND ENTIRE

> Call 1, just use the one that is already there, sprint lambda can use it too, we'll deal with that later. Call 2, sure

## CALL 1 -- the GitHub credential

The card: mint a read-only PAT and rotate it into `estate-report/github-token`. **Ruled: NO new PAT.** The token
already in `estate-report/github-token` (live since 2026-07-31; admin/maintain/push where the secret's own
Terraform description says read-only) stays as it is, and the daily-sprint Lambda READS THAT SAME SECRET. The
over-grant is DEFERRED by his word ("we'll deal with that later"); it stays on the record as `NFRA_CLDGRPH-S132`
and is not re-asked.

What this settles: the Lambda's Terraform points at `opal/daily-sprint-github-read`, a secret that does not exist;
that name changes to `estate-report/github-token` (a one-line change in the Lambda's own files, `0.7.0_AE_CloudOps`'s
lane, `infra/aws/**`), the IAM read grant names that secret's ARN, and the credential blocker on the Lambda is
CLOSED. The apply of the Lambda remains its steward's deploy act under a change-management entry.

## CALL 2 -- the Terraform state-bucket lifecycle rule

The card: apply `infra/aws/terraform/terraform-state-bucket-lifecycle/` (noncurrent-version expiration 90 days;
abort incomplete multipart uploads 7 days; plan `1 to add, 0 to change, 0 to destroy` at `ddb6073675`).
**Ruled: YES.** The apply is authorized. The gate (`1.0.0_SA_CTO`) reads it per `D0_INFRA_TIGHTENING_PRD` s.6
row 8's acceptance: the plan RE-READ at apply time shows exactly the one lifecycle configuration with the two named
rules; the change-management entry prints the blast radius as every `backend{}` block naming the bucket (the
286-hit census is the denominator); unscoped re-plan 0/0/0 after; the bucket's noncurrent versions expire per the
rule, measured on the bucket.

## WHAT LANDS ON THIS WORD

- This record. `D0_INFRA_TIGHTENING_PRD` s.6 row 8: status APPLY AUTHORIZED (Andrew-direct 05:0xZ), steward's act.
- `0.7.0_AE_CloudOps` told, as information carrying his word: both rulings, the secret name, the acceptance the gate
  reads. `0.0.0_AB_MSTR` told: the sprint Lambda's credential is settled (LD-0547's ask is answered).
- Both `/open-calls` cards CLOSED on his word.
