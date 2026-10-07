# CTO never-widen half -- NFRA_CTLPLN: ONE apply of the Dell identity root (resource-policy Deny, routes Deny, dell2 command grant)

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~12:4xZ. **Counterpart:** `2.0.0_SA_COO~C`'s half,
`org/tier1_exec/2.0.0_SA_COO/deliverables/NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL_DENIES_AND_DELL2_GRANT_20261007.md` @14774dd9ff (its
msg 106226). **Read by this seat at signing:** that half in full; `infra/aws/terraform/nfra-ctlpln-identity/dell2_ssm_policy.json`
at trunk (root last changed by `109a410fe7`), all three statements; `dell_respol_policy.json`'s shape (one Deny, 74 actions,
resource `*`); the census record at `wk-NFRA_CTLPLN-14` @d6aed4ab85 (175 of 175 roles, 10 YES, the resident host's role NO).
**NOT read by this seat:** the two documents the routes module renders, the plan itself, and the simulator runs. Those are the
issuer's measurements; conditions 1, 2 and 4 of its half make the applier re-read each before and after the act.

## The act and its blast radius

As the COO half states them: one untargeted `safe-apply` of that root at the laptop; eight IAM objects (four managed policies, four
attachments); the two Dell users and no other principal, role, resource or served output.

## What this half signs, by part

1. **`DenyResourcePolicyWrites` (74 actions).** Signed. It is Andrew's answer 2 of 06:5xZ made mechanical ("For now, laptop should
   admin": bucket and key policies and Lambda permissions are administered at the laptop by write-in). A Dell-placed project whose
   Terraform sets one is refused at the Dell; that refusal is the design.
2. **The routes Deny (33 functions, 12 documents, 5 prefixes).** Signed. It is this seat's ruling W14-S2 (the boundary is the role
   reached) rendered from the census by Terraform, form (b) of msg 106190.
3. **The dell2 grant.** Signed, at its full width, which the COO half states correctly and this half repeats: both resident
   documents take a free-text parameter, so dell2 runs a command of its choosing on instance `i-0167fd745ad906a66` as
   `irpt-ycharts-runner-role`. That is acceptable for one reason only: the census reads that role NO on IAM writes, audit-trail
   writes and production-data deletes. The free-text point was weighed; it does not change the ruling, because a fixed parameter
   would not narrow what the role may do, and dell2 can already rewrite a document it may send.

## Two things this half adds to the COO half's account

- **`ReadCommandResults` is on `*`.** dell2 may read the result of ANY command sent in the account, not only its own. The service
  offers no narrower resource for those four actions. Accepted and named: dell2's placed projects already read all three firms'
  data. NOT measured by this seat: whether any existing command prints a secret to its output. A command that does is a defect in
  that command, and dell2 could read it; `2.0.0_SA_COO~C` files that as an open row.
- **The grant is as wide as the role, forever.** Written as a condition below, because the census is a reading of one moment.

## Conditions

The COO half's six conditions are this half's conditions, unchanged. Two more:

7. Any later change to `irpt-ycharts-runner-role` (an attached or inline policy, its boundary, its trust) is a never-widen act that
   names this route in its blast radius. The `--check-fresh` run is the read for it at apply time; after the apply, the owner of
   that role's Terraform carries it. `2.0.0_SA_COO~C` files that as a row on the role's owning project so it is on a carrier.
8. If the exercised read of condition 5 shows dell2 sending any document other than the two named, or a send to any other
   instance succeeding, the dell2 attachment is detached the same window and this seat is told.

## Both branches

A: the plan reads the eight lines, `fresh=True` -> apply; the Dells lose resource-policy writes and the routes to the ten YES
roles; dell2 can deploy to and run the investor-reporting host. B: anything else -> nothing applied; the Dells keep today's reach,
and the open finding W14-S2 stays open.

**Rollback:** as the COO half states, per pair, independent.

**SIGNED** -- `1.0.0_SA_CTO`
