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
    "id": "NFRA_IAMROLES202609-Z-W3-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~3",
    "surfaced_at": "2026-09-10T08:45:23Z",
    "one_line": "comp-find --corpus aws classifies seeking-alpha-scraper-role as LIVE-no-DECLARED, but it is genuinely declared in Terraform (resource \"aws_iam_role\" \"seeking_alpha_role\" { name = \"seeking-alpha-scraper-role\" ... } at infra/aws/terraform/seeking-alpha/main.tf:240-241) and comp-iam's own Terraform parse lists it directly by that exact name -- one member of IAM-s-5's settled 16 is a false positive on the drift plane, corrected here to IN-CODE rather than dispositioned as an exemption.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/seeking-alpha/main.tf:240-241 @52c82c7537 (unchanged in this worktree): 'resource \"aws_iam_role\" \"seeking_alpha_role\" {' then 'name = \"seeking-alpha-scraper-role\"' -- a genuine, name-matching IAM role declaration in first-party Terraform source.",
        "This cell's own fresh `.tools/comp-iam roles` run at 2026-09-10T08:48:35Z lists it directly: 'seeking-alpha-scraper-role' / 'tf_resource: seeking_alpha_role' / 'source: infra/aws/terraform/seeking-alpha/main.tf' -- a second, independent instrument, same conclusion.",
        "IAM-s-5's deliverable (DECLARED_VS_LIVE.md @52c82c7537, this same folder) carries seeking-alpha-scraper-role inside the 16-member LIVE-no-DECLARED set measured via `comp-find '.' --corpus aws IAM_ROLE --all` at vintage 2026-09-10 05:57:16 UTC (DECLARED=203 LIVE-no-DECLARED=16 of 219 nodes) -- the two instruments disagree about the same named role at overlapping vintages.",
        "Corroborating drift recorded so a later aggregate-count reader is not misled by it (not this row's main claim): this cell's fresh `.tools/comp-iam stats` (2026-09-10T08:48:35Z) reports 'IAM roles parsed: 191', not the 195 this TO's own BATTERY FINDINGS section cites from the L5-lane preflight -- a live Terraform-source-parsed count that does not hold across a same-day re-run. This cell's 16-member dispositions do not depend on the aggregate count, only on the per-name checks above and in GOVERNANCE_DISPOSITION.md."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This TO's BATTERY FINDINGS state 'comp-find --corpus aws: RUN -- 219 IAM_ROLE nodes, DECLARED=203, LIVE-no-DECLARED=16' and instruct this cell to dispose of exactly that 16-member set as IAM-s-5 established it; separately, the bound instructs that 'a role you cannot find in Terraform via comp-iam is a role to look for BY NAME before you class it EXEMPT' for the comp-iam parser specifically.",
    "world_is": "One member of the 16, seeking-alpha-scraper-role, IS declared in Terraform by exact name, confirmed independently via direct source read and via a fresh comp-iam parse -- the LIVE-no-DECLARED drift classification comp-find --corpus aws assigned it does not match ground truth in source. NOT BLOCKING for this cell: resolved in-lane, this member is dispositioned IN-CODE (not exempt) in GOVERNANCE_DISPOSITION.md item 13, and the other 15 members were separately confirmed absent from both a fresh comp-iam parse and first-party Terraform source, so the correction is scoped to this one member and does not unsettle the rest of the set.",
    "notes": "The bound anticipated exactly this failure mode for comp-iam's PARSER blindness ('classing a declared-but-unparsed role as EXEMPT would manufacture a governance finding'); this instance surfaced on the comp-find --corpus aws DRIFT-CLASSIFICATION plane instead, a different instrument answering the same DECLARED question and getting it wrong for the same named role. THE REUSABLE SHAPE: two instruments both claiming to answer 'is this declared', built on different mechanisms (a Terraform-source parser vs. a live-graph-to-declared cross-reference), can and did disagree about one concrete member while a downstream consumer (IAM-s-5, then this cell) was instructed to treat the drift plane's classification as the settled set. A name-level check against the OTHER instrument is what caught it, not a wider read of either instrument alone. Remedy (reconciling why the DECLARED-vs-LIVE cross-reference misses a role that IS in Terraform source) is a tooling fix outside this cell's <paths> and outside a worker's lane; named to 1.0.0_SA_CTO~Z as the seat this fabric's L10 always routes tooling/spec-plane defects through."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~3",
    "surfaced_at": "2026-09-10T08:45:23Z",
    "one_line": "Three of the 16 undeclared roles (ecsTaskExecutionRole, rds-monitoring-role, vpc-flow-logs-role) carry the exact conventional names AWS's own console/service quick-create flows assign, but this worker has no CloudTrail or console-history access to confirm the origin and no authority to sign a formal exemption -- dispositioned exempt with owner=UNASSIGNED per the bound's own instruction, and the decision (confirm origin, name a real owner) is owed and unmade.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "GOVERNANCE_DISPOSITION.md (this folder) items 4, 12 and 15: all three names absent from this cell's fresh `.tools/comp-iam roles` parse (2026-09-10T08:48:35Z, 191 roles) and from every first-party Terraform file this cell searched via `.tools/comp-find '<name>' infra/ --all` -- only world-model census/inventory JSON mentions any of the three, never a `resource \"aws_iam_role\"` block.",
        "IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes name these three as 'AWS SERVICE-DEFAULT roles, the kind a console action or managed service mints on its own' -- a plausibility this cell re-checked by name rather than inheriting, and did not find contradicted, but also could not confirm (no CloudTrail CreateRole event access from this worker's tooling).",
        "The task order's own bound, quoted exactly: 'AN EXEMPTION IS A DECISION SOMEONE MAKES, NOT ONE YOU MINT ... Where a member plainly needs an owner you cannot name, record the disposition as EXEMPT with owner=UNASSIGNED and a reason stating what decision is owed and by whom, AND FILE A SURPRISE ROW naming it.'"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FWD-4's ACCEPT: 'Something deliberately kept outside the normal way of doing things says who decided that and why' -- an exemption needs a named decision-maker, and this cell's bound forbids this worker from minting one.",
    "world_is": "No named decision-maker exists anywhere in this repo for any of these three roles' Terraform-exclusion; this worker cannot mint one. Recorded as exempt, owner=UNASSIGNED, reason naming the decision owed, in GOVERNANCE_DISPOSITION.md items 4, 12 and 15. NOT BLOCKING: the cell's shape is satisfied (every member carries a token; every exempt line carries an owner and a reason) -- what remains open is the actual sign-off, which is a decision for a seat with cloud-IAM-governance authority, not a defect in this cell's output.",
    "notes": "Grouped as one row for three members sharing the same class and the same remedy shape (confirm origin, then name an owner), rather than filing three near-identical rows for the same unresolved decision. Disarm: 2.0.0_SA_COO~ZI can route this to whichever seat holds cloud-IAM-governance sign-off authority, or accept the exempt/UNASSIGNED disposition as this round's answer and carry the open decision forward explicitly rather than let it read as closed."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~3",
    "surfaced_at": "2026-09-10T08:45:23Z",
    "one_line": "Two of the 16 undeclared roles (portal-auth-lambda-role, opal-data-refresh-lambda-role) sit on the production serving path -- portal-auth-lambda-role has zero Terraform touch and a distinctly-named declared sibling (opalinvest-auth-lambda-role) in the same module; opal-data-refresh-lambda-role backs a live Lambda by literal role_arn and is called 'pre-existing' in Terraform's own comment -- and this worker cannot make the heavier exemption call IAM-s-5's character note flags, so both are dispositioned exempt with owner=UNASSIGNED.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/portal-auth/iam.tf:16 @52c82c7537: `resource \"aws_iam_role\" \"auth_handler\"` declares `name = \"opalinvest-auth-lambda-role\"` -- a distinctly-named sibling in the same module as the undeclared `portal-auth-lambda-role`, confirmed NOT the same object; `portal-auth-lambda-role` itself has zero SURFACED/DEF hits anywhere in Terraform via `.tools/comp-find 'portal-auth-lambda-role' infra/ --all`.",
        "infra/aws/terraform/data-refresh/main.tf:38 @52c82c7537: `role_arn = \"arn:aws:iam::313476888478:role/opal-data-refresh-lambda-role\"` on the `data_refresh_api` Lambda module; main.tf:53 comment: 'SSCN S3 access -- inline policy attached to the pre-existing opal-data-refresh-lambda-role' -- Terraform attaches policies to this role by literal name but never creates it as a resource.",
        "GOVERNANCE_DISPOSITION.md (this folder) items 8 and 10 carry the full per-role citations and the reasoning; IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes: 'portal-auth-lambda-role, opal-data-refresh-lambda-role -- attached to functions on the production serving path.'",
        "The task order's own text: 'portal-auth-lambda-role and opal-data-refresh-lambda-role are PRODUCTION SURFACES ON THE SERVING PATH. An exemption here is a much heavier claim' -- naming the stakes without naming who bears them."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order names these two as carrying heavier exemption stakes than the rest of the set but does not name who decides; the bound forbids this worker from inventing that owner or quietly marking the line IN-CODE to avoid the requirement.",
    "world_is": "Neither role has a named decision-maker anywhere in this repo. Recorded as exempt, owner=UNASSIGNED, with the decision owed stated per-role in GOVERNANCE_DISPOSITION.md items 8 and 10. NOT BLOCKING: the shape this cell owes is met: every member carries a token, both exempt lines carry an owner and a reason. What remains open is a real sign-off on two roles this worker's own evidence shows sit closer to production than any other member of the set.",
    "notes": "Grouped as one row for the two members IAM-s-5's own character note singled out as the heavier class, distinct from the three service-default candidates (S3) and from the residue case (S5). Disarm: 2.0.0_SA_COO~ZI, given the production-serving-path stakes named in the task order itself; CLAUDE.md's own convention for served-output changes (never-widen sign-off, CTO+COO) suggests this decision likely needs more than one seat's word before either adoption or exemption is final, which this row states rather than resolves."
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S5",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_NFRA_IAMROLES202609~3",
    "surfaced_at": "2026-09-10T08:45:23Z",
    "one_line": "lambda-test-role reads as test/scratch residue rather than a serving role, which is a different remedy shape than either template this cell otherwise uses (add-to-Terraform, or except-with-reason) -- the real question is whether it is still exercised at all and should be retired, which neither IAM-s-5 nor this cell has usage-telemetry access or the mandate to answer, so it is dispositioned exempt with owner=UNASSIGNED naming that decision.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~ZI",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "`lambda-test-role` is absent from this cell's fresh `.tools/comp-iam roles` parse (2026-09-10T08:48:35Z) and from every first-party Terraform file searched via `.tools/comp-find 'lambda-test-role' infra/ --all` -- only world-model census/inventory JSON mentions it, with nothing describing its purpose or last use.",
        "IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes: 'lambda-test-role -- name suggests a test/scratch role rather than a serving-path role', and this TO's own cell text: 'lambda-test-role READS AS RESIDUE.'",
        "This cell's bound: 'DO NOT MODIFY ANY TERRAFORM AND DO NOT CREATE, DELETE OR EDIT ANY ROLE' -- retirement (deletion) is explicitly out of this cell's remedy even if it is the more likely correct answer for residue, so the binary IN-CODE/EXEMPT template does not fit this member cleanly and the gap between 'add to code' and 'the right answer might be delete it' is itself the finding."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "This cell's shape requires every member to carry either IN-CODE or EXEMPT with an owner and a reason; it does not provide a third disposition for a role that may not deserve to keep existing at all.",
    "world_is": "lambda-test-role is recorded exempt, owner=UNASSIGNED, reason naming retirement-vs-formalize as the decision owed, in GOVERNANCE_DISPOSITION.md item 7. NOT BLOCKING: the mechanical shape is met. What is open is a usage check (is this role still invoked) that this worker has no instrument for and no mandate to run, followed by a real decision either way.",
    "notes": "Filed separately from S3 and S4 because the remedy shape differs: those two classes end in 'adopt or except', this one may end in 'neither -- delete', a third outcome this cell's binary schema cannot express and does not attempt to. Disarm: 2.0.0_SA_COO~ZI, who can route a usage check to whichever seat has invocation-log or CloudTrail access, or accept the exempt/UNASSIGNED disposition as final for this round while naming the open question explicitly."
  }
]
```
