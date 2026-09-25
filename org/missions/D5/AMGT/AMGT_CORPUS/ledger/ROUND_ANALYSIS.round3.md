# AMGT_CORPUS -- ROUND 3 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-25 ~02:4xZ

**Inputs:** `3.0.0_SA_CVO~Z`'s slug, msg 25840, and `ADJUDICATION_v6.md` @`4749dc06e2` (blob IDENTICAL at
that pin and at HEAD, verified); the FINAL drain-end packet @`4be92efa19`; my own reads of the served
crosswalk and the re-ingest log.

**GRADE ACCEPTED.** L10 preconditions MET: 5 of 5 terminal; 13 rows dispositioned; judgment criteria
**NONE cut -- met vacuously, and the adjudication says so in those words.** A vacuous pass declared as
vacuous is worth more than a criterion invented to avoid saying it.

---

## 1. THE IDENTITY RESIDUE IS CLOSED -- verified three times, by three seats, on two planes

The thing that was this goal's live edge all day -- 40 names, then 4, then AMD -- is **done**.

| read | instrument | result |
|---|---|---|
| served crosswalk (mine, 02:0xZ) | `boto3 get_object` on `crosswalk/v1/2026-09-25.json` | records **235**, MEASURED **235**, UNRESOLVED **0**, **94** distinct folders |
| served crosswalk (CVO's, independent) | same key, its own read | 235 records, 94 folders, 235/235 keyed |
| the re-ingest (mine, at the log) | `reingest_after_remint5_20260925T015837Z.log` | **`resolved_folders 94 files_in_resolved 354 stored 354 (put_performed 83 existed 271) read_failed 0`**, `unresolved_files 0 in 0 folders`, `rc=0` |

`Z-S25` measured *"89 of 94 live folders carry a MEASURED identity, SHORT BY FIVE."* **Closed, and
confirmed on the plane the consumer reads.** The re-ingest was the one limb my own never-widen half named
as a PREDICTION only it could settle; it is now a measurement.

**A note I owe that lane:** the CVO used the NESTED `source_row.folder` path *"because of your instrument
note yesterday"*. That note existed because I produced the false 94-folders-missing census myself and
declined to publish it. **An instrument trap recorded after a near-miss did its job in another seat's
hands a day later** -- which is the only evidence that writing them down is worth the words.

## 2. THE ARTIFACT CONTRADICTS ITSELF, AND IT IS GOAL-CRITICAL -- I RULE ON IT HERE

The CVO's headline finding, which I verified on the served object rather than accepting:

```
denominators.input_names             89          <- the DISCLOSURE
coverage_vintage.denominator_folders 89          <- from the 2026-09-10T23:18Z builder snapshot
identity_universe                    s3://opal-data-harvest/universe/v1/2026-09-16.json
ACTUAL distinct folders in records   94          <- the DATA
```

**The DATA moved to 94. The DISCLOSURE still reads 89.** This is not a wrong claim -- it is **a claim a
reader cannot verify from the object that carries it.** Anyone checking "94 of 94" against the artifact's
own `denominators` block gets 89 and concludes the round overstates by five.

**Why it is goal-critical and not bookkeeping:** the goal is *"every single security in the Asset
Management research folder"*, and **this object IS that denominator.** A completion test that reads
`denominators.input_names` measures against a stale snapshot that excludes the five newest folders,
AMD among them. The universe pin is the `2026-09-16` file, which **Andrew's ~17:4xZ word superseded when
he made the universe the LIVE research directory.**

**RULING, and it binds this project:**
1. **NO COMPLETION TEST MAY READ `denominators.input_names` OR `coverage_vintage.denominator_folders`
   UNTIL THEY ARE REBUILT.** Until then the denominator is the distinct `source_row.folder` count over
   `records`, and any statement of it names that as its source.
2. **Round 4 cuts ONE cell that rebuilds the denominators block and re-pins `identity_universe` to the
   live research directory**, so the object's disclosure matches its contents. It is a DISCLOSURE fix,
   not a data fix -- the contents are already correct, which is what makes it cheap.
   [**CORRECTED 2026-09-25 ~03:4xZ -- SEE AMENDMENT 1. "re-pins `identity_universe`" IS WRONG AS
   WRITTEN and `2.0.0_SA_COO~X` caught it: that field is the RESOLUTION INPUT, not the denominator of
   record. Taking my instruction literally would have broken identity resolution to fix a disclosure.**]
3. **A VALUE MUST CARRY ITS CLAIM applies to a denominator as much as to a figure.** An artifact whose
   own count field disagrees with its own rows is the failure that law exists to prevent, and it is worse
   here than a missing field would be, because a WRONG denominator is confidently readable.

**Cost:** one cell, no vendor act, no served-data change. **Non-application:** it does not reach any other
artifact's denominators block; this ruling names this object.

## 3. THE OPEN SCOPE QUESTION -- RULED: THE ROUND-39 RULE REACHES `AMGT_CORPUS`, WITH THE EXCEPTION IT NEEDED

The CVO raised, and pointedly did NOT act on, whether round 39's `AMGT_RESAPP` ruling -- *"A ROUND WHOSE
CELLS TOUCH SERVED FIGURES CARRIES AT LEAST ONE JUDGMENT CRITERION, graded at L9"* -- reaches this
project. **Refusing to widen it was correct**: converting one project's ruling into a bar on another is
the move CLAUDE.md section 2 forbids, and routing the decision to the seat that issued it is exactly
right.

**RULING: YES, it reaches `AMGT_CORPUS`, and it acquires an exception this round earned.**

- **It reaches**, because its rationale is not project-specific: an all-mechanical round has no
  plausibility oracle, and every column can read green over a served figure that is wrong. This project
  serves figures; the reason applies unchanged.
- **THE EXCEPTION: a served outcome with NO REAL RUN is declared NOT GRADEABLE, and no judgment criterion
  is invented for it.** Two of this round's three served outcomes -- the Model block and the dossiers --
  had no real run, and a criterion cut against them would have graded nothing while reading as a grade.
  **The rule exists to stop an unexamined served figure passing, not to require a criterion where there
  is nothing to examine.** A manufactured criterion is worse than none: it converts an honest gap into a
  false pass.
- **This round satisfies the rule's INTENT and not its LETTER**, and I grade it on the intent: the one
  served outcome that DID move -- the crosswalk -- was independently verified at the served key by a seat
  that did not run it. That is what a judgment criterion buys. **From round 4, `AMGT_CORPUS` cuts one
  explicitly** rather than relying on the CVO's own initiative to supply it.

## 4. OUTCOMES

- **`FWD-19` -- NOT REALIZED.** Its ACCEPT is *Andrew names any of the securities and gets its corpus
  layers or the reason it has none.* The dossier sequence is **blocked at step 1** and had no real run;
  identity being complete is its PRECONDITION, not its satisfaction.
- **`FWD-12` -- NOT REALIZED, and NOT GRADEABLE this round.** The derive did not run. Its last served
  state is **31 blocks restored by copy-forward + 58 honest-empty**, and `Z-S29` (history `{}` for every
  key while reference and forecast landed, the client dropping a request-level error) is the live cause.
- **The identity residue -- CLOSED**, per section 1.

## 5. `Z-S26` IS A SERVED-OUTPUT INCIDENT AND THE ADJUDICATION IS RIGHT TO GRADE IT AS ONE

Security keys passed where Bloomberg identifiers were required; **31 names served empty blocks for ~7
minutes**; rolled back copy-forward 31 of 31; ledger entry closed run-and-rolled-back. **It stays ARMED**
because the condition that produced it -- a pull that cannot distinguish an empty response from a failed
one -- is still live as `Z-S29`. **Grading the incident closed because its ROLLBACK completed would have
retired the hazard while its CAUSE ran.** That distinction is the adjudication's, and I adopt it.

## 6. THE ROUND'S BEST FINDING, AND IT IS NOW A THREE-INSTANCE CLASS

The packet's own enrichment 4: *"A verify leg checks CONTENT, not presence"* -- `Z-S26`: **89 of 89 raw
objects existed, all 89 were empty, and the verify PASSED.**

That is the same shape as `AMGT_RESAPP-Z-S265` (a P/E rendered 100x wrong under a 12-of-12 green grid) and
`Z-S268` (a harness that computed extras and never graded them). **An instrument that confirms a thing
EXISTS and never asks what it SAYS.** Three instances, two projects, one week -- and my own session added
a fourth of the same family: a re-pull whose 89 of 89 keys "landed" while every history payload was `{}`.

**STANDING RULE for both projects, stated with its cost and non-application:** a verify leg that can pass
on an object's EXISTENCE states what it read INSIDE the object, and prints the count of objects that were
present-but-empty beside the count present. **Cost:** one field per verify leg. **Non-application:** a
leg whose subject genuinely IS existence -- a write-once landing check, where presence is the whole
claim -- says so and is exempt.

## 7. ROUND 4 -- `2.0.0_SA_COO~X`'s to cut

1. **The denominators/universe-pin rebuild** (section 2), so the object's disclosure matches its contents.
2. **The FWD-12 derive**, once `Z-S29`'s field-limit cause is resolved -- the historical request grew 23
   -> 39 fields and the client DROPS a request-level error. **The dropped error is MEASURED; the
   per-request field limit is INFERRED**, and the cell states which it is testing.
3. **The dossier sequence**, blocked at step 1 -- `FWD-19`'s remaining path.
4. **ONE JUDGMENT CRITERION**, per section 3.
5. **The verify-leg content rule** (section 6) applied to whichever legs round 4 cuts.

## 8. WHAT THIS ROUND DOES NOT CLOSE

`AMGT_CORPUS` is **not** complete. Identity is complete; the backfill is not. **The goal's clause is the
backfill, and the clause below identity is still open**: 58 of 89 model blocks are honest-empty, the
dossier sequence is blocked at step 1, and `FWD-12` and `FWD-19` are both NOT REALIZED.

---

**ROUND 3 IS CLOSED.** `2.0.0_SA_COO~X` recuts round 4 from section 7 in ONE issuance.

---

# AMENDMENT 1, 2026-09-25 ~03:4xZ -- SECTION 2's INSTRUCTION WAS WRONG AND THE ISSUER'S READING IS RIGHT

`2.0.0_SA_COO~X`'s decomposition v4.0 s.8 flags its own reading for my correction, which is the right way
to raise it. **The reading is correct and my instruction was not.**

**What I wrote:** *"re-pins `identity_universe` to the live research directory."*

**What that would have done:** `identity_universe` is the builder's **RESOLUTION INPUT** -- its 250 names
are what folder forms resolve AGAINST. Re-pinning it to the 94-folder research directory would have
narrowed the resolver's own input from 250 to 94, **breaking identity resolution in order to fix a
disclosure.** The two things my sentence ran together are: the SET A RESOLVER SEARCHES, and the
POPULATION A COMPLETION TEST COUNTS. They are different fields with different consumers and only the
second was ever my subject.

**The issuer's reading, adopted verbatim as this analysis's own:** `identity_universe` stays the identity
input; the DENOMINATOR OF RECORD becomes the live directory, disclosed in `research_universe` and
`denominators.research_folders_live`. **And it correctly declines the data change** -- rebuilding
coverage records from the live listing is NOT cut, because section 2 already said the contents are
correct and this is a disclosure fix.

**The keepable form, and it is the same failure I have now made twice tonight in different clothes:** I
named a FIELD when I meant a PROPERTY. Section 2's finding was about the object's *disclosed
denominator*; naming `identity_universe` as the thing to re-pin was me reaching for the nearest field
that mentioned "universe" -- the same reflex that had me trace Peers P/E to the first path mentioning
P/E. **A ruling that names a field commits its reader to that field; a ruling that names the property
lets the implementer pick the field that carries it, and the implementer knows the schema better than
the ruler does.**

**So the standing form for my own rulings from here:** where a ruling can name a PROPERTY (*"the
disclosed denominator must match the contents"*) rather than a FIELD (*"re-pin `identity_universe`"*),
it names the property and says which consumer must be able to read it. **Cost:** nothing -- it is
shorter. **Non-application:** where the field IS the subject (a schema's enum, a named key in a
contract), name it exactly, because there the field and the property are the same thing.

**One consequence worth recording beside it:** decomp v4.0 s.5 has f-3's drain verifying *"dossiers
present for the 94 folders' resolved keys"*, while `AMGT_RESAPP`'s `rp-1` measures `FWD-30` across **89**.
**Both are internally correct** -- CORPUS works the live corpus, RESAPP the coverage-list snapshot -- but
the two projects are now demonstrably working to DIFFERENT POPULATIONS. That is not a defect to fix here;
it is the measured consequence of the universe card at Andrew, and it makes that card concrete rather
than theoretical.
