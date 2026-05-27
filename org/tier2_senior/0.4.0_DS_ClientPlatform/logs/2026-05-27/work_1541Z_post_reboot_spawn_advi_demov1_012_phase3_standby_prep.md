# Post-reboot spawn — ADVI_DEMOV1.012 Phase 3 STANDBY-PREP

**archetype:** COORDINATE+SCRIBE
**date:** 2026-05-27
**spawn:** MSTR `[SPAWN-WITH-DIRECTION]` 2026-05-27T15:33:28Z per ws COO /drive #165 ALLOCATION-REQUEST 1531Z (LD-0107-class Fix-3 canonical fire #5 — MED priority parallel pickup pair to AE 0.7 HIGH)
**TO ref:** `org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_DEMOV1.012-completeness-calibration-instrumentation.md`
**Posture:** STANDBY-PREP — AC1 mine shipped pre-reboot `8de9c5415` 09:58Z; AC2 Fire 1 AE-lane in-flight `5caba4eb` (ETA 17:30-18:30Z terminal)

## Cycle actions
1. `/watcher` ran clean — registered LIVE, watcher PID 27473 tracked task `bmnepzhk1`/`b9ebr7r0t`, MSTR spawn-msg pulled + acked.
2. `org/XXX.md` startup protocol completed — session-id serial file written, hooks idempotent, comp-graph context set, `/work 20m` CronCreate armed (job 04aca66e at 7,27,47 each hour off-minute).
3. AC1 ship verified pushed origin/CLOUD (`git branch -r --contains 8de9c5415` → `origin/CLOUD`). Code-substrate anchors verified at `data/demo/scripts/transform/demo_transform.py` L89/L97/L100/L755/L777/L820/L890-891.
4. Phase 3 RAVC2 scaffold pre-staged at `.runtmp/advi_demov1_012_phase3_ravc2/SCAFFOLD.md` — AC1 PASS substrate inline, AC2-AC6 placeholders + verification recipes + 5 banking obs candidates pre-listed.
5. 3 MCPs dispatched: MSTR `[SPAWN-ACK]` orient summary, ws COO FYI, AE 0.7 parallel-pair handshake with Fire 1 terminal MCP request.

## Fire 1 terminal trigger plan (compression target ~5-10min wall)
On AE 0.7 Fire 1 `5caba4eb` terminal MCP:
- Pull `apply_report.json` (S3 path TBD from MCP) + parse `source_total`/`written_total`/`complete` + per-subpath summary.
- Run AC3 strict `pii_leak_scan.py` independently parallel to AE-side (no `--f1-residue-tolerance`) → expect `leak_count=0 + format_anomaly_count=0 + exit 0`.
- Finalize AC4 calibration table: Fire 6 wall + Fire 1 wall + steady-state baseline + formula `max(steady×1.5, first_post_rev×1.5)`.
- Confirm AC5 wrapper hardening with AE's diff hunk reference.
- Execute AC6 F1 retire absorption decision logic (post-AC2 scan for z-prefix residue across all 4 PASS2_DEST_SUBPATHS).
- Ship joint RAVC2-Request to ws COO with CC AE 0.7 + CC MSTR; final doc-of-record at `org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-27/work_<HHMM>Z_advi_demov1_012_phase3_ravc2.md`.

## Compiler tools
- `comp-pipescript io / deployed / postdeps` — N/A this tick (no script edits; AC1 ship was pre-reboot session and used these gates per `8de9c5415` discipline).
- `comp-validate` — N/A (no `gold_validate_config.yaml` for demo chain; AC3 strict-scan + `apply_report.json` = AC2/AC3 substantive verification surface per [[feedback_verification_class_taxonomy_for_b_extension_rulings]] LD-0095 empirical-smoke-class).

## Standing posture
KEEP-LIVE through Fire 1 terminal window. /work cron 20m cadence keeps watcher + heartbeat fresh; substantive RAVC2 ticks gated on Fire 1 terminal MCP arrival.

work-cycle:1
