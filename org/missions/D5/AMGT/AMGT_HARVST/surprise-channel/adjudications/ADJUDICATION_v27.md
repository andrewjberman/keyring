# AMGT_HARVST ROUND 19 -- L8 COMPILE (no judgment criterion; the offered plausibility read answered)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~22:3xZ
**Input:** `2.0.0_SA_COO~H`'s `round19/ROUND19_DRAIN_END_PACKET.md` @`86ee31f531`. The packet was read to EOF (3,960 B).
**L7 re-measured, not adopted:** `i-1`..`i-4` all read `complete` on their LAST `<status>` tag. 0 judgment criteria.
Class: WORLD.

---

## 1. THE SERVED AND DEPLOYED STATE, RE-READ BY THIS SEAT

- **Lambda:** `opal-amgt-scoped-api` returns CodeSha256 **`uv0oTSMaW3gDvq0H/pn64hORUYCYFAzWN7OsjC2x+Ng=`**, LastModified
  2026-09-29T21:57:59Z. This equals i-4's close.
- **The deploy entry:** `amgt-harvst-i4-scoped-api-publisher-codes-20260929` was CLOSED on CLOUD @`84548218ef`.
  - Swept across all 16 live worktrees. The sentinel survives only in `C:/tmp/r49-175`, an AMGT_RESAPP round-49 worker
    branch cut between the open and the close.
  - That copy is stale, not an open deploy: the artifact is measured at the closed state.
  - The branch never touched the file, so its drain keeps CLOUD's deletion.
- **Gold, `chatter_daily`:** `date=2026-09-29/part-20260929T212132Z`, ETag `4743eb602f1d88b92017bae0022b66e1`, read by this
  seat with pyarrow:
  - 51,952 rows, 22 columns;
  - DENIED 51,803 with `[]`;
  - PARTIAL 148 `["sa"]` (ASML_NA 74, ASML_US 74) and 1 `["wsj"]` (992_HK, 2026-09-23);
  - COMPLETE 0.
  - This equals the packet.

## 2. THE OFFERED PLAUSIBILITY READ -- "does a PARTIAL day now say who covered it, in terms a PM can act on?"

**It names a publisher correctly by the producer's definition. But that definition is not what "covered" says to a PM, and
every PARTIAL day this seat opened has no article behind it.**

- **This seat's reads of the deployed `/timeline/day`:**
  - `992_HK_Equity/timeline/day/2026-09-23` returns PARTIAL, `publishers_covered_codes ["wsj"]`, **`articles []`**.
  - `ASML_NA_Equity` on 2026-07-15, 2026-08-21 and 2026-09-26 (first, middle and last of its 74) each return `["sa"]` with
    **0 articles**.
- **The definition,** read at `lib/research/harvest/publication_gold.py:553-592` (`publisher_coverage`) and `:652-658`:
  - a publisher "covers" a day when its **listing search for the name reaches back to that day**;
  - the span runs from the oldest published date its listings reached through its fetch date;
  - the definition does not say the publisher wrote about the name.
  - So PARTIAL `['sa']` with 0 articles means: **Seeking Alpha was searched through this day and had nothing; the other four
    were not reached.** That is a real, attributable zero, which is useful.
- **The risk:** "covered by sa" reads, to a PM, as "Seeking Alpha wrote about ASML that day". A PM who acts on it looks for an
  article that does not exist.
- **For the analysis (a DSGN_AMGTV1 wording ruling):** the page should say "searched: Seeking Alpha (nothing found); not reached:
  4 others", not "covered by". The API field name `publishers_covered` carries the same ambiguity.

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W45-S1` (the whole-brand list and limb (a) disagree on UBS) | **GRADUATED** | i-1 removed UBS from the list. The list agrees with its limb, and there were 0 served moves (packet section 2). |
| `Z-W45-S2` (the whole-brand ASML entered listing_hit identifiers; ASML flipped to PARTIAL) | **GRADUATED** | The round-18 analysis ruled the identifier path correct. i-2, i-3 and i-4 now serve which publisher each PARTIAL day rests on, and this seat read `["sa"]` on both listings' 148 rows. The remaining question is wording (section 2), not this row's. |
| `Z-S41` (the reader was redeployed between the pair's read and the puts) | **CARRIED**, INERT | The lesson was applied in i-3's dry step (the packet); left for the issuer to close. |
| `Z-W45-S3`, `Z-W45-S4` | **CARRIED**, INERT | unchanged |
| `Z-S37`, `Z-W39-S1`, `Z-W41-S1` (ARMED) | **CARRIED** | as in v25 and v26; no landed remedy |

`_latest_dispositions('.', 'AMGT_HARVST')` before this row returned **108 items: 58 GRADUATED, 25 DISMISSED_WITH_REASON,
25 UNDER_INVESTIGATION**, read from 31 files, with 0 unknown targets.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 4 of 4. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** the three ARMED rows are CARRIED as before. **MET**
3. **Every judgment criterion graded:** 0 in the round. The offered read is answered in section 2. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S37",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T22:35:00Z",
    "one_line": "L8 round 19: deployed uv0oTSMa... and chatter_daily part 4743eb60 re-read (PARTIAL 148 ['sa'] + 1 ['wsj'], DENIED 51,803); every PARTIAL day this seat opened on /timeline/day serves 0 articles -- 'covered' means the publisher's listing search reached the day, not that it wrote about the name; Z-W45-S1 and Z-W45-S2 graduate.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: TO-HVST-i-1..i-4 read 'complete' on their LAST <status> tag.",
        "Lambda get-function-configuration opal-amgt-scoped-api: CodeSha256 uv0oTSMaW3gDvq0H/pn64hORUYCYFAzWN7OsjC2x+Ng=, LastModified 2026-09-29T21:57:59Z.",
        "S3 opal-data-harvest amgt/harvest/gold/chatter_daily/date=2026-09-29/part-20260929T212132Z.parquet ETag 4743eb602f1d88b92017bae0022b66e1: 51952 rows, 22 cols; Counter {(DENIED, []): 51803, (PARTIAL, [sa]): 148, (PARTIAL, [wsj]): 1}.",
        "Deployed /api/scoped/amgt/security/992_HK_Equity/timeline/day/2026-09-23 -> 200 {data_status PARTIAL, publishers_covered_codes [wsj], articles []}; ASML_NA_Equity 2026-07-15, 2026-08-21, 2026-09-26 -> 200, [sa], articles 0.",
        "lib/research/harvest/publication_gold.py:553-592 publisher_coverage: span from the oldest published date the publisher's listings reached for the security through its fetch date; :652-658 PARTIAL when some but not all ENABLED_PUBLISHERS cover the day.",
        "Deploy entry closed @84548218ef; sentinel present only in C:/tmp/r49-175 of 16 live worktrees (stale branch copy)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W45-S1",
      "AMGT_HARVST-Z-W45-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @86ee31f531 asserts i-1..i-4 terminal and VALID, the deployed /timeline naming the publisher on PARTIAL days, and CLOSE RUN OK, and offers a plausibility read: does a PARTIAL day say who covered it in terms a PM can act on?",
    "world_is": "True as read. The named publisher is the one whose listing search reached the day; on every PARTIAL day sampled it found nothing (0 articles). The data is right; 'covered' is the wrong word for a PM.",
    "notes": "FOR THE ROUND-19 ANALYSIS: rule the PM wording of a PARTIAL day -- 'searched: <publisher> (nothing found); not reached: N others' -- in DSGN_AMGTV1, and consider whether the API field name publishers_covered should say 'searched'. The stale i-4 sentinel on C:/tmp/r49-175 clears at that branch's drain."
  }
]
```
