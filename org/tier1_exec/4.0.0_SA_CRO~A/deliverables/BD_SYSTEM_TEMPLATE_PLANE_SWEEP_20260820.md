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

---

# ROUND 2 (under Andrew's ~0135Z egress line; CTO bound 013236Z)

## THE PRE-REGISTERED REFUSAL IS FINALLY OBTAINED -- BD WAS ASKED AND SAID NO

Round 1 established the four ids 404 on `GET /template/{id}` -- an ADDRESSING result. But the design's
branch fires when **the RUN FLOW is asked and refuses**, and nobody had ever asked it. Now asked:

| call | result |
|---|---|
| `POST /v1/run {"templateId": 5}` | **404 `"Template Not Found, StatusCode=NotFound, SourceId=5"`** |
| `POST /v1/run {"exportType": "FirmHouseholding"}` | **400 `"Request does not have a valid TemplateId or Template provided."`** |
| `POST /v1/zzz_negctl_9999` (NEG-CTL) | 404 |
| `GET /v1/template` (POS-CTL) | 200 JSON 15,378 B |

**The run endpoint EXISTS, PARSES the body, and answers specifically**: it accepts only `TemplateId`
or `Template` (the 400 states it), and asked for id 5 it says **Template Not Found by name**. That is
the pre-registered refusal, in BD's own words -- not a prior, not an addressing inference.
`?exportType=` as a query param is IGNORED (returns the unfiltered roster).

**So: system templates are not on the datamining plane by ANY verb, and `exportType` is not a key
this plane accepts.** The thread's mechanism question is closed on measurement.

## ⛔ SECOND FALSE-POSITIVE TRAP, AND IT WOULD HAVE BEEN A HEADLINE: `*.bdreporting.com` IS A WILDCARD CATCH-ALL

Andrew's brief names a **"Business Intelligence" endpoint**, so `bi.bdreporting.com` returning
**200** looked like the find of the night.

| host | status | bytes |
|---|---|---|
| `bi.bdreporting.com` | 200 | 242,826 |
| `reporting.bdreporting.com` | 200 | 242,826 |
| `app.bdreporting.com` | 200 | 242,826 |
| **`zzz-negctl-9999.bdreporting.com`** (INVENTED) | **200** | **242,826** |
| `billing.bdreporting.com` | 200 | 118,402 |
| `api.bdreporting.com` | **429** | 63 (JSON) |
| `clientview.bdreporting.com` | — | connection timeout |

**A subdomain I invented returns the same byte count as `bi.`** -- so `bi`/`reporting`/`app` are a
wildcard catch-all page, NOT distinct applications. **Subdomain existence is not a probeable oracle
on this domain; only a response that DIFFERS from the catch-all is evidence.**

*Second time in one session that an invented-input control killed an apparent hit -- and this one
would have been reported as confirming the sovereign's own words about a BI endpoint. **The more a
false positive agrees with what you were told to expect, the more it needs the control.***

## REAL RESIDUE: `api.bdreporting.com` is a genuinely distinct service

429 + `application/json` against a catch-all that returns 200 + HTML = a real, separate service.
**DELIBERATELY NOT RETRIED. A 429 is a back-off instruction, and hammering a vendor endpoint to
satisfy a probe is not a read I am willing to take** -- it risks the account for a lead that keeps.
`clientview` does not resolve, so the ClientView half of Andrew's brief is not on this domain.

**NEXT (unfired, needs no new word but does need a cool-off):** one spaced probe of
`api.bdreporting.com` for an exportType-keyed route. If that is also negative, the human channel
(CALL 2, approved) is the route, and browser observation remains its own scoped ask.
