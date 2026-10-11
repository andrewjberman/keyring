# TO TCKT_VNEXT.TO-R3-pc1 -- the clamp precheck decides the ticket host from the deploy record and the deployed content, not a typed list

<to_id>TCKT_VNEXT.TO-R3-pc1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~13</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** WORLD by path floor (its `<paths>` names `infra/` files it only reads); nothing is
applied and nothing runs against AWS | **Decomp cell:** `R3-pc-1` (`decompositions/TCKT_VNEXT_DECOMP_R3.md`) | **outcome_ref:** FWD-1
(the run's precheck) | **depends_on:** none for the build

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~13`. Your worktree is `C:/tmp/tckt-r3-13` (cut from box/dell2 at the issuance commit). Work and commit
only there, with
`bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~13 <0.9.0_WK_TCKT_VNEXT~13@opal.agent>" -F <msgfile> -- <paths>`. Write the
message file with the Write tool. If a `portal` folder exists in the worktree it is a separate repository: never touch or stage it.

### WHY

Before a live test run, a precheck confirms that the "firm clamp" is live on 27 portal routes across 8 Lambda functions. The current
instrument is `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/reread_27.py` (80 lines; read it first). For the
seven Investor Reporting hosts it checks that the deployed `served.py` hashes to one of a small set of signed release builds. For the
eighth host, `opal-ticket-api`, it checks the deployed `lambda_function.py` against `TICKET_OK`, a HAND-TYPED set of file hashes.
Every correct, signed deploy of that function therefore makes the precheck refuse until someone types a new hash in; that stopped a
run on 2026-10-11 (row TCKT_VNEXT-D2-S28).

### THE CELL `R3-pc-1`

Build a NEW instrument in the NEW folder
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/clamp_precheck/`:
`clamp_precheck.py` and `test_clamp_precheck.py`. Do not edit `reread_27.py`.

1. **Importable with no side effect, every outside read replaceable.** The AWS read of a function (configuration + package
   download), the git read of a file at a commit, and the source-map read are three functions a test can replace. `import
   clamp_precheck` makes no AWS call, no network call and no git call.
2. **Same routes, same output shape.** The route table comes from the same census file `reread_27.py` reads
   (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json`, the rows where any token's verdict
   is `MORE_THAN_ONE`). One line per host, then `READ27 <clamped>/<total>`; exit 0 only when every route is clamped. Write the
   table as JSON to a path given by a REQUIRED `--out` argument (nothing is written beside the script).
3. **The seven Investor Reporting hosts: unchanged rule.** The deployed `served.py` must hash to a member of the release set, copied
   from `reread_27.py`'s `SERVED_RELEASES` with its labels. (That set is the other project's signed release list; replacing it is
   not this cell.)
4. **`opal-ticket-api`: decided by the deploy record and the content, with NO typed list of builds.** Read the function's entry in
   `infra/aws/lambda/ci/lambda-source-map.json` (path overridable by `--source-map`): `artifact_sha256`, `last_deployed_commit`,
   `source_dir`, `files`. The host is CLAMPED only when ALL of these hold; each failure has its own named verdict on the host's
   line, and the host then counts as not clamped:
   - `MAP-STALE`: the live `CodeSha256` is not the map's `artifact_sha256`. (The record does not describe what is running.)
   - `NOT-THE-RECORDED-FILE`: the deployed `lambda_function.py`'s sha256 is not the sha256 of
     `git show <last_deployed_commit>:<source_dir>/lambda_function.py`. (Deployed bytes are compared with the build input by
     CONTENT, never by commit ancestry.)
   - `CLAMP-ABSENT`: read the DEPLOYED member's source with `ast` (do not import or execute it) and require both: the three
     helpers `_profile_scope`, `_resolve_scope` and `_in_profile_scope` are each defined as a function; and each of the seven
     route handlers `create_ticket`, `list_tickets`, `metrics`, `get_ticket`, `claim_ticket`, `complete_ticket`, `report_ticket`
     calls at least one of those helpers, directly or through `_firm_allowed` / `_create_firm_allowed` (a helper that itself calls
     one of the three). Read `infra/aws/lambda/ticket_center/lambda_function.py` at HEAD to confirm these names and how the clamp
     is reached before you fix the rule; if a handler reaches the clamp by a route this rule would miss, state it in your report
     and encode what the code does, not what this face guesses. The verdict names the helper or handler that failed.
   - `UNREADABLE`: the function, its package, the map entry or the commit's file could not be read. Never counted as clamped.
5. No `TICKET_OK` and no other set of allowed ticket builds anywhere in `clamp_precheck.py`.
6. No client data in any file; no non-ASCII; make NO AWS call and NO network call (the tests use fakes: a fake function answer, a
   zip built in memory, a fake map, a fake git reader).

### ACCEPTANCE

<criterion id="R3-pc1-AC1" cell_refs="R3-pc-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py pc-rules</invocation><expect>PC-RULES-OK</expect></criterion>
`R3-pc1-AC1`: tests `test_map_live_and_commit_agree_and_clamp_present_is_clamped`,
`test_live_build_not_the_maps_is_map_stale_and_not_clamped`, `test_member_not_the_recorded_commits_file_is_refused`,
`test_a_clamp_helper_removed_is_not_clamped`, `test_a_route_handler_that_stops_calling_the_clamp_is_not_clamped` exist and pass, and
the source carries no `TICKET_OK`.

<criterion id="R3-pc1-AC2" cell_refs="R3-pc-1"><invocation>python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py pc-hosts</invocation><expect>PC-HOSTS-OK</expect></criterion>
`R3-pc1-AC2`: tests `test_irpt_host_on_a_release_build_is_clamped`, `test_irpt_host_off_the_release_set_is_not_released`,
`test_unreadable_host_is_named_and_the_total_is_not_full`, `test_exit_zero_only_when_every_route_is_clamped` exist and pass.

<expected_criteria>R3-pc1-AC1 R3-pc1-AC2</expected_criteria>

Dry-run at base: both FAIL (absent), as expected.

## BOUNDS

- **Grant:** the `<paths>` block and this order's file (status flip only). You write ONLY inside your `clamp_precheck/` folder and
  the investigation file; every other path in the block is read-only for you.
- Make no AWS call, no network call, no deploy. Do not edit `reread_27.py`, the source map, or anything under `infra/`.
- A row, if you need one: append it in BINARY mode as `TCKT_VNEXT-D2-W13-S<k>`, its own fenced block at the end of the investigation
  file, keeping the file's line endings; `surfaced_at` = `date -u +%FT%TZ` at filing. Never weaken a test.
- The proof check takes criterion ids COMMA-separated. Do not write report or markdown summary files; findings go in your report.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R3_CHECKS/r3_checks.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R1_RUN/reread_27.py
org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~6/SA_ROUTE_CENSUS.json
infra/aws/lambda/ci/lambda-source-map.json
infra/aws/lambda/ticket_center/lambda_function.py
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R3.md</decomp_doc> (round 3), cell `R3-pc-1`.
<owned_cells>R3-pc-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R3-pc1-AC1 R3-pc1-AC2. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~13/TCKT_VNEXT.TO-R3-pc1.clamp-precheck-reads-the-source-map.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> R3-pc1-AC1,R3-pc1-AC2` before the flip.
</proof_of_spec>

**REPORT (once):** each check line verbatim, the commits, how each of the seven handlers reaches the clamp in the HEAD handler (file
and line), the exact rule you encoded for `CLAMP-ABSENT`, the committed blob's sha256 of `clamp_precheck.py` (from
`git show HEAD:<path> | sha256sum`), and any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE (no schedule).
comp-iam: DECLARED-NOT-APPLICABLE (no IAM change; nothing runs against AWS in this cell).
comp-adversary: DECLARED-NOT-APPLICABLE (nothing is applied in this cell). The adversarial arms are the four refusal tests on the face.
</preflight>

Source: CTO round-3 analysis @f1c513af8e section 3 item 4; rows TCKT_VNEXT-D2-S28 and D2-S25. The live read of this instrument
needs the deploy record of cell `R3-sm-1`; the issuer runs it live at the drain.
