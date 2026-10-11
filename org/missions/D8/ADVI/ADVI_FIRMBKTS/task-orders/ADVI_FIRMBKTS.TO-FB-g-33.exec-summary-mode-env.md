# ADVI_FIRMBKTS task order -- `FB-g-33` -- ACT 4b'S CARRIER: THE EXEC-SUMMARY ROOT'S `platinum_mode` VARIABLE (ABSENT BY DEFAULT)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-33</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~56</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository files only; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- repository files only: no AWS act. The act that passes the variable (acts 4b and 4c) is staged under `org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/NEVER_WIDEN_ROUND4_ACT4BC_LAMBDAS_COO_HALF.md` and its CTO half, both SIGNED.
comp-adversary: RUN by the issuer -- at base `r4_modeenv.py` reads 2 of 4 (E3 dormant and E4 fmt PASS as controls; E1 and E2 FAIL as expected: no variable, no conditional). Blindness: the check reads the Terraform text; the effect of the variable is the act's own scoped plan (one attribute of one function's environment).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-33` (round 4, workstream `MODEEXEC`; acts 4b and 4c's carrier of the ONE environment value)

The acts move one Lambda to the canonical home by ONE environment value, `BD_PLATINUM_MODE=canonical`. The trunk must not carry
that value before the window (other seats apply this root for their own work), so the value rides a Terraform VARIABLE that is
ABSENT by default: the plan is byte-identical until the act passes `-var platinum_mode=canonical`.

### 1a. Behavior (the whole spec)

1. In `infra/aws/terraform/exec-summary/variables.tf` (a NEW file if it does not exist, else append) declare:
   `variable "platinum_mode"` with `type = string`, `default = ""`, a one-sentence description (acts 4b and 4c; empty means the
   Lambda's code default `legacy`), and a `validation` that admits exactly `""`, `"legacy"` and `"canonical"` (error message
   naming the three).
2. In `infra/aws/terraform/exec-summary/main.tf` make the `aws_lambda_function.exec_summary_generator`'s environment the base's map UNCHANGED plus one conditional: `merge(<the base map>,
   var.platinum_mode == "" ? {} : { BD_PLATINUM_MODE = var.platinum_mode })`. (The file's `environment { variables = {...} }` block keeps its five keys.) Every base key and value stays
   character for character; nothing else of the file changes.
3. `terraform fmt` must read clean on every file you change.

## 2. BOUNDS

1. Files that change: `infra/aws/terraform/exec-summary/main.tf` and `infra/aws/terraform/exec-summary/variables.tf`. No other file, no apply, no plan in the root, no AWS call.
2. Do not set the variable anywhere (no `.tfvars`, no default but `""`).
3. ASCII only; keep each file's own line endings. If the commit is refused by a gate, do not override or force: file a BLOCKING
   row with the gate's lines.

## 3. SURFACES

<paths>
infra/aws/terraform/exec-summary/main.tf
infra/aws/terraform/exec-summary/variables.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~56/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~56/ADVI_FIRMBKTS.TO-FB-g-33.mode-env.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-33"><invocation>cd /c/dev/wk-firmbkts-56 &amp;&amp; timeout 118 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_modeenv.py --arms var --cell exec --root /c/dev/wk-firmbkts-56 --base 9c6d5ea3ba; echo "exit=$?"</invocation><expect>ROUND 4 MODE ENV: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-33"><invocation>cd /c/dev/wk-firmbkts-56 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-56 --allow infra/aws/terraform/exec-summary/main.tf --allow infra/aws/terraform/exec-summary/variables.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~56/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/exec-summary/main.tf --require infra/aws/terraform/exec-summary/variables.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the variable (declared, string, default empty, validated), the environment (the base's map plus one conditional),
that the base's lines are kept and that the formatter is clean. AC2 is the write-surface bound. Each invocation terminates
inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-33.mode-env.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~56`. Commit the files
and your rows, then the instance second. **Do not flip this order's `<status>`**. Row ids: `ADVI_FIRMBKTS-D1-W56-S<k>`,
`k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the 4b/4c pair names "ONE environment value added: `BD_PLATINUM_MODE=canonical`" and the CTO's ADDENDUM 11
timing. Carrying it as an absent-by-default variable keeps the trunk dormant: `partners-api` is applied by other work
(`AMGT_RESAPP`), and an unconditional edit would flip it early. The act passes `-var platinum_mode=canonical` on its scoped
plan and apply; after the window the issuer asks for the default to be committed. Workstream `MODEEXEC`. Class WORLD by the path
floor, dormant.

<status>complete</status>
<round>4</round>
<workstream>MODEEXEC</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-g-33</to_id>
<slot>~56</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
