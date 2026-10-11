# ADVI_FIRMBKTS task order -- `FB-g-30` -- ACT 4: THE FLIP COMMIT (ONE REGISTRY VALUE AND THE REGENERATED TARGETS)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-30</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~53</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository files only; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act and no grant. The act that deploys what this commit generates is a separate order under the act 4 pair (`NEVER_WIDEN_ROUND4_ACT4_CUTOVER_COO_HALF.md` and its ADDENDA, `..._CTO_HALF.md`, both SIGNED).
comp-adversary: RUN by the issuer -- at base `r4_flipcommit.py --verify` reads 2 of 4 (V3 `validate` and V4 in-sync PASS as controls; V1 and V2 FAIL as expected: no flip). The same tool rehearsed in a scratch worktree reads 4 of 4 at apply: 16 files, 1 registry, 2 value-changing, 13 mark-line only. Blindness: the check reads the repository only; it cannot see a deployed byte (the act's own reads do).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-30` (round 4, workstream `FLIPCOMMIT`; act 4, the act's ONE value)

Act 4's engagement is ONE registry value: the 49financial scope's alias `opal-data-bd` loses its `routed` marker, so the scope's
routed bucket becomes its own `opal-data-49financial`. Every generated target is then regenerated from the registry. You
make that commit, and ONLY that commit. You deploy nothing.

### 1a. Steps (the whole spec)

1. In `infra/logic/registry/scopes.json` make ONE text edit: in the alias block whose `"spelling"` is `"opal-data-bd"` of the scope whose `"key"` is
   `"49financial"`, change `"routed": true` to `"routed": false`. Every other byte of the file stays. (The tool does this.)
2. Run the tool that does steps 1 and 3 and prints what changed:
   `python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flipcommit.py --root /c/dev/wk-firmbkts-53 --apply`
   (it edits the registry text, runs `python lib/opal_naming.py generate --out <root>`, and reads the result).
3. Commit exactly the registry file and the regenerated targets below, nothing else, in ONE commit.

### 1b. The files this commit may change (the whole list; 1 registry and 15 generated targets)

The registry file and the regenerated targets the builder lists as changed in the rehearsal. The value-changing ones are
`infra/aws/lambda-edge/_shared/firm-config.mjs` (two `bucket:` lines) and `infra/aws/lambda/investor-reporting/_authz/loaders.py`
(one `"bucket"` line). The other thirteen change only their generated mark line (the registry hash).

### 1c. Rules

1. If the tool reads P3 FAIL (a value-changing set other than the two), STOP before the commit and file a BLOCKING row naming
   each extra target; do not commit.
2. The nested `portal/` submodule's `firmDisplayNames.generated.ts` is a generated target outside this repository's index:
   do NOT edit or commit anything under `portal/`; note in your report that its mark line is stale (a mark line only).
3. ASCII only; keep each file's own line endings. If the commit is refused by a gate, do not override or force: file a BLOCKING
   row with the gate's lines.

## 2. BOUNDS

1. One commit; the sixteen files above only. No deploy, no apply, no push, no other registry value.
2. If the registry's alias block does not read `"routed": true` before your edit, STOP: someone else moved it; file a BLOCKING
   row.

## 3. SURFACES

<paths>
infra/logic/registry/scopes.json
.tools/ds-precommit-check.py
data/assets/scripts/gold/investor_reporting/directory_runner.py
data/assets/scripts/gold/investor_reporting/holdings_snapshot.py
data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py
data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py
data/black_diamond/scripts/gold/lib/platinum_dest_view.py
data/firm_registry.json
data/mdpf/config/bronze_homes.json
infra/aws/lambda-edge/_shared/firm-config.mjs
infra/aws/lambda/exec-summary-generator/platinum_dest_view.py
infra/aws/lambda/investor-reporting/_authz/loaders.py
infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py
infra/aws/terraform/modules/opal_name/generated_locals.tf
infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl
infra/aws/terraform/modules/opal_name/tests/vectors.json
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~53/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~53/ADVI_FIRMBKTS.TO-FB-g-30.flip-commit.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-30"><invocation>cd /c/dev/wk-firmbkts-53 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_flipcommit.py --root /c/dev/wk-firmbkts-53 --verify --base BASEREF; echo "exit=$?"</invocation><expect>ROUND 4 FLIP COMMIT: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-30"><invocation>cd /c/dev/wk-firmbkts-53 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-53 --allow infra/logic/registry/scopes.json --allow .tools/ds-precommit-check.py --allow data/assets/scripts/gold/investor_reporting/directory_runner.py --allow data/assets/scripts/gold/investor_reporting/holdings_snapshot.py --allow data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py --allow data/black_diamond/scripts/bronze/_asset_dim_rest_pin.py --allow data/black_diamond/scripts/gold/lib/platinum_dest_view.py --allow data/firm_registry.json --allow data/mdpf/config/bronze_homes.json --allow infra/aws/lambda-edge/_shared/firm-config.mjs --allow infra/aws/lambda/exec-summary-generator/platinum_dest_view.py --allow infra/aws/lambda/investor-reporting/_authz/loaders.py --allow infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/platinum_dest_view.py --allow infra/aws/terraform/modules/opal_name/generated_locals.tf --allow infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl --allow infra/aws/terraform/modules/opal_name/tests/vectors.json --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~53/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/logic/registry/scopes.json --require infra/aws/lambda-edge/_shared/firm-config.mjs --require infra/aws/lambda/investor-reporting/_authz/loaders.py; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the committed flip against the base: the registry differs by exactly the one routed line, the value-changing set is
exactly the two targets, `validate` exits 0 and every changed target equals the builder's output. AC2 is the write-surface
bound. Each invocation terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-30.flip-commit.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~53`. The flip commit
FIRST, your rows and the instance second. **Do not flip this order's `<status>`** (the issuer drains it). Row ids:
`ADVI_FIRMBKTS-D1-W53-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: the tool's output lines, AC1 and AC2
outputs and the FULL 40-hex commit hash of the flip commit.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** STAGED for the window (act 4). Not spawned until the issuer's GO (the registry hash in every mark line is
the hash at the cut, so the commit is made in the window against the HEAD of that moment; BASEREF in AC1 is filled at the GO).
The worker's order grant covers the generated targets' lanes (a worker is admitted to exactly its order's paths). Its merge is
the issuer's, at the drain, immediately followed by `FB-g-31` (the eight re-pins), the integrate pass and the units' builds.
Workstream `FLIPCOMMIT`. Class WORLD by the path floor.

<status>parked</status>
<round>4</round>
<workstream>FLIPCOMMIT</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-30</to_id>
<slot>~53</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
