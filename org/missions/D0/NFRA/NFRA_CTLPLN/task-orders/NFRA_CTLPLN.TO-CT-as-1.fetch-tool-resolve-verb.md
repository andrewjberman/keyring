# TO NFRA_CTLPLN.TO-CT-as-1 -- workstream OUTCOME round 21 (cell CT-as-1): the organic journey, step 2 -- `intake_fetch.py` gains a read-only `resolve` verb that names the exact wheel file the index offers for each closure member and the Linux target, and the closure tool's `fetchlist` stops naming Windows files for a Linux closure (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-as-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~131</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after its own re-run in the worker tree (wk-NFRA_CTLPLN-131 @5010135b2e) and again in the main tree after merge 12a02b633b: CTas1-AC1 RESOLVE arms=9/9 ok=True; CTas1-AC2 INTAKE-FETCH-TEST cases=21/21 ok=True (base 19/19); CTas1-AC3 INTAKE-CLOSURE-TEST cases=10/10 ok=True (base 10/10); proof VALID; the earlier CT-ar-1 test still reads LINUX-CLOSURE arms=7/7 ok=True; the branch changed 5 files, all inside the order's paths. Row W130-S2 CLOSED by the command `python org/devices/intake/intake_closure.py fetchlist --from-file org/devices/intake/closure_cp312_linux_x86_64_yfinance.json`, which now exits 2 with `fetchlist: this closure targets cp312-linux_x86_64; use intake_fetch.py resolve to name its files` and writes no file (issuer re-run); `build_fetchlist()` itself is unchanged, the CLI refuses before it. The worker made NO request to the real index (a dry run against closed loopback port 127.0.0.1:9 showed the gate accepted all 17 lines and failed at connect). Beyond the spec the verb adds the reasons REQUIRES-PYTHON-UNMET, NO-DIGEST and NO-FILES, and without a host file prints host_conflicts=UNREAD. No row filed. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>21</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-as-1` (`decompositions/NFRA_CTLPLN_DECOMP.round27.md`, amendment 2) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** CT-ar-1 (complete, merge 97477e8786)

---

## WORKER FACE

### THE CELL

The organic journey of dell2's `yfinance==1.2.0` Linux closure (call `XB-20261016T052534Z-983c`; the laptop CTO's ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_XB983C_YFINANCE_LINUX_CLOSURE_20261016.md`, read it whole). Step 1 is DONE: `org/devices/intake/closure_cp312_linux_x86_64_yfinance.json` names 24 members, 7 the host already satisfies, 17 to fetch (`to_fetch`), from the LAPTOP's installed versions. Whether the index offers a Linux wheel for each of those 17 `name==version` is UNREAD, and the fetch tool needs the EXACT file name (all four tags, e.g. `numpy-2.4.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl`; `same_file` compares every part except the distribution name exactly). This cell builds the tool that reads it. It makes NO request to the real index: its tests use a LOOPBACK fake index (read `org/devices/intake/test_intake_fetch.py` for how it starts one with `--index-base`). The real run is the next cell: the CTO has approved the 17 `name==version` lines (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_YFINANCE_LINUX_20261016.md` @7d012e8f36; the real run will pass it as `--approved-by`), and asked for the exact wheel file names plus a re-check of the host-satisfied set against the index's own metadata (msg 109620); a wheel-less member or a host conflict is a STOP for him: no source archive, no version change. Read first: `org/devices/intake/intake_fetch.py` whole (the `Policy`, `Fetch.run`, `gate_public` and the release-document request `GET <base>/pypi/<name>/<version>/json`), `org/devices/kit_python_wheels.py` `parse_target` and `supported_tags` (CT-ar-1 added the `linux_x86_64` label there), and `org/devices/intake/intake_closure.py` `build_fetchlist` and `cmd_fetchlist`.

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's ruling is outside that set: add `org/tier1_exec/1.0.0_SA_CTO/deliverables` to read it.

### BUILD

1. **The `resolve` verb in `intake_fetch.py`:** `resolve --closure <closure json> --target cp312-linux_x86_64 --approved-by <file> [--index-base URL] [--out <json>]`. For every closure member whose `host_class` is not `HOST-SATISFIED` (the `to_fetch` set), it makes EXACTLY ONE request: the release document `GET <base>/pypi/<name>/<version>/json` (through the same `Policy`, `get_json`, redirect and size limits the fetch uses; NO request to a file host, no download, no project document, no attestation). From that document's `urls` it chooses ONE file: a wheel (`packagetype` `bdist_wheel` or a `.whl` name) whose tags fit the target by `kit_python_wheels` (`tag_fits` against the target's supported tags), not yanked, with `requires_python` satisfied by Python 3.12. When several fit, prefer in this order: (1) `py3-none-any` or `py2.py3-none-any` (pure), (2) `cp312-abi3`-or-`cp312-cp312` manylinux with the HIGHEST glibc level that is <= 2.34 (`manylinux_2_34` over `manylinux_2_28` over `manylinux_2_17`/`manylinux2014`), (3) other fitting tags by the same glibc rule. The tie-break is the lexicographically smallest file name. A member with no fitting wheel is `NO-WHEEL` with the reason: `SDIST-ONLY` (only a source archive), `OTHER-PLATFORM-ONLY` (wheels exist, none fits; list their tags), `YANKED`, or `NO-RELEASE` (HTTP 404). A `NO-WHEEL` member is a STOP printed for the CTO; the tool never picks a source archive and never edits the list. The approval gate stays: before ANY socket, `--approved-by` must name an existing file that contains the exact `name==version` of EVERY member to be resolved (one missing line refuses the whole run before any request). Output JSON `schema` `intake-resolve/1`: the target, the closure file name, the index base, one row per member `{name, version, outcome: CHOSEN|NO-WHEEL, file_name, sha256, size, upload_time, requires_python, tags, reason, other_fitting_files}`, the `requests` log (url, status, bytes), and the last line `INTAKE-RESOLVE target=<t> members=<n> chosen=<c> no_wheel=<w> requests=<r> ok=<True|False>` (`ok` False when any member is `NO-WHEEL`). Also write a Markdown table beside it when `--out` ends in `.json` (same stem, `.md`; ASCII).
1b. **The re-check against the index's own metadata (the CTO's addendum ask, msg 109620).** The CHOSEN release documents carry `info.requires_dist`. For each CHOSEN member, `resolve` also records its `requires_dist` lines, evaluates every marker for the target environment (the kit target's `env`; `extra == ...` lines are NOT followed, as in the closure tool), and reports, as printed STOP lines that the tool never fixes: (i) `NEW-MEMBER <name> required by <parent> <specifier>` for a required distribution that is not a member of the closure at all (neither in `to_fetch` nor host-satisfied); (ii) `SPECIFIER-MISMATCH <name> <chosen version> unmet by <parent> <specifier>` for a closure member whose chosen version violates a parent's specifier; (iii) with the optional `--host-pydeps <json>` (the file CT-ar-1 wrote, `org/devices/intake/records/intake-20261016-yfinance-linux/HOST_PYDEPS.json`): `HOST-CONFLICT <name> host <version> unmet by <parent> <specifier>` for a host-satisfied member whose HOST version fails a specifier that the INDEX metadata puts on it, and `HOST-OK` lines naming each host-satisfied member with the host version and the specifiers it meets. The saved JSON carries these lists; the last line gains `new_members=<n> specifier_mismatches=<m> host_conflicts=<h>`, and `ok` is False when any of the three is non-zero. A member whose `requires_dist` is absent from the document is printed `NO-METADATA` (not a conflict).
2. **`fetchlist` in `intake_closure.py`:** CT-ar-1's worker found that `build_fetchlist` hard-codes the `-cp314-cp314-win_amd64.whl` suffix, so on the Linux closure it names 7 Windows wheel files (row `NFRA_CTLPLN-W130-S2`). Make `fetchlist` REFUSE a closure whose target is not `cp314-win_amd64` with the message `fetchlist: this closure targets <t>; use intake_fetch.py resolve to name its files` and a non-zero exit, and keep the Windows output byte-identical (compare against a run on `org/devices/intake/closure_cp314_win_amd64.json` before and after).
3. **A NEW test** `.tools/tests/test_round27_resolve.py` (standard library plus the tools; loopback fake index only; no real network; ASCII output). Arms: (a) three fake releases on one loopback index: a pure `py3-none-any` wheel is CHOSEN; a compiled release with BOTH a `manylinux_2_17_x86_64` and a `manylinux_2_28_x86_64` wheel (and a win_amd64 wheel and an `sdist`) is CHOSEN as the `manylinux_2_28` file; a release with only a source archive is `NO-WHEEL` `SDIST-ONLY`; (b) a release whose only wheel is `musllinux_1_1_x86_64` is `NO-WHEEL` `OTHER-PLATFORM-ONLY`, and a yanked wheel is never chosen; (c) the approval gate: with one `name==version` missing from the approval file the run refuses and the loopback server saw ZERO requests; (d) exactly ONE request per member and none to any other path; (e) the output JSON carries `sha256` and `size` from the index and the rows are sorted by name; (f) `fetchlist` on the saved Linux closure refuses with the stated message, and `fetchlist` on the Windows closure is byte-identical to its pre-change output (control); (g) CONTROL of the instrument: the same arm (a) assertion run on a hand-made result that picks the `manylinux_2_17` file returns FAIL; (h) the re-check: on the loopback index a CHOSEN release whose `requires_dist` names a distribution outside the closure prints `NEW-MEMBER`, one whose chosen version violates a parent's pin prints `SPECIFIER-MISMATCH`, a host-satisfied member whose host version fails an index-side specifier prints `HOST-CONFLICT`, and the clean case prints `HOST-OK` for it with `ok=True`; a `requires_dist` line with a marker that is false for Linux (`sys_platform == "win32"`) is not followed. Last line `RESOLVE arms=<k>/<n> ok=<True|False>`.
4. Add cases to `org/devices/intake/test_intake_fetch.py` only for the new verb (its count of 19 grows); change no existing case.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~131/`. Every experiment runs in a temporary folder or repository unless the cell says otherwise. NO request to the real package index or any outside host: only the loopback server; no `pip`; no install. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~130/NFRA_CTLPLN.TO-CT-ar-1.closure-tool-linux-target-yfinance.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W131-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it. Report the closure of `NFRA_CTLPLN-W130-S2` (the `fetchlist` suffix) by the command that now refuses.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTas1-AC1" cell_refs="CT-as-1"><invocation>python .tools/tests/test_round27_resolve.py</invocation><expect>ok=True</expect></criterion>
`CTas1-AC1` -- the resolve verb names one exact wheel per member from a loopback index, stops on a source-only or other-platform release, refuses before any socket when the approval lacks a line, and `fetchlist` no longer names Windows files for a Linux closure (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTas1-AC2" cell_refs="CT-as-1"><invocation>python org/devices/intake/test_intake_fetch.py</invocation><expect>ok=True</expect></criterion>
`CTas1-AC2` -- the fetch tool's own suite still passes with the verb added (base: `INTAKE-FETCH-TEST cases=19/19 ok=True`, a control); report the whole last line.

<criterion id="CTas1-AC3" cell_refs="CT-as-1"><invocation>python org/devices/intake/test_intake_closure.py</invocation><expect>ok=True</expect></criterion>
`CTas1-AC3` -- the closure tool's suite still passes after the `fetchlist` change (base: `INTAKE-CLOSURE-TEST cases=10/10 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTas1-AC1,CTas1-AC2,CTas1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~131/NFRA_CTLPLN.TO-CT-as-1.fetch-tool-resolve-verb.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTas1-AC1,CTas1-AC2,CTas1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round27.md</decomp_doc>
<owned_cells>CT-as-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_fetch.py
org/devices/intake/intake_closure.py
org/devices/intake/test_intake_fetch.py
.tools/tests/test_round27_resolve.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no request to any outside host: the tests use a loopback fake index.
comp-adversary: RUN -- a request to the real index from a test (the base is always a loopback URL and arm c counts the server's requests; a missing `--index-base` on the public base needs the approval gate and the test never passes it); a download slipping in (arm d requires one request per member to the release document path only); a source archive chosen when no wheel fits (arm a, b); a yanked file chosen (arm b); the highest-glibc rule picking a level the host cannot run (the cap is 2.34, the host's glibc; arm a pins manylinux_2_28 over 2_17 and the control arm g fails a wrong pick); the Windows fetchlist output changing (arm f compares bytes before and after); the approval gate weakened (arm c); BLIND: the real index's release documents may differ in shape from the fake index (the later real run reads them and the tool refuses an unusable entry as `fetch` does); `packaging.tags` on this laptop reads the running host (CT-ar-1 row W130-S1), so the supported tag order must come from the kit target's written-out list, not from the running machine.
risk: LOCAL -- a read-only metadata verb and a refusal in a closure tool, tested against a loopback server; no real network, no download, no install.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the journey (XB-983c @5740f0d341) and its list step needs named files (term 1, term 3).
</preflight>

Base checks, dry-run by the issuer before the cut: CTas1-AC1 FAIL as expected (the test does not exist); CTas1-AC2 PASS as expected (a control: `INTAKE-FETCH-TEST cases=19/19 ok=True`); CTas1-AC3 PASS as expected (a control: `INTAKE-CLOSURE-TEST cases=10/10 ok=True`).
Source: CTO ruling @5740f0d341 terms 1-3; CT-ar-1's row `NFRA_CTLPLN-W130-S2`; FWD-15, FWD-16.
