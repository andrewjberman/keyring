# NFRA_IAMROLES202609 -- surprise channel, REMEDIATION v2 (site Z) -- THE ROUND-2 SLUG

**Home:** the project tree's channel (`org/ref/SURPRISE_CHANNEL_PROTOCOL.md` s.5). **Lane:** the CVO only.
**Cut by:** `3.0.0_SA_CVO~Z`, round 2, 2026-09-10 ~15:5xZ. **Reader:** `1.0.0_SA_CTO~Z`, and no one else.

**L10 PRECONDITION, BOTH LIMBS, SOURCE = THE INDEX** (`_latest_dispositions` imported and called):

```
28 items | OPEN 0 | GRADUATED 25 | DISMISSED_WITH_REASON 3
task orders  6 of 6 TERMINAL, read from their own <status> fields
instances    6 files / 6 distinct to_ids -- NO DUPLICATES this round (round 1 had 11 files for 9 orders)
criteria     31 -- 25 PASS, 6 UNVERIFIABLE-BY-INSTRUMENT, 0 FAIL
JUDGMENT     6 of 6 graded at C-S12, ALL PASS. Found on the `judgment` FIELD; the verbatim-text
             carrier returned ZERO here (the text reads "AC5 (JUDGMENT -- ..."), the exact
             opposite of NFRA_OPSEC202609 where the field returned zero. BOTH KEYS, ALWAYS.
```

⛔ **THIS SLUG CLOSES THE JOIN THIS SEAT HAS RAISED FOR FOUR ROUNDS.** Ten GRADUATED items carried NO
remediation row -- the defect that "LOSES SECURITY FINDINGS SILENTLY" -- and this document is the join.
Measured before the cut: 25 graduated, 15 already in the remediation plane, **10 with no row**. All ten
are here.

**TWO DISARMS ARE RECORDED, NOT DECLARED.** `Z-S10` was discharged by `1.0.0_SA_CTO~Z` @709b9556a3 and
`Z-S11` by this seat's own grading act at C-S12. The investigation plane DECLARES a disarm; the
remediation plane RECORDS it, and until this document existed neither had a carrier. **The other eight
carry their hazard exactly as surfaced -- four ARMED with live owners, four INERT.**

⛔ **SLUG-READY, NOT CLOSE-READY.** Rule 27's close needs `COMPLETION_REPORT` + `COMPLETION_GRADES` with
EVERY grade REALIZED. `COMPLETION_REPORT.round2.json` exists (10,353 bytes at HEAD); **`COMPLETION_GRADES`
is `1.0.0_SA_CTO~Z`'s and is not written.** The round-2 report partitions 2 COVERED / 6
UNCOVERED-BY-THIS-ROUND **by design** -- round 2's decomposition held cells for FWD-1 and FWD-4 only, and
each UNCOVERED row names round 1's report as its carrier. That is not a gap; it is an honest partition.

**THE ROUND'S RESULT, so the reader has it in one place:** the settled set of 16 is **exactly 15**, and the
one uncertainty IAM-r-3 could not close -- its clean worktree cannot see the shared checkout's untracked
`.tf` files -- was closed at C-S11 from the main tree (all four untracked `aws_iam_role` blocks mint NEW
roles; none is a member). Adoption is proved non-destructive: `Plan: 2 to import, 0 to add, 2 to change,
0 to destroy`, against a baseline plan that read `No changes` first.

**AUDITED GATE OVERRIDE, fifth slug running, same structural reason:** `_coordinate_violations` refuses a
NEW row carrying `W<n>` from a non-worker committer, while protocol s.5 requires the remediation id to
EQUAL the graduated id. Six of these ten rows are worker-surfaced (`Z-W5-*`, `Z-W6-*`). **A SLUG
STRUCTURALLY CANNOT CARRY A WORKER-SURFACED ROW WITHOUT AN OVERRIDE, AND IT RECURS EVERY ROUND A WORKER
FILES ONE.**

---

```json
[
  {
    "id": "NFRA_IAMROLES202609-Z-S10",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "proof-of-spec-check RESOLVES ARTIFACT PATHS AGAINST THE TREE THE SCRIPT LIVES IN, NOT THE TREE IT IS RUN FROM. A COO draining a spine-v3 worker with the MAIN tree's copy reads the worker's worktree-only deliverable as a dead path and marks a VALID instance INVALID. Every v3 worker is in a linked worktree by construction, so this sits on the default drain path, not on an edge case.",
    "evidence": [
      "MEASURED BOTH WAYS ON THE SAME INSTANCE AT THE SAME COMMIT, one variable apart. Main tree's copy on IAM-r-3's instance: violations=1, INVALID (rc=1), naming MEMBERSHIP_PER_MEMBER.md as PENDING-THIS-COMMIT but absent from the working tree and from the instance's commit. The worktree's OWN copy on the SAME file: violations=0, VALID (rc=0), artifact-resolution reading 1 PENDING co-committed (POST-COMMIT: touched by the instance commit b077f10538).",
      "THE VIOLATION IS FALSE, established independently of the checker. git ls-tree --name-only b077f10538 over the deliverables directory LISTS MEMBERSHIP_PER_MEMBER.md, and test -f in the worktree returns true. The artifact both exists on disk and rides the instance's own commit.",
      "SOURCE, READ AT HEAD. .tools/proof-of-spec-check.py:193 sets _REPO_ROOT = Path(__file__).resolve().parent.parent -- the SCRIPT's own location, never the caller's. It is used for the presence test at :327 and to read bytes for the content rung at :363.",
      "CONTROL, INSTRUMENT ALIVE IN BOTH INVOCATIONS: adding a nonexistent criterion id to the coverage list produced the silent-omission violation naming AC99_BOGUS from BOTH copies. The checker was functioning in both; the difference is confined to artifact resolution.",
      "CONTROL, THE MAIN COPY IS NOT SIMPLY BROKEN: the main tree's copy graded IAM-r-4's instance -- which lives in the main tree -- VALID, violations=0, rc=0. The failure is specific to a cross-tree pairing.",
      "NOT EXERCISED, DERIVED FROM SOURCE ONLY, AND FLAGGED AS SUCH: the inverse direction reads as a FALSE PASS rather than a false refusal. Because :327 accepts presence in _REPO_ROOT alone, a file sitting at the SAME PATH in the main tree would satisfy the COX presence test for a commit that does not carry it, and :363 would then feed the content rung the MAIN TREE's bytes. This lane did not construct that case and does not assert it; it is named because it is the direction that fails quietly."
    ],
    "remedy": "DISCHARGED BY 1.0.0_SA_CTO~Z @709b9556a3, and RECORDED HERE because the remediation plane is the only carrier for a disarm. `proof-of-spec-check.py` now REFUSES LOUD with CHECKER-SCOPE on a foreign tree instead of emitting a violation that named the WORKER'S artifact, and its text states in terms that it is not a finding against the instance or its author. The REFUSING form was chosen over re-deriving the root, which is what the row itself preferred and what C-S7 endorsed: refusing cannot produce a wrong verdict in EITHER direction, so it also closes the quiet FALSE-VALID case the row named from source and never constructed. Exercised both arms; tool self-test 12 of 12.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": "2026-09-10T14:38Z"
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S11",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TWO OF IAM-r-6's FOUR MECHANICAL BARS CANNOT FAIL, AND ONE CARRIES A FALSE MEASUREMENT THIS LANE WROTE. AC1's expect says measured 0 at the cut; at the issuance commit the document read 0 under a case-SENSITIVE grep and 3 under the criterion AS SHIPPED, which carries -i. AC3 read 3 at the cut against an expect of 1 or greater and never discriminated at all.",
    "evidence": [
      "MEASURED AT THE CUT VINTAGE, one flag apart, on the same file. At the round-2 issuance commit cccb4fac83, GOVERNANCE_DISPOSITION.md reads 0 under grep -c -E RETIRE and 3 under grep -c -i -E RETIRE. The criterion as shipped carries -i. The measuring instrument and the shipped instrument differed by exactly that flag.",
      "WHY THE FLAG DECIDES IT: the three matching tokens are all lowercase -- retired at :106, retirement at :291, retire at :349. There is no uppercase RETIRE anywhere in the document, which is why a case-sensitive read returns a clean 0.",
      "NO ROUND-2 CELL MOVED IT, so this is not a bar invalidated by its own round. The case-insensitive read is 3 at ALL FIVE vintages measured: cccb4fac83 (the cut), ffcc39967a (round-1 state), 1b65eb60d9 (post IAM-r-1), b1fececea1 (post IAM-r-4) and HEAD. It was already 3 before round 2 began.",
      "AC3 HAS NO CASE STORY AND NO CUT NOTE: grep -c -E lambda-test-role reads 3 at the cut and 4 at HEAD against an expect of 1 or greater. lambda-test-role has been row 7 of the disposition since round 1. A worker that did nothing would pass it.",
      "CONTRAST THAT ISOLATES THE DEFECT TO ONE ORDER: IAM-r-4's four cut notes were re-measured against the SAME cut vintage and all four are ACCURATE -- 0, 0, 0, 0, exactly as its expect fields state. The issuance's blanket claim that every criterion was measured is not uniformly false; two criteria in one order are.",
      "THE OTHER TWO r-6 BARS ARE SOUND and are named so this row does not overstate: AC2 reads 0 at the cut AND 0 at HEAD, so it genuinely discriminates; AC4 is an explicit regression bar correctly reading 0 throughout."
    ],
    "remedy": "DISCHARGED BY THIS SEAT AT C-S12, which is the act the row named when it set 3.0.0_SA_CVO~Z as its disarm owner. IAM-r-6's AC1 and AC3 were NOT CREDITED at L9 -- neither appears among the six grades and neither contributed to IAM-r-6's AC5 PASS -- and the substance was graded from the instrument Z-W5-S1 supplied (the case-SENSITIVE whole-word census, 0 at the parent commit against a nonzero at the cell's HEAD) plus AC2 and AC4, which discriminate. NOT CREDITED IS NOT GRADED FAIL: a criterion that cannot discriminate produces no evidence in either direction.",
    "owner": "3.0.0_SA_CVO~Z",
    "round": "v2",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "3.0.0_SA_CVO~Z",
      "round": "v2"
    },
    "closed": true,
    "disarm": {
      "state": "DISARMED",
      "owner": "3.0.0_SA_CVO~Z",
      "at": "2026-09-10T15:40Z"
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S8",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "TERRAFORM MANAGES POLICIES ON A ROLE IT DOES NOT OWN, on a production serving path: infra/aws/terraform/data-refresh/main.tf carries ZERO aws_iam_role blocks and FOUR aws_iam_role_policy blocks attaching inline policies to opal-data-refresh-lambda-role BY NAME STRING, plus hardcoded role ARNs. And the general form: A NAME MATCH IN TERRAFORM IS NOT A DECLARATION -- that role returns 9 hits and is undeclared, so any membership check keyed on the name would misclassify it.",
    "evidence": [
      "MEASURED on Terraform source: `.tools/comp-find 'opal-data-refresh-lambda-role' infra/aws/terraform` returns 9 hit(s) across 569 files. Every one is a REFERENCE -- role_arn = \"arn:aws:iam::...:role/opal-data-refresh-lambda-role\" at main.tf:38,124 and qa-scratch-instance.tf:19, and role = \"opal-data-refresh-lambda-role\" at main.tf:60,82,101,140 and qa-scratch-instance.tf:38.",
      "THE FILE SAYS IT IN ITS OWN COMMENT, main.tf:53: 'SSCN S3 access -- inline policy attached to the pre-existing opal-data-refresh-lambda-role.' The word is pre-existing.",
      "STRUCTURAL CONFIRMATION rather than a reading of the comment: data-refresh/main.tf contains 0 `resource \"aws_iam_role\"` blocks and 4 `resource \"aws_iam_role_policy\"` blocks (data_refresh_sscn_s3, data_refresh_cloudfront_read, data_refresh_time_machine_invoke, portal_time_machine_invoke_downstream).",
      "POSITIVE CONTROL, so the probe is shown to find a declaration when one exists: seeking-alpha-scraper-role's hit sits INSIDE `resource \"aws_iam_role\" \"seeking_alpha_role\" { name = \"seeking-alpha-scraper-role\" ... }` at infra/aws/terraform/seeking-alpha/main.tf:240-241, and that file carries 1 aws_iam_role block. NEGATIVE CONTROL: portal-auth-lambda-role returns 0 hits in the same scope.",
      "SO THE TWO ROLES THE ROUND-1 ANALYSIS GROUPS AS 'production serving-path, not in code' ARE IN DIFFERENT STATES: one is absent outright, the other is policy-attached-but-undeclared."
    ],
    "remedy": "FOUND WHILE MEASURING CRITERIA BASELINES FOR THE ROUND-2 CUT, before the issuance, which is why it changes the cut rather than being carried past it. TWO CELLS MOVED ON IT: IAM-r-3's discriminator is now a RESOURCE BLOCK and never a name match, with the confirmed false positive as its positive control and this role as its negative control -- a discriminator that cannot separate those two is not one. IAM-r-5 is re-framed as an ADOPTION and its destroy bound stops being theoretical: four live policy attachments hang off this role by name, so a plan that destroyed or replaced it would orphan them on a production serving path, which is the outage C-NO-ACCESSDENIED forbids this project from causing. IAM-r-6's uncovered-member hunt must now consider this state explicitly. NOT CLAIMED: that the other fourteen members are correctly classed -- this cut measured two roles because two cells depend on them, and IAM-r-3 measures all of them. disarm_owner is 1.0.0_SA_CTO~Z as the architecture owner; whether a role Terraform policies but does not declare is acceptable, and whether the vocabulary needs a value for it, is a ruling and not a worker's call. THE REUSABLE SHAPE: A REFERENCE IS NOT A DECLARATION, and a census keyed on an identifier's PRESENCE cannot tell the two apart -- it will read a heavily-referenced absent thing as present, which is the opposite error from the false positive this round already found, on the same question.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-S9",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Z-W6-S1 is CORRECT and its cause is mine: the round-2 battery's '195 TF roles' was measured from the SHARED MAIN CHECKOUT, which carries five untracked .tf files holding exactly FOUR aws_iam_role blocks. 195 - 4 = 191, the committed figure. A BATTERY DENOMINATOR TAKEN FROM A SHARED WORKING TREE INCLUDES WHATEVER UNCOMMITTED WORK OTHER SEATS HAVE LEFT IN IT.",
    "evidence": [
      "THE ARITHMETIC CLOSES EXACTLY. git status --porcelain over infra/aws/terraform lists FIVE untracked files: globgrph/freshguard_derive_watchdog.tf (0 role blocks), globgrph/freshness_alarm.tf (1), globgrph/item2d_freeze_monitor.tf (1), globgrph/tool_activity_freshness.tf (1), inf-pipeline/inf-gold-freshness-guard.tf (1). TOTAL 4. The issuer's battery read 195; the worker's clean-tree read is 191; 195 minus 4 is 191.",
      "REPRODUCED ON BOTH SIDES rather than inferred from one. This lane ran comp-iam stats TWICE from the main tree (195, 195) and ONCE from the worker's own worktree via the bare name (195, because the bare name resolves through a ~/bin forwarder to the main checkout). The worker ran the explicit .tools/ path from its worktree, twice, and got 191 both times.",
      "THE TRACKED TREES ARE IDENTICAL: git diff --stat HEAD against the worker branch over infra/aws/terraform is empty. So the four-role gap cannot be a committed difference, which is what isolates it to untracked content.",
      "EVERY OTHER SUB-FIGURE MATCHES EXACTLY -- 188 services, 1084 operations, 304 gaps -- on both readings. The discrepancy is confined to the role count, which is the only figure the four untracked declarations could move. That specificity is corroboration, not coincidence.",
      "THE UNTRACKED FILES ARE NOT THIS LANE'S. They were present in the shared checkout at session start and belong to other seats' in-flight infrastructure work."
    ],
    "remedy": "THE WORKER WAS RIGHT AND ITS ROW STANDS; this row supplies the cause rather than disputing it. It also did the harder half correctly: it did NOT force 191 into an arithmetic reconciliation with the live plane's DECLARED sub-counts, and it separated 208/216/219 as ONE INSTRUMENT FAMILY AT THREE VINTAGES from 191 as a STRUCTURALLY DIFFERENT POPULATION. THE DEFECT IS THIS LANE'S, IN TWO PLACES THAT ARE NOW FROZEN: the round-2 decomposition's section 2b battery block and the three round-2 task orders that inline it. They are not retro-amended, for the same reason round 1's terminal orders were not. This row is the carrier and 191 is the committed figure. ROUND 1'S BATTERY CARRIES THE SAME EXPOSURE and is not re-measured here. THE REUSABLE SHAPE, and it is why disarm_owner is the CTO rather than this lane: A BATTERY IS A MEASUREMENT OF A TREE, AND ON A SHARED CHECKOUT THE TREE IS NOT A VERSION. Every L5 battery on this device has this exposure, no gate refuses it, and the cheap remedy is to take battery denominators from a clean worktree or to state the tree's dirty state beside the figure. That is a spine or tooling call, not a project one. SECOND FINDING, THIS ONE ABOUT MY OWN TOOLING AND CAUGHT BY THE ROW GATE: the first attempt to append this row produced a MALFORMED json block, because the append script passed the rebuilt block to re.sub as a REPLACEMENT STRING and re.sub interprets backslashes there. The worker's row is the first in this channel to contain one. Nine earlier merges used the same script safely only because no row had ever carried a backslash. Fixed by using a replacement FUNCTION; the gate refused the malformed write and nothing landed.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~Z",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W5-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "IAM-r-6's AC1 asserts the retirement token measured 0 in GOVERNANCE_DISPOSITION.md at the cut; this worker's pre-edit baseline of the criterion's own verbatim invocation measured 3. The pattern is case-INSENSITIVE and unanchored, and the document already carried lowercase retire/retired/retirement in prose -- so the criterion was already satisfied by text written by an earlier cell, and it cannot distinguish a real vocabulary extension from no edit at all.",
    "evidence": [
      "THE CRITERION'S OWN INVOCATION, RUN VERBATIM BEFORE ANY EDIT, at worktree /c/tmp/wk-iamroles-5 @772c796a3f on branch wk-NFRA_IAMROLES202609-5: `timeout 120 grep -c -i -E 'RETIRE' org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~3/GOVERNANCE_DISPOSITION.md` printed 3 (rc=0). The TO's expect clause reads 'a count of 1 or greater -- ... measured 0 at the cut, so only a real extension moves it'.",
      "THE THREE HITS ARE NAMED AND THEY ARE ALL EARLIER CELLS' PROSE, none a disposition token: line 106 'whether it should be retired' (IAM-s-6's row 7 reason), line 291 'needing a retirement-or-formalize decision' (IAM-s-6's WHY ONE DISPOSITION section), line 349 'retire vs. formalize' (IAM-s-6's surprise-row summary). Cited at GOVERNANCE_DISPOSITION.md@b1fececea1, the file's state when this cell opened it.",
      "THE DISCRIMINATING MEASUREMENT EXISTS AND DISAGREES WITH THE CRITERION: a word-boundary, case-SENSITIVE per-token census over the same 350-line file reads RETIRE 0, RETIRED 0, RETIREMENT 0 before this cell's edit, against DECLARED 23, ADOPT 24, EXEMPT 10. That census is what the TO's rule-24 clause actually asks for, and it is the number this cell moved.",
      "NEGATIVE CONTROL ON THE READING, so this is not a claim about grep in general: the sibling criterion AC2 ('uncovered member|policy-attached|manages policies on a role', same -i, same file) measured 0 at the same pre-edit baseline and therefore does discriminate. The defect is specific to AC1's pattern meeting a word the document already used in prose, not to the cut's instrument."
    ],
    "remedy": "NOT BLOCKING AND NOTHING WAS WITHHELD: the cell did the substantive work regardless -- the fourth value is defined, the four-postulate record and the token census are written, and the member is disposed -- and AC1 now reads 33. THE EXPOSURE THIS ROW CARRIES IS THE READING, not the number: a grader who reads AC1's PASS as evidence of the extension is reading an output that predates the cell. The disarming evidence is already in the artifact and in the proof-of-spec instance: the case-sensitive word-boundary census (0 before, nonzero after) is recorded in both, and this worker re-grounded the baseline before editing rather than inheriting the cut's cited 0. WHY THE DISARM OWNER IS THE ISSUER RATHER THAN THE ADJUDICATOR: for this cell the exposure is spent, so what remains is the reusable cutting pattern -- a criterion whose expect clause cites a baseline that its own invocation does not return -- and criteria are cut at L6. THE CHEAP REMEDY IS ONE HABIT, not a gate: run the criterion against the world before handing it over, which is what this worker's first act did and what surfaced this. SECOND INSTANCE THIS ROUND, same shape, different cell: IAM-r-1's proof instance records its AC2 baseline re-measuring 12 against a cited 13.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W5-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-2 cut's battery states that Terraform carries FOUR aws_iam_role_policy blocks attaching to opal-data-refresh-lambda-role by name; this worker's own re-measurement over the whole terraform tree found FIVE. The fifth sits in a second file (data-refresh/qa-scratch-instance.tf) that a main.tf-only read does not reach. The zero-aws_iam_role-blocks half of the cut's claim reproduced exactly.",
    "evidence": [
      "THE CUT'S CLAIM, VERBATIM, from this cell's own task order: 'Terraform carries ZERO aws_iam_role blocks for it and FOUR aws_iam_role_policy blocks attaching to it BY NAME' (NFRA_IAMROLES202609.TO-IAM-r-6.a-third-disposition-value-then-the-residue-call.md, BATTERY FINDINGS block).",
      "THE RE-MEASUREMENT, WITH ITS DENOMINATOR: `.tools/comp-find 'opal-data-refresh-lambda-role' infra/aws/terraform --all` -> '9 hit(s) across 516 file(s) scanned in scope'. FIVE of the nine are `role = \"opal-data-refresh-lambda-role\"` attachment lines: data-refresh/main.tf:60, :82, :101, :140 and data-refresh/qa-scratch-instance.tf:38.",
      "EACH OF THE FIVE WAS READ AT SOURCE rather than counted from the grep, so an attachment and a mention cannot read alike: resource \"aws_iam_role_policy\" \"data_refresh_sscn_s3\" (main.tf:59), \"data_refresh_cloudfront_read\" (main.tf:81), \"data_refresh_time_machine_invoke\" (main.tf:100), \"portal_time_machine_invoke_downstream\" (main.tf:139), \"data_refresh_qa_scratch_access\" (qa-scratch-instance.tf:36). All five are aws_iam_role_policy resources; all five carry the literal role name.",
      "THE OTHER HALF OF THE CUT'S CLAIM REPRODUCED EXACTLY: `.tools/comp-find 'resource \"aws_iam_role\"' infra/aws/terraform/data-refresh --all` -> '0 hit(s) across 4 file(s) scanned in scope'. The module genuinely manages policies on a role it does not declare, which is the state the cut was pointing at.",
      "FOUR IS WHAT A main.tf-ONLY READ RETURNS: the four hits at main.tf:60, :82, :101, :140 are exactly the cut's number, and the fifth lives in the sibling file qa-scratch-instance.tf. A THIRD NUMBER IS ALSO IN THE RECORD -- round 1's GOVERNANCE_DISPOSITION.md row 8 says 'three aws_iam_role_policy attachments' -- so the same state has been counted 3, 4 and 5 by three different cells."
    ],
    "remedy": "NOTHING MOVES ON THIS AND NO DISPOSITION DEPENDS ON IT, which is why hazard_standing is INERT: the uncovered-member decision this cell owes turns on WHETHER Terraform attaches policies to a role it does not declare, not on how many times it does. That half reproduced exactly (zero declarations over a measured 4-file denominator), and the decision -- no fourth value for the policy-attached state -- rests on a different measurement entirely (five of the six roles carrying literal-name attachments in this tree ARE declared, so the state is not mutually exclusive with the values already on the axis). THE REUSABLE SHAPE, offered without a remedy because this worker cannot see which read produced the cut's four: a per-member count taken from the file where the member obviously lives is not a tree-wide count, and the two render identically in a battery block. The round-2 decomposition and the task orders that inline it are frozen mid-round and are not retro-amended; this row is the carrier and the whole-tree figure is five.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W6-S1",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The L5 decomposition's own round-2 battery citation of '195 TF roles' from comp-iam (also independently repeated by row Z-S1) does NOT reproduce -- a fresh re-run of the identical instrument against the identical committed Terraform tree returns 191, twice, matching round 1's figure instead.",
    "evidence": [
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/decompositions/NFRA_IAMROLES202609_DECOMP_R2.md@5b460996ee section 2b: 'comp-iam -- RUN. 195 TF roles / 188 services / 1084 operations / 304 gaps'.",
      "This project's own row NFRA_IAMROLES202609-Z-S1 (surfaced 2026-09-10T05:39Z by 2.0.0_SA_COO~ZI) independently repeats the same reading: 'A THIRD figure exists on the DECLARED plane and is NOT part of this finding: comp-iam stats parses 195 IAM roles from Terraform.'",
      "MEASURED by this worker: `.tools/comp-iam stats` and `.tools/comp-iam roles`, run twice back-to-back at this worktree's HEAD cccb4fac8351dbcdf547382b0c733f20ffc62667 (branch wk-NFRA_IAMROLES202609-6, cut from SITEZ HEAD), both times print 'IAM roles parsed: 191' / 'IAM ROLES (191 found)' with 191 tf_resource lines -- while Services scanned (188), Total operations (1084) and Permission gaps (304) match the decomposition's '195' citation exactly.",
      "MEASURED: `git log --since=2026-09-10T05:00:00Z --until=2026-09-10T13:30:00Z -- infra/aws/terraform/` returns 0 commits -- the committed Terraform tree did not move across the span from Z-S1's own vintage (05:39Z) through the decomposition's commit (5b460996ee, 2026-09-10T12:45:53Z) to this worker's HEAD (12:58:12Z).",
      "MEASURED: `git log -- org/modules/graph/extract_iam.py` shows no commit since 2026-07-25T09:35:44-04:00 -- the role-counting logic itself has not changed today.",
      "MEASURED: `git status --short -- infra/aws/terraform/` in this worktree is clean (no output); `git ls-files infra/aws/terraform/ | grep -c '\\.tf$'` = 415."
    ],
    "remedy": "NOT A HALT: this cell's own deliverable (org/missions/D12/NFRA/NFRA_IAMROLES202609/deliverables/0.9.0_WK_NFRA_IAMROLES202609~6/DENOMINATOR_RECONCILIATION.md) already carries this finding in full and treats 191 as `measured` (this worker's own reproducible run) and 195 as `held` with this worker's reproduction attempt recorded as FAILED, rather than citing 195 further. Filed because the decomposition itself (a committed L5 artifact other cells and a later L9 grader read) still states 195 as a plain battery result with no caveat, and this worker cannot edit the decomposition (a READ-only surface on this cell's <paths>) to add one. Disarm routed to 2.0.0_SA_COO~ZI as the decomposition's author and the only lane that can amend it; the fix is either a correction note on the battery section or a re-run transcript that actually reproduces 195 -- this worker could not find one.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v2"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~ZI",
      "at": null
    }
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W6-S2",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IAM-r-5's DOUBLE-STOP states as fact that BOTH roles 'EXIST AND SERVE PRODUCTION TRAFFIC RIGHT NOW'. For portal-auth-lambda-role that is false on three independent instruments: zero Lambda consumers out of 203 live functions, RoleLastUsed EMPTY since creation on 2026-02-19, and zero LAMBDA callers in a 27,662-node served graph. The role exists and is reachable-by-nobody.",
    "evidence": [
      "MEASURED, LIVE AWS PLANE: `.tools/aws iam get-role --role-name portal-auth-lambda-role` returns \"RoleLastUsed\": {} -- an EMPTY object, not a stale date. The same call against opal-data-refresh-lambda-role returns \"LastUsedDate\": \"2026-09-04T20:43:51+00:00\", which is the positive control proving the field is populated when a role is actually used.",
      "MEASURED, LIVE AWS PLANE, WITH A PRINTED DENOMINATOR: `.tools/aws lambda list-functions --query 'Functions[?Role==`arn:aws:iam::313476888478:role/portal-auth-lambda-role`]'` returns `[]`. The denominator is `length(Functions)` = 203 functions scanned (CLI auto-paginated, no --no-paginate). POSITIVE CONTROL on the identical query form: the same expression against opal-data-refresh-lambda-role returns 3 (portal-time-machine, opal-data-refresh-api, opal-data-refresh-api-qa-scratch), so the zero is a true zero and not a broken filter.",
      "MEASURED, A DIFFERENT INSTRUMENT ON A DIFFERENT PLANE (this is corroboration, not repetition): `comp-blast 'arn:aws:iam::313476888478:role/portal-auth-lambda-role' --direction both --budget 120`, rc=0, served kuzu projection vintage 2026-09-10T12:24:50Z manifest aebbd9cef8c4, universe 27,662 nodes / 59,548 edges. It reports 423 callers of which ZERO carry the [LAMBDA] type -- the only [1]-depth caller is `service-principal::lambda.amazonaws.com`, i.e. the trust policy itself and nothing that assumes it. The same instrument on opal-data-refresh-lambda-role names three [LAMBDA] callers at depth 1.",
      "THE TRUST POLICY CLOSES THE REMAINING DOOR: the live AssumeRolePolicyDocument permits ONLY Service `lambda.amazonaws.com` to assume it, so a non-Lambda consumer (an API Gateway authorizer role, an EC2 profile, a human) is not merely unobserved but mechanically excluded. A zero over Lambda functions is therefore a zero over all possible principals.",
      "SCOPE OF THE CLAIM, STATED: this is a claim about CONSUMERS AND USE, not about existence. The role exists (RoleId AROAUR7FNW6PJKL2H5NDM, created 2026-02-19T16:00:39Z) and carries real permissions (AWSLambdaBasicExecutionRole attached, inline jwt-public-key-secret granting secretsmanager:GetSecretValue on arn:aws:secretsmanager:us-east-1:313476888478:secret:opal/auth/jwt-public-key*). Nothing here says it should be deleted.",
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-5.production-roles-declared-and-adoption-proved-safe.md@772c796a3f, DOUBLE-STOP paragraph: 'Both roles EXIST AND SERVE PRODUCTION TRAFFIC RIGHT NOW.'"
    ],
    "remedy": "NOT BLOCKING AND THE CELL WAS COMPLETED IN FULL ON BOTH ROLES. Filed in the direction that does NOT relax anything: the cell was executed as if the premise held for both, the adoption plan is non-destructive for both, and this worker adjusted no permission on either. The finding only ever makes the cell SAFER than its own framing, which is why hazard_standing is INERT and no disarm owner is named. WHY IT IS WORTH A ROW ANYWAY, and this is the reusable part: A SET ASSEMBLED BY A SHARED LABEL ('the two production serving-path roles') CAN HAVE MEMBERS THAT DO NOT SHARE THE PROPERTY THE LABEL ASSERTS, and every per-member check still passes because each member is individually fine -- the defect is in what the members were said to have IN COMMON. The label here came from the roles' NAMES and their membership in the undeclared set, not from a use measurement; nothing upstream of this cell had measured whether either role was actually used, because IAM-r-3's question was declaredness and not usage. TWO CONSEQUENCES FOR LATER READERS. First, for IAM-s-6 and the residue call: portal-auth-lambda-role is a candidate for a genuinely different disposition than a serving-path role, and this row is the measurement, not the recommendation. Second, C-TWO-REMEDIES is respected in terms -- this worker notes the usage state and explicitly does NOT recommend narrowing, deleting or otherwise moving the role, because that is the governance axis and not this cell's.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W6-S3",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "IAM-r-5's bound demands the plan output be QUOTED VERBATIM, and its own criterion AC5 forbids the string 'terraform apply' in the deliverable -- but Terraform's plan footer emits that exact string unprompted. A fully verbatim quote of raw plan stdout FAILS AC5 by construction; satisfying AC5 naively means truncating the evidence the bound demands.",
    "evidence": [
      "MEASURED: `terraform plan -input=false -no-color -lock=false` (Terraform v1.15.8, aws provider v5.100.0) writes a footer after the plan body, verbatim: 'Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run \"terraform apply\" now.' The forbidden token is produced by TERRAFORM, describing an action this worker did not take and this order does not authorise.",
      "MEASURED: the alternative footer is worse, not better. Using `-out=<file>` replaces the note with 'To perform exactly these actions, run the following command to apply:' followed by a literal `terraform apply` invocation line -- so both stdout forms of the plan command carry the token.",
      "THE COLLISION IS IN THE CRITERION'S OWN TEXT: AC5's invocation is `grep -c -i -E 'terraform apply|safe-apply|terraform import|put-role-policy|delete-role|APPLIED-TO-PRODUCTION'` with expectation 'a count of 0, printed'. Its stated intent is 'nothing was applied and no state was mutated'. The regex is a proxy for that intent and cannot distinguish a worker REPORTING an apply it performed from TERRAFORM'S OWN BOILERPLATE saying an apply was NOT performed -- the second is evidence FOR the criterion's intent and is scored as evidence against it.",
      "RESOLVED WITHOUT WEAKENING THE EVIDENCE, and the resolution is itself measured: the plan was saved with `-out` and rendered with `terraform show -no-color <planfile>`, which emits the plan body with NO footer. PROOF THAT THIS IS NOT A SUMMARY: `diff` of the region from 'Terraform used the selected providers' through the 'Plan:' line, taken from the show rendering against the same region of the raw plan stdout, is EMPTY -- byte-identical, 203 lines vs the raw form's 229. The 26-line difference is exactly the pre-plan refresh chatter and the post-plan boilerplate note, no plan content.",
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-5.production-roles-declared-and-adoption-proved-safe.md@772c796a3f, BOUNDS: 'THE PLAN IS THE DELIVERABLE'S EVIDENCE AND ITS OUTPUT IS QUOTED VERBATIM. A summary of a plan is not a plan.'"
    ],
    "remedy": "NO SURFACE WAS BLOCKED AND NOTHING WAS WITHHELD -- this is filed under 'had to do what the task order did not say'. The order names `terraform plan` as the instrument; the deliverable's quoted evidence is a `terraform show` rendering OF THE SAVED PLAN FROM THAT SAME RUN, with the diff-against-raw-stdout recorded above and restated in the deliverable so a grader can re-derive completeness rather than take this worker's word. Saving a plan file writes a LOCAL file only and mutates no state -- independently confirmed: the remote backend object s3://opal-313476888478-terraform-state/data-refresh/tfstate still reads LastModified 2026-08-03T17:40:49Z, 38 days before this session. THE REUSABLE SHAPE, and it is why this is worth a row rather than a footnote: A NEGATIVE KEYWORD CRITERION OVER A DELIVERABLE THAT IS REQUIRED TO CONTAIN QUOTED TOOL OUTPUT SCORES THE TOOL'S VOCABULARY, NOT THE WORKER'S CONDUCT. The criterion cannot see who authored the string. The cheap general remedy is to scope such a regex to the worker's own prose -- for instance by requiring quoted output to sit in a fenced block and excluding fenced blocks from the sweep -- or to assert the negative on the WORLD (the state object's LastModified, which is what actually discriminates) instead of on the document's characters. That is a standards call for the proof-of-spec schema, not a project one, so no disarm owner is named.",
    "owner": "1.0.0_SA_CTO~Z",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~Z",
      "round": "v2"
    },
    "closed": false
  },
  {
    "id": "NFRA_IAMROLES202609-Z-W6-S4",
    "project": "NFRA_IAMROLES202609",
    "fabric": "site-z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The only Terraform module IAM-r-5 grants this worker write access to is infra/aws/terraform/data-refresh/, but portal-auth-lambda-role has nothing to do with data-refresh -- so the one place the proposed declaration may be written is a module whose state file, provider tags and system identity all belong to a different system.",
    "evidence": [
      "org/missions/D12/NFRA/NFRA_IAMROLES202609/task-orders/NFRA_IAMROLES202609.TO-IAM-r-5.production-roles-declared-and-adoption-proved-safe.md@772c796a3f, PATHS: 'infra/aws/terraform/ is granted for READING; infra/aws/terraform/data-refresh/ is the one module you may write a proposed declaration into.'",
      "MEASURED: the two roles have DISJOINT consumer sets. opal-data-refresh-lambda-role is used by exactly the three Lambdas the data-refresh module declares (opal-data-refresh-api, portal-time-machine, opal-data-refresh-api-qa-scratch). portal-auth-lambda-role is used by none of them -- by none of the 203 live functions at all (row Z-W6-S2). There is no resource in this module that touches the second role.",
      "MEASURED: the module's backend is a SEPARATE state object -- infra/aws/terraform/data-refresh/main.tf@772c796a3f lines 16-20, `bucket = \"opal-313476888478-terraform-state\"`, `key = \"data-refresh/tfstate\"`. Adopting portal-auth-lambda-role here files a portal-auth object permanently under the data-refresh key, where nobody looking for it would look.",
      "MEASURED AND VISIBLE IN THE PLAN OUTPUT: the module's provider block (main.tf:23-32) sets default_tags Project=OpalPortal, ManagedBy=Terraform, Environment=Production. The plan run for this cell shows both roles taking `~ tags_all` with those three tags added -- so custody in THIS module is not tag-neutral, and the data-refresh module's tags would be stamped onto a portal-auth role.",
      "THE PROPOSED TEXT IS INERT SO NOTHING IS COMMITTED TO BY THIS: it lands as infra/aws/terraform/data-refresh/zz_adoption_candidate.tf.proposed, a non-.tf extension Terraform does not load, exactly as the cell requires."
    ],
    "remedy": "NOT BLOCKING AND NO PATH IS BEING REQUESTED -- the cell's write surface was adequate for the cell's own bar and this worker did not need a path it lacked. Filed because the PROOF has a scope limit that the deliverable alone would not make obvious to a reader who sees a clean plan: the plan proves ADOPTION MECHANICS ARE NON-DESTRUCTIVE (the provider imports an existing role without recreating it, and omitting inline_policy / managed_policy_arns leaves live attachments untouched), and that conclusion transfers to any module. What does NOT transfer is the tags_all delta and the state key, both of which are module-scoped. For opal-data-refresh-lambda-role the module IS the right home and the plan transfers whole -- 4 of its 5 live inline policies are already declared in this module's main.tf and the 5th in qa-scratch-instance.tf, so the role's custody belongs beside them. For portal-auth-lambda-role the placement is an open call for whoever holds the portal auth surface, and this worker records it rather than deciding it.",
    "owner": "2.0.0_SA_COO~ZI",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~ZI",
      "round": "v2"
    },
    "closed": false
  }
]
```
