# ETFS_RIVALS task order -- `RIV-pc-1` -- ROUND 16 (REPAIR OF ROUND 15): A HOLDING-IMPLIED PRICE IS DRAWN ONLY FOR A LISTING QUOTED IN US DOLLARS; THE CHART SAYS THE CURRENCY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pc-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~6</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell (it reads a column of a table the publisher already reads and adds one key to an object the publisher already writes)
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files and the real-run record
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two peer groups): rankings, buying trend, AI accounts per fund, a security dialog per holding, and a separate audit page; published to S3 by the package `data/etfs/scripts/rivalfunds/` (five AWS stage Lambdas) and served signed-in by the opal-gateway. **Round 15** (PRD v0.18 FWD-22, FWD-23) built the security dialog's price curve: a per-security price series (`price_series.py`), a per-fund chart object written by the publisher (`publish_page.py`), and the page's one script that draws it (`render.py`, `CHART_SCRIPT`). All of that is merged. **This order, round 16, is the one repair of round 15.** Nothing here deploys, merges or calls a vendor (stub every OpenAI and Bloomberg hook). Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-pc-1` -- a holding-implied price is drawn only for a listing quoted in US dollars; the chart says the currency (FWD-22; row Z-S55; CTO ruling 30787)
- Measured (real run, day 2026-10-06, 13 chart objects, 695 fund-securities): 598 carry both source codes; the first market
  close over the last holding-implied price before it is above 3 or below 1/3 for 152 of 598 (JP 43/43, LN 54/54, HK 11/11,
  KS 9/9; US 0/238). The funds' holding reports are in US dollars; a Bloomberg close is in the listing's quote currency.
  G4 `security_market.currency` (Bloomberg `CRNCY`) is stored per security: on 2026-10-05, 0 of 578 priced rows carry none;
  values include `USD` 193, `EUR` 92, `JPY` 78, `GBp` 35 (London quotes in pence; 1 London listing is `USD`).
- Interface: `price_series.series` reads each key's quote currency from the G4 frame it is handed: the `currency` of the
  key's NEWEST G4 row that carries one (a row with no `px_close` still counts). The value is READ, never inferred from the
  exchange code. Exactly `"USD"` -> the series is built as today (`m`, then `i`, then a gap). Anything else, and a key
  with no stored currency, -> market closes only: a day with no positive close is `None` whatever the funds report, and
  its gap reason is `"no market close on file (the funds' holding reports are in US dollars and this listing is not quoted
  in US dollars)"`. Each key's result gains `"currency": <the stored string> | None`. `source_words` says in plain words
  which sources the series uses and, for a non-dollar listing, that the prices are in the listing's currency.
  The chart object's `securities[<key>]` gains `"currency"`. The page's one script shows the currency beside the price
  axis and in the hover's price words (`null` -> "currency not on file"). A trade marker is placed by its DATE on the
  curve and never by a dollar price; on a day with no price it keeps its date marker.
- Rulings at the cut (issuer): `load` reads G4 as it does today (the same window), so a key whose only G4 rows fall outside
  the window has no stored currency and is treated as non-dollar. The currency comparison is exact and case-sensitive
  (`GBp`, `ZAr`, `ILs`, `KWd` are not dollars). No new Bloomberg field is requested and nothing under `integrations/`
  changes. The fixtures of `round15/checks/co-1.AC1.py`, `co-1.AC2.py`, `md-1.AC1.py` and `md-1.AC2.py` hold no G4
  currency; the cell may plant G4 rows carrying `currency` `USD` (no `px_close`) for those fixtures' securities and add
  `"currency"` to an exact key set those checks compare, and may change nothing else in them.
- **Organic trigger:** opening a non-US security's modal on the live page; the issuer's real run re-measures the 598.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 370ae7a279 or later)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/_common.py` before you build. Where a docstring and the cell's "Rulings at the cut" differ, the RULING wins and the check accepts it.
- `price_series.py` today: `_market(g4, wanted)` gives `(key, ISO date) -> positive px_close`; `_implied(g1, g4, wanted)` gives the holding-implied prices; `series(...)` joins them; `load(s, keys, start, end)` reads the two tables through the sink. Its `_G4_COLUMNS` does not read `currency`; the stored column is `currency` in `enrichment_bloomberg.MARKET_COLUMNS`. A G4 row maps to a key by the rule `_market` already uses; use the same rule for the currency.
- `publish_page._build_charts` builds each `securities[<key>]` from `price_series.load` and `trade_markers.markers`; `_chart_json` thins an object over the cap. Add `"currency"` there from the series result.
- `render.CHART_SCRIPT` is the page's ONE inline script (plain text in a Python string; the suite runs its `plan` and `words` under node and `node --check` parses it). It draws the y axis from the points, each marker as a circle at its end date, and a hover line. Keep it one bare inline script: `render.validate` refuses a second script, `src=`, `<link`, `@import` and `url(`. Read how the script places a marker before you change anything: if it already places a marker by date on the curve (no dollar price), say so in the report and leave that part alone.
- A page with no script change still has to pass `md-1.AC2.py`, which pins the script count and the refused constructs.
- The earlier checks `co-1.AC1.py`, `co-1.AC2.py`, `md-1.AC1.py`, `md-1.AC2.py` build their fixture with no G4 table, so after your change every price in them would be dropped as "currency not stored". You may edit those four files ONLY to plant G4 rows carrying `currency` `USD` (no `px_close`) for the fixture's securities, and to add `"currency"` to an exact key set they compare (`SEC_KEYS` in co-1.AC1). No assertion, expected value or message in them changes. The issuer diffs those four files at the merge.
- Existing package tests that build a chart object or a series with no G4 currency will need the same planted `USD` row; say in the report which tests you changed and why.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), every file not in your `<paths>`, the round-8..15 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/` except the four check files named in your `<paths>`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (FWD-22, ADDENDUM F).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~6/`). NEVER: any S3 read or write, any deploy or gateway release, any Terraform, any OpenAI or Bloomberg call (stub every vendor hook), any environment gate flip outside a test, any file under `integrations/`. New tests as `data/etfs/scripts/rivalfunds/tests/test_r15pc1_*.py`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/price_series.py
data/etfs/scripts/rivalfunds/publish_page.py
data/etfs/scripts/rivalfunds/render.py
data/etfs/scripts/rivalfunds/tests/
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC1.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/co-1.AC2.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC1.py
org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/md-1.AC2.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the series reads the stored quote currency; a dollar listing keeps its holding-implied points; a non-dollar or unknown one carries market closes only, with the non-dollar gap reason; control: the fixture frames hold the planted values (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC1.py`)
- **AC2** -- the chart object carries each security's currency, the page's one script reads it, and ps-1.AC1, co-1.AC1, co-1.AC2, md-1.AC1 and md-1.AC2 still end PASS; control: the page publishes on the fixture (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC2.py`)
- **J1** (judgment, graded by 3.0.0_SA_CVO~RV on the issuer's real run, never by you): on the real day's chart objects no security's curve joins two currencies, and a reader of a non-US security's dialog can tell which currency the prices are in.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-pc-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round15/checks/pc-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="J1" cell_refs="RIV-pc-1" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~6/ETFS_RIVALS.TO-RIV-pc-1.an-implied-price-is-drawn-only-for-a-dollar-listing-and-the-chart-says-the-currency.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pc-1.an-implied-price-is-drawn-only-for-a-dollar-listing-and-the-chart-says-the-currency`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; the exact lines you changed in the four earlier check files; every existing test assertion changed and why; how the script places a marker; the suite's final line; rows filed (id + one line); anything the issuer must do at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.18 @6e245cbebe (ADMITTED: ratified half signed by 3.0.0_SA_CVO~RV); decomposition v1.6 (round 16, the repair of round 15, appended). Source: row ETFS_RIVALS-Z-S55 @a26fc880e9 and the ruling of 1.0.0_SA_CTO~Z msg 30787 (shape (a): implied prices only where the stored quote currency is USD; the currency read from a stored field; the chart object carries it and the axis shows it; a dollar trade price is not plotted against a non-dollar axis; proof on the same real run -- jumps over 3x 0 of 598, US 238 of 238 unchanged, euro listings measured and printed). Term 4 is the issuer's act at the drain, not a worker criterion. Chain `~6`, slot `~6`, position 1 of 1. Checks written and dry-run at base 370ae7a279 by the issuer: pc-1.AC1 FAIL 3 failures as expected (arms a, c, d; b and the control e PASS); pc-1.AC2 FAIL 2 failures as expected (arms a, b; c and the control d PASS).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>16</round>
<slot>~6</slot>
<fabric>site-z</fabric>
