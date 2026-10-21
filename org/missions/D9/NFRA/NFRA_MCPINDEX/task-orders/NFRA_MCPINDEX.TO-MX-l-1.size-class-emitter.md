# NFRA_MCPINDEX task order -- `MX-l-1` -- the catalog emitter states every table's size class as a measured claim: `--size-census`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round28-GATEWAY.md</decomp_doc>
<owned_cells>MX-l-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-l-1.size-class-emitter</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~97</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; one script edited and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant. The emitter reads local files; the option reads one more local JSON file.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (every criterion FAILs at the base: the option and the functions are absent) and the single-defect copies of the issuer's reference are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-l-1` (round 28, workstream GATEWAY; PRD v0.20 FWD-26, signed and admitted; CTO round-27 analysis `ledger/ROUND_ANALYSIS.round27.md` item 1)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). FWD-26 says every indexed table carries its folder, its plain-words meaning and a SIZE CLASS (small / large / very large) so Claude can warn before a heavy query. The size of each table was MEASURED by `workflows/gateway_battery/size_census.py` and written to a `size_census/1` file. You edit `workflows/atom_decomposition/emit_catalog_v02.py` so that `--size-census FILE` gives every row of the three asset sections a `size:` mapping, and you add the test file `workflows/atom_decomposition/tests/test_size_class.py`. You do NOT run the emitter into the catalog (the real emit is the issuer's drain act); the index states the class and refuses nothing.

**The census file** `size_census/1` is JSON: `schema`, `read_at` (a full UTC stamp `YYYY-MM-DDTHH:MM:SSZ`), `catalog_md5`, `entries[]`, `skipped[]`. An entry holds `entity`, `section`, `bucket`, `prefix`, `newest_partition`, `bytes_newest` (listed bytes), `rows_newest` (or null), `bytes_uncompressed_newest` (or null) and `error` (null or a code); a skipped item holds `entity`, `section`, `reason`. A real example: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/evidence/SIZE_CENSUS_20261021.json`. Fixtures for your tests are YOURS to write inside each test (small, synthetic); the issuer's check fixtures are `round28/fixtures/l1_*` under the same deliverables folder.

### The contract (the decomposition's L1 as AMENDED by the issuer at the cut; where the two differ THIS section wins)

1. **The option.** `--size-census FILE` (optional; absent = the existing output byte for byte, and the existing options behave as before). A named FILE that does not exist exits 2 with the line `EMIT REFUSED (size census): <FILE> does not exist -- NOTHING WRITTEN` before anything is read or written (the same shape as the existing `--serves-map` refusal). A file that is unreadable, not JSON, or has another `schema` than `size_census/1` is an emit error (item 6).
2. **Matching is by ENTITY, not by location.** The census is keyed by each entry's `entity` (and each skipped item's `entity`); a row is matched to the entry whose `entity` equals the row's `entity`. Two entities may share one (bucket, prefix) in the real census and each takes its own entry. For a measured row the entry's `bucket` and `prefix` must equal the row's `bucket` and `prefix`; a difference is an emit error naming the entity.
3. **The mapping.** Every row of `silver_datasets`, `portal_datasets` and `harvest_datasets` gains a `size` key, appended AFTER the row's existing fields (it is the last key), as exactly one of:
   - measured (the entity has an entry with no `error`): the keys in THIS order `class`, `claim`, `measured_at`, `newest_partition`, `rows`, `bytes`, `basis` with `claim: measured`; `measured_at` is the first ten characters of the census `read_at` (a `YYYY-MM-DD` string); `newest_partition` and `rows` are the entry's `newest_partition` and `rows_newest` (null stays null); `bytes` is `bytes_uncompressed_newest` and `basis` is `uncompressed` when `bytes_uncompressed_newest` is not null, else `bytes` is `bytes_newest` and `basis` is `listed`; `class` is `size_class(bytes, rows)`. A measured entry whose chosen byte count is not a non-negative integer is an emit error naming the entity;
   - absent (the entity has no usable entry): the keys in THIS order `class`, `claim`, `reason` with `class: unmeasured`, `claim: absent` and `reason` the census skipped reason, the entry's `error` code, or `not in the census`.
4. **The class** is computed in the emitter by the ruled thresholds, held as module constants `SIZE_LARGE_BYTES = 8388608` (8 MiB), `SIZE_VERY_LARGE_BYTES = 25165824` (24 MiB) and `SIZE_VERY_LARGE_ROWS = 1000000`: `size_class(nbytes, rows=None)` returns `very large` when `nbytes >= SIZE_VERY_LARGE_BYTES` or (`rows` is not None and `rows >= SIZE_VERY_LARGE_ROWS`), else `large` when `nbytes >= SIZE_LARGE_BYTES`, else `small`.
5. **The header.** With the option, the catalog gets ONE extra comment line written once, right after the existing header block and a blank line, then another blank line: `# size census: <read_at> over catalog <catalog_md5> (thresholds 8 MiB, 24 MiB, 1000000 rows)` (read_at as in the file). Without the option no line is added.
6. **Errors refuse.** Every emit error of this option (items 1 to 3, a duplicate entity in `entries`, an entity both in `entries` and `skipped`, an entity twice in `skipped`, a `read_at` that is not a full UTC stamp, a missing `catalog_md5`, a row with no `entity`, an invalid mapping) is collected and, if there is any, printed as `EMIT REFUSED (size census, MX-l-1): <n> error(s) -- NOTHING WRITTEN:` followed by one indented line per error, and `main` returns 2 BEFORE the output file is written (the existing refusal blocks are the model; put it before the single write).
7. **`validate_size(label, m)`** returns a list of error strings (empty when valid) and is the one place a mapping is validated; it is applied to every mapping the option attaches. It refuses: `class` outside `small`, `large`, `very large`, `unmeasured`; a measured mapping whose keys are not exactly the measured keys in the item-3 order, whose `measured_at` is not a `YYYY-MM-DD` string, whose `basis` is not `uncompressed` or `listed`, whose `bytes` (or non-null `rows`) is not a non-negative integer, or whose `class` does not follow `size_class(bytes, rows)`; an absent mapping whose keys are not exactly the absent keys in order, whose `class` is not `unmeasured`, or whose `reason` is empty; any other `claim`. NOTE (a correction to the decomposition): do NOT route this through the existing `validate_claim`, which requires a full UTC stamp for `measured_at`; the size mapping carries a date.
8. **Nothing else changes.** Every other field of every row, the whole tool_index and every other section are untouched; two runs with the same inputs give the same bytes; no firm token enters the code (the naming gate).

### The interface the checks call (names are exact; all at module level in `emit_catalog_v02.py`)

- constants `SIZE_CENSUS_SCHEMA = "size_census/1"`, `SIZE_LARGE_BYTES`, `SIZE_VERY_LARGE_BYTES`, `SIZE_VERY_LARGE_ROWS`;
- `size_class(nbytes, rows=None)` -> str;
- `validate_size(label, m)` -> list of str;
- `load_size_census(path)` -> `(census, errors)`: reads the file, validates item 6's file-level errors, returns a census object (any shape you like, passed back to `attach_size` and `size_header_line`); an unusable file returns errors;
- `attach_size(section_rows, census)` -> list of str: `section_rows` is the emitter's dict of section name -> list of row dicts (the three asset sections as keys; a missing key is an empty list); it APPENDS `size` to each row in place and returns the errors of items 2, 3 and 7;
- `size_header_line(census)` -> the item-5 line without a newline;
- `apply_size_census(path, section_rows)` -> `(header_line, errors)`: `("", [])` with the rows untouched when `path` is None or empty; else loads, attaches and returns the header line (empty string when there are errors) and every error;
- `main` adds the option with `ap.add_argument("--size-census", ...)`, refuses a missing file (item 1), calls `apply_size_census(args.size_census, section_rows)` once the rows are final and BEFORE the output directory is made, keeps its errors in a variable named `size_errors` and refuses on them (item 6), writes the header line (item 5), and prints one summary line `SIZE CENSUS (MX-l-1, round 28): rows classed small N, large N, very large N, unmeasured N` when the option is used.

### Inputs you read (you do NOT edit them)

- `workflows/atom_decomposition/emit_catalog_v02.py` (you edit it), its tests `tests/test_group_links.py`, `tests/test_c_group.py`, `tests/test_tool_index_and_harvest.py`, `tests/test_depth_kinds.py`, `tests/test_serves_map.py` (the model for a test file here: `test_serves_map.py` loads the emitter by path and exercises the functions on synthetic rows), `workflows/gateway_battery/size_census.py` (the census writer), the example census above.
- Where the rows are built: `main` builds a `section_rows` dict from `build_asset_rows`; `GROUP_SECTIONS` names the three asset sections; rows are dumped with `_yaml.safe_dump(..., sort_keys=False)`, so a key appended to a row dict lands last in the output with no change to a writer. Find the existing refusal blocks (search for `EMIT REFUSED`) and the single write of the output file, and the header string; the rest of the emitter you do not touch.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. FIRST run `git sparse-checkout add workflows/gateway_battery workflows/atom_decomposition infra/aws/ec2/opal-gateway/app infra/aws/lambda/ci/function-map` (the only sparse change you may make; the issuer pre-adds them, and the command is harmless when they are there). Without them the cone can lack the folders the naming gate reads.
1. Read the emitter around `main`, the refusal blocks and `test_serves_map.py`, then read `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l1_check.py` (the executable form of this section; read what each arm grades). Edit the emitter, then write the test file: at least 8 tests of your own, on rows and a census you build inside each test: the threshold edges (8388607 / 8388608 / 25165823 / 25165824 bytes; 999999 / 1000000 rows); uncompressed bytes win over listed bytes and `basis` says which; unmeasured rows carry the three reasons; `size` is the last key and nothing else changes; two entities sharing a location take their own entries; a mismatched location and a missing byte count are errors; the load refusals (another schema, a duplicate entity, measured and skipped, a short `read_at`, not JSON); no option leaves rows and header alone; `validate_size` refuses planted defects; an absent `--size-census` file makes `main` return 2.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`. Run `python -m ruff check` on both files you touch (py39) and fix what it prints before you commit.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's checks, fixtures or decomposition, `size_census.py`, `tool_battery.py`, any other script or test under `workflows/`, `members.yaml`, the catalog (`DATA_CATALOG.yaml`) or any row file under `catalog_entries/`, the PRD, any file under `infra/`, or the round-23 to round-27 evidence. Do NOT run the emitter with its default output (it writes the catalog): the criteria and your tests call functions, or `main` only on a path that refuses before any write. No AWS call, no network call, no grant, no deploy, no push.
2. Python 3.9, standard library plus what the emitter already imports. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9. The commit gate runs `py_compile`, the naming gate and `ruff` for py39 (semicolon-separated statements are E702 errors: one statement per line), and it BLOCKS a strict-utf-8 `open()` of a path whose name or variable contains `log` or `catalog`: write `errors="replace"` on every `open()` you add for reading (the reference-style `open(path, encoding="utf-8")` on a variable named `path` is fine). The naming gate must exit 0 on your code commit; if it prints NAMING ERROR, add the sparse folders of step 0 and run it again.
3. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output (no new key in a row, no new option beyond `--size-census`, no change to a section writer).
4. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
5. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l1.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `l1_check.py` in the same folder). Do not edit any of them. (The environment variable `L1_ROOT` in the check is the issuer's; leave it unset.)
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_size_class.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~97/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-l-1.size-class-emitter.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W97-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-l-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l1.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (fixture l1, 14 rows in 3 sections, a census of 12 entries and 1 skipped item, 14 expected size mappings); the interface present; the class edges and row edges right; the census loads and attaches with no error; every one of the 14 rows takes exactly its expected size mapping in the contract key order, two entities sharing a location each take their own entry, the unmeasured reasons are right, size is the last key and other fields are untouched, the header line is exact, the YAML of a row is ASCII and loads back to the same mapping, validate_size accepts every attached mapping -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-l-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l1.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the controls (a missing --serves-map file still exits 2, --help still lists the existing options) ok; --help lists --size-census; a missing --size-census file exits 2 with EMIT REFUSED (size census) and nothing written; no option changes nothing; the planted census and attach refusals, the planted validate_size defects and the determinism arm all ok; main is wired to the option -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-l-1" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round28/checks/l1.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 96 passed: the 88 existing tests of the five files plus at least 8 of test_size_class.py) -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~97/NFRA_MCPINDEX.TO-MX-l-1.size-class-emitter.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes. The proof's `to_id` is the FULL order id `NFRA_MCPINDEX.TO-MX-l-1.size-class-emitter` (the short id is read as a defect at the round close). The checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, and record the output so that `RESULT: PASS` is followed by `exit=0`.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip. Message files are written with the Write tool, ASCII, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 28, workstream GATEWAY, worker ~97. Source: PRD v0.20 FWD-26 (signed and admitted, CVO review @a81f56eb3e), the CTO's round-27 analysis (msg 36317, `ledger/ROUND_ANALYSIS.round27.md` @f5f824c16e) item 1 and the ruling on the size thresholds (msg 36313). Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round28-GATEWAY.md` (R28.3 L1, frozen at the cut; this order AMENDS it in two places, found by building the reference: (1) the decomposition matches a census entry by (bucket, prefix) and makes a duplicate prefix an emit error, but the real census of 2026-10-21 has two entities on one location, so matching is by ENTITY and the location must agree; (2) it says `validate_claim` accepts the measured form, which cannot hold because the existing rule demands a full UTC stamp equal to `read_at` while L1 fixes a date, so a separate `validate_size` carries the rule). The cell does not change the trunk catalog: nothing reaches it before NFRA_OPLGTW batch17's ledger reads CLOSED (the tracked catalog must stay md5 03d2dbbae1f07b8d4fa5f0eaa73355d6); the real emit, diff and placement are drain acts (R28.4 step 1). Lessons carried from rounds 24 to 27: the sparse cone may lack folders (step 0); the commit gate blocks a strict utf-8 `open()` on a path whose name contains `log` or `catalog`; every mutant in the checks is planted from fixtures; a refusal arm requires the script's own `EMIT REFUSED` text; the proof's `to_id` is the full order id.
Base dry-runs 2026-10-21 (option, constants and functions absent): `l1.AC1` base: FAIL as expected (0 of 1 arms: the interface is missing, the rest cannot run); `l1.AC2` base: FAIL as expected (2 ok, 2 failed: the two controls, a missing --serves-map file still exits 2 and --help still lists the existing options, PASS at the base; the --size-census help line and the interface FAIL); `l1.AC3` base: FAIL as expected (test file absent). The issuer's scratch reference (the emitter patched in a copy at `C:/tmp/l1ref`, outside the repository, pointed at with `L1_ROOT`; 11 tests of its own) passes all three (15 of 15, 26 of 26, 99 tests = the 88 existing + 11); its ruff run is clean. Four single-defect copies of the reference each fail the check: `>` instead of `>=` at 8 MiB fails `l1.AC1` (2 arms) and `l1.AC2` (2 arms); listed bytes always (uncompressed ignored) fails `l1.AC1` (3 arms); matching by location instead of entity fails `l1.AC1` (2 arms) and `l1.AC2` (1 arm); rows ignored fails `l1.AC1` (3 arms).

<status>issued</status>
<round>28</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
