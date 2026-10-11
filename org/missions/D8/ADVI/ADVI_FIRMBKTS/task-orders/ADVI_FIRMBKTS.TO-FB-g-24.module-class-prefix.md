# ADVI_FIRMBKTS task order -- `FB-g-24` -- THE `opal_name` MODULE EXPOSES A SCOPE'S CANONICAL CLASS PREFIXES (THE CTO'S ACT-0 ADDENDUM 1: THE DELETE GRANT IS GENERATED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-24</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~46</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository files only; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. The output is read by a later cell that writes the grant.
comp-adversary: RUN by the issuer -- at base `r4_modclass.py` reads 2 of 5 (M3 `terraform test` and M4 dormant PASS as controls; M5 reads FAIL because the committed mark line is one registry edit behind, which this cell's regeneration repairs; M1 and M2 FAIL as expected: no local, no output). Blindness: `terraform test` runs the module's own vectors; it cannot see a root that reads the output by a name this cell adds.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-24` (round 4, workstream `FENCECLS`; the CTO's act-0 CTO half ADDENDUM 1, msg 3931)

The producers' grant (act 0) must gain `s3:DeleteObject` on exactly the two directories the stale-advisor cleanups delete
under (`D_04:789-812` and `D_02:3245-3280`). The naming gate refuses a typed key or prefix in HCL, so the two directories
must come from the module. The module already outputs `bucket`, `platinum_prefix` and `ownership_key` per scope; it lacks
the per-class directories. You add the generated local and the output, dormant.

### 1a. Behavior (the whole spec)

1. **The generated local.** In `lib/opal_naming.py` extend the renderer of `infra/aws/terraform/modules/opal_name/generated_locals.tf` so it also renders one local `class_prefix`:
   a map from each scope's LONG form to a map from each REGISTERED destination class's LEGACY prefix (the
   `legacy_prefix` of every row of `platinum_destinations.json`, e.g. `platinum/advisors/`) to that class's CANONICAL
   directory prefix, a string ending in `/` (e.g. `advi/<firm>/platinum/advisors/`). The canonical directory is what
   `lib/platinum_dest.py`'s canonical destination of a key under that legacy prefix has as its parent directory: derive it
   from the builder's own `address()` derivation (the one `platinum_prefix` and `ownership_key` use), never by string
   surgery on a literal. Every registered class is present (11 today), each once. Add the registry files it reads to that
   target's `TARGET_REGISTRY_KEYS` row if it reads any not already listed.
2. **The output.** In `infra/aws/terraform/modules/opal_name/main.tf` add `output "class_prefix"`: `var.scope == null ? null : lookup(local.class_prefix,
   var.scope, null)`, with a one-line description, in the file's own style. Existing outputs and locals are untouched.
3. **Dormant.** Every base line of `infra/aws/terraform/modules/opal_name/generated_locals.tf` and `infra/aws/terraform/modules/opal_name/main.tf` stays in order; the only additions are the new local, its comment,
   the output, and the generated file's mark line (which also moves because `exemptions.json` changed since the last
   regeneration: that is correct, the file is regenerated). `tests/vectors.json` and `tests/opal_name.tftest.hcl` do not
   change. Regenerate with the builder (`python lib/opal_naming.py generate --out /c/dev/wk-firmbkts-46 --target infra/aws/terraform/modules/opal_name/generated_locals.tf`), never by hand.

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
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~46/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~46/ADVI_FIRMBKTS.TO-FB-g-24.module-class-prefix.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-24"><invocation>cd /c/dev/wk-firmbkts-46 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modclass.py --arms module --root /c/dev/wk-firmbkts-46; echo "exit=$?"</invocation><expect>ROUND 4 MODULE CLASSES: 5 of 5 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-24"><invocation>cd /c/dev/wk-firmbkts-46 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-46 --allow lib/opal_naming.py --allow infra/aws/terraform/modules/opal_name/generated_locals.tf --allow infra/aws/terraform/modules/opal_name/main.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~46/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require lib/opal_naming.py --require infra/aws/terraform/modules/opal_name/generated_locals.tf --require infra/aws/terraform/modules/opal_name/main.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the local and the output, that each entry is the seam's canonical directory and sits under the platinum prefix,
that `terraform test` passes, that the base's lines are kept and that the file is the builder's output. AC2 is the
write-surface bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-24.module-class-prefix.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~46`.
Commit the three files and your rows, then the instance second. **Do not flip this order's `<status>`** (the issuer drains
it). Row ids: `ADVI_FIRMBKTS-D1-W46-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2
outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut on the CTO's act-0 CTO half ADDENDUM 1 (msg 3931): `s3:DeleteObject` on the exact prefixes the two
cleanups delete under, printed from the code. The grant cell (`FB-g-25`, `infra/aws/terraform/bd-pipeline/iam.tf`) follows this
merge; the fail-loud cell (`FB-g-26`) runs beside it. Row `ADVI_FIRMBKTS-D1-S29`. Workstream `FENCECLS`. Class WORLD by the
path floor, dormant.

<status>pending</status>
<round>4</round>
<workstream>FENCECLS</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-24</to_id>
<slot>~46</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
