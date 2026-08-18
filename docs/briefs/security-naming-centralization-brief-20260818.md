# Security Naming Centralization

**Brief for Andrew | 2026-08-18 | Author: 1.0.0_SA_CTO~X | Status: COMPLETE, live on PROD (portal-v2.1.163)**

---

## 1. What you saw, and what is true now

The Positioning page's Attribution Breakdown rendered ticker **VUG** with the name
`1.61931034482759` — a benchmark weight where a security name belongs. That cell now reads
**"Vanguard Growth ETF"** on PROD, and the fix was deliberately not a one-cell patch: the
investigation found that security *naming* logic lived in **eight places** across backend and
frontend, most of them drifting copies and one of them (the frontend fallback map) actively
masking the underlying producer defect for every ticker except VUG. On your "Execute" order the
whole class was centralized: **one canonical registry, every producer reads it, every shadow
decommissioned.**

## 2. Anatomy of the defect (three stacked causes)

1. **Producer parse vestige.** The AWS Lambda function `yang-generate-holdings-attribution`
   read the holding name from Excel column index 4 ("Column E"), a layout that died with the
   June-2026 workbook format. The current workbook
   (`s3://opal-data-portal-v2/uploads/Model Portfolio Attribution 20260731.xlsx`) has **no name
   column at all** — column 4 holds the first portfolio's Style Bench Average Weight. Every
   emitted `name` was therefore a number (per period sheet, hence the four distinct values VUG
   carried) or `--`.
2. **Registry placeholder.** The DynamoDB (Amazon's key-value database service) table
   `etf-classifications` — the system's own declared single source of truth (SSOT) for security
   metadata — carried `name = "VUG"`, a seed-script placeholder. VUG entered the model
   portfolios after the last canonical sweep (2026-03-25) and had been registered on **no**
   naming surface: not the registry, not the canonical seeder list, not any of four hardcoded
   portal maps. Of 56 held tickers it was the only one with that property. 59 other
   (non-held) registry rows carried the same placeholder class.
3. **The mask.** The frontend resolved names as
   `ETF_NAME_FALLBACKS[ticker]?.name || h.name` — a hand-maintained map that hid the producer
   junk for every held ticker except VUG. A masking layer converts a loud, obvious defect into
   a silent one that surfaces only on the first unregistered ticker.

## 3. The architecture, before and after

**Before** — eight naming surfaces, five of them shadows:

| # | Surface | Kind |
|---|---|---|
| 1 | FILE `infra/aws/lambda/v2_portal/_shared/etf_classification.py` (`ETF_NAME_OVERRIDES`) | author-time canon (7 names) |
| 2 | DynamoDB table `etf-classifications` (116 rows) | runtime canon — 60 placeholder names |
| 3 | Inline `ETF_NAME_OVERRIDES` inside `yang-generate-positioning` (29 names) | shadow |
| 4 | Hardcoded `BENCHMARK_ETFS` names inside the same Lambda | shadow (found by a failed prediction, §5) |
| 5 | FILE `portal/src/pages/Attribution/constants/holdings-shared.tsx` (`ETF_NAME_FALLBACKS`, 53) | shadow + mask |
| 6 | FILE `portal/src/pages/Attribution/constants/etf-categories.ts` (56 `name` fields) | shadow, never read |
| 7 | FILE `portal/src/pages/Positioning/constants/etf-categories.ts` (36 `name` fields) | shadow, never read |
| 8 | FILE `portal/src/lib/tickerRegistry.ts` (`displayName`, 54 entries) | shadow, never read — and **26 of 51 values named the wrong security outright** (UTWO, a 2-Year Treasury ETF, labeled "ProShares Ultra Russell 2000"; CLIP, a T-Bill ETF, labeled a preferred-stock fund; a duplicate QBER entry sat in two asset classes under two fabricated names) |

Plus a structural hazard: the DynamoDB client module `etf_classifications_dynamodb.py` existed
as two independently-editable byte-copies, and `yang-generate-positioning`'s deploy package
carried a **third** shadow — a stale copy of `etf_classification.py`, 492 diff-lines behind
`_shared`, imported by nothing, shipped with every deploy.

**After** — one canon, one flow:

```
_shared/etf_classification.py ──seed──► DynamoDB etf-classifications  (one canon,
(author-time, 66 names)                 (runtime, 116 rows, 0 placeholders)   two halves)
                                                  │  GetItem at generation time, via the ONE
                                                  │  vendored client (source of truth: _shared;
                                                  │  copies parity-gated by vendor-manifest.sh)
                        ┌─────────────────────────┴───────────────┐
                        ▼                                         ▼
        yang-generate-holdings-attribution         yang-generate-positioning
                        │                                         │
                        ▼                                         ▼
        holdings_attribution_data.json             positioning_data.json
                        └───── portal renders h.name DIRECTLY ─────► screen
```

The serving path (S3 `opal-data-portal-v2` → CloudFront → portal) is unchanged; what changed is
that **display names now have exactly one producer-side origin**, and the frontend carries no
naming opinion at all.

## 4. What was changed, layer by layer

- **Data (registry):** VUG's row fixed by targeted, attribute-preserving `update-item`; then all
  59 remaining placeholder rows fixed the same way, names transcribed **programmatically** from
  the estate's own canonical comments (100% coverage, zero hand-typing), each update conditioned
  on the row still holding its placeholder. Post-scan: 116/116 rows, zero placeholders,
  names-only delta, no bystander rows touched.
- **Producer Lambdas (Terraform-deployed, tags `yang-pipeline-v1.5.4` → `v1.5.7`):**
  `resolve_display_name(ticker, classification, fallback)` — registry name first, a fallback
  value only if it is an actual name (never numeric / `--` / ticker-equal), ticker as last
  resort — wired into `yang-generate-holdings-attribution` (v1.5.4), then
  `yang-generate-positioning` including its `BENCHMARK_ETFS` path (v1.5.5–v1.5.6). Inline
  override dicts deleted; the stale packaged shadow module deleted. No new IAM: the registry
  read rides the grant the pipeline already exercised in production.
- **Seeder hardening:** `seed_canonical_securities.py` converted from full-item `put_item`
  (which measurably **dropped** `management_style`/`sector` on registry rows and would have
  deleted the LLM classifiers' `rationale` on 392/400 sampled `bd-securities` rows) to
  attribute-preserving `update_item` on both write paths — exercised on live tables with
  isolated planted fixtures, then cleaned. VUG added to `CANONICAL_SECURITIES` and to `_shared`
  `ETF_NAME_OVERRIDES` so no future reseed can regress the fix.
- **Packaging:** `etf_classifications_dynamodb.py` single-homed at
  `infra/aws/lambda/v2_portal/_shared/` (DIR), per-Lambda copies declared as vendored artifacts
  via `BUILD_MANIFEST.json` + `ci/vendor-manifest.sh --check` — the estate's existing vendoring
  mechanism, no new infrastructure.
- **Frontend (portal commits `8dbaf56b` + `12058841`, promoted to PROD as `portal-v2.1.163`):**
  `ETF_NAME_FALLBACKS` retired (repeating the Positioning page's identical 2026-06-01
  retirement); `SelectionTab` reads `h.name`/`h.asset_class` directly; never-read `name` fields
  stripped from both `etf-categories.ts` files; `tickerRegistry.ts` ratified as a **non-naming**
  projection — dead `displayName` stripped, duplicate QBER deleted.
- **Promote:** requested from `0.4.0_DT_ClientPlatform` (their lane) on your order; DT executed
  `/prod-deploy` with pushes routed through MSTR per the integrator-only law. PROD =
  `e27dd5fa`, CI run 32169492889 success, rollback base `449a6a0e` encoded in the merge message.

## 5. How it was verified (the part worth trusting)

- **Ground truth first:** an atom_decomp SSOT rectangle (16 measured cells) was written before
  any mutation — FILE
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/VUG_SECURITY_NAMING_ATOM_DECOMP_SSOT_20260818.md`.
- **Predict-then-measure:** every producer deploy carried a pre-committed prediction of the
  exact served delta. The one miss was itself the method working: predicting 5 name changes and
  measuring 3 exposed the third name path (`BENCHMARK_ETFS`) feeding AGG/BIL; after the patch the
  served artifact matched the full prediction exactly.
- **Names-only deltas:** every regenerated served artifact was diffed whole-file against its
  prior vintage with `name` excluded — byte-identical non-name payload, identical ticker
  membership, both artifacts.
- **Deployed bytes, not repo bytes:** every Lambda package was downloaded post-apply and
  member-hashed against source (and pre-fix, to baseline that repo == executing code).
- **Rendered acceptance:** headless render of the Attribution page against the real served
  JSON, screenshot read: VUG shows "Vanguard Growth ETF", all rows named, color law clean.
- **PROD bundle markers, two independent readers:** DT's served-bytes read and my own sweep
  (entry + 43 lazy chunks): the old wrong-name strings ("Invesco Variable Rate Preferred ETF",
  "ProShares Ultra Russell 2000") at **zero** hits, and a string that exists only in the new
  code present — discriminating a fresh deploy from a cached bundle.

## 6. Residuals (surfaced, not chased — each is now a one-place fix, which is the point)

1. **ICSH name ruling:** registry says "iShares Ultra Short-Term Bond ETF"; two estate comments
   say "BlackRock Ultra Short-Term Bond ETF" (issuer rebrand vintage). One registry row on your
   word.
2. **Classification dicts:** `yang-generate-positioning` still inlines asset-class /
   management-style / sector dicts — the same disease in a different organ (classification, not
   naming). The registry already carries these fields; routing them through it is the same
   pattern again, on your GO.
3. **`tickerRegistry.ts` `description` fields** share the fabrication problem `displayName` had
   (and are equally unread). Left as non-naming scope.
4. Workspace commits + tags ride the integration window per lanes-commit / integrators-push
   (MSTR executed the portal pushes for the promote already).

**Records:** deploy ledgers (closed) in DIR `org/critical_paths/change_management/`
(`20260818T1710Z_vug-naming-*` and `20260818T1845Z_naming-centralization-*`); step-by-step
session logs in DIR `org/tier1_exec/1.0.0_SA_CTO/logs/2026-08-18/`.
