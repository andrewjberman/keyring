# TO IRPT_ANLREQ.TO-AR-y-192.ycharts-generate-release-census -- the release census of irpt-ycharts-generate and the resident (S33, W53-S9)

<to_id>IRPT_ANLREQ.TO-AR-y-192</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>19</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-192` (`decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-192`, inlined) -- READ. Nothing is changed or called.

*The release census of `irpt-ycharts-generate` and of the resident:* what moving the reader means, member by member, so the release moves the reader and nothing else.

**Read first:** row `IRPT_ANLREQ-D2-W53-S9` and `IRPT_ANLREQ-D2-W52-S28` in `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md`, the AR-y-145 release census `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/UPLOAD_DOOR_RELEASE_CENSUS.json`, the CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_19_20261013.md` section 1, and `infra/aws/lambda/ci/lambda-source-map.json` (the `irpt-ycharts-generate` entry: `source_dir`, `files`, `staged_from` with each member's `pin`, `packaged_as`, `sha256`, its long notes, `artifact_sha256`, `deployed_code_sha256`).
How an earlier release was done (read it as a pattern, not to repeat it): `org/critical_paths/change_management/20261012T1340Z_advi-firmbkts-fb-f-11-act4-irpt-leg-20261012_deploy_completion.md` (build-and-upload, scoped plan, safe-apply, before/after samples, the source-map record).

1. **The map's members.** List every `staged_from` row of `irpt-ycharts-generate`: member, pin, `packaged_as`. Mark the ones the READER RELEASE must move (the upload door and reader: at least `uploads.py`, `template_reader.py`, and any member their head versions import that the pinned versions do not, found by comparing the head's import closure with the pins) and the ones it must NOT.
2. **The four native unpinned members** (row W53-S9: `acceptance.py`, `submission.py` from IB-pr-455 `74bbdbb322`; `submission_service.py` from AR-y-37 `2f7cc7be42`; `durable_job.py` from TO-AR-g-21 `3acafb3f45`): for each, the commit the map pins it to or states it is native at, the head blob hash, and which commit's blob the LIVE package carries if the map or a deploy record says (`deployed_code_sha256`, the ledger's priors). Say what is KNOWN and what only the live package can tell (the executor reads it). Give the PLANNED pin move: pin each to the commit whose blob equals the live bytes, so the release moves exactly the reader members.
3. **The resident.** Find and state: the rule that builds the resident package (`one backend pin over whole folders`), its CURRENT pin (the compile named `0485393f3a` as the resident's pin and `st32`), the builder script, the deploy path (how and by which seat it reaches the host `i-0167fd745ad906a66`), whether the head's `uploads.py` and `template_reader.py` are in the resident's folders, and the OWNING LANE (which COO lane releases resident packages; read the round-14/15 compile and rows S5/S6 and the worktrees `rel-resident-r5`). Do NOT guess an owner: name what you read.
4. **Write `r19/YCHARTS_GENERATE_RELEASE_CENSUS.json`:** `map_entry_members` (list of objects: `member`, `pin`, `packaged_as`, `moves_in_this_release`), `native_unpinned_members` (objects with `member`, `pinned_or_native_at`, `head_blob`, `live_commit_if_known`), `planned_pin_moves` (objects with `member`, `from_pin`, `to_pin`), `members_that_move` (list of member names), `resident` (object with `pin_rule`, `current_pin`, `builder`, `deploy_path`, `owner_lane`), `claim`, `not_read`.
5. **In your report:** the members that must move and the pins that must be set; what the release cannot know without the live package; the resident's owner and path; any member the planned moves would change as a side effect.

### ACCEPTANCE

<criterion id="AR192-y-AC1" cell_refs="AR-y-192"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r19/ar19_checks.py y192-census --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y192-CENSUS-OK</expect></criterion>
`AR192-y-AC1`: the record names the map members, the four native unpinned members, the planned pin moves, the members that move and the resident's pin rule, current pin, builder, deploy path and owner lane.

<criterion id="AR192-y-AC2J" cell_refs="AR-y-192" judgment="true"/>
`AR192-y-AC2J` (judgment, graded at L9, never by you): each pin and hash was read from the repository rather than assumed, the planned moves change only the reader members, and what only the live package can tell is said to be unknown.

<expected_criteria>AR192-y-AC1 AR192-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R19_Y.md</decomp_doc>
<owned_cells>AR-y-192</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-192.ycharts-generate-release-census.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-192`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of the repository; nothing is changed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading row W53-S9 (four native members differ from live and ship on any rebuild) against the cell; the lens: a planned pin move that changes a member nobody meant to ship. The order requires the planned moves and a statement of what only the live package can tell. NOT seen: the live package and the resident host (0 live objects read).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-19 analysis item 1. Base: `AR192-y-AC1` FAIL as expected (no record).
