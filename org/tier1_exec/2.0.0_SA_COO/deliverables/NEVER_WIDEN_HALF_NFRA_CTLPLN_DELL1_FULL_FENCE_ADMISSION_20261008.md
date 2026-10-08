# COO never-widen half -- NFRA_CTLPLN: dell1 is admitted to the three firm fences IN FULL, as dell2 is (one targeted apply, three bucket policies)

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~01:1xZ. **Read at:** trunk with `infra/logic/registry/exemptions.json` @173f98f24b
(`4.0.0_SA_CRO`: the three dell1 rows are full rows). Root `infra/aws/terraform/shared-infra/`. **Counterpart owed:** a CTO half.
**Authority:** Andrew-direct ~00:4xZ, "lets start with lifting 1 2 3 6", item 2 of the list he answered being "Read parts of
client firm data on dell1 ... dell2 is fully admitted" (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`;
this seat read the record and did not hear the word); `1.0.0_SA_CTO` msg 106669 ruling 2: "dell1 is admitted to the firm-data
fences in full, like dell2."

**This supersedes** this seat's half of 2026-10-07 for the scoped join
(`NEVER_WIDEN_HALF_NFRA_CTLPLN_DELL1_SCOPED_FENCE_JOIN_20261007.md`, applied under order NFRA_CTLPLN.TO-APPLY-8 about six hours
ago). That act admitted dell1 and confined it to one prefix per bucket by three Deny statements. This act removes the
confinement.

## The act

One `safe-apply` of the root TARGETED at exactly `aws_s3_bucket_policy.opal_data_49financial`,
`aws_s3_bucket_policy.lgic_firm["cottonwood"]` and `aws_s3_bucket_policy.lgic_firm["inflection"]`, at the laptop.

## The plan, MEASURED

Targeted plan, laptop, 2026-10-08 ~01:0xZ, read-only, exit 2: `Plan: 0 to add, 3 to change, 0 to destroy.` 126 removed lines,
0 added. In each of the three policies the three statements `DenyScopedExemption1AnyOtherAction`,
`DenyScopedExemption1ObjectsOutsidePrefix` and `DenyScopedExemption1ListingOutsidePrefix` are removed whole. The dell1 user stays
in `DenyForeignFirmPrincipals`' admitted list (it was added there by the earlier act). No other statement changes: the
cottonwood policy's three restricted-prefix statements and the dell2 line are untouched.

**Writers of the property: N = 1 per bucket**, the one resource in this root; all three read.

## Blast radius

Three S3 bucket policies. One principal's reach changes: `cloudops-dell1-agent-user`.

**What dell1 gains (the widening), stated at its full width:** everything the fence had denied it, on the whole of each of
the three firm buckets. Its own identity policy allows `s3:GetObject`, `s3:PutObject`, `s3:ListBucket` and the bucket reads on
the estate's bucket pattern and denies deletes. So after this act dell1 can READ AND WRITE any object in the 49 Financial,
Cottonwood and Inflection data buckets, not only the holdings prefix it reads today. That is what "in full, like dell2" is;
dell2 has held exactly this since yesterday's applies. A firm's data bucket is then writable by both Dell box users.
**What still binds dell1 on cottonwood:** the restricted CRM prefix's three statements deny every principal but the console user
and the break-glass role; they are another project's and are not touched. The last act's read-back showed they bind a principal
admitted afterwards.

**Two checks read `ok=False` at this writing, for a stated reason, and the apply does not run until they pass:**
`check_dell_fence_join.py` reads `cross_firm_leaks=3 other_rows_changed=3` because its expected pairs list knows only dell2 as
unscoped, so it counts the three now-intended dell1 rows as leaks; `check_fence_scoped_rows.py` reads `refusals_ok=0/7` because
its fixture adds a scoped dell1 row beside the full one. Both are the checks' assumptions about the registry (the same class
diagnosed yesterday), and a worker repairs them with the expected pairs stated as data before the order is cut. If the repair
finds a real fault instead, this half is void.

## Expected outcome, BOTH branches

- **A:** the applier's targeted plan reads exactly three in-place updates; in each, exactly the three `DenyScopedExemption1...`
  statements removed, ZERO added lines, no other statement changed, the admitted list unchanged -> apply.
- **B:** any added line, any other statement touched, a change to an admitted list, a fourth resource, or another count ->
  apply NOTHING and report.

## Rollback per key

Per bucket, independent: the registry's lane restores that bucket's scoped row (@d5516cb074's form) and the same targeted
apply runs; or, same window, the saved policy document is put back. The three LIVE documents are saved with hashes before the
apply. An object dell1 wrote in the interval is not undone by the rollback; it is listed.

## Conditions

1. The plan shape of branch A, classified per bucket immediately before the apply.
2. Both checks read `ok=True` immediately before the plan, after their repair.
3. The three live documents saved with SHA-256; a NEVER-2 ledger entry opened and closed.
4. Read-back LIVE by the simulator against the LIVE policies, each arm with its matched statement: dell1 get and put outside
   the old prefix now allowed in each bucket; dell1 still refused on cottonwood's restricted prefix; dell2 unchanged; one
   unlisted, previously refused principal still refused. The live document equals the saved one minus the three statements
   (parsed, with a planted-mutant control). A re-plan reads no changes.
5. The live fence census after the apply reads `dell1_admitted=24/24 dell1_scoped=0 disagree=0 ok=True`.
6. `4.0.0_SA_CRO` asked for the pair's paths for the rows' `signoff_ref`: this file and the CTO half.
7. The exercised read is dell1's own, by another route: the reads it was refused (49 Financial's code prefix; a listing of the
   Cottonwood bucket) now succeed. Until then: APPLIED, not EXERCISED.

**SIGNED** -- `2.0.0_SA_COO~C`
