# CTO ROUNDS 99-100 ANALYSIS -- IRPT_DASHBD (workstream B) -- the cash reads close; FWD-21 moves from one sample to the three firms (2026-10-14 ~02:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** the CVO slug for rounds 99-100 (msg 7443, `ADJUDICATION_v61.md` @16319ab2e9; 8 rows dismissed,
DB100-1 re-run PASS) and the issuer's drain-end `IRPT_DASHBD_ROUND99_100_B_DRAIN_END_20261014.md` @af115c9b37.

## Rounds 99 and 100: CLOSED

- **Round 99 (DB-b-185):** the CASH_USD change was built, counted at 0 of 4,315 served positions and 0 of 1,314,777 lots, then reverted on
  this seat's ruling (msg 7422, @0f8d33c431). D2-W147-S3 is dismissed on two zero counts. No pair is owed for CASH_USD.
- **Round 100 (DB-b-186):** the 11 lots with ticker `CASH` already class as cash by the canonical branch. No class change.
- **"Cash as a ticker should be CASH"** (the CVO's open question): answered by this seat to D2 (msg 7427 reply). Andrew's screenshot shows
  the IR Holdings TICKER column reading "Cash" on the SmartX model cash row. That is a display item, held by `2.0.0_SA_COO~P2` as row
  IRPT_BCKEND-D2-S145. Nothing in this project moves for it.
- **Round 98 is not terminal:** DB-b-183 (the FDRXX apply) stays known-held on dell1's ledger SC-e-97 (ruling msg 7397 reply). Its rows
  (D2-S24, D2-W149-S1 to -S3) wait for its packet. D2-W146-S4 and -S5 stay open with the issuer.

## FWD-21: where it stands, graded against its DONE WHEN (PRD v0.14, line 199)

| DONE WHEN limb | state |
|---|---|
| one household at **49 Financial** rendered from gold, tab and export | RENDERED, partial: 44 of 117 contract members filled, 73 ABSENT with reasons (DB96-1 PASS, drain @32070ec5e1) |
| one household at **Cottonwood** and one at **Inflection** | NOT STARTED |
| the same layout for every firm | NOT EXERCISED (one firm) |
| a figure Opal cannot produce says so in words, never blank | MET in kind; the words repeat in every cell (defect 1) |
| checked section by section against the baseline by a seat | NOT RUN |
| Andrew's read (the organic arm) | the sample paths were put before him; no word yet |

The three render defects the issuer named (its 00:59Z message): (1) the absent reason repeats in every cell; (2) the footer reads "As of Not
available yet"; (3) the charts draw nothing. PDF clipping is NOT ESTABLISHED (no raster read).

## ENRICHMENT LIST for round 101 (ONE issuance; LOCAL or the dell2 candidate branch only; nothing served moves)

1. **The three render defects, fixed in the sample builder and the render:**
   - an ABSENT reason prints once, at its section or table head, and each cell it covers reads a short word;
   - the "As of" footer reads the household's last measured gold date;
   - each chart draws from the series the contract already carries, or prints its ABSENT reason in words.
   Proof: re-render the 49F sample into the private folder and read the PDF as an image, page by page, for clipping.
2. **The 73 ABSENT members, measured before anything is built.** Classify each as (a) available in an existing gold table under C-SHAPE,
   so the builder maps it; (b) derivable from gold by one rule already in a ratified method; or (c) truly ABSENT, with the gold table
   that would hold it. Fill every (a) in this round. List (b) and (c) for round 102. Print the denominator (73).
3. **The Cottonwood and Inflection households:** one multi-account household at each, built by the same builder into the same contract,
   rendered into the private folder. Print each one's filled and ABSENT counts beside 49F's. No firm-specific branch is permitted outside
   its adapter (C-ADAPTERS); a needed branch is a finding row.
4. **The section-by-section check (the seat's grading arm):** a seat other than the builder reads each of the three renders against the
   baseline schema `BD_FINANCIAL_PERFORMANCE_REPORT_BASELINE_SCHEMA_20261013.md` and prints, per section, PRESENT / PARTIAL / ABSENT with
   the reason. This is a JUDGMENT criterion, graded at L9.

**Placement of "on DEV":** under the laptop portal ruling (`CTO_RULING_20261013_213xZ_LAPTOP_E846_7D95_BB8B.md`, "A box never pushes DEV"),
FWD-21's render ships as one `cand/dell2/<slug>` branch cut from origin/PROD, run on the 5174 dev build for the reads, and registered as a
client-facing approval row once the check of item 4 passes. That reading of the DONE WHEN is a wording placement, not an ENDPOINT change.

**Hold carried into the issuance:** no YCharts call until the dell1 WAF probe clears (msg 7433, this seat's relay 7438-7441). The four Opal
benchmarks read from gold as served; a benchmark that would need a live YCharts pull reads ABSENT this round.

**Client data:** every render and every figure stays in `C:/dev/_irpt_private_evidence_20261009/`. The repo holds counts, member ids and
words only.

## Acts only Andrew can do

None new. His read of the samples is FWD-21's organic arm (a qualified essential wait, his own words at PRD v0.14). It runs beside the
seat's check and does not hold the round.

-- 1.0.0_SA_CTO~DELL2
