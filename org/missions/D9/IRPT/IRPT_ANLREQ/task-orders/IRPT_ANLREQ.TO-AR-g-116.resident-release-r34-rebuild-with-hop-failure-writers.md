# TO-AR-g-116 -- REBUILD the release-34 resident tarball a third time: the swap pass, the dated pool snapshot, the door's yfinance checker and the hop_failure writers (BUILD ONLY: nothing is uploaded, installed, applied or run on a host)

<to_id>IRPT_ANLREQ.TO-AR-g-116</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~256</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-116` (`decompositions/IRPT_ANLREQ_DECOMP_R33_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** `AR-g-98`, `AR-g-101`, `AR-g-106`, `AR-g-109` (merged `bc0e7e96c4`), `AR-g-110` (merged `3c2c4eb87b`); the tooling commit `c43f8fc13a` (the pin). Order: CTO msgs 8693, 8711, 8863, 8968, 8907, 8971 (the writers fold into r34 after the rollback; this rebuild supersedes `AR-g-112`'s record).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~256`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-256` (branch `wk-IRPT_ANLREQ-256`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~256 <0.9.0_WK_IRPT_ANLREQ~256@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W256-S<k>` (take the next free `<k>`; check the channel file for `W256` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no install, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Scratch outside the product tree. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-116`, inlined)

The issuer has written the tools of the release-34 build and committed them at the pin (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): the builder (with the `--opal-swap-pool` flag), the packer, the clock wrapper, the files-from list, the script generator and the driver `r34_build.py`. The driver builds twice under one fixed clock and compares, packs once, diffs against the release-32 tarball, derives the four host scripts, runs `bash -n` on each, dry-runs the two sha256 gates and writes the record. It refuses unless every tool on disk equals the same tool at the pin. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver and requires the tarball to equal the issuer's own trial build of the same pin.

1. FIRST create the record's folder (the driver does not): `mkdir -p org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256/r34`. Print `git rev-parse c43f8fc13a`: it must equal the 40-hex below; if it does not, STOP and file a row. The stage folder `C:/dev/irpt-release-r34d` must not exist (r34, r34b and r34c are earlier stages: never touch them). THEN **run the driver** from the worktree root (it takes about two minutes; give it `timeout` 590000 ms; it needs `C:/dev/irpt-release-r32/` on this box, which holds the release-32 tarball):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34_build.py --pin c43f8fc13a950dd031f2c5c79a7ab0e11d730fd0 --out C:/dev/irpt-release-r34d --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256/r34/RESIDENT_R34_BUILD.json`
   (Before you run it, print `git rev-parse c43f8fc13a`: it must equal the 40-hex above. If it does not, STOP and file a row. The stage folder must not exist; the tool refuses a non-empty one.) The last line it prints must begin `R34-BUILD-OK`. If it prints `R34-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder `C:/dev/irpt-release-r34d` exactly as the driver made it.
3. **Report** the line the driver printed, the tarball's sha256 and size, the four script names with their sha256, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR116-g-AC1" cell_refs="AR-g-116"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g107_checks.py verify C:/dev/irpt-release-r34d org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256/r34/RESIDENT_R34_BUILD.json 56410a26bafe530b8765f4fe50de1ac076000f90478b1c55c4ccd66034b1f725</invocation><expect>^AR-G107-OK</expect></criterion>

<criterion id="AR116-g-AC2" cell_refs="AR-g-116"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g107_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-116.resident-release-r34-rebuild-with-hop-failure-writers.md</invocation><expect>^AR-G107-SCOPE-OK</expect></criterion>

<expected_criteria>AR116-g-AC1,AR116-g-AC2</expected_criteria>

- AC1 recomputes, from the tarball, the release-32 tarball and the git objects at the pin: the artifact hash and that it equals the issuer's own build of the same pin (the third argument); the delta (exactly 10 members changed, 4 added, none removed, 300 identical, 314 in all); every changed or added member against `git show <pin>:<path>`; the shipped pool (schema `irpt-swap-pool.v1`, claim held, as-of 2026-10-16, 4419 rows) against the committed AQ2 snapshot; the bindings (exactly one key added, `opal_swap_pool`, pricing still off); the two builds identical; no credential-shaped text; each host script (ASCII, `bash -n`, the pins, the fail-closed running-root guards, one member check per changed or added member); and the two sha256 gates. At base (no record) it FAILs.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changes nothing under `infra/` and nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-116.resident-release-r34-rebuild-with-hop-failure-writers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R33_G.md</decomp_doc> round 33, workstream ~G, cell `AR-g-116`.
<owned_cells>AR-g-116</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR116-g-AC1, AR116-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~256/IRPT_ANLREQ.TO-AR-g-116.resident-release-r34-rebuild-with-hop-failure-writers.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-116`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR116-g-AC1,AR116-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository and one record under the worker's folder; nothing is uploaded, installed, applied, invoked or run on a host, and no AWS call is made. The release is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius (the swap pass, its per-holding Yahoo request bound, the dated pool snapshot, the resident running-root guard).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's trial build at the pin (a stage folder outside the repository: 314 members, 10 changed, 4 added, 0 removed, builds identical 314 of 314, tar 56410a26...f725) and the verifier run on it (AR-G107-OK), with two negative controls (a wrong expected tarball sha256, a record whose pool row count is altered: each FAILs). Traps: a tool on disk that is not the tool at the pin; a member in the tarball that no merged cell changed (the delta must be exactly 10 and 4); two builds that differ; a pool that is not the committed snapshot; a script that pins the wrong tarball or does not refuse a wrong running root (it must be r32); a gate that passes a one-byte change; a credential-shaped string; anything written under infra/ or outside the stage folder. The verifier recomputes all of it independently of the driver.
</preflight>

- Cut on the CTO's sequence (msgs 8693, 8711, 8863: r34 is the swap and the dated pool snapshot, own pair, after r33) and the issuer's trial build. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR116-g-AC1` FAILs (no record) and `AR116-g-AC2` PASSes.
- The rebuild replaces `AR-g-112`'s record: after the rollback (CTO msg 9070) the library delivery takes time and r34 is re-applied on one more signed packet; the hop_failure writers (`AR-g-109`) ride in the same resident release (decision recorded in `decompositions/IRPT_ANLREQ_DECOMP_R33_G.md`). Stage folder `C:/dev/irpt-release-r34d` is new.
- The tarball sha256 in AC1 is the issuer's trial of the SAME pin: the builder is deterministic under the fixed clock `2026-10-16T00:00:00Z`.
