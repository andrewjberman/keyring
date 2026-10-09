# IRPT_YCDGEN task order -- `YCD-o-6` -- ROUND 6 (THREAD): THE CHARACTERISTICS READER RUNS SINGLE-THREADED SO THE HOST PROCESS EXITS CLEANLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6H.md</decomp_doc>
<owned_cells>YCD-o-6</owned_cells>
</decomp_ref>
<to_id>IRPT_YCDGEN.TO-YCD-o-6.characteristics-reader-single-threaded</to_id>
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

### `YCD-o-6` -- the characteristics reader runs single-threaded so the host process exits cleanly (hops 4 Classify, 6 Compute (held data); FWD-1)
- `ycharts/research/layout_overview.py`: R16, the one call at `_read_characteristics` (around line 842).
- `ycharts/research/tests/test_layout_overview.py`: the tests the criteria name; keep every existing test passing.

## 2. THE CONTRACTS YOU BUILD AGAINST (inlined from the decomposition and IRPT_BCKEND PRD v0.28)

**R16 The characteristics reader runs single-threaded.** `layout_overview._read_characteristics` reads the characteristics parquet with `use_threads=False`: `pq.read_table(io.BytesIO(body), columns=[...], use_threads=False)`. Every row it returns, for the same bytes, is unchanged. No other line of the module changes. Why (measured on the resident host, Amazon Linux 2023, python3.12, pyarrow 18.1.0): a `BytesIO` read with the default thread pool aborts the interpreter at exit (exit 134, 'terminate called without an active exception'), the same read with `use_threads=False` and a read from a path both exit 0.

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD at the issuance commit)

- Read first: `layout_overview.py` `_read_characteristics` (816-844) and how the existing tests drive it (they inject `s3`); the decomposition `org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6H.md` for the measurement.
- Code lives under `infra/aws/lambda/investor-reporting/ycharts/research/`. pyarrow 18.1.0 is installed in the test environment (the same version the host will carry); a test may build a small real parquet in memory with it.
- The assertion that the thread pool is off is on the call, not on the process exit (the abort is host-specific): wrap `pq.read_table` in the test to record its keyword arguments and assert `use_threads is False`, and assert the returned rows equal the rows of a small parquet the test builds.
- ASCII only in code and comments.
- Module home and test layout: tests sit beside the code, no `conftest.py`, paths inserted at the top of each test file (as `ycharts/session/tests/test_resident_session.py:9`). Python tests run with `python -m pytest <file> -q -p no:cacheprovider` from your worktree root. Encoding: ASCII only in code and logs; no client figure and no secret in any committed file (C-FIRM, C-SECRET).

## 4. SURFACES AND BOUNDS

You READ (never edit): everything outside your `<paths>`, including `lib/`, `infra/logic/`, `docs/`, `org/missions/D9/IRPT/IRPT_YCDGEN/` (the PRD, the decompositions). NEVER: a vendor call (YCharts, Yahoo, Bloomberg or any other), an S3 or DynamoDB write, a live AWS call of any kind, a deploy, a Terraform command, a cookie, token or session value in any file, a figure value from a client file in any committed file, and none of another cell's files. A check you cannot satisfy inside your `<paths>` is a surprise row appended to `org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` (one `## <ROW-ID> -- <title>` section with a fenced json row; ids `IRPT_YCDGEN-W1-S<k>`, next unused k; `surfaced_at` the real UTC time), never an edit outside them.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/layout_overview.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
org/missions/D9/IRPT/IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the characteristics read passes use_threads=False to pyarrow (tests -k characteristics_read_is_single_threaded, >= 1 passed)
- **AC2** -- the rows returned for a small real parquet are unchanged (tests -k characteristics_rows_unchanged, >= 1 passed)
- **AC3** -- the whole test file passes (tests, all, no failure)

<proof_of_spec>
  <criterion id="AC1" cell_refs="YCD-o-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k characteristics_read_is_single_threaded</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC2" cell_refs="YCD-o-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider -k characteristics_rows_unchanged</invocation><expect>^[1-9][0-9]* passed</expect></criterion>
  <criterion id="AC3" cell_refs="YCD-o-6"><invocation>python -m pytest infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py -q -p no:cacheprovider</invocation><expect>^[0-9]+ passed</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/0.9.0_WK_IRPT_YCDGEN~1/IRPT_YCDGEN.TO-YCD-o-6.characteristics-reader-single-threaded.proof_of_spec.json` with `to_id` `IRPT_YCDGEN.TO-YCD-o-6.characteristics-reader-single-threaded`. Report once: each mechanical criterion's verdict line with the output above it; files written; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~Y):** round 6 cut from PRD v0.5 @e6a801f7f0 section 2 (the thread) and IRPT_BCKEND PRD v0.28 @3a8950aa20 items 29-31; CTO ruling msg 105387 (all cells in one issuance); decomposition round 6 revision 1.0 (`IRPT_YCDGEN_DECOMP_R6.md`). Chain `~1`, first order of addendum H (decomposition IRPT_YCDGEN_DECOMP_R6H.md), the one-argument fix for the host abort found while proving the pinned pyarrow for branch B2 (CTO ruling msg 105485 point 3). Risk WORLD: the gate's floor for infra paths and portal product files; nothing live moves inside the cell.

**DRAIN (2.0.0_SA_COO~Y, 2026-10-06 ~03:2xZ):** worker 0.9.0_WK_IRPT_YCDGEN~1 @98f0a7bfb2, merged dfce2635d7; o-6.AC1-AC3 PASS on the merged tree (AC3: 43 passed), instance VALID. The diff of layout_overview.py is exactly the one call: `use_threads=False` added to `pq.read_table(io.BytesIO(body), ...)`; two tests added (one records the keyword arguments, one compares rows for a small real parquet). The abort at exit is host-specific, so the host re-run of the pinned pyarrow with this code is B2's real-stack proof; no row filed.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<workstream>R6H_PYARROW_THREADS</workstream>
<slot>~1</slot>
<fabric>laptop</fabric>
