# NFRA_MCPINDEX task order -- `MX-c-39` -- two depth kinds, `latest` and `series_start`, declared on the member spec and carried by every measured depth claim

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-39</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-39</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~53</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change, no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- c39.AC2 derives each claim's expected kind independently from members.yaml and anchors the six series-start claims.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-39` (round 21, R21-2 of the round-20 analysis)

Work in your own worktree (cut from `box/sitez`; its sparse cone already holds `workflows`, `lib`, `.tools`, `infra/aws/ec2`, `infra/logic` and the project folder; you may add nothing else). Every path is relative to its root.

**Why.** Round 20 (MX-c-28) tagged every measured `history_depth` claim `depth_kind: floor` with `measured_at`. The CVO showed that is wrong for a SERIES-START claim: the claim `2024-11-01` read from `total.series_start` or `as_of_first` is the date a series BEGINS; if a later read finds a LATER start the history got shorter, and a floor reading would pass it. The CTO accepted this (msg 35237). Two kinds: `latest` (the object's latest date; a floor: a later served value means more data) and `series_start` (a ceiling: an equal or EARLIER served start passes, a LATER start FAILS). Today 33 measured claims are `latest` and 6 are `series_start` (the three tools that read the aum and aggregate-AUA rows).

**What to build.**

1. **Declare the kind on the member spec** in `workflows/atom_decomposition/tool_index/members.yaml` (and `pending_members.yaml` if any spec there qualifies): every depth spec dict that names a `row` and a `field` where the field is `total.series_start` or `as_of_first` gains the line `depth_kind: series_start` (right after its `method` line). A spec with no `depth_kind` means `latest`. Change no other line of the file.
2. **The emitter** (`workflows/atom_decomposition/emit_catalog_v02.py`): replace MX-c-28's `as_floor` by a function that, for every `measured` claim of an (a) entry's `history_depth` (the claim itself or each measured element of a `per-link` claim), sets `depth_kind` to the kind the entry's member spec declares for that claim's (`row`, `field`) pair (find the specs by walking the member dict for dicts with both keys; `latest` when none declares it) and `measured_at` equal to the claim's `read_at`. `freshness`, `inferred` and `absent` claims get neither key. Nothing is guessed from a field name in the emitter.
3. **The validator** (`validate_claim` and its helper): `depth_kind`, when present, must be `latest` or `series_start` and the claim must be `measured`; the old value `floor` is REFUSED (name it in the message); `measured_at` as before (a full UTC stamp equal to `read_at`). A measured claim emitted by `load_tool_index` always carries a kind.
4. **Tests**: update the 8 tests of `tests/test_depth_floor.py` to the new values (`latest` where they asserted `floor`; one test must assert that `floor` is now refused), and add a NEW file `tests/test_depth_kinds.py` with at least 8 tests on inline fixtures (a temp `TOOL_INDEX_DIR` with a tiny `members.yaml`, `pending_members.yaml` and `measured.yaml`, as `test_depth_floor.py` does): a spec with `depth_kind: series_start` gives a series_start claim; a spec without it gives latest; a per-link entry tags each element by its own spec; two specs sharing a row but differing in field get their own kinds; freshness, inferred and absent claims get no key; `validate_claim` accepts both kinds, rejects `floor`, rejects `ceiling`, rejects a kind on an inferred claim.

### Steps

0. Control (must pass before you start): `cd workflows/atom_decomposition && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_depth_floor.py tests/test_tool_index_and_harvest.py tests/test_c_group.py tests/test_serves.py`.
1. Make the changes and the tests. Run the control line with `tests/test_depth_kinds.py` added (all pass).
2. Run the two criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No entry file, no catalog, no `measured.yaml`, no `measure.py`, no registry file, no gateway file, no checker. The emitter is NOT run into the repo's catalog (the issuer emits). No deploy. No push.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a new hand-kept token). Run `python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <file>` on your code commit before you make it; it must exit 0.
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round21/checks/c39.AC1.sh` and `c39.AC2.sh` (python `c39_check.py`). Read them for exactly what is graded. Do not edit them.
5. Another worker (`~52`) edits `gen_silver_rows.py` at the same time (no shared file).
6. Name your session log `session_log_MX-c-39.json` (other workers share the deliverables folder tree).
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tool_index/members.yaml
workflows/atom_decomposition/tool_index/pending_members.yaml
workflows/atom_decomposition/tests/test_depth_kinds.py
workflows/atom_decomposition/tests/test_depth_floor.py
infra/aws/ec2/opal-gateway/app/refs/DATA_CATALOG.yaml
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~53/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W53-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-39" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/c39.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_depth_kinds.py, test_depth_floor.py, test_tool_index_and_harvest.py, test_c_group.py and test_serves.py; the new file holds at least 8 tests -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-39" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/c39.AC2.sh; echo "exit=$?"</invocation><expect>tool_index entries 127; errors 0; measured history_depth claims 39; kind differs from its member spec 0; still the old value floor 0; measured_at != read_at 0; series_start claims 6; other claims carrying the keys 0; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-c-39" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round21/checks/p21.AC1.sh; echo "exit=$?"</invocation><expect>tracked catalog md5 9c456f9341dd2d5ab2369f9e1479c3ab; expected 9c456f9341dd2d5ab2369f9e1479c3ab; the tracked catalog is the candidate; r21.AC1 PASS on the tracked catalog; r21.AC2 PASS on the tracked catalog -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~53/NFRA_MCPINDEX.TO-MX-c-39.two-depth-kinds-latest-and-series-start.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where counts may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) the emitter, `members.yaml`, `pending_members.yaml` (if changed) and the two test files; (ii) the proof instance.
4. Report once, with: the change by function; the lines changed in `members.yaml` (which specs); the AC1 and AC2 DENOMINATOR and CHECK lines verbatim; the test count; the two commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 21, worker ~53, an independent chain. Source: CTO round-20 analysis @3f03a45f83 (R21-2, msg 35237) on the CVO slug ADJUDICATION_v16 @b0966935f7. The issuer's own instrument `round12/checks/c12_depth.py` already grades by kind (selftest 16 of 16: a later series start FAILS in every mode; an untagged claim is read by its field). The kind is DECLARED on the member spec, matched by (row, field); no re-measure is needed. Base dry-run in a SPARSE worktree cut like the worker's: `c39.AC1` FAIL (no test file), `c39.AC2` FAIL (0 of 39 claims carry a kind, all 39 still say floor; the anchor of 6 series-start claims reads 0).

<status>issued</status>
<round>21</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~20:5xZ) -- MX-c-39 COMPLETE.** Worker ~53 replaced `as_floor` with `as_depth_kind` (helpers `_depth_specs`, `_mark_depth_kind`; `_kind_key_errors` refuses `floor` by name) in `emit_catalog_v02.py`, added `depth_kind: series_start` on four specs of `members.yaml` (gateway_query_catalog mp.01 and mp.03, mdpf_get_aggregate_aua mp.03, mdpf_get_aum_metrics mp.01; `pending_members.yaml` unchanged), moved the 8 tests of `test_depth_floor.py` to the new values (one asserts `floor` is refused) and wrote 17 tests in `test_depth_kinds.py` (`1071edbdbc`, `ee6cb1847c`). Drained by `safe-merge.sh` at `8906f5fb80` (7 files, 0 foreign). Flip waited on the consumers: issuer re-run c39.AC1 PASS (80 passed, 17 new) and c39.AC2 PASS (39 of 39 measured history_depth claims carry the kind their member spec declares, 6 `series_start`, 0 still `floor`, 0 stray keys); the atom_decomposition suite 363 passed; ruff clean; the proof instance VALID; and a TRIAL EMIT (`round21/emit_final.sh`, temp folder, nothing landed): `r21.AC1` PASS (rows byte-equal to the live blob `b81c48aa3c`, tool index equal once the two keys are removed, each claim carries the kind its field implies), `r21.AC2` PASS, `c23.AC4`, `c21.AC2` and `r13.AC3` PASS; candidate md5 `b014f6379707e9071cb73b3a94516182`. Row Z-W53-S3 is dispositioned by `NFRA_MCPINDEX-Z-S133`. The candidate is not landed: the emit waits on MX-c-29 (CTO) and rides `2.0.0_SA_COO~O`'s next batched release with MX-c-24. Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate.

**AMENDMENT A1 (2.0.0_SA_COO~MI, 2026-10-16 ~21:1xZ; no gate limb graded it: a path grant and one added criterion on an existing order; the CTO's round-21 analysis @fa79b33427 opened no new cell and named this emit for the next batched release).** The kind-keyed catalog is the product of this cell: the issuer re-measured (`0bc424dd91`, read 21:01Z) and emitted the release candidate at the workspace root (`round21/emit_final.sh`: r21.AC1, r21.AC2, c23.AC4, c21.AC2 and r13.AC3 PASS). Candidate file `C:/tmp/r21_final/DATA_CATALOG.final.yaml`, md5 `9c456f9341dd2d5ab2369f9e1479c3ab`. The re-seated worker ~53 only PLACES it (the cell's emitter cannot run in a sparse worktree: it needs `portal/src/api`): `python org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round18/place_catalog.py <worktree root> C:/tmp/r21_final/DATA_CATALOG.final.yaml 9c456f9341dd2d5ab2369f9e1479c3ab` must print `copied=1 equal=1`; then run the enforcing naming gate on the diff (`python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <file>`, exit 0, 0 REFUSE), run criterion AC3 (`p21.AC1.sh`: md5 equal, r21.AC1 and r21.AC2 on the tracked catalog, all PASS; it fails at the base as expected), commit the catalog ALONE through `.tools/safe-commit.sh` (message file by the Write tool, ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`, push state LOCAL) and refresh the instance with the AC3 row (pinned to that commit; digits as `[0-9]+` where counts may differ) in a second commit. The catalog file is the ONLY file you place; change no other. Widening, stated: none. The diff is the 39 measured history_depth claims gaining `depth_kind` and `measured_at` plus the `read_at` stamps of the re-read; rows, tools, `serves`, visibility and every value are byte-equal to the live blob `b81c48aa3c` (r21.AC1 proves it).

<status>in_progress</status>
