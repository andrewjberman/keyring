# 2.0.0_SA_COO — /drive Empirical Companion

Operational steps: `.claude/skills/drive/SKILL.md`.
Cross-agent learnings: `~/.claude/projects/.../memory/MEMORY.md` → Driver Discipline section.
**This doc holds COO-side organization + scope discipline ONLY (no SKILL.md duplication).**

## Chain-invoke at cycle end: `/allocation`

Every /drive cycle chain-invokes `.claude/skills/allocation/SKILL.md` at Step 8 — emits worker-set delta + MCPs MSTR for execution. /drive = demand signal; /allocation = supply signal. v0.1 Andrew sovereign 2026-05-26T13:42Z.

## Cycle-log discipline

- Per-cycle path: `logs/{YYYY-MM-DD}/coo_drive_cycle_NN_{theme}.md` — one per /drive fire.
- Never drop cycle logs at the COO folder root. Always under `logs/{YYYY-MM-DD}/`.
- End-of-day / end-of-session: roll the day's per-cycle logs into `logs/{YYYY-MM-DD}/session_drive_NN_to_MM_{theme}.md` capturing range + theme. Preserve per-cycle files in `logs/{YYYY-MM-DD}/cycles/` (move, don't delete — audit-survivable).
- Canonical session-consolidation anchor: `logs/2026-05-26/session_drive_67_to_89_ld0089_pavc_through_ac9_convergence.md`.

## Scope + posture

- **ws COO drives ws-fabric registry only (LD-0042).** Cross-fabric requests route via MSTR or joint CTO+COO consult.
- **AC9-window / Tier-2-3-absent posture:** when workers offline (post-reboot or pending sovereign sign-off), route authoring-axis work to live Tier-1 (CTO/CVO/MSTR); do not dispatch NEXT-ACTION TOs to offline serials.
- **Step 6 hard-gate paths:** ≥1 project-axis dispatch OR per-project monitoring-path attestation OR queue-hygiene to MSTR. "Standing by" is never terminal.

## Recurring pitfalls (memory pointers — do not restate)

- JSON > REGISTRY at Step 2 read: `feedback_drive_read_json_not_registry.md`
- Verify in-flight by artifact, not SLA: `feedback_track_inflight_to_by_artifact_not_sla.md`
- CORROBORATE-with-additive materializes immediately: `feedback_corroborate_with_additive_meta_materializes_immediately.md`
- Track by artifact during multi-phase TO execution: `feedback_surface_phase_artifacts_during_execution.md`
