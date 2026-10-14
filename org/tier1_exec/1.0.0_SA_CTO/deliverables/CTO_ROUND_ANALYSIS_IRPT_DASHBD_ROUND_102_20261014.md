# CTO ROUND-102 ANALYSIS -- IRPT_DASHBD (workstream B) -- the render fix, the model windows, and Cottonwood's gold (2026-10-14 ~04:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for rounds 101-102 (msg 7521, `ADJUDICATION_v62.md` @55d585884e; L9 DB101-5-J1 PASS,
39 rows dismissed) and D2's drain-end `IRPT_DASHBD_ROUND101_102_B_DRAIN_END_20261014.md` @4404620f0a.
**Re-bases** this seat's msg 7490 on the corrected gold census (D2 msg 7494; DB-b-190 re-seated) and folds in rulings 7508 and 7511.

## Where FWD-21 stands

- **49F:** rendered on tab and export from gold, 14 pages, none clipped (read as images). 46 of 117 members filled; 6 sections PARTIAL;
  taxable realized and disclosure ABSENT. The section check by a second seat is graded PASS at L9.
- **Cottonwood:** 1 of 8 C-SHAPE tables (`account_return_daily`, schema EQUAL to contract), but its newest partition is 2026-06-22
  (row D2-W155-S10, ARMED).
- **Inflection:** 0 of 8 tables.
- **Not met yet:** the same layout for three firms, and a figure Opal cannot produce reading in client-safe words.

## ENRICHMENT LIST for round 102 (ONE issuance)

1. **The render fix (first; ruling 7508 plus the CVO's L9 note):**
   - percents print at their stored scale, with a test pinning a stored 1.5 to read "1.5%";
   - no build, contract or ruling language on any client-facing line, with a word-list check over the rendered text;
   - an omitted chart or row is said in words;
   - the holdings table in the baseline's orientation;
   - **the page header prints the firm's report title from the firm registry, never the placeholder "Sample Firm"**, and never a
     hard-coded name.
   Re-render 49F into the private folder and read every page as an image.
2. **The model benchmark windows (ruling 7511):**
   - the builder reads `model_portfolio_timeseries.json` as an input, lands it in the report's gold with source and data_as_of claimed,
     and compounds QTD, YTD, 12M and since-household-inception cumulatively;
   - the 12-month chart draws from it;
   - print how many of the 32 benchmark members fill.
3. **Cottonwood `account_return_daily`, stale since 2026-06-22 (read, LOCAL):**
   - name its producer, its schedule or trigger (DESIRED vs APPLIED), and why the newest partition stops at 2026-06-22 (trading
     calendar);
   - name what a resume needs.
   A resume that writes served or gold partitions is a later round under a pair. This cell reads only.
4. **The Cottonwood adapter, first tables (build, own bounds):**
   - `account_dim` and the household key (the Black Diamond relationship id) from Cottonwood's silver, read in the shared
     `opal-data-assets` bucket under Cottonwood's own key prefix only, never another firm's prefix (CLAUDE.md cross-firm rule);
   - the order's paths and grant name that prefix (the issuer's grant decision, as the drain says).
   Written to the `address()` gold home, per the contract.

**Round 103:** the Cottonwood household rendered once items 3 and 4 land; then the Inflection adapter through the same contracts.

## Rows held with their owners (named, not taken)

- **D2-W152-S3** (ARMED, the issuer): the sheet height is set inline because `print.css` is outside the grant. The issuer widens its own
  grant, or rules the inline height acceptable.
- **D2-W155-S9** (ARMED): the firm registry's bucket field disagrees with `address()` for Cottonwood and Inflection. The registry is
  LGIC's (`infra/logic/registry/`). The issuer routes the row to the LGIC owner. Every reader in this project uses `address()` meanwhile.
- **Round 98:** DB-b-183 stays known-held on dell1's SC-e-97. Dell1 reads M1's status as an idempotence read near 06:15Z (MSTR relay 7523).
  That is dell1's reading, not M1's word.

## Acts only Andrew can do

None new. His read of the 49F sample stays FWD-21's organic arm. The sample is re-rendered after item 1, and the paths go to him then.

-- 1.0.0_SA_CTO~DELL2
