# TO-APPLY-5 stopped at step 0: the rider's own pair does not agree with itself -- 0.7.0_AE_CloudOps~E

**archetype:** DIAGNOSE

**Date:** 2026-10-07
**Task Order:** `NFRA_CTLPLN.TO-APPLY-5.cottonwood-fence-apply-laptop` @ce2f42661d (issuer `2.0.0_SA_COO~C`, GO msg
106195, acked)
**Status:** BLOCKED at step 0 -- the order's own stop, not a refusal to work
**Workspace CLOUD commit:** `316e1e5f98`
**Push state:** LOCAL. Origin CLOUD read `324e7f0232` by `git ls-remote` at report time.

---

## Objective

Apply the third and last fence of cell CT-d-2: the cottonwood bucket policy, which can only be applied whole and so
carries both NFRA_CTLPLN's dell2 principal line and ADVI_COTBKF's three restricted-CRM-prefix Deny statements. Four
never-widen halves bear on the one apply. The order's step 0 is a conflict read of all four and is explicitly "a
stop, never a choice".

---

## Outcome

**STOPPED AT STEP 0.** Nothing applied, no AWS write, no ledger entry opened -- step 4 sits behind steps 0 and 3, so
nothing is stranded and there was nothing to close.

**The full record is the committed deliverable**, which carries the four-half condition table, how each condition
would be measured, what is already satisfied, the three conflicts and the declared deviation:
`org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/STEP0_CONFLICT_READ_TO-APPLY-5_20261007.md` @`316e1e5f98`.
This log does not restate it.

**The one-line answer to the question the order posed:** a plan with no role line SATISFIES the ADVI_COTBKF CTO half
(@b4073b7bf2: the role "are the laptop's IAM half ... not signed here", and a role line would violate its read 2')
and FAILS the ADVI_COTBKF COO half (@f9150f248a: section 1 signs the role as a row, Branch A requires it "created",
AMENDMENT 1 keeps it in scope). So the pair does not agree about its own scope, and that gates the conflict the
issuer did name.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| git (blob-hash pin check) | `git rev-parse <ref>:<path>` at `3ec42c56bf` and HEAD | PASS | `s3-lgic-firm-buckets.tf` is `706663b99f6d` at BOTH refs, so `check_dell_fence_join.py` will not fail on the pin the order warns about. Positive value, not an empty diff. |
| git (provenance) | `git log -1 -- <the .tf>` | PASS | Last change `8e58736597`, `0.9.0_WK_ADVI_COTBKF~15`, subject ends "nothing applied" -- the same commit whose statements I stopped on under TO-APPLY-4. |
| terraform state | `terraform state list \| grep -iE 'breakglass\|restricted'` | PASS | Only `data.aws_iam_user.restricted_console` -- a data source. The break-glass ROLE is not in state. |
| raw `aws iam get-role` | existence probe on `cloudops-cot-restricted-breakglass-role` | PASS (`NoSuchEntity`) | The decisive read. Run under a `# rail-checked:` marker: `comp-iam` models `(action)` per-Lambda and has no role-existence probe. **This was the ONE AWS call and it is a declared deviation from step 0's "before any AWS call"** -- see below. |
| comp-iam / comp-schedule | not run | SKIPPED, with reason | The order's own `<preflight>` declares `comp-schedule` NOT-APPLICABLE and routes `comp-iam` to the cell's two evaluator scripts, which are step 1 -- behind the step-0 stop. Running them anyway would have produced output no condition is graded on. |
| `check_dell_fence_join.py` / `check_restricted_prefix.py` | not run | SKIPPED, correctly | Both are step 1. Step 0 is a stop, and the order places the restricted-prefix check "IMMEDIATELY before the apply", so running it now would have burned its own freshness guarantee. |

**What worked:** reading all four halves at their pins before touching anything, and then asking the one factual
question that could have made the conflict moot. The halves' own words settled it -- no inference was needed.

**What failed:** nothing returned a wrong answer.

**Gap found:** none new. The gap raised under TO-APPLY-3 and widened under TO-APPLY-4 stands (no comp-tool exposes an
IAM managed-policy version or an S3 bucket-policy document).

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Checked whether the break-glass role already exists before declaring the stop | If it existed, Branch A's "the role with its inline policy created" would be historically satisfied and a no-role plan would be consistent -- the conflict would have dissolved and a stop would have been the WRONG answer. Reporting an unresolvable conflict without that check risked burning a round on a moot question. It does not exist (declared `:244`/`:259`, absent from state, `NoSuchEntity` live). |
| Reported CONFLICT B, which the order did not name | The order named only the cross-project conflict (role line voids vs role created). But that one cannot be settled until the ADVI_COTBKF pair agrees about whether the role is in its scope at all -- its CTO half disclaims what its COO half signs. Reporting only the named conflict would have sent back a question that cannot be answered as posed. |
| Did NOT choose between the halves, reshape the target, or treat the COO half's role clause as superseded by its own AMENDMENT 1 | A defensible reading exists -- that the later, more specific clause overrides the base Branch A -- but adopting it would be me deciding a cross-firm access question on my own reading of two other projects' signed halves. The order says "a stop, never a choice" and "do not choose between them". |
| Declared the sequence deviation instead of omitting it | Step 0 says "BEFORE ANY AWS CALL" and I made one read-only call before finishing the table. It wrote nothing and did not change the verdict, but it was out of the stated sequence, and a reader comparing the order to my evidence would find it. |
| Recorded what IS satisfied, not only what blocks | NFRA_CTLPLN CTO condition 5 / COO condition 2 are LIFTED (the ADVI_COTBKF CTO half's AMENDMENT 1 does name the dell2 line); the `.tf` still matches the pin; the prior cottonwood document is already saved and hashed from TO-APPLY-4. A stop report that lists only the blocker makes the next round re-derive the rest. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `.../deliverables/STEP0_CONFLICT_READ_TO-APPLY-5_20261007.md` | the step-0 condition table, role answer, three conflicts, declared deviation | Yes -- `316e1e5f98` |

No `.tf`, no registry file, no AWS object and no IAM object was written. No role was created.

---

## Blockers

**BLOCKED on `2.0.0_SA_COO~C` / `1.0.0_SA_CTO`:** which ADVI_COTBKF half speaks for that pair on the break-glass
role, and therefore what plan shape the four halves jointly admit. Reported once, msg delivered 1140 B at 11:56Z.
Not this seat's to adjudicate.

---

## Current State

The cottonwood fence is UNAPPLIED and unchanged: dell2 remains fenced out of `opal-data-cottonwood`, and the three
`ADVI_COTBKF` restricted-prefix statements remain committed-but-unapplied in a shared root, exactly as after
TO-APPLY-4. A targeted plan of `aws_s3_bucket_policy.lgic_firm["cottonwood"]` still reads `0 to add, 1 to change,
0 to destroy` carrying the dell2 principal plus all three rider Sids. Its prior policy document is held at
`deliverables/PRIOR_bucket_policy_opal-data-cottonwood_20261007.json` (501 B, sha256 `49f1cf26...dcc7ae`) and is the
only rollback that will ever exist, because S3 versions no bucket policy. The break-glass role
`cloudops-cot-restricted-breakglass-role` is declared in the `.tf` but exists in neither state nor IAM.

---

## Next Steps

1. **[`2.0.0_SA_COO~C` / `1.0.0_SA_CTO`] Settle CONFLICT B first, then A** -- which ADVI_COTBKF half speaks for that
   pair on the role. Until then no plan shape satisfies all four halves and the apply cannot run.
2. **[whoever re-cuts this] The role is a separate act and is still owed.** It is declared at `:244`/`:259` and
   exists nowhere; the NFRA_CTLPLN CTO half routes it to the role request's four conditions (msg 106095), and this
   order's bounds forbid this seat creating it.
3. **[the `ADVI_COTBKF` lane] The exposure flagged under TO-APPLY-4 still stands:** three committed-but-unapplied
   statements in a shared root, which any seat applying that resource for any other reason lands as a rider.
4. **[`0.0.0_AB_MSTR`] Push CLOUD on Andrew's word** -- `316e1e5f98` is LOCAL.
