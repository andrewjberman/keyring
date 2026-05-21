# Session Log — ADVI_DEMOV1.000 Phase-0 Serving-Path + PII Probe

**Agent:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-21
**Task Order:** ADVI_DEMOV1.000 (issued by 2.0.0_SA_COO~C; org lane CTO base ← COO~C ← DS~C)
**Status:** COMPLETE — read-only probe; brief delivered; RAVC2 to COO~C.

## Current State

Phase 0 of ADVI_DEMOV1 complete. The probe closed the §3.2 linchpin (the
static-platinum `?firm=` serving mechanism), produced an independent PII field
inventory reconciled against the ADVI_ANONYM map, characterized the dynamic
serving topology, and audited firm-specific code branches a new `demo` firm
would trip. Read-only — no code, no infra, no S3 writes.

Deliverable brief:
`docs/briefs/advi-demov1-phase0-serving-path-pii-probe-20260521.md`.

### Key findings

1. **§3.2 RESOLVED.** Static-platinum routes: CloudFront `EVTSA9VEHNZVH` →
   behavior `/api/scoped/advisor-intelligence/*` → Lambda@Edge `auth-validator-edge`
   (injects `X-Firm-Id`) + `shared-advisor-router` (runtime origin-mutation,
   bucket from `FIRM_CONFIG` in `_shared/firm-config.mjs`). `?firm=` is consumed
   only for `opal-capital` internal staff. GO — recommended Phase-1 path: explicit
   `FIRM_CONFIG` `'demo'` entry + CI-sentinel flip + OAI bucket-policy grant.
2. **Pseudonymizer retired.** `opal-partners-data` `needs_pseudonymization()`
   returns `False` (Andrew, 2026-04-15) — real PII served cleartext; no
   serve-time net. Corrects proposal §3.1/§4.
3. **Not platinum-only.** `handle_client_detail` reads
   `gold/entities/clients/{id}/detail.json` — DEMOV1 transform scope widens.
   `bd-client-detail` Lambda (risk #6) is pipeline-time, not portal-facing — moot.
4. **PII inventory** — 7 DEMOV1-ONLY field classes beyond the ANONYM map
   (`firm_id`, `firm_name`, `advisor_id`, `name`, `display_name`, `rel_id`,
   `adv_drill` keys/list-strings) + S3-key slugs + exec_summary free-text.
   Context-dependent `label`/`key` (tickers vs names) ⇒ transform must be
   JSON-path-aware.
5. **2 required portal changes** for a `demo` firm: `firmAccess.ts`
   `FIRM_ALLOWED_PATHS` entry + `_partners/demo/` tenant layout (both DE).

The §3.2 verdict was surfaced to COO~C mid-probe as a phase artifact (per the TO
"surface artifacts as you hit them"); COO~C ACK'd and banked it into TO-1.

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/advi-demov1-phase0-serving-path-pii-probe-20260521.md | CREATED — the Phase-0 probe brief (deliverable) |
| docs/proposals/advisor-intelligence-demo-dataset-20260521.md | EDITED earlier this session — folded the ADVI_ANONYM reuse finding into §6 + §7 (pre-TO, CTO-requested) |
| org/tier2_senior/0.4.0_DS_ClientPlatform/task_orders/ADVI_DEMOV1.000.dsc-static-platinum-serving-path-pii-probe.md | status staged → pending |
| org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-05-21/advi_demov1_phase0_probe~C.md | CREATED — this log |

## Compiler Tools

| Tool | Result | What it showed |
|------|--------|----------------|
| `comp-routes trace getPlatinumFirmDashboard` | RESOLVED | CF behavior `/api/scoped/advisor-intelligence/*.json` → S3 origin `S3-opal-data-bd`, edge JWT, Router `shared-advisor-router`. Named the §3.2 linchpin component — drove the whole serving-path resolution. |
| `comp-blast opal-partners-data` (Phase 1) | `No downstream consumers found` | Baseline — the dynamic serving Lambda is a leaf node. |
| `comp-pii audit` | 3 PII refs (ClientsTab), rest clean; "0 S3-direct PII" | Portal-component model only; reflects field-name classification, not the retired-pseudonymizer runtime. Used as one input; §3 of the brief is the independent S3-tree walk per the TO `<if_mismatch>` (comp-pii does not walk the platinum tree). |
| `comp-blast opal-partners-data` (Phase 3) | `No downstream consumers found` | Identical to Phase-1 baseline — confirms the probe mutated nothing. |

## Next Steps

| Recipient | Item |
|-----------|------|
| **2.0.0_SA_COO~C** | RAVC2 — ADVI_DEMOV1.000 COMPLETE. Brief delivered; §3.2 resolved (GO); 8 ACs met. Feeds CTO PRD risk section. |
| **1.0.0_SA_CTO (CC)** | Phase-0 deltas to fold into `docs/architecture/ADVI_DEMOV1.md` risk section — brief §7. |
| **DS~C (self)** | Hold Phases 1-4 — gated on PRD ship + COO~C decomposition. |
