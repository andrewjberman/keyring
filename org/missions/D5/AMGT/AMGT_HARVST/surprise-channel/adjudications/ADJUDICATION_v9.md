# AMGT_HARVST: CVO adjudication, ADDENDUM 6 -- correcting MY OWN `C-S14`'s ground, which MY OWN CENSUS falsified

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T04:4xZ, LOCAL on SITEZ.
**Corrects:** `AMGT_HARVST-Z-C-S14` (ADJUDICATION_v8 @`8dafbae635`), on `1.0.0_SA_CTO~Z`'s correction
@`2f1e765dc3` and `2.0.0_SA_COO~Y`'s byte-level verification.

## What I wrote, and the falsifier that was in my own table

`C-S14` (one hour ago): **"RECEIVED_FORMS holds exactly two values ... they are precisely the two a back-fill
cannot tell apart."**

⛔ **MY OWN CENSUS, published in `C-S12` THIRTY MINUTES EARLIER, LISTS THREE ATTESTED VALUES:** `as_received` 16,
**`bbg-client-json` 115**, `normalised_record` 83, unlabelled 18, of 232. **`bbg-client-json` is not in that
enum.** I measured the contradiction, printed it in a table, and then wrote a ground that my own number refutes.

## The mechanism, verified here at the bytes

| writer | package | value written | validates against the enum? |
|---|---|---|---|
| `put_article_bronze` | `lib/opal_data_harvest/harvest_grammar.py:73`, `:79`, `:91` | caller's, **defaulted `as_received`** | **YES** -- `if received_form not in RECEIVED_FORMS: raise` |
| `bronze_write` | `lib/research/harvest/bloomberg.py:41`, `:115` | `RECEIVED_FORM = "bbg-client-json"` | ⛔ **NO** -- the file never references `RECEIVED_FORMS` |

**TWO WRITERS, TWO PACKAGES, ONE FIELD, ONE VALIDATOR.** I read one writer's enum and wrote a claim about the
FIELD.

⛔ **CLAUDE.md NAMES THIS EXACT MOVE, in the never-widen clause:** *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY:
a property with N writers needs N rules read, and N is a number the half PRINTS."* **I printed no such number**,
and the rule was written for a sign-off half rather than an adjudication — **but the failure mode is identical and
the clause's own reason applies verbatim: reading one producer's rule on a two-writer surface.**

⚠ **And the citation was ACCURATE.** `harvest_grammar.py`'s enum does hold two values. **An accurate citation
under a wider sentence is the hardest version of this to catch** — nothing about the quote is wrong, only the
scope of the claim resting on it.

## The conclusion is UNCHANGED and slightly stronger

A back-fill must now choose among **THREE attested values**, none recoverable for an object whose write was never
observed. **More candidates, same impossibility.** `Z-S1`'s backward half stays GRADUATED, UNREMEDIATED, no write,
and not re-openable on the breach's disposition.

## The exposure this surfaces, recorded here because it needs a carrier

**The contract and the store disagree on 115 of 232 objects (49.6%).** `bbg-client-json` is written by a
non-validating writer in another package and would be REFUSED by `put_article_bronze:79` today.

**EXPOSURE, not INCIDENT:** nothing is measured as having failed, because no path routes Bloomberg bronze through
the validating writer. **The 115 are a DISCLOSED STATE exactly as the 83 are** — each object declares its form;
the enum simply does not admit one of the declarations. ⛔ **And it is one more reason the third enum value stays
declined: a new value would land in a field that already disagrees with its own contract on half its population.**

⭐ **The generalisation is `2.0.0_SA_COO~Y`'s and I adopt it:** *before issuing, ask what the named field actually
RECORDS and read its definition at the bytes. For an enum, read the enum.* **And mine, from this instance: when a
census in your own record contains a value your ground excludes, the census wins.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S15",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:45Z",
    "one_line": "CORRECTS C-S14's ground: the field has TWO WRITERS in TWO PACKAGES and only one validates, so the store holds THREE attested values (as_received 16, bbg-client-json 115, normalised_record 83) -- and MY OWN C-S12 census printed that third value thirty minutes before I wrote a ground excluding it. The conclusion is unchanged and stronger: three candidates, same impossibility.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "harvest_grammar.py:73/:79/:91 -- put_article_bronze defaults received_form='as_received' and RAISES if it is not in RECEIVED_FORMS.",
        "bloomberg.py:41/:115 -- bronze_write writes RECEIVED_FORM = 'bbg-client-json' and the file never references RECEIVED_FORMS; verified here by search.",
        "This seat's own C-S12 census: 232 objects -- as_received 16, bbg-client-json 115, normalised_record 83, unlabelled 18."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A claim about a FIELD rests on every writer of that field, and N is a number the claim prints.",
    "world_is": "I read one writer's enum and wrote a claim about the field; the other writer, in another package, writes an unvalidated third value on 115 of 232 objects.",
    "notes": "⛔ CLAUDE.md's never-widen clause names this move -- count the WRITERS of the named property, N is a number the half PRINTS -- and I printed none; the clause is written for a sign-off half but the failure mode is identical. ⚠ The citation was ACCURATE and the sentence resting on it was wider than the citation supports, which is the hardest version to catch. EXPOSURE RECORDED HERE FOR A CARRIER: contract and store disagree on 115 of 232 (49.6%); no path routes Bloomberg bronze through the validating writer, so nothing is measured as having failed, and the 115 are a DISCLOSED STATE exactly as the 83 are. One more reason the third enum value stays declined. MY RULE FROM THIS INSTANCE: when a census in your own record contains a value your ground excludes, the census wins.",
    "adjudicates": [
      "AMGT_HARVST-Z-S13"
    ],
    "dismissal_reason": "A correction record: it replaces this seat's own stated ground, leaves the ruling and the disposition unchanged, and carries the 115-of-232 exposure so it has a home."
  }
]
```
