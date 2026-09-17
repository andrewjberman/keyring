# LGIC_LGCTFM -- surprise channel, INVESTIGATION v1

**Opened by:** `2.0.0_SA_COO~G`, 2026-09-16, at the project's L5. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate, folder == project).
**Append-only.**

**Why it is opened at L5.** The first row is a count disagreement between three carriers of ONE fixture's
denominator, found while building the decomposition's fixed inputs. It is a surprise against this project's own
PRD, so it is a row here, not a message.

**Denominator at this write: 1 row** -- `LGIC_LGCTFM-S1`, 2.0.0_SA_COO~G.

```json
[
  {
    "id": "LGIC_LGCTFM-S1",
    "project": "LGIC_LGCTFM",
    "fabric": "laptop",
    "surfaced_by": "2.0.0_SA_COO~G",
    "surfaced_at": "2026-09-16T17:20Z",
    "one_line": "THE FORK FIXTURE'S DENOMINATOR DISAGREES ACROSS THREE CARRIERS. PRD v1.1's cell candidate T4 says 'IV.5's FOUR positive forks'; the brief's IV.5, which is the carrier that ENUMERATES them, lists FIVE, each stated to be a positive control for O2; the brief's Part III O2 bar names THREE by way of example. A fixed input built on the PRD's four would under-cover the control set by one member and the fork cell's coverage claim would read clean while missing it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~G",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ENUMERATED BY SUBTRACTION FROM THE CARRIER THAT LISTS THEM, not by recall. Brief docs/briefs/d14-legacy-transform-brief-20260916.md section IV.5 states the rule ('A fork is two current resources whose DESIRED canonical form is ONE string') and then lists its measured members as SEMICOLON-SEPARATED clauses, closing with 'Each is a positive control for O2: a run over its subject that does not return it as a FORK row has a defect.' Splitting that sentence on its semicolons gives FIVE members.",
        "THE FIVE: (1) schwab/08335338/gold/ -- 2,108 json / 2,108 parquet, R18, the dual-write twin; (2) blackdiamond/49financial/{bronze,silver}_legacy/ beside {bronze,silver}/ -- 8,852 objects, dead 17d at census; (3) opal-data-assets/gold/mdpf_revamp/ (492) and portal/gold/ (415) -- both live, both JSON, one product; (4) opal-data-bd/canonical/schwab/{silver,gold} beside the monolith's schwab/08242234/silver/; (5) the naming census's bd / 49f / 49financial spellings of one firm across every resource type -- Lambda 20/9/1, role 20/12/1.",
        "THE NEGATIVE CONTROL IS UNAMBIGUOUS AND ALL THREE CARRIERS AGREE ON IT: smartx/platform/ beside smartx/account/{uuid}/ is NOT a fork (different jobs, one conformant, one R2-violating) and must grade as a TENSION. It is the whole discriminator -- a fork detector that fires on everything that looks alike passes every positive arm and is worthless.",
        "THE THREE CARRIERS, read at HEAD: PRD v1.1 @92154e0b63 cell-candidate row T4 fixtures column reads 'IV.5's four positive forks and the SmartX negative'. Brief IV.5 enumerates five. Brief Part III O2 names three inside em-dashes -- 'the Schwab gold twin, the two MDPF gold trees, the _legacy pairs' -- which reads as ILLUSTRATIVE rather than as a count, so O2 is not in conflict; the conflict is PRD four against IV.5 five.",
        "THIS SEAT PROPAGATED THE FOUR BEFORE MEASURING IT. The decomposition committed at 686d196fa1 says in section 3a 'IV.5's four POSITIVE forks (the Schwab twin, the two MDPF gold trees, the _legacy pairs)' -- which is the PRD's count welded to O2's three examples, a forward list assembled from two carriers and checked against neither. Rule 24(i) names exactly this shape: a forward list covers what its author had in mind and omits silently."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v1.1 T4: the fork fixture is IV.5's FOUR positive forks plus the SmartX negative.",
    "world_is": "The brief's IV.5 enumerates FIVE positive members and states that each is a positive control. Four would omit one.",
    "notes": "ARMED, disarm_owner 2.0.0_SA_COO~G -- this seat's, because the artifact that carries the defect is this seat's own decomposition and the fixed input that has not been written yet. NOT ADJUDICABLE and not routed: nothing in the PRD's RATIFIED text is touched, the cell-candidate table is explicitly the COO lane's to split, merge and re-sequence, and no other seat is blocked. THE ACT: FORK_CONTROLS.json is built with FIVE positives and the one negative, its denominator printed and this row cited, and the decomposition's section 3a is amended to five in the same commit. DISARM WHEN both land. * If 1.0.0_SA_CTO reads IV.5's fifth member -- the bd/49f/49financial spelling set -- as a NAMING tension rather than a fork, the count returns to four and this row disarms the other way; on the bytes it satisfies IV.5's own rule (several current spellings whose desired canonical form is one string) and IV.5 makes no exception for it, so five is what the carrier says. I am recording that reading rather than resolving it silently, because the fifth member is the only one of the five that is not a pair of PATHS."
  },
  {
   "id": "LGIC_LGCTFM-S2",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-17T14:15Z",
   "one_line": "DECOMPOSITION v1's CONSTRAINT 1 COUNTS THREE WRITERS OF lib/opal_lgctfm.py AND THE ROUND-1 CUT HAS FOUR: T6's plan is engine code (the PRD's PATHS row names lib/opal_lgctfm.py for T3-T9), so LT-p-1 on slot ~2 writes the engine after slot ~1's LT-e-1/e-2/e-3. Found at the L6 cut, before any order existed; v1.1 s.10 states it and the edge LT-e-3 -> LT-p-1 already sequences it.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "LGIC_LGCTFM_DECOMP.md s.5 CONSTRAINT 1 @686d196fa1: 'LT-e-1, LT-e-2 and LT-e-3 all write lib/opal_lgctfm.py ... this is the ONE file more than one cell writes'; s.3's table gives LT-p-1's write surface as 'the run directory' only.",
     "LGIC_LGCTFM_PRD.md v1.4 PATHS: 'new | lib/opal_lgctfm.py, lib/lgctfm_render.py, lib/tests/test_opal_lgctfm.py | T3-T9'; T6 (the plan) is inside that range and CONTRACTS names plan.json and plan.md as produced by the run, i.e. by engine code.",
     "LGIC_LGCTFM_DECOMP.md s.5 edges: 'LT-e-3 -> LT-p-1' -- so the fourth writer starts only after the third drains; no two open orders edit the engine at once."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "Decomposition v1 s.5 CONSTRAINT 1: three writers of lib/opal_lgctfm.py, one queue on slot ~1.",
   "world_is": "Four writers across two slots, sequenced by the existing edge set; LT-p-1's order grants lib/opal_lgctfm.py and says it starts after LT-e-3 drains. v1.1 s.10 records it.",
   "notes": "INERT: the count, not a cell or an edge, was wrong, and it was caught at the cut before any worker read it. The same seat wrote v1; a writer census taken from the cells' 'writes' column inherited that column's omission rather than re-reading the PRD's PATHS table."
  },
  {
   "id": "LGIC_LGCTFM-W1-S1",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_LGCTFM~1",
   "surfaced_at": "2026-09-17T14:30Z",
   "one_line": "LT-e-2's OWN GRADED CRITERION E2R1-AC1 (check_lt_r1.py e2-reproduce) NOW FAILS ON A RE-RUN AGAINST THIS ROUND'S WALK OUTPUT, THOUGH NOTHING IN LT-e-2's CELL CHANGED. This round (LT-e-3) plants a third resource whose node_type fits no type in NAMING_SCHEMA.json's 33-type vocabulary at all (COGNITO_USER_POOL, WORKER FACE's own requirement), and lib/opal_lgctfm.py now returns desired.verdict = NOT_COVERED for it per 11_LGCTFM_CONTRACT_SCHEMA_RECORD.md s.3.1's six-value verdict enum. check_lt_r1.py's core_reproduce (built for e2-reproduce, LT-e-2's own arm) treats ANY raising builder call as correct ONLY when desired.verdict == 'RAISE' -- it has no branch for NOT_COVERED, a verdict this round's own WORKER FACE mints. Re-running e2-reproduce now: 'rows with a builder call the checker can make: 278; reproduced: 277' and 'VERDICT: FAIL-E2-DESIRED-EQUALS-BUILDER'.",
   "class": "OBSERVATION",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py core_reproduce() (:585-610): 'good = cell_value(d.get(\"verdict\")) == \"RAISE\" and bool(...)' on any raised exception -- no NOT_COVERED branch.",
     "infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md s.3.1: 'desired.verdict | NAMING_SCHEMA.json grade.verdicts CONFORMANT | ALIAS | OUT-OF-PATTERN + RAISE (grade.unplaceable) + NOT_GRADED (grade.not_graded) + NOT_COVERED (not_covered) | adopted whole; no fourth verdict (brief IV.6)' -- NOT_COVERED is a SIXTH value, distinct from RAISE, and this order's own WORKER FACE requires it: 'its row carries desired.verdict = NOT_COVERED and no tension names it.'",
     "Measured this run: `python check_lt_r1.py e2-reproduce` against the regenerated org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/walk/contract.json prints 'R-0278 grade([...COGNITO_USER_POOL]) -> RAISE G1.1: ... ; contract form=None verdict='NOT_COVERED'' and 'VERDICT: FAIL-E2-DESIRED-EQUALS-BUILDER', where the prior round's own re-run at commit 9b628270a1 recorded '277 of 277 builder calls reproduced'.",
     "This is not this order's own criterion (E2R1-AC1 belongs to the DRAINED, MERGED order LGIC_LGCTFM.TO-LT-e-2-r1, whose <status> already reads complete); this row is filed because a later re-run of that criterion -- by an issuer, the CVO at L9, or a future round's regression sweep -- would read a FAIL that is not a defect in LT-e-2's own code, but a fixed-input checker's assumption (any raise = RAISE) this round's own spec supersedes for one verdict."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "check_lt_r1.py's core_reproduce (LT-e-2's E2R1-AC1 arm) asserts a raising grade() call is correctly reported only when desired.verdict == RAISE.",
   "world_is": "11_LGCTFM_CONTRACT_SCHEMA_RECORD.md s.3.1 and this order's WORKER FACE both require a G1.1 raise (no type fits) to read desired.verdict = NOT_COVERED, not RAISE; e2-reproduce has no branch for it and reads FAIL when re-run against a walk contract carrying the LT-e-3 untypeable plant.",
   "notes": "ARMED because e2-reproduce is a mechanical, re-runnable checker and nothing marks it superseded; disarm_owner is 2.0.0_SA_COO~G because check_lt_r1.py under fixed_inputs/r1/ is this seat's own artifact and this worker's BOUNDS forbid editing a fixed input even to fix its own assumption. THE FIX, for the disarm owner: add a NOT_COVERED branch to core_reproduce (good = verdict in (RAISE, NOT_COVERED) with the appropriate paired field check), or accept the one-row miss as a known, superseded-by-spec exception the issuer records rather than re-grades. Not routed as BLOCKING: it blocks no criterion of THIS order (E3R1-AC1..AC6 all read PASS against the same regenerated contract), and LT-e-2's order is already complete and merged."
  },
  {
   "id": "LGIC_LGCTFM-W2-S1",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_LGCTFM~2",
   "surfaced_at": "2026-09-17T20:40Z",
   "one_line": "DEC-9's MARK COMMIT AND THE ENGINE'S OWN RUN ARTIFACTS ARE NOT COMMITTABLE AT DEC-12's RUN HOME: .tools/naming-gate.py (ENFORCE mode) REFUSES contract.json, plan.json, PLANT.json, PLANT_UNTYPEABLE.json and MARK.json wholesale (1719 REFUSE + 49 RAISE lines on the first real run) because workflows/legacy_transform/ is covered by none of the gate's three exemptions, and the walk's own MEASURED current-state values are exactly the legacy tokens (opal-data-bd, 49financial, 49f, blackdiamond/49f/session-trigger-mode.json, ...) the gate's carrier rule refuses as a NEW hand-kept literal. Never exercised before this cell: every prior graded round wrote to org/missions/.../deliverables/, which IS exempt.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "1.0.0_SA_CTO",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     ".tools/naming-gate.py:83 RECORD_TREE_PREFIXES = (\"org/\", \"docs/\"); :77 REGISTRY_PREFIX = \"infra/logic/registry/\"; :904-905 'if path.startswith(REGISTRY_PREFIX): return rows  # the registry files: every token is permitted there'; :906 '/tests/ fixtures are not graded'. workflows/legacy_transform/blackdiamond-49financial/ (DEC-12's run home, LGIC_LGCTFM_PRD.md v1.4) matches none of the three, so every new file there is fully graded.",
     "MEASURED this run: `bash .tools/safe-commit.sh --author \"0.9.0_WK_LGIC_LGCTFM~2 <...>\" -F .scratch/commit_msg_1.txt -- infra/logic/registry/remediations.json workflows/legacy_transform/blackdiamond-49financial/` against the run directory written by `python lib/opal_lgctfm.py run --subject 49financial --seed opal-data-bd --seed opal-data-49financial --run-home-subject blackdiamond-49financial --root workflows/legacy_transform` printed 'ERROR: BLOCKED -- the naming limb refused (LGIC_ENFORCE DEC-6, ENFORCE mode). Commit aborted; files unstaged.' with 1719 'NAMING REFUSE' + 49 'NAMING RAISE' lines against exactly 5 of the run's files: contract.json, plan.json, PLANT.json, PLANT_UNTYPEABLE.json, MARK.json (the sixth JSON file, VINTAGE.json, and the four .md files carried no graded literal and committed clean on the second attempt).",
     "infra/logic/registry/remediations.json itself -- an EXISTING file under REGISTRY_PREFIX -- committed a new surface ({\"kind\": \"s3-prefix\", \"bucket\": \"opal-data-bd\", \"prefix\": \"gold/\"}) with ZERO naming-gate lines: the registry exemption (naming-gate.py:904-905) is real and working; it is workflows/ that carries no equivalent.",
     "lib/opal_lgctfm.py's own docstring (module header, LT-e-1) states the walk's purpose as recording current-state resources verbatim, including ones no instrument can place ('planted deliberately and returned as an UNMEASURED row, never silently dropped'); the engine is not mine to edit (WORKER FACE: 'You edit no code: an engine defect is a BLOCKING row') and neither is .tools/naming-gate.py (outside this order's <paths> grant)."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "LGIC_LGCTFM_PRD.md DEC-9: 'the mark act appends to the three existing registries only ... in the run's own commit, through safe-commit and the naming gate.' DEC-12: the run home is workflows/legacy_transform/.",
   "world_is": ".tools/naming-gate.py's exemption set (RECORD_TREE_PREFIXES, REGISTRY_PREFIX, /tests/) does not reach workflows/legacy_transform/, so the run's own contract.json/plan.json/PLANT.json/PLANT_UNTYPEABLE.json and any MARK.json naming a legacy bucket-alias or s3-prefix are refused by the same gate DEC-9 says the mark commit runs through -- the two ratified decisions (DEC-9/DEC-12 here, LGIC_ENFORCE's gate exemptions) were never checked against each other outside org/, and this cell is the first to leave that exemption.",
   "notes": "BLOCKING because it stops the run's own core deliverable (contract.json) and the DEC-9 mark commit from ever landing on git, not just one criterion; ARMED because every future LGCTFM run at this same home refires it identically. disarm_owner 1.0.0_SA_CTO: this is a naming-gate.py exemption-set change (LGIC_ENFORCE's file, this worker's <paths> does not include it) or a DEC-12 run-home change (a PRD decision only the CTO amends) -- either repair is an L4 act. THIS WORKER'S ACT, inside its own grant: commit everything the gate accepts (the run's .md files, VINTAGE.json, and the registry mark) and leave the five refused files PRESENT, UNTRACKED, on disk in the run directory so the disk-reading criteria can still grade them; recorded, not worked around."
  },
  {
   "id": "LGIC_LGCTFM-W2-S2",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "0.9.0_WK_LGIC_LGCTFM~2",
   "surfaced_at": "2026-09-17T21:05Z",
   "one_line": "EVERY WALK EMITS A ROW WHOSE node_type (COGNITO_USER_POOL) IS OUTSIDE org/standards/LGCTFM_CONTRACT.schema.json's 33-value node_type ENUM, SO NO REAL CONTRACT lib/opal_lgctfm.py PRODUCES CAN EVER VALIDATE AGAINST ITS OWN SCHEMA. The row is LT-e-3's own unconditional plant (cmd_walk() always injects name 'opal-blackdiamond-49financial-legacy-user-pool', node_type COGNITO_USER_POOL, PLANT_UNTYPEABLE.json), built to prove the walk returns an untypeable resource NOT_COVERED rather than dropping it silently -- but the schema's resource_or_plane_row.node_type enum (record s.1.1, 'the 33 node types BY SUBTRACTION from NAMING_SCHEMA.json') has no 34th 'untypeable' value, so the plant row fails 'row' oneOf, and this run's X1R1-AC1 (`check_lt_r1.py x1-run-dir`) reads FAIL on schema errors: 1 for exactly this reason.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "MEASURED this run: `python check_lt_r1.py x1-run-dir` against workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/contract.json prints 'schema errors on its contract: 1' and 'VERDICT: FAIL-X1-RUN-DIRECTORY-COMPLETE'; the single jsonschema error's path is ['rows', 184] (row_id R-0185, node_type 'COGNITO_USER_POOL', message ends '... is not valid under any of the given schemas', schema_path ['properties','rows','items','oneOf']).",
     "org/standards/LGCTFM_CONTRACT.schema.json:70-78 $defs.node_type.enum lists 33 values and does not include COGNITO_USER_POOL; $defs.resource_or_plane_row (:122-149) requires node_type to match that ref, so no oneOf branch admits this row.",
     "workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/PLANT_UNTYPEABLE.json and org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/walk/PLANT_UNTYPEABLE.json are byte-identical ({\"name\": \"opal-blackdiamond-49financial-legacy-user-pool\"}) across two different subjects/seed sets and two different engine writers (LT-e-3 planted it, LT-p-1's cmd_walk() self-invocation of walk still emits it) -- the plant is unconditional, not seed-dependent, so this fires on every future real run identically.",
     "row LGIC_LGCTFM-W1-S1 (this same channel) already names a RELATED but DISTINCT defect on the same plant -- check_lt_r1.py's own core_reproduce (LT-e-2's arm) has no NOT_COVERED branch. That row is about a FIXED-INPUT CHECKER's assumption; this row is about the CONTRACT SCHEMA's own enum never having grown to admit the type LT-e-3 chose to plant, which is a defect in the shipped standard, not in a checker."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "org/standards/LGCTFM_CONTRACT.schema.json validates every contract lib/opal_lgctfm.py walk produces (X1R1-AC1's own bar; DEC-11's receiving-check gains artifact type lgctfm-contract on the same premise).",
   "world_is": "The schema's node_type enum (33 values, record s.1.1) does not include COGNITO_USER_POOL, the node_type of LT-e-3's own unconditional untypeable plant, so every real contract this engine writes fails schema validation on exactly that one row.",
   "notes": "BLOCKING because it fails this order's own X1R1-AC1 and will fail it on every future real run identically; ARMED for the same reason. disarm_owner 2.0.0_SA_COO~G as the LT-e-3/LT-p-1 issuer and the seat that authored 11_LGCTFM_CONTRACT_SCHEMA_RECORD.md's node_type subtraction -- the repair is either a 34th enum value naming the untypeable case (schema, org/standards/, L4-adjacent) or excluding NOT_COVERED-verdict rows from the row oneOf's requirement that node_type be typed. THIS WORKER'S ACT: none available inside <paths> (the schema and the engine are both outside this order's write grant, and 'you edit no code' forbids the engine fix regardless); X1R1-AC1 is graded FAIL on the measured output, verbatim."
  }
]
```
