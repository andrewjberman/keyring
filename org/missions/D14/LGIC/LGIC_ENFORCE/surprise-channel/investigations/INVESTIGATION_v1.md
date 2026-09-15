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
  }
]
```
