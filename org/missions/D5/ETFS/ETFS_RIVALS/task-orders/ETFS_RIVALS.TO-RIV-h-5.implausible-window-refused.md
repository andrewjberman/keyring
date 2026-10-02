# ETFS_RIVALS task order -- `RIV-h-5` -- ROUND 5 (ENRICHMENT): AN IMPLAUSIBLE WINDOW IS REFUSED, NEVER INFERRED (HOP-9 b)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-h-5</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~3</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (2026-10-01 ~23:xxZ, --drift) -- no armed gate names rivalfunds/, issuer-site/etfs/, bloomberg/etfs/ or this cell's files; the notifier moratorium binds.
comp-iam: RUN at L5 -- no IAM change in this cell.
comp-adversary: RUN at L5 on the round-5 decomposition; declared on RIV-b-2 and RIV-l-1, not this cell.
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric site-z) -- *rivalfunds*: daily holdings of rival active ETFs in two peer groups (IDVZ, PFOE), each fund's trade schedule, and a served page grouped by Opal fund (13 funds, package `data/etfs/scripts/rivalfunds/`, five AWS stage Lambdas, a terminal-machine Bloomberg leg run by the vehicle from the CLOUD working tree). **Round 5** bounds G1, fixes three trade-inference method defects (CTO hop-9 rulings), makes the issuer floor per fund, and builds the v0.8 Bloomberg leg inert. Nothing in round 5 deploys. Work ONLY in the worktree your spawn line names; every path below is relative to that root.

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-h-5` -- an implausible window is REFUSED, never inferred (hop-9 ruling b; after h-4 on `~3`)

**Refusal rule.** A fund-window is refused when either holds:
- the flow factor f lies outside `flow_factor_band`;
- the share of its non-cash lines with quantity 0 on either side exceeds `max_zero_quantity_share`.

**Thresholds.** Both live in `guardrails_config.json` as PROVISIONAL: `flow_factor_band` value `[0.5, 1.5]`,
`max_zero_quantity_share` value `0.2`.

**What a refused window serves.**
- A G6 row gains `status` (`REFUSED`, or empty) and `reason` (`flow_factor_out_of_band` | `zero_quantity_share`).
- The window infers ZERO trades.
- The same rule runs on the daily, backfill and replay paths, so a refused window cannot reach served trades by any path.

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base 9e201639c3)

- Flow factor (`gold_trade_schedule.py` ~425-428): `f = median(b[k]["q"] / a[k]["q"])` over unchanged positions, unbounded;
  used only for `flow_adj` (FLOW-WINDOW confidence). Zero-quantity lines are never counted (a d1 q=0 line becomes a trim).
- G6 recon dict ~542-556; `gold_flow_reconciliation.SCHEMA` (~49-63) has no `status`/`reason`. `infer_recon(df)` returns a
  DataFrame with `g6mod.COLUMNS`.
- Replay (`run_stage` ~739-788) writes G5/G6 with no guardrail; the page runs `guardrails` only in `publish_page`.
- `guardrails.load_config` (~39-66) requires every threshold PROVISIONAL and the override env refuses unknown names -- the new
  thresholds go in `guardrails_config.json`.
- Measured on served G1: INEQ 2025-08-28 -> 08-29 f = 0.0 with 100 inferred trades; TXUE 2025-04-11 -> 04-14 f = 83.0 with 25
  (the ruling's acceptance cases; also TSEL 2025-01-16, INEQ 2025-11-28).

## 3. SURFACES AND BOUNDS

You READ (never edit): `lib/`, `integrations/bloomberg/` (the Positioning pull is under an Andrew-direct no-modify order), the package's other modules and tests, `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round{3,4,5}/checks/`, the CTO rulings `org/missions/D5/ETFS/ETFS_RIVALS/ledger/CTO_RULING_20261001_HOP9_METHOD_DEFECTS.md` and `org/missions/D5/ETFS/ETFS_RIVALS/ledger/ROUND_ANALYSIS.round4.md`, the device-local captures under `C:\Users\Opal Bloomberg\Desktop\ajb_workspace\.runtime\`, and live S3 READ-ONLY where a check reads it.

You WRITE only the `<paths>` below (plus `deliverables/0.9.0_WK_ETFS_RIVALS~3/`). NEVER: any S3 write, any deploy, any Bloomberg or OpenAI call (stub every vendor hook in tests), the vehicle, any file another round-5 cell owns. Tests go beside the code as `tests/test_r5h5_*.py`, run with `python -m pytest <file> -q` from `data/etfs/scripts/`; run the whole package suite before you report (it must read 0 failed).

<paths>
data/etfs/scripts/rivalfunds/gold_trade_schedule.py
data/etfs/scripts/rivalfunds/gold_flow_reconciliation.py
data/etfs/scripts/rivalfunds/guardrails_config.json
data/etfs/scripts/rivalfunds/tests/test_r5h5_*.py
data/etfs/scripts/rivalfunds/tests/test_g2_trade_schedule.py
data/etfs/scripts/rivalfunds/tests/test_g52_trade_schedule_v2.py
data/etfs/scripts/rivalfunds/tests/test_g6_*.py
data/etfs/scripts/rivalfunds/tests/test_p1_page_and_guardrails.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from your worktree root)

- **AC1** -- config carries flow_factor_band [0.5,1.5] and max_zero_quantity_share 0.2 PROVISIONAL; f=1.8 and a 50% zero window are REFUSED with 0 trades; control f=1.037 infers its trade (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-5.AC1.py`)
- **AC2** -- on SERVED G1 (READ-ONLY), INEQ 2025-08-29 and TXUE 2025-04-14 are REFUSED with 0 trades; control: INEQ's previous window is not (`org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-5.AC2.py`)

**Time bound (fabric ruling 9):** `h-5.AC2` read a whole window or a 50-date fixture: run it under `timeout 600`, not 120. rc 124 is a timeout, never a FAIL; report it as such.

<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-h-5"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-5.AC1.py</invocation><expect>AC1 RESULT: PASS 0 failures</expect></criterion>

  <criterion id="AC2" cell_refs="RIV-h-5"><invocation>python org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round5/checks/h-5.AC2.py</invocation><expect>AC2 RESULT: PASS 0 failures</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~3/ETFS_RIVALS.TO-RIV-h-5.implausible-window-refused.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-h-5.implausible-window-refused`. Report once: each criterion's verdict line with the output above it; files written; any test assertion changed and why; rows filed (id + one line). Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L5/L6, 2.0.0_SA_COO~RV):** Round-4 analysis @6dcb0074e4 (msg 28075), decomposition round 5 v1.0. Checks dry-run
at base 9e201639c3: h-5.AC1 FAIL, h-5.AC2 FAIL -- each FAIL as expected, each control PASS.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>staged</status>
<round>5</round>
<slot>~3</slot>
<fabric>site-z</fabric>
