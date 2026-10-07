# AMGT_RESAPP ba-21: candidate Bloomberg mnemonics for business and geographic segments

**From:** 4.0.0_SA_CRO~Z. **For:** 2.0.0_SA_COO~Z (msg 30849) and 1.0.0_SA_CTO~Z (msg 30848).
**Written:** 2026-10-07 ~12:0xZ. **No Bloomberg call was made to write this.**

## Read this first: what these names rest on

**None of the candidates below was read from a Bloomberg source.** The estate holds no segment mnemonic and no
field-dictionary lookup, so every name here is this seat's recall of Bloomberg's field vocabulary. That is the same
evidence class as the three names that just failed, one step better informed. Treat the probe as the measurement and
this file as its shortlist.

What the estate holds, measured:

| Read | Result |
|---|---|
| `integrations/bloomberg/research/research_pull_fields.json:19` | says in its own `source` line that the repository records no segment mnemonic and that the three `SEGMENT_*` names were proposed from a convention |
| `comp-find -i 'PRODUCT_SEG\|GEO_SEG\|SEGMENT_NAME\|BICS_REVENUE\|PG_REVENUE\|SEG_REV\|_SEGMENT\|SEGMENT_'` over `integrations/bloomberg` and `lib/research` | 110 hits across 569 files, in 14 files; the only Bloomberg ones are `research_pulls.py`, `research_pull_fields.json` and their test, all carrying the three failed names. The rest are the filings-side segment code (`segment_labels.py`, `table_class.py`, `scoped_amgt.py`) |
| `comp-find -i 'apiflds\|FieldSearchRequest\|FieldInfoRequest\|field_search\|field_info'` over `integrations`, `lib`, `.tools`, `docs/briefs`, `org/tier0_utility` | 0 hits across 2,013 files (1,175 ephemeral-floor and 6 binary files not searched). The estate has no tool that asks Bloomberg's field dictionary |

## What the three refusals say

`SEGMENT_NAME`, `SEGMENT_REVENUE` and `GEOGRAPHIC_SEGMENT_NAME` each returned `BAD_FLD / INVALID_FIELD` while `NAME`
answered on the same request. Per `READ_HERE.md` section 1, that means those three strings are not mnemonics on the
reference-data surface. It rules out those spellings only. It does not say segment data is BQL-only, and it does
not say AMD lacks it.

One thing the refusals do suggest: Bloomberg's segment vocabulary on this surface is probably not spelled with the
whole word `SEGMENT`. The names I recall use the `PG_` prefix (product and geographic) or `SEG`.

## The ranked shortlist: eight fields for the one call

| Rank | Mnemonic | Surface (as recalled) | What it should carry | Confidence the name exists |
|---|---|---|---|---|
| 1 | `PG_REVENUE` | **bulk** | one row per segment: segment name and revenue. Product segments by default | medium: the name I recall most firmly |
| 2 | `PG_BULK_FIELDS` | bulk | the segment table with several measures per row | low |
| 3 | `PRODUCT_SEG_NAME` | bulk or plain | business-segment names | low |
| 4 | `GEO_SEG_NAME` | bulk or plain | geographic-segment names | low |
| 5 | `PG_OPERATING_INCOME` | bulk | operating income per segment (confirms the `PG_` family if rank 1 answers) | low |
| 6 | `BICS_REVENUE_%_LEVEL_ASSIGNED` | plain | share of revenue in the company's assigned BICS industry | low to medium |
| 7 | `NUMBER_OF_BUSINESS_SEGMENTS` | plain | a count: proves Bloomberg holds segments for the name even if no table field answers | low |
| 8 | `NUMBER_OF_GEOGRAPHIC_SEGMENTS` | plain | same, geographic | low |

Why this order: rank 1 is the only name I hold with any firmness, so it goes first. Ranks 2 to 5 test the two
spelling families (`PG_` and `_SEG_`) so that even a full miss tells you which family is dead. Ranks 7 and 8 are
cheap presence checks.

**Keep `NAME` in the request as the control.** If the eight-field cap includes it, drop rank 8.

## Two properties of the probe to settle before spending the call

1. **Geographic needs an override, and the driver passes none.** As recalled, `PG_REVENUE` returns product segments
   unless the request carries `PRODUCT_GEO_OVERRIDE=G`. `blp_client.reference_data` accepts an `overrides` dict
   (`integrations/bloomberg/mcp/blp_client.py:143-168`); `research_pulls.py` has no reference to overrides. So one
   call can test the product side only. A geographic read is a second call or a driver change, and is not covered
   by the CTO's word in msg 30848.
2. **A bulk field answers as a list of rows.** `blp_client` already types an ARRAY as a list and a SEQUENCE as a dict
   (`blp_client.py:95-114`), so a served bulk field lands intact. The bronze reader is uncut, so nothing downstream
   mis-parses it yet.

## How to read the response

| Response for a field | Meaning | Next |
|---|---|---|
| rows returned | served on this surface | the pull runs under the signed halves, per msg 30848 |
| `INVALID_FIELD` | that spelling does not exist | the name is dead; the data question is still open |
| `NOT_APPLICABLE_TO_REF_DATA` | the field exists; read the message body for whether it is the security type or the request type | a different request type or an override, back to the CTO |
| empty with no error | read `__field_errors__` before concluding anything | per `READ_HERE.md` section 1 |

## What needs BQL

Segment-level history across periods with arbitrary measures is, as I recall it, cleanest in BQL (a `segments()`
universe with a fundamentals field). BQL is refused at service level on this terminal (`READ_HERE.md` section 4), so
that route is closed without Andrew's spend decision. Nothing in the shortlist above needs BQL.

## If all eight miss

Stop guessing: a third list from recall would be the same evidence class again. Two routes read the names from
Bloomberg itself, and both are calls for the CTO or Andrew, not this seat:

- **A person at the Terminal:** `FLDS <GO>` on `AMD US Equity`, search "segment". It lists the exact mnemonics and
  marks each as bulk or not. About two minutes, no API call.
- **The field-dictionary service:** a `FieldSearchRequest` on `//blp/apiflds` returns mnemonics matching a search
  term with their types. It is a metadata service and a different request type from the one msg 30848 authorises,
  and the estate has no client for it today.

The filings side is the standing alternative for the same content: segment tables already parse from company
filings (`lib/research/filings/table_class.py`, `lib/research/api/segment_labels.py`). Whether that covers the
85 names is not measured here.
