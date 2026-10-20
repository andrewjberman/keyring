# NFRA_MCPINDEX task order -- `MX-y-6` -- cheatsheet.py gen-all learns `--upload-manifest`: the exact list of files the issuer uploads to the "Opal Gateway Cheat Sheets" folder, guarded the way the upload tool guards them

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-6</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-6.sheets-upload-manifest</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~89</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant, no upload: the script writes a manifest, the issuer uploads.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base) and the planted-mutant controls the issuer ran against a reference are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-6` (round 25, workstream GATEWAY; PRD v0.19 FWD-25; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md`, item 7 and ruling (c))

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). Round 24 built `cheatsheet.py gen-all`, which writes one cheat sheet (`<local>.md`) and one examples list (`<local>.examples.json`) per roster person. The CTO ruled (c): the sheets are written to a SharePoint folder named `Opal Gateway Cheat Sheets`, in the site that `upload_text_to_site` writes to, and writing them there is the generator's act; sending a sheet to a person stays held for Andrew. The upload itself is made by the issuer with the gateway tool `upload_text_to_site`; THIS cell makes the script produce, next to the sheets, the exact list of calls to make, and refuse a file the tool would refuse. You EDIT `workflows/gateway_battery/cheatsheet.py` (add one option to `gen-all`; keep `gen` and the rest of `gen-all` exactly as they are) and add one new test file.

**What to build.** `gen-all` gains one OPTIONAL option:

```
python workflows/gateway_battery/cheatsheet.py gen-all --census F --grants F --tier-decisions F --graded F --connect F --roster F --relevance F --out-dir D [--upload-manifest FILE]
```

and `workflows/gateway_battery/tests/test_cheatsheet_upload.py` with at least 5 tests. Without `--upload-manifest` the command prints and writes exactly what it does today (byte for byte); the existing `tests/test_cheatsheet.py` and `tests/test_cheatsheet_batch.py` must keep passing unchanged.

### The contract (it is the whole specification)

**The manifest.** With `--upload-manifest FILE`, after the sheets are validated and written, the script writes FILE: JSON with `json.dump(..., indent=1)` and a trailing newline, schema `gateway_sheet_upload/1`:

```
{"schema": "gateway_sheet_upload/1", "site": "default", "folder": "Opal Gateway Cheat Sheets",
 "files": [{"filename": "...", "content": "...", "bytes": N}, ...]}
```

- The four top-level keys are exactly these, with exactly these values for `schema`, `site` and `folder`.
- `files` holds ONE entry for each file the command writes under `--out-dir`: for each distinct roster person `<local>.md` and `<local>.examples.json` (so 2 x P entries), sorted by `filename` (plain string order). Each entry has exactly the keys `filename`, `content`, `bytes`. `content` is the file's text verbatim (the sheet text; the examples list as `json.dump(examples, indent=1)` followed by one newline, which is what is written to the file), and `bytes` is `len(content.encode("utf-8"))`.
- The manifest lists only the files written under `--out-dir`. The manifest file itself is written wherever `FILE` says and is never one of its own entries.
- The command's stdout stays EXACTLY the one `SHEETS people=P written=W legacy=L placeholder=H` line, exit 0.

**Guards** (a file the upload tool would refuse, refused here first). Every one of these is checked BEFORE anything is written, when `--upload-manifest` is given; each is a refusal: exit 2, ONE line on stderr starting `ERROR:`, NOTHING written (not the sheets, not the out folder, not the manifest):
1. Every `filename` matches `^[A-Za-z0-9._-]+\.(md|json)$` and no filename is listed twice. (The tool's own guard is `_FILENAME_BAD = re.compile(r'[\\/:*?"<>|]')` and a non-blank name, `infra/aws/ec2/opal-gateway/app/tools.py:382` and `:876`; this one is deliberately stricter.)
2. Every `content` is pure ASCII.
3. Every file is under 200000 bytes (a file of 200000 bytes or more is refused).
4. The folder that would hold FILE exists (the script does not create it).

The sheet rules themselves (which tools a person is listed, the placeholder line, narrowing by relevance) are the round-24 rules and do not change; the manifest does not re-decide anything, it copies what was written. The command reads no clock and no network, uploads and sends nothing, and the same inputs give byte-identical sheets and a byte-identical manifest.

**Clarifications of the contract against the real tool (issuer; they bind).**
- `upload_text_to_site` is `upload_text_to_site(site_id, folder_path, filename, content)` (`tools.py:870`): ALL FOUR arguments are required and it has NO default site. The manifest's `"site": "default"` is therefore a LABEL the issuer resolves into a `site_id` (with `find_sharepoint_site`) at upload time, and `"folder"` is what the issuer passes as `folder_path`. Write the two values exactly as above; do not invent a `site_id` field.
- The tool never overwrites: it writes with `conflictBehavior=fail` (`tools.py:872-875`), so a second upload of the same filename fails. File names are deterministic (the person's lower-cased local part), which is correct for a first upload; do not add a timestamp or a counter.
- The tool's filename guard also refuses a name containing `\ / : * ? " < > |`; guard 1 above already excludes all of them.

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/fixtures/w7_census.json`, `w7_tiers.json`, `w7_grants.json`, `w7_graded.json`, `w7_connect.md`, `w7_roster.txt`, `w7_relevance.json`: the round-24 fixtures (a 12 tool census, a 4 person roster: one profile person, two legacy people with a role, one legacy placeholder person). The criteria plant their defects into copies of these at run time; read them to see the shapes.
- Real outputs, for orientation (do not read them in the criteria): `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/sheets/` (the 17 real sheets and examples files; the largest is about 13 KB, all ASCII, every name matches guard 1).
- The tool definition, read-only: `infra/aws/ec2/opal-gateway/app/tools.py` lines 870-890 (`upload_text_to_site`).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. First run `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` (the one sparse change you may make; the issuer usually pre-adds these). Without `infra/aws/ec2/opal-gateway/app` you cannot read the tool definition.
1. Read `workflows/gateway_battery/cheatsheet.py` (`gen_all` and `Refusal` are what you extend), `tests/test_cheatsheet_batch.py` (its helper builders `make_inputs`, `census_doc`, `graded_doc`, `entry`, `relevance_doc`, `run_all`, `read`, `write` may be imported by path in your tests: put `sys.path.insert(0, <the tests folder>)` then `import test_cheatsheet_batch as b`; there is no `__init__.py`), the fixtures above, then `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y6_check.py` (the arms for your cell). Make the option, the guards and the test file.
2. Your test file holds at least 5 tests of its own: each runs the script by path as a subprocess on small inputs built with `tmp_path`. Cover at least: the manifest lists every written file verbatim; two runs give byte-identical manifests; the sheets are the same with and without the option; an unsafe filename, a non-ASCII character and an oversize file each exit 2 with an `ERROR:` line and nothing written; a missing manifest folder exits 2 with nothing written.
3. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other script under `workflows/`, `members.yaml`, the catalog, the emitter, any file under `infra/`, the PRD, or any other file. No AWS call, no network call, no grant, no deploy, no push, no upload and no send: the script writes local files only.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9. Only `re` is new among the imports. The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, firm or vendor is typed as a whole-string literal in the script (the folder name, the schema string, the site label and the filename pattern are the contract's fixed words and may appear); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y6.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `.../round25/checks/y6_check.py`). Read `y6_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them. (The environment variable `Y6_PKG_DIR` in the check is the issuer's; leave it unset.)
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/cheatsheet.py
workflows/gateway_battery/tests/test_cheatsheet_upload.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~89/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-6.sheets-upload-manifest.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W89-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y6.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; gen-all without the option is unchanged; with --upload-manifest it exits 0 and prints exactly SHEETS people=4 written=4 legacy=3 placeholder=1; the manifest has exactly the keys schema, site, folder and files with the contract values, 8 entries (a sheet and an examples file per person) sorted by filename, each with exactly filename, content and bytes, content verbatim the file written under --out-dir and bytes its UTF-8 length; every filename matches the pattern, every content is ASCII, every file is under 200000 bytes; the manifest lists exactly the files under --out-dir; each listed sheet carries exactly the tools its person is admitted to; the sheets are byte-identical with and without the option -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y6.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; two runs give byte-identical manifests and sheets; nothing is written outside --out-dir and the manifest path; the script holds no network or upload word and carries the folder name; an unsafe filename, a non-ASCII character, a file of 200000 bytes or more and a manifest folder that does not exist each exit 2 with one ERROR line and nothing written, and (except the last) the same inputs succeed without the option -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-y-6" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y6.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 5 passed) for `test_cheatsheet_upload.py` -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~89/NFRA_MCPINDEX.TO-MX-y-6.sheets-upload-manifest.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The `expect` fields are matched as a regex against your recorded output: record the literal printed tokens (`RESULT: PASS` then `exit=0`).
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. A strict-utf8 read of a log- or catalog-named file in a .py needs `errors="replace"` or the commit gate refuses it.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~89. Source: the CTO's round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` (msg 36225) ruling (c) and item 7: write the 17 sheets to the folder "Opal Gateway Cheat Sheets" in `upload_text_to_site`'s default site; delivery to a person stays held for Andrew. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (R25.3 Y6). **The face CLARIFIES Y6 against the real tool** (the clarifications bind; no decomposition change is needed, the manifest keys are unchanged): `upload_text_to_site(site_id, folder_path, filename, content)` has no default site (tools.py:870), so `"site": "default"` is a label the issuer resolves into a `site_id` with `find_sharepoint_site`, and `"folder"` is passed as `folder_path`; the tool never overwrites (tools.py:872-875), so the issuer uploads each file once and a re-run needs new names or an empty folder; guard 1 is stricter than the tool's own filename guard on purpose. Y6's sentence "no sheet content carries a tool name that the person's tier does not admit" is graded by the check on the listed sheets (the expected tool sets of the round-24 fixtures), not re-decided by the manifest code. The manifest FILE's location is not under `--out-dir`, so "writes only under --out-dir" (round 24) becomes "only under --out-dir and the manifest path". Base dry-runs 2026-10-20: y6.AC1 base: FAIL as expected (1 of 11 arms ok: only the regression arm, gen-all without the option unchanged, PASSes at the base as intended); y6.AC2 base: FAIL as expected (1 of 9 arms ok: the no-network arm, which holds trivially at the base); y6.AC3 base: FAIL as expected (test file absent). The issuer's scratch reference (a copy of the merged script carrying the option, plus 7 reference tests, outside the repository; the check reads it through `Y6_PKG_DIR`) passes y6.AC1 (11 arms), y6.AC2 (9 arms) and y6.AC3 (7 tests); fifteen planted mutants (content trimmed; bytes off by one; no ASCII guard; no size guard; no filename guard; unsorted files; wrong folder name; wrong schema; an extra manifest key; the examples files dropped; a second stdout line; a timestamp in the manifest; a network import; no manifest-folder guard; sheets that differ when the option is given) each read FAIL on AC1 or AC2. Real-input measurement: the 17 round-24 sheets and examples files are all ASCII, the largest is 12962 bytes, every name matches guard 1. Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
