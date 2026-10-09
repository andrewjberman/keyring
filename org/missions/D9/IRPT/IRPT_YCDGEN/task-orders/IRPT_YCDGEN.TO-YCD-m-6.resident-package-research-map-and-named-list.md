# IRPT_YCDGEN task order -- `YCD-m-6` -- ROUND 6 (THREAD): THE RESIDENT PACKAGE CARRIES THE PRODUCER, THE MAP AND A NAMED FILE LIST

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6E.md</decomp_doc>
<owned_cells>YCD-m-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-m-6.resident-package-research-map-and-named-list</to_id>
<issued_to>0.9.0_WK_IRPT_YCDGEN~1</issued_to>
<issued_by>2.0.0_SA_COO~Y</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; no schedule, trigger or EventBridge rule is added or read
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; the resident host's role is proved by the issuer's close run
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches this surface
</preflight>

**Project:** IRPT_YCDGEN (D9/IRPT, fabric laptop) -- the Analysis report made in house, Opal-branded, with no YCharts call. **Round 6** builds one thread: Andrew submits a Cottonwood portfolio for an Overview and opens an Opal-made report. The first version carries no pricing (returns, risk, benchmark and risk-free print not available, reason `NOT_IN_THIS_VERSION`). No worker calls a vendor, writes the store, deploys or grants: the issuer makes every live act at close. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the round-6 decomposition)

### `YCD-m-6` -- the resident package carries the producer, the map and a named file list (hops release tooling; FWD-1)
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`: R13 (1) to (4).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py`: R13 (5).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py` (new): the tests the criteria name, including R13 (6) as a packaged import smoke.
- A build with none of the new flags stays byte-for-byte the build of today.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R13 The resident package carries the producer, the map and a named file list; the gate understands the list.** (1) `--research`: the builder also packages every tracked non-test file under `infra/aws/lambda/investor-reporting/ycharts/research/` at the pin (`.py`, `.json`, `.sh`, `.md` and `.cjs`; no `tests/`, `fixtures/`, `__pycache__`) as `ycharts/research/<name>`. (2) `--opal-map REPO_PATH`: that tracked file at the pin is packaged as `ycharts/research/overview_map.json` and the bindings gain `"opal_map": {"path": "../ycharts/research/overview_map.json", "sha256": <digest>}` (relative to `reports/`, like `census`); without the flag the bindings carry no `opal_map` key. (3) Named file list: `--base-pin P --files-from LIST` builds the package from P's tree by the same member rule as today, EXCEPT the files named in LIST (one repo path per line; each must exist at `--pin`), which come from `--pin`; the report prints the list and its count, and the bindings provenance records `base_pin`, the list's sha256 and its count; no unlisted member differs from P. (4) `--state-json FILE` reads the core state document from a file in place of the S3 read, so tests run offline; the default is unchanged. (5) `resident_package_gate.py` takes `--base-pin P --files-from LIST`; G2 then compares each listed member to `git show <pin>:<path>` and every other member to `git show P:<path>`, and a member that differs from its expected blob fails G2 with the count printed. (6) A package built with (1) and (2) imports `opal_producer`, `layout_overview`, `runner`, `keeper` and `held_data` through `resident_worker.load_opal_producer()` in a clean interpreter with the host's import path (the package root plus the directories `ycharts/generate/resident_main.py` and `reports/resident_installed.py` put on `sys.path`), and `resident_installed._opal_map_loader` returns the map as a dict. A build with none of the new flags is byte-for-byte the build of today.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: both tool files in full; `infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` (`load_opal_producer`, 136-142) and `infra/aws/lambda/investor-reporting/reports/resident_installed.py` (the `sys.path` setup near 39-40, `OPAL_MAP_BINDING`, `_opal_map_loader` near 246); the worker rows IRPT_YCDGEN-W1-S13 and IRPT_BCKEND-S339 (the second in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`).
- The builder reads `git show <pin>:<path>`, never the worktree; the tests use real commits of this repository as pins: the running package's pin `3f29017cfc` (the base) and the merge `d2b625e697` (the overlay), and the 14-line list of round-6 files in `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/2.0.0_SA_COO~Y/round6/act/PACKAGE_CENSUS_3d705e700f-st22.json` (its `added` and `changed` names, mapped to repo paths) is the reference case: building base `3f29017cfc` plus that list from `d2b625e697` must equal the census recorded there (added 5, changed 10 including the regenerated bindings, removed 0). Read that file for the expected member names.
- Offline: the builder's `core_outputs()` reads the core Terraform state from S3. Add `--state-json` (R13 (4)); a test fixture state needs only `serial` and `outputs.queues.generation.url`, `outputs.tables.jobs`, `outputs.tables.requests`.
- The Overview element map to package in the smoke is `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json`.
- Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from the worktree root; no AWS call, no network, no write outside the test's temp dir. ASCII only in code.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the research directory's non-test files are packaged and no test file is (tests -k research_dir_packaged, >= 1 passed)
- **AC2** -- the opal_map binding is pinned to the packaged map and the installer's loader reads it (tests -k opal_map_binding_pinned, >= 1 passed)
- **AC3** -- a named-list package differs from the base pin's package by exactly the listed files (tests -k named_list_package_differs_only_by_the_list, >= 1 passed)
- **AC4** -- the gate accepts the listed package and refuses one with an extra differing member (tests -k gate_accepts_listed_package_and_refuses_an_extra_member, >= 1 passed)
- **AC5** -- a built package imports the producer modules and loads the map in a clean interpreter (tests -k packaged_import_smoke, >= 1 passed)
- **AC6** -- a build with none of the new flags is unchanged (tests -k default_build_unchanged, >= 1 passed)
- **AC7** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k research_dir_packaged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k opal_map_binding_pinned</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k named_list_package_differs_only_by_the_list</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k gate_accepts_listed_package_and_refuses_an_extra_member</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k packaged_import_smoke</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider -k default_build_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC7" cell_refs="YCD-m-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-m-6.resident-package-research-map-and-named-list.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-m-6.resident-package-research-map-and-named-list`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, first order of addendum E (decomposition IRPT_YCDGEN_DECOMP_R6E.md), cut on the CTO's ruling msg 105454 (a round-6 addendum cell like g-6; named file list; the packet prints the list and count) to disarm worker row W1-S13 and the builder half of IRPT_BCKEND-S339. Writer read recorded in the decomposition: 0 non-terminal orders name either tool file. The renderer's availability on the host is NOT proved here; it is branch B's first real exercise. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~01:5xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @2b5f4f00e1, merged 3ef2d8c8f8; m-6.AC1-AC7 PASS on the merged tree (AC7: 7 passed in 113 s), instance VALID. The reference case (base 3f29017cfc plus the 14-file list from d2b625e697) gives added 5, removed 0, changed 10, and the pinned-member digests equal PACKAGE_CENSUS_3d705e700f-st22.json. Builder: --research, --opal-map, --base-pin with --files-from, --state-json; gate: --base-pin with --files-from; a build with none of the new flags is unchanged (AC6). Row W1-S13 DISARMED (the opal_map binding has an installed home); IRPT_BCKEND-S339 builder half DISARMED (a named list builds exactly the named change set; a build that omits --base-pin still ships the whole tree, so the disarm holds only for a builder who uses the list: carried in the branch B packet). Row W1-S15 INERT, accepted (the builder records provenance.opal_map_source and the gate reads it from the package's own bindings; under --base-pin the research files come from P's tree like every member, so a research file P lacks must be in LIST). NOT PROVED by this cell: the renderer on the host (render_pdf.cjs and a headless browser); that is branch B's first real exercise.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6E_PACKAGING</workstream>
<slot>~1</slot>
<fabric>laptop</fabric>
