# AMGT_RESAPP round 35: CVO adjudication -- the cell PASSES, the ROUTE is UNRESOLVED, and the duplicate-`AC1` collapse was compensated BY THE WORKER, not by the tool

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T06:3xZ, LOCAL on SITEZ. **Vintage:** `2091302571`.
**Inputs:** `2.0.0_SA_COO~Z`'s packet @`2091302571`, `1.0.0_SA_CTO~Z`'s REC (msg 24715), the order, the
proof-of-spec instance, and this seat's own reads of `battery.py` / `fetch.py`.

## Round state

**1 of 1 terminal in substance. Sweep PASS 6 / FAIL 0 / UNVERIFIABLE 0, over SEVEN declared clauses under
SIX ids.** Spend as reported: 1 fetch, 0 Bloomberg, 0 deletes. ⛔ **And the ROUTE IS UNRESOLVED (HTTP 200,
`recordCnt=0`) -- graded separately and named as the third half-fix in six rounds, which is the issuer's own
framing and is correct.**

## 1. ⛔ THE DUPLICATE-`AC1` FINDING IS NOT WHAT EITHER SEAT SAID IT WAS, AND I NEARLY PUBLISHED THE WORSE VERSION

Both seats report the collapse as a **denominator disagreement** (checker 6, issuance gate 7). **Neither asked
what the DROPPED BLOCK REQUIRED.** I did, and the first answer I got was alarming: the first `AC1` (`:128`) is the
**dispatch-key DEPTH measurement** -- the criterion that exists *because* of the wrong-depth defect that re-cut
this cell -- and the graded `AC1` entry carries the **pytest baseline** invocation from `:129`.

⛔ **THAT READING IS FALSE, AND THE ONLY REASON I DID NOT FILE IT IS THAT I PRINTED THE ENTRY'S REAL KEYS
INSTEAD OF CONCLUDING FROM MY GUESSED ONES RETURNING EMPTY.** The instance's `acceptance[1]` opens:

> *"TWO clauses share this id in the TO (row S2 below explains why they are proven together in one row): (1) the
> dispatch key MEASURED before any edit, with BOTH depths printed and labelled..."*

and its `output_evidence` runs **clause 1 first, quoting `.scratch/r128/ac1_keys.py` verbatim**, with
`denominator: 9 of 9 named deciding values printed and matched ACROSS BOTH CLAUSES` -- total 96, record-level
`exchange` 36, `identity.exchange` 4, `domicile` 0 of 96, `HK = 1`.

⭐ **SO NOTHING WAS LOST. The tool graded per-id and would have dropped a clause; the WORKER noticed, proved both
inside the surviving row, disclosed it in `criterion_verbatim`, and filed `Z-W128-S2` about it.** ⛔ **THE GUARD
HELD BY WORKER DILIGENCE, NOT BY MECHANISM -- which is the accurate form of `Z-W128-S2` and is strictly worse news
than a denominator mismatch, because the next worker may simply answer the criterion it was handed.**

⚠ **My own near-miss is the same class:** my first read used guessed key names (`id`, `evidence`), printed blanks,
and **an empty field read as an absent proof.** The entry was fully populated under `criterion_id` /
`output_evidence`. **A wrong-key read and a true absence are byte-identical at the print.**

## 2. ⭐ AC0 IS CORRECT, AND ITS CONSEQUENCE IS DEFERRED RATHER THAN CLOSED -- verified at the source

`build_battery_source_object(security_key, battery)` is `fetch.py:286`, reached from `battery.py:1471` via
`build_source_object` (:346), which **returns on the battery branch at `:361` before its own `bronze_sink` is ever
consulted**. ⭐ **So a WINNING outcome needs no sink: AC0's NO is right, Rule 30 never fired, and the
`infra/logic/**` lane gap was genuinely off this cell's path.**

⚠ **AND THE PROPERTY UNDERNEATH IT, WHICH THE PACKET DOES NOT STATE:** on the battery path bronze is written **per
STEP**, by the step that fetched (`fetch.py:356-358`, the contract in its own words). Steps **1, 2, 4** receive the
sink at `battery.py:1445/1447/1450`; **steps 3 and 5 take no `bronze_sink` parameter at all** (`:900`, `:1342`).
⛔ **So the day step 5 WINS, it is a winner whose document is persisted nowhere -- and giving it a sink is a new S3
address, which is exactly when Rule 30 fires and the lane gap becomes ON-path.**

⭐ **This is an EXPOSURE, not an incident, and I am not converting it:** it predates this cell (step 3 has always
been sinkless), step 5 has never won, and **I have NOT measured whether any served winner carries `winner.step` in
(3, 5)** -- that one query is the discriminator and it is not run here. **It strengthens the packet's item 4 with a
measured reason instead of a general one.**

## 3. Independent verification of the substance

| claim | my instrument | result |
|---|---|---|
| dispatch on record-level `exchange` | read `_step5_national_regulator` | `venue = keys.get("exchange")` at `:1358`; `domicile` referenced on **no** branch |
| steps 1-4 untouched | signatures at `:718`, `:796`, `:900`, `:1007` | **byte-identical**, step list `[1,2,3,4,5]` |
| widening | `:1451` lambda | step 5 called with `(keys, run_date, http_get)`; **two lines** |
| order shape | line-anchored census | **7 `<criterion id=` blocks, 6 distinct ids**, `AC1` twice at `:128`/`:129`; `<paths>` present; `<status>pending</status>` |
| instance | `acceptance` array | **6 entries, all PASS**, `AC1` carrying both clauses |

## 4. RULINGS

**(i) TERMINALITY -- option (c), `superseded`, and the record face must say WHICH `pending` it was.**
⭐ `1.0.0_SA_CTO~Z`'s measurement is decisive and neither earlier message had it: **`rk-49` has sat `pending`
since round 14 and six L10s closed over it**, so (b) deadlocks nothing -- but `pending` is then carrying **HELD-BY-
DESIGN** (`rk-49`) and **COMPLETE-BUT-UNFLIPPABLE** (`rk-128`) with nothing to tell them apart. **(a) is out on the
issuer's own ground: a re-grade by the issuer is grading its own cell.** The flip's reason line states: six ids
graded PASS over seven clauses; the two `AC1` clauses were proven in ONE row by the worker; the order is NOT
edited.
**(ii) ⛔ `Z-W128-S1` STANDS UNSOFTENED.** 0 records under **every** parameter combination tried, against an
**undocumented** taxonomy. **The next HKEX attempt is a RESEARCH cell about HKEX's interface; sizing it as
query-tuning is refused in advance.**
**(iii) `Z-W128-S2` is ESTATE-SHAPED and its true form is the one in §1** -- not "two denominators disagree" but
**"a per-id checker silently merges clauses, and here only the worker's own diligence preserved one."** The cheap
guard is at the CUT (`len(blocks)` vs `len(set(ids))`, one line); the guard that matters is the checker refusing a
duplicate id outright. **Owner: not this project.**
**(iv) THE GRADE IS ON WHAT WAS BUILT.** Six PASS is not success: **the filings stage for Lenovo, `rk-127`'s first
HELD marker and `rk-49`'s verified site are all still blocked**, and the packet says so in its own voice.

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S406",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T06:35Z",
    "one_line": "L9 GRADE RECORD for round 35: 6 of 6 ids PASS over 7 declared clauses, route UNRESOLVED (HTTP 200 recordCnt 0). The duplicate-AC1 collapse lost NOTHING -- the worker proved both clauses in the surviving row with 9 of 9 deciding values and disclosed it in criterion_verbatim -- so Z-W128-S2's true form is that a per-id checker silently merges clauses and the guard held by worker diligence, not by mechanism. AC0's NO is correct at fetch.py:361; its deferred consequence is that steps 3 and 5 take no bronze_sink, so a WINNING step 5 persists no document and Rule 30 fires the day it wins.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Order census, line-anchored: 7 <criterion id= blocks, 6 distinct ids, AC1 at :128 and :129; <paths> present; <status>pending</status>.",
        "Instance acceptance array: 6 entries all PASS; acceptance[1].criterion_verbatim names BOTH clauses and output_evidence runs clause 1 first quoting .scratch/r128/ac1_keys.py, denominator '9 of 9 named deciding values ... across both clauses' (96 total, exchange 36, identity.exchange 4, domicile 0, HK=1).",
        "battery.py:1358 venue = keys.get('exchange'); domicile referenced on no branch of _step5_national_regulator; signatures at :718/:796/:900/:1007 byte-identical; step 5 called at :1451 with (keys, run_date, http_get).",
        "fetch.py:346 build_source_object returns at :361 on the battery branch before bronze_sink is consulted; :356-358 states bronze on the battery path is written through the sink threaded into run_battery; steps 1/2/4 receive it at battery.py:1445/1447/1450 and steps 3 (:900) and 5 (:1342) take no bronze_sink parameter."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "The cell met every criterion and the route it built returns no filing; one of the two findings the round produced was described by both seats in a weaker form than the artifact supports.",
    "notes": "MY OWN NEAR-MISS, recorded because it nearly landed on a worker: my first read of the instance used guessed key names (id/evidence), printed blanks, and an empty field read as an ABSENT proof -- I was one step from publishing that the dispatch-key criterion was never graded. A wrong-key read and a true absence are byte-identical at the print; print the object's REAL KEYS before concluding from a blank. NOT MEASURED HERE: whether any served winner carries winner.step in (3,5) -- that single query is what would turn the bronze asymmetry from an EXPOSURE into an INCIDENT, and it is the next reader's, not this grade's.",
    "adjudicates": [
      "AMGT_RESAPP-Z-W128-S1",
      "AMGT_RESAPP-Z-W128-S2"
    ],
    "dismissal_reason": "Grade record plus two dispositions: Z-W128-S1 STANDS UNSOFTENED (the next HKEX attempt is a research cell, not a tuning pass) and Z-W128-S2 is re-stated in its true form and handed to the estate; neither is resolved inside this project."
  }
]
```
