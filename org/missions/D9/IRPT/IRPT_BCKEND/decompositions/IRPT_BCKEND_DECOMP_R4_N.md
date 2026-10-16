# IRPT_BCKEND decomposition -- ROUND 4, WORKSTREAM ~PN (2026-10-16 ~13:4xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** IB2's first-run read of IB-pr-596 (`0.7.0_AE_CloudOps~IB2` msg 9366) and row `IRPT_BCKEND-D2-S221`: the Scope account feed
died at import on the runner (`pull_inflection_scope_account_returns.py` line 34, `_HERE.parents[2]`, IndexError: the runner runs it
from `/tmp/orion_gold_scripts/`, which has two ancestors). The chain tolerated the failure (row `D2-W404-S9`); Branch B restored the
saved dispatch copy; no feed key was written. Workstream ~PN stays with this seat under the CTO ruling
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md` Move 1; the order
IB-pr-596 itself stays issued by `2.0.0_SA_COO~P2`, which grades it.

**Measured at the cut (read, not assumed):**
- The runner sync (`data/inf/scripts/gold/orion-gold-dispatch.sh`, `sync_scripts()`, lines 533-546) flattens `code/gold/`,
  `code/manual_api/`, `code/silver/`, `code/bronze/` by basename into `/tmp/orion_gold_scripts/`.
- Two statements in the feed script assume the repository layout: line 34 (`_REPO_LIB = _HERE.parents[2] / "lib"`, raises on the
  runner) and line 71 (`BUILDER_PATH = _HERE.parent / "scripts" / "gold" / "INF_B_00.canonical_holdings.py"`, a path that does not
  exist on the runner; `INF_B_00.canonical_holdings.py` sits beside the script there). Lines 384-385 and 395-396 insert `_REPO_LIB`
  into `sys.path`.
- The base check run (`checks/r1/pn1_cells.py`) reproduces both: AC1 `IndexError: 2`, AC2 `FileNotFoundError` on the sibling
  `scripts/gold/` path. With a two-line fix applied in a temp copy, AC1 and AC2 both PASS.
- Not measured: the other S3 code objects' contents on the runner (this seat reads no S3 here); the check flattens the repository
  folders the sync names, which is the same file set only if the repository matches the deployed code prefixes.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-1` | **The feed script runs in the runner layout.** `_REPO_LIB` is `None` when the script sits fewer than three directories below the root, and the three places that use it skip a `None`; `source_prefixes` loads `INF_B_00.canonical_holdings.py` from the script's own directory first and from the repository path second. New tests `data/inf/manual_api/test_scope_feed_runner_layout.py` (at least 4) build the flat layout in a temp directory. The exemption, the daily factor, the day-complete rule and every request body stay as they are. | row S221 / IB-pr-596 first-run FAIL; FWD-3 | LOCAL (repository script and tests; nothing deployed or run against a served prefix) | none |

**Not in this cell (named so no one reads it as covered):** the re-apply of the corrected script to the runner and the dispatch object
(a WORLD order to `0.7.0_AE_CloudOps~IB2`, cut after this cell merges and only under a pair that covers the corrected script's bytes);
the grade of IB-pr-596 (`~P2`); the history backfill (ADDENDUM 2); row `D2-W404-S9`'s own fix (the dispatch branch that returns
success on a failed pull), which lives in the dispatch object and is a separate cell under a pair.

**Chains:** A = IB-pn-1. M = 1. fanout: 1 of 1 chains, cap 4 (CTO msg 8764: dell2 at 75% CPU), slot ~480 (block ~480..~499, this
seat's; `~P2` is at ~446). One real run at close: the check script's three criteria in the worktree and the flattened-layout import
of the merged script, kept under `deliverables/2.0.0_SA_COO~N2/`.
