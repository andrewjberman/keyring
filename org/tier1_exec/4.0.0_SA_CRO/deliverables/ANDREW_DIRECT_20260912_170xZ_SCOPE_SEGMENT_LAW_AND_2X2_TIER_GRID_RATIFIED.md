# ANDREW-DIRECT 2026-09-12 ~17:0xZ -- two `/open-calls` recs approved: NO entity ids in the scope segment; the 2x2 tier grid is THE rule

**archetype:** SCRIBE (record)
**Channel:** the `4.0.0_SA_CRO~D` terminal, direct to this seat. **Recorded by:** `4.0.0_SA_CRO~D`.
**Author:** 4.0.0_SA_CRO (Chief Research Officer)
**Home:** org/tier1_exec/4.0.0_SA_CRO/
**Status:** LAW-SHAPED DIRECTION RULED. ⛔ **NOTHING MOVES. NOT A MIGRATION AUTHORIZATION.** The
~16:1xZ pause on projects actively building data pipelines is UNCHANGED by this.

---

## 1. THE WORDS, VERBATIM AND COMPLETE

> **"Recs approved. How do we structure the implementation of these now? I am wondering if it is a
> brief that effectively becomes the principal priority project. We just need to decide the outcomes
> and the sequencing of outcomes."**

⛔ **THAT IS THE WHOLE OF WHAT HE SAID.** The first two words answer the two-card `/open-calls` set
this seat put to him minutes earlier; the rest is a question to this seat, recorded because it names
the shape he is reaching for (a BRIEF -> the principal priority project) and is not itself a ruling.

Immediately before, answering `/next-steps`, VERBATIM: *"I agree with all of these and their
ordering"* -- DIRECTION (not law): execute the five options in rank order.

---

## 2. WHAT "Recs approved" RULES, CARD BY CARD

| card | the call | ruling |
|---|---|---|
| 1 | May an ENTITY IDENTIFIER (UUID, account id, company slug) occupy the `{scope}` segment of the canonical grammar? | **REC APPROVED -- NO.** A scope is a business unit (a firm, a product, a master). An entity id belongs in the KEY or the PARTITION beneath the layer, never above it. |
| 2 | Ratify the 2x2 (general / client-confidential x served-as-ingested / derived) as THE rule for which tiers are mandatory? | **REC APPROVED -- YES.** |

### The scope-segment law, as it now binds

```
{source}/{scope}/{layer}/{type}/{date}/...
          ^^^^^^^
          a FIRM, a PRODUCT, or a MASTER -- never an entity identifier.
          smartx/platform/          CONFORMANT   (a stable scope name)
          smartx/account/{uuid}/    VIOLATION    (7,066 planes minted this way)
          smartx/allocation/{uuid}/ VIOLATION    (5,366)
          smartx/model/{uuid}/      VIOLATION    (11)
          opal-data-imo corp/{co}/  VIOLATION    (304, dead 103d)
```
Measured basis: `DATA_ENGINEERING_BIBLE_PART1_ESTATE_PLANE_CENSUS_20260912.md` s.3 (`d35653da5e`).

### The 2x2 tier grid, as it now binds

| | **served as-ingested** | **derived** |
|---|---|---|
| **general** (ETFs, harvest, market) | bronze -> serve. **No silver/gold/platinum required.** (Pathfinder, TrueShares) | bronze -> silver -> gold -> platinum in `opal-data-portal-v2`. **Recommended.** |
| **client-confidential** | bronze -> silver -> serve from the firm bucket | **ALL FOUR TIERS, IN THE FIRM BUCKET. MANDATORY.** |

Andrew's own words behind it (~15:5xZ, this session): the discipline is *"mandatory"* for client data
and a *"general rule of thumb ... recommended to be followed"* elsewhere; *"if the information can be
presented raw, then there isn't really a need to do all of this stuff"*; and the reason client data
is different: *"for clients, we may want to do a lot of derivation, and we need audit for where the
numbers came from."*

---

## 3. ⛔ WHAT THIS DOES **NOT** RULE

1. **NO MIGRATION IS AUTHORIZED.** SmartX's 12,432 planes stay exactly where they are. Naming a
   plane a VIOLATION classifies it for the conformance ledger; it does not move it. NEVER#3 unchanged.
2. **The general+derived cell is RECOMMENDED, not mandated.** A general pipeline that skips a tier
   is a declared exception to record, not a defect to fix.
3. **D10-1 (product- vs firm-shaped, per scope) is UNCHANGED** -- the default and the mechanism were
   ruled at 16:0xZ; per-scope ticks still return to him. Card 1 rules what a scope IS, not which
   shape each one takes.
4. **Nothing here lifts or narrows the ~16:1xZ pause.** Its lift is his word, by name.

---

## 4. CLOSED BY THIS SEAT'S OWN CORRECTION, RECORDED SO IT IS NOT RE-ASKED

**Client SILVER home is NOT an open call and this seat twice presented it as one.** Andrew-direct
2026-08-25 ~17:55Z: *"SILVER event-triggered parquet conversion, in opal-data-assets (unchanged)"*;
restated in the 17b amendment `dd9b33de65`. The ADVI clause that appeared to conflict governs
PORTAL READS, and silver is never portal-read. Settled: **client silver lives in `opal-data-assets`.**
`opal-data-inf/silver/` (16,757 live objects) is a D10-2 migration row, not a decision.

---

## 5. DIRECTION IN FORCE FROM THE SAME EXCHANGE

`/next-steps` five options approved in order: (1) the doctrine as a checkable rule set; (2) the D10-1
scope tick-list; (3) contradiction check on the paused projects; (4) re-derive the ADVI routing half;
(5) the identity-spine draft. Option 1 is in flight at this seat.

His structural question -- brief -> principal priority project, decide outcomes + sequencing -- is
answered in-terminal this turn and, if he blesses the shape, becomes the L1 brief via `/brief-create`
(4.0.0_SA_CRO only, Rule 27).
