# MDPF_ASSETS.027 -- SmartX 49F-coverage feasibility probe -- findings

| | |
|---|---|
| **TO** | MDPF_ASSETS.027.ds-smartx-49f-coverage-feasibility-probe |
| **Author** | 0.4.0_DS_ClientPlatform~B |
| **Date** | 2026-05-20 |
| **For** | 1.0.0_SA_CTO~B (PRD v0.9 amendment) | CC 2.0.0_SA_COO~B |
| **Status** | COMPLETE -- non-mutating probe (no code, no artifact, no deploy) |
| **Method** | Read-only: the prior live SmartX API-surface probes (MDPF_ASSETS.011 2026-05-18, SXPL_RESTIN.001 2026-05-15) + an empirical read of the live WS-B SmartX-pull feeder partition (2026-05-20). |

---

## Verdict (AC3)

**OUTCOME (b) -- Schwab-based fallback.** Andrew's stated preference,
SmartX-direct, is NOT feasible: SmartX cannot yield a 49F non-model (1b)
figure at all. AND -- the headline finding -- the mandate's premise is
empirically inconsistent: **"what SmartX covers" is $1,374.2M, not ~$1.65B.**
The ~$1.65B / ~$1.75B figures in the mandate are the Schwab-custodied book,
which SmartX does not cover. CTO~B + Andrew need to disambiguate which the
mandate means (see "Mandate inconsistency" below) before PRD v0.9.

---

## Q1 -- Can SmartX directly yield a clean 1b (49F non-model)? NO.

SmartX, on the available `opal7` Manager-role credential, exposes ONLY
per-Opal-model allocation data. Every endpoint in the probed API surface is
model-scoped:
- SXPL_RESTIN.001 (2026-05-15) probed 13 endpoints x 7 models -- ALL are
  `models/`, `reportedmodels/`, or `enterprises/{aum,allocations,advisors}
  ?modelid=` -- model-keyed. None exposes a non-model or whole-account view.
- MDPF_ASSETS.011 (2026-05-18) probed the account surface directly:
  `enterprises/accounts` (the 49F enterprise account list) returns **401
  Unauthorized** -- "opal7 is not an administrator and does not have access to
  [49 Financial's enterprise]". `accounts/{id}` returns 401 on every variant.
  `users/access` for opal7 shows `accountAccess: []` -- zero account grants.

SmartX places 49F's Opal-model trades at Schwab, so it knows the model book --
but the `opal7` credential is a pure model-Manager role, walled off from the
enterprise account list. 49F's NON-model assets (held-away, direct, cash, any
account not allocated to an Opal model) are not visible on SmartX at all.
There is no endpoint, accessible or otherwise on this credential, from which a
clean 1b can be read. (A higher-privilege 49F-enterprise SmartX credential
would change this -- that is an access request to Andrew/49F, not engineering;
MDPF_ASSETS.011 already flagged it.)

## Q2 -- Disjoint buckets vs residual? SmartX gives 1a + 1c disjoint; 1b absent.

Within SmartX, Cohort 1a (Opal models) and 1c (Opal SMAs) ARE cleanly
disjoint: each `enterprises/allocations` row is one account allocated to one
specific model, and the registry `model_type` flags which of the 7 models are
`sma`. They are additive and separately summable. BUT 1b is simply NOT in
SmartX's data at all -- so there is no SmartX-direct additive `1a + 1b + 1c`.
1b can only ever be a RESIDUAL against a non-SmartX 49F total (the Schwab book
or the full BD book). The v0.8 "is 1c nested inside 1b" question does not arise
on the SmartX side -- SmartX separates 1a and 1c explicitly; the nesting only
exists on whichever residual basis supplies 1b.

## Q3 -- Empirical SmartX-covered sum (2026-05-20). $1,374.2M -- NOT ~$1.65B.

Read live from the WS-B SmartX-pull feeder partition
`s3://opal-data-mdpf/mdpf/feeds/model_aua_positions/49financial/2026-05-20.parquet`
(the daily product of a real SmartX `enterprises/allocations` pull, 6,880
open allocations):

| Cohort | Source | 2026-05-20 |
|--------|--------|-----------|
| 1a (Opal models) | SmartX, 6,786 model allocations | $1,349,272,608.00 |
| 1c (Opal SMAs) | SmartX, 94 sma allocations | $24,929,683.38 |
| **SmartX-covered TOTAL (1a + 1c)** | | **$1,374,202,291.38** |

SmartX-covered 49F = **$1.374B**. The mandate expected ~$1.65B. The gap
(~$280M) IS the 49F non-model book -- which SmartX does not see. For
reference, the full BD book `certified_aua` (2026-05-20) = $1,812,084,304.28;
the Schwab-custodied 49F book ~$1.65B (MDPF_ASSETS.011: Schwab RPS covers ~95%
of "49F's ~$1.68B Schwab book").

## Q4 -- The Schwab fallback (the feasible mechanism).

Since SmartX cannot supply 1b, 1b must be a residual against a non-SmartX 49F
total. To hit the mandate's ~$1.65B 49F basis, that total is the
Schwab-custodied book:

  1b (49F non-model) = Schwab_49F_book - model_aua(1a)   [SMA-inclusive]

The Schwab book is available two ways:
- (i) Schwab RPS silver -- `s3://opal-data-schwab/silver/RPS/date={d}/` --
  per-account position grain, ~95% coverage of the ~$1.68B Schwab book
  (MDPF_ASSETS.011 verified).
- (ii) the WS-E `compute_partner_custody_total` Schwab account->custodian
  crosswalk path -- which produced the original ~$1,655M Schwab-only basis.
  NOTE: this crosswalk machinery was RETIRED in MDPF_ASSETS.025 / .016
  Correction 7 (the WS-E LEGACY block deleted, `build_custody_crosswalk_cache.py`
  removed) because the v0.7 Ruling-2 basis had moved off Schwab to the full BD
  book. Under Mandate Change 3 the Schwab basis is wanted again -- CTO~B's
  re-scope must either revive that path or build 1b off Schwab RPS silver (ii).

1a + 1c stay as today (the WS-B SmartX pull). 1b switches from the v0.7
certified_aua residual to a Schwab-book residual.

## Mandate inconsistency -- needs an Andrew disambiguation (for CTO~B)

The mandate as relayed -- "Cohort 1 (49F) = ONLY what SmartX covers (~$1.65B)"
-- is internally inconsistent. "What SmartX covers" and "~$1.65B" are two
different numbers. Two readings, two different headlines:

| Reading | 49F basis | 1b | 49F total | Headline (+2a ~$93.7M) |
|---------|-----------|----|-----------|-----------------------|
| **A -- literal "only what SmartX covers"** | SmartX model+sma only | none (SmartX has no 1b) | $1.374B | ~$1.468B |
| **B -- "the ~$1.65B Schwab figure"** | Schwab-custodied book | Schwab-book residual | ~$1.65B | ~$1.75B |

The mandate's own stated expectations -- "~$1.65B" and "headline ~$1.75B" --
reproduce ONLY under Reading B. Reading A (literal) yields ~$1.47B, not the
stated ~$1.75B. So the mandate INTENDS the Schwab book (Reading B) but labels
it "what SmartX covers," which it is not. **Recommend CTO~B confirm Reading B
with Andrew before PRD v0.9** -- if it is genuinely Reading A (drop 1b
entirely, 49F = model+sma only), the headline is ~$1.47B and the wording
should change; if Reading B, the basis is the Schwab book and outcome (b)
holds.

## Recommendation

Outcome **(b) Schwab-based fallback**, Reading B: 49F = 1a + 1b + 1c where
1a/1c are the SmartX pull (unchanged) and 1b = Schwab_49F_book - 1a
(SMA-inclusive). CTO~B's PRD v0.9 + the re-scoped .024/.025/.016/.026:
- 1a / 1c -- no change (WS-B SmartX pull).
- 1b (WS-E) -- residual basis switches from `certified_aua` (full BD book,
  v0.7) to the Schwab-custodied book. Revive the retired Schwab path or build
  off Schwab RPS silver.
- headline `opal_aggregate_aua` = 1a + 1b + 2a ~= $1.75B (2-term-per-cohort
  formula from .024 is unchanged; only the 1b basis moves).
- The .016 historical backfill re-scopes its 1b basis the same way; the
  methodology_version tag gains a third value for the Schwab-book basis.

AC1-AC4 satisfied. Non-mutating -- no code, no artifact, no deploy.
