# IRPT_BCKEND decomposition -- ROUND 6, WORKSTREAM ~PN (2026-10-19 ~13:3xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** the CTO ruling `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/1.0.0_SA_CTO~DELL2/RULING_IB_PN5_BRONZE_ENVELOPE_FIX_WRITER_FIRST_20261019.md`
(@2f780e14a6, option B, on this seat's note @6aaf4caa55), and on TO-IB-pn-4 complete (@c9cef038ef): the corrected Scope feed ran clean on the runner at
the 2026-10-18 11:33Z chain, so the history backfill (ADDENDUM 2) is the next act, and it is held until the writer is fixed.

**Measured at the cut (read from the script at HEAD, blob `e2ed945d2e920673231e0848a5e51784aefc4db8`):**
- The feed script holds three nested blocks, SCOPE-FEED-A (line 17), -B (592) and -C (787), each redefining `run`; the last, in block C
  (lines 798-889), is the live one. In each, a day's bronze envelope carries `"responses": [... c["response"] ...]` for every household, the
  full window, written into every complete day's object (live site: lines 871-883; earlier sites: 555 and 771).
- `lib/opal_naming.address(source, scope, tier, table, partition, object)` validates source, scope and tier but not the table or the
  partition, so a run-level address `address("orion", "inflection", "bronze", "scope_account_returns", "run=<day>", "<object>")` is built, not typed;
  the script holds no `s3://` and no `orion/inflection` literal today (count 0 and 0).
- No existing test asserts the envelope's `responses` member or its schema string (read: the five test files in `data/inf/manual_api/`);
  the 49 tests pass in 9 s on this tree.
- `silver` bytes for the fixtures are deterministic across runs (two runs, equal sha256): the golden values in the check are the
  pre-change writer's output.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-5` | **The raw Orion replies are written ONCE per run.** A new `run_object_address(pull_date, window_start, digest)` (builder output; sidecar fallback on the runner) and a run-level bronze object `orion-scope-raw-replies-v1` holding every household's reply UNCHANGED; each day's bronze envelope drops `responses`, gains `raw_object {"key","sha256"}` and schema `orion-scope-account-returns-bronze-v2`; silver byte-equal to today's. New tests `data/inf/manual_api/test_scope_feed_run_object.py` (at least 3). | CTO ruling @2f780e14a6; note @6aaf4caa55; ADDENDUM 2 condition 3 | LOCAL | none |

**Not in this cell:** the WORLD apply of the new script and the backfill run (a new ADDENDUM 5 pair, then an apply order to `0.7.0_AE_CloudOps~IB2`,
then the backfill order: the CTO's rule is that a signed half covers only the bytes it graded); IB2's two read-only reads for ADDENDUM 5 (a separate
~PO order, `IB-pn-6`); row `D2-W404-S9`'s own fix; the B-IN adapter.

**Chains:** A = IB-pn-5. M = 1. fanout: 1 of 1 chains, cap 4, slot ~490 (block ~490..~499). One real run at close: the three criteria of
`checks/r6/pn5_cells.py` on the merged tree, plus the drain checks once (`py_compile`, `ruff --target-version py39` on the two files).
