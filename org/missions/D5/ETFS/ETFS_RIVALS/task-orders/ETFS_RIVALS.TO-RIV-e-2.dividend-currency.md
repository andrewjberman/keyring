# ETFS_RIVALS task order -- `RIV-e-2` -- ROUND 6 (ENRICHMENT): DIVIDEND CURRENCY (analysis cell 5, W3-S11)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-e-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-02 ~15:2xZ, --drift) -- carrier C1: 31 sentinels scanned, 12 gates armed, none names rivalfunds/, etfs-rivalfunds or this cell's files; C2-C5 not scanned inside the 90 s budget (blind there); the notifier moratorium binds.
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work for the L8/L9 packet; at the cut nothing is returned, and the issuer's evidence context is this order's check files
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, the A1 rankings, buying trend, input census and AI accounts, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg the vehicle runs from the CLOUD working tree). **Round 6** makes the A1 tables follow their inputs, puts the AI accounts into the scheduled path, adds the plausibility guard, fixes dividend currency and exit pricing, gives the census three states and the page real names, and carries the 33-item page walk (PRD v0.12). Nothing in round 6 deploys from a worker. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-e-2` -- dividend currency (analysis cell 5; W3-S11; W3-S12 waits on I-2's probe)
- `DVD_CRNCY` joins the dividend request: the OFFLINE plan's `fields` list it beside `DVD_HIST_ALL`.
- `rows_from_responses` fills G3 `currency` from a security's `DVD_CRNCY`, NULL when absent.
- `gold_trade_schedule.dividend_ccy(security_key, g3_currency) -> (ccy, source)`: the G3 currency wins ("g3"); otherwise the
  suffix table answers, labelled "suffix_table", with the LN/SJ/IT mixed-unit rule unchanged. G5's income conversion uses
  it.
- W3-S12's child identity is code only after I-2 names a field.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- `enrichment_bloomberg`: FIELD 'DVD_HIST_ALL' (~77); plan mode returns `{fields, start, end, overrides, batches}` (~10-11, `handler_entry` ~506); `rows_from_responses(data, as_of, provenance)` (~160) leaves `currency` NULL today.
- `gold_trade_schedule`: SUFFIX_CCY (~148), MIXED_UNIT_SUFFIX LN/SJ/IT (~159), the conversion at ~492 (`ccy = BASE_CCY if sfx in MIXED_UNIT_SUFFIX else SUFFIX_CCY.get(sfx)`).
- This file is ALSO run by the terminal vehicle from the CLOUD tree (the 08:03 enrichment step): the daily pull must keep landing; never call Bloomberg.
- AMENDMENT A1 (issuer, 2026-10-02 ~17:3xZ): the issuer's live DVD_CRNCY read (6 securities) returns Bloomberg MINOR units for some listings: BATS LN -> `GBp` (pence), NPN SJ -> `ZAr` (rand cents); SHEL LN and TEVA IT -> `USD`; ASML NA -> `EUR`; 8306 JP -> `JPY`. As built, a G3 `GBp` wins and has no `GBp Curncy` rate, so pence dividends read UNCONVERTED. Make G5's income conversion read a minor-unit code at its major currency's rate divided by 100: GBp and GBX -> GBP/100, ZAr and ZAc -> ZAR/100, ILs and ILa -> ILS/100. A major currency keeps its own rate. The label `dividend_ccy` returns may stay "g3". AC4 below uses test_g52's fixture.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6e2_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r6e2_*.py
data/etfs/scripts/rivalfunds/tests/test_e1_enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- the offline plan's fields list DVD_CRNCY beside DVD_HIST_ALL (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC1.py`)
- **AC2** -- G3 currency comes from DVD_CRNCY; NULL without it (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC2.py`)
- **AC3** -- dividend_ccy: a G3 currency wins ('g3'), the suffix table answers labelled 'suffix_table', the LN/SJ/IT base rule kept (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC3.py`)
- **AC4** -- (a fourth criterion; reason: amendment A1, Bloomberg's minor-unit codes) GBp/GBX and ZAr/ZAc dividends convert at GBP/100 and ZAR/100; control: a major currency (USD, JPY) converts at its own rate (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC4.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-e-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-e-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-e-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC4" cell_refs="RIV-e-2"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/e-2.AC4.py</invocation><expect>AC4 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-e-2.dividend-currency.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-e-2.dividend-currency`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~3`, slot `~3`, position 1 of 2 (e-2 -> x-1). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
e-2.AC1 FAIL (control DVD_HIST_ALL OK) as expected; e-2.AC2 FAIL (control NULL OK) as expected; e-2.AC3 FAIL (no dividend_ccy) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>6</round>
<slot>~3</slot>
<fabric>site-z</fabric>
