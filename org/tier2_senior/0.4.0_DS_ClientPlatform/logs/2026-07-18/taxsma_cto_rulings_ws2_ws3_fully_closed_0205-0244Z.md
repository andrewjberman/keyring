# OPAL_TAXSMA_PT2: CTO rulings received -> WS-2/WS-3 FULLY CLOSED; cot re-arm gate standing (delta)

**archetype:** COORDINATE
**serial:** 0.4.0_DS_ClientPlatform (base lane) · **window:** 2026-07-18 02:05Z -> 02:44Z
**prior log:** taxsma_pt2_ws2_silver_ws3_gold_landed_0008-0205Z.md @ f2c8d7ee2

## Summary

Short delta window: no new code commits -- this was the closure of the TAXSMA_PT2 SEV1
workstream via two CTO rulings + a durable memory persist. All my TAXSMA + cot-drift work is
now FULLY CLOSED or correctly parked under a standing gate.

## Work done (rulings received + dispositions)

1. **CTO cot-exporter drift ruling (msg 022214Z):** DEFER accepted (Andrew). CTO now HOLDS a
   STANDING, cross-session **RE-ARM-BEFORE-COT-APPLY gate**: before ANY cot-pipeline terraform
   apply, `CotDetectionSnsPublish` must first be re-added to `iam.tf:241 cot_exporter_policy`
   (restore config==deployed, targeted plan=no-op verify), so the apply cannot strip it and
   silently kill the e2 pricing-defect alarm. CTO framed it as a **Class-B correctness firebreak**
   (an already-deployed detector protected from a drift-strip), explicitly OUTSIDE Andrew's
   alert-suspension. My role: executor-on-trigger (flag + prep the config change when a cot apply
   becomes imminent, under CTO's apply-gate). Read-only grounding held (Rule 13); NO cot infra touched.
   -> PERSISTED to DS memory `project_cot_exporter_sns_publish_rearm_before_apply.md` (+ MEMORY_FULL.md
   pointer under "COT / BD pipeline facts") so a future DS cot-pipeline deploy can't strip it unknowingly.
   ACK'd CTO (022423Z).

2. **CTO WS-4 SEV1 PII ruling (relayed by COO, msg 023744Z):** the design point COO surfaced
   (real schwab account number in the gold S3 key path) is RULED -> **REAL ACCOUNT-NUMBER KEY
   ACCEPTED; WS-3 STANDS as landed (1ba779e0b); NO surrogate rekey.** Rationale: Alyssa operates
   BY exact account number (OPAL_TAXSMA_REGISTRY resolver, Andrew-non-negotiable), so serving her
   data keyed that way is INTENDED; an account number is a business key, not name/SSN-class PII;
   the CONTENT PII I scrubbed + mutant-tested is what mattered and it's proven. The enumeration
   concern (path-based ListObjectsV2 of others' account numbers) MOVES to WS-4's account-scoped
   IAM (AE/DT lane), NOT my gold build. -> My surrogate-rekey standby is RELEASED (stood down).

3. **WS-2 + WS-3 FULLY CLOSED, no rework.** ACK'd COO (023941Z); broker summary updated to reflect
   full closure. WS-4 go-live stays CTO's hard-withhold (account-scoped IAM applied+exercised
   controls + CVO independent PII verify -- CTO pulled CVO).

## Compiler Tools

None this window -- ruling-receipt + closure coordination + a memory persist; no code/infra change
(the WS-2/WS-3 comp-tool runs are in the prior log @ f2c8d7ee2; cot-drift grounding likewise).

## Blockers

None. WS-2/WS-3 CLOSED. cot re-arm gate is DORMANT (fires only on an imminent cot apply; CTO holds
it). WS-4 is CTO/AE/DT/CVO lanes, not mine. No open work.

## Current State (handoff surface)

- **SILVER + GOLD unchanged from prior log (both LIVE, CLOSED):**
  `s3://opal-data-assets/blackdiamond/49f/silver/fact_taxsma_report/date=2026-07-17/` (4d5b0148c) and
  `s3://opal-data-assets/blackdiamond/49f/gold/dim_taxsma_report/account=0027265115/date=2026-07-17/` (1ba779e0b).
  Real-account-number key CONFIRMED to stand by CTO. No rekey pending.
- **cot re-arm gate:** standing, CTO-held; DS executor-on-trigger; persisted to DS memory. Trigger =
  next imminent cot-pipeline terraform apply. Grounding on record (msgs 013731Z/020211Z; CTO 022214Z).
- **Follow-on gaps (non-blocking):** semantic window labels (Q/QTD/YTD/SI) + trade-start need Yang's
  xlsx (PRD sec-7 open decision); strategy not in BD feeds.

## Next Steps

- **[1.0.0_SA_CTO]** WS-4 hard-withhold: account-scoped IAM applied+exercised (positive/negative
  controls) + CVO independent PII verify against the live gold artifact. Holds the standing cot re-arm gate.
- **[3.0.0_SA_CVO]** (pulled by CTO) independent PII-safety verify of gold dim_taxsma_report -- the
  mutant-tested gate + served read-back are on record; verify against the live artifact. Flag me if anything surfaces.
- **[me / 0.4.0_DS base]** No open work. Event-driven + reachable (Monitor b3921ocfs). Turn fast if:
  CVO's PII verify surfaces something on the gold; a base-lane TO surfaces (COO); or a cot apply
  becomes imminent (re-arm prep under CTO's gate).
