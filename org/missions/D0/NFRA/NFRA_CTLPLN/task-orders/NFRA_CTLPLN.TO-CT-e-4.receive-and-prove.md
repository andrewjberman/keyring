# TO NFRA_CTLPLN.TO-CT-e-4 -- round 5 CT-e-4: the receiving box installs one delivered file with no index, imports it, and writes its receipt

<to_id>NFRA_CTLPLN.TO-CT-e-4</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~8</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-e-4` (`decompositions/NFRA_CTLPLN_DECOMP.round5.md`) | **outcome_ref:** FWD-15 |
**depends_on:** none (the record contract below is the seam; no cell waits on another's code)

---

## WORKER FACE

### THE CELL

`CT-e-4`, C-INTAKE clause 5: "The laptop has no Python 3.14, so a delivered file is proven on the Dell: an install with no
index, then an import, read back." A delivered pack (files, their check records, a manifest) arrives on a box over the private
network. This cell's tool, run on that box with the standard library only, refuses anything whose check record does not read
"checked" or whose bytes differ, installs each file with no index and no dependency resolution into a scratch target first,
imports it, and writes a receipt. The same tool runs on Python 3.14 (the Dells) and 3.12 (this machine, for the test).

### THE SEAM

THE RECORD CONTRACT (fixed here so the four cells share FILES and never wait on each other's code).
All records are JSON, UTF-8, ASCII-only, one file per event, under `org/devices/intake/records/<batch>/`:
- FETCH record `<file name>.fetch.json`, written by the fetch tool AT THE TIME OF THE FETCH, also when the fetch fails:
  `schema` ("intake-fetch/1"), `batch`, `requested` {`name`, `version`, `python_tag`, `abi_tag`, `platform_tag`, `file_name`},
  `index_base`, `requests` (a list, one entry per HTTP request made: `url`, `method`, `status`, `bytes`, `at` UTC),
  `published` {`sha256`, `size`, `upload_time`, `yanked`, `requires_python`} (as the index states them for that exact file name),
  `project` {`release_count`, `first_release_at`, `this_release_at`}, `attestation` ("present" | "absent" | "unread", with the
  URL asked), `held_path` (relative to the holding root, never absolute), `held_sha256`, `held_bytes`, `outcome`
  ("held" | "refused" | "failed") with `reason`, `fetched_by` (the serial), `at`.
- CHECK record `<file name>.check.json`, written by the check tool: `schema` ("intake-check/1"), `batch`, `file_name`,
  `held_sha256`, `checks` (a list of exactly eight, in the brief's order, each `n`, `name`, `verdict`
  ("passed" | "failed" | "not_applicable" | "unsigned"), `evidence`, `rules_out`, `leaves` -- the last two the brief's own
  words for that check), `verdict` ("checked" only when checks 1 to 7 are each passed or not_applicable WITH a reason and
  check 8 reads "passed" with a signer and a file path; otherwise "not_checked"), `checked_by`, `at`.
- RECEIPT record `<file name>.receipt.<device>.json`, written on the receiving box: `schema` ("intake-receipt/1"), `device`,
  `python`, `file_name`, `received_sha256`, `check_record_sha256`, `install` {`command`, `rc`}, `imports` (per top-level module:
  `module`, `rc`, `first_error_line`), `outcome` ("installed_imported" | "installed_import_failed" | "refused" | "install_failed")
  with `reason`, `at`.
The HOLDING ROOT is outside every git tree: `<drive>/opal-intake/` (derive the drive prefix: `/cygdrive/c` if it exists, else
`/c`; on Windows Python resolve it from the workspace root's drive), with `holding/<batch>/` for fetched files and
`release/<batch>/` for files whose check record reads "checked". A file moves from holding to release ONLY by the check tool.

### BUILD

1. `org/devices/intake/intake_receive.py` (standard library only; it must import on Python 3.12 and 3.14):
   - `verify --from <pack dir>`: every file against `MANIFEST.json` (SHA-256, size); every wheel has its CHECK record (THE SEAM)
     beside it, the record's `held_sha256` equals the wheel's, its `verdict` is "checked", and its eight checks are present in
     order; nothing in the folder is unlisted. LAST line
     `INTAKE-VERIFY pack=<dir name> wheels=<n> verified=<v> checked=<c> stray=<s> ok=<True|False>`.
   - `prove --from <pack dir> --scratch <new empty dir>`: `verify` first (a failure stops it); then per wheel
     `python -m pip install --no-index --no-deps --target <scratch>/<file stem> <wheel path>` with THIS interpreter (the command
     must always contain `--no-index` and `--no-deps`; assert it in the test), then one import per top-level module (from
     `top_level.txt`, else derived from `RECORD`) in its own subprocess with a 60-second bound and that target first on the
     path; an import failing with `ModuleNotFoundError` for a module that is not the package's own is `import_missing_dep`
     (named), distinct from a failure. Writes one RECEIPT record per wheel into `<pack dir>/receipts/` (the box sends those
     back; it does not write into a git tree). LAST line
     `INTAKE-PROVE device=<name> python=<version> wheels=<n> installed=<i> imported=<m> import_missing_dep=<d> failed=<f> refused=<r> ok=<True|False>`
     (`ok=True` when nothing was refused or failed to install; the import counts are the finding). The device name comes from
     the environment variable `AGENTBUS_DEVICE`, never from a path.
   - `install --from <pack dir>`: the real install, on the box's own decision after `prove`: the same command with `--user` in
     place of `--target`, refused unless a receipt for each wheel reads `installed_imported` or `installed_import_failed` with
     only `import_missing_dep` causes.
   - The tool makes no network request and offers no flag that adds an index.
2. `org/devices/intake/test_intake_receive.py`, with THIS interpreter on synthetic `py3-none-any` wheels and hand-written check
   records in a temporary pack folder: two checked wheels verify, install into scratch and import, with receipts; a wheel whose
   record reads "not_checked" is refused and NOT installed (assert the scratch target does not exist); a wheel with one byte
   flipped is refused; a stray file fails `verify`; a wheel importing an absent module reads `import_missing_dep`; the pip
   command line built for every install contains `--no-index` and `--no-deps` and no URL; `install` refuses without receipts.
   LAST line `INTAKE-RECEIVE-TEST cases=<k>/<n> ok=<True|False>`.
3. In your deliverables folder, `INTAKE_RECEIVE_COMMANDS.md`: the exact commands, in order, a receiving box runs for a pack
   (verify, prove into a new scratch folder, send the receipts back, then install), and what each last line means.

### RULES FOR THIS CELL

**No request leaves this machine from anything YOU run.** No `pip install`, `pip download`, `pip index`, no `curl`, `wget`,
`npm`, `bun`. Every HTTP request your code makes in a test goes to a listener you start on 127.0.0.1. You never run your tool
against the public index: the first real fetch is the issuer's act, after the drain, on the CTO's signature.
No non-ASCII in any file you write. Standard library only unless the order names a package. Bake no absolute path and no user name.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CT5e4-AC1" cell_refs="CT-e-4"><invocation>python org/devices/intake/test_intake_receive.py</invocation><expect>INTAKE-RECEIVE-TEST cases=</expect></criterion>
`CT5e4-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CT5e4-AC2" cell_refs="CT-e-4"><invocation>python org/devices/intake/intake_receive.py selftest-unchecked</invocation><expect>refused=1</expect></criterion>
`CT5e4-AC2` -- the difference control: a synthetic wheel whose record reads "not_checked" is refused and nothing is installed; the same line must read `installed=0`.
</proof_of_spec>

<expected_criteria>CT5e4-AC1,CT5e4-AC2,CT5e4-AC3</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~8/NFRA_CTLPLN.TO-CT-e-4.receive-and-prove.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CT5e4-AC1,CT5e4-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round5.md</decomp_doc>
<owned_cells>CT-e-4</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_receive.py
org/devices/intake/test_intake_receive.py
org/devices/intake/test_intake_seam.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a box installing a file nobody checked (the check record is read and must say checked, with the wheel's own hash; a criterion); a resolver reaching the index from the receiving box (--no-index and --no-deps on every command, asserted; no flag adds an index); a failed proof changing the box (the proof installs into a scratch target; the real install needs the receipts); a missing dependency read as a broken wheel (its own class); BLIND: whether the package behaves on the box beyond importing -- the lane's own work is the outcome's last step and is not this tool's.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.17 @301f06300d (ADMITTED), ADDENDUM v0.15 and v0.16, contract C-INTAKE; brief
`docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md` @adc8997f1b Part V.1; CTO msgs 106327, 106363, 106372,
106424, 106436, 106445.

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~22:1xZ) -- REOPENED: the receiving tool reads the pack the check tool actually writes; the seam run becomes a committed test

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; the earlier commits are
inherited state on the trunk. THE SEAM RUN (the issuer's act 1 after the drain, on the merged trunk @b78e8bef7c): one synthetic
wheel went through fetch, check, release and pack against a loopback index, all four reading as expected, and then
`intake_receive.py verify` REFUSED the pack the check tool had just written:
`INTAKE-VERIFY pack=pack wheels=1 verified=0 checked=0 stray=3 ok=False` with
`PACK-DEFECT: MANIFEST.json entry lacks name/sha256/bytes` and the wheel, its check record and its delivery text each read as
STRAY. Cause, by the two workers' own reports: the check tool's `pack` writes `MANIFEST.json` as an object with `files[]`, ONE
entry per wheel, carrying `name`, `sha256`, `size`, `check_record`, `check_record_sha256`, `delivery`, `delivery_sha256`; this
tool expects one entry per FILE with `name`, `sha256`, `bytes`. The seam text left the manifest's shape open, so the defect is
the issuer's; the seam run is what found it. Gate limb: none graded this modification.

1. `org/devices/intake/intake_receive.py` reads the manifest `org/devices/intake/intake_check.py` `pack` writes, as its PRIMARY
   shape: read `intake_check.py`'s pack code first and match it field for field. For each `files[]` entry: the wheel by `name`
   with `sha256` and `size`; its check record by `check_record` with `check_record_sha256`; its delivery text by `delivery` with
   `delivery_sha256`. Every one of the three is verified by hash, and all three count as listed (none is a stray). `bytes` is
   accepted as a synonym of `size`. The two shapes the tool accepted before stay accepted. A manifest entry naming a companion
   file that is absent, or whose hash differs, refuses that wheel. Nothing else in `verify`, `prove` or `install` changes, and
   every refusal the tool made before it still makes. You do NOT edit `intake_check.py`.
2. `org/devices/intake/test_intake_seam.py`: the issuer's seam-run script is in your worktree at that path, UNCOMMITTED, as a
   starting point (it takes the repository root as its one argument and ends `SEAM-RUN stages=6 ok=<True|False>`). Make it a
   test that needs no argument (derive the root from its own location), removes its temporary directory, keeps every request on
   127.0.0.1, uses stand-ins for the installed copy, the antivirus answer and the signer through the tools' own environment
   variables, and adds three negative arms on the SAME pack: one byte of the packed wheel flipped -> `verify` refuses; the
   check record's `verdict` hand-edited to "not_checked" -> refused; the delivery text removed -> refused. LAST line
   `INTAKE-SEAM-TEST stages=6 negative_arms=<k>/3 index_requests=4 ok=<True|False>`.
3. In `test_intake_receive.py` add one case that builds a pack by CALLING the check tool's own pack function (import
   `intake_check`) so the two tools cannot drift apart again unnoticed.

**ACCEPTANCE.** `CT5e4-AC1` and `CT5e4-AC2` are unchanged (the case count grows). One criterion is ADDED:

<criterion id="CT5e4-AC3" cell_refs="CT-e-4"><invocation>python org/devices/intake/test_intake_seam.py</invocation><expect>INTAKE-SEAM-TEST stages=6 negative_arms=3/3 index_requests=4 ok=True</expect></criterion>
`CT5e4-AC3` -- the four tools run as one on a synthetic wheel, and the three tampered packs are refused.

**BOUNDS.** No request leaves this machine. The only `pip install` is the tool's own, `--no-index --no-deps --target <temporary dir>`,
on synthetic wheels. No test-virus string. Standard library only.
