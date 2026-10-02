# AMGT_CORPUS ROUND 32 -- L8 COMPILE -- BEST_DIV_YLD now labelled PERCENT on the served blocks, values unmoved; the percent label reads right

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~16:3xZ
**Input:** `2.0.0_SA_COO~X`'s `ROUND32_DRAIN_END_PACKET.md` @`8a7f8a78fa` (4,415 B, read to EOF), msg 28568.
**L7:** no task order was cut. The direct acts are `CRPS-ah-1` @`75ea254ddc` and `CRPS-ah-2` @`b2aee0c0f2`; the SERVED act is
`CRPS-ah-3` (ledger `amgt-corpus-r32-ah3` CLOSED, 5 legs; map `7527f440e7`, blocks `b540a1b480`). All four commits are
ancestors of HEAD. **0 judgment criteria**: an all-mechanical round, so this seat's read below is the plausibility check.

## 1. The served act, re-read by this seat (S3 `opal-data-harvest/derived/model_block/`)

| key | newest block (prev) | BEST_DIV_YLD unit | values |
|---|---|---|---|
| BA_US | `20261002T154901Z` (`20261001T070950Z`) | DECIMAL -> **PERCENT** | equal: 0.00254, 0.145, 0.603 |
| GOOGL_US | `20261002T154902Z` (`20260930T093809Z`) | DECIMAL -> **PERCENT** | equal: 0.251, 0.223, 0.233 |
| HEI_US | `20261002T154903Z` (`20260930T083958Z`) | DECIMAL -> **PERCENT** | equal: 0.081, 0.090, 0.097 |
| PWR_US | `20261002T154906Z` (`20260930T093852Z`) | DECIMAL -> **PERCENT** | equal: 0.068, 0.073, 0.083 |

The new stamps equal leg c's (154901Z-154906Z). The label moved and no value moved, on all four, as the packet states.

## 2. The plausibility read (packet section 4: "does a percent label on a 0.25% yield read right to an analyst?")

**Yes.**
- **GOOGL:** 0.25 read as PERCENT is a 0.25% consensus dividend yield, consistent with a small recent dividend payer at its
  price. Read as DECIMAL it would claim 25%.
- **BA:** 0.0025 / 0.145 / 0.603 read as ~0% / 0.15% / 0.60% is a suspended dividend resuming small. The page already prints
  0.0% / 0.1% / 0.6%. Read as DECIMAL it would claim a 60% yield.
- **HEI and PWR:** 0.07-0.10% are ordinary yields for those payers.

The DECIMAL reading is implausible on every key; the PERCENT reading fits.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-S74` (not-measured prefixes) | DISMISSED_WITH_REASON | remedied by ah-1 @`75ea254ddc` (on HEAD). The packet's census reads the ZERO-DOMINATED and UNRESOLVED-ON- prefixes as UNRESOLVED (10+1 units, 11 signs), with the other 37,735 unchanged |
| `Z-S81` (DECIMAL-by-magnitude labels on 8 mnemonics) | **GRADUATED** | the round-32 analysis's enrichment candidate. 77 figures remain (Z-S82) on the same 0 < \|v\| < 0.3 heuristic just retired for BEST_DIV_YLD. The face is unaffected because the page reads the row type, not the unit field |
| `Z-S82` (amends Z-S81 to 77) | DISMISSED_WITH_REASON | the count record; its population is carried on Z-S81 |

## 4. L10 PRECONDITION

The rectangle's cells are DONE (2 direct acts and the SERVED act with its ledger CLOSED); no BLOCKING or ARMED row of the round
is open; 0 judgment criteria. **MET.**

```json
[
  {
    "id": "AMGT_CORPUS-Z-C-S39",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T16:29:00Z",
    "one_line": "Round 32 L8: on the served blocks (read by this seat) BA, GOOGL, HEI and PWR moved BEST_DIV_YLD DECIMAL -> PERCENT with every value equal; the plausibility read holds (GOOGL 0.25 is a 0.25% yield, BA 0.603 a 0.60% yield; as DECIMAL they would claim 25% and 60%); Z-S74 remedied by ah-1; Z-S81 (77 DECIMAL-by-magnitude labels) graduated to the analysis; L10 precondition MET.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git merge-base --is-ancestor: 75ea254ddc, b2aee0c0f2, 7527f440e7, b540a1b480 -> true.",
        "S3 opal-data-harvest derived/model_block/{BA,GOOGL,HEI,PWR}_US_Equity/: newest 20261002T154901Z..154906Z vs the previous stamp: BEST_DIV_YLD unit 'DECIMAL (differs from CRO's PERCENT reading on SAP)' -> 'PERCENT'; values equal on all 6 entries per key.",
        "BA values 0.002540650406504065, 0.14532520325203252, 0.603150406504065; GOOGL 0.2512212142358688, 0.22301698069318446, 0.23290300069783673."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S74",
      "AMGT_CORPUS-Z-S82"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S74 is remedied by ah-1 (on HEAD; the served census reads the newer prefixes as UNRESOLVED); Z-S82 is the count record of Z-S81.",
    "spec_asserts": "Drain-end packet @8a7f8a78fa: BEST_DIV_YLD DECIMAL 12 -> 0, exactly 4 blocks moved, 0 value moves.",
    "world_is": "True on the four moved blocks as read; the plausibility read supports PERCENT.",
    "notes": "No act owed on these two."
  },
  {
    "id": "AMGT_CORPUS-Z-C-S40",
    "project": "AMGT_CORPUS",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T16:29:00Z",
    "one_line": "Z-S81 graduates to the round-32 analysis: 77 served figures on the remaining percent-family mnemonics still carry the 0 < |v| < 0.3 'DECIMAL' magnitude label that round 32 retired for BEST_DIV_YLD alone; the page does not read the unit field, so the face is unaffected.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_CORPUS-Z-S81 and #AMGT_CORPUS-Z-S82 (92 -> 77 after ah-3).",
        "ROUND32_DRAIN_END_PACKET.md section 3: HEI EQY_DVD_YLD_IND stays DECIMAL (a negative arm)."
      ]
    },
    "adjudicates": [
      "AMGT_CORPUS-Z-S81"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "A served unit label says what the number is.",
    "world_is": "77 figures labelled DECIMAL by magnitude alone.",
    "notes": "FOR THE ROUND-32 ANALYSIS: the identity-rule approach of ah-2, one mnemonic family at a time."
  }
]
```

-- 3.0.0_SA_CVO~Z
