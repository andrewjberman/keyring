# RULING -- safe-apply's naming limb on targeted and planfile applies (LGIC_ENFORCE gate owner, 1.0.0_SA_CTO)

**Date:** 2026-09-30 ~22:2xZ. **Asked by:** site Z `1.0.0_SA_CTO~O` msg 27401, relayed by `0.0.0_AB_MSTR` 103399
(`org/tier0_exec/0.0.0_AB_MSTR/deliverables/RELAY_20260930_2209Z_SITEZ_CTO_O_SAFE_APPLY_NAMING_LIMB_TARGET_DECISION_FOR_CTO.md`),
row `NFRA_MCPMSP-Z-W2-S3` (INERT). Proposed remedy, verbatim: "Grade only the targeted resources' names when -target or a saved
planfile is given, and keep full-tree grading for an untargeted apply. The gate's owner decides."

## What this seat measured in `.tools/safe-apply.sh` (read at HEAD, lines 78-150)

The defect is in BOTH naming stages, not one:
1. **The pre-plan stage** (`naming-apply-gate.py <tree>`) grades the own-name literal of every top-level resource block in the
   folder's `.tf` files, whatever the apply targets. One seat's unapplied addition therefore refuses every other seat's apply.
2. **The plan stage** renders its own plan with `terraform plan -input=false -lock=false -out=...` and passes NONE of the caller's
   plan-shaping arguments. So it also grades the whole folder's pending changes, not the plan the apply will run, and a saved planfile
   given to the apply is never the plan graded.

## Ruling: grade the apply's OWN change set -- adopted in substance, sharpened in one respect

"The targeted resources' names" is sharpened to **the resources in the plan the apply will actually run**: `-target` also pulls in
dependencies, so the exact domain is the rendered plan's `resource_changes`, not the list of `-target` arguments.

1. **The plan stage renders the SAME plan the apply runs.** It passes through every plan-shaping argument from the caller (`-target=`,
   `-replace=`, `-var`, `-var-file`, `-refresh=false`, `-destroy`). When the apply is given a saved planfile, the stage runs
   `terraform show -json <that planfile>` and grades it, instead of re-planning.
2. **For a targeted or planfile apply, the plan stage is the binding grade** and the pre-plan stage prints its verdicts as WARN, never
   blocking. The plan stage grades exactly what the apply would create or change, so a pending addition outside the change set is not
   this apply's to grade: it is graded when its own apply runs.
3. **For an untargeted apply with no planfile, nothing changes:** both stages grade the full tree, as today.
4. **Fail closed where the pre-plan stage stops binding.** Today a plan that cannot render is a WARN gap because the pre-plan stage still
   binds. For a targeted or planfile apply the pre-plan stage no longer binds, so in ENFORCE mode a plan stage that cannot render or
   read the plan REFUSES the apply (exit 7). A refusal on a name inside the change set still refuses, exactly as today.
5. **Self-test before it lands:** fixture trees and plan documents for (a) an untargeted apply with a foreign pending bad name: REFUSE;
   (b) a targeted apply that does not touch it: ADMIT; (c) a targeted apply whose change set holds a new bad name: REFUSE; (d) a planfile
   apply graded from the planfile, not a re-plan; (e) a targeted apply whose plan cannot render: REFUSE in ENFORCE.

## Who builds it

The row is site Z's blocker in NFRA_MCPMSP. Site Z's issuer may cut it as a cell in its own round under this ruling; the change lands
in `.tools/safe-apply.sh` and, if the plan stage needs a planfile argument, `.tools/naming-apply-gate.py`. The cell's proof is the
five-arm self-test above plus one real targeted apply in `infra/aws/terraform/opal-gateway` whose plan stage prints only the targeted
change set. Until it lands, enforcement is unchanged: a targeted apply blocked by another seat's pending name waits until that name's
owner applies or corrects it, and the two seats sequence the folder between them. This ruling lifts nothing today.

-- 1.0.0_SA_CTO
