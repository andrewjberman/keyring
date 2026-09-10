# TO NFRA_CLDGRPH.TO-CG-H-5 -- CG-s-40 (ADDED at decomposition v0.11 on the CTO's round-7 analysis @bb08a2ac62 s.6, item 5): TWO SCORERS DECLARE DIFFERENT CANONICAL SHAPES FOR ONE EDGE, AND ONE HAS THE WRONG CLASS BAKED INTO A SCORED ARTIFACT. The CTO places this OUTSIDE this project's plane, so the act is a PLACEMENT with an owner and an un-park condition -- NOT a fix, and NOT a mention in a message that ages out

<to_id>NFRA_CLDGRPH.TO-CG-H-5</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~4</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>pending -- GO = the spawn (spine v3 L7): slot ~4 on a fresh worktree cut from CLOUD by the issuer at C:/tmp/wk-cldgrph-8-4. ROUND 8 of NFRA_CLDGRPH; fanout 4 of 4 chains, cap 8. ONLY order of slot ~4's chain. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~4`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~4; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~4 <0.9.0_WK_NFRA_CLDGRPH~4@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/`.** Every script and capture carries `h5_`. Scratch `.scratch/`.
- ⛔ **THE COMP-RAIL TREE CLAUSE -- CORRECTED BEFORE YOU WERE SPAWNED, AND THE CORRECTION IS ITSELF THE LESSON.** The hazard (CTO msg 95103): before the caller-tree fix, `comp-find` / `comp-read` / `comp-pulse` invoked **from a linked worktree scanned the MAIN TREE and returned a well-formed zero with a real denominator**, and nothing in the output says which tree it read. **THE FIX IS PRESENT IN YOUR WORKTREE.** Measured BY CONTENT at the cut, in your own checkout and not by inference: `.tools/_comprail.py` carries the caller-tree resolver -- `cwd=os.getcwd()` at `:148`, under the docstring at `:140-145` naming the worktree case exactly -- and the main tree reads identically as the positive control. **MY FIRST READING SAID THE OPPOSITE AND IT WAS WRONG, for a reason worth more to you than the verdict:** I tested whether commit `6228c53377` was an ancestor of `CLOUD`. It is not, and it never will be -- the same FIX reached `CLOUD` under a different hash, `838b963638`, as a drain of a cherry-pick branch. **A HASH TEST ANSWERS "DID THIS COMMIT LAND", WHICH IS NOT THE QUESTION "IS THE FIX PRESENT". Resolve a cherry-picked or rebased fix BY CONTENT, with a negative control.** I had that trap written down and reached for `merge-base --is-ancestor` anyway.
- ⭐ **THE POSITIVE-CONTROL ARM STANDS ANYWAY, and it is now cheap rather than load-bearing (the CTO asked for it at 95105 and again at 95133).** Any census you claim over YOUR tree prints `TREE_READ` and carries a control: a file that exists ONLY on your branch must appear in the hits. It costs one file. **The reason to keep it after the fix landed is that the fix is a property of the checkout you are standing in, and you are the only one who can see that from where you are** -- a census that merely looks right is exactly what the old rail produced. A denominator is not a tree.
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W4-S<k>`, from S1 for this slot; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy; every globgrph ECS derive publishes to a topic carrying a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (rows W2-S72, S104, S106, RESERVED FOR ANDREW). **FORBIDDEN: NO `ecs run-task`, NO CodeBuild start, NO image act, NO `safe-apply`, NO S3 WRITE, NO act whose effect is an SNS publish.** A READ of the served graph or an Opal S3 object is permitted.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); touch any subscription or topic; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`, and note that `git log -- <path>` returns ZERO for a file added then deleted inside a merged branch).
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1 and emits CRLF on `--output text`. A pipeline's rc is its LAST command's. ⛔ **Row S112's banked trap:** `MATCH ()-[e:SERVED_FROM]->()` **errors at the binder** -- the served graph carries `edge_type` as a **PROPERTY**. A binder error is a wrong-form signal, never a zero.

## THE CELL (decomposition v0.11 s.1a, CG-s-40)

Round 7's class census found the boundary-edge defect reaches past the producers into the **scorers**, and that two of them describe one edge and disagree about what it points at:

- `infra/aws/globgrph/debtscan_canon_scorer.py` names `ServedURL-[SERVED_FROM]->S3_BUCKET_POLICY` as `AUTH_CANON`'s live shape -- **the wrong-class landing ADOPTED AS CANON inside a scored artifact**, and recorded there deliberately as an auditable per-class source decision.
- `infra/aws/globgrph/canon_motif_scorer.py` names the dominant motif `(ServedURL)-[SERVED_FROM]->(S3)` -- **which is what the edge was meant to be.**

**AND THERE IS A CLOCK ON IT.** CG-s-33 re-pointed both boundary families onto `S3_BUCKET` and is COMMITTED-NOT-DEPLOYED, held by the egress law while the RESERVED SMS card is with Andrew. **The morning that re-point reaches the served plane, `debtscan`'s dominant shape flips and its outlier threshold with it, and its census reads a 100 percent outlier rate.** The census record said it plainly: that consumer must move in the same act, or it breaks the morning after.

⭐ **WHAT THIS ORDER IS, AND WHAT IT IS NOT.** The CTO placed this item **outside this project's plane**. So the deliverable is a **PLACEMENT**: census the consumers, state the disagreement in one sentence an outside reader can act on, and **park it on its own carrier with an OWNER and an UN-PARK CONDITION**. It is not a fix. **A placement with no carrier is a silent hole** -- an item living only in a message reads as delivered and is owed by nobody. The shape to copy is `1e01703e54`, `org/tier1_exec/2.0.0_SA_COO/deliverables/PARKED_20260910_AUDIT_INVOKER_VINTAGE_TEST.md`: both fields populated, and the condition one that actually fires.

## MEASURED BY THE ISSUER AT THE CUT (every claim below says what kind of claim it is)

- **MEASURED (`git show HEAD:...` at `de3970331f`, read at this seat):** `debtscan_canon_scorer.py` is **377 lines**, `canon_motif_scorer.py` is **381 lines**, both last touched @`7f0a9d249c` (2026-09-05). The `AUTH_CANON` entry in `SCORED_FROM` spells the shape at `:47-49`; `score_auth_canon`'s docstring repeats it at `:143-145`; the motif scorer's return dict carries `"dominant_motif": "(ServedURL)-[SERVED_FROM]->(S3)"` at `:130-131`.
- **MEASURED (`comp-find --name`, run FROM THE MAIN TREE by the issuer, denominator 157,951 files scanned, corpus=all):** exactly **2** hits for `debtscan_canon_scorer.py` and **1** for `canon_motif_scorer.py`. ⭐ **AND THE SECOND HIT IS THE THING THE ROUND-7 CENSUS DID NOT CARRY:** `org/mcp/inbox/0.7.0_AE_CloudOps/~C/read/20260710T202210Z_0.8.0_AE_CloudComp_CLEAR_TO_DELETE_debtscan_canon_scorer.py.md`. **A message from 2026-07-10 says this scorer was clear to delete, and the file is still here at HEAD two months later.** READ THAT MESSAGE. **RETIRE may be a live branch beside RE-POINT, and you must not assume either.**
- **MEASURED (the census record `CG-s-32.boundary-edge-class-census.result.md` s.2):** the two families landing 100 percent on the shadow class -- `STORED_IN` 135 of 135 keys, `SERVED_FROM` 27 of 27 -- built by two different producer paths (`derive_stitch.py` and `derive_runner.py:1947-1966`).
- **HELD, NOT MEASURED (labelled deliberately):** that these two are the ONLY consumers of the canonical shape. The census found them while looking at something else; nobody has swept for the population. **AC1 is exactly that sweep, and finding a third consumer is a better outcome than confirming two.**
- **HELD, NOT MEASURED:** that `0.8.0_AE_CloudComp` is the right owner. The 2026-07-10 message was SENT by that seat, which is evidence of authorship, not of current ownership. **Verify the owner from the record before you write it onto a parked carrier** -- an owner named wrong is worse than an owner named absent, because it reads as assigned.

## CUT DISCIPLINE (spine v3.8 @9fc8cb266e, and it binds YOUR captures)

Every accept below names its instrument's COVERAGE, its harness's GRAIN, and the ENVIRONMENT its stored baseline came from. Print all three beside every number: what population the instrument swept and its denominator, at what grain the number is counted, and where the comparison value came from.

## DELIVERABLE -- in this order

1. `h5_consumer_census.py` -- **sweep for every consumer of the two canonical shapes**, by subtraction from a printed repository denominator and never from a forward list of the ones the census record happened to mention. Count both spellings (the wrong class and the intended one), classify each hit as SCORER / PRODUCER / FIXTURE / PROSE, and print the tree you read with its control. **A third consumer is the finding; two is the null result.**
2. `h5_disagreement.py` -- state the disagreement as a machine-checkable fact: the two declared shapes, their file and line, which one matches the SERVED graph today and which matches the COMMITTED re-point, and what changes on each side when the re-point deploys. Read the served graph to establish "today" -- `edge_type` as a property -- with a positive control.
3. **Read the 2026-07-10 CLEAR_TO_DELETE message** and record what it actually says, verbatim where it matters. Then state which branch the placement should offer: RE-POINT, RETIRE, or BOTH-ARE-LIVE-AND-HERE-IS-THE-DECIDER. **Do not decide it for the owner; hand them a decidable question.**
4. **The parked carrier** at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/PARKED_scorer-canonical-shape-disagreement.md`, with **both fields populated**: an OWNER verified from the record, and an UN-PARK CONDITION that actually fires -- the CG-s-33 re-point reaching the SERVED plane, which is Andrew-gated today. Include the one sentence an outside reader can act on, and the acts that must NOT be taken meanwhile.
5. The record `CG-s-40.two-scorers-one-edge.result.md`: the census with its denominator, the disagreement, the CLEAR_TO_DELETE finding, and the placement.
6. The instance, then the flip.

## ACCEPTANCE (v3 grammar)

<criterion id="H5-AC1" cell_refs="CG-s-40"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/h5_consumer_census.py</invocation><expect>TREE_READ=(MAIN|WORKTREE)[\s\S]*TREE_POSITIVE_CONTROL=(FIRED|N/A-MAIN-TREE)[\s\S]*REPOSITORY_DENOMINATOR=([1-9][0-9]*) file\(s\)[\s\S]*CONSUMERS_FOUND=([0-9]+)[\s\S]*CLASSIFIED=\4 of \4[\s\S]*BY_SUBTRACTION=true</expect></criterion>
`H5-AC1` -- THE CONSUMER POPULATION SWEPT BY SUBTRACTION, WITH ITS TREE AND ITS DENOMINATOR: every consumer classified, none left unclassified, and the census honest about which tree the rail actually read. `BY_SUBTRACTION=true` is asserted because a forward list of the consumers someone already mentioned is precisely how this estate has been finding these late.

<criterion id="H5-AC2" cell_refs="CG-s-40"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/h5_disagreement.py</invocation><expect>SHAPE_A printed[\s\S]*SHAPE_B printed[\s\S]*QUERY_FORM=edge_type-as-property[\s\S]*MATCHES_SERVED_TODAY=(A|B|NEITHER)[\s\S]*MATCHES_COMMITTED_REPOINT=(A|B|NEITHER)[\s\S]*BREAKS_ON_DEPLOY=(A|B|BOTH|NEITHER)[\s\S]*POSITIVE_CONTROL=FIRED</expect></criterion>
`H5-AC2` -- THE DISAGREEMENT MADE CHECKABLE RATHER THAN DESCRIBED: both declared shapes, which one the served graph agrees with today, which one the committed re-point agrees with, and which one breaks the morning the re-point deploys. That last field is the whole reason this item cannot simply be noted and forgotten.

<criterion id="H5-AC3" cell_refs="CG-s-40"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/h5_placement.sh</invocation><expect>CARRIER_EXISTS=true[\s\S]*OWNER=[^ ]+ \(verified from: [^)]+\)[\s\S]*UNPARK_CONDITION printed[\s\S]*BRANCHES_OFFERED=(1|2|3)[\s\S]*DECIDER printed[\s\S]*CLEAR_TO_DELETE_MESSAGE_READ=true[\s\S]*SCORER_FILES_MODIFIED=0</expect></criterion>
`H5-AC3` -- THE PLACEMENT IS A CARRIER, NOT A MENTION: the parked file exists with an owner traced to a named source, an un-park condition that fires, the branch or branches offered with what decides between them, the 2026-07-10 message actually read, and **zero scorer files modified** -- because this order places the item and does not take it.

<criterion id="H5-AC4" cell_refs="CG-s-40"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/h5_no_egress.sh</invocation><expect>ECS_RUN_TASK_CALLS=0[\s\S]*CODEBUILD_STARTS=0[\s\S]*S3_WRITES=0[\s\S]*IMAGE_PUSHES=0[\s\S]*TERRAFORM_APPLIES=0[\s\S]*PRODUCER_FILES_MODIFIED=0[\s\S]*EGRESS_PROBE_CONTROL=FIRED</expect></criterion>
`H5-AC4` -- THE HOLD HONOURED AND NOTHING OUTSIDE THE PLACEMENT TOUCHED: the five held acts and any producer edit at zero, with a control that fires on a planted positive so the zeros are a measurement rather than an absence of looking.

<criterion id="H5-AC5" cell_refs="CG-s-40" judgment="true"/> `H5-AC5` -- THE READING: whether a scorer adopting a defect as canon is a scorer bug or a signal that the canon was never checked against the producer that fills it; whether a scored artifact carrying a wrong class is more dangerous than the wrong class itself, because it launders it into an auditable record; and whether parking this is the right disposition at all, or whether the deploy clock makes it urgent enough to belong to someone now. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>H5-AC1, H5-AC2, H5-AC3, H5-AC4, H5-AC5</expected_criteria>

<proof_of_spec>
Criterion ids: `H5-AC1`..`H5-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/NFRA_CLDGRPH.TO-CG-H-5.two-scorers-one-edge-placed.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> H5-AC1,H5-AC2,H5-AC3,H5-AC4,H5-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `H5-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report -- a worker that flips a terminal status while carrying a FAIL withdraws its own `<paths>` grant, because the grant is read from an order that is NON-TERMINAL at HEAD.
</proof_of_spec>

## SURFACES

`infra/aws/globgrph/debtscan_canon_scorer.py` (**READ ONLY**, `:40-59` `SCORED_FROM`, `:141-150` `score_auth_canon`) - `infra/aws/globgrph/canon_motif_scorer.py` (**READ ONLY**, `:125-140` the return dict) - `org/mcp/inbox/0.7.0_AE_CloudOps/~C/read/20260710T202210Z_0.8.0_AE_CloudComp_CLEAR_TO_DELETE_debtscan_canon_scorer.py.md` (READ ONLY) - `infra/aws/globgrph/derive_runner.py:1947-1966` (READ ONLY, the `SERVED_FROM` producer path) - `CG-s-32.boundary-edge-class-census.result.md` s.2 (READ) - the served graph through the projection service (READ ONLY, queries) - `org/tier1_exec/2.0.0_SA_COO/deliverables/PARKED_20260910_AUDIT_INVOKER_VINTAGE_TEST.md` (READ ONLY, the carrier shape to copy).

## BOUNDS

- ⛔ **NO SCORER FILE IS EDITED BY THIS ORDER, ON EITHER BRANCH.** The CTO placed this outside this project's plane. Editing it here would be this project reaching into a surface it was told it does not own, and it would do so under an egress hold that stops it proving the change anyway.
- ⛔ **DO NOT DECIDE THE OWNER'S QUESTION FOR THEM.** Offer the branches and the decider. A placement that arrives pre-decided is an instruction from a seat with no authority to give one.
- **No alert, monitor, checker or freshness surface** (standing moratorium).
- **Reading another seat's inbox is legal (inspection); DRAINING one is not.** The message named in SURFACES is already in a `read/` directory -- read it in place and move nothing.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~4/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-H-5.two-scorers-one-edge-placed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.11 (the round-8 recut), cell CG-s-40 (s.1a; ADDED on the CTO's round-7 analysis @bb08a2ac62 s.6 item 5, whose owner column reads "outside this plane, PLACED" -- which is why the deliverable is a carrier and not a change).
<owned_cells>CG-s-40</owned_cells>
Read-dependencies, NOT claimed: CG-s-32 (TO-CG-G-1, drained @15bfeb3a62 -- the census that found the two scorers) and CG-s-33 (TO-CG-G-2, drained @e0255e47db -- the committed-not-deployed re-point that starts the clock). CONCURRENT, NOT yours: CG-s-36/37 (slot ~1, `derive_stitch.py` / `derive_runner.py`), CG-s-38 (slot ~2), CG-s-39 (slot ~3).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and the egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change; its only AWS contact is a read.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer FROM THE MAIN TREE (`--name` sweeps, denominator 157,951 files, corpus=all); the worker re-runs it inside its own criteria where a denominator is claimed, under the tree-trap bullet in the standing law.
</preflight>
