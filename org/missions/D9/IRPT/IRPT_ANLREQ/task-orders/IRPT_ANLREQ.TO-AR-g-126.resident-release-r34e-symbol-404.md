# TO-AR-g-126 -- BUILD the release-34e resident tarball: the r34c root plus the symbol-404 checker fix (root 0485393f3a-r34e) (BUILD ONLY: nothing is uploaded, installed, applied or run on a host)

<to_id>IRPT_ANLREQ.TO-AR-g-126</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~261</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-126` (`decompositions/IRPT_ANLREQ_DECOMP_R40_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** `AR-g-125` (merged `5e7fe11fc8`); the tooling commit `f9f851d215` (the pin). Order: CTO msgs 9345 and 9354 (cut r34e under its own pair, own names; r34d was applied and rolled back at V2).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~261`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-261` (branch `wk-IRPT_ANLREQ-261`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~261 <0.9.0_WK_IRPT_ANLREQ~261@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W261-S<k>` (take the next free `<k>`; check the channel file for `W261` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no install, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Scratch outside the product tree. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-126`, inlined)

The issuer has written the tools of the release-34e build and committed them at the pin (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): `r34e_build.py` (the driver) and `make_scripts_r34e.py` (the script generator); the builder, packer, clock wrapper and files-from list are the r34c ones. The release is built over the RUNNING r34c root: the driver builds twice under one fixed clock and compares, packs once, diffs against the r34c tarball (it REFUSES unless exactly `SHA256SUMS`, `reports/resident_bindings.json` and `intake/yfinance_check.py` differ, with `provenance.package_pin` the only bindings change), derives the four host scripts, runs `bash -n` on each, dry-runs the two sha256 gates and writes the record. It refuses unless every tool on disk equals the same tool at the pin. You run it, you do not edit it. The issuer's verifier then recomputes everything without trusting the driver and requires the tarball to equal the issuer's own trial build of the same pin.

1. FIRST create the record's folder (the driver does not): `mkdir -p org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261/r34e`. Print `git rev-parse f9f851d215`: it must equal `f9f851d215b1bcbb83ebe9c7a110e66d700d2191`; if it does not, STOP and file a row. The stage folder `C:/dev/irpt-release-r34h` must not exist (`C:/dev/irpt-release-r34f` is the r34c stage and holds the base tarball the driver reads: never touch it, nor any other `C:/dev/irpt-release-*` folder). THEN **run the driver** from the worktree root (it takes about two to five minutes; give it `timeout` 590000 ms):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34e_build.py --pin f9f851d215b1bcbb83ebe9c7a110e66d700d2191 --out C:/dev/irpt-release-r34h --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261/r34e/RESIDENT_R34E_BUILD.json`
   The last line it prints must begin `R34E-BUILD-OK`. If it prints `R34E-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder `C:/dev/irpt-release-r34h` exactly as the driver made it.
3. **Report** the line the driver printed, the tarball's sha256 and size, the four script names with their sha256, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR126-g-AC1" cell_refs="AR-g-126"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g126_checks.py verify C:/dev/irpt-release-r34h org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261/r34e/RESIDENT_R34E_BUILD.json a96fbfb74db2caf6ad55d93ab35c3b7dd419cf54f4a4dba444bb3268e68e9227</invocation><expect>^AR-G126-OK</expect></criterion>

<criterion id="AR126-g-AC2" cell_refs="AR-g-126"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g126_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-126.resident-release-r34e-symbol-404.md</invocation><expect>^AR-G126-SCOPE-OK</expect></criterion>

<expected_criteria>AR126-g-AC1,AR126-g-AC2</expected_criteria>

- AC1 recomputes, from the tarball, the r34c tarball and the git objects at the pin: the artifact hash and that it equals the issuer's own build of the same pin (the third argument); the delta (exactly 3 members changed, none added or removed, 311 identical, 314 in all); `intake/yfinance_check.py` against `git show <pin>:<path>` and that it carries the symbol-404 fix (`_symbol_404`); the bindings (no key added; only `provenance` changed, and in it only `package_pin`, equal to the pin); the shipped pool (4419 rows, as-of 2026-10-16); the two builds identical; no credential-shaped text; each host script (ASCII, `bash -n`, NEW r34e and OLD r34c, the fail-closed running-root guards, one member check per changed member); and the two sha256 gates. At base (no record) it FAILs.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changes nothing under `infra/` and nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-126.resident-release-r34e-symbol-404.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40_G.md</decomp_doc> round 40, workstream ~G, cell `AR-g-126`.
<owned_cells>AR-g-126</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR126-g-AC1, AR126-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~261/IRPT_ANLREQ.TO-AR-g-126.resident-release-r34e-symbol-404.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-126`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR126-g-AC1,AR126-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository and one record under the worker's folder; nothing is uploaded, installed, applied, invoked or run on a host, and no AWS call is made. The release is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius (one changed member, the resident running-root guard, the r34c rollback root).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's trial build at the pin (a stage folder outside the repository: 314 members, 3 changed, 0 added, 0 removed, builds identical 314 of 314, tar a96fbfb7...9227) and the verifier run on it (AR-G126-OK). Traps: a tool on disk that is not the tool at the pin; a member in the tarball that no merged cell changed (the delta must be exactly 3); two builds that differ; a bindings change beyond the package pin; a script that pins the wrong tarball or does not refuse a wrong running root (it must be r34c); a gate that passes a one-byte change; a credential-shaped string; anything written under infra/ or outside the stage folder. NOT seen (blind): the live host, S3, and whether the worktree's cone carries every file the driver reads until step 1 runs; denominator: 314 members, 3 changed.
</preflight>

- Cut on the CTO's ruling (msgs 9345 and 9354) and the issuer's trial build. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR126-g-AC1` FAILs (no record) and `AR126-g-AC2` PASSes.
- The tarball sha256 in AC1 is the issuer's trial of the SAME pin: the builder is deterministic under the fixed clock `2026-10-16T00:00:00Z`.
