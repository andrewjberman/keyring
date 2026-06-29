# 0.7.0_AE_CloudOps TO-Registry Reconciliation (2026-06-29)

**Author:** 0.7.0_AE_CloudOps~B · **For:** 2.0.0_SA_COO (GO 141032Z, Option A) · **Method:** ground each open TO vs shipped commits / closed deploy-ledgers / live AWS+graph.
**Result:** authoritative `to-check --all --assignee 0.7.0_AE_CloudOps` went **42 -> 40 active** (this session's full flip-set = 5, incl. C/W4/P2-2 flipped earlier today). The registry is **mostly accurate**; the churn came from a small stale-set, now corrected.

## Flipped -> complete this session (grounded)
| TO | grounding |
|---|---|
| ADVI_COTETL.AUAFIX-DATEMODE-C | deployed ded252bae; live SSM holdings step present; sentinel intact (ad580cab4) |
| NFRA_COSTAWS.W4 | core superseded by 06-05 universal enforcer; hygiene census filed fb35565cd (a435e83d0) |
| NFRA_TSGRAPH.P2-2 | ledger 20260626T2022Z CLOSED; live-verified 91 PanelCluster nodes HEAD-current (1871a357e) |
| NFRA_COSTAWS.R2 | 14d tighten applied+served-verified 6bd00c015 (the /govern gate was MET); project-JSON COMPLETE (99baedee5) |
| NFRA_GLOBGRPH.TO-MAINT | genuinely complete e3d806c2d (parent project CLOSED) -- added parseable <status> tag (was markdown-only) (99baedee5) |

## ROOT-CAUSE findings (the registry-lying mechanism)
1. **Status-format inconsistency breaks to-check.** TO-MAINT used markdown `**Status:** complete`; to-check parses only the `<status>` XML tag -> it showed `[??]`. Recommend a status-format standard (parseable `<status>` first-word = pending|active|staged|complete|queued) OR teach to-check to also read `**Status:**`. Several TOs mix formats.
2. **Long multi-clause status strings** (e.g. DTAFLP.P1 "complete -- LANDED ... read active ...") fool naive first-word/substring classifiers (my own quick census false-flagged D5, DTAFLP.P1, MDPF_002 as open -- to-check itself reads them correctly, but the lesson stands: keep the status FIRST WORD a clean state token; put detail after).

## 2 FLIP-CANDIDATES needing one confirm before flip (did not flip -- avoid wrong-drop)
- **ADVI_COTETL.CHAIN-FIX** -- status "active -- AE-LEG DONE+ACCEPTED (cot-pipeline-v0.4.0+v0.4.1)". AE leg done+accepted; confirm no open non-AE (DS) leg, then flip.
- **ADVI_COTETL.AUAFIX-L1** -- "verify 06-19 nightly unblocks chain" (06-18 issued); that nightly is long past + the chain was reworked via DATEMODE-A/B/C. Almost certainly superseded -> close-as-superseded after a 1-line confirm.

## GENUINELY-OPEN dispatch source (the 40), by readiness

### READY NOW (un-gated, GO-cleared -- safe to dispatch ~B)
- **NFRA_COMPAWS.PHASE-0** -- active-GO "can begin now" (CVO hand-audit).
- **NFRA_COMPAWS.LAMBDAMAP-P2** -- active-GO (sha-vs-live phase 2).
- **NFRA_COMPAWS.IAM-CONDITIONS** -- active (comp-iam condition-blind FP fix; the estate-accuracy fix that mis-read SCTY.W2's bd-exporter grant).
- **NFRA_COSTAWS.W3** -- methodology drafted b4a75d076; needs finalize/RAVC2-accept (right-sizing premise largely dissolved per CTO -- likely a short close).
- **NFRA_COSTAWS.W5** -- cadence/ownership drafted (costaws-cost-cadence-ownership-v1.md); needs COO co-sign to close.
- **NFRA_OPLMCP.05.R8** -- active (R8 audit-lake).

### GATED (external blocker -- do NOT burn a cycle)
- NFRA_DEBTSCAN.TO-D1 (after D8-AE Part B) / TO-D4 (after D1+D2) / TO-D3 (AC4 pending CVO).
- DATA_PLATFORM.DC1, DC2 (recon gates / CTO pre-apply) ; DC0 in-flight.
- NFRA_COSTAWS.W1 (leg-c CE resource-granularity = Andrew console toggle; legs a/b done, CUR live-verified today).
- ADHC_INFDATA.REPIDS (Andrew inf-data ruling, LOW). FABRIC_GOHOOK.001 (behind NFRA queue, CTO-gated, LOW). SCTY_MCPGUARD.S0 (Andrew PRD review).
- NFRA_ALERTSUB (LOW monitoring gap).

### BASE'S ACTIVE AUTH/COT SURFACE (do NOT pull -- collision)
- ADVI_COTETL: DATEMODE-B, BACKFILL.ae-session, AUAFIX-L2, AUAFIX-L4 (partial: comp-freshness cot-registration present, staleness-alarm+F-1 egress pending), AUAFIX-L5 (CVO-led), CHAIN-FIX. ADVI_BDAPIMIG.GATEB-LOCK (new today).

### IN-FLIGHT / STAGED (owner progressing)
- NFRA_GRAPHS.D8-AE (Part A complete, Part B core in progress), D7-FIX.T5, D7-FIX.T6.
- NFRA_GLOBGRPH.ITEM-3 (load-layer complete, AC-gates unvalidated -> needs honest AC-validation).
- NFRA_INFRPT.P2, P3, GUARD-REFILE (staged). tf-plugin-cache-dedup-disk-reclaim (staged).
- NFRA_OPLMCP.04, NFRA_WRKFLW.P1 (queued). SCTY.W1 (CTO arch-gate). SCTY.W2 (~B mine -- assessment+Moltbot done; residual remediations tracked). ASTN_WSJFT.B (~C), B1.

## Recommendation
Dispatch ~B from the **READY NOW** bucket (PHASE-0 / LAMBDAMAP-P2 / IAM-CONDITIONS are clean un-gated AE infra; W3/W5 are short doc-closes). Confirm+flip the 2 flip-candidates (CHAIN-FIX, AUAFIX-L1) to drop the count further. Adopt the status-format standard so to-check stops mis-counting.
