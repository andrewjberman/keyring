# P3-prep — Cottonwood (COT): Advisor/Office Dimension Scope + the §6.1 Open-Decision

**Author:** 0.4.0_DS_ClientPlatform
**Date:** 2026-06-08
**Project:** ADVI_CCAETL (P3-prep)
**Companions:** Brief 1 (HAR/API), Brief 2 (field population §6.1 flag), Brief 3 (medallion port §5.1)
**Purpose:** Scope what a COT `office_mapping`/advisor-dimension equivalent needs, and sharpen the §6.1 advisor-gap open-decision into a concrete, empirically-grounded question for Andrew. **Per COO: do NOT build the C_07 COT variant until Andrew rules §6.1.**

---

## 1. The 49F advisor/office structure (what we'd be porting)

49F's advisor analytics are driven by 6 `config/office_mapping/*.csv` files + `C_07.advisor_attribution.py`:

| Asset | Rows | What it is |
|---|---|---|
| `advisor_registry_all_roles_clean.csv` | 178 | Canonical advisor roster across **5 role types**: architect / implementor / consultant / local_ops / additional_advisor |
| `advisor_registry_lusha_office_bridge_clean.csv` | 178 | **Lusha-enriched** person→office map (matched_full_name, job_title, city, state, linkedin, office, mapping_method) — built because 49F's advisor→office link was incomplete and needed external enrichment |
| `account_role_office_assignments_long_clean.csv` | 19,597 | account × role × advisor × office |
| `relationship_role_office_assignments_long_clean.csv` | 8,857 | relationship × role × advisor × office |
| `account_office_rollup_clean.csv` | 5,806 | account → office rollup |
| `relationship_office_rollup_clean.csv` | 2,743 | relationship → office rollup |

**`C_07.advisor_attribution.py`** consumes these → produces `gold/views/account_team.parquet` (architect/implementor/consultant/local_ops/additional_advisor per account) + `relationship_team` rollup. Its core logic is **49F-specific**: the `'49F House'` placeholder handling, and a 3-layer architect/implementor **pairing-table** attribution (modal implementor → architect inference at ≥60% threshold).

**Downstream advisor consumers:** `D_01.partner_analytics` (the **adv** view / architect cohort), `D_00c.portal_leaderboard` (architect/implementor leaderboards), `D_00b.portal_timeseries`. The AUA/NNA/geo/client views do **not** depend on the advisor dimension.

---

## 2. The COT reframe — advisor data EXISTS, but the model differs (empirical, from the HAR catalog)

Brief 2 flagged COT's `DST Rep Name` as 99% "No RepName Assigned" — which read as "COT has no advisor dimension." **The DataMining `DimensionsFacts` catalog (queryTypeId=1) corrects that:** COT's BD *does* carry advisor + office structure, just in **different fields than the ones Andrew's `CW_Transactions_Rich` template selected** (it pulled only `repName` = DST Rep Name, the empty one).

**Account-level advisor candidates (available, population untested):**
| id | mappedColumn | name |
|---|---|---|
| 48388 | `accountUDF1` | **Advisor of Record Name & B2B ID** ← most likely the primary COT advisor field (Salentica/CRM UDF) |
| 27 | `manager` | Manager |
| 49113 | `managedAccountManagerName` | Managed Account Manager Name |
| 48392 | `accountUDF5` | Team Name - Salentica |
| 35884 | `accountBillingTeamName` | Account - Billing Team Name |
| 60 | `repCode` | Rep Code |
| 14606 | `repName` | DST Rep Name (the 99%-empty one Andrew pulled) |

**Team-level office/geo (id=1 level) — NATIVE, fully structured:**
`team`, `teamDisplayName`, `teamAddress1/2`, `teamCity`, `teamState`, `teamZipCode`, `teamPhone`, `teamPrimaryEmail`.

### Two structural consequences

1. **COT's advisor model is single-"Advisor of Record" + Team, NOT 49F's 5-role architect/implementor team.** So **C_07 does not port as-is** — its architect/implementor pairing logic has no COT analog. A COT advisor dimension would be a *simpler, different* build (Advisor of Record → Team → office), not a port.
2. **COT likely needs NO Lusha enrichment.** 49F needed the Lusha office-bridge because its advisor→office link was incomplete. COT's BD carries a **native Team dimension with full office address/city/state** — the office/geo comes straight from BD. This is a meaningful simplification (no external enrichment pass, no 178-name Lusha cache to build).

---

## 3. The §6.1 open-decision — sharpened for Andrew's ruling

The question is no longer "does COT have advisors?" but **"which COT advisor fields are populated, and do we want the advisor-dimension analytics for COT v1?"** This needs one cheap empirical probe + one product call.

**Empirical probe (cheap, gates the rest):** pull a small COT DataMining export adding `accountUDF1` (Advisor of Record), `manager`, `accountUDF5` (Team), `repCode`, and the Team-level office fields, and measure population (same method as Brief 2). Andrew can run this by hand in BD in minutes (build a template like CW_Transactions_Rich + these columns), OR it waits for P0 auth infra. **This is the single fact that resolves §6.1.**

**Three scope outcomes:**

| Outcome | Condition | Gold-D scope |
|---|---|---|
| **A — usable advisor dim (simpler than 49F)** | `accountUDF1`/`manager` populated | Build a **COT-specific** advisor attribution (Advisor of Record + Team→office; native geo, **no Lusha**). Adv-cohort (D_01) + a simplified leaderboard feasible. **Not** a C_07 port. |
| **B — no advisor dim** | all advisor fields empty | **Skip** C_07 / adv-view / leaderboards for v1. AUA / NNA / geo / client views fully work (geo confirmed real, Brief 2). Gold-D scope simplifies. |
| **C — partial** | some populated | Degrade gracefully (AC4 spirit) — build adv dim where present, null elsewhere. |

**Geo analytics work in ALL outcomes** — client state/city are populated (Brief 2, 87% TX), and the Team dimension adds office-level geo. The §6.1 ruling only gates the **advisor** dimension (attribution, adv-cohort, architect leaderboard), not geo/AUA/NNA/client.

---

## 4. Recommendation

1. **Hold the C_07 COT variant** (per COO) — and note it's a *rebuild*, not a port, if Outcome A.
2. **Andrew §6.1 ruling needs the probe in §3** — recommend Andrew pull the advisor-field probe export by hand (fastest path; no P0 dependency) so the ruling is empirical, not assumed (Standard §3 discipline).
3. **If Outcome A:** the COT advisor build is *cheaper* than the 49F one (native Team office, no Lusha, single advisor-of-record vs 5-role pairing logic). Budget accordingly — don't carry the 49F Lusha-pass cost into COT estimates.
4. **COT advisor-roster research for a Lusha pass (COO's P3-prep item): likely UNNEEDED** — the native Team dimension supplies office/geo. Defer the Lusha-pass scoping unless the probe shows advisor names present but office/team absent (unlikely given the Team level exists).

---

## 5. What a COT office_mapping equivalent needs (if Outcome A)

Far less than 49F:
- A COT advisor registry derived from `accountUDF1`/`manager` (not a 5-role architect/implementor registry).
- The account→advisor→team assignment table — **directly from the BD Account+Team dimensions**, no enrichment.
- Office rollups from the Team dimension (native city/state) — no Lusha bridge.
- A COT-specific (simpler) `C_07` analog, authored fresh — gated on the §6.1 ruling.

---

## 6. Bottom line

COT's advisor gap is a **field-selection + model-difference** issue, not a data-absence one. COT's BD carries advisor data (`accountUDF1` Advisor-of-Record, `manager`, Salentica team) and **native office/geo** (Team dimension) — but in a simpler single-advisor model that does **not** match 49F's 5-role architect/implementor structure, so C_07 is a COT-specific rebuild (not a port) and likely needs **no Lusha pass**. The §6.1 ruling reduces to one cheap probe (measure `accountUDF1`/`manager`/Team population) + Andrew's product call on whether COT v1 carries advisor analytics. Geo/AUA/NNA/client views are unaffected and proceed regardless. C_07 COT build held pending the ruling.
