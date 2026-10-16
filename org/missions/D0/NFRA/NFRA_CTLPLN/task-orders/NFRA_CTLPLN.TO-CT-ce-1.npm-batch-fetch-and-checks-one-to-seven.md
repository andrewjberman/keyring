# TO NFRA_CTLPLN.TO-CT-ce-1.npm-batch-fetch-and-checks-one-to-seven -- workstream OUTCOME round 33 (cell CT-ce-1): the npm batch: fetch dell1's 50 bun packages (the lockfile of mcportal@c66ca82952) through the checked route into the holding folder and run checks 1-7 on each (check 8 is the CTO's, after)

<to_id>NFRA_CTLPLN.TO-CT-ce-1.npm-batch-fetch-and-checks-one-to-seven</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~149</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>open</status>
<status_reason>Issued by the issuer 2.0.0_SA_COO~C in the round-29 issuance, per the CTO's round-28 analysis (ROUND_ANALYSIS.round28.md @3894648aa3, msg 109677).</status_reason>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>33</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ce-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** the intake route (C-INTAKE); an inbound ask from dell1 (HVST-cc-7, row D1-S36), ruled by the CTO (msgs 109738, 109746, 109752) |
**depends_on:** CT-cd-1 (merged 888087920b)

---

## WORKER FACE

### THE CELL

dell1's `AMGT_HARVST` (HVST-cc-7, row D1-S36) needs 50 npm packages in its bun cache to redeploy the mcportal dashboard build (`mcportal@c66ca82952`). The CTO ruled the route's npm limb (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md`, addenda 2 and 3: read it WHOLE) and the limb is built and merged (`CT-cc-1` `867c77705c`, `CT-cd-1` `888087920b`). The CTO wrote his approval file with the 50 exact lines: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` (read it whole, including its conditions). The lockfile is `org/tier0_exec/0.0.0_AB_MSTR/deliverables/MCPORTAL_c66ca82952_bun.lock` (carried from dell1; its sha256 MUST equal `7e6b71c2ea3876561f18e2df606203a78b48bd7013404bf26d614ea70d10c4bc` and it holds 278 lines: check both BEFORE any request; a different file is a BLOCKING row and a stop). THIS cell fetches the 50 tarballs through the checked route into the holding folder and runs checks 1-7 on each; check 8 is the CTO reading ALL the per-package records and signing ONCE for the batch, after you finish (you do not write it, release, pack or send anything).

Read first: `org/devices/intake/README.md` and `APPROVAL_AND_SIGNED_FILE_DEMANDS.md`, `python org/devices/intake/intake_fetch.py fetch --help` and `python org/devices/intake/intake_check.py check --help` (both take `--ecosystem npm`; the check takes `--lockfile`), the records of the earlier real batch (`org/devices/intake/records/intake-20261016-yfinance-linux/` `*.fetch.json` and `*.check.json`) and the shape of its test `.tools/tests/test_round27_yfinance_batch.py` (its `--fetch` and `--check` flags are the shape you copy for 50 tarballs).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero. The CTO's approval file and ruling are under `org/tier1_exec/1.0.0_SA_CTO/deliverables/` and the lockfile under `org/tier0_exec/0.0.0_AB_MSTR/deliverables/`: add both folders.

### BUILD

1. **The list.** From the approval file read the 50 `name@version` lines. Verify the lockfile (sha256 and 278 lines) and that every one of the 50 appears as a `name@version` key with a `sha512-` integrity in it (the CTO checked this: you re-check it). Print the 50 rows (`name`, `version`) before any fetch. The held file name rule is the tool's (`babel__core-7.29.7.tgz` for `@babel/core@7.29.7`): read it from the first fetch record, never invent it.
2. **Fetch ONE tarball at a time, in the printed order, never in parallel:** `python org/devices/intake/intake_fetch.py fetch --ecosystem npm --batch intake-20261016-npm-mcportal-bun --name <name> --version <version> --approved-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` (each under `timeout 120`). These are real requests to `registry.npmjs.org` from the laptop (the laptop alone fetches; egress is open on this channel): 3 per package (the version document, the packument, the tarball); NO other host. Never `npm install`, `bun install` or any package manager. If the tool REFUSES or FAILS on a package, record its printed line, retry that one package at most ONCE after reading the refusal, and if it still does not hold, STOP the cell and file a BLOCKING row naming the package and the printed refusal; do not edit the approval file, do not pick another version, do not fetch outside the tool. Commit the fetch records after each 10 packages and at the end (`org/devices/intake/records/intake-20261016-npm-mcportal-bun/<file>.fetch.json`). The tarballs land in the holding folder outside every git tree (`<workspace drive>/opal-intake/holding/intake-20261016-npm-mcportal-bun/`); never copy one into the repository. If the tool resolves the records to the main tree, set `OPAL_INTAKE_RECORDS` to your worktree's folder and say so.
3. **Run checks 1-7 on each held tarball** with `python org/devices/intake/intake_check.py check --ecosystem npm --batch intake-20261016-npm-mcportal-bun --file <held file name> --approved-by <the approval file above> --lockfile org/tier0_exec/0.0.0_AB_MSTR/deliverables/MCPORTAL_c66ca82952_bun.lock --signed-by org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK8_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` (each under `timeout 280`; a check includes a scanner wait). That check-8 file does NOT exist; do NOT write it, do NOT run `release`, `pack`, `verify` or `install`. Read the check tool and its first record before you start, and stop if any check extracts, imports or runs a tarball outside the tool's own in-memory reading. Commit the check records after each 10 packages and at the end. For EACH package report each of checks 1-7 as the record states it (passed, failed or not_applicable, and its evidence line): a failed check is a FINDING for the CTO, not a defect you repair; do not re-run to make it pass, and there is NO check-4 waiver for this batch (a failure stays a refusal).
4. **Aggregate the facts the CTO signs on** into `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NPM_BATCH_FACTS.md` (written by you from the records, not by hand-copy): one table of the 50 with sha512 (registry = lockfile?), release age in days, lifecycle scripts listed, native binaries named, and the verdict of each check; then two short lists: every package with a lifecycle script, and every package with a native binary or an `os`/`cpu` restriction (expected: the esbuild and rollup win32 binaries and esbuild's own install script; report what the records say, not what is expected).
5. **A NEW test** `.tools/tests/test_round30_npm_batch.py` (standard library plus the kit tool; READ-ONLY on the records and the holding folder; no network; ASCII output; Python 3.12). Flag `--fetch` prints `NPM-BATCH-FETCH tarballs=<n> expected=50 names_equal=<True|False> sha512_equal=<True|False> held=<h> device=<d> ok=<True|False>`: ok when exactly the 50 approved packages are in the holding folder and no other file, each file's sha512 equals the lockfile's integrity AND its fetch record's, every fetch record's outcome is `held`, and the device equals this box; with two mutant cases (a 51st file; one record whose digest differs) that must read `held=True`. Flag `--check` prints `NPM-BATCH-CHECK tarballs=<n> checks_run_each=<k> failed_total=<f> not_applicable_total=<m> check8=<AWAITING|SIGNED|OTHER> released=<True|False> ok=<True|False>`: ok when all 50 check records exist with checks 1-7 each carrying a verdict, check 8 AWAITING, nothing released; a `failed_total` above 0 does NOT make ok False (it is printed, with one `NPM-BATCH-CHECK-FAIL <file> check <n> <evidence>` line per failure, for the CTO). Flag `--natives` prints `NPM-BATCH-NATIVES tarballs=<n> lifecycle=<l> native=<v> listed_in_facts=<True|False> ok=<True|False>`: ok when the counts equal what the records carry and every such package is in `NPM_BATCH_FACTS.md`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/`. The only network the cell may use is `registry.npmjs.org` through `intake_fetch.py`; NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W149-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. NEVER `npm`, `bun`, `pip` or any package manager; never release, pack, verify, install or send; never write the CTO's check-8 file; never touch `C:/opal-intake/` outside the tool's own holding writes.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTce1-AC1" cell_refs="CT-ce-1"><invocation>python .tools/tests/test_round30_npm_batch.py --fetch</invocation><expect>ok=True</expect></criterion>
`CTce1-AC1` -- exactly the 50 approved tarballs are held, each digest equal to the lockfile's and its fetch record's, nothing released (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTce1-AC2" cell_refs="CT-ce-1"><invocation>python .tools/tests/test_round30_npm_batch.py --check</invocation><expect>ok=True</expect></criterion>
`CTce1-AC2` -- all 50 check records carry a verdict for checks 1-7, check 8 awaits the CTO, and every failed check is printed for him (base: the test does not exist); report the whole last line and every `NPM-BATCH-CHECK-FAIL` line.

<criterion id="CTce1-AC3" cell_refs="CT-ce-1"><invocation>python .tools/tests/test_round30_npm_batch.py --natives</invocation><expect>ok=True</expect></criterion>
`CTce1-AC3` -- every package with a lifecycle script or a native binary is named in the facts the CTO signs on (base: the test does not exist); report the whole last line and the two lists.
</proof_of_spec>

<expected_criteria>CTce1-AC1,CTce1-AC2,CTce1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NFRA_CTLPLN.TO-CT-ce-1.npm-batch-fetch-and-checks-one-to-seven.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTce1-AC1,CTce1-AC2,CTce1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-ce-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/records/intake-20261016-npm-mcportal-bun/
.tools/tests/test_round30_npm_batch.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the only network is `registry.npmjs.org` through the checked fetch tool, from the laptop; nothing is installed, extracted or run.
comp-adversary: RUN -- a tarball fetched outside the approval (the tool refuses any line absent from the approval file and any host but the registry); a digest accepted on one source (check 1 compares the registry's integrity AND the lockfile's; the batch test compares the file against both and its own record); a native binary or lifecycle script passing unseen (listed in the records and in the facts file, signed by name in check 8 by the CTO); a swapped lockfile (its sha256 and line count are verified before any request); a check failure repaired by re-running (forbidden: a failure is a finding; no waiver for check 4); a release before the signature (the test requires check 8 AWAITING and released False); BLIND: the registry's own claims (integrity, publish time) are what the checks compare, not a third party's attestation; the files are not run here, and dell1's unpack is a later act by `0.7.0_AE_CloudOps~SC1` after its own sha512 re-check.
risk: SERVED -- 50 real tarballs enter the holding folder from the public registry for a box other than the laptop; nothing is released, packed, sent, unpacked or run.
lane: the <paths> block IS the grant (worker RULING 1). The CTO ruled the route, the batch and the approval (msgs 109738, 109746, 109752).
</preflight>

Base checks, dry-run by the issuer before the cut: CTce1-AC1, AC2 and AC3 FAIL as expected (the test does not exist).
Source: CTO npm-limb ruling addenda 2-3 and his approval file `CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_NPM_MCPORTAL_BUN_20261016.md` (@1e9f508ce9); MSTR msgs 109730, 109737, 109747; dell1 AMGT_HARVST HVST-cc-7 (row D1-S36).
