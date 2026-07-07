# ADVI_ETLFIX WS-3 -- MDPF custody flip close-out: Req-1 FAILS, re-freeze found, STOPPED per mandate

**archetype:** DIAGNOSE
**secondary_archetypes:** VALIDATE, COORDINATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL | **TO:** ADVI_ETLFIX.WS3 (COO DRIVE 132713Z, status=pending)

## Outcome
COO dispatched WS-3 as a close-out/hardening pass on the 07-02 MDPF custody flip (bd -> schwab-native,
commit 12dd979c7). Ran the TO's compiler_tools_mandate live. Reqs 2/3/4 were already substantively done
07-02 (CVO parity cert + ledger CLOSE + GATE-3 pattern doc). **Req 1 (3 consecutive post-flip nightly
advances) FAILS** -- the custody figure has been frozen since the flip, masked by an advancing wrapper
`as_of_date`. Invoked the mandate's own STOP clause: escalated to COO, did NOT close anything.

## Grounding (live, not self-report -- Rule 22/22a)
1. **Raw Schwab landing** `s3://opal-data-schwab/01_raw/`: latest file = `CRS20260701.*` (landed
   2026-07-02T11:04Z). No `CRS20260702/0703/0706/0707` -- zero new raw Schwab deliveries in 5 calendar days.
2. **Schwab silver RPS** `s3://opal-data-bd/schwab/silver/rps/`: 619 `date=` partitions total, latest
   `date=20260701`. No partition past 07-01.
3. **MDPF non_model_aua feeder** `s3://opal-data-mdpf/mdpf/feeds/non_model_aua/49financial/`: only 2
   post-flip files exist, `2026-07-02.parquet` and `2026-07-06.parquet` (07-03 is the observed Jul-4
   holiday + weekend, expected gap). Pulled both, compared field-for-field:
   - `partner_custody_total`: **$1,604,173,986.44 in BOTH** -- byte-identical.
   - `model_aua_input`: $1,386,552,xxx (07-02) -> $1,400,958,xxx (07-06) -- legitimately moved.
   - Confirms the custody figure specifically (the entire point of the flip) has not moved since the
     flip fired, while the rest of the pipeline continued to run and advance its own `as_of_date`.

**Mechanism (source-grounded, not inferred):** `build_mdpf_wse_49f_non_model_aua.py`
`_latest_rps_partition()` resolves the latest `date=` partition under `schwab/silver/rps/` -- with no
partition past 07-01, every run since resolves the same `rps_date=20260701` and recomputes an identical
custody total. The only runtime guard is a value-magnitude sane-band fail-closed (lines ~165-171,
813-832) -- a frozen-but-plausible number stays in-band and passes. **No staleness-ceiling exists on
`rps_date` itself** -- the AC6 staleness-ceiling from the GATE-3 basis-move-protection-gate pattern
(`a29b5d4f5`/`910c18b2c`, CTO-arch-blessed 07-02) was authored as a **pattern description**, not yet
wired into this script. This is the exact mtime-fresh/content-stale class the 06-25 freeze P0 was about,
recurring silently behind an advancing wrapper timestamp.

## Cross-check -- not a fresh discovery, already routed on WS-2's side
`get_agent_status(0.6.2_AE_PartnerETL)` -- their 07-06 logs cite "Schwab 07-02 conv" as still
delivery-gated: blocked on an `s3:PutObject-on-bronze/*` IAM grant landing before tonight's run, sentinel
emit, then silver roll (`/49-schwab-conv when 07-02 lands`). So WS-2 ingest health -- the TO's own stated
gate for Req 1 -- is the actual blocker, not something closeable from the WS-3/AE_OpalETL side.

## Action taken
Escalated to COO (`20260707T140231Z`) with full grounding, recommending WS-3 stay open pending WS-2's
raw-delivery resume (or priority escalation if this needs 06-25-P0-level urgency). Did not touch the
MDPF flip deploy-completion ledger (already CLOSED 07-02, `3694b94d0` -- correctly reflects that day's
state; today's finding is a NEW recurrence, not a stale closure). Did not mark WS-3 complete.

## Compiler Tools
| Tool | Result | Pass/Fail vs `<expect>` |
|---|---|---|
| `comp-to ADVI_ETLFIX.WS3.mdpf-custody-flip-close` | OK -- session TO_ID set | n/a (setup) |
| `comp-freshness artifact s3://opal-data-portal-v2/json/mdpf/aggregate-aua-timeseries.json` | PASS, content as_of 2026-07-06, 1td behind frontier | Tool has no `mdpf`/`--history` shorthand (TO's literal invocation string doesn't match the actual CLI, corrected to `artifact <s3_key>`); single-snapshot PASS **did not** surface the frozen-value finding -- content-mode as_of alone is insufficient, had to read the underlying feeder parquet values to catch the freeze. **FAIL vs the mandate's intent** (mandate expected this step alone to gate re-open detection; it does not -- flagging as a tool gap) |
| `comp-pipescript io schwab_native_ingest` | NOT-FOUND (`schwab_native_ingest` isn't a registered script ID; `comp-pipescript io` only resolves BD-gold IDs A_00..S_00) | Mandate's literal script name doesn't exist; used `comp-grep`/direct source read instead (rail-checked -- comp-pipescript io has no MDPF-script coverage) |
| `comp-blast build_mdpf_wse_49f_non_model_aua` | "No downstream consumers found -- no EXTRACTED edge -- NOT provably zero" (graph coverage gap, dynamic/FUNC-key reads not edged) | No NEW undeclared consumer surfaced (satisfies mandate intent), but tool gives no positive confirmation -- graph does not cover MDPF's dynamic-prefix consumption pattern |
| `aws s3 ls` (01_raw, silver/rps, mdpf/feeds) -- rail-checked, no comp-tool covers historical per-date partition/object enumeration (comp-freshness is current-snapshot-only) | Grounded the actual re-freeze (see above) | This is what actually caught the finding the two comp-tools above did not |
| `get_agent_status(0.6.2_AE_PartnerETL)` | Confirms WS-2 blocker already routed (IAM grant + tonight's run gate) | Cross-domain coordination check (TO's WS-2 dependency note) |

**Tool-gap note for the record:** neither `comp-freshness` (single current-snapshot, content-mode PASS)
nor `comp-blast` (no MDPF graph coverage) would have caught this re-freeze on their own. The mandate's
step-1 `comp-freshness` PASS looked clean; only reading the actual feeder parquet field values across two
dates surfaced the frozen custody total. Worth a COMPDEBT/graph-coverage note: MDPF scripts are not
graph-extracted, and `comp-freshness`'s content-mode as_of check doesn't catch "value repeated, wrapper
date advanced."
