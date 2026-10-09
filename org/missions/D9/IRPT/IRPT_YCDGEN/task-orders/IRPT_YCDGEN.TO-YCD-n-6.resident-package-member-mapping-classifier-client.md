# IRPT_YCDGEN task order -- `YCD-n-6` -- ROUND 6 (THREAD): THE RESIDENT PACKAGE CARRIES THE CLASSIFICATION CLIENT: A MEMBER MAPPING IN THE BUILDER AND THE GATE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6G.md</decomp_doc>
<owned_cells>YCD-n-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-n-6.resident-package-member-mapping-classifier-client</to_id>
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

### `YCD-n-6` -- the resident package carries the classification client: a member mapping in the builder and the gate (hops release tooling; FWD-1)
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`: R15 (1) and (2).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py`: R15 (3).
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py` (new): the tests the criteria name, including R15 (4) as a packaged import smoke.
- A build with none of the new flags stays byte-for-byte the build of today.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R15 One repository file at a packaged path.** (1) `--member PACKAGED_PATH=REPO_PATH`, repeatable: the builder packages the tracked file `REPO_PATH` at `--pin` as the member `PACKAGED_PATH`. It refuses (nonzero, a named message) a `PACKAGED_PATH` that is absolute, contains `..`, or is already a member of the package, and a `REPO_PATH` that does not exist at `--pin`. Under `--base-pin` the member is read from `--pin` and needs no entry in the `--files-from` list. (2) The bindings provenance records `members_added`: a list of `{"packaged": ..., "repo_path": ..., "sha256": ...}`; the key is absent when no `--member` is given (a build with no new flag is byte-for-byte the build of today), and the builder's printed report lists them. (3) `resident_package_gate.py` reads `members_added` from the package's own `reports/resident_bindings.json`; G2 expects each added member equal to `git show <pin>:<repo_path>`, and a member that differs fails G2 with the count printed; the census counts each as added. (4) A package built with `--member ycharts/research/etf_classifications_dynamodb.py=infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` lets `layout_overview._default_classifier()` return an `ETFClassifier` in a clean interpreter whose only import-path entries are the host's (the package root and the directories `ycharts/generate/resident_main.py` and `reports/resident_installed.py` put on `sys.path`, with `ycharts/research` appended as `load_opal_producer()` appends it), with no `v2_portal` directory anywhere on it, and with `AWS_DEFAULT_REGION` set so no network call is made.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: both tool files in full (they were last changed by cell m-6: `--research`, `--opal-map`, `--base-pin` with `--files-from`, `--state-json`; keep every one of them working) and m-6's test file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py` (read only: how it builds from real commits offline with `--state-json`); `infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py` `_default_classifier` (the import and the `HERE.parents[2] / v2_portal / _shared` fallback) and `infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (imports only boto3 and botocore); the worker row IRPT_YCDGEN-S10 in `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (the last two rows).
- Tests use real commits of this repository as pins, as m-6's did: base `3f29017cfc`, overlay/pin `d2b625e697` (both on CLOUD); the classifier file exists at both. No AWS call, no network, no write outside the test's temp dir; `AWS_DEFAULT_REGION=us-east-1` is set in the smoke's environment.
- Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from the worktree root; a build takes tens of seconds and the whole file may take a couple of minutes. ASCII only in code.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/live_walk/resident_package_gate.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- --member packages the repository file at the packaged path and records it in the bindings provenance (tests -k member_flag_packages_and_records, >= 1 passed)
- **AC2** -- --member refuses an absolute or dotted packaged path, a duplicate member and a missing repository file (tests -k member_flag_refusals, >= 1 passed)
- **AC3** -- the gate reads the added members from the bindings, accepts the package and refuses one whose added member differs (tests -k gate_checks_added_members, >= 1 passed)
- **AC4** -- a built package lets _default_classifier return an ETFClassifier in a clean interpreter with no v2_portal directory (tests -k packaged_classifier_import_smoke, >= 1 passed)
- **AC5** -- a build with none of the new flags is unchanged and carries no members_added key (tests -k default_build_has_no_members_added, >= 1 passed)
- **AC6** -- m-6's test file still passes (tests, all, no failure)
- **AC7** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider -k member_flag_packages_and_records</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider -k member_flag_refusals</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider -k gate_checks_added_members</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC4" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider -k packaged_classifier_import_smoke</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC5" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider -k default_build_has_no_members_added</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC6" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_listed.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
  <criterion id="AC7" cell_refs="YCD-n-6"><invocation>python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/tests/test_build_resident_package_member.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-n-6.resident-package-member-mapping-classifier-client.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-n-6.resident-package-member-mapping-classifier-client`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, first order of addendum G (decomposition IRPT_YCDGEN_DECOMP_R6G.md), cut to disarm row IRPT_YCDGEN-S10 (the resident package lacks the classification client; a listed principal's request would end ATTENTION). Writer read recorded in the decomposition: 0 non-terminal orders name either tool file. pyarrow (row S11) is not in this cell. Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~03:4xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @c1dd9ada9c, merged cb5d6be8a4; n-6.AC1-AC7 PASS at the worker (AC7: 5 passed, AC6: m-6's 7 passed) and AC1, AC2, AC4 re-run PASS on the merged tree; instance VALID. Builder: --member PACKAGED=REPO repeatable, refuses an absolute or dotted path, a duplicate, a missing repo file and an argument with no '='; records provenance.members_added only when used; all m-6 flags still work. Gate: G2 checks each added member against git show <pin>:<repo_path> and its recorded sha256 and prints a 'G2 added members: N of M' line; tampered-member and member-removed negative arms included; the smoke ran in a clean interpreter (-I) with no v2_portal on sys.path. Worker's one cosmetic note accepted (a members_added entry missing from the package fails the gate; the main G2 'differ' line does not count it, the added-members line does). Row IRPT_YCDGEN-S10 stays ARMED until B2 is installed and its real-stack proof reads closed.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6G_CLASSIFIER_MEMBER</workstream>
<slot>~1</slot>
<fabric>laptop</fabric>
