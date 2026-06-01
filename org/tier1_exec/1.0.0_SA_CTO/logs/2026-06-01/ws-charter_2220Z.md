# /ws-charter event-driven action — 2026-06-01 ~2220Z

**CLASS:** NOVEL — surfaced to Andrew (new-macro request; not authored, gate-respected)

## Trigger
- **0.7.0_AE_CloudOps [BRIEF + PRD-REQUEST]** (221737Z): propose a NEW macro `NFRA` (non-functional/infrastructure/shared-cloud) + a standing Cloud/Shared-Resource Cost-Governance PRD. Brief committed 813651cf4. Andrew-directed May cloud-cost forensic surfaced real findings + a structural gap (no cloud-cost macro: ADHC=ad-hoc, ADVI_SHARED=firm-data-shared).
  - Findings: May $602; EC2-Compute 59% ($355); bd-gold-layer-runner c6i.16xlarge = $204 (34%); right-sizing real-but-nuanced (bursts to 64-core saturation, averages ~14%/median 7%, RAM ~99% idle — needs wall-time-vs-cost analysis NOT a guess); telemetry partial (gold_prof on bd+inf only, inf cpu:null); attribution blocked (no CUR/tags, ephemeral IDs); hygiene (EBS $63 stopped vols, 8x stopped backfill fleet, QA runner no-auto-shutdown).
  - Lesson encoded: AE's first-pass core-normalized-CPU mis-read (Andrew-rejected) → PRD must mandate units-verified + CPU-as-instance-% + live corroboration + wall-time-vs-cost BEFORE any downsize.
  - 5-item scope: attribution / fleet-telemetry / right-sizing-methodology / lifecycle-hygiene / cadence+owner.

## Classification + action
- **NOVEL** (new macro = REGISTRY Active-section addition = ws-charter HARD-BLOCK #7). ws CTO does NOT originate NOVEL autonomously; Andrew direction required. The May forensic was Andrew-directed, but institutionalizing it as a new macro + standing PRD is a structural step beyond the forensic = Andrew's taxonomy call.
- Andrew is LIVE in-session → SURFACED to Andrew directly (not HALT+CC-MSTR, which is the Andrew-unavailable path) with a CTO recommendation. Did NOT author the macro/PRD (gate-respected).
- **ACK'd AE** (221942Z): CTO lean = APPROVE (gap real, NFRA reasonable, scope sound, rigor-mandate excellent). On Andrew greenlight: AE authors the draft on my charter (has the forensic + corrected ground-truth), I shape macro framing + REGISTRY registration + review, CVO methodology-verify gate before any downsize. HARD PRD requirements I'll insist on: rigor-mandate as gating precondition, CVO methodology-gate on right-sizing, attribution-before-optimization.

## Follow-on / next-cycle expected state
- Andrew go/no-go on the NFRA macro + cost-gov PRD (added to his decision queue; non-blocking, deadline-free standing governance, distinct from BMKAUD durability-TF).
- On greenlight: AE drafts → CTO macro-framing + REGISTRY → CVO methodology-verify.
- Commit-tag: ws-charter-cycle:0026 class:NOVEL.
