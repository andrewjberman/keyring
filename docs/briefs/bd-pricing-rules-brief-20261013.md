# BRIEF -- Black Diamond pricing rules: every served price comes from a rule someone chose

**Author:** `4.0.0_SA_CRO~DELL1` | **Date:** 2026-10-13 | **Mode:** NEW (default) | **Requested by:** `1.0.0_SA_CTO~DELL1`, msg 4694
**Consumer:** `/endpoint --forward` (L2, `1.0.0_SA_CTO`). Cite sections as `BRIEF S<part>.<n>` (e.g. `BRIEF SI.O2`).

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (becomes FWD-1):** a 49 Financial advisor opens one client account on the portal, at the default T-1 date, and
sees one holding that has no public ticker. The holding is valued at a price produced by a stated rule. The same advisor, or an Opal
analyst, can ask "where did this price come from?" and get the rule and the trades behind it. One firm, one account, one untickered
holding, the default window. The other outcomes are enrichment rounds after it.

### O1 -- An analyst can trace any served price to its rule and inputs

An Opal analyst picks any served Black Diamond price for an asset and a date. They can name the rule that produced it (override,
public close, trades observed that day, interpolation or carry-forward), and they can name the rows or the close it came from. Today
this cannot be done for a material share of rows: 603 of 1,610 served trade-observed prices do not equal what the current file
recomputes, and the cause is not isolated (PART VI.3).

### O2 -- An advisor sees an untickered holding valued at the median of distinct trades

A holding with no public price is valued from that day's trades. Each trade counts once, however many portfolio groups the file
repeats it under. Today the median is taken over repeated rows, so an asset held in more groups pulls the price toward its repeated
rows. Nobody chose that weighting (PART IV.2).

### O3 -- The price shown for a date is the same on every run

When two price sources carry the same asset on the same date, the price the advisor sees is the one a written precedence selects,
not whichever row an unstable sort leaves first. Running the same build twice on the same inputs serves the same price (PART IV.3).

### O4 -- A past date's figure reads that date's trades

An advisor or analyst who opens an account's gains or a price for a past date sees a figure built from the trades whose trade date is
that date. A later rewrite that moves rows between daily files does not change a past figure unless the trades themselves changed
(PART IV.4). **First question for this outcome:** which reading the producer intends. This brief does not choose (PART VII.1).

### O5 -- Andrew sees what a corrected rule will move before it moves

Before any corrected rule changes a served price, Andrew and the figure owners can see, per fix:
- which assets' prices move, and by how much;
- which client-facing figures move with them: holdings values, account gains, firm totals;
- which past dates are restated.

Each fix moves served output on its own, under its own sign-off pair (PART V.4).

### O6 -- An engineer changes a pricing rule in one place

Today the served T-1 price has more than one writer, plus one more four-times-a-day writer of `canonical_prices.parquet` that has not
been identified (PART IV.5). An engineer who corrects a rule changes it once, and every writer of a served price applies the change.
No writer keeps an older copy of the rule.

### O7 -- An advisor reads a lot's gain computed on one consistent basis

The gain or loss an advisor sees on an open lot compares a market value and a cost basis stated on the same footing. If one side is
scaled for unit-count doubt, the other side is too; otherwise the gain is shown as unverified. A lot whose units held their value does
not appear as a large loss because only its market value was compressed (PART IV.8). Added on `1.0.0_SA_CTO~DELL1` msg 4754.

---

## PART II -- WHERE THE BOUNDARY SITS

**This project OWNS** the rules by which a served Black Diamond price is chosen:
- the T-1 trade-observed median and its de-duplication;
- the precedence among price sources and its tie behaviour;
- the date a price or a gains figure is keyed to;
- the single home of those rules across the writers;
- the basis on which a served lot's gain compares market value and cost (O7). This widens the project from price rules to valuation
  rules. The rule that compresses market value for unverified unit counts is B_01's tiered unit-confidence cap. Andrew and the CTO
  approved it on 2026-04-17 (`docs/architecture/GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md`). This project owns how the gain is stated
  around that cap, and does not own whether lots are capped.

**It RELIES ON, and does not own:**
- **`ADVI_FIRMBKTS`** (D8, dell1): where the 49 Financial data lives. That project moved this pipeline's served output to
  `opal-data-49financial` and found these three defects. It did not define the rules and does not own fixing them (round-5 analysis
  section 2). Its own un-park condition for these rows (the act-4 read-back) is a precondition here (PART V.1), not shared work.
- **`MDPF_SECCLASS`** (D8, dell1): how a holding is classified (the BD Mix and its Unclassified line). It consumes prices and does not
  set them. A price change moves its figures, so it is a downstream reader named in each fix's blast radius (O5).
- **`IRPT_DASHBD`** (D9, dell2): the investor-reporting dashboard. Its workers measured S32-S34 first (rows `IRPT_DASHBD-D2-W122-S1`,
  `-W124-S1`, `-W125-S1/-S2`, `-W126`). It is a reader of these prices, not their owner.
- **Public closes** (`historical_prices.parquet`, written by the 9 AM ET scheduler): this project uses them as an input and does not
  change how they are fetched.
- **Scoped overrides** (`scoped_price_exceptions.json`, `inject_scoped_overrides.py`): this is the existing mechanism for deliberate
  corrections. This project keeps it as the top precedence and does not re-decide which assets carry overrides.

**Not in scope:**
- the other two firms' buckets (`opal-data-inf`, `opal-data-cot`);
- any vendor or new data source;
- the Bloomberg queue;
- moving this existing pipeline to the LGIC naming canon. That is migration work under doctrine R19, never a rider here.

---

## PART III -- THE QUALITATIVE BAR

1. An analyst asked "why is this price this number?" answers from a record of the rule and its inputs. The answer does not come from
   re-running code against today's files and hoping they match what was served.
2. A price for an untickered holding is one a reviewer would recognise as the typical price of that day's distinct trades. A reviewer
   who sees one trade counted four times would call the price wrong, and the rule does not allow it.
3. Two runs on the same inputs serve the same prices. A difference between runs always traces to an input that changed.
4. A client-facing number that changes because a rule was corrected reaches a client only after Andrew has seen what moved. He never
   discovers the move by noticing a figure changed.
5. The people who own downstream figures (classification, reporting, gains) learn of a price-rule change from its blast radius. They
   do not learn of it from a broken comparison afterwards.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

Each item is a finding from what was read. Code was read at `origin/box/dell1` @60c9b52ff0.

1. **Producer and precedence exist and are stated in code.** The precedence is `SOURCE_RANK` in
   `data/black_diamond/scripts/silver/bd_price_update.py:65-71`: `scoped_override` -2, `yahoo_finance` -1, `transaction_observed` 0,
   `linear_interpolation` 2, `carry_forward` 3. `upsert_canonical` (:587-603) keeps the lowest rank per `(date, asset_name)`. The
   pattern is sound; the defects are in what feeds it and what reads it.
2. **S32, the median over repeated rows, is measured.**
   - `extract_t1_prices` (:327-344) takes the median of `|market_value|/|units|` per `asset_name` over the rows of
     `load_transactions_for_date` (:263-271). That loader does not de-duplicate.
   - The new-asset loader does de-duplicate (`drop_duplicates(subset=['transaction_id'])`, :258-259), and so does the 30-day observed
     path (:898-899). The rule is applied inconsistently inside one file.
   - **Measured** (FB-h-7, read 2026-10-13T07:05:55Z): over 20 weekday partitions, 2026-09-16 to 10-13, 830 of 5,366 asset-days change
     their median when de-duplicated by `transaction_id`. The changes fall across 450 assets, with a maximum change of 753.5.
   - The CVO recomputed the result with independent code and got the same numbers.
   - One partition alone, 2026-09-16, holds 13,975 rows for 2,982 distinct `transaction_id`s.
3. **S33, the tie order on read, is latent and not active today.**
   - `data/black_diamond/scripts/gold/B_01.holdings_lots.py:331-361` concatenates the daily price files and `canonical_prices.parquet`
     in key order. It then sorts by date with the default (unstable) kind and keeps the first row per asset. The tie between same-date
     rows from two objects is therefore settled by sort order, not by `SOURCE_RANK`.
   - **Measured:** 0 of 11,108 tied assets are decided by the tie in the current file set, because a later-dated row exists for every
     one of them.
   - **Inferred, not measured:** replaying the file set as it stood at the 10-09 run makes the tie decisive for all 11,108 assets, and
     3,906 of their alternative prices differ.
   - The production runner installs pandas unpinned (`infra/aws/ec2/bd-gold-layer-runner/setup-instance.sh:20`), so the sort's tie
     behaviour on the live host is unknown.
4. **S34, file-day versus trade-date keying.**
   - Three served readers key on the `silver/transactions/<file day>` object rather than on `trade_date`: `B_03.account_gains.py:327`,
     `bd_price_update.py:265` and the Lambda twin `infra/aws/lambda/bd-pipeline/bd-price-update/lambda_function.py:143`.
   - **Measured:** for the 12 served objects for 2026-08-20..23, 0 of 12 changed under the strict day-after reading and 2 of 12 changed
     under the instant reading (`silver/transactions/2026-08-20` and `-22`).
   - `B_03` re-ran on 2026-10-13 between 05:13 and 05:14Z: 2,473 of 2,473 account-gains objects were rewritten, and its 36 versions for
     those dates have identical content.
5. **Writers of the served price: three are known, and one is not identified.**
   - Known writers: the silver script `bd_price_update.py:609`, the Lambda twin `lambda_function.py:441`, and the emergency full
     rebuild `data/black_diamond/scripts/gold/build_canonical_prices_v2.py:660`.
   - The silver script is not synced to the runner (`deploy-to-ec2.sh:16-20`) and has no run record.
   - The Lambda `bd-price-update` ran 35 times since 2026-09-02 (CloudWatch Invocations).
   - Dell2 measured `canonical_prices.parquet` being rewritten four times a day by a writer not yet identified (`D1-S33` notes). The rule
     therefore lives in at least two running copies.
6. **Prior art to reuse, so the PRD does not re-buy it.**
   - Pricing diagnostics already exist: `E_05.gap_by_pricing_source.py`, `E_06.trace_asset_pricing.py`, `E_12.dump_all_non_yahoo.py`,
     `E_16.unit_math_audit.py` (`data/black_diamond/scripts/gold/`). `E_06` is the nearest existing instrument for O1.
   - The bucket is versioned (FB-h-7), so before/after reads and rollback by prior VersionId are available for O5.
   - The FB-h-7 scripts (`pricing_quant_s32_s33.py`, `pricing_quant_s34.py` under
     `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/`) already replicate the read logic offline.
8. **Gain on capped lots: the market value is scaled, and the cost basis is not.**
   - `_apply_silver_noncash_cap` (`data/black_diamond/scripts/gold/B_01.holdings_lots.py:2291`) scales `market_value` on open lots of
     classes B and C, the lots with no custody row. It recomputes `accrued_gain` as the scaled market value minus the unscaled
     `cost_basis`, keeps `market_value_uncapped`, and leaves units, cost basis and price unchanged (its docstring).
   - The approved design records that "accrued_gain fields reflect the capped valuation"
     (`docs/architecture/GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md`). The behaviour therefore matches an approved design. The
     inconsistency is in the design, not a drift from it.
   - **Measured** (FB-j-12, read 2026-10-13T09:59:36Z, merged @e6c4d46700): one advisor's IQLT lots are scaled to 0.2287. They read
     -69.2% (-$302,165) against a +34.6% (+$151,031) uncapped gain. IQLT's price (49.84) and its cost (0 of 60 lots flagged) are both
     consistent.
   - On the served 2026-10-09 holdings object, 64,629 of 492,998 open lots (13%) are compressed, across 3,057 accounts and 1,007
     tickers.
9. **No existing project owns these rules.** A register read of every `org/missions/D*/*/*/project.json` whose name names pricing
   returned no Black Diamond pricing project.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

These are named, not sequenced. Sequencing is step 5.

1. ADVI_FIRMBKTS's act-4 read-back is complete. It is the un-park condition already stated on rows `D1-S32/S33/S34`.
2. The intended date reading for S34 is decided by whoever owns the meaning of a past-dated figure. The choices are trade date, the
   strict day after, or the instant reading.
3. The four-times-a-day writer of `canonical_prices.parquet` is identified, so O6 has a complete writer list.
4. Each corrected rule that moves served prices is its own act under a never-widen pair (CTO + COO). Each pair names the assets that
   move, the client-facing figures that move, and the rollback per key.
5. A restatement of past client-facing figures goes to a PROD page only on Andrew's word, under the push law for client-facing pages.
6. The pandas version on the gold runner is known (pinned or read) before O3 is claimed on the live host.
7. The 603-of-1,610 gap (PART VI.3) is explained, or bounded, before O1 is claimed. A trace instrument that cannot reproduce what was
   served does not satisfy O1.
8. O7 changes how an Andrew-approved design (2026-04-17) states a gain, so the basis is chosen on Andrew's word. The choices include
   scaling cost with market value, stating the gain on uncapped values, or marking the gain unverified on capped lots.
9. The executive-summary position slots that rest on capped market values stay disabled until O7's correction is served. This is the
   CTO's ruling in ADVI_FIRMBKTS (`CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md` ADDENDUM 1).

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Status ages; do not cut outcomes from it.

1. **S32:** 830 of 5,366 asset-days and 450 assets, with a maximum change of 753.5. The money effect on the latest available holdings
   snapshot (2026-10-09) is 25,479.05 across 15 changed assets. That figure is not in the record (FB-h-7 narrative). Measured
   2026-10-13T07:05:55Z.
2. **S33:** 0 of 11,108 decided by the tie in the current file set. Measured 2026-10-13T07:05:55Z.
3. **Served versus recomputed:** of 1,610 served `transaction_observed` rows over the 20 days, 1,007 equal the recomputed median and 603
   do not. Candidate causes are a multi-day backfill, or the file's state at write time. Neither has been isolated. Measured
   2026-10-13T07:05:55Z.
4. **S34:** 2 of 12 under the instant reading and 0 of 12 under the strict reading. Measured 2026-10-13T07:05:55Z.
5. **Capped lots:** 64,629 of 492,998 open lots (13%), across 3,057 accounts, carry a scaled market value against a whole cost basis
   on the served 2026-10-09 object. That object was last written 2026-10-13T05:06:00Z. Measured 2026-10-13T09:59:36Z (FB-j-12).
6. **Rows:** `ADVI_FIRMBKTS-D1-S32`, `-S33` and `-S34` are OBSERVATION/INERT, UNDER_INVESTIGATION, and owned by
   `1.0.0_SA_CTO~DELL1`. Read at `origin/box/dell1` @60c9b52ff0, 2026-10-13T07:3xZ.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

1. It does not choose S34's reading. The worker's record carries the instant reading as the conservative quantification, not as the
   intent.
2. It does not claim S33 is active. The 3,906 figure is an inferred replay, not a measured served state.
3. It does not claim S32's dollar effect beyond one snapshot. The 25,479.05 covers one date and 15 assets, and is not in the record.
4. It does not identify the fourth writer, and does not know whether that writer applies the same rule.
5. It does not establish which portal pages, and which client logins, render these prices. O5's blast radius has to be measured per
   fix.
6. It did not read the dell2 IRPT_DASHBD records directly. Their figures are as relayed in the ADVI_FIRMBKTS rows.
7. It does not choose O7's basis, and does not claim the capped lots' units are held or not held. FB-j-12 left that unit-count
   question open. It also does not measure the dollar size of the gain misstatement across the 64,629 lots.
8. It sets no numeric bar. Tolerances and sample sizes are the PRD's to set once the mechanics are known.

---

## PART VIII -- DONE WHEN (proposed; Andrew confirms)

Proposed qualitatively, for Andrew to confirm or rewrite:

1. **Rule on record:** every served Black Diamond price for 49 Financial is produced by a rule written down in one place.
2. **Traceability:** an analyst can trace any served price to that rule and its inputs.
3. **Approved moves only:** every price that moved because of this project moved under a fix Andrew saw before it moved.
4. **Consistent gains:** every served per-lot gain compares market value and cost on the basis Andrew chose for capped lots.

---

## REFS TO CARRY

```
  BRIEF PATH        docs/briefs/bd-pricing-rules-brief-20261013.md
  PROJECT           NONE-YET (CTO registers at L3)
  EXISTING PRD      NONE
  SIBLING PROJECTS  ADVI_FIRMBKTS (D8, dell1), MDPF_SECCLASS (D8, dell1), IRPT_DASHBD (D9, dell2)
  SOURCES           org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/ROUND_ANALYSIS.round5.md section 2
                    org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~66/PRICING_QUANT.{md,json}
                    org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md rows D1-S32, -S33, -S34
                    org/missions/D8/ADVI/ADVI_FIRMBKTS/ledger/CTO_SAMPLE_READ_FB_J_10_EXEC_SUMMARIES_20261013.md ADDENDUM 1
                    org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~75/IQLT_TRACE.{md,json} (@e6c4d46700)
                    docs/architecture/GOLD_B01_TIERED_UNIT_CONFIDENCE_CAP.md (approved design, 2026-04-17)
  PRIOR ART         SOURCE_RANK + upsert_canonical (bd_price_update.py:65-71, :587-603); scoped overrides;
                    E_05/E_06/E_12/E_16 pricing diagnostics; FB-h-7 offline replicas; versioned opal-data-bd
  MEASURED AT       2026-10-13T07:05:55Z (FB-h-7); 2026-10-13T09:59:36Z (FB-j-12); code read at origin/box/dell1 @60c9b52ff0
```
