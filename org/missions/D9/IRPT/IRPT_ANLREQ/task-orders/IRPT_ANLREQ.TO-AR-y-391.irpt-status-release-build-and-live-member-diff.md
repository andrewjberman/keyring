# TO IRPT_ANLREQ.TO-AR-y-391.irpt-status-release-build-and-live-member-diff -- BUILD ONLY: the irpt-status package built twice at a named pin with the repository's own builder, and its members diffed one by one against the recorded live zip, every mover named with the commits that moved it and acceptance.py shown to carry get_commentary_ref; nothing uploaded, planned or applied

<to_id>IRPT_ANLREQ.TO-AR-y-391</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~290</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ52</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD (the class the `<paths>` imply: a Lambda package build for a served function; the worker builds only, uploads and applies nothing)
**Decomp cell:** `AR-y-391` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the ticket's commentary PDF opens) | **depends_on:** none (pin `faf037e0d02c021c0717f051b01ec72ed0b063d2`)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~290`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-290` (branch `wk-IRPT_ANLREQ-290`), provisioned by the issuer (sparse: `.tools/`, `lib/`, `infra/`, `data/`, `docs/`, `org/standards/` and the project folder). First confirm `org/` and `.tools/` exist in it. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~290 <0.9.0_WK_IRPT_ANLREQ~290@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. A row id has the form `IRPT_ANLREQ-D2-W290-S<k>` (check the channel file for `W290` first); `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `INVESTIGATION_v1.md` (0 deletions). Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- **BUILD ONLY.** No upload, no plan, no apply, no invoke, no AWS call of any kind, no network, no push, no change under `infra/`. The stage folder is OUTSIDE the repository. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-y-391`, inlined)

*Context. Andrew's own ticket's commentary PDF cannot be opened through the ticket page: the LIVE irpt-status package (CodeSha256 `+TcZDWmwE7uv3sUwos2+jn1lbKyQikK+13nNBzD6q4A=`, release 35, 49 members, built at pin `90b69dcb12cdfedc786966ab33d034bf14229396`) packages `acceptance.py` at the zip root without `get_commentary_ref`, so `ops/owned_report.py` (lines 350 to 373) refuses `COMMENTARY_PDF_NOT_RETAINED`. The CTO (msg 10600) authorized a new irpt-status release: build the bundle from the function map, print the member list and diff it member by member against the live zip, name every mover (acceptance.py must carry `get_commentary_ref`; any other mover must be justified). The issuer recorded the live zip's member names and sha256 at `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json` (read-only live read; keys `code_sha256`, `member_count`, `members` as a list of `{name, size, sha256}`). The issuer's release-35 build tool, `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r35/r35l_build.py`, builds `irpt-status` TWICE at a pin with the repository's own builder (`BUILD_ONLY=1`, nothing uploaded), refuses unless the two zips are byte-identical, compares the members with the offline census build, and writes a record (key `functions.irpt-status` holding `zip`, `zip_sha256`, `code_sha256`, `bytes`, `members`, `member_sha256`, `delta_vs_deployed_commit`). You run it; you do not edit it.*

1. **Pin and folders.** Print `git rev-parse faf037e0d0` (it must equal `faf037e0d02c021c0717f051b01ec72ed0b063d2`; if not, STOP and file a row). Create `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49` first. The stage folder `C:/dev/irpt-release-r36s` must not exist.
2. **Run the build tool** from the worktree root (about two minutes; command `timeout` 590000 ms; if it is killed or fails for a reason that is not an `R35L-BUILD-BAD` line, run it ONCE more with a new absent `--out` such as `C:/dev/irpt-release-r36sb`, and use that folder after): `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r35/r35l_build.py --pin faf037e0d02c021c0717f051b01ec72ed0b063d2 --out C:/dev/irpt-release-r36s --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49/R36S_BUILD.json`. The last line must begin `R35L-BUILD-OK`; on `R35L-BUILD-BAD <why>` file ONE row with that line and the last 20 lines, change nothing, report; do not edit the tool or retry with other arguments.
3. **Write `r49/live_diff.py`** (stdlib only, run with `python -I`): it takes the record and the live-members file as arguments and prints, first, `BUILT sha=<code_sha256> members=<n>` and `LIVE sha=<code_sha256> members=<n>`; then ONE line per member of the union, sorted: `SAME|MOVED|ADDED|REMOVED <name> built=<sha12|-> live=<sha12|->`; then, for each MOVED, ADDED or REMOVED name, the commits that moved it since the live build pin: resolve the member's repository path from the function map `infra/aws/lambda/ci/function-map/irpt-status.json` at the pin (`git show <pin>:<path>`; the entries pair `repo_path` with `packaged_as`) and print `git log --oneline 90b69dcb12cdfedc786966ab33d034bf14229396..<pin> -- <repo_path>` (an empty list is printed as `NO-COMMIT-SINCE-90b69dcb12`: a mover with no commit is a FINDING, say so); then it checks that the built zip's `acceptance.py` contains the text `def get_commentary_ref` (open `<stage>/irpt-status.zip` with zipfile) and that the live one does not (from the live file's hash only: print the live acceptance.py sha12 and the built one). It prints the final line `LIVE-DIFF-OK moved=<k> added=<a> removed=<r> same=<s> acceptance_has_get_commentary_ref=yes` only when `acceptance.py` is MOVED and carries the text; otherwise `LIVE-DIFF-BAD <why>`, exit 1. Its control: `--selftest` runs it against a copy of the built record in which `acceptance.py`'s hash is set equal to the live one, and prints `CONTROL-FIRES` only when that copy yields `LIVE-DIFF-BAD`.
4. **Run it and keep the output.** Save the full output of `live_diff.py` to `r49/LIVE_DIFF.txt` and the output of `--selftest` to `r49/SELFTEST.txt`. Commit the record and these files (record first, then the rest, as separate commits). Leave the stage folder exactly as the tool made it.
5. **Report** the tool's last line, the zip's sha256, CodeSha256 and size, the `LIVE-DIFF-OK` line, the full list of movers with their commit subjects, and anything marked `NO-COMMIT-SINCE-90b69dcb12`.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR391-y-AC1" cell_refs="AR-y-391"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49/live_diff.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49/R36S_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json</invocation><expect>LIVE-DIFF-OK </expect></criterion>
`AR391-y-AC1`: the member-by-member diff against the live zip prints `LIVE-DIFF-OK` (acceptance.py MOVED and carrying `get_commentary_ref`); at base the script is absent and the criterion FAILS.

<criterion id="AR391-y-AC2" cell_refs="AR-y-391"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49/live_diff.py --selftest org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/r49/R36S_BUILD.json org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/irpt_status_release/LIVE_IRPT_STATUS_MEMBERS_20261017.json</invocation><expect>CONTROL-FIRES</expect></criterion>
`AR391-y-AC2`: the control: with acceptance.py's built hash forced equal to the live one the diff must reject.

<criterion id="AR391-y-AC3J" cell_refs="AR-y-391" judgment="true"/>
`AR391-y-AC3J` (judgment, graded at L9, never by you): the build is of the named pin, built twice identically; every mover, adder and remover is listed with the commits that moved it; nothing was uploaded, planned, applied or pushed; and the record says plainly what it did not read.

<expected_criteria>AR391-y-AC1 AR391-y-AC2 AR391-y-AC3J</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block, the deliverables folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/` and this order's file (status flip only). BUILD ONLY, as above. The stage folder `C:/dev/irpt-release-r36s` (or its `b` twin) is outside the repository and is yours.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-391</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~290/IRPT_ANLREQ.TO-AR-y-391.irpt-status-release-build-and-live-member-diff.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-391`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR391-y-AC1,AR391-y-AC2,AR391-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a package build in a throwaway worktree and a stage folder outside the repository; nothing is uploaded, planned, applied, invoked or pushed.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the live zip's own members (issuer read: 49 members, `acceptance.py` without get_commentary_ref), the r35l build tool and ledger (3 of 49 members moved at release 35) and the audit's wrong-name trap (a member packaged as `acceptance.py` was searched as `ycharts/generate/acceptance.py`) against the cell; the lens: a member searched by the repository path instead of the packaged name, a mover with no commit behind it, an unjustified extra mover riding the release, a diff that compares the build with the build pin instead of the LIVE zip, a control that cannot fail. The cell requires the live record as the base, per-member hashes, the moving commits named, and a control that fires. NOT seen (blind): the live zip beyond the issuer's read, any apply; denominator: 49 live members, one build, 2 mechanical criteria.
</preflight>

---

## RECORD FACE

- Cut on the CTO's authorization (msg 10600, "YES, now: cut the irpt-status release so the commentary PDF opens from a ticket"). Workstream `ZZ52` of round 43. Base: `r49/` and the stage folder are absent, so `AR391-y-AC1` and `AC2` FAIL as expected.
- After the worker: the issuer re-runs the two checks, writes the never-widen packet (COO half) with the printed movers and sends the CTO the packet sha; the apply is `0.7.0_AE_CloudOps~IB2`'s (plan 0/1/0 on irpt-status code only, outside the weekday 11:30Z to 14:15Z band, an after-read of the commentary route returning 200 with a body for a synthetic request, rollback to the prior artifact version `vP3Bt0tM_n0qEa17Nf_VA0ZtXjwMt4GX`'s predecessor as the r35l ledger records).
