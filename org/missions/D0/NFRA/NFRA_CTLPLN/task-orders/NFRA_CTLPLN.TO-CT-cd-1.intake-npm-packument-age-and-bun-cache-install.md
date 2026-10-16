# TO NFRA_CTLPLN.TO-CT-cd-1.intake-npm-packument-age-and-bun-cache-install -- workstream OUTCOME round 32 (cell CT-cd-1): the npm limb's second half: check 4 reads the packument's publish time (CTO addendum 3, row W147-S1) and a bun-cache install verb places each verified tarball as an unpacked name@version@@@1/ directory that dell1's own precheck reads as present

<to_id>NFRA_CTLPLN.TO-CT-cd-1.intake-npm-packument-age-and-bun-cache-install</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~148</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-148 @f634082740) and again in the main tree after merge 888087920b: CTcd1-AC1 INTAKE-NPM-PACKUMENT arms=4/4 ok=True (the too-new release reads check 4 failed with age_days=2.0 and no waiver; a packument with no time[version] or a different integrity is refused before any tarball request; the mutant ignoring the time is detected); CTcd1-AC2 INTAKE-NPM-INSTALL-TEST arms=9/9 ok=True (dell1's OWN precheck, run as a subprocess on the installed scratch cache, reads `3 of 3` rc=0; on an empty cache `0 of 3` rc=1; the mutant without package.json reads `0 of 3`); CTcd1-AC3 INTAKE-FETCH-TEST cases=21/21 ok=True; proof VALID. Neighbouring suites green in the main tree: INTAKE-NPM 13/13, INTAKE-CHECK-TEST 60/60, INTAKE-RECEIVE-TEST 36/36, INTAKE-CLOSURE-TEST 10/10, INTAKE-SEAM-TEST 6 stages 4/4, INTAKE-PAGE 13 blocks 10 accepted 35 refused, WAIVER 20/20, CHECK6-PLATFORM 14/14. The verb: `intake_receive.py install --ecosystem npm --pack <dir> --target <bun cache> --lockfile <bun.lock>` (the lockfile is required because verify needs it: W148-S3); refuses the whole pack if any tarball or destination fails; unpacks into <name>@<version>@@@1/ via a temporary sibling then rename; an already-present destination is left untouched, an incomplete one refused; never runs a lifecycle script or bun; writes a receipt (default <pack>/receipts/). dell1's CTO named the unpacker (call 333b): 0.7.0_AE_CloudOps~SC1 runs it in its HVST-cc-7 order after re-checking each sha512 against the bun.lock. Row W147-S1 disarmed by the evidence of arm (b) (the disarm record is the CTO's, the row is append-only). Rows W148-S1..S5 OBSERVATION, INERT (S4: the precheck's total is host-filtered while the install's present counts every packed tarball: dell1's win32 binaries count on a Windows host). Not read: dell1's own cache (out of reach by rule). LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>32</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-cd-1` (`decompositions/NFRA_CTLPLN_DECOMP.round29.md`) | **outcome_ref:** the intake route (C-INTAKE); no FWD (the npm limb for dell1's 50 bun packages) |
**depends_on:** CT-cc-1 (merged 867c77705c)

---

## WORKER FACE

### THE CELL

Cell `CT-cc-1` (merged `867c77705c`) built the npm limb of the package intake route: `--ecosystem npm`, fetch from `registry.npmjs.org` only, two independent sha512 sources, lifecycle scripts listed, native binaries named, check 8 with `NATIVE`/`LIFECYCLE` lines, pack and verify, proven against a loopback registry. Two things remain before the batch (dell1's 50 bun packages for the mcportal dashboard build, the next cell):

1. **Check 4 reads the packument (the CTO's ADDENDUM 3, ruling of W147-S1).** Read it whole: `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md` (ADDENDUM 3 @3466da2bcd). The version document carries no publish time, so `CT-cc-1`'s check 4 reads `failed` and needs a waiver. The CTO ruled: the fetch ALSO reads `https://registry.npmjs.org/<name>` (the packument; same host, scoped names URL-encoded the same way) and check 4 takes `time[<version>]` as the publish time and measures the release age and the earlier-release facts as it does for PyPI (read `check_4` and `check_4_npm`). Two additions: the packument's `versions[<version>].dist.integrity` must EQUAL the version document's `dist.integrity`, or the file is REFUSED (a registry that tells two stories); and a packument with NO `time[<version>]` is REFUSED. NO check-4 waiver for this batch: check 4 reads passed or failed on measured facts, and a failure stays a refusal unless the CTO writes a `WAIVE <file> check 4` line (the existing waiver machinery is unchanged; the cell adds no new waiver). Row `NFRA_CTLPLN-W147-S1` disarms on the test of arm (b) below.
2. **A bun-cache install verb (the CTO's ruling item 5, with dell1's cache facts).** dell1 answered (MSTR msg 109742, `org/tier0_exec/0.0.0_AB_MSTR/deliverables/DELL1_BUN_CACHE_DETAILS_ANSWER_20261016.md`; read it): bun's cache holds UNPACKED packages in directories named `<name>@<version>@@@1/` (a scoped package keeps its slash: `@alloc/quick-lru@5.2.0@@@1/`) under `~/.bun/install/cache` (on dell1 `C:\Users\Test\.bun\install\cache`); `infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py <bun.lock> [<cache dir>]` (166 lines, in THIS repository: read it whole) counts a package `present` only when `<cache>/<name>@<version>@@@1` exists, is non-empty, and holds a `package.json` that parses with the SAME name and the EXACT version; it prints `<present> of <total>` and exits 0 only when nothing is missing; a bare `.tgz` does not count. dell1's CTO answers the question of WHO unpacks on call `XB-20261016T175819Z-333b`; the verb you build is generic (it unpacks into a `--target` directory) and is run by whoever the CTO names, on the box that holds the cache.

Read first: `org/devices/intake/` whole as in `CT-cc-1` (README, `APPROVAL_AND_SIGNED_FILE_DEMANDS.md`, `intake_fetch.py`, `intake_check.py`, `intake_receive.py`, `test_intake_npm.py` (13 arms, which must stay green and may need its fixture registry to serve a packument: change it only as far as that), `test_intake_fetch.py`, `test_intake_check.py`, `test_intake_receive.py`), and the precheck script above.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. A tool that reads the repository and finds a folder missing may print a SHORT result with exit 0 (row W137-S1): read the denominator a tool prints, and add the folder before you trust a zero.

### BUILD

1. **Packument read in the fetch (`intake_fetch.py`, npm mode):** after the version document and before the tarball, GET the packument from the same registry host (the base override for the loopback registry still applies), record its `time[<version>]`, `time.created` and the published version list's `time` entries needed by `check_4_npm` in the fetch record; refuse (with a stated reason, no tarball request) when the packument is unreadable, lacks `time[<version>]`, or its `versions[<version>].dist.integrity` differs from the version document's. A host other than `registry.npmjs.org` stays refused before a request.
2. **Check 4 (`intake_check.py`, `check_4_npm`):** measure the release age from `time[<version>]` against the same threshold the PyPI check uses (`--min-age`, default 14 days) and the earlier-releases rule from the packument's other versions' `time` entries (read how PyPI's check counts `release_count`), pass or fail on those facts with the same evidence shape; it no longer reads failed merely for lack of a source.
3. **The install verb (`intake_receive.py install --ecosystem npm --pack <pack dir> --target <bun cache dir> [--by <serial>]`):**
   - it refuses a pack that is not a verified npm pack (run the same verification as `verify` first; one failed file refuses the whole install and writes nothing);
   - for each `.tgz`, unpack IN MEMORY-SAFE FASHION (refuse an absolute member, a `..` member, a link that leaves the package, a member over a sane size) into `<target>/<name>@<version>@@@1/` with the leading `package/` directory removed, written first into a temporary sibling folder and then renamed into place (a half-unpacked directory is never visible); a scoped name keeps its slash as a directory (`<target>/@scope/<name>@<version>@@@1/`);
   - a destination that is ALREADY present by the precheck's own definition is left untouched and reported `already`; a destination that exists but is NOT present (empty, no manifest, version mismatch) is REFUSED, never overwritten (the issuer or dell1 decides);
   - after unpacking it applies the precheck's `present` definition to every package of the pack (reuse the logic: load `bun_cache_precheck.py` by path, or restate its rule and test that the two agree on the same cache) and prints one line per package and a last line `INTAKE-NPM-INSTALL tarballs=<k> unpacked=<u> already=<a> refused=<r> present=<p>/<k> ok=<True|False>`; it writes an install receipt (JSON, ASCII, one file in a `--receipt-dir` or beside the pack: each package's unpack result and the sha256 of its `package.json`), never executes a lifecycle script, never runs `bun` or any package manager, and opens no socket.
   - `--ecosystem pypi` (default) is byte-identical to today.
4. **Tests.** A NEW file `org/devices/intake/test_intake_npm_packument.py` (temporary folders; loopback registry; ASCII; last line `INTAKE-NPM-PACKUMENT arms=<k>/<n> ok=<True|False>`) with arms: (a) the packument is read from the loopback registry; check 4 passes on a packument whose `time[<version>]` is old enough with earlier releases, and FAILS on a too-new release with the measured age in the evidence (no waiver involved); (b) a packument with NO `time[<version>]` is REFUSED (this disarms `W147-S1`); (c) a packument whose `dist.integrity` differs from the version document's is REFUSED with zero tarball requests; (d) a mutant that ignores the packument time makes arm (a)'s too-new case pass and the arm fails. A SECOND NEW file `org/devices/intake/test_intake_npm_install.py` (temporary folders only; loopback registry; ASCII): (e) install of a 3-package pack (one scoped) lands `<name>@<version>@@@1/` directories with `package.json` that parse; (f) **the REAL precheck reads them**: run `python infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py <synthetic bun.lock> <scratch cache>` as a subprocess and require its output `3 of 3` and exit 0 (the independent oracle: your own present check is not the grader), and require the SAME script to read `0 of 3` and exit 1 on an empty cache (negative control); (g) a pack with one tarball whose sha512 differs from its record is refused and NOTHING is written to the target; (h) a `..` member and an absolute member are refused; (i) an already-present directory is left byte-identical (compare mtimes and bytes) and reported `already`; (j) an existing empty directory at a destination is refused, not overwritten; (k) a run twice is idempotent; (l) a lifecycle script in the package is NOT executed (plant a postinstall that would write a marker; the marker never appears); (m) control: a mutant that writes the files but no `package.json` makes arm (f) read `2 of 3` or fewer. Last line `INTAKE-NPM-INSTALL-TEST arms=<k>/<n> ok=<True|False>`.
5. **The page:** add the install verb and the packument rule to `APPROVAL_AND_SIGNED_FILE_DEMANDS.md` in its own style (keeping its graded examples green: extend `.tools/tests/test_round28_intake_page.py` only if you add graded blocks).
6. **Neighbours.** At the base and after: `test_intake_npm.py` (13/13), `test_intake_fetch.py`, `test_intake_check.py`, `test_intake_receive.py`, `test_intake_closure.py`, `test_intake_seam.py`, `.tools/tests/test_round28_intake_page.py`, `.tools/tests/test_round27_waiver.py`, `.tools/tests/test_round28_check6_platform.py`: report base and after last lines.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~148/`. Every experiment runs in a temporary folder with a loopback registry and a scratch bun cache; NEVER write under the real `~/.bun` or `C:/opal-intake/`. NO network request, no `pip`, no install. No push, no deploy, no AWS write, no `terraform` command. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W148-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. When your own change turns a neighbouring suite red, say so in your report with the suite's whole last line: the issuer re-runs every suite that imports what you changed at the merge. NO request of any kind to the public internet (no `registry.npmjs.org`, no `pypi.org`): a public host in a request log is a failure of the cell. You may RUN `infra/aws/ec2/opal-gateway/ops/bun_cache_precheck.py` (it opens no socket and runs no bun); you may NOT edit it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTcd1-AC1" cell_refs="CT-cd-1"><invocation>python org/devices/intake/test_intake_npm_packument.py</invocation><expect>ok=True</expect></criterion>
`CTcd1-AC1` -- check 4 reads the packument's publish time and passes or fails on measured facts with no waiver; a packument with no `time[<version>]` or with a different integrity is refused before any tarball request (base: the test does not exist; the existing `test_intake_npm.py` reads `INTAKE-NPM arms=13/13 ok=True` and must stay green); report the whole last line with its denominator.

<criterion id="CTcd1-AC2" cell_refs="CT-cd-1"><invocation>python org/devices/intake/test_intake_npm_install.py</invocation><expect>ok=True</expect></criterion>
`CTcd1-AC2` -- a verified npm pack is placed as unpacked `name@version@@@1/` directories that dell1's OWN precheck reads `3 of 3` present, nothing is written for a failed file, an unsafe member or an incomplete destination, and no lifecycle script runs (base: the test does not exist); report the whole last line with its denominator and the precheck's own output.

<criterion id="CTcd1-AC3" cell_refs="CT-cd-1"><invocation>python org/devices/intake/test_intake_fetch.py</invocation><expect>INTAKE-FETCH-TEST cases=21/21 ok=True</expect></criterion>
`CTcd1-AC3` -- the PyPI fetch behaves exactly as before (base: `INTAKE-FETCH-TEST cases=21/21 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTcd1-AC1,CTcd1-AC2,CTcd1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~148/NFRA_CTLPLN.TO-CT-cd-1.intake-npm-packument-age-and-bun-cache-install.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTcd1-AC1,CTcd1-AC2,CTcd1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round30.md</decomp_doc>
<owned_cells>CT-cd-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_fetch.py
org/devices/intake/intake_check.py
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_npm.py
org/devices/intake/test_intake_npm_packument.py
org/devices/intake/test_intake_npm_install.py
org/devices/intake/APPROVAL_AND_SIGNED_FILE_DEMANDS.md
.tools/tests/test_round28_intake_page.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request: a loopback registry and a scratch cache in temporary folders; the real precheck script is run read-only.
comp-adversary: RUN -- a registry that tells two stories (the packument's integrity must equal the version document's: arm c); a missing publish time read as old (REFUSED: arm b); a half-unpacked directory visible to bun (temporary sibling then rename; arm e and the mutant of arm m); a destination overwritten (an incomplete one is refused, a complete one untouched: arms i, j); an unsafe member written (arm h); a lifecycle script run (arm l); the cell grading itself (arm f runs dell1's own precheck as the oracle, with a negative control); a PyPI regression (the default byte-identical, AC3 and the neighbouring suites); writing the real cache (forbidden: temporary folders only); BLIND: who unpacks on dell1 is its CTO's design (call 333b): this verb is generic and unproven against dell1's real cache until its first real run; the real registry is first read by the batch cell.
risk: LOCAL -- tool changes and tests against a loopback registry and a scratch cache; nothing is fetched, released, moved, sent or installed for real.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the design (npm limb ruling addenda 2 and 3, msgs 109738 and 109746).
</preflight>

Base checks, dry-run by the issuer before the cut: CTcd1-AC1 FAIL as expected (the test does not exist; control: `INTAKE-NPM arms=13/13 ok=True` for the existing suite); CTcd1-AC2 FAIL as expected (the test does not exist); CTcd1-AC3 PASS as expected (control: `INTAKE-FETCH-TEST cases=21/21 ok=True`).
Source: CTO npm-limb ruling addenda 2 and 3 (msgs 109738, 109746); dell1's bun cache answer (MSTR msg 109742); rows W147-S1 and W147-S2.
