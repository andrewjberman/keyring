# TO NFRA_SCHWABBF.TO-BF-j6 -- the schwab converter role carries a schwab-only variant of the one-way fan-in fence that leaves the 15 enumerated firm state resources writable (Terraform text only)

<to_id>NFRA_SCHWABBF.TO-BF-j6</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~1</issued_to>
<issued_by>2.0.0_SA_COO~SB</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>release-0840</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `BF-j-6` (`decompositions/NFRA_SCHWABBF_DECOMP_R6.md`) |
**outcome_ref:** FWD-1, FWD-6, FWD-8 | **depends_on:** `BF-k-6` (same worker, same file: run it after `TO-BF-k6`, on the same branch)

---

## WORKER FACE

### THE CELL

`BF-j-6` (surprise row `NFRA_SCHWABBF-S4`). Every silver converter role, the schwab one included, is attached to the shared policy `aws_iam_policy.one_way_fan_in_fence` (`infra/aws/terraform/opal-assets/router_iam.tf` lines 139-179) through `aws_iam_role_policy_attachment.silver_fence` (`infra/aws/terraform/opal-assets/silver.tf` about lines 532-538, `for_each = local.silver_families`). That policy's belt 1 (`DenyAnyS3MutationOutsideMonolith`) is an explicit Deny of nine S3 mutation actions (`local.s3_mutation_actions`) on everything except `opal-data-assets` (`NotResource` = the monolith bucket and its keys). An explicit Deny beats every Allow, so the schwab converter can NEVER write the state tier that PRD v1.0 C-TIERS places in the FIRM buckets (`opal-data-49financial`, `opal-data-cottonwood`), whatever `silver_state_write_schwab_firm` (round 5, `silver.tf` about lines 714-766) and the bucket-side exemption rows say. This cell gives the schwab role its OWN copy of the fence with exactly 15 more resources outside the Deny, and detaches the shared one from the schwab role only. It edits Terraform TEXT and adds one test; it runs no `terraform init`, `plan` or `apply` and no `aws` command.

**Build** (`infra/aws/terraform/opal-assets/silver.tf` only; the file already carries your `TO-BF-k6` edit: keep it).
1. `aws_iam_role_policy_attachment.silver_fence`: change `for_each = local.silver_families` to `for_each = { for k, v in local.silver_families : k => v if k != "schwab" }`. The keys of the other five families are unchanged, so their state addresses do not move.
2. New `resource "aws_iam_policy" "one_way_fan_in_fence_schwab"`: name `opal-assets-one-way-fan-in-fence-schwab`; the same three statements as the shared policy, same `Sid`s and same actions (`local.s3_mutation_actions`), with ONE change: belt 1's `NotResource` is the two monolith entries plus the 15 state object resources, written exactly as the resource list of `silver_state_write_schwab_firm` writes them (five masters: `08403355` under `opal-data-49financial/schwab/49financial/state/`, `08719286`, `08134043`, `08165601`, `08480305` under `opal-data-cottonwood/schwab/cottonwood/state/`; tables `complete`, `conversions`, `backfill_status`; `date=*/<master>.*`). Belts 2 and 3 reference the same locals (`local.source_buckets`, `local.inf_gold_sentinel_arn`) as the shared policy. To avoid typing the 15 resources twice, hoist them into one `locals` entry that BOTH `silver_state_write_schwab_firm` (its Resource list stays byte-identical in value) and the new policy use; if hoisting would change the rendered value of the existing policy, copy instead and let the test pin the two lists equal. A comment block (ASCII) states the reason and the rollback: revert this commit and re-apply.
3. New `resource "aws_iam_role_policy_attachment" "silver_fence_schwab"` attaching the new policy to `aws_iam_role.silver["schwab"].name`.
4. Test `data/canonical/schwab/tests/test_converter_fan_in_fence.py` (function names contain `fan_in_fence`), reading `silver.tf` and `router_iam.tf` as text in the style of `test_firm_prefix_grants.py` (read how it extracts a resource body and how its `terraform fmt` arm runs): (a) `silver_fence`'s `for_each` excludes `schwab` and the attachment `silver_fence_schwab` exists; (b) the variant's belt 1 `NotResource` holds the two monolith entries and exactly the 15 state resources, equal as a set to the resource list of `silver_state_write_schwab_firm`, each in the bucket the registry (`infra/logic/registry/scopes.json`, the firm's `bucket`) names, none ending in `/*` alone or in a bare bucket ARN; (c) belt 2 and belt 3 of the variant equal the shared policy's (same actions, same resource expressions); (d) the shared policy in `router_iam.tf` is byte-equal to `git show HEAD:infra/aws/terraform/opal-assets/router_iam.tf` (that file is not edited); (e) neither the variant nor the new Allow side grants a delete action on those resources (`s3:DeleteObject` appears in belt 1's Action list only); (f) `terraform fmt -check` on `silver.tf` passes (copy the existing arm).

### ACCEPTANCE

<criterion id="BF6-j6-AC1" cell_refs="BF-j-6"><invocation>python -m pytest data/canonical/schwab/tests/test_converter_fan_in_fence.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-j6-AC1` -- the schwab role leaves the shared fence for its own variant, which differs from the shared one by exactly the 15 state resources; nothing else changes.

<criterion id="BF6-j6-AC2" cell_refs="BF-j-6"><invocation>python -m pytest data/canonical/schwab/tests/test_firm_prefix_grants.py -q -p no:cacheprovider --color=no</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`BF6-j6-AC2` -- the control: the round-2 to round-5 grant arms (23 passed at the base) still pass with the edited `silver.tf`.

<expected_criteria>BF6-j6-AC1,BF6-j6-AC2</expected_criteria>

Dry-run at the base: AC1 "file or directory not found" (rc 4) -- FAIL as expected; AC2 `23 passed` -- PASS as expected (a control that must stay green). Before starting this order, run your `TO-BF-k6` AC1 once more: it must be green at your branch head.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit; `router_iam.tf` is READ-ONLY.
- **WORLD floor, nothing applied.** No `terraform init`, `plan` or `apply`, no `aws` command, no deploy. The apply is the NFRA CloudOps lane's act (`BF-r-3`) after the never-widen pair covers this fence change (CTO word owed).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing; read the investigation file for the highest `W1-S<k>` and use the next). Append the row to `org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md` at the BYTE level (do not use the Edit tool on that file: it mixes CRLF and LF; insert before the closing `]`; the previous last row gains a trailing comma). Do not weaken the test to pass.

<paths>
infra/aws/terraform/opal-assets/silver.tf
data/canonical/schwab/tests/test_converter_fan_in_fence.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_R6.md</decomp_doc> (round 6), cell `BF-j-6`.
<owned_cells>BF-j-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: BF6-j6-AC1, BF6-j6-AC2. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~1/NFRA_SCHWABBF.TO-BF-j6.converter-fence-variant.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> BF6-j6-AC1,BF6-j6-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the lines of the changed `for_each`, the new policy and the new attachment, whether you hoisted the 15 resources or copied them, the two pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- Terraform text; the converter is event-driven.
comp-iam: RUN -- scanned router_iam.tf (the shared fence, belts 1-3) and silver.tf (the attachment, the four converter write grants of rounds 2-5), 2 Terraform files; the diagnosis is READ FROM TEXT: the live attachment census (`aws iam list-entities-for-policy`) is the release act R1's check; BLIND: the live IAM plane (0 roles read). The 49F box role has no equivalent Deny (iam.tf: only the bd, cot and inf planes).
comp-adversary: DECLARED-NOT-APPLICABLE as a lens run; finding inlined: carving the schwab role out of the shared attachment for one apply leaves it briefly unfenced between the detach and the attach (seconds, same apply, no converter write outside the monolith is possible in that gap because no Allow outside the monolith exists until the same apply lands).
lane: the <paths> block IS the grant.
</preflight>

Source: row NFRA_SCHWABBF-S4; PRD v1.0 C-TIERS; CTO rulings 109966 and 109970 (converter state in the firm bucket); decomposition round 6 cell BF-j-6; BF-g-5 merge `f27dfcc831e`, BF-h-5 merge `27acf60210d`.
