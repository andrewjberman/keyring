# LGIC_ENFORCE -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~G`, 2026-09-14, in LGIC_ENFORCE's L6 issuance commit, so that the round's workers have a channel to
append to. **Home:** the project tree's channel. Lane `ANY`; the gate `.tools/surprise-row-gate.py` validates every NEW row
(schema, identity, coordinate, folder == project). **Append-only.** A worker's row id is `LGIC_ENFORCE-W<n>-S<k>`, where `<n>` is
its slot; a seat's is `LGIC_ENFORCE-S<k>`.

**Denominator at this write: 1 row, LGIC_ENFORCE-S1, which mints the channel.**

```json
[
  {
    "id": "LGIC_ENFORCE-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T19:40Z",
    "one_line": "The L6 coverage limb of the TO issuance gate reads every cell id a decomposition CITES as one of its own cells, so a decomposition that cites another project's cells cannot be covered by its own orders; and the audited override its refusal text offers is never read by that limb.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REFUSAL, exercised: this project's first L6 attempt (no commit was made) printed 'the issuance under org/missions/D14/LGIC/LGIC_ENFORCE/project.json owns 22 of 26 cell(s) ... MISSING: LN-f-1, LN-g-1, LN-h-3, LN-l-1'. All four are LGIC_NAMING cells that decomposition v1 @8d1d4d3e2f CITES, at :76, :89, :157, :159, :209, :305, :390 and :468 (10 citations).",
        "CODE, read: .tools/to-pipeline-gate.py@a369a0f55d _coverage_gap (:414-419) takes set(CELL_ID_RE.findall(decomp_text)) over the whole document, with no project scoping; CELL_ID_RE (:262-267) accepts any [A-Z][A-Z0-9]*- prefix.",
        "CODE, read and NOT exercised: the refusal (:473-476) offers 'take the audited # pipeline-override: on one order with the reason'. OVERRIDE_RE is read only in check_file (:2365-2386), which returns early with no violations for that ONE order. The coverage limb (:422-479, called at :2728-2731) never reads it. So by source, the named route leaves the refusal standing AND exempts that order from every per-file limb.",
        "DISCRIMINATOR, exercised: decomposition v1.1 @53d221f334 changed only the ten citations, to 'LGIC_NAMING cell <x-n>'. The gate's own _coverage_gap then read 22 ids with none missing, and the next issuance attempt's gate printed 'issuance coverage 22 of 22 cell(s)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3.0 L6 carrier 1, as the gate's docstring states it (:448-452): 'the union of <owned_cells> across the staged NEW orders must equal the named decomposition's cell set'. The refusal text: 'cut the missing order(s) in this same commit, or take the audited # pipeline-override: on one order with the reason'.",
    "world_is": "The gate's 'cell set' is every cell-id token anywhere in the decomposition, including cells of other projects cited as inputs or gates. And the one alternative the refusal names is not read by the limb that refused.",
    "notes": "Worked around in this project by decomposition v1.1: the citation form only, and no cell, edge, gate or criterion moved. The remedy is the gate owner's (1.0.0_SA_CTO): scope the id set to the project's own prefix or to the decomposition's cell table, and either honour the override in the coverage limb or drop it from the refusal text. INERT: the refusal fails closed, and no order was cut on the wrong set. The cost falls on the next seat whose decomposition cites another project's cells, and the refusal's own text sends that seat to the route that does not work."
  },
  {
    "id": "LGIC_ENFORCE-W3-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-14T20:10Z",
    "one_line": "GRADING_RULE.md grades (name, node_type) over the schema's 33 node types; no Terraform resource type is a node type and TO-EN-t-1 gives no map, so EN-t-1 graded under its own map of 34 Terraform types onto node types and RAISED the rest at G1.1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE, read: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@fd9c9ca174 G1.1 (:35-36): 'The type must be one of the 33 keys of DATA.kind.by_type and DATA.types_not_graded_by_kind, spelled exactly. Any other type RAISES.' org/standards/NAMING_SCHEMA.json@fd9c9ca174 node_type_vocabulary: every type key is a node_type value of the live-plane graph.",
        "CENSUS, run: deliverables/0.9.0_WK_LGIC_ENFORCE~3/instrument/census.py over the 468 tracked .tf files @fd9c9ca174 reads 2,035 resource blocks of 104 Terraform types: 34 mapped (28 to a graded node type, 6 to a NOT GRADED one), 30 that carry their own name and map to none, 40 that name nothing.",
        "RESULT, run: 690 of 2,035 labels and 66 of 1,332 name attributes RAISE at G1.1 because their Terraform type has no node type (deliverables/TF_LABEL_CENSUS.md section 3, branch wk-lgic-enforce-1-3)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-1 THE CELL: 'Grade each with the schema's rule ... Apply GRADING_RULE.md (LGIC_NAMING, merged) by its written steps'; the rule's G1.1 domain is the 33 node types.",
    "world_is": "The order hands over Terraform resource types (aws_iam_role_policy, aws_lambda_permission, ...), none of which is a node type, and names no map. The census's map is its own reading, stated in TF_LABEL_CENSUS.md section 3 (for example aws_iam_role_policy -> IAM_POLICY, aws_instance -> EC2_INSTANCE named by tags.Name, aws_apigatewayv2_route -> API_ROUTE).",
    "notes": "The seat that specifies the Terraform flagger (E8 second half) owns the choice of map; a different map moves the G1.1 counts and every mapped verdict. INERT: a report; nothing reads the map to act."
  },
  {
    "id": "LGIC_ENFORCE-W3-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-14T20:10Z",
    "one_line": "124 of the 1,332 Terraform name attributes are expressions, not names; the rule grades a written name, so EN-t-1 resolved 100 statically in their own directory (graded, value_claim inferred) and could not place 24 (22 RAISE at G3, 2 decided at G1.2).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE, read: GRADING_RULE.md@fd9c9ca174 G3 (:62-79) normalises a written name; NAMING_SCHEMA.json@fd9c9ca174 grade.unplaceable: 'A name the tokeniser cannot place ... RAISES.' Neither says what a Terraform expression (local.x, var.x, a template with each.key) is.",
        "CENSUS, run: census.py over the 468 tracked .tf files @fd9c9ca174: 1,208 literal values; 100 resolved through same-directory locals, variable defaults or same-directory resource name attributes (for example \"${local.bd49f_pull_name}-role\"); 24 not resolvable: 10 each.key, 4 var.firm with no default, 2 each.value.name, 2 var.function_name with no default, 2 a non-name attribute of aws_ses_domain_mail_from, 1 each.value, 1 local.firm_role_name[each.key], 1 var.firm_id, 1 each.value.family.",
        "READ: git ls-files infra/aws/terraform @fd9c9ca174 lists no .tfvars file, so a variable default is the only in-repo value a variable carries; an apply can override it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-1 THE CELL: 'list ... every resource-name ATTRIBUTE ... Grade each with the schema's rule.'",
    "world_is": "A name attribute's value is often a Terraform expression, which names nothing until Terraform evaluates it, and the order does not say whether to grade the expression text, an evaluated value, or neither. The census graded a literal as written, a same-directory static resolution where one exists (value_claim 'inferred', the resolved string in 'resolved'), and RAISED the rest at G3 (value_claim 'absent').",
    "notes": "The resolved values are inferred, not measured: a plan-time limb sees evaluated names and can grade what this census could not. INERT."
  },
  {
    "id": "LGIC_ENFORCE-W3-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-14T20:10Z",
    "one_line": "TO-EN-t-1 names role_name as a resource-name attribute, but no tracked resource block carries one; the names that module calls author (122 literal function_name arguments across 146 module blocks) are module arguments, outside a census of resource attributes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SEARCH, run: native Grep for the whole word role_name over infra/aws/terraform/*.tf in the worktree @fd9c9ca174: 0 occurrences across 0 files. POSITIVE CONTROL on the same path: the whole word function_name or a _role_name suffix, 462 occurrences across 155 files (the _role_name hits are local and variable names such as var.processor_role_name).",
        "CENSUS, run: census.py @fd9c9ca174 reads 146 top-level module blocks; their literal name-like arguments are 122, all function_name; the called module names its resource by var.function_name, which has no default inside the module directory, so a resource-attribute census cannot read those names."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-1 THE CELL: 'every resource-name ATTRIBUTE (name, function_name, bucket, role_name, and the like, whichever the resource type names by)'.",
    "world_is": "role_name is on no tracked resource block (the AWS provider names an IAM role by name). A name authored at a module call site is an argument of a module block, not an attribute of a resource block; the census counts them in its prose and grades none of them.",
    "notes": "Grading module-call names needs module instantiation (the call-site value carried into the module's resource), a wider cell than the order names. INERT."
  },
  {
    "id": "LGIC_ENFORCE-W3-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-14T20:15Z",
    "one_line": "GRADING_RULE.md is written against NAMING_SCHEMA.json v1.4 but the base carries v1.6: rule G2.3 RAISES log groups prefixed aws-waf-logs-, which v1.6 aws_fixed places outside the grade's domain, and 2 Terraform names hit it; FN1-FN4 (v1.5) are not in the rule either.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE, read: GRADING_RULE.md@fd9c9ca174 header (:7) 'org/standards/NAMING_SCHEMA.json v1.4, cited as DATA.<field>'; G2.3 (:56-57): 'A LOG_GROUP whose name does not begin with / (for example aws-waf-logs-*, RDSOSMetrics) ...' under G2, whose outputs RAISE.",
        "SCHEMA, read: org/standards/NAMING_SCHEMA.json@fd9c9ca174 version v1.6; aws_fixed.rule: 'names AWS fixes are OUTSIDE the grade's domain, like the NOT GRADED types: excluded, never a fourth verdict'; aws_fixed.by_name.LOG_GROUP includes 'prefix: aws-waf-logs-'. resource.function (FN1, v1.5): 'an agent noun is always written as its verb (publisher -> publish ...)'.",
        "CENSUS, run: census.py @fd9c9ca174 grades infra/aws/terraform/opal-gateway/waf.tf:22 aws-waf-logs-opal-gateway and infra/aws/terraform/portal-auth/waf-cloudfront.tf:282 aws-waf-logs-opal-cloudfront RAISE at G2.3; under v1.6 both are excluded."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-1 THE CELL: 'Grade each with the schema's rule ... Apply GRADING_RULE.md (LGIC_NAMING, merged) by its written steps and state which you used.'",
    "world_is": "The merged rule and the schema at the base disagree on at least two rulings: an AWS-fixed name is a RAISE in the rule and an exclusion in the schema, and FN1's verb form is in the schema and not in the rule. The census applied the rule as written, as ordered, and states both in TF_LABEL_CENSUS.md section 1.",
    "notes": "Not measured: how many canonical forms FN1 would change. check_en.py b1-agree grades EN-b-1's grade() against the rule's worked cases, so which of the two grade() follows decides these verdicts. INERT: nothing live moves on a grade."
  }
]
```
