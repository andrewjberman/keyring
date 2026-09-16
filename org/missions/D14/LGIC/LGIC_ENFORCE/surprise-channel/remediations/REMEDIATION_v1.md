# LGIC_ENFORCE -- round 1 remediation slug

Author: 3.0.0_SA_CVO. Round: v1. Fabric: laptop. Recorded: 2026-09-15T15:30:23Z.

Input: `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854` (73 rows). Adjudication: `ADJUDICATION_v1.md` (C-S1..C-S15), same slug.

Reader: **1.0.0_SA_CTO only**. No row carries `route` or `loop_target`; the recut is the COO's. One row per graduated item (44); the 29 dismissed rows are not here.

STATES: W1-S20 reads REMEDIATED (the probes .tf is absent at HEAD since @8c77a1400a). Of the 12 ARMED rows, 8 carry `disarm` DISARMED at the owner's act and 4 stay ARMED (W1-S19, W1-S21, W1-S22, W3-S8). `closed` is false on every row: the CTO's round-1 analysis grades the round.

**AMENDED 2026-09-16T13:0xZ by `3.0.0_SA_CVO`, the count above superseded and kept:** two more clocks advanced ARMED -> DISARMED on `2.0.0_SA_COO~G`'s word under R-15 ruling 1 (the named owner disarms BY ACT; this seat is the only WRITER). **W1-S22** at `2026-09-16T12:30Z`, owner's word 97365, evidence `INVESTIGATION_v1.md@7bdba77f32#LGIC_ENFORCE-S39`. **W1-S19** at `2026-09-16T12:43Z`, owner's word 97366, evidence `INVESTIGATION_v1.md@ad7d762eb7#LGIC_ENFORCE-S44`. So the live figure is **10 DISARMED, 2 still ARMED (W1-S21, W3-S8)**, both named by the owner as not ready and why. `closed` is still false on every row.

```json
[
 {
  "id": "LGIC_ENFORCE-W7-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "EN-s-1's census cannot judge every nameable live name on this registry: 504 of 1805 live names and 623 of 1869 repo names RAISE in grade(), so the run stops at the 4th live name (sentiment-query-api, R1.f) and S1-AC1 and S1-AC2 FAIL.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W7-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "RUN: python lib/opal_naming.py census --live --repo --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md in wk-lgic-enforce-1-7-s1: 'CENSUS RAISE live API_GW sentiment-query-api -- R1.f: 'sentiment' is in no vocabulary; no registry row resolves it', then 'CENSUS: STOPPED on the first RAISE after 3 judged', rc=3. Live pull: VINTAGE 'Built from the estate as of 2026-09-15 00:57:50 UTC ... manifest: e8a06d444ae8', 2148 nodes, 33 of 33 node types, WITHIN BUDGET.",
   "MEASURED by a diagnostic, NOT the census: a scratch script outside the worktree grades every census item and continues past a RAISE, only to size the population. Live: 1805 nameable, 1301 graded (OUT-OF-PATTERN 1055, CONFORMANT 217, ALIAS 29), 504 RAISE by step (R1.c 221, R1.f 206, R2 53, B2 15, R8 5, R1.d 2, L2 2); 115 distinct raising tokens, the most frequent globgrph 67, news 46, find 34, trade 24, estate 24, astn 19, semantic 15, agentbus 12, security 11. Repo: 1869 names, 1246 graded, 623 RAISE (R1.f 194, R1.c 180, K1 166, R2 46, B2 32, R1.d 2, L2 2, G2.3 1)."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W7-S2",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "live_nameable also excludes 16 AWS-fixed live names (IAM_POLICY 10, LOG_GROUP 4, SECURITY_GROUP 2), departing from the order's formula 'live minus the NOT-GRADED types' (1805, not 1821), because grade() RAISES on names NAMING_SCHEMA.json aws_fixed puts outside the domain.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W7-S2",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "SCHEMA: org/standards/NAMING_SCHEMA.json aws_fixed @32855486f0: 'names AWS fixes are OUTSIDE the grade's domain, like the NOT GRADED types: excluded, never a fourth verdict'. by_arn: an IAM_POLICY in account aws. by_name: SECURITY_GROUP default; LOG_GROUP RDSOSMetrics and the prefixes aws-waf-logs- and /aws/ecs/containerinsights/.",
   "CODE: lib/opal_naming.py grade() @32855486f0 raises G2.1 on SECURITY_GROUP 'default', G2.2 on an IAM name starting AWS or Amazon, and G2.3 on a log group not starting with / (GRADING_RULE.md G2, which predates AW1; row LGIC_ENFORCE-W3-S4 records the same departure)."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W7-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The order names the repo surfaces (Terraform, config.py-class files, Lambda sources) but not how a source literal is placed as a name or what 'Lambda sources' excludes. The census applies its own stated rule, so the repo denominator of 1869 is that rule's.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W7-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "ORDER: the TO-EN-s-1 WORKER FACE names the surfaces only, as does PRD DEC-7 (org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:292-293 @32855486f0). The gate's inputs (:257-265) name the literal classes: S3 key and bucket literals, resource-name literals 'the schema's resource grammar places as a name', and secret paths. They give no placement procedure.",
   "RULE APPLIED (lib/opal_naming.py _census_classify, in this order's commit): an s3:// URL is a bucket and a key; under a *bucket* binding, a bucket; under a secret, secret_name, _id, _arn or _path binding, a secret path; under a *key* or *prefix* binding and carrying a /, a key; otherwise, a kebab literal whose last token is a kind exactly one node type owns. Terraform: the name attribute of 28 resource types (CENSUS_TF_ATTR) when it is one literal; 113 interpolated names are not judged."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W7-S4",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "EN-s-2 sets the census totals beside N2, N6 and IV7, but the census it reads judged 3 of 1805 live names and 0 of 1869 repo names, all API_GW. So the names graded by both are 1 (N2) and 2 (N6), and IV7 grades no name. The comparison holds for those 3 names and says nothing about the estate.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W7-S4",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "CENSUS: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md@f64b6f35cb json fence: denominators judged_live 3, live_nameable 1805, judged_repo 0, repo 1869; 3 rows, all API_GW live (inf-otp-relay-api OUT-OF-PATTERN, opal-portal-data-proxy-api CONFORMANT, opal-session-analytics-api CONFORMANT); stopped on API_GW sentiment-query-api (row LGIC_ENFORCE-W7-S1).",
   "RECOUNT (a scratch script in the worktree's .scratch, not a deliverable, matching on (name, type)): 'N2 WORKED CASES: 43', 'N2: graded by both 1  agree 1'; 'N6 GRADER-A ROWS: 88', 'N6: graded by both 2  agree 2'; 'STOP NAME ('sentiment-query-api', 'API_GW') in N2: False  in N6: False'; 'IV7 RANKED ROWS: 10', and IV7 mentions none of the 3 census rows or the stop name."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S11",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "grade() reads its system vocabulary from infra/logic/registry/systems.json, where astn, trade and news are unresolved, so it RAISES on a name whose system slot needs one of them, where GRADING_RULE.md V1 lists all three as PRODUCT systems and gives a verdict.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S11",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "RULE: GRADING_RULE.md @ce7349b7cc V1 :91 lists irpt, advi, yang, news, astn, amgt, trade as PRODUCT; :95-97 'V1 is INTERIM. The registry rows belong to LGIC_ENFORCE (PRD CONTRACTS row 3)'.",
   "REGISTRY: infra/logic/registry/systems.json @a925c8a642 'unresolved' holds astn, trade and news, for want of a citable owner_directive (row LGIC_ENFORCE-W1-S6)."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S6",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Nine of the sixteen system rows carry an owner_directive the register does not state (owner_claim inferred), and astn, trade and news, which GRADING_RULE.md V1 lists as PRODUCT systems, are held unresolved because no owner can be cited.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S6",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S5",
   "CENSUS: org/missions/DIRECTIVES.yaml @e0171ca585, a whole-token case-insensitive read attributed to each D-code block: yang 2 lines (D9), ycharts 4 (D9), smartx 2 (D3, D9), schwab 2 (D2, D3), trueshares 4 (D4); news, astn, trade, fred, seeking, orion, eclipse, blackdiamond and pathfinder 0 each.",
   "CENSUS: the mission tree org/missions/D<n>/<MACRO>/<CODE> @e0171ca585, 18 project directories: none is a yang, news, astn, trade, fred, seeking-alpha or vendor-feed project."
  ],
  "remedy": "Registry rows (infra/logic/registry/systems.json) or rule steps for the 115 raising system tokens, ruled at the round-1 analysis; then EN-s-1 re-run to a complete census and EN-s-2 re-compared on it. FWD-5 is NOT REALIZED by this round.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S19",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "TO-EN-x-1 step 2 asks for 49financial's SHORT form to change in scopes.json and be regenerated. lib/opal_naming.py validate refuses any short that differs from org/standards/NAMING_SCHEMA.json firm_forms, which pins '49f', and generate refuses with it. NAMING_SCHEMA.json is outside the order's <paths>, so no 'after' commit can exist inside the grant and X1-AC3 cannot pass.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S19",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S6",
   "RUN 2026-09-15T~10:15Z on the practice copy (branch prac-lgic-enforce-x1 @104f092d69), after the change \"short\": \"49f\" -> \"short\": \"f49\" in infra/logic/registry/scopes.json (1 occurrence): 'python lib/opal_naming.py validate' printed \"REFUSED scopes.json[0].short: 'f49': NAMING_SCHEMA.json firm_forms gives '49f'\" and 'VALIDATE: REFUSED 1 refusal(s), 9 warning(s)', rc=1.",
   "RUN, same tree: 'python lib/opal_naming.py generate --out .scratch/gen_after' printed 'ERROR: the registry is refused (1 refusal(s)); run: python lib/opal_naming.py validate', rc=1. Nothing was generated."
  ],
  "remedy": "1.0.0_SA_CTO rules whether FWD-2 and FWD-7 mean one carrier: either firm_forms is generated from scopes.json (or scopes.json reads firm_forms), and the module test file is rendered by the generator; or the PRD states the second list. Then X1-AC3 is re-cut with a grant that can pass.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-16T12:43Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W8-S2",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Firm N+1 as one scopes.json row is not all the registry asks for: validate prints 'WARN scopes.json[3].key: firm 'quillwater' is not in NAMING_SCHEMA.json firm_forms', and scopes.json itself says firm_forms owns which firm short forms exist. Generate and the gate proceed on the row alone.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W8-S2",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S6",
   "RUN: 'python lib/opal_naming.py validate' in the practice copy after the row was added: 'WARN scopes.json[3].key: firm 'quillwater' is not in NAMING_SCHEMA.json firm_forms' ... 'VALIDATE: OK 16 system row(s), 10 scope row(s), 10 warning(s) at registry@8f946960611a1880', rc 0. Then 'GENERATE: 9 written, 0 skipped, into . at registry@8f946960611a1880'.",
   "CODE: lib/opal_naming.py:286-290 @652d3a2204. A FIRM row whose key is absent from firm_forms is appended to warnings, never refused. generate() (:1391-1393) stops only on refusals."
  ],
  "remedy": "1.0.0_SA_CTO rules whether FWD-2 and FWD-7 mean one carrier: either firm_forms is generated from scopes.json (or scopes.json reads firm_forms), and the module test file is rendered by the generator; or the PRD states the second list. Then X1-AC3 is re-cut with a grant that can pass.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S12",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "terraform test cannot iterate run blocks, so infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl runs the 32 generated vectors as 32 indexed run blocks plus a coverage run that refuses any other count; a registry that grows the vectors fails terraform test until a run block is added by hand.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S12",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S6",
   "ORDER: TO-EN-m-1 WORKER FACE 'A terraform test file runs every vector through the module's name output' and 'You may extend lib/opal_naming.py's generator only to render the locals and vectors', so the test file is hand-held, not generated.",
   "TOOL: Terraform v1.9.8 (C:/Users/AndrewBerman/Desktop/ajb_workspace/.tools/terraform.exe version). A run block takes no for_each or count, and check_en.py m1_vectors counts passed run blocks against the vector count ('int(m.group(1)) >= len(rows)', check_en.py:523 @1ca17cc88e)."
  ],
  "remedy": "1.0.0_SA_CTO rules whether FWD-2 and FWD-7 mean one carrier: either firm_forms is generated from scopes.json (or scopes.json reads firm_forms), and the module test file is rendered by the generator; or the PRD states the second list. Then X1-AC3 is re-cut with a grant that can pass.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S8",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "To generate the eight carriers from the registry, scopes.json rows carry fields DEC-1 does not list (tenant, masters, monolith_scopes, pipeline_trees, trees, bucket_provisioned, and the alias fields planes, routed and provisioned), and a scope's bucket is its ruled opal-data-{long} form with the live legacy bucket an alias.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S8",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S6",
   "PRD: LGIC_ENFORCE_PRD.md DEC-1 :173 @78128f29ea: 'scopes.json rows: key, class, long, short, tenancy, bucket, aliases.'",
   "FILES @e0171ca585: data/firm_registry.json carries display_name, kind, enabled, email_domain, the portal/mdpf/pipeline scopes, tree_token and five nullable bindings per firm; firm-config.mjs:65-94 a displayName per tenant, mockadv included; perfrp_firm_pin.py:33-42 the ADVI tree; ds-precommit-check.py:68-71 and :110-113 the pipeline-directory separations. None of these is one of DEC-1's seven scope fields."
  ],
  "remedy": "1.0.0_SA_CTO rules whether FWD-2 and FWD-7 mean one carrier: either firm_forms is generated from scopes.json (or scopes.json reads firm_forms), and the module test file is rendered by the generator; or the PRD states the second list. Then X1-AC3 is re-cut with a grant that can pass.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W8-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "D2-AC2's instrument, check_en.py d2-control, never plants or searches anything. It passes if the worker-written control field in EXERCISE_FWD1_SEARCH.md has hits == 1 and a non-empty planted string, so the verdict repeats the graded worker's own number.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W8-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "CODE: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py:1129-1131 @9a05002d39. d2_control reads fenced_json(EXERCISE_FWD1_SEARCH.md).get('control') and prints PASS-CONTROL-FIRES if c.get('hits') == 1 and c.get('planted'). It runs no git show and no search, and writes no scratch copy.",
   "CODE, the contrast: the same file :1120-1126 @9a05002d39 (d2_zero) re-reads the committed pipeline with git show <commit>:<path> and re-searches it with its own regex, so D2-AC1 does not rest on the worker's hits field alone."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S21",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "check_en.py x1-moves-both counts a NAME line as any added diff line carrying the new short form and the text 'role', and a FENCE line as any added line carrying it and '*'. The regenerated fence-pattern line in generated_locals.tf ('arn:aws:iam::313476888478:role/*-<short>-*') satisfies both, so X1-AC3 would read PASS-BOTH-MOVE on a diff in which only the fence pattern moved.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S21",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "CODE: check_en.py:1188 @c6d652a6dc 'name_lines = [ln for ln in out.splitlines() if ln.startswith(\"+\") and new_short and new_short in ln and \"role\" in ln]', and :1189 'fence_lines = [... new_short in ln and \"*\" in ln]'. One line may satisfy both filters.",
   "FILE: infra/aws/terraform/modules/opal_name/generated_locals.tf:66 @c6d652a6dc '\"49financial\" = [\"arn:aws:iam::313476888478:role/*-49f-*\"]' carries both 'role' and '*', and regenerates with the new short form."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  }
 },
 {
  "id": "LGIC_ENFORCE-W3-S7",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The issuer's bad_tree name BadQueueName is not OUT-OF-PATTERN: grade('BadQueueName','SQS_QUEUE') RAISES (R1.f: 'bad' is in no vocabulary), so no canonical form exists to print; the limb refuses it under DEC-6's RAISE row and prints '-> (rule or registry defect)'.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S7",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "MEASURED: lib/opal_naming.py @39aae459ed grade('BadQueueName','SQS_QUEUE') raises RaiseDefect \"R1.f: 'bad' is in no vocabulary; no registry row resolves it\"; so do 'badqueuename' and 'bad-queue-name'. grade('etfs-price-refresh-queue','SQS_QUEUE') -> ('CONFORMANT', 'etfs-price-refresh-queue').",
   "RULE: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:255 @78128f29ea: a RAISE is 'printed as a rule or registry defect, never as a verdict, and refused like any refusal once enforcing'. The limb prints 'NAMING REFUSE .../t2/bad_tree/main.tf:2 BadQueueName -> (rule or registry defect)', why 'RAISE as SQS_QUEUE: a rule or registry defect, not a naming verdict: R1.f ...', and exits 1 under NAMING_GATE_ENFORCE=1."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W5-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "EN-v-3's generated firm_bucket_map() returns the same five tenant->bucket pairs as its pre-image, in a different ITERATION ORDER: registry order (49financial, inflection, cottonwood, mockadv, demo) where the pre-image returned firm-config.mjs order (49financial, inflection, mockadv, demo, cottonwood). check_en.py compares the exports with ==, which does not see order.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W5-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "PRE-IMAGE @b02fdaa849: data/assets/scripts/gold/investor_reporting/directory_runner.py:170-174 and holdings_snapshot.py:145-153 parse FIRM_CONFIG out of infra/aws/lambda-edge/_shared/firm-config.mjs, whose tenant blocks sit at :66 49financial, :70 inflection, :74 mockadv, :78 demo, :87 cottonwood.",
   "VIEW (branch wk-lgic-enforce-1-5, generated at registry@50e4fabd1cb6a150): directory_runner.py:170-180 and holdings_snapshot.py:145-155 return a dict literal ordered 49financial, inflection, cottonwood, mockadv, demo."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W4-S2",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The first generation of firm-config.mjs re-orders FIRM_CONFIG's keys (base 49financial, inflection, mockadv, demo, cottonwood; generated 49financial, inflection, cottonwood, mockadv, demo), so Object.keys of FIRM_CONFIG and of FIRM_BUCKET_MAP change order, and check_en.py v2-delta0 cannot see order: an order-only mutant reads EQUAL.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W4-S2",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "BASE, run: node .scratch/ctl/keys.mjs over git show b02fdaa849:infra/aws/lambda-edge/_shared/firm-config.mjs -> [\"49financial\",\"inflection\",\"mockadv\",\"demo\",\"cottonwood\"] for both FIRM_CONFIG and FIRM_BUCKET_MAP; both frozen.",
   "LIVE, run: the same over the generated file (python lib/opal_naming.py generate --out . --target infra/aws/lambda-edge/_shared/firm-config.mjs, registry@50e4fabd1cb6a150) -> [\"49financial\",\"inflection\",\"cottonwood\",\"mockadv\",\"demo\"] for both; both frozen. The GENERATED block is firm-config.mjs:65-88 in the worktree wk-lgic-enforce-1-4-v2."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W5-S4",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "check_en.py's v4-delta0 probes loaders.py bucket_for in a process where IRPT_DIRECTORY_BUCKET_MAP is unset, so all 11 probes raise BucketUnmapped in both copies: a change to bucket_for's return path reads EQUAL and prints PASS-DELTA0.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W5-S4",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S7",
   "INSTRUMENT: fixed_inputs/check_en.py:211-221 @b02fdaa849 (exports_of) calls bucket_for(t) for 11 probe tokens in-process and records repr(result) or 'raises <class>'. Of its 1175 lines, only :105 (run(): e = dict(os.environ), a subprocess env) and :519 (SAFE_APPLY_TERRAFORM) touch os.environ, and no line reads or sets IRPT_DIRECTORY_BUCKET_MAP.",
   "SUBJECT: infra/aws/lambda/investor-reporting/_authz/loaders.py:29,43-53 @b02fdaa849: bucket_for reads the firm map from env IRPT_DIRECTORY_BUCKET_MAP (default '{}') and raises BucketUnmapped for a token not in it, so with the variable unset every probe takes the refusal branch."
  ],
  "remedy": "The issuer re-cuts each instrument to discriminate: d2-control plants its own copy, x1-moves-both separates the name line from the fence line, t2-refuse requires a canonical form, the delta0 compares include export order (or each view's header puts order out of contract), and v4-delta0 probes with the map set as well.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T02:38Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W3-S8",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "At apply there is no diff, so DEC-6's NEW/EXISTING split has nothing to read: the limb reads every graded name as the tree states it, and one switch (org/mcp/naming-gate.enforce) arms both limbs. Under ENFORCE, 57 of the 78 Terraform roots at HEAD would be refused before plan.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S8",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S8",
   "RULE: org/missions/D14/LGIC/LGIC_ENFORCE/prd/LGIC_ENFORCE_PRD.md:243-244 @78128f29ea: 'A string is NEW when it is on the diff's added lines and absent from the same file's pre-image'. An apply carries no diff, and whether a resource is being ADDED is known only to a plan, which the PRD (:290-291) and the cell place after this stage.",
   "MEASURED @39aae459ed with this build (deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_coverage.py): 78 directories hold a tracked .tf under infra/aws/terraform; 1266 resource-name attributes of the limb's 30 types; 1148 graded literals: 144 CONFORMANT, 3 NOT-GRADED, 593 REFUSE as OUT-OF-PATTERN or ALIAS, 408 REFUSE as RAISE; 118 expressions not graded. 57 of 78 roots carry at least one REFUSE verdict."
  ],
  "remedy": "Before gate G-F: an existing-name baseline or a separate switch for the apply limb, and an exemption for machine-written plan JSON (or a deliverable form the commit limb does not grade as hand-written).",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": null
  }
 },
 {
  "id": "LGIC_ENFORCE-W1-S22",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "TO-EN-x-1 orders fwd2_plan.json, a terraform show -json, committed under the worker's deliverables folder. The commit-time naming gate graded 151 names in that machine output, 115 NAMING REFUSE (every one on fwd2_plan.json) and 13 NAMING RAISE, and passed the commit only because org/mcp/naming-gate.enforce is absent (WARN mode). With enforce on, the gate would refuse the deliverable the order names.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S22",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S8",
   "RUN: bash .tools/safe-commit.sh of commit d49089952b on branch wk-lgic-enforce-1-1-x1, 2026-09-15T~10:40Z. Its log (352 lines) prints '[naming-gate] NAMING-GATE: WARN 151 graded', with 115 'NAMING REFUSE' lines and 13 'NAMING RAISE' lines. All 115 REFUSE lines name org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/fwd2_plan.json:1, the one-line JSON.",
   "RUN, same log: 'NAMING REFUSE .../fwd2_plan.json:1 advi-49f-fwd2-exercise-queue -> advi-49f-fwd2-exercise-queue', why: \"CONFORMANT as SQS_QUEUE, but a NEW hand-kept carrier of '49f' outside every permitted context: read it through lookup('49financial')\". This is the cell's own resource, named by module opal_name."
  ],
  "remedy": "Before gate G-F: an existing-name baseline or a separate switch for the apply limb, and an exemption for machine-written plan JSON (or a deliverable form the commit limb does not grade as hand-written).",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-16T12:30Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W5-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "The order's proof validation, run as a dry run before the flip (nothing staged, per Rule 14a's no pre-add), returns INVALID rc=1 for an EN-v cell. Its artifacts are MODIFIED tracked carriers, and proof-of-spec-check.py:383-386 refuses any PENDING-THIS-COMMIT path that is tracked and unstaged as CCX ('ALREADY COMMITTED at HEAD'). The same instance reads VALID rc=0 against a temporary index holding the commit's paths.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W5-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S9",
   "EXERCISED dry run (branch wk-lgic-enforce-1-5, nothing staged): 'VIOLATION: artifact-resolution: data/assets/scripts/gold/investor_reporting/directory_runner.py is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged' and the same for holdings_snapshot.py; 'INVALID (rc=1)'.",
   ".tools/proof-of-spec-check.py:344-354 and :379-386 @b02fdaa849: an unstaged instance sets ctx PRE-COMMIT with dry_run true, and a tracked, unstaged PENDING path is refused at :383 before the dry_run branch at :387 is reached. The comment at :352-353 says the CCX refusal stands in both runs 'because that artifact cannot ride this commit whatever gets staged'."
  ],
  "remedy": "The checker's author makes the pre-flip run grade a tracked, modified, unstaged PENDING-THIS-COMMIT artifact as it will be committed (for example against a temporary index), so 'validate before the flip' and Rule 14a can both be followed.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T02:38Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W5-S5",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "proof-of-spec-check.py's pre-flip dry run refuses a PENDING-THIS-COMMIT artifact that is a TRACKED file modified in place and not staged as 'ALREADY COMMITTED at HEAD' (CCX class), so an EN-v carrier regenerated at its existing path reads INVALID rc 1 until it is staged, while Rule 14a says not to pre-git add.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W5-S5",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S9",
   "CHECKER: .tools/proof-of-spec-check.py:379-388 @b02fdaa849 (checker-vintage da3e61889d). In PRE-COMMIT: a staged artifact is co-committed; otherwise a path `ls-files --error-unmatch` finds tracked is the CCX violation; only after that does `elif dry_run` grant PENDING. Its comment at :348-354 describes the dry-run case for UNTRACKED artifacts only.",
   "SUBJECT: infra/aws/lambda/investor-reporting/_authz/loaders.py is tracked at b02fdaa849, and its worktree bytes differ from HEAD by +4 comment lines, so the change is not already committed."
  ],
  "remedy": "The checker's author makes the pre-flip run grade a tracked, modified, unstaged PENDING-THIS-COMMIT artifact as it will be committed (for example against a temporary index), so 'validate before the flip' and Rule 14a can both be followed.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W6-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "EN-v-5 could not commit the carrier, instance and flip together. Before staging, proof-of-spec-check refuses a PENDING-THIS-COMMIT row on a MODIFIED tracked carrier, and Rule 14a forbids pre-staging, so the carrier went in its own commit efacdee1e0 and the proof pins it.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W6-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S9",
   "RUN: python .tools/proof-of-spec-check.py <EN-v-5 instance> V5-AC1,V5-AC2 with the carrier row at PENDING-THIS-COMMIT and the carrier modified but unstaged in wk-lgic-enforce-1-6: 'VIOLATION: artifact-resolution: 'data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py' is PENDING-THIS-COMMIT but is ALREADY COMMITTED at HEAD and NOT staged -- it will not ride this commit; pin the row to the commit that carried it (CCX class)' INVALID (rc=1).",
   "CODE: .tools/proof-of-spec-check.py:379-384 @b02fdaa849. In PRE-COMMIT context a PENDING row passes only when the path is in `git diff --cached`; a path that is tracked (ls-files --error-unmatch) and not staged is refused, whether or not the worktree changed it."
  ],
  "remedy": "The checker's author makes the pre-flip run grade a tracked, modified, unstaged PENDING-THIS-COMMIT artifact as it will be committed (for example against a temporary index), so 'validate before the flip' and Rule 14a can both be followed.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S17",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "After EN-f-2's drain @c6d652a6dc, the shared index carried the pre-drain blobs of 2 drained paths (TO-EN-f-2 and this channel), staged with no merge in progress. Committed as it stood, the index would have flipped TO-EN-f-2 back to pending and removed row W1-S18, silently reverting the drain.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S17",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S10",
   "MEASURED 09:59Z-10:05Z on the primary checkout: 2 paths staged, no MERGE_HEAD, no index.lock. TO-EN-f-2's staged blob e4b65cfcfc reads '<status>pending</status>', where HEAD reads complete. The channel's staged blob 2855206f3a holds 65 rows, without W1-S18, where HEAD holds 66. Each staged blob equals its version at c6d652a6dc^1, the CLOUD commit before the drain.",
   "The working tree and HEAD (23cad64541) both held the drained versions: git diff HEAD on the 2 paths was empty. The staged entries were the only stale copy."
  ],
  "remedy": "Identify the writer that restores the shared index around its own commit, and run the first-parent-vs-branch diff census over other seats' drains; safe-merge.sh checks the recorded paths against the branch's own diff before it prints MERGED.",
  "owner": "0.0.0_AB_MSTR",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "0.0.0_AB_MSTR",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S18",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Correction to LGIC_ENFORCE-S17: the index restore did more than leave stale staging. It truncated the drain itself. Merge c6d652a6dc recorded 2 of EN-f-2's 8 changed paths, so CLOUD kept the probe-roles .tf and the open-deploy sentinel and lacked the closed entry, FENCE_PROBES.md, the proof and the result. Landed after the fact in 3 commits.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S18",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S10",
   "MEASURED: git diff --name-status c6d652a6dc^1 c6d652a6dc lists 2 paths (TO-EN-f-2, INVESTIGATION_v1.md). The branch changed 8 more against the merge base; one, check_en.py, was already equal on CLOUD. lgic-enforce-fence-probes.tf and the .open_deploys sentinel were PRESENT at c6d652a6dc and at HEAD, and absent at c6d652a6dc^2. The shared working tree showed them as unstaged deletions.",
   "CENSUS: all 55 merge commits by 2.0.0_SA_COO~G since 2026-09-14 12:00Z. A path counts as dropped when the merge's blob differs from the branch tip's while CLOUD's side left the path untouched. Result: 1 of 55 affected (c6d652a6dc), 6 paths."
  ],
  "remedy": "Identify the writer that restores the shared index around its own commit, and run the first-parent-vs-branch diff census over other seats' drains; safe-merge.sh checks the recorded paths against the branch's own diff before it prints MERGED.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S20",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "CLOUD @c6d652a6dc still declares the three LGIC fence-probe roles and their three policies in infra/aws/terraform/shared-infra/lgic-enforce-fence-probes.tf, which EN-f-2 removed from AWS. A read-only plan of shared-infra from that tree therefore creates 6 resources besides this cell's queue, and an apply of shared-infra from CLOUD would create them again.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S20",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S10",
   "RUN 2026-09-15T~10:10Z: terraform v1.9.8 plan -lock=false of infra/aws/terraform/shared-infra from the practice copy (base c6d652a6dc plus this cell's .tf), against the real S3 backend: 'Plan: 7 to add, 0 to change, 0 to destroy.' Creates: aws_iam_role.lgic_fence_probe[\"49f\"], [\"cot\"] and [\"unscoped\"]; aws_iam_role_policy.lgic_fence_probe_read[\"49f\"], [\"cot\"] and [\"unscoped\"]; aws_sqs_queue.lgic_enforce_fwd2. Plan JSON: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/fwd2_plan.json (239 resource_changes, 7 not no-op).",
   "RUN, check_en.py x1-plan on that JSON, 2026-09-15T~10:22Z, lists the planned create names 'mdpf-49f-fenceprobe-role', 'mdpf-cot-fenceprobe-role', 'mdpf-fenceprobe-role' and three 'fenceprobe-read-opal-data-49financial'."
  ],
  "remedy": "EXECUTED @8c77a1400a (2.0.0_SA_COO~G): lgic-enforce-fence-probes.tf deleted as the worker did; absent at HEAD 6a2beed8d2 by this seat's read. Nothing further is owed for this row; the mechanism behind it is S17's.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T11:02:20Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W3-S4",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADING_RULE.md is written against NAMING_SCHEMA.json v1.4 but the base carries v1.6: rule G2.3 RAISES log groups prefixed aws-waf-logs-, which v1.6 aws_fixed places outside the grade's domain, and 2 Terraform names hit it; FN1-FN4 (v1.5) are not in the rule either.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S4",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S11",
   "RULE, read: GRADING_RULE.md@fd9c9ca174 header (:7) 'org/standards/NAMING_SCHEMA.json v1.4, cited as DATA.<field>'; G2.3 (:56-57): 'A LOG_GROUP whose name does not begin with / (for example aws-waf-logs-*, RDSOSMetrics) ...' under G2, whose outputs RAISE.",
   "SCHEMA, read: org/standards/NAMING_SCHEMA.json@fd9c9ca174 version v1.6; aws_fixed.rule: 'names AWS fixes are OUTSIDE the grade's domain, like the NOT GRADED types: excluded, never a fourth verdict'; aws_fixed.by_name.LOG_GROUP includes 'prefix: aws-waf-logs-'. resource.function (FN1, v1.5): 'an agent noun is always written as its verb (publisher -> publish ...)'."
  ],
  "remedy": "Rule on each reading: re-grade GRADING_RULE.md against the current schema (G2.3 and aws_fixed), write the camel-rejoin and bucket-as-container steps into the rule or drop them from grade(), and name the Terraform type to node type map the flagger uses.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S9",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The IV.3 control CloudWatchLogs (IAM_POLICY) OUT-OF-PATTERN does not follow from GRADING_RULE.md as written, which RAISES it at R1.f; grade() reaches the order's verdict only by rejoining the camel pieces of one word into a vocabulary word (cloud+watch -> cloudwatch), a step the rule does not state.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S9",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S11",
   "RULE: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md @ce7349b7cc (byte-identical at HEAD 2a6c7d8543): N2 :68-70 splits before each capital, so CloudWatchLogs gives cloud, watch, logs; V3 :109-110 lists the purpose word cloudwatch as one token; R1.f :149-150 'Any other t1 is in no vocabulary. RAISE'. V1 :92 states the one multi-token match the rule makes: seeking-alpha, 'two tokens, matched as one'.",
   "SIBLING: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md :2262, :2462, :2599, :2902, :3023 @1cc0d2fe73 grade the literal CloudWatchLogs 'RAISE ... R1.f: t1 cloud is in no vocabulary'."
  ],
  "remedy": "Rule on each reading: re-grade GRADING_RULE.md against the current schema (G2.3 and aws_fixed), write the camel-rejoin and bucket-as-container steps into the rule or drop them from grade(), and name the Terraform type to node type map the flagger uses.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S10",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The IV.3 control opal-data-inf/silver/x (S3Key) OUT-OF-PATTERN naming {source} does not follow from GRADING_RULE.md K1, which RAISES a key whose segment 1 is neither a source nor a tier; grade() reaches it by taking a bucket the registry knows out of segment 1 as the key's container.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S10",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S11",
   "RULE: GRADING_RULE.md @ce7349b7cc K1 :254-259 'Anything else RAISES, because segment 1 is neither a source nor a tier'; K5.c :284-285 'The S3Key node carries no bucket, and the bucket is what decides them'.",
   "SCHEMA: org/standards/NAMING_SCHEMA.json key.container '{bucket} -- the bucket that holds the key; NEVER a segment of the key'."
  ],
  "remedy": "Rule on each reading: re-grade GRADING_RULE.md against the current schema (G2.3 and aws_fixed), write the camel-rejoin and bucket-as-container steps into the rule or drop them from grade(), and name the Terraform type to node type map the flagger uses.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "GRADING_RULE.md grades (name, node_type) over the schema's 33 node types; no Terraform resource type is a node type and TO-EN-t-1 gives no map, so EN-t-1 graded under its own map of 34 Terraform types onto node types and RAISED the rest at G1.1.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S11",
   "RULE, read: org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md@fd9c9ca174 G1.1 (:35-36): 'The type must be one of the 33 keys of DATA.kind.by_type and DATA.types_not_graded_by_kind, spelled exactly. Any other type RAISES.' org/standards/NAMING_SCHEMA.json@fd9c9ca174 node_type_vocabulary: every type key is a node_type value of the live-plane graph.",
   "CENSUS, run: deliverables/0.9.0_WK_LGIC_ENFORCE~3/instrument/census.py over the 468 tracked .tf files @fd9c9ca174 reads 2,035 resource blocks of 104 Terraform types: 34 mapped (28 to a graded node type, 6 to a NOT GRADED one), 30 that carry their own name and map to none, 40 that name nothing."
  ],
  "remedy": "Rule on each reading: re-grade GRADING_RULE.md against the current schema (G2.3 and aws_fixed), write the camel-rejoin and bucket-as-container steps into the rule or drop them from grade(), and name the Terraform type to node type map the flagger uses.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S2",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "124 of the 1,332 Terraform name attributes are expressions, not names; the rule grades a written name, so EN-t-1 resolved 100 statically in their own directory (graded, value_claim inferred) and could not place 24 (22 RAISE at G3, 2 decided at G1.2).",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S2",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S12",
   "RULE, read: GRADING_RULE.md@fd9c9ca174 G3 (:62-79) normalises a written name; NAMING_SCHEMA.json@fd9c9ca174 grade.unplaceable: 'A name the tokeniser cannot place ... RAISES.' Neither says what a Terraform expression (local.x, var.x, a template with each.key) is.",
   "CENSUS, run: census.py over the 468 tracked .tf files @fd9c9ca174: 1,208 literal values; 100 resolved through same-directory locals, variable defaults or same-directory resource name attributes (for example \"${local.bd49f_pull_name}-role\"); 24 not resolvable: 10 each.key, 4 var.firm with no default, 2 each.value.name, 2 var.function_name with no default, 2 a non-name attribute of aws_ses_domain_mail_from, 1 each.value, 1 local.firm_role_name[each.key], 1 var.firm_id, 1 each.value.family."
  ],
  "remedy": "Decide whether the naming limbs gain a plan-time pass over evaluated names and module-call arguments, or whether FWD-4's grade states that it covers literal names only.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-EN-t-1 names role_name as a resource-name attribute, but no tracked resource block carries one; the names that module calls author (122 literal function_name arguments across 146 module blocks) are module arguments, outside a census of resource attributes.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S12",
   "SEARCH, run: native Grep for the whole word role_name over infra/aws/terraform/*.tf in the worktree @fd9c9ca174: 0 occurrences across 0 files. POSITIVE CONTROL on the same path: the whole word function_name or a _role_name suffix, 462 occurrences across 155 files (the _role_name hits are local and variable names such as var.processor_role_name).",
   "CENSUS, run: census.py @fd9c9ca174 reads 146 top-level module blocks; their literal name-like arguments are 122, all function_name; the called module names its resource by var.function_name, which has no default inside the module directory, so a resource-attribute census cannot read those names."
  ],
  "remedy": "Decide whether the naming limbs gain a plan-time pass over evaluated names and module-call arguments, or whether FWD-4's grade states that it covers literal names only.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S9",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The order says the limb grades every resource-name attribute, but 118 of 1266 at HEAD are expressions (references, calls, templates) whose value exists only in a plan. The limb runs before plan, so it lists them as 'unresolved before plan' and grades none of them.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S9",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S12",
   "MEASURED with deliverables/0.9.0_WK_LGIC_ENFORCE~3/controls/t2_coverage.py @39aae459ed: 1266 attributes, 1148 literal, 118 expression, 0 reading a module whose source is opal_name. At the census base fd9c9ca174 the limb's reader and EN-t-1's census (its own tfscan.py) agree row for row: 1266 and 1266, 0 one-sided, the literal/expression split 1148/118 identical, 0 literal values differing.",
   "MEASURED: grade('etfs-{x}-queue','SQS_QUEUE') raises 'G3: the tokeniser cannot place a character of a resource name'. A template graded with the commit limb's {x} placeholder would RAISE, and under ENFORCE be refused, whatever it resolves to."
  ],
  "remedy": "Decide whether the naming limbs gain a plan-time pass over evaluated names and module-call arguments, or whether FWD-4's grade states that it covers literal names only.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The L6 coverage limb of the TO issuance gate reads every cell id a decomposition CITES as one of its own cells, so a decomposition that cites another project's cells cannot be covered by its own orders; and the audited override its refusal text offers is never read by that limb.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "REFUSAL, exercised: this project's first L6 attempt (no commit was made) printed 'the issuance under org/missions/D14/LGIC/LGIC_ENFORCE/project.json owns 22 of 26 cell(s) ... MISSING: LN-f-1, LN-g-1, LN-h-3, LN-l-1'. All four are LGIC_NAMING cells that decomposition v1 @8d1d4d3e2f CITES, at :76, :89, :157, :159, :209, :305, :390 and :468 (10 citations).",
   "CODE, read: .tools/to-pipeline-gate.py@a369a0f55d _coverage_gap (:414-419) takes set(CELL_ID_RE.findall(decomp_text)) over the whole document, with no project scoping; CELL_ID_RE (:262-267) accepts any [A-Z][A-Z0-9]*- prefix."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S9",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Two slots minted duplicate row ids from separate branches: slot ~4's EN-v-1 and EN-v-2 both minted W4-S1, and slot ~5's EN-v-3 and EN-v-4 both minted W5-S1 and W5-S2. The issuer renumbered the later branch's rows before its drain (W4-S2; W5-S4, W5-S5) under an audited override, and names each later spawn's first row id.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S9",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "SURFACED_AT: W4-S1 at 00:18Z (EN-v-1) and 00:59Z (EN-v-2); W5-S1 and W5-S2 at 00:40Z (EN-v-3) and at 01:05Z and 01:19Z (EN-v-4). The earlier row keeps its id.",
   "RENUMBER COMMITS on the worker branches: b484d8dec4 (EN-v-2) and 8298325909 (EN-v-4). Each changes the row ids and their references in that branch's proof instance and result file. EN-v-4's also pins its loaders.py artifact row from PENDING-THIS-COMMIT to 56b867ac4c, the commit that carried it, because any later commit to the instance voids that sentinel (the checker's CCX remedy). Nothing else moves."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "comp-find's default corpus reads a worker's untracked <WS>/.scratch/, so a census saved there is counted by the next census run (198,931 phantom hits here), and an :(exclude) pathspec scans 0 files instead of excluding one.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "RUN 1, exercised at fd9c9ca174 with .scratch empty: a whole-word boundary pattern over the whole worktree -> 'DENOMINATOR: 374404 hit(s) across 32449 file(s)'; its --all output was saved to .scratch/census_all.txt (77,495,647 bytes).",
   "RUN 2, exercised: the order's segment pattern over the whole worktree -> 'DENOMINATOR: 387942 hit(s) across 32450 file(s)'; parsing its --all listing, 198,931 of those hits are lines of .scratch/census_all.txt, that is, run 1's output."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-14T22:07Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W2-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "comp-iam role <name>, the instrument TO-EN-c-2 names for the grant half, resolved 0 of the 94 roles the grants and belts name, although its own comp-iam roles listing carries 79 of them; a CamelCase control resolves.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W2-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "EXERCISED: 94 calls of 'timeout 120 comp-iam role <name>' in worktree wk-lgic-enforce-1-2 @fd9c9ca174, 2026-09-14 after 20:01Z: 94 of 94 printed \"No role matching '<name>'\" (for example bd-exporter-ec2-role, opal-portal-lambda-role). Output kept in the worker's .scratch/c2/compiam_role_out.txt, not committed.",
   "EXERCISED: 'comp-iam roles' at the same HEAD prints 'IAM ROLES (209 found)'; 79 of the 94 names appear in it with a source: line (bd-exporter-ec2-role: tf_resource bd_exporter)."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W3-S6",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "Even with Git Bash, safe-apply.sh stops at its halt checkpoint in a worker worktree: halt-gate-check.sh resolves the principal only from org/mcp/sessions/<CLAUDE_CODE_SESSION_ID>.serial or an orphan-cleaned marker under the worktree root, neither exists there, and it fails closed IDENTITY UNRESOLVED (exit 3) before the naming stage.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W3-S6",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "RESOLVER: .tools/halt-gate-check.sh:52-119 @39aae459ed reads the CLAUDE_CODE_SESSION_ID .serial file, then a <sid>.*.orphan-cleaned marker, then returns 1; :38 sets HALT_GATE_REPO_ROOT to the directory above the library, which is the worktree; :272-290 prints IDENTITY UNRESOLVED and returns 3. OPAL_AGENT_SERIAL is not read: it was exported for the run and the gate still blocked.",
   "MEASURED: CLAUDE_CODE_SESSION_ID=9d2c2e56-da40-4edc-ba9d-6924a8f8a17d. The worktree's org/mcp/sessions/ (gitignored, .gitignore:423) holds no file for it. The main tree's copy holds '2.0.0_SA_COO~G': the worker runs under the issuer's session id, so even a copied file would name the issuer, not the worker."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T05:19Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W1-S17",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "TO-EN-f-1 has the author hand-add SIGNOFF slots to the ledger entry, and the ledger tool does not keep them. deploy_ledger.py re-renders the whole entry from its sentinel on every close-leg, so EN-f-2's first close-leg erases both seats' SIGNOFF lines, the lines f2-signoff reads.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S17",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S13",
   "CODE: .tools/deploy_ledger.py _render_entry (:239-286 @39aae459ed) builds the entry from the sentinel's fields only: the header, the manifest and the log. _write_entry (:289-291) overwrites the file. Its docstring says 'open / close-leg / close / hold re-render the entry from the sentinel' and 'Never hand-edit an entry.'",
   "EXERCISED in memory, no file written: _render_entry of this ledger's sentinel returns 23 lines with no '## Sign-off', while the entry on disk has 34 lines, the section included. A sentinel with one more log event (a simulated close-leg) renders with no SIGNOFF line. Positive control: the render equals the on-disk entry up to its Log."
  ],
  "remedy": "Each tool's owner fixes its tool: the L6 coverage limb scoped to the project's own cells and the override honoured or dropped; row ids keyed by order or refused when minted on another open branch; comp-find honouring an exclude and not reading .scratch/; comp-iam role resolving the roles its listing carries; the halt checkpoint reading OPAL_AGENT_SERIAL (or the decomposition's pin corrected); deploy_ledger.py keeping hand-written lines at close-leg.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T10:05Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "Every LGIC_ENFORCE face's preflight says a path under .tools/ 'refuses by lane and is admitted only by this order's <paths>'. The owned-paths lane in fact admits ANY worker serial on .tools/, including a serial that holds no order. So the worker grant binds .tools/ only through the issuer's drain check, not through the lane.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S14",
   "EXERCISED, owned-paths-validate.py --check-agent at HEAD 94bd0afa97, 4 paths (.tools/naming-gate.py, .tools/naming-apply-gate.py, .tools/some-new-tool.py, lib/some_new_lib.py) for three serials: 0.9.0_WK_LGIC_ENFORCE~1 (six pending orders, none granting .tools/), 0.9.0_WK_LGIC_ENFORCE~9 (no order at all) and 0.9.0_WK_NOPROJECT~1 (no such project). Each printed 1 VIOLATION of 4, on lib/some_new_lib.py only; all three .tools/ paths were admitted.",
   "Found by G-C for slot ~1 before EN-r-1 spawned: the negative arm (.tools/naming-gate.py plus an infra .tf probe) refused 1 of 2."
  ],
  "remedy": "At the recut: the faces' .tools/ line says the drain check binds it (or the lane enumerates workers), each view's header hashes only the files it reads, and the commit limb validates the registry it reads.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S14",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "Adding the exemption rows moves the registry hash from 50e4fabd1cb6a150 to ba5318901b937130, so 7 generated views outside this order's grant now carry a stale GENERATED header. Their content is otherwise unchanged.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S14",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S14",
   "CODE: lib/opal_naming.py REGISTRY_FILES (:52 @39aae459ed) includes exemptions.json, and registry_hash (:92-101) hashes every registry file. RUN: 'VALIDATE: OK 16 system row(s), 9 scope row(s), 9 warning(s) at registry@ba5318901b937130' after the rows, where the base read 50e4fabd1cb6a150.",
   "READ: at base 39aae459ed, 50e4fabd1cb6a150 appears in 7 generated views outside TO-EN-f-1's <paths>: data/firm_registry.json, infra/aws/lambda-edge/_shared/firm-config.mjs, infra/aws/lambda/investor-reporting/_authz/loaders.py, data/assets/scripts/gold/runners_49f/perfrp_firm_pin.py, data/assets/scripts/gold/investor_reporting/holdings_snapshot.py, data/assets/scripts/gold/investor_reporting/directory_runner.py and .tools/ds-precommit-check.py. The module's two generated files are in the grant and were regenerated here."
  ],
  "remedy": "At the recut: the faces' .tools/ line says the drain check binds it (or the lane enumerates workers), each view's header hashes only the files it reads, and the commit limb validates the registry it reads.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T06:22Z"
  }
 },
 {
  "id": "LGIC_ENFORCE-W2-S9",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The registry's own validator refuses the fictitious row the order asks for, because the project is not in DIRECTIVES.yaml. The commit limb loads the registry without validating and still reads the row as live, so the refusal fired on a row validate refuses.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W2-S9",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S14",
   "python lib/opal_naming.py validate in the practice copy. Pre-plant (39aae459ed): 'VALIDATE: OK 16 system row(s), 9 scope row(s), 9 warning(s) at registry@50e4fabd1cb6a150', rc=0. Post-plant (6640c8153d): rc=1, 'REFUSED remediations.json[0].project: 'PRAC_FWD6REM' is not a project in org/missions/DIRECTIVES.yaml', 'REFUSED remediations.json[0].owner_directive: 'D14': the directive whose projects list names 'PRAC_FWD6REM'', 'VALIDATE: REFUSED 2 refusal(s), 9 warning(s)'.",
   "RULE: lib/opal_naming.py:414-420 @39aae459ed. LOAD WITHOUT VALIDATION: .tools/naming-gate.py:509 @39aae459ed calls mod._registry(), and lib/opal_naming.py:121-124 shows that is load_registry with no validate()."
  ],
  "remedy": "At the recut: the faces' .tools/ line says the drain check binds it (or the lane enumerates workers), each view's header hashes only the files it reads, and the commit limb validates the registry it reads.",
  "owner": "2.0.0_SA_COO~G",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~G",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W1-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The unscoped whole-segment carrier census finds 12,917 hand-kept firm carriers across 1,506 files outside DEC-5's eight definitions; this round's generated views cover only the eight.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W1-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S15",
   "CENSUS, exercised at HEAD fd9c9ca174: comp-find -i over the order's whole-segment pattern, 38 top-level pathspecs (the worktree minus .scratch and the .git pointer), --all -> 'DENOMINATOR: 189011 hit(s) across 32448 file(s) scanned in scope [corpus=all]'. Partition: 12,949 token-hit carriers + 176,062 excluded = 189,011, plus 4 definition-pattern carriers (row LGIC_ENFORCE-W1-S2). Record: org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/CARRIER_CENSUS.md, json keys carriers and outside_dec5_rows.",
   "RULE, read: the carrier test is LGIC_ENFORCE_PRD.md@78128f29ea :266-277 -- a firm token in a string literal outside (a) the registry files, (b) a generated file, (c) a builder or lookup argument, (d) prose, comments and */tests/* fixtures is 'a HAND-KEPT CARRIER ... a second copy of a registry row'. (c) is empty at fd9c9ca174: lib/opal_naming.py does not exist yet."
  ],
  "remedy": "Rulings at the round-1 analysis: FWD-3's grade names its eight-definition scope; which plane governs demo's tenancy (then the registry row and its note, or 02_DOCTRINE.md s.1, change); whether write logging reaches opal-data-49financial; and whether a consumer-test criterion grades against the base's own failures.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-S5",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The identity registry's demo row sets tenancy FIRM with the note 'a tenant class the doctrine does not define', while the doctrine defines demo as a DEMO-TENANT class, 'neither firm nor general' (02_DOCTRINE.md:60, ruled KEPT at :366-367; ledger X6), so the registry and the canon disagree on demo's tenancy.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-S5",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S15",
   "REGISTRY: infra/logic/registry/scopes.json row demo, read at HEAD (last written by LGIC_ENFORCE EN-r-1 @a925c8a642): class FIRM, tenancy FIRM, tenant.kind demo, note 'a tenant class the doctrine does not define (05_IDENTITY_SPINE.md s.3, tick-list row 17)'.",
   "DOCTRINE: infra/logic/02_DOCTRINE.md:60 '`opal-data-demo`: a tenancy class that is neither firm nor general -- serves prospective users with demo accounts (Andrew ~01:3xZ 09-13, KEPT)'; :366-367 'RULED card 8: KEPT as a DEMO-TENANT class (s.1 vocabulary)'."
  ],
  "remedy": "Rulings at the round-1 analysis: FWD-3's grade names its eight-definition scope; which plane governs demo's tenancy (then the registry row and its note, or 02_DOCTRINE.md s.1, change); whether write logging reaches opal-data-49financial; and whether a consumer-test criterion grades against the base's own failures.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W2-S3",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The served-key write trail logs platinum/firm/ writes on opal-data-bd, -inf and -cot only, so for opal-data-49financial no write is observed at all, not only writes outside platinum/firm/.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W2-S3",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S15",
   "LIVE READ: aws cloudtrail get-event-selectors --trail-name opal-served-key-write-trail, 2026-09-14 ~19:55Z: resources.ARN StartsWith arn:aws:s3:::opal-data-inf/platinum/firm/, arn:aws:s3:::opal-data-bd/platinum/firm/, arn:aws:s3:::opal-data-cot/platinum/firm/; readOnly false. No opal-data-49financial prefix.",
   "FILE: infra/aws/terraform/globgrph/item2e_served_write_trail.tf:30 @fd9c9ca174: served_write_trail_buckets = [\"opal-data-inf\", \"opal-data-bd\", \"opal-data-cot\"]."
  ],
  "remedy": "Rulings at the round-1 analysis: FWD-3's grade names its eight-definition scope; which plane governs demo's tenancy (then the registry row and its note, or 02_DOCTRINE.md s.1, change); whether write logging reaches opal-data-49financial; and whether a consumer-test criterion grades against the base's own failures.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false
 },
 {
  "id": "LGIC_ENFORCE-W4-S1",
  "project": "LGIC_ENFORCE",
  "fabric": "laptop",
  "class": "BLOCKING",
  "hazard_standing": "ARMED",
  "mechanism": "check_en.py v1-tests reads FAIL-CONSUMER-TESTS whatever data/firm_registry.json says: the same 14 tests in test_seam_paired.py fail at the base bytes and at the generated view, because they read the portal fixture from the primary checkout (12 keys) and routes.json (12 routes) against an asserted 11.",
  "evidence": [
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md@47f1045854#LGIC_ENFORCE-W4-S1",
   "org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/adjudications/ADJUDICATION_v1.md (same slug) row LGIC_ENFORCE-C-S15",
   "EXERCISED, a discriminating pair in worktree wk-lgic-enforce-1-4 @2a6c7d8543 where only the carrier varies: the four consumer test files with data/firm_registry.json at its HEAD bytes gave '14 failed, 95 passed' rc 1; with the generated view gave '14 failed, 95 passed' rc 1; the FAILED sets compared equal (14 = 14, IDENTICAL SET: True), every one in infra/aws/lambda/investor-reporting/_contracts/tests/test_seam_paired.py.",
   "EXERCISED, per file on the generated view: _keys/tests/test_keys.py 45 passed rc 0; _gate/tests/test_policy_completeness.py 3 passed rc 0; org/modules/graph/tests/test_comp_keys.py 8 passed rc 0; _contracts/tests/test_seam_paired.py 14 failed, 39 passed rc 1."
  ],
  "remedy": "Rulings at the round-1 analysis: FWD-3's grade names its eight-definition scope; which plane governs demo's tenancy (then the registry row and its note, or 02_DOCTRINE.md s.1, change); whether write logging reaches opal-data-49financial; and whether a consumer-test criterion grades against the base's own failures.",
  "owner": "1.0.0_SA_CTO",
  "round": "v1",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v1"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~G",
   "at": "2026-09-15T02:38Z"
  }
 }
]
```
