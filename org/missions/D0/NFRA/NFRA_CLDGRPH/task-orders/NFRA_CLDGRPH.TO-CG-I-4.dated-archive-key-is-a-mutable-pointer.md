# TO NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer -- CG-s-44 (ADDED at decomposition v0.12): A DATED ARCHIVE KEY THAT READS IMMUTABLE AND IS A MUTABLE POINTER, ON AN UNVERSIONED BUCKET -- so three records cite bytes nobody can recover

<to_id>NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<status>pending -- GO = the spawn (spine L7, read at HEAD): slot ~3 on a worktree cut from CLOUD BY THE ISSUER and named in your prompt. ROUND 9 of NFRA_CLDGRPH; fanout 4 of 4 chains, cap 8. ONLY order of this slot's chain. The assignee commits its own status flip after a VALID proof-of-spec instance whose mechanical rows ALL read PASS.</status>

## STANDING LAW (inlined)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~3; export PATH="/c/Users/AndrewBerman/AppData/Local/Programs/Python/Python312:$PATH";`. Commit via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~3 <0.9.0_WK_NFRA_CLDGRPH~3@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool and NEVER with a shell `printf` or heredoc (rule 14a: a shell-built message file re-opens the injection one step earlier -- your issuer broke this once today and caught it before committing). Never push, merge, rebase, `checkout --` or `clean`. Push state LOCAL.
- **Write surface = the PATHS block + `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/`.** Every script and capture carries `i4_`. Scratch `.scratch/`.
- ⛔ **THE TREE CLAUSE. Your issuer got this wrong last round and the correction is the lesson.** The comp-rail once resolved its corpus from the TOOL'S INSTALL LOCATION, so a census run from a linked worktree scanned the MAIN TREE and returned a well-formed zero with a real denominator. **THE FIX IS PRESENT IN YOUR WORKTREE** -- measured BY CONTENT at this cut, in your own checkout: `.tools/_comprail.py` carries the caller-tree resolver `cwd=os.getcwd()` at `:148` under its `:140-145` docstring. Last round I claimed the opposite, having tested whether a COMMIT was an ancestor when the claim needed whether the FIX was present; the fix had arrived under a different hash. **A HASH TEST ANSWERS "DID THIS COMMIT LAND", NOT "IS THE FIX PRESENT" -- resolve a cherry-picked fix BY CONTENT, with a control.**
- ⭐ **THE POSITIVE-CONTROL ARM STANDS ANYWAY.** Any census you claim over YOUR tree prints `TREE_READ` and carries a control: a file existing ONLY on your branch must appear in the hits. It costs one file. **It survives its own premise because the fix is a property of the CHECKOUT YOU ARE STANDING IN, and you are the only one who can see that from where you are.**
- **Surprise = ONE ROW** (`NFRA_CLDGRPH-W3-S<k>`, continuing from the highest `W3-S<k>` already in the file; `surfaced_at` a REAL minute, never an `x`; restate the denominator by parsing every fenced json block; never edit an existing row; keep working).
- **Every criterion invocation under `timeout 120`.** Non-ASCII refused in code, logs and captures (`OK:` / `WARN:` / `ERROR:` / `SKIP:` / `BLOCKED:`).
- **THE EGRESS HOLD.** CLAUDE.md excludes ALL EGRESS OFF OPAL INFRASTRUCTURE from standing agent autonomy; every globgrph ECS derive publishes to a topic carrying a LIVE SMS SUBSCRIPTION TO A PERSONAL MOBILE (rows W2-S72, S104, S106, RESERVED FOR ANDREW). ⛔ **ANDREW'S ~17:1xZ "take off any holds on CLDGRPH" DOES NOT LIFT THIS AND YOU MAY NOT READ IT AS DOING SO** -- it is an estate-wide law, not a project hold, and the SMS card is a separate decision still his. **FORBIDDEN: NO `ecs run-task`, NO CodeBuild start, NO image build or push, NO `safe-apply` or `terraform apply`, NO S3 WRITE, NO act whose effect is an SNS publish.** ⭐ **PERMITTED: every READ of Opal infrastructure** -- `s3api get-object`/`head-object`/`list-*`, `logs`, `ecs describe-*`/`list-*`, `codebuild batch-get-builds`, `cloudtrail lookup-events`, a query through the projection service, and (where your cell names it) a warehouse read. Publishing nothing and paging nobody is the test.
- **NEVER:** build or propose any alert, alarm, SNS, SES, notification, freshness-checker or monitor (standing moratorium); touch any subscription or topic; `2>/dev/null` on a verdict-bearing read; bare `git commit`; `git log -- <path>` for a provenance question (use `--full-history`).
- **Search rail:** `python .tools/comp-read <file> --for "<question>"` and `python .tools/comp-find '<pattern>' <pathspec> --limit N`; raw recursive grep/find is refused by the hook; a `cmd | grep` receiver is free.
- **Instruments:** `jq` is absent -- read JSON with python. `.tools/aws` is CLI v1: v2-only flags fail as unknown options and it emits CRLF on `--output text`, so strip CR before any field test. A paginated `list-*` with `--query length()` returns the PAGE count. `cloudtrail lookup-events --start-time` is INCLUSIVE at the second. **A pipeline's rc is its LAST command's -- read the OUTPUT, never `cmd | tail`'s exit code.** ⛔ **Row S112:** `MATCH ()-[e:STORED_IN]->()` FAILS AT THE BINDER -- the served graph carries `edge_type` as a **PROPERTY**. A binder error is a wrong-form signal, NEVER a zero.
- ⛔ **IF A PATH YOU NEED IS NOT IN `<paths>`, THAT IS A BLOCKING ROW AND A REPORT, NEVER AN OVERRIDE.** And if a granted path's modification mechanically OBLIGES a second artifact, this face names the override and its owner below -- if it does not and you hit one, that omission is itself the row.

## THE CELL (decomposition v0.12 s.1a, CG-s-44)

`s3://opal-313476888478-globgrph/snapshots/<date>/graph-<date>.tar.gz` **reads as a dated, immutable archive and IS a mutable pointer.** Any derive run on that date key overwrites it.

Round 8 measured the consequence: the `20260909` key now carries `LastModified 2026-09-10T00:09:02Z`, **three hours after** the `21:05:21Z` bytes that THREE separate round-6 records cite. `get-bucket-versioning` returns **no Status** and `list-object-versions` returns exactly one version with `VersionId 'null'`. **So the cited bytes are not recoverable by anyone** -- not by the citing seat, not by the CVO, not by a later round.

⭐ **THE KEY GRAMMAR IS THE HAZARD.** A reader seeing `snapshots/20260909/graph-20260909.tar.gz` reasonably believes it names the 9th's archive. It names whatever was written last on the 9th's key. **Every citation of a dated snapshot in this project's record is therefore a citation without a recoverable referent, and nothing in the key says so.**

## MEASURED BY THE ISSUER AT THE CUT (each claim says what KIND it is)

- **MEASURED (row `W1-S43`, live reads by the round-8 worker):** `head-object` -> `LastModified Thu, 10 Sep 2026 00:09:02 GMT`, `ContentLength 1674681`, `ETag 336e29e366197e43063d372b9002302f`; `get-bucket-versioning` -> rc 0 with NO Status; `list-object-versions --prefix snapshots/20260909/` -> exactly one Version, `VersionId 'null'`, `IsLatest true`.
- **MEASURED:** rows `W2-S61` and `W2-S75` both cite `LastModified 2026-09-09T21:05:21Z` for that same bucket and key.
- **HELD, NOT MEASURED:** that changing the WRITER's key grammar is preferable to changing the estate's citation grammar. **Both close it and they have different owners and different costs. AC2 is that comparison, not this face's assumption.**
- ⛔ **AND ONE THING THIS FACE DOES NOT ASSERT:** how many citations in this project's record actually point at overwritten bytes. **Nobody has counted them. AC1 is that count**, and it decides whether this is a documentation cleanup or a live evidential problem.
## CUT DISCIPLINE (binds YOUR captures)

Every accept names its instrument's COVERAGE, its harness's GRAIN, the ENVIRONMENT its stored baseline came from, and the TREE it ran in. Print all four beside every number. A count without its denominator is refused at the flip, and so is a denominator that does not say what it excluded. **And a claim's PROVENANCE LABEL is graded here as much as its value: `measured` is what an instrument returned in this run; `held` is what you reasoned to; `inferred` is what follows from something else. Round 8's five false premises were all mislabelled `measured`, and the two labelled `held` cost nothing.**
## DELIVERABLE -- in this order

1. `i4_census.py` -- **count the citations at risk.** Sweep this project's record for citations of a dated snapshot key, with a printed denominator and the tree stated, and for each determine whether the bytes it names are still the bytes at that key -- by ETag or LastModified against the citation's own claim. **Classify: STILL-VALID / OVERWRITTEN / UNDECIDABLE.** The UNDECIDABLE count is as important as the other two.
2. `i4_layers.py` -- **compare the two remedies with their owners and costs**: the WRITER changes so an archive key names the write (a timestamped or content-addressed key), or the CITATION GRAMMAR changes so an S3 object is always cited as `bucket/key@ETag`. Print who owns each, what each costs, and what each does NOT fix.
3. **Whichever the evidence supports, taken or filed with its owner** -- and if it is the citation grammar, this project's own live citations are re-stated in it. **STATE WHICH.**
4. `i4_no_write.sh` -- prove no S3 write and no derive: this cell reads the bucket and changes nothing in it.
5. The record `CG-s-44.dated-archive-key.result.md`, the instance, then the flip.
## ACCEPTANCE (v3 grammar)

<criterion id="I4-AC1" cell_refs="CG-s-44"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/i4_census.py</invocation><expect>TREE_READ=(MAIN|WORKTREE)[\s\S]*TREE_POSITIVE_CONTROL=(FIRED|N/A-MAIN-TREE)[\s\S]*CITATIONS_FOUND=([0-9]+) of ([1-9][0-9]*) file\(s\)[\s\S]*STILL_VALID=([0-9]+)[\s\S]*OVERWRITTEN=([0-9]+)[\s\S]*UNDECIDABLE=([0-9]+)</expect></criterion>
`I4-AC1` -- THE CITATIONS AT RISK ARE COUNTED, NOT ESTIMATED: every dated-snapshot citation in this project's record, classified against the live object, with the tree and the denominator printed. The UNDECIDABLE bucket is reported rather than folded into either other -- an unrecoverable referent is a different fact from a wrong one.

<criterion id="I4-AC2" cell_refs="CG-s-44"><invocation>timeout 120 python org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/i4_layers.py</invocation><expect>REMEDIES_COMPARED=2 of 2[\s\S]*OWNER_PER_REMEDY printed[\s\S]*COST_PER_REMEDY printed[\s\S]*WHAT_EACH_DOES_NOT_FIX printed[\s\S]*CHOSEN=(WRITER_KEY|CITATION_GRAMMAR|FILED)</expect></criterion>
`I4-AC2` -- BOTH REMEDIES COMPARED WITH THEIR OWNERS, THEIR COSTS AND THEIR LIMITS, before one is chosen. `WHAT_EACH_DOES_NOT_FIX` is the field that matters: a key grammar change does not recover already-lost bytes, and a citation grammar change does not stop the next overwrite.

<criterion id="I4-AC3" cell_refs="CG-s-44"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/i4_remedy.sh</invocation><expect>BRANCH=(TAKEN|FILED)[\s\S]*(REMEDY_LANDED printed[\s\S]*PROJECT_CITATIONS_RESTATED=([0-9]+)|BLOCKER printed[\s\S]*OWNER_NAMED printed)[\s\S]*ACTS_NOT_TO_TAKE printed</expect></criterion>
`I4-AC3` -- THE REMEDY IS TAKEN OR FILED WITH ITS OWNER, and either way the acts that must NOT be taken meanwhile are printed -- because the cheapest wrong move here is to 'fix' a dated key by writing to it. **Both branches pass.**

<criterion id="I4-AC4" cell_refs="CG-s-44"><invocation>timeout 120 bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/i4_no_write.sh</invocation><expect>S3_WRITES=0[\s\S]*ECS_RUN_TASK_CALLS=0[\s\S]*CODEBUILD_STARTS=0[\s\S]*TERRAFORM_APPLIES=0[\s\S]*S3_READS=([0-9]+) \(permitted\)[\s\S]*EGRESS_PROBE_CONTROL=FIRED</expect></criterion>
`I4-AC4` -- READS ONLY, AND THE READS COUNTED: this cell investigates an overwrite and must not perform one. The permitted reads print as a non-zero count so that having looked is distinguishable from not having looked.

<criterion id="I4-AC5" cell_refs="CG-s-44" judgment="true"/> `I4-AC5` -- THE READING: whether a key grammar that reads immutable and is not is a naming bug or a storage-design decision nobody wrote down; whether an unversioned bucket holding an ARCHIVE is defensible; and what an estate should require of a citation before it is allowed into a record that later rounds will lean on. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>I4-AC1, I4-AC2, I4-AC3, I4-AC4, I4-AC5</expected_criteria>

<proof_of_spec>
Criterion ids: `I4-AC1`..`I4-AC5`. Instance at `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> I4-AC1,I4-AC2,I4-AC3,I4-AC4,I4-AC5` BEFORE the flip; rc 0 AND every mechanical row PASS. `I4-AC5` is `judgment="true"`: `UNVERIFIABLE-BY-INSTRUMENT`, `status_reason` naming `3.0.0_SA_CVO`; **`PASS`/`FAIL` on it is INVALID.** Two commits at the flip (the acts, then the instance + the status). A VALID instance is not a met order: if any mechanical row reads FAIL, the order STAYS OPEN, `<status>` is NOT flipped, and you report -- a worker that flips a terminal status while carrying a FAIL withdraws its own `<paths>` grant, because the grant is read from an order NON-TERMINAL at HEAD.
</proof_of_spec>

## SURFACES

`s3://opal-313476888478-globgrph/snapshots/**` (READ ONLY -- `head-object`, `list-object-versions`, `get-bucket-versioning`) - this project's own records under `org/missions/D0/NFRA/NFRA_CLDGRPH/` (READ; re-stated only on the citation-grammar branch) - the producer that writes the archive key (READ; edit only on the writer branch) - rows W1-S43, W2-S61, W2-S75 (READ).

## BOUNDS

- ⛔ **NO S3 WRITE, FOR ANY REASON.** A cell investigating an overwrite that performs one is the whole failure.
- ⛔ **DO NOT re-date, move or copy an existing archive object to 'preserve' it.** That is a write, it changes the evidence, and the lost bytes are already unrecoverable.
- **No alert, monitor or freshness surface** (standing moratorium).
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-I-4.dated-archive-key-is-a-mutable-pointer.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.12 (the round-9 recut), cell CG-s-44 (s.1a).
<owned_cells>CG-s-44</owned_cells>
Read-dependencies, NOT claimed: CG-s-37 (TO-CG-H-2, whose census read the surviving bytes and whose row W1-S43 is this cell). CONCURRENT, NOT yours: CG-s-41 (slot ~1), CG-s-42/43 (slot ~2), CG-s-45 (slot ~4).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-09 15:3xZ at the round-5 recut (GATES ARMED 25) and unchanged since; the C3 moratoria bind BOUNDS, and the egress hold binds harder.
comp-iam: DECLARED-NOT-APPLICABLE -- this order performs no AWS write, no principal, policy or grant change. If a READ you need is refused by IAM, that is a finding and a row, never a reason to widen anything.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 (rc 0 @07288006e5); the L9 seat's compose is the deliverable's context.
comp-find: RUN at the cut by the issuer FROM THE MAIN TREE; the worker re-runs it inside its own criteria where a denominator is claimed, under the tree clause in the standing law.
</preflight>
