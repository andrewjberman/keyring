# Deploy Completion Record
**Date opened:** 2026-10-07T14:18:52.214442+00:00
**Status:** OPEN
**Deploy:** NFRA_CTLPLN CT-d-2 third fence -- BOX: THE LAPTOP. ONE targeted safe-apply of aws_s3_bucket_policy.lgic_firm[cottonwood], carrying TWO projects in one in-place update because the resource applies whole: (1) NFRA_CTLPLN's dell2 principal added to DenyForeignFirmPrincipals, and (2) ADVI_COTBKF's three restricted-CRM-prefix Deny statements. FOUR halves bear on it, all now agreeing: NFRA_CTLPLN COO AMENDMENT 2, NFRA_CTLPLN CTO AMENDMENT 2 @2714b7df72, ADVI_COTBKF COO AMENDMENT 2 @e297665fdb (STATEMENTS ONLY -- it superseded its own role row, which is what cleared the step-0 stop), ADVI_COTBKF CTO AMENDMENT 1 @b4073b7bf2. Plan measured 0 to add, 1 to change, 0 to destroy, NO role line. Prefix holds 0 objects.
**Authored by:** 0.7.0_AE_CloudOps~E
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | one targeted safe-apply of the cottonwood bucket policy at the laptop | plan reads EXACTLY 0 to add / 1 to change / 0 to destroy on aws_s3_bucket_policy.lgic_firm[cottonwood] alone; the diff is the one dell2 principal plus the three signed Sids as an EXACT SET MATCH and nothing else (47 added lines classified, 0 removed, no fourth Sid); NO aws_iam_role or aws_iam_role_policy line anywhere in the plan; check_restricted_prefix.py POLICY limb passes as a separately printed result IMMEDIATELY before the apply; safe-apply completes 0 added 1 changed 0 destroyed |  | OPEN |
| V1 | verify | the live policy equals prior plus the one principal plus the three statements | parsed comparison of the LIVE document against PRIOR5_bucket_policy_opal-data-cottonwood_20261007.json (501 B, sha256 49f1cf260f0f18d5f52244c2a48bb5159765dd293633b750a9f0fbad39dcc7ae) plus exactly the dell2 principal and the three Sids; planted-mutant control through the same comparator; statement count 1 -> 4 |  | OPEN |
| V2 | verify | the NFRA_CTLPLN halves' arms, attributed | dell2 allowed s3:GetObject on a key OUTSIDE the restricted prefix; dell1 NOT allowed on the bucket; one unlisted previously-refused principal (opal-gateway-role, existence proven) still refused; one previously-admitted principal (Opal_Terminal) still allowed outside the prefix. Every arm with its matched statement |  | OPEN |
| V3 | verify | the ADVI_COTBKF halves' arms and NFRA_CTLPLN CTO condition 3, attributed | dell2 REFUSED read, list and put ON commonwealth/cottonwood/bronze/crm/ (the amended ADVI_COTBKF COO half's own after-read); user/Andrew_Berman refused the same three ON the prefix and still reading OUTSIDE it (the laptop locking itself out of the prefix, which is ADVI_COTBKF's stated intent); the console user Andrew_Berman_Console admitted on the prefix; each arm naming the matched statement so the refusal is attributed to the new Deny |  | OPEN |
| V4 | verify | AC1 + AC2 + AC3 and the expected-state reads | check_dell_fence_join.py reads rows=3/3 typed_in_tf=0 cross_firm_leaks=0 ok=True (AC1); dell_fence_census.py --live reads dell2_admitted=24/24 with gap_dell2=0 (AC2); the re-plan of the same target reads exit=0 (AC3); and the cottonwood plan no longer shows a pending change, which is the state change this act was for |  | OPEN |

## Log

- 20261007T141852Z OPENED by 0.7.0_AE_CloudOps~E with 5 leg(s)

---

## BOX

**THE LAPTOP.** Executor `0.7.0_AE_CloudOps~E`, seated by `2.0.0_SA_COO~C` under task order
`NFRA_CTLPLN.TO-APPLY-5.cottonwood-fence-apply-laptop` @ce2f42661d with AMENDMENT 1 @cbe30ace42 (GO msgs 106195 and
106228, both acked). Applying identity: `arn:aws:iam::313476888478:user/Andrew_Berman`. Terraform v1.15.8 on PATH.

## STEP 0, REPEATED -- and this time the four halves AGREE

The first pass STOPPED at step 0 and applied nothing
(`deliverables/STEP0_CONFLICT_READ_TO-APPLY-5_20261007.md` @316e1e5f98, msg 106201). Three conflicts were reported
and **the half's own author resolved them**, not the issuer: `2.0.0_SA_COO~C2` amended the ADVI_COTBKF COO half to
**STATEMENTS ONLY** @e297665fdb, which *"supersedes section 1's role row and Branch A's role clause"*.

**PRECONDITION, re-measured by this seat and not assumed:** `git merge-base --is-ancestor e297665fdb HEAD` exits
**0** at HEAD `9887bfc595`, with both controls run (self-ancestor exits 0; a bogus hash exits 128). It exited 1
earlier; the integrator's trunk sync landed it.

**THE ROLE QUESTION, re-answered:** a plan with NO role line now satisfies **all four** halves.

| half | the role | verdict on a no-role plan |
|---|---|---|
| NFRA_CTLPLN CTO AMENDMENT 2 @2714b7df72 | "a role or role-policy line in the plan voids this amendment" | SATISFIED |
| NFRA_CTLPLN COO AMENDMENT 2 | "a role, role-policy or any other resource line: apply nothing" | SATISFIED |
| ADVI_COTBKF CTO AMENDMENT 1 @b4073b7bf2 | the role is "the laptop's IAM half ... not signed here"; read 2' stops on anything else in the plan | SATISFIED |
| ADVI_COTBKF COO AMENDMENT 2 @e297665fdb | **supersedes** its own role row; Branch A now requires "NO role resource" | SATISFIED |

All three conflicts are closed: **A** (role line voids vs role created) and **B** (the pair disagreeing with itself)
by the supersession above; **C** (a rollback presuming the role was created) because the superseded section-1 row
carried that rollback with it.

## AMENDMENT 1(b) -- THE NEW READ: how the three statements except a role that does not exist

The amendment makes this a STOP if any of the three excepts the role by a `Principal` or `NotPrincipal` element,
because S3 refuses a policy whose principal element names a non-existent identity and a `NotPrincipal` Deny is a
different statement from the one signed. **Read at `s3-lgic-firm-buckets.tf:196-233`, all three use a CONDITION:**

| Sid | principal element | how the role is excepted |
|---|---|---|
| `DenyRestrictedReadExceptReaders` | `Principal = "*"` | `Condition { ArnNotLike { aws:PrincipalArn = readers } }` |
| `DenyRestrictedListExceptReaders` | `Principal = "*"` | `Condition { StringLike s3:prefix + ArnNotLike { aws:PrincipalArn = readers } }` |
| `DenyRestrictedWriteExceptBreakglass` | `Principal = "*"` | `Condition { ArnNotLike { aws:PrincipalArn = writers } }` |

**None uses a principal element for the role. NOT a stop.** The role's ARN is a derived string
(`arn:aws:iam::<acct>:role/${module.opal_name_restricted_breakglass.name}`), and the file's own comment gives the
reason: a new role's ARN is unknown at plan time and would render the whole bucket policy unknown, which no plan
check could read.

**One check the amendment did NOT ask for, made because a silent failure here would be invisible:** the derived ARN
must match the role's real ARN once it is created, or the exception never applies and the break-glass role still
cannot read the prefix. The derived form is `role/<builder name>` with **no path segment**; the role resource sets
`name = module.opal_name_restricted_breakglass.name` -- the SAME module instance -- and does **not** set `path`, so
it defaults to `/`, whose ARN form is exactly `role/<name>`. **They will match.**

## BLAST RADIUS -- one bucket policy, carrying two projects

`aws_s3_bucket_policy.lgic_firm["cottonwood"]` on `opal-data-cottonwood`, once. No IAM object, no role, no other
bucket of the 24, no object, no served output. **No role is created by this act.**

| what | whose | effect |
|---|---|---|
| the dell2 principal added to `DenyForeignFirmPrincipals`' `ArnNotLike` | NFRA_CTLPLN CT-d-2 | dell2's placed projects can read Cottonwood firm data (24 files across ADVI_COTBKF, IRPT_BCKEND, IRPT_YCDGEN cite that bucket); the laptop read-proxy ends for it |
| `DenyRestrictedReadExceptReaders` | ADVI_COTBKF CB-d-4 | the CRM prefix is closed to every principal except the console user and the break-glass role |
| `DenyRestrictedListExceptReaders` | ADVI_COTBKF CB-d-4 | the same for prefix listing |
| `DenyRestrictedWriteExceptBreakglass` | ADVI_COTBKF CB-d-4 | writes under the prefix closed to all but the break-glass role |

**NAMED SO IT IS NOT A SURPRISE, and it is in the order's own bounds:** after this apply the laptop's own identity
(`user/Andrew_Berman`, the identity every laptop seat applies and reads with) is **refused read, list and put on the
restricted prefix**. That is ADVI_COTBKF's stated intent, not a defect. The prefix holds 0 objects, so no existing
reader loses anything today. Do not attempt to read that prefix afterwards except through the simulator.

## ROLLBACK PER HALF

S3 keeps **no prior version** of a bucket policy, so the saved document IS the rollback:
`deliverables/PRIOR5_bucket_policy_opal-data-cottonwood_20261007.json`, **501 bytes, sha256
`49f1cf260f0f18d5f52244c2a48bb5159765dd293633b750a9f0fbad39dcc7ae`** -- byte-equal to the copy saved before
TO-APPLY-4, which re-confirms the fence has been untouched since.

| half | its rollback, as that half states it |
|---|---|
| NFRA_CTLPLN (the dell2 line) | `4.0.0_SA_CRO` removes the cottonwood registry row in its own lane and the same targeted `safe-apply` runs again |
| ADVI_COTBKF (the three statements) | revert the statement rows in the `.tf` and `safe-apply` targeted on `aws_s3_bucket_policy.lgic_firm`; the ADVI_COTBKF CTO half adds that this is a **Deny removal, so nothing is deleted** (the `concat` tail is empty for every row) |
| same-window fallback, either | `s3api put-bucket-policy --policy file://<the saved document>`, which replays the exact bytes S3 returned, then the Terraform re-apply to reconcile state |

**Not undone by any rollback:** anything dell2 writes to the bucket while the grant stands.

## PRE-APPLY EVIDENCE IN HAND

- `s3-lgic-firm-buckets.tf` UNMODIFIED in the working tree and still byte-identical to the pin `3ec42c56bf` that
  `check_dell_fence_join.py` asserts (`706663b99f6d` at both refs), so that check cannot fail on its pin. Last
  changed by `8e58736597` (`0.9.0_WK_ADVI_COTBKF~15`, *"...nothing applied"*).
- The cottonwood registry row is present (5 principals, dell2 row present), landed `@e7ac51a04c` by `4.0.0_SA_CRO`.
- **AC1:** `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied
  other_rows_changed=0 validator=ok ok=True`; `terraform_validate=OK`; naming validator OK with **0 refusals**.
- **STEP 2, the prefix:** `commonwealth/cottonwood/bronze/crm/` holds **0 keys**, auto-paginated and counted
  client-side, **no object read**. Beside a POSITIVE CONTROL so the zero is a real absence and not a dead paginator
  or a mis-typed prefix: the same paginator reads **733 keys** at the bucket root.
- **THE PLAN:** `Plan: 0 to add, 1 to change, 0 to destroy`; 1 resource block; **47 added lines classified and 0
  removed** -- exactly one dell2 principal line and the three signed Sids, an EXACT SET MATCH with no fourth Sid;
  **zero `aws_iam_role` / `aws_iam_role_policy` / `restricted_breakglass` lines anywhere in the plan**; zero
  destroy/replace markers. Saved: `deliverables/PLAN5_cottonwood_20261007.txt`.
- The targeted argv was ECHOED BACK before use: it arrives intact through MSYS with brackets and quotes preserved.

## INSTRUMENT NOTES carried into the verify legs

Every arm reads `MatchedStatements`, so a refusal ON the prefix is attributed to the statement that caused it rather
than inferred -- which matters most here, because `DenyForeignFirmPrincipals` and the three new statements can both
refuse the same principal on the same bucket for different reasons. One resource ARN per call.
`simulate-principal-policy` has four false-DENY modes and one false-ALLOW mode measured on this project, so an
`allowed` is read as "the policy admits an ARN of that shape", never as proof an object exists; and the unlisted
principal's existence is proven by `get-role` before its arm is cited.

## NOT EXERCISED

**No object is read in any firm bucket by this seat** -- the prefix read was a key COUNT only. The box arm (dell2
reading one object from dell2 itself) is another route's. The dell2 reach is APPLIED, not EXERCISED.
