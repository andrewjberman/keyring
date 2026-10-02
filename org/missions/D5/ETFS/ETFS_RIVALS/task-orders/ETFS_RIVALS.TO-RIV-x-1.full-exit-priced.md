# ETFS_RIVALS task order -- `RIV-x-1` -- ROUND 6 (ENRICHMENT): A FULL EXIT IS PRICED (RFW-D10)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-x-1</owned_cells>
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

### `RIV-x-1` -- a full exit is priced (RFW-D10)
- Measured at the cut: an exit whose line is ABSENT from the later report is already priced and only lacks a label. The served
  "n/a" comes from a line KEPT AT QUANTITY 0 in the later report, which today reads `trim` with no price or notional (TXUE
  ATD_CN_Equity 138,182 -> 0).
- An exit is a line with prior quantity above 0 that is absent from the later report OR at quantity 0 there. It reads action
  `exit`, `est_price` = the prior market_value / the prior quantity, and `est_notional` = `est_notional_base` = minus the prior
  market_value. A new G5 column `est_price_source` (in `SCHEMA` and `COLUMNS`) reads "prior_valuation".
- A line with prior quantity 0 is never priced this way. A 0->0 row (CRO CALL 12) stays as today.
- A trim or an add keeps today's values exactly.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin))

- Measured at the cut: an ABSENT-line exit is already priced (-50,000 / 50.0) and lacks only the label; a line KEPT AT 0 reads `trim` with no price or notional (served TXUE ATD_CN_Equity 138,182 -> 0, the 'n/a' cells).
- Add `est_price_source` to `SCHEMA` and `COLUMNS` (do not reuse `est_price_band_reason`).
- AMENDMENT A1 (issuer, 2026-10-02 ~16:3xZ): first, disarm row ETFS_RIVALS-Z-W3-S20. RIV-e-2 (this slot's previous order) changed the daily dividend request to `["DVD_HIST_ALL", "DVD_CRNCY"]`, and `tests/test_s4_security_market.py` still pins `fields == ["DVD_HIST_ALL"]` at lines ~153, ~160 and ~171 (2 tests fail). Change those three comparisons to the new list and nothing else; the file is granted below. Then set the row's state to RESOLVED in the investigation file, citing your commit.

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/` and round 5's `.../round5/checks/`, the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.12), the walk brief `docs/briefs/rivalfunds-ui-data-walk-20261002.md` and its register `docs/briefs/rivalfunds-ui-data-findings-20261002.json`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-6 chain owns, and none of the merge hookups the decomposition names (the issuer adds them). Tests go beside the code as `tests/test_r6x1_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed). A check you cannot satisfy without leaving your `<paths>` is a surprise row in the investigation file, never an edit outside them.

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_r6x1_*.py
data/etfs/scripts/rivalfunds/tests/test_g2_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
data/etfs/scripts/rivalfunds/tests/test_s4_security_market.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- a line kept at quantity 0 and a line absent from the later report are both exits priced from the prior valuation (50.0 / -50,000), labelled prior_valuation (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC1.py`)
- **AC2** -- control: trims and adds equal today's output exactly (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC2.py`)
- **AC3** -- control: 0->0 rows stay exit with no price or notional; a line at 0 on both reports produces no row (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC3.py`)

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-x-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-x-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-x-1"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round6/checks/x-1.AC3.py</invocation><expect>AC3 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-x-1.full-exit-priced.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-x-1.full-exit-priced`. Report once: each mechanical criterion's verdict line with the output above it; each judgment criterion left UNVERIFIABLE-BY-INSTRUMENT for the CVO; files written; any existing test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-5 analysis @56c99763bb (msg 28485) section 4 + PRD v0.12 @afc2bed44f
(RFW register, msg 28535); decomposition round 6 v1.0; Andrew-direct "/canonical-drive with max parallelization on
subagents" (cooRV record 141xZ). Chain `~3`, slot `~3`, position 2 of 2 (e-2 -> x-1). Checks dry-run at base CLOUD bdbd7a257b (rv-fast; package unchanged since 722f0db291, the deployed pin):
x-1.AC1 FAIL (4) as expected; x-1.AC2 PASS (control) as expected; x-1.AC3 PASS (control) as expected.

<risk>SERVED</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>6</round>
<slot>~3</slot>
<fabric>site-z</fabric>
