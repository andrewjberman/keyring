# DS~B Session Summary -- 2026-05-21

**Agent:** 0.4.0_DS_ClientPlatform~B
**Branch:** CLOUD
**Lane:** ~B (orders from ~B-serialized agents only)

## Headline

Closed out the MDPF v0.9 historical line. The `.032` 1c-source probe found
`.031`'s `1c=0` was a wrong-source artifact; the `.031` A4 re-run corrected it
on CTO~B's ruling; **MDPF_ASSETS the project is 3-step CLOSED** (commit
`459fdba3c`). The v0.9 line `.027`-`.031 A4` is fully landed.

## Task orders worked

### MDPF_ASSETS.032 -- 1c (SMA) source probe -- COMPLETE/CLOSED
- Non-mutating read-only probe. Found the authoritative SMA source is the
  SmartX `enterprises/allocations` endpoint (the WS-B feeder's per-model
  roster path), NOT the consolidated store `.031` item-(d) probed.
- SMA real across both ranges; program launch positively pinned **2021-09-02**
  (earliest SMA allocation `openedDate`) -- OUTCOME (a): `.031`'s `1c=0` is
  WRONG. Routed to CTO~B for the 1c-method ruling.
- Brief: `docs/briefs/mdpf-assets-032-1c-sma-source-probe-20260521.md`
  (commit `3308f0d34`).

### MDPF_ASSETS.031 A4 -- 1c re-derive + 297-partition re-run -- COMPLETE/RAVC-accepted
- Per CTO~B's `.032` ruling: re-derived `1c` for all 297 `.031` partitions
  from `0` to flat **$19,673,469.29** (the `.031/.029` seam anchor), on the
  SMA program's own trajectory (not 1a-coupled). Recomputed
  `1b = calibrated_Schwab - 1a - 1c`.
- `.029` quick-check: stored ratio-1c within ~$1.5M of an independent
  upper-bracket SMA estimate -- in tolerance -> `.029` stands, no re-open.
- Premise correction surfaced + acknowledged by CTO~B: flat is chosen because
  the SMA per-date value is genuinely unrecoverable (95/189 allocations
  closed, no close-dates, no historical values), NOT because "SMA is mature."
- Applied to S3 (297 partitions + the rollup rebuilt). Verified all-pass:
  1c flat 297/297, identity 0 breaks, 0 negative 1b, AC1 daily-per-model
  297/297, **1c component-seam CLOSED ($0.00 step)**, **headline invariant**.
- RAVC2 -> COO~B CC CTO~B. CTO~B output-validation ACCEPT + COO~B independent
  S3 re-validation PASS. Brief:
  `docs/briefs/mdpf-assets-031-a4-1c-rerun-ravc2-20260521.md` (commit
  `156223c36`). `.031` re-closed; MDPF_ASSETS project closed (`459fdba3c`).

## Other

- **Registration repair:** discovered the MCP `set_summary`/`heartbeat`/
  `get_agent_status` tools strip the `~B` suffix and operate on the BASE
  serial -- an earlier `set_summary` had overwritten the base
  `0.4.0_DS_ClientPlatform` session's summary. Caught via `get_live_agents`,
  restored the base summary, set the `~B` summary via `register_agent` (which
  respects the full serial). Memory saved:
  `reference_mcp_tilde_serial_set_summary_strips_suffix`.
- **inbox-watch.sh:** health-checked on the `/loop` cadence; restarted once
  after the watcher process (PID 723400) died -- now PID 778668, full path,
  PPID=1, detached.

## Memory written this session

- `feedback_mdpf_historical_backfill_use_existing_daily_artifacts`
- `feedback_surface_phase_artifacts_during_execution`
- `feedback_walk_components_across_backfill_seam`
- `reference_mcp_tilde_serial_set_summary_strips_suffix`

## Compiler Tools

`build_aggregate_aua_timeseries.py` run unmodified (`--upload`) to rebuild the
portal-consumed rollup from the corrected S3 partitions. The `.031` backfill
is a one-time data re-materialization via `.runtmp` scratch scripts (gitignored)
-- no `data/*/scripts/` producer changed, so Rule 13/14/15 deploy/commit gates
did not apply to the re-run itself.

## Current State

MDPF_ASSETS CLOSED -- the final MDPF TO landed. DS~B lane idle/watchdog: no
pending DS~B TOs. The remaining `~B` book (ADHC_VALGATE Phase 2/3,
TRSB_LEDGER `.012`) is Andrew-gated -- nothing dispatchable. On `/loop`
watchdog standby; COO~B surfaces the lane when `~B` DS work opens.
