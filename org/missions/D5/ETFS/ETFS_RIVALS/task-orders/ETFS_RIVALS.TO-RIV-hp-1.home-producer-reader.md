# ETFS_RIVALS task order -- `RIV-hp-1` -- ROUND 3 (ENRICHMENT): THE HOME-PRODUCER READER -- IDVZ AND PFOE BESIDE THEIR RIVALS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-hp-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~1</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~06:4xZ, --drift) -- 2 armed gates fabric-wide, none names rivalfunds/, bbg/<D>/constituents/ or this cell's files; the Positioning pull is under an Andrew-direct no-modify order (read only).
comp-iam: RUN at L5 -- no IAM change in this cell; the canonical-shape Lambda's read of bbg/<D>/constituents/ is measured by RIV-d-4 before the deploy (a GetObject the round-2 policy may not grant).
comp-adversary: RUN at L5 on the round-3 decomposition (3 of 3 cited commits verified); declared on RIV-i-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ,
PFOE), each fund's trade schedule, and a served page grouped by Opal fund. Rounds 1-2 built and enriched the live pipeline (package
`data/etfs/scripts/rivalfunds/`). The page today shows the two OPAL funds themselves as ABSENT ("home-producer reader: next
round"). **This cell gives them a reader.** Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-hp-1` -- the home-producer reader (C-HOME-PRODUCER v0.5; row W1-S8)

- **`home_producer.py` (new):** reads `s3://opal-data-etfs/bbg/<D>/constituents/constituents_issuer_fill.parquet` for the
  `home_producer` funds of the map (IDVZ, PFOE); report date = each row's `date`; address = the producer's own
  (`etf_daily_pull.PREFIX` / `BUCKET`), read, never rebuilt. Columns used: `fund_ticker`, `holding_ticker`, `cusip`,
  `security_name`, `shares`, `price`, `market_value`, `weight_pct`, `is_cash`, `date`.
- **`gold_canonical_shape.py`:** the `home_producer` policy now has a reader: each home fund's rows for the report date land in G1
  with `source_used = 'home_producer'`, every row of the landing kept (cash included, `is_cash_line` from the landing's `is_cash`
  or the vocabulary's sentinel), identity through the existing crosswalk path on CUSIP/ticker; the report dates a replay considers
  include the landing dates.
- **`gold_holdings_coverage.py`:** the home funds get G2 rows from the same landing (`source = 'home_producer'`, `selected = true`);
  a trading day with no landing reads `gap` with the cause (capture-forward from 2026-08-21, the C-HOME-PRODUCER limit).
- The page needs no edit: a home fund with G1 data renders through the normal fund view (the placeholder appears only when G1
  has none).
- No second copy: nothing is written under `bbg/` or any silver prefix for the home funds.

## 2. THE CONTRACT YOU IMPLEMENT (PRD v0.7 C-HOME-PRODUCER, verbatim)

"(v0.5, Andrew-direct 2026-09-30 ~21:0xZ: "1b" ...; ~20:2xZ: "we're leaving the existing pull alone") For IDVZ and PFOE, this
pipeline READS the Positioning pull's landing as a named source. It lands no second copy. The Positioning pull is not modified.
The grain shortfall RIV-m-1 measured is a stated LIMIT on FWD-2/3 for the home funds, never engineered around: capture-forward
from 2026-08-21, 22 of 27 days. Missing days read ABSENT with their cause. IDVZ and PFOE leave this pipeline's Bloomberg request.
Never two producers of one fund's holdings."

## 3. WHAT YOU NEED TO KNOW (measured at the cut, base 78167bb8fc)

- The landing exists for every trading day since 2026-08-21 (probed: 2026-09-23/24/25/28/29 present). One file per run date holds
  four funds: `fund_ticker` counts on 2026-09-29: PFDE 90, IDVZ 41, DIVZ 30, PFOE 25. DIVZ and PFDE are NOT in the universe and
  never enter G1. Schema (30 columns) includes `date` (timestamp), `fund_ticker`, `holding_ticker`, `cusip`, `security_name`,
  `shares`, `price`, `market_value`, `weight_pct` (percent), `is_cash` (often null), `fill_source`.
- `integrations/bloomberg/pipeline/etf_daily_pull.py` defines `BUCKET = "opal-data-etfs"` and `PREFIX = "bbg"` (READ, never edit).
- `gold_canonical_shape.py` today: `select_sources(funds, issuer_funds, bbg_funds)` puts `home_producer` funds in `unread`;
  `universe.policy(f)` returns `home_producer` for IDVZ and PFOE (`peer_groups.json`); the module docstring's "home_producer -- no
  reader exists yet" line is yours to update. Sinks: `sinks.get_sink("local:<dir>")` maps an `s3://bucket/key` URI to
  `<dir>/bucket/key` -- the checks place the landing there.
- `publish_page.py` / `render.py` already render a fund with G1 rows normally and a `home_producer` badge (`render.SOURCE_LABEL`).
  They are NOT yours this round (another cell owns `publish_page.py`); if the page needs more than G1/G2 data, file a row.

## 4. SURFACES AND BOUNDS

You READ (never edit): `integrations/bloomberg/pipeline/etf_daily_pull.py`, `lib/research/identity/`, `lib/trading_calendar.py`,
`data/etfs/scripts/rivalfunds/universe.py`, `peer_groups.json`, `homes.py`, `markers.py`, `sinks.py`, `publish_page.py`,
`render.py`; `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{1,2,3}/checks/`; live S3 READ-ONLY for
`bbg/<D>/constituents/` (the checks copy two objects locally); the device-local captures under
`C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~1/`). NEVER: any S3 write, any deploy, the Positioning
pull or anything under `integrations/bloomberg/`, any Bloomberg or OpenAI call, `publish_page.py`, `sweep.py`, `silver_issuer.py`,
`gold_trade_schedule.py`, `enrichment_bloomberg.py`. Tests: `tests/test_hp1_*.py`, run with `python -m pytest <file> -q` from
`data/etfs/scripts/`.

<paths>
data/etfs/scripts/rivalfunds/home_producer.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/gold_holdings_coverage.py
data/etfs/scripts/rivalfunds/tests/test_hp1_*.py
data/etfs/scripts/rivalfunds/tests/test_g12_canonical_multi_source.py
data/etfs/scripts/rivalfunds/tests/test_g21_holdings_coverage.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

(The two existing test files are granted because they assert "home_producer is counted unread"; change only that assertion and say so.)

## 5. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- G1 carries IDVZ and PFOE rows from the landing (`source_used = home_producer`), row counts equal to the landing's, no
  DIVZ/PFDE, TXUE still `bloomberg`, nothing written under `bbg/` (`.../round3/checks/hp-1.AC1.py`)
- **AC2** -- G2 has an IDVZ row selected from `home_producer`, and the page shows IDVZ and PFOE with a calendar and a
  `home_producer` badge, with no placeholder (`.../round3/checks/hp-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-hp-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/hp-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-hp-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round3/checks/hp-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 6. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~1/ETFS_RIVALS.TO-RIV-hp-1.home-producer-reader.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-hp-1.home-producer-reader`. Report once: each criterion's verdict line with the output above it; the files you wrote; any test assertion changed; any row filed. Leave the `<status>` flip to the issuer. Your slot then continues with RIV-i-1 and RIV-g-6, handed to you after each merge.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** PRD v0.7 @01114ae8a8 ADMITTED. Round-2 analysis item 3 / ruling 4. Checks dry-run at base
78167bb8fc: hp-1.AC1 FAIL (IDVZ 0 vs 41, PFOE 0 vs 25 landing rows), hp-1.AC2 FAIL (no IDVZ G2 row; no home badges; placeholder
served) -- each FAIL as expected.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>3</round>
<slot>~1</slot>
<fabric>site-z</fabric>
