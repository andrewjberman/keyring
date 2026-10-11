# TO IRPT_ANLREQ.TO-AR-y-102 -- the composition-read function's map entry builds the LIVE digest with NO parity skip and every member pinned

<to_id>IRPT_ANLREQ.TO-AR-y-102</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the floor of an `infra/` path). NOTHING is uploaded, applied, planned or invoked by this order.
**Decomp cell:** `AR-y-102` (`decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it.
- **Every build here is `BUILD_ONLY=1` with `TMPDIR` set to a folder OUTSIDE the worktree.** Without `BUILD_ONLY=1` the build script
  UPLOADS: never run it so. Never set `BAU_PARITY_SKIP` in this order: making the build pass without it is the cell.

### THE CELL (`AR-y-102`, inlined)

*The map entry of `irpt-commentary-composition-read-lambda` builds the LIVE digest with NO parity skip and with every member pinned.*

Why. The function is LIVE at `CodeSha256` `DbvBUxTGlCsdG4htVOhbI4NBxBMNbmjD6BLpMGu2Yo4=`, built today from commit
`35044a21aaa7187ecd35fcb1ae564befeb4352cb` with `BAU_PARITY_SKIP=1` (the parity check OFF), because the check refuses the build:
its source folder `infra/aws/lambda/investor-reporting/reports/` holds files that are not in the entry's `files[]` (row
`IRPT_ANLREQ-D2-S34`). And four of the entry's sixteen members carry no `staged_from` row, so the build takes them from whatever
tree builds it: any merge to the trunk that touches one changes what a rebuild ships (rows S45, S53). The map's job is to reproduce
what is LIVE.

Edit ONE entry, `functions["irpt-commentary-composition-read-lambda"]` in `infra/aws/lambda/ci/lambda-source-map.json`, in two parts:

1. **`outside_package` (the parity check).** Read the build script's own description of the mechanism
   (`infra/aws/lambda/ci/build-and-upload.sh`, about lines 269-292 and 450-500) and how the report store's entry
   (`irpt-commentary-report-store` or whichever entry shares `source_dir` `.../reports`; cell `AR-y-33` did this) declares it.
   Declare, with a one-line reason each, exactly the files of the source folder that the check names as outside this function's
   package. A file is either a member or outside, never both; a name that does not exist is refused as stale. Do not add a file to
   `files[]`: the live package has sixteen members and must keep sixteen.
2. **Pins for the four unpinned members** -- `commentary_composition.py`, `composition.py`, `repository.py`, `retention.py`. Add one
   `staged_from` row for each, in exactly the form of the twelve rows already there (same keys), with `pin` =
   `35044a21aaa7187ecd35fcb1ae564befeb4352cb` and `sha256` = the sha256 of the bytes of `git show <pin>:<repo path>` (compute it
   from the bytes, in binary; never from the working file). For each, also record in your report whether the working file at your
   HEAD is byte-equal to the pinned blob (it may not be, later: that is what the pin is for).
3. Change no other key of the entry and no other entry. Keep the file's formatting (indent, key order, final newline) so the diff is
   only your lines; say how many lines the diff adds and removes.
4. Build with NO skip, twice: `BUILD_ONLY=1 TMPDIR=<outside> bash infra/aws/lambda/ci/build-and-upload.sh investor-reporting
   irpt-commentary-composition-read-lambda`. Both must print `BUILD_ONLY:` with `sha256=DbvBUxTGlCsdG4htVOhbI4NBxBMNbmjD6BLpMGu2Yo4=`.
   If the digest differs, do NOT adjust until it matches by trial: list the members of your build against the pinned blobs' hashes,
   find which member differs and why, and say so. If it cannot equal live with these pins, STOP and file a row.
5. **Negative control, reported, not committed:** change one byte of the working `repository.py` (uncommitted), build once, confirm
   the digest is STILL `DbvBUxTG...` (the pin, not the working file, is what ships), then restore the file by writing back the bytes
   of `git show HEAD:<path>` and confirm `git status --porcelain` shows it clean. Report both lines. If the digest MOVES, the pin
   does not bind: STOP and file a row.
6. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r10/COMPOSITION_READ_MAP_PINS.json`:
   `{"read_at": "<UTC>", "tree_head": "<short hash>", "outside_package": {"<file>": "<reason>", ...}, "pins": [{"packaged_as": "...",
   "repo_path": "...", "pin": "...", "sha256": "...", "working_file_equals_pin": true|false}, ...], "build": {"parity_skip": false,
   "sha256_first": "...", "sha256_second": "...", "members": <n>}, "negative_control": {"digest_with_one_byte_changed": "...",
   "restored_clean": true|false}, "diff_lines": {"added": <n>, "removed": <n>}}`. Commit the map and this record.

### ACCEPTANCE

<criterion id="AR102-y-AC1" cell_refs="AR-y-102"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r10/ar10_checks.py y102-build --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y102-BUILD-OK</expect></criterion>
`AR102-y-AC1`: no member of the entry is unpinned, the entry records the live digest, and a build with no parity skip prints it.

<expected_criteria>AR102-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else, the build script included (do NOT edit it).
- No live call of any kind: no AWS read, no upload, no plan, no apply, no invoke. No non-ASCII in what you add.

<paths>
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R10_Y.md</decomp_doc>
<owned_cells>AR-y-102</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR102-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-102.composition-read-builds-with-no-skip-and-all-pinned.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-102`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR102-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 map entry of 16 members (12 pinned rows, 4 unpinned, counted by the issuer's check at the base) and 20 lines of the build script naming the mechanism; NOT seen: which files of the source folder the parity check names (the worker reads the check's own output), and whether another entry shares these pins. comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the map is read at build time only, 1 reader (the build script). comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission change; nothing is applied.
comp-adversary: RUN -- by reading 1 entry against 1 live digest; the lens: a pin that does not bind (the build still takes the working file), or a digest matched by trial instead of by member bytes. The face orders a one-byte negative control for the first and forbids the second. NOT seen: the build script's staging code path for a member that is both in files[] and pinned in the function's own source folder.
lane: one map entry, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-10 analysis @57cdd1cdde, item 2 (row `IRPT_ANLREQ-D2-S34`; CTO msg 5241 condition 3).
  `AR102-y-AC1` base: FAIL as expected (4 members unpinned; the build with no skip prints PARTIAL, 0 built).
- One mechanical criterion; the negative control is a reported step of the cell, read by the issuer at the drain.
- `irpt-intake-poller`, the other function row S34 names, is not this cell: its refusal is a missing member file.
- Seating: slot ~53 is reused; its earlier order is terminal.
