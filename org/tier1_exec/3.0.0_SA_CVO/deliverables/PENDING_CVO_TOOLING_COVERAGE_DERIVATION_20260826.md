# PENDING — `proof-of-spec-check` coverage derivation (HELD, with a stated trigger)

**Owner:** `3.0.0_SA_CVO` · **Opened:** 2026-08-26T01:1xZ · **State:** HELD, NOT FORGOTTEN
**Why this file exists:** the commitment currently lives in a message (CVO 71584 to `1.0.0_SA_CTO`)
and in one seat's head. **A message scrolls; a successor CVO would inherit the obligation with no way
to find it.** That is the failure this fabric hit four separate times on 2026-08-25 — including twice
by this seat — so it is written down instead.

---

## THE CHANGE, RULED BUT NOT LANDED

`1.0.0_SA_CTO` put the design call to CVO (71578): should the BARE invocation of
`proof-of-spec-check.py` be made impossible, since a coverage gap and a clean pass are byte-identical
to anyone who runs it without passing the criteria?

**CVO RULING (71584): NEITHER forbid it NOR document it — DERIVE it.**
The checker already resolves the governing TO on every run and prints that resolution. It is standing
on the document that contains `<expected_criteria>` and then waits to be handed the criteria by hand.
**Read the field it is already on.** Requiring the argument instead would move the failure from
FORGETTING to MISTYPING — and a hand-passed SUBSET passes cleanly (`expected=4 carried=4 matched=4`
is VALID), which is the same hole one step later wearing the appearance of compliance.

## ⛔ TWO CONSTRAINTS THAT MUST SHIP WITH IT

**1. REPORT, DO NOT REFUSE.** Always printing the coverage line with its denominator is CVO's own
instrument and CVO's call. **Making it fail-closed is a NEW GATE ON EVERY SEAT'S WORK, which CLAUDE.md
reserves to Andrew.** CTO delegating the design does not create authority neither seat holds. If the
estate wants it blocking, that is a gate candidate that goes to Andrew with this reasoning attached.

**2. MULTI-ARTIFACT TOs MUST REPORT `COVERAGE-INDETERMINATE`, NOT `INVALID`.**
Measured on this seat's own row: `OPAL_ADVIPOINTERS.P4-PINS-CERT-49F` is a TWO-PHASE TO whose work
landed in THREE artifacts, so its seven declared criteria can never be satisfied by any single
instance. Run with its own `<expected_criteria>` it returns INVALID — 4 violations, 3 named omissions
— and **2 of the 3 are discharged in a named sibling cert while the third is openly declared OPEN.**
**A check that flags a correctly-closed row every time it runs gets suppressed, and a suppressed
control is not a control.** Until a TO can declare its INSTANCE SET or its criteria PER PHASE, the
derived form must distinguish "criteria missing" from "criteria satisfied in a declared sibling".

## THE TRIGGER — MEASURED, NOT REMEMBERED

**Land it when the live wave closes**, because the change moves VERDICTS (it can turn a passing run
INVALID) and six seats are filing returns through the tool. *(Contrast: the crash-vs-INVALID exit-code
fix `@9c9b2fd96b` moved NO verdict and was landed mid-wave deliberately — that distinction is the
reason, not an exception.)*

**Wave state measured 2026-08-26T01:1xZ — DO NOT LAND YET:**

| TO | status |
|---|---|
| `ADVI_PERFRP.TO-R1-DE` | ACTIVE |
| `ADVI_PERFRP.TO-R1-DS` | complete |
| `ADVI_PERFRP.TO-R1-AE` | ACTIVE |
| `ADVI_STITCH.TO-A1-DS` | ACTIVE |
| `ADVI_STITCH.TO-A1-AE` | COMPLETE |
| `ADVI_INSURE.TO-R1-DS` | pending |

**2 of 6 complete. The hold stands.**

**HOW A SUCCESSOR CHECKS:** re-read the six `<status>` fields above from their TO files. **Do not take
this table as current — it is a timestamp, not a fact** (the lesson `0.8.0_AE_CloudComp` established
tonight on a moving S3 root, and the reason this table carries its read time).
`2.0.0_SA_COO` owns wave state and may release the hold earlier.
