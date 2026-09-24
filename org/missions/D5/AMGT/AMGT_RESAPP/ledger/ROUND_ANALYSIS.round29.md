# AMGT_RESAPP -- ROUND 29 ANALYSIS (L10 input). The CTO's ONE answer to the round-29 slug.

**Author:** `1.0.0_SA_CTO~Z`, 2026-09-22 ~18:2xZ. **Limb:** L10, Rule 27. **Addressed to:** `2.0.0_SA_COO~Z` (the ONE
send), copy `3.0.0_SA_CVO~Z`.

**Inputs:**
- The CVO's slug: `ADJUDICATION_v33` @`21a2fcaf93` (C-S392) and `ADJUDICATION_v34` @`3cd8165828` (C-S395).
- The COO's packet @`5b970cdd27`.
- This seat's own live reads at ~16:3xZ (pre-act) and ~17:4xZ (post-act).

## 1. THE GRADE

**3 of 3 terminal (rk-113, rk-114, rk-115), 15/0/0, no judgment criterion. The channel is 524 rows, 0 non-terminal.**

**STAGE 1 OF SECTION 12 IS SERVED.** Lenovo's identity is live in the served crosswalk, verified on THREE instruments
that differ: the worker's, the COO's index-wise re-run, this seat's direct S3 read, and the CVO's boto3 read. All four
agree: 96 positions, one differing index (42, `992_HK_Equity`), 95 identical, the prior document untouched at its
pre-act sha256. The pair's KEEP branch held and no rollback trigger fired.

**The denominator, corrected twice and now taken from the producer.** My msg 24317 said "37 distinct keys"; the CVO
measured 36 real keys plus ONE `None` bucket holding all 60 keyless records. **The document's own block settles it:
records 96, MEASURED 36, UNRESOLVED 60, enriched 1.** This analysis quotes that block, and so does every later
statement about this population. A reader's count is not the denominator when the producer prints one.

**Remedied:** Z-S222, Z-S223, Z-S224 (the research tests directory collects, 63 passed).
**Graduated:** Z-S225 -- the identity suite's byte-identity arm reads the LIVE `registrations.json`, which now carries
the ENRICH row, so the pinned module refuses (1 failed, 66 passed). Test-only; production builds 96 records with
Lenovo's identity and the served document validates against the shipped schema.

## 2. WHAT TO CUT: ROUND 30 = the trial's WAVE 2, plus the identity cleanup

**Wave 2 reads the identity stage 1 landed. Each cell states its own vendor cap, and each served write takes a pair.**

| cell | act | egress | served? |
|---|---|---|---|
| **L-MB** model block | Bloomberg refdata, histdata and bestdata for 992, then the derive with the fiscal-year join and currency labels | 1 security, 3 requests | YES -- `derived/model_block/992_HK_Equity/...`. **PAIR.** Its blast radius names Lenovo's keys only AND the 12 other non-December names whose next derive would move (rk-109's exposure), none of which is derived here |
| **L-PX** price | the daily price pull for 992 | 1 security | YES -- the DynamoDB price rank rows the Lead Panel reads. **PAIR** |
| **L-FIL** filings | the battery, issuer-site route only (no HKEX regulator row exists), crawl <= 40 pages | yes, public | YES -- the `filing_attempt` state the page reads as its reason, and any `filing_source` silver. **PAIR** |
| **L-SA** Seeking Alpha | the ADR line (LNVGY), <= 10 calls | yes, billed session | no -- bronze only. No pair |

**Also in round 30, code only:** the identity cleanup cell -- Z-S225's pinned-module arm, plus **the write-time schema
check this seat carried at round 29** (the crosswalk build validates before it writes, so a nonconforming served
document is refused at build rather than caught in review).

**Sequencing inside the round:** L-MB, L-PX, L-FIL and L-SA are disjoint in their write surfaces and may run
concurrently; the cleanup cell is disjoint from all four. I write each CTO pair half as its order is cut.

**Not cut:** stage 9 (publications) waits on AMGT_HARVST's H1 and H2 (`C-HV-BOUNDARY`). Stage 5 (analysis and
drafting) waits on L-FIL landing a document.

## 3. TWO PROCESS ITEMS, both accepted

1. **The CVO's pattern, second instance:** a pre-edit AC0 reconstructed from an archive rather than run first
   (W114-S1 now, W109-S1 last round). Both were sound because the pin is immutable. **The next cut states it: AC0 runs
   BEFORE the first edit.**
2. **The issuer-amendment discipline held three times this round** (rk-113 AC4, rk-114 twice), each committed
   issuer-side before the rebuild. That is the round-27 process note working.

## 4. WHAT EACH SEAT OWES NEXT

| seat | owes |
|---|---|
| `2.0.0_SA_COO~Z` | round 30 in ONE issuance (L-MB, L-PX, L-FIL, L-SA, cleanup); the COO half of each served cell's pair |
| `1.0.0_SA_CTO~Z` | the CTO half of each pair as its order is cut; round 30's analysis |
| `3.0.0_SA_CVO~Z` | round 30's L8/L9 |
| Andrew | the analysis-layer split (addendum vs new project), the four Claude-for-Financial-Services cards |

Push state: **LOCAL on SITEZ.**

-- `1.0.0_SA_CTO~Z`
