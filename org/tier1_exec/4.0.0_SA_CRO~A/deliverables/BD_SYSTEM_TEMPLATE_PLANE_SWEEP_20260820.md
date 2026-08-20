# BD system-template plane -- ENDPOINT SWEEP: NEGATIVE (plane NOT located)

**Seat:** `4.0.0_SA_CRO~A` | **2026-08-20 ~0130Z** | **Authority:** scanning grant; CTO GO 005752Z.
Pure read: no run, no export, no client data. One-shot grant remains **OPEN / UNCONSUMED**.

## Result: NEGATIVE. The plane serving system templates was NOT found.

12 candidate paths probed across 2 families. Reported as a negative rather than continued
guessing, because the next guess has no better prior than the last twelve.

## Finding 1 -- MECHANISM IDENTIFIED (real progress, zero egress): they are EXPORTS, not QUERIES

Every `systemTemplates[]` entry carries a UNIQUE `exportType` that `userTemplates[]` entries do not
have at all, and `queryType: "NotAQueryType"` states it outright:

| id | name | exportType |
|---|---|---|
| 5 | Firm Householding | `FirmHouseholding` |
| 50 | Client Account Assignment | `ClientAccountAssignment` |
| 51 | Firm User Account Assignment | `FirmUserAccountAssignment` |
| 7010 | Account Registration Codes | `BulkAccountRegistration` |

29 system templates, 29 distinct exportTypes, 1:1. **So these are keyed by exportType on an EXPORT
plane, not by templateId on the datamining query plane.** That explains the earlier 404s
mechanically rather than by inference: they were never addressable there.

## Finding 2 -- ⛔ `/Api/DataMining` IS NOT A PROBEABLE ORACLE. A 200 THERE IS NOT EVIDENCE.

**Negative control `/Api/DataMining/zzz_negctl_9999` returns `200`.** So does every real-looking
path. Two response shapes, neither of them data: a **5,534-byte HTML app-shell** (`<!DOCTYPE html>`)
or a **0-byte 200**.

> On the first pass I probed this family on STATUS CODE alone and it produced four apparent hits,
> including `/Api/DataMining/ExportSystemTemplate/5 -> 200 (5,534 B)`. **That reads exactly like
> success.** Only the invented-path control exposed it. An instrument that answers 200 to a path
> that cannot exist has not answered the question -- it could not have said otherwise.

**Anyone probing this family by path WILL manufacture false positives.** Verdict must be
content-based (JSON content-type + non-trivial bytes), never status-based.

## Finding 3 -- the `/datamining/request/v1` family IS discriminating, and it is uniformly 404

Controls both directions: negative `/zzz_negctl_9999` -> **404**; positive `/template` (roster)
-> **200 JSON, 15,378 B**. Against a working oracle, all six candidates 404:
`/systemtemplate/5` · `/systemtemplate` · `/export/FirmHouseholding` · `/export` ·
`/template/5/export` · `/template/5`. **The plane is not on this family under any name I guessed.**

## What this changes about the eventual Andrew ask

CTO's rider stands: *"a different endpoint = a different egress ask"* -- and **an ask still cannot be
made decidable, because no endpoint has been located to name.** Path-guessing is exhausted as a
method; twelve guesses against a discriminating oracle is enough to stop.

**RECOMMENDED NEXT METHOD -- not more guessing, and the cheapest one is not technical:** Andrew has
a live 49F data contact and a transcript already in scope (`Data Discussion.docx`, his own
sequencing instruction). **Asking which endpoint serves Firm Householding costs zero egress, zero
guesses, and converts the ask from undecidable to one-word.** The technical alternative -- observing
the BD web app's own network calls during a Firm Householding export -- is a different KIND of act
(browser observation, not REST probing) and should be scoped as such rather than improvised.
