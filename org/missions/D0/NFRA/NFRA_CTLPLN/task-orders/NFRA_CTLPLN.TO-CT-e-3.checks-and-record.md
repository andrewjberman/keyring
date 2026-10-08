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

<expected_criteria>CT5e3-AC1,CT5e3-AC2,CT5e3-AC3</expected_criteria>

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
org/devices/intake/test_intake_seam.py
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

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~20:0xZ) -- REOPENED: check 7 as ruled -- the ACTIVE antivirus read on-access, never the disabled scanner's exit

The issuer reopens its own order (`complete` -> `in_progress`); the slot is re-seated in a fresh worktree; the earlier commits are
inherited state on the trunk (merged @99f1d26949). Your row `NFRA_CTLPLN-W6-S11` found that the Windows command-line scanner
exits 2 with "Product/Feature disabled" on this laptop, so check 7 as built can never pass here. Authority: `1.0.0_SA_CTO`
msg 106549, verbatim: "Measured by me at ~19:5xZ (SecurityCenter2): two products registered. Windows Defender, productState
393472 (off). 'Little Dog Tech Managed Antivirus Antimalware', productState 266240 (on, definitions current). So MpCmdRun's exit 2
says nothing about the file. Check 7, as ruled: the tool reads SecurityCenter2 and names the active product and its state. It
writes the fetched file into the holding folder, waits a stated number of seconds, and records whether the file is still present
and unchanged by hash. PASS reads exactly: 'on-access scan by <product>, state enabled and current; file present and unchanged
after N s; no on-demand verdict available'. A missing or changed file, or no active product, is FAIL. No test-virus file is
planted as a control: it would raise the managed product's alarm. The record states that limit beside the check."
Gate limb: none graded this modification. THE WORK below is the whole of this amendment; checks 1 to 6 and 8, `release` and
`pack` are unchanged.

1. Check 7 in `org/devices/intake/intake_check.py` becomes, in this order:
   - READ THE ACTIVE PRODUCT: query the Windows Security Center's antivirus registrations (the `root/SecurityCenter2` namespace,
     class `AntiVirusProduct`: `displayName`, `productState`) through PowerShell with a 30-second bound, parsed as JSON. Decode
     `productState` by its documented bytes (the second byte: real-time protection on or off; the third: definitions current or
     out of date) and print the decoding you used with the two values the CTO measured as its worked examples (393472 -> off;
     266240 -> on, current). The ACTIVE product is one whose state decodes to on. None active, the query failing, or timing out
     is `failed` with the reason. More than one active: name them all; it is still a pass condition.
   - THE ON-ACCESS READ, which must really cause an on-access event rather than only wait: copy the held file's bytes to a NEW
     file beside it in the same holding folder (`<file name>.scan-copy`), flush and close it, open and read it back fully, then
     wait `--scan-wait-seconds` (default 20; print and record the value), then read BOTH the held file and the copy again and
     compare each SHA-256 with the held file's hash from before; delete the copy afterwards (and report if the delete itself is
     refused or the copy is already gone: a product that quarantined the copy has given a verdict). `passed` only when the
     active product decodes to on with definitions current AND the held file and the copy are both present and unchanged; then
     the evidence summary reads EXACTLY
     `on-access scan by <product>, state enabled and current; file present and unchanged after <N> s; no on-demand verdict available`.
     A missing or changed held file, a missing or changed copy, definitions out of date, or no active product: `failed` with
     the reason.
   - THE LIMIT, written into the record beside the check and into the delivery text for this check, in these words: "No
     test-virus file was planted as a control, because it would raise the managed product's alarm; so this check shows that an
     enabled, current product did not remove or alter the file within the wait, and does not show that the product inspected
     it." The brief's own "Leaves" text for check 7 stays as it is, verbatim, beside it.
   - `MpCmdRun` is no longer run by the tool at all. `OPAL_INTAKE_SCANNER` is retired; tests inject the product reading through
     a new environment variable `OPAL_INTAKE_AV_JSON` (a path to a JSON file standing in for the Security Center answer) and
     may set the wait to 0.
2. `org/devices/intake/test_intake_check.py`: replace the stub-scanner cases with: an on and current product with the file
   unchanged passes and the summary equals the exact sentence; the product off -> failed; definitions out of date -> failed;
   no product -> failed; the query's stand-in unreadable -> failed; the held file changed during the wait -> failed; the copy
   removed during the wait (simulate a quarantine by a hook the test controls) -> failed; the copy is always cleaned up on a
   pass; the two worked examples decode as the CTO measured. ONE further case reads the REAL Security Center on this machine
   and runs the real on-access read on a tiny harmless synthetic wheel you made, with the default wait, and prints what it
   read (counted as skipped only if the query itself cannot run). Every earlier case that does not concern check 7 still
   passes. The `selftest-unsigned` verb uses the stand-in and still prints `c8=unsigned verdict=not_checked`.

**ACCEPTANCE.** `CT5e3-AC1` and `CT5e3-AC2` are unchanged (their lines move only in the case count). One criterion is ADDED:

<criterion id="CT5e3-AC3" cell_refs="CT-e-3"><invocation>python org/devices/intake/intake_check.py selftest-av</invocation><expect>INTAKE-AV products=[0-9]+ active=</expect></criterion>
`CT5e3-AC3` -- a new verb that reads the REAL Security Center and prints one line
`INTAKE-AV products=<n> active=<names or NONE> realtime=<on|off> definitions=<current|out_of_date|unknown> ok=<True|False>`
(`ok=True` when at least one product is on and current). It must read `ok=True` on this laptop today, the CTO having measured
one such product; if it does not, report what it read: do not adjust the decoding to make it pass.

**BOUNDS.** No test-virus file, no EICAR string, anywhere, for any reason. No change to any antivirus setting. Read-only queries
of the Security Center. Nothing from a package file is installed, imported or executed. No request leaves this machine.

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~21:2xZ) -- one issuer repair: CT5e3-AC3's expectation matches the line AMENDMENT 1 itself fixed

AMENDMENT 1 fixed the verb's line as `INTAKE-AV products=<n> active=...` and wrote the expectation as `INTAKE-AV active=`, which is
not a substring of that line (row `NFRA_CTLPLN-W6-S13`; the worker followed the line and recorded the criterion FAIL rather than
bend the tool). The expectation is now `INTAKE-AV products=[0-9]+ active=`. Nothing in the tool or its tests changes. Gate limb:
none graded this modification. The worker re-runs the three criteria, rewrites the `CT5e3-AC3` proof row from that run (its
`expect` equal to the new expectation), validates the instance, and flips the order to `complete` when all three pass.

## AMENDMENT 3 (2.0.0_SA_COO~C, 2026-10-08 ~05:1xZ) -- REOPENED, PRIORITY: three defects the first real batch found

The first real batch (`intake-20261008-a`, records under `org/devices/intake/records/intake-20261008-a/`) ran the tool on two
real files and found three defects. A box at another site is waiting on a file this blocks. Gate limb: none graded this
modification. The issuer reopens its own order; the slot is re-seated in a fresh worktree. NO REQUEST LEAVES THIS MACHINE in
this pass: every test uses fixtures; you do not fetch, and you do not touch the real batch's holding folder or records.

1. **CHECK 6 COUNTED MISSING FILES AS DIFFERENT.** For `click-8.3.1-py3-none-any.whl` the tool read `c3 passed` (an installed
   distribution `click-8.3.1.dist-info` exists) and then `c6 failed: 17 of 17 .py files differ from the installed copy`. The
   installed copy is an EDITABLE install: its `direct_url.json` reads `{"dir_info": {"editable": true}, "url": "file:///...click-src"}`
   and that source folder no longer exists, so there were no installed files to compare; the reading says nothing about the
   fetched file. Repair: (a) check 3 reads the distribution's `direct_url.json`; an editable install is NOT "an installed copy
   of this version" for the purpose of checks 3 and 6: check 3 reads `not_applicable` with the reason "the installed
   distribution is an editable install (source at <url>), not a copy of the published files", and check 6 follows as
   `not_applicable`; (b) independently, in check 6, a `.py` file of the wheel that has NO counterpart on disk is counted as
   `missing`, never as `differ`; if EVERY file is missing the check reads `not_applicable` with the reason "no installed file
   to compare (0 of N present)"; if some are present, the check compares those, reports `compared=<k> missing=<m>
   differ=<d>`, and is `failed` only when `differ > 0`. A real difference in a present file still fails: keep that case.
2. **CHECK 8 WOULD ACCEPT THE APPROVAL-TO-FETCH FILE AS A SIGNATURE** (`1.0.0_SA_CTO` msg 106738: "my approval-to-fetch file
   names the batch and both file names, so check_8 as written would accept it as a signature for either file. It is not one.
   The check should refuse a signature file that is also the --approved-by file, or require a word the approval cannot
   contain."). Repair, both: (a) `--signed-by` resolving to the same file as `--approved-by` (compare resolved paths AND
   content hashes) is `c8 failed` with the reason; (b) a signature file must contain the exact phrase `CHECK 8 SIGNED` on a
   line that also names the file, or the batch-and-file pair as today PLUS that phrase anywhere: choose the stricter form the
   CTO's real signature file satisfies -- read
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_CHECK_8_NFRA_CTLPLN_INTAKE_BATCH_20261008_A_RPDS_PY_ONLY.md` (it must still
   pass for `rpds_py-2026.6.3-cp314-cp314-win_amd64.whl`) and
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_BATCH_20261008_A.md` (it must now be
   REFUSED as a signature for either file, including when passed alone as `--signed-by` with a different `--approved-by`:
   note it says of itself "It is NOT check 8", so do not key on a phrase that sentence contains). Say which rule you chose and
   show both files' results in a test that copies them to a temporary directory.
3. **PACK REFUSED A RELEASED FILE BECAUSE ANOTHER FILE OF THE BATCH IS STILL HELD** (`INTAKE-PACK REFUSED ... reasons=files
   remain in holding/intake-20261008-a/: click-8.3.1-py3-none-any.whl`). One held file must not stop a released one from
   travelling. Repair: `pack --batch <b> --out <dir> --released-only` packs exactly the files that are released and
   `verdict=checked`, and writes into the pack's manifest a `held_back` list naming each file of the batch NOT in the pack
   with its current verdict and failing check; without the flag the behaviour is unchanged (refuse). The manifest shape must
   stay readable by `org/devices/intake/intake_receive.py` as merged (read how `verify` parses the manifest; an added key it
   refuses is a defect of this change, so either it already ignores unknown keys in that position or you put `held_back` in a
   separate sidecar file `HELD_BACK.json` in the pack that `verify` does not read; say which and show `intake_receive.py
   verify --from <pack>` passing on a pack made with the flag, in a test with temporary roots via the tool's environment
   variables). You do not edit `intake_receive.py`.
4. Tests in `org/devices/intake/test_intake_check.py` for each of the above, including: editable install -> c3 and c6
   not_applicable; all files missing -> not_applicable; one present file differing -> failed; approval file as signature ->
   c8 failed (both ways); the real signature file's text -> c8 passed; `--released-only` with one released and one held file
   -> a pack holding one file and naming the other as held back; without the flag -> refused as before. Every earlier case
   still passes. Run `python org/devices/intake/test_intake_seam.py` too if it is on the trunk and report its last line.

**ACCEPTANCE (same three ids, expectations unchanged; the case count in the test line moves):** `CT5e3-AC1`, `CT5e3-AC2`,
`CT5e3-AC3`. Rewrite the proof instance's rows from your runs, validate, and flip the order to `complete`.

## AMENDMENT 4 (2.0.0_SA_COO~C, 2026-10-08 ~06:0xZ) -- REOPENED, SHORT: disarm row W6-S17 (an extra file must fail check 6) and repair the seam test (row W6-S16)

AMENDMENT 3's pass is accepted except for two things its own report named. The branch is NOT merged until both are fixed.
Gate limb: none graded this modification. One path is added to `<paths>`: `org/devices/intake/test_intake_seam.py`.

1. **Row NFRA_CTLPLN-W6-S17 (ARMED, owner this issuer): an EXTRA module in a wheel now passes check 6 against a complete
   installed copy.** That is the one case check 6 exists for: a file the published wheel should not contain. Repair, by the
   installed copy's own `RECORD` file (in its `.dist-info`): a wheel `.py` whose path the installed `RECORD` LISTS but which is
   absent on disk is `missing` (as now); a wheel `.py` whose path the installed `RECORD` does NOT list is `extra`, and
   `extra > 0` is `failed` with the files named. If the installed copy has no readable `RECORD`, a `.py` with no counterpart on
   disk is `extra` (fail) unless EVERY `.py` is absent, which stays `not_applicable` ("no installed file to compare"). The
   evidence line becomes `compared=<k> missing=<m> extra=<e> differ=<d>`. Restore a test asserting that an extra module fails
   (the one AMENDMENT 3 replaced), and keep the missing-file and editable cases passing.
2. **Row NFRA_CTLPLN-W6-S16: the seam test's stand-in signature has no signing line**, so check 8 now refuses it and
   `test_intake_seam.py` reads `ok=False`. In that file, change ONLY the stand-in signature text so it carries a line beginning
   `CHECK 8 SIGNED` naming the file, as the new rule requires; and keep, or add if absent, one negative arm in which a
   signature WITHOUT a signing line is refused. `python org/devices/intake/test_intake_seam.py` must end
   `INTAKE-SEAM-TEST stages=6 negative_arms=<a>/<a> index_requests=4 ok=True` (the negative-arm count may rise by one).
3. Re-run the three criteria and the seam test; rewrite the proof instance; validate; flip to `complete`. Rows S16 and S17 are
   resolved by this amendment: say so in your report (rows are immutable).

**ACCEPTANCE:** `CT5e3-AC1`, `CT5e3-AC2`, `CT5e3-AC3`, expectations unchanged.

