# TO IRPT_ANLREQ.TO-AR-y-197.resident-four-members-read -- the issuer's four members of the resident delta read for the pair

<to_id>IRPT_ANLREQ.TO-AR-y-197</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~54</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-197` (`decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~54`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-54` (branch `wk-IRPT_ANLREQ-54`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~54 <0.9.0_WK_IRPT_ANLREQ~54@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W54-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-197`, inlined) -- READ. Nothing is changed or called.

*The issuer's four members of the resident delta, read for the pair.* The CTO (section 4 point 2): `2.0.0_SA_COO~Y2` reads its own three members and IRPT_YCDGEN's one.

**Read first:** `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~55/r19/RESIDENT_PACKAGE_DELTA.json` (`differing`, `other_differing_by_owner`, `attribution`), `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 4, and for each member the two blobs: the live pin `0485393f3a` and the release pin `069b8f797e` (`git -C C:/dev/ajb_workspace show <pin>:infra/aws/lambda/investor-reporting/<member>`).
The four members: `_authz/served.py`, `infra/logic/registry/name_rulings.json`, `ops/status.py` (owner IRPT_ANLREQ) and `ycharts/generate/resident_worker.py` (owner IRPT_YCDGEN).

For EACH of the four, write an object in `members` with:
1. `old_blob`, `new_blob` (git blob hashes at the two pins) and `commits` (every commit in `0485393f3a..069b8f797e` that touched it: hash, subject, project/order).
2. `resident_use`: whether and how the RESIDENT uses the member -- trace the imports from the resident's entry point (`ycharts/generate/resident_main.py` / `resident_installed.py` / `resident_worker.py` and what they import) to the member, and cite file:line. For `_authz/served.py` say specifically whether the resident calls `Entry.handle` or `Entry._internal_allowed_firms` (the status rule, AR-y-172, and the caller-class log line, AR-y-184, are in this file at the release pin) or only imports other names from it; if the resident never reaches the changed code, say so with the evidence. For `ops/status.py` say which functions the resident imports and what changed in them.
3. `behaviour_change`: what the resident does differently with the new bytes, in plain words, for each changed function the resident reaches; or `NONE REACHED` with the trace that shows it.
4. `risk_note`: anything in the diff the pair should name (a new import, a new environment read, a new AWS call, a changed default).
Then `claim` and `not_read` (the host's installed copy and the resident's real runtime path are not read).

**Write `r19/RESIDENT_FOUR_MEMBERS_READ.json`** with `members` (the four objects), `claim`, `not_read`. **In your report:** per member, the behaviour change and whether the resident reaches the changed code; in particular whether the status rule and the log line reach the resident at all.

### ACCEPTANCE

<criterion id="AR197-y-AC1" cell_refs="AR-y-197"><invocation>python C:/dev/wk-irpt-anlreq-54/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y197-four --root C:/dev/wk-irpt-anlreq-54</invocation><expect>Y197-FOUR-OK</expect></criterion>
`AR197-y-AC1`: the record has the four members, each with its old and new blob, its commits, the resident's use of it and the change in behaviour.

<criterion id="AR197-y-AC2J" cell_refs="AR-y-197" judgment="true"/>
`AR197-y-AC2J` (judgment, graded at L9, never by you): each resident-use claim is traced from the resident's entry point with file:line, and a member the resident does not reach is shown not reached rather than assumed.

<expected_criteria>AR197-y-AC1 AR197-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19R2_Y.md</decomp_doc>
<owned_cells>AR-y-197</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~54/IRPT_ANLREQ.TO-AR-y-197.resident-four-members-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-197`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of the repository; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (section 4 point 2) against the cell; the lens: a member declared harmless because it was not read through the resident's imports. The order requires the import trace with file:line. NOT seen: the host's installed copy (0 host files read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis section 4 point 2. Base: `AR197-y-AC1` FAIL as expected (no record).
