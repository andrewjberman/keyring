# NFRA_IAMROLES202609 -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~ZI` at L5, 2026-09-10. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate,
folder == project). **Append-only during the round.**

**Why this file is opened BEFORE L7.** The first row was found while the L5 owner re-grounded the
manifest's two `measured` cells, which PRD section 8 instructs L5 to do in terms. It is a mismatch
between what the specification asserts and what the world reads today, which is exactly the step-7
trigger -- the fact that no worker exists yet does not make it a different kind of finding.

**Denominator at this write: 2 rows** (`NFRA_IAMROLES202609-Z-S1`, `2.0.0_SA_COO~ZI`, 05:39Z;
`NFRA_IAMROLES202609-Z-S2`, `2.0.0_SA_COO~ZI`, 07:29Z).

## Row context -- what was run

`comp-find '.' --corpus aws IAM_ROLE`, vintage 2026-09-10T03:31:02Z, manifest `5361815924ce`:
`DENOMINATOR: 219 hit(s) across 219 aws node(s)`, `DRIFT (scanned): DECLARED=203 LIVE-no-DECLARED=16`
(203 + 16 = 219, reconciles exactly). The 16 were enumerated at that vintage and are carried in the
L5 decomposition at section 1a so that `IAM-s-6` disposes of a SET rather than a count.

⚠ **THE ROW IS ABOUT THE DENOMINATOR, NOT THE SET.** The undeclared count has held at exactly 16
across three vintages and two instruments, which SUPPORTS the PRD's "settled set" claim rather than
disputing it. What moved is what the 16 is out of. ⛔ **This lane did NOT measure member identity of
the 16 against the brief's list and does not claim it** -- a stable count is equally consistent with
"the same 16" and with "one left and one arrived". Establishing membership is `IAM-s-5`'s act.

**Mitigated for this project already, which is why the class is OBSERVATION and not BLOCKING:** the
L5 decomposition binds `IAM-s-2` at section 2c with *"DO NOT HARDCODE 208 -- the posture number's
denominator is a LIVE quantity and must be READ at render time with its vintage printed beside it"*.
That bound travels into the L6 cut regardless of whether the PRD is ever corrected. **The hazard is
still ARMED because the bound protects THIS cut only:** a later round, a re-decomposition, or another
project reading the same PRD cell inherits `208` with nothing to stop it. The disarm is an edit to
`prd/` , which is lane `ANY_CTO` and not this lane's to make.

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZI",
    "surfaced_at": "2026-09-10T05:39Z",
    "one_line": "PRD v0.2 section 8's S5 evidence cell states two different role-population denominators in one sentence -- '16 of 208' and 'DECLARED=200 LIVE-no-DECLARED=16' (which sums to 216) -- and the live plane reads 219 today; the undeclared count itself has held at 16 throughout.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md @076f37eeb2 section 8 row S5 evidence cell: 'brief F2a: 16 of 208 undeclared is a SETTLED COUNT AND A SETTLED SET, corroborated across two substrates and re-measured at the merged head (216 hit(s) / 216 aws node(s), DECLARED=200 LIVE-no-DECLARED=16)'. 200 + 16 = 216, not 208; both denominators sit in one sentence with no reconciliation.",
        "Re-measured by this lane on the instrument the manifest names: comp-find '.' --corpus aws IAM_ROLE -- DENOMINATOR 219 hit(s) across 219 aws node(s) scanned [corpus=aws types=IAM_ROLE]; DRIFT (scanned) DECLARED=203 LIVE-no-DECLARED=16; VINTAGE built from the estate 2026-09-10T03:31:02Z, manifest 5361815924ce. 203 + 16 = 219.",
        "Population across three vintages: 208 (brief F2 @1a90986047) -> 216 (brief F2a merged head) -> 219 (this lane, 2026-09-10T03:31Z). DECLARED across the latter two: 200 -> 203. LIVE-no-DECLARED across all three: 16, 16, 16.",
        "A THIRD figure exists on the DECLARED plane and is NOT part of this finding: comp-iam stats parses 195 IAM roles from Terraform. That is a different plane and a different instrument (comp-iam emits two NOTEs that role labels 'orchestrator' and 'scheduler' were reused across modules and silently mis-linked pre-fix), so 195-vs-203 is not drift and is recorded in the decomposition at section 1b so a later reader does not read it as such."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.2 section 8 presents the S5 evidence as a settled measurement and states that the population of IAM roles is 208, of which 16 are undeclared; acceptance property 1 requires that EVERY NUMBER CARRIES ITS DENOMINATOR AND ITS VINTAGE, and FWD-1's whole bar is a posture number stating 'what it is out of, and when it was taken'.",
    "world_is": "The live plane reads 219 IAM_ROLE nodes at 2026-09-10T03:31:02Z (DECLARED=203, LIVE-no-DECLARED=16). The role population is a LIVE, MOVING quantity that grew twice while this project was being specified, and the PRD cell that commissions the denominator discipline carries two unreconciled denominators of its own. The undeclared count is unaffected and remains 16.",
    "notes": "Filed at L5 by the decomposition's owner, not by a worker, so the id carries the site-Z fabric coordinate and no W allocator coordinate. NOT A HALT: L5 completed and all nine cells are OPEN. The remedy is an edit to the PRD's section 8 S5 evidence cell (re-pin the denominator with its vintage, or state which of the two it means), which is lane ANY_CTO and belongs to 1.0.0_SA_CTO~Z; this lane cannot make it and does not propose the wording. DISARMED is not REMEDIATED. The general shape, which the PRD itself names one paragraph earlier about a different citation: a number goes stale fastest when nothing in the fabric announces that the world moved under it."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZI",
    "surfaced_at": "2026-09-10T07:29Z",
    "one_line": "Relayed spine v3.7 states the L7 worker's model is Opus at high effort BY THE AGENT TYPE'S OWN DEFINITION, but this fabric's .claude/agents/worker.md reads 'model: sonnet' at HEAD -- the amendment and the worker.md edit that carries it are both local to the laptop fabric, so every worker spawned on site-Z runs at a model the amendment does not intend, and no per-spawn override is lawful to correct it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "MEASURED AT HEAD WITH git show, not by reading the worktree path: `git show HEAD:.claude/agents/worker.md` returns frontmatter `name: worker` / `model: sonnet` at HEAD b5bad26a0c. The worktree copy agrees, so this is not an unlanded local edit being misread -- both planes say sonnet.",
        "The spine at HEAD is 462 lines and its changelog's newest row is version 3.6 (`git show HEAD:org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`). v3.7, v3.8 and v3.9 are absent from this fabric entirely.",
        "The relay is 0.0.0_AB_MSTR~Z msg 20764 (SPAWN-DIRECT, ACKed by this lane), which states: 'v3.7 -- the L7 worker's model is Opus at high effort BY THE AGENT TYPE'S OWN DEFINITION (.claude/agents/worker.md). NEVER chosen per task order, NEVER a per-spawn override. This is a constraint on how you SPAWN workers.' The same message declares all three amendments LOCAL to the laptop, 462 lines here vs 480 there, and RELAY-GRADE NOT MEASURED.",
        "The two clauses of v3.7 come apart on this fabric and that is the whole finding: its MECHANISM (never a per-spawn override) is honourable here and is honoured -- round 1's workers are spawned with NO model parameter, taking whatever the agent type's definition says. Its VALUE (Opus at high effort) is not present, because the definition it points at says sonnet."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Spine v3.7, as relayed, asserts that the L7 worker's model is Opus at high effort and that this is fixed by the worker agent type's own definition at .claude/agents/worker.md, never chosen per task order and never overridden per spawn.",
    "world_is": "On the site-Z fabric .claude/agents/worker.md declares `model: sonnet` at HEAD, and the spine here is v3.6 at 462 lines with no v3.7 clause at all. Workers spawned here therefore run sonnet. Passing an Opus override at spawn WOULD violate the same amendment's explicit mechanism, so the divergence cannot be closed by the spawning seat and was not.",
    "notes": "Filed by a seat at L6/L7, not by a worker, so the id carries the site-Z coordinate and no W allocator coordinate. NOT A HALT: round 1's spawn proceeds on the agent type's own definition, whatever it says, and the round runs. This row records a DIVERGENCE, not a defect in anyone's act -- the relay was honest about being relay-grade and told this lane to re-read the spine once the amendments land. The remedy is the cross-fabric landing of v3.7-v3.9 plus whatever worker.md edit that implies, which is process law (1.0.0_SA_CTO~Z as the spine's scribe) carried across fabrics by the integrator (0.0.0_AB_MSTR~Z); it is not this lane's to make and this lane does not propose the model value. THE REUSABLE SHAPE, which is why this is worth a row rather than a shrug: an amendment that fixes a VALUE by pointing at a DEFINITION travels only as far as that definition does. Relaying the amendment's text across a fabric boundary carries the constraint and leaves the value behind, and the two halves then disagree with nothing able to fail -- the spawn succeeds, the worker runs, and only a reader who checks the definition against the relay can see it."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~1",
    "surfaced_at": "2026-09-10T08:20Z",
    "one_line": "The dispatch prompt for TO-IAM-s-1 named the proof-of-spec deliverable path as '<TO_ID>.proof_of_spec.json' (the shortened id, no descriptive suffix), but the live gate .tools/to-pipeline-gate.py:check_complete_flip globs on the TO FILE'S FULL BASENAME STEM ('<TO_ID>.<descriptive-suffix>.proof_of_spec.json') -- the shortened name is invisible to it and the status-flip commit was REFUSED with 'NO proof-of-spec instance was found beside it' even though the correctly-scoped file existed in the same staged commit.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Spawn/dispatch prompt for 0.9.0_WK_NFRA_IAMROLES202609~1 (IDENTITY section, this session) states verbatim: 'Write your proof-of-spec instance to org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-1.proof_of_spec.json' -- the shortened form.",
        ".tools/to-pipeline-gate.py check_complete_flip(): `stem = os.path.basename(rel).rsplit('.md', 1)[0]; names = (stem + '.proof_of_spec.json', stem + '_PROOF_OF_SPEC.json')` against the TO's own basename 'NFRA_IAMROLES202609.TO-IAM-s-1.permission-grain-usage-instrument.md' -- the only names it globs for both carry the full descriptive suffix; the shortened form is not a candidate under either branch.",
        "Reproduced directly: `bash .tools/safe-commit.sh ... -- org/modules/graph/comp_iam_usage.py .tools/comp-iam-usage <TO file, status flipped to complete> <deliverables>/NFRA_IAMROLES202609.TO-IAM-s-1.proof_of_spec.json` (all four staged in one call) -> commit-gate PASS, then 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate)... NO proof-of-spec instance was found beside it', files unstaged. Every other existing tree-project instance sampled (NFRA_CLDGRPH.TO-CG-D-1.shared-image-rebuild-deriver-live.proof_of_spec.json, NFRA_OPSEC202609.TO-OP-S-8.identity-and-rbac-table-protection.proof_of_spec.json, and every other file under org/missions/**/deliverables/**/*.proof_of_spec.json) carries the FULL descriptive stem, confirming the shortened form is the outlier, not the convention."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The dispatching prompt (this worker's IDENTITY section, written by 2.0.0_SA_COO~ZI's spawn) asserts a specific, shortened proof-of-spec filename as the correct deliverable path for a mechanically-gated 'staged -> complete' flip on a pipeline-registered (dep_stage=EXECUTING) project.",
    "world_is": "The mechanism that actually enforces the flip (to-pipeline-gate.py, wired into safe-commit.sh's LAYER 2) resolves the instance ONLY by the TO file's full basename stem, so a worker who follows the dispatch prompt's literal filename verbatim gets a REFUSED commit at the flip step even with a fully valid instance staged alongside it in the same commit. Disarmed for THIS cell by renaming to the full-stem filename before the real commit (this lane's own fix, within its write grant); the same dispatch-prompt template, if reused verbatim for IAM-s-3 / IAM-s-2 / IAM-s-9 or any other tree-project worker spawn, reproduces the identical refusal.",
    "notes": "NOT A HALT: caught before any commit landed (safe-commit.sh unstages on refusal, so nothing was left half-committed); this lane renamed the file to the full-stem form and re-committed successfully. Filed as OBSERVATION/ARMED rather than BLOCKING because the fix was fully within this worker's own write grant and cost one rename -- but the SOURCE (the dispatch prompt template) is not this lane's to edit, hence disarm_owner is the issuing COO."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~1",
    "surfaced_at": "2026-09-10T08:35Z",
    "one_line": "The same dispatch prompt told this worker its own surprise-row id grammar was '<PROJECT>-W<n>-S<k>' (no fabric infix), but this project's fabric is site-z and org/surprise_channel/schemas/investigation_item.schema.json + .tools/surprise-row-gate.py both require the Z- infix ('<PROJECT>-Z-W<n>-S<k>') for a site-z row -- a row minted exactly as instructed is REFUSED by the live gate.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Spawn/dispatch prompt for 0.9.0_WK_NFRA_IAMROLES202609~1 states verbatim: 'Your surprise row id is NFRA_IAMROLES202609-W1-S<k>, k the next unused number within your slot's coordinate.' -- no Z- infix named anywhere in that instruction.",
        "org/missions/D12/NFRA/NFRA_IAMROLES202609/project.json: 'fabric': 'site-z'.",
        "org/surprise_channel/schemas/investigation_item.schema.json id field description: '{PROJECT}-Z-W{n}-S{k} composes, fabric first' and 'The fabric coordinate is REQUIRED for site Z because both certifiers otherwise allocate the same sequence by construction'.",
        "Reproduced directly: staging this file with a row id 'NFRA_IAMROLES202609-W1-S1' and running the real commit path -> `.tools/safe-commit.sh` -> surprise-row-gate.py REFUSED with \"fabric='site-z' but the id lacks the Z- infix, which means 'laptop'. site-z iff the id carries Z-.\" rc non-zero, files unstaged."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The dispatching prompt asserts the row-id grammar for this worker's surprise-channel entries is '<PROJECT>-W<n>-S<k>'.",
    "world_is": "The live gate that actually accepts or refuses a new row requires '<PROJECT>-Z-W<n>-S<k>' on this project because its registered fabric is site-z; the grammar the dispatch prompt names is REJECTED outright, not merely non-preferred. The same worker's own first row (Z-W1-S1, above) hit this exact refusal before being corrected.",
    "notes": "NOT A HALT: caught before any commit landed; this lane corrected both this row's and the sibling row's ids to carry the Z- infix before committing. Same root shape as Z-W1-S1 (a dispatch-prompt literal that a live gate does not accept) but a DIFFERENT gate and a DIFFERENT field, filed separately rather than folded in, since class is judged on form and these are two distinct mechanical facts. If the same dispatch-prompt template is reused for IAM-s-3 / IAM-s-2 / IAM-s-9 or other site-z worker spawns, it reproduces the identical refusal on their first surprise row, if any."
  }
]
```
