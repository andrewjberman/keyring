# AMGT_HARVST ROUND 42 -- L8 COMPILE + L9 JUDGMENT -- FWD-17's chatter_window: all 618 rows equal an independent recompute; tone null exactly at 0 voters, never 0.0; 6 covered names carry no row; L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-04 ~00:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round42/ROUND42_DRAIN_END_PACKET.md` @`b19b278080` (2,180 B, read to EOF), msg 29086. One issuer direct
act, `HVST-ao-1`. It is SERVED as a new gold table that no route reads yet. Pair COO `f0eb10b97d` / CTO `d5d17b2d91`, under Andrew's
card 2 (@`9fe6e6f111`). No collection ran.

## 1. The judgment: does each row give the window's tone as FWD-17 states it? YES

FWD-17 (PRD at HEAD) asks for, per name per 30/90/365-day window ending at the last trading day: `articles_total`; `voters` (the
articles whose FinBERT label is not neutral); and a tone over the voters only, null at 0 voters and never 0.0.

**This seat's independent recompute.** It read S3 `opal-data-harvest` directly:
- the written part `amgt/harvest/gold/chatter_window/date=2026-10-04/part-20261004T001638Z.parquet` (618 rows, 206 securities);
- the served mention table `article_security_mention/.../part-20261003T222707Z.parquet` (31,042 rows).

From the mention rows' OWN tone fields, which this seat showed at v53 equal the score store on 31,042 of 31,042, it rebuilt every
window:
- UTC publication day; articles deduplicated by `article_key` per security;
- window `[max(end - (N-1) days, 2026-01-01), end]`, with end 2026-10-02 (Friday, T-1);
- voters are the non-neutral labels; tone is their mean signed score.

| check | result |
|---|---|
| rows matched (articles_total, scored, voters, tone to 1e-9) | **618 of 618, 0 mismatch** |
| tone exactly 0.0 | **0** |
| tone null iff voters == 0 | **0 violations** (496 rows with tone, 122 null) |
| real all-neutral windows (scored > 0, voters 0) | **40, all null**: AIG 90-day, ATO 365-day, BBSE3 30-day ... (the packet's sample) |
| 365-day `window_start_served` | 2026-01-01 on all 206: the store's start, beside `window_start_requested` 2025-10-03 |

**Grade: FWD-17 PASS in gold.** It is not yet served: no route reads `chatter_window`. RESAPP FWD-36's tone limb reads it in RESAPP's
cell, and until then that route serves tone null with its reason.

## 2. One judgment note: covered names with no row

212 names are in the universe file and 206 carry window rows. The 6 without (8766_JP, BKRKY_US, EXPD_US, ICT_PM, KCDMY_US, ST_SP)
have 0 mention rows, and the builder makes rows only for securities present in the mention table. FWD-17 says "per name per window",
and a consumer reading `chatter_window` cannot tell "no articles in any window" from "not built" for those 6. That is a value with no
carried claim. Serving explicit rows (`articles_total` 0, `voters` 0, tone null) would make the absence readable. This is an
enrichment item, graduated as Z-C-S74, not a miss of the rule as built.

## 3. L10 PRECONDITION

The one act is done; no rows were filed; HARVST ARMED is 0; the judgment limb is graded above. **MET.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S73",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T00:39:00Z",
    "one_line": "Round 42 L9: FWD-17 PASS in gold -- the first chatter_window part (618 rows, 206 securities x 30/90/365, end 2026-10-02) equals this seat's independent recompute from the served mention rows' own tone on 618 of 618 rows; tone is never 0.0 and is null exactly when voters == 0 (40 real all-neutral windows null); 365-day windows are served from the store start 2026-01-01 beside the requested start.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "S3 opal-data-harvest amgt/harvest/gold/chatter_window/date=2026-10-04/part-20261004T001638Z.parquet (618 rows) vs a recompute from amgt/harvest/gold/article_security_mention/date=2026-10-03/part-20261003T222707Z.parquet (31,042 rows): 0 mismatch; 0 tone == 0.0; 0 null-iff-0-voters violations; 496 with tone, 122 null, 40 all-neutral.",
        "lib/research/harvest/window_tone.py:64-108 (the rule recomputed independently: UTC day, article_key dedupe, inclusive window, voters non-neutral, mean signed score)."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The round's judgment limb reads PASS on the written part; no act is owed for it.",
    "spec_asserts": "FWD-17: per name per window, articles_total, voters (non-neutral) and a tone over voters only, null at 0 voters, never 0.0.",
    "world_is": "True on all 618 rows.",
    "notes": "FOR THE CTO: grade FWD-17 (gold) on this read; not served until RESAPP's cell reads it."
  },
  {
    "id": "AMGT_HARVST-Z-C-S74",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-10-04T00:39:00Z",
    "one_line": "Enrichment: 6 covered universe names (8766_JP, BKRKY_US, EXPD_US, ICT_PM, KCDMY_US, ST_SP) carry no chatter_window row because they have 0 mention rows; a consumer cannot tell 'no articles in the window' from 'not built' -- explicit zero rows (articles_total 0, voters 0, tone null) would carry the claim.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "round42/ROUND42_DRAIN_END_PACKET.md @b19b278080 section 2 (212 in the universe file, 206 with rows; the 6 have 0 mention rows).",
        "chatter_window part: 206 distinct security_key."
      ]
    },
    "disposition": "GRADUATED",
    "spec_asserts": "A value carries its claim: a name with no articles reads as zero, distinguishable from a missing build.",
    "world_is": "6 names are absent from the table.",
    "notes": "For the round-42 analysis; RESAPP's reader should handle it either way."
  }
]
```

-- 3.0.0_SA_CVO~Z
