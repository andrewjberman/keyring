# L4-R review -- ETFS_RIVALS PRD v0.1, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** `3.0.0_SA_CVO~Z` - **Written:** 2026-09-30 ~06:2xZ
**Delivery:** 1.0.0_SA_CTO~Z msgs 26958/26959. The PRD is
`org/missions/D4/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` @`6492522bac`, with half_hash `d01a72df1807`.
**`prd-signoff status`:** the ratified-text half is MISSING and OWED BY 3.0.0_SA_CVO~Z (live). The brief half is SIGNED (auto, the
CRO wrote the brief).
**Sign-off mode:** proportionate (rule 27). This seat signs once, and a wording change under the section hash does not re-open.

**VERDICT: REFUSE -- one operative constraint of Andrew's is absent from CONTRACTS. The fix is one bullet in C-SHAPES.**

---

## 1. ENDPOINT verbatim against the ratified pin: PASS

The FWD-1..FWD-9 block in the PRD was compared byte for byte with the block in
`ENDPOINT_FORWARD_RIVALFUNDS_20260930.md` @`33c1d096a3`, the pin Andrew approved ("1.) Yes approved.", record @`77c891c869`).
**Both are 7,237 characters, and they are IDENTICAL.** The one line outside the block, "Landed verbatim from ... as Andrew approved
it", cites the pin. It is not history or a seat name. DSGN_AMGTV1's PRD carries the same pattern, which this seat signed.

## 2. Every operative constraint present: ONE MISSING

Andrew's verbatim words (`AMGT_RECONN_SOURCES_20260929/ANDREW_DIRECT.md`, read in full) were checked against ENDPOINT + CONTRACTS.

| Andrew's word | carried by |
|---|---|
| "a separate function ... etfs-rivalfunds-daily" (gap 1) | C-SEPARATE-PIPELINE, C-NAMES |
| "a platinum folder in opal-data-etfs that has the served files archived by day", "/rivalfunds" (gap 4) | C-HOMES platinum, C-SERVING, FWD-1 |
| "We definitely can use OpenAI" (gap 4) | C-VENDOR |
| "Trigger on batch complete works" (gap 6); "S9 looks fine" | C-TRIGGERS |
| "ad hoc those then from the outset" (gap 7) | C-SOURCE-POLICY backfill |
| "issuer at 7a ET and BBG ... fallback ... 8:03" (gap 9) | C-SOURCE-POLICY, FWD-3 |
| "guardrails to check on that pre-publishing" (gap 10) | C-GUARDRAILS, FWD-9 |
| "we expect them to be different in bronze/silver ... gold accrual table that coalesces the various shapes" (gap 14) | C-SHAPES |
| "less than 2Y ... as much as we can up to that threshold ... weekly, fine" | FWD-2 |
| "reverse engineer their actual trades ... a gold table for each active etf that is effectively their trade schedule"; "one really, really clear signal" | C-TRADE-SCHEDULE, C-ONE-SIGNAL, FWD-5 |
| "Trades can be 0.2% or more"; "bbg should have dividend calendar for the holdings" | C-TRADE-SCHEDULE |
| answers 2-4 (R-21 scripted; no support question; "any signed in account") | C-VENDOR, C-SERVING |
| "following LGIC NAMING standards" | C-HOMES, C-NAMES (builder output) |
| **L1 direction point 3: the canonical shape is "a denormalized base table with all info that we'd want. Every holding, every sub asset class and GICS industry tag in fields, anything we can get, put it all in there."** | **NOT CARRIED.** The PRD has **0** occurrences of "GICS", "sub asset" / "sub-asset" or "industry". C-SHAPES carries "every disclosed position" and "a raw field ... is kept", which covers what the FUND disclosed, not the classification enrichment Andrew named. |

**Why it matters and is not a wording nit:**
- CONTRACTS is what the COO decomposes and grades against. A `canonical_shape` cell could pass every contract with no
  classification columns at all.
- The brief's own supporting spec already holds the right content: `GOLD_TABLES_AND_PROMPTS.md:88-97` gives Opal classification
  (`asset_class`, `sub_asset_class`, provenance, version) and the GICS hierarchy (sector, industry group, industry, sub-industry,
  with taxonomy and version) as separate fields. At `:97` it also warns that **"the current ETF positioning vocabulary uses GICS
  sectors as an equity subasset allocation axis"**.
- That is the exact grain confusion this seat graded in DSGN_AMGTV1 rounds 8-9 (ADJUDICATION_v10 q-3 PARTIAL, v11 p-1): a
  "Sub Asset" column holding sector names beside Positioning's buckets. **Fixing it in this contract now prevents it here.**

**The fix, one bullet in C-SHAPES** (the wording is the CTO's):
> `canonical_shape` carries, per position, Opal's classification (`asset_class`, `sub_asset_class`) and the GICS hierarchy (sector,
> industry group, industry, sub-industry) as SEPARATE fields, each with its source and as-of date, per
> `GOLD_TABLES_AND_PROMPTS.md:88-97`. A value that cannot be resolved is carried with a status, never guessed.

## 3. No annotation, history or seat name inside the ENDPOINT section: PASS

Inside the section there is only the pin citation (section 1). ⚠ CONTRACTS carries one history line, "⚠ A correction to the brief,
measured by this seat" (C-NAMES). That is not inside ENDPOINT and is not a refusal ground, but the CTO may move it to PROVENANCE.

## 4. CONTRACTS agrees with the counterpart PRD: NOT APPLICABLE

No counterpart PRD is named. The gateway routes (`/rivalfunds`, `/rivalfunds/<day>`, `/rivalfunds/archive`) and the platinum page
are this PRD's own write surface (C-SERVING). C-SEPARATE-PIPELINE bounds it off `etfs-netassets-daily`.

## 5. On re-delivery

Proportionate sign-off: the bullet above is a CONTRACTS wording change. This seat re-reads the one bullet and signs; nothing else
re-opens.
