# TO NFRA_CTLPLN.TO-CT-aw-1 -- workstream OUTCOME round 25 (cell CT-aw-1): intake check 6 becomes platform-aware, so a signed waiver stays exceptional (FWD-15, FWD-16)

<to_id>NFRA_CTLPLN.TO-CT-aw-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~135</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<status_reason>Closed by the issuer 2.0.0_SA_COO~C after three seatings of slot ~135 on branch wk-NFRA_CTLPLN-135 (final HEAD 67458aef7e), its own re-run in the worker tree, and again in the main tree after merge 528891b0b7: CTaw1-AC1 CHECK6-PLATFORM arms=14/14 ok=True; CTaw1-AC2 REAL4 passed=4/4 ok=True (curl_cffi, numpy, pandas, websockets, read only, no waiver; numpy via the one listed build-metadata file); CTaw1-AC3 INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True; proof VALID. Neighbouring suites at the merge: INTAKE-RECEIVE-TEST 36/36, INTAKE-CLOSURE-TEST 10/10, INTAKE-FETCH-TEST 21/21; `.tools/tests/test_round27_waiver.py` read WAIVER arms=19/20 (its arm g1 pinned the old verdict): cut as CT-az-1. Two rulings shaped the rule: W135-S1 (the issuer withdrew `change no existing case` for the one stale case in test_intake_check.py) and, by the CTO, W135-S2 (msg 109671: block with up to 4 adjacent empty lines) then W135-S3 (msg 109673: collapse the blank run on BOTH sides at the one seam). W135-S4 OBSERVATION: the wheel side has no before/after split at the seam, so the cell takes up to 4 empty lines from the run's start and up to 4 from its end; a wheel run of 5 to 8 empty lines is fully collapsed; no real file takes that path. The four existing waivers stay on their records as issued; nothing under C:/opal-intake/ was written. LOCAL until MSTR pushes.</status_reason>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>OUTCOME</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-aw-1` (`decompositions/NFRA_CTLPLN_DECOMP.round28.md`) | **outcome_ref:** FWD-15, FWD-16 |
**depends_on:** none (the signed-waiver cell `CT-av-1` is merged, 6f07651fdf)

---

## WORKER FACE

### THE CELL

Intake check 6 compares each `.py` file of a held wheel with the laptop's INSTALLED copy of the same distribution, byte for byte. For a Linux wheel compared with the laptop's Windows install it fails by construction: four yfinance wheels (curl_cffi, numpy, pandas, websockets) failed it and travel today on four signed waivers. The CTO ruled (`org/missions/D0/NFRA/NFRA_CTLPLN/ledger/ROUND_ANALYSIS.round27.md`, ruling 3; read it) that check 6 becomes platform-aware so a waiver stays exceptional. The existing four waivers stay on their records as issued: touch no record under `C:/opal-intake/` or `org/devices/intake/records/`.

Read first: `org/devices/intake/intake_check.py` `check_6` (line ~508; it already records `compared_across_platforms`, `installed_platform`, `held_platform` and `differ_after_crlf_normalisation`), `check_3` (it puts the installed copy into the check context), `run_check` (line ~952, how `ctx` is built), `compute_verdict`, and `org/devices/intake/test_intake_check.py` (how its synthetic wheels and installed copies are built).

YOUR WORKTREE WAS CUT BY `.tools/wk-provision.sh` AND IS A SPARSE CHECKOUT: it holds `.tools/`, `lib/`, the project folder `org/missions/D0/NFRA/NFRA_CTLPLN/`, `org/modules/graph/`, `org/devices/`, `infra/logic/registry/`, `org/standards/` and the paths of this order. If a command fails because a file or folder is missing, run `git sparse-checkout add <folder>`, retry, and name the folder, the command and the error in your final report. The CTO's ruling is under `org/missions/D0/NFRA/NFRA_CTLPLN/ledger/` (already inside the project folder).

### BUILD

1. **The rule, in `check_6`, only when `compared_across_platforms` is true.** For each differing `.py` file (the same set `py_diff` collects today, EXCEPT the `.data/(scripts|headers|data)/` members and the files over `MAX_PY_BYTES`, which keep failing as today), normalise BOTH sides the same way before comparing: replace CRLF with LF, then remove every block that starts at a line containing `# start delvewheel patch` and ends at the line containing `# end delvewheel patch` (both marker lines included; remove the block from both sides, so a block present on only one side leaves the rest equal). Then:
   - equal after normalisation: the file is NOT a difference; list it in a new evidence list `platform_normalised_equal`;
   - not equal, and its site-relative path is in the module constant `CHECK6_BUILD_METADATA_FILES`: the file is NOT a difference; list it in a new evidence list `build_metadata_residual` (with the path);
   - any other residual: a difference, exactly as today (it stays in `py_differing` and makes check 6 `failed`).
   `CHECK6_BUILD_METADATA_FILES` holds exactly ONE entry, `numpy/__config__.py` (a file numpy's own build writes with the build machine's compiler and flags). Adding an entry is a CTO ruling, never a worker's: say so in a comment above the constant.
2. **When `compared_across_platforms` is false nothing changes:** the raw byte comparison, the failure on a CRLF-only difference, and every existing evidence key behave as at the base. The verdict `summary` string of a passed check 6 names the two new counts when they are non-zero (`platform-normalised-equal=N build-metadata-residual=M`).
3. **Record, do not hide.** The evidence keeps `py_differing_count` as the raw count of byte-different files, and adds `py_differing_after_platform_rules` (the count that decides the verdict). `differ_after_crlf_normalisation` keeps its meaning.
4. **The test**, a NEW file `.tools/tests/test_round28_check6_platform.py` (standard library plus the check tool; synthetic wheels and installed copies in temporary folders as `test_intake_check.py` builds them; no network; ASCII output), with these arms:
   (a) cross-platform, a CRLF-only difference: check 6 `passed`, the file in `platform_normalised_equal`;
   (b) cross-platform, the installed copy carries a delvewheel block the wheel lacks, otherwise equal: `passed`;
   (c) cross-platform, a differing `numpy/__config__.py` (a synthetic distribution named numpy): `passed`, the path in `build_metadata_residual`; the SAME difference in a file NOT on the list: `failed`;
   (d) cross-platform, one PLANTED edited line in an ordinary module, with or without CRLF and a delvewheel block beside it: `failed`, the file in `py_differing`;
   (e) same platform (the installed WHEEL `Tag:` equals the wheel's): a CRLF-only difference still `failed` as at the base, and a differing `numpy/__config__.py` still `failed`;
   (f) `.data/scripts` and over-size files keep failing across platforms;
   (g) control arms that make the suite fail if the rule ever passes a planted edit, or fires when `compared_across_platforms` is false.
   Last line `CHECK6-PLATFORM arms=<k>/<n> ok=<True|False>`.
5. **The real-wheel arm**, `python .tools/tests/test_round28_check6_platform.py --real4`: READ ONLY. For each of the four real wheels `curl_cffi`, `numpy`, `pandas`, `websockets` in `C:/opal-intake/release/intake-20261016-yfinance-linux/` (the file whose name starts with that distribution name and ends `.whl`), build the context the way `run_check` does but in memory only, run `check_3` then `check_6`, write NOTHING (no record, no copy into any folder under `C:/opal-intake/`, no sidecar), and print one line per wheel `REAL4 <name> check6=<verdict> compared_across_platforms=<bool> residual=<py_differing_after_platform_rules> metadata=<n>`, then the last line `REAL4 passed=<k>/4 ok=<True|False>`. If the release folder is absent print `REAL4 SKIPPED folder absent` and exit 2 (never a pass). Expected after your change: 4 of 4 passed with no waiver; if one does not, report the residual files it names (do not widen the rule: file a row).
6. Add to `org/devices/intake/test_intake_check.py` only the cases the change needs (its count grows); change no existing case.

### AMENDMENT 1 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~10:5xZ; a re-seat of slot ~135 on the SAME branch `wk-NFRA_CTLPLN-135`)

The first seating stopped on two rows and built the rest. INHERITED STATE: its commits `8144b24967` (rule in `intake_check.py`), `dc48c3b47f` (the test file; 8 of 8 arms), `9e91c5b375` (rows `W135-S1`, `W135-S2`), `b41edcb1de` and `2a6005ecb6` (a proof instance with two FAIL rows, which you REPLACE). Keep what works; do not start over. Two rulings now bind and OVERRIDE the build steps above where they differ:

- **W135-S1 (issuer's ruling, my order froze a case the rule must reverse).** Build step 6 ("change no existing case") is WITHDRAWN for exactly ONE case: `case_check_6_records_the_cross_platform_comparison_and_the_crlf_count` in `org/devices/intake/test_intake_check.py` (about lines 1170-1181). Its old assertion was that a cross-platform CRLF-only difference reads check 6 `failed`; under the ruled rule the same pair reads `passed` and is listed in `platform_normalised_equal`. Edit THAT case's expectation to the new behaviour while it still checks what its name says (`compared_across_platforms` true and the post-CRLF count 0), change no other existing case, and quote the old and the new assertion in your report. The suite must then read 60/60 plus any cases you add.
- **W135-S2 (the CTO's ruling, msg 109671).** The delvewheel block removal of build step 1 is: remove the block TOGETHER WITH up to 4 empty lines directly before it and up to 4 empty lines directly after it, then compare exactly. A blank-line difference ANYWHERE ELSE in the file still fails. Real files this must pass: `numpy/__init__.py` and `pandas/__init__.py` (the empty lines sit on either side of the block and nowhere else). Implement it so that those two real files compare equal with no waiver, and so that a file with no delvewheel block gets NO blank-line leniency at all. Add to your test file (a) a planted blank line far from the block (more than 4 lines away) FAILS, (b) a planted blank line inside the 4-line reach of the block on a file whose other content differs by a real edit still FAILS, (c) a synthetic block with blank lines on both sides passes. The real-wheel arm `--real4` must now read `REAL4 passed=4/4`; if it does not, report the residual lines and file a row, do not widen the rule further.
- Re-run all three criteria; the proof instance is rewritten on the committed state with every row you can pass, and a row that still FAILS says why in its `status_reason`.

### AMENDMENT 2 (issuer 2.0.0_SA_COO~C, 2026-10-16 ~11:0xZ; a second re-seat of slot ~135 on the SAME branch)

The second seating built the padding rule and the amended case (`0577033587`, `a5caea51cf`, `6b83313bf2`): AC1 12 of 12, AC3 60 of 60, AC2 `REAL4 passed=3/4`; `pandas/__init__.py` fails by ONE empty line (row `W135-S3`: the installed copy has 2 empty lines before its block and 1 after, the wheel keeps its own 1 empty line at that seam). Keep all of it. The CTO's ruling (msg 109673) REPLACES the padding rule of Amendment 1 with this one:

- At the position where the delvewheel block was removed from the installed copy, collapse the run of empty lines on BOTH sides (the installed copy's lines around the removed block, and the wheel's lines at the same seam), at most 4 empty lines each side, then compare exactly. Only that one seam per removed block is touched; a blank-line difference anywhere else in the file still fails; a file with no delvewheel block gets no leniency.
- Keep the planted far-blank-line test; ADD one test where the seam carries a NON-blank line on one side only: it must FAIL. Keep arms h-k and re-check them against the new rule (arm j, the padded block, must still pass). The `--real4` arm must now read `REAL4 passed=4/4` with no waiver; if it does not, report the residual and file a row, do not widen the rule.
- Re-run all three criteria and rewrite the proof instance on the committed state.

### RULES FOR THIS CELL

Write surface = the `<paths>` plus your own folder `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~135/`. Every experiment runs in a temporary folder or repository. NO network request of any kind, no `pip`, no install. Do NOT run `release`, `pack`, `check` or any verb that writes against the real batch `intake-20261016-yfinance-linux`; the real arm of step 5 reads only. No push, no deploy, no AWS write. Use `.tools/safe-commit.sh` for every commit, with explicit file paths, and read its whole output (do not pipe it through tail or head). Do NOT commit the `portal` gitlink or `org/git-author-override-audit.laptop.log`. ASCII only; Python 3.12; bash is Git Bash 3.6.7 (default utilities only). CLAUDE.md and org/XXX.md are LOCKED. COMMIT A WORK-IN-PROGRESS COMMIT AS SOON AS A FILE EXISTS, and again after each criterion passes. COPY the proof instance's field names from an existing VALID instance, `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~134/NFRA_CTLPLN.TO-CT-av-1.intake-signed-waiver-for-a-failed-check.proof_of_spec.json` (`config` is not an artifact kind; each control carries `determinism` and `mutant`). The `<status>` flip is the issuer's (your order file is outside your `<paths>`): do not edit it and do not report it as a defect. When you write your proof instance, pin every artifact row to the commit that carried it, never `PENDING-THIS-COMMIT` for a file an earlier commit carried. If a gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W135-S<k>`, `surfaced_at` = `date -u +%FT%TZ`, `disposition` `UNDER_INVESTIGATION`) and keep working. A WARN from safe-commit that the client-data check had no account-id list is the standing WARN-only state (ruled): quote it in your report, file no row for it.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTaw1-AC1" cell_refs="CT-aw-1"><invocation>python .tools/tests/test_round28_check6_platform.py</invocation><expect>ok=True</expect></criterion>
`CTaw1-AC1` -- across platforms a CRLF-only difference, a delvewheel block and the one listed build-metadata file stop failing check 6, while a planted edited line, an unlisted file and every same-platform comparison still fail (base: the test does not exist); report the whole last line with its denominator.

<criterion id="CTaw1-AC2" cell_refs="CT-aw-1"><invocation>python .tools/tests/test_round28_check6_platform.py --real4</invocation><expect>REAL4 passed=4/4</expect></criterion>
`CTaw1-AC2` -- the four real yfinance wheels pass check 6 on the new rule with no waiver, read-only (base: the test does not exist); report all five lines.

<criterion id="CTaw1-AC3" cell_refs="CT-aw-1"><invocation>python org/devices/intake/test_intake_check.py</invocation><expect>ok=True</expect></criterion>
`CTaw1-AC3` -- the check tool's own suite passes with the new cases added (base: `INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True`, a control); report the whole last line.
</proof_of_spec>

<expected_criteria>CTaw1-AC1,CTaw1-AC2,CTaw1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 280`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~135/NFRA_CTLPLN.TO-CT-aw-1.intake-check-6-platform-aware.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTaw1-AC1,CTaw1-AC2,CTaw1-AC3` on the COMMITTED state.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round28.md</decomp_doc>
<owned_cells>CT-aw-1</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_check.py
org/devices/intake/test_intake_check.py
.tools/tests/test_round28_check6_platform.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no network request; synthetic wheels in temporary folders, and one read-only pass over four local files.
comp-adversary: RUN -- the rule widening into a general pass (arms c, d, e, f and the controls: an unlisted file, a planted edit, a same-platform comparison and a `.data` member all still fail); the rule hiding a difference (the raw count stays in `py_differing_count`, the two new lists name every file the rule excused); the metadata list growing silently (one entry, a comment says an addition is a CTO ruling); the real-wheel arm writing into the real batch (forbidden, read-only, nothing is written under `C:/opal-intake/`); the real arm passing because it SKIPPED (exit 2, never a pass); BLIND: whether numpy's `__config__.py` is the only build-generated file in a future batch is unknown, so another wheel can fail check 6 on one and need a CTO ruling or a waiver.
risk: LOCAL -- changes to the intake check tool and its tests against synthetic wheels; one read-only pass over four local wheel files; no file is released, moved or sent.
lane: the <paths> block IS the grant (worker RULING 1). `org/devices/intake/` is NFRA_CTLPLN's (C-INTAKE); the CTO ruled the design (round-27 analysis ruling 3, msg 109661).
</preflight>

Base checks, dry-run by the issuer before the cut: CTaw1-AC1 FAIL as expected (the test file does not exist); CTaw1-AC2 FAIL as expected (the test file does not exist); CTaw1-AC3 PASS as expected (control: `INTAKE-CHECK-TEST cases=60/60 skipped=0 ok=True`).
Source: CTO round-27 analysis ruling 3 and enrichment item 1; FWD-15, FWD-16.
