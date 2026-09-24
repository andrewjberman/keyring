# PLAN -- how AMGT_RESAPP's data is structured and managed in `opal-data-harvest`

**From** `4.0.0_SA_CRO~Z`, 2026-09-18 ~23:0xZ, at Andrew's ask: *"i want you to do a deep dive on teh shapes of the data
we're pulling from the various sources for RESAPP, and review the LGIC_NAMING system standards, and come up with a plan
on how to manage this properly. We can run bronze and silver inside the opal-data-harvest bucket, that is fine, it does
not need to be in opal-data-assets, which i believe should exclusively be for client assets."* **To** `1.0.0_SA_CTO~Z`
for the L4, with `0.0.0_AB_MSTR~Z` on the registry rows. **Status:** a PLAN. It moves no object, writes no registry row
and cuts no cell.

**Its two measured halves, both committed with it:** `RESAPP_DATA_SHAPE_INVENTORY_20260918.md` (every stream, its shape
and its tier) and `LGIC_NAMING_STANDARD_READ_20260918.md` (the grammar, the builders run, the refusals verbatim).

---

## 1. The answer in one screen

**Andrew's instruction costs zero data movement.** All 1,333 AMGT objects (31.9 MB) are already in
`opal-data-harvest`, and the estate writes NOTHING to `opal-data-assets` (`opal-data-assets` occurs 0 times in
`lib/research`'s 134 files). The whole job is the KEY GRAMMAR above the bucket, plus five structural defects the
grammar cannot fix by itself.

| what | today, measured | under the plan |
|---|---|---|
| addresses | 16 top-level prefixes named after ENGINES (`peers/`, `posture/`, `scores/`), so no address says what tier it is | `{source}/{scope}/{tier}/{table}/{partition}`, tier in the third segment |
| the builder | `address()` REFUSES every AMGT key (`scope 'amgt' resolves to no scopes.json row`); it returns an `opal-data-harvest` address in 0 of 1350 combinations | one `scopes.json` row plus the tenancy decision, then every address comes from the builder |
| bronze | `raw/bloomberg/` and `raw/seekingalpha/` keep vendor bytes; **EDGAR and the publishers keep NONE** | raw bytes land before any derivation, for every source |
| identity | six key conventions live, one of which puts a `/` inside the key (10 objects) | one key form, slash-safe, minted in one place |
| writers | 4 `write_pool*` implementations + 5 direct `put_object`s; integrity metadata present or absent by accident | one write path, metadata on every object |
| vintage | posture overwritten in place on 31 of 33; 632 non-latest versions against a contract that says "nothing is ever written to a path that already exists" | vintage in the key, no overwrite in place |

---

## 2. What we pull, and what tier it is (the inventory, condensed)

Twenty-five streams. Tier per the canon's own definitions (bronze RAW as delivered; silver typed derivation; gold
firm/product-attributable product; platinum the serving format; state pointers and logs).

| tier | streams | objects |
|---|---|---|
| **BRONZE** | `raw/bloomberg/` (refdata, histdata), `raw/seekingalpha/` (the untouched JSON:API envelope) | 97 |
| **SILVER** | crosswalk, union universe, filing analysis, management roster, model block, model block FYE, publication links | ~90 |
| **GOLD** | drafting, management pool stat, posture, peer sets, scores, the metrics table | ~880 |
| **PLATINUM** | none in S3 -- the page is served by the API from gold and silver | 0 |
| **STATE** | UNRESOLVED-SOURCE markers (176), pack ledgers and status, identity crossref, release artifacts | ~220 |

**Three shapes do not fit their prefix, and these are the plan's real decisions:**

1. **`filings/v1/<key>/<accession>.source.json` is bronze and silver in ONE object, and its bronze half is a
   TRUNCATED EXCERPT of bytes nobody kept.** It carries `excerpt.text` (137,314 characters for Boeing) and
   `document_sha256` -- a hash over the full EDGAR document, which is stored NOWHERE (0 of 1,333 objects). **A re-parse
   with a new `parser_version` cannot be replayed.** This is the single most consequential finding in the inventory.
2. **`publications/v1/` keeps no vendor response either** -- `response_sha256` attests bytes that are gone; what
   remains is block-segmented text. It is silver whose bronze does not exist.
3. **`derived/model_block/` is SILVER, not gold**, despite the name: every figure is a unit-tagged restatement of
   Bloomberg's own fields, with Opal judgment applied only above it (scores, posture).

---

## 3. The standard, and exactly what it refuses today

**The grammar** (`02_DOCTRINE.md:209-229`): `s3://{bucket}/{source}/{scope}/{tier}/{table}/{partition}/{object}`.
The bucket is the container and never a segment; the tier is always the third segment and one of six closed tokens;
`state` is a tier, not a folder inside one; a new platinum leaf is kebab-case `.json`.

**Measured refusals, from running the builders:**
- `address()` and `key()` refuse `scope='amgt'` and `scope='harvest'`: **no `scopes.json` row** (9 rows exist; none is
  ours). `systems.json` DOES carry `amgt` and `harvest` -- a different file and a different slot, which is why this
  looks registered at a glance.
- **A scope row alone cannot honour Andrew's instruction:** `tiers.json` homes bronze and silver to
  `shared:opal-data-assets` in **4 of 4 tenancies**. Simulated: a `harvest` scope row puts gold, state and code in
  `opal-data-harvest` and leaves bronze and silver in assets. A tenancy whose six cells are `home: scope` puts all six
  tiers in `opal-data-harvest` (validate: 0 refusals; negative control fires on an unknown tenancy).
- **The scope token must not be `amgt` under source `amgt`:** `a product is never a scope beneath itself`.
- **Three of our sources have no `systems.json` row at all: EDGAR/SEC, Lusha and Bright Data** (`bloomberg` and
  `seeking-alpha` exist as VENDOR rows). They cannot be named in a conforming key today.
- **The gate cannot catch this class:** `grade()` accepts a systems.json-only PRODUCT key in the scope slot, so a
  hand-typed `bloomberg/amgt/bronze/...` passes the commit gate while `address()` refuses it. And the naming gate is
  ENFORCING, not WARN (`org/mcp/naming-gate.enforce`, committed `d181e0ac5a`) -- CLAUDE.md Rule 30's "WARN today" is stale.

---

## 4. The target grammar for RESAPP

**Vendor bronze keeps the vendor as the source, our project as the scope:**

| stream | target address |
|---|---|
| Bloomberg reference | `bloomberg/<scope>/bronze/security_reference/date=<d>/<security>.json` |
| Bloomberg history | `bloomberg/<scope>/bronze/security_history/date=<d>/<security>.json` |
| Seeking Alpha | `seeking-alpha/<scope>/bronze/<endpoint>/date=<d>/<security>.json` |
| EDGAR filing (NEW) | `sec/<scope>/bronze/filing/<accession>/<primary_document>` -- the fetched bytes, verbatim |
| publisher article (NEW) | `<publisher>/<scope>/bronze/article/<sha256>/response.json` |

**Our own derivations take `amgt` as the source.** The scope token beneath it cannot be `amgt`, and a PRODUCT scope
beneath a PRODUCT source is refused, so the derived tiers resolve through the COMPOSITE route: `amgt/global/<tier>/...`
(`global` is the registered COMPOSITE scope). Measured consequence: gold, state and code under `global` are
SOURCE-homed, so they need an `amgt` scopes.json row naming `opal-data-harvest`; bronze and silver under any scope need
the tenancy decision. **The exact token pair is the L4's to fix** -- the two candidates are `<vendor>/harvest/...` +
`amgt/global/...`, or `<vendor>/amgt/...` + `amgt/global/...` -- and both are measured above.

| stream | tier | table (proposed) |
|---|---|---|
| crosswalk, union universe | silver | `identity_crosswalk`, `union_universe` |
| filing analysis, passages | silver | `filing_analysis` |
| model block (+ FYE) | silver | `model_block`, `model_block_fye` |
| management roster | silver | `management_roster` |
| publication links | silver | `publication_link` |
| drafting, peers, posture, scores, management pool | gold | `thesis_draft`, `peer_set`, `posture_verdict`, `security_scores`, `management_pool` |
| the page payload, if ever landed | platinum | kebab `.json` |
| UNRESOLVED markers, pack ledger and status, run logs | state | `filing_unresolved`, `pack_ledger`, `pack_status` |

**The `v1` in ten prefixes retires.** No prefix ever had a `v2`; the documents already carry `schema_version`, which is
the field that actually moved. It is decorative, and it has already cost precision in an IAM grant.

---

## 5. The five defects the grammar does not fix, and what each needs

1. **Bronze retention (the one that cannot wait).** EDGAR documents and publisher responses are not stored. Land the
   fetched bytes at bronze BEFORE any derivation (`C-RAW-BEFORE-DERIVED` already says so; the filings path does not obey
   it), and have the silver object cite the bronze key instead of embedding an excerpt of it. Until then, every parser
   change is unrepeatable and `document_sha256` attests nothing anyone can check.
2. **One security key.** Six conventions are live; `BP/_LN_Equity` and `NG/_LN_Equity` put a `/` INSIDE the key, so 10
   objects sit one level deeper than their siblings and every `split("/")` reads a phantom security called `BP`. Mint
   one form in one place, slash-safe, and let every key builder take it from there.
3. **One write path.** Four `write_pool*` implementations plus five direct `put_object`s mean integrity metadata is
   present or absent by accident. One writer, `document-sha256` and `schema-version` on every object, read-back
   verified.
4. **Vintage in the key, never an overwrite.** Posture is rewritten in place on 31 of 33 objects (the key says 16 Sep,
   the write was 18 Sep); `filings/` carries 506 non-latest versions because the UNRESOLVED marker has no vintage at
   all. The bucket's own declared contract says nothing is ever written to an existing path; 632 non-latest versions
   say otherwise.
5. **Two grammars in one prefix, twice.** `scores/v1/` holds 33 canonical + 31 superseded objects whose
   `schema_version` is a STRING where the canonical is an INT; `peers/v1/` holds a dated form (empty members) and a
   stamped form (12 members) that resolve by ASCII luck, so a 2026-10 dated object would serve the empty shape. Retire
   one of each, and make the reader resolve by rule rather than by sort order.

---

## 6. How to move, without a day of the page being wrong

**The order is fixed by one fact: only ONE of seventeen S3 streams has a trigger** (`amgt-resapp-chatter-axis-daily`).
Everything else is produced by hand, so there is no race between a producer and a migration.

1. **Registry first** -- the rows, then `address()` returns a real address. Nothing else can be built honestly before it.
2. **Writers second** -- each producer takes its address from `address()` and writes the NEW key. **Both keys are
   written for one cycle.**
3. **Readers third** -- the adapter reads NEW, falls back to OLD, and prints which it used.
4. **Backfill fourth** -- copy the existing objects to their new addresses, vintage preserved, never a rewrite.
5. **Cut the fallback last**, when a census reads 0 objects served from the old address.
6. **The old prefixes stay until a census proves nothing reads them**, then they are removed in one act with its own
   change record.

**What must not happen:** a reader change and an object move in the same act, or a backfill that rewrites a document's
bytes (a re-derivation is a new vintage, not a move).

---

## 7. What this needs from others

| owner | item |
|---|---|
| Andrew | the doctrine-versus-tenancy choice, in words (still open); whether the release artifact under `lib/` leaves the data bucket |
| `0.0.0_AB_MSTR~Z` | the `scopes.json` row(s); the tenancy cells; three new VENDOR `systems.json` rows (SEC, Lusha, Bright Data) and whichever publisher rows the article stream needs; the R8 declared reason, written as X2 is written, not left OWED as X3 is |
| `1.0.0_SA_CTO~Z` | the token pair (s.4), the tier classification's final word, and where this lands: its own project under Rule 30 R19, or a declared chain |
| `2.0.0_SA_COO~Z` | the cut, when it is placed; the migration is not a rider on a round-14 cell |

---

## 8. What this plan does not claim

It does not move an object, write a registry row, or re-open round 14. It does not decide whether AMGT data is
"general" in the canon's sense -- Andrew has ruled where it lives, and the doctrine wording is his and the
integrator's. The per-stream tier table is measured from each object's own shape; the three ambiguous cases in s.2 are
argued, not asserted, and each is the L4's to ratify. And it inherits one open question the inventory raised but did
not answer: the peer-candidate database it depends on (`opal-data-portal-v2/json/security_scanner/latest/`) has not
moved in 42 days and carries no vintage in its address -- which is a different project's surface, and a real
dependency of ours.
