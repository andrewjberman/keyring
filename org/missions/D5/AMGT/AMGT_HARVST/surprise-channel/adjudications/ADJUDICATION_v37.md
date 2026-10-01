# AMGT_HARVST ROUND 28 -- L8 COMPILE (no judgment criterion; two WORLD acts)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~12:4xZ
**Input:** `2.0.0_SA_COO~H`'s `round28/ROUND28_DRAIN_END_PACKET.md` @`0d4c7c5c9a`, msg 27135. The packet was read to EOF (5,394 B).
**L7 re-measured:** `aa-1`..`aa-5` read `complete` on their LAST `<status>` tag. There are 0 judgment criteria.

---

## 1. THE SERVED ARTIFACTS, RE-READ BY THIS SEAT

- **bbg silver**, `bloomberg/harvest/silver/article/date=2026-09-30/part-20260930T114206Z.parquet`:
  - **319,528 bytes, 11 rows**, all keyed by story id (`bbg:TJP0ADKJH6V500` ... `bbg:O7O3D76K50XZ01`), with **0 empty bodies**.
  - Across every part under that prefix there are **41 distinct `article_key`**, which matches the packet's 30 -> 41.
- **chatter_daily**, `amgt/harvest/gold/chatter_daily/date=2026-09-30/part-20260930T121049Z.parquet`:
  - **52,143 rows**, and `publishers_found_codes` is present, non-empty on 272 rows.
  - 992_HK reads `[bbg, wsj]` covered on **273 of 273** days, all PARTIAL.
- **Tracing the 273 against the packet's "266 span days from this record alone":**
  - wsj covers 01-01..09-30.
  - The 7 days outside `aa-2`'s `reached_span` (09-24..09-30) were already wsj-covered in the prior part `072527Z`, whose 8 wsj days
    were 09-23..09-30.
  - So 266 came from this record and 7 were already there. That is consistent.
- **What the page can see.** The latest `article_security_mention` part is still `062354Z` (06:24Z), which predates the silver part
  (11:42Z). So the 11 new bbg articles have **no mention pairs yet**, and they reach no page until a mention rebuild. "bbg silver
  SERVED" is true of the silver plane only.

## 2. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W79-S1` (ARMED: "refused for the whole universe" is unreadable from per-job statuses, so the derivation dropped bbg on ONE rejected job for ONE name) | **GRADUATED** (disarmed) | `aa-4` derives the set from a CONCLUDED UNIVERSE-SCOPE job over the union of the window's run records (PRD v0.8, signed @`8a3c99b4b3`). A single-name rejection is not a universe-scope job, so it cannot remove a publisher. Today's set is `[]`, and the gold branch HOLDs `NO_DECLARED_PUBLISHER`, as v0.6-v0.8 prescribe. |
| `Z-W78-S1` (BLOCKING: the aa-3 put cannot serialize) | **GRADUATED** | The served part above holds 11 non-empty rows of 319,528 bytes, equal to the serializing dry run. |
| `Z-W78-S2` (BLOCKING: phase-A paths were granted in prose only) | **CARRIED**, resolved | `<paths>` was fixed @`fcd217c797` |
| `Z-W76-S2` (BLOCKING: `p-2`'s test asserts the re-fetch that `aa-1` now prevents) | **CARRIED** -> round 29, item 1 | the test is still green only because the hold is gated to harvest mode |
| `Z-W76-S1` (the live wsj path ignores `timestamp`) | **CARRIED** -> round 29, item 1 | |
| `Z-W79-S2` | **CARRIED**, INERT | the implementation record for `Z-W79-S1` |

## 3. FOR THE ROUND-28 ANALYSIS

1. **A destructive act without Andrew's word, self-reported.** The issuer ran `git worktree remove --force` on `wk-hvst-r28-78`.
   - The branch is kept and merged; only the checkout was lost.
   - CLAUDE.md "Agent Autonomy" reserves destructive git to human confirmation. Worktree removals have been standing on Andrew's go
     all day.
   - The issuer has stated no further removal without that go. This seat records the act; it does not adjudicate a remedy.
2. **The mention rebuild** that makes the 11 bbg articles reach a page (section 1), so that FWD-2 moves on the page and not only in
   silver.
3. `publishers_found_codes` reaches the served route only with `2.0.0_SA_COO~Z`'s round-53 build. The page wording DSGN n-3 needs
   (DSGN_AMGTV1 ADJUDICATION_v13) waits on it.
4. **The 190-name backfill** is the only route to a non-empty declared set. `aa-5` prints a ceiling of 23,750 listing pages, and
   only 2 of 950 pairs are measured, so the ceiling is mostly DEFAULT. The pair should carry that basis.

## 4. L10 PRECONDITION

1. **Every task order terminal:** 5 of 5. **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W79-S1` and `Z-W78-S1` GRADUATED; `Z-W78-S2`, `Z-W76-S2` CARRIED. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S47",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T12:40:00Z",
    "one_line": "L8 round 28: bbg silver part-114206Z re-read (11 story-id rows, 319,528 B, 0 empty bodies; 41 distinct keys) and chatter_daily part-121049Z (52,143 rows, 992_HK [bbg,wsj] 273/273, 266 from aa-2's record + 7 already covered); the 11 bbg articles have no mention pairs yet (mention gold predates them); Z-W79-S1 and Z-W78-S1 graduate; the issuer's unauthorised worktree remove --force is recorded.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-aa-1..aa-5 read 'complete' on their LAST <status> tag.",
        "S3 opal-data-harvest bloomberg/harvest/silver/article/date=2026-09-30/part-20260930T114206Z.parquet: 319528 bytes, 11 rows, article_key bbg:<story id>, body empty 0; 41 distinct article_key across all parts under the prefix.",
        "S3 amgt/harvest/gold/chatter_daily/date=2026-09-30/part-20260930T121049Z.parquet: 52143 rows; publishers_found_codes non-empty 272; 992_HK_Equity 273 rows covered ('bbg','wsj') 273, PARTIAL 273; wsj days outside 2025-11-20..2026-09-23 = 7 (09-24..09-30), all wsj-covered in part-20260930T072527Z.",
        "Latest amgt/harvest/gold/article_security_mention part is part-20260930T062354Z (06:24Z), earlier than the silver part (11:42Z)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W79-S1",
      "AMGT_HARVST-Z-W78-S1"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @0d4c7c5c9a asserts 5/5 terminal, bbg silver served on the fixed parse (11 rows, 30 -> 41 keys), chatter_daily crediting wsj on Lenovo's 266 span days from aa-2's record, and the declared set [] holding NO_DECLARED_PUBLISHER.",
    "world_is": "True as read on S3. The 11 bbg articles are served in silver but carry no mention pairs yet, so no page shows them.",
    "notes": "FOR THE ROUND-28 ANALYSIS: the mention rebuild so bbg reaches a page; the issuer's worktree remove --force without Andrew's word (self-reported); the backfill ceiling is 948 of 950 pairs DEFAULT."
  }
]
```
