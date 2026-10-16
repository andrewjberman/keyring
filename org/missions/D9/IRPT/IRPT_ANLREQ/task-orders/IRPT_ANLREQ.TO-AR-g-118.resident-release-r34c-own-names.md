# TO-AR-g-118 -- BUILD the release-34c resident tarball: the same content as the third r34 form under its OWN names (root 0485393f3a-r34c, keys ...-r34c.*) (BUILD ONLY: nothing is uploaded, installed, applied or run on a host)

<to_id>IRPT_ANLREQ.TO-AR-g-118</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~257</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-118` (`decompositions/IRPT_ANLREQ_DECOMP_R34_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** `AR-g-109`, `AR-g-110` (merged); the tooling commit `bc9f2d0c44` (the pin). Order: CTO msg 9114 (the first install's root and S3 keys still exist and may not be deleted, so the re-apply needs names of its own); this build supersedes `AR-g-116`'s record.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~257`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-257` (branch `wk-IRPT_ANLREQ-257`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~257 <0.9.0_WK_IRPT_ANLREQ~257@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W257-S<k>` (take the next free `<k>`; check the channel file for `W257` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no install, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Scratch outside the product tree. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-118`, inlined)

The issuer has written the tools of the release-34 build and committed them at the pin (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): the builder (with the `--opal-swap-pool` flag), the packer, the clock wrapper, the files-from list, the script generator and the driver `r34_build.py`. The driver builds twice under one fixed clock and compares, packs once, diffs against the release-32 tarball, derives the four host scripts, runs `bash -n` on each, dry-runs the two sha256 gates and writes the record. It refuses unless every tool on disk equals the same tool at the pin. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver and requires the tarball to equal the issuer's own trial build of the same pin.

1. FIRST create the record's folder (the driver does not): `mkdir -p org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257/r34`. Print `git rev-parse bc9f2d0c44`: it must equal the 40-hex below; if it does not, STOP and file a row. The stage folder `C:/dev/irpt-release-r34f` must not exist (r34, r34b, r34c and r34d are earlier stages: never touch them). THEN **run the driver** from the worktree root (it takes about two minutes; give it `timeout` 590000 ms; it needs `C:/dev/irpt-release-r32/` on this box, which holds the release-32 tarball):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34_build.py --pin bc9f2d0c44ab320f43a62951bc77d438790dd5a5 --out C:/dev/irpt-release-r34f --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257/r34/RESIDENT_R34_BUILD.json`
   (Before you run it, print `git rev-parse bc9f2d0c44`: it must equal the 40-hex above. If it does not, STOP and file a row. The stage folder must not exist; the tool refuses a non-empty one.) The last line it prints must begin `R34-BUILD-OK`. If it prints `R34-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder `C:/dev/irpt-release-r34f` exactly as the driver made it.
3. **Report** the line the driver printed, the tarball's sha256 and size, the four script names with their sha256, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR118-g-AC1" cell_refs="AR-g-118"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g107_checks.py verify C:/dev/irpt-release-r34f org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257/r34/RESIDENT_R34_BUILD.json 272d5c543bc7731217f57157afd9817db9ed8906b148977852c9b9b1714d2ff8</invocation><expect>^AR-G107-OK</expect></criterion>

<criterion id="AR118-g-AC2" cell_refs="AR-g-118"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g107_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-118.resident-release-r34c-own-names.md</invocation><expect>^AR-G107-SCOPE-OK</expect></criterion>

<expected_criteria>AR118-g-AC1,AR118-g-AC2</expected_criteria>

- AC1 recomputes, from the tarball, the release-32 tarball and the git objects at the pin: the artifact hash and that it equals the issuer's own build of the same pin (the third argument); the delta (exactly 10 members changed, 4 added, none removed, 300 identical, 314 in all); every changed or added member against `git show <pin>:<path>`; the shipped pool (schema `irpt-swap-pool.v1`, claim held, as-of 2026-10-16, 4419 rows) against the committed AQ2 snapshot; the bindings (exactly one key added, `opal_swap_pool`, pricing still off); the two builds identical; no credential-shaped text; each host script (ASCII, `bash -n`, the pins, the fail-closed running-root guards, one member check per changed or added member); and the two sha256 gates. At base (no record) it FAILs.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changes nothing under `infra/` and nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-118.resident-release-r34c-own-names.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R34_G.md</decomp_doc> round 34, workstream ~G, cell `AR-g-118`.
<owned_cells>AR-g-118</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR118-g-AC1, AR118-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~257/IRPT_ANLREQ.TO-AR-g-118.resident-release-r34c-own-names.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-118`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR118-g-AC1,AR118-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository and one record under the worker's folder; nothing is uploaded, installed, applied, invoked or run on a host, and no AWS call is made. The release is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius (the swap pass, its per-holding Yahoo request bound, the dated pool snapshot, the resident running-root guard).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's trial build at the pin (a stage folder outside the repository: 314 members, 10 changed, 4 added, 0 removed, builds identical 314 of 314, tar 272d5c54...2ff8) and the verifier run on it (AR-G107-OK), with two negative controls (a wrong expected tarball sha256, a record whose pool row count is altered: each FAILs). Traps: a tool on disk that is not the tool at the pin; a member in the tarball that no merged cell changed (the delta must be exactly 10 and 4); two builds that differ; a pool that is not the committed snapshot; a script that pins the wrong tarball or does not refuse a wrong running root (it must be r32); a gate that passes a one-byte change; a credential-shaped string; anything written under infra/ or outside the stage folder. The verifier recomputes all of it independently of the driver.
</preflight>

- Cut on the CTO's sequence (msgs 8693, 8711, 8863: r34 is the swap and the dated pool snapshot, own pair, after r33) and the issuer's trial build. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR118-g-AC1` FAILs (no record) and `AR118-g-AC2` PASSes.
- The build replaces `AR-g-116`'s record: only the release's NAMES change (the tarball, the sums file, the host script and the root are `0485393f3a-r34c`; the first attempt's r34 root and its three S3 objects are kept on the host and in S3 and are not touched by this release). The members, the delta (10 changed, 4 added of 314) and the pool are the same. Stage folder `C:/dev/irpt-release-r34f` is new.
- The tarball sha256 in AC1 is the issuer's trial of the SAME pin: the builder is deterministic under the fixed clock `2026-10-16T00:00:00Z`.
