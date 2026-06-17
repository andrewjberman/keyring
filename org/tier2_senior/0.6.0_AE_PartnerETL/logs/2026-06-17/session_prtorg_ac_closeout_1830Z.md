# 0.6.0_AE_PartnerETL — 06-17 ADVI_PRTORG AC-CLOSEOUT structural verify (COO GO)
**archetype:** VALIDATE

## Window
06-17 ~1828Z-1836Z. COO GO 182810Z (ADVI_PRTORG.AC-CLOSEOUT, CTO close-gate ruling: structural ACs
1/4/7 run NOW, chain-INDEPENDENT). Quick structural smoke to close PRTORG; ran between SS4c increments.

## Result: 3/3 structural ACs PASS -> PRTORG clear to close (1 chain-gated sub-check deferred)
- **AC1 (Cottonwood TF module org): PASS.** partner-firms/cottonwood.tf (548B) + cot-pipeline/ TF root +
  modules/partner-firm-table/ shared module; identity table opal-partner-cottonwood DDB ACTIVE (1 item) =
  proof cottonwood.tf is APPLIED; cot-pipeline applied proven by live opal-data-cot bronze/silver artifacts.
- **AC4 (FE module): PASS.** portal main tree on DEV (Rule 19). _partners/cottonwood/ {constants,index,
  layout,roles}.ts (all 4) + dispatcher (import CottonwoodAdvisorIntelligence + PARTNER_VIEWS['cottonwood']
  + ALL_PARTNER_FIRMS entry) + firmAccess FIRM_ALLOWED_PATHS['cottonwood'] + domain map. (FIRM_CONFIG data
  binding = SERVING plane = PRTORG.03, separate/closed, live v2.1.119 PROD.)
- **AC7 (ownership_map.json): STRUCTURAL PASS + 1 deferred sub-check.** s3://opal-data-cot/platinum/
  cottonwood/ownership_map.json well-formed {schema_version:1, firm_id:"cottonwood", advisors:{}} (empty
  advisors EXPECTED per PRD §6.1 OUTCOME B = COT v1 firm-level Distribution-only). DEFERRED: generated_at
  2026-06-09 (gold-chain-frozen freshness = the cot-platinum-freeze, tracked via ADVI_COTETL.CHAINFIX) --
  live-served-freshness aspect, defers per the CTO split; non-blocking (content structurally final for v1).

## Hygiene flag (not my lane -> DT)
portal/.runtmp/portal-promote-v2118/ + portal-promote-v2120/ = stale promote-worktree leftovers in the
portal main tree (Rule 19 ephemeral-worktree discipline). Non-blocking; flagged to COO for DT cleanup routing.

## Compiler Tools
No comp-* tool run. Why (gate): structural existence/wiring verification (repo TF + portal-DEV-tree FE +
live DDB describe-table + S3 head/cp of the ownership_map artifact) -- no code/infra/gold change, no comp
trigger applies. Tooling: ls/find/grep on repo + portal, aws dynamodb describe-table, aws s3 ls/cp.
(comp HUD nudged pipescript --resource on the ownership_map S3 grep; not needed -- I head-object'd the exact
key + verified content directly, which is the authoritative read for a structural existence check.)

## MCP traffic
1 inbound (COO GO 182810Z) -> ACK 182951Z -> RAVC2 results 183552Z (CC CTO). COO owns the 2-step atomic close.

## Blockers
None.

## Current State / Next Steps
- ADVI_PRTORG: 3/3 structural ACs PASS; verify-TO marked complete; COO to do the 2-step atomic close
  (JSON status + REGISTRY row) citing this evidence. 1 deferred AC7 freshness sub-check already tracked (CHAINFIX).
- [2.0.0_SA_COO] 2-step atomic close of ADVI_PRTORG.
- [DT] tear down portal/.runtmp/portal-promote-v21{18,20}/ leftovers.
- [0.6.0_AE_PartnerETL] resume SS4c build (canary TF + TIER-2 weekly chain leg + alarms + deploy).
