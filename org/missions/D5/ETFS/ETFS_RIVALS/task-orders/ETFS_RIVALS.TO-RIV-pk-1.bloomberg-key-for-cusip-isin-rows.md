# ETFS_RIVALS task order -- `RIV-pk-1` -- ROUND 12 (ENRICHMENT): BLOOMBERG'S OWN KEY FOR CUSIP/ISIN-KEYED SECURITIES RIDES THE EXISTING G4 REQUEST; THE ONE-KEY JOIN READS IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-pk-1</owned_cells>
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

### `RIV-pk-1` -- Bloomberg's own key for CUSIP/ISIN-keyed securities rides the existing G4 request; the one-key join reads it (ADDENDUM 1 @982e914b1d, row Z-S43)
- Measured 2026-10-06 on G1 2026-10-01: GQGU reports Nebius CUSIP-only (security_id null, raw N97284108, cusip N97284108, isin
  NL0009805522); WCMG reports `NBIS_US_Equity` with NO CUSIP/ISIN. RIV-ok-1's CUSIP/ISIN join cannot meet them; a refresh publish
  at its code is byte-identical to the control (Nebius shows twice).
- Interface: `enrichment_bloomberg` mode `market`: the current-value reference request for an identifier-keyed security
  ('/cusip/..', '/isin/..') also asks `PARSEKYABLE_DES`; a Bloomberg-keyed security's request does not. The answer lands in G4
  column `security_parsekey` (null when not asked or not answered); the market result's detail carries the number of
  PARSEKYABLE_DES points asked (S24's daily budget). `gold_holding_contribution` and the trade schedule's position key (RIV-ok-1's
  `row_keys` / `stable_key`): a row keyed by a CUSIP/ISIN whose G4 row carries `security_parsekey` P takes the key
  `security_key(P)` when another row in the input window carries that key; otherwise it keeps its own key.
- **Organic trigger:** the vehicle's 07:00 ET market pull (G4), then the 07:00 ET marker publish (A1) and the batch chain (G5).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD 6c489cc6de)

- The check file's docstring is the exact interface it reads: read `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/pk-1.AC1.py` (and `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/_common.py`) before you build. You run this order AFTER RIV-eb-1 on the same branch: keep eb-1's session bound intact.
- The G4 reference request: `_market_pull` asks `plan["fields"]` per batch (`build_market_plan`, ~455); identifier-keyed securities are the '/cusip/..' and '/isin/..' request strings. `market_rows` builds the G4 rows -- add `security_parsekey` there (null for a Bloomberg-keyed row). Ask PARSEKYABLE_DES ONLY for identifier-keyed securities (a separate reference batch for those keys, or the same request with the field added for them only -- your choice, stated in the report) and put the number of points it adds in the market result's detail.
- RIV-ok-1 (commit 4f86af2279) added the CUSIP/ISIN join in `gold_holding_contribution.py` (`_books` / the alias map) and `gold_trade_schedule.py` (`row_keys` / `stable_key`); its tests are `tests/test_r10ok1_one_key_per_security.py`. Extend that join with the G4 parsekey; a parsekey whose `security_key(P)` no row in the window carries changes nothing.
- G5 stamps `producer_version` (`gold_trade_schedule.GOLD_VERSION`, RIV-gt-1): if your change alters any G5 row, bump GOLD_VERSION and say so in the report; if it does not, leave it.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (under an Andrew-direct no-modify order: no file there is written or read differently), the package's other modules, the round-12 and earlier rounds' check folders under `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/`, the decomposition `org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md`, and the analysis `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round10.md`, and ADDENDUM 1 there.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~2/`). NEVER: any S3 read or write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests; blpapi is never imported off the terminal), any environment gate flip outside a test, any file under `integrations/`. New tests go beside the code as `tests/test_r12pk1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite (`python -m pytest rivalfunds/tests -q` from `data/etfs/scripts/`) before you report: it must read 0 failed. A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file (`surfaced_at` = `date -u +%FT%TZ` at filing), never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/gold_holding_contribution.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r12pk1_*.py
data/etfs/scripts/rivalfunds/tests/test_r10ok1_one_key_per_security.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the G4 reference request asks PARSEKYABLE_DES for exactly the identifier-keyed securities and stores it; GQGU's CUSIP-only Nebius row joins WCMG's NBIS_US_Equity; control: a CUSIP whose parsekey names a key no row carries keeps its CUSIP (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/pk-1.AC1.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-pk-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round12/checks/pk-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~2/ETFS_RIVALS.TO-RIV-pk-1.bloomberg-key-for-cusip-isin-rows.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-pk-1.bloomberg-key-for-cusip-isin-rows`. Report once: each mechanical criterion's verdict line with the output above it; files written; every existing test assertion changed and why; the package suite's final line; rows filed (id + one line); the hookups you need the issuer to add at the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** decomposition round 12 v1.1 (issuer amendment when the Bloomberg hold lifted, MSTR~Z msg 30169 @8555ce7e12). Chain `~2`, slot `~2`, position 2 of 2 (eb-1 then pk-1: both write enrichment_bloomberg.py). Check dry-run at base CLOUD 6c489cc6de: pk-1.AC1 FAIL (2; control (c) PASS) as expected. Issuer acts after the drain (ADDENDUM 1 items 3-4): the merged-pair census across all funds on the first real G4 with parsekeys, and ok-1's J1 under its own deploy pair (the NBIS label riding it).

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>12</round>
<workstream>BBGLEG</workstream>
<slot>~2</slot>
<fabric>site-z</fabric>
