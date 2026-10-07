# ETFS_RIVALS task order -- `RIV-rt-1` -- ROUND 15 (ENRICHMENT): THE GATEWAY SERVES A FUND'S CHART OBJECT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-rt-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~4</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell (the backfill is ad hoc by Andrew's word and is run by the issuer, never scheduled)
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (the chart objects sit under the page prefix the publisher already writes and the gateway already reads)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. **Round 15** (PRD v0.18 FWD-22, FWD-23): every period becomes 30 / 90 / 365 calendar days; the security dialog gains a price curve with the fund's buys and sells marked on it, fed by a per-fund chart object behind one gateway route and drawn by the page's one script; a Bloomberg close-price backfill is built (never run by a worker). Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

Shared vocabulary (binding on every cell):
- **Periods:** `R30`, `R90`, `R365` -- calendar days. `asof = prev_trading_day(page_day)` (the existing CALL 3 rule); a window's
  first day is `asof - N calendar days`, its last day `asof`. `MTD`, `QTD`, `YTD` keep computing and are never displayed.
- **Chart object:** one JSON per fund per page day at `homes.page(<day>, "charts/<FUND>.json")` (opal_naming output), shape
  `{"fund", "asof", "generated_at", "ranges": {"R30": <first day>, "R90": ..., "R365": ...}, "securities": {<security_key>:
  {"name", "source_words", "points": [[<YYYY-MM-DD>, <price>|null, <source code>], ...], "gaps": [{"start", "end", "reason"}],
  "markers": [{"side": "buy"|"sell", "start", "end", "span": bool, "usd", "bps", "r", "n_trades"}]}}}`. Source codes:
  `m` market close, `i` holding-implied. `points` ascend by date and cover `asof - 365d .. asof`.
- **Route:** `GET /rivalfunds/<YYYY-MM-DD>/chart/<FUND>` on the gateway, JSON, behind the same identity wall.

### `RIV-rt-1` -- the gateway serves a fund's chart object (FWD-22; F.5 item 2; WORLD, released by NFRA_OPLGTW)
- Today `rivalfunds_view` serves `/rivalfunds/<day>` and `/rivalfunds/<day>/audit` (2 MB cap, audit log, identity wall).
- Interface: `rivalfunds_view.chart_key(day, fund)` (the page prefix + `date=<day>/charts/<FUND>.json`; `fund` must match
  `^[A-Z0-9]{1,8}$`) and handler `rivalfunds_chart` for `/rivalfunds/{day}/chart/{fund}`: 200 `application/json` with the
  object's bytes; bad day or bad fund -> 400; no object -> 404 JSON `{"error": "no chart for this fund and day"}`; over the cap
  -> the page's own over-cap refusal; every call audit-logged with `{"day", "fund", "route": "chart"}`. The route is declared
  in `ROUTE_CLASS` as `access-layer` and mounted in `server.py` by this cell.
- Rulings at the cut (issuer): CORRECTION -- the over-cap refusal is the page's own (502, `rivalfunds_view.py` `_serve_day`),
  not a 413. No viewer -> 401 as the other routes. The 200 and the 404 are audit-logged; a 400 and a 401 are not, as today.
  The `server.py` Route and the `ROUTE_CLASS` line are THIS cell's (the lane refuses the issuer's commit there: round 13
  AMENDMENT 1), so both files are in its paths.
- **Organic trigger:** a signed-in click on a security modal after RIV-md-1 is served.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rt-1.AC1.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- Model the handler on `rivalfunds_audit` / `_serve_day` in the same file (identity, cap, cache, audit log). JSON, not HTML: `Content-Type: application/json`.
- Mount `Route("/rivalfunds/{day}/chart/{fund}", rivalfunds_view.rivalfunds_chart, methods=["GET"])` in `server.py` beside the audit route and declare it `access-layer` in `ROUTE_CLASS` (`tests/test_principal_cutover.py`), as round 13 did for the audit route; the two route-census tests must pass.
- New tests go in `app/tests/test_rivalfunds_view.py` (the existing file). NO gateway release, NO Terraform, NO S3 call: the release is NFRA_OPLGTW's.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~4/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests in `app/tests/test_rivalfunds_view.py`; run the gateway suites (`python -m pytest app/tests tests -q` from `infra/aws/ec2/opal-gateway/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
infra/aws/ec2/opal-gateway/app/rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/tests/test_rivalfunds_view.py
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the chart key, 200 JSON with the object's exact bytes, 400 on a bad day or fund, 404 JSON on no object, the audit log; control: the audit route still serves (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rt-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-rt-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/rt-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~4/ETFS_RIVALS.TO-RIV-rt-1.the-gateway-serves-a-funds-chart-object.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-rt-1.the-gateway-serves-a-funds-chart-object`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~4`, slot `~4`, position 1 of 1. Checks dry-run at base by the issuer: rt-1.AC1 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~4</slot>
<fabric>site-z</fabric>
