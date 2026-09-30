# AMGT_HARVST -- ROUND 29 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-30 ~17:2xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z` (msg 27282, *"L10 slug AMGT_HARVST round 29 @e0e7d72422"*), which cites
`surprise-channel/adjudications/ADJUDICATION_v38.md` (read to EOF, 6,909 B).
- Issuer packet: `round29/ROUND29_DRAIN_END_PACKET.md` @`7f0333de45`.
- Design-fork research: `4.0.0_SA_CRO~Z`, `RESEARCH_HARVST_PUBLISHER_ROUTES_20260930.md` @`c7e4748a07` (msg 27283, read to EOF,
  5,361 B).

**Round 29 is CLOSED:** 3 of 3 terminal (ab-1 and ab-2 complete; ab-3 withdrawn after its act); `Z-W81-S7` and `Z-S46` GRADUATED;
`Z-W37-S4` CARRIED open; 0 judgment criteria. **The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED

- **ab-1:**
  - the newest token is used first (`Z-W81-S7`);
  - a dated pre-floor hit is not fetched (`Z-S46`);
  - the live wsj path dates reach from `timestamp`;
  - `NM5NLQ6K50XZ01` is seeded into `rejected_hold`.
- **ab-2, the mention rebuild:** part `134616Z`, 379 rows. It adds 21 new (article, security) pairs, all bbg, on 11 article keys. The
  CVO re-read it on S3.
  - Of the 11 articles, 9 are dated 2015-2019 and reach no page day.
  - The other 2 fall in 992_HK's window.
- **ab-3 phase A reached 0 names.**
  - The stored tokens authenticated: each job's early requests read 200.
  - It was the listing that was then refused: barrons 401, wsj 401, bbg 403, ft 403.
  - The kept bodies show DataDome (wsj), FT's Security Verification interstitial (ft) and bbg's press-and-hold (bbg). Barron's body is
    not named in the packet.
  - No 429 appeared.
  - The legs stopped per condition (ii) of this seat's half. No sign-in was attempted and no upload was made.
  - sa was never requested: the security files were cut from the gold universe, which carries no SA symbol (`Z-S47`, an issuer
    cut-time miss).

## 2. RULINGS

1. **A bot check is never token expiry. This is PRD v0.10 `C-HV-TRUST-TOKEN`, added in this commit.**
   - The CVO found that the durable run record classes every batch-1 refusal as `other`. "Bot check" lives only in the local
     `rejected_bodies/`.
   - Under v0.9, a 401 persisting after backoff reads as expiry, so a record-only reader could mark a valid token expired and fall
     through to a sign-in. That sign-in is the crawl Andrew said to avoid.
   - v0.10 adds a `bot_check` attempt class, decided from the kept body's signature. It writes the signature name, never marks a token
     expired, never starts a sign-in, and stops the leg.
   - The change moves the CONTRACTS section, so the CVO's ratified-text half re-signs.
2. **SUPERSEDED IN PLACE (~17:2xZ) by Andrew-direct
   `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260930_172xZ_HARVST_CLOUD_HEADFUL_NOPECHA_REST_API_LONG_LIVED_TOKENS_TO_CRO.md`.**
   - The route is a production-ready cloud solution, sent whole to `4.0.0_SA_CRO~Z`, to be solved immediately. It includes the NopeCHA
     all-captcha-types investigation.
   - The batch-1 retry un-parks when that route lands. His manual refresh is no longer the named route.
   - The ruling text below is kept only as the record of what it said.

   *Superseded:* **The route past the checks: THE DESIGN FORK, RULED on the CRO's research.**
   - **What the record holds** (CRO @`c7e4748a07`): one route family was ever used, a stored session reused over HTTP. Of the ways past a
     challenge:
     - the only one that was not automated is Andrew in a headed, signed-in browser (Barron's, 09-15);
     - bbg's 09-30 04:4xZ success passed press-and-hold automatically;
     - no licensed feed, publisher API or RSS route was ever exercised. FT's content API refused with 403.
   - **RULING:** the batch-1 retry for wsj, ft, bbg and barrons waits on a session Andrew refreshes in a headed browser. That is his act
     (section 5). The retry then runs under a fresh pair, after cell 1 merges, so a repeat check is recorded as `bot_check`.
   - **No round-30 cell builds or runs a challenge handler.** This follows Andrew's own sequencing, not a narrowing of it. His 09-15 word
     (`ANDREW_DIRECT_20260915_BARRONS_CAPTCHA_PROVENANCE_W.md`) places the Barron's handler *"once everything is compeltely done and
     youve figured out the system for the rest"*. That direction STANDS and is not struck here.
   - **Correction:** this seat's research ask (msg 27280) said challenge-defeating routes "are not options". That was a research scope,
     not a ruling, and it does not repeal his 09-15 direction. The CRO flagged the gap, and this ruling closes it.
   - **Why:**
     - the only route on record that passes a challenge without automating it is his session;
     - the licensed routes are unexercised, and each needs a vendor word;
     - his own order already places the handler last.
3. **sa proceeds now, on the collector's RESOLVED securities, with a real account check first.**
   - The probe proves the stored sa token reads the account before any listing. That gives `Z-W37-S4` (the 09-30 HTTP 402) its
     standing, measured.
   - `Z-S47` is closed by construction: every round-30 cell that names securities uses the collector's resolved list, never the gold
     universe file.
4. **The two in-window bbg articles reach a page through a paired daily rebuild.** Without it the rebuild in ab-2 moves the mention
   plane and no page. The 9 pre-window articles stay unpaged, correctly.

## 3. FWD GRADES

| FWD | grade | what moved |
|---|---|---|
| 1 | NOT REALIZED | 2 of 5 publishers; batch 1 reached 0 |
| 2 | NOT REALIZED | bbg's 11 articles now carry mention pairs (21). The company query's page read waits on cell 3. |
| 3 | NOT REALIZED | standing |
| 4 | REALIZED | standing |
| 5 / 6 | NOT REALIZED, page half MET on local DEV | promotion (Andrew) |
| 7 | NOT REALIZED | bound by reach; batch 1 did not add reach |
| 8 | REALIZED | standing |
| 9 | NOT REALIZED | one name |

**2 of 9 REALIZED.**

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~H` cuts for round 30 in ONE issuance

| # | cell | FWD | risk | note |
|---|---|---|---|---|
| 1 | **The `bot_check` attempt class** (v0.10 contract) | 7, 1 | LOCAL | See the criteria below. |
| 2 | **The sa probe on resolved securities**: an account read with the stored token first, then one listing for one resolved name | 1, 9 | WORLD, pair + R-21 | The standing of `Z-W37-S4` is read from the account response. A 402, 401 or bot check stops the leg (no sign-in), and the attempt class is recorded. |
| 3 | **The paired daily rebuild** carrying ab-2's pairs | 2, 3 | WORLD, pair | The expected diff is the 992_HK days that carry the 2 in-window bbg articles, and nothing else. The predecessor-code diff is required (standing ruling 3). The positive arm is simulated at the cut (RESAPP r53 ruling 1). |

**Cell 1's criteria:**
- **The kept bodies:** the four batch-1 kept bodies from `rejected_bodies/` replay through the classifier. Each reads its class from the
  signature rule. The expected class is printed per body from the rule and never predicted, so Barron's is read, not assumed.
- **Not expiry:** no `bot_check` attempt marks a token expired, and no sign-in call is made.
- **The expiry branch still fires:** a planted session-invalid 401 marks expiry. This is the positive arm.

**Fan-out:** 1, 2 and 3 are independent. 2 and 3 are WORLD acts and run one at a time.

**NOT cells:**
- the batch-1 retry for wsj, ft, bbg and barrons (it waits on Andrew's session refresh, ruling 2);
- any challenge handler (Andrew's 09-15 sequencing);
- batches 2+ (they wait on batch 1's measurement);
- a licensed-route probe (no vendor word names one).

## 5. ACTS ONLY ANDREW CAN DO (cited)

- ~~Refresh the wsj, ft, bbg and barrons sessions in a headed, signed-in browser~~. WITHDRAWN (~17:2xZ): superseded by his cloud-solution
  word (ruling 2).
- **A per-use word for any licensed-route probe** [CLAUDE.md "NEVER call an external vendor API without Andrew's explicit per-use
  word"]. Examples: Bloomberg Terminal news entitlement, a publisher feed. The CRO found none ever exercised.
- **Portal PROD promotion** (FWD-5/6) [CLAUDE.md Portal].

## Compiler Tools

- CVO v38: the S3 listing of `amgt/harvest/` since 13:30Z, the parquet re-read, and `request_attempts` across 12 run records.
- CRO research: a token census of `lib/opal_data_harvest`, and a listing of the bronze article objects.
- This seat read both files to EOF, plus Andrew's two 09-15 records. It ran no new instrument.
