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

---

## ADDENDUM -- v2.13 @fed23ff9ff, ratified-text half -- REFUSE

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 5077 and 5078.
**Reviewed bytes:** `git show fed23ff9ff:org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`, blob d0ea4877cc. It is equal at HEAD and
in the working tree. Ratified-text half_hash **3eea94b4862515db2cc8608991fc53e9a93970b9f98a007242c26c2503652f71** (equal to the CTO's
quote 3eea94b48625); endpoint_hash cb2f5ef3d855.
**Diff** `84aecdf45f..fed23ff9ff`, read whole, +68 -18: the header v2.13, FWD-9's DONE WHEN and ACCEPT rewritten, and the v2.13 note in the
ADDENDUM. Nothing else in ENDPOINT or CONTRACTS moved.

### The seven items, against this seat's ground

| item | v2.13 | this seat's check | verdict |
|---|---|---|---|
| 1 draw | dates A-D | lib.trading_calendar with build date 2026-10-13: A = 2026-10-12 (it carries a category-views object), B = 2026-08-27 (a trading day), C = 2026-08-26, D = 2026-08-31 (the first trading day after 08-27 with no object; 32 trading days 08-27..A against 21 objects). "The first gap day" is defined in the text and resolves deterministically. | taken |
| 2 comparison | to the cent, against served members | named | taken in form; see the contradiction below |
| 3 citations | path:line | `CategoryViewTree.tsx:87-95` is `L1_COLOR` (Custom = `fuchsia500`); `mdpf_category_registry.py:150-157` is the `fee_taking` Client axis (`DISPLAY_L1_AXIS`); `FWD9_GROUPING_READ.md:28-32` is the member map. All three exist as cited. | taken |
| 4 Client source | ruling (i) | unchanged (21 of 21, reproduced in the first review) | taken |
| 5 composition | the Client chips split `non_model_aua` with an "Other AUA" remainder | remainder = `non_model_aua` - (Supervised + Unsupervised) is >= 0 on 21 of 21 dates (served ts 2026-10-12 against each dated object), so the split is coherent and chips + remainder = `non_model_aua` by construction | taken -- but see below |
| 6 absent | observable named, no "-$0" | named | taken |
| 7 mechanism | dev:live at a stated commit | named | taken |

The added terms trace to their sources: "Other AUA" remainder to this seat's measurement, "adds up" to CN-d-3's property (C-S39), and
Custom absorbing Other Models to the fe9b ruling (A). They are not Andrew's words, but they are fair readings of his "group on this basis".

### What blocks: the series set contradicts the sum-to-Total arm

This seat summed v2.13's own series set from the served global `aggregate-aua-timeseries/2026-10-12.json`: the five canonical models +
Custom (the non-canonical model-class lines) + ETF (`opal_div_sma`, `opal_growth_sma`, `pfde`) + ALT + `non_model_aua`.

| date | canonical + custom vs `model_aua` | stack - `opal_aggregate_aua`, ALT = `tax` once | ALT = `tax` + `tax_additive_aua` | carries (`opal_div_sma` + `opal_growth_sma`) |
|---|---|---|---|---|
| 2026-10-09 | +0.01 | **+21,121,201.39** | +50,055,335.01 | 21,121,201.38 |
| 2026-08-27 | 0.00 | **+22,794,766.25** | +22,794,766.25 (tax 0 that date) | 22,794,766.25 |

- **The two carries overshoot the Total by their own value, to the cent.**
  - ETF lists `opal_div_sma` and `opal_growth_sma` as members. They are the FWD-3 carries, held by no firm, frozen at 2026-07-17 counts.
  - Their dollars are in no headline sum: this seat measured that `opal_aggregate_aua` = model + non_model + sma_additive (= `pfde`) +
    tax_additive (ADJUDICATION_v4 C-S41 / S13). Per the fold's docstring note (`dim_mdpf_aggregate_aua_timeseries.py:2274`), the 49F SMA
    sleeves sit inside the 49F non-model residual, which this seat did not re-measure.
  - So stacking them beside `non_model_aua` draws those dollars twice. Arm (2) fails on every drawn date where the carries have a value
    (B and A at least).
- **ALT lists two members that are the same dollars.** `tax` (by_model) equals `tax_additive_aua` to the cent (28,934,133.62 on 10-09).
  Summing both adds 28.9M.
- **The fold suppresses; it does not redistribute.** CN-f-1 (`round6/draft/TO-CN-f-1.DRAFT.md:24-28`, steps 5-6) sets the pooled
  `other_models` line to None on a date where fewer than 2 firms hold the pool. The dollars leave `by_model` while `model_aua` and
  `opal_aggregate_aua` are unchanged. On such a date at Global, Custom (which absorbs Other Models) cannot carry them, so the stack is
  below the Total by the suppressed amount. FWD-3 requires that (a one-firm book is not shown). FWD-9 must then not claim sum-to-Total
  there. It does not contradict FWD-3 as written, but the universal "so no dollar is drawn twice" is only true on the drawn dates if none
  is a suppression date; A-D are post-cottonwood and very likely are not, which this seat did not measure post-fold.
- SMA lines are never folded (step 7: "non-model-class entries (SMA lines, `tax`) are carried unchanged"). So the carries stay at Global
  after the fold, and the overshoot survives round 6.

**Fix (all wording within FWD-9):**
- (a) ETF's stacked member is `pfde` (= `sma_additive_aua`). The two carries are not stacked: they are already inside `non_model_aua` via
  the 49F residual. If they are to be shown, they are carved out of "Other AUA" by a stated rule. Which one is the CTO's (or Andrew's, under
  fe9b) to state.
- (b) ALT's stacked member is ONE of `tax` / `tax_additive_aua`, named.
- (c) Arm (2)'s sum-to-Total holds on each drawn date, and on a fold-suppressed date at Global the stack is below the line by the
  suppressed amount, read from the fold's own record, never drawn.

With (a)-(c), this seat expects to sign. The other six items are taken as above.

**Verdict: REFUSE** at half_hash 3eea94b48625. The series set as written cannot meet its own sum-to-Total arm on the served data: it
overshoots by the carries, 21,121,201.39 on 2026-10-09 and 22,794,766.25 on 2026-08-27.

-- 3.0.0_SA_CVO

---

## ADDENDUM -- v2.15 @567018c9e5, ratified-text half -- REFUSE (v2.14 @a08f5f1eb1 superseded unstamped)

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 5089, 5091 and 5093. v2.14 was read but not stamped: v2.15 landed 81 s later and the coordinator
re-pinned.
**Reviewed bytes:** `git show 567018c9e5:org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`, blob d17eb92783. The working tree
differs only in line endings (`git diff HEAD` is empty). Ratified-text half_hash
**4320120f04983fc6d032efd63d555b18234fcdcc9baeb399dd525e983ec2e74a** (equal to the CTO's quote 4320120f0498; the v2.14 quote f36e377d0227
was never at HEAD when this seat read it); endpoint_hash a6663fa19f87.
**Diff** `fed23ff9ff..567018c9e5`, read whole (two commits): the header v2.14 -> v2.15; FWD-9's ETF, ALT, Other AUA, history-route,
color and sum-to-Total clauses; and the v2.14 and v2.15 ADDENDUM notes. Nothing else in ENDPOINT or CONTRACTS moved.

### Checks on this seat's ground

The served global timeseries (`aggregate-aua-timeseries/2026-10-12.json`, 495 dates) and the 21 dated category-views objects.

- **(a) Stack on 2026-10-09 = `opal_aggregate_aua`:**
  - canonical 1,768,949,039.59; custom 68,083,780.15; ETF = pfde 411,720.53 + carve-outs 21,121,201.38; ALT 28,934,133.62; Supervised
    285,224,615.28; Unsupervised 0.00; Other AUA 190.77.
  - Stack 2,172,724,681.32 against the Total 2,172,724,681.31: diff 0.01, within the arm's <= 0.01.
  - On 2026-08-27 the diff is 0.00 and Other AUA is 0.00.
  - Each carve-out dollar is drawn once (under ETF, subtracted from Other AUA). **Holds.**
- **(b) ALT = `tax_additive_aua` only:** a single member, with no double count. **Holds.**
- **"drawn once" is enforceable:** a double draw would break the sum-to-Total arm by the carve-out amount (this seat measured that
  failure at v2.13). The arm is the enforcement. **Holds.**
- **The history route:** an OWED cell, not yet drafted (`round7/draft/` holds CN-h-1 and CN-i-1; CN-i-1:175 notes that no portal route
  reads the category-views objects). The text makes it read-only over the existing objects under its own never-widen pair, which is not a
  served write. Acceptable as owed. **Name its owner and cell id** in the round-7 cut, and its route or resource names come from builder
  output at that cell.
- **vermilion500:** traces to Andrew's 2026-10-01 word, quoted at `portal/src/lib/modelPortfolioColors.ts:137-140` ("more orange scaled
  (since its an alternative, and we canonically use vermillion for alts)"), said of the Tax-Managed SMA, which is ALT's only stacked
  member. **Holds.** The Total Assets `green400` disagreement is noted for Andrew, as the ADDENDUM says.
- **No regression** in the draw (A 10-12, B 08-27, C 08-26, D 08-31), the citations, the absent observable, or dev:live.

### What blocks

1. **The measured claim in the ratified text is not true.** FWD-9 says the carve-outs are "measured equal to the Client gap to the cent:
   21,121,201.38 on 2026-10-09". This seat's read: on 2026-10-09, `non_model_aua` - (Supervised + Unsupervised) = 21,121,392.15 against
   carve-outs of 21,121,201.38, a remainder of +190.77. The two are equal to the cent on 2026-08-27 only. Over the 21 dates the remainder
   `non_model_aua` - Client - carve-outs runs from **-4,649.20 to +301,207.84**.
2. **"Other AUA" is NEGATIVE on 13 of the 21 dates:**

   | date | remainder | date | remainder |
   |---|---|---|---|
   | 2026-08-28 | -534.13 | 09-29 | -1,637.76 |
   | 09-09 | -1.86 | 09-30 | -4,649.20 |
   | 09-10 | -403.98 | 10-01 | -197.70 |
   | 09-15 | -91.00 | 10-06 | -22.01 |
   | 09-21 | -372.22 | 10-07 | -1,435.39 |
   | 09-22 | -9.92 | 10-08 | -1.98 |
   | 09-28 | -75.91 | | |

   - A stacked band cannot be negative, and "drawn only when not zero" does not cover a negative.
   - The sum-to-Total arm still passes by construction (the remainder telescopes), so the arm cannot catch this: on those dates it would
     pass while drawing a negative band, or the build would have to invent a clamp.
   - The cause is likely that the category-views snapshot and the timeseries are different reads of the same day (a vintage or basis
     difference of up to about 300K). This seat did not establish the cause.
   - Off the 21 dates, `non_model_aua` - carve-outs is >= 0 on 474 of 474.

**Fix (wording within FWD-9):**
- (i) Restate the measurement truthfully: equal to the cent on 2026-08-27; within the range above on the 21 dates.
- (ii) State the rule for a negative remainder. For example: "Other AUA reads ABSENT where the remainder is below zero, and the stack's
  shortfall from the Total on that date equals |remainder|, printed with the read". Or another rule the CTO chooses, with the sum-to-Total
  arm adjusted to match, so no negative band and no silent clamp are possible.
- (iii) Add one drawn date where the remainder is negative (2026-09-30, the largest) as a named arm.

**Verdict: REFUSE** at half_hash 4320120f0498.
- The stack composition and the single-count now hold to the cent.
- What blocks is a false "to the cent" claim in the text, and a negative "Other AUA" band on 13 of 21 dates that no clause governs.

-- 3.0.0_SA_CVO

---

## ADDENDUM -- v2.16 @ba8b400e03, ratified-text half -- SIGN

**Delivery:** `1.0.0_SA_CTO~DELL1` msgs 5100 and 5101.
**Reviewed bytes:** `git show ba8b400e03:org/missions/D8/MDPF/MDPF_CANON/prd/MDPF_CANON_PRD.md`, blob c71496c343. It is equal at HEAD;
the working tree has the same content (`git diff HEAD` is empty). Ratified-text half_hash
**d8db1b7ab4845919abac7e9846faae3a9adc6be02c83899034cd233635e704fa** (equal to the CTO's quote); endpoint_hash 9c61c436ab1e.
**Diff** `567018c9e5..ba8b400e03`, read whole: the header v2.16; FWD-9's measurement, Other AUA, sum-to-Total and draw clauses; and the
v2.16 note. Nothing else in ENDPOINT or CONTRACTS moved.

### Reproduced

On the served global timeseries `aggregate-aua-timeseries/2026-10-12.json` (ETag ad4381e454..., equal to this seat's copy) and the 21
dated category-views objects:
- **The range:** remainder (`non_model_aua` - Client - carve-outs) from **-4,649.20 to +301,207.84**, equal to (i). At or below zero
  on 16 dates: 13 negative, 3 exactly 0.00 (2026-08-27, 09-25, 10-12).
- **Rule (ii) applied:**
  - On every date with remainder > 0, the stack - `opal_aggregate_aua` is within 0.01.
  - On every date at or below zero, the excess equals |remainder| within 0.01: 1.87 against 1.86 on 09-09; the 0.01 is the per-model
    rounding by which canonical + custom differ from `model_aua`, the same cent the sum arm already allows.
- **Date E:** 2026-09-30 is the most negative date, with remainder -4,649.20 and excess exactly 4,649.20. The arm is well-defined: it
  is named by date, and its excess is computed at read time, so it stays gradeable if a later re-emit moves the figure.

### The judgment

**1. "Absent, with the excess printed" is honest and gradeable, and Andrew's word permits it.**
- **His words set grouping and color, not a sum.** Andrew's FWD-9 source (`ANDREW_DIRECT_20261013_184xZ_..._CHIPS.md` @5e80d5eb9b,
  printed in this file's first section) asks for a Custom Models block in the Models-hover color and chips for ALT, ETF, Client
  Supervised and Client Unsupervised: "easier to group on this basis rather than trying to stack all this random shit". "It adds up" and
  sum-to-Total to the cent are the CTO's and CN-d-3's, not his. FWD-9 still keeps them on every date except two named, bounded
  exceptions.
- **The value carries its claim.**
  - The chart draws no negative band and no invented clamp.
  - The Client chips are the served category-views values, unaltered.
  - The difference is a measured basis difference between two served artifacts, printed with the read as that date's figure.
  - A clamp or a pro-rata adjustment would put an unmeasured number on a client-facing page; absent is the honest form.
- **It is not visibly inconsistent at the rendered precision.** The worst excess is 4,649.20 on a total of about 2.17B (about 2 parts
  per million). The tooltip formats to three significant digits (round-4 render: "$2.15B", "$410K"), so rows that exceed the Total by
  4.6K read identical.
- **It is gradeable.** Arm E checks excess = |remainder| to the cent, and B checks a zero-remainder date. **Condition, not a block:**
  Andrew's PROD card should state it in one line beside "21 of 495 dates": "on up to 13 dated days the Client snapshot and the time series
  differ by at most 4,649.20; Other AUA is then absent". His promote word is then given on it.

**2. "A basis difference noted for a later cell" is not a wait on FWD-9.**
- Every FWD-9 arm (A-E, the absent observable, the sums) is gradeable now on served data. The cause-finding is not a condition of any
  arm, so FWD-9 is not partly ungradeable.
- As written, though, the later cell has no owner and no carrier ("noted" is a wish). **Condition, not a block:** park it on its own
  carrier: a surprise row with `disarm_owner` (suggest `2.0.0_SA_COO~D1`) and its un-park condition. It cites the range and date E from
  this addendum, and lands at the round-7 cut.

**3. Prior items:** all held at v2.15 and are unchanged here: the stack composition, the single-count ALT, the owed read-only history
route, vermilion500 traced to Andrew 2026-10-01, the draw A-D, the citations, the absent observable and dev:live.

**Verdict: SIGN** at half_hash d8db1b7ab484.
- Conditions carried to the CTO, neither blocking:
  - the PROD card line on the basis difference;
  - an owned row for the basis-difference cause.
- Proportionate sign-off: a wording-only change under this hash would not re-open the half.

-- 3.0.0_SA_CVO
