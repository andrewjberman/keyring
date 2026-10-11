# TO IRPT_ANLREQ.TO-AR-y-103 -- the census for release 5's return: a proposed one-pin irpt-status entry, built twice, diffed against live, each served change with its portal reader

<to_id>IRPT_ANLREQ.TO-AR-y-103</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (one live single-resource read of a function's package). NOTHING is uploaded, applied, planned or invoked, and the source map is NOT changed.
**Decomp cell:** `AR-y-103` (`decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it.
- **Every build here is `BUILD_ONLY=1` with `TMPDIR` set to a folder OUTSIDE the worktree, and with NO `BAU_PARITY_SKIP`.** Without
  `BUILD_ONLY=1` the build script UPLOADS: never run it so.
- **You never COMMIT a change to `infra/aws/lambda/ci/lambda-source-map.json`.** The map on the trunk must keep building what is LIVE
  until the release itself. Your one-pin entry is a deliverable file.

### THE CELL (`AR-y-103`, inlined)

*The census for release 5's return.*

Why. `irpt-status` is LIVE at `CodeSha256` `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=` (revision 6), and the map's entry is pinned,
member by member, at three different commits so that it builds exactly that. A release built this morning from one tree was rolled
back after 61 minutes: it changed a served answer that a portal reader on PROD admits by an exact key set, and the release's record
had counted no portal reader. The return will be built from ONE tree again, and it now also carries round 7's ticket binding
(`AR-y-71`, merged at `31d02ad19c`: the report read takes an optional `ticket_id` and can refuse `REPORT_TICKET_MISMATCH`). The pair
that authorises it is written on THIS census. The census's job is to name every member that moves and, for each one that changes
what a caller is served, the portal code that reads that answer.

1. **The pin.** `P` = `git rev-parse HEAD` of your worktree at start. Confirm `git merge-base --is-ancestor 31d02ad19c P` (rc 0) and
   print a positive control beside it. Record `P` (full hash).
2. **The proposed entry**, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r10/IRPT_STATUS_ENTRY_ONE_PIN.json`:
   a copy of `functions["irpt-status"]` from `infra/aws/lambda/ci/lambda-source-map.json` in which EVERY member of `files[]` has a
   `staged_from` row (same keys as the existing rows) with `pin` = `P` and `sha256` = the sha256 of the bytes of
   `git show P:<repo path>` (binary; never the working file). No other key changes. Leave `artifact_sha256` and the deployed fields
   as they are: they record what is live.
3. **The build, twice.** Save the map's bytes; write your proposed entry into the worktree's map (UNCOMMITTED); run
   `BUILD_ONLY=1 TMPDIR=<outside> bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting irpt-status` twice; the two
   `BUILD_ONLY:` digests must be equal. Then RESTORE the map by writing back the saved bytes and confirm
   `git status --porcelain -- infra/aws/lambda/ci/lambda-source-map.json` prints nothing. Keep the built zip (outside the worktree)
   for step 5. If the build refuses (parity or anything else), report the refusal's lines and STOP: do not add a skip.
4. **The live package.** `.tools/aws lambda get-function --function-name irpt-status` returns a `Code.Location` link. Use it ONCE, in
   the same command, to download the zip into a temp folder OUTSIDE the worktree; NEVER print, log, write or report the link. Its
   `Configuration.CodeSha256` must be the digest above and the downloaded file's base64 sha256 must equal it; if either differs, STOP
   and say what you read (the live function moved). Hash every member (sha256 hex). Delete both zips when you are done.
5. **The diff.** Members whose bytes differ between your build and the live zip (`changed_members_vs_live`), members only in the
   build (`added`), members only in live (`removed`).
6. **One row per changed member** (`moved_members`). The record of this morning's release,
   `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/release5/REPIN_CENSUS_IRPT_STATUS.json`, has a row for most
   of them: start from it, but RE-READ each diff yourself (the live side is the same; the build side has moved since) and write
   what you read. Each row: `packaged_as`, `repo_path`, `owning_commits` (`<short hash> <author>` for every commit between the
   member's old pin and `P` that touched it: `git log --format='%h %an' <old pin>..P -- <repo path>`), `served_effect` =
   `CHANGES_SERVED_ANSWER` (a caller of any route of this function can be served different bytes, a different status, a different
   key set or a different refusal) or `INERT`, `why` (two sentences with file and line), `claim` (`measured` if you ran or parsed
   something that shows it, `inferred` if you reasoned it from reading).
7. **For every `CHANGES_SERVED_ANSWER` row, two more members -- this is the half this morning's record lacked:**
   - `after_read`: one read a seat can make after the release that shows the change (the route, what to send, what comes back
     differently from today). Words only; no id of a real request, no client name, no figure.
   - `portal_reader`: the portal code that reads that answer. Read it in the portal repository WITHOUT changing any worktree:
     `git -C C:/dev/wk-irpt-anlreq-51/portal show origin/PROD:<path>` and `... show origin/DEV:<path>` (another worker is editing that
     worktree's files: read refs only, never the working files, never check anything out). Name `file:function` on each of PROD and
     DEV, and for each say `admits_new_shape: true|false` with the line that decides it (an exact key-set check, a closed list of
     reason codes, a status switch). `origin/PROD` is `37aa1247ee` and `origin/DEV` is `9ca634c6` at this cut; record what you read.
     Start from `src/pages/InvestorReporting/contracts/owned-requests.ts` (`readOwnedHistory`, `readOwnedRequest`: exact key sets),
     `src/pages/InvestorReporting/render/Page.tsx` (`CONTRACT_NAMED_REASON_CODES`) and `src/pages/TicketCenter/analysisRequest.ts`;
     search the tree at each ref for any other reader of the route (`git -C <portal> grep -n <term> origin/PROD -- src`), and say
     what you searched for. If you find NO portal reader for a served change, write `portal_reader: {"found": false, "searched": "..."}`:
     a zero must say what it looked through.
8. **Write the census**, `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r10/RETURN_CENSUS_IRPT_STATUS.json`:
   `{"read_at": "<UTC>", "pin": "<P>", "carries_ar_y_71": true, "live": {"code_sha256": "...", "last_modified": "...",
   "member_count": <n>}, "build": {"parity_skip": false, "sha256_first": "...", "sha256_second": "...", "bytes": <n>, "members": <n>,
   "changed_members_vs_live": [...], "added": [...], "removed": [...]}, "moved_members": [ ...rows of steps 6 and 7... ],
   "portal_refs_read": {"PROD": "<hash>", "DEV": "<hash>"}, "prod_must_carry_first": ["<portal file: what, and the DEV commit that
   has it>", ...], "map_unchanged": true}`. `prod_must_carry_first` lists every portal change that must be on PROD BEFORE this build
   is released because PROD's reader does not admit the new shape. Commit the proposed entry and the census (never the map).

### ACCEPTANCE

<criterion id="AR103-y-AC1" cell_refs="AR-y-103"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r10/ar10_checks.py y103-census --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y103-CENSUS-OK</expect></criterion>
`AR103-y-AC1`: the map is untouched and still records the live digest; the proposed entry has every member at one pin; the census
holds two equal digests built with no skip, the live digest, and one complete row per member that differs from live, each served
change with its after-read and its portal reader. It grades the record's form: it cannot see whether a row's reading is right.

<criterion id="AR103-y-AC2" cell_refs="AR-y-103" judgment="true"/>
`AR103-y-AC2` (judgment, graded at L9, never by you): every `CHANGES_SERVED_ANSWER` row names the portal reader that actually decides
whether PROD admits the new answer, and no member read `INERT` changes what a caller is served.

<expected_criteria>AR103-y-AC1 AR103-y-AC2</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else. The source map is edited ONLY uncommitted for the two builds and restored; the build script is not edited.
- Live: exactly ONE `get-function` on `irpt-status` and the one download it enables. No list call, no invoke, no upload, no plan, no
  apply. The signed link is never printed, logged, written or reported. No non-ASCII in what you add.
- The portal repository at `C:/dev/wk-irpt-anlreq-51/portal`: `git show` and `git grep` against `origin/PROD` and `origin/DEV` only.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md</decomp_doc>
<owned_cells>AR-y-103</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR103-y-AC1 AR103-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-103.irpt-status-return-census-one-pin.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-103`. `AR103-y-AC2` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason`
naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR103-y-AC1,AR103-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 map entry of 49 members pinned at 3 distinct commits (counted by the issuer) and this morning's census of the same function (1 record); NOT seen: which members differ from live at today's head (the worker measures it), and the portal readers on PROD (the worker reads them at the ref). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of the deliverables. comp-iam: RUN -- by reading 1 earlier order of this lane (TO-AR-y-91): the dell2 identity made the same single-function get-function read today; no permission is changed.
comp-adversary: RUN -- by reading 1 rollback record (release 5, 61 minutes) against this face; the lens: a served change counted with no portal reader, or a zero that does not say what it searched. The face makes the portal reader a required member of every served row and a not-found carry its search. NOT seen: readers of these routes outside the portal repository.
lane: the worker's deliverables; read-only on the world and on the map.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-10 analysis @57cdd1cdde, item 3 ("the pair for release 5's return, WRITTEN and held") and item 2.3 (one
  pair whose census lists release 5's members and the binding's three files together). `AR103-y-AC1` base: FAIL as expected (no
  proposed entry, no census).
- The pair (COO half) and the apply order are the issuer's, written on this census and HELD until portal PROD carries what
  `prod_must_carry_first` lists.
- Seating: slot ~52 is reused; its earlier order is terminal.
