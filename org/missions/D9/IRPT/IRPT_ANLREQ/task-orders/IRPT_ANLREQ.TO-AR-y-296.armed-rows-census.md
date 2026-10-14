# TO IRPT_ANLREQ.TO-AR-y-296.armed-rows-census -- READ every ARMED row the issuer owns and say, with evidence, which are resolved on the trunk and which still stand

<to_id>IRPT_ANLREQ.TO-AR-y-296</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~114</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>29</round>
<workstream>YT</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-296` (`decompositions/IRPT_ANLREQ_DECOMP_R29A_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~114`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-114` (branch `wk-IRPT_ANLREQ-114`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~114 <0.9.0_WK_IRPT_ANLREQ~114@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W114-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-296`, inlined) -- READ. Nothing is changed or called. The output is a verdict list the issuer adjudicates; you file no row that disarms anything.

*The L10 slug may be sent only after every BLOCKING or ARMED row is dispositioned (CLAUDE.md rule 27). The surprise channel `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` holds about 320 rows; 32 are ARMED with `disarm_owner` `2.0.0_SA_COO~Y2`, and 10 of those are named by a later row whose `one_line` says `DISARMS`, which leaves 22 (the issuer's own count, by a parse of the JSON blocks: `hazard_standing` equal to `ARMED`, `disarm_owner` containing `Y2`, the row id not named in the `one_line` of any later row that contains `DISARMS`). Many were raised mid-round and answered by a later cell (for example the serving path's missing price date, row `W75-S1`, was answered by `AR-y-245`; the calendar row `W77-S3` by the same cell's calendar member). Each one needs a verdict with proof so the issuer can write one disarm row per resolved item and carry only the true remainder to the CVO.*

1. **Compute the list yourself, from the file, and print its denominator.** Parse every fenced ```json block of the channel file. A row is ARMED-OWNED when `hazard_standing` is `ARMED` and `disarm_owner` contains `Y2`. Remove every row whose id appears in the `one_line` of a LATER row (a row further down the file) whose `one_line` starts with `DISARMS` or contains the word `DISARMS` (read each such row; print the ids it disarms). Print: rows parsed, rows ARMED-OWNED, rows already disarmed, rows left. The issuer's counts are 320 rows parsed, 32 ARMED-OWNED, 22 left; a different count is a finding (say which rows differ and why).
2. **For each row left, one verdict** with its evidence, in this vocabulary only: `RESOLVED` (a commit, a cell or a record on the trunk makes the hazard impossible or answers the question; name the commit sha or the record path and line, and run or read the check that shows it), `STILL_ARMED` (the hazard stands today; say what would disarm it and which seat or cell can do that), or `UNCLEAR` (you could not decide from the repository alone; say what would settle it). A row about a LIVE state (a deployed package, a stored object, a queue message) is `RESOLVED` only on a record or a read-only live read that shows it now (`aws ... get/describe/list` through the `.tools/aws` shim is permitted); a code change on the trunk does not resolve a hazard that sits in the live world. `ABSENT != EXERCISED-AGAINST`: write what you read, and say when you did not read the live world. Never resolve a row because it is old.
3. **Group the verdicts** by the thing that resolved them (a cell, a release, a ruling) so the issuer can write one disarm row per group: `groups` (objects: `resolved_by`, `rows`, `proof`).
4. **Write `r29/ARMED_ROWS_CENSUS.json`:** `denominator` (rows parsed, ARMED-OWNED, already disarmed with their disarming rows, left), `rows` (objects: `id`, `one_line` (first 120 characters), `verdict`, `evidence` (list of strings with a path or sha), `would_disarm` (for `STILL_ARMED` and `UNCLEAR`)), `groups`, `claim`, `not_read`.
5. **In your report:** the denominator, the number of rows in each verdict, the groups, and the `STILL_ARMED` and `UNCLEAR` rows by id with one line each.

### ACCEPTANCE

<criterion id="AR296-y-AC1" cell_refs="AR-y-296"><invocation>python C:/dev/wk-irpt-anlreq-114/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y296-armed --root C:/dev/wk-irpt-anlreq-114</invocation><expect>Y296-ARMED-OK</expect></criterion>
`AR296-y-AC1`: the record prints the denominator (rows parsed, ARMED-OWNED, already disarmed, left), carries exactly one verdict from the vocabulary for every row left that the checker's own parse finds, and every RESOLVED verdict names evidence.

<criterion id="AR296-y-AC2J" cell_refs="AR-y-296" judgment="true"/>
`AR296-y-AC2J` (judgment, graded at L9, never by you): each RESOLVED verdict rests on a commit, a record or a read that shows the hazard gone (a live-world hazard is resolved only by a live read or a record of one), no row is resolved for being old, and the STILL_ARMED and UNCLEAR rows name what would disarm them.

<expected_criteria>AR296-y-AC1 AR296-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~114/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R29A_Y.md</decomp_doc>
<owned_cells>AR-y-296</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~114/IRPT_ANLREQ.TO-AR-y-296.armed-rows-census.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-296`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR296-y-AC1,AR296-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- READ-only: the channel file, the trunk's history and records, and (where a row is about a live state) read-only live AWS get/describe/list calls; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the one-line text of three of the 32 rows (W75-S1, W77-S3, W109-S2) against the cells that answered them; the lens: a hazard that sits in the live world marked resolved because a trunk commit exists, a row resolved for being old. The order requires a live read or a record of one for any live-state row and names the vocabulary. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut so the L10 slug can be sent (every ARMED row dispositioned) as workstream `YT` round 29. The issuer adjudicates the verdicts and files the disarm rows. Base: `AR296-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
