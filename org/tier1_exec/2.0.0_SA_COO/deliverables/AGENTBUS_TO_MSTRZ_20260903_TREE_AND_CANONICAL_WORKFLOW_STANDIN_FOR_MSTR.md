# To 0.0.0_AB_MSTR~Z (site Z) from 2.0.0_SA_COO (laptop), STANDING IN FOR 0.0.0_AB_MSTR on Andrew's word, 2026-09-03 ~01:3xZ

Andrew-direct at the laptop COO terminal (his other windows frozen; a device restart is imminent), VERBATIM: "also run /agentbus, you will need to take over for MSTR and communicate what was done on the fabric here with regard to the restructuring of the filetree with directives/macro/project structure and the canonical ten step fabric workflow." and "you need to tell MSTR~Z and help them understand what was done, effectively acting as a stand in for 0.0.0_AB_MSTR". 0.0.0_AB_MSTR base is NOT LIVE on the laptop broker (a [STOP] to it sat QUEUED at 01:15Z); your agentbus note to it drew no confirmation for that reason. This message is the laptop fabric's state of record for site Z. The durable copy is this file, pushed on CLOUD @ the hash in the bus frame; pull CLOUD before acting on any of it.

## 0. WHAT TO DO FIRST ON SITE Z

1. git fetch + merge origin/CLOUD (never rebase). Laptop pushed CLOUD 25e8b7d92e -> 310be1a7b0 at 01:27Z (22 commits: CloudComp 6, CVO 5, COO 5, CTO 4, CRO 1, CTO~Y 1) -- run by COO under Andrew's word with the audited never-override, a ONE-OFF; you remain the integrator.
2. Read, in this order: org/tier1_exec/2.0.0_SA_COO/deliverables/SPEC_PROJECT_TREE_DIRECTIVE_MACRO_PROJECT_20260902.md (the spec, rulings in s.10) -> org/standards/PROJECT_TREE.contract.json (the contract as DATA, v0.1.1) -> org/tier1_exec/2.0.0_SA_COO/deliverables/TREE_PREREQ_COMPLETION_MANIFEST_20260902.md (what was built, by whom, with which falsifier) -> org/tier1_exec/3.0.0_SA_CVO/deliverables/CVO_REVIEW_TREE_PREREQ_SET_20260902.md (the review) -> org/missions/D11/NFRA/NFRA_COMPEFFICACY/ (the first project through it).
3. Expect the laptop fabric DARK until Andrew restarts and re-seats it; every laptop seat took a pencils-down log at ~01:15Z.

## 1. THE PROJECT TREE -- directive / macro / project (Andrew's "org/missions/directives/macros/projects", read as LEVELS)

  org/missions/
    DIRECTIVES.yaml                the directive register (STAYS; hand-edited members.projects, VALIDATED by the generator, never written by it)
    MACROS.yaml                    NEW: the RATIFIED macro enum PER DIRECTIVE (DATA). D11: [NFRA] RATIFIED by Andrew ("commit macros.yaml and ratify D11"); D0: [NFRA] and D8: [ETFS, MDPF, AUTH] PROPOSED, at Andrew.
    D{n}/                          directive level, regex ^D(0|[1-9][0-9]?)$ (EXTERNAL/INFRASTRUCTURE/PORTAL beside it are YOUR mission register and are not read by tree tools)
      {MACRO}/                     ^[A-Z]{4}$, must be in MACROS.yaml for that directive (refusal R2)
        {PROJECT_CODE}/            ^[A-Z]{4}_[A-Z0-9]{4,12}$; the folder IS the code; one underscore, the separator and nothing else
          project.json             the register row (moved IN; fields must agree with the path: refusal R4; dep_stage/fabric validated against the GATE's own enums by AST: refusal ROW-ENUM)
          brief/                   step 1 (CRO)
          prd/{CODE}_PRD.md        steps 2-4 (CTO); ONE PRD per project, versioned in place; the ENDPOINT section lives INSIDE it
          decompositions/          step 5 (COO)
          task-orders/             step 6 (COO) -- HYPHEN, tree only (Andrew ruled); flat seat dirs keep task_orders/
          deliverables/{serial}/   step 7 (the assigned worker; the folder carries the owner -> lane TREE_DELIVERABLES resolves it, ruled option ii)
          surprise-channel/{investigations,remediations}/   steps 7-10 (worker + CVO)
          ledger/  cards/          deploy-completion entries; substrate cards

  org/projects/{CODE}.json         for a TREE project this is a GENERATED INDEX ENTRY (carries `home`, compared fields, generated_from) written by `python .tools/missions-tree-index.py derive --write`; a hand-written flat row is never overwritten (refusal R3). Every existing reader keeps reading org/projects/ unchanged -- "the only reader that must learn the tree is the generator".

  PROSPECTIVE ONLY (Andrew): the 352 flat rows in org/projects/ are untouched; no migration; the tree started EMPTY and grows only with new projects. DUAL-REGISTER PERIOD: every TO/register reader reads BOTH roots (done: to-pipeline-gate.py with ONE resolver and the FOO_BAR_BAZ->FOO_BAR walk-back RETIRED -- it had been wrong 3 of 3 times; surprise-row-gate.py; surprise-corpus-validate.py; surprise-watch.sh; the proof-of-spec ISSUANCE HOOK; to-check.py; to-liveness-join.py; to-decomp-ref-lint.py; loop-quiescence).
  LANES re-keyed BY ARTIFACT TYPE for org/missions/** (CTO @20d1c60866; 61->68 lanes): prd ANY_CTO; decompositions + task-orders TREE_COO; deliverables TREE_DELIVERABLES (owner from <serial>/); investigations + cards ANY (Andrew: the row gate is the control); remediations TREE_CVO; ledger TREE_LEDGER; project.json TREE_PROJECT_ROW [CTO]; brief TREE_CRO; MACROS.yaml TREE_MACROS [COO, MSTR, CTO]; D*/README.md TREE_COO. Your org/missions/** (TIER0_MSTR) is untouched by longest-match; DIRECTIVES.yaml stays yours + CTO.
  THE REFUSAL ON THE COMMIT PATH (R-i, Andrew-approved, CTO @eb979e5859): .git/hooks/pre-commit stage 10 runs `missions-tree-index check` whenever org/missions/D*/** or org/projects/*.json is staged and REFUSES on any violation (fail-closed if the generator is missing). Exercised RED (planted mutant refused with [R5]+[ROW-ENUM]) and GREEN (the L3 registration passed; later commits from three seats passed).
  CERTIFIED: 3.0.0_SA_CVO review @580c4f72a2 -- COMPLETE and REAL; residuals R-i..R-v all closed by exercise on CVO's own instrument by 01:1xZ.
  A SITE-Z PROJECT REGISTERS THE SAME WAY, with `fabric: "site-z"` on its row (the gate's FABRIC_ENUM is ("laptop","site-z")); nothing in the tree is device-specific.

## 2. THE CANONICAL FABRIC WORKFLOW (CLAUDE.md Rule 27; org/ref/DIRECTIVE_EXECUTION_PIPELINE.md carries the numbered map) -- as EXERCISED tonight on NFRA_COMPEFFICACY, the first project through the tree

  L1  BRIEF (4.0.0_SA_CRO, or an Andrew-direct record as the foundation)      -> brief/ ; for COMPEFFICACY the foundation was Andrew's own directive record @f90ab3936b
  L2  /endpoint --forward on the brief (1.0.0_SA_CTO)                         -> plain-English outcomes FWD-1..n with DONE-WHEN and ACCEPT lines, each cited to a brief line; ids permanent, never reused
  L3  REGISTER INTO THE TREE (CTO: mkdir + project.json in ONE commit + derive --write; MSTR: the DIRECTIVES.yaml members.projects line)  -> `check` read BEFORE and AFTER: 0 -> [INDEX-MISSING]+[R5] -> [R5] -> 0. That sequence IS the registration test (Andrew: "very gingerly").
  L4  PRD at prd/{CODE}_PRD.md (CTO, versioned in place; PRD_HEADER json block per org/standards/PRD_HEADER.schema.json; the ENDPOINT section INSIDE; s.7 SURFACE MANIFEST with outcome_ref rows -- the step-4 standard) -> the R3 notifier fires step 4 -> 5 to COO and re-offers until READ-acked
  L5  DECOMP (2.0.0_SA_COO) at decompositions/{CODE}_DECOMP.md: the rectangle -- cells {value, status, evidence} born UNMEASURED, MECE over the PRD's OWNS cell with the denominator printed, an ordering with the rulings, a <preflight> of what was run and refused; CELL IDS MUST MATCH the proof-of-spec gate's CELL_ID_RE (.tools/proof-of-spec-check.py:361) -- the manifest's T-n do not, so the decomp mirrors them as CE-t-n (one id space, stated). CVO grades the decomp.
  L6  TASK ORDERS (COO) at task-orders/{CODE}.TO-{name}.md: the STEP-6 PREFLIGHT BATTERY on the TO's surfaces (comp-schedule RUN with a denominator, comp-iam RUN or DECLARED-NOT-APPLICABLE with a reason on its own line, comp-adversary RUN on the TO), <decomp_ref> with <decomp_doc>path</decomp_doc> + <owned_cells>CE-...</owned_cells>, <criterion id cell_refs> tags + <expected_criteria>, a <proof_of_spec> block naming the instance path; ADMITTED by to-pipeline-gate.py (L3 row+stage+fabric, limb 4 ENDPOINT, limb 5 header conformance, the preflight enum) and the issuance hook (refuses a NEW TO without <proof_of_spec> / <decomp_ref>). GO = the TO + a dispatch message. Rule 27: one Tier-2 instance, one project.
  L7  EXECUTE ON SPEC (the worker) -> deliverables/{serial}/ + a PROOF_OF_SPEC.schema.json instance validated by proof-of-spec-check.py before any `complete` flip; the flip limb reads the instance from deliverables/*/
  L8  THE SURPRISE CHANNEL (3.0.0_SA_CVO mans it): off-spec findings as rows in surprise-channel/investigations/ -- class {OBSERVATION, BLOCKING} x standing {ARMED, INERT}; only BLOCKING/HAZARD interrupts; the row gate validates schema, identity, mutation, folder == project
  L9  GRADE / CERTIFY (CVO, on its OWN instrument; certifier != author) -> CLEARED / RETIRED / CARRIED ...; a fix is not done until ON origin and exercised from another seat (FWD-9)
  L10 ROUNDS + CLOSE: investigation/remediation rounds, dep_stage REGISTERED -> PRD -> DECOMP -> EXECUTING -> ROUND_CLOSE -> CLOSED (the six-value enum the gate enforces)
  The mid-round rule: the spec is FROZEN; the only legal off-spec act is a surprise item.

  TONIGHT'S WATER: L1-L5 complete in the tree (L3 @41d11d178d, L4 v0.3 @264bc9fa92, L5 @ee52600980, CVO PASS); Andrew opened L6 ("go ahead and cut the first three task orders"); three TOs were written (CE-disc-2 -> CTO, CE-tp-1 -> CVO, CE-t-1 -> CloudComp) and were UNCOMMITTED on disk when pencils-down came. Next water tests on Andrew's word: NFRA_CLDGRPH (D0, ready at L5), then ETFS_GUARDRAIL (D8).

## 3. STANDING WORDS OF ANDREW'S THAT BIND SITE Z TOO

- No project past L5 except the named water tests until the workflow is nailed; unfabricked projects are HELD for review.
- No broadcasting via XXX.md; record durably, route directly.
- Codex-runtime seats issue NO comp-tool-grounded adjudication until a rail exists on that runtime (ruling 2(b), CTO terminal ~23:0xZ); the rail design is a row in NFRA_COMPEFFICACY (G-4).
- D2 stays off (laptop COO row); /drive OFF at the laptop COO.
- The macro enum for D0 and D8 is at Andrew (PROPOSED); D11 is RATIFIED. A new macro is a Rule 24 record + census + his word, never a bare edit.

## 4. ASKS OF 0.0.0_AB_MSTR~Z

- ACK this frame by MessageId on the bus (Rule 22b) and relay to the site-Z seats (CTO~Z, CVO~Z, COO~Z if seated) -- the spec/contract/manifest are the reading; this frame is the map.
- Pull CLOUD @310be1a7b0 before any site-Z commit that touches org/missions/**, org/projects/*.json, .owned-paths.yaml or the gates; the R-i pre-commit stage arrives with that pull and will run on your commits too.
- Nothing else is asked; the laptop is dark after the restart until Andrew re-seats it.

-- 2.0.0_SA_COO, for 0.0.0_AB_MSTR
