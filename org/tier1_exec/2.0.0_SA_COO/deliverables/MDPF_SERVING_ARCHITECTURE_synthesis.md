# MDPF Serving Architecture -- Synthesis (P1-P3)

**Author:** `2.0.0_SA_COO`. **Date:** 2026-07-23. **Status:** GROUNDED CORE (byte-verified tonight) + PENDING DE's full read-surface enumeration (the estate-wide denominator).
**Purpose (Andrew-direct):** *"identifying what the actual architecture for these artifacts is so we can make sure that our infrastructure, particularly that which is on a daily schedule to regenerate and store these artifacts, is fitting into the structure of the actual portal consumption... keeping various firm data partitioned as well as accounting for the aggregate data for the Global view."* -- "100% clarity as we build out our opal-data-assets infrastructure."
**Program owner:** CTO (P1-P4 phasing, msg 20260723T200227Z). **This doc:** the COO synthesis wrapping P1-P3 (CTO-assigned). **Landings referenced:** the scope-coverage gate doctrine (CTO ruling 20260723T222919Z, comp-learns-backlog @b4fca85ea).

---

## 0. Why this exists, and what grounds it
The MDPF Global-view product completed 2026-07-23 (promotes v2.1.145-148, all tag-verified, DOM-confirmed on live PROD 17256834). In closing it, the **consumed keys and the producer->consumer coupling were byte-verified against the served bytes** -- not asserted from memory or a comment. This doc captures that as the durable architecture record so the daily-regeneration infrastructure is built to the ACTUAL consumption, not a parallel guess. Tonight produced two live proofs that the guess-vs-actual gap is real and expensive: **two stale-sibling key traps** (W-6, W-7), each caught only because the consumed key was exercise-verified. Those are §2's motivating cases.

## 1. Consumption map (P1) -- what the portal actually reads
The MDPF `ModelPortfolios` view resolves its artifacts through `portal-proxy.ts` (firmId-interpolated paths), CloudFront `/json/*` static rewrite, to `s3://opal-data-portal-v2`. **Pinned to the deployed line + EXERCISE-verified** (the $1.78B->$1.95B flip landed on the /global/ key, proving the consumer):

| View / element | queryKey + fn | S3 CONSUMED key (opal-data-portal-v2) | Verification |
|---|---|---|---|
| Global aggregate + count | `['mdpf-aggregate-timeseries','global']` -> `getMdpfAggregateAUATimeSeriesByFirm('global')` (portal-proxy.ts:511) | `json/mdpf/global/aggregate-aua-timeseries.json` | md5 55a8b379, $1,951,676,164.42 + account_count_total, byte-verified + co-signed |
| Per-firm aggregate + count | `getMdpfAggregateAUATimeSeriesByFirm('{firmId}')`; per-firm query `enabled: effectiveFirmId !== 'global'` | `json/mdpf/{49financial\|inflection\|cottonwood}/aggregate-aua-timeseries.json` | 3 firms byte-verified (49F 501407 / INF e3c8db3 / COT 194e5bb), counts co-signed |
| Global account-distribution (bell) | `['account-distribution']` -> `getAccountDistribution()` (ModelPortfolios.tsx:576,1243; aum.ts:552) | `json/portfolios/account-distribution.json` | md5 f45c37e1, 3-firm (294 COT folded) |
| Per-firm account-distribution | `getAccountDistributionByFirm` (gated off for 'global') | `json/mdpf/{firmId}/account-distribution.json` | firm-partitioned |

**Load-bearing facts:**
- The Global aggregate consumes `json/mdpf/global/...`, NOT the top-level `json/mdpf/aggregate-aua-timeseries.json` sibling (which exists but no consumer reads -- the W-7 trap).
- The Global bell consumes `json/portfolios/account-distribution.json`, NOT the `json/mdpf/global/account-distribution.json` sibling (the W-6 trap).
- Consumer identity is settled by **observed behavior on the live instance** (which key the deployed bundle reads), not by a filename's apparent meaning. A line-pin alone is necessary but not sufficient; the exercise (which key the fix landed on) is the proof.

**PENDING (P1 completion, DE):** the estate-wide read-surface enumeration -- EVERY consumed artifact -> exact bucket+key+tier (json/ vs any platinum/ dual-path per key) -> queryKey/fn -> firm-partition-or-aggregate class -> FE-composed-vs-published flag. This §is the MDPF slice; DE's enumeration is the full denominator everything else keys on.

## 2. Producer/consumer parity (P2) -- the coupling and its failure mode
**The failure mode, twice tonight:** a producer wrote the right bytes to the WRONG key -- a key no consumer reads -- while the consumed key stayed stale. W-6: the bell published to the mdpf/global sibling while the view read json/portfolios. W-7: the count published to the top-level while the view read /global/. Both were caught by asking "which key does the view ACTUALLY read?" and exercise-verifying it, BEFORE the render wired against the stale key.

**The invariant:** the **publish set MUST be DERIVED from the consumption map (§1)**, never maintained as a parallel hand-list. Two lists drift; one enumeration cannot. The P2 parity instrument makes them ONE: a consumed key with no producer, or a producer writing an unconsumed key, **FAILS a structural check that runs as an instrument, not a review** (the registration-invariant pattern -- same shape as comp-manifest-check for comp-tools).

**The scope-coverage sub-doctrine (CTO ruling 20260723T222919Z, banked @b4fca85ea):** *a control inherits the scope it was written in; a change does not.* Before a mutant/control runs, **enumerate the scopes/axes a change can reach** (shared component -> every view it renders; contract -> every scope that applies it; producer -> every tier that serves it) and carry a control per scope; an un-exercised scope is named **UNCOVERED** in the evidence, never silently passed. Three escapes of this one class tonight: (a) v2.1.147's W-3b anchor mutant was per-firm-scoped and could not falsify the Global mis-application; (b) the producer/consumer parity gap (blind to the serve-tier axis); (c) the count co-sign (per-firm 0 cliffs / global 22 -- the cliff lived only in aggregation). This is the P2 instrument's design requirement: per-scope controls.

## 3. Firm-partition security (P3) -- physical partitioning + aggregate-for-Global
**Requirement (Andrew-direct):** firms physically receive ONLY their own firm's data; Opal employees receive the aggregate (Global) + all firm-level items. Baked into KEY STRUCTURE + IAM/CF behavior, not enforced in the FE.
- Per-firm artifacts live under a firm-prefixed key (`json/mdpf/{firmId}/...`) a firm's access can reach; the aggregate (`json/mdpf/global/...`) is Opal-only.
- DS's firm-isolation design (`org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/MDPF_FIRM_ACCESS_ISOLATION_DESIGN_20260723.md`) folds in as input; the estate already solves this one level down via the AdvisorIntelligence scoped router (a proven pattern, not net-new). Ratifies at CTO's gate, coordinated with PORTAL_AUTHHARD (CTO~B) + the firm-sep law, then TF/policy through the normal cycle with the 22a IAM battery (per-`(action, resource)` simulate-principal-policy, one --resource-arns per call).
- **THREE OPEN QUESTIONS AT ANDREW (P3 gating, surfaced via /open-calls):** (1) the identity source for Opal-vs-firm (m365/Entra group / portal user-table role / auth-provider claim); (2) do firm users consume via the portal, or is the requirement per-firm DELIVERY to firm-owned destinations; (3) confirm the aggregate/Global is strictly Opal-only.

## 4. Generation contracts (P4) -- daily regeneration fitting consumption
- The daily producers write to the **consumed keys (§1)** -- the publish set derived from the consumption map (§2), not a parallel list.
- Two-write per Andrew's architecture: **gold-append** (`opal-data-assets/gold/mdpf/...` -- heavy full-history archive) + **portal-overwrite** (`opal-data-portal-v2/json/...` -- light current view the portal reads). History in the assets bucket; the portal bucket stays light.
- Each artifact carries a generation contract (DS preamble family @077c06738); the server-side generator is built to those; **first-emit byte-ties the bridge artifacts** (the standing conformance condition) before scheduling becomes config. Correct-by-construction = P2's parity gate + P4's contracts together.

## 5. Open items (the completion path)
- **P1 full enumeration** (DE) -- the estate-wide read-surface map; completes §1 as the denominator.
- **P2 parity instrument** build (DS + 0.7.0 on P1's output) -- the structural check; publisher key-map DERIVES from the consumption map.
- **P3 security** -- the 3 Andrew questions above, then the design ratifies at CTO's gate.
- **P4 generation contracts** -> generator -> byte-tie cutover -> scheduling as config.
- **scope-coverage gate** -- binding now on DE/DT/DS acceptance batteries (CTO ruling); flips to BUILT when scope-enumeration lands in the batteries + P2 instrument.
- **nm-vintage residual** ($514K, MDPF tooltip Non-Model roll-forward) -- re-source the tooltip nm to the aggregate's frontier vintage, or await non_model_assets emission; tomorrow-class.

## 6. The one principle that unifies this
**The consumption map is the denominator; everything -- the publish set, the parity instrument, the firm-partition, the generation contracts -- DERIVES from it.** The night's two escaped-then-caught traps and the three scope-coverage escapes all reduce to the same root: a producer/control reasoning from its own list/scope instead of from the one enumeration of what the consumer actually reads and every scope a change actually touches. Correct-by-construction means there is ONE enumeration, and every producer and control is generated from it.

-- `2.0.0_SA_COO`, 2026-07-23. Grounded core; DE's P1 enumeration completes it.
