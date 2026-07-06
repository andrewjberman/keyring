# Brief -> CTO: PRD request ADVI_INFFEE (Inflection fee-classification audit + revision)

**From:** 0.4.0_DE_ClientPlatform
**To:** 1.0.0_SA_CTO (PRD authoring)
**Date:** 2026-07-06
**Requested artifact:** PRD `ADVI_INFFEE` — audit + revise the Inflection fee-paying / non-fee-paying / total-account accounting so the Books "Firm Overview" and Distribution panels reconcile and are honest.
**Origin:** Andrew-direct (live portal smoke, 2026-07-06). Andrew flagged the numbers; DE investigated and ground-truthed against served artifacts + gold source.

---

## 1. Problem statement (what Andrew saw)

On the Inflection **Books tab -> Firm Overview** panel:

| Card | Value | Sub |
|---|---|---|
| Total AUM | $203M | as of 2026-07-02 |
| Fee-Paying Accounts | **789** | $136M AUM |
| Non-Fee-Paying Accounts | **1** | $67M AUM |
| Total Accounts | **868** | small (<$40k) |

Two things look wrong to the eye:
1. **Fee (789) + Non-fee (1) = 790, but Total Accounts = 868.** The row doesn't add up.
2. **1 non-fee-paying account holding $67M** — a third of the entire book in a single "account."

The **Distribution tab -> Segment Analytics** bell curve independently shows **Total Accounts 790** — agreeing with 789+1 but disagreeing with the Books "Total Accounts" (868).

## 2. Findings (grounded — served artifacts 07-06 12:55Z build + gold source)

**The frontend is a faithful passthrough. Every number is real; the defects are upstream in the data.** Three *different* "account" universes are being stitched into one card row:

| Number | Source artifact | Field | Grain |
|---|---|---|---|
| 789 fee / 1 non-fee / $136M / $67M | `s3://opal-data-inf/platinum/firm/header_metrics.json#total` | `fee_earning_account_count` / `non_fee_earning_account_count` / `fee_earning_aua` / `non_fee_earning_aua` | **billing** (790 accounts) |
| 868 Total Accounts | `clients_tab.json#headline.account_count` (= sum of accounts across 300 households) | `account_count` | **custody / holdings** |
| 790 bell curve | `header_metrics` account_count (789+1) | — | **billing** |

Stitch point (served `clients-tab-slim.json`, the Books N1 Lambda payload): builder `INF_D_04.build_clients_tab_slim` (`data/inf/scripts/gold/INF_D_04.client_portal_summary.py:4071-4079`) takes `account_count` from `clients_tab.json` (**868**, custody) but fee/non-fee counts from `header_metrics.total` (**789 / 1**, billing). Different artifacts, different grains, same card row.

### Root cause A — non-fee is a residual with mismatched denominators (data correctness)

`INF_D_04.client_portal_summary.py:798-802` (firm-total `_fee_block`):
```python
non_fee_aua      = max(0.0, total_aua - fee_earning_aua)          # residual on CUSTODY base ($202.5M)
non_fee_accounts = max(0, account_count - fee_earning_accounts)   # residual on BILLING base (790)
```
- `fee_earning_aua` ($135.5M) and `fee_earning_accounts` (789) are **positively measured** from the billing dim (`COUNT DISTINCT account_id WHERE is_fee_earning`).
- **Non-fee is a pure residual, and the AUA vs count residuals use different denominators.** The AUA residual subtracts from the full custody total ($202.5M / 868 accounts); the count residual subtracts from the billing count (790). Result: the $67M of un-billed AUA (dominated by 78 custody accounts with no billing row) collapses into a phantom **count of 1**.
- **Decisive tell it's not a real single account:** the same `header_metrics.total` reports **13 non-fee-paying *clients* but 1 non-fee-paying *account*** — impossible (1 account can't span 13 households). True non-fee/unbilled account count is ~**79** (868 custody - 789 fee-billed), not 1.
- Code already anticipated this class: `non_fee_earning_aua_status: 'residual_clipped_pending_canonical_rerun'` with `expected_value_post_rerun ~$19.6M` (`portal/src/pages/AdvisorIntelligence/_shared/types.ts:437-443`). Observed residual is **$67M**, ~$47M above the expected genuine value — i.e. ~$47M of AUA that *should* carry a fee classification is missing a billing record.

### Root cause B — billing-dim coverage gap (data completeness)

**868 custody accounts vs 790 billing accounts = 78 accounts with no billing-dim row at all.** The billing dim (`build_billing_dim.py`, silver) only covers 790 of the 868 custody accounts. Those 78 uncovered accounts are what inflate the non-fee AUA residual and cannot be fee-classified. Needs an audit of *why* they're absent (rep-coverage? account-type exclusion? join key?).

### Root cause C — cross-grain presentation (frontend)

Even with A + B fixed, the Books card row pairs a **custody-grain** "Total Accounts" (868, from `clients_tab`) with **billing-grain** fee splits (from `header_metrics`). Two different account universes will never visually reconcile as fee + nonfee = total. This is a DE-lane relabel/regrain fix. The Distribution bell curve (790, billing) and Books Total (868, custody) disagreeing is the same cross-grain issue surfacing twice.

## 3. Proposed PRD scope (ADVI_INFFEE)

**Goal:** the fee-paying / non-fee-paying / total-account figures are (a) internally consistent (fee + nonfee reconciles to total *on a stated grain*), (b) honest (no phantom "1 account = $67M"), and (c) grain-labeled so custody vs billing is never silently mixed.

**In scope:** audit the billing-dim coverage gap; replace residual non-fee counts with positively-measured counts (or an explicit "unclassified/unbilled" bucket); make the served `header_metrics` + `clients_tab` + `clients-tab-slim` grain-coherent; align the Distribution bell-curve total with the Books total; FE presentation so the panel reconciles or clearly labels grains. Applies to Inflection first; check 49F for the same residual pattern (`_fee_block` is shared shape).

**Out of scope:** the broader WS-4 AC-2 vintage/as_of work (separate, in-flight).

## 4. Suggested TO decomposition (Andrew-specified owners)

| TO | Owner | Scope |
|---|---|---|
| ADVI_INFFEE.TO-1 (audit) | **0.6.1_AE_PartnerETL** | Audit the billing-dim coverage gap: why 78 of 868 custody accounts have no billing row (`build_billing_dim.py` + upstream silver / Orion billing feed). Quantify the true fee vs non-fee vs unbilled populations at account grain. Root-cause whether ~$47M is genuinely fee-earning-but-unbilled or genuinely non-fee. |
| ADVI_INFFEE.TO-2 (gold revise) | **0.4.0_DS_ClientPlatform~A** | Revise `INF_D_04` fee-block: emit positively-measured non-fee account count (not `account_count - fee`), coherent denominators for AUA vs count, and a stated grain (or explicit unbilled/unclassified bucket). Reconcile `header_metrics.account_count` (790) vs `clients_tab.account_count` (868) into one documented model. Re-emit + verify served artifacts. |
| ADVI_INFFEE.TO-3 (frontend) | **0.4.0_DE_ClientPlatform** (me) | Repoint / regrain the Books "Firm Overview" cards + Distribution bell-curve total to the reconciled grain; label custody vs billing where both are shown; surface an "unbilled/unclassified" bucket if DS emits one so fee + nonfee + unclassified = total on-screen. Render-verify against the re-emitted artifacts. |

Sequencing: TO-1 (audit) informs TO-2 (gold model), TO-2 emits inform TO-3 (FE). Coordinate on the shared artifacts (`header_metrics.json`, `clients_tab.json`, `clients-tab-slim.json`) via `<cross_domain_coordination>`.

## 5. Suggested acceptance criteria (machine-checkable)

- Served `clients-tab-slim.json#headline`: `fee_earning_account_count + non_fee_earning_account_count + unclassified_account_count == account_count` (on one stated grain), and `non_fee_earning_client_count` is consistent with `non_fee_earning_account_count` (no 13-clients-1-account impossibility).
- No non-fee bucket where a single account carries a firm-material share (e.g. > 5%) of AUA unless positively confirmed as one real account.
- Books "Total Accounts" and Distribution bell-curve "Total Accounts" render the **same** number (or are explicitly labeled different grains).
- 49F checked for the same residual pattern; documented clean or fixed.

## 6. Grounding (Rule 22 — mechanism is source-confirmed, not inferred)

- Served (07-06 12:55Z build): `header_metrics.json#total` = {account_count 790, fee 789, nonfee 1, fee_aua 135,541,810.96, nonfee_aua 67,001,038.85, fee_clients 294, nonfee_clients 13}; `clients_tab.json#headline` = {account_count 868, client_count 300}; sum of 300 households' account_count = 868; sum of households' total_aua = $202,542,849.81.
- Source: `data/inf/scripts/gold/INF_D_04.client_portal_summary.py` — residual `:798-802`, per-advisor residual `:3691-3698`, slim stitch `:4071-4079`, positive fee measurement `:793-796`.
- Frontend passthrough: `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx:831-857` (card build), `panels/ConsolidatedOverviewPanel.tsx` (render), `types.ts:437-443` (known residual-clip flag).
