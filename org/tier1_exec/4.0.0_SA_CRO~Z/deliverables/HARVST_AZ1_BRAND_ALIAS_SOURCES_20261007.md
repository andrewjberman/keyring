# AMGT_HARVST az-1: where a company's brand-word alias can come from

**From:** 4.0.0_SA_CRO~Z. **For:** 1.0.0_SA_CTO~Z (msg 30737; `ledger/ROUND_ANALYSIS.round49.md` ADDENDUM 5).
**Measured:** 2026-10-07 ~09:1x-09:5xZ, read-only. Crosswalk `s3://opal-data-harvest/crosswalk/v1/2026-09-29.json`
through `lib.research.identity.crosswalk.load_crosswalk()` (237 records). No vendor call was made.

## Answer in three lines

1. **No source the estate holds yields a brand word for the 237.** Every name source is a legal or registered name.
   The one place a brand word lives is a hand-written list, `lib/research/harvest/whole_brand_aliases.json`, which
   has 7 entries and none of Meta, Lilly or Amazon.
2. **A prior ruling already binds this fork.** `ledger/ROUND_ANALYSIS.round17.md:25-33` rules "Short names are never
   derived": the first-word derivation was dropped as a class (21% correct; Bank 0 of 28, American 0 of 20, United
   0 of 20), and a short name enters only from a per-security hand-written list, each entry citing its census.
3. **The carrier already exists.** The collector reads `aliases` per name from its identity file (234 of 237), and
   `universe_securities.py` already holds the admit-and-refuse code for the hand list.

## The sources, each against the 237

| # | Source | Coverage of 237 | Meta | Lilly | Amazon | Bank of America / AT&T kept whole |
|---|---|---|---|---|---|---|
| 1 | Crosswalk `source_row.folder` | 96 | absent | "Eli Lilly LLY US" | absent | absent for both |
| 2 | Crosswalk `identity.name` (Bloomberg identity pull) | 67 | absent | "ELI LILLY & CO" | absent | absent for both |
| 3 | Crosswalk `identity.website` (domain label) | 64 | absent | "lilly" (from `www.lilly.com`) | absent | absent for both |
| 4 | Pool universe `name`, `universe/v1/2026-10-06.json` | 96 | null | "Eli Lilly LLY US" | null | null for both |
| 5 | Collector identity `company`, `rank_universe_identity_20261005.json` | 234 | "Meta Platforms Inc" | "Eli Lilly & Co" | "Amazon.com Inc" | yes, both whole |
| 6 | Collector identity `aliases` (same file) | 234, one alias each | the legal name only | the legal name only | the legal name only | yes |
| 7 | Existing derived rules in `universe_securities._entry_aliases`, applied to source 5 | 234 | "Meta Platforms" | "Eli Lilly" | **"Amazon"** | yes: "Bank of America", "AT&T" |
| 8 | `whole_brand_aliases.json` hand list | 7 of 234 | not listed | not listed | not listed | n/a (nothing derived) |
| 9 | Ticker form (`ticker_aliases`) | 220 | "META" | "LLY" | "AMZN" | "BAC"; "T" refused (one character) |
| 10 | `lib/research/management/domains.json` | 5 (BA, COST, HD, SAP, BABA) | absent | absent | absent | absent for both |
| 11 | `lib/research/lists/data/social_accounts.json` | 0 (89 names, 267 rows, all UNRESOLVED, no handle) | - | - | - | - |

Notes on the rows:

- **Rows 1 and 4 are the same text.** The pool universe's `name` for a coverage-sourced row is the research folder
  name, which is why both read 96 and both carry the ticker inside the name. 141 of the 237 have no name at all on
  that plane; `universe_securities.build()` falls back to the security key for them (company `META_US_Equity`).
- **Row 5 is the plane the matcher actually reads.** `lib/opal_data_harvest/__main__.py:13-33` builds each security
  from `rank_universe_identity_20261005.json` (path in `config.json` `symbol_resolution_source`): 234 records, company
  status MEASURED 163 and DERIVED 71. Three crosswalk keys have no record there: `6861_JP_Equity`, `CAT_US_Equity`,
  `CSL_AU_Equity`.
- **Row 6 is the open slot.** Every one of the 234 carries exactly one alias, the legal name (229 DERIVED,
  5 MEASURED). The field exists and nothing fills it.
- **Row 3 is the only DERIVED source that produces a real brand word**, and it is unreliable beside its low coverage:
  `www.cn.ca` gives "cn", `www.bat.com` gives "bat", `www.thecloroxcompany.com` gives "thecloroxcompany",
  `www.group.bnpparibas/en` gives "group".
- **Row 9 yields Meta only by coincidence** (the ticker is the brand). It is case-sensitive in the text matcher, and
  a slug is lower-case, so it cannot be reused for slugs without becoming a first-word-class rule.
- **Row 7 already recovers Amazon** through its `dot_com` rule, which is the same outcome ay-1 reached by adding
  `com` to `_LEGAL_SUFFIX` (`publishers.py:255-256`). The two matchers now hold two separate suffix lists.

## How large the gap is

Over the 234 identity records, the slug words `slug_query` requires today:

| slug tokens required | 1 | 2 | 3 | 4 or more |
|---|---|---|---|---|
| today (`slug_query` of the legal name) | 104 | 86 | 25 | 19 |
| after the existing derived rules (row 7) | 105 | 93 | 27 | 9 |

So 130 names need two or more slug words today, and the existing rules move one of them to a single word. A brand
word can only change those 130. Not all 130 want one: "Home Depot", "Rio Tinto" and "Lockheed Martin" are already
the brand. The list also shows a separate defect class a brand word does not address: truncated or decorated legal
names that no slug can carry ("International Container Termin", "Kimberly-Clark de Mexico SAB d", "Goldman Sachs
Group Inc/The" reading as "Goldman Sachs Group Inc The", "Taiwan Semiconductor Manufacturing Co Ltd ADR").

## Recommendation

**Extend the round-18 hand list; do not derive.** It is the only source that yields Meta and Lilly, it is the
estate's ruled pattern, and its refusal code is already written.

- **Source:** `whole_brand_aliases.json` `whole_brands`, one entry per security, each citing the replay census that
  admitted it (for az-1: slug candidates and accepted before and after).
- **Guard:** `universe_securities.brand_refusal` as it stands. Run over the 234, it refuses none of Meta, Lilly or
  Amazon, and it also does not refuse "Bank" for Bank of America, so the guard does not replace the census: a
  first word still has to be kept out by not listing it.
- **Carrier:** the identity file's `aliases` field, which the collector already loads. az-1 then changes the slug
  matcher to accept any one alias's full token set, as ADDENDUM 3 item 2 already states.
- **First entries:** Meta and Lilly (the two the replay names). Amazon needs no entry.
- **Worklist for later entries:** the 130 two-or-more-word names, admitted one at a time on a census, never in bulk.

## Calls that are not this seat's

1. Whether a text-matcher brand (the 7 existing entries, admitted on article-text hits) is automatically a slug
   brand, or each plane needs its own census. The two planes fail differently: text is word-bounded prose, a slug is
   a short hyphenated title.
2. Whether the two suffix lists (`CORPORATE_SUFFIXES` in `universe_securities.py:71-75` and `_LEGAL_SUFFIX` in
   `publishers.py:255-256`) become one.
3. The truncated-name class above: it is a name-quality defect on the identity file, owner unassigned.

## Bounds on what this says

- Coverage figures are counts of non-empty fields; I did not grade whether each present value is correct.
- The token table comes from my own loop over `slug_query` and `_entry_aliases`, with the ticker argument formed
  from the security key. It was not run through the replay, so it sizes the population and predicts no candidate
  counts.
- "No source yields a brand word" is bounded by what I searched: the crosswalk's fields, the pool universe, the
  collector's identity file, and a `comp-find` for `short_name|display_name|brand_name|alias|ir_domain|SHORT_NAME|
  LONG_COMP_NAME|SECURITY_NAME` over `lib/research`, `lib/opal_data_harvest` and `org/missions/D5/AMGT` (883 hits
  across 6,978 files; I read the DEF and CONFIG bands' data files named above, not every hit). The portal's display
  names and the RESAPP company records were not opened separately; `scoped_amgt.py` appears in that census and I did
  not read its name field.
- A Bloomberg short-name field was not pulled. That would be a vendor call and needs Andrew's per-use word.
