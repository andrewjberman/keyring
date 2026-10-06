# ETFS_RIVALS task order -- `RIV-eb-1` -- ROUND 12 (ENRICHMENT): THE ENRICHMENT BOUNDS ITS BLOOMBERG SESSION ATTEMPTS AND EXITS "UNREACHABLE" SO THE VEHICLE REACHES ITS LATER STAGES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-eb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~2</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check file
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, and a terminal-machine Bloomberg leg the vehicle under `integrations/bloomberg/` runs from the CLOUD working tree at 07:00 ET). **Round 12, cells added when the site-Z Bloomberg hold lifted** (Andrew 2026-10-06 ~17:44Z). Nothing in round 12 deploys, merges, flips a gate or calls Bloomberg/OpenAI from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-eb-1` -- the enrichment bounds its Bloomberg session attempts and exits "unreachable" (ADDENDUM 2 @b555e81836)
- Measured 2026-10-06: with the DAPI precondition already FAILED, `rivalfunds.enrichment_bloomberg` kept issuing one blp_client
  request per batch (each opens its own short-lived session; `no RESPONSE ... within 90s` per batch) until Task Scheduler's
  30-minute ExecutionTimeLimit killed the vehicle at 11:30:01Z (0x41306); the names stage and the D12 leg never ran. Offline at
  base: 300 securities, Bloomberg down -> 18 calls (6 dividend + 6 historical + 6 reference batches), exit 3.
- Interface: an exception whose class name is `BloombergError` (blp_client's session/connect-level error: session start, open
  service, no-RESPONSE timeout) is UNREACHABLE; `BlpResponseError` and per-security errors are not. `SESSION_ATTEMPTS` (module
  int, 2 or 3): after that many CONSECUTIVE unreachable failures in one run the run makes no further Bloomberg call (dividends,
  market, names), lands nothing, and returns status FAILED with `detail.unreachable` true and `detail.session_attempts`;
  `exit_code` maps it to 1 (the existing contract). eg-1's guard unchanged. `integrations/bloomberg/` is NOT touched (Andrew's
  no-modify order).
- **Organic trigger:** the vehicle's 07:00 ET enrichment step on a day Bloomberg is unreachable.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 6c489cc6de)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/eb-1.AC1.py` (and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/_common.py`) before you build.
- Every Bloomberg call in the module goes through `_blp_reference_data` / `_blp_historical_data` (enrichment_bloomberg.py ~274-288), which lazily import `integrations.bloomberg.mcp.blp_client` (it imports `blpapi` at load). blp_client raises `BloombergError` for a session that will not start, a service that will not open, and `no RESPONSE ... within <timeout>s`; `BlpResponseError` for a request-level refusal. Detect by CLASS NAME so the module never has to import blp_client to classify.
- Callers today: `_daily_dividends` (~710), `_market_pull` (~516, historical then reference batches), `fetch_names` (~310, the names stage via `security_names`). Each catches per batch and continues -- that is the loop that ate the window. One run-scoped counter must span them all (a run = one `handler_entry` call).
- `exit_code` (~746) already maps `detail.unreachable` to 1; `main` prints the result JSON and returns `exit_code`.
- Keep eg-1 (`tests/test_r10eg1_*`) and every existing enrichment test.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules, the round-12 and earlier rounds' check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests; blpapi is never imported off the terminal), any environment gate flip outside a test, any file under `integrations/`. New tests go beside the code as `tests/test_r12eb1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: it must read 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r12eb1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- Bloomberg unreachable (session start or no-RESPONSE): exit 1 within SESSION_ATTEMPTS calls, detail.unreachable true; control: a reachable session still lands G4 and the daily run exits 0 (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/eb-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-eb-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/eb-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-eb-1.enrichment-bounds-bloomberg-session-attempts.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-eb-1.enrichment-bounds-bloomberg-session-attempts`. Report once: each mechanical criterion's verdict line with the output above it; files written; every existing test assertion changed and why; the package suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** decomposition round 12 v1.1 (issuer amendment when the Bloomberg hold lifted, MSTR~Z msg 30169 @8555ce7e12). Chain `~2`, slot `~2`, position 1 of 2 (eb-1 then pk-1: both write enrichment_bloomberg.py). Check dry-run at base CLOUD 6c489cc6de: eb-1.AC1 FAIL (2: 18 calls, exit 3; control (c) PASS) as expected. Organic proof: the next vehicle run with Bloomberg down (nothing is planted on the world).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<workstream>BBGLEG</workstream>
<slot>~2</slot>
<fabric>site-z</fabric>
