# NFRA_MCPINDEX task order -- `MX-c-28` -- a measured depth claim is a FLOOR with its `measured_at`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.md</decomp_doc>
<owned_cells>MX-c-28</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-c-28</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~51</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule.
comp-iam: DECLARED-NOT-APPLICABLE -- no role, policy or grant change, no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE -- the check c28.AC2 compares the new output with the tracked catalog's tool index with the two new keys removed (a difference control).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-c-28` (round 20, R20-2 of the round-19 analysis)

Work in your own worktree (cut from `box/sitez`; its sparse cone already holds `workflows`, `lib`, `.tools`, `infra/aws/ec2`, `infra/logic` and the project folder; you may add nothing else). Every path is relative to its root. The file you change is `workflows/atom_decomposition/emit_catalog_v02.py`.

**Why.** The catalog's `tool_index` entries carry `history_depth` and `freshness` claims. A `measured` claim is a point-in-time fact: the value was read from the live source at `read_at`, and a source only moves forward, so after a release the value is a FLOOR (the source is at least that deep), not a standing equality. Today the claim is graded for equality with the live source, and every publish ages it (the shipped v3 catalog went from 11 of 11 to 7 of 11 in 2.5 hours). The CTO ruled (round-19 analysis): after release each depth claim is marked a floor with its `measured_at`, and the emitter stays strict. The issuer's checker already grades a post-release catalog `monotone`; this cell makes the catalog itself say so.

**What to build** (in `emit_catalog_v02.py`):

1. In `load_tool_index` (near the line `depth, cerr = compose_basis(depth, row_keys or {})`), for the entry's `history_depth` ONLY: every claim with `claim == "measured"` (the claim itself, or each element of `links` of a `per-link` claim) gains two keys, `depth_kind` equal to the string `floor` and `measured_at` equal to that claim's own `read_at`. Put them after the claim's existing keys. `freshness` claims, `inferred` claims and `absent` claims get neither key. Nothing else about the entry changes.
2. In `validate_claim`: when a claim carries `depth_kind` it must equal `floor` and the claim must be `measured`; when it carries `measured_at` it must match `STAMP_RE` and equal the claim's `read_at`. A claim without either key is valid exactly as today (so the validator still accepts a measured file written before this change).
3. The emitter stays strict: no tolerance is added anywhere, no measured value changes.
4. **Tests**: a NEW file `workflows/atom_decomposition/tests/test_depth_floor.py` with at least 6 tests on small inline fixtures (inject the census and the row keys the way `tests/test_tool_index_and_harvest.py` does, and point `TOOL_INDEX_DIR` at a temp folder holding a tiny `members.yaml`, `pending_members.yaml` and `measured.yaml`): a measured history_depth claim gets both keys; a per-link claim gets them on each measured element; a freshness claim does not; an inferred claim does not; `validate_claim` rejects `depth_kind: ceiling`; it rejects a `measured_at` that differs from `read_at`; it accepts a claim with neither key.

### Steps

0. Control (must pass before you start): `cd workflows/atom_decomposition && PYTHONPATH=. python -m pytest -q -p no:cacheprovider tests/test_tool_index_and_harvest.py tests/test_c_group.py tests/test_serves.py`.
1. Make the change and the tests. Run the control line with `tests/test_depth_floor.py` added (all pass).
2. Run the two criteria in section 4.

## 2. BOUNDS

1. You change only the files in `<paths>`. No entry file, no catalog, no `measured.yaml`, no registry file, no gateway file, no checker. The emitter is NOT run into the repo's catalog (the issuer emits). No deploy. No push.
2. No firm or product name is typed as a whole-string literal in code (the naming gate refuses a new hand-kept token).
3. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project (row Z-W34-S8): your proof instance is one. Run `python .tools/naming-gate.py --diff <your diff> --enforce --staged-paths <file>` on your code commit before you make it; it must exit 0.
4. The checks are `deliverables/2.0.0_SA_COO~MI/round20/checks/c28.AC1.sh` and `c28.AC2.sh` (python `c28_check.py`). Read them for exactly what is graded. Do not edit them.
5. Another worker (`~50`) edits the silver-row generator at the same time (no shared file).
6. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/atom_decomposition/emit_catalog_v02.py
workflows/atom_decomposition/tests/test_depth_floor.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~51/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W51-S<k>`;
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 1)

<proof_of_spec>
  <expected_criteria>AC1,AC2</expected_criteria>
  <criterion id="AC1" cell_refs="MX-c-28" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/checks/c28.AC1.sh; echo "exit=$?"</invocation><expect>pytest rc=0 on test_depth_floor.py, test_tool_index_and_harvest.py, test_c_group.py and test_serves.py; the new file holds at least 6 tests -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-c-28" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round20/checks/c28.AC2.sh; echo "exit=$?"</invocation><expect>DENOMINATOR tool_index entries 127; errors 0; DENOMINATOR measured history_depth claims 39; without depth_kind floor and measured_at == read_at 0; freshness claims carrying them 0; inferred/absent claims carrying them 0; every CHECK ok -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~51/NFRA_MCPINDEX.TO-MX-c-28.measured-depth-claims-are-floors-with-measured-at.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. (The expect fields are prose; the checker matches `expect` as a regex against your recorded output: encode the literal printed tokens, replacing digits with `[0-9]+` where counts may differ, and disclose that in a row. Pin each artifact row to the commit that carried it, not `PENDING-THIS-COMMIT`, when the file was committed before the instance.)
2. Do NOT flip the order's status; the issuer does.
3. Commit through `.tools/safe-commit.sh`, message files written with the Write tool, each ending `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>` and stating push state LOCAL, in two commits: (i) `emit_catalog_v02.py` and the test file; (ii) the proof instance.
4. Report once, with: the change by function (lines added); the AC1 and AC2 DENOMINATOR and CHECK lines verbatim; one measured claim before and after (no more than 10 lines, from your tests); the test count; the two commit shas.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 20, worker ~51, an independent chain. Source: CTO round-19 analysis @9b905362bc (R20-2; the monotone grade endorsed as the contract for every depth claim, strict at emit). The new claim keys change the catalog bytes when the issuer next emits (39 claims x 2 keys); that catalog rides `2.0.0_SA_COO~O`'s next batched gateway release (R20-3), and before it the issuer runs the gateway tests that read the tool index against the candidate. Base dry-run in a SPARSE worktree cut like the worker's: `c28.AC1` FAIL (no test file), `c28.AC2` FAIL (0 of 39 measured claims carry the keys).

<status>issued</status>
<round>20</round>
<workstream>ASSETS</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER RULING (2.0.0_SA_COO~MI, 2026-10-16 ~19:2xZ) -- MX-c-28 COMPLETE.** Worker ~51 added `as_floor` and `_floor_key_errors` to `emit_catalog_v02.py` (41 lines added, one replaced: `validate_claim` is now a wrapper over the unchanged body) and 8 tests (`99951b626b`); its mutant control (`as_floor` as identity) fails c28.AC2 with 0 of 39. Drained by `safe-merge.sh` at `614a633c9a` (9 files, none foreign). This time the flip waited on the consumers: issuer re-run on the merged tree, c28.AC1 PASS (63 passed, 8 new) and c28.AC2 PASS (39 of 39 measured history_depth claims carry `depth_kind: floor` and `measured_at` equal to `read_at`; no freshness, inferred or absent claim does); the atom_decomposition suite 334 passed; ruff clean; and a TRIAL EMIT (all six group maps, `round20/emit_final.sh`, written to a temp folder, nothing landed): 284 rows, `r20.AC1` PASS (every row of the three sections byte-equal to the live blob `b81c48aa3c`, the tool index equal once the two keys are removed, 39 claims marked), `r20.AC2` PASS (the gateway discover, firm-visibility and portal-index tests, 77 passed, with the candidate placed), `c23.AC4`, `c21.AC2` and `r13.AC3` strict PASS, and the enforcing naming gate on the candidate diff exits 0 with 0 REFUSE and 0 RAISE. The candidate (md5 `eb1f5c35...`) is NOT landed: no catalog is emitted onto trunk until MX-c-27 is on trunk (the CTO's BLOCKING), and it rides `2.0.0_SA_COO~O`'s next batched gateway release with MX-c-24. Proof-of-spec VALID. Gate limb that graded this ruling: the flip-needs-a-VALID-instance limb of to-pipeline-gate.

<status>complete</status>
