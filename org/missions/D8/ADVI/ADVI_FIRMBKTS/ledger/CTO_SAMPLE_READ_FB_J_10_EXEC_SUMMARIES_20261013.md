# CTO sample read -- FB-j-10's 39 exec-summary bullets, 10 advisors (`1.0.0_SA_CTO~DELL1`, 2026-10-13 ~09:4xZ)

Source: `deliverables/0.7.0_AE_CloudOps~FB1/DRYRUN10_FIGURES.json` (FB1 msg 4744). Each bullet is printed beside the figures from the generator's own context builders.
- 1 artifact (4 bullets) is WITHHELD by FB1: a client display name appears in a `top_nna_mover` bullet and the PII guard did not drop it (row D1-S50).
- 35 bullets were read.

**Verdict: NOT READY TO SERVE AS IS. Four of five slots read well; `top_nna_mover` is broken.**

**What reads well** (`top_gainer`, `top_loser`, `concentration_risk`, `tax_loss_candidate`):
- **The figures match the text:** IDVZ $2,610,720.59 at 0.126083 reads "$2.61M (+12.6%)"; IEFA at 0.110859 of AUM reads "11.09%". Spot-checked on every advisor, with no mismatch found.
- **The tone is factual,** with a wash-sale caution on every tax-loss bullet.

**Defects found:**
1. **`top_nna_mover` attributes ONE client to TWO advisors.**
   - "Client rel_id 0" with the identical $9,625,309.46 inflow appears for `alex_bright` (93.88 pct) and for `garrett_newberry` (100.11 pct).
   - `rel_id "0"` is a placeholder or unmapped key, so the flows of unrelated accounts are pooled under one fake client.
   - The slot also prints raw relationship ids (<relationship id, scrubbed>) to advisors, and it is the slot where the withheld client name leaked.
2. **The PII guard misses client display names** (D1-S50). Every slot that names a client is unsafe until it is fixed.
3. **An accuracy question:** `garrett_newberry`'s IQLT reads "down $302,321 (-69.2%)" on a broad international ETF. A 69 pct unrealized loss on that fund is implausible, and it suggests a
   cost-basis or price defect of the kind the Black Diamond pricing brief covers. It is checked before any serve.

**Ruling for FB-j-7 (the regeneration pair):**
- (a) **`top_nna_mover` is DISABLED** for the first regeneration (a slot switch in config, not deleted code) until its client key is fixed. That is a product fix, and it
  goes to the CRO's exec-summary brief.
- (b) The PII guard learns client display names before ANY slot that can name a client serves.
- (c) IQLT's -69.2 pct is traced to its cost basis and price before serve. If it is a data defect, the affected bullets are held.
- (d) **Andrew is offered the sample** (the four good slots) before FB-j-4 turns the trigger on: these become the first client summaries ever to carry text, and tax-loss
  suggestions are advisory content he may want to see.
FB-j-4 stays BLOCKED until (a) through (c) are done, and until FB-j-7 is signed citing this read.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-13 ~10:1xZ) -- condition (c) resolved: IQLT's -69.2 pct is a SERVED-DATA defect (B_01's silver-noncash cap). ALL position slots are held; the trigger lands empty-for-empty.

`2.0.0_SA_COO~B1` msg 4752, FB-j-12 (read-only), merged @e6c4d46700.
- **IQLT's price is consistent:** canonical 49.84 and silver 49.31 agree. Its cost basis is also consistent (0 of 60 lots flagged).
- **The cause:** the bullet's market value of $134,351 comes from B_01's `_apply_silver_noncash_cap`. Open lots with no custody row have their market value SCALED (here to 22.9 pct
  of units times price) while cost basis is left WHOLE. So the gain reads -$302,165; uncapped, it is +34.6 pct.
- **Scale:** the cap compresses **64,629 of 492,998 open lots (13 pct), in 3,057 accounts and 1,007 tickers,** in the served 2026-10-09 holdings object. Every position slot
  (gainer, loser, tax-loss, concentration) rests on that market value, and so does any served per-lot gain.

**Rulings:**
1. **ALL position slots are DISABLED for the first regeneration** (`top_gainer`, `top_loser`, `tax_loss_candidate`, `concentration_risk`, plus `top_nna_mover` from (a)). So
   FB-j-7 and FB-j-4 land the TRIGGER with empty-for-empty: the per-advisor no-regression criterion holds by construction, 36 new advisors receive an empty artifact, and
   **act 4b (the generator writing the canonical home under the fence) is EXERCISED,** which closes FIRMBKTS's 4b NOT-EXERCISED grade. Text waits for B_01's owner.
2. **B_01's cap is a SERVED holdings-value defect, not only an exec-summary one.** A scaled market value against an unscaled cost basis misstates per-lot gains on 13 pct of open
   lots. It joins the Black Diamond pricing-rules brief (CRO) as an outcome: "a served lot's gain is computed from a market value and cost basis on the same basis". That
   project's line 3 (every price move shown to Andrew first) covers its correction.
3. **Andrew is told** as information that served per-lot gains on about 13 pct of 49 Financial open lots are understated by this cap.
Condition (d), offering Andrew a sample, waits until a slot can carry text.

-- 1.0.0_SA_CTO~DELL1
