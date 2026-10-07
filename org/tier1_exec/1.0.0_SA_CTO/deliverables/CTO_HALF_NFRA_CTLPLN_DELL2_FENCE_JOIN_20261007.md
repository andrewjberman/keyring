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

## AMENDMENT 1, 2026-10-07 ~10:1xZ -- a TWO-bucket apply now; cottonwood waits for its rider's own pair

**What happened (`2.0.0_SA_COO~C` msg 106148, from `0.7.0_AE_CloudOps~E`'s stop):** the plan read 0 to add, 3 to change, 0 to destroy,
and all three fences gain the dell2 principal, but the cottonwood policy's diff ALSO adds three unapplied ADVI_COTBKF statements (the
restricted CRM prefix Deny set, commit 8e58736597). Condition 1 above ("each policy's diff is the one added principal and nothing
else") voided both halves on that. The executor stopped at the plan gate; nothing was applied and no ledger entry was opened. That
stop is the half working.

**RULING: (a).** Apply two now, by resource address: `aws_s3_bucket_policy.opal_data_49financial` and
`aws_s3_bucket_policy.lgic_firm["inflection"]`. The cottonwood fence is NOT in this apply. It is applied when ADVI_COTBKF's three
restricted-prefix statements have their own pair, which is dell2's (`1.0.0_SA_CTO~DELL2` and `2.0.0_SA_COO~C2`), in one laptop apply
that then carries both the rider and the dell2 principal.

**This half, as amended, covers:** the targeted apply of those two resources only. Every section above stands with "three" read as
"two" and the cottonwood bucket removed from the blast radius and from what dell2 gains.

**Conditions, replacing 1 and 2 above; 3 and 4 stand (two prior policy documents saved, not three):**
1. The targeted plan reads exactly two in-place updates on the two addresses named, 0 to add, 0 to destroy, and each diff is the one
   added principal. Any other line or statement voids both halves again.
2. Read-back: `cloudops-dell2-agent-user` reads one object in each of the two buckets; it is STILL refused on the cottonwood bucket
   (the third arm, now a negative one); `cloudops-dell1-agent-user` is still refused on both; one previously refused unlisted
   principal is still refused.

**Both branches, as amended:** applied, dell2 reads and lands on the 49financial and inflection buckets and stays fenced out of
cottonwood; not applied, dell2 stays fenced out of all three.

**What dell2 still cannot do after this apply:** anything on the cottonwood firm bucket. IRPT work that reads Cottonwood's firm data
keeps using the laptop read proxy until the second apply.

**SIGNED as amended** -- `1.0.0_SA_CTO`

## AMENDMENT 2, 2026-10-07 ~11:1xZ -- the cottonwood fence: the dell2 principal rides ONE apply with ADVI_COTBKF's three statements

**Who cuts it (`2.0.0_SA_COO~C` msg 106171, question 1): `2.0.0_SA_COO~C`, as NFRA_CTLPLN's third fence apply.** Andrew-direct ~06:1xZ
keeps that seat "only ... focused on this work, not cottonwood backfill project". THIS SEAT'S READING, stated as a reading: joining
the dell2 user to the cottonwood fence IS this work (cell CT-d-2), and the resource it changes can only be applied whole. The seat
writes no ADVI_COTBKF artifact, rules nothing of that project and cuts no ADVI_COTBKF order; the three statements arrive with dell2's
own two halves (`2.0.0_SA_COO~C2` @c65cf8604d, `1.0.0_SA_CTO~DELL2` @87d7642a72) and ride NFRA_CTLPLN's apply. If Andrew reads his
word more narrowly, the alternative is a dell2-issued order to a laptop cloud-operations lane, and nothing here prevents it.

**Read by this seat at signing** (`origin/CLOUD`, `infra/aws/terraform/shared-infra/s3-lgic-firm-buckets.tf:196-280`): the three
statements are Deny statements on the restricted prefix alone -- `DenyRestrictedReadExceptReaders`, `DenyRestrictedListExceptReaders`,
`DenyRestrictedWriteExceptBreakglass` -- whose only admitted principals are the console-only user and the break-glass role; the
role's trust admits the console-only user alone ("one principal, no wildcard, no service"). They narrow access; they admit no one new.

**This amendment covers:** the dell2 principal added to the cottonwood fence, in the same in-place update that adds those three
statements. Blast radius: the cottonwood bucket's policy, once.

**Conditions for this apply:**
1. The plan reads exactly ONE in-place update, of the cottonwood bucket policy, 0 to add, 0 to destroy; its diff is the dell2
   principal in the fence and the three statements named above, by Sid, and nothing else. A role or role-policy line in the plan
   voids this amendment: the break-glass role is a separate act under the role request's four conditions (msg 106095).
2. Before: the restricted prefix holds 0 objects (dell2's own condition; a listing by the applier).
3. After: `cloudops-dell2-agent-user` reads one object in the bucket OUTSIDE the restricted prefix; it is refused read, list and put
   ON the prefix; `user/Andrew_Berman` is refused the same three on the prefix and still reads outside it; `cloudops-dell1-agent-user`
   is still refused on the bucket.
4. The prior policy document saved in the ledger entry before the apply.
5. `1.0.0_SA_CTO~DELL2`'s half names the dell2 principal line. As written it is conditional on "plan changes no other row", which
   this plan does not meet; until it is amended, that half is void and this apply does not run.

**Both branches:** applied, dell2 reaches the cottonwood firm bucket except the restricted prefix, and the restricted prefix is
closed to every agent identity; not applied, dell2 stays fenced out of cottonwood and the restricted prefix stays open to agents.

**SIGNED, amendment 2** -- `1.0.0_SA_CTO`

## AMENDMENT 3, 2026-10-07 ~19:1xZ -- the restricted-prefix statements re-applied alone

Andrew at dell2, as `2.0.0_SA_COO~C2` records it (bus c7e5ac77; record
`org/tier1_exec/2.0.0_SA_COO~C2/deliverables/ANDREW_DIRECT_20261007_185xZ_COTBKF_THREE_CALLS_APPROVED.md` @1f47ffb77a, CALL 3):
"ANDREW YES on the C-RESTRICTED re-apply, statements only." This seat did not hear the word and has not read that record; it
relies on the relay and says so.

AMENDMENT 2's condition 1 named the dell2 principal AND the three statements in one update. Where the principal is already live,
condition 1 reads: the plan is exactly ONE in-place update of the cottonwood bucket policy whose diff is the three statements by
Sid (`DenyRestrictedReadExceptReaders`, `DenyRestrictedListExceptReaders`, `DenyRestrictedWriteExceptBreakglass`) and nothing
else; no role or role-policy line. Conditions 2 to 4 stand. Condition 5 is met by `1.0.0_SA_CTO~DELL2`'s amended half
@b4073b7bf2 and `2.0.0_SA_COO~C2`'s AMENDMENT 2 @e297665fdb. If the three statements are already live, the plan reads no
changes and nothing is applied.

**SIGNED, amendment 3** -- `1.0.0_SA_CTO`

