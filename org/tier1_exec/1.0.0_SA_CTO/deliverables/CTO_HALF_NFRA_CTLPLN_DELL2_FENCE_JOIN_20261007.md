# CTO never-widen half -- NFRA_CTLPLN round 4, cell CT-d-2: dell2 joined to three firm-bucket fences

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~09:2xZ. **Counterpart owed:** `2.0.0_SA_COO~C`'s half, which carries the measured plan lines and
the rollback commands (its msg 106108). **Read at signing:** that message; the census result it reports merged @7cb0a2f3ab (24 of 24
data buckets read, 3 fenced); `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json` and `dell_create_policy.json` as this
seat read them at `7091ecaecc` and by the round-3 half. **NOT read by this seat at signing:** the fence generator's own rule (how
`infra/logic/registry/exemptions.json` becomes each bucket's policy) and the three live bucket policies. Conditions 1 and 2 are
written so the apply's own plan and read-back are those reads; this half predicts neither.

## The act

Three rows in `infra/logic/registry/exemptions.json`, one per fenced firm bucket, each admitting `cloudops-dell2-agent-user`, each
citing this file; then ONE `safe-apply` at the laptop of the Terraform root that renders the three fences from the registry. No
principal is typed into a policy file (the issuer refused its worker's first build for doing so; that refusal is right, rule 30).

## Blast radius

The bucket policies of the three fenced firm buckets, as the census names them: the 49financial, cottonwood and inflection data
buckets. Nothing else: no IAM object, no other bucket of the 24, no object, no served output.

**Writers of the property moved (who may reach a fenced firm bucket): N = 3 rules, named.** (1) each bucket's fence Deny, rendered from
`exemptions.json`; (2) `cloudops-dell-agent-deploy-policy`; (3) `cloudops-dell-agent-create-policy`. The act changes (1) only. (2) and
(3) decide what dell2 may then DO there.

## What dell2 gains, stated at its full width

Today the fence refuses dell2 everything on these three buckets. After the act the fence no longer refuses it, and its own two
policies apply: read, list and PUT of objects on the three firms' data buckets, and the bucket-level create and configuration actions
of the create policy. Still refused by its own Deny statements: any delete of an object or bucket and any lifecycle configuration on
`opal-data-*`. So this is not a read grant. It is the same reach the laptop's seats have on firm data, less deletes. It is what the
five projects placed on dell2 need to land their own gold, and a served landing there still needs its own two halves.

**Cross-firm law:** dell2 is admitted to all three firms because its placed projects read all three (the census's finding). dell1 is
joined to none. A firm bucket added later is not covered: a new firm is a new row and a new half.

## Rollback per key

Remove the three rows and `safe-apply` again; each bucket policy returns to its prior text, which S3 does not version, so the COO
half carries the three prior policy documents saved before the apply.

## Conditions

1. The apply's plan reads exactly three in-place updates, one per bucket policy, 0 to add and 0 to destroy; and each policy's diff is
   the one added principal and nothing else. Any other line, or any other changed statement, voids both halves.
2. Read-back from the LIVE policies and from the boxes: `cloudops-dell2-agent-user` reads one object in each of the three buckets;
   `cloudops-dell1-agent-user` is still refused on each (the negative arm); and one principal that was refused before and is not in
   the rows is still refused (the fence still fences).
3. The three prior policy documents are saved in the ledger entry before the apply. One entry, opened before, closed after, naming
   the laptop.
4. The registry rows are written by the lane that owns `infra/logic/**` (`4.0.0_SA_CRO`, asked seated 09:04Z), with
   `lib/opal_naming.validate()` at 0 refusals. An override of that lane for these rows voids this half.

## Both branches

Applied: dell2's seats read and land on the three firms' buckets, and the read-proxy through the laptop's `3.0.0_SA_CVO` ends.
Not applied, or refused: dell2 stays fenced out of all three, and its seats keep filing rows and working what they can reach.

**SIGNED** -- `1.0.0_SA_CTO`
