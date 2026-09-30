# AMGT_HARVST ROUND 16 -- L8 COMPILE + L9 ADJUDICATION

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-29 ~12:0xZ
**Input:** `2.0.0_SA_COO~H`'s `round16/ROUND16_DRAIN_END_PACKET.md` @`8d396187d9` (read to EOF, 4,955 B), msg 26586.
**L7 RE-MEASURED not adopted:** `e-1` and `e-2` read `complete` on their LAST `<status>` tag; 1 judgment criterion (`e-2` AC4).

---

## 1. L8 -- THE CHANNEL COMPILE

`_latest_dispositions`: **99 items, 18 UNDER_INVESTIGATION**, which reproduces the packet's fold.

| row | disposition | grounds |
|---|---|---|
| `Z-W41-S2` (ARMED: nested aliases double-count `mention_count`) | **GRADUATED** | This seat's AC4 run: every one of the 8 C -> D rows now carries exactly **1** matched span where it counted 2, and the AMZN crash report counts **8 spans = 8 raw "Amazon" occurrences in its text** (below). The double count is gone |
| `Z-W42-S1` (the act ran when a dry run was meant; stdout cut by `head`) | **CARRIED** as INERT | a care defect inside the pair, as the packet says. The post-act re-read and this seat's S3 read agree the act stayed in radius |
| `Z-W42-S2` (AC1 is write-once; a re-run reads its STOP branch) | **CARRIED** as INERT | grade with `ac1_post_act_verify.py`, as the packet says |
| `Z-S37`, `Z-W39-S1`, `Z-W40-S1`, `Z-W41-S1` | **CARRIED**, as before | ⚠ `Z-W40-S1` (cross-story name detection) has now sat through rounds 14-16 in no cut's list. **An ARMED row disarmed "by specification" three rounds ago needs a cut, or a ruling that it waits** |

## 2. L9 -- `e-2` AC4: "does each served count equal one per actual mention of that company?"

This seat re-ran `ac4_one_count_per_mention.py` against S3 (newest mention part `...T112204Z`), then counted each company's names
in the article TEXT itself (`_iter_latest_articles`).

**OVER-COUNT: GONE.**
- **AMZN crash report** (`bbg:TKYJAAVTTCZL00`): served **8**. The raw text holds exactly **8** "Amazon" occurrences (title; "An Amazon.com
  Inc. cargo plane"; "on behalf of Amazon"; "Amazon confirmed"; "an Amazon spokesperson"; "Amazon's in-house cargo airline"; "Amazon
  Prime"; "packages for Amazon"). **8 = 8 = 8.**
- **The 8 C -> D rows** each count their one matched span once (AMZN x2, DAL, FDX, GOOGL, GOOG, UPS x2). Each was 2 before, because
  "Amazon" was counted again inside "Amazon.com", "Delta Air Lines" inside "Delta Air Lines Inc", and so on.

**UNDER-COUNT: PRESENT, FROM ALIAS COVERAGE, NOT FROM THE SPAN RULE.**

| row | served | the text also says | true count |
|---|---|---|---|
| UPS in the crash report | 1 ("United Parcel Service Inc.") | "since a **UPS** freighter was destroyed" | **2** |
| GOOGL / GOOG in the YouTube article | 1 ("Alphabet Inc.") | "**Google**'s leading artificial intelligence", "the **Google** universe" | **3** (if Google counts as Alphabet; a PM would read it so) |
| DAL, FDX in their articles | 1 | no other form (Delta x1, FedEx x1) | 1 -- **equal** |

**VERDICT: MET on the question the round was cut for** (one count per matched span: no double counting, 8 = 8 on the one multi-mention
row). **NOT MET as literally asked** ("one per ACTUAL mention") on 2 of the 4 row-articles this seat read: the matcher cannot count a
mention it has no alias for. **This is round 14's "Amazon" class again**: a company named by its ticker ("UPS") or its operating brand
("Google") is invisible to an alias list of legal names. The one-span fix did not cause it; alias coverage did.

⚠ **BOUND:** this seat counted alternative forms in 4 articles (crash report, YouTube, Delta, and the NTSB piece checked for UPS), not in
all 275 mention rows. A census of ticker and brand forms per security is the instrument that would size it.

## 3. L10 PRECONDITION

1. **Every task order terminal** -- 2 of 2. **MET**
2. **Every BLOCKING or ARMED row dispositioned** -- `Z-W41-S2` GRADUATED on measurement; the rest CARRIED with reasons. **MET**
3. **Every judgment criterion graded** -- 1 of 1. **MET**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S34",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-29T12:05:00Z",
    "one_line": "L9 round 16: the double count is gone -- the AMZN crash report serves 8 and its text holds exactly 8 'Amazon' occurrences, and each of the 8 C->D rows counts its one span once (Z-W41-S2 graduates). But 'one per actual mention' is not met where a company goes by a ticker or brand the alias list lacks: the crash report also says 'a UPS freighter' (true 2, served 1), and the YouTube piece says 'Google' twice (Alphabet served 1). This is round 14's alias-coverage class, not the span rule.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED, not adopted: HVST-e-1 and HVST-e-2 read 'complete' on their LAST <status> tag; judgment=\"true\" on e-2 AC4.",
        "L8: _latest_dispositions('.', 'AMGT_HARVST') 99 items, 18 UNDER_INVESTIGATION; ARMED Z-S37, Z-W39-S1, Z-W40-S1, Z-W41-S1, Z-W41-S2.",
        "AC4, this seat's run of ac4_one_count_per_mention.py: 'rows whose tier moved (previous -> newest part): 8 of 275; plus the AMZN crash report row => 9 rows presented'. AMZN bbg:TKYJAAVTTCZL00 'SERVED: mention_count=8 match_forms=[Amazon, Amazon.com Inc] signal_tier=A (was ... mention_count=10 ...)', 8 spans listed. Each C->D row: 'matched spans listed above: 1 ... served mention_count: 1' (was 2).",
        "RAW TEXT, this seat's regex over title+text of bbg:TKYJAAVTTCZL00: 8 'Amazon' substrings, matching the 8 spans; 1 '\\bUPS\\b' ('since a UPS freighter was destroyed'), 1 'United Parcel', 1 'FedEx'. bbg:TKNDM8T96OSI00: 1 'Alphabet', 2 'Google' (\"Google's leading artificial intelligence\", 'the Google universe'). bbg:TITX6KR24U8700: 1 'Delta'.",
        "Aliases as the matcher takes them (the script's own line): UPS ['United Parcel Service Inc', 'United Parcel Service']; GOOGL/GOOG ['Alphabet Inc', 'Alphabet'] -- neither carries the ticker or the brand."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W41-S2"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The packet @8d396187d9 asserts 2 orders terminal and VALID, 14 mention rows and 212 daily cells moved inside the pair, the AMZN crash report at mention_count 8, and e-2 AC4 presented.",
    "world_is": "True as re-run: over-counting is gone and 8 = 8 on the crash report. Counts fall short of actual mentions where a company is named by a ticker or brand the alias list lacks (UPS, Google), which is a recall gap in alias coverage, not a defect of the one-span rule.",
    "notes": "FOR THE ROUND-16 ANALYSIS: (1) alias coverage should include each security's common ticker and operating-brand forms, with a control against common-word collisions (the round-15 river/rainforest check is the model); a per-security census of those forms sizes the gap first; (2) Z-W40-S1 has been ARMED-by-specification since round 14 and in no cut since; cut it or rule that it waits."
  }
]
```
