# TO IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers -- BUILD ONLY: build the resident tarball and its host scripts twice at one pin, with the r34l tool copied to r34m, and diff it against the running r34l tarball: exactly five members move (SHA256SUMS, reports/resident_bindings.json, reports/resident_installed.py, ycharts/generate/resident_worker.py, ycharts/research/opal_packager.py); nothing is uploaded, installed, applied or run on a host

<to_id>IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~315</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>43</round>
<workstream>ZZ89</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a build in a stage folder outside the repository; the only repository writes are the worker's deliverables) | **Decomp cell:** `AR-y-430` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (a packaged report reaches the ticket: O5, the packager attaches at READY), FWD-8 | **depends_on:** AR-y-417 (merged a732c5ef25a) and AR-y-423 (merged a2008503d59); ~V2 msg 11163 (the service and the page are LIVE on PROD: the CTO condition msg 11099 is met); the r34l tarball RUNNING on the host (record RESIDENT_R34L_BUILD_PINC.json)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~315`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-315` (branch `wk-IRPT_ANLREQ-315`), provisioned by the issuer from the current branch. First confirm `org/` and `.tools/` exist. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~315 <0.9.0_WK_IRPT_ANLREQ~315@opal.agent>" -F <msgfile> -- <paths>`; write every message file with the Write tool; do not pre-`git add`. A commit may take longer than 120 s: give it up to 400 s and check `git log` before retrying. The worktree may show a modified `.parquet` fixture and ` M portal`: never commit either. A row id has the form `IRPT_ANLREQ-D2-W315-S<k>`; `surfaced_at` = `date -u +%FT%TZ`; APPEND only to `org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md` (0 deletions), class OBSERVATION or BLOCKING. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (ruff clean; no single-letter names `l`, `O`, `I`; no non-ASCII).
- **No AWS call, no network, no push, no deploy.** The proof instance copies the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (read it first; `git show HEAD:<path>` if absent), with `to_id` exactly the order's id, a `controls.mutant` that FIRES (named in the cell) and a `controls.determinism` really run; run `python .tools/proof-of-spec-check.py <instance> "<ids>"` with THIS worktree's own `.tools/` and flip `<status>` to `complete` (commit alone) only on VALID.

### THE CELL (`AR-y-430`, inlined)

*Context.* The resident host runs release `irpt-resident-0485393f3a-r34l` (tarball sha256 `e1466cb8a0465572e4e0f9a42d79e193313c8afea5fbc2f3370a9ec015a33b6c`, 317 members, installed 2026-10-19 21:39Z; the stage folder `C:/dev/irpt-release-r35d/` holds `irpt-resident-0485393f3a-r34l.tar.gz`, its `package.SHA256SUMS` and the host `scripts/`; its record is `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/RESIDENT_R34L_BUILD_PINC.json`, read-only for you). Two merged code changes must now reach the resident: `AR-y-417` (`ycharts/generate/resident_worker.py`: the `analysis_ready` signal goes out for every ticketed request, merged `a732c5ef25a`) and `AR-y-423` (the O5 packager half: at READY the package is attached WITHOUT the commentary, `pdf_ref` and `commentary_ref` both null together, and a conflict replaces through `prior_attached_at`; files `reports/resident_installed.py`, `ycharts/generate/resident_worker.py`, `ycharts/research/opal_packager.py`, merged `a2008503d59`). The ticket service and the page that admit a null pair are LIVE on PROD (~V2 msg 11163).

*The pin, measured by the issuer.* `7f1eab530cde4661e9a559bf45439ebdbf73dab2` (the issuer's scratch branch `scratch/r34m-pin`): the r34l pin C `2a3aaa2815874f8efaed622065676332ec41808d` with ONLY those three files at their trunk blobs. The issuer compared the 41 files of `files_from_r34.txt` between pin C and the trunk HEAD: five differ (`reports/resident_installed.py`, `ycharts/generate/resident_worker.py`, `ycharts/research/opal_packager.py` = the three above, and `ycharts/research/layout_overview.py`, `ycharts/research/opal_producer.py` = ~G2's paused price-page work and a later producer, which therefore stay at pin C's blobs); the three movers' commits since pin C are exclusively AR-y-417 and AR-y-423. The two `--member`/map inputs `lib/trading_calendar.py` and `overview_map.json` also stay at pin C's blobs. Release machinery is the r34l set, unchanged: `org/tier1_exec/2.0.0_SA_COO~G2/deliverables/r34/` (builder, `pack_r34.py`, `run_builder_fixed_clock.py`, `smoke_imports_r34.py`, `files_from_r34.txt`) and your predecessor's copies in `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/` (`r34l_build.py`, `make_scripts_r34l.py`, `check_r34l_record.py`, `check_r34l_xref.py`).

*What to do.*
1. Make the folder `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/`. Copy the four r34l files from `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/r56/` into it as `r34m_build.py`, `make_scripts_r34m.py`, `check_r34m_record.py`, `check_r34m_xref.py`, and shift the names in ONE pass (r34l -> r34m and r34k -> r34l, simultaneously, so nothing is shifted twice). Apply exactly: `R32_DIR = "C:/dev/irpt-release-r35d"`; `R32_TAR` = `R32_DIR + "/irpt-resident-0485393f3a-r34l.tar.gz"`; `R32_TAR_SHA = "e1466cb8a0465572e4e0f9a42d79e193313c8afea5fbc2f3370a9ec015a33b6c"`; the `R55` folder constant becomes your `r57/` folder (the script generator is read from your copy); `EXPECT_CHANGED = ["SHA256SUMS", "reports/resident_bindings.json", "reports/resident_installed.py", "ycharts/generate/resident_worker.py", "ycharts/research/opal_packager.py"]`, `EXPECT_ADDED = []`; every output name reads r34m (`irpt-resident-0485393f3a-r34m.tar.gz`, `.package.SHA256SUMS`, `resident_host_install_0485393f3a-r34m.sh`, record id `RESIDENT_R34M_BUILD`, schema `irpt-resident-r34m-build-v1`, `delta_vs_r34l`); the rollback root reads `/opt/irpt-resident/0485393f3a-r34l` and its base tarball sha is the r34l sha above; the bindings comparison is against the r34l bindings (only `provenance.package_pin` may change; `opal_pricing` and `ycharts_window_budget` stay what r34l has). Any literal that still names r34k after the pass, or any other edit, is a BLOCKING row naming it. Record the sha256 of each of your four copies in the record.
2. The stage folder is `C:/dev/irpt-release-r35e` and must not exist before the build; never use or delete `r35a`, `r35b`, `r35c` or `r35d` (r35d is the OLD root). The base pin of the driver stays `0485393f3ad0a7e564f4867f5e70003e2e62195b`. Before the real run print the actual member difference the way the driver computes it, and STOP if it differs from the five members above: a sixth mover, a missing mover or an added member is a BLOCKING surprise row naming it (and NOT a loosened expectation).
3. Run `python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/r34m_build.py --pin 7f1eab530cde4661e9a559bf45439ebdbf73dab2 --out C:/dev/irpt-release-r35e --record org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/RESIDENT_R34M_BUILD.json` from your worktree (several minutes: give each command up to 600 s). It prints `R34M-BUILD-OK <members> ...` or `R34M-BUILD-BAD <why>`.
4. Print, from the record, the tarball sha256 and member count, the two-build identity line, the delta against r34l (changed, added, removed), the import smoke line, the gate dry-run return codes, and the sha256 of each of the four host scripts. Also print `git diff --stat` between pin C and the build pin for the three movers.
5. Commit your files and the record (the stage folder stays outside the repository). Then write the proof instance and flip the order only after the checker prints VALID: copy the shape of `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~306/IRPT_ANLREQ.TO-AR-y-406.resident-release-r34l-build-only-two-movers.proof_of_spec.json` (your predecessor's AR-y-406 instance; read it first, `git show HEAD:<path>` if absent), `to_id` exactly `IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers`, a real `controls.mutant` (for example the record copied with one member name changed, the checker must refuse) and `controls.determinism` (build_a equals build_b); run `python .tools/proof-of-spec-check.py <instance> "AR430-y-AC1,AR430-y-AC2,AR430-y-AC3"`; flip `<status>` to `complete` (commit alone) only on VALID.

---

## ACCEPTANCE

<criterion id="AR430-y-AC1" cell_refs="AR-y-430"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/RESIDENT_R34M_BUILD.json</invocation><expect>R34M-RECORD-OK changed=5 added=0 removed=0</expect></criterion>
<criterion id="AR430-y-AC2" cell_refs="AR-y-430"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/check_r34m_record.py org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/RESIDENT_R34M_BUILD.json --identity</invocation><expect>R34M-IDENTITY-OK builds_identical=yes smoke_fail=0</expect></criterion>
<criterion id="AR430-y-AC3" cell_refs="AR-y-430"><invocation>python -I org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/r57/check_r34m_xref.py C:/dev/irpt-release-r35e/irpt-resident-0485393f3a-r34m.tar.gz</invocation><expect>^R34M-XREF-OK missing=0</expect></criterion>

You also write `check_r34m_record.py` (your shifted copy of `check_r34l_record.py`, ruff clean): no flag, it prints `R34M-RECORD-OK changed=<n> added=<n> removed=<n>` only when `delta_vs_r34l.changed` equals exactly the five members above, `added` and `removed` are empty, and the artifact has a 64-hex sha256 and a member count; otherwise `R34M-RECORD-BAD <why>` and a non-zero exit. With `--identity` it prints `R34M-IDENTITY-OK builds_identical=yes smoke_fail=0` only when `two_builds.files_compared == two_builds.identical` and the import smoke line reads `fail=0`. Run both against the base state (record absent: BAD or an error) and against a mutated copy of the record with a sixth changed member (BAD) before relying on them.

You also write `check_r34m_xref.py` (your shifted and WIDENED copy of `check_r34l_xref.py`, ruff clean, stdlib only). The class it catches: a mover reads a name from a sibling member that the held-back sibling lacks (the r34l pin-B defect: the delta gate and the import smoke both pass such a build). It opens the tarball and, for each of the three movers `reports/resident_installed.py`, `ycharts/generate/resident_worker.py` and `ycharts/research/opal_packager.py`, parses it with `ast`; for every `import X` / `import X as Y` and `from X import a, b` whose X resolves to ANOTHER member of the tarball (match the module's dotted path or its basename to a member `.py` path), it collects every attribute `Y.<NAME>` the mover reads and every imported `a`, `b`; it prints `R34M-XREF-OK missing=0 names=<n>` only when each NAME is defined at module level in that sibling (assignment target, def, class, or an import binding), otherwise `R34M-XREF-BAD missing=<k> <names>` and a non-zero exit. DIFFERENCE CONTROL (required, before you rely on it): run it on a copy of the new tarball's tree with one name the mover reads deleted from the sibling (it MUST print `R34M-XREF-BAD missing=1 <name>`), and on your new tarball (`R34M-XREF-OK missing=0`); record both lines.

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR430-y-AC1,AR430-y-AC2,AR430-y-AC3"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-430</owned_cells>
</decomp_ref>

- **Grant.** The `<paths>` block, this order's file (status line only) and the surprise investigation file are the only repository places you write.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~315/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-y-430.resident-release-r34m-build-only-three-o5-movers.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a build in a stage folder outside the repository and four tool copies in the worker deliverables; nothing is uploaded, installed, applied or run on a host.
comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call by the worker.
comp-adversary: RUN -- by reading r34l_build.py and the pin measurement against this cell; the lens: a sixth mover riding the files-from list (STOP, a row, no loosened expectation), a rename that leaves an r34k name in an output (the record and the tarball name must read r34m), the base tarball not equal to the one running (the sha256 gate), the clock not fixed (builds differ), the stage folder created inside the repository (refused), r35d is the OLD root (do not delete), a mover reading a name the held-back sibling lacks (the xref check with its difference control). NOT seen (blind): the live host, the live root and the release key; denominator: three criteria.
</preflight>
