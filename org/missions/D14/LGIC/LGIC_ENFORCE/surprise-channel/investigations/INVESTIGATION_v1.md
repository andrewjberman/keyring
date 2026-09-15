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
  },
  {
    "id": "LGIC_ENFORCE-W1-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T20:18Z",
    "one_line": "The unscoped whole-segment carrier census finds 12,917 hand-kept firm carriers across 1,506 files outside DEC-5's eight definitions; this round's generated views cover only the eight.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS, exercised at HEAD fd9c9ca174: comp-find -i over the order's whole-segment pattern, 38 top-level pathspecs (the worktree minus .scratch and the .git pointer), --all -> 'DENOMINATOR: 189011 hit(s) across 32448 file(s) scanned in scope [corpus=all]'. Partition: 12,949 token-hit carriers + 176,062 excluded = 189,011, plus 4 definition-pattern carriers (row LGIC_ENFORCE-W1-S2). Record: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md, json keys carriers and outside_dec5_rows.",
        "RULE, read: the carrier test is LGIC_ENFORCE_PRD.md@78128f29ea :266-277 -- a firm token in a string literal outside (a) the registry files, (b) a generated file, (c) a builder or lookup argument, (d) prose, comments and */tests/* fixtures is 'a HAND-KEPT CARRIER ... a second copy of a registry row'. (c) is empty at fd9c9ca174: lib/opal_naming.py does not exist yet.",
        "NAMED EXAMPLES at fd9c9ca174: comp-constants.config.yaml (170 carrier lines; file_lanes and search_surfaces keyed by cot, bd, inf); .tools/comp-secrets:56, :58, :59 (the firm pattern PRD DEC-5 names at :239); data/mdpf/config/partner_roster.json and its copy infra/aws/lambda/opal-assets/opal-assets-daily-emitter/partner_roster.json; infra/aws/lambda/ci/lambda-source-map.json (340); org/projects/NFRA_GRAPHUNI/NFRA_GRAPHUNI.P1.d_s3key_firm_qualified.json (295; read by infra/aws/globgrph/extract_pipeline_cloud.py:280 and extract_gold_compute.py:31).",
        "INSIDE DEC-5 FILES: 52 of the 12,917 sit in a DEC-5 file but outside its definition's span, for example data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py:46-50 FOREIGN_FIRM_BUCKETS, a second firm map beside FIRM_TREES; they are listed and mapped to this row too."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO LGIC_ENFORCE.TO-EN-c-1: the hand-kept firm carriers are re-derived by an unscoped read, the eight DEC-5 definitions must be among them, and 'A carrier OUTSIDE those eight is listed AND filed as one surprise row. The generated views of this round cover only the eight, so an extra one is a finding, never a silent extension.' PRD DEC-5 (:224-240) names eight definitions and says at least one carrier outside them (comp-secrets) is already known.",
    "world_is": "12,917 carriers across 1,506 files fall outside the eight definitions. Every one is listed in CARRIER_CENSUS.md's carriers and mapped to this row in outside_dec5_rows. They are filed as ONE row because they are one finding of one form, a hand-kept carrier this round's views do not generate; a row per carrier would be 12,917 rows with the same spec_asserts.",
    "notes": "Form only: this row grades no carrier as wrong and says nothing about which must move. Repointing consumers that compute a firm's location in their own code is ADVI_FIRMBKTS FWD-3's (PRD DEC-5 :241). The count applies the PRD's context rule literally, so every firm-token string literal in code or config is counted, including S3 key and resource-name literals, and the population is wide; the named examples are the maps and lists in DEC-5's sense. INERT: nothing in this round moves these carriers, and they stand exactly as at fd9c9ca174."
  },
  {
    "id": "LGIC_ENFORCE-W1-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T20:18Z",
    "one_line": "Four of DEC-5's eight definitions carry no firm token on or within 3 lines of their definition line, so the ordered token census cannot find them; the census admits them as definition-pattern carriers and counts them as +4 in its hits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS, exercised at fd9c9ca174: the whole-segment comp-find read has 0 hits within 3 lines of data/assets/scripts/gold/investor_reporting/directory_runner.py:170, data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:145, infra/aws/lambda/investor-reporting/_authz/loaders.py:43 and data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py:57 (the classifier's DEC-5 check printed 'carriers+-3: 0  token hits+-3: 0' for each of the four).",
        "CODE, read at fd9c9ca174: firm_bucket_map() (directory_runner.py:170, holdings_snapshot.py:145) parses FIRM_CONFIG out of firm-config.mjs with a regex and holds no firm token itself; bucket_for (loaders.py:43) maps a tenant through the JSON held in the environment variable named by DIRECTORY_BUCKET_ENV, so its firm values are not in the file; resolve_firm (perfrp_firm_pin.py:57) resolves over FIRM_TREES at :33-42, whose tokens are 16 or more lines away.",
        "CHECKER, read: check_en.py (fixed input, 2.0.0_SA_COO~G) c1_dec5 admits a carrier within 3 lines of each cited line (:246), and c1_partition requires len(carriers) + len(excluded) == denominator.hits (:253-256)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO EN-c-1: 'Read the repo for every firm long form ... as a WHOLE segment ... with comp-find'; 'Classify every hit'; 'The eight DEC-5 definitions ... must appear among your carriers'; 'hits equals the carriers plus the excluded.' PRD DEC-5 :238: 'Cell E1 first re-derives the whole carrier population by an unscoped read'.",
    "world_is": "The token read yields 4 of the 8 definitions (firm_registry.json, FIRM_CONFIG and the two precommit maps). The other 4 are functions with no token at their definition. To satisfy both 'must appear among your carriers' and 'hits equals the carriers plus the excluded', the record admits the 4 as kind 'function' carriers at their cited lines, taken from the L5 definition-pattern re-measure (decomposition v1.1 @53d221f334 :67-76). It states hits = 189,015 = 189,011 token hits + 4, with denominator.token_hits and denominator.definition_pattern_additions carrying the two halves.",
    "notes": "The token read and the definition-pattern read are two different instruments over one population, and the carrier population is not token-closed: a function that reads a map, a file or an environment variable carries the registry row without spelling a firm."
  },
  {
    "id": "LGIC_ENFORCE-W1-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T20:18Z",
    "one_line": "comp-find's default corpus reads a worker's untracked <WS>/.scratch/, so a census saved there is counted by the next census run (198,931 phantom hits here), and an :(exclude) pathspec scans 0 files instead of excluding one.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN 1, exercised at fd9c9ca174 with .scratch empty: a whole-word boundary pattern over the whole worktree -> 'DENOMINATOR: 374404 hit(s) across 32449 file(s)'; its --all output was saved to .scratch/census_all.txt (77,495,647 bytes).",
        "RUN 2, exercised: the order's segment pattern over the whole worktree -> 'DENOMINATOR: 387942 hit(s) across 32450 file(s)'; parsing its --all listing, 198,931 of those hits are lines of .scratch/census_all.txt, that is, run 1's output.",
        "EXCLUDE, exercised: the same pattern with the pathspec ':(exclude).scratch' -> 'DENOMINATOR: 0 hit(s) across 0 file(s) scanned in scope'.",
        "RUN 3, exercised: the same pattern over 38 positive pathspecs (every top-level entry but .scratch and .git) -> 'DENOMINATOR: 189011 hit(s) across 32448 file(s)', equal to run 2 minus its .scratch hits (189,011).",
        "STATE, read: git check-ignore .scratch/census_all.txt -> rc=1 (not ignored); .tools/comp-find@fd9c9ca174 docstring :60: 'untracked-not-ignored files IN scope. The boundary is the .gitignore, and only the .gitignore.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker definition: 'Scratch: <your worktree>/.scratch/ only'. TO EN-c-1: 'Read the repo ... with comp-find (the estate's instrument; print its denominator line)'.",
    "world_is": "Following both, the instrument's denominator includes the worker's own scratch output: the second run of the order's pattern printed 387,942 hits, 198,931 of them from the first run's saved output. The recorded census had to run over 38 explicit top-level pathspecs to keep .scratch out, because comp-find's :(exclude) form returns an empty scope rather than an exclusion.",
    "notes": "ARMED: any census worker that saves comp-find output under .scratch/ and then reads again gets an inflated denominator that still prints as measured, and the file-count delta is 1 per saved file, which is easy to miss. This round's EN-t-1 and EN-s-1 are census cells. disarm_owner is this round's issuer, who seats workers under the .scratch convention. Candidate remedies, none taken here: a .gitignore entry for .scratch/, comp-find honouring exclude pathspecs, or a worker-definition line saying where to save census output. This census's recorded denominator is run 3's."
  },
  {
    "id": "LGIC_ENFORCE-W2-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "comp-iam role <name>, the instrument TO-EN-c-2 names for the grant half, resolved 0 of the 94 roles the grants and belts name, although its own comp-iam roles listing carries 79 of them; a CamelCase control resolves.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: 94 calls of 'timeout 120 comp-iam role <name>' in worktree wk-lgic-enforce-1-2 @fd9c9ca174, 2026-09-14 after 20:01Z: 94 of 94 printed \"No role matching '<name>'\" (for example bd-exporter-ec2-role, opal-portal-lambda-role). Output kept in the worker's .scratch/c2/compiam_role_out.txt, not committed.",
        "EXERCISED: 'comp-iam roles' at the same HEAD prints 'IAM ROLES (209 found)'; 79 of the 94 names appear in it with a source: line (bd-exporter-ec2-role: tf_resource bd_exporter).",
        "CONTROL: 'comp-iam role FredMacroIngestionLambdaRole' prints 'ROLE: FredMacroIngestionLambdaRole', source infra/aws/terraform/fred-pipeline/iam.tf, statements: 3. 'comp-iam role fred_macro_ingestion' and 'comp-iam role bd_exporter' print No role matching.",
        "SUBSTITUTE, a different plane: aws iam get-account-authorization-details (read-only): 250 roles, 7 users, 1 group, 56 managed policies; list-roles 250 and list-users 7 agree; 48 of 48 attached managed policy ARNs resolve in the dump."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE, GRANTED: 'For each, give the grant line (policy name and statement, or .tf file and line). Use comp-iam role <name> per principal and the Terraform in infra/aws/terraform/.' Decomposition v1.1 s.6 (:411-412): 'EN-c-2 uses comp-iam role <name> per principal for the grant half of its census.'",
    "world_is": "comp-iam role returns No role matching for every hyphenated role name tried, 94 of 94, including 79 that comp-iam roles itself lists. So FENCE_WRITER_CENSUS.md takes each grant line from the live authorization dump (policy name, statement index and Sid), takes each role's .tf file from the comp-iam roles listing's source: line, and records the comp-iam role result per role in a comp_iam field.",
    "notes": "The census does not depend on comp-iam role: the live dump is a wider plane (250 live roles against comp-iam's 209 Terraform roles). The cause inside comp-iam was not investigated (the worker bound: nothing deeper). A seat that reads comp-iam role's No role matching as 'not declared in Terraform' is misled; recorded here, not fixed."
  },
  {
    "id": "LGIC_ENFORCE-W2-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "bd-gold-layer-runner, which the PRD names as a known legacy principal of opal-data-49financial, is not an IAM principal: it is a stopped EC2 instance whose instance profile carries bd-exporter-ec2-role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE READ: aws iam list-roles (250) and list-users (7), 2026-09-14 ~20:00Z: no role or user is named bd-gold-layer-runner. Roles with gold-layer in the name: bd-gold-layer-lambda-role, cot-gold-layer-ec2-role, inf-gold-layer-ec2-role, inf-gold-layer-lambda-role.",
        "LIVE READ: aws ec2 describe-instances --filters Name=tag:Name,Values=bd-gold-layer-runner -> i-01003b035d2988dfb, State stopped, IamInstanceProfile arn:aws:iam::313476888478:instance-profile/bd-exporter-profile.",
        "LIVE READ: aws iam get-instance-profile --instance-profile-name bd-exporter-profile -> Roles [bd-exporter-ec2-role].",
        "FILE: infra/aws/terraform/shared-infra/s3-49financial.tf:74-76 @fd9c9ca174: 'the ratified P2D-4 invocation contract executes the gold chain on bd-gold-layer-runner under bd-exporter-profile -- a bd-tree principal that MUST read silver inputs' outputs into gold here.'",
        "CENSUS: bd-exporter-ec2-role is granted on opal-data-49financial by a literal identity grant and is seen reading it 206 times in the window (FENCE_WRITER_CENSUS.md)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE_PRD.md v1.1 @78128f29ea :206-207, condition (ii): 'One is known already: the template's own comment names bd-gold-layer-runner. It is a legacy principal carrying the refused token bd, and it must read silver outputs into gold.'",
    "world_is": "bd-gold-layer-runner is the Name tag of EC2 instance i-01003b035d2988dfb (stopped). The IAM principal it runs as is bd-exporter-ec2-role, through instance profile bd-exporter-profile. The census carries bd-exporter-ec2-role, and no row carries bd-gold-layer-runner as a principal.",
    "notes": "An exemption or pattern keyed on the host name would match no principal ARN. Form only; which name the fence uses is EN-f-1's."
  },
  {
    "id": "LGIC_ENFORCE-W2-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "The served-key write trail logs platinum/firm/ writes on opal-data-bd, -inf and -cot only, so for opal-data-49financial no write is observed at all, not only writes outside platinum/firm/.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "LIVE READ: aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail, 2026-09-14 ~19:55Z: resources.ARN StartsWith arn:aws:s3:::opal-data-inf/platinum/firm/, arn:aws:s3:::opal-data-bd/platinum/firm/, arn:aws:s3:::opal-data-cot/platinum/firm/; readOnly false. No opal-data-49financial prefix.",
        "FILE: infra/aws/terraform/globgrph/item2e_served_write_trail.tf:30 @fd9c9ca174: served_write_trail_buckets = [\"opal-data-inf\", \"opal-data-bd\", \"opal-data-cot\"].",
        "LIVE READ: aws cloudtrail get-trail-status --name opal-served-key-write-trail: IsLogging true, StartLoggingTime 1783522018 (2026-07-08T14:46:58Z). The file's header, item2e_served_write_trail.tf:4, reads '*** PROPOSED -- NOT YET APPLIED ***'.",
        "CENSUS: the trail's 2026/09/14 us-east-1 log files (112 files, 2333 records) hold 2333 WriteOnly events on platinum/firm/ in the window: bd 1 writer, inf 1, cot 1, 49financial 0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE: 'The limit you must state: the org trail logs these buckets' data events ReadOnly (cloudtrail-organization-trail.tf:73), so writes outside platinum/firm/ are NOT observed.' SEEN: 'every principal item2e_served_write_trail.tf's WriteOnly events show WRITING platinum/firm/.'",
    "world_is": "For opal-data-49financial, writes INSIDE platinum/firm/ are not observed either, because the served trail does not select that bucket. Its seen-writer count of 0 is 0 by construction, not by measurement. The census's unobserved_writes sentence states this for opal-data-49financial.",
    "notes": "The decomposition already says the served trail covers 'three served buckets' (:88-90), and Andrew's ruling 6 (decomposition :93, gate G-W) names write logging on opal-data-bd, -inf and -cot, not -49financial. The trail and its stale header are outside this order's paths; left as found."
  },
  {
    "id": "LGIC_ENFORCE-W2-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-14T20:20Z",
    "one_line": "The order puts the role-side belts in GRANTED, but a belt is an explicit Deny; the 125 principal-bucket pairs that carry only a belt, and opal-data-49financial's bucket-policy Deny, are recorded beside granted, not in it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FILE: infra/aws/terraform/inf-pipeline/cross-firm-deny.tf:1-28 @fd9c9ca174 ('cross-firm Deny belt', 'the belts, each a standalone aws_iam_role_policy cross-firm-bucket-deny'); bd-pipeline/bd-silver-merge.tf:13 and :75 ('EXPLICIT DENY opal-data-cot (firm-sep belt)'). comp-find -i '\\bbelts?\\b' over infra/aws/terraform: 92 hits across 578 files.",
        "LIVE READ: the authorization dump (250 roles, 7 users): principals whose policies carry a Deny naming the bucket and no Allow on it: opal-data-bd 47, opal-data-inf 18, opal-data-cot 47, opal-data-49financial 13 (125 pairs).",
        "LIVE READ: aws s3api get-bucket-policy --bucket opal-data-49financial: one statement, Sid DenyForeignFirmPrincipals, Effect Deny, Principal '*', ArnLike role/cot-*, role/inf-*, role/mdpf-*, role/opal-assets-mdpf-*.",
        "FILE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:535-537 @fd9c9ca174: _writers_49 reads every principal in granted and seen of opal-data-49financial as a writer that EN-f-1 must cover."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-c-2 WORKER FACE: 'GRANTED: every principal an identity policy grants any s3:* action on the bucket or its objects, plus every principal the bucket's own policy names, plus the role-side belts.'",
    "world_is": "A Deny-only row under granted would be graded as a writer by the issuer's own consumer. FENCE_WRITER_CENSUS.md records them under buckets.<bucket>.belt_only (each with its Deny statement and token) and buckets.opal-data-49financial.bucket_policy_deny. A granted principal that also carries a belt lists that belt in its own belts field.",
    "notes": "The C2 criteria read granted and seen only (check_en.py:283-309), so this placement moves no C2 verdict. Whether belts belong under granted is the issuer's call."
  },
  {
    "id": "LGIC_ENFORCE-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T22:07Z",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W1-S3 (comp-find's default corpus reads a worker's own .scratch/). No recorded denominator in this round includes scratch output, and EN-s-1, the one census cell still to run, is spawned with its census output directed outside its worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S3@e0171ca585 is ARMED, with disarm_owner 2.0.0_SA_COO~G, naming this round's census cells EN-t-1 and EN-s-1.",
        "EN-c-1 was drained @7625f537b4. Its recorded denominator is its third run, over 38 explicit top-level pathspecs that leave .scratch out, as W1-S3 says. The issuer's re-run of c1-denominator on the slot's bytes printed PASS-DENOMINATOR.",
        "EN-t-1 was drained @dedf3bb3f9. Its denominator is `git ls-files infra/aws/terraform` restricted to .tf (468), which reads the index and never an untracked folder. The issuer's re-run of t1-denominators printed PASS-DENOMINATORS.",
        "EN-c-2 (drained @03062fcea1) read comp-iam, the IAM authorization dump and the org trail's data events; it ran no comp-find census over the repo.",
        "EN-s-1 (census mode over the repo and the live plane) is not yet spawned. It sits at level 3, after EN-b-1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": ".claude/agents/worker.md: 'Scratch: <your worktree>/.scratch/ only'. CLAUDE.md Rule 21: comp-find's default corpus is all -- tracked, untracked and gitignored, minus a printed ephemeral floor.",
    "world_is": "The worker's scratch convention puts census output inside the corpus comp-find reads by default. A census that saves its output there and then reads the repo again counts its own output, and comp-find's :(exclude) form scans nothing rather than excluding one folder.",
    "notes": "DISARM, per W1-S3's own clause, by its disarm owner. (1) The recorded denominators of EN-c-1, EN-t-1 and EN-c-2 are shown above to carry no scratch output. (2) EN-s-1's identity line at spawn directs its census output to a slot-unique folder outside its worktree and cites W1-S3; its face is not edited mid-round. (3) The structural remedies W1-S3 lists -- a .gitignore entry for .scratch/, comp-find honouring an exclude pathspec, a worker-definition line -- are outside this round's grants. They are carried to the round's drain-end read for 1.0.0_SA_CTO. INERT: no measurement in this round rests on a scratch-inflated count, and the one exposure left is closed at its spawn."
  },
  {
    "id": "LGIC_ENFORCE-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-14T23:21Z",
    "one_line": "Every LGIC_ENFORCE face's preflight says a path under .tools/ 'refuses by lane and is admitted only by this order's <paths>'. The owned-paths lane in fact admits ANY worker serial on .tools/, including a serial that holds no order. So the worker grant binds .tools/ only through the issuer's drain check, not through the lane.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, owned-paths-validate.py --check-agent at HEAD 94bd0afa97, 4 paths (.tools/naming-gate.py, .tools/naming-apply-gate.py, .tools/some-new-tool.py, lib/some_new_lib.py) for three serials: 0.9.0_WK_LGIC_ENFORCE~1 (six pending orders, none granting .tools/), 0.9.0_WK_LGIC_ENFORCE~9 (no order at all) and 0.9.0_WK_NOPROJECT~1 (no such project). Each printed 1 VIOLATION of 4, on lib/some_new_lib.py only; all three .tools/ paths were admitted.",
        "Found by G-C for slot ~1 before EN-r-1 spawned: the negative arm (.tools/naming-gate.py plus an infra .tf probe) refused 1 of 2.",
        "The faces' preflight line: 'A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>' (every LGIC_ENFORCE task order, record face)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 27 and RULING 1: 'A worker's write surface is exactly the <paths> its non-terminal order names (.tools/owned-paths-validate.py)'. The faces' lane line: .tools/ refuses by lane.",
    "world_is": "For .tools/ the lane is open to every worker serial, so a worker's .tools/ write outside its <paths> passes the lane gate at commit. What still refuses it is the issuer's per-order grant check at every drain (the changed files against that order's <paths>), which this issuer runs on every drain and which has read 0 outside-grant files on all 12 drains so far.",
    "notes": "INERT: the drain check covers it, and no drain in this round has carried an out-of-grant .tools/ file. Two cells of this round legitimately write .tools/ (EN-g-1 naming-gate.py, EN-t-2 naming-apply-gate.py), both through their <paths>. The faces' lane line overstates the lane for .tools/ and is this issuer's wording; the faces are frozen mid-round, so this row is the correction. Whether the .tools/ lane should enumerate workers is the lane owner's call (the owned-paths lanes' author), carried to the round's drain-end read for 1.0.0_SA_CTO."
  },
  {
    "id": "LGIC_ENFORCE-W1-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T23:22Z",
    "one_line": "DEC-5's loaders.py:43 bucket_for holds no firm data: it reads IRPT_DIRECTORY_BUCKET_MAP, which Terraform sets from data/firm_registry.json, so its generated view re-emits the function unchanged and no registry fact enters it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FILE: infra/aws/lambda/investor-reporting/_authz/loaders.py:29 and :43-53 @e0171ca585: bucket_for reads os.environ IRPT_DIRECTORY_BUCKET_MAP and raises BucketUnmapped for a tenant it cannot map.",
        "FILE: infra/aws/terraform/investor-reporting/directory/iam.tf:20-26 and :40 @e0171ca585: local.firm_bucket_map = { for f in local.client_firms : f.firm_id => f.bucket }, with client_firms read from data/firm_registry.json; lambda.tf:39 and schedule.tf:149 set IRPT_DIRECTORY_BUCKET_MAP = jsonencode(local.firm_bucket_map).",
        "EXERCISED: check_en.py exports_of on loaders.py at base e0171ca585, copied into a temp dir, returns 'raises BucketUnmapped' for every probe token (the env var unset); python lib/opal_naming.py generate reproduces it (check_en.py r1-generate: 'EXPORTS EQUAL: 7', of 7 carrier files)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-1 WORKER FACE and LGIC_ENFORCE_PRD.md DEC-5 :224-236 @78128f29ea: loaders.py:43 bucket_for is one of the eight carrier definitions, each to become a generated file of the registry.",
    "world_is": "The definition carries no registry row: its data path is Terraform, then the env var, then data/firm_registry.json, a carrier that EN-v-1 makes a generated view. lib/opal_naming.py's bucket_for block is a fixed template wrapped in the GENERATED markers, with a comment naming that data path.",
    "notes": "Whether loaders.py needs a generated view at all, or only the pointer to firm_registry.json it already has, is EN-v-4's and the issuer's call."
  },
  {
    "id": "LGIC_ENFORCE-W1-S5",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T23:22Z",
    "one_line": "generate's no-target contract includes infra/aws/terraform/modules/opal_name/tests/vectors.json, but the vectors are built over name(), cell EN-b-1's builder, so EN-r-1's generate prints SKIP for that file and writes the other eight.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: TO-EN-r-1 WORKER FACE, the CLI interface: 'With no --target, it writes the 8 DEC-5 carrier files, the module's generated locals, and infra/aws/terraform/modules/opal_name/tests/vectors.json'; the same face: 'the builders key, address, name and grade are EN-b-1's'.",
        "PRD: LGIC_ENFORCE_PRD.md DEC-3 :186-189 @78128f29ea: the module is proved against lib/opal_naming.name() on a vector file the Python builder generates.",
        "EXERCISED: python lib/opal_naming.py generate --out .scratch/gen_try printed 'SKIP infra/aws/terraform/modules/opal_name/tests/vectors.json (vectors are built over name(), cell EN-b-1's builder, which is not in this module yet)' and 'GENERATE: 8 written, 1 skipped', rc 0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-1 WORKER FACE: generate with no --target writes the 8 DEC-5 carrier files, the module's generated locals and vectors.json.",
    "world_is": "vectors.json cannot be written before name() exists. build_vectors() raises NotBuilt, and the vectors CLI verb exits 2. The decomposition's edge EN-b-1 -> EN-m-1 puts the builder before the module that reads the file.",
    "notes": "EN-b-1 replaces build_vectors(). No R1 criterion reads vectors.json."
  },
  {
    "id": "LGIC_ENFORCE-W1-S6",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T23:22Z",
    "one_line": "Nine of the sixteen system rows carry an owner_directive the register does not state (owner_claim inferred), and astn, trade and news, which GRADING_RULE.md V1 lists as PRODUCT systems, are held unresolved because no owner can be cited.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS: org/missions/DIRECTIVES.yaml @e0171ca585, a whole-token case-insensitive read attributed to each D-code block: yang 2 lines (D9), ycharts 4 (D9), smartx 2 (D3, D9), schwab 2 (D2, D3), trueshares 4 (D4); news, astn, trade, fred, seeking, orion, eclipse, blackdiamond and pathfinder 0 each.",
        "CENSUS: the mission tree org/missions/D<n>/<MACRO>/<CODE> @e0171ca585, 18 project directories: none is a yang, news, astn, trade, fred, seeking-alpha or vendor-feed project.",
        "EXERCISED: python lib/opal_naming.py validate printed 'VALIDATE: OK 16 system row(s), 9 scope row(s), 9 warning(s)', one WARN per inferred owner (yang, schwab, blackdiamond, orion, eclipse, smartx, pathfinder, fred, seeking-alpha)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-1 WORKER FACE and LGIC_ENFORCE_PRD.md DEC-1 :167-172 @78128f29ea: every systems.json row carries owner_directive, the D-code of the owning directive, which resolves in org/missions/DIRECTIVES.yaml.",
    "world_is": "The register names an owner for 7 of the 16 rows (mdpf D8, etfs D4, irpt D9, advi D2, amgt D5, trueshares D4, ycharts D9). The other 9 carry a reading, marked owner_claim inferred with its basis: 7 feeds read as D8 (Data Pipelines), pathfinder as D4 through the etfs product, and yang as D9. astn, trade and news sit in systems.json unresolved rather than under a guessed owner, so grade() will not resolve them as systems; none of GRADING_RULE.md's 43 worked cases names them.",
    "notes": "Confirming or correcting an owner is a registry edit. The validator prints each inferred owner as a WARN until then."
  },
  {
    "id": "LGIC_ENFORCE-W1-S7",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T23:22Z",
    "one_line": "check_en.py's _v_delta0 loads each carrier's BASE copy from a temp directory, where directory_runner.py (and, by the same imports, holdings_snapshot.py) cannot import trading_calendar, so EN-v-3's v3-delta0 reads FAIL whatever the view says.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "FILE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:726-741 @e0171ca585: at_base writes 'git show <base>:<path>' into tempfile.mkdtemp()/<path>, and _compare_carriers loads that copy first.",
        "FILE: data/assets/scripts/gold/investor_reporting/directory_runner.py:102-108 and holdings_snapshot.py:83-88 @e0171ca585: _REPO = _HERE.parents[4], sys.path gets _REPO/lib, then import trading_calendar. In a temp dir _REPO/lib does not exist; firm_bucket_map() also reads _REPO/infra/aws/lambda-edge/_shared/firm-config.mjs.",
        "EXERCISED, a discriminating pair on one instrument in one process: check_en.exports_of on the base copy in a temp dir printed 'AT-BASE LOAD FAILS data/assets/scripts/gold/investor_reporting/directory_runner.py ModuleNotFoundError No module named trading_calendar' and 'AT-BASE LOAD OK infra/aws/lambda/investor-reporting/_authz/loaders.py' (every token raises BucketUnmapped)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE_DECOMP.md EN-v-3 row @53d221f334: its exported content is byte-equivalent to the pre-image (DELTA=0), graded by check_en.py v3-delta0.",
    "world_is": "The pre-image side cannot be loaded outside the worktree, so the comparison records directory_runner.py as DIFFER before it reads the view. r1-generate is not affected: it loads the live carrier first, and that load puts lib/ on sys.path.",
    "notes": "holdings_snapshot.py is read, not exercised. The other v-cells' base copies (the JSON, the mjs, loaders.py, perfrp_firm_pin.py and ds-precommit-check.py) import only the standard library or nothing."
  },
  {
    "id": "LGIC_ENFORCE-W1-S8",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-14T23:22Z",
    "one_line": "To generate the eight carriers from the registry, scopes.json rows carry fields DEC-1 does not list (tenant, masters, monolith_scopes, pipeline_trees, trees, bucket_provisioned, and the alias fields planes, routed and provisioned), and a scope's bucket is its ruled opal-data-{long} form with the live legacy bucket an alias.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD: LGIC_ENFORCE_PRD.md DEC-1 :173 @78128f29ea: 'scopes.json rows: key, class, long, short, tenancy, bucket, aliases.'",
        "FILES @e0171ca585: data/firm_registry.json carries display_name, kind, enabled, email_domain, the portal/mdpf/pipeline scopes, tree_token and five nullable bindings per firm; firm-config.mjs:65-94 a displayName per tenant, mockadv included; perfrp_firm_pin.py:33-42 the ADVI tree; ds-precommit-check.py:68-71 and :110-113 the pipeline-directory separations. None of these is one of DEC-1's seven scope fields.",
        "EXERCISED: check_en.py r1-bd 'OCCURRENCES OUTSIDE AN alias/refused FIELD: []'; check_en.py r1-generate 'CARRIER FILES: 7  EXPORTS EQUAL: 7  DIFFER: []'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-1 WORKER FACE: scopes.json rows key, class, long, short, tenancy, bucket and aliases; bd appears only as an alias or a refused token.",
    "world_is": "Each added field holds one fact a carrier holds today, and each view is rendered from those fields (lib/opal_naming.py _firm_registry_rows, _separations, _blk_firm_trees). The live buckets opal-data-bd, opal-data-inf and opal-data-cot are bucket-plane aliases marked routed, because r1-bd refuses bd anywhere but an alias and GRADING_RULE.md grades opal-data-bd an ALIAS of opal-data-49financial. mockadv is an alias of 49financial with its own tenant block. Each registry file's _about states its fields.",
    "notes": "DEC-1's field list may be read as a minimum, and this as its extension; that read is the issuer's and 1.0.0_SA_CTO's to make."
  },
  {
    "id": "LGIC_ENFORCE-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T00:17Z",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W1-S7: check_en.py's v3-delta0 now loads each base copy beside its live file, so directory_runner.py's and holdings_snapshot.py's __file__-relative imports resolve. A base that equals its live copy reads PASS-DELTA0, where it read FAIL by construction.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S7 (ARMED, disarm_owner 2.0.0_SA_COO~G): the base copies were written into a temp tree, where trading_calendar and ids do not import.",
        "FIX @9951c799b1: fixed_inputs/check_en.py _v_delta0 writes each base copy as a hidden sibling of its live file, per exports_of's contract ('as if it lived at path'), and removes it afterwards.",
        "DISCRIMINATING PAIR, the same inputs for both (base = HEAD, so it equals live; not-yet-generated guard stubbed): the old instrument printed FAIL-DELTA-NONZERO (ModuleNotFoundError trading_calendar), and the patched one printed PASS-DELTA0 (2 of 2 exports equal).",
        "GUARD: unstubbed, v3-delta0 on the pre-view tree still prints FAIL-NOT-GENERATED. Sibling files left after the run: 0."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "EN-v-3's V3-AC2: 'the file's exported content equals its pre-image at the spawn base (DELTA=0)'.",
    "world_is": "Before the fix, no EN-v-3 view could satisfy V3-AC2, however correct. After it, the criterion measures the exports, as its text says.",
    "notes": "DISARM, per W1-S7's own clause, by its disarm owner, before EN-v-3 spawns; no worker ran the defective subcommand against a real view. The criterion text, the face and the fixtures are unchanged: the fix corrects the instrument's loader, a harness defect in the issuer's own fixed input, disclosed in its commit. INERT: EN-v-3 will be spawned from a base carrying the fix."
  },
  {
    "id": "LGIC_ENFORCE-W1-S9",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T00:43:07Z",
    "one_line": "The IV.3 control CloudWatchLogs (IAM_POLICY) OUT-OF-PATTERN does not follow from GRADING_RULE.md as written, which RAISES it at R1.f; grade() reaches the order's verdict only by rejoining the camel pieces of one word into a vocabulary word (cloud+watch -> cloudwatch), a step the rule does not state.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md @ce7349b7cc (byte-identical at HEAD 2a6c7d8543): N2 :68-70 splits before each capital, so CloudWatchLogs gives cloud, watch, logs; V3 :109-110 lists the purpose word cloudwatch as one token; R1.f :149-150 'Any other t1 is in no vocabulary. RAISE'. V1 :92 states the one multi-token match the rule makes: seeking-alpha, 'two tokens, matched as one'.",
        "SIBLING: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md :2262, :2462, :2599, :2902, :3023 @1cc0d2fe73 grade the literal CloudWatchLogs 'RAISE ... R1.f: t1 cloud is in no vocabulary'.",
        "ORDER: LGIC_ENFORCE.TO-EN-b-1 WORKER FACE and PRD LGIC_ENFORCE_PRD.md :350 @78128f29ea (E3): 'CloudWatchLogs OUT-OF-PATTERN'; check_en.py b1-controls wants OUT-OF-PATTERN.",
        "EXERCISED: lib/opal_naming.py _res_tokens rejoins pieces of ONE original segment whose concatenation is a V1/V2/V3/V4 word: grade('CloudWatchLogs','IAM_POLICY') = ('OUT-OF-PATTERN', '{system}-cloudwatch-logs-policy'); grade('cloud-watch-logs','IAM_POLICY') still RaiseDefect 'R1.f: 'cloud' is in no vocabulary'. Mutant arm with the rejoin removed: b1-controls 'CONTROLS: 4  CORRECT: 3', b1-agree 'WORKED CASES: 43  AGREE: 43' -- no worked case turns on it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-b-1 WORKER FACE: grade() implements the written rule EXACTLY; the brief's IV.3 control CloudWatchLogs (IAM_POLICY) is OUT-OF-PATTERN.",
    "world_is": "The written rule tokenises CloudWatchLogs to cloud, watch, logs and RAISES at R1.f, as sibling cell EN-t-1 recorded five times. To meet the control, grade() carries one reading the rule does not write: camel pieces of one word rejoin into the vocabulary word they spell, the camel-case analogue of V1's seeking-alpha. No worked case depends on the reading.",
    "notes": "Which side carries the defect, the rule's R1/N2 or the control, is graded against the rule under the PRD's CONTRACTS row 2. That grading belongs to the rule's owner."
  },
  {
    "id": "LGIC_ENFORCE-W1-S10",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T00:43:07Z",
    "one_line": "The IV.3 control opal-data-inf/silver/x (S3Key) OUT-OF-PATTERN naming {source} does not follow from GRADING_RULE.md K1, which RAISES a key whose segment 1 is neither a source nor a tier; grade() reaches it by taking a bucket the registry knows out of segment 1 as the key's container.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE: GRADING_RULE.md @ce7349b7cc K1 :254-259 'Anything else RAISES, because segment 1 is neither a source nor a tier'; K5.c :284-285 'The S3Key node carries no bucket, and the bucket is what decides them'.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json key.container '{bucket} -- the bucket that holds the key; NEVER a segment of the key'.",
        "ORDER: TO-EN-b-1 WORKER FACE; PRD LGIC_ENFORCE_PRD.md :282-283 @78128f29ea 'For opal-data-inf/silver/x, that slot is {source}, unless the producer declares its source. It never guesses.'",
        "EXERCISED: grade('opal-data-inf/silver/x','S3Key') = ('OUT-OF-PATTERN', '{source}/inflection/silver/x'): opal-data-inf is a bucket alias of inflection in infra/logic/registry/scopes.json @a925c8a642, so the scope is filled and {source} is named. grade('opal-data-zzz/silver/x','S3Key') still RaiseDefect 'K1: segment 1 'opal-data-zzz' is neither a source nor a tier'. Mutant arm with the container step removed: b1-controls 'CONTROLS: 4  CORRECT: 3'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-b-1 WORKER FACE: grade() implements the written rule EXACTLY; opal-data-inf/silver/x (S3Key) is OUT-OF-PATTERN, with {source} named as the unfilled slot.",
    "world_is": "K1 as written RAISES this key. grade() adds one step the rule does not write: a first segment that is a bucket the registry knows (standing shared, a scope's bucket, or a bucket alias) is taken out as the container, fills the scope a firm's bucket decides, and the rest is graded. An unknown bucket-like first segment still RAISES.",
    "notes": "The PRD's singular 'that slot is {source}' implies that the scope slot is filled. Filling it from a legacy bucket alias (opal-data-inf -> inflection) is this reading. The commit limb's fixture 01_new_key_literal.patch uses the same key shape."
  },
  {
    "id": "LGIC_ENFORCE-W1-S11",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T00:43:07Z",
    "one_line": "grade() reads its system vocabulary from infra/logic/registry/systems.json, where astn, trade and news are unresolved, so it RAISES on a name whose system slot needs one of them, where GRADING_RULE.md V1 lists all three as PRODUCT systems and gives a verdict.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE: GRADING_RULE.md @ce7349b7cc V1 :91 lists irpt, advi, yang, news, astn, amgt, trade as PRODUCT; :95-97 'V1 is INTERIM. The registry rows belong to LGIC_ENFORCE (PRD CONTRACTS row 3)'.",
        "REGISTRY: infra/logic/registry/systems.json @a925c8a642 'unresolved' holds astn, trade and news, for want of a citable owner_directive (row LGIC_ENFORCE-W1-S6).",
        "EXERCISED: grade('astn-foo-lambda','LAMBDA'), grade('trade-foo-lambda','LAMBDA') and grade('news-foo-lambda','LAMBDA') each RaiseDefect 'R1.c: ... is an unresolved token (V2)'. None of the 43 worked cases carries one: b1-agree 'WORKED CASES: 43  AGREE: 43  DISAGREE: 0'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-b-1 WORKER FACE: grade() implements the written rule EXACTLY; the builders read the registry at run time and copy none of it.",
    "world_is": "The two instructions diverge on three tokens. The module takes the registry, which the rule's own V1 defers to, so a name led by astn, trade or news RAISES rather than grading. The divergence closes when those three rows gain an owner_directive.",
    "notes": "Downstream consumer: EN-s-1's census stops on a RAISE (DEC-7). A live name led by one of these three tokens would stop that run."
  },
  {
    "id": "LGIC_ENFORCE-W6-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~6",
    "surfaced_at": "2026-09-15T00:49Z",
    "one_line": "EN-v-5 could not commit the carrier, instance and flip together. Before staging, proof-of-spec-check refuses a PENDING-THIS-COMMIT row on a MODIFIED tracked carrier, and Rule 14a forbids pre-staging, so the carrier went in its own commit efacdee1e0 and the proof pins it.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: python .tools/proof-of-spec-check.py <EN-v-5 instance> V5-AC1,V5-AC2 with the carrier row at PENDING-THIS-COMMIT and the carrier modified but unstaged in wk-lgic-enforce-1-6: 'VIOLATION: artifact-resolution: 'data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py' is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged -- it will not ride this commit; pin the row to the commit that carried it (CCX class)' INVALID (rc=1).",
        "CODE: .tools/proof-of-spec-check.py:379-384 @b02fdaa849. In PRE-COMMIT context a PENDING row passes only when the path is in `git diff --cached`; a path that is tracked (ls-files --error-unmatch) and not staged is refused, whether or not the worktree changed it.",
        "CONTRAST: the sibling instance deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-r-1...proof_of_spec.json carries PENDING-THIS-COMMIT on NEW (untracked) files, which the dry run counts as pending-on-worktree, not as a violation.",
        "REMEDY TAKEN (the checker's own words: 'pin the row to the commit that carried it'): carrier alone at efacdee1e0; the instance row pinned efacdee1e0 with introduces ['END GENERATED [FIRM_TREES]'] (present at the pin, absent at b02fdaa849)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Worker definition, Proof: 'rc 0 AND every mechanical criterion PASS-by-output, then flip the task order's <status> to complete and commit instance, deliverables and flip together'; Rule 14a: 'do NOT pre-git add'.",
    "world_is": "For a cell that MODIFIES a tracked file, the pre-flip manual validation cannot return rc 0 while the deliverable is uncommitted and unstaged. Instance, deliverable and flip cannot ride one commit without pre-staging, so the deliverable took a commit of its own.",
    "notes": "Form only. Every EN-v-<n> cell modifies a tracked carrier, so the same shape is expected on each of them. The order stayed open until the proof commit; no criterion was affected."
  },
  {
    "id": "LGIC_ENFORCE-W5-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~5",
    "surfaced_at": "2026-09-15T00:40Z",
    "one_line": "EN-v-3's generated firm_bucket_map() returns the same five tenant->bucket pairs as its pre-image, in a different ITERATION ORDER: registry order (49financial, inflection, cottonwood, mockadv, demo) where the pre-image returned firm-config.mjs order (49financial, inflection, mockadv, demo, cottonwood). check_en.py compares the exports with ==, which does not see order.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRE-IMAGE @b02fdaa849: data/assets/scripts/gold/investor_reporting/directory_runner.py:170-174 and holdings_snapshot.py:145-153 parse FIRM_CONFIG out of infra/aws/lambda-edge/_shared/firm-config.mjs, whose tenant blocks sit at :66 49financial, :70 inflection, :74 mockadv, :78 demo, :87 cottonwood.",
        "VIEW (branch wk-lgic-enforce-1-5, generated at registry@50e4fabd1cb6a150): directory_runner.py:170-180 and holdings_snapshot.py:145-155 return a dict literal ordered 49financial, inflection, cottonwood, mockadv, demo.",
        "EXERCISED: .scratch/ctl_v3.py ARM O, check_en.py's own exports_of over the base copy and the view: MAPPING-EQUAL True, ORDER-EQUAL False, for each of 2 files; check_en.py v3-delta0 'BASE: b02fdaa849  FILES: 2  EXPORTS EQUAL: 2  DIFFER: []' (its comparison, check_en.py:381, is a == b over dicts).",
        "CALL SITES in the two carriers: directory_runner.py:876 (the map is passed to run_firm; the loop at :886 walks client_firms(), not the map) and holdings_snapshot.py:510, :667, :866, :1223-1224 (keyed .get). 5 of 5 in-file call sites use keyed lookups or pass the map on; none iterates it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-v-3 WORKER FACE: 'The first generation is BYTE-EQUIVALENT in what it exports (DELTA=0)'; V3-AC2: 'the file's exported content equals its pre-image at the spawn base (DELTA=0)'.",
    "world_is": "The exported mapping is equal key for key and value for value, and V3-AC2 reads PASS-DELTA0; its insertion order is not the pre-image's. The generated block cannot be reordered by hand without breaking its GENERATED mark, and lib/opal_naming.py, which fixes the order, is outside this order's <paths>.",
    "notes": "INERT on the 5 in-file call sites read above. Importers of firm_bucket_map() outside the two carriers were not censused (outside this order's face). Whether order is part of 'what it exports' is for 2.0.0_SA_COO~G and 3.0.0_SA_CVO to decide."
  }
,  {
    "id": "LGIC_ENFORCE-W5-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~5",
    "surfaced_at": "2026-09-15T00:40Z",
    "one_line": "V3-AC3 describes the consumer test's firm_bucket_map as read from firm-config.mjs, and test_directory_runner.py:77 is named test_firm_bucket_map_comes_from_firm_config_mjs. Once the EN-v-3 view lands, firm_bucket_map() reads no file (it returns a literal generated from the registry), and the test passes because it asserts values only.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "TO: org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-v-3.irpt-firm-bucket-map.md @b02fdaa849, V3-AC3: 'its consumers' existing tests pass: data/assets/scripts/gold/investor_reporting/tests/test_directory_runner.py (its firm_bucket_map is read from firm-config.mjs)'.",
        "TEST @b02fdaa849: test_directory_runner.py:77-80 'def test_firm_bucket_map_comes_from_firm_config_mjs(): m = dr.firm_bucket_map(); assert m[\"49financial\"] == \"opal-data-bd\"; assert m[\"inflection\"] == \"opal-data-inf\"'.",
        "VIEW (branch wk-lgic-enforce-1-5): directory_runner.py:170-180 is a GENERATED block returning a dict literal; firm_bucket_map() no longer reads FIRM_CONFIG_PATH, and _FIRM_CFG_RE at :166-167 is left defined with no reader in the function.",
        "EXERCISED: check_en.py v3-tests 'CMD: python -m pytest -q data/assets/scripts/gold/investor_reporting/tests/test_directory_runner.py  rc=0  20 passed' / 'VERDICT: PASS-CONSUMER-TESTS'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-v-3 V3-AC3: the consumer test's firm_bucket_map 'is read from firm-config.mjs'.",
    "world_is": "After the view, firm_bucket_map() reads no file. The test's name still names firm-config.mjs as the source, and its value assertions pass against the registry-generated literal. The test file is outside this order's <paths> and is unchanged.",
    "notes": "INERT: the test still checks the values the map serves. The mismatch is between the test's name and the function's source. Renaming or re-pointing the test is not this cell's work."
  },
  {
    "id": "LGIC_ENFORCE-W5-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~5",
    "surfaced_at": "2026-09-15T01:03Z",
    "one_line": "The order's proof validation, run as a dry run before the flip (nothing staged, per Rule 14a's no pre-add), returns INVALID rc=1 for an EN-v cell. Its artifacts are MODIFIED tracked carriers, and proof-of-spec-check.py:383-386 refuses any PENDING-THIS-COMMIT path that is tracked and unstaged as CCX ('ALREADY COMMITTED at HEAD'). The same instance reads VALID rc=0 against a temporary index holding the commit's paths.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED dry run (branch wk-lgic-enforce-1-5, nothing staged): 'VIOLATION: artifact-resolution: data/assets/scripts/gold/investor_reporting/directory_runner.py is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged' and the same for holdings_snapshot.py; 'INVALID (rc=1)'.",
        ".tools/proof-of-spec-check.py:344-354 and :379-386 @b02fdaa849: an unstaged instance sets ctx PRE-COMMIT with dry_run true, and a tracked, unstaged PENDING path is refused at :383 before the dry_run branch at :387 is reached. The comment at :352-353 says the CCX refusal stands in both runs 'because that artifact cannot ride this commit whatever gets staged'.",
        ".tools/safe-commit.sh:369-392 @b02fdaa849: safe-commit stages the declared pathspec (cg_stage_pathspec) before its gate stages, so at hook time a modified carrier is in the index and takes the co-commit branch at proof-of-spec-check.py:380-382.",
        "EXERCISED temp-index run: GIT_INDEX_FILE=.scratch/idx_v3, a copy of the worktree index plus the 5 commit paths: 'artifact-resolution: 0 resolved at pin / 3 PENDING co-committed', 'VALID (rc=0)'; the worktree's real index afterwards: 0 staged paths.",
        "SCOPE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:56-64 @b02fdaa849 (VIEW_OF) names existing tracked carriers for EN-v-1 through EN-v-6, so every EN-v order's artifacts are modified tracked files."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-v-3 <proof_of_spec>: 'validated with python .tools/proof-of-spec-check.py <instance> V3-AC1,V3-AC2,V3-AC3 BEFORE the complete flip'; the worker definition: 'ONLY the exit code is the verdict'.",
    "world_is": "Run as a plain pre-flip dry run, the named invocation refuses a modified tracked artifact as if it could not ride the commit, although safe-commit stages it before its gates. The comment's reason holds for an unmodified tracked file, not a modified one. To reach the pre-commit state without a pre-add, this worker ran the same invocation with GIT_INDEX_FILE pointed at a scratch copy of its index and flipped on that rc 0. The commit's own hook run stays the authority.",
    "notes": "ARMED: EN-v-1, -2, -4, -5 and -6 carry the same artifact shape, so a worker that follows its order's 'validate before the flip' under Rule 14a gets rc 1 on its dry run. The remedy (a face note for the sibling orders, or a route to the checker's owner) is for the disarm owner to choose."
  },
  {
    "id": "LGIC_ENFORCE-W4-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~4",
    "surfaced_at": "2026-09-15T00:18Z",
    "one_line": "check_en.py v1-tests reads FAIL-CONSUMER-TESTS whatever data/firm_registry.json says: the same 14 tests in test_seam_paired.py fail at the base bytes and at the generated view, because they read the portal fixture from the primary checkout (12 keys) and routes.json (12 routes) against an asserted 11.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, a discriminating pair in worktree wk-lgic-enforce-1-4 @2a6c7d8543 where only the carrier varies: the four consumer test files with data/firm_registry.json at its HEAD bytes gave '14 failed, 95 passed' rc 1; with the generated view gave '14 failed, 95 passed' rc 1; the FAILED sets compared equal (14 = 14, IDENTICAL SET: True), every one in infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py.",
        "EXERCISED, per file on the generated view: _keys/tests/test_keys.py 45 passed rc 0; _gate/tests/test_policy_completeness.py 3 passed rc 0; org/modules/graph/tests/test_comp_keys.py 8 passed rc 0; _contracts/tests/test_seam_paired.py 14 failed, 39 passed rc 1.",
        "FILE: infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py:47-62 @2a6c7d8543: portal/ is a gitlink a linked worktree does not populate, so portal_root() falls back to C:/Users/AndrewBerman/Desktop/ajb_workspace/portal and the run printed 'consumer fixtures read from the primary checkout'; :216 asserts len(smoke) == 11 and failed 'assert 12 == 11'.",
        "READ: the portal gitlink at HEAD 2a6c7d8543 is e85f6eb84f; the primary checkout's portal is at 0d07580841 on DEV (e85f6eb84f is its ancestor, merge-base --is-ancestor rc 0). src/pages/InvestorReporting/fixtures/smoke/default.json holds 11 keys at e85f6eb84f and 12 at 0d07580841.",
        "FILE: docs/contracts/investor-reporting/v1/routes.json @2a6c7d8543 holds 12 route entries (last touched d9c940244a, 2026-09-11 12:32 -04:00); test_seam_paired.py:428 asserts len(declared) == 11 and failed 'assert 12 == 11' after printing 'routes in routes.json: 12 = 12 DECLARED'. The test was last touched at 49035683d1 (2026-09-11 19:47 -04:00)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-v-1 V1-AC3: 'its consumers' existing tests pass: the three investor-reporting tests (_keys, _gate, _contracts) and org/modules/graph/tests/test_comp_keys.py', graded by check_en.py v1-tests expecting VERDICT: PASS-CONSUMER-TESTS.",
    "world_is": "The _contracts test fails 14 of 53 at the spawn base with the carrier unchanged, so V1-AC3 cannot read PASS from any view of data/firm_registry.json. Moving it takes an edit to test_seam_paired.py or a different portal state, and neither is in this order's <paths>. V1-AC1 and V1-AC2 pass by output. The order stays pending.",
    "notes": "The failure text of the 11 parametrized test_paired_consumer_request_through_the_real_dispatcher cases was not read; only their names and the shared FAILED set. Whether a worktree whose portal/ is populated at gitlink e85f6eb84f would pass the 13 fixture-reading tests was not exercised: populating portal/ is outside this cell. The same v1-tests invocation graded in the shared tree reads the same primary portal."
  },
  {
    "id": "LGIC_ENFORCE-S5",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "4.0.0_SA_CRO",
    "surfaced_at": "2026-09-15T02:05Z",
    "one_line": "The identity registry's demo row sets tenancy FIRM with the note 'a tenant class the doctrine does not define', while the doctrine defines demo as a DEMO-TENANT class, 'neither firm nor general' (02_DOCTRINE.md:60, ruled KEPT at :366-367; ledger X6), so the registry and the canon disagree on demo's tenancy.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "REGISTRY: infra/logic/registry/scopes.json row demo, read at HEAD (last written by LGIC_ENFORCE EN-r-1 @a925c8a642): class FIRM, tenancy FIRM, tenant.kind demo, note 'a tenant class the doctrine does not define (05_IDENTITY_SPINE.md s.3, tick-list row 17)'.",
        "DOCTRINE: infra/logic/02_DOCTRINE.md:60 '`opal-data-demo`: a tenancy class that is neither firm nor general -- serves prospective users with demo accounts (Andrew ~01:3xZ 09-13, KEPT)'; :366-367 'RULED card 8: KEPT as a DEMO-TENANT class (s.1 vocabulary)'.",
        "LEDGER: infra/logic/06_CONFORMANCE_LEDGER.md:135 X6 'opal-data-demo | tenancy | a demo tenant, neither firm nor general | a DEMO-TENANT class (doctrine v0.3 s.1) | ... | PERMANENT | GRANTED'.",
        "NAMING: org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md s.3 RULING DM reads demo as a firm in naming slots from this row's class, and states 'The row answers the naming question'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "02_DOCTRINE.md s.1 (v0.3): opal-data-demo is 'a tenancy class that is neither firm nor general', KEPT as a DEMO-TENANT class (card 8).",
    "world_is": "The registry row reads tenancy FIRM, and its note says the doctrine does not define the class, which the doctrine at :60 and :366-367 does. Naming is unaffected: LGIC_NAMING RULING DM reads demo as a firm from the row's class, and the naming brief lists demo among the firms. INERT at this seat: no consumer that branches on demo's tenancy was measured, and that census was not run.",
    "notes": "Surfaced by 4.0.0_SA_CRO during the LGIC_NAMING v1.7 L4-R, which it signed; this is not a ground there. For the registry's owner (LGIC_ENFORCE, EN-r-1) and the canon's author (LGIC_CANON): either the row's tenancy and note change, or the doctrine's s.1 class does. Which plane governs demo's tenancy was not decided here."
  },
  {
    "id": "LGIC_ENFORCE-W1-S12",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T01:55:44Z",
    "one_line": "terraform test cannot iterate run blocks, so infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl runs the 32 generated vectors as 32 indexed run blocks plus a coverage run that refuses any other count; a registry that grows the vectors fails terraform test until a run block is added by hand.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: TO-EN-m-1 WORKER FACE 'A terraform test file runs every vector through the module's name output' and 'You may extend lib/opal_naming.py's generator only to render the locals and vectors', so the test file is hand-held, not generated.",
        "TOOL: Terraform v1.9.8 (C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe version). A run block takes no for_each or count, and check_en.py m1_vectors counts passed run blocks against the vector count ('int(m.group(1)) >= len(rows)', check_en.py:523 @1ca17cc88e).",
        "RUN: check_en.py m1-vectors in wk-lgic-enforce-1-1-m1: 'VECTORS: 32  terraform test: 37 passed, 0 failed  (init rc=0, test rc=0)'. The 37 are coverage, vector_00..vector_31 and four negative or map arms.",
        "CODE: lib/opal_naming.py build_vectors crosses 4 _VECTOR_SHAPES with None plus every FIRM, GLOBAL and MASTER scope row, 4 x 8 = 32 at infra/logic/registry@50e4fabd1cb6a150. One new such scope row adds 4 vectors."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-m-1 WORKER FACE: tests/vectors.json is generated by the Python builder, never typed, and a terraform test file runs every vector through the module's name output.",
    "world_is": "Every expected value comes from tests/vectors.json at test time, and the test file holds none. What the file does hold is a fixed index count (0..31): terraform test offers no way to run a vector list of unknown length as one run per vector. The coverage run makes a grown vector set fail loudly instead of running short.",
    "notes": "Form only. The fix, if one is wanted, is for the generator to render the test file as well. That is outside this order's grant to the generator (locals and vectors only)."
  },
  {
    "id": "LGIC_ENFORCE-W4-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~4",
    "surfaced_at": "2026-09-15T00:59Z",
    "one_line": "The first generation of firm-config.mjs re-orders FIRM_CONFIG's keys (base 49financial, inflection, mockadv, demo, cottonwood; generated 49financial, inflection, cottonwood, mockadv, demo), so Object.keys of FIRM_CONFIG and of FIRM_BUCKET_MAP change order, and check_en.py v2-delta0 cannot see order: an order-only mutant reads EQUAL.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "BASE, run: node .scratch/ctl/keys.mjs over git show b02fdaa849:infra/aws/lambda-edge/_shared/firm-config.mjs -> [\"49financial\",\"inflection\",\"mockadv\",\"demo\",\"cottonwood\"] for both FIRM_CONFIG and FIRM_BUCKET_MAP; both frozen.",
        "LIVE, run: the same over the generated file (python lib/opal_naming.py generate --out . --target infra/aws/lambda-edge/_shared/firm-config.mjs, registry@50e4fabd1cb6a150) -> [\"49financial\",\"inflection\",\"cottonwood\",\"mockadv\",\"demo\"] for both; both frozen. The GENERATED block is firm-config.mjs:65-88 in the worktree wk-lgic-enforce-1-4-v2.",
        "INSTRUMENT, read: check_en.py:187-204 @b02fdaa849 (exports_of) loads the .mjs through node and returns json.loads(JSON.stringify(m.FIRM_CONFIG)); :375-384 (_compare_carriers) compares the two with a == b on Python dicts, which ignores key order. EXERCISED: _compare_carriers over an order-only mutant ('demo' moved first, node reads [\"demo\",\"49financial\",...]) against the base -> 'EQUAL: 1 DIFFER: []'; over a bucket mutant ('opal-data-cot' -> 'opal-data-cottonwood') -> 'EQUAL: 0 DIFFER: [infra/aws/lambda-edge/_shared/firm-config.mjs]'.",
        "CONSUMERS, read: Grep 'FIRM_CONFIG|FIRM_BUCKET_MAP' over infra/aws/lambda-edge (node_modules excluded): 3 importing functions, and every use indexes by key: auth-validator-edge/index.mjs:153, shared-advisor-router/index.mjs:242-243 and :380, shared-advisor-router-response/index.mjs:106 and :122. The one iteration is the file's own FIRM_BUCKET_MAP derivation (firm-config.mjs:106-110 @b02fdaa849), which inherits the order."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-v-2 THE CELL: 'The first generation is BYTE-EQUIVALENT in what it exports (DELTA=0). ... Change nothing but the carrier'; V2-AC2: 'the file's exported content equals its pre-image at the spawn base (DELTA=0)'.",
    "world_is": "Every key and every value is equal (V2-AC2 PASS-DELTA0) and both exports stay frozen, but the insertion order, which JavaScript exposes through Object.keys, Object.entries and JSON.stringify, is now the registry's order and not the carrier's. The generated block also drops the in-map history comments (the 'demo' ADVI_DEMOV1.001 note, the 'cottonwood' FIRMSEP.10 note and the FUTURE note). V2-AC2 compares parsed dicts, so it cannot tell an order change from no change.",
    "notes": "0.9.0_WK_LGIC_ENFORCE~1 disclosed the reorder and the comment loss as a declared exclusion in TO-EN-r-1's proof ('The exports are equal (R1-AC6); how EN-v-2 and EN-v-6 carry the comments is theirs'). This row adds two facts: the order is an exported property, and the DELTA=0 instrument does not look at it. Whether insertion order is part of 'what it exports' is for 2.0.0_SA_COO~G and 1.0.0_SA_CTO to decide. The carrier was written exactly as the generator emits it, with nothing re-ordered or restored by hand. INERT: no consumer iterates either export (census above) and nothing is deployed in this cell. A deploy or a future iterating consumer would see the registry's order."
  },
  {
    "id": "LGIC_ENFORCE-W5-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~5",
    "surfaced_at": "2026-09-15T01:05Z",
    "one_line": "check_en.py's v4-delta0 probes loaders.py bucket_for in a process where IRPT_DIRECTORY_BUCKET_MAP is unset, so all 11 probes raise BucketUnmapped in both copies: a change to bucket_for's return path reads EQUAL and prints PASS-DELTA0.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: fixed_inputs/check_en.py:211-221 @b02fdaa849 (exports_of) calls bucket_for(t) for 11 probe tokens in-process and records repr(result) or 'raises <class>'. Of its 1175 lines, only :105 (run(): e = dict(os.environ), a subprocess env) and :519 (SAFE_APPLY_TERRAFORM) touch os.environ, and no line reads or sets IRPT_DIRECTORY_BUCKET_MAP.",
        "SUBJECT: infra/aws/lambda/investor-reporting/_authz/loaders.py:29,43-53 @b02fdaa849: bucket_for reads the firm map from env IRPT_DIRECTORY_BUCKET_MAP (default '{}') and raises BucketUnmapped for a token not in it, so with the variable unset every probe takes the refusal branch.",
        "DISCRIMINATING PAIR, check_en.py's own exports_of loaded by path, live generated loaders.py against scratch copies: ENV UNSET (the checker's state): live exports 1 distinct value ['raises BucketUnmapped']; unmutated EQUAL, raise-class mutant (BucketUnmapped -> KeyError) DIFFER, return-path mutant (return mapping[tenant] + '-x') EQUAL. ENV SET to a map over 10 of the 11 probes: live exports 11 distinct values; unmutated EQUAL, raise-class mutant DIFFER, return-path mutant DIFFER.",
        "SAME HELPER, SECOND SUBCOMMAND: r1_generate (check_en.py:387-395 @b02fdaa849) compares the carriers through the same _compare_carriers -> exports_of, so its DELTA=0 on loaders.py has the same unset-env read."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "EN-v-4's V4-AC2: 'the file's exported content equals its pre-image at the spawn base (DELTA=0)'. The cell: 'The first generation is BYTE-EQUIVALENT in what it exports (DELTA=0). That is the served plane unmoved, and it needs no never-widen hold.'",
    "world_is": "Under the checker's environment, V4-AC2 grades only bucket_for's refusal branch (the exception class). A view whose mapped-firm branch returned a different bucket would still print PASS-DELTA0. THIS generation is unaffected: its bucket_for body is byte-identical to the base (the diff adds 4 comment lines only), and the unmutated copy reads EQUAL under both arms.",
    "notes": "Filed by the worker on EN-v-4; the fixed inputs are read-only to it, and nothing was changed. ARMED because the next regeneration of this carrier, or any later edit to the generator's _BUCKET_FOR template, would be graded by the same subcommand and certify DELTA=0 on the refusal branch alone. Disarm owner: the fixed input's issuer. One remedy is for exports_of to probe under both an unset and a populated IRPT_DIRECTORY_BUCKET_MAP; how to disarm is the owner's call."
  },
  {
    "id": "LGIC_ENFORCE-W5-S5",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~5",
    "surfaced_at": "2026-09-15T01:19:39Z",
    "one_line": "proof-of-spec-check.py's pre-flip dry run refuses a PENDING-THIS-COMMIT artifact that is a TRACKED file modified in place and not staged as 'ALREADY COMMITTED at HEAD' (CCX class), so an EN-v carrier regenerated at its existing path reads INVALID rc 1 until it is staged, while Rule 14a says not to pre-git add.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: .tools/proof-of-spec-check.py:379-388 @b02fdaa849 (checker-vintage da3e61889d). In PRE-COMMIT: a staged artifact is co-committed; otherwise a path `ls-files --error-unmatch` finds tracked is the CCX violation; only after that does `elif dry_run` grant PENDING. Its comment at :348-354 describes the dry-run case for UNTRACKED artifacts only.",
        "SUBJECT: infra/aws/lambda/investor-reporting/_authz/loaders.py is tracked at b02fdaa849, and its worktree bytes differ from HEAD by +4 comment lines, so the change is not already committed.",
        "DISCRIMINATING PAIR, same instance bytes, same worktree. Nothing staged: 'VIOLATION: artifact-resolution: 'infra/aws/lambda/investor-reporting/_authz/loaders.py' is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged', INVALID (rc=1). Under GIT_INDEX_FILE pointed at a copy of the worktree index, with the 4 changed declared paths staged in the copy: '2 PENDING co-committed (PRE-COMMIT: staged in this commit)', VALID (rc=0). Real index: 0 paths staged before and after.",
        "RULE: CLAUDE.md Rule 14a 'do NOT pre-`git add`'; .tools/safe-commit.sh:42 'DO NOT pre-`git add` -- this wrapper stages your declared pathspec itself.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The worker definition: validate with `python .tools/proof-of-spec-check.py <instance> <ids>`, then flip on rc 0. The checker's own comment at :348-350: 'a worker's natural dry run is an UNTRACKED instance with UNTRACKED artifacts and nothing staged'.",
    "world_is": "If the artifact already exists at HEAD and is modified in place, as every EN-v carrier is, the natural dry run reads INVALID rc 1 on the CCX limb. rc 0 is reachable only with the artifact staged. This worker staged it in a temporary index copy, never in the real index.",
    "notes": "The act the order did not name: the temporary-index dry run, used to get the pre-flip rc 0 without pre-adding to the real index. INERT: the refusal fails closed (a false INVALID, never a false VALID), and inside safe-commit's hook the pathspec is staged, so the commit-time run grades the co-commit (the checker's comment at :350; this worker's commit is the exercise). Sibling EN-v workers regenerating a carrier in place will meet the same rc 1."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T02:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S6",
    "one_line": "Issuer's disposition of LGIC_ENFORCE-W4-S1: V1-AC3's FAIL is the consumer suite's state at the base, not the view's. TO-EN-v-1 stays pending, its VALID proof counts it terminal at the L10 precondition (96806), and the red suite is already routed to IRPT_BCKEND as IRPT_BCKEND-S51.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W4-S1 (BLOCKING, ARMED, disarm_owner 2.0.0_SA_COO~G) came with EN-v-1's drain @78ba3385aa.",
        "EXERCISED in the drain, in the worker's worktree: check_en.py v1-tests printed VERDICT: FAIL-CONSUMER-TESTS; v1-header and v1-delta0 printed PASS; proof-of-spec-check read VALID (rc 0).",
        "EXERCISED, two trees: pytest over infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py read '14 failed, 39 passed' in the primary checkout at b9fa612c43 (data/firm_registry.json at its pre-view bytes) and '14 failed, 39 passed' in the worker's worktree (the generated view). The FAILED name sets compare identical, 14 = 14.",
        "LIMIT: both runs read the same portal checkout (0d07580841), because a linked worktree falls back to the primary one (test_seam_paired.py:47-62 @2a6c7d8543). The pair is independent on the carrier, not on the portal.",
        "ROW: IRPT_BCKEND-S51 (ARMED, 2026-09-13, routed by 1.0.0_SA_CTO) already records this suite at 14 failed, 39 passed: the consumer's smoke map moved to v1 paths and the route table grew from 11 to 12, while the producer's paired test did not.",
        "GATE: 1.0.0_SA_CTO's 96806 (@fa6521ea12) reads an order as terminal for the L10 precondition when its proof instance reads VALID bound to it."
      ]
    },
    "spec_asserts": "TO-EN-v-1 V1-AC3: 'its consumers' existing tests pass: the three investor-reporting tests (_keys, _gate, _contracts) and org/modules/graph/tests/test_comp_keys.py', graded by check_en.py v1-tests.",
    "world_is": "No view of data/firm_registry.json can make V1-AC3 PASS while IRPT_BCKEND-S51 stands: one of the four consumer files is red at the base for reasons outside this cell.",
    "notes": "DISPOSITION by the disarm owner, not a flip. The order's word stays pending: the worker was right not to flip, and RULING T is standing for LGIC_NAMING only (96793). The frozen criterion is not edited. Nothing in this round waits on the word: EN-d-1 depends on EN-v-1..6 MERGED, which EN-v-1 is. For 1.0.0_SA_CTO at L10: whether a consumer-test criterion should grade against the base's own failures rather than an absolute pass. INERT: the hazard was a round that could not close on this order, and 96806 removes it."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T02:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S7",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W5-S3: proof-of-spec-check's pre-flip run refuses a tracked carrier changed but not staged. Every EN-v worker routed around it and every proof read VALID at the issuer's drain; the three level-3 workers were spawned with the checker's own remedy in their identity lines.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W5-S3 (ARMED, disarm_owner 2.0.0_SA_COO~G). The same refusal is filed as LGIC_ENFORCE-W6-S1 (EN-v-5) and LGIC_ENFORCE-W5-S5 (EN-v-4), and was reported by the EN-b-1, EN-v-2 and EN-v-6 workers.",
        "ROUTES TAKEN: the carrier committed first with the proof pinned to it (EN-b-1, EN-v-2, EN-v-5, EN-v-6), or the check run against a scratch copy of the index (EN-v-3, EN-v-4). No worker pre-staged.",
        "EXERCISED at the drains: proof-of-spec-check read VALID (rc 0) in the worktrees of EN-b-1, EN-v-1, EN-v-3, EN-v-5 and EN-v-6, and of EN-v-2 and EN-v-4 after their renumber.",
        "SPAWNS: EN-m-1 (0.9.0_WK_LGIC_ENFORCE~1), EN-g-1 (~2) and EN-s-1 (~7) were spawned with the two-commit remedy in their identity lines. Their faces are unchanged."
      ]
    },
    "spec_asserts": "Each order's proof_of_spec block: 'validated with python .tools/proof-of-spec-check.py <instance> <ids> BEFORE the complete flip'. CLAUDE.md Rule 14a: do not pre-git add.",
    "world_is": "The checker's pre-flip run grades a PENDING-THIS-COMMIT artifact against HEAD, so an in-place edit of a tracked carrier reads as already committed until it is staged, and the rules forbid staging first.",
    "notes": "DISARM by its owner for this round: every order still to run is spawned with the remedy. The structural fix, in .tools/proof-of-spec-check.py, is outside this round's grants and goes to the round's drain-end read for 1.0.0_SA_CTO. INERT."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T02:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S8",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W5-S4: check_en.py v4-delta0 grades bucket_for with IRPT_DIRECTORY_BUCKET_MAP unset, so it sees only the refusal branch. EN-v-4's view reads EQUAL on both branches by the worker's own mutant pair, and no other order in this round calls v4-delta0.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W5-S4 (filed as W5-S1 on EN-v-4's branch and renumbered before its drain; ARMED, disarm_owner 2.0.0_SA_COO~G).",
        "READ: of the 22 LGIC_ENFORCE task orders, only TO-EN-v-4's V4-AC2 invokes v4-delta0.",
        "WORKER'S PAIR (TO-EN-v-4's proof instance): with the variable unset, a changed return value still reads EQUAL; with a map set, it reads DIFFER; the committed view reads EQUAL both ways.",
        "EXERCISED at the drain: V4-AC1..3 printed PASS in the worker's worktree, and proof-of-spec-check read VALID."
      ]
    },
    "spec_asserts": "TO-EN-v-4 V4-AC2: the file's exported content equals its pre-image at the spawn base (DELTA=0).",
    "world_is": "The instrument compares one of bucket_for's two branches. A regeneration that changed only the mapped branch would read PASS-DELTA0.",
    "notes": "DISARM by its owner: INERT for this round, since its one consumer has run and the view is equal on both branches. The fixture fix, probing with a map set as well as unset, is the issuer's own and goes to the round's drain-end read. No mid-round patch: nothing left to grade would read it."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T02:38Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S9",
    "one_line": "Two slots minted duplicate row ids from separate branches: slot ~4's EN-v-1 and EN-v-2 both minted W4-S1, and slot ~5's EN-v-3 and EN-v-4 both minted W5-S1 and W5-S2. The issuer renumbered the later branch's rows before its drain (W4-S2; W5-S4, W5-S5) under an audited override, and names each later spawn's first row id.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SURFACED_AT: W4-S1 at 00:18Z (EN-v-1) and 00:59Z (EN-v-2); W5-S1 and W5-S2 at 00:40Z (EN-v-3) and at 01:05Z and 01:19Z (EN-v-4). The earlier row keeps its id.",
        "RENUMBER COMMITS on the worker branches: b484d8dec4 (EN-v-2) and 8298325909 (EN-v-4). Each changes the row ids and their references in that branch's proof instance and result file. EN-v-4's also pins its loaders.py artifact row from PENDING-THIS-COMMIT to 56b867ac4c, the commit that carried it, because any later commit to the instance voids that sentinel (the checker's CCX remedy). Nothing else moves.",
        "OVERRIDES, both audited: surprise-row-gate refused each commit -- a renamed row reads as deleted, and a W-coordinate row committed by a seat reads as mis-allocated -- so each carries '# surprise-row-override:'. The worker files sit in lane TREE_DELIVERABLES, which admits only the serial in the path, so each carries GIT_COMMIT_AUTHOR_OVERRIDE=TREE_DELIVERABLES. A channel-only renumber was tried first and left each proof INVALID (its surprises entries resolved to no row). safe-commit wrote the audit lines into each worktree's own untracked audit log; the issuer copied them verbatim into the primary checkout's org/git-author-override-audit.log.",
        "EXERCISED: proof-of-spec-check read VALID (rc 0) on both renumbered worktrees, with exactly each commit's paths staged in a scratch copy of the index, before their drains.",
        "IDS on the channel with this row: 37 rows, 37 unique."
      ]
    },
    "spec_asserts": "Each face's BOUNDS: 'id LGIC_ENFORCE-W<n>-S<k> (<n> your slot)'.",
    "world_is": "A slot's queued orders cold-start on separate branches cut at spawn, and each worker reads <k> from the channel at its own base. Two orders of one slot spawned before the first drains mint the same ids, and the issuer's union resolver keys rows by id, so one row would be lost at the drain.",
    "notes": "For this round: the level-3 identity lines name each worker's first row id (W1-S12, W2-S5, W7-S1), and later spawns will too. Structural remedies -- ids keyed by order rather than by slot, or the row gate refusing an id already minted on another open branch -- go to 1.0.0_SA_CTO at the drain-end read. INERT: both collisions are renumbered and no id is duplicated."
  },
  {
    "id": "LGIC_ENFORCE-W2-S5",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-15T02:10Z",
    "one_line": "EN-g-1's context rule names 'firm and product tokens as whole segments', but both PRODUCT scopes (mdpf, etfs) are also systems.json keys that name() writes in the system slot, so a whole-segment product match would refuse the builder's own output written as a literal. The limb matches a product token only as the whole string, and exempts float() arguments because lookup('inf') is the inflection row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN (registry read in wk-lgic-enforce-1-2-g1 @1ca17cc88e): 'PRODUCT scopes: ['mdpf', 'etfs'] | also systems.json keys: ['etfs', 'mdpf']'.",
        "RUN: lib/opal_naming.py name('mdpf', None, 'publisher', 'role') = 'mdpf-publisher-role' and name('etfs', None, 'netassets', 'daily') = 'etfs-netassets-daily': the product token is the whole first segment of a canonical shared name.",
        "RUN: lib/opal_naming.py lookup('inf')['long'] = 'inflection', so the numeric spelling in float('inf') is a firm spelling to a whole-segment matcher.",
        "CODE: .tools/naming-gate.py @02d2869cf0 -- :513-527 build the token sets (FIRM spellings into firm_whole, and into firm_seg when alphanumeric; PRODUCT spellings into product_whole only); :576-585 carrier() matches product_whole on the whole string and firm_seg per segment; :70 EXEMPT_CALLS = {'float'}, applied at :266."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE.TO-EN-g-1 worker face, THE CELL item 1: 'The inputs are S3 key and bucket literals, resource-name literals, secret paths, and firm and product tokens as whole segments. The context rule: a token is PERMITTED in the registry files, in a generated file, as an argument to key(), address(), name() or lookup() ... Anywhere else it is a HAND-KEPT CARRIER: a NEW one is refused'.",
    "world_is": "The registry holds mdpf and etfs both as PRODUCT scopes and as systems.json keys, and name() puts the system first. Matching product tokens as whole segments would refuse every new hand-written mdpf-* or etfs-* name, including the literal spelling of name()'s own conformant output. As built, a product token is a carrier only when it is the whole string (bare 'mdpf', or a lookup-able alias such as 'mdpf_revamp'). Firm tokens are matched as whole segments, as written. Strings passed to float() are not graded.",
    "notes": "Form only: the cell's words, read against the registry, take two readings, and this row records the one built. No criterion turns on it: the g1 fixtures carry firm tokens only. The reading is L9's to accept or re-cut; the carrier sets are data in Naming.__init__, so a re-cut is a one-line change."
  },
  {
    "id": "LGIC_ENFORCE-W2-S6",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-15T02:10Z",
    "one_line": "EN-g-1's output grammar says <verdict> is the grade or REFUSE, but a bare hand-kept firm token has no node type and so no grade. The limb prints OUT-OF-PATTERN for an EXISTING one (a WARN, canonical lookup(<long>)), and RAISE for a RaiseDefect; a why: line under each says which.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: lib/opal_naming.py:1239-1240 @1ca17cc88e -- grade(name, type) raises RaiseDefect 'G1.1: ... is not a node type of NAMING_SCHEMA.json' for a type outside the schema, so a string with no node type cannot be graded.",
        "CODE: .tools/naming-gate.py @02d2869cf0 -- :694 an EXISTING carrier with no type returns line verdict OUT-OF-PATTERN, counted as WARN; :697 a RaiseDefect returns line verdict RAISE, counted as WARN, never REFUSE.",
        "RUN (safe-commit of 02d2869cf0, WARN mode, the stage grading its own file): '[naming-gate] NAMING RAISE .tools/naming-gate.py:547 /aws/ -> (rule or registry defect)' with 'why: RAISE as LOG_GROUP: rule or registry defect, not a refusal: L2: service '' gives no resource type', then 'NAMING-GATE: WARN 9 graded', safe-commit rc=0.",
        "CODE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:781 @1ca17cc88e reads 'NAMING (OUT-OF-PATTERN|REFUSE)', so no criterion turns on the choice."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE.TO-EN-g-1 worker face, interfaces: 'Output: one NAMING <verdict> <file>:<line> <string> -> <canonical> line per graded string (<verdict> is the grade, or REFUSE)'; THE CELL item 1: 'RAISE: printed as a rule or registry defect.'",
    "world_is": "Two line verdicts fall outside 'the grade, or REFUSE'. RAISE is grade()'s own outcome (it raises instead of returning a verdict). OUT-OF-PATTERN on a bare carrier is the limb's word, since grade() has nothing to return. Both count as WARN in the NAMING-GATE summary and never as REFUSE.",
    "notes": "Form only. A consumer of org/mcp/naming-gate-verdicts.log that parses the verdict word sees five words: CONFORMANT, ALIAS, OUT-OF-PATTERN, NOT-GRADED, RAISE, plus REFUSE. The why: line is printed but not logged."
  },
  {
    "id": "LGIC_ENFORCE-W7-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~7",
    "surfaced_at": "2026-09-15T02:20Z",
    "one_line": "EN-s-1's census cannot judge every nameable live name on this registry: 504 of 1805 live names and 623 of 1869 repo names RAISE in grade(), so the run stops at the 4th live name (sentiment-query-api, R1.f) and S1-AC1 and S1-AC2 FAIL.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: python lib/opal_naming.py census --live --repo --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md in wk-lgic-enforce-1-7-s1: 'CENSUS RAISE live API_GW sentiment-query-api -- R1.f: 'sentiment' is in no vocabulary; no registry row resolves it', then 'CENSUS: STOPPED on the first RAISE after 3 judged', rc=3. Live pull: VINTAGE 'Built from the estate as of 2026-09-15 00:57:50 UTC ... manifest: e8a06d444ae8', 2148 nodes, 33 of 33 node types, WITHIN BUDGET.",
        "MEASURED by a diagnostic, NOT the census: a scratch script outside the worktree grades every census item and continues past a RAISE, only to size the population. Live: 1805 nameable, 1301 graded (OUT-OF-PATTERN 1055, CONFORMANT 217, ALIAS 29), 504 RAISE by step (R1.c 221, R1.f 206, R2 53, B2 15, R8 5, R1.d 2, L2 2); 115 distinct raising tokens, the most frequent globgrph 67, news 46, find 34, trade 24, estate 24, astn 19, semantic 15, agentbus 12, security 11. Repo: 1869 names, 1246 graded, 623 RAISE (R1.f 194, R1.c 180, K1 166, R2 46, B2 32, R1.d 2, L2 2, G2.3 1).",
        "CODE: lib/opal_naming.py grade() @32855486f0 (EN-b-1) raises R1.c on a V2 (unresolved) first token and R1.f on a token in no vocabulary. Its V1 is systems.json's keys, and row LGIC_ENFORCE-W1-S11 records astn, trade and news held unresolved. org/standards/NAMING_SCHEMA.json grade.unplaceable @32855486f0: a token no registry row resolves 'is a defect in the tokeniser, this file or the registry and is fixed there'.",
        "CRITERIA: check_en.py s1-planes gives 'PLANES: ['live']' and 'VERDICT: FAIL-PLANES', rc 1. check_en.py s1-all-judged gives 'LIVE NAMEABLE: 1805  JUDGED: 3  LIVE ROWS: 3' and 'VERDICT: FAIL-NOT-ALL-JUDGED', rc 1."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-s-1 WORKER FACE: the census 'judges every nameable name in the repo ... and in the live plane', and 'A RAISE stops the run loudly, printing the string, and is never filed as out-of-pattern'. S1-AC2: 'every nameable live name is judged'.",
    "world_is": "At registry@50e4fabd1cb6a150 both cannot hold. 28 percent of the live nameable names raise, the first at the 4th name in census order, so the run stops before it reaches the repo plane. The remedy is registry rows (infra/logic/registry/systems.json) or rule steps, and neither is in this order's <paths>. The census was not altered to skip a RAISE or file it under a verdict.",
    "notes": "Form only. The census, its stop and S1-AC4 behave as specified; the blocked criteria are S1-AC1 and S1-AC2. The diagnostic's raise list is at C:/Users/AndrewBerman/AppData/Local/Temp/lgic_enforce_w7/raises2.json on this device. It is not a deliverable."
  },
  {
    "id": "LGIC_ENFORCE-W7-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~7",
    "surfaced_at": "2026-09-15T02:20Z",
    "one_line": "live_nameable also excludes 16 AWS-fixed live names (IAM_POLICY 10, LOG_GROUP 4, SECURITY_GROUP 2), departing from the order's formula 'live minus the NOT-GRADED types' (1805, not 1821), because grade() RAISES on names NAMING_SCHEMA.json aws_fixed puts outside the domain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json aws_fixed @32855486f0: 'names AWS fixes are OUTSIDE the grade's domain, like the NOT GRADED types: excluded, never a fourth verdict'. by_arn: an IAM_POLICY in account aws. by_name: SECURITY_GROUP default; LOG_GROUP RDSOSMetrics and the prefixes aws-waf-logs- and /aws/ecs/containerinsights/.",
        "CODE: lib/opal_naming.py grade() @32855486f0 raises G2.1 on SECURITY_GROUP 'default', G2.2 on an IAM name starting AWS or Amazon, and G2.3 on a log group not starting with / (GRADING_RULE.md G2, which predates AW1; row LGIC_ENFORCE-W3-S4 records the same departure).",
        "RUN: census --live: '2148 node(s) ...; 327 of NOT GRADED types, 16 aws_fixed; 1805 to judge'. The report's denominators carry live_not_graded_types 327 and live_aws_fixed 16 beside live_nameable 1805."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-s-1 report shape: 'live_nameable: <n, live minus the NOT-GRADED types>'.",
    "world_is": "Taken literally, the formula puts 16 names into the judged population that grade() RAISES on, so the census would stop on an AWS-managed name the schema puts outside the domain. The census applies the schema's aws_fixed exclusion (_aws_fixed) and prints both subtractions.",
    "notes": "Form only. No criterion turns on the 16. S1-AC2 compares judged_live with live_nameable and the live row count, and fails on the RAISE stop (row LGIC_ENFORCE-W7-S1) under either formula."
  },
  {
    "id": "LGIC_ENFORCE-W7-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~7",
    "surfaced_at": "2026-09-15T02:20Z",
    "one_line": "The order names the repo surfaces (Terraform, config.py-class files, Lambda sources) but not how a source literal is placed as a name or what 'Lambda sources' excludes. The census applies its own stated rule, so the repo denominator of 1869 is that rule's.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ORDER: the TO-EN-s-1 WORKER FACE names the surfaces only, as does PRD DEC-7 (org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:292-293 @32855486f0). The gate's inputs (:257-265) name the literal classes: S3 key and bucket literals, resource-name literals 'the schema's resource grammar places as a name', and secret paths. They give no placement procedure.",
        "RULE APPLIED (lib/opal_naming.py _census_classify, in this order's commit): an s3:// URL is a bucket and a key; under a *bucket* binding, a bucket; under a secret, secret_name, _id, _arn or _path binding, a secret path; under a *key* or *prefix* binding and carrying a /, a key; otherwise, a kebab literal whose last token is a kind exactly one node type owns. Terraform: the name attribute of 28 resource types (CENSUS_TF_ATTR) when it is one literal; 113 interpolated names are not judged.",
        "POPULATION: git ls-files: 468 .tf files. 3329 candidate source files (infra/aws/lambda/** .py .mjs .js .cjs .ts, plus every config.py), minus 2864 vendored or test files, leaves 465. Together they give 1869 repo names. The first version of the rule (deep binding, any *secret* binding, no test-file rule) placed 2072, including 'us-east-1' and 'utf-8' as SECRET. It was tightened before the report was written."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-s-1 WORKER FACE: 'It judges every nameable name in the repo (the Terraform, lib/config.py-class files, and Lambda sources)'.",
    "world_is": "Nothing the order names defines which literal in a config or Lambda source is a nameable name, so the worker defined it and printed the rule and its exclusions in the report and the module.",
    "notes": "Form only. No criterion turns on the repo denominator. The repo plane is never judged in this run, because the run stops in the live plane first (row LGIC_ENFORCE-W7-S1)."
  },
  {
    "id": "LGIC_ENFORCE-W7-S4",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~7",
    "surfaced_at": "2026-09-15T03:19Z",
    "one_line": "EN-s-2 sets the census totals beside N2, N6 and IV7, but the census it reads judged 3 of 1805 live names and 0 of 1869 repo names, all API_GW. So the names graded by both are 1 (N2) and 2 (N6), and IV7 grades no name. The comparison holds for those 3 names and says nothing about the estate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CENSUS: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md@f64b6f35cb json fence: denominators judged_live 3, live_nameable 1805, judged_repo 0, repo 1869; 3 rows, all API_GW live (inf-otp-relay-api OUT-OF-PATTERN, opal-portal-data-proxy-api CONFORMANT, opal-session-analytics-api CONFORMANT); stopped on API_GW sentiment-query-api (row LGIC_ENFORCE-W7-S1).",
        "RECOUNT (a scratch script in the worktree's .scratch, not a deliverable, matching on (name, type)): 'N2 WORKED CASES: 43', 'N2: graded by both 1  agree 1'; 'N6 GRADER-A ROWS: 88', 'N6: graded by both 2  agree 2'; 'STOP NAME ('sentiment-query-api', 'API_GW') in N2: False  in N6: False'; 'IV7 RANKED ROWS: 10', and IV7 mentions none of the 3 census rows or the stop name.",
        "HAND PRODUCTS: GRADING_RULE.md@51b0952d71 section 9 (43 worked cases); n6-grader-a.tsv@388b07f486 (88 rows); TENSION_RANKING.md@3497a41c31 (10 ranked surfaces, no per-name verdict, figures from infra/logic/09_NAMING_CENSUS.md over 2,531 live nodes on 2026-09-13)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-s-2 WORKER FACE: 'Set NAMING_CENSUS_REPORT.md's totals beside three hand products, each with its own denominator' and 'For every name graded both by the census and by hand, compare the verdicts'. The cell cites DEC-7: 'its comparison half waits for them, and they now exist'.",
    "world_is": "The hand products exist. The census totals they are set beside come from a stopped run: 3 rows of one type, the first three API_GW names in census order, not a sample. The names graded by both are 1 of N2's 43 and 2 of N6's 88. IV7 ranks 10 surfaces measured on a different census and names none of the 3. The comparison was written on these denominators as they are. No name the census did not judge was graded to fill one.",
    "notes": "Form only. S2-AC1 checks that each denominator is present and non-zero, and S2-AC2 checks the shape of the disagreement rows, so both can pass on denominators this small. IV7's json denominator is its 10 ranked surfaces, labelled as such, with names_graded_by_both 0 beside it. A census re-run after row W7-S1's registry rows would change the rows NAMING_CENSUS_COMPARISON.md reads."
  },
  {
    "id": "LGIC_ENFORCE-W8-S1",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~8",
    "surfaced_at": "2026-09-15T03:45Z",
    "one_line": "D1-AC3 and D1-AC6 can both pass only if the new pipeline is committed BEFORE the expected-set commit, but the cell lists writing it last (step 5). On scratch branch prac-lgic-enforce-d1 it was committed first, @b4afbb00c7.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:1053-1058 @652d3a2204 (d1-pipeline) passes only if 'git cat-file -e <generated>:<pipeline_path>' succeeds, so the pipeline must exist AT the generated commit.",
        "CODE: the same file :1033-1040 @652d3a2204 (d1-diff-equal) compares 'git diff --name-only <expected_set> <generated>', less infra/logic/registry, to expected_files for exact equality, so any commit between the two that adds the pipeline puts it in the actual set.",
        "SCRATCH BRANCH prac-lgic-enforce-d1 (never pushed): b4afbb00c7 the pipeline, then 5e6573d25f expected_diff.txt (expected_set), then 92bc3b51bf the row and the generator's output (generated). 'git diff --name-only 5e6573d25f 92bc3b51bf' prints 10 paths: the 9 expected plus infra/logic/registry/scopes.json."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-d-1 THE CELL: step 1 'Compute the expected diff set FIRST ... That commit is expected_set'; step 2 'Add ONE scopes.json row ... That commit is generated. The actual diff, less the registry itself, must equal the expected set exactly'; step 5 'Write a NEW pipeline for the firm ... and commit it on the scratch branch.'",
    "world_is": "A pipeline committed after 'generated' is absent at 'generated', which fails D1-AC6. One committed between the two commits enters the diff, which fails D1-AC3. Only a commit that is an ancestor of expected_set satisfies both, so the pipeline was committed first. The expected set was still computed and committed before the row was added.",
    "notes": "Form only. The pipeline's path is under this worker's deliverables folder (deliverables/0.9.0_WK_LGIC_ENFORCE~8/pipeline/qwt_positions.py) because the order's <paths> admits no data/ path. The order names no location for it."
  },
  {
    "id": "LGIC_ENFORCE-W8-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~8",
    "surfaced_at": "2026-09-15T03:45Z",
    "one_line": "Firm N+1 as one scopes.json row is not all the registry asks for: validate prints 'WARN scopes.json[3].key: firm 'quillwater' is not in NAMING_SCHEMA.json firm_forms', and scopes.json itself says firm_forms owns which firm short forms exist. Generate and the gate proceed on the row alone.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: 'python lib/opal_naming.py validate' in the practice copy after the row was added: 'WARN scopes.json[3].key: firm 'quillwater' is not in NAMING_SCHEMA.json firm_forms' ... 'VALIDATE: OK 16 system row(s), 10 scope row(s), 10 warning(s) at registry@8f946960611a1880', rc 0. Then 'GENERATE: 9 written, 0 skipped, into . at registry@8f946960611a1880'.",
        "CODE: lib/opal_naming.py:286-290 @652d3a2204. A FIRM row whose key is absent from firm_forms is appended to warnings, never refused. generate() (:1391-1393) stops only on refusals.",
        "SCHEMA: org/standards/NAMING_SCHEMA.json:112-117 @652d3a2204. firm_forms lists 49financial, inflection, cottonwood and demo. Its authority line :17 reads 'WHICH firm short forms exist (49f, inf, cot beside the long forms; bd refused in every slot) -- Andrew-direct 2026-09-13 ~03:5xZ card 2'.",
        "REGISTRY: infra/logic/registry/scopes.json:4 @652d3a2204, row_fields: 'short (NAMING_SCHEMA.json firm_forms owns which firm short forms exist)'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-d-1 THE CELL: 'EN-d-1 -- firm N+1 is one row (PRD candidate E11, its first half; DEC-9).'",
    "world_is": "The row alone regenerates all 9 views, and it makes the gate refuse the firm's hand-typed address and its name. The validator still warns that the firm's short form is not in NAMING_SCHEMA.json firm_forms, the list the registry names as the owner of which short forms exist. That file is outside this order's <paths>. The exercise added the row only and left the schema unchanged.",
    "notes": "Form only. No criterion turns on the warning. This row does not say whether a firm row missing from firm_forms should be refused or warned."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T05:19Z",
    "class": "OBSERVATION",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S10",
    "hazard_standing": "INERT",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W3-S5 and W3-S6: check_en.py's t2 subcommands now run safe-apply.sh by the absolute Git Bash the estate's resolver names, and seat the halt checkpoint's identity for their one run. T2-AC1 and T2-AC2 read PASS on EN-t-2's stage and FAIL where no stage exists.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROWS: LGIC_ENFORCE-W3-S5 (a bare 'bash' resolves to the WSL launcher) and W3-S6 (the halt checkpoint reads identity only from org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial), both BLOCKING and ARMED, disarm_owner 2.0.0_SA_COO~G.",
        "FIX @c30637c49c: fixed_inputs/check_en.py -- run_bash() through .tools/git_bash_resolver.py; _apply writes the running serial to a synthetic session file and removes it in a finally block.",
        "DISCRIMINATING PAIR, EN-t-2's worktree, the same inputs for both: t2-refuse FAIL-NOT-REFUSED-BEFORE-PLAN -> PASS-REFUSED-BEFORE-PLAN; t2-pass FAIL-GOOD-TREE-BLOCKED -> PASS-STAGE-PASSES.",
        "NEGATIVE ARM: the patched checker in EN-f-1's worktree, whose safe-apply.sh carries no naming stage, reads FAIL on both. Session files left in either worktree afterwards: 0."
      ]
    },
    "spec_asserts": "TO-EN-t-2 T2-AC1: 'an apply over a tree naming a resource the module would not produce is refused before Terraform is called'; T2-AC2: 'the tree with a module-produced name passes the stage and reaches Terraform'.",
    "world_is": "Before the fix, neither criterion could reach safe-apply.sh on this box, whatever the stage did. After it, both measure the stage, as their text says.",
    "notes": "DISARM by the owner. The criteria text, the face and the fixtures are unchanged; the fix corrects how the instrument launches its process. INERT: TO-EN-t-2's criteria are re-run by a worker cut from a base carrying the fix."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T05:19Z",
    "class": "OBSERVATION",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S11",
    "hazard_standing": "INERT",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W1-S16: check_en.py reads the live plane through the .tools/aws shim, run by Git Bash, not a bare 'aws' this box cannot launch. F1-AC4 reads PASS-PRIOR-VERBATIM on EN-f-1's record; EN-f-2's f2-policy-live and f2-removed share the fixed path.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S16 (BLOCKING, ARMED, disarm_owner 2.0.0_SA_COO~G): no aws.exe, only the .CMD and bash shims.",
        "FIX @c30637c49c: fixed_inputs/check_en.py -- aws_json() and f2-removed call run_bash(['.tools/aws', ...]).",
        "DISCRIMINATING PAIR, EN-f-1's worktree: f1-prior FAIL-PRIOR-DIFFERS ('NOT RUNNABLE: [WinError 2]') -> PASS-PRIOR-VERBATIM ('PRIOR == LIVE (read now): True')."
      ]
    },
    "spec_asserts": "TO-EN-f-1 F1-AC4: 'FENCE_PRIOR_POLICY.json equals the live policy read now'.",
    "world_is": "Before the fix, the live read never ran on this box, so F1-AC4 read FAIL whatever the file held. After it, the criterion compares the file with the live policy.",
    "notes": "DISARM by the owner, before EN-f-2 spawns: f2-policy-live and f2-removed go through the same function. INERT: F1-AC4 is re-run by a worker cut from a base carrying the fix."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T05:19Z",
    "class": "OBSERVATION",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S12",
    "hazard_standing": "INERT",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W2-S7: check_en.py's p1-surface passes over a carrier whose grade RAISES, as the cell's rule says, instead of stopping on it. P1-AC1 reads PASS-SURFACE-BY-RULE on EN-p-1's record, the rule's surface found at carrier 23 of 12,953.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W2-S7 (BLOCKING, ARMED, disarm_owner 2.0.0_SA_COO~G): the checker stopped on carrier 1's RaiseDefect.",
        "FIX @c30637c49c: fixed_inputs/check_en.py -- p1_surface catches the module's own RaiseDefect per carrier and counts it; any other exception is a FAIL-NOT-EVALUABLE verdict, returned.",
        "DISCRIMINATING PAIR, EN-p-1's worktree: FAIL-NOT-EVALUABLE -> PASS-SURFACE-BY-RULE ('carriers read: 23 of 12953, passed over on a RAISE: 18'), matching the worker's own statement of the rule's result.",
        "NEGATIVE ARM: the patched checker in the primary tree, where no exercise record exists, reads FAIL-SURFACE."
      ]
    },
    "spec_asserts": "TO-EN-p-1: 'The first whose token grade(token, \"S3Key\") marks OUT-OF-PATTERN is the SURFACE.'",
    "world_is": "Before the fix, P1-AC1 could not read PASS on any record, because 18 of the first 22 carriers raise. After it, the criterion applies the cell's rule.",
    "notes": "DISARM by the owner. The criterion text and the face are unchanged. INERT: P1-AC1 is re-run by a worker cut from a base carrying the fix."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T05:19Z",
    "class": "OBSERVATION",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S13",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "one_line": "Issuer's fix for LGIC_ENFORCE-W1-S17, not yet exercised: check_en.py's f2-signoff now reads the SIGNOFF lines from every committed version of the ledger entry as well as the file, so deploy_ledger.py's rebuild of the entry at a close-leg cannot erase the evidence that both seats signed before the apply.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S17 (ARMED, disarm_owner 2.0.0_SA_COO~G): deploy_ledger.py rebuilds the entry from its sentinel on every close-leg, dropping lines it did not write.",
        "FIX @c30637c49c: fixed_inputs/check_en.py -- _entry_history_text() reads 'git show <commit>:<entry>' for every commit that touched the entry, and f2_signoff reads the union.",
        "NOT EXERCISED: no SIGNOFF line exists yet, because gate G-E has not run. The criterion's question and its grammar are unchanged."
      ]
    },
    "spec_asserts": "TO-EN-f-2's f2-signoff: both SIGNOFF lines precede L2's close, the apply.",
    "world_is": "The ledger tool is the only writer of the entry at a close-leg, and it keeps only what its sentinel holds. A SIGNOFF line committed before the apply survives in the entry's git history.",
    "notes": "ARMED until exercised: EN-f-2's f2-signoff, run after G-E and the L2 close, is the first read that can show the history reader finds the two lines. The tool behavior itself (deploy_ledger.py dropping foreign lines at close-leg) goes to its owner at the round's drain-end read. The two SIGNOFF lines, when G-E runs, are committed before EN-f-2 applies."
  },
  {
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T05:19Z",
    "class": "OBSERVATION",
    "disposition": "UNDER_INVESTIGATION",
    "id": "LGIC_ENFORCE-S14",
    "hazard_standing": "INERT",
    "one_line": "Issuer's disposition of LGIC_ENFORCE-W3-S8: under ENFORCE, the safe-apply limb would refuse 57 of 78 Terraform roots, because an apply has no diff to split new from existing names. The limb ships in WARN, the enforce file is absent, and the live flip is gate G-F, outside this round.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W3-S8 (OBSERVATION, ARMED, disarm_owner 2.0.0_SA_COO~G), measured by EN-t-2's worker over the 78 roots at HEAD.",
        "STATE: org/mcp/naming-gate.enforce is absent (G1-AC14 and the EN-g-1 drain), and the stage never changes safe-apply's exit code in WARN mode (EN-t-2's WARN control)."
      ]
    },
    "spec_asserts": "The PRD's DEC-6 matrix: NEW names refuse, EXISTING names warn unless a remediation owns the surface.",
    "world_is": "The commit limb reads a diff and so can tell NEW from EXISTING; the apply limb reads a whole tree and cannot. Under one shared enforce switch, an ENFORCE flip would refuse most applies.",
    "notes": "INERT for this round: nothing sets ENFORCE. The finding bears on gate G-F, the live flip, and goes to 1.0.0_SA_CTO at the round's drain-end read: the apply limb needs its own switch or an existing-name baseline before G-F."
  },
  {
    "id": "LGIC_ENFORCE-W2-S7",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-15T03:41Z",
    "one_line": "check_en.py p1-surface cannot evaluate the order's rule. It calls grade(token, 'S3Key') inside a bare next() with no RaiseDefect handling, and the first sorted carrier raises, so P1-AC1 prints FAIL-NOT-EVALUABLE whatever the record says.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "INSTRUMENT: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:986-994 @39aae459ed. want = next(p for p, _, tok in cands if tok and o.grade(tok, 'S3Key')[0] == 'OUT-OF-PATTERN') sits inside a try whose except prints FAIL-NOT-EVALUABLE. A RaiseDefect from any candidate before the first OUT-OF-PATTERN ends the read.",
        "RUN, before any record existed (WS wk-lgic-enforce-1-2-p1 @39aae459ed): 'RaiseDefect: K1: segment 1 '\\\\\"' is neither a source nor a tier' / 'VERDICT: FAIL-NOT-EVALUABLE', rc=1.",
        "WHY: sorted by (path, line), candidate 1 of 12953 is .claude/settings.local.json:26 with token '\\\"/aws/lambda/inf-ec2-launch-monitor\\\"'. It raises in lib/opal_naming.py _grade_key (:1225 @39aae459ed). 18 of the first 22 candidates raise and 4 grade CONFORMANT.",
        "THE RULE, read with a raising token skipped (a RAISE is not OUT-OF-PATTERN): candidate 23 of 12953, .claude/skills/mdpf-refresh/mdpf_refresh.py:292, token 'platinum/mdpf/inflection/aggregate-aua-timeseries.json', OUT-OF-PATTERN -> 'mdpf/inflection/platinum/aggregate-aua-timeseries.json'. EXERCISE_FWD6.md names this path."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-p-1 WORKER FACE: 'The first whose token grade(token, \"S3Key\") marks OUT-OF-PATTERN is the SURFACE.' P1-AC1 runs check_en.py p1-surface and expects 'VERDICT: PASS-SURFACE-BY-RULE'.",
    "world_is": "The instrument raises at carrier 1 of 12953, before it reaches the rule's answer at carrier 23, so no record can pass P1-AC1. The fixed inputs are read-only to the worker.",
    "notes": "P1-AC1 is recorded FAIL by output and the order stays open. The record states the rule's result as read with raising tokens skipped."
  },
  {
    "id": "LGIC_ENFORCE-W2-S8",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-15T03:41Z",
    "one_line": "A live remediation already owns the rule's surface. MDPF_CANON's s3-prefix platinum/mdpf/ matches the bucket-less key, so the touching diff is refused before any row is planted. The planted row shows only in the project name the refusal prints.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRE-PLANT CONTROL, practice copy prac-lgic-enforce-p1 @39aae459ed, the touching diff with --enforce: 'NAMING REFUSE .claude/skills/mdpf-refresh/mdpf_refresh.py:292 platinum/mdpf/inflection/aggregate-aua-timeseries.json -> mdpf/inflection/platinum/aggregate-aua-timeseries.json', 'why: EXISTING and OUT-OF-PATTERN as S3Key in a surface remediations.json assigns to the live remediation MDPF_CANON', 'NAMING-GATE: REFUSE 1 graded', rc=1.",
        "MECHANISM: .tools/naming-gate.py remediation_of (:613-632 @39aae459ed). A key whose first segment is not a bucket gets bucket None, and the test 'bucket is None or bucket == sf.get(\"bucket\")' admits every s3-prefix by prefix alone. infra/logic/registry/remediations.json:28 @39aae459ed: MDPF_CANON owns {s3-prefix, opal-data-portal-v2, platinum/mdpf/}. org/missions/D8/MDPF/MDPF_CANON/project.json reads status 'active'.",
        "POST-PLANT, plant 6640c8153d on prac-lgic-enforce-p1 with the row placed first in the array: the same diff was refused and named 'the live remediation PRAC_FWD6REM'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-p-1 WORKER FACE step 1: 'Plant ONE remediations.json row: a fictitious remediation project owning that surface.' Step 2: 'it must REFUSE, naming the surface.'",
    "world_is": "The surface was owned before the plant, so a REFUSE alone cannot show that the planted row was read. The worker put the row first and ran a pre-plant control. The discriminator is the project named (MDPF_CANON before, PRAC_FWD6REM after), not the verdict.",
    "notes": "Form only. The literal's bucket is a variable (Bucket=PORTAL, i.e. opal-data-portal-v2), so the bucket-less match happens to be right for this surface."
  },
  {
    "id": "LGIC_ENFORCE-W2-S9",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-15T03:41Z",
    "one_line": "The registry's own validator refuses the fictitious row the order asks for, because the project is not in DIRECTIVES.yaml. The commit limb loads the registry without validating and still reads the row as live, so the refusal fired on a row validate refuses.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python lib/opal_naming.py validate in the practice copy. Pre-plant (39aae459ed): 'VALIDATE: OK 16 system row(s), 9 scope row(s), 9 warning(s) at registry@50e4fabd1cb6a150', rc=0. Post-plant (6640c8153d): rc=1, 'REFUSED remediations.json[0].project: 'PRAC_FWD6REM' is not a project in org/missions/DIRECTIVES.yaml', 'REFUSED remediations.json[0].owner_directive: 'D14': the directive whose projects list names 'PRAC_FWD6REM'', 'VALIDATE: REFUSED 2 refusal(s), 9 warning(s)'.",
        "RULE: lib/opal_naming.py:414-420 @39aae459ed. LOAD WITHOUT VALIDATION: .tools/naming-gate.py:509 @39aae459ed calls mod._registry(), and lib/opal_naming.py:121-124 shows that is load_registry with no validate().",
        "COMMIT: the plant commit ran every safe-commit stage clean ('[naming-gate] NAMING-GATE: PASS 0 graded'; to-pipeline-gate and surprise-row-gate OK). No stage validates the registry."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-p-1 WORKER FACE step 1: 'Plant ONE remediations.json row: a fictitious remediation project owning that surface. Commit it on the scratch branch.'",
    "world_is": "The plant commit 6640c8153d landed with every stage clean, yet validate refuses the registry at that commit, and the limb still honoured the row. A fictitious project and a valid registry cannot both hold.",
    "notes": "Scratch branch only, never merged. Form only: whether the limb should validate the registry it reads is not this worker's call."
  }
]
```
