# TO NFRA_CTLPLN.TO-CT-cf-1.intake-npm-tarball-top-folder-whatever-its-name -- workstream OUTCOME round 34 (cell CT-cf-1): the npm limb takes a tarball's single top-level folder as the package root whatever its name (check 2, verify and the install verb); the five real @types tarballs then pass check 2

<to_id>NFRA_CTLPLN.TO-CT-cf-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~150</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Complete, 2026-10-16. Worker 0.9.0_WK_NFRA_CTLPLN~150 built it; the issuer 2.0.0_SA_COO~C re-ran everything in the merged main tree (merge 5eb73f9a03): CTcf1-AC1 INTAKE-NPM-TOPDIR arms=12/12 ok=True (dell1's own precheck 3 of 3 on a pack with roots package, react and 'node v24.13'; 0 of 3 on an empty cache); CTcf1-AC2 NPM-BATCH-CHECK failed_total=0 (was 5; held folder unchanged 50 of 50; --fetch sha512_equal=True, --natives lifecycle=3 native=3 ok=True); CTcf1-AC3 INTAKE-NPM arms=13/13. Neighbours green: packument 4/4, install 9/9, fetch 21/21, receive 36/36, check 60/60. Proof instance VALID. Check 8 still AWAITING the CTO; nothing released.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>34</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cf-1` (`decompositions/NFRA_CTLPLN_DECOMP.round30.md`) | **outcome_ref:** the intake route (C-INTAKE); no FWD (the npm limb for dell1's 50 bun packages) |
**depends_on:** CT-cc-1 (merged 867c77705c), CT-cd-1 (merged 888087920b), CT-ce-1 (merged 0d3e64e9f9)

---

## WORKER FACE

### THE CELL

The npm limb of the package intake route (`org/devices/intake/`, built by `CT-cc-1` and `CT-cd-1`) assumes every npm tarball's top-level folder is literally `package/`. npm and bun do NOT assume that: they strip the FIRST path component of a tarball whatever its name. The 50-package batch for dell1 (`intake-20261016-npm-mcportal-bun`, held in `C:/opal-intake/holding/intake-20261016-npm-mcportal-bun/`; its records are merged in `org/devices/intake/records/intake-20261016-npm-mcportal-bun/`) shows it: five DefinitelyTyped tarballs fail check 2 (identity, never waivable) with `package/package.json is absent or unreadable (absent)`: `types__bun-1.4.2.tgz` (top folder `bun/`), `types__estree-1.0.9.tgz` (`estree/`), `types__node-24.13.6.tgz` (`node v24.13/`: a folder name with a SPACE), `types__react-dom-19.3.0.tgz` (`react-dom/`), `types__react-19.3.0.tgz` (`react/`). The other 45 use `package/`. The sha512 of all 50 equals the lockfile's: the defect is the TOOL's, not the packages'. The same assumption would make the install verb refuse or mis-place those five on dell1. Read the issuer's finding: `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/2.0.0_SA_COO~C/NPM_BATCH_EARLY_FINDING_TOPDIR_20261016.md`.

Where the literal `package` sits (read each place whole before you change it; line numbers are at the base and may drift by a few): `org/devices/intake/intake_check.py` (the member listing that finds `package/package.json`, about lines 1030-1190, `check_2_npm` about lines 1264-1313, and the native/restriction names such as `package/esbuild.exe` that check 6 records) and `org/devices/intake/intake_receive.py` (the member-safety test about lines 517-570 that REFUSES a member whose first component is not `package`, and the unpack that removes the leading `package/`, about lines 572-623).

THE RULE TO BUILD (one shared function, used by check, verify and install, so the three never disagree):

- The tarball's PACKAGE ROOT is its single top-level folder, whatever its name. A tarball is REFUSED (a stated reason) when it has NO top-level folder (a member at the archive root), MORE THAN ONE distinct first component, an absolute first component, a first component that is `.` or `..`, a backslash or a drive-qualified name, or a first component that is itself not a directory (a file at the root). A folder name with a space, a dot, a version string (`node v24.13`) or any other ordinary character is accepted as written.
- Check 2 (identity) reads `<root>/package.json` and compares name and version exactly as today; the failure text names the root it looked in. The `package.json` must be directly under the root (never one level deeper).
- The member-safety test (absolute, `..`, link that leaves the package, oversize) is unchanged except that "inside the package folder" now means "inside the one root".
- The install verb removes the one root component (whatever its name) when it writes `<target>/<name>@<version>@@@1/`, writing into the same temporary sibling then renaming as today; a root with a space still lands at the correct destination and the destination name never contains the root's name.
- Check 6's recorded names of natives and restrictions use the real member path (`<root>/esbuild.exe`), so for the 45 `package/` tarballs they read exactly as before (the existing records and `NPM_BATCH_FACTS.md` lines stay byte-true for them).
- `--ecosystem pypi` (default) is byte-identical to today.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **The shared root function** and its use in `intake_check.py` and `intake_receive.py` as above. One function; the three callers import or share it (the intake folder's own style; do not add a package).
2. **A NEW test file** `org/devices/intake/test_intake_npm_topdir.py` (temporary folders only; tarballs built in the test with `tarfile`; ASCII; last line `INTAKE-NPM-TOPDIR arms=<k>/<n> ok=<True|False>`). Arms: (a) a tarball whose root is `package/` still passes check 2 and installs (a control that the 45 are unchanged); (b) a root `react/` passes check 2 and installs; (c) a root `node v24.13/` (a space) passes check 2, verifies and installs, and the destination is `<name>@<version>@@@1/` with no root name in it; (d) a scoped name (`@types/react`) with root `react/` lands at `<target>/@types/react@19.3.0@@@1/`; (e) NO root (a member at the archive root) is refused by check 2, by verify and by install, and install writes nothing; (f) TWO roots (`a/package.json` and `b/x`) refused the same three ways; (g) an absolute first component and a `..` first component refused, nothing written; (h) a file at the root where the folder should be refused; (i) **the REAL precheck reads them**: after installing a 3-package pack whose roots are `package`, `react`, `node v24.13`, run `python infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py <synthetic bun.lock> <scratch cache>` as a subprocess and require `3 of 3` and exit 0, and the same script `0 of 3` and exit 1 on an empty cache (the independent oracle; you may RUN that script, not edit it); (j) a mutant that keeps the literal `package` assumption makes arm (b) read refused and the arm fail (state the mutant in the test and show it reading ok=False); (k) check 6 names a native at `<root>/<file>` for a root other than `package`. Reuse the helpers of `test_intake_npm_install.py` / `test_intake_npm.py` where they exist.
3. **Re-run `check` for the real batch, read-only against the held files.** The CLI route is the one `CT-ce-1` used for the batch (read `org/devices/intake/README.md` and `intake_check.py --help`; the existing `*.check.json` records show the shape). Re-run it for the FIVE failing files only (`types__bun-1.4.2.tgz`, `types__estree-1.0.9.tgz`, `types__node-24.13.6.tgz`, `types__react-dom-19.3.0.tgz`, `types__react-19.3.0.tgz`) so their records in the worktree's `org/devices/intake/records/intake-20261016-npm-mcportal-bun/` carry the new verdicts, and commit those five record files; do NOT touch the other 45 records, the fetch records or the held files. The held folder must be byte-unchanged: print sha256 of every file in `C:/opal-intake/holding/intake-20261016-npm-mcportal-bun/` before and after and report `unchanged 50 of 50`. NO check-2 waiver, NO check-8 signature, NO release, pack, verify or install against the real folder or the real cache, no network request.
4. **The facts file.** `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NPM_BATCH_FACTS.md` (written by the previous cell from the records) says check 2 failed for those five. Change ONLY what the five re-run records change (their c2 cells, the failed-checks section and its total, the header count of failed checks), by the same wording; the lifecycle and native sections stay as they are. Then `python .tools/tests/test_round30_npm_batch.py --natives` must still end `ok=True`.
5. **The page:** one short paragraph in `org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md`, in its own style, stating the package-root rule and the refusals (extend `.tools/tests/test_round28_intake_page.py` only if you add graded blocks).
6. **Neighbours.** At the base and after, report the whole last line of: `org/devices/intake/test_intake_npm.py` (13/13), `test_intake_npm_packument.py`, `test_intake_npm_install.py`, `test_intake_fetch.py`, `test_intake_check.py`, `test_intake_receive.py`, `test_intake_closure.py`, `test_intake_seam.py`, `.tools/tests/test_round28_intake_page.py`, `.tools/tests/test_round27_waiver.py`, `.tools/tests/test_round28_check6_platform.py`, and `python .tools/tests/test_round30_npm_batch.py --fetch --check --natives`.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~150/`. Every experiment runs in a temporary folder with a scratch cache; NEVER write under the real `~/.bun` or `C:/opal-intake/` (the held folder is read, never written). NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W150-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. NO request of any kind to the public internet. The `portal` gitlink in your worktree may show modified: do not commit it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcf1-AC1" cell_refs="CT-cf-1"><invocation>python org/devices/intake/test_intake_npm_topdir.py</invocation><expect>ok=True</expect></criterion>
`CTcf1-AC1` -- check 2, verify and install take the tarball's single top-level folder as the package root whatever its name (a space included), refuse none, many, absolute, `..` and file-at-root, and dell1's OWN precheck reads the installed pack `3 of 3` (base: the test does not exist); report the whole last line with its denominator and the precheck's own output.

<criterion id="CTcf1-AC2" cell_refs="CT-cf-1"><invocation>python .tools/tests/test_round30_npm_batch.py --check</invocation><expect>failed_total=0</expect></criterion>
`CTcf1-AC2` -- the batch's check records read zero failed checks once the five @types records are re-run (base: `NPM-BATCH-CHECK tarballs=50 checks_run_each=7 failed_total=5 ... ok=True`); report the whole last line and the held-folder `unchanged 50 of 50` line.

<criterion id="CTcf1-AC3" cell_refs="CT-cf-1"><invocation>python org/devices/intake/test_intake_npm.py</invocation><expect>INTAKE-NPM arms=13/13 ok=True</expect></criterion>
`CTcf1-AC3` -- the existing npm suite still reads 13 of 13 (base: `INTAKE-NPM arms=13/13 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTcf1-AC1,CTcf1-AC2,CTcf1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~150/NFRA_CTLPLN.TO-CT-cf-1.intake-npm-tarball-top-folder-whatever-its-name.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTcf1-AC1,CTcf1-AC2,CTcf1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cf-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_check.py
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_npm_topdir.py
org/devices/intake/test_intake_npm.py
org/devices/intake/test_intake_npm_install.py
org/devices/intake/test_intake_npm_packument.py
org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md
org/devices/intake/records/intake-20261016-npm-mcportal-bun/types__bun-1.4.2.tgz.check.json
org/devices/intake/records/intake-20261016-npm-mcportal-bun/types__estree-1.0.9.tgz.check.json
org/devices/intake/records/intake-20261016-npm-mcportal-bun/types__node-24.13.6.tgz.check.json
org/devices/intake/records/intake-20261016-npm-mcportal-bun/types__react-dom-19.3.0.tgz.check.json
org/devices/intake/records/intake-20261016-npm-mcportal-bun/types__react-19.3.0.tgz.check.json
org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~149/NPM_BATCH_FACTS.md
.tools/tests/test_round28_intake_page.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request: temporary folders for the tests; the five real held tarballs are only read by the intake check.
comp-adversary: RUN -- a tarball with no top folder, two top folders, an absolute or `..` first component or a file at the root accepted as a package (refused three ways: arms e-h); a folder name with a space mis-placed at the destination (arm c, and the real precheck as the oracle in arm i); the literal-`package` assumption left in one of the three callers (the three share one function; mutant arm j); the 45 `package/` tarballs' records or names changed (arm a, only five records touched, the facts file's lifecycle and native sections unchanged); the held folder written (sha256 before and after, 50 of 50); a check-2 waiver used to get past the failure (forbidden: identity is never waivable); BLIND: the install verb against dell1's real cache with a real `@types` tarball is unproven until SC1's real run.
risk: LOCAL -- tool changes, tests in temporary folders, five check records re-run read-only against held files; nothing is fetched, released, moved, sent or installed for real.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE). The five record files and the facts file are the previous cell's outputs, changed only as the re-run changes them.
</preflight>

Base checks, dry-run by the issuer before the cut: CTcf1-AC1 FAIL as expected (the test does not exist); CTcf1-AC2 FAIL as expected (`failed_total=5`); CTcf1-AC3 PASS as expected (control: `INTAKE-NPM arms=13/13 ok=True`).
Source: the issuer's early finding `NPM_BATCH_EARLY_FINDING_TOPDIR_20261016.md` and the CT-ce-1 facts file.
