# ETFS_RIVALS task order -- `RIV-pd-2` -- ROUND 15 (ENRICHMENT): EVERY SWITCH OFFERS 30d | 90d 365d AND OPENS ON 30d

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pd-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
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

### `RIV-pd-2` -- every switch on the page offers 30d | 90d 365d and opens on 30d; no QTD, YTD or MTD is displayed (FWD-23)
- Today `render.PERIODS = ("R30","QTD","YTD")`, `PERIOD_LABEL` names them, `_dialog_keys` covers R30 and YTD (:753), the trend
  sentence says "this year" for YTD (:1750), `_sec_dialogs` prefers the YTD trend row (:1776).
- Interface: `render.PERIODS = ("R30","R90","R365")`; `PERIOD_LABEL = {"R30": "Last 30 days", "R90": "Last 90 days", "R365":
  "Last 365 days"}`; the switch reads 30d, the dividing line, then 90d and 365d, and opens on R30. No element of the rendered
  main page or audit page carries the visible text QTD, YTD, MTD, "Quarter to date", "Year to date" or "Month to date". The
  dialog keys cover R30 and R365; the security dialog's trend row prefers R365. A period that ranks nothing for the fund greys
  and says why (unchanged rule). Rows of MTD / QTD / YTD in the context are ignored, not an error.
- Rulings at the cut (issuer): the switch's own words are short -- `render.PERIOD_SHORT = {"R30": "30d", "R90": "90d", "R365":
  "365d"}` is what each period radio's label prints (Andrew: "30d, then | 90d and 365d"); `PERIOD_LABEL` (the long names) is
  for table headings and dialog rows. The clause "the dialog keys cover R30 and R365" is WITHDRAWN (`_dialog_keys` has no
  caller); the dialog lists the three periods and its buying line is the R365 trend row.
- **Organic trigger:** the 07:00 ET marker publish.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD f14a8198f7)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- Many existing tests pin QTD / YTD labels and panels (`tests/test_r6ui2_ranking_panels.py`, `tests/test_r8rn1_period_switch.py`, `tests/test_crorv_layout.py` and others): re-pin them to the three rolling periods and list every assertion you change and why.
- Keep round 14's badge (`data-build`, `grounding_census`) and the audit size rule intact: re-run `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round14/checks/ab-1.AC1.py` and `as-1.AC1.py` before you report and give each final line.
- You run this AFTER RIV-pd-1 on the same branch; RIV-md-1 follows.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, FWD-23, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15pd2_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the constants, no visible QTD / YTD / MTD on the main or audit page, the switch order and the R30 default; control: the R30 rankings render (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC1.py`)
- **AC2** -- the security dialog lists the three periods, its buying line is the R365 trend row, an empty period greys with its reason; control: the dialog keeps a section per fund (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pd-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-pd-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pd-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-pd-2" judgment="true"/>
</proof_of_spec>

J1 (graded by 3.0.0_SA_CVO~RV at L9 on the served page, never self-graded): every ranking, trend and dialog offers exactly 30d, 90d and 365d, opens on 30d, and a period a fund's history does not reach reads partial with its reason.

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-pd-2.the-page-offers-30d-90d-365d-and-opens-on-30d.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pd-2.the-page-offers-30d-90d-365d-and-opens-on-30d`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; every existing test assertion changed and why; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.5 (round 15 appended). Chain `~1`, slot `~1`, position 2 of 3. Checks dry-run at base by the issuer: pd-2.AC1 FAIL as expected (control PASS); pd-2.AC2 FAIL as expected (control PASS). Check files drafted by read-only helpers under the issuer's brief and re-run by the issuer.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>15</round>
<slot>~1</slot>
<fabric>site-z</fabric>
