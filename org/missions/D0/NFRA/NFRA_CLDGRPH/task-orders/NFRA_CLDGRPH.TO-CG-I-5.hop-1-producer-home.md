# TO NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home -- CG-s-45 (ADDED at decomposition v0.12): HOP 1's COMMITTED PRODUCER HAS NO PRODUCTION HOME -- the route that built every served zip in round 6 is still a script in a worker's deliverable folder

<to_id>NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~4</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>complete -- FLIPPED 2026-09-10T18:5xZ by `0.9.0_WK_NFRA_CLDGRPH~4` on branch `wk-cldgrph-9-4` (LOCAL, never pushed). Instance `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home.proof_of_spec.json` VALID rc=0, 0 violations, `python .tools/proof-of-spec-check.py <instance> I5-AC1,I5-AC2,I5-AC3,I5-AC4,I5-AC5`. FOUR mechanical rows PASS by output: `I5-AC1` WORKFLOW_EVER_RAN=YES / ZIPS_ATTRIBUTED=5 of 5 / BLIND_REPORTED=2; `I5-AC2` HOME_DECIDED=WORKFLOW / PIN_DISPOSITION=RESOLVES; `I5-AC3` BRANCH=FILED with 3 owned items, HALF_MOVED=false over 31,838 files; `I5-AC4` ZIP_PUSHES=0 WORKFLOW_TRIGGERS=0 S3_WRITES=0 TERRAFORM_APPLIES=0 CODEBUILD_STARTS=0 EGRESS_PROBE_CONTROL=FIRED 5 of 5. `I5-AC5` UNVERIFIABLE-BY-INSTRUMENT, no verdict taken, graded by `3.0.0_SA_CVO` at L9. THE CELL'S PREMISE IS FALSIFIED AND THE FINDING IS LARGER: the committed route is not unrun -- 855 runs, 8 successes all predating the step that packs portal/src, 847 runs and 0 successes since, and 0 correct publishes EVER. Acts @`a658d981cd`. ONE ROW: `NFRA_CLDGRPH-W4-S10`, OBSERVATION, ARMED, disarm_owner `0.0.0_AB_MSTR`.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~4; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~4 <0.9.0_WK_NFRA_CLDGRPH~4@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool and NEVER with a shell `printf` or heredoc (rule 14a: a shell-built message file re-opens the injection one step earlier -- your issuer broke this once today and caught it before committing). Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/`.** Every script and capture carries `i5_`. Scratch `.scratch/`.
- ⛔ **THE TREE CLAUSE. Your issuer got this wrong last round and the correction is the lesson.** The comp-rail once resolved its corpus from the TOOL'S INSTALL LOCATION, so a census run from a linked worktree scanned the MAIN TREE and returned a well-formed zero with a real denominator. **THE FIX IS PRESENT IN YOUR WORKTREE** -- measured BY CONTENT at this cut, in your own checkout: `.tools/_comprail.py` carries the caller-tree resolver `cwd=os.getcwd()` at `:148` under its `:140-145` docstring. Last round I claimed the opposite, having tested whether a COMMIT was an ancestor when the claim needed whether the FIX was present; the fix had arrived under a different hash. **A HASH TEST ANSWERS "DID THIS COMMIT LAND", NOT "IS THE FIX PRESENT" -- resolve a cherry-picked fix BY CONTENT, with a control.**
- ⭐ **THE POSITIVE-CONTROL ARM STANDS ANYWAY.** Any census you claim over YOUR tree prints `TREE_READ` and carries a control: a file existing ONLY on your branch must appear in the hits. It costs one file. **It survives its own premise because the fix is a property of the CHECKOUT YOU ARE STANDING IN, and you are the only one who can see that from where you are.**
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W4-S<k>`, continuing from the highest `W4-S<k>` already in the file; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy; every globgrph ECS derive publishes to a topic carrying a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (rows W2-S72, S104, S106, RESERVED FOR ANDREW). ⛔ **ANDREW'S ~17:1xZ "take off any holds on CLDGRPH" DOES NOT LIFT THIS AND YOU MAY NOT READ IT AS DOING SO** -- it is an estate-wide law, not a project hold, and the SMS card is a separate decision still his. **FORBIDDEN: NO `ecs run-task`, NO CodeBuild start, NO image build or push, NO `safe-apply` or `terraform apply`, NO S3 WRITE, NO act whose effect is an SNS publish.** ⭐ **PERMITTED: every READ of Opal infrastructure** -- `s3api get-object`/`head-object`/`list-*`, `logs`, `ecs describe-*`/`list-*`, `codebuild batch-get-builds`, `cloudtrail lookup-events`, a query through the projection service, and (where your cell names it) a warehouse read. Publishing nothing and paging nobody is the test.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); touch any subscription or topic; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`).
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1: v2-only flags fail as unknown options and it emits CRLF on `--output text`, so strip CR before any field test. A paginated `list-*` with `--query length()` returns the PAGE count. `cloudtrail lookup-events --start-time` is INCLUSIVE at the second. **A pipeline's rc is its LAST command's -- read the OUTPUT, never `cmd | tail`'s exit code.** ⛔ **Row S112:** `MATCH ()-[e:STORED_IN]->()` FAILS AT THE BINDER -- the served graph carries `edge_type` as a **PROPERTY**. A binder error is a wrong-form signal, NEVER a zero.
- ⛔ **IF A PATH YOU NEED IS NOT IN `<paths>`, THAT IS A BLOCKING ROW AND A REPORT, NEVER AN OVERRIDE.** And if a granted path's modification mechanically OBLIGES a second artifact, this face names the override and its owner below -- if it does not and you hit one, that omission is itself the row.

## THE CELL (decomposition v0.12 s.1a, CG-s-45)

`CG-s-38` (round 8, merged `4ab0da7983`) made the portal sha travel all four hops and took hop 1 as branch (a): both routes now write `portal_sha.txt` into the archive. **What (a) did NOT reach is the producer's HOME.**

No path in that order's grant was a production location, so **the route that actually produced every served zip in round 6 is still `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f3_build_source_zip.py`** -- a script in a worker's deliverable folder. The worker filed it as an owned item: `1.0.0_SA_CTO` to place, `0.7.0_AE_CloudOps` to run.

**AND THE COMMITTED ROUTE HAS ITS OWN DEFECT.** `.github/workflows/stitch-source-push.yml:66` checks the portal out at a LITERAL pinned ref `b96562720505...` under a comment calling the pin deliberate, against a real head of `5907cbca98...`. **Nothing updates it.** Round 8's row `W2-S78` armed exactly this.

⭐ **THE ITEM UNDERNEATH IS NOT A VINTAGE PROBLEM.** A production input to the served graph has no committed producer in a production location, and five pushes in one round were all made by hand.

## MEASURED BY THE ISSUER AT THE CUT (each claim says what KIND it is)

- **MEASURED (`CG-s-38`'s own record and its cited files re-read at HEAD):** 5 served pushes in round 6, 2 with any portal record, 0 declared; `f3_build_source_zip.py:84` computes the portal head; the workflow's literal pin at `:66`; the real head `5907cbca98...`.
- **MEASURED:** `CG-s-38` reported `HOP1_BRANCH=COMMITTED_PRODUCER`, `WRITES_PORTAL_SHA=true`, `HALF_DONE=false` -- **the producer works; it is only homeless.**
- **HELD, NOT MEASURED:** that the `.github/workflows` route is the one that SHOULD run. Round 8's face said this and it is still true: nobody has established whether the hand route existed because the workflow was broken, unauthorized, or merely unused. ⛔ **THAT IS A QUESTION FOR YOUR READING AND NOT AN ASSUMPTION OF THIS FACE** -- and it decides where the home should be.
- ⛔ **AND ONE THING NEITHER ROUND MEASURED:** whether the workflow has ever run at all. `W2-S78`'s own note says it needs a secret that may never have been provisioned. **An unrun route is not a route.**
## CUT DISCIPLINE (binds YOUR captures)

Every accept names its instrument's COVERAGE, its harness's GRAIN, the ENVIRONMENT its stored baseline came from, and the TREE it ran in. Print all four beside every number. A count without its denominator is refused at the flip, and so is a denominator that does not say what it excluded. **And a claim's PROVENANCE LABEL is graded here as much as its value: `measured` is what an instrument returned in this run; `held` is what you reasoned to; `inferred` is what follows from something else. Round 8's five false premises were all mislabelled `measured`, and the two labelled `held` cost nothing.**
## DELIVERABLE -- in this order

1. `i5_route.py` -- **establish which route has ACTUALLY run**, from run history rather than from the file's existence: has the committed workflow ever executed, and what produced each of round 6's five served zips. Print the denominator and the instrument, and report BLIND where retention or access prevents an answer.
2. `i5_home.py` -- **decide the home on that evidence**: if the workflow is the real route, its pin must resolve rather than sit literal, and the producer belongs beside it; if the hand route is the real one, its script needs a production location and an owner. **Print which, and what the other would have cost.**
3. **The move, or the filing.** Either the producer lands in a production location within your grant, or the blocker is filed as a named owned item with its owner and what unblocks it. **STATE WHICH.** Do not half-move it.
4. `i5_no_push.sh` -- prove no zip was pushed, no workflow triggered, nothing applied.
5. The record `CG-s-45.hop-1-home.result.md`, the instance, then the flip.
## ACCEPTANCE (v3 grammar)

<criterion id="I5-AC1" cell_refs="CG-s-45"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/i5_route.py</invocation><expect>WORKFLOW_EVER_RAN=(YES|NO|BLIND)[\s\S]*EVIDENCE printed[\s\S]*ZIPS_ATTRIBUTED=([0-9]+) of 5[\s\S]*INSTRUMENT printed[\s\S]*BLIND_REPORTED=([0-9]+)</expect></criterion>
`I5-AC1` -- WHICH ROUTE ACTUALLY RAN, FROM RUN HISTORY: whether the committed workflow has ever executed, and what produced each of round 6's five served zips, with blind instruments reported as blind rather than contributing a zero. **An unrun route is not a route, and the file's existence is not evidence that it ran.**

<criterion id="I5-AC2" cell_refs="CG-s-45"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/i5_home.py</invocation><expect>HOME_DECIDED=(WORKFLOW|HAND_ROUTE|FILED)[\s\S]*ON_EVIDENCE printed[\s\S]*PIN_DISPOSITION=(RESOLVES|LITERAL-WITH-OWNER|N/A)[\s\S]*ALTERNATIVE_COST printed</expect></criterion>
`I5-AC2` -- THE HOME IS DECIDED ON THE EVIDENCE OF AC1, not on which file looks more official: which route is real, what happens to the literal pin, and what the road not taken would have cost. The pin's disposition is graded because a pin nothing updates is the defect that armed this cell.

<criterion id="I5-AC3" cell_refs="CG-s-45"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/i5_move.sh</invocation><expect>BRANCH=(MOVED|FILED)[\s\S]*(PRODUCTION_PATH printed[\s\S]*HALF_MOVED=false|BLOCKER printed[\s\S]*OWNER_NAMED printed[\s\S]*WHAT_UNBLOCKS printed)</expect></criterion>
`I5-AC3` -- THE PRODUCER IS HOMED OR THE BLOCKER IS FILED WITH ITS OWNER: a real production location with nothing half-moved, or an explicit filing naming who can place it and what unblocks them. **Both are passes.** Half a move is the one outcome that is not.

<criterion id="I5-AC4" cell_refs="CG-s-45"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/i5_no_push.sh</invocation><expect>ZIP_PUSHES=0[\s\S]*WORKFLOW_TRIGGERS=0[\s\S]*S3_WRITES=0[\s\S]*TERRAFORM_APPLIES=0[\s\S]*CODEBUILD_STARTS=0[\s\S]*EGRESS_PROBE_CONTROL=FIRED</expect></criterion>
`I5-AC4` -- NOTHING WAS PUSHED OR TRIGGERED: this cell decides where a producer lives; it does not run it. A triggered workflow here would publish a source zip, which is squarely inside the hold.

<criterion id="I5-AC5" cell_refs="CG-s-45" judgment="true"/> `I5-AC5` -- THE READING: whether a production input with no committed producer in a production location is a bigger finding than the vintage it was found through; whether a deliberately pinned literal with no update step is a design or a defect; and what an estate should require before a hand-run script is allowed to feed a served artifact five times. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>I5-AC1, I5-AC2, I5-AC3, I5-AC4, I5-AC5</expected_criteria>

<proof_of_spec>
Criterion ids: `I5-AC1`..`I5-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> I5-AC1,I5-AC2,I5-AC3,I5-AC4,I5-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `I5-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report -- a worker that flips a terminal status while carrying a FAIL withdraws its own `<paths>` grant, because the grant is read from an order NON-TERMINAL at HEAD.
</proof_of_spec>

## SURFACES

`.github/workflows/stitch-source-push.yml` (`:66` the literal pin -- possible FIX SURFACE) - `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f3_build_source_zip.py` (the route that ran; READ, and MOVE only on that branch) - GitHub Actions run history and CodeBuild history (READ ONLY) - `CG-s-38.portal-vintage-four-hop-feed.result.md` and row W2-S78 (READ).

## BOUNDS

- ⛔ **NO ZIP IS PUSHED AND NO WORKFLOW IS TRIGGERED.** Running the route to find out whether it works publishes a source zip, which is inside the hold. Read its history instead.
- ⛔ **DO NOT MOVE THE SCRIPT AND LEAVE THE CALLER BEHIND.** `HALF_MOVED=false` is graded.
- **Nothing is applied.**
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-I-5.hop-1-producer-home.md
.github/workflows/stitch-source-push.yml
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.12 (the round-9 recut), cell CG-s-45 (s.1a).
<owned_cells>CG-s-45</owned_cells>
Read-dependencies, NOT claimed: CG-s-38 (TO-CG-H-3, merged @4ab0da7983 -- the four-hop feed and hop 1's branch (a)). CONCURRENT, NOT yours: CG-s-41 (slot ~1), CG-s-42/43 (slot ~2), CG-s-44 (slot ~3).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and the egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change. If a READ you need is refused by IAM, that is a finding and a row, never a reason to widen anything.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer FROM THE MAIN TREE; the worker re-runs it inside its own criteria where a denominator is claimed, under the tree clause in the standing law.
</preflight>
