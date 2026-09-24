# L4-R REVIEW -- AMGT_RESAPP PRD v0.22, BRIEF HALF -- verdict: SIGN

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`d0597e7e0a`,
v0.22, brief half hash `31f3a919efdc` (msg 24250). **Brief:** @`19ce7d5b4d`, unchanged. **Prior signature:** v0.18,
`293d81a89f` (half hash `6b2257c8d997`).

## Scope, measured rather than taken from the change note

My last signature was at v0.18, and three versions passed without a brief delivery. So I computed the brief half hash
with `.tools/prd_signoff_lib.half_hashes()` at every version since: `788846596a` (v0.18), `752b2f0881` (v0.19),
`4183e30531` (v0.20) and `b2c0a06527` (v0.21) all give **`6b2257c8d997`**; `d0597e7e0a` (v0.22) gives **`31f3a919efdc`**.
So the brief bytes moved only at v0.22, and v0.20's CONTRACTS provenance cleanup touched the ratified-text half alone.

`git diff -U0 b2c0a06527 d0597e7e0a` has four hunks: the header (`:8`), the change note in the unhashed preamble
(`:204-213`), the section 11 plan pin (`:1859`), and the new section 12 (`:1900-1976`). **No BRIEF COVERAGE entry and no
brief pin moved.**

## Checks

| item | check | result |
|---|---|---|
| Andrew's word | verbatim quote against the record `ANDREW_DIRECT_20260922_135xZ_...` @`cd0cca7f46` | faithful |
| posture out, no other security, no schedule, no deletion | section 12 "does NOT authorise" against @`78106b9cea` and the trial record | faithful |
| the caps | section 12's table against the record `:23-32` ("the caps are this seat's, stated so Andrew can object") | identical; the PRD correctly calls them the L4 owner's, not Andrew's |
| key handling | composite FIGI RECORDED as an attribute, and `security_key` stays the partition key until the key design is ruled | consistent with @`6f1a72e4be` ("for the purposes of research") and this seat's research @`dbbf6fd782` s.4 |
| Z-S221 before any filing analysis | cites `ADJUDICATION_v30` @`921cc430c1` | ordering stated before the stage it guards |
| s.11 re-pin | `:1859` -> `1b43fd2933` | correct: that is this seat's SA-hash correction, and 0 later plan commits exist |
| "19 of 1,780 harvest objects" | full bucket listing just now: **1,780** objects, **18** keys contain `992_HK` (peers 5, model_block 3, new-grammar bloomberg bronze 2, raw/bloomberg 2, scores 2, packs 1, posture 1, filings/v1 1, filing_attempt state 1) | denominator agrees; numerator **18, not 19** |

## Notes, none a ground for refusal

1. **18 versus 19.** The key census finds 18 objects. The 19th may be a record carried inside a shared object (the
   crosswalk, the universe, or a silver parquet row) rather than a key. Recommend the stage table say which
   instrument counted 19, so the trial report's "before" state is reproducible.
2. **Stage 3 names "the HKEX filings the issuer publishes"**, but the filings battery's five routes are edgar-ticker,
   edgar-bloomberg-cik, esef-lei, company-site and national-regulator. HKEX is the national-regulator route, and its
   `systems.json` source row does not exist yet (plan s.5.3: "one row per regulator, minted when a route first returns
   a document"). If the trial fetches from HKEX, the builder will refuse the bronze address until that row lands. That
   is a registry-lane act, and it belongs before stage 3. **Measured:** `address("hkex","harvest","bronze",...)`
   returns REFUSED (`source 'hkex' is not a systems.json key`), and no `systems.json` key contains `hk` or `regul`. A
   document fetched from Lenovo's OWN site resolves under `issuer-site` today; one fetched from hkexnews.hk does not.
