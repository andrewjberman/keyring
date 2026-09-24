# AMGT_RESAPP: CVO classification -- the deployed API SERVES 179 sentences the ratified clause HOLDS. INCIDENT, not exposure.

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T17:1xZ, LOCAL on SITEZ.
**Source:** `4.0.0_SA_CRO~Z`'s measurement on the deployed `opal-amgt-scoped-api`, relayed to this seat.
**Boundary:** retained-data integrity -- this seat's, under the accepted reviewer structure @`dba746f9b4`.
**Dispositions:** none. This row OPENS a hazard.

## THE MEASUREMENT (attributed; not re-derived here -- a live invoke is a deployed-plane act)

**12 bounded `GET /thesis` engineering invokes, plus a missing-firm control returning 401. All 12 return
HTTP 200 with `drafting_status: SERVED`: 389 sentences, 179 WITHOUT SPANS, and all 12 no-span text-hash
sets MATCH the exact historical census.** Package code hash unchanged, `LastModified 2026-09-22T10:07:44Z`.

⛔ **The ratified clause `C-VERBATIM-GATE` (v0.12, PRD `:1107-1114`, Andrew-direct *"Agreed, yes."*):
a drafted sentence with no verbatim span is HELD -- never served.** **Production serves all 179.**

## 1. CLASSIFICATION -- INCIDENT, AND THE REMEDY IS DOUBLE

⭐ **Rule 22's negative mirror: a missing guard is an EXPOSURE until someone measures whether it FIRED;
then it is an INCIDENT, and the two carry DIFFERENT remedies.** ⛔ **This fired -- 12 of 12, with
hash-matched identity against the historical census.** **An exposure is closed by BUILDING the guard. An
incident ALSO requires RE-OPENING WHATEVER THE GAP ADMITTED**, and what it admitted is the served
documents.

## 2. ⛔ THE REPAIR IS A SERVED-OUTPUT ACT AND IS GATED

**No retained object may be rewritten to remove those sentences without the NEVER-WIDEN PAIR** -- the
CTO and COO halves naming the act's blast radius and the per-key rollback. **That is `R2` of the
retained-controls list this seat signed @`974081d221`, and a quiet re-emission of 12 documents is
precisely the act the pair governs.** ⭐ **`4.0.0_SA_CRO~Z` reports "no object rewrite, deployment or
schema fix made yet" -- the correct posture, and it holds until the pair is on file.**
**Build the runtime enforcement with its positive / refused / held regression controls first.**

## 3. ⛔ THE CAUSE IS A PLANE DIFFERENCE, AND IT CORRECTS THIS SEAT

Twenty minutes earlier this seat reviewed `I5` and wrote *"the pipeline matches the v0.12 clause; the
schema alone is weaker."* ⚠ **That rested on a REPO probe.** `4.0.0_SA_CRO~Z`'s correction: it is **not
literally schema-only** -- the **DEPLOYED** `_validate_drafting_document` runs jsonschema,
`validate_evidence` and `check_against_sources` but **OMITS the pipeline no-span HOLD, so empty spans
pass VACUOUSLY.**

⭐ **That is Rule 22's GRAIN axis: the object certified was the repo path; the object that SERVES is the
deployed artifact, and they differ on the one clause that matters.** ⭐ **It was found by exercising the
deployed route rather than re-reading the repo -- the fifth wrong-object instance today and the first
where the wrong object was a PLANE rather than a path.**

## 4. THE L4-R GATE IS RE-BASED

This seat's gate question was *"how many of the 179 does the figure branch RELEASE?"*, answered **0** --
**about the REPO.** ⛔ **In the deployed plane all 179 are already served, so the amendment's premise is
false in production.** ⭐ **RULED: the L4-R question is asked against the DEPLOYED state. No amendment is
reviewed as "releasing 0" while production releases 179. Fix the deployed enforcement first.**
**The `I5` verdict itself stands -- it graded a candidate that changes nothing served, and said so.**

```json
[
  {
    "id": "AMGT_RESAPP-Z-C-S412",
    "project": "AMGT_RESAPP",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T17:15Z",
    "one_line": "INCIDENT, not exposure: the deployed opal-amgt-scoped-api SERVES 179 no-span sentences that C-VERBATIM-GATE v0.12 (Andrew-direct) requires to be HELD -- measured by 4.0.0_SA_CRO~Z over 12 of 12 bounded GET /thesis invokes, all HTTP 200 SERVED, 389 sentences, 179 no-span, hash-matched to the historical census. Cause is a PLANE difference: the deployed _validate_drafting_document omits the pipeline no-span HOLD and empty spans pass vacuously, so this seat's earlier repo-probe finding that the pipeline matches the clause does not reach the served artifact.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "4.0.0_SA_CRO~Z for the runtime enforcement repair; 1.0.0_SA_CTO and 2.0.0_SA_COO jointly for the never-widen pair that any retained-object rewrite requires",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "4.0.0_SA_CRO~Z, deployed opal-amgt-scoped-api: 12 bounded GET /thesis invokes plus a missing-firm 401 control; all 12 HTTP 200 with drafting_status SERVED, 389 sentences, 179 without spans, all 12 no-span text-hash sets matching the exact historical census; package code hash unchanged, LastModified 2026-09-22T10:07:44Z.",
        "Ratified clause C-VERBATIM-GATE v0.12 at AMGT_RESAPP PRD :1107-1114: a drafted sentence with no verbatim span is HELD, never served (Andrew-direct ~19:4xZ, 'Agreed, yes.'), withholding 179 of 389 across 12 served documents.",
        "Causal correction by the same seat: the deployed _validate_drafting_document runs jsonschema, validate_evidence and check_against_sources but omits the pipeline no-span HOLD; empty spans pass vacuously.",
        "This seat's own CLAUSE_COMPARISON-based statement that the pipeline matches the clause was a REPO probe and does not reach the deployed artifact."
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "A drafted sentence with no verbatim span is HELD: never served.",
    "world_is": "The deployed API serves all 179 of them, and has since at least the 2026-09-22 package.",
    "notes": "REMEDY IS DOUBLE AND THE HALVES HAVE DIFFERENT OWNERS: (1) build the runtime enforcement with positive/refused/held regression controls; (2) re-open what the gap admitted -- the served documents -- which is a SERVED-OUTPUT ACT requiring the never-widen pair (R2 of the signed retained-controls list). NO RETAINED OBJECT IS REWRITTEN BEFORE THAT PAIR IS ON FILE; 'no object rewrite, deployment or schema fix made yet' is the correct posture and holds. NOT RE-DERIVED HERE: a live invoke is a deployed-plane act and this row attributes the measurement rather than repeating it. AND THE L4-R GATE IS RE-BASED: the figure-branch question is asked against the DEPLOYED state, since 'releases 0 of 179' is true of the repo while production already releases all 179."
  }
]
```
