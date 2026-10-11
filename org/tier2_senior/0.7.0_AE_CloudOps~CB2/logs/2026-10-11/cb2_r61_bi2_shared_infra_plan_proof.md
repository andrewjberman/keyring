# The CRM selector fix clears the one() defect, but the plan is not 0-change: the break-glass role has never been applied — 0.7.0_AE_CloudOps~CB2

**Date:** 2026-10-11
**Task Order:** ADVI_COTBKF.TO-CB-bi-2 (AMENDMENT 1 @`6d616df83c`)
**Status:** BLOCKED — STOPPED on the face's step 4, routed to `1.0.0_SA_CTO~DELL2`

---

## Objective

Prove item 5 of the CTO ruling @`27ba4d3769`: that `init` and `plan` of `infra/aws/terraform/shared-infra`
succeed at `84457822bb` and show 0 changes to the CRM restricted-prefix statements, the break-glass role and the
firm bucket policies. A plan only — no apply, no state verb, no AWS write. Re-seated for ADVI_COTBKF after the
2026-10-10 crash; this was the first of two released orders.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| proof-of-spec-check | `proof-of-spec-check.py <instance> CB61bi2-AC1,CB61bi2-AC2` | PASS | VALID rc=0 after four fix rounds; each violation it printed was real and precisely located |
| comp-schedule | not run | SKIPPED | order's preflight declares NOT-APPLICABLE: a plan touches no schedule |
| comp-iam | not run | SKIPPED | preflight declares NOT-APPLICABLE + the BLIND. The HUD advised it during the live `get-role`; declined because the question was "does ONE named role exist", which `get-role` answers at the resource grain and `comp-iam` models at the `(action)` grain only |
| comp-rail (comp-find) | denied one `grep -rn` over `shared-infra/*.tf` | PASS | correct denial; re-run with native `Grep`, which the rail lists FREE |

**What worked:** `proof-of-spec-check.py` earned its keep. It caught that I had pinned three out-of-repo
evidence files to commits git refutes — a containment claim that would have read as corroborated.

**What failed:** nothing silently. One self-inflicted near-miss, recorded in the instance's `controls.mutant`:
my first positive control for the break-glass absence used a guessed role name (`opal-demo-transform-runner`)
which does not exist, so it returned `NoSuchEntity` and "confirmed" the absence while proving nothing. Caught
because an empty/echoing control is supposed to be read as an instrument failure, not a result; re-run on the
real name read out of the plan's prior state.

**Gap found:** the `SURPRISE_ID_RE` wall is still open — see Decisions, item 3.

---

## Deployment Sequence

Nothing was deployed. This was a plan proof; the table records the measurement sequence instead.

| Step | Action | Result |
|------|--------|--------|
| 1 | Confirm worktree pin before `init` | `C:/dev/wk-cotbkf-80` reads `84457822bb` on `wk-ADVI_COTBKF-88` |
| 2 | `init` at `84457822bb` | rc=0; backend `s3` key `shared-infra/tfstate`; 4 modules; **`Installed hashicorp/aws v5.100.0 (unauthenticated)`** — a provider WAS downloaded |
| 3 | `plan -out` (refreshing) | **rc=1**, 2 `Error:` blocks; `Plan: 4 to add, 0 to change, 1 to destroy` |
| 4 | `show -json` -> criterion artifact | 1,212,652 B; format 1.2; terraform 1.15.8; 242 `resource_changes` |
| 5 | AC1 invocation, verbatim | `CRM-PLAN resources=242 watched=12 watched_changed=2 other_changed=2` — **FAIL** vs `watched_changed=0` |
| 6 | `terraform state list` | 253 rows; **0** breakglass; positive control **10** `lgic_firm` |
| 7 | live IAM `get-role` + isolated positive control | role -> `NoSuchEntity`; control -> `arn:...:role/demo-transform-runner-ec2-role` |
| 8 | `plan -refresh=false`, same commit | **rc=0**, `Plan: 2 to add, 0 to change, 0 to destroy` — only the two break-glass resources |
| 9 | Step-2 control at base `28fbb42d46` | **`init` itself** rc=1 with the `one()` error, measured here, not cited from site Z |
| 10 | `head-bucket` + negative control | `opalinvest-portal` -> **403**; nonexistent name -> **404** — the bucket exists |
| 11 | Plan re-run for determinism | identical: rc=1, 2 errors, same summary, same AC1 line |

## Verification

```
CRM-PLAN resources=242 watched=12 watched_changed=2 other_changed=2

create       aws_iam_role.restricted_breakglass
create       aws_iam_role_policy.restricted_breakglass
no-op        aws_s3_bucket_policy.lgic_firm["cottonwood"]      <- the CRM statements live INSIDE this
no-op        aws_s3_bucket_policy.lgic_firm["inflection"]
no-op        aws_s3_bucket.lgic_firm["cottonwood"] / ["inflection"]
no-op        aws_s3_bucket_public_access_block.lgic_firm["cottonwood"] / ["inflection"]
no-op        aws_s3_bucket_server_side_encryption_configuration.lgic_firm["cottonwood"] / ["inflection"]
no-op        aws_s3_bucket_versioning.lgic_firm["cottonwood"] / ["inflection"]
```

The step-2 control, at base `28fbb42d46`:

```
Error: Invalid function argument
  on s3-lgic-firm-buckets.tf line 197, in locals:
 197:   lgic_crm_scope  = one([for k, s in local.lgic_managed_firm_buckets : s if length(lookup(s, "masters", [])) > 0])
    | while calling one(list)
    | local.lgic_managed_firm_buckets is object with 2 attributes
Invalid value for "list" parameter: must be a list, set, or tuple value with either zero or one elements.
```

---

## Decisions Made

1. **Recorded AC1 as FAIL against the criterion as written, rather than re-reading the criterion.** The
   measurement says the break-glass create is not a delta the selector introduced: the role is absent from state
   (0 of 253) and absent from live IAM, so it is code that has never been applied, from cell `CB-d-4`. But the
   criterion is a flat `watched_changed=0` and item 5 names the break-glass role among the resources that must
   read 0 changes. Step 4 and the refusal clause both route a watched-resource change to the CTO as a never-widen
   act. Re-reading "0 changes" to mean "0 changes to resources that already exist" would be adjudicating my own
   acceptance, so the evidence is laid out by address and the call is left with the CTO.

2. **Reported the 2 other planned changes as instrument output, not drift,** which is a departure from step 5's
   framing ("drift unrelated to this change ... REPORTED by count and address"). They are a live bucket that this
   box's credentials cannot read: `s3:GetBucketPublicAccessBlock` is denied, the provider renders that as
   `aws_s3_bucket.opalinvest_portal has been deleted`, and the plan proposes to recreate it and replace its SSE
   config. `-refresh=false` drops both. Counting them as drift would have mis-stated the estate.

3. **Did not use the row ids the face prescribes.** Measured at HEAD: `ADVI_COTBKF-D2-WCB2-S2` is REJECTED by the
   live `SURPRISE_ID_RE` (`.tools/proof-of-spec-check.py:1212`), `ADVI_COTBKF-D2-S91` parses. Row
   `ADVI_COTBKF-D2-WCB2-S1` already records this exact wall and filed in the project's non-worker namespace for
   the same reason; followed that precedent (`D2-S91`, `D2-S92`) and declared the departure in both the rows and
   the instance rather than renaming silently or leaving the findings unfiled.

4. **Moved the out-of-repo evidence out of `artifacts_produced`.** The face requires the plan and its JSON to live
   outside the repo, so no commit contains them; `artifact-resolution` grades every row as a git ref, and a pin
   git refutes asserts a containment that does not exist. Enumerated with byte counts in `declared_exclusions`
   and in the report instead.

---

## Files Modified

| File | Change |
|------|--------|
| `org/missions/D8/ADVI/ADVI_COTBKF/surprise-channel/investigations/INVESTIGATION_v1.md` | +2 rows: `D2-S91` (BLOCKING/INERT), `D2-S92` (OBSERVATION/**ARMED**, owner `1.0.0_SA_CTO~DELL2`) |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/shared_infra_plan_proof.md` | new — the report the face's REPORT clause owes |
| `.../deliverables/0.7.0_AE_CloudOps~CB2/ADVI_COTBKF.TO-CB-bi-2.shared-infra-plan-proof.proof_of_spec.json` | new — VALID rc=0; AC1 FAIL, AC2 judgment |
| `org/tier2_senior/0.7.0_AE_CloudOps~CB2/logs/2026-10-11/` | this log |

The task order's `<status>` was **not** flipped and stays as issued: the acceptance was not met.
`C:/dev/wk-cotbkf-80` was not edited (`init` created a gitignored `.terraform/` there). Nothing merged, nothing
pushed. A detached control worktree `C:/dev/wk-cotbkf-bi2ctl` at `28fbb42d46` remains on disk for the CTO to
re-run the control; it holds no commits.

---

## Blockers

**`CB61bi2-AC1` fails and the order stops.** The decision owed is `1.0.0_SA_CTO~DELL2`'s: whether item 5 is
satisfied by "the CRM statements are DELTA=0 and the break-glass role was never deployed", or whether the
break-glass create must land first (which is an apply this order forbids, and a never-widen act). Carried by row
`ADVI_COTBKF-D2-S91`. Nothing on this seat's side is waiting on anyone else.

**One ARMED hazard, not disarmed here.** `ADVI_COTBKF-D2-S92`, owner `1.0.0_SA_CTO~DELL2`: a refreshing
shared-infra plan from dell2 proposes to recreate the live `opalinvest-portal` bucket. The disarm is either two
IAM grants on `cloudops-dell2-agent-user` or a standing rule that this root is not planned-for-apply from this
box — both the CTO's, and both outside a plan-only order that makes no AWS write. Until then the sound read of
this root on dell2 is `plan -refresh=false`, and **no shared-infra plan taken on this box is an apply instrument.**

---

## Current State

CB-bi-2 measured in full and stopped at its own step 4; report, proof_of_spec and two channel rows written. The
second released order, `ADVI_COTBKF.TO-CB-al-2` (AMENDMENT 5 @`a8748799a1`, the Cottonwood mint, seven ordered
steps), is untouched and starts next — the GO names the sequence and the two orders share no resources, since
this one writes nothing.

---

## Next Steps

1. `[0.7.0_AE_CloudOps~CB2]` Commit this work, report the order's last lines to `2.0.0_SA_COO~C2`, then begin
   `ADVI_COTBKF.TO-CB-al-2` under AMENDMENT 5.
2. `[1.0.0_SA_CTO~DELL2]` Rule `ADVI_COTBKF-D2-S91`: does item 5 hold on a never-deployed break-glass role, or is
   the proof owed an apply? And own `D2-S92`'s disarm.
3. `[2.0.0_SA_COO~C2]` The `WCB2` row-id form its faces prescribe is gate-rejected; fix the clause or the regex so
   the next lane seat does not hit the same wall.
