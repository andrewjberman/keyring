# L4-R REVIEW -- MDPF_CANON PRD v2.12 @47e92c2935, ratified-text half -- REFUSE

**Reviewer:** `3.0.0_SA_CVO`. The last ratified-text half was signed by `3.0.0_SA_CVO~L`, which has no live session, so this seat reviews
in its place. **Delivery:** `1.0.0_SA_CTO~DELL1` msg 5066.
**Prior signed:** v2.11 @1e5dcef9cb (half_hash 9535c5fe77ef, endpoint_hash 1a31840f1783, `3.0.0_SA_CVO~L`, 2026-10-11T18:44Z).
**Reviewed bytes:** `git show 47e92c2935:org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`. It is equal at HEAD: blob 84a6ad0f0b, and
the working tree's hash-object is the same. Ratified-text half_hash
**4abec89e2e553b09ab39836af4bad8f4182f8d85315385386d58278e7ca0e368**, endpoint_hash e45afb043e1b (`prd_signoff_lib.half_hashes` /
`endpoint_hash`). `prd-signoff.py status MDPF_CANON` reads the half STALE against 1a31840f1783 and the delivery WITHHELD.

## The change

`git diff 1e5dcef9cb 47e92c2935` on the PRD, read whole: +41 -2, one commit (47e92c2935, CTO~DELL1, 2026-10-13).
- Header: `prd_version` v2.12; `endpoint_outcomes` gains FWD-9.
- ENDPOINT: the new FWD-9 block (`:188-207`).
- The L10 ADDENDUM v2.12 at the end.

Nothing else in ENDPOINT or CONTRACTS moved. No existing outcome's text and no contract row changed.

## Andrew's words (source record fetched and printed by this seat)

`git fetch origin box/dell2`; 5e80d5eb9b is on `origin/box/dell2` (is-ancestor rc 0). Record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_184xZ_MODEL_PORTFOLIOS_AUA_TREND_GROUP_CUSTOM_MODELS_AND_CHIPS.md`,
verbatim:

> We should not be including every single individual custom model, I would include "Custom Models" as its own block in these outputs,
> using the color for those that we use in the Hover display on the "Models" card in the "Total Assets" component. By the same token, I'd
> give a chip to ALT Strategies, ETF Strategies, Client Supervised, and Client Unsupervised. It is easier to group on this basis rather
> than trying to stack all this random shit into the Trend views.

**Against FWD-9's DONE WHEN:**
- Each constraint he states is carried: one "Custom Models" block, its color taken from the Total Assets "Models" card hover, and a chip
  for each of the four groups.
- FWD-9 adds three readings he did not say: the four take "the Total Assets breakdown's grouping and colors"; the canonical Opal models
  "stay as their own series"; and the ACCEPT "it matches Total Assets". The record's "What it sets" (`1.0.0_SA_CTO~DELL2`) states the
  first two. They are fair readings, but they are the recorder's, and the DONE WHEN should say so where it binds them (item 3).

## FWD-9 -- what is gradeable as written, and what is not

1. **"three drawn dates" is not drawn by any stated rule.** No draw (seeded, fixed or rule-based) is given, and no calendar basis.
   **Fix:** name the draw. For example: the as-of frontier (`lib/trading_calendar.prev_trading_day` of the build date), the last trading
   day of the prior quarter (a period-end bar), and one date drawn by a stated seed from the trading days where every grouped series is
   non-null. Each date is printed with its basis.

2. **"equals the sum of its members" has no comparison and no source.** It does not say to what precision, or against which values: the
   served `by_model` members, the category-views nodes, or the chart's own rows.
   **Fix:** "to the cent (abs diff <= 0.01) against the served artifact's member values for that date". Also name which artifact
   carries the members (item 4).

3. **Membership and color for the five groups are named, not defined, and the names do not match the component they point to.**
   - The Total Assets breakdown's L1 keys are `Custom`, `ETF Strategies`, `ALT Strategies`, `Client - Opal Supervised` and
     `Client - Opal Unsupervised`, with colors in `portal/src/components/CategoryViewTree.tsx:87-95` (`L1_COLOR`; Custom =
     `PALETTE.fuchsia500`).
   - The groups come from the category registry: `data/mdpf/scripts/gold/mdpf_category_registry.py` (VIEW_TREE; the Client L1 drilldown
     is the `fee_taking` axis, `:150-157`).
   - FWD-9 says "Client Supervised" and "Client Unsupervised", and cites neither file.
   - ETF Strategies is defined by prose only (`CategoryViewTree.tsx:681`: SMAs on DIVZ, IDVZ, PFDE, PFOE). ALT Strategies is not defined
     at all.

   **Fix:** cite the registry nodes as the membership rule and `L1_COLOR` as the color source, by path and line, and state the label each
   chip shows. Say whether "the color the Models card hover uses for custom models" is `L1_COLOR.Custom`. This seat did not render the
   hover, so that is not established here.

4. **"No new data are needed; the sums are of series the page already serves" (ADDENDUM) is contradicted for three of the four chips.**
   This seat read the served global `aggregate-aua-timeseries` (2026-10-08). The Trend's per-date series are:
   - `by_model`: 16 model-class and 4 sma-class keys (`pfde`, `opal_div_sma`, `opal_growth_sma`, `tax`). None is tagged ETF or ALT.
   - `non_model_aua`.
   - `sma_additive_aua` and `tax_additive_aua`.
   - `non_model_assets_detail.time_series` (496 rows of enterprise_total, model_aum, non_model_aum, non_model_pct).

   No per-date Client Supervised / Unsupervised split exists. The ETF / ALT partition of the four sma keys is not carried. The
   category-views object that holds those groups is a dated snapshot, not a timeseries over the Trend's 2024-11-01..frontier window.
   So either:
   - (a) a producer change emits per-date group series (WORLD; a served-output change under its own pair; any new key cites
     `lib/opal_naming.py` output), or
   - (b) FWD-9 bounds the Client and SMA chips to what exists (dates with a category-views partition, or a stated mapping of the four sma
     keys to ETF / ALT, with the Client split shown only where measured).

   As written, the outcome cannot be realized on the served data for Client Supervised and Client Unsupervised.
   **Fix:** state (a) or (b) in the outcome, with the source of each grouped series named.

5. **The grouping is not reconciled with FWD-3's fold or with CN-d-3.**
   - The round-6 cell CN-f-1 (fe9b ruled (A); `round6/draft/TO-CN-f-1.DRAFT.md:61-72`) folds every Global per-model line held at fewer
     than 2 firms into one "Other Models" line in the served object. Most custom models are such lines (ADJUDICATION_v3 C-S20: 10 one-firm
     entries, all custom).
   - At Global, after the fold, "Custom Models" would sum lines that are no longer served individually, beside an "Other Models" line
     that holds them.
   - FWD-9 also does not say where "Other AUA", "Additive SMA sleeves" and "Tax-Managed SMA" (CN-d-3's bands) go. It does not keep
     CN-d-3's property, graded at round 4 (C-S39): the stack's rows add to the producer Total on an additive date.

   **Fix:** state the full post-change series set per scope (Global and per-firm); how "Custom Models" relates to "Other Models" at Global;
   and "the grouped stack still sums to the producer Total (`opal_aggregate_aua`) on each drawn date" as an arm.

6. **The mechanism exists; name it.** `portal/package.json` `dev:live` -> `portal/scripts/dev-live.mjs` (the deployed CloudFront front
   door, no origin secret). Per CLAUDE.md the port is 5174: `bun run dev:live --port 5174`.
   **Fix:** name the command, and "at a stated portal commit".

## Against CONTRACTS and FWD-1..8

- No CONTRACTS row is contradicted.
- FWD-3: item 5, an overlap the outcome must resolve.
- FWD-1, 2, 4-8 are untouched (storage, access and bronze; FWD-9 is presentation).
- No new S3 address or resource name is typed in FWD-9. If item 4 (a) is taken, the new key must cite builder output.
- The client-facing PROD card on Andrew's word (ADDENDUM) agrees with the push law.

## Verdict

**REFUSE** at half_hash 4abec89e2e55. Items 1-5 each block a grade on the text as written; item 6 is wording. Item 4 is the substantive
one: three of the four chips have no per-date data in what the Trend reads.

The re-sign condition: a v2.13 whose FWD-9 names the draw (1), the comparison and its source (2), the membership and color sources by path
(3), the data source or bound per chip (4), and the post-fold, sums-to-Total series set (5). Under proportionate sign-off, a wording-only
fix of 6 alone would not re-open the half.

-- 3.0.0_SA_CVO
