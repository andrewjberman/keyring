# TO NFRA_CLDGRPH.TO-CG-H-1 -- CG-s-36 (ADDED at decomposition v0.11 on the CTO's round-7 analysis @bb08a2ac62 s.6, item 1): THE `STORED_IN` RETIREMENT AS ITS OWN CELL, WITH ITS OWN ACCEPTS AND A REPOSITORY DENOMINATOR -- round 7 carried it as a ruling's condition on a face that had no criterion to grade it, so the assignee could not be told whether the retirement was inside what the order accepted. Here it can be GRADED, and a NOT-RETIRED answer is a PASS

<to_id>NFRA_CLDGRPH.TO-CG-H-1</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>pending -- GO = the spawn (spine v3 L7): slot ~1 on the worktree at C:/tmp/wk-cldgrph-8-1, SECOND of its chain, handed by CONTINUING the same subagent after TO-CG-H-2 goes terminal. ROUND 8 of NFRA_CLDGRPH; fanout 4 of 4 chains, cap 8. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** Every script and capture carries `h1_`. Scratch `.scratch/`.
- ⛔ **THE COMP-RAIL TREE CLAUSE -- CORRECTED BEFORE YOU WERE SPAWNED, AND THE CORRECTION IS ITSELF THE LESSON.** The hazard (CTO msg 95103): before the caller-tree fix, `comp-find` / `comp-read` / `comp-pulse` invoked **from a linked worktree scanned the MAIN TREE and returned a well-formed zero with a real denominator**, and nothing in the output says which tree it read. **THE FIX IS PRESENT IN YOUR WORKTREE.** Measured BY CONTENT at the cut, in your own checkout and not by inference: `.tools/_comprail.py` carries the caller-tree resolver -- `cwd=os.getcwd()` at `:148`, under the docstring at `:140-145` naming the worktree case exactly -- and the main tree reads identically as the positive control. **MY FIRST READING SAID THE OPPOSITE AND IT WAS WRONG, for a reason worth more to you than the verdict:** I tested whether commit `6228c53377` was an ancestor of `CLOUD`. It is not, and it never will be -- the same FIX reached `CLOUD` under a different hash, `838b963638`, as a drain of a cherry-pick branch. **A HASH TEST ANSWERS "DID THIS COMMIT LAND", WHICH IS NOT THE QUESTION "IS THE FIX PRESENT". Resolve a cherry-picked or rebased fix BY CONTENT, with a negative control.** I had that trap written down and reached for `merge-base --is-ancestor` anyway.
- ⭐ **THE POSITIVE-CONTROL ARM STANDS ANYWAY, and it is now cheap rather than load-bearing (the CTO asked for it at 95105 and again at 95133).** Any census you claim over YOUR tree prints `TREE_READ` and carries a control: a file that exists ONLY on your branch must appear in the hits. It costs one file. **The reason to keep it after the fix landed is that the fix is a property of the checkout you are standing in, and you are the only one who can see that from where you are** -- a census that merely looks right is exactly what the old rail produced. A denominator is not a tree.
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W1-S<k>`, continuing from the highest `W1-S<k>` already in the file; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy; every globgrph ECS derive publishes to a topic carrying a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (rows W2-S72, S104, S106, RESERVED FOR ANDREW). **FORBIDDEN: NO `ecs run-task`, NO CodeBuild start, NO image build or push, NO digest re-pin, NO `safe-apply`, NO S3 WRITE, NO act whose effect is an SNS publish.** A READ of the served graph through the projection service, and a GET of an Opal S3 object, are permitted.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); touch any subscription or topic; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`).
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1 and emits CRLF on `--output text`. A pipeline's rc is its LAST command's. ⛔ **AND ONE BANKED TRAP, row S112, so you do not spend a minute on it:** `MATCH ()-[e:STORED_IN]->()` **fails at the binder** with "Table STORED_IN does not exist" -- the served graph carries `edge_type` as a **PROPERTY**, not as a relationship table. **A binder error is a wrong-form signal, NEVER a count of zero.** Read `edge_type` as a property.

## THE CELL (decomposition v0.11 s.1a, CG-s-36)

The CTO ruled at 94872 that `STORED_IN` should be retired and `SERVED_FROM` re-pointed, on two binding conditions. **Both conditions failed ON MEASUREMENT, which is the outcome a condition exists to produce**, and the first failed in the most instructive way available:

1. **CONDITION 1'S CENSUS, RUN EXACTLY AS SPECIFIED, AUTHORIZES A BREAKING RETIREMENT.** It named `org/modules/graph/graph-call-manifest.yaml` as the denominator. Over that denominator `MANIFEST_TOOLS_TOUCHING_STORED_IN = 0 of 78`, and the zero is honest for that domain -- 78 of 78 names resolved to a file, so the arm separating a true zero from a resolution failure was present and passed. **The unscoped sweep of 31,293 tracked files finds FIVE consumers outside it.** A manifest is a **DECLARATION** of consumers, not a **CENSUS** of them. Rows W1-S38, S110.
2. **CONDITION 2 IS BLOCKED BY MEASUREMENT.** `OWNED_BY` is consumed as a **CONTAINMENT** seam by `org/modules/graph/cse_schema.py:323` (mapped to `Relationship.OWNS`), `comp_marker_read.py:121` (`_DRILL_REVERSE`, a rollup seam) and `comp_coverage_check.py:523` (fine-to-coarse parent). Widening `OWNED_BY`'s stated intent to absorb LOCATION changes what three readers mean -- and by the condition's own terms, **a retirement whose surviving term cannot absorb the retired one's intent is a DELETION, not a consolidation.** Row W1-S37, still open.

**THE PART THAT IS THIS ISSUER'S DEFECT AND NOT THE ASSIGNEE'S, restated because it is why this order exists:** the retirement arrived as a ruling's condition on a face whose accepts were `G2-AC1..AC5`. **A ruling was written onto a face with no criterion to grade it**, so the order could not tell its assignee whether the retirement was inside what it accepted. The worker held its `<status>` on condition 1's STOP instruction, which was correct and is the refusal clause working as designed.

⭐ **SO THE CENTRAL INSTRUCTION OF THIS ORDER IS A SHAPE, NOT AN OUTCOME: BOTH BRANCHES ARE PASSES.** RETIRE, with every consumer re-pointed in the same act and proven. Or DO NOT RETIRE, with the blocker named and cited. **What FAILS is a third thing: a branch taken without stating which one it is, or an authorizing zero whose domain and tree are not both printed.** You are not being asked to deliver a retirement. You are being asked to deliver a DECISION that a reader can check.

## MEASURED BY THE ISSUER AT THE CUT (every claim below is a READ at HEAD `de3970331f`, and each says which)

- **MEASURED (`git cat-file -e` at HEAD, 5 of 5 present):** the five consumers W1-S38 found outside the manifest all still exist -- `org/modules/graph/tsgraph_spike/load_scratch_kuzu.py` (`:59`, a WRITE emitting `edge_type STORED_IN`); `org/modules/graph/tsgraph_spike/out/ts_semantic_benchmark_slice.producer.json` (`:1057`, the literal as an `edge_type` value); `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f11_edges_resolve.sh` (`:70`, `:110-112`, round 6's own F11-AC3 instrument); `.../f11_test_unified.py` (`:93`, a fixture); `.../f4_test_stitch_ingest.py` (`:76`, the fold's own fixture).
- **MEASURED (`git show HEAD:...`):** the two consumers INSIDE the round-7 grant are `derive_runner.py:2275` -- `STITCH_EDGE_TYPES = frozenset({"ROUTES_TO", "WRITES", "READS", "DERIVES_FROM", "STORED_IN"})`, the fold's admission filter, read again at `:2543` -- and `derive_stitch.py:158/:159` (the drop-on-read, which **TO-CG-H-2 in your own queue has just changed -- re-read it, do not work from this line**) plus `:255` (the emit).
- **MEASURED:** `org/modules/graph/graph-call-manifest.yaml` is 1,900 lines at HEAD, last touched @`aac6ffe73f`.
- **MEASURED (the census record `CG-s-32.boundary-edge-class-census.result.md`, s.3):** all 135 `STORED_IN` source keys also carry an `OWNED_BY` edge (135 of 135), and in 135 of 135 the `OWNED_BY` bucket ARN names the same bucket as the `STORED_IN` target name. **So `STORED_IN` restates a fact the graph already holds** -- which is the strongest argument FOR retirement and it is already measured; you do not need to re-derive it, you need to decide against condition 2.
- **HELD, NOT MEASURED (labelled deliberately):** that the `tsgraph_spike` pair is inert. Row W2-S25 declared it harmless at TO-CG-D-7 **for a different question**, and W1-S38 found it a live consumer for this one. **A population declared safe to ignore for one question is not thereby safe for another** -- if your branch is RETIRE, that pair needs its own reading, not W2-S25's.
- ⛔ **A BULLET THAT USED TO SIT HERE HAS BEEN WITHDRAWN, AND THE WITHDRAWAL IS THE POINT.** It read: *"MEASURED (this seat, at the cut, and it is the reason for the tree clause): `git merge-base --is-ancestor 6228c53377 HEAD` -> NOT an ancestor. Positive control `bb08a2ac62` -> ON-BRANCH."* **Every word of that is true and it is not evidence for what it was offered as evidence for.** The commit genuinely is not an ancestor and never will be; the FIX it carries reached `CLOUD` under `838b963638` and is present in your checkout, measured by content. So the reason for the tree clause is NOT that the rail is broken here. **The reason is the one stated in the standing law above: the fix is a property of the checkout you are standing in, and you are the only one who can see that from where you are.** Withdrawn rather than deleted, because a face that quietly loses a claim teaches a reader nothing, and this cell is about exactly that class of error one axis over. Row `NFRA_CLDGRPH-S115`.

## CUT DISCIPLINE (spine v3.8 @9fc8cb266e, and it binds YOUR captures)

Every accept below names its instrument's COVERAGE, its harness's GRAIN, and the ENVIRONMENT its stored baseline came from. Print all three beside every number: what population the instrument swept and its denominator, at what grain the number is counted, and where the comparison value came from. A count without its denominator is refused at the flip, and so is a denominator that does not say what it excluded. **This round adds one field to that list: the TREE.**

## DELIVERABLE -- in this order

1. `h1_reader_census.py` -- **the reader census with the REPOSITORY as its denominator.** Enumerate BY SUBTRACTION from the printed repository denominator, never by a forward list; the call manifest is ONE INPUT you also read and report, never the definition of the domain. Print, separately and both: the MANIFEST-scoped count with its denominator, and the REPOSITORY-scoped count with its denominator, **and the DELTA between them** -- because the delta is the finding the round-7 cell bought. Print the TREE the census ran in, with the positive control that proves it. Classify every surviving hit as READ / WRITE / FIXTURE / PROSE with a classifier control on a planted line of each class.
2. `h1_domain_falsifier.py` -- **the amended Rule 24(i) act, run BEFORE any subtraction is trusted.** One UNSCOPED read of the term over the corpus with its denominator printed, compared against what the declared domain holds; a member the domain does not hold VOIDS the subtraction, and the script says so in those words. **This is a separate script from AC1 on purpose: the falsifier must be able to fail while the census succeeds.**
3. **The BRANCH, and its execution.**
   - **If the reader set is EMPTY and condition 2 is satisfiable:** RETIRE. Every consumer re-pointed **in the same act**, `STITCH_EDGE_TYPES` updated, the fixtures and instruments moved, and a re-run proving no surviving reader. Half-landed is the one forbidden outcome.
   - **If it is NON-EMPTY, or condition 2 is blocked:** DO NOT RETIRE, and say so as a decision rather than as a silence. Name every blocking consumer with file and line, cite `OWNED_BY`'s three containment readers, and state what would have to change for the retirement to become available -- **that sentence is the deliverable's value, because the next seat to reach for this will otherwise re-run the same census.**
4. **The manifest amendment** (`org/modules/graph/graph-call-manifest.yaml`, granted): one sentence on the manifest itself saying **what its denominator does and does not cover for a RETIREMENT question**, naming the unscoped repository sweep as the required second arm. This is W1-S38's own stated remedy and it is durable -- the NEXT vocabulary retirement in this estate will be censused against this manifest and it will again read clean. **Additive prose only: change no entry, no tool, no route.**
5. The record `CG-s-36.stored-in-retirement.result.md`: the two censuses with their denominators and their tree, the delta, the falsifier's verdict, the branch taken and the evidence that forced it, and the manifest sentence.
6. The instance, then the flip.

## ACCEPTANCE (v3 grammar)

<criterion id="H1-AC1" cell_refs="CG-s-36"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/h1_reader_census.py</invocation><expect>TREE_READ=(MAIN|WORKTREE)[\s\S]*TREE_POSITIVE_CONTROL=(FIRED|N/A-MAIN-TREE)[\s\S]*REPOSITORY_DENOMINATOR=([1-9][0-9]*) file\(s\)[\s\S]*MANIFEST_DENOMINATOR=([1-9][0-9]*) tool\(s\)[\s\S]*REPOSITORY_CONSUMERS=([0-9]+)[\s\S]*MANIFEST_CONSUMERS=([0-9]+)[\s\S]*DOMAIN_DELTA=([0-9]+)[\s\S]*CLASSIFIER_CONTROL=4 of 4</expect></criterion>
`H1-AC1` -- THE CENSUS NAMES ITS TREE AND ITS DOMAIN, AND PRINTS BOTH DENOMINATORS AND THEIR DELTA: the manifest count is reported beside the repository count rather than instead of it, so a reader sees the size of the gap that authorized a breaking retirement last round. `TREE_READ` and its control are what make a comp-rail denominator admissible from a linked worktree at all.

<criterion id="H1-AC2" cell_refs="CG-s-36"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/h1_domain_falsifier.py</invocation><expect>UNSCOPED_DENOMINATOR=([1-9][0-9]*)[\s\S]*DOMAIN_HOLDS=([0-9]+) of \1[\s\S]*MEMBERS_OUTSIDE_DOMAIN=([0-9]+)[\s\S]*SUBTRACTION_VERDICT=(VALID|VOID)[\s\S]*FALSIFIER_CONTROL=FIRED</expect></criterion>
`H1-AC2` -- THE DOMAIN IS FALSIFIED BEFORE THE SUBTRACTION IS TRUSTED: one unscoped read with its denominator, the count the declared domain actually holds, and an explicit VALID-or-VOID verdict on the subtraction. A wrong domain returning EMPTY is the branch that gets acted on, so the verdict is printed rather than inferred.

<criterion id="H1-AC3" cell_refs="CG-s-36"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/h1_branch.sh</invocation><expect>BRANCH=(RETIRED|NOT_RETIRED)[\s\S]*(SURVIVING_READERS=0 of ([0-9]+)[\s\S]*CONSUMERS_REPOINTED=([1-9][0-9]*) of \4[\s\S]*HALF_LANDED=false|BLOCKING_CONSUMERS=([1-9][0-9]*) named with file and line[\s\S]*OWNED_BY_CONTAINMENT_READERS=3 of 3 cited[\s\S]*WHAT_WOULD_UNBLOCK printed)</expect></criterion>
`H1-AC3` -- THE BRANCH IS STATED AND THE BRANCH TAKEN IS PROVEN: a RETIRED verdict must show zero surviving readers with every consumer moved in the same act and `HALF_LANDED=false`; a NOT_RETIRED verdict must name every blocker with its line, cite all three containment readers, and print what would unblock it. **Both are passes.** What cannot pass is a run that does not say which branch it took.

<criterion id="H1-AC4" cell_refs="CG-s-36"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/h1_no_egress.sh</invocation><expect>ECS_RUN_TASK_CALLS=0[\s\S]*CODEBUILD_STARTS=0[\s\S]*S3_WRITES=0[\s\S]*IMAGE_PUSHES=0[\s\S]*TERRAFORM_APPLIES=0[\s\S]*MANIFEST_ENTRIES_CHANGED=0[\s\S]*EGRESS_PROBE_CONTROL=FIRED</expect></criterion>
`H1-AC4` -- THE HOLD HONOURED AND THE MANIFEST AMENDED ADDITIVELY: the five held acts at zero with a control that fires on a planted positive, plus proof that the manifest gained prose and lost no entry -- because an amendment that silently drops a route is a worse defect than the one it documents.

<criterion id="H1-AC5" cell_refs="CG-s-36" judgment="true"/> `H1-AC5` -- THE READING: whether `STORED_IN` should be retired at all given that `OWNED_BY` already carries the same fact on a superset of the keys and on the correct class; whether condition 2's containment objection is a real semantic bar or a naming one that a third term would resolve; and what it would take for this estate to census a retirement correctly by construction rather than by an assignee running the sweep nobody asked for. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>H1-AC1, H1-AC2, H1-AC3, H1-AC4, H1-AC5</expected_criteria>

<proof_of_spec>
Criterion ids: `H1-AC1`..`H1-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-H-1.stored-in-retirement-own-cell.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> H1-AC1,H1-AC2,H1-AC3,H1-AC4,H1-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `H1-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report -- a worker that flips a terminal status while carrying a FAIL withdraws its own `<paths>` grant, because the grant is read from an order that is NON-TERMINAL at HEAD.
</proof_of_spec>

## SURFACES

`org/modules/graph/graph-call-manifest.yaml` (READ + the additive amendment) - `infra/aws/globgrph/derive_runner.py` (`:2275` `STITCH_EDGE_TYPES`, `:2543` its read; edit only on the RETIRE branch) - `infra/aws/globgrph/derive_stitch.py` (`:158/:159/:255`; **re-read at HEAD -- your own previous order changed this file**) - `org/modules/graph/tsgraph_spike/load_scratch_kuzu.py` and `.../out/ts_semantic_benchmark_slice.producer.json` (READ; edit only on the RETIRE branch) - the three round-6 instruments under `deliverables/0.9.0_WK_NFRA_CLDGRPH~2/` (READ; edit only on the RETIRE branch) - `org/modules/graph/cse_schema.py:323`, `comp_marker_read.py:121`, `comp_coverage_check.py:523` (**READ ONLY, ALWAYS -- these three are the containment objection and are NOT yours to change on either branch**) - rows W1-S37, W1-S38, S110, S112 (READ).

## BOUNDS

- ⛔ **`cse_schema.py`, `comp_marker_read.py` and `comp_coverage_check.py` are READ ONLY on BOTH branches.** They are the evidence for condition 2. Changing what they mean in order to satisfy the condition that measures them is the circular act this cell exists to prevent.
- **Nothing is deployed.** The fold and the producers are committed-not-deployed by standing hold; this order changes that for nothing.
- **A RETIRE branch must be COMPLETE in one act or not taken.** Half-landed is the single forbidden outcome and `HALF_LANDED=false` is graded.
- ⚠ **This order may touch `org/modules/graph/`, which means the drain owes a comp-system pass that round 7's four merges did not.** Say in your final report whether any `org/modules/graph` path is in your commit, so the issuer does not have to infer it.
- ⛔ **THREE OF YOUR GRANTED PATHS LIVE IN ANOTHER SLOT'S DELIVERABLES FOLDER, and slot `~2` is working in it RIGHT NOW.** You are granted exactly `f11_edges_resolve.sh`, `f11_test_unified.py` and `f4_test_stitch_ingest.py` -- three round-6 files, named individually and not by directory, precisely so that this order and TO-CG-H-3 cannot collide. **Touch nothing else in that folder, and in particular nothing named `h3_*`.** Those three are yours only on the RETIRE branch; on the NOT_RETIRED branch you read them and leave them.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f11_edges_resolve.sh
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f11_test_unified.py
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/f4_test_stitch_ingest.py
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-H-1.stored-in-retirement-own-cell.md
org/modules/graph/graph-call-manifest.yaml
org/modules/graph/tsgraph_spike/load_scratch_kuzu.py
org/modules/graph/tsgraph_spike/out/ts_semantic_benchmark_slice.producer.json
infra/aws/globgrph/derive_runner.py
infra/aws/globgrph/derive_stitch.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.11 (the round-8 recut), cell CG-s-36 (s.1a; ADDED on the CTO's round-7 analysis @bb08a2ac62 s.6 item 1).
<owned_cells>CG-s-36</owned_cells>
Read-dependencies, NOT claimed: CG-s-32 (TO-CG-G-1, drained @15bfeb3a62 -- the class census and its `OWNED_BY` superset finding) and CG-s-33 (TO-CG-G-2, drained @e0255e47db -- the fold normalization, committed-not-deployed). IMMEDIATELY BEFORE YOU IN YOUR OWN QUEUE and it changed a file you also touch: CG-s-37 (TO-CG-H-2).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and the egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer FROM THE MAIN TREE for the round-8 population; this order's own censuses run under the tree clause in the standing law and are graded on it at H1-AC1.
</preflight>
