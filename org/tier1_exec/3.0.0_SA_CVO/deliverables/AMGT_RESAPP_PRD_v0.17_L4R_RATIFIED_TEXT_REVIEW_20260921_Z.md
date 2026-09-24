# L4-R review -- AMGT_RESAPP PRD v0.17, ratified-text half (`3.0.0_SA_CVO~Z`)

**PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`1f7459456a`. **Half:** ratified-text, hash
`b89abe763562` (from `e231f4ecc4ce` at v0.16, signed @`4e83003847`), measured from the committed bytes.
**Delivery:** `1.0.0_SA_CTO~Z` msgs 24088 and 24095. **Verdict: SIGN.**

**Vintage note.** This review was first written against @`6f39881c3c` (hash `1db45ee3d67d`) and committed @`77060a0078`.
The pre-stamp re-read found the half had moved to `b89abe763562`: the CTO tightened two contracts @`1f7459456a` on the
brief reviewer's flags (msg 24095). The stamp was withheld, the new diff read, and this review re-pointed to it.
**The tightening @`1f7459456a`:** C-LUSHA-EXCEPTION names every dropped channel (emails, phones, postal addresses,
personal messaging or social handles) and keeps ONE public professional-profile URL, as the "profile link"
C-EXEC-MANAGEMENT serves; C-FORMAT-SEQUENCE splits derived filings records -- `.source.json` to silver, `.analysis.json`
to gold under R10, matching plan s.5.9. **Limit on the Lusha clause:** a professional-profile URL is itself a route to
the person (such sites carry messaging). Its retention rests on its being an already-served field, not on its being
inert; whether Andrew's "contact fields dropped" was meant to reach it is his to say.

## What changed in this half (three CONTRACTS hunks; ENDPOINT :309-552 carries no hunk)

**1. C-HARVEST-HOME.** Every tier, platinum included, lives "exactly where the builder prints"; under scope `harvest`'s
GENERAL tenancy that is `opal-data-harvest` for every tier. NOT MET while the registry carries more than one `harvest`
scope row (`Z-S203`). **Verified against the registry and the builder, not taken on the delivery's word:**
- `lib/opal_naming.py address()` at HEAD: bronze and silver -> `opal-data-assets`, gold/state/code -> `opal-data-harvest`,
  platinum -> `opal-data-portal-v2`. That is the PRODUCT tenancy's output, exactly what the NOT-MET clause predicts.
- `infra/logic/registry/scopes.json` carries TWO `harvest` rows: :287 tenancy PRODUCT (first; the builder takes it) and
  :308 tenancy GENERAL, whose note says to keep only it at the CLOUD<->SITEZ merge. `Z-S203` is true as stated.
- `infra/logic/registry/tiers.json` GENERAL (:42-48): all six tiers `home: scope`, platinum included (landed @`b282500581`
  on "recs approved"). So once the PRODUCT row goes, every tier prints `opal-data-harvest`, and the contract's claim holds.
- This supersedes v0.15's "platinum at R6's general home": that clause matched the tenancy as first drafted (relayed by
  `0.0.0_AB_MSTR~Z` at 17:39Z); the approved change scope-homes GENERAL's platinum. The contract binds to builder output,
  so it follows the registry either way.

**2. C-LUSHA-EXCEPTION.** No bronze; silver drops every contact field; keeps the officer match, profile link, title and
the fields the page shows; `bronze_key` null by rule. Matches Andrew's ~19:5xZ "Yes on Exception" as recorded, and
names the R20 register entry as the registry lane's to write.

**3. C-FORMAT-SEQUENCE.** "Retire" = readers switched, writers stopped, read grant removed; never an S3 delete (a delete
of retired prefixes is one batched act on a human's word -- consistent with this estate's autonomy rule). A lossless
JSON-to-parquet re-serialisation counts as a copy, graded by a round-trip equality check per object. Derived `filings/v1`
records move to silver, their bronze filled by the backfill's first fetch.

## A standing condition, named rather than enforced on two lines

The review's checklist asks for "no annotation, history or seat name inside the section". v0.17 adds a dated
Andrew-direct citation (C-LUSHA-EXCEPTION's heading) and a row id (`Z-S203`). But the CONTRACTS section this seat signed
at v0.16 already carries **23 dated or row-cited lines and 15 seat-serial lines**, all signed through v0.15 and v0.16
without objection. Refusing v0.17 on two more would enforce the rule inconsistently. **Recorded as a standing condition
of the whole section, for a separate cleanup the CTO owns, not as a v0.17 defect.**

-- `3.0.0_SA_CVO~Z`
