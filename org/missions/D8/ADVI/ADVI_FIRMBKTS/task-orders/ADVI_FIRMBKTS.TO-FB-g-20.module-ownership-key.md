# ADVI_FIRMBKTS task order -- `FB-g-20` -- THE `opal_name` MODULE EXPOSES A SCOPE'S CANONICAL OWNERSHIP KEY (THE CTO'S ADDENDUM 8: IDENTITY GRANTS ARE GENERATED THROUGH opal_name)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-20</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~42</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the builder and the module's files; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_modkey.py` reads 3 of 5 (M3 `terraform test`, M4 dormant and M5 in-sync PASS as controls; M1 and M2 FAIL as expected: no local, no output). Blindness: `terraform test` runs the module's own vectors; it cannot see a root that reads the output by a name this cell adds.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-20` (round 4, workstream `FENCE3B`; the CTO's round-3 ADDENDUM 8, msg 3915)

Act 3b gives each reader of the ownership map an identity-side `s3:GetObject` on the canonical ownership key, generated
through `opal_name` (the naming gate refuses a typed ARN). The module already outputs `bucket` and `platinum_prefix` per
scope (`FB-g-13`); it lacks the key. You add the generated local and the output, dormant, so ten roots can later write
`"arn:aws:s3:::${module.x.bucket}/${module.x.ownership_key}"`.

### 1a. Behavior (the whole spec)

1. **The generated local.** In `lib/opal_naming.py` extend the renderer of `infra/aws/terraform/modules/opal_name/generated_locals.tf` so it also renders one local `ownership_key`: a
   map from each scope's LONG form to the canonical key of its REGISTERED legacy ownership-map address (the same set
   `lib/opal_naming.py`'s `_blk_ownership_keys` uses: `legacy_addresses.json` rows keyed `...-ownership-map`, owner = the destination
   class that starts the template; the value is the seam's destination for that template, as `_blk_ownership_keys`
   derives `canonical`). Reuse that derivation (do not copy-and-type it). Add the registry files it reads to that target's
   `TARGET_REGISTRY_KEYS` row if it reads any not already listed.
2. **The output.** In `infra/aws/terraform/modules/opal_name/main.tf` add `output "ownership_key"`: `var.scope == null ? null : lookup(local.ownership_key,
   var.scope, null)`, with a one-line description, in the file's own style. Existing outputs and locals are untouched.
3. **Dormant.** Every base line of `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/main.tf` stays in order; the only additions are the new local, its comment,
   the output, and the generated file's mark line. `tests/vectors.json` and `tests/opal_name.tftest.hcl` do not change.
   Regenerate with the builder (`python lib/opal_naming.py generate --out /c/dev/wk-firmbkts-42 --target infra/aws/terraform/modules/opal_name/generated_locals.tf`), never by hand.

## 2. BOUNDS

1. Files that change: `lib/opal_naming.py`, `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/main.tf`. No other file; no consumer root; no apply; no AWS call.
2. `terraform init -backend=false` and `terraform test` in the module folder are local and allowed; keep `.terraform` out of
   the commit.
3. No firm, bucket or key literal is typed. If the commit is refused by the naming gate, do not override or force: file a
   BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
lib/opal_naming.py
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/main.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~42/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~42/ADVI_FIRMBKTS.TO-FB-g-20.module-ownership-key.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-20"><invocation>cd /c/dev/wk-firmbkts-42 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modkey.py --arms module --root /c/dev/wk-firmbkts-42; echo "exit=$?"</invocation><expect>ROUND 4 MODULE KEY: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-20"><invocation>cd /c/dev/wk-firmbkts-42 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-42 --allow lib/opal_naming.py --allow infra/aws/terraform/modules/opal_name/generated_locals.tf --allow infra/aws/terraform/modules/opal_name/main.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~42/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require lib/opal_naming.py --require infra/aws/terraform/modules/opal_name/generated_locals.tf --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the local and the output, that each entry is the seam's canonical destination and sits under the platinum
prefix, that `terraform test` passes, that the base's lines are kept and that the file is the builder's output. AC2 is the
write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-20.module-ownership-key.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~42`.
Commit the three files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W42-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2
outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** workstream `FENCE3B`; beside `FB-g-19` (a different region of `main.tf`; the issuer merges in sequence).
The ten identity-grant cells that consume this output follow (edge role, eight IRPT roots, exec-summary root); the
partners role already holds its Allow.

<status>pending</status>
<round>4</round>
<workstream>FENCE3B</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-20</to_id>
<slot>~42</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
