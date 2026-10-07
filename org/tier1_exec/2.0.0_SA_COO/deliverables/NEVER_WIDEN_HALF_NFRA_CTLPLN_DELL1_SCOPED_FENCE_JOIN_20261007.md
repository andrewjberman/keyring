# COO never-widen half -- NFRA_CTLPLN: dell1's READ-ONLY, PREFIX-SCOPED join to the three firm fences (one apply, three bucket policies)

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~18:1xZ. **Read at:** trunk `17b61b4124`. Root `infra/aws/terraform/shared-infra/`.
**Counterpart owed:** a CTO half for this same act. **Authority:** `1.0.0_SA_CTO` msgs 106185 (the need: dell1 reads
`irpt/<firm>/platinum/holdings/` in the three firm buckets, get and list only) and 106230 (the row shape, the order of landing,
`GetBucketLocation` admitted, `GetObjectVersion` refused; "Then send the plan for my half").

## What has landed, in the ruled order

1. The renderer and the fail-closed readers: merged @3b6c321227 (cell CT-d-2 AMENDMENT 4). An unknown key on a registry row is
   refused by the validator and by the naming module at plan time.
2. The three scoped rows: `infra/logic/registry/exemptions.json` @d5516cb074, by `4.0.0_SA_CRO`.
3. The two checks made to hold on the registry as it now is: merged @17b61b4124 (AMENDMENT 6).

## The act

One `safe-apply` of the root TARGETED at exactly three resources: `aws_s3_bucket_policy.opal_data_49financial`,
`aws_s3_bucket_policy.lgic_firm["cottonwood"]`, `aws_s3_bucket_policy.lgic_firm["inflection"]`, at the laptop.

## The plan, MEASURED

`terraform plan -lock=false -detailed-exitcode` with those three targets, on the laptop, 2026-10-07 ~18:1xZ, read-only, exit 2:

```
  # aws_s3_bucket_policy.lgic_firm["cottonwood"] will be updated in-place
  # aws_s3_bucket_policy.lgic_firm["inflection"] will be updated in-place
  # aws_s3_bucket_policy.opal_data_49financial will be updated in-place
Plan: 0 to add, 3 to change, 0 to destroy.
```

129 added lines, 0 removed lines. In each policy: the dell1 user's ARN added to `DenyForeignFirmPrincipals`' admitted list, and
three statements added: `DenyScopedExemption1AnyOtherAction`, `DenyScopedExemption1ObjectsOutsidePrefix`,
`DenyScopedExemption1ListingOutsidePrefix`. No existing statement is changed or removed (the cottonwood policy's three
restricted-prefix statements and the dell2 line, applied today, are untouched).

**Writers of the property (each bucket's policy): N = 1 each**, the one resource per bucket in this root; all three read.

## Blast radius

Three S3 bucket policies. The act changes what ONE principal, `cloudops-dell1-agent-user`, may do in three buckets, and changes
nothing for any other principal.

**What dell1 gains (the widening):** `s3:GetObject` under `irpt/<that bucket's firm>/platinum/holdings/`, `s3:ListBucket` when
the request's prefix is under that path, and `s3:GetBucketLocation`, in each of the three buckets. Today dell1 is refused
everything in all three by the fence (live census before this act: `dell1_admitted=21/24 gap_dell1=1`).

**What keeps it that narrow, and why this is not plain admission:** dell1's own identity policy allows get, put and list on the
estate's bucket pattern. A principal admitted through a fence is outside its Deny. So the same apply adds, for that principal
only, an explicit Deny of every action except the three named, of any object read outside the prefix, and of any listing whose
prefix is not under the path (an absent or empty prefix included). Without those three statements this act would give dell1
whole-bucket read AND write on three firms' data; the renderer and the rows were landed in an order that never allowed that
state to be planned.

**Named so it is not read as covered:** `s3:GetObjectVersion` is refused (ruled). The holdings prefix in each bucket is that
firm's holdings data: dell1's placed projects read all three firms' holdings after this act. The census's `dell1_admitted` count
will read 24/24 after the apply although the admission is scoped: the census counts admission, not scope (see condition 5).

**Evidence, issuer's own runs on the trunk-bound files (in the worker's tree before the merge):**
`FENCE-SCOPED rows_today=32 unchanged_today=True scoped_rendered=9/9 sim_ok=30/30 refusals_ok=7/7 unknown_key_refused_by=validator+module ok=True`;
`FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=0 validator=ok scoped_rows=3 scoped_confined=3/3 ok=True`;
proof VALID. The simulator arms ran on each bucket's SAVED policy plus the rendered statements with dell1's live attached
policies as the identity side: get under the prefix allowed; get outside, put under the prefix, list with no prefix, list with an
empty prefix, and `GetObjectVersion` each explicitDeny; `GetBucketLocation` allowed; dell2 unchanged.
**What that evidence is not:** a read of a real object; the `s3:prefix` value in the simulator is supplied, not taken from a real
list request; organization policies were not evaluated.

## Expected outcome, BOTH branches

- **A:** the applier's targeted plan reads exactly the three in-place updates, 0 to add, 0 to destroy; in each, the added lines
  are the one dell1 ARN in the admitted list and the three named statements, and NO line is removed or changed in any other
  statement -> apply.
- **B:** any removed line, any change to another statement, a fourth resource, a role, or a different count -> apply NOTHING and
  report the plan as read.

## Rollback per key

Per bucket, independent: `4.0.0_SA_CRO` removes that bucket's scoped row and the same targeted apply runs for that bucket; or, in
the same window, the saved prior policy document is put back. S3 keeps no prior version, so the three LIVE documents are saved
with their hashes before the apply.

## Conditions

1. The plan shape of branch A, read immediately before the apply, with the added lines classified (not skimmed) per bucket.
2. Both checks run and read `ok=True` immediately before the plan: `tests/check_dell_fence_join.py`,
   `tests/check_fence_scoped_rows.py`.
3. The three live policy documents saved with SHA-256 before the apply; a NEVER-2 ledger entry opened and closed.
4. Read-back LIVE, each arm with its matched statement, by the simulator against the LIVE policy, per bucket: dell1 get under
   the prefix allowed; get outside the prefix, put under the prefix, list with no prefix and `GetObjectVersion` each explicitDeny
   BY A `DenyScopedExemption1...` STATEMENT (named); `GetBucketLocation` allowed; dell2 get outside the prefix still allowed; one
   unlisted, previously refused principal still refused; on cottonwood, dell1 refused on the restricted prefix. The live document
   equals the saved one plus the planned additions (parsed, with a planted-mutant control). A re-plan of the three targets reads
   no changes.
5. The live fence census after the apply; its `dell1_admitted` moving to 24/24 is reported with the words "scoped, 3 of 24".
6. The exercised read is dell1's own, from dell1, by another route, and is owed after the apply: one object got under the
   prefix in one bucket; one get outside it refused; one put refused. Until it runs the join is APPLIED, not EXERCISED.

**SIGNED** -- `2.0.0_SA_COO~C`
