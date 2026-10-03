# AMGT_HARVST ROUND 38 -- L8 COMPILE + L9 -- gold #6 quarantines ft (22,765 rows, 0 ft; others unchanged); 8 of the 10 ARMED rows disarmed in place; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-02 ~23:3xZ
**Input:** `2.0.0_SA_COO~H`'s `round38/ROUND38_DRAIN_END_PACKET.md` @`2648af4f5a` (7,556 B, read to EOF), msg 28794. **4 of 4 orders
are terminal** (ak-1 through ak-4).

## 1. The served act, re-read by this seat

**Gold rebuild #6, the ft quarantine alone** (pair COO `42aedf5638` / CTO `5eb4e11b3d`; act `a85ebb6161`, an ancestor of HEAD). Read from
S3 `opal-data-harvest`:

| part | rows | per publisher | tone fields |
|---|---|---|---|
| before `part-20261002T165144Z.parquet` | 23,691 | barrons 637, bbg 2,825, **ft 926**, sa 18,476, wsj 827 | absent |
| after `part-20261002T224559Z.parquet` | **22,765** | barrons 637, bbg 2,825, **ft 0**, sa 18,476, wsj 827 | `sentiment_finbert_label`, `sentiment_finbert_score` and `sentiment_scorer` present, **non-null on 0 rows** |

- **The quarantine.** 23,691 - 926 = 22,765, and every non-ft publisher's count is unchanged.
- **No tone is served.** It is held on Andrew's publisher-terms card `CARD_HARVST_PUBLISHER_TERMS_20261002.md` @`8d20bc24c8`.
- **The served page path.** `opal-amgt-scoped-api` `/security/BA_US_Equity/timeline/day/2026-07-28` answers 200 with 3 rows, all sa;
  the packet's "before" was 4 (sa 3, ft 1).
- **Publisher text and vendors.** ak-1's FinBERT calls (6 + 3) were fixed sentences on Opal's own `opal-news-ai-sentiment`, and 0
  publisher text reached it. No vendor was called.

## 2. Outcome state (for the CTO's grade)

| FWD | state |
|---|---|
| FWD-16 / FWD-17 | code built and AC-graded. HELD on Andrew's card; nothing served (0 non-null tone, read above) |
| FWD-6 density | census: re-deriving events covers 49.7% of 2x spike days against 1.3% served (8 events). The event rebuild is HELD on the card |
| FWD-11 ft limb (1) | licence-only (FT s.3.2); STOP_FT HARD; waits on the FT licence card (Andrew's spend) |

## 3. The 10 ARMED rows (packet section 5; CTO 28792)

Each graduated item leaves ARMED only through its remediation row (`comp-surprise`), so this commit advances the rows IN PLACE, clocks
only. Every fix commit cited in section 5 is an ancestor of HEAD, checked by this seat: `adc9d85b92`, `d5ef6e6371`, `651f750a5a`,
`3669bd0f0a`, `4901fd709b`, `58135da029`, `78aac97ada`.

Two claims were spot-read:
- **Z-W9-S1:** one shared `_silver_append_retrying_object_name` serves both uploaders (`uploads.py:20`, `:552`).
- **Z-W26-S1:** 0 dotted-string `patch("lib...")` targets remain under `lib/opal_data_harvest` tests.

| item | file | advance | evidence row |
|---|---|---|---|
| Z-W9-S1, Z-W11-S1, Z-S23, Z-W22-S2 | REMEDIATION_v1 | REMEDIATED, DISARMED | Z-S70, Z-S71, Z-S72, Z-S73 |
| Z-W8-S2 (inert-historical) | REMEDIATION_v1 | REMEDIATED, DISARMED | Z-S76 |
| Z-W26-S1 | REMEDIATION_v3 | REMEDIATED, DISARMED | Z-S74 |
| Z-W29-S1, Z-W30-S1 (inert-historical) | REMEDIATION_v4 | REMEDIATED, DISARMED | Z-S75, Z-S77 |
| **Z-S11** | REMEDIATION_v1 | **stays OPEN, ARMED**: routed to the checker's owner `1.0.0_SA_CTO` (invocation-alignment compares strings) | Z-S78 |
| **Z-W91-S10** | REMEDIATION_v5 | **stays OPEN, ARMED**: placed as a round-39 LOCAL cell (`listing_empty_200`) | Z-S79 |

## 4. DISPOSITIONS of the round's rows

| row | disposition | grounds |
|---|---|---|
| Z-S70 .. Z-S79 | DISMISSED_WITH_REASON | the issuer's disarm, placement and routing records. Their items are advanced or carried in section 3 |
| Z-W90-S22, Z-S69 | DISMISSED_WITH_REASON | resolved: the 4 research tests read `GRADED_PUBLISHERS` (ak-4's rule) |
| **Z-S67** (silver `record_hash` hashes `run_stamp`) | **GRADUATED** (Z-C-S67) | it breaks FWD-16's "an unchanged one never is [re-scored]": every re-silvering of an unchanged article changes its `record_hash`, so the `record_hash`-keyed FinBERT store would re-score it. This must be decided before FWD-16 resumes |
| Z-S68 (3 stale `/timeline/day` silver-path tests) | **GRADUATED** (Z-C-S67) | the round-39 repair cell (packet 6.2); RESAPP am-1 removed the path by design |

## 5. L10 PRECONDITION

4 of 4 orders are terminal. No BLOCKING or ARMED investigation row is left UNDER_INVESTIGATION. The two items still ARMED (Z-S11,
Z-W91-S10) are GRADUATED, with an owner and a placement. Judgment criteria: 0 cut. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S66",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T23:19:00Z",
    "one_line": "Round 38 L8: gold rebuild #6 quarantines ft on the served table (read by this seat: 23,691 -> 22,765 rows, ft 926 -> 0, barrons/bbg/sa/wsj unchanged, the three tone columns null on every row) and the served BA 2026-07-28 day answers 3 sa rows; 8 of the 10 ARMED items are disarmed in place on the issuer's evidence (7 fix commits on HEAD, 2 claims spot-read), Z-S11 routed to the CTO and Z-W91-S10 placed in round 39.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest amgt/harvest/gold/article_security_mention/date=2026-10-02/part-20261002T165144Z.parquet (23,691; ft 926) and part-20261002T224559Z.parquet (22,765; ft 0; sentiment_finbert_label/score, sentiment_scorer non-null 0).",
        "opal-amgt-scoped-api /security/BA_US_Equity/timeline/day/2026-07-28: 200, 3 rows, publisher sa x3.",
        "git merge-base --is-ancestor: adc9d85b92 d5ef6e6371 651f750a5a 3669bd0f0a 4901fd709b 58135da029 78aac97ada a85ebb6161 eff5c79d35 -> all true.",
        "lib/opal_data_harvest/uploads.py:20 and :552 (one suffix-retry wrapper); 0 dotted-string patch('lib...') targets under lib/opal_data_harvest tests."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S70",
      "AMGT_HARVST-Z-S71",
      "AMGT_HARVST-Z-S72",
      "AMGT_HARVST-Z-S73",
      "AMGT_HARVST-Z-S74",
      "AMGT_HARVST-Z-S75",
      "AMGT_HARVST-Z-S76",
      "AMGT_HARVST-Z-S77",
      "AMGT_HARVST-Z-S78",
      "AMGT_HARVST-Z-S79",
      "AMGT_HARVST-Z-W90-S22",
      "AMGT_HARVST-Z-S69"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Z-S70..Z-S79 are the issuer's disarm, placement and routing records, whose items are advanced in place (8) or carried open with owner and placement (Z-S11, Z-W91-S10) in REMEDIATION_v1/v3/v4/v5 in this commit; Z-W90-S22 is resolved by Z-S69 (the tests read GRADED_PUBLISHERS).",
    "spec_asserts": "The ft quarantine changes only ft rows; a graduated hazard leaves ARMED only on its remediation row.",
    "world_is": "True on the served table; 8 rows advanced, 2 stay open by design.",
    "notes": "L10 precondition MET."
  },
  {
    "id": "AMGT_HARVST-Z-C-S67",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-02T23:19:00Z",
    "one_line": "Two items graduate to the round-38 analysis: Z-S67 (silver record_hash hashes run_stamp, so an unchanged article re-silvered gets a new record_hash and FWD-16's record_hash-keyed FinBERT store would re-score it -- against FWD-16's 'an unchanged one never is'; decide before FWD-16 resumes) and Z-S68 (3 tests pin the removed /timeline/day silver path; the round-39 repair cell).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigations/INVESTIGATION_v1.md#AMGT_HARVST-Z-S67 and #AMGT_HARVST-Z-S68.",
        "AMGT_HARVST PRD v0.16 FWD-16 DONE WHEN: 'keyed to the article's record_hash so a re-silvered article is re-scored and an unchanged one never is'."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-S67",
      "AMGT_HARVST-Z-S68"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "FWD-16: an unchanged article is never re-scored.",
    "world_is": "The key it is scored by changes with every run.",
    "notes": "Neither moves a served figure today (no tone is served)."
  }
]
```

-- 3.0.0_SA_CVO~Z
