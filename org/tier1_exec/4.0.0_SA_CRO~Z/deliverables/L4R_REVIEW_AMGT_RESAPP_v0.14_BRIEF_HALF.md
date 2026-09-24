# L4-R REVIEW -- AMGT_RESAPP PRD v0.14, BRIEF HALF -- verdict: REFUSE (one correction, by line)

**Reviewer:** `4.0.0_SA_CRO~Z`. **PRD:** `org/missions/D5/AMGT/AMGT_RESAPP/prd/AMGT_RESAPP_PRD.md` @`c09b35ee5a`,
`prd_version` v0.14, brief half hash `57b77104c1c0` (as delivered in msg 23990). **Brief:**
`docs/briefs/amgt-resapp-security-analysis-20260910.md` @`19ce7d5b4d`, unchanged since v0.13.
**Previous signature:** this seat SIGNED the brief half at v0.13 (`half_hash c0d38674e972`, pin `1699960261`).

## Independence limit, stated first

This seat authored the plan section 11 adopts (`PLAN_AMGT_HARVEST_CHANNEL_FORMATS_20260921.md` @`bc8c18a28f`).
Per `1.0.0_SA_CTO~Z`'s msg 23991, this review grades whether **section 11 states the plan faithfully and whether its six
contracts hold**, not whether the plan is right. **The defect below is in this seat's own plan first**: the PRD copied
it faithfully.

## Scope: what changed since the signed v0.13

`git diff 1699960261 c09b35ee5a -- <PRD>` is **one commit, +37 / -1**: the `prd_version` header, the v0.14 change note
(PRD `:204-210`), and section 11 (`:1695-1721`). **No BRIEF COVERAGE entry changed, and neither did the brief pin**, so the
heading denominator and the coverage carried at v0.13 stand as signed (review `L4R_REVIEW_AMGT_RESAPP_v0.11_BRIEF_HALF.md`
@`8a788d2eaf`). This review therefore grades the two new hunks only.

## The six contracts against the plan

| contract | faithful to the plan? | holds? |
|---|---|---|
| `C-HARVEST-HOME` | yes | yes. Until the tenancy act lands, `address()` prints `opal-data-assets` for bronze and silver, so "every address is `address()` output" and "every tier lives in `opal-data-harvest`" cannot both be met. `C-FORMAT-SEQUENCE` puts the tenancy act in the gate, which resolves this. |
| `C-BRONZE-AS-RECEIVED` | **NO** (see the correction) | **NO** |
| `C-SILVER-PARQUET` | yes | yes, with one flagged exception already named in "Not decided here": the plan's Lusha silver drops contact fields, which "every vendor field kept" would forbid. Recommend the Lusha clause name silver too (below). Not refuse-worthy on its own. |
| `C-DEDUPE-BY-KEY` | yes | yes. Note: retiring `opal-harvest-articles` is a DynamoDB table deletion and needs a human's confirmation when it is executed. The contract records intent, not authority to delete. |
| `C-SLASH-SAFE-KEY` | yes | yes. "Entity id" reads as the SECURITY key. The document ids the plan puts in `object` (an accession, a 16-hex IR id) are slash-free by construction. |
| `C-FORMAT-SEQUENCE` | yes, one ambiguity | yes. "Existing objects move by copy ... never by re-fetch" is correct for the 1,461 live objects. The bronze that was NEVER kept (13 EDGAR documents, 1 IR document, 7 publisher responses) is filled by the backfill's first fetch (plan s.7, corrected). Recommend one clause so a worker does not read the sentence as forbidding that. |

## THE CORRECTION (the refusal rests on this alone)

**PRD `:1705-1706`, `C-BRONZE-AS-RECEIVED`,** gives ONE bronze template:
`{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`. Section 11 also says (`:1698-1699`)
*"Where the plan and this section disagree, this section binds."* **Seven of the plan's s.5 bronze addresses do not
follow that template**, all of them builder-resolved and CONFORMANT:

| channel | plan s.5 address shape | why it differs |
|---|---|---|
| SEC filing | `sec/harvest/bronze/filing/cik={cik}/{accession}/{primary_document}` | an immutable document; the accession is the fetch key |
| SEC ticker table | `sec/harvest/bronze/company_tickers/date=.../sec_ticker_cik_cache.json` | a request, not an entity; **already in code** (`lib/research/identity/build_universe.py:456-462`) |
| issuer document | `issuer-site/harvest/bronze/document/security_key={k}/{id16}/{file}` | an immutable document |
| ESEF filing | `filings-xbrl/harvest/bronze/filing/lei={lei}/{package_sha256}.zip` | an immutable document |
| social snapshot | `bright-data/harvest/bronze/social_snapshot/date=.../{request_sha256}.json` | a request |
| SERP | `bright-data/harvest/bronze/serp/date=.../{query_sha256}.json` | a request |
| Lusha | `lusha/harvest/bronze/company_contacts/date=.../{request_sha256}.json` | a request |

So as written, the binding clause turns seven correct addresses non-conforming, **including one the codebase already
reads**. The source is this seat's plan: its s.1 item 2 gave the single template while s.5 used three forms. It is
corrected in the plan at the pin this review cites.

**Replacement text for `:1705-1706`** (offered; the wording is the CTO's):

> **`C-BRONZE-AS-RECEIVED`** -- bronze is the response bytes exactly as received, one object per fetch, never
> overwritten, with the channel's FETCH key in the partition, in one of three forms (plan s.1 item 2): (a) an entity
> fetched repeatedly: `{vendor}/harvest/bronze/{request}/{entity}={id}/{YYYYMMDDTHHMMSSZ}.{ext}`; (b) an immutable
> document: `{vendor}/harvest/bronze/{request}/{entity}={id}/{document id}/{vendor file name}`; (c) a request:
> `{vendor}/harvest/bronze/{request}/date=YYYY-MM-DD/{request hash or file}.{ext}`.

## Two recommended clarifications (not grounds for refusal)

1. **`C-FORMAT-SEQUENCE`:** add *"Bronze that was never kept is filled by the backfill's first fetch under its fetch
   key; that is a first fetch, not a re-fetch."*
2. **"Not decided here":** *"Whether Lusha keeps bronze, and whether its silver drops contact fields (an exception to
   `C-SILVER-PARQUET`), is Andrew's call."*

## What re-opens on the fix

Only the brief half: section 11 sits in it and the ENDPOINT/CONTRACTS sections do not move. The plan pin to cite after
the fix is the commit that carries this review.
