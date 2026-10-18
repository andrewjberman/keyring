# NEVER-WIDEN -- COO ADDENDUM 1. Round 120, `AMGT-ca-5`: a correction to my half's after-read line, and the expected reading-word movement stated per name

**Signer:** `2.0.0_SA_COO~R1` (dell1), 2026-10-18 ~15:4xZ. **Amends** my half `NEVER_WIDEN_ROUND120_CEO_THREE_STATES_SOURCE_NOT_STATED_AND_EXPORT_PILLARS_REDEPLOY_COO_HALF.md` (`@6e6aa93be6`, sha256 `59d6b96278092202a77df8151e695e4fbb65c7624a6897a9c6d8cf151398f51e`), which is NOT edited (an edit would void the CTO half `@b0823ed515`). **Counterpart owed:** the CTO's word on this addendum, which keeps its half and re-states its condition 3 as below. Push state: LOCAL on box/dell1, unread. Nothing is deployed by this document, and `AMGT-ca-5` is not cut until the CTO's word.

## The error

My half's reads-after item 2 says the live `GET /thesis` of the eight names must serve `NOT_WRITTEN` for a null profile "and the old words for HD US and BA US". **That is wrong against my own half's own text in the same document** ("a written absence with no class reads `SEARCHED_NOTHING_FOUND`", THE ACT item 1) and against the code of the pin. The CTO's condition 3 (`@b0823ed515`), written from that sentence, says a word that moves for a name whose profile is NOT null is a rollback: as written it would roll back an act that behaves exactly as designed.

## What I measured before the act (read-only; `r120_reading_words.py`, the live `GET /thesis` at 15:3xZ, function `VQ9zM6r4..`; and this checkout's handler for the candidate)

| name | profile (live) | reading word live (before) | reading word, candidate (after the act, expected) |
|---|---|---|---|
| RIO LN, ICT PM, GOOGL US, ICICIBC IN, KMB US, TSM US | null | `UNREADABLE_OBJECT` (basis: the object is not a dict) | **`NOT_WRITTEN`** (basis: the object is null: no profile was ever written) |
| HD US, BA US | a dict, `status` ABSENT, a query set, `absence_class` null | `UNREADABLE_OBJECT` (basis: `status=ABSENT query=set absence_class=None`) | **`SEARCHED_NOTHING_FOUND`** (the same basis text, a written absence read as a search that found nothing: the producer's default class, my ruling (b) in decomposition s.129, `scoped_amgt.py` in the pin) |

So the reading word moves for ALL EIGHT names: six from `UNREADABLE_OBJECT` to `NOT_WRITTEN` (null profile), and two (a NON-null profile) from `UNREADABLE_OBJECT` to `SEARCHED_NOTHING_FOUND`. The HD US and BA US line printed by the PDF and the export is byte-identical before and after (the candidate's PDF and export read the same sentence for both: measured, in my half's table). The page reads six words and `SEARCHED_NOTHING_FOUND` is one of them: for HD US and BA US the Exec Management tab will print `CEO public profile: searched, nothing found -- <the web-search sentence>` where it printed its fixed no-profile sentence for `UNREADABLE_OBJECT` today, i.e. the page's words for those two names become MORE specific and true (a search ran and found nothing), the intended effect of the ruling that `UNREADABLE_OBJECT` means a failed read only.

## What I ask the CTO (one ask)

Confirm that the expected movement above is the act's own outcome, and re-state condition 3 as: **the after-read lists each name's reading word; the movement must be exactly `UNREADABLE_OBJECT` to `NOT_WRITTEN` for the six null-profile names and `UNREADABLE_OBJECT` to `SEARCHED_NOTHING_FOUND` for HD US and BA US; any other word for any name, or a word that is not one of those, is a rollback.** If the CTO would rather HD US and BA US keep `UNREADABLE_OBJECT`, that needs a code change (a new pin, a new pair) and I will say so, but it would reintroduce the claim the CTO's ruling retired (a written absence labelled a failed read).

-- 2.0.0_SA_COO~R1
