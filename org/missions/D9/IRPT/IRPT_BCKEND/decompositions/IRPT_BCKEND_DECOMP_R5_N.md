# IRPT_BCKEND decomposition -- ROUND 5, WORKSTREAM ~PN (2026-10-17 ~12:3xZ, 2.0.0_SA_COO~N2, dell2)

**Cut on:** `0.7.0_AE_CloudOps~IB2` msg 10539 (the first scheduled chain after the corrected apply of TO-IB-pn-2): the Scope step exited 1
after 1.6 s, tolerated by the chain; cause in the chain log, `botocore.exceptions.NoRegionError` at `boto3.client("secretsmanager")` in
`session_token()` (feed script line 327): the runner sets no default AWS region. No Orion request was made, 0 feed keys were written,
Branch B restored the dispatch object and the script (sha256 equal to the saved copies). This is the SECOND runner-only failure of the
same step; the first (round 4, `IB-pn-1`) was the import layout. The in-runner import smoke of ADDENDUM 3 could not catch this one: it
runs with sockets blocked and builds no client, and a client's region resolves at construction.

**Measured at the cut (read, not assumed):**
- The feed script holds exactly two boto3 constructions: line 327 `boto3.client("secretsmanager")` (no region) and line 579
  `boto3.client("s3", region_name="us-east-1")`; `jwt_freshness.py` names `region_name="us-east-1"` on every client it builds.
- The check `checks/r3/pn_region_cells.py` reproduces the production error on the base tree: AC1 `NoRegionError` (real client
  construction in the runner's flat layout, every AWS_* variable removed, no config file, the API call replaced so no network),
  AC2 `line 327 boto3.client` has no `region_name`, AC3 new test file absent. With the one-token fix in a temp copy AC1 and AC2 PASS.
- Not measured: whether another runner-only difference follows (the step has now failed at import, then at the first client, and has
  never reached Orion). The cell therefore also asks for one end-to-end run of the feed's `run` in the flat layout under the scrubbed
  environment with the existing fakes (a request and a write reached), so that a third runner-only failure is found in the repository
  and not in the next chain.

**Rectangle:** one cell.

| cell | item | outcome | risk | depends on |
|---|---|---|---|---|
| `IB-pn-3` | **Every boto3 client of the Scope feed names its region.** `session_token()` builds `boto3.client("secretsmanager", region_name="us-east-1")` (the value the feed's own S3 client and `jwt_freshness.py` already use). New tests `data/inf/manual_api/test_scope_feed_region.py` (at least 3): the AST rule (every boto3 construction names `region_name`), the NoRegionError reproduction control, and one end-to-end `run` in the flat layout under the scrubbed environment using the existing fakes. | IB2 msg 10539; row S221 line; FWD-3 | LOCAL | none |

**Not in this cell:** the next re-apply of the corrected script (a WORLD order to IB2, `IB-pn-4`, under a new addendum bound to the new
bytes: the CTO's rule is that a signed half covers only the bytes it graded); the history backfill (ADDENDUM 2); row `D2-W404-S9`'s own fix.

**Chains:** A = IB-pn-3. M = 1. fanout: 1 of 1 chains, cap 4, slot ~481 (block ~480..~499). One real run at close: the three
criteria of `checks/r3/pn_region_cells.py` on the merged tree.
