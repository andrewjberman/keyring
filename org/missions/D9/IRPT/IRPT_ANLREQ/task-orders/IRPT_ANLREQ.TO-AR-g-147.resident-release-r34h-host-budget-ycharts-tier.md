# TO-AR-g-147 -- BUILD the release-34h resident tarball: the r34g root plus the host call budget, the resolve-hop requeue and the YCharts price tier (root 0485393f3a-r34h) (BUILD ONLY: nothing is uploaded, installed, applied or run on a host)

<to_id>IRPT_ANLREQ.TO-AR-g-147</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~274</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>50</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-147` (`decompositions/IRPT_ANLREQ_DECOMP_R50_G.md`) |
**outcome_ref:** FWD-1 run 3 | **depends_on:** `AR-g-142`, `AR-g-143`, `AR-g-144`, `AR-g-146` (merged); the tooling commits through `64a348dc50` and its provenance fix; the pin `12c5c4f8da` (scratch branch). Order: CTO msgs 9727, 9757 and 9761 (the YCharts tier and ONE per-window call budget per host, (6 calls, 390 s); the apply waits for ~Y2's window 4).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~274`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-274` (branch `wk-IRPT_ANLREQ-274`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~274 <0.9.0_WK_IRPT_ANLREQ~274@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W274-S<k>` (take the next free `<k>`; check the channel file for `W274` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- **BUILD ONLY.** No upload, no install, no apply, no invoke, no AWS call of any kind, no network, no push, no change to anything under `infra/`. The stage folder is OUTSIDE the repository. Scratch outside the product tree. Never `rm -rf` a folder you did not create.

### THE CELL (`AR-g-147`, inlined)

The issuer has written the tools of the release-34h build and committed them (through the provenance fix, all in the pin) (`org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/`): `r34h_build.py` (the driver) and `make_scripts_r34h.py` (the script generator); the builder, packer, clock wrapper and files-from list are the r34c ones. The release is built over the RUNNING r34g root: the driver builds twice under one fixed clock and compares, packs once, diffs against the r34g tarball (it REFUSES unless exactly `SHA256SUMS`, `reports/resident_bindings.json`, `reports/resident_installed.py`, `ycharts/generate/resident_worker.py`, `ycharts/session/operation_lease.py` and `ycharts/session/resident_session.py` differ and `ycharts/research/price_transport_ycharts.py` is added, with `provenance` (package_pin and the files-from list's count and sha256), `opal_pricing` (the ycharts tier added) and the new `ycharts_window_budget` (6, 390) the only bindings changes), derives the four host scripts, runs `bash -n` on each, dry-runs the two sha256 gates and writes the record. It refuses unless every tool on disk equals the same tool at the pin. You run it, you do not edit it. The pin `12c5c4f8dac9bb3fac2cfcc1cc68303ad1c75a03` is a commit on the scratch branch `scratch/r34h-pin` (it is not an ancestor of your branch; its objects are in the shared object store, so `git rev-parse` resolves it). The issuer's verifier then recomputes everything without trusting the driver and requires the tarball to equal the issuer's own trial build of the same pin.

1. FIRST create the record's folder (the driver does not): `mkdir -p org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274/r34h`. Print `git rev-parse 12c5c4f8da`: it must equal `12c5c4f8dac9bb3fac2cfcc1cc68303ad1c75a03`; if it does not, STOP and file a row. The stage folder `C:/dev/irpt-release-r34r` must not exist (`C:/dev/irpt-release-r34m` is the r34g stage and holds the base tarball the driver reads: never touch it, nor any other `C:/dev/irpt-release-*` folder). THEN **run the driver** from the worktree root (it takes about two to five minutes; give it `timeout` 590000 ms):
   `python -I org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/r34h_build.py --pin 12c5c4f8dac9bb3fac2cfcc1cc68303ad1c75a03 --out C:/dev/irpt-release-r34r --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274/r34h/RESIDENT_R34H_BUILD.json`
   The last line it prints must begin `R34H-BUILD-OK`. If it prints `R34H-BUILD-BAD <why>`, file ONE row with that line and the driver's last 20 lines, change nothing, and report: do not edit a tool, do not retry with other arguments.
2. **Run the two criteria below.** Commit the record, then the proof and the status flip, as separate commits (record first). Leave the stage folder `C:/dev/irpt-release-r34r` exactly as the driver made it. In `artifacts_produced` name only files in the repository (the record, the proof); never list a staged file.
3. **Report** the line the driver printed, the tarball's sha256 and size, the four script names with their sha256, and both criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR147-g-AC1" cell_refs="AR-g-147"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g145_checks.py verify C:/dev/irpt-release-r34r org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274/r34h/RESIDENT_R34H_BUILD.json 60cc8d1d68627c993121df7eca946a40046f1d7f63ddfd2968f83e27077b93c0</invocation><expect>^AR-G145-OK</expect></criterion>

<criterion id="AR147-g-AC2" cell_refs="AR-g-147"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g145_checks.py scope box/dell2 org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274 org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-147.resident-release-r34h-host-budget-ycharts-tier.md</invocation><expect>^AR-G145-SCOPE-OK</expect></criterion>

<expected_criteria>AR147-g-AC1,AR147-g-AC2</expected_criteria>

- AC1 recomputes, from the tarball, the r34g tarball and the git objects at the pin: the artifact hash and that it equals the issuer's own build of the same pin (the third argument); the delta (exactly 6 members changed, 1 added, none removed, 308 identical, 315 in all); each changed or added member against `git show <pin>:<path>` and that it carries its marker (OPERATION_WINDOW_BUDGET, window_budget=window_budget, RESOLVE_WINDOW_CLASS, ycharts_window_budget, def make_transport); the bindings (only `ycharts_window_budget` added, equal to `{calls: 6, window_s: 390}`; only `provenance` and `opal_pricing` changed, in `provenance` only `package_pin` (equal to the pin) and the files-from count and sha256, and `opal_pricing` exactly `{enabled: true, tiers: [estate, yfinance, ycharts]}` against `{enabled: true, tiers: [estate, yfinance]}` in r34g); the shipped pool; the two builds identical; no credential-shaped text; each host script (ASCII, `bash -n`, NEW r34h and OLD r34g, the fail-closed running-root guards, one member check per changed member); and the two sha256 gates. At base (no record) it FAILs.
- AC2 checks (against the merge-base with `box/dell2`) that your branch changes nothing under `infra/` and nothing outside your own folder, your order, the channel file and the issuer's issuance files. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. BUILD ONLY, as above.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-147.resident-release-r34h-host-budget-ycharts-tier.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R50_G.md</decomp_doc> round 50, workstream ~G, cell `AR-g-147`.
<owned_cells>AR-g-147</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR147-g-AC1, AR147-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~274/IRPT_ANLREQ.TO-AR-g-147.resident-release-r34h-host-budget-ycharts-tier.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-147`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the record first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR147-g-AC1,AR147-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- BUILD ONLY: local files outside the repository and one record under the worker's folder; nothing is uploaded, installed, applied, invoked or run on a host, and no AWS call is made. The release is applied later by a CloudOps applier under a signed never-widen pair that names the blast radius (six changed members and one added, the bindings, the resident running-root guard, the r34g rollback root; the lease's count has a row of its own so the r34g lease still reads its row after a rollback).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's trial build at the pin (a stage folder outside the repository: 315 members, 6 changed, 1 added, 0 removed, builds identical 315 of 315, tar 60cc8d1d...3c0) and the verifier run on it (AR-G145-OK). Traps: a tool on disk that is not the tool at the pin; a member in the tarball that no merged cell changed (the delta must be exactly 6 changed and 1 added; the trunk's `lib/trading_calendar.py` carries the DASHBD hunk `f25618c0b4`, an extra changed member, which is why the pin is the scratch commit `12c5c4f8da` that puts that one file back to the r34e bytes); two builds that differ; a bindings change beyond the package pin, the files-from provenance fields, the ycharts tier and the host budget; a script that pins the wrong tarball or does not refuse a wrong running root (it must be r34g); a gate that passes a one-byte change; a credential-shaped string; anything written under infra/ or outside the stage folder. NOT seen (blind): the live host, S3, and whether the worktree's cone carries every file the driver reads until step 1 runs; denominator: 315 members, 6 changed and 1 added.
</preflight>

- Cut on the CTO's rulings (msgs 9727, 9757 and 9761) and the issuer's trial build. Risk WORLD: the floor of an infrastructure path; the cell moves nothing deployed. Base: `AR147-g-AC1` FAILs (no record) and `AR147-g-AC2` PASSes.
- The tarball sha256 in AC1 is the issuer's trial of the SAME pin: the builder is deterministic under the fixed clock `2026-10-16T00:00:00Z`.
