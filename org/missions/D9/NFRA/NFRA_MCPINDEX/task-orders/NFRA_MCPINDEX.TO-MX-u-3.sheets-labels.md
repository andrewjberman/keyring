# NFRA_MCPINDEX task order -- `MX-u-3` -- cheatsheet.py gen-all learns `--platform-labels`: a `Platform labels` section on every sheet that lists a `client_*` tool, read from a `gateway_platform_labels/1` file

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md</decomp_doc>
<owned_cells>MX-u-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-u-3.sheets-labels</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~96</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant, no upload: the script writes sheets, the issuer decides what is uploaded.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every new-behavior arm FAILs at the base) and the planted-mutant controls the issuer ran against a reference are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-u-3` (round 27, workstream GATEWAY; PRD v0.19 FWD-25; CTO round-26 analysis `ledger/ROUND_ANALYSIS.round26.md`, item 2 and ruling 3.1)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). `cheatsheet.py gen-all` writes one cheat sheet (`<local>.md`) and one examples list (`<local>.examples.json`) per roster person. The `platform` argument of the `client_*` tools is a CUSTODIAN label read from the vendor's own data, never a vendor or contract name; a person cannot guess it, so each sheet that lists a `client_*` tool must say what the label is and what leaving it out does. Another cell (MX-u-1) reads the label rules out of the gateway source into a `gateway_platform_labels/1` file; this cell makes the sheets use that file. The two cells are independent: you work from the fixture file named below.

**What to build.** `gen-all` gains one OPTIONAL option:

```
python workflows/gateway_battery/cheatsheet.py gen-all --census F --grants F --tier-decisions F --graded F --connect F --roster F --relevance F --out-dir D [--upload-manifest FILE] [--platform-labels FILE]
```

and `workflows/gateway_battery/tests/test_cheatsheet_labels.py` with at least 6 tests. Without `--platform-labels` the command prints and writes exactly what it does today (byte for byte, with or without `--upload-manifest`); the existing `tests/test_cheatsheet.py`, `tests/test_cheatsheet_batch.py` and `tests/test_cheatsheet_upload.py` keep passing unchanged. `gen` (one employee) is NOT changed.

### The contract (it is the whole specification)

**The labels file** (`--platform-labels FILE`): JSON, schema `gateway_platform_labels/1`: `{"schema": "gateway_platform_labels/1", "items": [{...}, ...]}`. Each item is an object with the keys `tool`, `adapter`, `firm`, `accepts_platform`, `platform_meaning`, `label_source`, `omit_means`, `refusals`, `cite`, `evidence`. THIS CELL READS ONLY four of them and requires each to be a non-blank string: `tool`, `adapter`, `platform_meaning`, `omit_means`; the other keys are neither read nor validated.

**The section.** For every sheet that lists at least one `client_*` tool (a tool whose name starts with `client_` and which the sheet lists under a `###` heading, that is, in the person's narrowed `by_channel`), the sheet text as `build_sheet` returns it is followed by exactly:

```
<one blank line>
## Platform labels
<one blank line>
<one line per entry, see below>
```

i.e. new_text = old_text + "\n## Platform labels\n\n" + "\n".join(lines) + "\n" (old_text already ends with one newline). The lines, for the `client_*` tools the sheet lists, sorted by tool name (plain string order):
- a tool with exactly ONE item in the file: `- <tool>: platform: <platform_meaning> | omit: <omit_means>`;
- a tool with SEVERAL items: one line per item, sorted by `adapter` (plain string order): `- <tool> [<adapter>]: platform: <platform_meaning> | omit: <omit_means>`;
- a listed `client_*` tool with NO item: `- <tool>: platform label not recorded in the labels file`.
A sheet that lists no `client_*` tool is byte-identical to what it is without the option. The examples files are never changed by the option. The stdout stays EXACTLY the one `SHEETS people=P written=W legacy=L placeholder=H` line, exit 0.

**Guards.** The labels file is read and checked BEFORE anything is written (when the option is given); each of these is a refusal: exit 2, ONE line on stderr starting `ERROR:`, NOTHING written (not the sheets, not the out folder, not an upload manifest):
1. the file cannot be read or is not JSON;
2. `schema` is not `gateway_platform_labels/1`, or `items` is not a list, or an item is not an object;
3. an item lacks one of `tool`, `adapter`, `platform_meaning`, `omit_means`, or one is not a non-blank string;
4. a `tool` that does not start with `client_` (the file may describe only `client_*` tools);
5. any of the four texts holds a non-ASCII character or a line break (`\n` or `\r`);
6. two items carry the same (`tool`, `adapter`) pair.
The order of the items in the file does not matter: the same items in any order give byte-identical sheets. With `--upload-manifest` given as well, the manifest carries the sheets as written, the section included, and keeps all its round-25 guards. The command reads no clock and no network, uploads and sends nothing, and the same inputs give byte-identical output. The section holds no data value and no account identifier: it copies the two texts of the file and nothing else.

**Clarifications of the decomposition's U3 paragraph (issuer; they bind).** The decomposition says each line states "the tool name, then `platform: ` ... then `omit: `"; the exact line shapes above are the specification (the adapter appears in brackets only when a tool has several items). "An unknown tool name" means a tool outside the `client_` prefix (guard 4); do NOT type any tool name in the script (only the prefix `client_`, the schema string, the heading and the fixed phrases of this contract may appear as literals).

### Inputs you read (you do NOT edit them)

- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/fixtures/u3_labels.json`: a hand-made labels file (six items; `client_get_holdings` has two adapters; the tools, adapters and texts are fixtures, not real data); read it to see the shape.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/fixtures/w7_*.json|md|txt`: the round-24 fixtures (a 12 tool census, a 4 person roster: one profile person, two legacy people with a role, one legacy placeholder person); `round27/fixtures/u3_base/`: the eight files `gen-all` wrote on those fixtures BEFORE this cell (the criteria compare against them byte for byte). The criteria plant their defects into copies at run time.
- Real outputs, for orientation only: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/sheets/` (the 17 real sheets).

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. First run `git sparse-checkout add infra/aws/ec2/opal-gateway/app workflows/atom_decomposition workflows/gateway_battery` (the one sparse change you may make; the issuer usually pre-adds these).
1. Read `workflows/gateway_battery/cheatsheet.py` (`gen_all`, `build_sheet`, `upload_manifest_text` and `Refusal` are what you extend), `tests/test_cheatsheet_batch.py` (its helper builders `make_inputs`, `census_doc`, `graded_doc`, `relevance_doc`, `run_all`, `read`, `write` may be imported by path in your tests: `sys.path.insert(0, <the tests folder>)` then `import test_cheatsheet_batch as b`; there is no `__init__.py`), `tests/test_cheatsheet_upload.py` (the pattern of a subprocess test), the fixtures above, then `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u3_check.py` (the arms for your cell). Make the option, the guards and the test file.
2. Your test file holds at least 6 tests of its own: each runs the script by path as a subprocess on small inputs built with `tmp_path` (to get a sheet that lists a `client_*` tool, add such tools to a principal's `by_channel` in the grants file you write). Cover at least: the section's lines for one-item and several-item tools; a sheet with no `client_*` tool is unchanged; a listed tool with no item gets the not-recorded line; two runs are byte-identical; each guard exits 2 with an `ERROR:` line and nothing written; the manifest carries the section.
3. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other script under `workflows/`, `members.yaml`, the catalog, the emitter, any file under `infra/`, the PRD, or any other file. No AWS call, no network call, no grant, no deploy, no push, no upload and no send: the script writes local files only.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9. The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. No tool name, firm or vendor is typed as a whole-string literal in the script (the prefix `client_`, the schema string, the heading and the phrases of the contract are the fixed words and may appear); tests under `tests/` and data files are exempt.
4. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u3.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `.../round27/checks/u3_check.py`). Read `u3_check.py` for exactly what each arm grades; it is the executable form of section 1. Do not edit any of them. (The environment variable `U3_PKG_DIR` in the check is the issuer's; leave it unset.)
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/cheatsheet.py
workflows/gateway_battery/tests/test_cheatsheet_labels.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~96/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-u-3.sheets-labels.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W96-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 3)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-u-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u3.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; gen-all without the option writes exactly the frozen round-25 files; with --platform-labels it exits 0 and prints exactly SHEETS people=4 written=4 legacy=3 placeholder=1; the sheets and examples files of people who list no client_ tool, and every examples file, are byte-identical to the frozen files; the profile person's sheet is the frozen sheet plus exactly the section for client_get_holdings (one line per adapter, sorted by adapter); with all five client_ tools listed the sheet is the plain sheet plus the exact section (tools sorted); the section is last, the heading appears once, ASCII and no CR; a labels file in reverse item order gives the same sheets; a listed tool with no item gets the not-recorded line; sheets that list no client_ tool carry no section; ARMS lines with 0 failed; RESULT: PASS then exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-u-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u3.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; regression: gen-all with --upload-manifest and without the option still writes exactly the frozen round-25 sheets; both options together exit 0 and print exactly the SHEETS line; the upload manifest carries the sheets as written with the section and bytes the UTF-8 length; two runs byte-identical; nothing written outside --out-dir and the manifest path; the script reads no network; eight refusals (a wrong schema, an item without platform_meaning, a tool outside the client_ tools, a non-ASCII character, a line break, two items for one tool and adapter, an items value that is not a list, a labels file that does not exist) each exit 2 with one ERROR line and nothing written while the same inputs without the option succeed; ARMS lines with 0 failed; RESULT: PASS then exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-u-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round27/checks/u3.AC3.sh; echo "exit=$?"</invocation><expect>DENOMINATOR: pytest rc=0 passed=N (minimum 6) with N at least 6 for tests/test_cheatsheet_labels.py; ARMS: 1 ok, 0 failed; RESULT: PASS then exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~96/NFRA_MCPINDEX.TO-MX-u-3.sheets-labels.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The `expect` fields are matched as a regex against your recorded output: record the literal printed tokens (`RESULT: PASS` then `exit=0`).
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. A strict-utf8 read of a log- or catalog-named file in a .py needs `errors="replace"` or the commit gate refuses it.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.


<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 27, workstream GATEWAY, worker ~96. Source: the CTO's round-26 analysis `ledger/ROUND_ANALYSIS.round26.md` (msg 36269) item 2 ("write the label set into the per-employee sheets") and ruling 3.1 (the `platform_not_source_label` refusals are not tool faults until a run uses the labels the tools accept; the vocabulary is not in the tool descriptions, so a person cannot guess it). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round27-GATEWAY.md` (R27.3 U3). **The face CLARIFIES U3** (the clarifications bind; no decomposition change is needed): the exact line shapes (the adapter in brackets only when a tool has several items), the not-recorded line for a listed tool the file does not describe, "unknown tool name" = a tool outside the `client_` prefix, and that only four item keys are read. Real-data note: the sheets of the 17 round-24 people list a `client_*` tool only for the profile person and the legacy people whose tier admits one; the U1 file does not exist yet when this cell runs, so the cell works from the hand-made fixture; the issuer regenerates the 17 sheets with the real U1 file at the drain (they stay local; the sheets' site is held for Andrew). Base dry-runs 2026-10-21: u3.AC1 base: FAIL as expected (1 of 9 arms ok: only the control, gen-all without the option equals the frozen round-25 files, which holds at the base); u3.AC2 base: FAIL as expected (2 of 14 arms ok: the regression arm with --upload-manifest and the no-network arm, which hold at the base); u3.AC3 base: FAIL as expected (test file absent). The issuer's scratch reference (a copy of the merged script carrying the option plus 7 reference tests, outside the repository; the check reads it through `U3_PKG_DIR`) passes u3.AC1 (9 arms), u3.AC2 (14 arms) and u3.AC3 (7 tests), and the 37 tests of the four cheatsheet test files pass with it; ten planted mutants (the section on every sheet; tools unsorted; adapters unsorted; no ASCII guard; no `client_` prefix guard; the not-recorded line dropped; no duplicate guard; the heading changed; the omit text dropped; a second stdout line) each read FAIL on AC1 or AC2.

<status>issued</status>
<round>27</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
