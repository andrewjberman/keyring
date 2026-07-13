# 0.8.0_AE_CloudComp -- OPAL_ASSETS P0-A: lane resolution, G4/G5 design, deploy pairing

**archetype:** MIXED
**secondary_archetypes:** COORDINATE, IMPLEMENT, DIAGNOSE
**Serial:** 0.8.0_AE_CloudComp (PID 24384) | **Date:** 2026-07-13 | **Window:** session start (~03:32Z) -> 04:40Z (first log of session)

## Summary

Fresh session. Resolved a multi-round lane-identity churn, then drove OPAL_ASSETS.P0-A through an Andrew-direct re-scope: I do NOT build a parallel DynamoDB table (0.7.0~A owns the base table+emitter+backfill); my half = G4 (per-partner ETF-ownership fold) + G5 (convergence). Shipped 4 commits (2 design deliverables + 2 drafts), all Opal-side, all pushed. LIVE-demonstrated the fold on prod data. Grounded ~A's deployed table/emitter/IAM. Now at the deploy-coordination gate (paired with ~A + CTO~B-ruled).

## Lane resolution (session start)

Broker slot for 0.8.0 was contested across dead PIDs 34788 + 2508. Root cause (disclosed by base CTO 034838Z): **the base CTO session (PID 2508) lost its identity at a context compaction and adopted MY serial from the shared `.comp-graph/.agent_context`** -- it sent messages + authored commits under my line, killed my watcher twice, and claimed my P0-A TO. This is the exact shared-`.agent_context`-SERIAL-as-identity defect org/XXX.md Step E documents. Andrew confirmed directly in-channel: "you are the only 0.8.0_AE online."
- Reclaimed the broker slot to PID 24384 (register_agent x2 -- second reclaim after the stale-2508 re-appearance COO+MSTR flagged 041235Z).
- Re-armed the persistent inbox Monitor (task bus20xzz5; a prior Monitor b0kydph2z ended mid-session, re-armed clean, no orphan).
- **Attribution note (record cleanliness):** commits eab292707 / 19fde37de / 2526d3856 / 25dfc368e landed under my author line but are BASE CTO's work (disclosed to COO). I do NOT claim them. MY session commits: c509e1c9d, e57c02ff4, 9e6c402ba, 43b7d36d5.

## MCP traffic

~30 messages handled (many broker re-surfaces of already-read mail). Significant:
- IN: COO CLEAN-SLATE re-scope (0.7.0~A owns base table; I fold/extend) + G4-accept + G5-GO + do-both-(a+b) steer; ~A HANDOFF (live table ARNs + emitter path + row shape); CTO~B DUAL RULING (additive-rows APPROVED + self-classifying condition; measured-source RATIFIED over target_weight); DS shape-accept + 3 arch-gate notes; base CTO release+handoff+apology.
- OUT: G4 design + G5 spec delivered to COO; fold draft + IAM verify routed to CTO~B+~A; deploy-coordination proposal to ~A; single-source ratify req to CTO~B. All RAVC loops ACK'd both directions.

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-which | "what serves mdpf aggregate_aua daily" | PARTIAL | near-tie route; grounded served path at source instead |
| comp-blast | mdpf_aggregate_aua | WARN | no EXTRACTED edges (lower bound; dynamic-key consumers not edged) |
| comp-glob | `**/*avgcap*`, `**/*rps_recon*` | PASS | located avgcap_bd_rps_recon.py (etfs gold) + ETFS_AVGCAP.md; 972 sovereign-held paths correctly excluded |
| comp-iam (equiv) | `aws iam simulate-principal-policy` on the emitter role | PASS | Rule-22a pre-check: opal-data-etfs read=implicitDeny (grant needed), mdpf read=allowed (positive control -> deny is real), table PutItem=allowed |
| commit-gate | on 2 draft .py | PASS | py_compile + ds-precommit + ruff clean both |

**Worked:** simulate-principal-policy (not comp-iam DESIRED) was the right Rule-22a instrument -- cleanly showed the one grant needed + a real positive control. comp-glob's sovereign-held exclusion kept me on rails. **Gap found:** comp-which near-tied on the mdpf-serves question (no single canonical route) -- routing gap worth a coverage note. **Grounding discipline:** caught that the PRD-named `avgcap_bd_rps_recon` is a SOVEREIGN-reading diagnostic (reads opal-data-bd/schwab on demand), NOT a served artifact -- the real Opal-side source is opal-data-etfs/daily. That distinction kept the whole G4 interim fold zero-sovereign-read.

## Files Modified

See commit messages: c509e1c9d, e57c02ff4, 9e6c402ba, 43b7d36d5 (all under org/tier2_senior/0.8.0_AE_CloudComp/deliverables/). No infra/live-code edits yet -- design + drafts only; the live-emitter edit + safe-apply are deploy-paired-pending (see Blockers).

## Blockers

**PAIRING GATE (not hard-blocked -- coordination on a shared TF module):** the G4 deploy waits on 0.7.0~A's reply on (1) the CTO~B-required classifier field: value_class="cohort_aum"+value_basis (CTO~B literal) vs an additive `record_type` (my lean); (2) WHO safe-applies infra/aws/terraform/opal-assets/ (~A's module -- one applier, no TF race). Evidence: my pairing msg 044019Z; ~A's handoff invited "ping me to pair." Not assumption-blocked -- surfaced + awaiting the emitter-owner's call before touching his live TF.

## Current State (handoff surface)

**Re-scope (Andrew-direct, COO 034836Z):** 0.7.0~A owns the base OPAL_ASSETS table+emitter+backfill; I own G4 (per-partner ETF-ownership fold) + G5 (convergence), EXTENDING ~A's table. No parallel table.

**~A's LIVE table (verified, not self-report):**
- Table `opal-assets-daily-aua` ACTIVE. ARN `arn:aws:dynamodb:us-east-1:313476888478:table/opal-assets-daily-aua`. Base keys PK=`run_date` / SK=`cohort_id`; GSI `cohort_history` (PK=cohort_id, SK=run_date). PAY_PER_REQUEST, PITR+SSE. Backfilled (07-06 partition present; date-aware states).
- Emitter `infra/aws/lambda/opal-assets/opal-assets-daily-emitter/lambda_function.py` -- `build_rows(body, run_date)` is PURE (14 base cohort rows from the served mdpf partition); role `opal-assets-daily-emitter-role` reads opal-data-portal-v2/mdpf/* + writes the table+GSI. TF `infra/aws/terraform/opal-assets/{main.tf,emitter.tf}`. Deployed opal-assets-v0.1.0. Daily EventBridge 17:15Z. Backfill: `python lambda_function.py --backfill START END`.

**My deliverables (all on origin/CLOUD):**
- G4 avgcap-fold design -- c509e1c9d (deliverables/OPAL_ASSETS_P0A_G4_avgcap_fold_design_20260713.md). Fold consumes the already-served Opal-side `opal-data-etfs/daily/{partner}/{date}.json` (49F frozen 06-24 = 08242234-RPS side; inflection+cottonwood fresh 07-10). ZERO sovereign read.
- G5 convergence spec -- e57c02ff4. interim->full = value change on a FIXED key set (never-widen at row level); both-masters custody POST-G2; served cutover P2/gated (NEVER#2+#4).
- Fold draft + Rule-22a IAM verify -- 9e6c402ba (deliverables/drafts/g4_fold_etf_ownership_draft.py + rule22a_iam_verify_opal_assets_emitter.sh). LIVE dry-run 07-13: 12 held_by_partner entries/4 ETFs, honest state.
- build_ownership_rows extension (drop-in for ~A's emitter) -- 43b7d36d5 (deliverables/drafts/g4_build_ownership_rows_extension.py). Sibling to build_rows (keeps it pure); ownership_pct from etf_decomposition already in body.

**CTO~B rulings (043831Z, binding):** (1) additive per-(ETF,partner) ownership rows APPROVED with the SELF-CLASSIFYING condition -- every row (incl. the 14 base) must positively carry a dimension classifier so a run_date-partition read can't double-count ownership into AUM; document the served-read contract in the emitter docstring. (2) canonical held-source RATIFIED = measured opal-data-etfs/daily, NEVER target_weight. Both bind my fold + DS's P0-B.

**Rule-22a state:** the ONE new grant needed = s3:GetObject on opal-data-etfs/daily/* (pre-checked implicitDeny; mdpf-read positive control allowed; table write already allowed). Post-apply: re-simulate -> allowed + a deployed-role PutItem exercise.

**Discipline held:** zero sovereign reads (bd/Schwab/RPS/08335338/08242234 untouched); no parallel table; no TF race (deploy paired); no unilateral schema call on the shared contract.

## Next Steps

1. **[0.7.0_AE_CloudOps~A]** reply: classifier field (A value_class="cohort_aum"+value_basis vs B additive record_type -- I lean B) + WHO safe-applies opal-assets TF + anything in-flight on that module.
2. **[me, on ~A reply]** open deploy-completion ledger (NEVER#5) -> edit base build_rows (add classifier field) + add build_ownership_rows sibling + emitter.tf IAM read grant -> commit -> safe-apply (single agreed applier) -> deploy code -> backfill re-write -> Rule-22a post-verify (re-simulate + deployed-role exercise) -> RAVC2 to 2.0.0_SA_COO (table ARN + 2 demo queries + simulate evidence+positive control + 14-base + folded-ownership day dump).
3. **[0.4.0_DS_ClientPlatform]** P0-B (mdpf emitter extension + G4 fold at source) binds to the same locked schema + single-source rule; staged post-Round-8.
4. **[1.0.0_SA_CTO~B, next session]** optional steer on classifier field (A vs B) if he has a preference; else ~A's call stands.
