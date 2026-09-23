# OPEN CALL AT ANDREW -- `1.0.0_SA_CTO~Z` (1 call, 2026-09-23 ~17:2xZ)

**A clause you ratified is being violated by a deployed API.** This card exists because the
violated clause is YOUR word, not because the repair needs your permission -- the repair is
already in flight and nothing waits on this card.

---

## BLOCKING (an act is held pending the word)

```
+-- CALL 1 of 1 ---------------------------------------------------------------+
  **The deployed `opal-amgt-scoped-api` is SERVING sentences that `C-VERBATIM-GATE`
  v0.12 -- your "Agreed, yes." -- says are HELD, NEVER SERVED. Do we (a) repair and
  re-emit on the normal path with the never-widen pair, or (b) stop the endpoint now?**
  Measured on the deployed route: 12 of 12 documents return HTTP 200 `drafting_status:
  SERVED`, carrying 179 no-span sentences, hash-matched to the historical census.
  ------------------------------------------------------------------------------
  **REC -- (a), REPAIR ON THE NORMAL PATH.** The repair is built and passing; a
  unilateral disable is itself an unmeasured-blast-radius deploy act, which is the
  defect we are fixing. ⛔ **This flips to (b) the moment the reachability
  measurement below returns "reachable outside engineering" -- that answer is
  PENDING and is the only thing that would change the rec.**
+------------------------------------------------------------------------------+
```

---

## THE MEASUREMENT, AND WHAT IS STILL UNMEASURED

| | |
|---|---|
| instrument | 12 bounded `GET /thesis` engineering invokes against the **deployed** API, by `4.0.0_SA_CRO~Z` |
| result | **12 of 12** HTTP 200, `drafting_status: SERVED` |
| held-but-served | **179 no-span sentences TOTAL across the twelve documents** (389 sentences total); **per-document range 2 to 26** |
| identity | all 12 no-span text-hash sets **match the exact historical census** |
| negative control | missing-firm request returns **401** -- the 200s mean *served*, not *answers anything* |
| ⛔ **window opens** | **no later than 2026-09-19** -- the pinned `rk-41` ledger already records a deployed BA response serving 21 no-span sentences |
| ⚠ **PENDING** | the **complete current drafting set** (the 12 were explicitly HISTORICAL, so 12 is a sweep, not the set) |
| ⚠ **PENDING** | **non-engineering reachability** -- whether anything outside the engineering path can reach this endpoint |

⛔ **SENT IS NOT READ.** This is demonstrated deployed API output. **Nothing here measures whether a
human or a browser ever viewed these sentences**, and that question is open in both directions.
The remedy does not wait on it: the capability is live and reachable on demand.

## THE CAUSE -- A GUARD THAT IS BLIND TO THE EMPTY CASE

The deployed `_validate_drafting_document` runs `jsonschema`, `validate_evidence` **and**
`check_against_sources`. ⛔ **It omits the pipeline's no-span HOLD, and an object with zero spans
passes VACUOUSLY** -- a validator that iterates over spans cannot fail an object that has none.
It is not a weak guard; it is **structurally blind to the empty case, and it reports success while
being blind.**

⭐ **The same shape surfaced on two unrelated surfaces within the hour** -- a period-ordering check
that repeats the lexical comparison it validates, and a generation that publishes COMPLETE over an
input population that was never collected. **A check that grades MEMBERS cannot grade the ABSENCE
of members.** Every validator written from here carries an empty-input fixture.

## WHAT IS ALREADY DONE, AND WHAT IS DELIBERATELY NOT

**DONE:** runtime read-boundary repair implemented locally (empty/missing/blank spans held, valid
quoted siblings retained, separate object-vs-read held counts exposed, retained files unchanged);
**54 focused API tests PASS**; surprise row filed with `hazard_standing: ARMED`; classification
independently reached as **INCIDENT** by `1.0.0_SA_CTO~Z` and `3.0.0_SA_CVO~Z` on separate reads.

⛔ **NOT DONE, DELIBERATELY:** no deploy · no retained-object rewrite · no source rewrite. **The 12
retained objects ARE the incident's evidence and a rewrite would destroy it.** Any re-emission is a
served-output act requiring the **CTO+COO never-widen pair** before it moves, and `3.0.0_SA_CVO~Z`
has stated it refuses to review a cutover whose pair is absent.

## TWO THINGS I GOT WRONG ON THIS ITEM, BOTH CORRECTED IN-HOUR

1. ⛔ **I ruled "releases 0 of 179, therefore no L4-R is owed."** That was true of the **REPO** and
   false of **PRODUCTION**, where all 179 are already served. `3.0.0_SA_CVO~Z` re-based its own gate
   against its own earlier certification and I withdrew mine. **An amendment cannot be reviewed as
   "releasing nothing" while production already releases everything.**
2. ⛔ **I told my own never-widen pair half that the fix "removes 179 of 389 (46%) from EVERY served
   document."** **179 is the TOTAL across twelve; per-document is 2 to 26.** I restated a **pooled
   ratio as a per-member property** -- in the one sentence a never-widen half exists to get right.
   Caught by `4.0.0_SA_CRO~Z`, corrected to all four recipients before the half was drafted.

⭐ **And the most uncomfortable finding: the incident was WRITTEN DOWN on 2026-09-19, in our own
pinned ledger, naming 21 served no-span sentences -- and nobody read it as an incident.** It took a
deliberate exercise of the deployed route today to see what the record already said. **A recorded
observation is not a recognised finding.**

-- `1.0.0_SA_CTO~Z`, site Z. All cited commits LOCAL; push owed by `0.0.0_AB_MSTR~Z`.

---

# UPDATE ~17:3xZ -- BOTH PENDING NUMBERS RESOLVED. THE TRIGGER FIRED AND THE REC DID NOT FLIP.

**Appended, not edited: the card above is true at its own vintage and this supersedes only the two
lines it marked PENDING.**

| was PENDING | now MEASURED |
|---|---|
| the complete current drafting set | ⭐ **EXACTLY 12 OBJECTS -- the sweep and the set COINCIDE.** The incident is fully scoped; 12-and-12 by coincidence reads identically to 12-of-many and only measuring the prefix distinguishes them |
| non-engineering reachability | ⛔ **REACHABLE. Traced: portal CloudFront -> CUSTOM-authorized API -> the affected Lambda.** ⚠ **REACHABLE is measured; REACHED is not** -- authenticated browser and human viewing remain unmeasured, and the card does not blur them in either direction |

## ⛔ THE TRIGGER FIRED. MY REC IS STILL (a), AND HERE IS WHY

The card said the rec flips to *stop the endpoint* on a "reachable outside engineering" answer.
**It came back reachable. I am not flipping it, and I am recording the reasoning rather than
letting the rec sit silently unchanged.**

**The fix is PROVEN against the exact retained bytes:** replay of all 12 versions ->
**210 served, 179 held, ZERO no-span output**, valid anchored text sequence, **source hashes
unchanged**, **225 API tests PASS**, Ruff PASS. ⭐ **210 + 179 = 389 reconciles exactly to the
historical census -- the repair holds precisely the 179 and touches none of the other 210.**

⛔ **Disabling a portal-reachable endpoint would be a served-output act with a LARGER blast radius
than deploying a validated repair, taken to avoid a defect we can already fix. That is the mirror of
the mistake being corrected.** **EXPEDITE THE DEPLOY, with the never-widen pair.**

## ⛔ MY NEVER-WIDEN HALF IS STILL UNSIGNED, DELIBERATELY

The rule requires the half to PRINT the number of WRITERS of the named property. **The named
property is "what the API serves", this surface already has two enforcement points that disagree
(the pipeline HOLD and the deployed `_validate_drafting_document`), and I have not counted them.**
**Owed by `4.0.0_SA_CRO~Z` before I sign: how many code paths can emit a served drafting document,
and does the repair sit on ALL of them?** ⚠ **If more than one, the repair is incomplete -- which is
exactly how the present defect exists.**

## ⚠ A SECOND, SEPARATE ITEM THAT AROSE FROM THE EVIDENCE PACKAGING

`4.0.0_SA_CRO~Z` self-reported that its incident-evidence commit captured a **live CloudFront origin
custom-header value**, halted the drain, did not repeat the value, and is redacting and replacing the
(unpushed) commit. ⭐ **Found by the seat that made it, within minutes.** I withdrew my own
ratification of that pin to `0.0.0_AB_MSTR~Z` -- the seat that pushes -- six minutes after issuing it.

⛔ **DECISION OWED AND NOT MINE: redaction removes the value from the artifact; it does not
un-expose it.** **If that commit ever reached a remote, or anything else read the file, the header
value should be ROTATED** -- an infra act belonging to Andrew and the CloudOps lane. **Discriminators
are cheap: `git ls-remote` on the branch, and whether the path is tracked or scratch.**

## ALSO AT ANDREW, UNRELATED TO THE INCIDENT

**Closer `S` still has NO MANDATE.** It confirms it has not inspected the C candidate and holds no
`S01` implementation, **because its own Codex chat retains task-order authorization** -- and
`2.0.0_SA_COO~X` correctly reports that **one closer cannot confer session authorization on
another.** ⛔ **This needs one line from Andrew in S's own chat: there are no task orders in closer
mode; the brief is the mandate.** Everything else in closer mode is running.

