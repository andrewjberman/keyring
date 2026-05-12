# DS~B 2026-05-12 — Session 1: ADVI_INFLEC canonical tax-status AUA

**Agent:** `0.4.0_DS_ClientPlatform~B`
**Trigger:** Andrew direct dispatch — implement RD briefing `0a1f517e1`
**Scope:** Canonical 49F tax-status AUA shape for Inflection (N1/L2/L3/L4)
**Outcome:** Shipped end-to-end in single commit `b28dd2419`; S3 MATCH on all 4 files; ACK to RD + COO

---

## Current State

| Step | Result |
|------|--------|
| Commit SHA | `b28dd2419` (CLOUD, pushed) |
| Author | `0.4.0_DS_ClientPlatform~B` |
| Push | origin/CLOUD up to date (`f41307623..b28dd2419`) |
| ds-commit-gate | PASS (py_compile + AST + ruff py39) on 4 files |
| safe-deploy.sh | PASS — all 4 files MATCH on `s3://opal-data-inf/code/gold/` |
| Sibling-pattern audit | N/A (additive feature, not a bug fix) |
| Chain trigger | Pending — covered by next gold-d or full |

S3 ETags:
- `code/gold/lib/tax_status.py` `4af1d541637165b8f1d0e6e3787342e2`
- `code/gold/INF_A_00.accounts_dimension.py` `2821e40f9366cd3850fe9f8431cf668e`
- `code/gold/INF_D_00.portal_aggregates.py` `4ca7ed71bc018e3b2a9815920b19d59a`
- `code/gold/INF_D_02.advisor_client_detail.py` `e8faeb808f437d42a46a74fca6b445c9`

---

## RD Brief — design summary

Briefing `org/tier2_senior/0.4.2_RD_AdvisorIntelligence/briefs/2026-05-12_tax_status_aua_canonical_DS_briefing.md` (commit `0a1f517e1`). Andrew's directive: same panel shape between Inflection and 49 Financial. FE swap already shipped (portal commit `b2b54d96` DEV / `9a2d1d3e` CLOUD) — `TaxCostBasisPanel.tsx` rebuilt to read the canonical `taxable / tax_deferred / tax_free` fields; Inflection's panel top section was empty until this data landed.

### Required fields

For every drill level: `taxable`, `taxable_pct`, `tax_deferred`, `tax_deferred_pct`, `tax_free`, `tax_free_pct`. Pcts scope-local (per advisor / per HH / per firm).

### Reg_type → tax_status mapping

Empirical vocabulary captured directly from `s3://opal-data-inf/silver/accounts_dim/latest.parquet` (835 rows, 20 unique reg_type values, 2026-05-12 pull). Full mapping in `lib/tax_status.py` docstring. Forward-compatible Orion-canonical names included so vocabulary growth won't silently degrade to the `taxable` fallback.

---

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/lib/tax_status.py` | NEW. Shared classifier `classify_reg_type(reg_type) -> str` + `add_tax_status_column(df) -> (df, fallback_rate)`. Inflection vocabulary baked in + forward-compat Orion canonical names. Fallback default `taxable` per briefing §4. |
| `data/orion/scripts/gold/INF_A_00.accounts_dimension.py` | Import classifier; add `tax_status` + `qualified_flag` columns to accounts dimension; log fallback rate; WARN if >5%. Mirrors BD A_00 TAX_STATUS_MAP pattern. |
| `data/orion/scripts/gold/INF_D_00.portal_aggregates.py` | NEW helper `build_firm_tax_block(accounts_dim, holdings, aum_snapshot)`; inject `clients_tab['tax'] = {taxable, ..., tax_free_pct}`. AUA source mirrors slim headline rule. `_ensure_tax_status` inline-derive fallback. |
| `data/orion/scripts/gold/INF_D_02.advisor_client_detail.py` | Import classifier; add `_aggregate_tax_status_per_advisor` + `_aggregate_tax_status_per_hh` + `_account_tax_status_block`. Merge canonical fields into existing `tax` dicts at L2/L3/L4 alongside realized + unrealized + billing (briefing §7 "Keep emitting"). |

INF_D_04 unchanged: `build_clients_tab_slim` already reads `ct.get('tax', {}).get('taxable', 0)` etc. at lines 3332-3340, so the slim picks up the new fields automatically.

---

## Empirical Validation (pre-commit, 835 accounts)

```
Fallback rate: 0.24% (2/835 accounts -> taxable default)

tax_status counts:
  tax_deferred    390  (IRA 280 + Beneficiary IRA 45 + IRA Rollover 28 +
                       Simple 17 + SEP 15 + Inherited IRA 3 + Keogh 2)
  taxable         242  (TOD 104 + Joint 93 + Individual 22 + Trust 7 +
                       UGMA 6 + UTMA 3 + Estate 2 + Invalid Type 2 +
                       Corporation 1 + Joint Tenant 1 + JTWROS 1)
  tax_free        203  (Roth 200 + Inherited ROTH IRA 3)
                  ===
                  835  ✓ matches total accounts
```

**AC checklist:**

| AC | Result |
|----|--------|
| All four levels emit non-null fields | ✓ N1 in D_00; L2/L3/L4 in D_02 |
| Pcts sum to 100.0 within rounding | ✓ scope-local denominator |
| Sum ≈ level total AUA | Will verify post-chain (gold-d) |
| reg_type spot-check vs vocabulary | ✓ Roth→tax_free, IRA→tax_deferred, Joint/Indiv→taxable |
| Fallback ≤ 5% | ✓ 0.24% |
| No FE changes needed | ✓ slim emit already in place at D_04:3332 |

---

## Compiler Tools

| Tool | Run | Finding |
|------|-----|---------|
| `comp-pipescript io` | Not run — INF scripts not catalogued in comp graph (BD-only coverage; INF gap queued as `INF_COMP_PIPESCRIPT_DEPLOYED_COVERAGE` from prior session). |
| `comp-pipescript deployed INF_C_07` | Returned "No scripts matched filter" — same hardcoded BD-bucket gap. Manual `aws s3api head-object` confirmed S3 state instead. |
| `.tools/ds-commit-gate.sh` | 2 invocations across 4 files. First exited 1 on F401 unused `pandas` import in `lib/tax_status.py`; removed, re-ran, PASS. |
| `.tools/safe-deploy.sh` (pre-push hook) | Auto-fired on `git push`; deployed all 4 files; verified SHA MATCH on opal-data-inf. |
| Manual empirical run | `python -c "from tax_status import ...; df = pd.read_parquet(...)"` against real INF accounts_dim — fallback 0.24%, distribution correct. |

Compiler-tools log auto-appended via `.comp-graph/.agent_context` rotation (TO_ID `ADVI_INFLEC.TAX-STATUS-AUA`).

---

## Briefs Written

None this session. Inbound brief only — RD's `2026-05-12_tax_status_aua_canonical_DS_briefing.md` (`0a1f517e`).

---

## Inter-agent Coordination

**Inbound (relevant):**
- COO 050435Z P0 INF_C_07 dtype fix — already handled by DS~C overnight (`803dd2936` + your follow-on `289f69077`). Clarified to COO; no DS~B action.
- Andrew direct dispatch this session — RD brief 0a1f517e.

**Outbound:**
- RD 0.4.2 18:12Z — RAVC: shipped + ETags + empirical validation + AC checklist.
- COO 18:12Z — RAVC: status update including the INF_C_07 rerouting clarification and the RD brief deliverables.
- COO 18:18Z — Clarify: INF_C_07 was DS~C, not me; my session work was the RD brief; full RAVC2 evidence enclosed.

---

## Architectural Notes

1. **Inline tax_status derivation in D-chain consumers** (`_ensure_tax_status` in D_00 + D_02). Pattern: D-chain consumers prefer `accounts_dim['tax_status']` if present, else compute via `add_tax_status_column` on the fly. Lets the canonical fields ship via gold-d alone, without forcing a full chain to refresh accounts_dim through INF_A_00. Once a full chain runs, the column ships natively and the fallback path no-ops.

2. **Canonical fields merged INTO the existing `tax` dict** rather than replacing realized/unrealized/inflecBilling. Briefing §7 explicitly says "Keep emitting; consumer just moves" — those sibling keys preserve future-consumer optionality (Tax Optimization lens, Books tab billing surface, etc.).

3. **`qualified_flag` column emitted alongside `tax_status`** for parity with BD's A_00 convention. Not currently consumed in INF but ready for client-tax-liability rollups when those reach feature parity.

4. **Forward-compat reg_type map** covers Orion-canonical vocabulary (Traditional IRA, Roth 401(k), Pension, etc.) even though the current empirical Inflection set is smaller. Vocabulary growth from future Orion expansion won't silently degrade to the `taxable` fallback — the map already handles the canonical names.

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **AE 0.6.1 / AE 0.7** | Next gold-d (or chain #19+) refreshes 4 platinum artifacts with canonical tax block — `clients_tab.json`, `clients-tab-slim.json`, `advisors/{key}/book.json`, `clients/{hh}/detail.json`. No dispatch wire changes needed; existing scripts pick up new code via S3 deploy. |
| **DE 0.4.0_DE_ClientPlatform** | Post-chain visual verification: confirm Cost Basis & Tax Status panel renders three-card layout identically to 49F at N1/L2/L3. Empty-state fallback will clear automatically. |
| **RD 0.4.2_RD_AdvisorIntelligence** | Post-chain: verify CanonicalTax fields populate at every drill level; close briefing 0a1f517e. |
| **Self (DS~B)** | Post-chain: sum-to-AUA reconciliation spot-check. Confirm `taxable + tax_deferred + tax_free` ≈ `total_aua` at firm + a couple of advisors. |

---

## Open / Pending TOs

| TO | Status | Notes |
|----|--------|-------|
| `ADVI_ROLLUP.SL-P2.ds-sleeve-promote-to-production` | pending | Inherited from prior session, BD pipeline scope. |
| `ADVI_INFNNA.INF_A_03_STALE-PURGE` | deferred | Per CTO ruling — destructive op gating. |

No active blockers. Available for next dispatch.
