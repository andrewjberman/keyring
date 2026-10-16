# TO NFRA_CTLPLN.TO-CT-ar-1 -- workstream OUTCOME round 20 (cell CT-ar-1): the organic journey, step 1 -- the closure tool gains a linux x86_64 cp312 target and a single-root, host-aware form, and computes the closure of yfinance==1.2.0 for dell2's resident host (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-ar-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~130</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-130 @a3b5781814) and again in the main tree after merge 97477e8786: CTar1-AC1 LINUX-CLOSURE arms=7/7 ok=True; CTar1-AC2 INTAKE-CLOSURE-TEST cases=10/10 ok=True (base 9/9); CTar1-AC3 INTAKE-CLOSURE target=cp312-linux_x86_64 lines=1 closure=24 dependencies_added=23 pure=17 fits=0 needs_fetch=7 unknown_not_installed=0 specifier_conflicts=0 fixed_point=True ok=True host_satisfied=7 host_conflicts=0 to_fetch=17; proof VALID; the Windows closure (cp314-win_amd64, 162 members) still reads back with its stored last line; the branch changed 8 files, all inside the order's paths. The closure is computed from the LAPTOP's installed versions (24 members: yfinance 1.2.0 plus 23 dependencies; 7 left out because the host already satisfies them: cffi, charset-normalizer, pycparser, python-dateutil, six, typing_extensions, urllib3; 17 to fetch; no host conflict); whether any Linux wheel exists on the index for any member is UNREAD. Rows W130-S1 (OBSERVATION, INERT: the manylinux platform list is written out, 33 strings, because packaging reads the running host) and W130-S2 (OBSERVATION, ARMED, disarm owner this issuer: `fetchlist` hard-codes the cp314 win_amd64 suffix and names 7 Windows wheel files for the linux closure; the next cell must not use it for this closure and carries the fix). LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ar-1` (`decompositions/NFRA_CTLPLN_DECOMP.round27.md`, amendment 1) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

The first ORGANIC consumer of the package route: `2.0.0_SA_COO~G2` (dell2, IRPT_ANLREQ) asks for the closure of `yfinance==1.2.0` as wheels for its resident host (call `XB-20261016T052534Z-983c`; body `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/XB_YFINANCE_CLOSURE_REQUEST_20261016.md`: read it whole). The laptop CTO ruled YES with terms (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB983C_YFINANCE_LINUX_CLOSURE_20261016.md`: read it whole). THIS cell is the first step only: the closure tool `org/devices/intake/intake_closure.py` (read its header and `org/devices/kit_python_wheels.py` `parse_target` and `supported_tags`) computes closures for WINDOWS targets only, from the INSTALLED copies on this laptop, with NO network. You give it a LINUX target and a one-root, host-aware form, and run it once for yfinance. Nothing is fetched, requested or installed; the tool stays offline. The target (read from the host by the requester): Linux x86_64, CPython 3.12.14, glibc 2.34; wheels tagged `manylinux2014_x86_64`, `manylinux_2_17_x86_64`, `manylinux_2_28_x86_64`, `manylinux_2_34_x86_64` or `any` fit; a `musllinux` wheel does not. The host already holds 22 distributions (the body's section "Already in the host's pydeps": one line, `name version; name version; ...`).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's ruling and the call body are outside that set: add `org/tier1_exec/1.0.0_SA_CTO/deliverables` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2` to read them.

### BUILD

1. **A linux target in `kit_python_wheels.py`.** `parse_target(python_tag, platform)` accepts the platform label `linux_x86_64` for the target, with the marker environment `sys_platform=linux`, `platform_system=Linux`, `os_name=posix`, `platform_machine=x86_64`, and `supported_tags` for it expands to the platform strings `manylinux2014_x86_64`, `manylinux_2_17_x86_64`, `manylinux_2_28_x86_64`, `manylinux_2_34_x86_64` (and the earlier `manylinux_2_5..2_16_x86_64` ones that `packaging.tags` yields for those) plus `any` through the existing `packaging.tags` calls. The three Windows labels and every Windows result stay byte-identical. Change nothing else in that file.
2. **`intake_closure.py`.** `make_target('cp312-linux_x86_64')` works and sets `python_full_version` and `implementation_version` to `3.12.14` for marker evaluation (as it does `3.14.7` for cp314). The `closure` verb gains `--root <requirement line>` (one line, here `yfinance==1.2.0`; when given it REPLACES the lines of `requirements.txt` as the start) and `--host-pydeps <json>` (a file of `{"schema": "intake-host-pydeps/1", "host": ..., "python": ..., "dists": {"<normalised name>": "<version>"}}`). With `--host-pydeps`, every closure member whose normalised name is in the host file is classed: `HOST-SATISFIED` when the host version satisfies every specifier any parent puts on it (the member is OMITTED from the fetch count and printed with the host version); `HOST-CONFLICT` when it does not (printed as a STOP: the tool does not choose). The saved JSON carries both lists. Extras of the root are NOT followed (`nospam`, `repair` are excluded by the ruling). The last line keeps its existing fields and gains `host_satisfied=<n> host_conflicts=<n> to_fetch=<n>` where `to_fetch` is the closure minus the host-satisfied members (EVERY such member is fetched through the checked route: a pure-Python installed copy is NOT repacked). `ok` keeps its existing meaning; a conflict does not make it False, it is counted.
3. **The host file.** Write `org/devices/intake/records/intake-20261016-yfinance-linux/HOST_PYDEPS.json` from the body's one-line list (read the line from the body file, do not retype it by eye: parse it with a few lines of Python and print the 22 pairs back). Name the body path and its commit hash in the file.
4. **Run it once** and commit its output: `python org/devices/intake/intake_closure.py closure --target cp312-linux_x86_64 --root yfinance==1.2.0 --host-pydeps org/devices/intake/records/intake-20261016-yfinance-linux/HOST_PYDEPS.json --out org/devices/intake/closure_cp312_linux_x86_64_yfinance.json`. Keep the whole last line. Also print and keep, from the saved JSON: every member (name, installed version, class), the `HOST-SATISFIED` list with host versions, the `HOST-CONFLICT` list (a conflict is a STOP to report, never to fix), and any member classed `UNKNOWN-NOT-INSTALLED` (its dependencies are then UNREAD: name it). Do NOT guess wheel file names: whether a manylinux file exists on the index is UNREAD (a later cell reads it).
5. **A NEW test** `.tools/tests/test_round27_linux_closure.py` (standard library plus the two tools; no network; ASCII output): arms (a) `supported_tags` for `cp312-linux_x86_64` contains an `(cp312, cp312, manylinux2014_x86_64)` triple, an `(py3, none, any)` triple and NO `win_amd64` triple; (b) a marker `sys_platform == "win32"` is excluded and `sys_platform == "linux"` is included for the linux target, the reverse for `cp314-win_amd64` (control); (c) host logic on a SYNTHETIC host file and synthetic parents: a satisfied pin is `HOST-SATISFIED`, an unsatisfied pin is `HOST-CONFLICT`; (d) CONTROL: `closure --from-file org/devices/intake/closure_cp314_win_amd64.json` prints the same last line as the one stored for that file (the Windows closure is unchanged); (e) the saved yfinance JSON has the root `yfinance`, no member classed `HOST-CONFLICT` AND `HOST-SATISFIED` at once, and `to_fetch` equals the closure minus the host-satisfied count. Last line `LINUX-CLOSURE arms=<k>/<n> ok=<True|False>`.
6. `org/devices/intake/test_intake_closure.py` may gain cases for the new form (its count of 9 grows); change no existing case and no other test file.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~130/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. NO network request of any kind; no `pip` command that reaches an index; no install. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~129/NFRA_CTLPLN.TO-CT-aq-1.tabulate-pack-taildrop-to-site-z.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W130-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. Report in your final message: the closure's last line, the member list with classes, the host-satisfied and host-conflict lists with versions, and every member you could not resolve.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTar1-AC1" cell_refs="CT-ar-1"><invocation>python .tools/tests/test_round27_linux_closure.py</invocation><expect>ok=True</expect></criterion>
`CTar1-AC1` -- the linux target, the host-aware form and the unchanged Windows closure are pinned (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTar1-AC2" cell_refs="CT-ar-1"><invocation>python org/devices/intake/test_intake_closure.py</invocation><expect>ok=True</expect></criterion>
`CTar1-AC2` -- the closure tool's own suite still passes after the change (base: `INTAKE-CLOSURE-TEST cases=9/9 ok=True`, a control); report the whole last line.

<criterion id="CTar1-AC3" cell_refs="CT-ar-1"><invocation>python org/devices/intake/intake_closure.py closure --from-file org/devices/intake/closure_cp312_linux_x86_64_yfinance.json</invocation><expect>ok=True</expect></criterion>
`CTar1-AC3` -- the committed yfinance closure reads back with its last line (base: the JSON does not exist); report the whole line.
</proof_of_spec>

<expected_criteria>CTar1-AC1,CTar1-AC2,CTar1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~130/NFRA_CTLPLN.TO-CT-ar-1.closure-tool-linux-target-yfinance.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTar1-AC1,CTar1-AC2,CTar1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round27.md</decomp_doc>
<owned_cells>CT-ar-1</owned_cells>
</decomp_ref>

<paths>
org/devices/kit_python_wheels.py
org/devices/intake/intake_closure.py
org/devices/intake/test_intake_closure.py
.tools/tests/test_round27_linux_closure.py
org/devices/intake/closure_cp312_linux_x86_64_yfinance.json
org/devices/intake/records/intake-20261016-yfinance-linux/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; the tool reads installed package metadata on this machine.
comp-adversary: RUN -- a Windows result changing (arm d compares the stored last line; AC2 re-runs the suite); a Linux marker evaluated as Windows (arm b); a host-satisfied member counted for fetch (arm e and the last line); a conflict silently resolved (the tool prints it as a STOP; the face says never fix); a guessed wheel file name (the face forbids it: UNREAD); an index request slipping in through pip (no pip command reaches an index, the tool's PIP_ALLOWED list stands); BLIND: closure versions are the versions installed on THIS laptop, not what the index would pick for a Linux host (a version the host cannot satisfy shows as HOST-CONFLICT only for the 22 host members; any other member's Linux wheel availability is the next cell's read); the laptop's installed copies are Windows builds, so a member's compiled-or-pure class describes this laptop, not the host.
risk: LOCAL -- a read-only change to a closure tool and its tests, one computed JSON; no network, no install, no AWS.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/` is NFRA_CTLPLN's (C-INTAKE); `kit_python_wheels.py` is imported by the closure tool; the CTO ruled the work (XB-983c ruling @5740f0d341, term 1).
</preflight>

Base checks, dry-run by the issuer before the cut: CTar1-AC1 FAIL as expected (the test does not exist); CTar1-AC2 PASS as expected (a control: `INTAKE-CLOSURE-TEST cases=9/9 ok=True`); CTar1-AC3 FAIL as expected (the JSON does not exist).
Source: CTO ruling @5740f0d341 term 1; call XB-20261016T052534Z-983c; FWD-15, FWD-16.
