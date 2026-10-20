# TO IRPT_ANLREQ.TO-AR-y-450.resident-release-r34n-rebuild-with-the-packager-api-base-through-cloudfront -- BUILD ONLY: rebuild the resident tarball as r34n with ONE changed value, the packager api_base in the bindings (the portal's CloudFront alias instead of the direct API Gateway host), so exactly two members move against the running r34m version 2 (SHA256SUMS and reports/resident_bindings.json); nothing is uploaded, installed, applied or run on a host

<to_id>IRPT_ANLREQ.TO-AR-y-450.resident-release-r34n-rebuild-with-the-packager-api-base-through-cloudfront</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~322</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ109</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (no repository write beyond the worker's deliverables) | **Decomp cell:** `AR-y-450` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the packager attaches the four pointers), O5 | **depends_on:** AR-y-438 (r34m version 2, installed 07:30Z; tarball sha256 00e1d165266bc5c1ad36cafcbd1cb91b7bef05b4138aa82383adcd200142ce0b at C:/dev/irpt-release-r35f/irpt-resident-0485393f3a-r34m.tar.gz); IB2 read A_PACKAGER_403.txt; CTO msg 11292 (r34n changes only the value if it is a binding)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~322`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-322` (branch `wk-IRPT_ANLREQ-322`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~322 <0.9.0_WK_IRPT_ANLREQ~322@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W322-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-450`, inlined)

*Context.* The running resident (install root `/opt/irpt-resident/0485393f3a-r34m`) carries `reports/resident_bindings.json` whose member `packager` is `{"api_base": "https://7k3ed8px20.execute-api.us-east-1.amazonaws.com", "secret_name": "opal/ticketing/svc-irpt-packager"}`. The direct host is refused by the API authorizer (403 ORIGIN_VERIFICATION_FAILED) because the request did not come through CloudFront. The CTO ruled (msg 11292): the packager calls the ticket service through the portal's CloudFront alias `https://opalinvest.dev`; the value is a binding, so ONE resident release, r34n, changes only that value. The path the packager appends is unchanged (`/api/scoped/tickets/<id>/package`). Nothing else moves.

*The builder and the tools.* Your predecessor's build tools for r34m version 2 are in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/` (`r34m_build.py`, `make_scripts_r34m.py`, `check_r34m_record.py`, `check_r34m_xref.py`). In `r34m_build.py` the `BUILD_ARGS` list carries `"--packager", "api_base=https://7k3ed8px20.execute-api.us-east-1.amazonaws.com,secret_name=opal/ticketing/svc-irpt-packager"`; the builder is `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/build_resident_package.py` (the option `--packager api_base=URL,secret_name=NAME`, https required).

*What to do.*
1. Make the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/`. Copy the four files of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/r58/` into it. Edit the copies, and only these things: (a) the `R58` constant names your `r60/` folder; (b) in `BUILD_ARGS` the `--packager` value becomes `api_base=https://opalinvest.dev,secret_name=opal/ticketing/svc-irpt-packager`; (c) the OLD root (the tarball the new one is compared with) becomes the running r34m version 2: tarball `C:/dev/irpt-release-r35f/irpt-resident-0485393f3a-r34m.tar.gz`, sha256 `00e1d165266bc5c1ad36cafcbd1cb91b7bef05b4138aa82383adcd200142ce0b` (print `sha256sum` of that file first; if it differs STOP and file a BLOCKING row); (d) `EXPECT_CHANGED` becomes exactly `["SHA256SUMS", "reports/resident_bindings.json"]` and `EXPECT_ADDED` stays empty; the bindings check must allow exactly ONE difference from the old bindings file: the value of `packager.api_base`; (e) wherever the release label `r34m` names the tarball, the install root or a host script, it becomes `r34n` (find every place with a search of the four copies and print the list; if the label is set in a file you may not copy, STOP with a BLOCKING row naming the file); the record id and file read `RESIDENT_R34N_BUILD` and the schema version `irpt-resident-r34n-build-v1`, and `check_r34m_record.py` expects `changed=2` and prints `R34N-RECORD-OK changed=2 added=0 removed=0`. Any other edit is a BLOCKING row naming it. Record the sha256 of each of the four copies.
2. The stage folder is `C:/dev/irpt-release-r35h` and must not exist before the build; never use or delete `r35a` to `r35f`. Before the real run print the member difference the way the driver computes it and STOP if it is not exactly the two members.
3. Run `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/r34m_build.py --pin <the pin your predecessor's record names for r34m version 2> --out C:/dev/irpt-release-r35h --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/RESIDENT_R34N_BUILD.json` from your worktree (several minutes, up to 600 s per command). The last line begins `R34N-BUILD-OK` or `R34N-BUILD-BAD <why>` (rename the printed tag in your copy accordingly).
4. Write `check_packager_base.py` in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/` (stdlib only, ruff clean, offline). Arguments: a tarball path and the OLD tarball path. It reads `reports/resident_bindings.json` from both, and prints `PACKAGER-BASE-OK api_base=https://opalinvest.dev secret=opal/ticketing/svc-irpt-packager other_members_equal=yes` ONLY when the new tarball's `packager.api_base` equals that value, `secret_name` is unchanged, every other key of the bindings equals the old bindings' value, and every member other than `SHA256SUMS` and `reports/resident_bindings.json` has the same sha256 in both tarballs; else `PACKAGER-BASE-BAD <why>` and exit 1. DIFFERENCE CONTROL: run it with the OLD tarball as the first argument and as the second (it MUST print `PACKAGER-BASE-BAD`), and on your new tarball (OK); record both lines.
5. Print the tarball sha256 and member count, the two-build identity line, the delta against r34m version 2, the import smoke line, the gate dry-run return codes and the sha256 of each host script. Commit your files and the record (the stage folder stays outside the repository). Write the proof instance (shape of the AR-y-438 instance in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/`; `controls.mutant`: the record copied with one member name changed, which the record checker must refuse; `controls.determinism`: build_a equals build_b), run the proof check and flip `<status>` to `complete` (commit alone) only on VALID.

*AMENDMENT 1 (issuer, 2026-10-20 ~10:1xZ, ruling on your BLOCKING row IRPT_ANLREQ-D2-W322-S1).* The host-script generator `make_scripts_r34m.py` (your r60 copy) refuses because it assumes the release moves package members; r34n moves none. You may make these further edits to YOUR r60 copy of that file, and only these: (i) the `for must in (...)` tuple becomes `(SUMS, BINDINGS)`; (ii) `PKG_DIFF` and `PKG_ALL` may be empty: at each of the three places that write a shell block `for ent in \` ... `done` (or the install's `entries()` splice) from `PKG_ALL`, an empty list writes ONE `echo` line instead, `no package member changes in r34n (the bindings member and the package sums only)`, and no empty `for` loop; (iii) the header comment lines that name the cells AR-y-417 and AR-y-423 become one sentence saying that r34n changes the bindings member (`packager.api_base`) and the package sums only; (iv) every `rep` count stays exact. THE STAGE FOLDER is now `C:/dev/irpt-release-r35h` (the folder `r35g`, left by the refused run, stays untouched: do not delete it and do not reuse it); change the stage path in your r60 copy, and criterion AC3 now names the tarball `C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz` (the order's text is amended in the same place; the criterion line below is the amended one). After the generator has run, print `bash -n` for each of the four written scripts (each must read rc 0) and, for each, `grep -c 'for ent in'` (none may be an empty loop); list the host scripts of the r34m version 2 build under the folder of worker 317 (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~317/`) and print a line-count diff between its `install_r34.sh` and yours. Any other refusal of the generator, or any other edit it seems to need, is a BLOCKING row and you stop.

---

## ACCEPTANCE

<criterion id="AR450-y-AC1" cell_refs="AR-y-450"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/RESIDENT_R34N_BUILD.json</invocation><expect>^R34N-RECORD-OK changed=2 added=0 removed=0$</expect></criterion>
<criterion id="AR450-y-AC2" cell_refs="AR-y-450"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/r60/RESIDENT_R34N_BUILD.json --identity</invocation><expect>R34N-IDENTITY-OK builds_identical=yes smoke_fail=0</expect></criterion>
<criterion id="AR450-y-AC3" cell_refs="AR-y-450"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/check_packager_base.py C:/dev/irpt-release-r35h/irpt-resident-0485393f3a-r34n.tar.gz C:/dev/irpt-release-r35f/irpt-resident-0485393f3a-r34m.tar.gz</invocation><expect>^PACKAGER-BASE-OK api_base=https://opalinvest.dev secret=opal/ticketing/svc-irpt-packager other_members_equal=yes$</expect></criterion>



<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/IRPT_ANLREQ.TO-AR-y-450.resident-release-r34n-rebuild-with-the-packager-api-base-through-cloudfront.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-450.resident-release-r34n-rebuild-with-the-packager-api-base-through-cloudfront`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR450-y-AC1,AR450-y-AC2,AR450-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-450</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~322/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-450.resident-release-r34n-rebuild-with-the-packager-api-base-through-cloudfront.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder outside the repository and tool copies in the worker deliverables; nothing is uploaded, installed, applied or run on a host.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading the builder option, the r34m version 2 record and the CTO ruling against this cell; the lens: a third mover, the label r34m left in the tarball name or the host scripts, the check that cannot refuse (the difference control with the OLD tarball must print BAD), the stage folder inside the repository, r35a to r35f deleted. NOT seen (blind): whether the CloudFront route admits the service token (cell AR-y-449 reads that; IB2 proves it live before any install); denominator: three criteria.
</preflight>
