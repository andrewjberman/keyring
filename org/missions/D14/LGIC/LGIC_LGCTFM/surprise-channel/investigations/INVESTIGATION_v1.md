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
  },
  {
   "id": "LGIC_LGCTFM-S3",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-18T00:20Z",
   "one_line": "LT-x-1's RUN DIRECTORY IS A COMPOSITE OF TWO DIFFERENT RUNS AND NOTHING INSIDE IT SAYS SO. contract.json, plan.json, PLANT.json and PLANT_UNTYPEABLE.json under workflows/legacy_transform/blackdiamond-49financial/20260917T202556Z-bb29248/ were ADDED by a LATER CELL's commit (LT-e-4, a5fca30175) and are byte-identical to that amendment's OWN default-off run 20260917T233115Z-a89fd61, while the directory's VINTAGE.json still declares run_id 20260917T202556Z-bb29248 at repo_head bb292483994d4e2c379d671e6512313864c0363c. So X1R1-AC1 -- the criterion that reads 'the run directory is complete and its contract validates' -- now grades an artifact LT-x-1's own run did not produce, and it reads PASS. MARK.json, the fifth file the naming gate refused, was never committed at all and the worktree that held it is gone, so X1R1-AC2's evidence no longer exists anywhere and re-running x1-marks at HEAD reads FAIL-X1-MARK-ROWS-IN-THE-THREE-REGISTRIES.",
   "class": "BLOCKING",
   "hazard_standing": "ARMED",
   "disarm_owner": "2.0.0_SA_COO~G",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "ADD commits, measured at caf09838c9 with `git log --oneline --diff-filter=A -- <path>` (one line each, no ambiguity): contract.json, plan.json, PLANT.json and PLANT_UNTYPEABLE.json all -> a5fca30175 'amend(LT-e-4-r1, 0.9.0_WK_LGIC_LGCTFM~2): the untypeable plant becomes OPT-IN'; VINTAGE.json -> 53d59778a1 (LT-x-1's own run+mark commit); FWD10.json -> ef6b9f3b9d (LT-x-1's proof-prep). Four of the six run files in LT-x-1's directory were written by a different cell.",
     "Byte equality, `git hash-object` at caf09838c9: contract.json is 84d4d1e62b in BOTH 20260917T202556Z-bb29248 and 20260917T233115Z-a89fd61, and 95b04ca692 in the flag-on run 20260917T233143Z-a89fd61; plan.json is f26d46db87 in all three; PLANT.json 2b347189db and PLANT_UNTYPEABLE.json d62982a9bd in the first two. The copy is exact, not merely similar.",
     "VINTAGE.json of the two directories, read side by side: identical graph_built '2026-09-17 18:16:22 UTC' and identical registry_hash 'scopes.json sha256:b2a54608f8ebbade', but DIFFERENT repo_head (bb292483994d... vs a89fd61a0baa...) and different run_id. The pairing of one run's VINTAGE with another run's contract is what makes the directory incoherent.",
     "MARK.json absence, two instruments: `git ls-tree -r --name-only HEAD` has no MARK.json anywhere under workflows/ (the only MARK.json at HEAD is an unrelated D11 card under org/tier2_senior/0.8.0_AE_CloudComp/); and `ls .worktrees/*/workflows/legacy_transform/blackdiamond-49financial/*/MARK.json` -> 'No such file or directory', with wk-lgic-lgctfm-1-2b (the worker's own worktree, where AC2 measured 4 of 4 entries) absent from `git worktree list`.",
     "The substantive act DID land and is citable at HEAD: 53d59778a1 is an ancestor of caf09838c9 (merge-base --is-ancestor, positive result) and carries the DEC-9 mark into infra/logic/registry/remediations.json -- the s3-prefix surface {\"bucket\": \"opal-data-bd\", \"prefix\": \"gold/\"} under ADVI_FIRMBKTS. What is lost is the REPRODUCIBILITY of the criterion, not the mark."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "X1R1-AC1 grades the run directory LT-x-1's OWN run wrote; DEC-12's run home holds one run per directory, and LT-h-1's run_home.py refuses to overwrite an existing run directory precisely so that a directory's contents and its VINTAGE.json describe the same run.",
   "world_is": "Four of the six files in LT-x-1's run directory were produced by a later cell's run at a different repo_head and placed into LT-x-1's directory by hand (the engine's own refusal cannot be what put them there), and a fifth, MARK.json, was never committed and no longer exists on this device.",
   "notes": "ARMED and BLOCKING because it blocks LT-x-1's `complete` flip, which is the ISSUER's act, not a worker's -- this row is the issuer refusing its own flip. THE MITIGATION IS REAL AND IS NOT THE FIX: both runs read the same graph vintage and the same registry hash, so under LT-d-1's determinism the copied bytes are very probably what LT-x-1's command WOULD emit under the amended engine. But they are not what its run DID emit -- its run carried the untypeable plant ON, which is exactly why its contract failed validation and LGIC_LGCTFM-W2-S2 was filed. Grading a PASS on a substituted artifact launders provenance into the record, and the substitution is invisible at the criterion: x1_run_dir reads the directory, not who wrote it. THE DISARM, chosen by the issuer and not proposed to anyone: re-hand LT-x-1 inside round 1 to re-run the engine at the amended default, minting a FRESH run directory with its own VINTAGE.json, writing and COMMITTING MARK.json (R-35 now exempts a minted run directory, so the commit that refused 1719 times will land), and re-grading X1R1-AC1 through AC5 against that one coherent run. The 20:25Z directory stays exactly as it is, as the historical record of the first run and of the defect W2-S2 describes."
  },
  {
   "id": "LGIC_LGCTFM-S4",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-18T00:22Z",
   "one_line": "DISARM EVIDENCE FOR LGIC_LGCTFM-W2-S2 (the untypeable row no schema could admit): the defect is repaired AT ITS ROOT and the fix is exercised, not merely written. 1.0.0_SA_CTO ruled R-36 -- the untypeable plant becomes OPT-IN behind --plant-untypeable, OFF by default, its carry counted in PLANT_UNTYPEABLE.json and PRINTED EVEN AT ZERO -- and the schema's 33-value node_type enum was NOT widened to admit COGNITO_USER_POOL. Cell LT-e-4 built it and drained at caf09838c9 with 8 of 8 criteria PASS.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "LT-e-4's eight mechanical criteria, re-run by the ISSUER at the branch tip before the merge (a different checkout from the worker's): a4-plant-off, a4-flag-on, a4-count-typed, a4-schema-valid, a4-e3-exercised, x1-run-dir, e1-stdlib and d1-pytest, all PASS. Merged by .tools/safe-merge.sh as caf09838c9.",
     "The default-off run 20260917T233115Z-a89fd61 carries 184 of 184 contract rows with no ungraded node_type and PLANT_UNTYPEABLE.json at 39 bytes (the printed zero); the flag-on run 20260917T233143Z-a89fd61 carries the untypeable resource as NOT_COVERED with PLANT_UNTYPEABLE.json at 2880 bytes. Both validate against org/standards/LGCTFM_CONTRACT.schema.json.",
     "The criterion the defect blocked now passes on a re-run at caf09838c9 in issuer worktree wk-lgic-lgctfm-1-5: `check_lt_r1.py x1-run-dir` -> 'missing of the 6 run files: []; schema errors on its contract: 0; VERDICT: PASS-X1-RUN-DIRECTORY-COMPLETE', against the worker's recorded 'schema errors on its contract: 1 ... COGNITO_USER_POOL ... is not valid under any of the given schemas'."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "W2-S2 asserts that no contract lib/opal_lgctfm.py produces can validate against its own schema, because every walk unconditionally plants a row whose node_type is outside the 33-value enum.",
   "world_is": "The plant is no longer unconditional: it is opt-in, off by default, and its carry is counted outside the contract rows. A default walk now produces a contract that validates, measured on two real runs.",
   "notes": "This row is EVIDENCE, not a disposition -- disarming is not disposing, and prose disarms nothing. W2-S2's own disarm_owner is 2.0.0_SA_COO~G and the act that disarms it is LT-e-4's drain, which is cited above by hash. The disposition of W2-S2 belongs to 3.0.0_SA_CVO at L9, which is why this row carries no `adjudicates`. NOT CLAIMED HERE: that the 20:25Z run directory is coherent -- it is not, and that is LGIC_LGCTFM-S3, a separate item with a separate remedy."
  },
  {
   "id": "LGIC_LGCTFM-S5",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-18T00:24Z",
   "one_line": "DISARM EVIDENCE FOR LGIC_LGCTFM-W1-S1 (LT-e-2's own graded criterion failing on a re-run it never changed): the issuer's fixed input was the defective party, and it was repaired rather than the criterion waived. check_lt_r1.py's core_reproduce gained a NOT_COVERED branch @56dbaee026 -- a NOT_COVERED verdict is now correct when the engine raised 'is not a node type' and emitted no form -- plus two new arms, e2-not-covered and e2-not-covered-wrong-raise, so the branch has a positive AND a negative control.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "Re-run at caf09838c9 in issuer worktree wk-lgic-lgctfm-1-5, a different checkout from both the worker's and the one the failure was measured on: `check_lt_r1.py e2-reproduce` -> 'rows with a builder call the checker can make: 278; reproduced: 278; VERDICT: PASS-E2-DESIRED-EQUALS-BUILDER'. The denominator is printed and is the whole population, not a sample.",
     "The repair is in the ISSUER's fixed input (fixed_inputs/r1/check_lt_r1.py), which is where the row said the defect was and where the worker's BOUNDS forbade it from going -- the worker was right to file a row rather than edit it."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "W1-S1 asserts that core_reproduce treats a raising grade() call as correctly reported only when desired.verdict == RAISE, so a NOT_COVERED verdict -- which the record and the WORKER FACE both require for an untypeable resource -- reads FAIL.",
   "world_is": "core_reproduce now accepts NOT_COVERED on the paired-field test the record specifies, and the arm passes on 278 of 278 rows. The untypeable case is additionally exercised by its own two arms.",
   "notes": "EVIDENCE, not a disposition; no `adjudicates`, and the disposition is 3.0.0_SA_CVO's at L9. WORTH SAYING PLAINLY BECAUSE IT IS THE SECOND TIME THIS ROUND: both W1-S29 (on LGIC_ENFORCE) and this row were defects in THIS SEAT's own fixed input, found by a worker running it, and in both cases the worker's report was the only instrument that could have found them -- a checker's author re-running its own checker is repetition. The cost of the fixed-input pattern is exactly this: the issuer's instrument is graded by nobody until a cell runs it for real."
  },
  {
   "id": "LGIC_LGCTFM-S6",
   "project": "LGIC_LGCTFM",
   "fabric": "laptop",
   "surfaced_by": "2.0.0_SA_COO~G",
   "surfaced_at": "2026-09-18T00:52Z",
   "one_line": "ANDREW_CARD.md's RECOMMENDATION -- the one line a decision-maker actually weighs -- SAID 'the two rows touching a live, client-facing surface' AND THERE IS EXACTLY ONE. Measured over all 179 tensions of the contract the card ranks: client_facing == true is 1 (T-0001, the opal-data-bd bucket), live == true is 1 (T-0001), both together 1, irreversible == true is 0. The card's TABLE is correct and its own analysis sentence is correct ('Rank 1 is the only irreversible-or-client-facing-or-live row in the top ten'), so the RANKING and the 179-row order are not impeached -- what was wrong is the summary written FOR the reader who decides without checking, which is exactly backwards from how a card is used.",
   "class": "OBSERVATION",
   "hazard_standing": "INERT",
   "grounding": {
    "status": "GROUNDED",
    "evidence": [
     "Found by 1.0.0_SA_CTO (msg 97745) on ANDREW_CARD.md @554d1de05b, with its own denominator table: 179 tensions, client_facing true 1, live true 1, both 1, irreversible 0.",
     "RE-DERIVED HERE ON A DIFFERENT ACCESSOR before acting, because the finding's own message records that the CTO's FIRST accessor read the factor values at the top level of each tension and returned 0 client_facing rows across 179 -- a confident zero that would have contradicted the card entirely. The values live under factors.<name>.value. This seat printed tensions[0].factors' real key set (client_facing, irreversible, live, rules_colliding) and then a VALUE HISTOGRAM over the whole population: {True: 1, False: 177, None: 1}. A histogram with three distinct values proves the accessor is reading a real cell rather than returning a constant, which a bare count of 1 does not.",
     "THE CORRECTION COULD NOT LAND IN THE CARD ITSELF AND THAT IS THE GATE WORKING: this seat edited the line, and .tools/owned-paths-validate.py clause 4 (ADHC_OWNPTH.004, lane TREE_DELIVERABLES) REFUSED the commit -- 'deliverables/0.9.0_WK_LGIC_LGCTFM~3/ANDREW_CARD.md ... agent=2.0.0_SA_COO~G not in permitted_agents'. A worker's deliverable folder admits exactly that serial. The edit was reverted (git checkout --) and the correction lands instead as this seat's own record at org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/ANDREW_CARD_CORRECTION_20260918.md, carried to Andrew BESIDE the card in the same act -- which is what 1.0.0_SA_CTO asked for and is better than an in-place edit of a document already in a reader's hands."
    ]
   },
   "disposition": "UNDER_INVESTIGATION",
   "spec_asserts": "V1R1-AC4 (x1 arm v1-card) asserts the card carries the ranking rule verbatim and its top ten tension ids, and it reads PASS. Nothing in round 1's criteria grades the card's PROSE against the population it characterises.",
   "world_is": "The card passed every mechanical arm with a recommendation line that overstated the top-priority population by one. The gap is structural, not a worker's slip: v1-card grades presence (rule verbatim, 10 of 10 ids), never the arithmetic of a sentence about the factors.",
   "notes": "INERT: the ranking is unaffected, the correction is landed, and Andrew has the corrected line beside the card in the same act. FOURTH INSTANCE OF ONE FAMILY IN ONE EVENING, which is what makes it worth a row rather than a fix: this seat's own LGIC_LGCTFM-S3 (a PASS on bytes the cell did not produce), the CTO's S25R4-AC5 (an id that exists in no order and survives a count check), LGIC_ENFORCE S61 (a quote whose one clean grep hit is the wrong file), LGIC_ENFORCE S62 (a right total with a wrong split) and this one (a right table with a wrong summary). In every case the EVIDENCE is sound and the SENTENCE ABOVE IT is not, and in every case a second seat caught it. THE CHEAP CONTROL, for any future card: state the claim as a count with its denominator ('1 of 179') rather than as a word ('the two rows'), because a number invites the check a word does not. NOT CLAIMED: that v1-card should have caught this -- grading a prose summary against the population it describes is a new criterion, not a repair of that arm, and it belongs to whoever cuts the next card cell."
  }
]
```
