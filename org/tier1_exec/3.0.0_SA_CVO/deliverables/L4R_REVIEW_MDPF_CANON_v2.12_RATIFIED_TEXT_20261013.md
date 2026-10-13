# L4-R REVIEW -- MDPF_CANON PRD v2.12 @84aecdf45f, ratified-text half -- REFUSE

**Reviewer:** `3.0.0_SA_CVO`. The last ratified-text half was signed by `3.0.0_SA_CVO~L`, which has no live session, so this seat reviews
in its place. **Delivery:** `1.0.0_SA_CTO~DELL1` msg 5066; re-pin msg 5073.
**Prior signed:** v2.11 @1e5dcef9cb (half_hash 9535c5fe77ef, endpoint_hash 1a31840f1783, `3.0.0_SA_CVO~L`, 2026-10-11T18:44Z).
**Reviewed bytes (HEAD):** `git show 84aecdf45f:org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`. It equals HEAD: blob 00c4faad4f, and
the working tree's hash-object is the same. Ratified-text half_hash
**b7aa2eb054be842b74af9ff59f606f78864d572d91fc48c1cb242ba3375b77e5**, endpoint_hash 7ba6711802e1 (`prd_signoff_lib`). `prd-signoff.py status
MDPF_CANON` reads the half STALE and the delivery WITHHELD.
**Supersedes** this file's first version (commit d73e3407b7). That version reviewed @47e92c2935 (half 4abec89e2e55), the bytes before the
re-pin, and was never stamped.

## The change

`git diff 1e5dcef9cb 84aecdf45f` on the PRD, read whole, two commits (both CTO~DELL1, 2026-10-13):
- **47e92c2935:** the header (v2.12, + FWD-9), the FWD-9 block in ENDPOINT, and the L10 ADDENDUM v2.12.
- **84aecdf45f:** one clause added to FWD-9's DONE WHEN, and the ADDENDUM's "no new data" corrected (CORRECTED bullet, ruling (i), citing
  `2.0.0_SA_COO~D1` msg 5071 / `round7/FWD9_GROUPING_READ.md` @1c9f519b6f, blob 9ca474f471 verified).

Nothing else in ENDPOINT or CONTRACTS moved.

## Andrew's words beside the added clause

Source record `ANDREW_DIRECT_20261013_184xZ_MODEL_PORTFOLIOS_AUA_TREND_GROUP_CUSTOM_MODELS_AND_CHIPS.md` @5e80d5eb9b, fetched from
`origin/box/dell2` (is-ancestor rc 0) and printed by this seat:

> We should not be including every single individual custom model, I would include "Custom Models" as its own block in these outputs,
> using the color for those that we use in the Hover display on the "Models" card in the "Total Assets" component. By the same token, I'd
> give a chip to ALT Strategies, ETF Strategies, Client Supervised, and Client Unsupervised. It is easier to group on this basis rather
> than trying to stack all this random shit into the Trend views.

The clause (84aecdf45f):

> Client Supervised and Client Unsupervised exist only on the dated category-views objects (the first is 2026-08-27): their chips draw on
> those dates alone and read ABSENT, never zero and never interpolated, on every date without one

**Reading:**
- The clause is a **measured limit his word allows, not a narrowing.** He asked for a chip for each Client group; it still exists. He did
  not ask for a history the data lacks, and the alternative (a producer back-cast or a new served key) is something he did not ask for.
- But the limit is large: 21 of the 495 time-series dates. He will see two chips with about six weeks of history on a trend that starts
  2024-11-01. **Recommendation:** the client-facing PROD card states "Client chips: 21 of 495 dates, from 2026-08-27" in its before/after,
  so his promote word is given on it.
- Constraints carried from his words: one "Custom Models" block, its color from the Total Assets "Models" card hover, and a chip for each
  of the four groups. FWD-9 adds two readings he did not say ("the Total Assets breakdown's grouping and colors" for the four, and
  "canonical models stay"). They are the recorder's (`1.0.0_SA_CTO~DELL2`) and fair (item 3).

## The 21, reproduced by this seat

- The prefix `s3://opal-data-assets/portal/gold/mdpf/global/category-views/` lists 21 keys (2026-08-27 .. 2026-10-12).
- 21 of 21 parse, and each carries `nodes.Client.children` {`Client - Opal Supervised`, `Client - Opal Unsupervised`}.
- The served global `aggregate-aua-timeseries/2026-10-12.json` has 495 dates and no supervised / unsupervised key.
- Equal to the issuer's count. The 21 span 2026-08-27..2026-10-12, which holds more trading days than 21, so "absent between" them is real
  and not only "absent before".

## FWD-9 -- what is gradeable as written, and what is not

1. **"three drawn dates" is not drawn by any stated rule** (unchanged by the re-pin). With the clause, a draw now also has to say whether
   the dates come from the 21 (Client chips present) or from all 495.
   **Fix:** name the draw and its basis. For example: the as-of frontier (`lib/trading_calendar.prev_trading_day` of the build date); one
   date inside the 21; and one date outside the 21 (the absent arm). Each is printed.

2. **"equals the sum of its members" has no comparison and no source** (unchanged).
   **Fix:** "to the cent (abs diff <= 0.01) against the served member values for that date". The served sources: the timeseries `by_model`
   for Custom, ETF and ALT; that date's category-views node for the Client chips.

3. **Membership and color sources are not cited, and the labels differ from the component they point to** (unchanged).
   - The Total Assets L1 keys are `Custom`, `ETF Strategies`, `ALT Strategies`, `Client - Opal Supervised` and `Client - Opal Unsupervised`,
     colored in `portal/src/components/CategoryViewTree.tsx:87-95` (`L1_COLOR`; Custom = `PALETTE.fuchsia500`).
   - The groups come from `data/mdpf/scripts/gold/mdpf_category_registry.py` (VIEW_TREE; the Client drilldown is the `fee_taking` axis,
     `:150-157`).
   - The issuer's read (FWD9_GROUPING_READ.md:28-32) already gives the member-to-key map: ETF = `opal_div_sma`, `opal_growth_sma`, `pfde`;
     ALT = `tax` / `tax_additive_aua`.

   **Fix:** cite these sources and the map by path and line, and state each chip's label.

4. **Data source per chip: RESOLVED for the Client chips by the clause and ruling (i)** (this seat's reproduction above). Custom, ETF and
   ALT draw on series served on all dates, per the issuer's read. One residue goes to item 5.

5. **The stack's composition is still undefined, and the new measurements make that blocking.**
   - The Client chips do not partition "Other AUA". On 3 of 3 dates this seat sampled, Supervised + Unsupervised is below the timeseries
     `non_model_aua`:

     | date | Supervised + Unsupervised | `non_model_aua` |
     |---|---|---|
     | 2026-08-27 | 267,632,047.22 | 290,426,813.47 |
     | 2026-09-30 | 266,631,690.88 | 287,404,137.45 |
     | 2026-10-09 | 285,224,615.28 | 306,346,007.43 |

     About 21-23M of non-model AUA is in no Client chip; the registry excludes Insurance from display, which is a likely candidate this
     seat did not verify. So the Client chips cannot simply replace Other AUA, and stacking them on top of it counts the same dollars
     twice.
   - Client Unsupervised reads 0.0 on all three dates, and -0.0 on 2026-09-30. A measured zero is correct to show, but it must render as
     $0, not "-$0".
   - FWD-3's round-6 fold (CN-f-1, `round6/draft/TO-CN-f-1.DRAFT.md:61-72`) pools the one-firm Global model lines into "Other Models";
     those lines are nearly the Custom members.
   - CN-d-3's property, graded at round 4 (C-S39), says the stack's rows add to the producer Total. FWD-9 says nothing about it.

   **Fix:** state the series set per scope and per date class (inside / outside the 21), and how Custom Models relates to Other Models at
   Global. Add as an arm: the grouped stack sums to `opal_aggregate_aua` to the cent on each drawn date, with Other AUA (or its remainder)
   shown so that the Client chips never double-count it.

6. **"read ABSENT, never zero and never interpolated" is gradeable once its observable is named.**
   **Fix:** on a date without a category-views object:
   - no Client bar or area segment is drawn;
   - the tooltip carries no Client row, or a row reading "absent", never "$0";
   - the legend chip stays (it names the series) but carries no value for that date.

   Graded on the drawn absent date (item 1).

7. **The mechanism exists; name it.** `bun run dev:live --port 5174` (`portal/package.json` `dev:live` -> `portal/scripts/dev-live.mjs`),
   at a stated portal commit.

## Against CONTRACTS and FWD-1..8

- No CONTRACTS row is contradicted.
- FWD-3 overlaps FWD-9 (item 5).
- FWD-1, 2, 4-8 are untouched.
- No new S3 address or resource name is typed. Ruling (i) mints no new served key.
- The client-facing PROD card on Andrew's word agrees with the push law.

## Verdict

**REFUSE** at half_hash b7aa2eb054be.
- The re-pin resolves the Client data source (item 4), and its limit is one Andrew's word allows.
- Items 1, 2, 3 and 5 still block a grade.
- Item 5 is now measured: the Client chips do not partition Other AUA, by about 21-23M on each sampled date.
- Items 6 and 7 are wording.

The re-sign condition: a v2.13 whose FWD-9 names the draw (1), the comparison and its sources (2), the membership and color sources by
path (3), and the per-date series set with the sum-to-Total arm (5).

-- 3.0.0_SA_CVO
