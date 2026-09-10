# NFRA_IAMROLES202609 -- surprise channel, INVESTIGATION v1 (round 1, site-Z fabric)

**Opened by:** `2.0.0_SA_COO~ZI` at L5, 2026-09-10. **Home:** the project tree's channel. Lane `ANY`;
the gate `.tools/surprise-row-gate.py` validates every NEW row (schema, identity, coordinate,
folder == project). **Append-only during the round.**

**Why this file is opened BEFORE L7.** The first row was found while the L5 owner re-grounded the
manifest's two `measured` cells, which PRD section 8 instructs L5 to do in terms. It is a mismatch
between what the specification asserts and what the world reads today, which is exactly the step-7
trigger -- the fact that no worker exists yet does not make it a different kind of finding.

**Denominator at this write: 5 rows** -- four seat rows and the round's first WORKER row
(`-Z-S4` records this lane DISARMING the worker's row `-Z-W3-S1` and the drain's continuation gap)
(`NFRA_IAMROLES202609-Z-S1`, `2.0.0_SA_COO~ZI`, 05:39Z; `-Z-S2`, `2.0.0_SA_COO~ZI`, 07:29Z;
`-Z-S3`, `2.0.0_SA_COO~ZI`, 07:42Z; `-Z-W3-S1`, `0.9.0_WK_NFRA_IAMROLES202609~3`, 08:00Z).
The worker row arrived through the L7 drain and the two sides collided at the same offset, which is
the append-only channel's normal path (NFRA_CLDGRPH-S36), not an exception: resolved as a UNION of
both sides' rows through `safe-merge.sh --continue`, so the row gate graded the merged index.

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
    "id": "NFRA_IAMROLES202609-Z-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZI",
    "surfaced_at": "2026-09-10T07:42Z",
    "one_line": "This lane's own L6 cut carried one defective criterion -- IAM-s-3 AC2 invoked comp-find BY BARE NAME, which from a worker's worktree censuses the MAIN checkout and would have returned a large confident denominator over a tree that does not contain the worker's extension; fixed before the order was handed out. The same measurement REFINES INSTRUMENT_LIMITS.md LIMIT 4: the limit belongs to the BARE NAME, not to the tool, because the explicit .tools/comp-find path honours the caller's worktree.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DISCRIMINATOR USED, chosen so a false zero and a true absence cannot read alike: `catviews-cottonwood-inflection.json` exists ONLY in the main checkout (untracked there, absent from every fresh worktree; `ls` confirms both halves).",
        "BARE NAME, run from /c/tmp/wk-iamroles-1: `comp-find --name 'catviews-cottonwood-inflection.json'` returns 1 hit across 55375 file(s) scanned -- a HIT for a file that does not exist in the caller's tree, with a denominator byte-identical to the main tree's. It read the MAIN checkout regardless of PWD.",
        "EXPLICIT PATH, same worktree, same query: `.tools/comp-find --name 'catviews-cottonwood-inflection.json'` returns 0 hit(s) across 31052 file(s) scanned -- the WORKTREE's own denominator, and a correct absence. Positive control from the main tree: 1 hit across 55377 scanned.",
        "MECHANISM, re-derived rather than assumed: `command -v comp-find` resolves to /c/Users/Opal Bloomberg/bin/comp-find, a ~/bin forwarder whose own script directory is the MAIN checkout -- so _comprail.repo_root()'s script-relative resolution lands on main. Invoked as .tools/comp-find from a worktree, that same script-relative rule lands on the worktree. Both behaviours follow from ONE rule; the entry states the rule and draws only one of its two consequences.",
        "SIBLING FORWARDER CHECKED AND IT IS SOUND, which is why this round's other criteria stand: .tools/comp-iam-usage sets WORKSPACE=\"$(cd \"$(dirname \"$0\")/..\" && pwd)\" and, re-derived from /c/tmp/wk-iamroles-1, resolves to /c/tmp/wk-iamroles-1 -- so a worker invoking it by explicit path exercises ITS OWN edited module. IAM-s-1's AC1-AC4 and IAM-s-3's AC3 are therefore correct as cut.",
        "SCOPE NOT CLAIMED: comp-read and comp-which share the shim shape and were NOT separately exercised here, exactly as msg 20828 declares of its own arms. This row claims comp-find only."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "INSTRUMENT_LIMITS.md LIMIT 4, filed @6858c8dd5f and relayed as msg 20828, states that a comp-find/comp-read/comp-which result obtained from inside a linked worktree describes the MAIN checkout and that the rule is to run any census or absence claim FROM THE MAIN CHECKOUT.",
    "world_is": "That is true of the BARE NAME and not of the tool. Measured from a live worker worktree: bare `comp-find` scans 55375 files (main) and returns a hit for a file absent from the caller's tree; `.tools/comp-find` scans 31052 files (the worktree) and correctly returns zero. There are therefore TWO remedies, not one -- run from main, OR invoke by the explicit .tools/ path -- and the second is the one a worker can actually use, because a worker is confined to its worktree and cannot run anything from the main checkout.",
    "notes": "TWO FINDINGS IN ONE ROW BECAUSE THEY ARE ONE MEASUREMENT. (1) AGAINST THIS LANE: the L6 issuance shipped IAM-s-3 AC2 as a bare-name comp-find. Caught before the order was handed to slot ~1 (which is still on IAM-s-1), REMEDIATED in the same commit as this row by pinning the explicit .tools/ path and by making the expected denominator itself the discriminator -- the criterion now says a scanned count near 55,000 means the bare name was used and the census is void. Every other comp-tool invocation in the nine orders was re-checked: IAM-s-5 AC1 uses --corpus aws, which reads the live AWS graph and not the repo tree, so it is unaffected. (2) FOR THE ENTRY'S OWNER: LIMIT 4's mechanism paragraph is correct and its REMEDY is over-broad by one clause. This matters most for the population the entry was written about -- L7 workers -- because 'run it from the main checkout' is the one remedy a worker cannot take. DIRECTION OF THE IMPRECISION IS SAFE: it forbids something that works rather than permitting something that does not, so nothing built on LIMIT 4 as written is wrong. Not urgent, not gating, and not sent as a mid-round message -- the COO's one message of a round is the drain-end read and this rides it. THE REUSABLE SHAPE: an instrument limit discovered through one invocation path gets written as a property of the TOOL, and the remedy then inherits a scope the mechanism never had."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~3",
    "surfaced_at": "2026-09-10T08:00:26Z",
    "one_line": "TO-IAM-s-5's WORKER FACE names the proof-of-spec instance path as '<TO-id-short>.proof_of_spec.json' (e.g. NFRA_IAMROLES202609.TO-IAM-s-5.proof_of_spec.json), but .tools/to-pipeline-gate.py's check_complete_flip derives the expected filename from the FULL TO FILENAME STEM (including the descriptive suffix) -- so the literally-instructed path does not match either name the gate globs for, and a status flip to complete on the instructed filename ALONE is mechanically REFUSED at commit.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Identity block for this worker (0.9.0_WK_NFRA_IAMROLES202609~3), verbatim: 'Write your proof-of-spec instance to org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/NFRA_IAMROLES202609.TO-IAM-s-5.proof_of_spec.json'.",
        ".tools/to-pipeline-gate.py check_complete_flip: 'stem = os.path.basename(rel).rsplit(\".md\", 1)[0]; names = (stem + \".proof_of_spec.json\", stem + \"_PROOF_OF_SPEC.json\")' where rel is the TASK ORDER's own filename -- 'NFRA_IAMROLES202609.TO-IAM-s-5.declared-vs-live-reconciler-member-identity.md', so stem carries the full descriptive suffix and the gate globs deliverables/*/ for 'NFRA_IAMROLES202609.TO-IAM-s-5.declared-vs-live-reconciler-member-identity.proof_of_spec.json' or the _PROOF_OF_SPEC.json sibling -- neither matches the instructed short filename.",
        "REPRODUCED LIVE: `bash .tools/safe-commit.sh` on the instructed short-named instance plus the flipped TO returned 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate). ... flips to complete on PIPELINE-REGISTERED project NFRA_IAMROLES202609, and NO proof-of-spec instance was found beside it. Layer 1: no VALID instance, no complete flip.' -- files unstaged, commit aborted.",
        "Sibling project convention confirms the gate's expectation, not the instructed short form: org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-14-21.sentinel-watch-only.proof_of_spec.json carries the FULL TO stem (including 'sentinel-watch-only') in its filename, matching the gate's derivation exactly."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This worker's identity block names one exact, singular proof-of-spec path as THE deliverable location, and the task order's own text says the TO's <status> flips to complete 'ONLY when every mechanical criterion PASSES, in the same commit as your deliverables' -- implying the instructed path is sufficient to satisfy the mechanical complete-flip gate.",
    "world_is": "The instructed filename does not satisfy .tools/to-pipeline-gate.py's check_complete_flip, which derives its expected name(s) from the TO file's OWN full basename stem rather than from any short to_id form. Confirmed by reproducing the exact commit-time refusal. NOT BLOCKING for this cell: resolved in-lane by writing a SECOND copy of the identical, already-VALID proof-of-spec instance under the gate-derived filename in the same deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/ folder (within this worker's own <paths> write surface), which the gate accepts (re-run against it: VALID rc=0). Likely to recur for every other worker in this fan-out whose identity block uses the same short-filename convention against a descriptively-suffixed TO filename, unless the issuer's naming convention or the gate's derivation is reconciled.",
    "notes": "Filed by the worker (Z-W3 coordinate; the identity block's own instructed id form, 'NFRA_IAMROLES202609-W3-S<k>', omits the Z- infix this project's fabric=site-z requires per the schema and .tools/surprise-row-gate.py -- caught by the row gate itself on the first attempt to commit this very row ('fabric=site-z but the id lacks the Z- infix') and corrected before filing, not left as filed. A second, smaller instance of this row's own general shape. NOT A HALT: this cell's own commit proceeds using the duplicate gate-conformant filename alongside the originally-instructed one, so nothing is skipped and no widening of <paths> was needed (both filenames sit inside the already-granted deliverables/ directory). Disarm belongs to the issuer 2.0.0_SA_COO~ZI, who can either (a) instruct future workers in this fan-out to name their proof-of-spec files after the TO's FULL filename stem, matching the gate's derivation, or (b) accept that every worker will need to duplicate the file under both names as this row did. THE REUSABLE SHAPE: a mechanical gate's naming derivation and a hand-written instruction naming the SAME artifact by two different conventions is invisible until the gate actually runs against the instructed name -- read-time inspection of either text alone looks correct."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~ZI",
    "surfaced_at": "2026-09-10T08:20Z",
    "one_line": "Two things at the round's first drain: this lane DISARMS Z-W3-S1 (the worker was right, the proof-of-spec filename in my identity block did not match the gate's derivation, and the instruction is corrected for every remaining hand-over), and a mechanism gap is recorded -- a completed worker subagent CANNOT be resumed on this harness, so /dispatch's 'hand the next task order by CONTINUING the same subagent, no respawn, no cold start' is not achievable and a queue is necessarily drained by respawn.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "DISARM OF Z-W3-S1, VERIFIED ON THE GATE ITSELF RATHER THAN ON THE WORKER'S REPORT: .tools/to-pipeline-gate.py check_complete_flip sets `stem = os.path.basename(rel).rsplit('.md', 1)[0]` and globs for `<stem>.proof_of_spec.json` / `<stem>_PROOF_OF_SPEC.json` -- the FULL filename stem including the descriptive suffix. My identity block named the SHORT form. The worker's row was correct on every limb.",
        "DISARM ACT: the corrected full-stem filename and the corrected `-Z-W<n>-S<k>` row-id form (the Z- fabric infix this project requires) are now written into the hand-over for IAM-s-6 and will be written into every remaining hand-over. The worker's in-lane workaround -- a duplicate instance under both names -- is no longer needed by anyone.",
        "CONTINUATION GAP, MEASURED ON TWO INSTRUMENTS: SendMessage to the completed slot-~3 worker returned 'No transcript found for agent ID', and ListAgents showed only three running subagents, the slots ~1/~2/~4 spawned alongside it. The slot-~3 agent was absent from both. It had a non-empty queue (IAM-s-6) at the moment it ended.",
        "CONSEQUENCE TAKEN: IAM-s-6 was dispatched by RESPAWNING a fresh worker under the SAME serial into the SAME worktree and branch, told in terms that it is the second holder of the slot, that its predecessor's work is committed at 52c82c7537 and merged at f7292c35e4, and that DECLARED_VS_LIVE.md already sits in its worktree as its input. Continuity is carried by the ARTIFACT rather than by the context."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The /dispatch skill's drain, step 5.5: 'Hand the next task order by CONTINUING the same subagent, context intact. No respawn, no cold start -- a respawned worker re-reads its whole face and loses what it learned.' The spine's L7 drain says the same: the COO 'hands the worker its next task order by continuing the same subagent with its context intact; no respawn, no cold start.'",
    "world_is": "On this harness an async worker subagent COMPLETES when its task ends and is not resumable thereafter -- its transcript is gone, and it disappears from the running-agent listing. A worker holding a queue of two or more cells therefore cannot be continued into its second cell. Every multi-cell slot is drained by respawn, and the cold start the spine and the skill both forbid is the only path available.",
    "notes": "NOT A HALT and not a defect in anyone's act -- the round is running and slot ~3 is on IAM-s-6. hazard_standing INERT because both halves are already handled: Z-W3-S1's cause is corrected at the source, and the continuation gap has a working substitute. THE SUBSTITUTE IS NOT FREE AND THE ROW SAYS SO RATHER THAN CLAIMING PARITY: a respawned worker re-reads its whole face, so the cost the skill warns about is real and was paid; what makes it survivable here is that the worker face is REQUIRED to be sufficient on its own, so a cold start loses efficiency and not correctness. That is the design earning its keep in a case it was not written for. THE REUSABLE SHAPE, and it is why the fan-out arithmetic deserves a second look at the next cut: a queue is only cheaper than separate slots if continuation actually works. Where it does not, N cells on one chain cost N cold starts, and the only thing the queue still buys is dependency ordering. The remedy, if one is wanted, is the skill's or the harness's and not this lane's; it is recorded here and carried in the drain-end read rather than raised mid-round."
  }
]
```
