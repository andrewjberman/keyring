# AMGT_CORPUS -- ROUND 25 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~20:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27353, *"L10 slug AMGT_CORPUS round 25 @27bbd26ccf"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v30.md` (read to EOF, 6,439 B). Issuer packet: `ROUND25_DRAIN_END_PACKET.md` @`5fe52a896a`.

**Round 25 is CLOSED:**
- 2 of 2 orders terminal, plus 2 issuer acts with CLOSED ledgers;
- `Z-S69` and `Z-S64` GRADUATED;
- `Z-S71` carried ARMED;
- 0 judgment criteria.

**The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **`Z-S69` is CLOSED on the served route.**
  - TSM `CUR_MKT_CAP` serves 2,339,877,750,964.95 **USD** ("quote (CRNCY)").
  - `NET_DEBT` carries no currency ("UNMEASURED"), an honest absence.
  - The negative arm holds: BA_US `CUR_MKT_CAP` is unchanged.
- **The label rule is wired at all 4 derive call sites** (aa-1). This answers `Z-W1-S22`'s "INERT because the callers pass no
  security".
- **BP/_LN and NG/_LN are derived on encoded keys from trusted raw** (aa-4, `Z-S64`):
  - 18 wrong sign labels are corrected;
  - NG serves a base case, 1,298.21 GBp, for the first time.
- **The CVO's census over 100 keys:** 0 sign contradictions; 31 UNRESOLVED units (BBSE3 10, TSM 1, BP 20).

## 2. RULINGS

1. **`Z-S71` leads round 26**, as ruled at aa-4 AMENDMENT 2.
   - BP's and NG's dossiers still read the 09-25 blocks through the raw key (`dossier.py:927`, `:966`).
   - **The owner is `2.0.0_SA_COO~X`.**
2. **BP's 10 `PE_RATIO` UNRESOLVED are a CLASSIFIER small-sample defect, NOT a currency mix. This corrects the CVO's attribution,
   measured here.**
   - **The series** (block `BP-SLASH-_LN_Equity/20260930T190146Z`), FY2016-2025: 1031.31, 41.10, 13.46, 31.53, 17.78, 11.91, 15.44,
     6.78, 206.72, 1663.44.
   - **The P/E is currency-consistent:** 1663.44 = PX_LAST 432.8 GBp (about USD 5.82) / `IS_EPS` 0.0035 USD. FY2016's 1031 = 509.6 GBp
     (about USD 6.3) / 0.0061 USD. These are Bloomberg's own converted ratios on near-zero GAAP EPS years: real outliers, correctly
     computed.
   - **The unit classifier sampled ONE magnitude,** the newest year's 1663, and refused the whole series.
   - `PROF_MARGIN` is the same defect: it sampled FY2025's 0.029 and refused a PERCENT series whose median is about 1.4.
   - **Ruling:**
     - a unit is decided from the key's SERIES (the median magnitude over its measured fiscal years), never from one sample;
     - the plausible band is not widened.
   - **The currency mix the CVO names is real, but it lives in `case_rule`'s OWN constructed input:** the trailing-median P/E built as
     PX_LAST (GBp) / `IS_COMP_EPS_ADJUSTED` (USD) = 778.57 (aa-4 item 2). That is ruling 3.
3. **`case_rule` refuses a constructed input, not only the value, when quote and reporting currencies differ** and the difference is
   not the GBp/GBP unit factor. The input is served null, with the reason, and the case stays ABSENT. No number built from mixed
   currencies is served anywhere in the payload.
4. **Every census count states its population** (the CVO's s.3 item 3). "31 over 100 keys" is never compared with "11 over 98".
   Round-26 before/after counts print the key count beside the number.
5. **`Z-S70` (proof-of-spec-check accepts a pin to ANY earlier commit carrying the path):**
   - **the owner is `1.0.0_SA_CTO~Z`**, since the checker is a spine carrier;
   - **INERT**, because the instance it mis-graded was re-verified at the graded content (aa-3);
   - the fix (resolve the pin by the graded blob's CONTENT hash, not by path presence; CLAUDE.md 22a) is carried to this seat's spine
     backlog, NOT a CORPUS cell, since the checker serves every project.
6. **Issuer defect 6** (a retry loop that did not stop on a gate BLOCK) is fixed by the issuer. It keys on the verdict token, never a
   positional slice.

## 3. FWD GRADES

- **13 of 19 REALIZED.**
- **The FWD that the TSM figure feeds is CLOSED again:** `Z-S69` is graduated, and the served label is USD with the negative arm
  held.
- The six render outcomes are as round 24 (MET on local DEV; promotion pending).
- `r-1`'s scheduled positive branch still waits on a fire with a population of at least 1.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 26 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **`Z-S71`:** `dossier.py:927` and `:966` read through `slash_safe_key` | LOCAL | The AC plants a slashed key, and the reader resolves the encoded block. The negative arm: a non-slashed key is byte-unchanged. |
| 2 | **The unit classifier decides from the series median** (ruling 2) | LOCAL | The AC runs the classifier on BP's `PE_RATIO` (expected RATIO) and `PROF_MARGIN` (expected PERCENT). **Every one of the 31 UNRESOLVED over 100 keys is re-read by the new rule, and each outcome is printed from the rule, never predicted.** The band is unchanged. |
| 3 | **`case_rule` refuses a mixed-currency input** (ruling 3) | LOCAL | The AC: BP's `trailing_median_pe` input is null with its reason, and NG (GBp/GBP) is unchanged at 1,298.21. |
| 4 | **The served act:** re-derive the names whose units or cases cells 2 and 3 move, then `write_one` BP and NG (cell 1) | WORLD, pair | After 1-3 merge. The expected diff comes from the serializing dry run. The predecessor-code diff is required (standing ruling 3), and the positive arm is shown before the cut. The act-start gate reads the act's IMPORT CLOSURE (aa-4 AMENDMENT 1). |
| 5 | **The header-currency census extended to BP and NG** | LOCAL read | Is BP's `CUR_MKT_CAP` label the currency of its value? The `Z-S69` class on one more name. |

**Fan-out:** 1, 2, 3 and 5 are independent. 4 follows 1-3.

## 5. ACTS ONLY ANDREW CAN DO (cited)

- **Portal PROD promotion** [CLAUDE.md Portal]: the six render outcomes.

## Compiler Tools

- The CVO's v30: the deployed `/thesis` invoke; the newest-block census over 100 keys.
- **This seat read BP's new block from S3** (`PE_RATIO`, `IS_EPS`, `IS_COMP_EPS_ADJUSTED`, `PX_LAST`, FY2016-2025) and reconciled 1663.44
  and 1031.31 by hand. That is the evidence for ruling 2.
- **This seat's own miss:** at aa-4 its independent script filtered on PERCENT -> UNRESOLVED transitions, so it did not see the 10
  `PE_RATIO` pointer -> UNRESOLVED moves. The COO half's "375 pointer units become measured" therefore passed this seat unchecked. A
  transition census reads every (from, to) pair, not the pair expected.
