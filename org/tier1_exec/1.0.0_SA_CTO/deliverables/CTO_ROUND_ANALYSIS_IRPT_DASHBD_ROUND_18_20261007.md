# IRPT_DASHBD -- ROUND ANALYSIS, round 18

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~10:1xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 301):
ADJUDICATION_v6 @01ab2f9950. 5 rows dismissed; W12-S1 closed in place; ARMED 0. The laptop-run gross record was re-hashed by the CVO
and is byte-exact.

## 1. What round 18 measured -- FWD-8 still NOT REALIZED

On the gross basis (BD's own reported fee added back per segment, W12-S1's ruling), **3,279 of 9,078 segments are still UNEXPLAINED**.
This seat's rounds 15-17 analysis expected about 1,345. That figure came from the round-17 record's line and was not measured; the
re-grade measured it, so the expectation is withdrawn. **2,299 of the 3,279 span the 2025-01-09 market closure.** That leaves about
980 unexplained segments that do not span it.

## 2. Ruling on the 2025-01-09 segments -- the same rule as W12-S1

A difference in how the two systems count a day is a BASIS difference, like the fee, so it is not an explanation either. No
"CALENDAR" reason joins the closed set by assertion. The 2,299 are MEASURED: for each segment, compute what the day 2025-01-09
contributes on Black Diamond's side (the extra day in `daysHeld`; any accrual or price BD books on a day the exchange was closed),
and compare the gap with and without it. Then:
- a segment whose gap falls within 0.35 pp once BD's closure-day contribution is removed is graded on that aligned basis, and the
  removal is printed beside both figures (as the fee add-back is);
- a segment that still falls outside stays UNEXPLAINED and joins the residue.

Opal's calendar is right: 2025-01-09 was an NYSE closure. Opal's figure is not moved toward BD's.

## 3. The ENRICHMENT LIST -- round 19, one issuance by `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **The closure-day alignment** (section 2) | (1) for each of the 2,299 segments, BD's 2025-01-09 contribution is computed from BD's own record and printed; (2) the count within 0.35 pp after removing it is printed with the 2,299 denominator; (3) no Opal figure changes | LOCAL |
| E2 | **The residue read** (round 18's E2, carried forward) | (1) the segments still unexplained after E1 (about 980 plus E1's leftovers) are counted against the closed reason set, each with named evidence; (2) a reason outside the set is filed as a surprise row, not added; (3) the final UNEXPLAINED count and its share of 9,078 are printed | LOCAL |
| E3 | `account_class_daily` | unchanged from rounds 15-17 E3: cut only once the six-class values land in `_shared/etf_classification.py` | -- |

E2 is cut after E1. Both read the landed records; if they need a firm-bucket read, it goes to the laptop as a FILE (standing rule).
FWD-8 is graded only after E2.

-- 1.0.0_SA_CTO~DELL2
