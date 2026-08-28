# CTO~Z — post-reboot resume: the deployed BYTES read, and a second served defect found in the coverage sweep for the first, 1628-1650Z

**archetype:** MIXED
**secondary_archetypes:** VALIDATE, COORDINATE, SCRIBE

**Serial:** `1.0.0_SA_CTO~Z` · **Window:** 2026-08-28 16:28Z -> 16:50Z (continues
`ctoZ_pre_reboot_close_1455-1605Z.md` across the ~16:0xZ device reboot)
**Basis:** ANDREW-DIRECT — *"Yes let's get the tier 1 ~Z agents back online and they can pick up
where they left off."* Startup order: `/watcher` once, then `org/XXX.md`. Zero crons stands.

---

## 1. WHAT CHANGED THIS WINDOW

- ⭐ **THE DEPLOYED LAMBDA BYTES WERE READ, AND THEY CARRY THE UNFIXED PREDICATE.** Not an inference
  from `LastModified`. Downloaded the `mdpf-gold-lambda` package, extracted
  `mdpf_gold_consolidator.py`, read the branch: `member.view_path == "SMA"` still at `:591`,
  `_l0_of` occurrences **0** — against a **positive control of 3** in `git show
  70a0828226:...`. So tomorrow's ~13:30Z fire reproduces the falsehood; TO-M1-DS AC1 and TO-N1-DS
  AC7 do not lift.
- ⛔ **A SECOND SERVED DEFECT, PREVIOUSLY UNREPORTED BY ANY SEAT.** `global.Client` aggregates over
  **ONE of three firms**, understating by **$359,773,356.74**. Served plane
  (`opal-data-portal-v2`, `platinum/mdpf/*/category-views.json`, 4 of 4 scopes, 13:50:50Z).
- **`build_package.py` interlock correction COMMITTED** @`51bf6208a5`, now ON ORIGIN as a parent of
  the merge `1f6fafa435` — 62 lines that had survived the reboot uncommitted.
- **The ship-lift card was RE-FRAMED and `2.0.0_SA_COO~Z` withdrew its own framing** rather than
  repairing it. `0.0.0_AB_MSTR~Z` carries the reframed card to Andrew.

## 2. ⛔ WHAT I GOT WRONG (2), AND THE FIRST ONE I CAUGHT ONLY BY MEASURING

| Claim | Truth | Caught by |
|---|---|---|
| "global.Client **is 49financial's figure**" (my own 13457) | a COINCIDENCE OF THE DATA. The mechanism is *aggregates over ONE of three members*; the 49f-equality is what that looks like today | myself, by testing it against the pending fix |
| pre-reboot: "the served artifact **cites Andrew**" | the falsehood is the **producer's INFERENCE FROM** his words. He said SMAs appear in SmartX **for 49 Financial only**; the producer templated that to "NO SMA members / A TRUE ZERO" across four scopes and **inverted on the one scope his sentence carves out** | myself, reading the `absent_reason` across all four |

⛔ **THE SECOND ONE MATTERED BECAUSE IT WAS HEADED FOR A CARD IN FRONT OF HIM.** "A served sentence
is false while citing Andrew" survives a careless read as *"Andrew said something false."*
`2.0.0_SA_COO~Z` had the identical phrasing in its `@4174052d92` cut message and its 16:05Z log, and
corrected its own record on this rather than defending it. **His statement is not the defect.**

⭐ **AND THE FIRST ONE IS THE REUSABLE ONE.** I described a defect BY A VALUE IT HAPPENED TO EQUAL.
Testing it against the pending fix showed the understatement is **EXACTLY INVARIANT** —
359,773,356.74 before and after — and equals `cottonwood.Client + inflection.Client` to the cent.
**A defect named by a coincidence will be re-derived wrong by the next reader.**

## 3. ⭐ THE FINDING THAT NO EXISTING CHECK COULD HAVE MADE

```
                 sum of 3 firms      global as SERVED
  Models         1,803,924,487.20    1,803,924,487.20    EXACT match
  Client           650,200,170.21      290,426,813.47    short by 359,773,356.74
  total_aua                     -    2,094,351,300.67    == global.Client + global.Models EXACTLY
```
⛔ **THE HEADLINE NUMBER RECONCILES WITH THE WRONG VALUE**, because it was computed *from* it. **A
recon predicate PASSES.** That is the first instrument a seat reaches for on a suspected aggregation
bug and it is structurally blind to this class — the estate holds a correct, exercised, 40/40
controlled recon check and this walks straight past it.
⭐ **WHAT DISCRIMINATED IT WAS THE SIBLING FIELD THAT WAS RIGHT.** `Models` matching the 3-firm sum
exactly proves **the aggregator CAN aggregate**, which kills the benign hypothesis — one the
artifact's own `scope_note` actively asserts (*"The global scope carries NO category-views object --
absent, not empty"*, while the object exists and is served). **Hunt the field that works.**

## 4. THE ARTIFACT CONTRADICTS ITSELF ON ITS OWN FACE

`SMA.absent_reason` reads *"A TRUE ZERO -- there are no SMA dollars inside Client for this firm to
extract"* — in an object that lists **six SMA members, every one `served: true`**, with
$22,794,766.25 of SMA sitting inside Client. One template, four scopes, firm name substituted:
correct for cottonwood, inflection and global; **inverted on 49financial.**

## 5. Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-which` | `"what does the gold lambda actually run - deployed package vs source"` | **NEAR-TIE, no fit** — top 3 tied at 1.50 (`comp-aws`, `comp-estate --resource`, `comp-iam service`), none covering deployed-bytes-vs-build-input. **Declared EXCEPTION path taken under Rule 21**, raw `aws` inspection, stated rather than assumed |
| `to-check.py` | `--all --assignee 1.0.0_SA_CTO` (+ `~Z` form) | **0** — and the zero is STRUCTURAL, not a broken lane read: `prompt.md` says *"The CTO does not receive task orders."* Denominator 94 TOs / 40 projects / scanned 2160; **positive control** `0.4.0_DS_ClientPlatform` returns 33 |
| `commit-gate.sh` | on `build_package.py` | PASS, 1 of 1 |

⚠ **`comp-which` was run and returned NO FIT — that is why raw `aws` appears below it.** Recording
the negative result, because a session that skips the rail and one where the rail found nothing look
identical in a log that only lists what ran.

## 6. Blockers

**NONE at this seat.** Two items sit elsewhere by design: the **ship-lift card at Andrew** (carried
by `0.0.0_AB_MSTR~Z`), and the **global-aggregation TO**, held personally by `2.0.0_SA_COO~Z` until
a DS lane is seated — deliberately NOT assigned to an unseated lane, since *naming a seat that does
not exist is how an ARMED item disarms on paper and stays live in fact.*

## 7. Current State (zero prior context)

- **Fabric is 4 seats**: `0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`, `2.0.0_SA_COO~Z`, `3.0.0_SA_CVO~Z`.
  **Tier 2 was deliberately NOT respawned** — Andrew scoped the respawn to Tier 1. Both
  ClientPlatform~Z lanes are gone; `2.0.0_SA_COO~Z` seats 3 replacements (1 AE + 2 DS, two projects
  so Rule 27 forbids one lane) under its own new `@b3f9f207da` authority.
- **`origin/SITEZ = local = 1f6fafa435`** (ls-remote). Merge `1f6fafa435` has parents `51bf6208a5`
  (SITEZ) + `b6410c65d7` (CLOUD) — **a MERGE, not a rebase**. `origin/CLOUD` is now contained in
  SITEZ; **the laptop leg is OUTSTANDING. This is LEG-OUTSTANDING, not parity.**
- ⛔ **BOTH category-views defects are SERVED right now** and every scheduled fire rewrites them.
  The fix for the first is on origin and **not deployed**; the second is unfixed and
  **arithmetically unmoved by shipping the first.**
- **`/mstr-spawn` + `/mstr-kill` are now a COO function ON THIS BRANCH** (merged). The
  `git show origin/CLOUD:...` workaround is retired.
- **The backtick class is at ZERO** — `3.0.0_SA_CVO~Z` closed the census 77/77 with the checker's
  own regexes; `2.0.0_SA_COO~Z` fixed the single survivor (`TO-S1-DE`) as issuer.
- ⚠ **`portal/src/api/endpoints/aum.ts:665-671` is a STALE CARRIER** — states category-views is
  "NOT SERVED YET". It is served. DE lane, unseated, surfaced not chased.

## 8. Next Steps

1. **[ANDREW]** The ship-lift card — now carrying **two** defects, one fixed-not-deployed and one
   unfixed. Plus the still-open Bloomberg field-width call.
2. **[`2.0.0_SA_COO~Z`]** Seat the 3 lanes; cut the global-aggregation TO from a D1_CATVIEWS cell.
3. **[UNOWNED, and it SIZES the second defect]** Does the portal ever pass `'global'` as `firmId` at
   `aum.ts:879`? **UNMEASURED.** The artifact is wrong either way; the render is not known.

## 9. One thing worth carrying

**I found the second defect while establishing COVERAGE for the first.** The SMA question was
answered at 49financial; reading all four scopes was the denominator discipline, not curiosity — and
the extra three scopes are where the $359M sat. ⭐ **The coverage rung is not bookkeeping. It is
where the unasked question gets answered**, and the two seats who had already measured this surface
correctly and independently both stopped at the scope they were asked about.

---

# ⛔ AMENDMENT BLOCK -- appended 2026-08-28 ~17:3xZ by `1.0.0_SA_CTO~Z`

## A1. THE HEADLINE FINDING OF THIS LOG IS RETRACTED. THE MECHANISM WAS MINE AND IT WAS FALSE.

Sections 1, 2, 3, 7 and 9 above assert that `global.Client` **aggregates over ONE of three firms and
understates by $359,773,356.74**. **THAT MECHANISM IS WITHDRAWN.** It is amended here rather than
edited out, per this estate's convention of recording retirements -- and because HOW IT SURVIVED is
worth more than the finding ever was.

**MEASURED ON THE SERVED OBJECT, the full Client node I never opened:**
```
  "predicate":         "unavailable"
  "held_constituents": ["cottonwood"]
  "children":          {}
  "declared_rule":     null
  "aum":               290426813.47
  "predicate_reason":  "global AGGREGATES its constituents and is held while ANY is held.
                        HELD BY: ['cottonwood']. It unholds BY ITSELF when the last constituent
                        clears -- there is no edit to make here"
```
⛔ **THE PRODUCER IS WORKING AS DESIGNED.** `mdpf_gold_consolidator.py:143-160`: `global` has no
entry in `CLIENT_L1_RULE`, the three firm rules "differ IN KIND so there is no obvious composition
into a fourth", `client_l1_split('global')` RAISES deliberately, and global "EMITS BUT ITS CLIENT L1
IS HELD ... unholds BY ITSELF when cottonwood clears." **The served object does exactly that.**

**CORRECTED, and it is smaller and two-sided:** a RESIDUAL `aum` on a node declared `unavailable`
(should be `null`), plus `CategoryCard` gating CHILDREN on the predicate while printing the HEADLINE
unconditionally -- so the page shows a dollar figure above a panel saying that figure is unavailable.
Renderer half GO'd into the R1/R2/R3 batch; producer half is data hygiene at `2.0.0_SA_COO~Z`.

## A2. WHAT SURVIVES, SO THE RETRACTION IS NOT READ WIDER THAN IT IS
- The **49financial SMA defect** stands as found. **The ship decision, the pin choice, the exposure
  sizing (7 files / 2,521 ins; drift 1,381 over 6 modules) and the four-arm acceptance predicate are
  all untouched.** Andrew's ruling is not re-opened.
- **Section 3's structural point stands**: `total_aua` = `Client` + `Models` exactly because it was
  computed FROM that value, so a recon predicate PASSES. A derived total agreeing with its own input
  is arithmetic, not evidence.
- The arithmetic (the gap equals cottonwood+inflection to the cent, invariant under the fix) is REAL.
  **"Understated" is what falls** -- it implies the node purported to be a complete total. It did not.
- ⚠ The exact match to the cent is **UNEXPLAINED and must stay that way.** "Happens to equal" is not
  an explanation of an exact equality, and the producer fix (`aum: null`) ERASES the evidence -- so
  the origin gets recorded before it is nulled.

## A3. ⭐ HOW IT SURVIVED -- THE ONLY PART WORTH CARRYING
**I built a mechanism from TWO numeric fields while the object carried an explicit self-description
three keys away.** Then **four seats corroborated it from three genuinely different instruments
(s3api, the served edge bytes, independent arithmetic) -- and every corroboration was of the
MAGNITUDE, never of the CLAIM the node made about itself.** Nobody read `predicate` for ~40 minutes,
by which time it had reached Andrew, a TO face, an Andrew-direct ruling record, a baseline README's
control set, a signed certificate, and a product card built on it.

⛔ **AND IT SURVIVED BECAUSE IT PREDICTED SOMETHING TRUE.** The gap equalled cottonwood+inflection
exactly and was invariant under the pending fix -- a relation the sloppier "global copies 49f" wording
could not have predicted. A landed prediction is normally strong evidence; here it confirmed only the
coincidence.

>> **SO "CORROBORATION, NOT REPETITION" -- which I invoked FOUR TIMES this session to license
   upgrades -- IS A TEST OF INDEPENDENCE, NOT OF TRUTH.** It certifies two confirmations are not one
   counted twice. It says nothing about whether both sit on the same RUNG. `s3api` and the served
   edge are different instruments that both answer *what is the value*; neither answers *what does
   the node claim about itself*. **Independence and rung-coverage are ORTHOGONAL.**

## A4. THE SECOND-ORDER ERROR, WHICH IS THE WORSE ONE
Having built the wrong mechanism, **I then designed an experiment to CONFIRM it** ("does global.Client
move with the ship?") and **pushed that experiment into a LIVE INSTRUMENT other seats would run** --
`3.0.0_SA_CVO~Z`'s baseline README control set. It was retracted from there at `@f8f1162560`.
**A false premise does not only produce a wrong claim; it produces wrong INSTRUMENTS, and those
outlive the claim because they look like rigour.** `global` is now in NEITHER column of that diff:
recorded, not scored.

## A5. SECTIONS SUPERSEDED BY THIS BLOCK
Section 1 bullet 2 · Section 2 row 1 · Section 3 in full · Section 7 bullet 3's global clause ·
Section 8 item 3 · Section 9's "the extra three scopes are where the $359M sat". **Section 9's actual
claim -- that COVERAGE is where the unasked question gets answered -- still holds: reading all four
scopes IS what surfaced this. It surfaced a real defect and I mis-diagnosed it.**

