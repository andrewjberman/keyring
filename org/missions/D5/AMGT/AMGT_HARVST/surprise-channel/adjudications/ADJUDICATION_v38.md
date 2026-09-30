# AMGT_HARVST ROUND 29 -- L8 COMPILE (no judgment criterion; two WORLD acts, one withdrawn after its act)

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~17:1xZ
**Input:** `2.0.0_SA_COO~H`'s `round29/ROUND29_DRAIN_END_PACKET.md` @`7f0333de45`, msg 27278. The packet was read to EOF (6,411 B).
**L7 re-measured:** `ab-1` and `ab-2` read `complete`, and `ab-3` reads `withdrawn`, on their LAST `<status>` tag. There are 0
judgment criteria.

---

## 1. RE-READ BY THIS SEAT

- **`ab-2`, the mention rebuild:** `amgt/harvest/gold/article_security_mention/date=2026-09-30/part-20260930T134616Z.parquet` is
  **44,376 bytes and 379 rows**.
  - Against the prior part `062354Z`: **21 new (article, security) pairs, all bbg, on 11 distinct article keys**.
  - This equals the packet.
- **Every write since 13:30Z**, from a full listing of `amgt/harvest/`:
  - **1** gold mention part (13:46:44Z);
  - **12** bronze run records (16:28-16:40Z, `ab-3` phase A);
  - **5** `research_dossier` objects (13:30-13:39Z: SHOP_CN, SNPS, SPOT, UBER, WDAY). These are AMGT_CORPUS round 24's leg-d tail,
    not this round.
  - Every write is accounted for. `ab-3` made no upload.
- **`ab-3`'s refusals, from the durable run records** (`request_attempts` across the 12 records):

  | publisher | attempts |
  |---|---|
  | barrons | 200 ok x2, then 401 `other` |
  | wsj | 200 ok x2, then 401 `other` |
  | bbg | 200 ok, then 403 `other` |
  | ft | 403 `other` |

  - The 200s in the same jobs support the packet's reading: the stored tokens authenticated, and it was the LISTING that was
    refused.
  - That makes this not token expiry, and no 429 appears, so it is not throttling.

## 2. THE FINDING THE CTO NEEDS FOR ROUND 30 -- THE RECORD CANNOT SAY "BOT CHECK"

`C-HV-TRUST-TOKEN` (v0.9, signed by this seat @`b9f1a8bc81`) requires each attempt's status and wait in the run record, "so a reader
can tell throttling from expiry". The record does that. But it has no class for the thing that actually happened.
- Every refusal is classed **`other`**.
- "Bot check" (DataDome's `geo.captcha-delivery.com` page for wsj, FT's "Security Verification", bbg's press-and-hold) is known only
  from bodies kept in the collector's LOCAL runtime `rejected_bodies/`, on site Z. Those bodies are not in the durable record.
- The contract treats a 401 that persists after backoff as expiry. So a collector reading only the record could mark a valid token
  expired and fall through to a fresh sign-in. That is the crawl Andrew said to avoid, and the path condition (ii) reserves to him.

**Asks for round 30:**
- Add a `bot_check` class, decided from the kept body's signature (the three are named above), to the attempt record.
- Make `bot_check` never mark a token expired.
- Name it in the contract, which is a v0.10 CONTRACTS line.

The route past the checks (an Andrew-run headed session, a different transport, or pacing) is the CTO's call, and Andrew's login
under condition (ii).

## 3. DISPOSITIONS

| row | disposition | grounds |
|---|---|---|
| `Z-W81-S7` (ARMED) | **GRADUATED** (disarmed) | `ab-1` A3: newest token first, complete on the trunk (close run 5/5) |
| `Z-S46` (pre-floor fetches) | **GRADUATED** (disarmed) | `ab-1` A1, a dated pre-floor hit is not fetched; its count is corrected by `Z-W81-S6` to 13 of 17 |
| `Z-W37-S4` (the sa 402) | **CARRIED**, OPEN | Per CTO msg 27213 its standing follows the probe, and the probe never requested: the security files came from the GOLD universe, which has no SA symbol (`Z-S47`). Round 30, item 2. |
| `Z-S47` (the sa probe was vacuous) | **CARRIED** | an issuer cut-time miss; the round-30 cell uses the collector's resolved securities |
| `Z-W76-S1`, `Z-W76-S2` | **CARRIED**, disarmed by `ab-1` | the live wsj path now dates from `timestamp` |
| `Z-W81-S1`..`S6`, `S8`..`S10`, `Z-W83-S1`/`S2` | **CARRIED**, INERT | as the packet |

## 4. FOR THE ROUND-29 ANALYSIS

1. **Section 2:** a `bot_check` class in the record and contract, before any retry of batch 1.
2. **sa on resolved securities, with a real account check.** It is the one publisher that may proceed now.
3. **The paired daily rebuild:** 9 of the 11 new bbg articles are dated 2015-2019 and reach no page day (`Z-S46`). Only 2 fall in
   992_HK's window.

## 5. L10 PRECONDITION

1. **Every task order terminal:** 3 of 3 (2 complete, 1 withdrawn after its act). **MET**
2. **Every BLOCKING or ARMED row dispositioned:** `Z-W81-S7` GRADUATED; `Z-W37-S4` CARRIED open with a named next act. **MET**
3. **Every judgment criterion graded:** 0. **MET (vacuous)**

---

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S48",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-30T17:10:00Z",
    "one_line": "L8 round 29: mention part-134616Z re-read (379 rows, 21 new bbg pairs on 11 keys); every write since 13:30Z accounted (1 mention part, 12 run records, 5 CORPUS dossiers); batch 1's refusals are all class 'other' in the durable record -- 'bot check' lives only in local rejected_bodies -- so the record cannot tell a bot check from expiry; Z-W81-S7 and Z-S46 graduate; Z-W37-S4 stays open (sa never requested).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "L7 RE-MEASURED: TO-HVST-ab-1, ab-2 'complete'; ab-3 'withdrawn' on their LAST <status> tag.",
        "S3 opal-data-harvest amgt/harvest/gold/article_security_mention/date=2026-09-30/part-20260930T134616Z.parquet: 44376 bytes, 379 rows; vs part-20260930T062354Z: 21 new pairs, publisher bbg 21, 11 distinct article_key.",
        "Objects under amgt/harvest/ modified since 2026-09-30T13:30Z: 18 = 1 gold mention part + 12 bronze run_record (16:28-16:40Z) + 5 gold research_dossier (SHOP_CN, SNPS, SPOT, UBER, WDAY, 13:30-13:39Z).",
        "request_attempts across run records 20260930T16*: barrons 200 ok x2, 401 other x1; wsj 200 ok x2, 401 other x1; bbg 200 ok x1, 403 other x1; ft 403 other x1; wsj job token_source saved_session_file (.runtime/opal-data-harvest/secrets/wsj.dpapi)."
      ]
    },
    "adjudicates": [
      "AMGT_HARVST-Z-W81-S7",
      "AMGT_HARVST-Z-S46"
    ],
    "disposition": "GRADUATED",
    "spec_asserts": "The drain-end packet @7f0333de45 asserts 3/3 terminal, the 11 bbg story ids on the mention plane, and batch 1 reaching 0 names because every requesting publisher met a bot check, none of it token expiry.",
    "world_is": "True as read. The bot-check diagnosis rests on locally kept bodies; the durable run record classes all four refusals as 'other', so a record reader cannot distinguish a bot check from expiry.",
    "notes": "FOR THE ROUND-29 ANALYSIS: add a bot_check attempt class from the kept body's signature, never marking a token expired, and name it in C-HV-TRUST-TOKEN; sa on resolved securities with a real account check."
  }
]
```
