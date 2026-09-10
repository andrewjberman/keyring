# NFRA_IAMROLES202609 -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~ZI` at L5, 2026-09-10. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate,
folder == project). **Append-only during the round.**

**Why this file is opened BEFORE L7.** The first row was found while the L5 owner re-grounded the
manifest's two `measured` cells, which PRD section 8 instructs L5 to do in terms. It is a mismatch
between what the specification asserts and what the world reads today, which is exactly the step-7
trigger -- the fact that no worker exists yet does not make it a different kind of finding.

**Denominator at this write: 3 rows** (`NFRA_IAMROLES202609-Z-S1`, `2.0.0_SA_COO~ZI`, 05:39Z;
`NFRA_IAMROLES202609-Z-S2`, `2.0.0_SA_COO~ZI`, 07:29Z; `NFRA_IAMROLES202609-W2-S1`,
`0.9.0_WK_NFRA_IAMROLES202609~2`, 08:16:55Z).

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
    "id": "NFRA_IAMROLES202609-W2-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "laptop",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~2",
    "surfaced_at": "2026-09-10T08:16:55Z",
    "one_line": "TO-IAM-s-4's WORKER FACE names the proof-of-spec instance path as <TO-id>.proof_of_spec.json (no descriptive suffix), but .tools/to-pipeline-gate.py's check_complete_flip computes its discovery stem from the TO FILE'S OWN full basename (WITH the descriptive suffix) and glob-searches deliverables/*/ for THAT stem -- so an instance written exactly where the identity mandate says will not be found, and the <status>complete</status> flip this same order requires is REFUSED at commit time with 'NO proof-of-spec instance was found beside it.'",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Task order org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-4.condition-axis-reader-what-a-policy-requires.md's WORKER FACE, verbatim (issuer 2.0.0_SA_COO~ZI): write the proof-of-spec instance to '.../deliverables/0.9.0_WK_NFRA_IAMROLES202609~2/NFRA_IAMROLES202609.TO-IAM-s-4.proof_of_spec.json'.",
        ".tools/to-pipeline-gate.py check_complete_flip @HEAD (this worktree, unmodified -- read only): `stem = os.path.basename(rel).rsplit('.md', 1)[0]` where `rel` is the STAGED TO file's own path, i.e. stem = 'NFRA_IAMROLES202609.TO-IAM-s-4.condition-axis-reader-what-a-policy-requires' (the FULL filename minus .md), then globs `deliverables/*/<stem>.proof_of_spec.json`. The short name the WORKER FACE names does not match that glob.",
        "MEASURED by running the real commit path: `bash .tools/safe-commit.sh` on the TO flip plus the short-named instance failed at pipeline layer 2 with the exact quoted message: 'flips to complete on PIPELINE-REGISTERED project NFRA_IAMROLES202609, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.' The instance itself was independently confirmed schema-VALID (proof-of-spec-check.py rc=0) at the very same path the gate could not find -- so the refusal is a NAMING/DISCOVERY mismatch, not a quality defect in the instance.",
        "Positive control: the sibling precedent org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-8.identity-and-rbac-table-protection.proof_of_spec.json IS named with the full descriptive-suffix stem matching its TO file, which is exactly what this gate's glob expects -- confirming the gate's convention is the estate's actual standing one, and this task order's WORKER FACE instruction is the outlier."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's WORKER FACE states the exact proof-of-spec instance path this cell must write, and separately requires the TO's <status> be flipped to complete in the same commit once every mechanical criterion passes -- implying that writing the instance at the stated path is sufficient to let that flip land.",
    "world_is": "The mechanical gate that actually enforces the complete flip (to-pipeline-gate.py, invoked inside safe-commit.sh) discovers the instance by a DIFFERENT filename rule (the TO file's own full basename, descriptive suffix included) than the one the WORKER FACE states, so the flip is refused at commit time when the instance sits ONLY at the WORKER-FACE-named path. This worker resolved it in-lane by additionally writing a second, byte-identical copy of the instance at the gate's required filename ('NFRA_IAMROLES202609.TO-IAM-s-4.condition-axis-reader-what-a-policy-requires.proof_of_spec.json'), verified independently VALID (rc=0), and committing both alongside the flip -- so this cell's own flip is not blocked. The hazard for anyone else following the WORKER FACE literally, unresolved, is ARMED: any of this fan-out's three sibling workers (~1, ~3, ~4), or any future task order minted from the same COO template, will hit the identical refusal the first time they try to flip status to complete, because the template's own instruction text cannot satisfy the gate it is graded by.",
    "notes": "Filed by a worker (W2), so the id carries the W allocator coordinate and no Z- fabric infix, per this task order's own literal instruction for the row-id form ('NFRA_IAMROLES202609-W2-S<k>') and per the general harness convention for worker rows -- fabric is set to 'laptop' to agree with the id's absent Z- infix per surprise-row-gate.py's RC1 identity check, though this worktree's branch is based on SITEZ and the TO's own record face carries `<fabric>site-z</fabric>`; that agreement is between the id and the fabric FIELD, not a claim about which physical device ran this worker. NOT A HALT and NOT BLOCKING: this cell's own commit is not stopped by it (the second, correctly-named copy resolves it in-lane), but the underlying mismatch is a property of the TASK ORDER TEMPLATE / GATE PAIR, not of this cell's execution, and will refire on every sibling task order in this fan-out unless the template is corrected. The remedy is either (a) editing to-pipeline-gate.py's check_complete_flip to also accept the shorter <to_id>.proof_of_spec.json form the WORKER FACE names, or (b) correcting the WORKER FACE template's instruction to name the full-stem filename the gate already expects -- both are outside this cell's <paths> (no .tools/ path is granted here) and outside a worker's lane in either case (gate mechanism = fabric tooling; task-order template = L6 issuance), so disarm is routed to 2.0.0_SA_COO~ZI as this fan-out's issuer."
  }
]
```
