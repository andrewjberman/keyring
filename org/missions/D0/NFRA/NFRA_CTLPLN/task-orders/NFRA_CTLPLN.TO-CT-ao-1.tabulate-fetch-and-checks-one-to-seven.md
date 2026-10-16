# TO NFRA_CTLPLN.TO-CT-ao-1 -- workstream OUTCOME round 17 (cell CT-ao-1): the absent-package arm, steps fetch and check -- the ONE approved tabulate wheel is fetched through the checked route and runs checks 1-7; check 8 (the CTO's signature) and the release wait (FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-ao-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~127</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-127 @b49543f073) and again in the main tree after merge 5834b9f30e: CTao1-AC1 JOURNEY-FETCH wheels=1 file=tabulate-0.9.0-py3-none-any.whl device=laptop sha256=024ca478df22 requests=4 ok=True (2 of 2 mutants held); CTao1-AC2 JOURNEY-CHECK checks_run=7 failed=0 check8=AWAITING released=False ok=True; proof VALID; diff paths inside the order. The issuer listed C:/opal-intake/holding/intake-20261016-tabulate/ (exactly the one wheel) and C:/opal-intake/release/ (only the two earlier batches): nothing of this batch is released. Checks 1-7: c1, c2, c3, c4, c6, c7 passed; c5 not_applicable (no attestation published). Risks the checks leave, for the CTO's check-8 reading: c3 and c6 compare against a pre-existing pip-installed tabulate 0.9.0 on this laptop (dated 2026-02-28), so they show agreement with that copy, not an independent build; c7 shows the file was not removed or altered by the managed antivirus (no test-virus control), not that a product inspected it; no check rules out a compromised upstream release process (FWD-17). No row filed. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ao-1` (`decompositions/NFRA_CTLPLN_DECOMP.round25.md`, amended) | **outcome_ref:** FWD-16 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcome FWD-16 (a package that is NOT approved becomes approved through one route). The CTO's round-24 analysis (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round24.md`, ruling 1) drives the absent-package arm deliberately with one small pure-Python wheel that `requirements.txt` lacks. Done so far: the request `org/devices/intake/requests/REQ-20261016T025712Z-tabulate.json` (tabulate==0.9.0, a laptop NFRA_CTLPLN lane, a stated test act) read REQUESTED, then the CTO decided APPROVED (read it: `python org/devices/intake/intake_request.py status --name tabulate --version 0.9.0` must print APPROVED). The fetch approval is the CTO's file `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md` (read it whole: batch `intake-20261016-tabulate`, ONE wheel `tabulate-0.9.0-py3-none-any.whl`; a second wheel or a source archive is a new batch). The wheel is pure Python, so its tags are python `py3`, abi `none`, platform `any`: no interpreter choice is needed. This cell is the fetch and the first seven checks only. Check 8 is the CTO reading checks 1-7 and signing them in a second file after they run; the release, the pack, the Taildrop and dell1's install are later cells. Read `org/devices/intake/README.md` and `python org/devices/intake/intake_fetch.py fetch --help` and `python org/devices/intake/intake_check.py check --help` first. The previous batch's records under `org/devices/intake/records/intake-20261015-duckdb/` (`*.fetch.json`, `*.check.json`) show the shape.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's approval file is under `org/tier1_exec/`: add that folder to the sparse set if it is absent.

### BUILD

1. **Fetch ONE wheel** through the checked route, from your worktree root: batch `intake-20261016-tabulate`, name `tabulate`, version `0.9.0`, `--python-tag py3 --abi-tag none --platform-tag any`, `--approved-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md`. This is a real request to the public package index from the laptop (the laptop alone fetches; egress is open on this channel); it makes one wheel's requests. If the tool refuses, STOP and file a BLOCKING row with its printed refusal; do not edit the approval file. Never `pip install` anything. Commit the fetch record (`org/devices/intake/records/intake-20261016-tabulate/tabulate-0.9.0-py3-none-any.whl.fetch.json`). The wheel lands in the holding folder outside every git tree (`<workspace drive>/opal-intake/holding/intake-20261016-tabulate/`); do not copy it into the repository. If the tool resolves the records folder to the main tree rather than your worktree, set `OPAL_INTAKE_RECORDS` to your worktree's `org/devices/intake/records` and say so.
2. **Run the checks** with `python org/devices/intake/intake_check.py check --batch intake-20261016-tabulate --file tabulate-0.9.0-py3-none-any.whl --approved-by <the approval file above> --signed-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_TABULATE_20261016.md` (that file does not exist yet; the tool must then leave the wheel UNRELEASED with check 8 awaiting). Do NOT write that file, do NOT run `release` and do NOT run `pack`. Commit the check record. Say plainly in your report how many of checks 1-7 passed and what each one saw, and name the risks those checks leave (the CTO's check-8 reading needs it).
3. A NEW test `.tools/tests/test_round25_journey_record.py` (standard library; READ-ONLY on the records and the holding folder; no network; ASCII output; Python 3.12): flag `--fetch` prints `JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False>` (ok: exactly one wheel in the batch's holding folder or release folder, named `tabulate-0.9.0-py3-none-any.whl`, no other file type in the holding folder, its SHA-256 equals the fetch record's, the fetch record's device equals this box); `--check` prints `JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>` (ok: checks 1-7 ran, 0 failed, check 8 AWAITING and not released, or SIGNED and released). Read `.tools/tests/test_round22_journey_record.py` for the shape (it is the duckdb run's test, wired to that batch and a cp tag; copy the approach, not the constants). The test also carries two mutant cases per flag that must read `held=True` (a second wheel in the folder; a record whose SHA-256 differs), as the round-22 test does.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~127/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~126/NFRA_CTLPLN.TO-CT-an-1.intake-receive-keeps-the-pip-log.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W127-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. The holding root is `<workspace drive>/opal-intake/`, outside your worktree.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTao1-AC1" cell_refs="CT-ao-1"><invocation>python .tools/tests/test_round25_journey_record.py --fetch</invocation><expect>ok=True</expect></criterion>
`CTao1-AC1` -- exactly one wheel, `tabulate-0.9.0-py3-none-any.whl`, was fetched, with a record that names this device and a SHA-256 that matches the file on disk (base: the test does not exist); report the whole line.

<criterion id="CTao1-AC2" cell_refs="CT-ao-1"><invocation>python .tools/tests/test_round25_journey_record.py --check</invocation><expect>ok=True</expect></criterion>
`CTao1-AC2` -- checks 1-7 ran with 0 failed, check 8 awaits the CTO's signature and nothing was released (base: the test does not exist); report the whole line and each check's finding.
</proof_of_spec>

<expected_criteria>CTao1-AC1,CTao1-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~127/NFRA_CTLPLN.TO-CT-ao-1.tabulate-fetch-and-checks-one-to-seven.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTao1-AC1,CTao1-AC2` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round25.md</decomp_doc>
<owned_cells>CT-ao-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261016-tabulate/
.tools/tests/test_round25_journey_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; one HTTPS request set to the public package index through the checked fetch tool; no credentials.
comp-adversary: RUN -- a second file fetched (the approval covers exactly one wheel; the test counts files in the holding folder); a source archive fetched by a flag slip (the tags are pinned and the test requires the wheel name); a wheel executed or installed on the laptop by the check step (the checks read the file; read the check tool before running it and stop if any check imports or runs the wheel outside the tool's own sandbox); the wheel copied into a git tree (the holding folder is outside every tree); the check releasing the file without the CTO's signature (the tool must refuse; the test requires released=False); the laptop already carries tabulate 0.9.0 as a transitive install, so check 3's comparison against an installed copy is a self-comparison risk the CTO's check-8 reading must see (the worker states it); BLIND: the checks cannot rule out a wheel whose maker's account was taken over (FWD-17's limit); the install on dell1 is a later cell.
risk: SERVED -- one real wheel from the public index into a quarantine folder outside the repository, reversible by deleting the folder; nothing is installed anywhere; the issuer re-reads the records and the holding folder at close.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` is NFRA_CTLPLN's intake record folder (C-INTAKE); the approval file is the CTO's, the fetch and check tools are `org/devices/intake/intake_fetch.py` and `intake_check.py` (read, not edited).
</preflight>

Base checks, dry-run by the issuer before the cut: CTao1-AC1 and CTao1-AC2 FAIL as expected (the test file does not exist; no fetch record exists for the batch).
Source: CTO round-24 analysis rulings 1 and 3 and section 3 (`ledger/ROUND_ANALYSIS.round24.md` @6b8e48b0d5), msg 109571; FWD-16.
