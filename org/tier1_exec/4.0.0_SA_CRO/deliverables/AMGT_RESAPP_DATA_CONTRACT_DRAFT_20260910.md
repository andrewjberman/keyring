# AMGT_RESAPP -- DATA CONTRACT (DRAFT) -- the Research Pack object

**Author:** `4.0.0_SA_CRO~Z` | **Date:** 2026-09-10 | **Status: DRAFT, NOT RATIFIED.**
Option 4 of the `/next-steps` set, unblocked by Andrew's Call 2 ruling.

> **LANE NOTE, deliberate:** the SSCN precedent puts a ratified contract at
> `docs/architecture/SSCN_DATA_CONTRACT.md`. This draft is held in the CRO deliverables tree
> **because AMGT_RESAPP is not yet minted and no L4 PRD exists** -- the L4 PRD is `1.0.0_SA_CTO`'s
> and this seat will not plant an unratified file in the architecture tree as though it were one.
> On ratification it becomes `docs/architecture/AMGT_RESAPP_DATA_CONTRACT.md`.

**What this is:** the single object the Security Analysis page renders AND the PDF renderer prints.
It is the contract both consume, so that -- per the standing invariant -- **the print artifact is
generated from the object, never screenshotted from the page.**

---

## 1. THE ONE INVARIANT THAT SHAPES EVERYTHING ELSE

**A pack is an IMMUTABLE, VERSIONED SNAPSHOT. "Refresh" mints a new one. Nothing is ever
overwritten.**

This is not a style preference, it is forced by measurement: Bloomberg derived fields are
**current-day-only with no backfill** (`integrations/bloomberg/READ_HERE.md` s4), so a value not
captured on the day it was served is gone permanently. Andrew's ruling makes it doubly binding --
*"make sure that its stored somewhere so we dont need to do it twice."*

**=> Every write to `opal-data-research` is an append. There is no update path in this contract.**

```
s3://opal-data-research/packs/{ticker}/{snapshot_utc}/pack.json     <- the object below
s3://opal-data-research/packs/{ticker}/{snapshot_utc}/raw/          <- verbatim vendor responses
s3://opal-data-research/packs/{ticker}/latest.json                  <- pointer ONLY (a snapshot id)
```

`raw/` exists so a normalization decision can be re-derived later without re-spending quota. It is
the cache half of Andrew's instruction and it is what makes the quota arithmetic a one-time cost.
**`latest.json` holds a pointer, never a copy** -- a copy is a second source of truth for one fact.

## 2. EVERY VALUE CARRIES ITS CLAIM

Per `docs/doctrine/A_VALUE_MUST_CARRY_ITS_CLAIM.md`: a bare number is not admissible. The atom of
this contract is not a scalar, it is:

```json
{
  "value": 11729,
  "claim": "measured",
  "unit": "EUR_MM",
  "sign_convention": "as_reported",
  "source": "bloomberg",
  "mnemonic": "EBITDA_ADJUSTED",
  "basis": "bloomberg_adjusted",
  "as_of": "2025-12-31",
  "captured_utc": "2026-09-10T14:52:03Z"
}
```

- **`claim`** is one of `measured | inferred | held | absent` -- the consuming half is the whole
  mechanism, so the renderer MUST visibly distinguish `measured` from `inferred` and MUST NOT render
  `absent` as zero or blank.
- **`unit` and `sign_convention` are MANDATORY and non-defaultable.** The field map measured that
  Bloomberg's units are inconsistent across its own field families -- `CUR_MKT_CAP` absolute while
  `NET_DEBT` and `CURR_ENTP_VAL` are millions, `EQY_SH_OUT_REAL` absolute while
  `IS_SH_FOR_DILUTED_EPS` is millions, every margin a percent, `CAPITAL_EXPEND` sign-inverted.
  **A mnemonic-only map silently produces a model off by 100x in some cells and 1e6 in others.**
- **`basis`** is what makes the normalization finding survivable: `bloomberg_adjusted` and
  `factset_recurring` are different answers to different questions and the page must say which it is
  showing.

## 3. THE PACK OBJECT

```
pack
  schema_version        str
  snapshot_id           str    {ticker}/{snapshot_utc}, immutable
  security              { ticker_bbg, ticker_display, name, exchange, country, currency,
                          sector: {value, taxonomy: "GICS"|"FACTSET"} }
  provenance            { captured_utc, requested_by, bloomberg_session_ok: bool,
                          vendor_calls: [{vendor, endpoint, fields_n, data_points_n, bytes}],
                          coverage: "covered_89" | "ad_hoc" }
  header                { <~16 valued atoms, s2 shape> }
  model
    fiscal_years        [int]                  <- the JOIN KEY. never a date string.
    lines               { <line_id>: [valued atom per fiscal year] }
    scenarios           { upside|base|downside: { years, eps, multiple, price, return,
                                                  ebitda, ev, mkt_cap } }
  peers                 { basis: "derived"|"analyst", members: [{ticker, name, <atoms>}] }
  narrative                                    <- Adam's five limbs; see s4
    company_description { text, segments: [...], claim }
    investment_thesis   [{ heading, text, claim }]
    risks               [{ heading, text, claim }]
    management_bio      { subject, role, text, claim }
    other_positives     [...]
    other_negatives     [...]
    analyst_sections    [{ heading, text }]    <- the open-ended limb; see s4 note
  evidence
    news                [{ headline, url, published_utc, source, corpus: "sa"|"rss",
                           ticker_tagged: bool, mention_count, recency_rank, frequency_rank }]
    ir_pages            [{ url, resolved_from, last_seen_utc }]
  ai_analysis           { generated_utc, model, inputs_digest,
                          limbs_drafted: [...], evidence_summary: {...},
                          framework_score: null }
  render_hints          { print_page_breaks: [...], chart_specs: [...] }
```

**`fiscal_years` is the join key and the date string is never used as one.** Measured: price and
fundamentals land on different dates in the same Bloomberg response -- **4 of 10 years split for
SAP, 14 rows for 10 fiscal years.** A consumer keying on `date` silently drops 40% of that name's
price history. This contract makes that error inexpressible.

## 4. `narrative` AND `ai_analysis` -- per Andrew's Call 2 ruling

*"A first, B sure maybe just based on recency and frequency of mentions. C can come later after
we've discussed."*

- **(a) IS THE PRIMARY DELIVERABLE.** `ai_analysis.limbs_drafted` writes INTO the `narrative`
  fields. Each carries `claim: "inferred"` -- generated prose is never `measured` -- so the page can
  mark machine-drafted text as such.
- **(b) IS IN, AND ITS RANKING FUNCTION IS SPECIFIED BY ANDREW: recency and frequency of mentions.**
  Hence `recency_rank` and `frequency_rank` as first-class fields on every evidence row. Buildable
  exactly as he stated it; **it is not to be embellished with relevance scoring or sentiment
  weighting**, which would be inventing a ranking he did not ask for.
- **(c) IS PARKED.** `framework_score` is present and **pinned `null`**. The field exists so adding
  (c) later is not a schema migration; the pin exists so **no seat can self-start (c)**, which his
  ruling reserves to a discussion that has not happened.

> **The `analyst_sections` note, carried honestly:** the filled packs' value lives in sections the
> template does not have (SAP's *IMPACT OF ARTIFICIAL INTELLIGENCE*; COPA's *MOAT*, *FLEET PLAN*,
> *2026 DYNAMICS*). An open-ended array admits them. **It does not solve them** -- an automation that
> fills only the fixed limbs reproduces the skeleton and none of the judgment. This is the honest
> boundary of v1 and it should be stated to Adam whenever contact reopens.

## 5. RULE 24 -- the four-postulate record

**(i) MECE over a declared domain.** Domain: *everything the Security Analysis page or the PDF
renderer displays for one security at one instant.* The uncovered-member hunt found three, all now
placed: **charts** (`render_hints.chart_specs` -- the packs carry 9-11 embedded images each and a
schema without them would have forced screenshots, defeating the print invariant); **the
Bloomberg session state** at capture (`provenance.bloomberg_session_ok`); **quota accounting**
(`provenance.vendor_calls`, which makes payload measurable per pack rather than estimated).

**(ii) Same grain.** Every leaf under `header`, `model.lines` and `peers` is the s2 valued atom --
never a bare scalar beside a valued one. `narrative` is at a different grain by intent (prose, not
measurement) and is therefore a **separate branch**, not a sibling of `model.lines`.

**(iii) Intent coherence.** One axis: *what is true about this security at this snapshot.* Anything
about the RUN rather than the SECURITY lives in `provenance`. `latest.json` holds a pointer for the
same reason -- mixing "which snapshot is current" into "what the snapshot says" would be two intents
in one object.

**(iv) State coherence -- which values one remedy does NOT move.** Re-running the pull moves
`header`, `model`, `peers`, `provenance`. It does **NOT** move `narrative` or `ai_analysis` unless
the AI leg is re-run, and it does **NOT** move `evidence` unless the news leg is re-run.
**These are three independently refreshable subtrees and the UI must not present one "Refresh"
button as though it moved all three.** A user who refreshes prices and reads day-old generated prose
beside them, with one timestamp on the page, has been misled by the schema.

## 6. OPEN AGAINST THIS DRAFT

1. **`basis` default for EBITDA/EPS** -- blocked on the normalization call (field map s5). The
   contract carries `basis` so either answer fits; the DEFAULT is undecided.
2. **`peers.basis`** -- `derived` (sector/size/geography) or `analyst` (judgment). Under Call 5,
   Adam cannot be asked; it must be inferred from the 89-name corpus or ruled by Andrew.
3. **`evidence` v1 source set** -- pending the SA corpus staleness measurement (probe record s"NOT
   MEASURED").
4. **`render_hints.chart_specs`** -- shape not drafted. Needs the design spec, which Andrew reserved
   for discussion.
5. **No DESIGN spec is drafted here, deliberately** -- header contents and tab shape are the thing
   he said *"let's discuss what that would look like."* This contract stops at the data boundary.
