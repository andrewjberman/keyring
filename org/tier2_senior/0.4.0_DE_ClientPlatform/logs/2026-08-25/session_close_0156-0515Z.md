# 0.4.0_DE_ClientPlatform~Z -- session close, 2026-08-25 0156-0515Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

Window: since `laneZ_fxfxx_classification_0020-0156Z.md`. Andrew-direct throughout; no TO was cut
for any of it, and none was needed -- every item was either his direct instruction or my own lane.

## WHAT LANDED

All portal DEV, all LOCAL and unpushed (DT pushes under the integration window):

| commit | what |
|---|---|
| `de32bacb` | ETFS_POSITIONING.TO-6 -- `# of Securities` label, canonical economy-code sector order, light->dark ramp |
| `36599dec` | Andrew's two colour corrections -- Industrials off the Equity tone (`blue550 #3073f1`), unmapped bucket darkened to `#111827` |
| `b3a59d09` | sector sort keys offset into a clear band -- DISARM of a collision `de32bacb` armed |
| `3134ccda` | ETFs subtitle "TrueShares ETFs" -> "Opal ETFs" (Andrew: two issuers, not one) |
| `b6444183` | `ETF_BOOKS` comment -- two false statements corrected (attribution + a stale SHELL claim) |
| `4b2f9be2` | editable ETF fund modals, issuer-sourced ETF copy, narrative rewrite of the Model Key Notes |
| `753b62a0` | **my own defect**: etfAdapter dropped 5 of 8 return windows |

Deliverable: `deliverables/deZ_ASSET_SUB_CATEGORIES_ETF_WIRING_BRIEF_20260825.md` (Andrew-direct,
for the backend team).

## COMPILER TOOLS

| tool | invocation | result | note |
|---|---|---|---|
| `comp-find` | ~20 runs across `portal/src`, `infra/`, `org/`, `docs/` | PASS | the workhorse; band + denominator repeatedly changed a conclusion |
| `comp-find` | `"TrueShares"` census, `portal/src` | PASS | 3 hits: 2 legitimate issuer selectors, 1 false attribution in my own file |
| `comp-find` | `"segment.sector"` + positive control `allocation.cash` | PASS | ZERO consumers with a FIRING control -- stopped a revert and a no-op publish |
| `comp-find` | `-i "TrueShares ETF"` over `org docs` | PASS | 9 hits, mostly CORRECTLY scoped -- prevented an unwarranted fabric-wide broadcast |
| `comp-find` | `"export function getAssetClassBgColor..."` | WARN | BRE-vs-python warning fired on my `\|`; the tool caught my pattern error and said so |
| `bun run typecheck` | `tsc -b --noEmit`, ~8 runs | PASS | caught undeclared `aum`/`data_as_of` reads; rc captured with no pipe every time |
| `scripts/ui-smoke.mjs` | ~9 renders | PASS | **the decisive instrument** -- see below |
| `aws s3api head-object` / `s3 cp` | served-key freshness + per-ticker reads | PASS | `s3api` deliberately, not `s3 ls` (UTC vs local) |

**What worked:** `comp-find`'s DENOMINATOR + positive controls converted three would-be findings
into non-findings before they shipped. The render harness caught two defects that typecheck could
not see.
**What failed:** nothing tool-side. My own misuse twice -- a BRE pattern the tool warned me about,
and reaching for raw `grep` on nudge-only paths (Andrew corrected me).
**Gap found:** none new. `comp-find`'s zero-result guard is good; the undercount case remains the
unguarded one (already in CLAUDE.md Rule 21).

## DE ADDITIONS -- FILES MODIFIED

See commit messages: `de32bacb`, `36599dec`, `b3a59d09`, `3134ccda`, `b6444183`, `4b2f9be2`,
`753b62a0`. Rows needing extra context:

| file | note |
|---|---|
| `shared/etfAdapter.ts` | the 5-of-8 defect. Was a three-key allowlist on `returns`; now spreads |
| `api/portal-proxy.ts` | `CurrentHolding.returns` widened by the five ETF-only windows (additive, optional) |
| `components/EtfModal.tsx` | NEW. Deliberate twin of ModelPortfolioModal; six live fields |
| `lib/etfNotes.ts` | NEW. Issuer-sourced prose, polencapital.com + pathfinderetfs.com |
| `lib/modelPortfolioNotes.ts` | narrative rewrite + a deck copy-paste defect fixed (LT/ULT shared an identical paragraph, both claiming "the most globally diversified") |

## THE THING WORTH READING -- THE 5-OF-8 DEFECT AND HOW IT WAS FOUND

Verifying the 04:45Z ad-hoc publish, the producer passed every check (105 holding tickers at 8/8 +
PFDE/PFOE = DS~Z's predicted 107; the predicted 58 at 2/8 exact) **and the page rendered 3 of 8
windows.**

- Candidate 1 (`current_holdings` absent from the artifact) -- REFUTED by CVO~Z: predicts 0 of 8, I
  measured 3. I had stated that bound myself and then accepted the refutation without checking ITS
  premise -- that the component reads the raw artifact. It does not.
- Candidate 2 (the QTD/YTD/1Y attribution path) -- REFUTED: `selectedPeriod` is hardcoded `'Current'`.
- **Two code reads failed. An instrument settled it:** a SENTINEL FIXTURE rewriting all 187 rows with
  values naming their own column (`1D=11.11 ... 1Y=88.88`). A value cannot then be mistaken for a
  neighbouring column and a blank cannot be a misread. It showed 3 of 8 unambiguously.
- `0.0.0_AB_MSTR~Z` closed it by reading source at a pinned vintage: `etfAdapter.ts:90-95` @
  `d43b88c5`, **authored by my base serial that morning**.

**The mechanism was a TYPE INTERSECTION, not carelessness:** `EtfHolding.returns` has 8 windows,
`CurrentHolding.returns` has 6, and their intersection is exactly QTD/YTD/1Y. The adapter could
carry only what both types could express.

>> **IT WAS INVISIBLE FOR A DAY BECAUSE EVERY WINDOW WAS NULL. A 3-key adapter and an 8-key adapter
render IDENTICALLY when the source carries nothing. The producer filling those windows did not
create the loss -- it made it OBSERVABLE.** An enumerated adapter field is a filter that does not
grow with its source, and it fails silent. Every other field on that object already used a generic
passthrough; `returns` was the one hand-written exception. <<

Fix exercised with the same instrument both ways: 3 of 8 before, 8 of 8 after; on real data MSFT
shows all eight matching the artifact to the decimal and HD still shows 2/8 because it genuinely is.

## MCP TRAFFIC

~90 messages handled. Significant: Andrew's 04:30Z STANDING POSTURE (prove end-to-end ad hoc FIRST,
scheduled publish as confirmation only) -- ACKed 7992, and I filed my own instance of the wrong order
(I had twice framed a dependency as waiting for 13:00Z rather than causing a run). Dispatches sent:
the FXFXX classification routing to CTO~Z (6226), the `segment.sector` zero-consumer measurement that
stopped both a revert and a no-op publish (7482), the sector-order mismatch catch (7384), and the
5-of-8 report + fix (8069, 8193).

## BLOCKERS

**None BLOCKED.** One OPEN DEPENDENCY, evidence-cited:
- ETF modal EDITING returns 400 until `etf_key_notes` joins `_SURFACE_ID_RE` at
  `infra/aws/lambda/portal_content/lambda_function.py:53`. Measured with controls both ways.
  **I authored the fix and the owned-paths gate correctly REFUSED me** (lane `CLOUD_OPS_OR_ETL`,
  any AE agent). Tree reverted clean; diff handed to `0.7.0_AE_CloudOps~Z` (7846). **And it is
  larger than the "one token" I first called it: 4 sites, and it amends CVO's PK ruling
  @a9a173e7fa -- `3.0.0_SA_CVO~Z`'s to rule on.** READING is unaffected.

## CURRENT STATE (for a reader with zero context)

- **portal DEV: 7 commits LOCAL, unpushed** (`de32bacb` .. `753b62a0`). Worktree clean, on DEV.
- **Workspace SITEZ: clean**, 0 unpushed. Earlier log `abdd6d1cdd` is on `origin/SITEZ`.
- **Served ETF artifact:** `s3://opal-data-portal-v2/platinum/etfs/positioning_data.json`,
  ad-hoc publish `04:45:15Z`, 125,915 B. FXFXX + SALXX render `Fixed Income / Ultra Short Duration`
  at the top of their books, verified per-ticker on the served bytes and on the rendered page.
- **Asset Sub-Categories in ETF mode: NOT WIRED.** `capabilitiesFor('etfs') -> attribution: false`
  (`shared/bookSet.ts:132`), so the section is absent, not empty. All ordering/colour/vocabulary
  machinery IS built and proven (`GICS_SECTOR_CODE`, `DECLARED_SECTOR_AXIS`, `sectorSortKey`,
  `sectorRampColor`). Full brief:
  `deliverables/deZ_ASSET_SUB_CATEGORIES_ETF_WIRING_BRIEF_20260825.md`.
- Dev server left running on :5199 (NOT :5175 -- CTO~Z reserved that for Andrew).

## NEXT STEPS

1. **[0.4.0_DT_ClientPlatform~Z]** push the 7 portal DEV commits at the next integration window.
2. **[backend / producer team, via 2.0.0_SA_COO~Z]** decide Option A vs B in the Asset Sub-Categories
   brief, then flip `attribution` on for ETF mode. Frontend rendering half is done.
3. **[0.7.0_AE_CloudOps~Z + 3.0.0_SA_CVO~Z]** the `etf_key_notes` surface-id family: CVO rules on the
   family set, AE authors + deploys. Unblocks ETF modal SAVING.
4. **[0.4.0_DE_ClientPlatform~Z, me, unsequenced]** two small display items surfaced and not built:
   distinguishing "does not pay a dividend" from "not retrieved" (30 of 38 null-yield rows are
   genuine non-payers; the discriminator is derivable today with no producer change), and the same
   shape for a fund-inception blank 1Y on PFDE/PFOE.
