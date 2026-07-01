# MDPF-Daily-Trigger Re-Point — gate on schwab/silver/rps freshness (for CTO arch-gate)

**Author:** 0.5.0_AE_OpalETL (mdpf-infra) | **Arch-gate:** 1.0.0_SA_CTO | **Verify:** 3.0.0_SA_CVO | **Deploy:** AE (Terraform, mdpf-pipeline)
**Part of:** MDPF 49F custody Schwab-native basis switch (design brief `mdpf-49f-custody-schwab-native-basis-switch-design-20260701.md`). This is the trigger-gate leg (pipescript-caught coupling); DS owns the WS-E swap in parallel.

## Why (CTO requirement)
`mdpf-daily-trigger` is the convergence gate: it fires on the INF spine sentinel, verifies freshness, then dispatches the runner. Today its 49F freshness check is `_check_bd_silver` over `silver/{allocations,fees}` (env `BD_SILVER_PREFIXES`, lambda_function.py:55). Under the basis switch, **the served 49F custody comes from `schwab/silver/rps`, and `silver/fees` becomes vestigial (its freeze was the 6-day break).** A gate still keyed on `fees` freshness is a FALSE SIGNAL — it would DEFER on a frozen-but-now-irrelevant input, OR pass while the actual RPS source is stale. **Re-point the gate to gate on the freshness that actually feeds the served number: `schwab/silver/rps`.** (CTO: "a trigger on the wrong freshness = a freshness false-signal.")

## The change
Replace the `_check_bd_silver` (allocations/fees) freshness check with a `_check_schwab_rps` freshness check. Three grounded specifics:

1. **Prefix/source:** `schwab/silver/rps` on `opal-data-bd` (the new custody source-of-record; env `SCHWAB_RPS_PREFIX`, default `schwab/silver/rps`). Retire `BD_SILVER_PREFIXES=silver/allocations,silver/fees` from the gate (they no longer feed the served custody).

2. **LAYOUT WRINKLE (the real work, not an env swap):** `_latest_bd_silver_partition` (lambda_function.py:122) parses **`{YYYY-MM-DD}.parquet` flat basenames**. `schwab/silver/rps` uses **`date=YYYYMMDD/` partition DIRECTORIES (compact date)** — a different layout. So the partition reader needs a schwab-RPS variant: list `s3://opal-data-bd/schwab/silver/rps/`, parse `date=(\d{8})/` keys, `datetime.strptime(m, "%Y%m%d")`. (Same shape the RPS converter's `already_converted()` uses.)

3. **Weekday cadence PRESERVED:** Schwab RPS is ALSO weekday-only (grounded this switch: 06-27 Sat / 06-28 Sun have no CRS delivery; 06-26 Fri, 06-29 Mon, 06-30 Tue are the real dates). So the existing `expected_last_trading_day` + `trading_days_behind` + `BD_MAX_LAG_TRADING_DAYS` logic (lambda_function.py:102-119) carries over UNCHANGED — RPS is "fresh vs its own weekday cadence," same as BD silver was. Do NOT reintroduce a weekend-expected bug. Reuse the trading-day helpers verbatim.

## What stays
- `_check_inf_spine` (INF daily freshness) — unchanged (the sentinel + INF spine are basis-independent).
- The dispatch path (mdpf-daily-dispatch.sh + the 6 scripts + mdpf_aggregate_aua) — untouched.
- `GATE_ENFORCE` defer-on-stale + the `mdpf-freshness-checker` alarm backstop — unchanged.
- `lambda_handler` (208): `gate = inf.fresh AND schwab_rps.fresh` (swap `bd` -> `schwab_rps` in the all_fresh compose + the decision log key `49financial`).

## SEQUENCING (critical — coordinate with the WS-E swap)
The trigger re-point + the DS WS-E swap must land TOGETHER (or trigger-first): the moment the served custody reads RPS, the gate must gate on RPS. Landing the trigger re-point while WS-E still reads BD = the gate passes on RPS-fresh but the served number uses the frozen BD (no un-freeze); landing WS-E while the trigger still gates on frozen `fees` = WS-E ready but the gate DEFERS forever (never dispatches). **Recommend: deploy the trigger re-point + WS-E swap in one coordinated activation** (COO sequences; CVO verifies the first post-switch run both dispatches AND serves RPS).

## Test
Adapt `test_convergence_gate_weekend.py` for the RPS layout (`date=YYYYMMDD/` fixtures) + confirm the weekend-cadence assertions hold (Fri RPS is "fresh" through the weekend; a genuinely-stale RPS DEFERS). CVO live-verify: the first post-switch trigger fire dispatches on RPS-fresh + the served aggregate advances.

## Arch-gate ask (CTO)
Confirm: (a) gate ONLY on `schwab/silver/rps` (custody source), or ALSO add a WS-B `model_aua_positions` freshness check (the model/sma inputs to the residual)? My rec: RPS-only for the gate (the custody is the basis-switch's new dependency; WS-B/INF freshness is separately handled + basis-independent), but flag if you want the residual-inputs gated too. (b) the layout-variant partition reader is correct. On GO, I implement + Terraform-deploy the mdpf-daily-trigger, coordinate the co-activation with DS's WS-E swap.

*Grounded 2026-07-01 against infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py (:55/:102-119/:122/:158/:208) + schwab/silver/rps layout. Author: 0.5.0_AE_OpalETL.*
