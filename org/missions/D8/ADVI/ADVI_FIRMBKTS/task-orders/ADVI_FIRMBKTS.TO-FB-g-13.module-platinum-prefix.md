# ADVI_FIRMBKTS task order -- `FB-g-13` -- THE `opal_name` MODULE EXPOSES A SCOPE'S BUCKET AND CANONICAL PLATINUM PREFIX (THE CTO'S ADDENDUM 4, AHEAD OF FB-g-2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-13</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~34</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the builder, a module's generated locals and two outputs; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant.
comp-adversary: RUN by the issuer -- at base `r4_modgrant.py` reads 3 of 5 (M3 `terraform test` 48 passed, M4 dormant and M5 in-sync PASS as controls; M1 and M2 FAIL as expected: no local, no outputs). Blindness: `terraform test` runs the module's own vectors; it cannot see a root that reads an output by a name this cell adds.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-13` (round 4, workstream `OWNKEYS`; the CTO's round-3 ADDENDUM 4, msg 3853)

The producers' role grant (`FB-g-2`) needs the canonical platinum prefix of 49 Financial's bucket in a Terraform ARN. The
naming gate (ENFORCE) refuses a hand-typed `arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/*` (row
D1-W25-S1). The CTO ruled: the policy name comes from `opal_name` module output and the ARNs from `address()`. The
module (`infra/aws/terraform/modules/opal_name`) already outputs `name` and `scope_bucket` over a generated `generated_locals.tf`; it lacks the
canonical platinum prefix, and a per-scope `bucket` output that needs no firm token at the call site. You add both,
generated, with nothing deployed.

### 1a. Behavior (the whole spec)

1. **The generated local.** In `lib/opal_naming.py` extend the renderer of `infra/aws/terraform/modules/opal_name/generated_locals.tf` so it also renders one local
   `platinum_prefix`: a map from each scope's LONG form to its canonical served-platinum prefix (ending in `/`), for the
   scopes the destination registry places (today 49financial only). Derive it from the destination view the builder
   already builds for `platinum_dest_view.py` (`_platinum_build`; read it): the common leading path of every class
   template placed in that scope's bucket, which must end in `/platinum/`; the builder raises `RegistryError` when it
   does not. Nothing is typed per firm; the prefix is the builder's own output (the gate's `address()` rule). Add the
   registry files it reads to that target's `TARGET_REGISTRY_KEYS` row.
2. **The outputs.** In `infra/aws/terraform/modules/opal_name/main.tf` add two outputs, each null when `var.scope` is null:
   - `bucket`: `lookup(local.scope_bucket, var.scope, null)`;
   - `platinum_prefix`: `lookup(local.platinum_prefix, var.scope, null)`.
   Write them in the file's own style with a one-line description each. The existing outputs and locals are untouched.
3. **Dormant.** Every base line of `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/main.tf` stays, in order; the only additions are the new local, its
   comment, the two outputs, and the generated file's mark line (the registry list it names). `tests/vectors.json` and
   `tests/opal_name.tftest.hcl` do not change (their marks are over registry files this change does not alter). Regenerate
   with the builder (`python lib/opal_naming.py generate --out /c/dev/wk-firmbkts-34 --target infra/aws/terraform/modules/opal_name/generated_locals.tf`), never by hand.

## 2. BOUNDS

1. Files that change: `lib/opal_naming.py`, `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/main.tf`. No other file; no consumer root; no `apply`; no AWS call.
2. `terraform init -backend=false` and `terraform test` in the module folder are local and allowed; keep any `.terraform`
   directory out of the commit.
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
lib/opal_naming.py
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/main.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~34/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~34/ADVI_FIRMBKTS.TO-FB-g-13.module-platinum-prefix.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-13"><invocation>cd /c/dev/wk-firmbkts-34 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modgrant.py --arms module --root /c/dev/wk-firmbkts-34; echo "exit=$?"</invocation><expect>ROUND 4 MODULE GRANT: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-13"><invocation>cd /c/dev/wk-firmbkts-34 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-34 --allow lib/opal_naming.py --allow infra/aws/terraform/modules/opal_name/generated_locals.tf --allow infra/aws/terraform/modules/opal_name/main.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~34/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require lib/opal_naming.py --require infra/aws/terraform/modules/opal_name/generated_locals.tf --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the local and the two outputs, that the prefix is the common root of the seam's templates in that bucket, that
`terraform test` passes in the module folder, that the base's lines are all kept, and that the file is the builder's output.
AC2 is the write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-13.module-platinum-prefix.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~34`.
Commit the three files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W34-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2
outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's round-3 ADDENDUM 4; workstream `OWNKEYS`; follows FB-g-11 (same builder file) and runs
beside FB-g-12 (a different function and generated file; the issuer merges them in sequence). FB-g-2 is re-seated on this
cell's merge: the grant's policy name comes from the module's `name` output (system advi, scope 49financial, function
`platinum-canonical-rw`, kind `policy`), its bucket from `bucket`, its prefix from `platinum_prefix`. The module is
consumed by other roots; adding outputs and a local changes no plan.

<status>complete</status>
<round>4</round>
<workstream>OWNKEYS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-13</to_id>
<slot>~34</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
