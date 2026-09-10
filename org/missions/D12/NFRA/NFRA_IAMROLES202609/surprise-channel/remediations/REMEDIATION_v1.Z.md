# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v1 (site Z) -- THE ROUND-1 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 1, 2026-09-10 ~11:4xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, BOTH LIMBS, SOURCE = THE INDEX** (`_latest_dispositions` imported and called):

```
18 items | UNDISPOSITIONED 0 | GRADUATED 15 | DISMISSED_WITH_REASON 3
task orders  9 of 9 TERMINAL, read UNSCOPED from their own <status> fields
JUDGMENT     9 of 9 graded at C-S4 -- EIGHT PASS, ONE FAIL (IAMs6-AC5)
             the set is NINE, de-duplicated: an instance-FILE census returns ELEVEN because two
             orders carry BYTE-IDENTICAL duplicate instances (C-S1)
CONTROL      the same census on NFRA_REPORT returns 27 items -- it fires on a second project
```

⛔ **SLUG-READY, NOT CLOSE-READY.** Rule 27 needs COMPLETION_REPORT + COMPLETION_GRADES with EVERY grade
REALIZED. `IAMs6-AC5` is a FAIL, and this project has **NO COMPLETION_REPORT at any round** -- the same
missing-record condition that blocks NFRA_OPSEC202609. A failed judgment criterion is a GRADED OUTCOME, not
an open item, so it does not block the slug; it rides it as a finding with a named remedy.

**THE ROUND'S SIGNATURE, so the recut reads the set rather than fifteen rows:** the HAND-OVER PROMPT IS NOT
THE COMMITTED ORDER. Four of four respawns delivered a worker face RICHER than the file on disk, and no gate
can catch it because no gate reads a spawn prompt. Every other thread is downstream of how this round was
issued rather than of what it found.

**`remedy` is carried VERBATIM from each row's own notes** where the row stated one; two rows carry a
different remedy and say why (`Z-S7` discharged at C-S4, `Z-S3` superseded by the comp-rail repair). `owner`
is the lane named by the row's own `disarm_owner`. **`remediation.state` is OPEN on all 15 and `disarm.state`
is ARMED wherever the source row was -- nothing here is claimed REMEDIATED or DISARMED.**

⚠ **NO L8 PACKET WAS EVER SENT FOR THIS ROUND.** `2.0.0_SA_COO~ZI` drained it and its completion report is
not written. This seat's L8 compile (`C-S1`) stands as the round's compile; where it and that lane's eventual
compile disagree, the disagreement is itself the finding.

**AUDITED GATE OVERRIDE**, fourth slug running, same structural reason: `_coordinate_violations` refuses a NEW
row carrying `W<n>` from a non-worker committer while protocol s.5 requires the remediation id to EQUAL the
graduated id.

---

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PRD v0.2 section 8's S5 evidence cell states two different role-population denominators in one sentence -- '16 of 208' and 'DECLARED=200 LIVE-no-DECLARED=16' (which sums to 216) -- and the live plane reads 219 today; the undeclared count itself has held at 16 throughout.",
    "evidence": [
      "PRD org/missions/D12/NFRA/NFRA_IAMROLES202609/prd/NFRA_IAMROLES202609_PRD.md @076f37eeb2 section 8 row S5 evidence cell: 'brief F2a: 16 of 208 undeclared is a SETTLED COUNT AND A SETTLED SET, corroborated across two substrates and re-measured at the merged head (216 hit(s) / 216 aws node(s), DECLARED=200 LIVE-no-DECLARED=16)'. 200 + 16 = 216, not 208; both denominators sit in one sentence with no reconciliation.",
      "Re-measured by this lane on the instrument the manifest names: comp-find '.' --corpus aws IAM_ROLE -- DENOMINATOR 219 hit(s) across 219 aws node(s) scanned [corpus=aws types=IAM_ROLE]; DRIFT (scanned) DECLARED=203 LIVE-no-DECLARED=16; VINTAGE built from the estate 2026-09-10T03:31:02Z, manifest 5361815924ce. 203 + 16 = 219.",
      "Population across three vintages: 208 (brief F2 @1a90986047) -> 216 (brief F2a merged head) -> 219 (this lane, 2026-09-10T03:31Z). DECLARED across the latter two: 200 -> 203. LIVE-no-DECLARED across all three: 16, 16, 16.",
      "A THIRD figure exists on the DECLARED plane and is NOT part of this finding: comp-iam stats parses 195 IAM roles from Terraform. That is a different plane and a different instrument (comp-iam emits two NOTEs that role labels 'orchestrator' and 'scheduler' were reused across modules and silently mis-linked pre-fix), so 195-vs-203 is not drift and is recorded in the decomposition at section 1b so a later reader does not read it as such."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): Filed at L5 by the decomposition's owner, not by a worker, so the id carries the site-Z fabric coordinate and no W allocator coordinate. NOT A HALT: L5 completed and all nine cells are OPEN. The remedy is an edit to the PRD's section 8 S5 evidence cell (re-pin the denominator with its vintage, or state which of the two it means), which is lane ANY_CTO and belongs to 1.0.0_SA_CTO~Z; this lane cannot make it and does not propose the wording. DISARMED is not REMEDIATED. The general shape, which the PRD itself names one paragraph earlier about a different citation: a number goes stale fastest when nothing in the fabric announces that the world moved under it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Relayed spine v3.7 states the L7 worker's model is Opus at high effort BY THE AGENT TYPE'S OWN DEFINITION, but this fabric's .claude/agents/worker.md reads 'model: sonnet' at HEAD -- the amendment and the worker.md edit that carries it are both local to the laptop fabric, so every worker spawned on site-Z runs at a model the amendment does not intend, and no per-spawn override is lawful to correct it.",
    "evidence": [
      "MEASURED AT HEAD WITH git show, not by reading the worktree path: `git show HEAD:.claude/agents/worker.md` returns frontmatter `name: worker` / `model: sonnet` at HEAD b5bad26a0c. The worktree copy agrees, so this is not an unlanded local edit being misread -- both planes say sonnet.",
      "The spine at HEAD is 462 lines and its changelog's newest row is version 3.6 (`git show HEAD:org/ref/CANONICAL_FABRIC_WORKFLOW_20260901.md`). v3.7, v3.8 and v3.9 are absent from this fabric entirely.",
      "The relay is 0.0.0_AB_MSTR~Z msg 20764 (SPAWN-DIRECT, ACKed by this lane), which states: 'v3.7 -- the L7 worker's model is Opus at high effort BY THE AGENT TYPE'S OWN DEFINITION (.claude/agents/worker.md). NEVER chosen per task order, NEVER a per-spawn override. This is a constraint on how you SPAWN workers.' The same message declares all three amendments LOCAL to the laptop, 462 lines here vs 480 there, and RELAY-GRADE NOT MEASURED.",
      "The two clauses of v3.7 come apart on this fabric and that is the whole finding: its MECHANISM (never a per-spawn override) is honourable here and is honoured -- round 1's workers are spawned with NO model parameter, taking whatever the agent type's definition says. Its VALUE (Opus at high effort) is not present, because the definition it points at says sonnet."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): Filed by a seat at L6/L7, not by a worker, so the id carries the site-Z coordinate and no W allocator coordinate. NOT A HALT: round 1's spawn proceeds on the agent type's own definition, whatever it says, and the round runs. This row records a DIVERGENCE, not a defect in anyone's act -- the relay was honest about being relay-grade and told this lane to re-read the spine once the amendments land. The remedy is the cross-fabric landing of v3.7-v3.9 plus whatever worker.md edit that implies, which is process law (1.0.0_SA_CTO~Z as the spine's scribe) carried across fabrics by the integrator (0.0.0_AB_MSTR~Z); it is not this lane's to make and this lane does not propose the model value. THE REUSABLE SHAPE, which is why this is worth a row rather than a shrug: an amendment that fixes a VALUE by pointing at a DEFINITION travels only as far as that definition does. Relaying the amendment's text across a fabric boundary carries the constraint and leaves the value behind, and the two halves then disagree with nothing able to fail -- the spawn succeeds, the worker runs, and only a reader who checks the definition against the relay can see it.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "This lane's own L6 cut carried one defective criterion -- IAM-s-3 AC2 invoked comp-find BY BARE NAME, which from a worker's worktree censuses the MAIN checkout and would have returned a large confident denominator over a tree that does not contain the worker's extension; fixed before the order was handed out. The same measurement REFINES INSTRUMENT_LIMITS.md LIMIT 4: the limit belongs to the BARE NAME, not to the tool, because the explicit .tools/comp-find path honours the caller's worktree.",
    "evidence": [
      "DISCRIMINATOR USED, chosen so a false zero and a true absence cannot read alike: `catviews-cottonwood-inflection.json` exists ONLY in the main checkout (untracked there, absent from every fresh worktree; `ls` confirms both halves).",
      "BARE NAME, run from /c/tmp/wk-iamroles-1: `comp-find --name 'catviews-cottonwood-inflection.json'` returns 1 hit across 55375 file(s) scanned -- a HIT for a file that does not exist in the caller's tree, with a denominator byte-identical to the main tree's. It read the MAIN checkout regardless of PWD.",
      "EXPLICIT PATH, same worktree, same query: `.tools/comp-find --name 'catviews-cottonwood-inflection.json'` returns 0 hit(s) across 31052 file(s) scanned -- the WORKTREE's own denominator, and a correct absence. Positive control from the main tree: 1 hit across 55377 scanned.",
      "MECHANISM, re-derived rather than assumed: `command -v comp-find` resolves to /c/Users/Opal Bloomberg/bin/comp-find, a ~/bin forwarder whose own script directory is the MAIN checkout -- so _comprail.repo_root()'s script-relative resolution lands on main. Invoked as .tools/comp-find from a worktree, that same script-relative rule lands on the worktree. Both behaviours follow from ONE rule; the entry states the rule and draws only one of its two consequences.",
      "SIBLING FORWARDER CHECKED AND IT IS SOUND, which is why this round's other criteria stand: .tools/comp-iam-usage sets WORKSPACE=\"$(cd \"$(dirname \"$0\")/..\" && pwd)\" and, re-derived from /c/tmp/wk-iamroles-1, resolves to /c/tmp/wk-iamroles-1 -- so a worker invoking it by explicit path exercises ITS OWN edited module. IAM-s-1's AC1-AC4 and IAM-s-3's AC3 are therefore correct as cut.",
      "SCOPE NOT CLAIMED: comp-read and comp-which share the shim shape and were NOT separately exercised here, exactly as msg 20828 declares of its own arms. This row claims comp-find only."
    ],
    "remedy": "SUPERSEDED BY A REPAIR, not by this round. The corpus_root split landed at @6228c53377 and is ON ORIGIN at ae556f5712, so a comp-find / comp-read / comp-pulse census from a linked worktree now scans that worktree. Z-S3's bare-name-vs-explicit-path remedy is moot for those three tools on this fabric. NOT RETROACTIVE: any figure quoted from a worktree BEFORE that commit was still measured over the wrong tree, and the other fabric does not have the repair until it pulls.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Two things at the round's first drain: this lane DISARMS Z-W3-S1 (the worker was right, the proof-of-spec filename in my identity block did not match the gate's derivation, and the instruction is corrected for every remaining hand-over), and a mechanism gap is recorded -- a completed worker subagent CANNOT be resumed on this harness, so /dispatch's 'hand the next task order by CONTINUING the same subagent, no respawn, no cold start' is not achievable and a queue is necessarily drained by respawn.",
    "evidence": [
      "DISARM OF Z-W3-S1, VERIFIED ON THE GATE ITSELF RATHER THAN ON THE WORKER'S REPORT: .tools/to-pipeline-gate.py check_complete_flip sets `stem = os.path.basename(rel).rsplit('.md', 1)[0]` and globs for `<stem>.proof_of_spec.json` / `<stem>_PROOF_OF_SPEC.json` -- the FULL filename stem including the descriptive suffix. My identity block named the SHORT form. The worker's row was correct on every limb.",
      "DISARM ACT: the corrected full-stem filename and the corrected `-Z-W<n>-S<k>` row-id form (the Z- fabric infix this project requires) are now written into the hand-over for IAM-s-6 and will be written into every remaining hand-over. The worker's in-lane workaround -- a duplicate instance under both names -- is no longer needed by anyone.",
      "CONTINUATION GAP, MEASURED ON TWO INSTRUMENTS: SendMessage to the completed slot-~3 worker returned 'No transcript found for agent ID', and ListAgents showed only three running subagents, the slots ~1/~2/~4 spawned alongside it. The slot-~3 agent was absent from both. It had a non-empty queue (IAM-s-6) at the moment it ended.",
      "CONSEQUENCE TAKEN: IAM-s-6 was dispatched by RESPAWNING a fresh worker under the SAME serial into the SAME worktree and branch, told in terms that it is the second holder of the slot, that its predecessor's work is committed at 52c82c7537 and merged at f7292c35e4, and that DECLARED_VS_LIVE.md already sits in its worktree as its input. Continuity is carried by the ARTIFACT rather than by the context."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): NOT A HALT and not a defect in anyone's act -- the round is running and slot ~3 is on IAM-s-6. hazard_standing INERT because both halves are already handled: Z-W3-S1's cause is corrected at the source, and the continuation gap has a working substitute. THE SUBSTITUTE IS NOT FREE AND THE ROW SAYS SO RATHER THAN CLAIMING PARITY: a respawned worker re-reads its whole face, so the cost the skill warns about is real and was paid; what makes it survivable here is that the worker face is REQUIRED to be sufficient on its own, so a cold start loses efficiency and not correctness. That is the design earning its keep in a case it was not written for. THE REUSABLE SHAPE, and it is why the fan-out arithmetic deserves a second look at the next cut: a queue is only cheaper than separate slots if continuation actually works. Where it does not, N cells on one chain cost N cold starts, and the only thing the queue still buys is dependency ordering. The remedy, if one is wanted, is the skill's or the harness's and not this lane's; it is recorded here and carried in the drain-end read rather than raised mid-round.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S5",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Worker row NFRA_IAMROLES202609-W2-S1 declares \"fabric\": \"laptop\" on a project whose row reads fabric: site-z, and carries no Z- infix. The two are consistent with each other, which is the point: the worker met the id-grammar gate by declaring the WRONG FABRIC rather than by adding the infix -- and the merged-index row gate exempted it from the foreign-row sweep, so nothing caught it.",
    "evidence": [
      "The row at HEAD carries \"fabric\": \"laptop\" and id NFRA_IAMROLES202609-W2-S1. org/missions/D12/NFRA/NFRA_IAMROLES202609/project.json reads \"fabric\": \"site-z\", and every other row in this channel -- including the two filed by slot ~1 and the one by slot ~3, all workers under the same issuance -- reads site-z and carries the Z- infix.",
      "MECHANISM, and it is why this is not simply carelessness: the issuer's identity block instructed the id form 'NFRA_IAMROLES202609-W<n>-S<k>' with NO Z- infix. surprise-row-gate.py refuses that form when fabric=site-z. Slots ~1, ~3 and ~4 each resolved it by ADDING the infix; slot ~2 resolved the same refusal by declaring fabric=laptop, which makes the instructed id lawful. Both routes satisfy the gate. One of them records a false fact.",
      "THE MERGE DID NOT CATCH IT AND SAID SO IN TERMS: at the drain, safe-merge.sh printed 'foreign-row sweep exempt for 1 row(s) a PARENT carried, attributed to 1 seat(s) (0.9.0_WK_NFRA_IAMROLES202609) and graded at their own authorship.' The exemption is correct policy -- the integrator is not the row's author -- and its consequence is that a wrong field value on a foreign row reaches HEAD ungraded.",
      "NOT EDITED IN PLACE, deliberately: the channel is append-only and a worker's row is graded at its own authorship, so the row was carried VERBATIM through the union resolution and the correction is this row instead."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): ROOT CAUSE IS THE ISSUER'S, NOT THE WORKER'S: the instructed id form omitted the Z- infix and the worker was given no fabric guidance at all, so it chose the branch that satisfied the gate. Already corrected at the source -- every hand-over since names both the Z- infix and fabric=site-z explicitly, and the IAM-s-8 hand-over to this same slot says in terms not to repeat it. disarm_owner is 3.0.0_SA_CVO~Z rather than this lane because the remedy is a DISPOSITION on a foreign row at L9, not an edit this seat may make. LOW SEVERITY, STATED SO IT IS NOT INFLATED: the row's substance -- the proof-of-spec filename defect -- is correct, corroborated by three sibling rows, and already disarmed; only the fabric field is false, and its practical effect is on census and routing, not on the finding. THE REUSABLE SHAPE: when a gate enforces INTERNAL CONSISTENCY between two fields and an instruction makes one of them wrong, the cheapest way past the refusal is to corrupt the OTHER field -- and the result passes every check, because it is now self-consistent.",
    "owner": "3.0.0_SA_CVO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "3.0.0_SA_CVO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S6",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "THE SETTLED SET OF 16 CONTAINS AT LEAST ONE FALSE POSITIVE, independently confirmed: seeking-alpha-scraper-role is declared in Terraform, so the undeclared population is at most 15. Stability across three vintages was never evidence of correctness. Plus: this lane DISARMS the five naming rows (one defect, five reports), and states that Z-W3-S3/S4/S5 are NOT disarmable in this lane.",
    "evidence": [
      "INDEPENDENT CONFIRMATION OF Z-W3-S2 ON A DIFFERENT INSTRUMENT than the worker used. The worker read comp-find --corpus aws plus a fresh comp-iam roles parse. This lane read the Terraform source directly under a pathspec: `.tools/comp-find 'seeking-alpha-scraper-role' infra/aws/terraform` returns 1 hit across 569 files scanned -- infra/aws/terraform/seeking-alpha/main.tf:241: name = \"seeking-alpha-scraper-role\". Corroboration, not repetition.",
      "NEGATIVE CONTROL, so a false zero and a true absence cannot read alike: the same command for lambda-test-role, a member nobody disputes is undeclared, returns 0 hits across the same 569 files. The probe discriminates.",
      "CONSEQUENCE FOR THE PROJECT'S CENTRAL CLAIM: the PRD, the brief (F2/F2a) and the L5 decomposition all lean on '16 undeclared roles' as a SETTLED SET AND A SETTLED COUNT, corroborated across two substrates and three vintages. At least one member of that set is declared. The undeclared population is therefore AT MOST 15, and the ratified FWD-4 bar is measured against a set whose membership the estate's own instrument gets wrong.",
      "WHY NEITHER EARLIER CELL COULD HAVE CAUGHT IT, which is the reusable half. IAM-s-5 established MEMBER IDENTITY by classing each member against the L5 lane's enumerated list -- that is the SAME INSTRUMENT'S OUTPUT AT TWO VINTAGES, so it could only ever confirm that the classifier was CONSISTENT, never that it was CORRECT. IAM-s-6 caught it because disposing of each member forced a per-member read against Terraform, which is a DIFFERENT plane from the one that built the set. C-TWO-REMEDIES earned its keep here in a way nobody predicted: splitting governance from permissions is what forced the second instrument onto the same members.",
      "DISARM OF THE NAMING FAMILY -- FIVE ROWS, ONE DEFECT: Z-W1-S1, Z-W1-S2, W2-S1, Z-W3-S1 and Z-W4-S1 all report the same issuer error (the proof-of-spec filename instructed in short form against a gate that globs the TO's full basename stem, plus the row-id form missing the site-z Z- infix). Verified at the gate itself and corrected at source; every hand-over from IAM-s-6 onward names the full-stem filename, the Z- infix and fabric=site-z explicitly. No later worker has hit it. Recorded once here rather than five times."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): SCOPE OF THE CLAIM, STATED NARROWLY: this row establishes ONE false positive, on one member, on evidence. It does NOT claim the other 15 are wrong, does not claim a rate, and does not claim the drift class is unfit -- a single false positive in a 16-member set is a finding about the SET's membership, not yet a finding about the instrument's reliability. Establishing that would need the same Terraform read run against all 16, which is a cell nobody has cut. hazard_standing ARMED with disarm_owner 1.0.0_SA_CTO~Z, matching Z-W3-S2, because the remedy touches the PRD's and the brief's headline figure and both are lane ANY_CTO. THREE ROWS THIS LANE OWNS AND CANNOT DISARM, stated rather than left to look neglected: Z-W3-S3 (three AWS-service-default roles need a named exemption owner), Z-W3-S4 (two production serving-path roles carry a heavier exemption claim) and Z-W3-S5 (lambda-test-role needs a retire-vs-formalize decision). Each needs a DECISION ABOUT A REAL ROLE'S OWNERSHIP OR RETIREMENT, which is outside this lane -- the task order itself forbade the worker inventing an owner, and the same bar binds the issuer. They are not disarmed, they are not abandoned, and they ride this round's drain-end read to 1.0.0_SA_CTO~Z.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S7",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-W1-S4 CONFIRMED AND IT IS SYSTEMATIC, NOT A ONE-OFF: every one of this round's four respawn hand-overs delivered a worker face RICHER than the committed task order, so the CVO grades AC5 from a file that is narrower than the bar the worker was actually held to. The delivered bar for IAM-s-9's AC5 is carried in this row so L9 has it.",
    "evidence": [
      "CONFIRMED ON THE COMMITTED FILE, with a positive control so the zeros are absences and not a broken probe: TO-IAM-s-9 at HEAD contains 0 occurrences of the one-role scope bound and 0 of the seeking-alpha finding, while the control string 'PATHS -- your write surface' returns 1 in the same file.",
      "SYSTEMATIC ACROSS THE ROUND, measured per order against text this lane actually sent in the hand-over prompt: IAM-s-2 (the do-not-quote-a-figure-forward bound) 0; IAM-s-6 (the bare-name comp-tool instrument note) 0; IAM-s-8 (the dependencies-already-in-your-tree detail) 0; IAM-s-9 (the one-role scope bound) 0. Four of four. Same positive control fires.",
      "THE DELIVERED BAR FOR IAM-s-9 AC5, so L9 grades what the worker was held to rather than what the file says: the hand-over required the harness to carry IAM-s-2's ONE-ROLE scope caveat forward, on the stated ground that 'a harness that reproduces the number while dropping the scope caveat would manufacture an estate-wide claim nobody made'. THE WORKER COMPLIED: rerun-assessment.sh contains 4 occurrences of the one-role/not-the-estate scope language, verified by this lane at the branch.",
      "THE MECHANISM, and it is a v3 consequence nobody wrote down. The spine says a worker face is never patched by a message, which assumes the face travels ONCE at the cut. On this harness a completed worker cannot be resumed (Z-S4), so EVERY cell after a slot's first is a fresh spawn whose prompt re-states the face -- and a re-stated face is an OPPORTUNITY TO IMPROVE IT. Improving it is the right instinct and it silently forks the record: the worker is held to the better bar, the CVO reads the older file."
    ],
    "remedy": "DISCHARGED AT C-S4. This row's only closing act was GRADING AC5 AGAINST THE DELIVERED BAR, and the nine judgment grades did exactly that -- IAM-s-9's AC5 was graded on the text Z-S7 carries rather than on the narrower committed file. The FINDING remains live for the next round and is why the row still graduates: no gate compares a spawn prompt to the order it claims to carry, so the divergence will recur unless the next issuance stops enriching hand-overs without amending the file.",
    "owner": "3.0.0_SA_CVO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "3.0.0_SA_CVO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The dispatch prompt for TO-IAM-s-1 named the proof-of-spec deliverable path as '<TO_ID>.proof_of_spec.json' (the shortened id, no descriptive suffix), but the live gate .tools/to-pipeline-gate.py:check_complete_flip globs on the TO FILE'S FULL BASENAME STEM ('<TO_ID>.<descriptive-suffix>.proof_of_spec.json') -- the shortened name is invisible to it and the status-flip commit was REFUSED with 'NO proof-of-spec instance was found beside it' even though the correctly-scoped file existed in the same staged commit.",
    "evidence": [
      "Spawn/dispatch prompt for 0.9.0_WK_NFRA_IAMROLES202609~1 (IDENTITY section, this session) states verbatim: 'Write your proof-of-spec instance to org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~1/NFRA_IAMROLES202609.TO-IAM-s-1.proof_of_spec.json' -- the shortened form.",
      ".tools/to-pipeline-gate.py check_complete_flip(): `stem = os.path.basename(rel).rsplit('.md', 1)[0]; names = (stem + '.proof_of_spec.json', stem + '_PROOF_OF_SPEC.json')` against the TO's own basename 'NFRA_IAMROLES202609.TO-IAM-s-1.permission-grain-usage-instrument.md' -- the only names it globs for both carry the full descriptive suffix; the shortened form is not a candidate under either branch.",
      "Reproduced directly: `bash .tools/safe-commit.sh ... -- org/modules/graph/comp_iam_usage.py .tools/comp-iam-usage <TO file, status flipped to complete> <deliverables>/NFRA_IAMROLES202609.TO-IAM-s-1.proof_of_spec.json` (all four staged in one call) -> commit-gate PASS, then 'ERROR: BLOCKED -- pipeline layer 2 (TO issuance gate)... NO proof-of-spec instance was found beside it', files unstaged. Every other existing tree-project instance sampled (NFRA_CLDGRPH.TO-CG-D-1.shared-image-rebuild-deriver-live.proof_of_spec.json, NFRA_OPSEC202609.TO-OP-S-8.identity-and-rbac-table-protection.proof_of_spec.json, and every other file under org/missions/**/deliverables/**/*.proof_of_spec.json) carries the FULL descriptive stem, confirming the shortened form is the outlier, not the convention."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): NOT A HALT: caught before any commit landed (safe-commit.sh unstages on refusal, so nothing was left half-committed); this lane renamed the file to the full-stem form and re-committed successfully. Filed as OBSERVATION/ARMED rather than BLOCKING because the fix was fully within this worker's own write grant and cost one rename -- but the SOURCE (the dispatch prompt template) is not this lane's to edit, hence disarm_owner is the issuing COO.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The same dispatch prompt told this worker its own surprise-row id grammar was '<PROJECT>-W<n>-S<k>' (no fabric infix), but this project's fabric is site-z and org/surprise_channel/schemas/investigation_item.schema.json + .tools/surprise-row-gate.py both require the Z- infix ('<PROJECT>-Z-W<n>-S<k>') for a site-z row -- a row minted exactly as instructed is REFUSED by the live gate.",
    "evidence": [
      "Spawn/dispatch prompt for 0.9.0_WK_NFRA_IAMROLES202609~1 states verbatim: 'Your surprise row id is NFRA_IAMROLES202609-W1-S<k>, k the next unused number within your slot's coordinate.' -- no Z- infix named anywhere in that instruction.",
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/project.json: 'fabric': 'site-z'.",
      "org/surprise_channel/schemas/investigation_item.schema.json id field description: '{PROJECT}-Z-W{n}-S{k} composes, fabric first' and 'The fabric coordinate is REQUIRED for site Z because both certifiers otherwise allocate the same sequence by construction'.",
      "Reproduced directly: staging this file with a row id 'NFRA_IAMROLES202609-W1-S1' and running the real commit path -> `.tools/safe-commit.sh` -> surprise-row-gate.py REFUSED with \"fabric='site-z' but the id lacks the Z- infix, which means 'laptop'. site-z iff the id carries Z-.\" rc non-zero, files unstaged."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): NOT A HALT: caught before any commit landed; this lane corrected both this row's and the sibling row's ids to carry the Z- infix before committing. Same root shape as Z-W1-S1 (a dispatch-prompt literal that a live gate does not accept) but a DIFFERENT gate and a DIFFERENT field, filed separately rather than folded in, since class is judged on form and these are two distinct mechanical facts. If the same dispatch-prompt template is reused for IAM-s-3 / IAM-s-2 / IAM-s-9 or other site-z worker spawns, it reproduces the identical refusal on their first surprise row, if any.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IAM-s-3 AC2's exact invocation ('.tools/comp-find 'unobservable' org/modules/graph --limit 20') scans 403 file(s) in this worktree, nowhere near either reference figure the criterion's own <expect> text names (~31,000 worktree-correct vs ~55,000 main-checkout-void per Z-S3's measurement) -- because AC2's own pathspec narrows the scan to one directory, and the bare-name-vs-explicit-path forwarder discrepancy Z-S3 measured (repo-wide) does not reproduce at this directory's scale: the main checkout scans only 404 files under the same pathspec, one more than the worktree.",
    "evidence": [
      "Invocation exactly as the TO's AC2 names it, run from this worktree: `.tools/comp-find 'unobservable' org/modules/graph --limit 20` -> 'DENOMINATOR: 38 hit(s) across 403 file(s) scanned in scope [corpus=all] | 11 EPHEMERAL-FLOOR, NOT searched | 4 BINARY, NOT searched'. 403 is neither 'about 31,000' nor 'near 55,000', the two figures the criterion's <expect> names as the pass/void discriminator.",
      "SAME invocation by BARE NAME (main-checkout forwarder, per Z-S3's own mechanism): `comp-find 'unobservable' org/modules/graph --limit 5` -> 'DENOMINATOR: 38 hit(s) across 404 file(s) scanned in scope'. Worktree (403) and main checkout (404) differ by exactly 1 file for THIS pathspec, not by the ~24,000-file gap Z-S3 measured repo-wide.",
      "Cause isolated with `.tools/comp-find --hidden org/modules/graph` vs bare `comp-find --hidden org/modules/graph`: worktree shows '0 searchable with --corpus all, 11 ephemeral/vendor floor'; main checkout shows '1 searchable with --corpus all, 174 ephemeral/vendor floor' -- the +1 searchable file accounts for the 403-vs-404 gap exactly. org/modules/graph is already merged between the two trees (IAM-s-1 landed and merged before this cell), so a directory-scoped pathspec has almost nothing left to discriminate on.",
      "Z-S3's own reference numbers (~31,000 / ~55,000) were measured with NO directory pathspec (`comp-find --name 'catviews-cottonwood-inflection.json'`, repo-wide) -- a different invocation shape than AC2's, which scopes to org/modules/graph per the decomposition's own instruction ('its census must run against the extended tool's own corpus')."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): NOT BLOCKING and NOT read as void: the criterion's OTHER stated condition ('a scanned count near 55,000 means the bare name was used') does not trigger (403 is nowhere near 55,000), and the invocation was run via the explicit .tools/ path exactly as instructed, printing a real denominator over the correct tree, discharging the decomposition's token-census debt (COVERAGE_VOCABULARY.md section 5 carries the full evidence and this row's citation). hazard_standing INERT: nothing about this finding requires a remedy to keep working -- the substance of AC2 (a printed denominator, over the worktree, via the explicit path) is satisfied; only the criterion's illustrative numeric anchor does not apply to its own pathspec-scoped invocation. THE REUSABLE SHAPE: a discriminator measured on one invocation SHAPE (repo-wide, no pathspec) was carried into a criterion whose actual invocation has a narrower shape (one directory, already-merged between trees), and the two shapes do not produce comparable denominators -- the numeric anchor traveled without the scope that produced it, same general class as Z-S3's own closing note about an instrument limit written as a property of the tool when it was a property of the invocation path.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W1-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "This worker's dispatch/spawn prompt for TO-IAM-s-9 (its WORKER FACE, this session's whole context) carries two clauses about carrying IAM-s-2's one-role scope caveat forward -- one appended to BOUNDS, one appended to AC5's meaning-note -- that are ABSENT from the committed TO file on disk; the committed record is narrower than what this worker was actually told to do.",
    "evidence": [
      "This session's dispatch prompt (WORKER FACE, IDENTITY block for 0.9.0_WK_NFRA_IAMROLES202609~1 on TO-IAM-s-9) states, as the closing paragraph of BOUNDS: 'AND CARRY IAM-s-2'S SCOPE STATEMENT FORWARD. Its posture figure is ONE ROLE, not the estate, and it says so repeatedly. A harness that reproduces the number while dropping the scope caveat would manufacture an estate-wide claim nobody made -- which is the exact failure FWD-1 and FWD-7 exist to prevent, arriving by a side door.'",
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-9.re-run-harness-composed-not-scheduled.md @c4a19f00ef (unchanged in this worktree at the time of this row), BOUNDS section: read in full, the block ends at 'COMPARABILITY REQUIRES THE DENOMINATOR AND THE VINTAGE TO TRAVEL. A re-run that prints a bare number is not comparable to anything -- that is acceptance property 1 and it binds here too.' -- no 'CARRY IAM-s-2'S SCOPE STATEMENT FORWARD' paragraph appears anywhere in the committed file.",
      "This session's dispatch prompt's AC5 meaning-note reads: 'Whether the harness is genuinely re-runnable BY A STRANGER, and whether it carries IAM-s-2's one-role scope caveat rather than implying an estate-wide claim, is graded by 3.0.0_SA_CVO~Z at L9.' The committed file's AC5 meaning-note (line 116) instead reads: 'Whether the harness is genuinely re-runnable BY A STRANGER is NOT self-gradeable by its builder or the COO -- graded by 3.0.0_SA_CVO~Z at L9.' -- shorter, and silent on the scope-caveat half entirely.",
      "Reproduced directly: `grep -c \"CARRY IAM-s-2\" org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-s-9.re-run-harness-composed-not-scheduled.md` -> 0, confirming the phrase this worker was dispatched with is not in the artifact a later reader (e.g. 3.0.0_SA_CVO~Z at L9, reading only the committed TO) would ever see."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): NOT A HALT and NOT BLOCKING: this worker followed the STRICTER (dispatch-prompt) instruction, which is a superset of the committed one, so no criterion is short-changed and the harness carries the scope caveat regardless of which text is authoritative. Filed because this is the SAME general shape as Z-W1-S1/Z-W1-S2/W2-S1/Z-W4-S1 (a dispatch prompt disagreeing with the committed record) but a DIFFERENT axis: those rows are about MECHANICAL GATE NAMING (a filename or an id-grammar the gate refuses), already disarmed at Z-S6; this one is about SUBSTANTIVE SPEC CONTENT (an added bound and an added judgment clause) that changes what AC5 is actually asking, with no mechanical gate able to catch a silent drop of it, since AC5 is judgment-only. Disarm routed to 2.0.0_SA_COO~ZI (this fan-out's issuer, who authored/generated the dispatch prompt) rather than self-resolved, because the fix is either amending the committed TO to match what was actually dispatched, or confirming the dispatch prompt over-stated the cell and no amendment is owed -- both are calls on the ISSUANCE, not on this worker's build.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "comp-find --corpus aws classifies seeking-alpha-scraper-role as LIVE-no-DECLARED, but it is genuinely declared in Terraform (resource \"aws_iam_role\" \"seeking_alpha_role\" { name = \"seeking-alpha-scraper-role\" ... } at infra/aws/terraform/seeking-alpha/main.tf:240-241) and comp-iam's own Terraform parse lists it directly by that exact name -- one member of IAM-s-5's settled 16 is a false positive on the drift plane, corrected here to IN-CODE rather than dispositioned as an exemption.",
    "evidence": [
      "infra/aws/terraform/seeking-alpha/main.tf:240-241 @52c82c7537 (unchanged in this worktree): 'resource \"aws_iam_role\" \"seeking_alpha_role\" {' then 'name = \"seeking-alpha-scraper-role\"' -- a genuine, name-matching IAM role declaration in first-party Terraform source.",
      "This cell's own fresh `.tools/comp-iam roles` run at 2026-09-10T08:48:35Z lists it directly: 'seeking-alpha-scraper-role' / 'tf_resource: seeking_alpha_role' / 'source: infra/aws/terraform/seeking-alpha/main.tf' -- a second, independent instrument, same conclusion.",
      "IAM-s-5's deliverable (DECLARED_VS_LIVE.md @52c82c7537, this same folder) carries seeking-alpha-scraper-role inside the 16-member LIVE-no-DECLARED set measured via `comp-find '.' --corpus aws IAM_ROLE --all` at vintage 2026-09-10 05:57:16 UTC (DECLARED=203 LIVE-no-DECLARED=16 of 219 nodes) -- the two instruments disagree about the same named role at overlapping vintages.",
      "Corroborating drift recorded so a later aggregate-count reader is not misled by it (not this row's main claim): this cell's fresh `.tools/comp-iam stats` (2026-09-10T08:48:35Z) reports 'IAM roles parsed: 191', not the 195 this TO's own BATTERY FINDINGS section cites from the L5-lane preflight -- a live Terraform-source-parsed count that does not hold across a same-day re-run. This cell's 16-member dispositions do not depend on the aggregate count, only on the per-name checks above and in GOVERNANCE_DISPOSITION.md."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): The bound anticipated exactly this failure mode for comp-iam's PARSER blindness ('classing a declared-but-unparsed role as EXEMPT would manufacture a governance finding'); this instance surfaced on the comp-find --corpus aws DRIFT-CLASSIFICATION plane instead, a different instrument answering the same DECLARED question and getting it wrong for the same named role. THE REUSABLE SHAPE: two instruments both claiming to answer 'is this declared', built on different mechanisms (a Terraform-source parser vs. a live-graph-to-declared cross-reference), can and did disagree about one concrete member while a downstream consumer (IAM-s-5, then this cell) was instructed to treat the drift plane's classification as the settled set. A name-level check against the OTHER instrument is what caught it, not a wider read of either instrument alone. Remedy (reconciling why the DECLARED-vs-LIVE cross-reference misses a role that IS in Terraform source) is a tooling fix outside this cell's <paths> and outside a worker's lane; named to 1.0.0_SA_CTO~Z as the seat this fabric's L10 always routes tooling/spec-plane defects through.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Three of the 16 undeclared roles (ecsTaskExecutionRole, rds-monitoring-role, vpc-flow-logs-role) carry the exact conventional names AWS's own console/service quick-create flows assign, but this worker has no CloudTrail or console-history access to confirm the origin and no authority to sign a formal exemption -- dispositioned exempt with owner=UNASSIGNED per the bound's own instruction, and the decision (confirm origin, name a real owner) is owed and unmade.",
    "evidence": [
      "GOVERNANCE_DISPOSITION.md (this folder) items 4, 12 and 15: all three names absent from this cell's fresh `.tools/comp-iam roles` parse (2026-09-10T08:48:35Z, 191 roles) and from every first-party Terraform file this cell searched via `.tools/comp-find '<name>' infra/ --all` -- only world-model census/inventory JSON mentions any of the three, never a `resource \"aws_iam_role\"` block.",
      "IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes name these three as 'AWS SERVICE-DEFAULT roles, the kind a console action or managed service mints on its own' -- a plausibility this cell re-checked by name rather than inheriting, and did not find contradicted, but also could not confirm (no CloudTrail CreateRole event access from this worker's tooling).",
      "The task order's own bound, quoted exactly: 'AN EXEMPTION IS A DECISION SOMEONE MAKES, NOT ONE YOU MINT ... Where a member plainly needs an owner you cannot name, record the disposition as EXEMPT with owner=UNASSIGNED and a reason stating what decision is owed and by whom, AND FILE A SURPRISE ROW naming it.'"
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): Grouped as one row for three members sharing the same class and the same remedy shape (confirm origin, then name an owner), rather than filing three near-identical rows for the same unresolved decision. Disarm: 2.0.0_SA_COO~ZI can route this to whichever seat holds cloud-IAM-governance sign-off authority, or accept the exempt/UNASSIGNED disposition as this round's answer and carry the open decision forward explicitly rather than let it read as closed.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two of the 16 undeclared roles (portal-auth-lambda-role, opal-data-refresh-lambda-role) sit on the production serving path -- portal-auth-lambda-role has zero Terraform touch and a distinctly-named declared sibling (opalinvest-auth-lambda-role) in the same module; opal-data-refresh-lambda-role backs a live Lambda by literal role_arn and is called 'pre-existing' in Terraform's own comment -- and this worker cannot make the heavier exemption call IAM-s-5's character note flags, so both are dispositioned exempt with owner=UNASSIGNED.",
    "evidence": [
      "infra/aws/terraform/portal-auth/iam.tf:16 @52c82c7537: `resource \"aws_iam_role\" \"auth_handler\"` declares `name = \"opalinvest-auth-lambda-role\"` -- a distinctly-named sibling in the same module as the undeclared `portal-auth-lambda-role`, confirmed NOT the same object; `portal-auth-lambda-role` itself has zero SURFACED/DEF hits anywhere in Terraform via `.tools/comp-find 'portal-auth-lambda-role' infra/ --all`.",
      "infra/aws/terraform/data-refresh/main.tf:38 @52c82c7537: `role_arn = \"arn:aws:iam::313476888478:role/opal-data-refresh-lambda-role\"` on the `data_refresh_api` Lambda module; main.tf:53 comment: 'SSCN S3 access -- inline policy attached to the pre-existing opal-data-refresh-lambda-role' -- Terraform attaches policies to this role by literal name but never creates it as a resource.",
      "GOVERNANCE_DISPOSITION.md (this folder) items 8 and 10 carry the full per-role citations and the reasoning; IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes: 'portal-auth-lambda-role, opal-data-refresh-lambda-role -- attached to functions on the production serving path.'",
      "The task order's own text: 'portal-auth-lambda-role and opal-data-refresh-lambda-role are PRODUCTION SURFACES ON THE SERVING PATH. An exemption here is a much heavier claim' -- naming the stakes without naming who bears them."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): Grouped as one row for the two members IAM-s-5's own character note singled out as the heavier class, distinct from the three service-default candidates (S3) and from the residue case (S5). Disarm: 2.0.0_SA_COO~ZI, given the production-serving-path stakes named in the task order itself; CLAUDE.md's own convention for served-output changes (never-widen sign-off, CTO+COO) suggests this decision likely needs more than one seat's word before either adoption or exemption is final, which this row states rather than resolves.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W3-S5",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "lambda-test-role reads as test/scratch residue rather than a serving role, which is a different remedy shape than either template this cell otherwise uses (add-to-Terraform, or except-with-reason) -- the real question is whether it is still exercised at all and should be retired, which neither IAM-s-5 nor this cell has usage-telemetry access or the mandate to answer, so it is dispositioned exempt with owner=UNASSIGNED naming that decision.",
    "evidence": [
      "`lambda-test-role` is absent from this cell's fresh `.tools/comp-iam roles` parse (2026-09-10T08:48:35Z) and from every first-party Terraform file searched via `.tools/comp-find 'lambda-test-role' infra/ --all` -- only world-model census/inventory JSON mentions it, with nothing describing its purpose or last use.",
      "IAM-s-5's DECLARED_VS_LIVE.md @52c82c7537 character notes: 'lambda-test-role -- name suggests a test/scratch role rather than a serving-path role', and this TO's own cell text: 'lambda-test-role READS AS RESIDUE.'",
      "This cell's bound: 'DO NOT MODIFY ANY TERRAFORM AND DO NOT CREATE, DELETE OR EDIT ANY ROLE' -- retirement (deletion) is explicitly out of this cell's remedy even if it is the more likely correct answer for residue, so the binary IN-CODE/EXEMPT template does not fit this member cleanly and the gap between 'add to code' and 'the right answer might be delete it' is itself the finding."
    ],
    "remedy": "CARRIED FROM THE ROW'S OWN NOTES (this slug invents no remedy the round did not state): Filed separately from S3 and S4 because the remedy shape differs: those two classes end in 'adopt or except', this one may end in 'neither -- delete', a third outcome this cell's binary schema cannot express and does not attempt to. Disarm: 2.0.0_SA_COO~ZI, who can route a usage check to whichever seat has invocation-log or CloudTrail access, or accept the exempt/UNASSIGNED disposition as final for this round while naming the open question explicitly.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  }
]
```
