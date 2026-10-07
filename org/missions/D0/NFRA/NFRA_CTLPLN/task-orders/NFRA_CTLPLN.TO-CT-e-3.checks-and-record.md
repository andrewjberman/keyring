# TO NFRA_CTLPLN.TO-CT-e-3 -- round 5 CT-e-3: checks 1 to 7 on a held file, the check record with what each check leaves, and the release

<to_id>NFRA_CTLPLN.TO-CT-e-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~6</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-e-3` (`decompositions/NFRA_CTLPLN_DECOMP.round5.md`) | **outcome_ref:** FWD-15, FWD-17 |
**depends_on:** none (the record contract below is the seam; no cell waits on another's code)

---

## WORKER FACE

### THE CELL

`CT-e-3`, C-INTAKE clause 1 and FWD-17 ("for anything that reached a box, a person can say what was checked before it was sent
and what was not"). A fetched file waits in the holding folder. This cell's tool makes the brief's eight narrow statements about
it, in order, each recorded as passed, failed or not applicable, each with the brief's own words for what it rules out and what
it LEAVES, and only a file whose record reads "checked" moves to the release folder. Running the package is NOT a check: the tool
never installs, imports or executes anything from the file. Check 8, a person signing the batch, is `1.0.0_SA_CTO`'s: your tool
records it from a signature file and can never pass it by itself.

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

1. `org/devices/intake/intake_check.py`, verb `check --batch <id> --file <file name>`: reads the held file and its FETCH record
   (THE SEAM) and writes the CHECK record. The eight, in the brief's order (read Part V.1 of
   `docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md` and copy each row's "Rules out" and "Leaves"
   text into the record verbatim; do not paraphrase them):
   1. the held file's SHA-256, re-read from disk now, equals `published.sha256` in the fetch record (and the size);
   2. name, version and tags: the file name parses to exactly the requested name, version, Python tag, ABI tag and platform tag
      in the fetch record; the archive's own `*.dist-info/METADATA` Name and Version and `WHEEL` Tag lines say the same; the
      request is a line of the approved list given by `--approved-by <path>` (a file whose text contains `name==version`);
   3. the version is one this machine already runs: an installed distribution of the same name and version exists here.
      `not_applicable` WITH the reason when the laptop holds no copy of that version (the record must then say so beside the
      delivery, as C-INTAKE clause 1 requires: CTO msg 106436 names one such file);
   4. age: the release's upload time and the project's first release and release count, from the fetch record; the thresholds
      are parameters with defaults the DESIGN does not set: take `--min-release-age-days` (default 14) and
      `--min-earlier-releases` (default 3), print the values used, and record them;
   5. build attestation: "present" or "absent" as the fetch record read it; the verdict is `passed` when present, and
      `not_applicable` with the reason "the project publishes none" when absent; "unread" is `failed`;
   6. the archive opened and LISTED, never installed: every `.py` file in the wheel is byte-identical to the same path in this
      machine's installed copy of the same version (count compared, count identical, the differing paths listed); every compiled
      file (`.pyd`, `.dll`, `.so`, `.exe`) is named and counted; and no installer, script or start-up hook is inside that the
      installed copy lacks: a `.pth` file, a `sitecustomize`/`usercustomize` module, a `*.data/scripts/` entry, an entry point
      in `entry_points.txt` absent from the installed copy's. `not_applicable` with the reason when check 3 was;
   7. Windows' own malware scan of the held file: run the platform's command-line scanner on that ONE file (locate
      `MpCmdRun.exe` under the Defender platform directory without baking a version; `-Scan -ScanType 3 -File <path>
      -DisableRemediation`), record its exit code and last lines; if the scanner is absent or refuses, the verdict is `failed`
      with the reason, never `passed`;
   8. the signature: `--signed-by <path>` names a file under `org/tier1_exec/1.0.0_SA_CTO/deliverables/` whose text names the
      batch id and this file name; then `passed` with the signer and the path; without the flag the verdict is `unsigned`.
   The record's overall `verdict` is "checked" only as THE SEAM states. LAST line
   `INTAKE-CHECK batch=<id> file=<file name> c1=<v> c2=<v> c3=<v> c4=<v> c5=<v> c6=<v> c7=<v> c8=<v> verdict=<checked|not_checked>`.
   - `release --batch <id> --file <file name>`: moves the file from `holding/` to `release/` ONLY if its check record reads
     "checked" AND the held file's SHA-256 still equals the record's; otherwise refuses naming the reason. It also writes, beside
     the released file, `<file name>.delivery.txt`: the eight lines (check, verdict, what it LEAVES) and the brief's sentence on
     what no check rules out, so the statement travels with the file.
   - `pack --batch <id> --out <dir>`: copies the released files of a batch with their check records and delivery texts into one
     folder with a `MANIFEST.json` (name, SHA-256, size), for the carrier. It refuses a batch holding any file not "checked".
2. `org/devices/intake/test_intake_check.py`, on synthetic wheels and hand-written fetch records in a temporary holding root
   (override the root by an environment variable the tool honours for tests, `OPAL_INTAKE_ROOT`): a clean file with a signature
   reads "checked" and releases; the same without a signature reads `c8=unsigned verdict=not_checked` and `release` refuses;
   one byte flipped in holding fails check 1; a `.py` that differs from the "installed" fixture fails check 6 and is listed; an
   added `.pth` fails check 6; a release two days old fails check 4 at the default and passes with `--min-release-age-days 1`;
   an absent attestation is `not_applicable`, an unread one `failed`; a file changed AFTER its check record was written is
   refused by `release`; `pack` refuses a batch with one unchecked file. Check 7 in the test uses a stub scanner (an executable
   path given by `OPAL_INTAKE_SCANNER`) so the test does not depend on the real scanner; ONE further case runs the REAL scanner
   on a tiny harmless synthetic wheel and reports what it returned (it may be skipped, counted as skipped, when the scanner is
   absent). LAST line `INTAKE-CHECK-TEST cases=<k>/<n> skipped=<s> ok=<True|False>`.

### RULES FOR THIS CELL

**No request leaves this machine from anything YOU run.** No `pip install`, `pip download`, `pip index`, no `curl`, `wget`,
`npm`, `bun`. Every HTTP request your code makes in a test goes to a listener you start on 127.0.0.1. You never run your tool
against the public index: the first real fetch is the issuer's act, after the drain, on the CTO's signature.
No non-ASCII in any file you write. Standard library only unless the order names a package. Bake no absolute path and no user name.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CT5e3-AC1" cell_refs="CT-e-3"><invocation>python org/devices/intake/test_intake_check.py</invocation><expect>INTAKE-CHECK-TEST cases=</expect></criterion>
`CT5e3-AC1` -- every case passing: the line must read `ok=True`.

<criterion id="CT5e3-AC2" cell_refs="CT-e-3"><invocation>python org/devices/intake/intake_check.py selftest-unsigned</invocation><expect>c8=unsigned verdict=not_checked</expect></criterion>
`CT5e3-AC2` -- the difference control: on a synthetic clean file the tool cannot reach "checked" without the CTO's signature file.
</proof_of_spec>

<expected_criteria>CT5e3-AC1,CT5e3-AC2</expected_criteria>

Each invocation runs under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~6/NFRA_CTLPLN.TO-CT-e-3.checks-and-record.proof_of_spec.json`, validate it
with `python .tools/proof-of-spec-check.py <instance> CT5e3-AC1,CT5e3-AC2`, and flip `<status>` to `complete` only when every criterion
passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round5.md</decomp_doc>
<owned_cells>CT-e-3</owned_cells>
</decomp_ref>

<paths>
org/devices/intake/intake_check.py
org/devices/intake/test_intake_check.py
docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call and no policy.
comp-adversary: RUN -- a tool that passes itself (check 8 is a file a person writes; unsigned is a verdict and a criterion); a check that silently did not run read as a pass (an absent scanner or an unread attestation is failed, never passed; not_applicable needs a reason); the package executed by its own check (the archive is listed, never installed or imported); a file swapped between check and send (release re-hashes; a changed file is refused); what the checks leave being forgotten (the brief's own "leaves" text is copied into the record and travels beside the file); BLIND: code inside a compiled file, which no check here sees -- the record says so in the brief's words.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_CTLPLN_PRD.md` v0.17 @301f06300d (ADMITTED), ADDENDUM v0.15 and v0.16, contract C-INTAKE; brief
`docs/briefs/nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md` @adc8997f1b Part V.1; CTO msgs 106327, 106363, 106372,
106424, 106436, 106445.
