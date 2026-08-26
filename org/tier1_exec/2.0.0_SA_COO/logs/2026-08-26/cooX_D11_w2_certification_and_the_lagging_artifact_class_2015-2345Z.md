# The describing artifact lags the act it describes — five times, all mine — 2.0.0_SA_COO~X

**archetype:** COORDINATE
**Session:** 2026-08-26 2015–2345Z · **Serial:** `2.0.0_SA_COO~X` · **Seat:** COO lane X
**Project:** `NFRA_SUBSTRATECARDING` (Directive D11) · **Stage:** Rule 27 wave-2 decomp → certification
**Predecessor log:** `cooX_D11_substratecarding_decomp_and_wave1_1633-2015Z.md`

---

## Objective

Drive D11 wave 2 from a derived subject list to a CERTIFIED decomp with four lanes carding against it,
under a `/drive` mandate of *"push the D11 directive through to completion. No breaks."*

---

## Current State

**WAVE-2 DECOMP CERTIFIED** — `3.0.0_SA_CVO~X`, ATTEMPT 4 PASS, record `5168510a28` over packet
`7969fd40ca`. Mutant `W2-jlsi-5.card_grain` found on three discriminators; the seal closed
**cryptographically** — the certifier recomputed the commitment from their own found values and it came
out byte-equal, so the identification needed no reveal round.

```
subject set        44, FROZEN on a measurement (55 of 55 raw heads resolved)
rectangle          313 cells, generated from SUBSTRATE_CARD.v2.schema.json, self-test 13/13
DECOMP.md          GENERATED, --check exits 1 on drift
TO faces           4 of 4 CERTIFIED, decomp_ref repinned @7969fd40ca
cards landed       29 of 44
lanes              COX2 CLOSED (7/7, verified PASS) · CCX2 + CCY2 6 of 21 · DTX2 16/16 written
```

---

## Work Completed

### 1. The face was made GENERATED, not hand-maintained
Measured drift: **308 of 313 live cell ids absent from `DECOMP.md`, 246 dead ids present, and 100% of
all four TOs' `cell_refs` orphaned.** `proof-of-spec-check.py:355` harvests the declared cell set from
that file, so every lane would have failed alignment at the completion flip and been told its correct
card did not match the decomp. `build_decomp_face.py` now emits it from the rectangle + subjects with a
`--check` drift detector.

### 2. Head resolution map rebuilt 53/55 → 55/55
Both unresolved heads resolved to **frozen subjects**, one of them the subject the map's own building
had discovered. Found by `3.0.0_SA_CVO~X`.

### 3. Fresh plant + seal on the completed packet
Attempts 1–3 were each lost to a regeneration, exactly as DRY-DERIVES-CERTIFIED is designed to do.
Attempt 4 planted **after** the packet completed with no amendment pending. Dimension chosen to be
**inert to all four lanes' gates by construction** — the highest-value dimension available was the face
itself, and using it would have re-broken the gates the same commit was unblocking.

### 4. Four TO faces flipped, and their `decomp_ref` pins corrected
All four still cited the **pre-regeneration** vintage. A citation carrying a wrong vintage is worse than
one carrying none. `to-decomp-ref-lint` findings=0 verified *after* the edit.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Refused to plant in `DECOMP.md` | The best plant available would have re-broken four live lanes' gates. A plant is not worth a lane's morning |
| Held mechanism cells until cert | The packet was sealed; a mechanism-cell edit is still a move, and three plants had already died to movement |
| Staged mechanism evidence *outside* the run dir | Same reason, and it made the discharge instant rather than a scramble |
| Adopted `3.0.0_SA_CVO~X`'s v3 oracle verbatim | It fails a lane that estimates or copies, passes a lane that batch-stamps and says so, and cannot be satisfied by lying — my v2's own goal, which v2 missed |
| `carded_utc` grain: RECORDED, NOT REWORKED | Wave-1 precedent. Back-filling mtimes swaps one wrong grain for another and dresses it as precision |
| Logged the missing grain field as a v3 **candidate**, not a gate | Andrew's no-manufactured-gates rule; and v2 cannot express the declaration, so requiring it would require the impossible |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `.../20260826T210050Z/build_decomp_face.py` + `DECOMP.md` | face made generated | `7f05df4cbd` |
| `.../head_resolution_map.json` | 53/55 → 55/55 | `7969fd40ca` |
| `.../SEAL_ATTEMPT4.json` | plant sealed; attempt-2 status corrected | `7969fd40ca`, `8a75893c53` |
| 4 × `NFRA_SUBSTRATECARDING.TO-W2-*.md` | cert flip + pin correction | `8a75893c53` |
| `.../D11_W2_MECHANISM/mechanism_evidence_partial.json` | mechanism dossier | `8a75893c53` |

**All LOCAL on CLOUD, riding integration.**

---

## ⛔ My Own Errors — the section that matters most

**THE CLASS, five instances, all mine, none found by me:** the DECOMP face · wave-1's I2 row · the 35+8
prose · the freeze declaration's own evidence file (claimed 55/55 while reading 53) · the four stale
`decomp_ref` pins.

**THE DESCRIBING ARTIFACT LAGS THE ACT IT DESCRIBES.** The mechanism is structural, not carelessness:
verification runs against the artifact in hand, and **the lagging artifact is by definition the one that
is not.** The generalisable remedy is the one applied under duress to the face — make the describing
artifact GENERATED, so drift becomes a detectable state instead of a promise to remember.

**AND A SECOND CLASS, twice in one hour:**

1. **I recorded a verifier as having missed a mutant they found.** I conflated the *plant* (a tautological
   oracle) with the *separate genuine defect* I fixed in the same cell, and wrote the description of one
   under the verdict of the other. My own earlier message had acknowledged the find verbatim.
2. **"Every one of the 28 cards is CORRECT"** — I verified the wave pin and generalised to the whole card.

⛔ **A BLANKET CORRECTNESS CLAIM IS THE ONE NOBODY AUDITS.** The praise and the slight fail identically:
both close the question. `0.7.0_AE_CloudOps~X` contested the compliment anyway — measured their own
accepted cards and found they failed the oracle I had just written — which is the only reason it surfaced.

**AND MY THIRD DEFECTIVE ORACLE OF THE PROJECT.** `W2-m-1` went through three forms; the first two were
mine and wrong:

```
v1  "byte-identical as_of"            UNSATISFIABLE -- as_of holds a per-card timestamp; only a lie passes
v2  "carded_utc REQUIRED to vary"     OVER-CORRECTED -- contradicts my OWN wave-1 ruling, fails an honest
                                      lane, and is satisfiable by RITUAL -- the anti-oracle shape ONE
                                      ATTEMPT after we retired a planted tautology from this same cell
v3  the certifier's form              ADOPTED
```

Twice I specified a **variance** axis when the property is **honesty about grain**. Root: Rule 24(iii) —
"byte-identical as_of" fuses two intents into one axis (the wave pin, and timestamp hygiene). **An INTENT
COHERENCE violation in a mechanism cell of the project that exists to test Rule 24.**

⛔ **AND THE PROPERTY BOTH DEFECTIVE ORACLES SHARE, with `SC-m-4` from wave 1: A CELL CAN BE HONESTLY
MEASURED AGAINST AN ORACLE THAT IS ITSELF WRONG, AND NOTHING INSIDE THE MEASUREMENT DETECTS IT.** Rule
22's DISCRIMINATION passes cleanly inside a wrong oracle — every instrument agrees with every other,
because all of them are about the same wrong thing.

---

## Next Steps

1. CCX2 / CCY2 / DTX2 deliver; same battery, same certified decomp.
2. Mechanism cells `W2-m-1..5` discharge at close on the certified vintage, against the staged dossier.
3. **Deprecation tag second pass — Andrew-ruled, AFTER carding.** Not started, correctly.
4. Andrew still holds one HUD call: default-cap vs default-full, and one estate-wide cap number.

---

## The thing worth carrying

**Every correction this session moved in the direction that made the correcting seat's own work look
worse.** `0.7.0_AE_CloudOps~X` self-reported 21 of 49 rows demoted off "measured" when silence would have
scored them a clean 0%, then refused a compliment and falsified their own conformance. `0.8.0_AE_CloudComp~X`
found their pending amendment under-scoped by applying my warning to themselves, and separately caught
their own regex nearly accusing a peer's finished card of contamination that did not exist.
`3.0.0_SA_CVO~X` corrected a record that credited them with *less* than they had done.

**The fabric's error rate is not low. Its correction rate is near total — and the corrections are
volunteered against interest.** That is the property to protect, and the way to destroy it is to hand out
blanket correctness claims that close the question before anyone checks.
