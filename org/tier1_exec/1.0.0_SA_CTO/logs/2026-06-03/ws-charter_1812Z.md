# ws-charter cycle:0024 — 2026-06-03 1812Z

**archetype:** VALIDATE
**Agent:** 1.0.0_SA_CTO (ws CTO). **Class:** FIX (architectural ratification nod). **Trigger:** off-cycle /ws-charter (Andrew-fired) + COO DRIVE_ESCALATION inbox.

## Inbox

- **DRIVE_ESCALATION (COO):** NFRA decomposed → RATIFICATION ASK on profiler swap (gold_prof.py → runner-telemetry) on bd gold_dispatch; time-boxed by tonight's nightly. → ACTIONED (nod below). Inbox now empty.

## Action — NFRA profiler-swap NOD (FIX-class architectural ratification)

NODDED the swap. Verified before nodding (not a rubber-stamp):

1. **Observational, not data-path.** `gold_prof.py` is invoked as a measurement wrapper at `gold_dispatch.sh:245` (`python3 gold_prof.py <script> <flags>`); `runner-telemetry.py` is the same role — `subprocess.Popen(cmd)` (`.tools/runner-telemetry.py:394`, `-- <cmd>` REMAINDER). The profiler does NOT sit on the data-correctness path. Worst case of a bad swap = wrong telemetry, never wrong gold data → makes "validate free on the scheduled nightly" architecturally safe (zero data-integrity exposure).
2. **PSS is the correct metric.** tree-summed RSS CoW-inflates (forked workers share parent pages; RSS counts shared pages per-worker → phantom TB peaks on a 128GB box). PSS counts each physical page once split among sharers = true footprint. Fix `fe907a974` is right.
3. **Consolidation kills silent-asymmetry.** Both profilers carried the RSS defect; collapsing to one canonical fixed wrapper + `gold_prof` PSS-parity-or-deprecate as NFRA.W2(b) prevents the fix-one-leave-the-other-defective failure mode.
4. **Cost-discipline aligned.** Validate-on-scheduled-nightly = zero extra compute, exactly Andrew's standing NFRA constraint (no manufactured gold runs; ref `memory/feedback_no_adhoc_gold_runs_validate_on_scheduled_nightly`).

### Conditions on the nod (AE-side RAVC deliverables; none block tonight's deploy)
- (a) Wrapper-only swap; wrapped gold script executes byte-identically; DRY_RUN/chain-label/chain-exit semantics unchanged.
- (b) Telemetry-output contract gate: runner-telemetry's per-script record + analyze output must land where perf_report reads (else empty perf_report tomorrow — telemetry miss, not data miss). Confirm tomorrow: PSS + sys_mem sane (~1.2GB/128GB, not phantom-TB) + p5/median/mean/p95.
- (c) `gold_prof.py` disposition NFRA.W2(b) DS lane: PSS-parity-or-deprecate; stub/pointer if deprecated so no caller silently gets RSS.
- (d) Normal deploy cycle (commit → push → S3 → `comp-pipescript deployed` MATCH); NO ad-hoc gold run.

**RAVC close:** I release on tomorrow's nightly perf_report showing PSS/sys_mem populated + sane. MCPs sent to COO (`20260603T181151Z`) + 0.6.0 (`20260603T181159Z`), CC 0.7.0.

## Project-state-sweep (affirmative)

origin/CLOUD fetched @ `6d4c9f9c0` (COO drive-tick 16). State:
- v2.1.114 — DT PRE-STAGED byte-identical, **Andrew-GO-ready** (`298ca25c8`). Not CTO-blocked.
- PMTRDX.001 — RD~B committed/handed-to-AE (`a2c246475`); awaiting AE deploy + CVO e2e.
- NFRA W2a/b — in motion (0.6.0 deploy-tonight per this nod; DS coordinating W2b).
- ADHC_KEEPWARM Lanes A/B — ride v2.1.114.
- **CVO dark since ~18:04Z** — COO routed MSTR `[SYNC]` (tick 16, <30m fresh). Blocks 3 CTO-side legs (PMTRDX close-gate / render-smoke / CMPAWS hand-audit). MSTR-scope (HARD-BLOCK #8); not redundantly re-MCP'd this tick. Escalate next tick if still dark + a CTO-gated close is ready.

No REPAIR-AMENDMENT (no CVO finding). No NOVEL (no Andrew new-PRD direction). No CVO_CONSULT (no Andrew-silent fork).

## Next-cycle expected state

NFRA deploy lands tonight → tomorrow's nightly = free validation. v2.1.114 awaits Andrew GO. PMTRDX + render-smoke + CMPAWS unblock when CVO returns live. Next cron tick 30m.
