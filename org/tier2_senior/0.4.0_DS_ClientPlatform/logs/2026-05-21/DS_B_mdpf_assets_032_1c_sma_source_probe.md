# DS~B Session Log -- MDPF_ASSETS.032 (1c SMA-source probe)

**Agent:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-05-21
**Branch:** CLOUD
**TO:** MDPF_ASSETS.032 -- 1c-source probe (sole blocker on the MDPF close)

## Summary

Read-only probe resolving the .031/.029 1c contradiction. Finding: OUTCOME (a)
-- SMA is real across both historical ranges; .031's 1c=0 is wrong.

## Probe

- **Phase 1 -- authoritative source:** the SmartX live API endpoint
  enterprises/allocations?modelid={model_id} (the WS-B feeder's per-model
  roster path), NOT the consolidated store. Confirmed: it returns 94 open SMA
  allocations / ~$24.77M -- matches the .028 1c ($24.93M/94, modulo a day's
  market move).
- **Phase 2 -- SMA presence:** opal_div_sma 118 allocations (earliest opened
  2021-09-02); opal_growth_sma 71 (earliest 2024-08-08). 82 SMA allocations
  open entering the .031 range; 173 entering the .029 range. SMA real, non-zero,
  throughout both ranges.
- **Phase 3 -- launch pin:** 2021-09-02, the earliest SMA allocation
  openedDate (opal_div_sma) -- a positive data pin, 3+ years before the .031
  range. Not a boundary inference.
- **Phase 4 -- OUTCOME (a):** SMA real both ranges -> .031's 1c=0 is WRONG.
  item-(d) probed the consolidated store, which doesn't track the SMA models
  -- a wrong-source artifact. .029's ratio-1c stands; .031's 1c+1b re-derive
  + the 297 partitions re-run, per a 1c method CTO~B rules.

## Files / artifacts

| Artifact | Detail |
|----------|--------|
| docs/briefs/mdpf-assets-032-1c-sma-source-probe-20260521.md | the probe finding -> CTO~B CC COO~B |
| .runtmp/mdpf032/sma_source_probe.py | the probe script (read-only; ad-hoc, not a pipeline producer) |

## Non-mutating

Read-only -- no partition rewritten, no producer changed, no S3 write. A brief
is the deliverable.

## Compiler Tools

| Tool | Result |
|------|--------|
| ds-commit-gate.sh | N/A for the probe script (.runtmp ad-hoc, not committed as a producer); the brief + log are .md |
| (probe) | direct SmartX-API read -- enterprises/allocations per SMA model_id; cross-checked vs the .028 94-account/$24.93M figure |

## Current State

MDPF_ASSETS.032 COMPLETE -- outcome (a) routed to CTO~B CC COO~B. On CTO~B's
1c-method ruling, .031 re-runs with the corrected 1c -> .031 re-closes ->
MDPF_ASSETS closes.

## Next

| Recipient | Item |
|-----------|------|
| CTO~B 1.0.0 | the probe finding + the 1c-method ruling (the TO outcome (a) fix). |
| COO~B 2.0.0 | CC; relays the ruling; on the .031 re-run, the MDPF close. |
