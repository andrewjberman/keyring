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
   - The slot also prints raw relationship ids (`z08374526`) to advisors, and it is the slot where the withheld client name leaked.
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
