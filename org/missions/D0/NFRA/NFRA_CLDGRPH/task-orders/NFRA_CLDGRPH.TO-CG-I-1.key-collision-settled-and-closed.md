# TO NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed -- CG-s-41 (ADDED at decomposition v0.12 on the CTO's round-8 analysis @2fa5bf1670 s.8): THE KEY COLLISION SETTLED, THEN CLOSED AT THE WRITER -- the root round 8 found and could not reach. SETTLE FIRST: a fix on an INFERRED root is a guess with a commit hash

<to_id>NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>complete -- flipped by 0.9.0_WK_NFRA_CLDGRPH~1 after a VALID proof-of-spec instance (proof-of-spec-check rc=0, violations=0) whose four MECHANICAL rows all read PASS by output; I1-AC5 is the judgment row and carries UNVERIFIABLE-BY-INSTRUMENT naming 3.0.0_SA_CVO at L9, never a verdict of mine. THE SETTLE RAN FIRST and returned SETTLED=YES before a producer line changed: the destroyed row is the S3_BUCKET_POLICY row whose node_id IS the bare bucket name, matched on the node_id limb, read off 27,685 of 27,685 warehouse rows at vintage 2026-09-10T12:24:50Z and corroborated on the AWS control plane with an EMPTY falsifier cell. The fix is COMMITTED AND NOT DEPLOYED at e86c4fb778 -- the running function is unchanged and the collision is still live in production. Two rows filed: NFRA_CLDGRPH-W1-S49 (ARMED -- the collision is FIVE class pairs, not one) and W1-S50 (INERT -- a third writer of graph_nodes carrying 7 columns where the live table carries 9). Push state LOCAL on branch wk-cldgrph-9-1.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool and NEVER with a shell `printf` or heredoc (rule 14a: a shell-built message file re-opens the injection one step earlier -- your issuer broke this once today and caught it before committing). Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.** Every script and capture carries `i1_`. Scratch `.scratch/`.
- ⛔ **THE TREE CLAUSE. Your issuer got this wrong last round and the correction is the lesson.** The comp-rail once resolved its corpus from the TOOL'S INSTALL LOCATION, so a census run from a linked worktree scanned the MAIN TREE and returned a well-formed zero with a real denominator. **THE FIX IS PRESENT IN YOUR WORKTREE** -- measured BY CONTENT at this cut, in your own checkout: `.tools/_comprail.py` carries the caller-tree resolver `cwd=os.getcwd()` at `:148` under its `:140-145` docstring. Last round I claimed the opposite, having tested whether a COMMIT was an ancestor when the claim needed whether the FIX was present; the fix had arrived under a different hash. **A HASH TEST ANSWERS "DID THIS COMMIT LAND", NOT "IS THE FIX PRESENT" -- resolve a cherry-picked fix BY CONTENT, with a control.**
- ⭐ **THE POSITIVE-CONTROL ARM STANDS ANYWAY.** Any census you claim over YOUR tree prints `TREE_READ` and carries a control: a file existing ONLY on your branch must appear in the hits. It costs one file. **It survives its own premise because the fix is a property of the CHECKOUT YOU ARE STANDING IN, and you are the only one who can see that from where you are.**
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W1-S<k>`, continuing from the highest `W1-S<k>` already in the file; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy; every globgrph ECS derive publishes to a topic carrying a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (rows W2-S72, S104, S106, RESERVED FOR ANDREW). ⛔ **ANDREW'S ~17:1xZ "take off any holds on CLDGRPH" DOES NOT LIFT THIS AND YOU MAY NOT READ IT AS DOING SO** -- it is an estate-wide law, not a project hold, and the SMS card is a separate decision still his. **FORBIDDEN: NO `ecs run-task`, NO CodeBuild start, NO image build or push, NO `safe-apply` or `terraform apply`, NO S3 WRITE, NO act whose effect is an SNS publish.** ⭐ **PERMITTED: every READ of Opal infrastructure** -- `s3api get-object`/`head-object`/`list-*`, `logs`, `ecs describe-*`/`list-*`, `codebuild batch-get-builds`, `cloudtrail lookup-events`, a query through the projection service, and (where your cell names it) a warehouse read. Publishing nothing and paging nobody is the test.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); touch any subscription or topic; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`).
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1: v2-only flags fail as unknown options and it emits CRLF on `--output text`, so strip CR before any field test. A paginated `list-*` with `--query length()` returns the PAGE count. `cloudtrail lookup-events --start-time` is INCLUSIVE at the second. **A pipeline's rc is its LAST command's -- read the OUTPUT, never `cmd | tail`'s exit code.** ⛔ **Row S112:** `MATCH ()-[e:STORED_IN]->()` FAILS AT THE BINDER -- the served graph carries `edge_type` as a **PROPERTY**. A binder error is a wrong-form signal, NEVER a zero.
- ⛔ **IF A PATH YOU NEED IS NOT IN `<paths>`, THAT IS A BLOCKING ROW AND A REPORT, NEVER AN OVERRIDE.** And if a granted path's modification mechanically OBLIGES a second artifact, this face names the override and its owner below -- if it does not and you hit one, that omission is itself the row.

## THE CELL (decomposition v0.12 s.1a, CG-s-41)

Round 8 attributed the 124-edge loss to a named Lambda by a hash match and then found the ROOT, and the root is a **KEY COLLISION** rather than a parenting choice.

`infra/aws/lambda/globgrph/incremental_updater/lambda_function.py:271` writes an `S3_BUCKET` node as `{"id": bucket, "arn": bucket_arn, "type": "S3_BUCKET", ...}` -- **`id` is the BARE BUCKET NAME.** And that exact string is `S3_BUCKET_POLICY`'s canonical key for **15 of 15** nodes of the class. `derive_runner.py`'s own key-rule docstring states the consequence in its own words: *"an edge built onto the short id does NOT dangle. It lands on whatever OTHER node holds that string as ITS canonical key ... So 135 STORED_IN and 27 SERVED_FROM edges resolved 100% of the time onto a bucket POLICY, and every dangling check in the estate read clean."*

**So two node classes contend for ONE warehouse key, and an upsert DESTROYS the other row.** That is the mechanism: one node left, `edges_skipped_missing_endpoint` rose `388 -> 512`, exactly the 124. The edges were never deleted -- their endpoint was.

⛔ **RE-PARENTING DOES NOT CLOSE THIS, AND THAT IS THE QUALIFIER THE WHOLE ROUND TURNS ON.** `CG-s-33`'s committed re-point changes which node the edges hang off. **The overwrite still destroys a node on every S3 write.** `CG-s-33` is NECESSARY AND NOT SUFFICIENT.

⛔ **AND `SERVED_FROM` IS STILL LOADED ON IT:** 27 edges, all 27 on the same parent class, measured at served vintage `2026-09-10T12:24:50` with `OWNED_BY=6385` as the positive control. Same collision, same Lambda path, untouched family. **That is a measurement, not a prediction.**

## MEASURED BY THE ISSUER AT THE CUT (each claim says what KIND it is)

- **MEASURED (`comp-find` by CONTENT from the MAIN tree, denominator 11,174 files scanned, ONE hit):** `infra/aws/lambda/globgrph/incremental_updater/lambda_function.py:271` is the only site in `infra/aws` writing `"id": bucket`. The file is **749 lines** at HEAD. I found it by what it DOES, not by the filename -- 21 files in the estate are called `lambda_function.py`.
- **MEASURED (`git show HEAD:`, read at this seat):** the writer's full node dict at `:270-273`, and `derive_runner.py`'s key rule `return str(n.get("arn") or "").strip() or str(n.get("id") or "").strip()` with the docstring quoted above.
- **MEASURED (this seat, through `projection_client`, one vintage `2026-09-10T12:24:50.576632+00:00`, manifest `aebbd9ce...`):** `STORED_IN=0`, `SERVED_FROM=27`, `S3_BUCKET_POLICY` nodes `12`, `OWNED_BY=6385` (positive control FIRED).
- ⛔ **INFERRED, AND LABELLED SO BECAUSE IT IS THE ONE THING THIS CELL MUST SETTLE FIRST:** *which* warehouse row the overwrite destroys. Row `W3-S19` labelled this `INFERRED` in its own words and said Trino/Athena would settle it, and that order had no grant. **A WAREHOUSE READ IS A READ AND IS PERMITTED. SETTLE IT BEFORE YOU CHANGE A LINE.**
- **HELD, NOT MEASURED:** that closing the collision at the writer is the right layer, rather than at the table's key definition or at the fold. **Three layers could hold this and I have not measured which is correct -- that is AC2's question, not an assumption of this face.**
## CUT DISCIPLINE (binds YOUR captures)

Every accept names its instrument's COVERAGE, its harness's GRAIN, the ENVIRONMENT its stored baseline came from, and the TREE it ran in. Print all four beside every number. A count without its denominator is refused at the flip, and so is a denominator that does not say what it excluded. **And a claim's PROVENANCE LABEL is graded here as much as its value: `measured` is what an instrument returned in this run; `held` is what you reasoned to; `inferred` is what follows from something else. Round 8's five false premises were all mislabelled `measured`, and the two labelled `held` cost nothing.**
## DELIVERABLE -- in this order

1. `i1_settle.py` -- **SETTLE THE INFERRED LINK.** Read the warehouse (Trino/Athena, or whatever instrument can actually see `graph_nodes` rows) and establish WHICH row the overwrite destroys and by what key. Print the instrument, its coverage and the key it matched on. **If no instrument available to you can see warehouse rows, that is `SETTLED=BLOCKED` with the instruments tried and what each could not see -- and that is a PASS.** What is not a pass is proceeding as if it were settled.
2. `i1_layers.py` -- **enumerate WHERE the collision can be closed** and what each layer costs: the writer (`:271`), the table's key definition, the fold's admission. For each, print whether it closes the collision for BOTH classes or only masks it, and which other writers of the same key space it would affect. **COUNT THE WRITERS of the key space and PRINT the count** -- a property with N writers needs N rules read, and this cell exists because one writer's convention silently overwrote another's.
3. **The fix at the layer step 2 names**, with the collision closed so two classes cannot contend for one key. **Producer/infra code only; NOTHING IS DEPLOYED.**
4. `i1_arm.py` -- **an OVERWRITE arm that goes RED first.** Build the collision on a fixture (two classes, one key, an upsert), show the second write destroying the first BEFORE the fix, capture that red run, then green after. **A negative control in the same run: two rows with genuinely distinct keys must both survive.**
5. `i1_served_from.py` -- **show `SERVED_FROM`'s 27 safe by the same arm rather than by argument.** They are on the same mechanism; if the fix closes it, they are covered, and that must be demonstrated rather than asserted.
6. The record `CG-s-41.key-collision.result.md` and the instance, then the flip.
## ACCEPTANCE (v3 grammar)

<criterion id="I1-AC1" cell_refs="CG-s-41"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/i1_settle.py</invocation><expect>SETTLED=(YES|BLOCKED)[\s\S]*INSTRUMENT printed[\s\S]*(DESTROYED_ROW_KEY printed[\s\S]*MATCHED_ON printed|INSTRUMENTS_TRIED=([1-9][0-9]*) of \3[\s\S]*WHAT_EACH_COULD_NOT_SEE printed)</expect></criterion>
`I1-AC1` -- THE INFERRED LINK IS SETTLED OR HONESTLY BLOCKED, BEFORE ANY LINE CHANGES: which warehouse row the overwrite destroys and on what key, from an instrument that can see rows -- or an explicit BLOCKED carrying every instrument tried and what each could not see. **Both are passes.** Changing code on an inferred root is what does not pass.

<criterion id="I1-AC2" cell_refs="CG-s-41"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/i1_layers.py</invocation><expect>LAYERS_ENUMERATED=([2-9]) of \1[\s\S]*KEY_SPACE_WRITERS=([0-9]+) counted[\s\S]*CLOSES_FOR_BOTH_CLASSES printed per layer[\s\S]*LAYER_CHOSEN=\S+[\s\S]*WHY printed</expect></criterion>
`I1-AC2` -- THE LAYER IS CHOSEN WITH ITS WRITERS COUNTED: every layer that could close the collision, whether each closes it for BOTH classes or merely masks it, and the WRITER COUNT of the key space printed rather than assumed. A property with N writers needs N rules read, and this cell exists because one writer's convention silently overwrote another's.

<criterion id="I1-AC3" cell_refs="CG-s-41"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/i1_arm.py</invocation><expect>BASELINE_RED_CAPTURED=true[\s\S]*OVERWRITE_ARM=PASS[\s\S]*DESTROYED_BEFORE=([1-9][0-9]*)[\s\S]*DESTROYED_AFTER=0[\s\S]*DISTINCT_KEYS_BOTH_SURVIVE=true[\s\S]*NEGATIVE_CONTROL=FIRED</expect></criterion>
`I1-AC3` -- THE ARM WENT RED FIRST: the collision reproduced on a fixture and shown destroying a row BEFORE the fix, zero after, with genuinely distinct keys still both surviving. `BASELINE_RED_CAPTURED` is what separates a test from a green that was always going to be green.

<criterion id="I1-AC4" cell_refs="CG-s-41"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/i1_no_egress.sh</invocation><expect>ECS_RUN_TASK_CALLS=0[\s\S]*CODEBUILD_STARTS=0[\s\S]*S3_WRITES=0[\s\S]*IMAGE_PUSHES=0[\s\S]*TERRAFORM_APPLIES=0[\s\S]*READS=([0-9]+) \(permitted\)[\s\S]*EGRESS_PROBE_CONTROL=FIRED</expect></criterion>
`I1-AC4` -- THE HOLD HONOURED AND THE PERMITTED READS COUNTED RATHER THAN HIDDEN: five held acts at zero with a control that fires on a planted positive, and the reads printed as a non-zero permitted count so 'took no read' and 'took an allowed read' are distinguishable.

<criterion id="I1-AC5" cell_refs="CG-s-41" judgment="true"/> `I1-AC5` -- THE READING: whether closing this at the writer is the right layer or merely the reachable one; whether a key space two classes can both claim is a schema defect that will recur under a different pair; and whether `CG-s-33`'s re-point should still deploy at all once the collision is closed, or becomes redundant. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>I1-AC1, I1-AC2, I1-AC3, I1-AC4, I1-AC5</expected_criteria>

<proof_of_spec>
Criterion ids: `I1-AC1`..`I1-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> I1-AC1,I1-AC2,I1-AC3,I1-AC4,I1-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `I1-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report -- a worker that flips a terminal status while carrying a FAIL withdraws its own `<paths>` grant, because the grant is read from an order NON-TERMINAL at HEAD.
</proof_of_spec>

## SURFACES

`infra/aws/lambda/globgrph/incremental_updater/lambda_function.py` (`:271`, the writer -- FIX SURFACE) - `infra/aws/globgrph/derive_runner.py` (the key rule and its docstring; READ, and edit only if AC2 names this layer) - the warehouse `graph_nodes` rows (READ ONLY, via whatever instrument can see them) - the projection service (READ ONLY, queries) - rows W3-S18, W3-S19, S112 and `CG-s-32.boundary-edge-class-census.result.md` (READ).

## BOUNDS

- ⛔ **SETTLE BEFORE YOU FIX.** AC1 runs first and its verdict is a precondition of AC3 meaning anything.
- **Nothing is deployed.** The fix is committed-not-deployed like every producer change in this project.
- ⛔ **DO NOT "FIX" THIS BY RE-PARENTING.** That is `CG-s-33`, it is already committed, and round 8 measured that it does NOT close the collision. A change that only moves the edges is this cell failing quietly.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-I-1.key-collision-settled-and-closed.md
infra/aws/lambda/globgrph/incremental_updater/lambda_function.py
infra/aws/globgrph/derive_runner.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.12 (the round-9 recut), cell CG-s-41 (s.1a).
<owned_cells>CG-s-41</owned_cells>
Read-dependencies, NOT claimed: CG-s-32 (TO-CG-G-1) and CG-s-33 (TO-CG-G-2, the committed-not-deployed re-point this cell must NOT mistake for a fix). CONCURRENT, NOT yours: CG-s-42/43 (slot ~2 edits `derive_stitch.py`), CG-s-44 (slot ~3), CG-s-45 (slot ~4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and the egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change. If a READ you need is refused by IAM, that is a finding and a row, never a reason to widen anything.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer FROM THE MAIN TREE; the worker re-runs it inside its own criteria where a denominator is claimed, under the tree clause in the standing law.
</preflight>
