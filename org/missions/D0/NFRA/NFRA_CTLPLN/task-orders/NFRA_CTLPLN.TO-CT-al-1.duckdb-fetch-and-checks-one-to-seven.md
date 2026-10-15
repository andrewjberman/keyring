# TO NFRA_CTLPLN.TO-CT-al-1 -- workstream OUTCOME round 12 (cell CT-al-1): the package journey, steps fetch and check -- the ONE approved duckdb wheel is fetched through the checked route and runs checks 1-7; check 8 (the CTO's signature) and the release wait (FWD-15/16/18/19)

<to_id>NFRA_CTLPLN.TO-CT-al-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~119</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-119 @36e4e2c9bc, merged 3c3d04d4ec) and its own read of the holding folder at 19:3xZ: JOURNEY-FETCH wheels=1 file=duckdb-1.5.0-cp314-cp314-win_amd64.whl device=laptop sha256=11ae50aaeda2 requests=4 ok=True; JOURNEY-CHECK checks_run=7 failed=0 check8=AWAITING released=False ok=True; JOURNEY-TAG recorded=cp314-cp314-win_amd64 wheel=cp314-cp314-win_amd64 ok=True; proof VALID. The issuer listed C:/opal-intake/holding/intake-20261015-duckdb/ (exactly one file, 13575130 bytes, sha256 11ae50aaeda2145b50294ee0...) and C:/opal-intake/release/ (only the earlier batch intake-20261008-a): the cp312 wheel was not fetched and nothing of this batch is released. The wheel was fetched on the CTO's approval @29a69ec1c5 with dell1's CTO's interpreter choice (cp314, call bde8). Check 8 is recorded by the tool as failed/not_checked because the CTO's signature file does not exist yet (W119-S1: the tool says failed, not awaiting); the CTO signs it after reading checks 1-7. Risks the checks leave (for the CTO's reading): check 3 compares against an installed copy on the laptop and not a cp314 build; the compiled _duckdb.cp314-win_amd64.pyd is named but not compared; check 7 does not show the antivirus inspected the file; no check can rule out a taken-over maker account (FWD-17). The fetch made 4 requests to the index for that one wheel (metadata, file, digest, attestation).</status_reason>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-al-1` (`decompositions/NFRA_CTLPLN_DECOMP.round22.md`) | **outcome_ref:** FWD-15, FWD-16, FWD-18, FWD-19 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

PRD outcomes FWD-15 (`prd/NFRA_CTLPLN_PRD.md` line 162), FWD-16, FWD-18, FWD-19. One real package takes the checked route to one Dell lane. Done so far: the request `org/devices/intake/requests/REQ-20261015T171032Z-duckdb.json` (duckdb==1.5.0, lane `2.0.0_SA_COO~D1`, MDPF_CANON on dell1) is APPROVED by the CTO with the CRO's co-decision (`org/tier1_exec/4.0.0_SA_CRO/deliverables/CRO_CODECISION_INTAKE_DUCKDB_REQ-20261015T171032Z_20261015.md`), and the fetch approval is `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md` (read it whole: exactly ONE of the cp312 or cp314 wheel is fetched, the one matching the interpreter dell1's lane runs). The tag is READ: dell1's manager measured bare `python` = 3.14.7 (`cp314-cp314-win_amd64`) and a second install Python312 (cp312) not first on PATH (call `XB-20261015T174945Z-6bd5`), and dell1's CTO `1.0.0_SA_CTO~DELL1` answered the lane's choice: **cp314, bare python 3.14.7** (call `XB-20261015T181716Z-bde8`, carried by `0.0.0_AB_MSTR` msg 109486). The wheel to fetch is therefore `duckdb-1.5.0-cp314-cp314-win_amd64.whl`; the cp312 wheel is NOT fetched. This cell is the fetch and the first seven checks only. Check 8 is the CTO reading checks 1-7 and signing them in a second file, after they run; the release, the pack, the taildrop and the install are the next cells.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report.

### BUILD

1. **Record the tag before the fetch.** Write `org/devices/intake/records/intake-20261015-duckdb/TAG_RECORD.md` (ASCII): the lane, the two interpreter tags dell1's manager read, dell1's CTO's choice (cp314), and the two call ids with the carrying message ids above. Commit it BEFORE the fetch (its own commit).
2. **Fetch ONE wheel** through the checked route, from your worktree root, reading `python org/devices/intake/intake_fetch.py fetch --help` first for the exact flags: batch `intake-20261015-duckdb`, name `duckdb`, version `1.5.0`, python tag `cp314`, abi tag `cp314`, platform tag `win_amd64`, `--approved-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md`. This is a real request to the public package index from the laptop (the laptop alone fetches; egress is open on this channel); it makes exactly one wheel's request. If the tool refuses, STOP and file a BLOCKING row with its printed refusal; do not edit the approval file and do not fetch the cp312 wheel. Never `pip install` anything. Commit the fetch record (`org/devices/intake/records/intake-20261015-duckdb/duckdb-1.5.0-cp314-cp314-win_amd64.whl.fetch.json`). The wheel itself lands in the holding folder outside every git tree (`<workspace drive>/opal-intake/holding/intake-20261015-duckdb/`); do not copy it into the repository.
3. **Run the checks** with `python org/devices/intake/intake_check.py check ...` (read its `--help` and `org/devices/intake/README.md` first; the first batch's records under `org/devices/intake/records/intake-20261008-a/` show the shape). Pass `--signed-by` the path where the CTO's check-8 file WILL be written, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md` (it does not exist yet; the tool must then leave the wheel UNRELEASED with check 8 awaiting). Do NOT write that file, do NOT run `release` and do NOT run `pack`. Commit the check record. Say plainly in your report how many of checks 1-7 passed and what each one saw, and name the risks those checks leave (the CTO's check-8 reading needs it).
4. A NEW test `.tools/tests/test_round22_journey_record.py` (standard library; READ-ONLY on the records and the holding folder; no network): flag `--fetch` prints `JOURNEY-FETCH wheels=<n> file=<name> device=<d> sha256=<12 hex> requests=<r> ok=<True|False>` (ok: exactly one wheel fetched, the cp314 file, record device equals this box, the cp312 wheel absent from the holding folder and the records); `--check` prints `JOURNEY-CHECK checks_run=<n> failed=<f> check8=<AWAITING|SIGNED> released=<True|False> ok=<True|False>` (ok: checks 1-7 ran, 0 failed, check 8 AWAITING, not released); `--tag` prints `JOURNEY-TAG recorded=<tag> wheel=<tag> ok=<True|False>` (ok: the tag in `TAG_RECORD.md` equals the fetched wheel's tag).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~119/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths. Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~105/NFRA_CTLPLN.TO-CT-ah-1.sparse-safe-commit-abs-path-link-batch.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W119-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. The holding root is `<workspace drive>/opal-intake/`, outside your worktree; if the tool resolves the records folder to the main tree rather than your worktree, set `OPAL_INTAKE_RECORDS` to your worktree's `org/devices/intake/records` and say so.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTal1-AC1" cell_refs="CT-al-1"><invocation>python .tools/tests/test_round22_journey_record.py --fetch</invocation><expect>ok=True</expect></criterion>
`CTal1-AC1` -- exactly one wheel, the cp314 one, was fetched, with a record that names this device (base: the test does not exist); report the whole line.

<criterion id="CTal1-AC2" cell_refs="CT-al-1"><invocation>python .tools/tests/test_round22_journey_record.py --check</invocation><expect>ok=True</expect></criterion>
`CTal1-AC2` -- checks 1-7 ran with 0 failed, check 8 awaits the CTO's signature and nothing was released (base: the test does not exist); report the whole line and each check's finding.

<criterion id="CTal1-AC3" cell_refs="CT-al-1"><invocation>python .tools/tests/test_round22_journey_record.py --tag</invocation><expect>ok=True</expect></criterion>
`CTal1-AC3` -- the recorded tag equals the fetched wheel's tag (base: the test does not exist); report the whole line.
</proof_of_spec>

<expected_criteria>CTal1-AC1,CTal1-AC2,CTal1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~119/NFRA_CTLPLN.TO-CT-al-1.duckdb-fetch-and-checks-one-to-seven.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTal1-AC1,CTal1-AC2,CTal1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round22.md</decomp_doc>
<owned_cells>CT-al-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261015-duckdb/
.tools/tests/test_round22_journey_record.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; one HTTPS request to the public package index through the checked fetch tool; no credentials.
comp-adversary: RUN -- a second wheel fetched (the approval covers exactly one; the test counts wheels in the holding folder and the records); the cp312 wheel fetched by a flag slip (the tag record and the test); a wheel executed or installed on the laptop by the check step (the checks read the file, they do not import it; read the check tool before running it and stop if any check imports or runs the wheel outside the tool's own sandbox); the wheel copied into a git tree (the holding folder is outside every tree); the check releasing the file without the CTO's signature (the tool must refuse; the test requires released=False); BLIND: the check cannot rule out a wheel whose maker's account was taken over (FWD-17's limit), a hash match with the index's own digest is all check 2-type reads can say; the install on dell1 and the lane's run are later cells.
risk: SERVED -- one real wheel from the public index into a quarantine folder outside the repository, reversible by deleting the folder; nothing is installed anywhere; the issuer re-reads the records and the holding folder at close.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/records/` is NFRA_CTLPLN's intake record folder (C-INTAKE); the approval file is the CTO's, the fetch tool is `org/devices/intake/intake_fetch.py` (read, not edited).
</preflight>

Base checks, dry-run by the issuer before the cut: CTal1-AC1, AC2 and AC3 FAIL as expected (the test file does not exist; no fetch record exists for the batch).
Source: CTO round-21 analysis sections 2-3 (`ledger/ROUND_ANALYSIS.round21.md` @a558191b7c), msg 109483; FWD-15, FWD-16, FWD-18, FWD-19.
