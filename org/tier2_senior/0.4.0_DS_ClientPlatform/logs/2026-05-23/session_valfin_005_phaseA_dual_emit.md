# Session Log: ADVI_VALFIN.005 Phase A -- Dual-Emit Capital Gains Field Rename
**Agent:** 0.4.0_DS_ClientPlatform  
**Date:** 2026-05-23  
**TO:** ADVI_VALFIN.005.ds-capital-gains-ttm-field-rename.md (commit 3ecf66be8)  
**Branch:** CLOUD  
**Session commit:** 92a18ce03

---

## Context

CVO LD-0012 YELLOW verdict (commit 1247fa15b) + DS Phase-2 forensic (commit f55ef0dc7) confirmed:
- `capital_gains_ttm` computation is CORRECT: delta cumulative unrealized gain over TTM window
- Field NAME is the sole defect: the name implies realized capital gains; it is actually delta-unrealized
- COO GO issued 2026-05-23T06:37Z via inbox message 20260523T065051Z

Phase A scope: DS-only. Portal-side rename (Phase B) is DE-lane, gated on DE pod-4 re-spawn (LD-0014 killed DE pod-4). This TO ships the dual-emit shim immediately.

---

## Dual-Emit Shim Design

Both gold scripts emit BOTH keys with identical values during the transition window:
- `capital_gains_ttm` -- deprecated key; portal continues reading it uninterrupted during Phase B transition
- `unrealized_gain_change_ttm` -- new semantically correct name (delta cumulative unrealized TTM)

Shim-removal trigger: Phase C (DS-lane), gated on Phase B production-deploy verify. Phase B (portal types/components swap, DE-lane) gated on DE pod-4 re-spawn after LD-0014.

---

## Compiler Tools Log (Phase 1 -- Before Write)

### comp-pipescript io INF_D_02

```
READS:
  silver/api_dims/tax_realized
  silver/api_dims/tax_unrealized
  silver/api_dims/accounts_dimension
  platinum/advisors/{id}/book.json upstream chain

COLUMN GAPS: none
PORTAL CONSUMERS: platinum/advisors/{id}/book.json downstream
```

RESULT: PASS. No column gaps on capital_gains_ttm. 4 READS confirmed. Proceed with write.

### comp-platinum reverse capital_gains_ttm (Phase 1 consumer check)

```
3 raw portal source hits:
  portal/src/api/endpoints/advisor-intelligence.ts:1013  (comment only)
  portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:571  (live read)
  portal/src/pages/AdvisorIntelligence/_shared/types.ts:934  (type field)
```

RESULT: PASS. No surprise consumers beyond the 5 documented in TO context (types.ts:934 + :1100, AdvisorBookView.tsx:571, ClientsTab.tsx:839, adapter). Dataflow index gap accounts for the 5-vs-3 discrepancy (comp-platinum indexer gap, expected per diagnostic).

---

## Code Changes (Phase A -- INF_D_02 + INF_D_00 Dual-Emit)

### INF_D_02.advisor_client_detail.py

Location 1: advisor-level tax_exposure block (~line 1899)
```python
        if cg_ttm is not None:
            adv_tax['capital_gains_ttm'] = cg_ttm  # deprecated key; Phase-B/C collapse
            adv_tax['unrealized_gain_change_ttm'] = cg_ttm
```

Location 2: household-level tax block (~line 2278)
```python
        if cg_ttm is not None:
            hh_tax['capital_gains_ttm'] = cg_ttm  # deprecated key; Phase-B/C collapse
            hh_tax['unrealized_gain_change_ttm'] = cg_ttm
```

Both locations: identical values assigned. Old key retained as deprecated shim.

### INF_D_00.portal_aggregates.py

Location 1: firm-scope tax emit (~line 837)
```python
    firm_tax_for_emit['capital_gains_ttm'] = firm_capital_gains_ttm  # deprecated key; Phase-B/C collapse
    firm_tax_for_emit['unrealized_gain_change_ttm'] = firm_capital_gains_ttm
```

---

## Compiler Tools Log (Phase 2 -- Before Commit)

### ds-commit-gate.sh INF_D_02.advisor_client_detail.py INF_D_00.portal_aggregates.py

```
All checks passed!
All checks passed!
OK: pre-commit gate clean for 2 file(s)
```

RESULT: PASS. py_compile + AST undefined-name scanner + ruff all clean.

### git diff --stat

```
 data/orion/scripts/gold/INF_D_00.portal_aggregates.py     |   3 +-
 data/orion/scripts/gold/INF_D_02.advisor_client_detail.py |   6 +-
 (4 other files in working tree -- not in this commit; safe-commit.sh --only scope)
```

Sentinel string check:
- `unrealized_gain_change_ttm` in INF_D_02: lines 1900, 2279 (PRESENT)
- `capital_gains_ttm` in INF_D_02: lines 118, 614, 627, 637, 680, 1814, 1818, 1899, 2179, 2278 (PRESENT)
- `unrealized_gain_change_ttm` in INF_D_00: line 838 (PRESENT)
- `capital_gains_ttm` in INF_D_00: lines 323, 814, 824, 828, 836, 837 (PRESENT)

RESULT: PASS. Both sentinel strings present in both files. Diff scoped to rename + dual-emit only. No scope-creep.

---

## Commit + Deploy (Phase 2 / Phase 3 transition)

### safe-commit.sh

```
[CLOUD 92a18ce03] feat(ADVI_VALFIN.005/PhaseA): dual-emit capital_gains_ttm + unrealized_gain_change_ttm
 Author: 0.4.0_DS_ClientPlatform <0.4.0_DS_ClientPlatform@opal.agent>
 2 files changed, 6 insertions(+), 3 deletions(-)
```

### safe-deploy.sh (pre-push hook)

```
safe-deploy: 2 script file(s) to deploy
  data/orion/scripts/gold/INF_D_00.portal_aggregates.py
  data/orion/scripts/gold/INF_D_02.advisor_client_detail.py

  DEPLOYED  [inf] data/orion/scripts/gold/INF_D_00.portal_aggregates.py
  DEPLOYED  [inf] data/orion/scripts/gold/INF_D_02.advisor_client_detail.py

OK: safe-deploy gate PASS -- all files deployed and verified
```

RESULT: PASS. Both scripts deployed and S3-verified on push. Commit 92a18ce03 is what runs.

---

## Compiler Tools Log (Phase 3 -- After Commit)

### comp-pipescript deployed INF_D_02 / INF_D_00

Note: comp-pipescript deployed is keyed to the BD pipeline bucket (opal-data-bd). INF scripts are on opal-data-inf. The `safe-deploy gate PASS` in the pre-push hook is the authoritative deploy verification for INF pipeline. No filter match is expected; this is a known tool-scope limitation.

RESULT: safe-deploy PASS is the structural confirmation per §5.3 analogous limitation.

### comp-blast capital_gains_ttm

```
BLAST RADIUS: gold:INF_D_00.portal_aggregates:compute_firm_capital_gains_ttm
  GOLD_SCRIPT (1): INF_D_00.portal_aggregates:_nearest_date_row_per_account
WARNING: affects 1 downstream nodes
```

### comp-platinum reverse capital_gains_ttm (Phase 3 consumer check)

```
3 raw portal source hits (same as Phase 1):
  portal/src/api/endpoints/advisor-intelligence.ts:1013
  portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:571
  portal/src/pages/AdvisorIntelligence/_shared/types.ts:934
```

RESULT: PASS. Same 3 consumers as Phase 1 check. No new consumers added during the write window.

---

## Sentinel Verify (AC3 -- PASS)

### Gold Runner Dispatch

Full chain triggered via inf-gold-trigger Lambda at 2026-05-23T07:00:48Z. However, full chain aborted at step 4 (INF_API_PULL_ASSETS_V2 failed -- Orion API timeout, same root cause as 2026-05-20 SCALED anomaly). EC2 remained running.

Follow-up: SSM dispatch of `--single INF_D_02` sent directly to running instance (command_id: ce7ac274-e44f-4ad6-b5da-d0f02b7b784b). This mode syncs all code from S3 (pulling commit 92a18ce03 dual-emit) then runs INF_D_02 alone against existing platinum data. SSM Status: Success.

### AC3 Sentinel Results -- platinum/advisors/{advisor}/book.json

| Advisor | capital_gains_ttm | unrealized_gain_change_ttm | Identical |
|---|---|---|---|
| peter_lee | -54,807,679.9 | -54,807,679.9 | PASS |
| patrick_scanlan | -11,739,001.09 | -11,739,001.09 | PASS |
| joe_brandenburg | -4,893,738.15 | -4,893,738.15 | PASS |

All 3 advisors: both keys present, values identical. AC3 PASS.

### AC4 Computation-Unchanged Check

Pre-deploy (Phase-2 forensic book.json read): capital_gains_ttm = -54,807,679  
Post-deploy: capital_gains_ttm = -54,807,679.9  
Delta: $0.90 (< $1.00 rounding threshold). AC4 PASS.

---

## Phase B/C Plan (Banked -- Not In This TO)

**Phase B (DE-lane, gated on DE pod-4 re-spawn after LD-0014):**
- portal/src/pages/AdvisorIntelligence/_shared/types.ts:934 + :1100 -- rename type field
- portal/src/pages/AdvisorIntelligence/_shared/AdvisorBookView.tsx:571 -- swap consumer reference  
- portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx:839 -- swap consumer reference
- portal adapter layer -- swap accessor to NEW key + drop old-key fallback

**Phase C (DS-lane, gated on Phase B production-deploy verify):**
- Collapse dual-emit: remove `capital_gains_ttm` key emit from both gold scripts
- Single source of truth post-Phase-C: `unrealized_gain_change_ttm`

Shim-removal trigger: Phase C ships after Phase B confirms no portal read-breaks on the new key.

---

## AC Summary (Phase A)

| AC | Description | Result |
|---|---|---|
| AC1 | INF_D_02 emits both keys (advisor + household) | PASS |
| AC2 | INF_D_00 emits both keys (firm scope) | PASS |
| AC3 | Sentinel verify: 3 advisors, both keys, identical values | PASS |
| AC4 | Computation logic unchanged: pre/post delta < $1 | PASS |
| AC5 | Deploy cycle clean: safe-deploy PASS on both scripts | PASS |
| AC6 | Session log: Compiler Tools section with observed output | PASS (this document) |
| AC7 | Brief entry: dual-emit pattern + Phase B/C plan | PASS (this document) |
| AC8 | RAVC2 to COO + CC CVO with all evidence | SENT (see below) |

## RAVC2 Sent

RAVC2 dispatched to 2.0.0_SA_COO via MCP, CC 3.0.0_SA_CVO.
All 8 ACs evidenced. Phase A complete.
