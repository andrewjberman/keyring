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
  },
  {
    "id": "LGIC_ENFORCE-W3-S5",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-15T04:03Z",
    "one_line": "T2-AC1 and T2-AC2 cannot print PASS on this box whatever the build: check_en.py _apply runs subprocess ['bash', '.tools/safe-apply.sh', ...], and Windows CreateProcess resolves a bare 'bash' to C:\\Windows\\System32\\bash.exe (the WSL launcher), which fails before safe-apply.sh runs.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CHECKER: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:906 @39aae459ed calls run(['bash', '.tools/safe-apply.sh', '-chdir=...', 'apply'], ...), and run() (:104-114) hands that list argv to subprocess.run.",
        "MEASURED in the worktree wk-lgic-enforce-1-3-t2: python subprocess.run(['bash','-c','echo BASH=$BASH_VERSION']) -> rc 1, stderr '<3>WSL (9 - Relay) ERROR: CreateProcessCommon:800: execvpe(/bin/bash) failed: No such file or directory', while shutil.which('bash') -> C:\\Program Files\\Git\\usr\\bin\\bash.EXE. 'where bash' lists Git's two bash.exe, then C:\\Windows\\System32\\bash.exe, then the WindowsApps alias; CreateProcess searches the system directory before PATH.",
        "CRITERION RUNS, the named invocations after the build: t2-refuse -> 'rc=1  terraform called: False  <3>WSL (9 - Relay) ERROR: CreateProcessCommon:800: execvpe(/bin/bash) failed: No such file or directory' then 'VERDICT: FAIL-NOT-REFUSED-BEFORE-PLAN'; t2-pass -> the same WSL line then 'VERDICT: FAIL-GOOD-TREE-BLOCKED'. The pre-build baseline run of t2-pass printed the same WSL line, so the failure does not depend on the build.",
        "CONTROL, not a criterion: the checker's own t2_refuse and t2_pass with argv[0] swapped for Git Bash's path and nothing else reach safe-apply.sh, and then stop at the halt checkpoint (row LGIC_ENFORCE-W3-S6)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-2 T2-AC1 and T2-AC2: 'cd <WS> && timeout 120 python .../check_en.py t2-refuse' expects 'VERDICT: PASS-REFUSED-BEFORE-PLAN'; 't2-pass' expects 'VERDICT: PASS-STAGE-PASSES'.",
    "world_is": "Both invocations print FAIL before any line of safe-apply.sh runs, because the checker's 'bash' is the WSL launcher on this box. The checker is a read-only fixed input and bash resolution is outside the worker's grant, so neither criterion can pass by output here.",
    "notes": "Form only. For the same reason the issuer's negative arm (selftest-negative) reads FAIL on t2-refuse and t2-pass whether or not the stage exists, so it could not tell a missing stage from a missing bash. One remedy shape, not taken: resolve argv[0] with shutil.which('bash') in _apply."
  },
  {
    "id": "LGIC_ENFORCE-W3-S6",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-15T04:03Z",
    "one_line": "Even with Git Bash, safe-apply.sh stops at its halt checkpoint in a worker worktree: halt-gate-check.sh resolves the principal only from org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial or an orphan-cleaned marker under the worktree root, neither exists there, and it fails closed IDENTITY UNRESOLVED (exit 3) before the naming stage.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RESOLVER: .tools/halt-gate-check.sh:52-119 @39aae459ed reads the CLAUDE_CODE_SESSION_ID .serial file, then a <sid>.*.orphan-cleaned marker, then returns 1; :38 sets HALT_GATE_REPO_ROOT to the directory above the library, which is the worktree; :272-290 prints IDENTITY UNRESOLVED and returns 3. OPAL_AGENT_SERIAL is not read: it was exported for the run and the gate still blocked.",
        "MEASURED: CLAUDE_CODE_SESSION_ID=9d2c2e56-da40-4edc-ba9d-6924a8f8a17d. The worktree's org/mcp/sessions/ (gitignored, .gitignore:423) holds no file for it. The main tree's copy holds '2.0.0_SA_COO~G': the worker runs under the issuer's session id, so even a copied file would name the issuer, not the worker.",
        "CONTROL, not a criterion: check_en.py t2_refuse and t2_pass with Git Bash substituted -> 'rc=3  terraform called: False', the IDENTITY UNRESOLVED banner, then FAIL-NOT-REFUSED-BEFORE-PLAN and FAIL-GOOD-TREE-BLOCKED. The checker sets HALT_ACK=1 (check_en.py:907), which acknowledges routine messages but names no principal.",
        "GRANT: the order's <paths> are .tools/safe-apply.sh, .tools/naming-apply-gate.py and this channel. org/mcp/sessions/ is not among them, and T2-AC3 requires the stage to run AFTER the halt checkpoint, so no placement of the stage reaches it first."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-2: the checker exercises the stage with a stub Terraform (SAFE_APPLY_TERRAFORM) over the issuer's trees, and the stage sits AFTER the halt checkpoint (T2-AC3).",
    "world_is": "In a worker worktree the halt checkpoint cannot resolve a principal, so every safe-apply run from there exits 3 before the naming stage, whatever the bash. The two criteria that run safe-apply.sh cannot reach the stage on this box.",
    "notes": "Form only. The same checkpoint runs first on every safe-apply from a worker worktree; the decomposition's tool pins for the applied cells (LGIC_ENFORCE_DECOMP.md:282-285 @53d221f334) export OPAL_AGENT_SERIAL for 'the two identity gates safe-apply carries', which this resolver does not read. With the halt library stubbed in a scratch copy (deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_controls.py), the checker's own assertions print PASS-REFUSED-BEFORE-PLAN and PASS-STAGE-PASSES over this build, and both FAIL over the base commit's safe-apply.sh."
  },
  {
    "id": "LGIC_ENFORCE-W3-S7",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-15T04:03Z",
    "one_line": "The issuer's bad_tree name BadQueueName is not OUT-OF-PATTERN: grade('BadQueueName','SQS_QUEUE') RAISES (R1.f: 'bad' is in no vocabulary), so no canonical form exists to print; the limb refuses it under DEC-6's RAISE row and prints '-> (rule or registry defect)'.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: lib/opal_naming.py @39aae459ed grade('BadQueueName','SQS_QUEUE') raises RaiseDefect \"R1.f: 'bad' is in no vocabulary; no registry row resolves it\"; so do 'badqueuename' and 'bad-queue-name'. grade('etfs-price-refresh-queue','SQS_QUEUE') -> ('CONFORMANT', 'etfs-price-refresh-queue').",
        "RULE: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:255 @78128f29ea: a RAISE is 'printed as a rule or registry defect, never as a verdict, and refused like any refusal once enforcing'. The limb prints 'NAMING REFUSE .../t2/bad_tree/main.tf:2 BadQueueName -> (rule or registry defect)', why 'RAISE as SQS_QUEUE: a rule or registry defect, not a naming verdict: R1.f ...', and exits 1 under NAMING_GATE_ENFORCE=1.",
        "COMMIT LIMB: .tools/naming-gate.py:699-703 @8a60d8e74e counts a RAISE as WARN even when enforcing, unless a NEW firm carrier rides on it. This limb follows PRD :255, so the two limbs differ on a RAISE under ENFORCE."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-2: 'bad_tree names a queue BadQueueName'; T2-AC1: refused before Terraform is called, 'with the canonical printed'; the limb has 'the same output lines and enforce rules as the commit limb'.",
    "world_is": "The name has no canonical form, only a RAISE. The limb prints the commit limb's defect string where the canonical goes, and refuses a RAISE once enforcing as DEC-6 says, where the commit limb warns on one.",
    "notes": "Form only. check_en.t2_refuse asserts only '->' and 'BadQueueName' in the output, so it cannot tell a canonical from the defect string. The canonical path is exercised elsewhere: the coverage control graded 593 names at HEAD REFUSE with a canonical printed (OUT-OF-PATTERN or ALIAS)."
  },
  {
    "id": "LGIC_ENFORCE-W3-S8",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-15T04:03Z",
    "one_line": "At apply there is no diff, so DEC-6's NEW/EXISTING split has nothing to read: the limb reads every graded name as the tree states it, and one switch (org/mcp/naming-gate.enforce) arms both limbs. Under ENFORCE, 57 of the 78 Terraform roots at HEAD would be refused before plan.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RULE: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:243-244 @78128f29ea: 'A string is NEW when it is on the diff's added lines and absent from the same file's pre-image'. An apply carries no diff, and whether a resource is being ADDED is known only to a plan, which the PRD (:290-291) and the cell place after this stage.",
        "MEASURED @39aae459ed with this build (deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_coverage.py): 78 directories hold a tracked .tf under infra/aws/terraform; 1266 resource-name attributes of the limb's 30 types; 1148 graded literals: 144 CONFORMANT, 3 NOT-GRADED, 593 REFUSE as OUT-OF-PATTERN or ALIAS, 408 REFUSE as RAISE; 118 expressions not graded. 57 of 78 roots carry at least one REFUSE verdict.",
        "SWITCH: .tools/safe-commit.sh:691 @39aae459ed and this order's stage in .tools/safe-apply.sh read the same NAMING_GATE_ENFORCE=1 or org/mcp/naming-gate.enforce, as the order requires ('the same enforce rules')."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-2: 'with the same output lines and enforce rules as the commit limb'; DEC-6's matrix grades NEW against a diff's pre-image.",
    "world_is": "The matrix's NEW/EXISTING axis does not exist at apply, so the limb refuses every name the module would not produce. That is what T2-AC1 asks for, and it also means the one flip that arms the commit limb leaves 57 of 78 existing roots unapplyable until their names are remediated or exempted.",
    "notes": "Form only. No criterion turns on the 57. In WARN mode, the shipped state, the stage never changes safe-apply's exit code (control: the bad tree with NAMING_GATE_ENFORCE unset reaches the stub terraform, rc 0)."
  },
  {
    "id": "LGIC_ENFORCE-W3-S9",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-15T04:03Z",
    "one_line": "The order says the limb grades every resource-name attribute, but 118 of 1266 at HEAD are expressions (references, calls, templates) whose value exists only in a plan. The limb runs before plan, so it lists them as 'unresolved before plan' and grades none of them.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED with deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_coverage.py @39aae459ed: 1266 attributes, 1148 literal, 118 expression, 0 reading a module whose source is opal_name. At the census base fd9c9ca174 the limb's reader and EN-t-1's census (its own tfscan.py) agree row for row: 1266 and 1266, 0 one-sided, the literal/expression split 1148/118 identical, 0 literal values differing.",
        "MEASURED: grade('etfs-{x}-queue','SQS_QUEUE') raises 'G3: the tokeniser cannot place a character of a resource name'. A template graded with the commit limb's {x} placeholder would RAISE, and under ENFORCE be refused, whatever it resolves to.",
        "CENSUS: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md section 4 @1cc0d2fe73 resolved 100 of its 124 expression values statically, as 'inferred' (a variable default can be overridden at apply). The limb resolves none: it refuses only on a string it has read."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-t-2: 'It grades every resource-name attribute in DIR's .tf files with grade()'.",
    "world_is": "An expression-valued name attribute has no string to grade before plan. The limb grades the literals, lists each expression with its source text, and prints the split on its NAMING-APPLY denominator line. A name passed through the opal_name module is an expression and passes.",
    "notes": "Form only. No criterion turns on it: both fixture trees name their queue with a literal."
  },
  {
    "id": "LGIC_ENFORCE-W1-S13",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T03:49Z",
    "one_line": "generate() renders no exemptions local, so the fence's exemption list cannot come from the module's GENERATED locals as TO-EN-f-1 says. Module opal_name reads infra/logic/registry/exemptions.json itself, with file() and jsondecode(), in main.tf.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: lib/opal_naming.py _gen_locals (:697-723 @39aae459ed) renders scope_short, scope_long, scope_class, name_scope_classes, scope_bucket, fence_patterns and account_id. It renders no exemptions list. The regenerated generated_locals.tf (registry@ba5318901b937130) has no exemptions local either.",
        "GRANT: TO-EN-f-1 <paths> names infra/aws/terraform/modules/opal_name/ and infra/logic/registry/exemptions.json. It does not name lib/, so the generator cannot be extended in this cell.",
        "BUILT: modules/opal_name/main.tf local fence_exemption_arns = jsondecode(file(\"${path.module}/../../../../logic/registry/exemptions.json\")), mapped per bucket to principal ARNs; output fence_exemption_arns. The Deny reads module.opal_name.fence_patterns[\"49financial\"] and module.opal_name.fence_exemption_arns[<bucket>].",
        "RUN: check_en.py f1-no-typed-list 'VERDICT: PASS-NO-TYPED-LIST'; m1-no-external PASS (no data \"external\"); m1-vectors '37 passed, 0 failed'; the plan renders the 1 pattern and the 16 exemption ARNs into the policy's ArnNotLike list."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-1 cell step 2: 'Both lists come from the module's generated locals and are never typed (DEC-4 (iii))'. Step 1: 'Then regenerate the module locals (generate)'.",
    "world_is": "generate() writes fence_patterns into generated_locals.tf and no exemptions list, and the generator (lib/) is outside this order's grant. The exemption list reaches the policy through a module local that reads the registry file at plan time, not through a generated local. It is still never typed.",
    "notes": "Form only. To bring the exemptions into the generated locals, _gen_locals would render one more map, and a seat whose grant holds lib/opal_naming.py would do it."
  },
  {
    "id": "LGIC_ENFORCE-W1-S14",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T03:49Z",
    "one_line": "Adding the exemption rows moves the registry hash from 50e4fabd1cb6a150 to ba5318901b937130, so 7 generated views outside this order's grant now carry a stale GENERATED header. Their content is otherwise unchanged.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: lib/opal_naming.py REGISTRY_FILES (:52 @39aae459ed) includes exemptions.json, and registry_hash (:92-101) hashes every registry file. RUN: 'VALIDATE: OK 16 system row(s), 9 scope row(s), 9 warning(s) at registry@ba5318901b937130' after the rows, where the base read 50e4fabd1cb6a150.",
        "READ: at base 39aae459ed, 50e4fabd1cb6a150 appears in 7 generated views outside TO-EN-f-1's <paths>: data/firm_registry.json, infra/aws/lambda-edge/_shared/firm-config.mjs, infra/aws/lambda/investor-reporting/_authz/loaders.py, data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py, data/assets/scripts/gold/investor_reporting/holdings_snapshot.py, data/assets/scripts/gold/investor_reporting/directory_runner.py and .tools/ds-precommit-check.py. The module's two generated files are in the grant and were regenerated here.",
        "RUN: python lib/opal_naming.py generate --out .scratch/regen (9 written) compared line by line with each live view: 7 of 7 differ ONLY in the lines naming the old hash (8 lines in total; 0 other differing lines). So the views' exported content is unchanged and only their headers are stale.",
        "CODE: check_en.py _v_header (:713-716 @39aae459ed) requires each view to carry the CURRENT registry hash. On a tree carrying this order's commit, every EN-v-<n> header criterion reads FAIL-HEADER until those 7 views are regenerated."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-1 cell step 1: add the exemptions.json rows, 'Then regenerate the module locals (generate)'. The <paths> grant names infra/logic/registry/exemptions.json and infra/aws/terraform/modules/opal_name/ only.",
    "world_is": "The registry hash covers exemptions.json, so any exemption row re-stales the header of every generated view. The order grants regeneration of the module's files only, and the 7 other views keep the old hash until a seat whose grant holds them runs generate.",
    "notes": "Form only. The disarm is one generate over those 7 targets (header-only, measured above), by the issuer or a cell it names. Left alone, the EN-v header criteria go red on the drained tree."
  },
  {
    "id": "LGIC_ENFORCE-W1-S15",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T03:49Z",
    "one_line": "The exemptions.json row form ('principal (a role name or an ARN)') cannot write an IAM user or a service-linked role in a form both check_en.py f1-covered and the policy accept, so each row also carries an arn field.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: check_en.py f1_covered (:540-557 @39aae459ed) finds a writer's row by its census name, or by 'arn:aws:iam::313476888478:role/' + name. A row written as a user ARN (user/Andrew_Berman) or a service-linked role ARN (role/aws-service-role/<service>/<name>) matches neither, so it reads UNCOVERED.",
        "CENSUS: FENCE_WRITER_CENSUS.md opal-data-49financial holds 16 principals: 3 are IAM users (Andrew_Berman, Andrew_Berman_Console, Opal_Terminal) and 3 are service-linked roles under aws-service-role/ paths. For those 6, a bare name rendered as role/<name> is a principal that does not exist, so the policy would deny the real one.",
        "CODE: lib/opal_naming.py validate (:404-410 @39aae459ed) requires principal, reason and signoff_ref, and refuses no other field. RUN after the rows: 'VALIDATE: OK'.",
        "BUILT: each of the 16 rows has principal = the census name and arn = the census ARN. main.tf takes arn first. RUN: f1-covered 'WRITERS OF opal-data-49financial: 16  COVERED: 16'."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "infra/logic/registry/exemptions.json _about.row_fields at base: 'principal (a role name or an ARN); reason; signoff_ref'.",
    "world_is": "Six of the sixteen principals are not the role ARN of their name. The checker matches only the name, and the policy needs the true ARN, so rows carry both and _about.row_fields now names arn.",
    "notes": "Form only."
  },
  {
    "id": "LGIC_ENFORCE-W1-S16",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T04:22Z",
    "one_line": "check_en.py f1-prior cannot read the live policy on this box. Its run() starts a bare 'aws' through Python's subprocess, which finds no aws.exe (only .CMD and bash shims exist), so F1-AC4 prints NOT RUNNABLE [WinError 2] and FAIL-PRIOR-DIFFERS whatever FENCE_PRIOR_POLICY.json holds.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN, the named invocation, twice (about 04:05Z and 04:18Z on 2026-09-15), identical: 'PRIOR == LIVE (read now): False  NOT RUNNABLE: [WinError 2] The system cannot find the file specified' / 'VERDICT: FAIL-PRIOR-DIFFERS' / rc=1.",
        "CODE: check_en.py run() (:104-114 @39aae459ed) calls subprocess.run(cmd) with the shell off; aws_json (:176-183) passes ['aws', ...]; the OSError comes back as rc 127 'NOT RUNNABLE'; _live_policy (:601-608) returns None, and f1_prior (:611-619) prints FAIL.",
        "ENV: C:\\Users\\AndrewBerman\\AppData\\Local\\Programs\\Python\\Python312\\python.exe: shutil.which('aws') returns C:\\Users\\AndrewBerman\\bin\\aws.CMD and which('aws.exe') returns None. where.exe aws lists only bin\\aws, bin\\aws.cmd, Python312\\Scripts\\aws and Python312\\Scripts\\aws.cmd. There is no C:\\Program Files\\Amazon\\AWSCLIV2\\aws.exe. For a bare name, CreateProcess tries only .exe.",
        "DIFFERENT INSTRUMENT (not the criterion's output): the .tools/aws shim from bash, read at 2026-09-15T04:18:57Z. FENCE_PRIOR_POLICY.json is byte-equal (428 bytes) and parse-equal to the live Policy string. Negative control: the same file with one pattern dropped reads unequal.",
        "SCOPE: every aws call in check_en.py goes through the same run(). f2-policy-live (:655-663) and f2-removed (:695-703), EN-f-2's criteria, fail the same way on this box."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-1 F1-AC4: 'cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py f1-prior', expecting 'VERDICT: PASS-PRIOR-VERBATIM': FENCE_PRIOR_POLICY.json equals the live policy read now.",
    "world_is": "In this worktree's shell, the named invocation cannot start its aws read, so it cannot print PASS. The file equals the live policy by a different instrument, but that is not the criterion's output.",
    "notes": "Form only. F1-AC4 is recorded FAIL by its output, and the order stays open. The disarm belongs to the instrument: run() would have to resolve aws in a form this box can start (for example, shutil.which, which finds the .cmd shim). That file is the issuer's fixed input, and a worker may not edit it."
  },
  {
    "id": "LGIC_ENFORCE-W1-S17",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T04:22Z",
    "one_line": "TO-EN-f-1 has the author hand-add SIGNOFF slots to the ledger entry, and the ledger tool does not keep them. deploy_ledger.py re-renders the whole entry from its sentinel on every close-leg, so EN-f-2's first close-leg erases both seats' SIGNOFF lines, the lines f2-signoff reads.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: .tools/deploy_ledger.py _render_entry (:239-286 @39aae459ed) builds the entry from the sentinel's fields only: the header, the manifest and the log. _write_entry (:289-291) overwrites the file. Its docstring says 'open / close-leg / close / hold re-render the entry from the sentinel' and 'Never hand-edit an entry.'",
        "EXERCISED in memory, no file written: _render_entry of this ledger's sentinel returns 23 lines with no '## Sign-off', while the entry on disk has 34 lines, the section included. A sentinel with one more log event (a simulated close-leg) renders with no SIGNOFF line. Positive control: the render equals the on-disk entry up to its Log.",
        "CODE: check_en.py f2_signoff (:645-652 @39aae459ed) reads the SIGNOFF lines from the entry's text and requires both timestamps to be before L2's closed_at. L2's close-leg is the very re-render that removes them.",
        "COMMITTED: the entry with its two blank slots, at 887cf01419 (org/critical_paths/change_management/20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-1 cell step 6: 'Leave two blank lines in the ledger entry for SIGNOFF 1.0.0_SA_CTO <YYYYMMDDTHHMMSSZ> <scope> and SIGNOFF 2.0.0_SA_COO~G <...>.'",
    "world_is": "The entry is a rendering of the sentinel, and the tool that closes L2 rewrites it without the Sign-off section. The sign-off record is erased by the step that records the apply it authorizes, unless its lines are carried where the tool keeps them or written back after every close-leg. f2-signoff then reads zero lines.",
    "notes": "Form only. The slots are left as the order says, at 887cf01419."
  },
  {
    "id": "LGIC_ENFORCE-S15",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T06:22Z",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W1-S14: the generated views are re-marked at registry@ba5318901b937130 by the generator itself, header lines only. v1..v6-header read PASS again on the shared tree, and v1..v6-delta0 read PASS, so every view exports what it did at its spawn base.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S14 (ARMED, disarm_owner 2.0.0_SA_COO~G): EN-f-1's 16 exemption rows moved the registry hash from 50e4fabd1cb6a150 to ba5318901b937130.",
        "BEFORE, on the shared tree at 9a05002d39: v1-header through v6-header read FAIL-HEADER, 6 of 6.",
        "REGEN @79ccef7d45, merged @93edc0fdc3: 'python lib/opal_naming.py generate --out .' wrote 9 files, 8 changed and 1 already current. Diff lines other than the GENERATED mark or the JSON _generated key: 0.",
        "AFTER, the issuer's checker @c30637c49c: v1..v6-header PASS-GENERATED-HEADER 6 of 6; v1..v6-delta0 PASS-DELTA0 6 of 6; m1-header PASS; m1-vectors PASS-VECTORS-MATCH.",
        "LANE: three of the eight paths sit in CLOUD_OPS_OR_ETL, so the regeneration commit carries GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL (audited)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round's interfaces: a GENERATED file carries 'GENERATED by lib/opal_naming.py from infra/logic/registry@<first 16 hex of registry_hash()>'.",
    "world_is": "registry_hash() spans every registry file, exemptions.json included, so a fence exemption re-marks all nine views though none of them reads exemptions.json.",
    "notes": "DISARM by the owner. The design point -- one registry file's rows re-mark every view, including views that do not read it -- goes to 1.0.0_SA_CTO at the round's drain-end read: a per-view hash over the files that view reads would not move on an exemption. INERT: the shared tree reads current again."
  },
  {
    "id": "LGIC_ENFORCE-W8-S3",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~8",
    "surfaced_at": "2026-09-15T06:10Z",
    "one_line": "D2-AC2's instrument, check_en.py d2-control, never plants or searches anything. It passes if the worker-written control field in EXERCISE_FWD1_SEARCH.md has hits == 1 and a non-empty planted string, so the verdict repeats the graded worker's own number.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "CODE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:1129-1131 @9a05002d39. d2_control reads fenced_json(EXERCISE_FWD1_SEARCH.md).get('control') and prints PASS-CONTROL-FIRES if c.get('hits') == 1 and c.get('planted'). It runs no git show and no search, and writes no scratch copy.",
        "CODE, the contrast: the same file :1120-1126 @9a05002d39 (d2_zero) re-reads the committed pipeline with git show <commit>:<path> and re-searches it with its own regex, so D2-AC1 does not rest on the worker's hits field alone.",
        "RUN, this cell: the control was run for real on a scratch copy with one planted literal. grep read 1 match on it and 0 on the unplanted copy, and check_en.py's d2-zero regex, applied by hand, read ['opal-data-quillwater'] and []. EXERCISE_FWD1_SEARCH.md records both. The checker does not read those runs."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-d-2 D2-AC2: 'the search's positive control finds exactly one planted literal', graded by 'check_en.py d2-control' expecting 'VERDICT: PASS-CONTROL-FIRES'. The cell: 'plant one literal in a scratch copy of the file (never committed) and show that your search finds exactly one.'",
    "world_is": "The criterion's invocation cannot tell a control that was run from a json field typed as {\"planted\": \"x\", \"hits\": 1}. Its PASS is the worker's self-report passed through a checker. Whether the control ran can be judged only from the prose and outputs recorded in EXERCISE_FWD1_SEARCH.md, not from D2-AC2's output.",
    "notes": "Form only. The plant is not committed by design (the order says 'never committed'), so a checker that re-ran it would have to plant its own copy. That is the instrument owner's call (2.0.0_SA_COO~G, the fixed input's author). INERT: in this cell the control was run and its outputs are recorded, and no other cell uses d2-control."
  },
  {
    "id": "LGIC_ENFORCE-W1-S18",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T08:38Z",
    "one_line": "TO-EN-f-2 step 3 runs deploy_ledger.py close, which unlinks the ledger sentinel, and check_en.py finds the ledger entry only through that sentinel. After the ordered close, f2-closed prints FAIL-LEDGER-OPEN and f2-signoff prints FAIL-SIGNOFF on a ledger that is closed, with both SIGNOFF lines in its committed history. F2-AC8 cannot pass in any state the order produces.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN, the named invocations after 'python .tools/deploy_ledger.py close --slug lgic-enforce-fence-49financial' (rc 0, 'sentinel removed'), 2026-09-15T08:37:06Z..08:37:36Z: f2-signoff 'SIGNOFF LINES: {}  APPLY (L2 closed_at): none' / 'VERDICT: FAIL-SIGNOFF' rc=1; f2-closed 'SENTINEL: absent' / 'VERDICT: FAIL-LEDGER-OPEN' rc=1.",
        "RUN, the same f2-signoff before the close, 08:23:20Z, sentinel present: 'SIGNOFF LINES: {'1.0.0_SA_CTO': '20260915T072924Z', '2.0.0_SA_COO~G': '20260915T070844Z'}  APPLY (L2 closed_at): 20260915T081903Z' / 'VERDICT: PASS-SIGNED-BEFORE-APPLY' rc=0.",
        "CODE: check_en.py f2_closed (:737-740 @d7d801c323) is ok = (s is None or s.get('status') == 'CLOSED') and 'CLOSED' in _entry_text().upper(). _entry_text (:653-656) takes the entry path from the sentinel, so with the sentinel absent it returns '' and the second clause is False. With the sentinel present its status is OPEN, so the first clause is False. f2_signoff (:676-683) takes L2's closed_at from the sentinel, and _entry_history_text (:659-673) takes the entry path from it too.",
        "CODE: .tools/deploy_ledger.py cmd_close (:428-443 @d7d801c323) sets status 'CLOSED -- nothing stranded', re-renders the entry, and unlinks the sentinel (:440). After a tool close there is no sentinel, and no sentinel ever holds status == 'CLOSED'.",
        "WORLD: the entry org/critical_paths/change_management/20260915T0334Z_lgic-enforce-fence-49financial_deploy_completion.md reads '**Status:** CLOSED -- nothing stranded -- closed 20260915T083705Z', and its last line is the ordered 'CLOSED 20260915T083706Z'. Both SIGNOFF lines are in its committed history, at ccb7422e15 and 766b5a0cfb."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-2 step 3: 'Close leg L4, then python .tools/deploy_ledger.py close --slug lgic-enforce-fence-49financial, and append a CLOSED <YYYYMMDDTHHMMSSZ> line to the entry. Commit the entry and the sentinel.' F2-AC8: check_en.py f2-closed, expecting 'VERDICT: PASS-LEDGER-CLOSED'. F2-AC1: check_en.py f2-signoff, expecting 'VERDICT: PASS-SIGNED-BEFORE-APPLY'.",
    "world_is": "The tool closed the ledger and the entry says so, but the checker reaches the entry only through the sentinel that the close deletes. F2-AC8 reads FAIL in both states the order produces: sentinel present (status OPEN) and sentinel absent (no entry read). F2-AC1 turns from PASS to FAIL at the same step.",
    "notes": "Form only. F2-AC8 is recorded FAIL by its output, and the order stays open. F2-AC1 is recorded with both runs. The disarm belongs to the instrument, for example finding the entry by slug under change_management/ when the sentinel is absent, and reading L2's closed_at from the entry or its history. check_en.py is the issuer's fixed input and a worker may not edit it. Re-creating a sentinel by hand to satisfy the checker would forge the ledger's state."
  },
  {
    "id": "LGIC_ENFORCE-S16",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T10:05Z",
    "one_line": "Issuer's disarm of LGIC_ENFORCE-W1-S18, and S13's fix now exercised. check_en.py finds the ledger entry by slug once deploy_ledger.py close has deleted the sentinel (@78f8820a58). F2-AC1 and F2-AC8 read PASS on the closed ledger and FAIL on an open one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ROW: LGIC_ENFORCE-W1-S18 (BLOCKING, ARMED, disarm_owner 2.0.0_SA_COO~G). The checker reached the ledger entry only through the sentinel, which TO-EN-f-2's ordered close deletes, so F2-AC8 read FAIL both before and after the close.",
        "FIX @78f8820a58: _entry_path() takes the sentinel's entry_path, or else the single change_management/*_<slug>_deploy_completion.md. _l2_closed_at() reads the entry's own 'LEG L2 closed' log line. f2_closed requires both the tool's '**Status:** CLOSED' and the order's 'CLOSED <ts>' line.",
        "BOTH ARMS, running the fixed file. CLOUD @040c8475a2, sentinel OPEN: f2-closed FAIL-LEDGER-OPEN, and f2-signoff FAIL-SIGNOFF (L2 closed_at none). EN-f-2's worktree, sentinel deleted: PASS-LEDGER-CLOSED and PASS-SIGNED-BEFORE-APPLY.",
        "EXERCISED at the drain. 0.9.0_WK_LGIC_ENFORCE~1's re-run @1c66f3c806, and the issuer's re-run on a fresh detached checkout of that branch: F2-AC1..F2-AC8 8 of 8 PASS, proof VALID. Merged @c6d652a6dc.",
        "S13 (the history-read fix for W1-S17, recorded 'not yet exercised') is now exercised. F2-AC1 on the closed ledger reads both SIGNOFF lines (2.0.0_SA_COO~G 20260915T070844Z, 1.0.0_SA_CTO 20260915T072924Z) from the entry's committed history, after the close-leg re-render dropped them from the file."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-f-2 step 3 closes the ledger with deploy_ledger.py close, and F2-AC8 expects 'VERDICT: PASS-LEDGER-CLOSED' on that closed ledger.",
    "world_is": "The fixed checker reads the closed ledger: F2-AC8 and F2-AC1 PASS after the ordered close and FAIL while the ledger is open.",
    "notes": "DISARM of W1-S18 by its owner; S13's fix for W1-S17 is exercised. INERT. Carried to 1.0.0_SA_CTO at the round's drain-end read: deploy_ledger.py's re-render drops hand-written lines from an entry (W1-S17's mechanism). The fence entry no longer carries its Sign-off section, which survives only in the entry's history."
  },
  {
    "id": "LGIC_ENFORCE-S17",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T10:11Z",
    "one_line": "After EN-f-2's drain @c6d652a6dc, the shared index carried the pre-drain blobs of 2 drained paths (TO-EN-f-2 and this channel), staged with no merge in progress. Committed as it stood, the index would have flipped TO-EN-f-2 back to pending and removed row W1-S18, silently reverting the drain.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED 09:59Z-10:05Z on the primary checkout: 2 paths staged, no MERGE_HEAD, no index.lock. TO-EN-f-2's staged blob e4b65cfcfc reads '<status>pending</status>', where HEAD reads complete. The channel's staged blob 2855206f3a holds 65 rows, without W1-S18, where HEAD holds 66. Each staged blob equals its version at c6d652a6dc^1, the CLOUD commit before the drain.",
        "The working tree and HEAD (23cad64541) both held the drained versions: git diff HEAD on the 2 paths was empty. The staged entries were the only stale copy.",
        "FIRST SIGHTING: this seat's append precheck refused at ~09:45Z, minutes after the drain commit, on these 2 staged paths. The paths stayed staged through a 10-minute bounded wait.",
        "WRITER NOT IDENTIFIED: the 7 commits between c6d652a6dc and 23cad64541 (3.0.0_SA_CVO, 1.0.0_SA_CTO~A, 2.0.0_SA_COO~F) touch neither path. The drain merged 9 paths, and only these 2 were re-staged. Both carry a change on each side of the merge.",
        "REMEDY APPLIED: git restore --staged on exactly the 2 paths. The staged count then read 0, and the index equals HEAD for both. Nothing was lost: the unstaged content is the committed blob at c6d652a6dc^1. Row S16 committed @8cc66fe669 on the cleared index."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "safe-merge.sh commits the merged index. Afterwards the shared index differs from HEAD only by other seats' in-flight staging of their own paths (CLAUDE.md Rule 14b).",
    "world_is": "Minutes after the drain, some process staged snapshot blobs older than the drain for 2 of the drained paths. A pathspec-scoped safe-commit would not sweep them in. An unscoped commit, or a merge graded on this index, would revert the drain without an error.",
    "notes": "INERT: cleared by the issuer at 10:05Z. The mechanism's owner is unknown. The candidates are any tool that saves and restores the shared index around its own commit, or any git add from a stale checkout. Carried to 1.0.0_SA_CTO and 0.0.0_AB_MSTR at the round's drain-end read. A second sighting on any project would make it a pattern."
  },
  {
    "id": "LGIC_ENFORCE-S18",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T11:04Z",
    "one_line": "Correction to LGIC_ENFORCE-S17: the index restore did more than leave stale staging. It truncated the drain itself. Merge c6d652a6dc recorded 2 of EN-f-2's 8 changed paths, so CLOUD kept the probe-roles .tf and the open-deploy sentinel and lacked the closed entry, FENCE_PROBES.md, the proof and the result. Landed after the fact in 3 commits.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED: git diff --name-status c6d652a6dc^1 c6d652a6dc lists 2 paths (TO-EN-f-2, INVESTIGATION_v1.md). The branch changed 8 more against the merge base; one, check_en.py, was already equal on CLOUD. lgic-enforce-fence-probes.tf and the .open_deploys sentinel were PRESENT at c6d652a6dc and at HEAD, and absent at c6d652a6dc^2. The shared working tree showed them as unstaged deletions.",
        "CENSUS: all 55 merge commits by 2.0.0_SA_COO~G since 2026-09-14 12:00Z. A path counts as dropped when the merge's blob differs from the branch tip's while CLOUD's side left the path untouched. Result: 1 of 55 affected (c6d652a6dc), 6 paths.",
        "FOUND BY: 0.9.0_WK_LGIC_ENFORCE~1 in row W1-S20. EN-x-1's read-only plan from c6d652a6dc showed the 3 probe roles as creates.",
        "REMEDY: each of the 6 working-tree paths was byte-compared to the branch tip 1c66f3c806 (git hash-object --path: 6 of 6 MATCH), then landed. Ledger entry and sentinel deletion @5ee8e068fd; the probes .tf deletion @8c77a1400a (lane override CLOUD_OPS_OR_ETL, audited); FENCE_PROBES.md, the proof and the result @d482e58ecf (lane override TREE_DELIVERABLES, audited).",
        "LIVE PLANE UNCHANGED throughout: the fence is applied, and the 3 probe roles returned NoSuchEntity on the issuer's own read. The hazard was a CLOUD plan or apply re-creating them, not their existence."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "safe-merge.sh reports 'MERGED and committed' only after grading the merged index. The resulting commit is the merged tree.",
    "world_is": "safe-merge graded 8 staged paths and printed 'MERGED and committed -- c6d652a6dc', but the commit recorded 2. The issuer reported the drain on that line without reading the resulting tree. 1.0.0_SA_CTO's ADVI_FIRMBKTS ruling 97031 cited the drain; its evidence (the live policy, the probes) stands independently of the record.",
    "notes": "INERT once the 3 landing commits are in. Carried to 1.0.0_SA_CTO and 0.0.0_AB_MSTR. A merge's first-parent diff should be checked against the branch's own diff before a drain is called landed; this issuer now does so. The census method would show whether other seats' merges were truncated the same way. The writer that restores the index is still not identified (S17)."
  },
  {
    "id": "LGIC_ENFORCE-W1-S19",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T10:21Z",
    "one_line": "TO-EN-x-1 step 2 asks for 49financial's SHORT form to change in scopes.json and be regenerated. lib/opal_naming.py validate refuses any short that differs from org/standards/NAMING_SCHEMA.json firm_forms, which pins '49f', and generate refuses with it. NAMING_SCHEMA.json is outside the order's <paths>, so no 'after' commit can exist inside the grant and X1-AC3 cannot pass.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN 2026-09-15T~10:15Z on the practice copy (branch prac-lgic-enforce-x1 @104f092d69), after the change \"short\": \"49f\" -> \"short\": \"f49\" in infra/logic/registry/scopes.json (1 occurrence): 'python lib/opal_naming.py validate' printed \"REFUSED scopes.json[0].short: 'f49': NAMING_SCHEMA.json firm_forms gives '49f'\" and 'VALIDATE: REFUSED 1 refusal(s), 9 warning(s)', rc=1.",
        "RUN, same tree: 'python lib/opal_naming.py generate --out .scratch/gen_after' printed 'ERROR: the registry is refused (1 refusal(s)); run: python lib/opal_naming.py validate', rc=1. Nothing was generated.",
        "CODE: lib/opal_naming.py:248 @c6d652a6dc builds firm_forms from NAMING_SCHEMA.json, and :287-288 refuses a scopes.json row whose short differs: refuse(where, \"short\", \"%r: NAMING_SCHEMA.json firm_forms gives %r\" ...).",
        "FILE: org/standards/NAMING_SCHEMA.json:112-113 @c6d652a6dc: '\"firm_forms\": [' then '{\"key\": \"49financial\", \"short\": \"49f\"},'.",
        "ORDER: TO-EN-x-1 <paths> names 5 paths (lgic-enforce-fwd2-resource.tf, infra/logic/registry/scopes.json, infra/aws/terraform/modules/opal_name/, deliverables/EXERCISE_FWD2.md, the surprise channel); org/standards/NAMING_SCHEMA.json is not among them. The change was restored byte-for-byte, the practice copy removed clean, and the scratch branch left at 104f092d69."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-x-1 THE CELL step 2: 'In the same practice copy, change 49financial's SHORT form in scopes.json (for example 49f to f49) and regenerate. Commit it; that commit is after. The resource's name AND the fence's pattern for the firm must both move on that one change.' BOUNDS: 'A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.'",
    "world_is": "The firm short form is written in two places the generator reads: scopes.json and org/standards/NAMING_SCHEMA.json firm_forms. The validator that generate runs first refuses them disagreeing, so 'one change' to scopes.json cannot regenerate, and the exercise needs a second, ungranted change to NAMING_SCHEMA.json. On this order as cut, X1-AC3 reads FAIL-NOT-BOTH."
  },
  {
    "id": "LGIC_ENFORCE-W1-S20",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T10:21Z",
    "one_line": "CLOUD @c6d652a6dc still declares the three LGIC fence-probe roles and their three policies in infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf, which EN-f-2 removed from AWS. A read-only plan of shared-infra from that tree therefore creates 6 resources besides this cell's queue, and an apply of shared-infra from CLOUD would create them again.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN 2026-09-15T~10:10Z: terraform v1.9.8 plan -lock=false of infra/aws/terraform/shared-infra from the practice copy (base c6d652a6dc plus this cell's .tf), against the real S3 backend: 'Plan: 7 to add, 0 to change, 0 to destroy.' Creates: aws_iam_role.lgic_fence_probe[\"49f\"], [\"cot\"] and [\"unscoped\"]; aws_iam_role_policy.lgic_fence_probe_read[\"49f\"], [\"cot\"] and [\"unscoped\"]; aws_sqs_queue.lgic_enforce_fwd2. Plan JSON: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/fwd2_plan.json (239 resource_changes, 7 not no-op).",
        "RUN, check_en.py x1-plan on that JSON, 2026-09-15T~10:22Z, lists the planned create names 'mdpf-49f-fenceprobe-role', 'mdpf-cot-fenceprobe-role', 'mdpf-fenceprobe-role' and three 'fenceprobe-read-opal-data-49financial'.",
        "TREE: git ls-tree c6d652a6dc -- infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf returns blob 7622aae012; the file was last touched by 080e1b97c6 (EN-f-1, authored).",
        "WORLD, the shared tree C:/Users/AndrewBerman/Desktop/ajb_workspace at ~10:17Z: 'git status --porcelain -- infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf' prints ' D', a deletion that is neither staged nor committed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spawn note 1 from 2.0.0_SA_COO~G for TO-EN-x-1: 'EN-f-2 is complete and merged @c6d652a6dc. The fence as EN-f-2 left it is live, and it is at your base.' EN-f-2's removal criterion (check_en.py f2_removed) requires the three probe roles to be ABSENT in AWS.",
    "world_is": "The live plane has no probe roles, while the committed tree at the base still declares them. The removal exists only as an uncommitted deletion in the shared tree, so tree and state differ by 6 resources, and every shared-infra plan from CLOUD carries them until the deletion is committed."
  },
  {
    "id": "LGIC_ENFORCE-W1-S21",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T10:21Z",
    "one_line": "check_en.py x1-moves-both counts a NAME line as any added diff line carrying the new short form and the text 'role', and a FENCE line as any added line carrying it and '*'. The regenerated fence-pattern line in generated_locals.tf ('arn:aws:iam::313476888478:role/*-<short>-*') satisfies both, so X1-AC3 would read PASS-BOTH-MOVE on a diff in which only the fence pattern moved.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "CODE: check_en.py:1188 @c6d652a6dc 'name_lines = [ln for ln in out.splitlines() if ln.startswith(\"+\") and new_short and new_short in ln and \"role\" in ln]', and :1189 'fence_lines = [... new_short in ln and \"*\" in ln]'. One line may satisfy both filters.",
        "FILE: infra/aws/terraform/modules/opal_name/generated_locals.tf:66 @c6d652a6dc '\"49financial\" = [\"arn:aws:iam::313476888478:role/*-49f-*\"]' carries both 'role' and '*', and regenerates with the new short form.",
        "The order suggests an SQS queue, whose name the module computes at plan time. The name is in no committed file, so no before..after diff can carry it. A regenerated tests/vectors.json would add real 'role' names (for example mdpf-<short>-publisher-role), but those are the module's vectors, not this resource.",
        "NOT EXERCISED: no 'after' commit could be made (row LGIC_ENFORCE-W1-S19), so this is read from the code and the file, not from a run."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-x-1 X1-AC3: 'one change to the short form moves the resource's name and the fence pattern together.' THE CELL: 'The resource's name AND the fence's pattern for the firm must both move on that one change.'",
    "world_is": "The instrument's two filters are not disjoint, and the fence-pattern line alone satisfies both. The criterion therefore cannot tell a moved resource name from a moved fence pattern. A plan (or show -json) at 'after' would carry the resource's name; the committed diff does not."
  },
  {
    "id": "LGIC_ENFORCE-W1-S22",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T10:42Z",
    "one_line": "TO-EN-x-1 orders fwd2_plan.json, a terraform show -json, committed under the worker's deliverables folder. The commit-time naming gate graded 151 names in that machine output, 115 NAMING REFUSE (every one on fwd2_plan.json) and 13 NAMING RAISE, and passed the commit only because org/mcp/naming-gate.enforce is absent (WARN mode). With enforce on, the gate would refuse the deliverable the order names.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN: bash .tools/safe-commit.sh of commit d49089952b on branch wk-lgic-enforce-1-1-x1, 2026-09-15T~10:40Z. Its log (352 lines) prints '[naming-gate] NAMING-GATE: WARN 151 graded', with 115 'NAMING REFUSE' lines and 13 'NAMING RAISE' lines. All 115 REFUSE lines name org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/fwd2_plan.json:1, the one-line JSON.",
        "RUN, same log: 'NAMING REFUSE .../fwd2_plan.json:1 advi-49f-fwd2-exercise-queue -> advi-49f-fwd2-exercise-queue', why: \"CONFORMANT as SQS_QUEUE, but a NEW hand-kept carrier of '49f' outside every permitted context: read it through lookup('49financial')\". This is the cell's own resource, named by module opal_name.",
        "RUN, same log: live names read out of the plan's prior state are refused as NEW, e.g. '/aws/lambda/etf-ownership-dashboard -> /aws/lambda/{system}-etf-ownership-dashboard-lambda', why 'NEW and OUT-OF-PATTERN as LOG_GROUP: REFUSE', and 'arn:aws:dynamodb:us-east-1:313476888478:table/bd-securities -> lookup('49financial')'.",
        "WORLD: org/mcp/naming-gate.enforce is ABSENT in the worktree and not tracked at HEAD ('git ls-files --error-unmatch' says it does not match any file), so the stage ran in WARN mode and the commit landed."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-x-1 THE CELL step 1: 'Plan the REAL tree read-only (plan -lock=false -out, then show -json, against the real backend), and save the JSON as org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/fwd2_plan.json.' The slot branch carries the records.",
    "world_is": "The naming gate grades a generated terraform plan artifact as newly hand-written names and carriers, including this cell's own CONFORMANT, module-built queue name. It passes the commit only because enforce is off. Nothing exempts a plan JSON deliverable from the stage, so once enforce is on, this order's own deliverable, and EN-f-1's fence_plan.json of the same kind, could not be committed as ordered."
  },
  {
    "id": "LGIC_ENFORCE-S19",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "4.0.0_SA_CRO",
    "surfaced_at": "2026-09-15T17:58Z",
    "one_line": "At NAMING_SCHEMA v1.9 (@645725150b, branch lgic-v19-landing) firm_forms is removed and the schema names the identity registry as the one carrier of firm forms, while the registry's own row_fields text (scopes.json:4) still says 'NAMING_SCHEMA.json firm_forms owns which firm short forms exist', so each carrier names the other as the owner.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "SCHEMA: org/standards/NAMING_SCHEMA.json@645725150b, parsed: key firm_forms absent; firm_forms_source reads 'A firm's forms (its key and its one sanctioned short form) are the identity registry's rows, infra/logic/registry/scopes.json, and every reader reads them there; this file carries no copy'.",
        "REGISTRY: infra/logic/registry/scopes.json@645725150b :4 _about.row_fields 'short (NAMING_SCHEMA.json firm_forms owns which firm short forms exist)'; :210 the demo note cites '(NAMING_SCHEMA.json firm_forms)'. Both lines are byte-identical to 2f554182b6, where the field still existed.",
        "ANALYSIS: org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md@7b5331c8c0 s.2 RULING ONE names the readers to repoint as lib/opal_naming.py :248, :287-288, validate and grade(). The registry's row_fields text is not in that list. RULING DEMO corrects the :210 note.",
        "CODE, read and NOT exercised: lib/opal_naming.py@645725150b :248 reads schema['firm_forms']; :287-290, :347 and :381 use it. The NAMING_SCHEMA v1.9 changelog says the readers land with EN-r-3 on the same branch, before one merge to CLOUD."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "RULING ONE (@7b5331c8c0 s.2): 'The identity registry (infra/logic/registry/scopes.json) is the ONE home of a firm's forms. The schema's firm_forms is removed, and every reader reads the registry.' NAMING_SCHEMA v1.9 firm_forms_source: 'this file carries no copy'.",
    "world_is": "At the pin the registry's own documentation defers the short form's authority to a schema key that no longer exists, and lib/opal_naming.py:248 still reads that key. The code is scheduled (EN-r-3); the row_fields text is not named by the ruling. INERT: the branch is not in CLOUD, and no write, deploy or served key reads this text.",
    "notes": "Surfaced by 4.0.0_SA_CRO during the LGIC_NAMING v1.9 L4-R, which it signed (review docs/briefs/sources/LGIC_NAMING_L4_BRIEF_REVIEW_v1_9_20260915.md); this is not a ground there. For round 2's one-carrier cell: repoint the row_fields text together with the readers."
  },
  {
    "id": "LGIC_ENFORCE-W6-S2",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~6",
    "surfaced_at": "2026-09-15T20:43Z",
    "one_line": "EN-r-5's named invocation, git apply of the worktree's copy of fixed_inputs/r2/gateway_whole.patch, returned rc=1 and refused 7 of 12 paths. The checkout copy is CRLF, and the 7 refused targets are eol=lf files. The committed blob of the same patch (LF, fd3b303d56) applied 12 of 12, so it was applied as is and not re-made by hand.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN in wk-lgic-enforce-2-6 @671925aecc: git apply --check --verbose org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/gateway_whole.patch -> 'error: patch failed: .tools/ds-precommit-check.py:65' ... 'error: lib/opal_naming.py: patch does not apply'; 7 refused: .tools/ds-precommit-check.py, directory_runner.py, holdings_snapshot.py, perfrp_firm_pin.py, loaders.py, generated_locals.tf, lib/opal_naming.py; rc=1. Each refused hunk shows '?' (CR) at every line end.",
        "EOL at 671925aecc (git ls-files --eol): the patch 'i/lf w/crlf attr/' (core.autocrlf=true, no eol attribute); the 7 refused targets 'i/lf w/lf attr/text eol=lf'; the 5 accepted targets (systems.json, GRADING_RULE.md, firm_registry.json, firm-config.mjs, vectors.json) 'i/lf w/crlf attr/'. The checkout copy is 18392 bytes; the blob is 18127 bytes.",
        "RUN: git show HEAD:<the patch> > .scratch/gateway_whole.lf.patch; git hash-object of it = fd3b303d5679d4ed6d681836b6db86cec9e3d4b0 = git rev-parse HEAD:<the patch>. git apply --check rc=0 on 12 of 12; git apply 'Applied patch ... cleanly' 12 of 12.",
        "RUN after the apply: python lib/opal_naming.py generate --out . -> 'GENERATE: 9 written, 0 skipped, into . at registry@0f9240483015d802'; git diff before and after the generate byte-identical (cmp). Committed at c19dcc8147, 12 files, 38 insertions, 29 deletions, the patch's own --stat."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-5-r2 THE CELL: 'In your worktree, run `git apply <that path>`. If it no longer applies, re-make its four parts by hand from the patch's own text, and never widen it'. SPAWN NOTES: 'apply YOUR worktree's copy (`git -C <WS> apply --check` first)'.",
    "world_is": "The worktree's copy, read by path, is the patch with a CR on every line, and git apply refuses its hunks against LF working files. The patch's own text still applies whole: the committed blob, byte-identical by hash to what the issuer committed, applied 12 of 12 with no hand edit and no widening. The failure comes from the checkout's line endings, not from drift in the target files.",
    "notes": "Form only. Neither branch the order names fits. The patch does apply, but not from the path the order names. It was applied from its blob, not re-made by hand, because the blob IS 'the patch's own text' and a hand re-make adds a transcription step. Any fixed-input .patch read by path from a checkout on this box (autocrlf, no *.patch eol attribute) meets the same refusal. INERT: this order is the patch's only consumer, and it is spent once applied."
  },
  {
    "id": "LGIC_ENFORCE-S20",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T21:30Z",
    "one_line": "check_en_r2.py's spawn_base() is `git merge-base HEAD CLOUD`, a reference that moves at the drain. Every criterion that diffs against it reads 0 changed lines once the cell is on CLOUD, so it cannot be re-graded after a drain. EN-r-5's R5-AC7 read FAIL-R5-WORKED-CASES on a separate checkout at the merge @6e3a01b939, and in the worker's own worktree after the drain, although the worker's pre-drain run read PASS and the change is on CLOUD.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN on .worktrees/wk-lgic-canon-1-8, detached @6e3a01b939 (CLOUD after the EN-r-5 drain): check_en_r2.py r5-worked-case -> 'LINES CHANGED IN GRADING_RULE.md SINCE THE BASE: 0 (every one the opal-gateway case: False)', 'THE CASE NOW: {\"name\": \"opal-gateway\", ... \"canonical_form\": \"gateway-lb\" ...', 'VERDICT: FAIL-R5-WORKED-CASES'. On the same checkout, r5-validate, r5-generate, r5-tests, r5-address, r5-name and r5-sharepoint read PASS.",
        "RUN in .worktrees/wk-lgic-enforce-2-6 (the worker's branch, tip 6eedbc3ddc, now an ancestor of CLOUD): the same subcommand -> 'VERDICT: FAIL-R5-WORKED-CASES'. The worker's pre-drain report read 'PASS-R5-ONE-WORKED-CASE-MOVED (2 lines changed, every one the opal-gateway case)'.",
        "READ check_en_r2.py r5_worked_case: 'base = spawn_base()' then 'git diff -U0 base -- GRADING_RULE'. Its failure text names spawn_base's source, 'git merge-base HEAD CLOUD failed'. The spawn_base() callers are at :277, :346, :538, :1014 and :1555 (5 call sites).",
        "Different instrument, RUN on the primary checkout: 'git diff --numstat 671925aecc 6e3a01b939 -- org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md' -> '1 1'. The - and + lines are both the opal-gateway LOAD_BALANCER case, canonical_form opal-gateway-lb -> gateway-lb. 'git log 671925aecc..6e3a01b939 -- GRADING_RULE.md' lists one commit, c19dcc8147 (EN-r-5)."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-5-r2 R5-AC7: 'only the `opal-gateway` worked case of `GRADING_RULE.md` moves, and it reads canonical `gateway-lb`', expect 'VERDICT: PASS-R5-ONE-WORKED-CASE-MOVED'. The COO's drain discipline re-runs every criterion on a checkout other than the worker's own, after the merge.",
    "world_is": "Once the cell's commits are ancestors of CLOUD, merge-base HEAD CLOUD is the cell's own tip (or later), so the diff the criterion counts is empty. The criterion then FAILs on every checkout, the worker's included, while the moved case is on CLOUD. The substance holds by the direct diff from the order's spawn base 671925aecc. The check's base, not the cell, is what differs.",
    "notes": "Issuer's own defect: check_en_r2.py is a fixed input authored by 2.0.0_SA_COO~G. INERT: EN-r-5 is verified by the direct diff and the worker's pre-drain run, and nothing reads the post-drain verdict. For round 2's analysis: pin each spawn_base() caller to the order's issuance base (671925aecc for round 2), or read the base from the worker's result file. Not yet measured: whether check_ln_r4.py and check_canon_r1.py read merge-base HEAD CLOUD the same way."
  },
  {
    "id": "LGIC_ENFORCE-S21",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-15T23:58Z",
    "one_line": "EN-r-3's R3-AC1 and R3-AC9 read PASS in the worker's own worktree and FAIL on the group branch after a SECOND cell landed beside it. The two criteria census the WORKING TREE with git grep, so LN-g-1's own proof instance and result file -- which quote the token because the re-cut rule's item 5 names firm_forms -- appear as unrecorded readers that EN-r-3's record could not list, because they did not exist when its census was written. The cell's own claim holds: lib/opal_naming.py no longer names firm_forms.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "RUN in .worktrees/wk-lgic-enforce-2-1 (the worker's own branch tip 3c42177812): check_en_r2.py r3-one-carrier -> 'UNSCOPED: 35216 tracked file(s) scanned (git ls-files); naming firm_forms besides lib/opal_naming.py: 57 ...' and 'VERDICT: PASS-ONE-CARRIER'; r3-reader-census -> 'VERDICT: PASS-READERS-CENSUSED'.",
        "RUN in .worktrees/wk-lgic-canon-1-9 (branch lgic-v19-group @10fe5d037c, after LN-g-1 @9f18dc922a and then EN-r-3 merged): the same two subcommands -> 'VERDICT: FAIL-TWO-CARRIERS' and 'VERDICT: FAIL-READER-CENSUS'. The other 7 mechanical criteria read PASS on that same tip, and the first-parent tree check read 10 of 10.",
        "MEASURED on the group tip, with the record parsed rather than grepped: 59 tracked files name firm_forms; FIRM_FORMS_READERS.md lists 57; the UNLISTED set is exactly 2, both LGIC_NAMING's and both authored by LN-g-1's worker -- deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-g-1-r4.grading-rule.proof_of_spec.json and deliverables/0.9.0_WK_LGIC_NAMING~3/grading-rule.r4.result.md. 'lib/opal_naming.py still names it: False'.",
        "READ check_en_r2.py: r3_one_carrier runs git ls-files and git grep -l firm_forms, and r3_reader_census runs git grep -l at HEAD and at spawn_base(). Both are worktree-scoped, so each grades the tree it runs in; neither is rooted at another checkout."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-3-r2 R3-AC1: 'a census (97200): 0 reads of firm_forms remain ... every other tracked file an unscoped search finds naming it is a recorded non-reader'. R3-AC9: 'every file that named firm_forms at the base carries a disposition, and none marked repointed still names it'.",
    "world_is": "Both criteria are written against ONE cell's tree and are graded again on the UNION the group branch makes. A record that is complete when its cell drains goes stale the moment a sibling cell lands a file that mentions the token, even a record file that only quotes a checker's output. The order was flipped complete on its own worktree's PASS, which was true there.",
    "notes": "ARMED, disarm owner 2.0.0_SA_COO~G: it disarms when FIRM_FORMS_READERS.md lists the two LGIC_NAMING records as 'another-project' -- a one-line record edit, not a re-cut, and NOT done tonight under the managed wind-down (Andrew ~23:3xZ via 0.0.0_AB_MSTR 97267). For 3.0.0_SA_CVO at L9: read EN-r-3's verdicts at the worker's tip 3c42177812, where the 10 mechanical criteria PASS, and read this row for the group-tree reading. The same class will meet any later cell whose criterion censuses the whole tree while a group branch stages several cells at once."
  },
  {
    "id": "LGIC_ENFORCE-W1-S23",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T23:16Z",
    "one_line": "LGIC_NAMING round 3's fixed inputs read NAMING_SCHEMA.json firm_forms, which v1.9 removed on this branch: blind_seat.py indexes s[\"firm_forms\"] (a KeyError under v1.9) and check_ln_r3.py reads s.get(\"firm_forms\", []) (a silently empty scope set), and the three r3 seat prompts carry a snapshot of the schema list and of the scopes.json fields bucket_basis and the demo note that this cell removes.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/blind_seat.py:109 @bd0f5d2c6c: 'return lines + \"\\\\nThe firm spellings, long and short (firm_forms):\\\\n\" + json.dumps(s[\"firm_forms\"], indent=1, ensure_ascii=True)' -- a direct index, so a KeyError on a schema with no firm_forms key.",
        "READ org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py:281 @bd0f5d2c6c: 'scopes = set(f[\"short\"] for f in s.get(\"firm_forms\", [])) | {s.get(\"global_scope\", {}).get(\"short\", \"global\")}' -- the default [] makes the firm half of that set empty, with no error.",
        "READ org/standards/NAMING_SCHEMA.json @bd0f5d2c6c: the top-level keys carry firm_forms_source and no firm_forms ('python lib/opal_naming.py validate' at this tip reads 0 refusals; the v1.9 removal is 1.0.0_SA_CTO's commit 645725150b, 'NAMING_SCHEMA v1.9 on lgic-v19-landing -- firm_forms removed').",
        "READ org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e1.prompt.txt:120, :168, :374, :393 @bd0f5d2c6c (e2.prompt.txt at the same four lines; e4.prompt.txt at :13, :38, :244, :263): each prompt embeds '\"firm_forms\": [', scopes.json's _about.row_fields naming it, the demo note naming it, and the bucket_basis field, all as the seat's given text.",
        "WORLD: this cell removes bucket_basis and rewrites _about.row_fields and the demo note in infra/logic/registry/scopes.json (DEC-1, RULING DEMO), so the prompts' snapshot is a vintage the registry no longer matches once this branch drains."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-3-r2 THE CELL item 5: 'LGIC_NAMING's round-3 fixed inputs read it for their seats: row that for the issuer, and do not edit them.' BOUNDS: 'Fixed inputs are read-only.'",
    "world_is": "Two of LGIC_NAMING round 3's instruments read the removed field as CODE, not as text: one raises, one degrades silently to an empty firm set. Neither is in this order's paths and neither is edited here. The three seat prompts additionally carry a registry snapshot this cell moves.",
    "notes": "Filed for the issuer, 2.0.0_SA_COO~G, which owns both projects' fixed inputs. ARMED because LGIC_NAMING's LN-g-1 runs in parallel from the same v1.9 base: an r3 instrument run against this schema meets the KeyError or the empty set. Not a claim about LGIC_NAMING's round; only about what these files read."
  },
  {
    "id": "LGIC_ENFORCE-W1-S24",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T23:16Z",
    "one_line": "LGIC_CANON's carriers still present NAMING_SCHEMA.json firm_forms as live: 10_ONBOARDING_CHECKLIST.md tells a seat to APPEND a new firm to the schema list and quotes the validate warning this cell removes, 02_DOCTRINE.md's generated naming section is stamped v1.8 and says the forms are read from the list, and check_canon_r1.py iterates s.get(\"firm_forms\").",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ infra/logic/10_ONBOARDING_CHECKLIST.md:72, :75, :77 @bd0f5d2c6c: 'builder: `org/standards/NAMING_SCHEMA.json` (`firm_forms`)'; \"`WARN scopes.json[<i>].key: firm '<LONG>' is not in NAMING_SCHEMA.json firm_forms`. This is the line\"; '- **If the line is printed:** append `{\"key\": \"<LONG>\", \"short\": \"<SHORT>\"}` to `firm_forms` in'. That WARN is the warning this cell removes from validate.",
        "READ infra/logic/02_DOCTRINE.md:163 and :190 @bd0f5d2c6c: 'stamp: org/standards/NAMING_SCHEMA.json v1.8 sha256:4ff4e61930b3c8cdcd767ba660e32d0e37e527196a340cec3c94e27f1dd9b8c0' and 'Firm forms read from `firm_forms` in the schema: 4 firms.' -- inside the GENERATED naming section markers.",
        "READ infra/logic/render_naming_section.py:98-107 @bd0f5d2c6c: 'forms = schema.get(\"firm_forms\")' returns '`firm_forms` in the schema' while the field exists, and otherwise the FIRM rows of the scope registry, so a re-render under v1.9 takes the registry branch with no code edit.",
        "READ org/missions/D14/LGIC/LGIC_CANON/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_canon_r1.py:226 @bd0f5d2c6c: 'for f in s.get(\"firm_forms\") or []:' -- LGIC_CANON round 1's issuer instrument, empty under v1.9.",
        "RUN: python lib/opal_naming.py validate at this worktree reads 'VALIDATE: OK 17 system row(s), 9 scope row(s), 9 warning(s)', all nine the inferred-owner warning; no firm-forms warning can be printed any more."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-3-r2 THE CELL item 5: 'A file you did not repoint that still names it is a historical record (a round's record, a review, an adjudication) or another project's.' The order's <paths> do not admit infra/logic/ outside the registry.",
    "world_is": "Three LGIC_CANON carriers outside this order's paths still teach the removed field. The checklist is the sharp one: followed as written, it re-adds firm_forms to NAMING_SCHEMA.json and so re-creates the second carrier RULING ONE removed; the warning it tells the seat to wait for can no longer print. The doctrine's line is generated and moves on a re-render of render_naming_section.py.",
    "notes": "Filed, not fixed: infra/logic/10_ONBOARDING_CHECKLIST.md, infra/logic/02_DOCTRINE.md and infra/logic/render_naming_section.py are outside this order's <paths>, and a path this order does not name is a row, never an override. Each is recorded 'another-project' in FIRM_FORMS_READERS.md."
  },
  {
    "id": "LGIC_ENFORCE-W1-S25",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-15T23:16Z",
    "one_line": "DEC-1 (remove any scope-row field nothing reads) and RULING DEMO (demo's note must cite X6) meet on the field 'note', which no generator and no validate limb read: to keep both, validate now READS note, refusing one that is present and not a non-empty string. The order names neither the read nor the removal of note.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ infra/logic/registry/scopes.json @bd0f5d2c6c: 'note' appears on the demo scope row only; the other 'note' the module reads is the GLOBAL row's tenant.note (lib/opal_naming.py _firm_registry_rows), a different field.",
        "RUN at this worktree: 'python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-dec1-fields' on the pre-edit tree printed 'SCOPE-ROW FIELDS: 18  NAMED BY NO STRING IN lib/opal_naming.py: ['bucket_basis', 'label']' -- the checker's instrument is a string-constant census, so it never saw 'note', which the module names for a different row's tenant block.",
        "WORLD: lib/opal_naming.py validate() now carries 'if \"note\" in row and (not isinstance(row[\"note\"], str) or not row[\"note\"]): refuse(where, \"note\", ...)', and scopes.json _about.row_fields lists note among the fields carried only where validate or a generator reads it."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-EN-r-3-r2 THE CELL item 3: 'a scope row carries the REQUIRED fields `validate` names, and a further field only if a generator or `validate` reads it. Remove any field nothing reads (row W1-S8).' Item 4: 'Demo's note no longer says the doctrine does not define the class; it cites X6.'",
    "world_is": "The two items are jointly satisfiable only by making note read or by deleting a field the same order requires content in. The read was added rather than the field removed. bucket_basis (global) and label (both MASTER rows), which nothing reads, were removed as the order says.",
    "notes": "Form only: the choice is recorded here because the order does not name it, and R3-J1 grades at L9 whether DEC-1's required list is the one validate enforces. INERT: nothing is left armed either way."
  },
  {
    "id": "LGIC_ENFORCE-W3-S10",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-16T00:20Z",
    "one_line": "G1R-AC1's own fixture, tests/g1r/01_plan_json_added.patch, is a corrupt unified diff (hunk header declares 13 added lines, body carries 12): the stated invocation reads VERDICT: FAIL-PLAN-FILE-GRADED against BOTH the pre-edit and the edited .tools/naming-gate.py, and git apply --check independently refuses the same bytes.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/tests/g1r/01_plan_json_added.patch @3ee4bb55ec93f2ecd136a2760908d648cf868473: the hunk header reads '@@ -0,0 +1,13 @@' while the body between it and EOF carries exactly 12 '+'-prefixed content lines (enumerated by splitting the CRLF-normalized text on newlines), a declared-vs-actual count mismatch of 1.",
        "RUN 'git apply --check org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/tests/g1r/01_plan_json_added.patch' at this worktree (3ee4bb55ec93f2ecd136a2760908d648cf868473): 'error: corrupt patch at ...:18', rc=128 -- git's own parser rejects the same bytes, independent of naming-gate.py.",
        "RUN the pre-edit commit limb (git show HEAD:.tools/naming-gate.py, saved to .scratch/naming-gate-orig.py, unmodified) --diff <same fixture> --enforce: 'NAMING ERROR not a unified diff: the hunk at diff line 4 ends early (0/0 old, 12/13 new)', rc=1 -- the corruption predates and is independent of this cell's edit.",
        "RUN the acceptance invocation exactly as named: cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py g1r-plan-not-graded -> 'MACHINE-WRITTEN PLAN FILE ADDED: rc=1  NAMING ERROR not a unified diff: ...' and 'VERDICT: FAIL-PLAN-FILE-GRADED' on the edited gate -- G1R-AC1 cannot read PASS through this fixture.",
        "RUN a header-corrected copy of the identical bytes in .scratch/ (only '@@ -0,0 +1,13 @@' changed to '@@ -0,0 +1,12 @@'): 'git apply --check' rc=0 (applies cleanly); the EDITED .tools/naming-gate.py --diff <corrected copy> --enforce prints 'NAMING SKIP .../fixture_plan.r2.json:1 <machine-written plan file> -> -' then 'NAMING-GATE: PASS 1 graded', rc=0, while the untouched control 02_authored_json_added.patch still prints 'NAMING REFUSE ...queues.json:2 mdpf-cottonwood-publisher-queue -> mdpf-cot-publisher-queue', rc=1 -- the cell's SKIP logic is correct; only the fixture's hunk-header count is wrong."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "G1R-AC1 names invocation 'cd <WS> && timeout 120 python .../check_en_r2.py g1r-plan-not-graded', expecting 'VERDICT: PASS-PLAN-FILE-NOT-GRADED'. THE CELL, item 1: 'A JSON file whose top level carries format_version, terraform_version, and resource_changes or planned_values ... is skipped, and the limb prints that it skipped it.' BOUNDS: 'Fixed inputs are read-only ... Never edit any of them.'",
    "world_is": "The fixture the criterion names to prove itself against is a corrupt unified diff: its hunk header overcounts the added lines by 1, so both the pre-edit and the edited naming-gate.py's own parse_diff() -- and real git via 'git apply --check' -- refuse it as unparseable, before the SKIP-a-plan-file logic this cell adds ever runs. The stated invocation therefore reads FAIL-PLAN-FILE-GRADED regardless of the commit limb's correctness. A byte-identical, header-corrected copy run outside the fixed-input path (a scratch file, never committed) confirms the edited gate's behavior matches the cell exactly: the plan file is SKIPped and the authored-JSON control is still REFUSEd with its canonical form.",
    "notes": "BLOCKING because G1R-AC1's named invocation cannot reach PASS while this fixture stands, through no defect in .tools/naming-gate.py. Filed for the issuer, 2.0.0_SA_COO~G, which owns fixed_inputs/r2/; the fixture is outside this order's <paths> and a path this order does not name is a row, never an override. Disarms with a one-line header fix (@@ -0,0 +1,12 @@) or a 13th content line, re-cut by the issuer. The proof-of-spec instance for G1R-AC1 records this row's id and the FAIL-by-output verdict the named invocation actually produced."
  },
  {
    "id": "LGIC_ENFORCE-W3-S11",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-16T01:10Z",
    "one_line": "W3-S10 disposed: 2.0.0_SA_COO~G corrected tests/g1r/01_plan_json_added.patch's hunk header (+1,13 -> +1,12, zero other bytes changed, all 17 CRLF endings intact) at 6f640ead30, drained to CLOUD at 4f7f050f2c; G1R-AC1 now reads VERDICT: PASS-PLAN-FILE-NOT-GRADED, rc=0, re-run in this worktree with the corrected fixture.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "READ org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/tests/g1r/01_plan_json_added.patch in this worktree (post-fix, uncommitted per the coordinator's resume message) against the blob at 6f640ead30 (git show 6f640ead30:<path>): the two differ only by CRLF rendering (0 CRLF in the stored blob, 17 in the checked-out copy); byte content is identical once normalized to LF -- an independent instrument, not a re-statement of the coordinator's own diff.",
        "RUN git diff HEAD -- <path> in this worktree: the only hunk changes '@@ -0,0 +1,13 @@' to '@@ -0,0 +1,12 @@'; no other line differs.",
        "RUN git merge-base --is-ancestor 7bdcbfb325 4f7f050f2c -> true (this worker's drained commit is an ancestor of the drain tip); git merge-base --is-ancestor 6f640ead30 4f7f050f2c -> true (the fixture fix is included in the drain tip).",
        "RUN the acceptance invocation exactly as named, in this worktree with the corrected fixture: cd <WS> && timeout 120 python .../check_en_r2.py g1r-plan-not-graded -> 'MACHINE-WRITTEN PLAN FILE ADDED: rc=0 ... NAMING-GATE: PASS 1 graded' and 'CONTROL, THE SAME NAME IN AN AUTHORED JSON FILE: rc=1 ... NAMING-GATE: REFUSE 1 graded', 'VERDICT: PASS-PLAN-FILE-NOT-GRADED', rc=0. G1R-AC2, G1R-AC3 and G1R-AC4 re-run unchanged: PASS-REGISTRY-VALIDATED-FIRST, PASS-COMMIT-LIMB-READS-SCHEMA-MAP, PASS-G1-SUITE-HOLDS."
      ]
    },
    "disposition": "GRADUATED",
    "adjudicates": ["LGIC_ENFORCE-W3-S10"],
    "spec_asserts": "The coordinator's resume message (2.0.0_SA_COO~G): 'You were right, and the fixture was the defect ... It is corrected +1,13 -> +1,12, zero other bytes changed, all 17 CRLF endings intact, committed as 6f640ead30 ... Append ONE row to the channel disposing W3-S10: it was a real BLOCKING finding, the cause was the issuer's fixture, the remedy has landed, and the criterion now passes.'",
    "world_is": "Independently confirmed rather than taken on the message's word: the fixture blob at 6f640ead30 matches the worktree copy byte-for-byte after CRLF normalization, both this worker's commit and the fixture fix are ancestors of the drain tip 4f7f050f2c, and re-running G1R-AC1's exact named invocation in this worktree now prints VERDICT: PASS-PLAN-FILE-NOT-GRADED, rc=0, with the plan file SKIPped and the authored-JSON control still REFUSEd. W3-S10 was a real BLOCKING finding (independently reproduced on the pre-edit gate and on git apply --check, per that row); its root cause was the fixed input, not .tools/naming-gate.py, and the remedy is landed and verified.",
    "notes": "Disposes LGIC_ENFORCE-W3-S10 (this row's adjudicates). hazard_standing INERT: the fixture defect is remedied and G1R-AC1 now passes by output; no owner needs to hold it further. The proof-of-spec instance for G1R-AC1 is updated to record the PASS and pinned to 6f640ead30 for the fixture, never PENDING-THIS-COMMIT."
  },
  {
    "id": "LGIC_ENFORCE-W1-S26",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-16T03:10Z",
    "one_line": "B2 (a bucket's scope) and K1 (an S3Key's segment 1) accept ONLY a V1 (system) token -- refused_keys (V3) membership resolves neither, so a class (b) registry addition cannot silence a K1 or B2 raise, only an R1.f/R1.c/R1.d/R2 one.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED: in a scratch copy of lib/opal_naming.py + infra/logic/registry with 'pm' added to systems.json refused_keys.generic_noun, grade('opal-data-pm', 'S3_BUCKET') still raises \"B2: 'pm' after opal-data- is no scope key\".",
        "EXERCISED: the same scratch addition of 'sentiment' leaves grade('sentiment/keyword-sentiments.json', 'S3Key') still raising \"K1: segment 1 'sentiment' is neither a source nor a tier\".",
        "MEASURED at HEAD, no scratch needed: fixed_inputs/r2/RAISE_POPULATION.json's ec2 and infrastructure groups -- BOTH already members of systems.json refused_keys.generic_noun before this cell ran -- each still carry a K1 example (S3Key ec2/astn-wsjft/deploy.sh; S3Key infrastructure/reports/) in this same population."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE.TO-EN-r-2-r2 THE CELL step 2, read plainly: 'Make each class (b) and (c) token one the registry recognizes, so the rule places it (the registry's refused_keys, or the list the rule reads for that class)' -- implying refused_keys membership places (resolves) any V3-classed token uniformly.",
    "world_is": "refused_keys resolves only R1.f/R1.c/R1.d/R2 (resource-grammar) raises. A token whose raise is K1 or B2 stays RAISING after a refused_keys addition, because those two clauses test membership in V1 specifically, never V3. 50 of the 152 population groups carry a K1/B2/R8/L2/G2.3 example; this cell classes each (d) or undecided rather than (b)/(c) unless every one of the group's examples independently resolves, and R2-AC4's per-example re-grade (0 of 378 still raising) is the mechanism that would have caught a wrong call here.",
    "notes": "Form only, no remedy owed: this cell's own classification already routes around the boundary (every B2/K1/R8/L2/G2.3-bearing group is class (d) or undecided), and R2-AC4 mechanically catches a future misclassification of the same shape on a later round. Filed because the decomposition's and the worker face's plain language does not state this boundary, and a reader taking 'the registry's refused_keys' at face value could misclassify a B2/K1-bearing token as (b) and have it silently fail AC4, or -- worse, if AC4 is ever loosened -- pass while still raising in the served naming-gate output."
  },
  {
    "id": "LGIC_ENFORCE-W1-S27",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-16T05:40Z",
    "one_line": "2 of RESOURCE_GAPS.json's 48 {system}-gap names (bd-merge-daily-lambda-role, bd-pipeline-task-role) have NO aws_iam_role (or any resource) declared anywhere under infra/aws/terraform/ at this base -- they are LIVE-only names the fixed population carries with no repo-side owner to cite.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "native Grep (recursive, repo-corpus) over infra/aws/terraform for 'bd-merge-daily-lambda-role', 'bd-pipeline-task-role', 'merge_daily', 'pipeline_task' at CLOUD @68644b3c19: 0 hit(s) for every pattern -- no resource label, no name/name= literal, no comment names either string anywhere the naming system reads.",
        "org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md@619dec559f lines 228-235 lists both names with only {name, canonical}, no file/line/evidence field -- its own source is org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/LIVE_NAMES.json, 'Built from the estate as of 2026-09-14 12:13:53 UTC' (a LIVE AWS census, not a Terraform read), so the population's OWN provenance for these two names is live-plane, not repo-plane.",
        "org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md (a full Terraform-label census of infra/aws/terraform at an earlier base, @fd9c9ca174) also carries 0 hits for either string, corroborating on an independent instrument (a different census, a different vintage) rather than repeating the same comp-find."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "LGIC_ENFORCE.TO-EN-r-4-r2 THE CELL item 4: 'A resource no owner can be named for gets NO row. It keeps its placeholder and is counted, never guessed.' The population's own _about field describes the 48 as resources 'whose canonical form carries {system} at the cut', implying each is a resource the naming system can locate and reason about.",
    "world_is": "Handled per the cell's own rule (both names are counted as placeholders in RESOURCE_ROWS.md with this absence as their reason, never guessed), so this is not a defect in this cell's output -- it is a gap in RESOURCE_GAPS.json's population itself: 2 of 48 fixed-input rows name a resource this worktree's Terraform tree cannot locate at all, so no Terraform-plane evidence can ever be cited for them, only a live-plane one (out of this cell's read surface, and RESOURCE_GAPS.json is a read-only fixed input this cell does not edit).",
    "notes": "Form only, no remedy owed here: the two placeholders are correctly counted, not guessed, and R4-AC10's gaps-covered check passes on them as counted-with-a-reason. Filed because a future round that tries to row these two from the repo alone will hit the same 0-hit absence, and the reason (LIVE-only provenance, not a missing citation on this seat's part) is not otherwise recorded anywhere the naming system reads."
  },
  {
   "id": "LGIC_ENFORCE-S22",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T09:35Z",
   "one_line": "EN-t-3 AS CUT CANNOT RUN ON THIS BOX: it orders terraform init on 73 Terraform roots and never says to clean up, and ONE initialised root costs 686 MB of AWS provider on this filesystem -- about 50 GB against 19 GB free. Caught at the pre-spawn read, before a worker filled the disk under four live siblings.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE ORDER: TO-EN-t-3-r2 item 1 says 'A root is a directory under infra/aws/terraform/ whose tracked .tf files declare a backend block; the checker enumerates them from git ls-files, 73 at the cut' and orders 'terraform init from the plugin cache, then a read-only plan, then show -json' for EACH one. Item 2 adds the pre-plan limb over all 78 Terraform directories. Nothing in the cell removes a root's .terraform afterwards.",
     "THE UNIT COST, measured on the one root already initialised in the main checkout: du -sh infra/aws/terraform/portal-auth/.terraform reads 686M, and the breakdown is 686M in .terraform/providers with 4.0K of state -- the whole of it is providers/registry.terraform.io/hashicorp/aws.",
     "IT IS A REAL COPY, NOT A LINK, which is the crux: TF_PLUGIN_CACHE_DIR IS set on this box (C:\\Users\\AndrewBerman\\.terraform.d\\plugin-cache, 722M) and the cache is populated, yet ls -la of the root's providers directory shows an ordinary directory tree. On this filesystem the plugin cache does not spare the per-root footprint, so the cache's existence is NOT mitigation.",
     "THE ARITHMETIC: 73 roots x 686 MB is roughly 50 GB. df -h /c reads 19 GB free at the time of this row, with three LGIC_CANON workers and one LGIC_ENFORCE worker live, each holding a 1.5 GB worktree.",
     "THE BLAST RADIUS IS NOT THE CELL. Filling this volume takes down every live worker, the other seats sharing the box and the shared index, not just EN-t-3 -- and a worker has no way to know it is the one that did it. That is why this is BLOCKING rather than an observation.",
     "NEGATIVE CONTROL on the claim that this is about THIS cell rather than terraform generally: EN-t-2, the sibling that just drained at abd07c7ef3, ran every criterion against fixtures under fixed_inputs/r2/tests/t2r/ and a stub terraform, initialised nothing, and cost nothing. The exposure is specific to EN-t-3's real-roots sweep."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "TO-EN-t-3-r2: plan every one of the 73 backend-declaring roots with terraform init + plan + show -json, keeping a small JSON extract per root.",
   "world_is": "The extracts are small, but the intermediate state each one requires is not: a single initialised root materialises 686 MB of AWS provider on this filesystem, and the cell orders 73 of them with no instruction to release any. As cut, the cell's peak disk demand exceeds this box's free space by roughly a factor of two and a half.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. The remedy is the issuer's and is bounded: correct the cell's own instruction, BEFORE any spawn, to work one root at a time and remove that root's .terraform once show -json has been captured -- which caps the footprint at about one root rather than 73 and leaves every deliverable, criterion and <paths> entry untouched. Disarms when that correction is committed and the cell is spawned against it. NOT a licence to skip roots: a root that cannot be planned is still recorded NOT planned with its reason, exactly as the cell already says."
  },
  {
   "id": "LGIC_ENFORCE-S23",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T09:38Z",
   "one_line": "THE WRITE-SURFACE DISJOINTNESS CENSUS I RUN AT EVERY ISSUANCE CANNOT SEE AN INSTRUMENT DEPENDENCY: EN-s-1 and EN-r-6 have disjoint <paths> and read as safe to run together, but EN-s-1's census RUNS lib/opal_naming.py and EN-r-6 WRITES it.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE TWO WRITE SURFACES ARE GENUINELY DISJOINT. EN-s-1 <paths>: NAMING_CENSUS_REPORT.md and the channel. EN-r-6 <paths>: lib/opal_naming.py, lib/tests/test_opal_naming.py, data/firm_registry.json, firm-config.mjs, directory_runner.py, holdings_snapshot.py, loaders.py, perfrp_firm_pin.py, ds-precommit-check.py, infra/aws/terraform/modules/opal_name/ and the channel. The intersection is the channel alone, which is the known append-only case every drain already handles.",
     "AND YET ONE IS THE OTHER'S INSTRUMENT: EN-s-1's cell text is 'Run python lib/opal_naming.py census --live --repo --report ...' and adds 'The code is round 1's; do not change it.' lib/opal_naming.py is the FIRST entry of EN-r-6's write surface.",
     "SO THE CENSUS THAT IS SUPPOSED TO CATCH CONTENTION RETURNS EMPTY ON EXACTLY THE PAIR THAT CONTENDS. A disjointness check over <paths> compares what two cells WRITE; it never asks what either cell RUNS or READS. Two cells can share no written byte and still have one produce the other's measuring instrument.",
     "THE CONSEQUENCE IF IT HAD BEEN MISSED: EN-s-1 would have censused the live and repo planes with the PRE-EN-r-6 naming code and written NAMING_CENSUS_REPORT.md from it, and S1R-AC5 ('the report was written at HEAD's registry') would then be graded after EN-r-6's drain moved both the code and data/firm_registry.json. The report would be a faithful record of an instrument that no longer exists.",
     "THE DECOMPOSITION DOES NOT CATCH IT EITHER: EN-s-1's declared depends_on is 'EN-r-2 and EN-r-4 round 2 (merged)' and both are complete, so by the dependency graph EN-s-1 is unblocked RIGHT NOW. The dependency that actually binds it is not in the graph.",
     "GENERALITY, checked rather than assumed on the same round: EN-t-3 has the same shape one step weaker -- it runs .tools/naming-apply-gate.py, which EN-t-2 wrote, but EN-t-2 has already DRAINED at abd07c7ef3, so the instrument is settled and the ordering is satisfied. The pattern is 'runs what another open cell writes', and it binds only while that other cell is open.",
     "This is CLAUDE.md Rule 22's shared-dependency limb -- a check scoped to the members cannot see a defect in what the members SHARE -- appearing at the ISSUANCE rather than inside a criterion. Each cell's write surface was verified; what they have in common, the code one of them executes, was not checked on its own."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "The round-2 preflight's write-surface line: 'MEASURED at the cut. The <paths> of every non-terminal order were intersected with this round's write surfaces; the intersection is EMPTY.'",
   "world_is": "An empty write-surface intersection certifies that two cells will not overwrite each other. It does NOT certify that they can run concurrently, because it never reads the INVOCATIONS: a cell whose criterion executes a file another open cell is editing is contended on an axis this census does not have.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. EN-s-1 is therefore HELD -- not blocked by its own dependency graph, held by this seat's judgment on measured evidence -- until EN-r-6 drains, and it is spawned against the post-drain lib/opal_naming.py so its report and S1R-AC5 describe the same instrument. Disarms when EN-s-1 is spawned after EN-r-6's drain AND the issuance census is widened to intersect each cell's INVOCATION targets with every open cell's <paths>, not only its own <paths>. The widening is the durable half; holding one cell is just this round's instance of it."
  },
  {
    "id": "LGIC_ENFORCE-W1-S28",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~1",
    "surfaced_at": "2026-09-16T09:10Z",
    "one_line": "loaders.py's bucket_for block reads ZERO registry keys (instrumented), yet EN-r-6's mark format and check_en_r2.py's PER_VIEW regex both require at least one declared file; resolved by declaring scopes.json, its documented trust anchor, not a literal read.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, this worktree: a registry dict wrapped to record every top-level key __getitem__/.get touches, run through _render_view for each of the 7 VIEWS plus _gen_locals/build_vectors/_gen_tftest -- every target touches at least {'scopes'} except infra/aws/lambda/investor-reporting/_authz/loaders.py ('bucket_for'), which touches the empty set.",
        "READ lib/opal_naming.py@1d519bff1b (this cell's spawn base) :651-653, _blk_bucket_for(reg, h16, path): return _block(\"bucket_for\", h16, \"#\", path, _BUCKET_FOR) -- _BUCKET_FOR is a fixed triple-quoted string constant with no reg[...] or reg.get(...) access anywhere in it.",
        "READ infra/aws/lambda/investor-reporting/_authz/loaders.py@c19dcc8147 :44-45 (pre-this-cell, already committed): 'This definition carries no registry row: the firm -> bucket map it serves is the environment variable Terraform sets from local.firm_bucket_map, read from data/firm_registry.json (itself a generated view).' -- the module's own prior author already documented the zero-read fact.",
        "READ org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py@5e908a4929 :69, PER_VIEW = re.compile(r\"GENERATED by lib/opal_naming\\.py from infra/logic/registry@([0-9a-f]{16}) over ([A-Za-z0-9_.,-]+)\") -- the trailing + requires at least one character, so a mark with a zero-length 'over' clause does not match; :295-300's require_per_view() then reads that target as carrying NO per-view mark, and every one of the ten R6-AC* subcommands calls require_per_view() before anything else, so ALL TEN would FAIL together, not just the one target.",
        "READ org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-r-6-r2.per-view-hashes.md THE CELL item 1: the mark format is given as 'over <file>[,<file>...]' -- one mandatory file plus optional others, the same non-empty shape the checker enforces.",
        "MEASURED, this worktree, after declaring scopes.json for this one target (lib/opal_naming.py@39cbad4214, TARGET_REGISTRY_KEYS): all ten check_en_r2.py r6-* subcommands print VERDICT: PASS-* (PASS-PER-VIEW-HEADERS, PASS-UNDECLARED-INERT 10 probed, PASS-DECLARED-MOVES 18 pairs probed, PASS-DELTA0-IN-ORDER incl. bucket_for both branches, PASS-GENERATE-REPRODUCES, PASS-NO-NEW-FAILURE-V1/V2/V3/V4/V6), rc=0 each."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "THE CELL item 1: 'each generated file declares the registry files its renderer reads ... Derive the declaration from what the renderer reads ... A registry file the renderer does not read is not listed.' The mark format 'over <file>[,<file>...]' and check_en_r2.py's PER_VIEW regex both presuppose every renderer reads at least one registry file.",
    "world_is": "One of the ten renderers (bucket_for) reads none, by design, and says so in its own pre-existing comment -- a genuine, previously-documented zero-dependency case the mark format cannot express. Declaring the empty set is not mechanically an option (it would fail require_per_view() for every one of the ten R6-AC* criteria, not just this one). scopes.json was declared instead: not a dict-key read this renderer makes, but the block's own documented trust anchor (the same file data/firm_registry.json itself declares), chosen because it is the least-arbitrary non-empty answer available and it lets every R6-AC* criterion PASS by output under this cell's own checker.",
    "notes": "No remedy owed to reach PASS -- all ten R6-AC* criteria pass under this resolution, cited above. Filed so 3.0.0_SA_CVO (L9) or a later round can confirm the scopes.json attribution is the right call, or amend the mark format/PER_VIEW regex to admit a literal zero-file 'over' clause for a renderer that truly reads nothing, should either be preferred to this worker's judgment call."
  },
  {
   "id": "LGIC_ENFORCE-S24",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:05Z",
   "one_line": "S23's rule applied for the FIRST time and caught a SECOND cell within the hour: EN-d-1 is unblocked by its dependency graph and by write-surface disjointness, and is HELD anyway, because it WRITES the two registry files the live EN-s-1 census READS.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "EN-d-1 READS AS READY ON BOTH EXISTING CHECKS. Its declared depends_on is 'EN-r-6 round 2 (merged)' and EN-r-6 drained at c8e9d02213. Its <paths> do not intersect EN-s-1's <paths> (EN-s-1 writes only NAMING_CENSUS_REPORT.md and the channel). Its worktree was provisioned and healthy at the time of this row.",
     "AND IT IS STILL CONTENDED. EN-d-1's write surface opens with infra/logic/registry/scopes.json and data/firm_registry.json. EN-s-1's cell is 'python lib/opal_naming.py census --live --repo', and that census READS the registry -- those two files are its INPUT, and S1R-AC5 grades that 'the report was written at HEAD's registry'.",
     "SO THE CONTENTION IS INPUT-vs-OUTPUT, one step out from S23's instrument-vs-output. EN-d-1 adds a demo firm to the registry; if it landed while EN-s-1 was censusing, EN-s-1's report would describe a registry that HEAD no longer carries, and S1R-AC5 would fail at drain through no fault of its worker.",
     "MEASURED SEQUENCE: EN-s-1 was spawned into wk-lgic-enforce-2d-2 at base c8e9d02213 and is LIVE at the time of this row. EN-d-1's worktree wk-lgic-enforce-2d-5 exists at the same base and NO worker has been spawned into it.",
     "THIS IS THE WIDENED CHECK FROM LGIC_ENFORCE-S23 RUNNING, NOT A NEW DISCOVERY OF THE SAME THING. S23 says to intersect each cell's INVOCATION targets with every open cell's <paths> rather than comparing <paths> to <paths>; doing exactly that on the next spawn decision returned this pair. Two instances in one round, found by one rule, is the evidence that the rule is worth keeping rather than a one-off."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "EN-d-1's depends_on (EN-r-6, merged) and the round's write-surface disjointness check both read this cell as ready to spawn.",
   "world_is": "Neither check reads what EN-s-1 CONSUMES. EN-d-1 writes the two registry files the live census reads as its input, so spawning it now would corrupt a sibling's measurement rather than its own.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. EN-d-1 is HELD until EN-s-1 drains, then spawned against the post-drain tree; its worktree is already provisioned so the hold costs a wait, not a rebuild. Disarms when EN-d-1 is spawned after EN-s-1's drain. \u26a0 This row does NOT re-argue S23 and does not disarm it -- S23 owns the durable widening of the issuance census; this row exists so a reader asking why EN-d-1 sat unspawned while every declared gate read MET finds the answer at the cell rather than only in the rule."
  },
  {
   "id": "LGIC_ENFORCE-S25",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:05Z",
   "one_line": "Four drain merges this hour are authored `2.0.0_SA_COO` (base) instead of `~G`. Surfaced by 1.0.0_SA_CTO as possibly a tool drop; MEASURED to be neither a tool drop nor an environment drop -- I typed the base serial into the export myself, on the merge path only, while typing ~G on every commit path.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "THE FINDING, as 1.0.0_SA_CTO measured it (msg 97341): git log --format=%an since 7db18a4464 reads 2.0.0_SA_COO 4, 2.0.0_SA_COO~G 3, workers 10. The four base-authored commits are all drain MERGES -- 2bc14e52f8 (CN-j-7), 5a391b0c46 (CN-k-3), c8e9d02213 (EN-r-6), abd07c7ef3 (EN-t-2, the earliest, which is why this row is on LGIC_ENFORCE's channel. Earlier drains this session (4730cec6ca, 40c268fc66, 901f48b1e0, ba15ed94a5) carry ~G.",
     "THE CTO ASKED WHETHER safe-merge.sh's MERGE PATH READS THE SERIAL DIFFERENTLY FROM safe-commit. IT DOES NOT. Read at HEAD: safe-merge.sh:326-334 REFUSES outright when OPAL_AGENT_SERIAL is unset ('cannot name the' author), then builds _AUTH=\"${OPAL_AGENT_SERIAL} <${OPAL_AGENT_SERIAL}@opal.agent>\" at :333 and passes it to git commit --no-edit --author at :335. It uses the variable VERBATIM and has a self-test arm asserting both behaviours (:75-78). There is no derivation, no lane stripping and no fallback to guess.",
     "SO IT IS NOT AN ENVIRONMENT DROP EITHER, and this is the part worth recording: the variable was not lost, it was SET TO THE BASE BY ME. Every merge invocation this hour opened with `export OPAL_AGENT_SERIAL=2.0.0_SA_COO` while every safe-commit invocation in the same window opened with `export OPAL_AGENT_SERIAL=2.0.0_SA_COO~G`. Two different values typed by one seat in one hour, split cleanly along the merge/commit line.",
     "WHY THE SPLIT EXISTED AT ALL: the deliverables lane refuses the BASE serial on a path under deliverables/2.0.0_SA_COO~G/ (measured earlier this session -- safe-commit rejected the base with 'agent=2.0.0_SA_COO not in permitted_agents'), so the commit path forced ~G on me by refusal. The merge path never refuses, because owned-paths-check exempts a merge on MERGE_HEAD. The lane taught me the right value on one path and stayed silent on the other, so the wrong value survived exactly where nothing graded it.",
     "THE HARM, and it is the CTO's framing, not mine to soften: an author census of the round -- the CVO's L8, the daily sprint, this loop's tick logs -- UNDER-COUNTS the lane and OVER-COUNTS a base seat that is not seated at all. Only ~G is live on the broker. Same class as A-15's disarm attribution finding: the record names one seat and the act was another's.",
     "NOT REDONE: the four merge commits stand. Their trees, their gate runs and their row grading are unaffected -- only the %an string is wrong, git history is append-only, and rewriting four merges on a shared branch to correct an attribution string would be a far larger act than the defect."
    ]
   },
   "disposition": "DISMISSED_WITH_REASON",
   "dismissal_reason": "Cause established and the remedy is a reading rule this seat now follows: export OPAL_AGENT_SERIAL=2.0.0_SA_COO~G for EVERY act, merge and commit alike, never the base. The tool needs no change -- it did exactly what it was told, and its refusal-on-unset plus its two self-test arms are correct as written. The four affected commits stand with their attribution as-is, disclosed here so the CVO reads the round's author census with this row beside it rather than concluding a base seat was working. INERT: nothing is armed, no act is owed by another seat, and the exposure ends with the next merge.",
   "spec_asserts": "A commit's author line names the seat that performed the act, so an author census of a round counts who did the work.",
   "world_is": "On the merge path the author line is whatever the invoking shell exported, and nothing grades it -- the lane check that would have refused the base serial is exempt on a merge commit. For four merges this hour the exported value was the base serial while the acting seat was the lane, so the census names a seat that is not seated.",
   "notes": "\u2b50 THE GENERAL SHAPE, which is why this is worth a row rather than a silent correction: A GATE THAT REFUSES ON ONE PATH AND IS EXEMPT ON ANOTHER TEACHES THE CORRECT VALUE ONLY WHERE IT BITES. I learned ~G from the lane refusal on the commit path and never learned it on the merge path, because the merge path never refused. The value was wrong in exactly the place no instrument was looking. \u26a0 Found by 1.0.0_SA_CTO, not by me, on an off-task census during its own tick -- and its hypothesis (a tool or environment drop) was the generous one; the measurement says the seat typed it."
  },
  {
    "id": "LGIC_ENFORCE-W2-S10",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~2",
    "surfaced_at": "2026-09-16T09:48Z",
    "one_line": "The EN-s-1 re-run's only OUT-OF-PATTERN row carries a LITERAL unfilled {system} into the census report -- live API_GW inf-otp-relay-api grades to '{system}-inf-otp-relay-api' while its own registered sibling inf-otp-relay-lambda-role grades to 'advi-inf-otp-relay-lambda-role', because resources.json is keyed by (name, type) and 18 of RESOURCE_GAPS.json's 48 gaps have no (name, type) row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "The EN-s-1 round-2 worker face (LGIC_ENFORCE.TO-EN-s-1-r2.census-run.md@4f9a9eb3f3, THE CELL, paragraph 'What the counts should show') states: EN-r-4's rows fill {system} where a name's own tokens resolve none.",
    "world_is": "At HEAD registry@254d4e9ece847acb they fill it only where a resources.json row matches the graded name AND its type. EXERCISED in this worktree: grade('inf-otp-relay-api','API_GW') returns ('OUT-OF-PATTERN','{system}-inf-otp-relay-api') -- the placeholder is emitted verbatim -- while grade('inf-otp-relay-lambda-role','IAM_ROLE') returns ('OUT-OF-PATTERN','advi-inf-otp-relay-lambda-role'). The first is the ONLY non-CONFORMANT row the re-run produced before its RAISE stop, so 1 of 1 OUT-OF-PATTERN rows in NAMING_CENSUS_REPORT.md carries the placeholder. This changes no S1R criterion's verdict and is filed, not chased.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, this worktree at HEAD c8e9d02213 (base CLOUD): lib/opal_naming.py@39cbad4214 loaded by path and called directly -- grade('inf-otp-relay-api','API_GW') -> ('OUT-OF-PATTERN', '{system}-inf-otp-relay-api'); grade('inf-otp-relay-lambda-role','IAM_ROLE') -> ('OUT-OF-PATTERN', 'advi-inf-otp-relay-lambda-role'). The pair is the discriminator: same resource family, same firm token inf, different type; only the type carrying a registry row resolves {system}.",
        "MEASURED, this worktree: infra/logic/registry/resources.json@b15ed01ee6 carries 30 rows; the one row naming otp is {'name': 'inf-otp-relay-lambda-role', 'type': 'IAM_ROLE', 'system': 'advi'}. There is NO row for inf-otp-relay-api of type API_GW.",
        "MEASURED, this worktree: over the 48 gaps of org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/RESOURCE_GAPS.json@4f9a9eb3f3, 18 have no (name, type) match among resources.json's 30 rows. DENOMINATOR: 48 of 48 gaps compared against 30 of 30 registry rows.",
        "MEASURED, the ordered run in this worktree: 'python lib/opal_naming.py census --live --repo --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md' rc=3, log line 'CENSUS OUT-OF-PATTERN live API_GW inf-otp-relay-api -> {system}-inf-otp-relay-api'. The written report's fenced json carries the same row verbatim: {'current': 'inf-otp-relay-api', 'canonical': '{system}-inf-otp-relay-api', 'verdict': 'OUT-OF-PATTERN', 'type': 'API_GW', 'plane': 'live'}.",
        "READ org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-s-1-r2.census-run.md@4f9a9eb3f3, THE CELL, paragraph 'What the counts should show' -- the asserted sentence is quoted in spec_asserts above."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "notes": "INERT, not ARMED: the defect surfaces as a VISIBLE placeholder token inside the canonical, which no consumer can mistake for a name -- it cannot silently produce a wrong rename target. SCOPE: whether 18 uncovered gaps is itself a defect belongs to EN-r-4's own criterion r4-gaps-covered (check_en_r2.py@5e908a4929) and is NOT graded here; this row records only what the EN-s-1 census output carries. No remedy is available to this worker -- infra/logic/registry/resources.json is outside this order's <paths> grant."
  },
  {
   "id": "LGIC_ENFORCE-S26",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T10:15Z",
   "one_line": "EN-d-1's S24 hold is CLEARED and the cell is STILL not spawned, for a second and different reason: it needs a PRACTICE-COPY worktree, and spawning it now would leave only about 1.5 GB above the 10 GB stop line EN-t-3 is running under -- so it could trip a sibling's own safety stop mid-census.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S24's condition is MET: it held EN-d-1 until EN-s-1 drained, because EN-d-1 WRITES the two registry files EN-s-1's census READS. EN-s-1 drained at 99c34fb574. That hold is over and this row does not re-argue it.",
     "THE NEW CONSTRAINT, measured: df -h /c reads 13 GB free. EN-d-1's cell text orders a SECOND worktree -- 'git worktree add -b prac-lgic-enforce-d1-r2 <WS>/../prac-lgic-enforce-d1-r2 HEAD' -- because its evidence is commit hashes on a scratch branch. A fresh worktree of this repo measures about 1.5 GB (du -sh on a live one). 13 - 1.5 leaves about 11.5 GB.",
     "AND A SIBLING IS RUNNING UNDER A 10 GB STOP LINE: EN-t-3's BOUNDS say 'the 10G stop line binds', and the S22 correction has it re-measure free space every ten roots and stop with a BLOCKING row below that line. So spawning EN-d-1 now leaves roughly 1.5 GB of margin between a sibling's working set and its own abort threshold.",
     "THE COST OF BEING WRONG IS ASYMMETRIC, which is what decides it: EN-d-1 delayed costs a wait. EN-t-3 tripping its stop line mid-run aborts a 73-root census that is most of an hour of terraform init/plan work, and the abort would be CORRECT behaviour by a guard I wrote, triggered by a spawn I chose. Waiting is cheaper than the thing I would be gambling on.",
     "EN-t-3's FOOTPRINT IS BEHAVING AS THE S22 CORRECTION INTENDED, measured in its worktree: exactly ONE .terraform directory present (served-guard-inf), infra/aws/terraform totalling 711M, worktree 2.2G overall. So the per-root cleanup is working and the steady state is about one root -- but 'about one root' is an observation over the roots seen so far, not a bound on the largest provider set still to come."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "A cell whose declared dependencies are met and whose write surface is clear is ready to spawn.",
   "world_is": "Readiness is not only dependency and write surface. This cell also needs DISK that a live sibling is already budgeting against, and the two cells' needs are invisible to each other -- neither order mentions the other, and no gate compares a spawn's footprint against a running cell's stop line.",
   "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G. EN-d-1 spawns when EN-t-3 drains and its worktree is removed, which returns about 2.2 GB. Its slot worktree (wk-lgic-enforce-2d-5) is ALREADY provisioned and is deliberately being kept rather than reclaimed -- removing and rebuilding it would cost two minutes and the same 1.5 GB on the way back in. \u2b50 THE GENERAL SHAPE, and it is the third variant of one blindness this round: S23 was instrument-vs-output, S24 was input-vs-output, and this is CAPACITY-vs-capacity. All three are cells whose <paths> do not intersect and which still cannot safely run at the same time. A write-surface census answers none of them."
  },
  {
    "id": "LGIC_ENFORCE-W3-S12",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-16T10:19Z",
    "one_line": "4 of the 72 backend roots cannot render a plan AT ALL on this box -- two carry plan-time configuration defects, one needs a gitignored build artifact whose builder egresses to PyPI, one needs a gitignored secret tfvars a linked worktree never carries -- so T3R-AC2 (every backend root planned) cannot pass inside this order's <paths> grant or its bounds.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "EXERCISED, this worktree (wk-lgic-enforce-2d-3, base 62c701411e), 2026-09-16 09:52-10:10Z: all 72 backend roots were init'd and planned one at a time with terraform v1.9.8, `plan -lock=false -input=false -out=<abs scratch>`; 68 rendered, 4 exited rc=1 at plan. Each root's .terraform (686 MB measured) was removed before the next init; dotdir_removed TRUE 72 of 72.",
        "MEASURED rc=1, infra/aws/terraform/nfra-agentbus-port2: 'Error: expected max_message_size to be in the range (1024 - 262144), got 1048576' on aws_sqs_queue.sitez_to_laptop (sqs.tf:31) AND aws_sqs_queue.laptop_to_sitez (sqs.tf:46) -- a provider validation error, so this root refuses at plan for any operator, not only here.",
        "MEASURED rc=1, infra/aws/terraform/seeking-alpha: 'Error: Missing required argument ... The argument \"artifact_key\" is required' and 'Error: Unsupported argument ... An argument named \"source_dir\" is not expected here', both on module \"news_dedup\" at main.tf:168-171 -- the module call and the module's declared variables disagree, so this root also refuses at plan for any operator.",
        "MEASURED rc=1, infra/aws/terraform/harvest: filebase64sha256(local.chatter_axis_zip) cannot open ./.build/chatter-axis-producer.zip. READ .gitignore:95 '*.zip' via `git check-ignore -v`, and the path is ABSENT from the main checkout C:/Users/AndrewBerman/Desktop/ajb_workspace as well as from this worktree, so it is not a worktree-provisioning gap. Its builder infra/aws/terraform/harvest/lambda_src/build_zip.py:225 runs `sys.executable -m pip download` (comp-read --enumerate, 11 hits, 9 in the CODE band): building it is egress off Opal infrastructure, which CLAUDE.md s.Agent-Autonomy excludes from standing authority and this order names as 'Never fetch off-box without the word.'",
        "MEASURED rc=1, infra/aws/terraform/trade-pipeline: 'The root module input variable \"jwt_secret\" is not set, and has no default value.' The value lives in secrets.auto.tfvars, which `ls -a` shows PRESENT in the main checkout's infra/aws/terraform/trade-pipeline/ and ABSENT from this linked worktree's -- a gitignored secret, by construction absent from every fresh worktree. A fabricated value would render a document that is not the root's real plan, which is exactly what T3R-J1 asks the extracts to be.",
        "MEASURED, this worktree: `python .../check_en_r2.py t3r-every-root-planned` prints 'ROOTS WITH A BACKEND BLOCK: 72  RECORDED: 72  MISSING: []  NOT A ROOT: []  NOT PLANNED OR NO EXTRACT: ['infra/aws/terraform/harvest', 'infra/aws/terraform/nfra-agentbus-port2', 'infra/aws/terraform/seeking-alpha', 'infra/aws/terraform/trade-pipeline']' / VERDICT: FAIL-ROOT-NOT-PLANNED, rc=1. The other three mechanical criteria PASS by output: t3r-preplan-zero (0 of 77 directories refused), t3r-zero-existing-refused (2431 resource changes, 0 refusals of a resource neither created nor renamed, 0 limb errors), t3r-additions-disclosed (34 of 34 listed).",
        "READ the task order's <paths>: only org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/LIMB_ROOTS_CENSUS.md and the investigation file. Every repair the four roots need is an edit under infra/aws/terraform/, which the grant does not name, and the order's own BOUNDS say a path the order lacks is a BLOCKING row, never an override."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "THE CELL item 1 tells this worker to plan every root and says 'A root that cannot init without fetching a provider from outside Opal infrastructure, or cannot plan, is recorded NOT planned with its reason' -- it EXPECTS unplannable roots. T3R-AC2 then requires VERDICT: PASS-EVERY-BACKEND-ROOT-PLANNED, and check_en_r2.py t3r_every_root_planned() computes unplanned = roots whose record is not planned or whose extract file is absent, and FAILS when that list is non-empty. The two clauses cannot both be satisfied while any root is unplannable.",
    "world_is": "Four backend roots are unplannable on this box, for four different reasons, none of them reachable from this order's write surface: two are plan-time configuration defects in infra/aws/terraform/ (an out-of-range SQS max_message_size; a module call that disagrees with its module's variables), one needs a gitignored build artifact absent from EVERY checkout on this box whose builder egresses to PyPI, and one needs a gitignored secret tfvars that a linked worktree never carries. The other 68 planned and the census records all 72 with reasons, as item 1 prescribes -- so the order's prose was satisfied and its criterion was not.",
    "notes": "No 'complete' flip: T3R-AC2 is FAIL by output and the order stays open, which is the report. INERT rather than ARMED because the harm this would cause -- reading '0 refusals of existing resources' off a census that never exercised 4 of 72 roots, and flipping G-F on it (the CTO's round-1 analysis s.2 RULING ADD) -- is already refused by the FAIL this row records, and the census discloses the 4 roots and their reasons in its own section 4 and in its json record. Whoever recuts this cell owns the choice: widen the <paths> grant to repair nfra-agentbus-port2/sqs.tf and seeking-alpha/main.tf in their own cell, or amend T3R-AC2 to admit a root recorded NOT planned with a reason -- which is what item 1 already says. harvest and trade-pipeline are not repairs at all: one needs Andrew's word for egress, the other needs a secret an operator supplies, and both would still need the criterion amended."
  },
  {
    "id": "LGIC_ENFORCE-W3-S13",
    "project": "LGIC_ENFORCE",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_LGIC_ENFORCE~3",
    "surfaced_at": "2026-09-16T10:21Z",
    "one_line": "`terraform init` does not only write .terraform: on 2 of the 72 roots it REWROTE the TRACKED .terraform.lock.hcl, pruning a provider the config no longer uses -- a write outside this order's <paths> grant, produced by an invocation the order itself prescribes.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED, this worktree after the 72-root run: `git status --porcelain` shows exactly two tracked modifications, ' M infra/aws/terraform/market-overview/.terraform.lock.hcl' and ' M infra/aws/terraform/seeking-alpha/.terraform.lock.hcl'; `git diff --stat infra/aws/terraform` reads '2 files changed, 1 insertion(+), 39 deletions(-)'. Denominator: 72 roots init'd, 2 lock files changed, 70 unchanged.",
        "MEASURED, the diff itself: both files lose the whole 'provider \"registry.terraform.io/hashicorp/archive\"' block (version 2.7.1, constraints ~> 2.0, 12 hashes) -- terraform v1.9.8 pruned a provider the current configuration no longer requires. Nothing else in either file moved; the hashicorp/aws block is untouched.",
        "READ the task order BOUNDS, Disk: 'Every `init` writes a `.terraform` directory into your worktree; the 10G stop line binds.' That is the only write the order attributes to init, and the whole per-root cleanup correction (row LGIC_ENFORCE-S22) is written about .terraform alone.",
        "NOT COMMITTED and NOT REVERTED: infra/aws/terraform/ is not in this order's <paths>, and the worker definition forbids `checkout --`. Both files are left MODIFIED AND UNSTAGED in this disposable worktree, so neither reaches the branch the COO drains; `git status` after the commit is the check."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The order's BOUNDS attribute exactly one write to `terraform init`: 'Every `init` writes a .terraform directory into your worktree.' The grant clause says the write surface is the <paths> block plus this worker's deliverables folder and the order file, 'Nothing else.'",
    "world_is": "init ALSO rewrites the tracked .terraform.lock.hcl when the config's provider set has moved, which it did on 2 of 72 roots. In a disposable worktree this is inert -- the change is unstaged and never merges. In the MAIN checkout, or any worktree a seat commits broadly from, the same invocation (including the one inside .tools/safe-apply.sh) silently dirties a tracked file that an unrelated `safe-commit -- <dir>` could sweep in.",
    "notes": "Filed for form, not significance: this worker neither committed nor reverted the two files and both stay unstaged. The durable question for whoever recuts or adjudicates: a cell that orders `terraform init` over N roots should either name .terraform.lock.hcl in its <paths> so the prune is a recorded decision, or say explicitly that lock-file drift is left in the worktree and discarded -- today the order says neither, and the two affected roots (market-overview, seeking-alpha) carry a stale archive-provider entry in their committed lock files that any future init will prune again."
  },
  {
   "id": "LGIC_ENFORCE-S27",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T11:30Z",
   "one_line": "ISSUER'S DISARM OF LGIC_ENFORCE-S22: the per-root cleanup correction was committed, EN-t-3 ran against it, and the worker's own readings prove the cap held -- 72 of 72 .terraform directories removed and the removal VERIFIED before the next init, low-water 12.96 GB against a 10 GB stop line that never fired.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S22 said EN-t-3 as cut could not run: it orders terraform init on the backend roots and never releases a root's .terraform, one initialised root costs 686 MB on this filesystem, and 73 x 686 MB is about 50 GB against 19 GB free with four workers live. Its disarm condition was that the correction be committed and the cell spawned against it.",
     "BOTH HALVES DONE: the correction landed at 2325c408c2 (one root at a time, delete that root's .terraform the moment its show -json is captured, re-measure free space every ten roots) and its own follow-up 62c701411e removed a SECOND stop line I had accidentally introduced at 5 GB where the order's BOUNDS already bound 10 GB. EN-t-3 was spawned against 62c701411e and drained at 2a2b853f79.",
     "AND THE CAP HELD, measured by the worker and reported with its denominators: 'one .terraform is 686 MB (the plugin cache does NOT spare it on this filesystem), each was deleted and its removal verified before the next init (72 of 72), free space 18.32 GB start / 12.07 GB end, 8 readings, lowest 12.96 GB -- the 10 GB stop line was never reached.'",
     "THE 686 MB UNIT COST IS NOW CORROBORATED ON A SECOND INSTRUMENT: I measured it on the one root already initialised in the main checkout (du -sh infra/aws/terraform/portal-auth/.terraform) BEFORE the cut; the worker measured it independently across 72 roots DURING the run. Same figure, different instrument, different population.",
     "THE CELL PRODUCED ITS DELIVERABLE: 68 of 72 backend roots planned with an extract and a plan_sha256; 2431 resource changes read; T3R-AC1, AC3 and AC4 PASS. So the correction did not buy safety at the cost of the measurement.",
     "\u26a0 WHAT DID NOT HOLD IS A DIFFERENT THING AND IS NOT DISARMED HERE: T3R-AC2 FAILED because 4 roots cannot render a plan on this box at all, and the criterion refuses the NOT-planned state that the cell's own item 1 prescribes recording. That contradiction is row LGIC_ENFORCE-W3-S12, BLOCKING, and it is the recut's to resolve."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "S22: EN-t-3 as cut would demand roughly 50 GB against 19 GB free and take the volume down under four live workers.",
   "world_is": "With the per-root cleanup it demanded roughly one root at a time, and the run's own eight free-space readings never came within 2.9 GB of the stop line. The hazard S22 named is dead.",
   "notes": "INERT. \u2b50 THE HALF WORTH KEEPING is not the fix but WHERE IT WAS FOUND: the pre-spawn read of the face I was about to hand a worker. The cell had a disk clause already -- 'the 10G stop line binds' -- and that clause would have fired correctly and aborted a 72-root census most of the way through. A guard that stops the work is not the same as a design that does not need stopping. COST of the pre-spawn read: one du and one df. \u26d4 AND IT DISARMS S22 ONLY. W3-S12 (four unplannable roots vs a criterion that refuses the state the cell prescribes) stays BLOCKING and is the recut's."
  },
  {
   "id": "LGIC_ENFORCE-S28",
   "project": "LGIC_ENFORCE",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-16T11:32Z",
   "one_line": "ISSUER'S DISARM OF LGIC_ENFORCE-S24 AND S26 TOGETHER, because they are two holds on ONE cell and both conditions are now met: EN-d-1 is spawned, after EN-s-1's drain (S24's input-vs-output hazard) and after EN-t-3's drain returned the disk (S26's capacity hazard).",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "S24 held EN-d-1 because it WRITES infra/logic/registry/scopes.json and data/firm_registry.json, which the then-live EN-s-1 census READS as its input -- an input-vs-output contention invisible to both the dependency graph (EN-d-1's depends_on read MET) and the write-surface census (the <paths> intersection was EMPTY). Its disarm condition was that EN-d-1 be spawned after EN-s-1's drain. EN-s-1 drained at 99c34fb574.",
     "S26 then held the SAME cell for a different reason: it needs a PRACTICE-COPY worktree of about 1.5 GB, free space was 13 GB, and the live EN-t-3 was running under a 10 GB stop line -- so spawning would have left about 1.5 GB between a sibling's working set and its own abort threshold. Its disarm condition was EN-t-3's drain returning that space. EN-t-3 drained at 2a2b853f79 and its worktree removal returned about 2.2 GB.",
     "BOTH MET, AND THE SPAWN HAPPENED IN THAT ORDER: EN-d-1 was spawned this tick into wk-lgic-enforce-2d-5, fast-forwarded to 2a2b853f79 first so its `generate` runs against the post-EN-r-6 lib/opal_naming.py rather than the vintage it was provisioned at.",
     "THE SPAWN ALSO CARRIED THE TWO HAZARDS FORWARD AS INSTRUCTIONS rather than trusting they were gone: the worker was told its base is deliberately current and why, told the practice copy costs about 1.5 GB against roughly 12 GB free with siblings sharing the volume, told to stop and file a BLOCKING row below 5 GB, and told that if any invocation modifies a tracked file its <paths> does not name it must leave it unstaged and file a row -- which is exactly what EN-t-3 measured happening to .terraform.lock.hcl on 2 of 72 roots."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "S24 and S26: EN-d-1 must not be spawned while EN-s-1 reads the registry it writes, nor while EN-t-3 is budgeting disk against a 10 GB stop line.",
   "world_is": "Both siblings have drained, the disk came back, and EN-d-1 is running against a base that postdates every artifact it depends on.",
   "notes": "INERT. \u26a0 ONE ROW FOR TWO HOLDS IS DELIBERATE AND IS NOT A COMPOUND ROW: S24 and S26 are two conditions on ONE act -- spawning EN-d-1 -- and that act happened once. Splitting the record would imply two independent events. \u26d4 S23 IS NOT DISARMED HERE and stays ARMED: its condition has TWO halves and only one is met. EN-s-1 was spawned after EN-r-6's drain (met), but the durable half -- widening the issuance census to intersect each cell's INVOCATION and INPUT targets with every OPEN cell's <paths>, rather than comparing <paths> to <paths> -- exists only as this seat's hand discipline across three instances (S23, S24, S26) and is embedded in no tool and no order template. A rule I apply by remembering is not a widened census."
  }
]
```
