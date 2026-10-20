# NFRA_MCPINDEX task order -- `MX-y-3` -- the emitter reads link GROUPS (one (bucket, vendor, firm) key per group, named in a groups file, never a firm token per link) and admits the C-GROUP store words; the four store rows lose the doubled `dynamodb_dynamodb_` prefix and the scoped-API row names its store

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-3.group-links-and-store-words</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~86</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; edits to one script, four renamed entry files, one entry, two tool_index files and one new test file.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (all three criteria FAIL at the base) and the planted fixture and present-data arms inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-3` (round 25, workstream GATEWAY; PRD v0.19 FWD-23; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` rulings (a) and (b), items 3 and 4)

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The catalog emitter `workflows/atom_decomposition/emit_catalog_v02.py` reads `tool_index/members.yaml`. Two rulings of the CTO change it:

- **(a) the `client_*` tools' links.** A link line that names a catalog row by its id carries a firm token (the ids hold the firm), and the commit-time naming gate refuses such a new line in `members.yaml`. The ruling: the link names the (bucket, vendor, firm) KEY once per GROUP, no firm token per line, no naming exception. The issuer measured the gate on the key itself: a `firm: <firm token>` line in `members.yaml` is refused as well (the gate reads a YAML value as a hand-kept carrier), while the same key in a JSON file under `org/` is not graded. So the key lives in a JSON GROUPS FILE under `org/` that the emitter reads (`--link-groups`), and `members.yaml` names only a group ID, which carries no firm token.
- **(b) the store rows.** The emitter's bucket vocabulary admits only `opal-data-` bucket names and DynamoDB wording, so a store row could not carry its own store word. It must admit the C-GROUP store words, the doubled `dynamodb_dynamodb_` entity prefix goes, and the scoped-API row names its store `amgt-scoped-api` with its route as the table.

You EDIT the emitter, rename four entry files and the ids that name them, edit one entry, and add one new test file.

### The contract (it is the whole specification; where it differs from the decomposition's Y3 paragraph, THIS text wins)

**Y3-i LINK GROUPS.**

1. `--link-groups FILE` (repeatable, like `--group-map`): a JSON file `{"schema": "gateway_link_groups/1", "groups": {"<id>": {"bucket": str, "vendor": str, "firm": str}}}`. A group id matches `^[a-z][a-z0-9_]*$`; a group holds EXACTLY the three keys, each a non-empty string; the same id in two files is an error; a wrong schema string is an error. The vocabularies of `GROUP_VENDORS` / `GROUP_FIRMS` are NOT checked here (a typo shows as a group that matches no row, below). A named file that does not exist makes `main` return 2 with `EMIT REFUSED (link groups): <path> does not exist -- NOTHING WRITTEN` before anything is read or written (the way `--group-map` does).
2. `load_link_groups(paths)` returns `(groups, errors)`: `groups` is `{id: {"bucket", "vendor", "firm"}}`, `errors` a list of strings (empty when valid). A file with errors contributes none of its groups.
3. `build_row_groups(section_rows)` returns `{entity: (bucket, vendor, firm)}` for every row of the three asset sections (`GROUP_SECTIONS`) that carries all three keys non-empty; a row missing one is left out. `main` builds it AFTER `apply_group_map` and `settle_row_buckets`, so a row's group key is the one the emitted catalog carries.
4. `load_tool_index(row_ids, census=None, row_keys=None, link_groups=None, row_groups=None)` gains the two keyword parameters (default None; with None every behavior of today is unchanged, byte for byte). For a member (a) entry:
   - a `links` element may be a mapping `{"group": "<id>"}` (a mapping with exactly that one key): it expands IN PLACE to the entity ids of the rows whose `(bucket, vendor, firm)` equals the group's key, sorted;
   - a `links` element that is a plain string stays EXACTLY as written, and a repeated plain string stays repeated (a per-link depth may name one row twice; an existing test relies on it);
   - an id that a GROUP expands to is skipped when the list already holds it;
   - `index` may be a mapping `{"group": "<id>"}`: it becomes the FIRST sorted entity id of the group;
   - the expansion happens BEFORE the existing checks, so the existing rule (the index is a row id and is in `links`, every link is a row id, the per-link depth rows equal the links) runs on the expanded lists, and the emitted entry carries the plain expanded ids (never the mapping);
   - a group id that no `--link-groups` file names (or `link_groups` None) is an error string that contains the tool name and the group id; a group that matches no row is an error string that contains the tool name, the group id and the words `no catalog row`.
5. `main` passes `link_groups` (from `load_link_groups(args.link_groups)`) and `row_groups` to `load_tool_index`, and adds the `load_link_groups` errors to the other group errors it already reports.

**Y3-ii STORE WORDS.** `STORE_BUCKET_WORDS = ("dynamodb", "graph", "amgt-scoped-api")` (constants `DYNAMODB_BUCKET`, `MS365_BUCKET` exist; add `SCOPED_API_BUCKET = "amgt-scoped-api"`). `normalize_bucket(value)` keeps its order of rules (any wording that names DynamoDB becomes `dynamodb`; an S3 bucket name is kept) and ALSO returns the value unchanged when it is exactly one of the three store words; anything else is still None (a lookalike such as `amgt-scoped-apix`, a bare `opal-data`, a URL stay None). `settle_row_buckets` therefore accepts a row whose bucket is a store word. No other store word is admitted.

**Y3-iii THE DOUBLED PREFIX.** The four entries `catalog_entries/dynamodb_dynamodb_etf_classifications.yaml`, `..._opal_keyword_intelligence.yaml`, `..._opal_news_articles.yaml`, `..._opal_news_trending_daily.yaml` are renamed (use `git mv`) to `dynamodb_etf_classifications.yaml`, `dynamodb_opal_keyword_intelligence.yaml`, `dynamodb_opal_news_articles.yaml`, `dynamodb_opal_news_trending_daily.yaml` (the entity id is the file name). Each old id is named exactly 4 times in `tool_index/members.yaml` and 0 times in `tool_index/pending_members.yaml`: change those 16 occurrences (and any in `pending_members.yaml`) to the new ids, nothing else in those two files. Print a census beside the result (a grep count of the old string over `workflows/atom_decomposition` before and after).

**Y3-iv THE SCOPED-API ROW.** In `catalog_entries/published_analysis_scoped_api.yaml`: `bucket: amgt-scoped-api` (was `opal-data-harvest`), `table: /api/scoped/amgt` (was null; the route the code names in `app/harvest_published.py`), and replace the `open_items` line that explains the forced bucket with a one-line note that the bucket is the C-GROUP store word and the table the route, as ruled in round 25. The issuer measured the naming gate on exactly these two values: it accepts both (`CONFORMANT as API_GW`, and the route is not graded). If the gate refuses either on your commit, STOP on that file, report the gate text, and do not work around it.

### Inputs you read (you do NOT edit them)

- The emitter and the tests beside it: `workflows/atom_decomposition/tests/test_c_group.py` (the model for a test file on synthetic rows: `_load_emitter`, `_sections`), `tests/test_depth_kinds.py` (the model for `load_tool_index` on a temp `TOOL_INDEX_DIR`: it injects the census and the row-key map), `tests/test_tool_index_and_harvest.py`, `tests/test_serves_map.py`.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/fixtures/y3_link_groups.json`, `y3_rows.json`, `y3_census.json`: the criterion AC1's fixture.
- Round 24's findings: `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round24/evidence/CATALOG_CANDIDATE_20261020.md` and `APPLY_REPORT_R24.json`.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The sparse cone may NOT hold everything the tests and the criteria read. First run `git sparse-checkout add infra/aws/ec2/opal-gateway lib infra/logic/registry workflows/atom_decomposition` (the only sparse change you may make; the folders are read-only for you except the files in `<paths>`). The existing `test_c_group.py` reads files under `infra/aws/ec2/opal-gateway/deploy/`, and the fork-registry join reads `lib/opal_naming.py` and `infra/logic/registry/`.
1. Control (must pass before you start): from `workflows/atom_decomposition`, `PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_c_group.py tests/test_tool_index_and_harvest.py tests/test_depth_kinds.py tests/test_serves_map.py` prints `72 passed`.
2. Read `emit_catalog_v02.py` (`normalize_bucket`, `settle_row_buckets`, `load_group_maps`, `apply_group_map`, `load_tool_index`, `main`) and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y3_check.py` (the executable form of this section; read what each arm grades). Make the changes of Y3-i, Y3-ii, Y3-iii and Y3-iv, then write `workflows/atom_decomposition/tests/test_group_links.py` with AT LEAST 8 tests of your own on synthetic rows, groups and members you write inside the test (not the issuer's fixtures). They cover at least: the expansion of a group in `links` (sorted ids), an `index` written as a group, equality of the group form with the line-per-row form, a repeated plain id staying repeated while a group-expanded duplicate is skipped, an unknown group (error names tool and group), a group matching no row (error names tool, group and `no catalog row`), `load_link_groups` refusals (wrong schema, bad id, missing key, repeated id), the missing-file exit 2 of `main`, `build_row_groups`, and `normalize_bucket` / `settle_row_buckets` on the store words and on a lookalike.
3. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, any other file under `workflows/atom_decomposition/` (the other tests, the other entries, the group maps, the census tools), `workflows/gateway_battery/`, any file under `infra/` or `lib/`, the PRD, the live catalog, or any evidence. In `members.yaml` and `pending_members.yaml` you change ONLY the 16 id occurrences of Y3-iii. You write NO group-form link into `members.yaml` and no groups file: the issuer does at the drain. You do NOT run the emitter against the live catalog and do not regenerate or overwrite `infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml`. No AWS call, no network call, no grant, no deploy, no push.
2. Python 3.9, standard library plus `yaml` (PyYAML, installed) only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39.
3. THE NAMING GATE reads every added line of a `.py` or `.yaml` file under `workflows/`. No firm, vendor or product token is typed as a literal in the emitter or in your tests (use neutral values such as `va`, `fa`, `opal-data-xa` and ids like `r.a1`, as the criteria's fixtures do; the new store word `amgt-scoped-api` and the route in the entry file are the two values the issuer measured as accepted). Before you commit, run `python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <a file listing the staged paths>`; it must exit 0, and a REFUSE on a line you added is yours to fix, not to override.
4. File reads: a read of a file named `*catalog*` or `*log*` with `open(...)` and no `errors=` is refused by the commit gate (strict utf-8 log read): pass `errors="replace"` on any new read of that kind (the emitter's existing reads are not yours to change).
5. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output (no new key in the emitted catalog, no new option beyond `--link-groups`, no new store word).
6. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
7. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y3.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `y3_check.py` in the same folder). Do not edit any of them.
8. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_group_links.py
workflows/atom_decomposition/catalog_entries/dynamodb_*.yaml
workflows/atom_decomposition/catalog_entries/published_analysis_scoped_api.yaml
workflows/atom_decomposition/tool_index/members.yaml
workflows/atom_decomposition/tool_index/pending_members.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~86/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-3.group-links-and-store-words.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W86-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y3.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the link-groups reader returns the fixture's groups and refuses a wrong schema, an upper-case id, a missing key, an empty vendor and a repeated id; build_row_groups keeps only rows with all three keys; a group in links and an index written as a group expand to the same ids as the line-per-row form; a repeated plain id stays and a group-expanded duplicate is skipped; an unknown group and a group matching no row are refused naming the tool and the group; without link groups the line form is unchanged; normalize_bucket admits exactly the three store words and refuses lookalikes; settle_row_buckets accepts a store-word row; main exits 2 on a missing --link-groups file -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y3.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the four store rows are files without the doubled prefix and the 16 ids that name them moved with them; every catalog entry still loads with no error; the scoped-API row has bucket amgt-scoped-api and table /api/scoped/amgt and settles to that bucket; every dynamodb_ id members.yaml names is an entry; the planted mutants are refused -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-y-3" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y3.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 80 passed = 72 existing + 8 new) for test_group_links.py and the four existing atom_decomposition test files -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~86/NFRA_MCPINDEX.TO-MX-y-3.group-links-and-store-words.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; the old-string census; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~86. Source: the CTO's round-24 analysis (`1.0.0_SA_CTO~Z`, 2026-10-20 ~15:4xZ, msg 36225) rulings (a) and (b) and items 3 and 4, PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (contract R25.3 Y3). **The decomposition's Y3-i paragraph is unimplementable as written** (it puts the key `{group: {bucket, vendor, firm}}` in `members.yaml`): the issuer measured `.tools/naming-gate.py --enforce` on a `firm: <firm token>` line of `members.yaml` and it REFUSES it (hand-kept carrier), while `firm: none` and `firm: multi` pass and a JSON file under `org/` is not graded. So this order moves the key to a groups file under `org/` (read by `--link-groups`) and keeps only a group id in `members.yaml`; the order text wins and the decomposition's Y3 is amended at the drain. The gate also accepts `bucket: amgt-scoped-api` (CONFORMANT as API_GW) and `table: /api/scoped/amgt` (not graded) for the scoped-API row. A sparse worktree cannot run the whole emitter (it needs `portal/src/api` and the census), so AC2 reads the entry files and `members.yaml` in-process and AC1 runs on fixtures; the real dry emit before and after is the issuer's drain act. Base dry-runs 2026-10-20 (at the base commit): `y3.AC1` FAIL (0 of 1 arms: the emitter lacks `load_link_groups`), `y3.AC2` FAIL (7 of 11 arms ok: the control arms and the entries-load arms pass at the base, the rename, scoped-row and unresolved-id arms fail), `y3.AC3` FAIL (test file absent). The issuer's scratch reference (a copy of the emitter plus the four renames and the scoped-row edit, outside the repository, and a 14-test file) passes AC1 (23 of 23 arms), AC2 (11 of 11) and AC3 (86 passed); planted mutants fire. Two lessons from round 24 are in the face: the sparse cone does not hold what the tests read, and the commit gate refuses a strict utf-8 read of a `*catalog*` file.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
