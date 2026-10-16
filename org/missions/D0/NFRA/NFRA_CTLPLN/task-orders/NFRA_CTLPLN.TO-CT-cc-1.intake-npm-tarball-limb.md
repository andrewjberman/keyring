# TO NFRA_CTLPLN.TO-CT-cc-1.intake-npm-tarball-limb -- workstream OUTCOME round 31 (cell CT-cc-1): the package intake route gains an npm-tarball limb (ecosystem npm): request, fetch from registry.npmjs.org only, checks with two independent integrity sources, check 8, pack and verify, proven against a loopback registry (the first batch is dell1's 50 bun packages; the batch itself is the next cell)

<to_id>NFRA_CTLPLN.TO-CT-cc-1.intake-npm-tarball-limb</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~147</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-147 @ec21f8e6fc) and again in the main tree after merge 867c77705c: CTcc1-AC1 INTAKE-NPM arms=13/13 ok=True; CTcc1-AC2 INTAKE-FETCH-TEST cases=21/21 ok=True; CTcc1-AC3 INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True; proof VALID. Neighbouring suites green in the main tree: INTAKE-RECEIVE-TEST 36/36, INTAKE-CLOSURE-TEST 10/10, INTAKE-SEAM-TEST 6 stages 4/4, INTAKE-PAGE blocks=13 accepted=10 refused=35 (7/5/21 at the base: the new npm blocks), WAIVER 20/20, CHECK6-PLATFORM 14/14. The limb: --ecosystem npm (default pypi, byte-identical): approval line name@version, fetch from registry.npmjs.org only (the version document, then dist.tarball on that host; --registry-base only for a loopback registry; a foreign tarball host refused before a request), sha512 equal to BOTH the registry's dist.integrity and the lockfile's (the lockfile mandatory), name and version inside package.json, lifecycle scripts listed, native binaries named, in-memory tar reading, check 8 with NATIVE and LIFECYCLE lines, release and pack of .tgz only, verify. Worker deviations accepted: check 4 reads FAILED with a stated reason (waivable) because the version document carries no publish time (row W147-S1, ARMED, owner the CTO: name the release-age source or rule a per-file WAIVE check 4 the accepted state before the next cell signs its batch); check 1 also compares dist.shasum when published; --index-base is refused with npm; prove and install stay PyPI-only. Rows W147-S2..S4 OBSERVATION, INERT. NOT in the cell: the real fetch of the 50 tarballs, the placement into dell1's bun cache and dell1's precheck. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>31</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cc-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** the intake route (C-INTAKE); no FWD (an inbound ask from dell1 via MSTR msg 109737, ruled by the CTO msg 109738) |
**depends_on:** none

---

## WORKER FACE

### THE CELL

The package intake route (`org/devices/intake/`: request, approve, fetch, checks 1-7, signed check 8, release, pack, verify, send) takes Python WHEELS from PyPI only (`intake_fetch.py` lines ~44-45: `PUBLIC_BASE = "https://pypi.org"`, hosts `pypi.org` and `files.pythonhosted.org`, every file must end `.whl`, lines ~96 and ~529). dell1's `AMGT_HARVST` (HVST-cc-7, row D1-S36) needs 50 npm packages for the mcportal dashboard build; its fallback waits on this intake. The CTO ruled (read WHOLE: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md`, with its addenda 1 and 2, msg 109738): YES, extend the route, as ONE limb on the same journey and the same records; no side door. THIS cell builds the limb and proves it against a LOOPBACK registry; the real fetch of the 50 tarballs is the NEXT cell (after the CTO signs). Your cell fetches NOTHING from the public internet.

Read first, whole: `org/devices/intake/README.md` and `APPROVAL_AND_SIGNED_FILE_DEMANDS.md`, then `intake_request.py`, `intake_fetch.py`, `intake_check.py`, `intake_receive.py`, `intake_closure.py` (the closure tool is PyPI-only and stays so: npm needs no closure here, the approved list IS the lockfile's closure), and the tests `test_intake_fetch.py`, `test_intake_check.py`, `test_intake_receive.py`, `test_intake_seam.py`. A bun lockfile example is `portal/bun.lock` in this repository (the real lockfile of mcportal@c66ca82952 is supplied by the issuer in the next cell).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### THE DESIGN (the CTO's ruling, pinned; implement it, do not redesign)

An ecosystem switch `--ecosystem pypi|npm` (default `pypi`) on every verb that touches a package (`request`, `fetch`, `check`, `release`, `pack`, `verify`, the receive verbs). With `pypi` EVERY existing behaviour, output line and record stays byte-identical (the existing suites are the control). With `npm`:

1. **Approval line.** `<name>@<version>` exactly (a scoped name is written whole: `@babel/core@7.29.7`); the fetch refuses any requested package whose line is absent from the approval file, exactly as `name==version` does today, and makes no request on a refusal.
2. **Fetch.** ONLY `https://registry.npmjs.org/<name>/<version>` (a scoped name is URL-encoded: `@babel%2Fcore`), then THAT document's `dist.tarball`, which must be on host `registry.npmjs.org`; any other host is refused before a request. `--registry-base` overrides the base for a LOOPBACK test registry only (as `--index-base` does for PyPI). ONE `.tgz` goes into `holding/<batch>/` unchecked, with a fetch record (the same record shape as a wheel's: the file name, sha256, size, the registry document's `dist.integrity` and `dist.shasum`, the URL). The held file name is `<name-with-@-removed-and-/-as-__>-<version>.tgz` (for example `babel__core-7.29.7.tgz`); document the rule in the page.
3. **Checks** (`intake_check.py`, npm mode; in each existing check's place, same record shape, same verdict vocabulary; checks 1 and 2 stay never-waivable):
   - **digest:** the tarball's sha512 (base64, as `sha512-<b64>`) equals the registry document's `dist.integrity`, AND equals the integrity string for that `name@version` in the lockfile given by `--lockfile <path>` (two INDEPENDENT sources: a bun text lockfile entry looks like `"name": ["name@version", "<registry>", {deps}, "sha512-..."]`; read the real shape from `portal/bun.lock` and match by the `name@version` first element). A missing `--lockfile` in npm mode is a refusal, never a skip;
   - **identity:** `package/package.json` inside the tarball names the requested `name` and `version`;
   - **lifecycle scripts:** `preinstall`, `install`, `postinstall` (and `prepare` if present) are LISTED in the record, never executed;
   - **native binaries:** any member ending `.node`, `.exe`, `.dll`, `.so` or `.dylib`, and any package whose `package.json` carries `os` or `cpu` restrictions, is NAMED in the record (for example `@esbuild/win32-x64`, `@rollup/rollup-win32-x64-gnu`, `@rollup/rollup-win32-x64-msvc`);
   - unsafe member names (absolute, `..`, links leaving the package), a tarball bomb (more than 200 MB expanded or 20000 members), and a non-gzip file FAIL; nothing is extracted to disk during the checks (read the tar in memory).
   The wheel-only checks (platform tags, `.py` byte compare, RECORD) are `not_applicable` with a reason in npm mode.
4. **Check 8** (the CTO's signed file, same rules as today: under the signer directory, names the batch and EVERY tarball file name, the `CHECK 8 SIGNED` marker): in npm mode a tarball that lists a lifecycle script or names a native binary additionally needs ITS OWN line `NATIVE <file name>: <reason>` or `LIFECYCLE <file name>: <reason>` in the signed file, or check 8 reads failed naming the missing line. The waiver form `WAIVE <file> check <N>: <reason>` works as today (never checks 1 or 2).
5. **Release, pack, verify:** the same hops, the pack carries the `.tgz` files, their records and the manifest; `intake_receive.py verify` in npm mode re-reads each tarball against its record and the lockfile entry and prints the same last-line shape (`INTAKE-VERIFY pack=... wheels=.. ` becomes the npm analogue with `tarballs=`; keep the PyPI line byte-identical).
6. **NOT in this cell:** the placement of the tarballs into dell1's bun cache and dell1's `ops/bun_cache_precheck.py` reading `77 of 77 present` (that is dell1's side: the issuer has asked dell1 how its cache lays packages out and what `present` reads; the receive-and-place verb is cut after dell1 answers). Do NOT write a placement step; verify stops at the pack.

### BUILD

Implement the design with the least change to each tool (a `--ecosystem` branch, not a rewrite). Then:

1. **The test**, a NEW file `org/devices/intake/test_intake_npm.py` (standard library plus the tools; a LOOPBACK registry served from a temporary folder in-process on 127.0.0.1; synthetic tarballs built with `tarfile` and `gzip`; a synthetic `bun.lock` in the real shape; temporary holding/records folders; no network; ASCII output) with arms: (a) a happy path for an unscoped and a scoped package: request, fetch, checks 1-7 all passed or not_applicable, sha512 equals both sources; (b) a name absent from the approval file is refused and the loopback registry reports ZERO requests; (c) a `dist.tarball` on another host is refused with zero tarball requests; (d) a tarball whose sha512 differs from the lockfile is refused at the digest check (the registry's integrity matching it); (e) a tarball whose sha512 differs from the registry's `dist.integrity` is refused; (f) a missing `--lockfile` is a refusal; (g) a `package.json` naming another version fails identity; (h) a tarball with a `postinstall` script lists it, and with a `.node` member or an `os`/`cpu` field names the native binary; (i) check 8: such a tarball with only the batch line reads failed, with its `NATIVE` or `LIFECYCLE` line passes; (j) an unsafe member name and a non-gzip file fail; (k) pack and verify round trip; (l) with `--ecosystem pypi` (default) a wheel flows exactly as before (compare with the existing test's fixtures, one arm); (m) controls: a mutant that skips the lockfile comparison makes arm (d) fail. Last line `INTAKE-NPM arms=<k>/<n> ok=<True|False>`.
2. **The page and README:** add the npm form to `APPROVAL_AND_SIGNED_FILE_DEMANDS.md` (the approval line, the held file name rule, the `NATIVE`/`LIFECYCLE` lines) in the page's own style, keeping its examples graded by `.tools/tests/test_round28_intake_page.py` (extend that test's blocks for the new examples; it must stay green), and one README line.
3. **Neighbours.** The existing suites stay green and the PyPI behaviour byte-identical: run at the base and after `test_intake_fetch.py`, `test_intake_check.py`, `test_intake_receive.py`, `test_intake_closure.py`, `test_intake_seam.py` and `.tools/tests/test_round28_intake_page.py`, `.tools/tests/test_round27_waiver.py`, `.tools/tests/test_round28_check6_platform.py`; report base and after last lines (a base value is learned first; a suite red at the base stays red and is listed).

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~147/`. Every experiment runs in a temporary folder with a loopback registry; NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W147-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. NO request of any kind to the public internet (no `registry.npmjs.org`, no `pypi.org`): a public host appearing in a request log is a failure of the cell.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcc1-AC1" cell_refs="CT-cc-1"><invocation>python org/devices/intake/test_intake_npm.py</invocation><expect>ok=True</expect></criterion>
`CTcc1-AC1` -- the npm limb fetches only from the registry host, refuses an unapproved name, a foreign tarball host, a sha512 that differs from either the registry or the lockfile, and a missing lockfile; lists lifecycle scripts, names native binaries, and requires their own lines in check 8 (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTcc1-AC2" cell_refs="CT-cc-1"><invocation>python org/devices/intake/test_intake_fetch.py</invocation><expect>INTAKE-FETCH-TEST cases=21/21 ok=True</expect></criterion>
`CTcc1-AC2` -- the PyPI fetch behaves exactly as before (base: `INTAKE-FETCH-TEST cases=21/21 ok=True`, a control); report the whole last line.

<criterion id="CTcc1-AC3" cell_refs="CT-cc-1"><invocation>python org/devices/intake/test_intake_check.py</invocation><expect>INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True</expect></criterion>
`CTcc1-AC3` -- the PyPI checks behave exactly as before (base: `INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTcc1-AC1,CTcc1-AC2,CTcc1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~147/NFRA_CTLPLN.TO-CT-cc-1.intake-npm-tarball-limb.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTcc1-AC1,CTcc1-AC2,CTcc1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cc-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_request.py
org/devices/intake/intake_fetch.py
org/devices/intake/intake_check.py
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_npm.py
org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md
org/devices/intake/README.md
.tools/tests/test_round28_intake_page.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request: a loopback registry in temporary folders; nothing is fetched from the public internet.
comp-adversary: RUN -- the npm limb becoming a side door (the fetch accepts only registry.npmjs.org and the `dist.tarball` on that host, `--registry-base` is a loopback test override, arms b and c); a tarball accepted on one integrity source (arms d, e, f: both the registry's `dist.integrity` and the lockfile must match, the lockfile is mandatory); a native binary or lifecycle script passing unseen (arms h and i: listed in the record and signed by name in check 8); extraction to disk during the checks (the tar is read in memory; arm j); a PyPI regression (arm l, the existing suites and the byte-identical default); a mutant skipping the lockfile comparison (arm m); BLIND: this cell does not read dell1's bun cache layout or its precheck (asked of dell1; the placement verb is a later cell), nor does it exercise the real registry (the next cell's real fetch is the first real run).
risk: LOCAL -- tool changes and tests against a loopback registry; nothing is fetched, released, moved or sent.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the design (msg 109738).
</preflight>

Base checks, dry-run by the issuer before the cut: CTcc1-AC1 FAIL as expected (the test does not exist); CTcc1-AC2 PASS as expected (control: `INTAKE-FETCH-TEST cases=21/21 ok=True`); CTcc1-AC3 PASS as expected (control: `INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True`).
Source: CTO ruling `CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md` (addendum 2 @0c771fe5fb) and msg 109738; MSTR msgs 109730 and 109737; dell1 AMGT_HARVST HVST-cc-7 (row D1-S36).
