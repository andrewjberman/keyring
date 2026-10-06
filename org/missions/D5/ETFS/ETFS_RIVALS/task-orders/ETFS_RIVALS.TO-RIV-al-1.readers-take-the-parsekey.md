# ETFS_RIVALS task order -- `RIV-al-1` -- ROUND 13 (ENRICHMENT, workstream BBGLEG): THE THREE READERS TAKE PK-1'S PARSEKEY, SO ONE SECURITY UNDER TWO LISTINGS IS ONE KEY ON THE WHOLE PAGE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-al-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<direct_act>true</direct_act>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE the readers already read G4 (gold/security_market) under their roles; no IAM grant, role or policy changes
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas). RIV-pk-1 (merged, NOT yet deployed) gave G4 a `security_parsekey` column and taught the rankings (`gold_holding_contribution`) and the trade schedule to join a CUSIP/ISIN-keyed holding to the Bloomberg key another fund carries. Three readers on the same page were left out; deploying pk-1 alone would show one security merged in the rankings and split in the trend. This cell aligns them; the deploy follows under one pair. Nothing here deploys, merges or calls Bloomberg/OpenAI. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-al-1` -- the three readers take pk-1's parsekey, so one security under two listings is one key on the whole page (ADDENDUM 5 @a8fb9c1df1)
- Measured 2026-10-06 (2.0.0_SA_COO~RV, AST census of `data/etfs/scripts/rivalfunds/` at CLOUD 325e20b091): 20 call sites of 10
  functions that take pk-1's parsekey (`pk` / `parsekeys`); 6 omit it -- gold_buying_trend.py:79 and :192 (identity_maps),
  gold_input_census.py:139 (identity_maps), :140 (_cross_sectors), :146 (_books), sweep.py:306 (held_funds). On a two-listing
  plant (GQGU Nebius CUSIP-only N97284108 + WCMG NBIS_US_Equity, G4 parsekey N97284108 -> "NBIS US Equity") the rankings bucket
  both under NBIS_US_Equity while the trend and the census name GQGU's by N97284108.
- Interface: each of the six sites passes the parsekey, taken from the G4 the reader already reads (`parsekey_map(g4)`) or, for
  the sweep's hold gate, from `gold_trade_schedule.load_parsekeys(s, canonical)`; `gold_buying_trend.build(..., g4)` derives it
  from its `g4` argument. A reader with no G4 passes an empty map (today's behaviour). No other site changes.
- **Organic trigger:** the 07:00 ET marker publish (A1: trend, census) and the 09:00 ET sweep (the hold gate).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD ba005db3b0)

- The check files' docstrings are the exact interface they read: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC1.py`, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC2.py` and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/_common.py` before you build.
- pk-1's API (gold_holding_contribution.py / gold_trade_schedule.py): `parsekey_map(g4)` -> {CUSIP/ISIN key: parsekey}; `identity_maps(g1, pk=None)`, `row_keys(df, alias, pk=None)`, `_books(g1, pk=None)`, `_cross_sectors(g1, day, pk=None)`; `load_parsekeys(s, canonical)`, `held_funds(canonical, actions, scope_end=..., parsekeys=None)`. Read `tests/test_r12pk1_parsekey_join.py` for how pk-1's own callers pass it.
- `gold_buying_trend.build(g5, g6, g1, day, universe_entries, g4=None)` (~184) and its `_sectors(g1)` (~70); the handler (~280) already reads G4 windows. `gold_input_census.build(day, s, universe_entries, readings, page_day=...)` (~119) already reads G4 (`g4w`, `g4u`). `sweep.py` ~298-306 builds `canonical` then calls `gts.held_funds(...)`.
- Keep every existing test green; RIV-ok-1 / pk-1 tests (`tests/test_r10ok1_*`, `tests/test_r12pk1_*`) must still pass.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (Andrew-direct no-modify order), the package's other modules, the round-12/13 check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition, and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md` (ADDENDUM 5).

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 read or write, any deploy, any Bloomberg or OpenAI call, any environment gate flip outside a test, any file under `integrations/`. New tests as `tests/test_r13al1_*.py`, run from `data/etfs/scripts/`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_buying_trend.py
data/etfs/scripts/rivalfunds/gold_input_census.py
data/etfs/scripts/rivalfunds/sweep.py
data/etfs/scripts/rivalfunds/tests/test_r13al1_*.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- census: every identity call site in the package passes the parsekey (denominator printed); control: the census still sees >= 20 sites (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC1.py`)
- **AC2** -- plant: one security under two listings is ONE key in the rankings, the trend and the census; control: the rankings already do it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC2.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-al-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-al-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round13/checks/al-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-al-1.readers-take-the-parsekey.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-al-1.readers-take-the-parsekey`. Report once: each criterion's verdict line with the output above it; files written; every existing test assertion changed and why; the package suite's final line; rows filed (id + one line); hookups for the issuer. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** ROUND_ANALYSIS.round10.md ADDENDUM 5 @a8fb9c1df1 item 1; decomposition v1.2. Round 13, workstream BBGLEG, chain `~3`, slot `~3`, position 1 of 1. Direct act (one cell, under ~300 product lines; its close is the issuer's real run, then the ONE deploy pair with pk-1 and the ADDENDUM 1 census). Checks dry-run at base CLOUD 325e20b091: al-1.AC1 FAIL (1: 6 of 20 sites omit; control (b) PASS) as expected; al-1.AC2 FAIL (2: trend and census name N97284108; control (a) PASS) as expected.

<risk>SERVED</risk>
<worker_class>worker-light</worker_class>
<status>pending</status>
<round>13</round>
<workstream>BBGLEG</workstream>
<slot>~3</slot>
<fabric>site-z</fabric>
