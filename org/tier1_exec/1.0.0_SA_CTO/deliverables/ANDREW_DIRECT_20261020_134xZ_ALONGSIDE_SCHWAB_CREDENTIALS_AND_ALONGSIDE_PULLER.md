# ANDREW-DIRECT 2026-10-20 ~13:4xZ -- Alongside Schwab credentials stored; an Alongside-specific Schwab EC2 daily puller for Cottonwood

Given at the laptop 1.0.0_SA_CTO terminal, with a screenshot of a Teams message from Mike Little (9:43 AM) carrying a Schwab username and
password. VERBATIM (the credential itself is NOT reproduced anywhere in the repo):

> "please note the following and add to secrets manager under Alongside Schwab Credentials. This is the login information we need to use
> for an alongside-specific schwab ec2 daily puller. this is how we can backfill the schwab accounts for Cottonwood."

## Done by this seat, same turn

- **Secret created:** `schwab/alongside/sdd-credentials`
  (`arn:aws:secretsmanager:us-east-1:313476888478:secret:schwab/alongside/sdd-credentials-9IP0UA`). The description reads "Alongside Schwab
  Credentials", the value is JSON with keys `username` and `password`, and it carries tags `project=NFRA_SCHWABBF` and `owner=1.0.0_SA_CTO`.
  - The value went from a scratchpad file, deleted the same command, and was read back by keys and lengths only (username matched,
    password 8 characters). It was never printed, committed or sent.
  - **The name:** the builder has no SECRET kind (`name()` refuses it). The name is graded `opal_naming.grade(..., 'SECRET')` ->
    `('CONFORMANT', 'schwab/alongside/sdd-credentials')`, the same route dell1 took for `fidelity/alongside/wealthscape-credentials`
    (`canonical-fidelity-ec2/secret.tf`). The missing SECRET builder kind is a row for `4.0.0_SA_CRO`.
  - The secret was created by CLI. The puller's Terraform root adopts it by `import` (metadata only, prevent_destroy), never by recreating it.

## What it changes

**NFRA_SCHWABBF's FWD-7 premise is superseded for Cottonwood.** Cottonwood's four masters (08719286, 08134043, 08165601, 08480305) no longer wait
on Schwab entitling Opal's existing SDD login. They come through an Alongside-specific Schwab login on its own EC2 daily puller. That is a
scope addition, carried into the PRD as an addendum. Whether that login actually sees the four masters is unmeasured until its session
exists.

## Security note (for Andrew)

The password travelled in a Teams chat. Now that it is stored, consider asking Mike Little to delete or expire the chat message, or rotating the
password at Schwab and updating the secret.

## Same sitting, ~13:5xZ, VERBATIM

> "Yes I will need to RDP into the EC2 box most likely to get that done."
> "But. it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box"

- **Andrew does the first sign-in himself, by RDP**, once the box exists.
- **The Alongside box is an exact copy of the 49F Schwab Box's setup and logic,** labeled explicitly as the Alongside Schwab Box.

-- 1.0.0_SA_CTO (laptop)
