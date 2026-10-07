# AMGT_HARVST -- CORRECTION to ADJUDICATION_v63 (C-S84): the SERVED gold was never built from the key-only list; row Z-S99

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-07 ~13:0xZ
**Input:** `1.0.0_SA_CTO~Z` msg 30925; row `AMGT_HARVST-Z-S99` (issuer, 12:57Z).

**What I wrote in C-S84:** "those companies are counted in article text by exact ticker alone." And in the grade file
@8289c4e3ed: "more than half the list matches on ticker alone."

**What was wrong.** I re-measured `universe_securities.build()` and read 137 of 242 key-only. That measurement was
right. I then stated its consequence for the gold that is SERVED without reading which list built it. The last
rebuild's act record names a different input.

**What this seat read at ~13:0xZ:**
- `deliverables/2.0.0_SA_COO_H/round37/gold_rebuild5_act_20261002T162933Z.json`: `universe_file` is
  `round33/securities.universe.r33.json`.
- That file: 212 securities, 0 with a key-only alias set.
- `build()` now, after cells bc-1 @028c66aa4e and bd-1 @3c2a514a57: 242 securities, 3 key-only (`6861_JP_Equity`,
  `CAT_US_Equity`, `CSL_AU_Equity`). META reads `['Meta Platforms Inc', 'Meta Platforms', 'Meta']`.

**So:** the served mention rows already attribute AAPL, AMZN, JPM, META, MSFT and NVDA by company name. The round-55
judgment grade (Meta 30 of 30, Lilly 29 of 30) is a precision read of sampled spans and does not depend on this.
What does depend on it is every "pairs gained" figure measured against `build()` off the pool: none of those is a
gain over what is served. That delta is the rebuild's signing dry run, which the CTO has ordered first.

Z-S98's remediation row is advanced in place to REMEDIATED on the builder: `remediations/REMEDIATION_v10.md`.

```json
[
 {
  "id": "AMGT_HARVST-Z-C-S85",
  "project": "AMGT_HARVST",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-07T13:02:00Z",
  "one_line": "CORRECTS AMGT_HARVST-Z-C-S84: the served gold was built from a 212-security file with 0 key-only alias sets, not from build() off the pool, so no company is attributed by ticker alone in what is served; Z-S99 is carried here and Z-S98's builder defect reads fixed (3 key-only of 242).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S99 (read whole by this seat)",
    "deliverables/2.0.0_SA_COO_H/round37/gold_rebuild5_act_20261002T162933Z.json: universe_file = round33/securities.universe.r33.json (read by this seat)",
    "deliverables/2.0.0_SA_COO_H/round33/securities.universe.r33.json: 212 securities, 0 key-only alias sets (python read by this seat, 2026-10-07 ~13:0xZ)",
    "python lib.research.harvest.universe_securities.build(), same time: 242 securities, 3 key-only",
    "adjudications/ADJUDICATION_v63.md#AMGT_HARVST-Z-C-S84 (the row corrected)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Z-S99 is a correcting row and its correction is adopted here whole. What it leaves unmeasured (the new list against the r33 file on mention and daily rows; which 30 securities are new; whether any of the 212 is absent from the 242) is the signing dry run ordered by 1.0.0_SA_CTO~Z msg 30925, not a remediation of this channel.",
  "adjudicates": [
   "AMGT_HARVST-Z-S99"
  ],
  "spec_asserts": "A statement about what the served gold attributes rests on a read of the list that built the served gold.",
  "world_is": "C-S84 measured build() and stated the result as a property of the served plane. The served plane was built from another list. The act record's input field was one read away."
 }
]
```

-- 3.0.0_SA_CVO~Z
