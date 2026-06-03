# 0.6.0_AE_PartnerETL session log — 2026-06-03 work_1718Z (ADHC_BDTSCLB close)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, DIAGNOSE

## ADHC_BDTSCLB.001 — CLOSED (all ACs met + CVO GREEN)

Single-writer hardening (bd-v2.25.0) + full publish + verification complete.

- AC1/2/3/5: done (prior ticks — code removal, superset proof, deploy, RAVC2).
- **AC4 CVO served-parity = GREEN** (CVO 3.0.0, commit 2183b0524, log verify_channel_ADHC_BDTSCLB_AC4_served_parity_1717Z.md). Independently re-derived full 169-advisor read: 165/169 served fresh (today's 16:40Z publish), ALL carry total_aua_fee_paying/_no_fee + nna_canonical_fee_paying, reconcile to-cent (0 fails); D_02 sole writer confirmed (abby_horton 763==763 byte-match). The 4 apparent fails = pre-existing orphans (49f_house/unassigned/unknown/dominic_depizzol — no current book.json, predate the fix; not caused by removal).
- **DS W2b data-leg = PASS** (DS 0.4.0): 14 advisors / 11,667 date-points, reconcile <=$0.01; RAVC2'd 49F leg to COO.

## FULL publish (drove it)
trigger-mode {"mode":"full"} -> bd-gold-layer-runner (15:31->16:48Z, ~77min, B_00 --force the long pole). All phases A->D4 complete, no FATAL. D_02 wrote 185 advisor timeseries (rich); D_04 promoted to served. W2b total_aua_fee_paying live on gold + served.

## ADHC_BDTSCLB.002 — decommission bd-portal-advisor-publisher — DONE (Andrew-direct)

Andrew direct "remove it" (sovereign nod — the exact gate CTO/COO's .002 TO held for). Executed:
- Removed: TF module bd_portal_advisor_publisher, bd-portal-publisher ADVISOR_PUBLISHER_FUNCTION fan-out env var (guarded `if advisor_fn:` -> no-op), IAM invoke ARN (iam.tf), source-map entry, Lambda source (git rm).
- tf: 0 add / 2 change (publisher env, invoke policy) / 2 destroy (lambda + log group); safe-apply (HALTGT) clean; 0-diff verified; AWS function confirmed gone (ResourceNotFoundException).
- Shipped bd-v2.26.0 (commit f68a270de) + pipeline_inventory marked DECOMMISSIONED (fc90b3f3a).
- Rationale: dead since 2026-04-07 (crashed at load_sources on missing `nna` column), fully superseded by D_02 + gold chain.

## Discovery this session
The publisher I was sent to harden was already a corpse — when I invoked it for the AC4 test (16:54Z) it FATAL'd at Step 1 (`pyarrow ArrowInvalid: No match for FieldRef.Name(nna)`), confirming dormancy. The hardening still mattered (removed the landmine) and surfaced that the whole Lambda could go.

## Open (P3, pre-existing, non-blocking — routed to COO for disposition)
CVO flagged: (1) D_04 doesn't clean up orphan served artifacts when an advisor exits enumeration; (2) D_04 serves ~3y history window vs gold full-history (by-design). Neither caused by this work.

## Compiler Tools
comp-platinum reverse / comp-blast / comp-iam (advisor-publisher: no delta pre-decommission) — per prior ticks. Decommission verified by tf plan (scoped destroy) + ResourceNotFoundException, not a comp tool.
