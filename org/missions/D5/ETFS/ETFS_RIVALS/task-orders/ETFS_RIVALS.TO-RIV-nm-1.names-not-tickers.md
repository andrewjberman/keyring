# ETFS_RIVALS task order -- `RIV-nm-1` -- ROUND 6 (ENRICHMENT): NAMES, NOT RAW TICKERS OR 30-CHARACTER CUTS (RFW-D05, RFW-D11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-nm-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~5</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-nm-1` -- names, not raw tickers or 30-character cuts (RFW-D05, RFW-D11; RFW-U14 data half)
- The rivalfunds BQL capture asks for the name: `get(id(), name()) for(holdings([...],dates=D))`. `collector_bloomberg`'s
  `request_plan` and `excel_fetch` build the SAME string; it is tested offline with fake COM modules, never a live session.
- silver stores the `name()` header as column `name`, and `gold_canonical_shape.build_bloomberg_rows` sets `security_name` to
  it exactly as captured. Display casing is the page's.
- New `rivalfunds/names.py` `display_name(candidates: list[str | None]) -> str | None`:
  - blanks are dropped;
  - a raw ticker is `<id> XX Equity` or `<id>_XX_Equity`;
  - the longest real name wins, but a name of exactly 30 characters ranks below any other real name;
  - with no real name the first ticker is returned; with no candidates, None;
  - an ALL-CAPS winner is re-cased per run of letters ("Mitsubishi Ufj Financial Group", "S&P Global Inc", "3M Co");
  - a name with any lower-case letter returns unchanged.
- Hazard, the issuer's to prove LIVE after the drain: the real BQL response shape for `name()` is unknown offline. A duplicate
  header makes silver refuse the capture, and `excel_fetch` reads columns A-P only.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- Today the BQL capture carries no name into silver/G1, so 9 Bloomberg funds show '8306 JP Equity'-style tickers; IDVZ's home-producer names are cut at exactly 30 characters (RFW-D05, RFW-D11).
- `excel_fetch` is tested with fake COM modules installed before the call (pywin32 is installed on this machine; never start Excel or a Bloomberg session). It reads columns A-P only.
- These files are ALSO run by the terminal vehicle from the CLOUD tree; the issuer proves the live response shape after the drain.
- Applying `display_name` in the producers is the issuer's merge hookup, not yours.
- AMENDMENT A1 (issuer, 2026-10-02 ~17:0xZ): the issuer's LIVE probe (BIDD, dates=2026-10-01, through your own excel_fetch, local file only) shows the real two-field response. Bloomberg PREFIXES every metadata column by its field: `ID, id().SOURCE, id().POSITION, id().POSITION_CHANGE, id().WEIGHTS, id().CURRENCY, id().REPORTED_MKT_VAL, id().DATE, id().REPORT_DATE, id().ORIG_IDS, id().POSITION_TYPE, id(), name().SOURCE, name().POSITION_TYPE, name().ID_DATE, name()` -- exactly 16 columns, so the A-P read is full. `silver_bloomberg.parse_capture` refuses it ("header lacks ORIG_IDS"), so as built the vehicle's Bloomberg leg would stop. The order's earlier fixture (an unprefixed `name()` column) was wrong. Make silver map the `id().` metadata to today's column names, keep `name()` as `name` (the `name().` metadata may be dropped or kept under non-colliding names), keep today's single-field capture working, and make excel_fetch read past column P. AC4 below uses the probe's real header and rows.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~5/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6nm1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/collector_bloomberg.py
data/etfs/scripts/rivalfunds/silver_bloomberg.py
data/etfs/scripts/rivalfunds/gold_canonical_shape.py
data/etfs/scripts/rivalfunds/names.py
data/etfs/scripts/rivalfunds/tests/test_r6nm1_*.py
data/etfs/scripts/rivalfunds/tests/test_b1_bloomberg_channel.py
data/etfs/scripts/rivalfunds/tests/test_g1_canonical_shape.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the offline plan and excel_fetch both ask for name(); silver stores it; canonical_shape security_name carries it; a row with no name stays NULL (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC1.py`)
- **AC2** -- display_name prefers the uncut name over a 30-character cut and a name over a raw ticker, consistently cased (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC2.py`)
- **AC3** -- control: a single good name passes unchanged; display_name([None, None]) is None (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC3.py`)
- **AC4** -- (a fourth criterion; reason: amendment A1, the live response shape) the real two-field capture imports and types, silver keeps today's id() column names plus `name`, G1 carries the names, excel_fetch reads past column P; control: today's single-field capture still lands (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC4.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-nm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-nm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-nm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC4" cell_refs="RIV-nm-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/nm-1.AC4.py</invocation><expect>AC4 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~5/ETFS_RIVALS.TO-RIV-nm-1.names-not-tickers.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-nm-1.names-not-tickers`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~5`, slot `~5`, position 1 of 1. Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
nm-1.AC1 FAIL (3; controls OK) as expected; nm-1.AC2 FAIL (no rivalfunds.names) as expected; nm-1.AC3 FAIL (no module; controls unreachable) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~5</slot>
<fabric>site-z</fabric>
