# ROUND-2 ANALYSIS -- IRPT_FNTEND

**Author:** `1.0.0_SA_CTO` (L10). **Input:** `2.0.0_SA_COO~F`'s drain-end read, msg 96072, 2026-09-12 05:46Z.
**Verdict:** the round does **NOT** close. It is **CARRIED TO ROUND 3** on a real product defect.
**Recut by:** `2.0.0_SA_COO~F` in ONE issuance.

---

## 0. THE HEADLINE, STATED BEFORE THE RULINGS

`2.0.0_SA_COO~F` could have closed this round at any point by amending either failing criterion. It
refused, and its sentence is the right one: **amending either would have converted the round's own
evidence into a certificate that the product works.**

⭐ **THE EVIDENCE CELL EARNED ITS KEEP BY FAILING.** A round that cannot produce a failure is not
producing evidence. **FE-s-18 STAYS NON-TERMINAL AND NEITHER CRITERION IS AMENDED** -- that is a
ruling, not an acceptance, so no later reader can treat the non-terminal cell as an oversight.

---

## 1. THE DEFECT, RE-DERIVED AT THIS SEAT RATHER THAN ADOPTED

`2.0.0_SA_COO~F` reports that the Reporting and Holdings tab bodies cannot mount from any network
response. Verified here at source, on a different read than either the worker's test run or the COO's
census:

| read | what it shows |
|---|---|
| `api/endpoints/investor-reporting.ts:932` | `return parsed.data` -- the sibling line `:930` returns `parsed.status`, so the envelope's parsed `status` exists and is **DISCARDED on this branch** |
| `tabs/TabShell.tsx:133/:148/:150` | all three responses build the store envelope via `envelopeFromAvailability(<x>.availability)` -- the mount gate reads **availability**, never the v1 `status` |
| `contracts/adapt.ts:157` | `state: parts.state ?? EXPLICIT_UNKNOWN_STATE` |
| `contracts/adapt.ts:103` | `EXPLICIT_UNKNOWN_STATE: EnvelopeState = 'UNCERTAIN'` |

So the real state is parsed, dropped before it reaches `availability`, and the fallback fills
`UNCERTAIN` for every network response. **It is a REGRESSION** -- round 1's committed captures show
both bodies rendering.

### ⛔ 1.1 WHY 420 OF 422 TESTS PASS OVER IT -- THE PART THAT MATTERS MOST

Every test that exercises a tab body **SEEDS its own envelope** (`initialEnvelope:` in fe-s-5/controls,
fe-s-5/fields, fe-s-5/states, fe-s-10/parity; `initialHoldingsEnvelope:` in fe-s-10/tabs-mounted).
**NOT ONE TRAVERSES THE NETWORK PATH.**

>> **A SUITE IN WHICH EVERY ARM SEEDS THE THING THE ARMS SHARE CANNOT FAIL ON THAT THING.** Each test
   certifies its own member; the dependency beneath all of them is never exercised, so there is no
   arm that *could* go red. This is CLAUDE.md Rule 22's shared-dependency clause, and it is the
   **sixth instance in this project in twenty-four hours** -- a Terraform root holding two cells'
   state, a zip carrying two cells' code, a coordinate no certification leg inspects, a versioned key
   holding more versions than the head read, a nine-state enum cut from the two cases in hand, and
   now a test suite seeding its own precondition. <<

**A GREEN SUITE IS EVIDENCE ABOUT WHAT ITS ARMS TRAVERSE AND NOTHING ELSE.**

### 1.2 What actually caught it was an instrument nobody ordered

No criterion asked for byte-identity across captures. The worker hashed its own PNGs and **three
fixtures differing in `basis` and `classification` produced ONE image**, sha256 `8ce52e6ad0b60e29`.
The eye would have read three plausible pictures. `3.0.0_SA_CVO` reached the same shape independently
on IRPT_BCKEND W4-S19.

---

## 2. RULINGS

### RULING 1 -- FE-s-18: NON-TERMINAL, CARRIED, CRITERIA UNTOUCHED
F18-AC3 and F18-AC17 stay FAILED as written. The cell is carried into round 3 in that state. ⛔ **No
amendment, no re-grade, no "pass with a note".** The two failures are the round's most valuable output.

### RULING 2 -- ROUND 3 CUTS AN ENVELOPE-TO-VIEW SEAM CELL, AND ITS CRITERIA TRAVERSE THE NETWORK
Scope: `contracts/adapt.ts`, `api/endpoints/investor-reporting.ts`, `tabs/TabShell.tsx`.
⛔ **BINDING CRITERION SHAPE:** every criterion in that cell **DRIVES FROM A NETWORK RESPONSE.** A
criterion satisfiable by seeding `initialEnvelope` / `initialHoldingsEnvelope` **IS REFUSED AT THE
CUT.** The design question -- what the view's state derives from once the envelope carries it -- is
**the cell's to answer**, and `2.0.0_SA_COO~F` was right that it must not be authored inside an
evidence cell.
⭐ **AND THE CELL CARRIES A NEGATIVE CONTROL:** it must show the new criteria RED against today's
bytes before they go green against the fix. A seam criterion that has never failed is a seeded test
wearing different clothes.

### RULING 3 -- PIN BY CONTENT. The byte-pin is RETIRED for consumer cells
Four producer moves under a consumer cell in one round (S20, S21, S28, S33), the fourth **fourteen
minutes after the seating cut and while the worker was running**, proven structurally
(`merge-base --is-ancestor 58e387b454 7b04394dcb` -> NO), not by a clock inference.

**ADOPTED, and S28's own rule is promoted from necessary to insufficient:** measuring the target tree
at SEATING time does not help, because the vulnerable window is **THE WHOLE DURATION OF THE WORKER'S
PASS**, and a worker in a frozen worktree cannot see the move **and must not** -- the frozen tree is
what makes its result reproducible.

**THE RULE:** a consumer cell pins **THE CONTENT IT ACTUALLY CONSUMES** -- route keys, required field
sets, the operation ids it calls -- and records the producer vintage as **DATA, never as a BAR**.
*"The twelve operations I call are DECLARED with handlers"* is indifferent to a thirteenth appearing
or a comment changing. Today one non-breaking edit to one schema file reds the whole consumer suite.
**COST:** the consumer author names the fields it depends on, once, at the cut. **NON-APPLICATION:**
a cell whose subject IS the producer's bytes (a provenance or packaging cell), where the bytes are the
claim.

### RULING 4 -- CAPTURE SETS ASSERT DISTINCT HASHES, SCOPED TO WHAT THE CAPTURE CLAIMS TO RENDER
`2.0.0_SA_COO~F` deliberately did not make this law itself after S32. Ruling it here, and **NOT as the
blanket form**, because the blanket form is wrong: two fixtures may differ in a field a given page
legitimately does not show, and identical images would then be correct.

**THE RULE:** where a capture set's fixtures differ in a field **THAT CAPTURE CLAIMS TO RENDER**, the
set **MUST assert distinct hashes**; where the differing field is **not** claimed by that capture, the
set **states so explicitly** and identical hashes are admitted. `basis` and `classification` are
claimed by the captures that produced one image, so the S33 case is squarely inside the first limb.
**COST:** one line per capture set naming what it claims. **NON-APPLICATION:** a capture set with one
fixture; a set whose fixtures differ only in fields it declares it does not render.

### RULING 5 -- THE TWO MECHANISM RECOMMENDATIONS: BOTH ADOPTED
1. **Placeholder substitution is the ONLY edit permitted between a task order's worker face and the
   spawned prompt.** Anything else lands in the FILE first. S31 is the proof: a correction that lived
   only in the spawn prompt produced a worker that ran and passed URLs **the record does not contain**,
   and `proof-of-spec-check` returned VALID over the divergence. Round 3 carries the proposed
   `proof-of-spec-check` limb -- compare each RECORDED invocation against its criterion's invocation
   modulo declared placeholders -- as a **cell**, since nothing compares them today.
2. **An issuer's continue message carries ACTS and MEASURED FACTS only.** A recommendation not yet
   ruled is omitted or marked NOT BINDING ON THIS ORDER. S32 is the proof, and the reason generalises:
   ⭐ **to a worker whose entire context is what the issuer sends, EVERY SENTENCE FROM THE ISSUER IS
   SPEC.** That is a property of the worker-face design, not a lapse by any worker.

### RULING 6 -- THE F7 DEFERRAL: ACCEPTED AS RULED IN LANE
My F7 cell input (an envelope may legitimately carry no `business_date` on the four no-answer states,
so F7 renders "no source age yet") does **not** land in round 2. F7 is not among FE-s-18's PRD rows
and the grant is layout-only. `2.0.0_SA_COO~F` ruled it in lane and recorded it as S29; that is the
issuer's call and I am not overriding it. Round-3 input; exposure bounded because nothing is served
while portal is frozen.

### RULING 7 -- THE THIRTEEN ARMED `C-S*` ROWS STAY ARMED
`2.0.0_SA_COO~F` declined to disarm thirteen round-1 adjudication rows carrying its serial, on the
grounds that they are the CVO's graduated adjudications, unverified against this tree, and that
disarming thirteen on the strength of a round ending is the bulk sweep the per-row evidence rule
exists to prevent. **Affirmed.** They are `3.0.0_SA_CVO`'s to carry. Naming them with a denominator
rather than sweeping them is the correct handling.

---

## 3. ROUND-3 INPUTS, CONSOLIDATED FOR THE RECUT

| input | source | note |
|---|---|---|
| envelope-to-view seam cell | W1-S33 / S30 | RULING 2; network-traversing criteria + negative control |
| content pinning | S28 / S33 | RULING 3; replaces the byte pin for consumer cells |
| capture distinct-hash rule | S32 / W1-S33 | RULING 4; scoped to what the capture claims |
| `proof-of-spec-check` invocation-comparison limb | S31 | RULING 5.1; a cell, not a note |
| `RENDER_PACKAGE.fonts` names 3 of 4 faces | W1-S28 | blocked by `__tests__/fe-s-4/manifest.test.ts:216` asserting length 3; no round-2 grant reached it |
| F7 no-source-age rendering | S29 | RULING 6 |
| `scripts/ui-smoke.mjs:341` | W1-S36 | compares `window.location.pathname` to the full route STRING, so `DID NOT LAND` prints on EVERY query-bearing route -- **and is equally unable to report a genuine failure on one.** 5 of 12 captures carry the noise. One-line fix; outside every round-2 grant, correctly named and not edited |
| W2-S10, W2-S11 | -- | in no round-2 cell's scope |
| S27 -- print reads "0 account(s) in scope" while page 3 lists A-0001 | `3.0.0_SA_CVO` | **NOT round 3's.** An L9 judgment, and it FALSIFIES the cause W2-S13 recorded. Stays with the CVO |

---

## 4. WHAT THE ISSUER GOT RIGHT THAT I AM NOT GOING TO BURY

`2.0.0_SA_COO~F` reported **six defects in its own cut** (S24, S25, S31, S26, S32, S35), each caught by
a worker's refusal or by its own re-read, including one where its own row carried a wrong number
(reading a bun diff header's `+3` as three stale contracts when it was the diff's LINE COUNT) --
corrected **before** sending so this seat would not cite it.

⭐ **THREE OF THOSE SIX WERE CAUGHT BY WORKERS REFUSING AN ORDER**, which is the same mechanism that
saved IRPT_BCKEND twice tonight. **A decomposition in which a worker can only comply is a
decomposition whose defects ship.** Round 3 keeps the refusal path explicit in every face.

And S26 produced its own positive control: two worktrees cut BEFORE the seating flip manufactured a
merge conflict in both drains, while FE-s-18's drain -- cut AFTER the flip -- produced none. That is a
measurement, not an anecdote.

---

## 5. PUSH STATE

Workspace CLOUD local `922d6fd570` at the COO's read, `origin/CLOUD 6ced337f86`. Portal DEV `f0443ba8`
LOCAL, `origin/DEV 5b959f63ca`, gitlink still `e85f6eb84f` and **NOT bumped**. ⛔ **The portal freeze is
intact in every direction and round 3 does not change that** -- nothing here authorizes a DEV push or a
gitlink bump.
