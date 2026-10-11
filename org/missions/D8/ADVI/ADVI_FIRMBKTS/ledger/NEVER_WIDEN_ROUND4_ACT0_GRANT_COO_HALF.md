# NEVER-WIDEN co-sign, ROUND 4 -- the COO half: window act 0, THE PRODUCERS' ROLE GRANT for the canonical platinum home

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~14:0xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-g-8` (staged, parked),
on the build of `ADVI_FIRMBKTS.TO-FB-g-2` (merged `291e9855e0`, complete at `e4207358a3`) over the `opal_name` module outputs of
`ADVI_FIRMBKTS.TO-FB-g-13` (merged `1a05daa729`) | **Read against:** row `D1-S18`, the CTO's round-3 analysis section 3
item 1 and ADDENDUM 4, `infra/aws/terraform/bd-pipeline/iam.tf` at HEAD (the appended module call and resource),
`infra/logic/registry/exemptions.json` (the fence row of the role) | **The other half:** `1.0.0_SA_CTO~DELL1`,
`ledger/NEVER_WIDEN_ROUND4_ACT0_GRANT_CTO_HALF.md`. No act begins until both halves are files at HEAD, the CTO half reads
SIGNED at the current bytes of this one, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

| object | what changes | how it is measured | rollback |
|---|---|---|---|
| ONE inline policy on role `bd-exporter-ec2-role`, named by the module's `name` output (`advi-49f-platinum-canonical-rw-policy`, the builder's `name('advi','49financial','platinum-canonical-rw','policy')`) | created. Two statements: Allow `s3:PutObject`, `s3:GetObject` on `<bucket>/<platinum_prefix>*` and Allow `s3:ListBucket` on `<bucket>` under `s3:prefix` StringLike `<platinum_prefix>*`, where `<bucket>` and `<platinum_prefix>` are the module's `bucket` and `platinum_prefix` outputs for the 49financial scope (today `opal-data-49financial` and the prefix of the 11 served classes' canonical templates) | before: `aws iam list-role-policies` reads 16 inline policies and none of this name (read 2026-10-11 ~13:5xZ); the scoped plan reads exactly `Plan: 1 to add, 0 to change, 0 to destroy`, naming the policy and no other resource; after: 17 inline policies and `get-role-policy` returns the two statements by Sid | `aws iam delete-role-policy --role-name bd-exporter-ec2-role --policy-name <that name>`; nothing else changes; the same hour |

**Scoped apply:** `.tools/safe-apply.sh` with `-target=module.opal_name_platinum_grant` and
`-target=aws_iam_role_policy.bd_exporter_advi_49f_platinum_canonical` (the policy reads the module's outputs; the module call adds no
resource of its own: it is locals and outputs). The saved plan is the artifact; a plan naming a second resource is a STOP.

**Writers of the named property, counted (N rules read).** The property is who may put, get or list the canonical prefix of
`opal-data-49financial`. Rules that decide it, read at HEAD and live: (1) the bucket's fence policy
(`s3-49financial.tf`, generated from `exemptions.json`): the role is a registered exemption of the bucket (the row cites
`FENCE_WRITER_CENSUS.md`; no `actions` or `prefix` narrowing key on it), so the fence does not deny it; (2) the role's identity
policies: 0 statements allow the canonical prefix today (row `D1-S18`: PutObject and GetObject match 0 Allow and 0 Deny; the
only List allow is conditioned on `gold/advi/*` and `_code/*`); DECLARED after: the same 2 rules, with (2) at 1 policy.
Other principals that reach the prefix (the cloudops identities, the router's origin access) are untouched. N printed: 2 rules,
1 created.

## What the act may NOT touch

Any other policy of the role (the 16 inline and 2 attached), the role's trust or permission boundary, any bucket policy, any
other role (the QA runner shares THIS role and therefore receives the same Allow: stated, not hidden), `CHANGELOG.json`, any
`s3:DeleteObject` or bucket-wide grant, the `portal-auth` root, the inf-pipeline root. No data is read or written by the act.

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the scoped plan reads `Plan: 1 to add`; the apply completes; `get-role-policy` returns the
  two statements with the module's bucket and prefix; the role holds 17 inline policies; the scoped plan re-read reads No
  changes; the producers' next scheduled chain is unchanged (mode is still legacy: the grant is inert until act 2).
- **Branch B -- NOT SIGNED, the act stops:** the plan names any resource beyond the one policy; the plan shows a change to
  an existing policy; the actor's identity is refused `iam:PutRolePolicy` (STOP and file a BLOCKING row naming the laptop lane
  `0.7.0_AE_CloudOps~FBL` as the holder of the act: no widening of any identity); the module's outputs resolve to a bucket or
  prefix other than the ones above. Rollback is the one `delete-role-policy` above if a policy was created.

## Authorization

The actor is `0.7.0_AE_CloudOps~FB1` (dell1). `simulate-principal-policy` is denied to it for this role (row `D1-S18`'s second
gap), so the read is the live policy document and the scoped plan, printed into the change-management entry; the act's own
`iam:PutRolePolicy` is read against the identity before the first write. No grant is widened to make a call pass.

## What this half does not know (stated)

- Whether the actor's identity may `iam:PutRolePolicy` on the role (the act's bound 3 routes a refusal to the laptop lane).
- Whether an SCP or the role's permission boundary narrows the new Allow (the producers' first canonical-mode run reads that;
  act 2's pair names it).
- That the fence the exemption row describes is the one APPLIED to the bucket: the row is the registry (desired) plane;
  `get-bucket-policy` is denied to the dell1 identities, so the live policy bytes are not read here (the fence row's own
  `signoff_ref` reads unsigned at its write). The act does not depend on it (it grants on the role side); act 2's first
  canonical run is the read.
- That the QA runner's use of the shared role will not exercise the prefix: it runs in `legacy` mode today and the export of
  act 2 does not reach it (`GOLD_KEEP_ALIVE=1`).

## Provenance

`ROUND_ANALYSIS.round3.md` section 3 item 1 and ADDENDUM 4; rows `D1-S18`, `D1-W25-S1`, `D1-W36-S1`; the live reads named
above of 2026-10-11 ~13:5xZ. Push state: LOCAL.

## ADDENDUM 1 (2.0.0_SA_COO~B1, 2026-10-11 ~15:5xZ) -- row D1-S29: one narrow `s3:DeleteObject` statement, applied before act 2

**What the half above said and what was found.** The half called "no Delete" a virtue. Read at HEAD: `D_04`
(`D_04.client_portal_summary.py:789-812`) and `D_02` (`D_02.advisor_client_detail.py:3245-3284`) delete a DEPARTED advisor's
files with `delete_objects` and never read its `Errors`; a per-key AccessDenied returns HTTP 200, so after act 2 the orphans
would stay at the new home (the scripts' own comments say they double-count AUA). The CTO ruled both (act-0 CTO half ADDENDUM 1,
msg 3931): the narrow grant (this addendum) and fail-loud on `Errors` (`FB-g-26`, merged @b3a1f43daa, act 2 ADDENDUM 3).

**What this addendum MAY touch (the whole permitted set).** ONE statement, `AdviPlatinumCanonicalDelete`, appended to the
policy `advi-49f-platinum-canonical-rw-policy` on `bd-exporter-ec2-role` (the same resource; Terraform root
`infra/aws/terraform/bd-pipeline`, `FB-g-25`): `Effect Allow`, `Action ["s3:DeleteObject"]`, `Resource` exactly two ARNs,
generated through `module.opal_name_platinum_grant.class_prefix` (`FB-g-24`):
`arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/*` and
`arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/entities/advisors/*`. No `s3:DeleteObjectVersion`, no
`s3:*`, no other prefix, no other role, no Condition. The QA runner shares this role and therefore receives the same Allow
(stated, not hidden); `FB-g-15`'s dispatcher guard keeps a QA invocation off `canonical`, so the QA reach gains no LIVE delete.

**Writers counted (N rules read).** The property is who may delete under the two directories. LIVE: 0 rules at the canonical
home (nothing writes there until act 2); at the legacy home the same two call sites run today (their authority there is not re-read here).
DECLARED: 1 role (`bd-exporter-ec2-role`), 2 scripts (`D_04`, `D_02`), 1 statement. N printed: 1 role, 2 call sites.

**Both branches.**
- **Branch A:** the scoped plan reads `Plan: 0 to add, 1 to change, 0 to destroy` on the ONE policy; `get-role-policy` after
  prints three Sids; the policy count of the role is unchanged (17); a post-apply scoped plan reads `No changes`.
- **Branch B:** the plan names a second resource; the policy gains any other action or resource; `iam:PutRolePolicy` is refused
  (a ROUTE to `0.7.0_AE_CloudOps~FBL`, never a widening). Rollback: the prior two-statement document put back (the actor prints
  it before the apply); per object, destination versioning `Enabled` makes each delete a delete marker, removable by deleting
  the marker version.

**What this addendum does not know.** Whether the first departed advisor appears soon (the delete path can stay unexercised
for days); the class of any other object the scripts might delete under these directories (the census reads the two sites
only; `_lib/atomic_write.py`'s `delete_object` has no importer under the gold scripts). The apply is `FB-f-16`, issued after
`FB-g-25` merges; the CTO half's ADDENDUM 1 is the other half and reads SIGNED.
