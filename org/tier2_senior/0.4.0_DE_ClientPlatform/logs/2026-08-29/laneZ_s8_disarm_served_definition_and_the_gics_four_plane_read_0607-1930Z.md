# 0.4.0_DE_ClientPlatform~Z -- 2026-08-29 06:07Z to 19:30Z -- S8 FALSIFIED, THE `served` FIELD DEFINED, AND (ii) MEASURED ON ALL FOUR PLANES

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, TRACE

Prior window: `laneZ_andrew_three_edits_shipped_and_the_mixed_basis_finding_0415-0607Z.md`
@`1dba72a301`. Not re-narrated.

---

## Commits

**NONE BY THIS LANE IN THIS WINDOW.** Correct output for a seat whose own item shipped at 06:04Z and
whose remaining work was measurement answering other seats' explicit questions. The one code
artifact touched -- `CategoryViewTree.tsx` -- was read at `origin/PROD`, never edited.

---

## OK: D1_CATVIEWS-S8 RE-OWNED HERE AND DISCHARGED THE SAME TURN

`2.0.0_SA_COO~Z` re-owned S8's code-branch half off a dead lane. **It discharges, and on the
strongest evidence available: the hazard's precondition ALREADY OCCURRED IN PRODUCTION and the
predicted failure DID NOT HAPPEN.**
```
  FILED     "aum.ts:776 returns absent_by_scope for global WITHOUT FETCHING, so if
             category-views is ruled all-scope the panel renders a CONFIDENT, REASONED
             EXPLANATION of why no global tree exists -- forever, and correctly-looking"
  RULED ALL-SCOPE?  registry CATEGORY_VIEWS_SCOPE_SET = "all-scope"; served artifact cites
                    CTO 68692 @c6b5ab4efe retiring the per-firm-only state
  GLOBAL OBJECT?    GET .../global/category-views.json -> 200, real body
  WHAT RENDERED     Models $1.80B . SMAs $22.79M . Client $267.63M -- THE TREE
```
⛔ **THE CITED BRANCH DOES NOT EXIST.** No pre-fetch scope short-circuit anywhere;
`absent_by_scope` is returned ONLY from `if (response.status === 404)`.
⭐ **SO THE COUPLING TO THE PENDING ALL-SCOPE RULING WAS A STALE GATE AND I SAID SO RATHER THAN
INHERITING IT** -- the accessor is ruling-INDEPENDENT by construction, so **no ruling in either
direction can arm this hazard.** `3.0.0_SA_CVO~Z` corroborated with TWO renders on TWO DIFFERENT
BUNDLES (pre- and post-promote), which is the stronger form for a claim whose whole content is
*"forever"*. Recorded @`23d0aa29a8`, ARMED 32 -> 31.
⚠ Second finding, deferred: the file's own disarm note says *"the builder STILL raises on
firm_id='global' (mdpf_category_registry.py:724)"*. **:724 is a crosswalk-keyspace check and
`CATEGORY_VIEWS_SCOPE_SET = "all-scope"` sits in that same file.** A note describing a pre-ruling
world, with a line number that has since come to mean something else.

## OK: THE `served` FIELD -- ANSWERING A QUESTION ITS ASKER DECLARED OUT OF REACH

`3.0.0_SA_CVO~Z` measured `served != (aum is not None)` in **26 of 60 members, in BOTH directions**,
and stated plainly they had NOT read what `served` is defined to mean. Read at source:
```
  mdpf_revamp_model_crosswalk.py:59   served: bool  # in the served by_model{7} for 49F?
                              :49     "gates inclusion in the served by_model projection"
```
>> ⛔ **IT IS A 49FINANCIAL-SCOPED PROJECTION-MEMBERSHIP PREDICATE, EMITTED ON MEMBERS AT EVERY
   SCOPE. So on the global artifact it answers a question about a DIFFERENT FIRM** -- the same
   mixed-basis shape as the Client node, one grain down. <<
⭐ **THE READING EXPLAINS BOTH DIRECTIONS, WHICH IS THE TEST OF IT:** `served=False + aum REAL` =
absent from 49F's projection, funded via other legs; `served=True + aum NULL` = in the projection,
no dollars today. **A reading that explained only one direction would have been wrong.**
⚠ **AND IT IS NOT ONE FIELD:** models get `served=e.served` (DERIVED from the crosswalk); SMA
members get `served=v` (a HAND-DECLARED literal). **Two populations, two provenances, one name** --
Rule 24(iii). Named, not renamed: four seats use the token and the carve_out/additive precedent says
fragmenting a live vocabulary for a latent collision costs more than the collision.
⭐ **`1.0.0_SA_CTO~Z` amended TM1-AC1 within the hour to bind FUNDED == `aum is not None`,
explicitly NOT `served`** -- which would have dropped **$51.9M** of real money. **Same field, same
money, nearly ruled away twice sixteen hours apart.**

## OK: TM1-AC1 -- THE RENDER RUNG ALREADY IMPLEMENTED THE RULING, AND (A) WOULD HAVE MADE IT A DEFECT

Read at `origin/PROD`, not a worktree: `visibleConstituents` gates on
`aum !== null && aum !== undefined` and **has never read `served`.**
>> ⭐ **THE ARGUMENT THE RULING DID NOT HAVE: under (A) -- "every DECLARED L2 node carries a value"
   -- the shipped renderer would be CONCEALING a standing criterion failure, because it
   deliberately hides declared-unfunded nodes. (A) does not merely leave a correct pipeline
   un-accepted; IT MAKES THE CORRECT RENDERER A DEFECT, and the remedy it implies is to delete the
   suppression -- the "rule working perfectly and removing the feature" outcome already ruled
   against.** <<
⛔ **Bounded honestly: the renderer is CONSISTENT with (B); it does not PROVE it.** (B)'s real test
is artifact-side and is not this lane's plane.

## OK: ETFS_INGEST (ii) -- ASSIGNED AS ONE READ, DELIVERED ON TWO PLANES

`2.0.0_SA_COO~Z` measured the DATA plane and routed the render half here explicitly.
```
  DATA      2.0.0_SA_COO~Z   both fields coexist, 180/189 and 188/189        NOT met
  PRODUCER  3.0.0_SA_CVO~Z   parallel axes; re-pointing NULLS non-equity     --
  CODE      this lane        both emitted, ONE cell, cites CTO 11382         NOT met
  PIXEL     this lane        both VISIBLY rendered, stacked                  NOT met
```
⛔ **(ii) IS UNMEETABLE, NOT MERELY UNMET:** `portal-proxy.ts:1031` records CTO ruling 11382 --
*"a PARALLEL field beside sub_asset_class, NEVER a replacement"*. **Satisfying (ii) literally
requires overturning a standing ruling** -- the TM1-AC1 shape again, with a ruling in place of a
business event.
⭐ **AND THE PREMISE IS CONFUSED, WHICH ONLY A SOURCE READ COULD SHOW: BOTH FIELDS ARE GICS.**
`bookSet.ts:464` -- *"our served `sub_asset_class` values are GICS sector NAMES"*; `industry_group`
is the GICS INDUSTRY GROUP, one level finer. **"GICS replaced by sub-categories" is a false
dichotomy: the sub-categories ARE GICS.**
✅ **A THIRD READING IS MET** -- "readable NAMES not raw CODES" (negative control: no raw code field
renders at all). ⛔ **Three readings, three verdicts, and WHICH ONE IS ANDREW'S IS NOT MINE TO RULE.**
⭐ **I CLOSED MY OWN STATED BOUND rather than leaving it conditional.** I had written *"a component
that emits both could still be visually hiding one, and I have not excluded that"*, then ran the
render: `Information Technology` over `Semiconductors & Semiconductor Equipment`, legible.
⭐ **AND THE PIXELS CONFIRMED A PRODUCER PREDICTION TAKEN FOR A DIFFERENT PURPOSE:** *"equity-only by
construction"* predicts non-equity rows carry no second line -- `SALXX` and `CASH` render ONE line
each. **An observation that could not have been steered toward the answer.**

## WARN: FOUR CORRECTIONS OF MY OWN, AND THE WORST WAS BANKED AS DOCTRINE

1. **A BAND FILTER UNDERCOUNTED MY OWN CITATIONS 2.4x** -- `1[456][0-9]{3}` over msg-ids. I reported
   "5 sites"; unfiltered it is **12 across 11 lines**. **An id band is a TIME filter in disguise**
   (ids are monotonic) **and a FORMAT filter's blind spot on top** -- 2 of mine are 6-digit and no
   band any seat used could match them. **Three seats chose a band for the same census in one hour.**
2. **MY PROPOSED REMEDY FAILED ON EXERCISE.** I wrote *"census the citing CONSTRUCTION, leave the
   number unconstrained"*; `2.0.0_SA_COO~Z` ran it: **23,501 -- a 66x OVERCOUNT.** ⛔ **I diagnosed
   a contaminated filter and prescribed a LESS constrained one; removing a constraint cannot ADD
   precision.** ⭐ Their closing finding is the real one: **37 / 353 / 23,501 for one question, a
   635x spread, and NOT ONE DECISION TURNED ON IT.** Stopped.
3. ⛔ **I BANKED AN IMPOSSIBILITY THAT WAS ONE CALL FROM AN ANSWER.** An ack returned *"already
   carried an ACK"* on a message I had just opened. I ran ONE control, found the RECEIPT does not
   discriminate, and wrote into a durable memory *"I cannot distinguish them from my side... no
   evidence any slot was actually stolen."* **`get_delivery_state(16826)` NAMES THE ACKING AGENT.**
   A slot HAD been stolen -- `0.4.0_DS_ClientPlatform~Y` self-reported forging it.
   >> ⛔ **I PROVED ONE INSTRUMENT BLIND AND WROTE IT DOWN AS A PROPERTY OF THE WORLD -- the exact
      class I had diagnosed in a peer FIFTY MINUTES EARLIER** (their `--click` could not reach a
      control; the right flag existed). **A banked NEGATIVE is worse than a wrong positive: a wrong
      claim invites re-measurement, "undecidable" reads as rigour and instructs the next reader not
      to look.** <<
   ⛔ **And the answer was ALREADY IN THE FILE I APPENDED TO** -- a 2026-08-27 section headed *"I WAS
   THE DISPLACED READER"* quoting the same broker string. **An append is the read-free write.**
4. **A DEAD POSITIVE CONTROL nearly made a working probe read broken** -- I controlled a sweep with
   `L1_DISPLAY_RANK`, a token I wrote in CODE and never in a MESSAGE. Re-ran with a phrase I had
   actually sent; only then were the zeros interpretable.

## OK: A MESSAGE ADDRESSED HERE THAT DID NOT FIT, HANDLED WITHOUT A ROUTING CLAIM

16816 credited this lane with an ancestry read on S14/`a239e4a9`. **Measured: this lane sent nothing
after 11:02:03Z, and `a239e4a9` appears in my entire inbox once -- in that message.** ⛔ **I reported
FIT and explicitly did NOT claim misaddressing**, because `3.0.0_SA_CVO~Z`'s own measurement that
morning established the `To:` field is per-recipient and constant (2,435 + my 831, zero listing a
co-recipient) -- **a reader cannot recover the recipient set.** Sender confirmed the second person
meant `2.0.0_SA_COO~Z`.

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `git show origin/PROD:<path>` / `git grep <ref>` | S8 branch, `visibleConstituents`, both GICS fields, with a negative control (`gics_code_raw` -> 0) | PASS -- every code claim read at the SERVED ref, never a worktree |
| `ui-smoke.mjs --origin` | PROD `/portfolios` global, `/positioning` MODELS then ETFs | PASS -- 3 PNGs READ; closed the pixel bound I had declared |
| edge reads (curl + RS256) | global category-views 200; 3 `/auth/login` | PASS -- S8's precondition established |
| `get_delivery_state` | id 16826 | PASS -- **falsified my own banked "cannot distinguish"** |
| source reads | crosswalk `served`, `etf_positioning_gold`, `MODE_LABELS` | PASS -- definitions, not inferences |

**What worked:** **answering the exact question another seat declared out of reach.** Twice --
`served`'s definition and the (ii) render half -- both were one source read, and both were left open
only because the asking seat correctly refused to guess.
**What failed:** ⛔ **`--clicktext ETFS` -> CLICKTEXT-FAIL.** The button reads `ETFS` on screen and is
`'ETFs'` in the DOM -- `className="... uppercase ..."`. **A second live instance of the CSS-transform
trap I had named for another seat two hours earlier, walked into by me.** I did NOT conclude the
toggle was unreachable; I read `MODE_LABELS` and clicked the real string.
**Gap found:** the estate's citation-hygiene census (`.md`/`.json` under `org/` + `docs/`) is blind to
source comments -- `portal/src/**` and `data/**/*.py` carry the same citations and outlive them.

---

## Blockers

**None at this lane.** Nothing owed, nothing waiting on me.

---

## Current State (written for zero prior context)

Andrew's three panel edits are LIVE and VERIFIED on PROD (`fc3a4421`, v2.1.173, 9 PASS / 0 FAIL / 0
UNSCORED by `3.0.0_SA_CVO~Z`). `D1_CATVIEWS-S8` CLOSED as FALSIFIED-BY-EVENTS. `TM1-AC1` needs no
render change. `ETFS_INGEST` (ii) is measured on all four planes and is a SOVEREIGN reading question,
not an engineering gap.

**THREE PRODUCT CALLS SIT AT ANDREW, and NO scheduled fire lifts any of them:** the footer source
line (`Source: Opal Capital Analysis.`), the Primary/Custom colour swap, and the I2 fork -- whether
global's `Client` aggregates all three firms or stays 49F-only with disclosure.

**Deferred, comment-only, to ride the next substantive edit:** THREE items now queued on
`aum.ts` from THREE seats (stale disarm note, the `absent_by_scope` name residue, per-recipient
msg-ids) -- **recorded together so they land in ONE touch, which no single seat could see.**

---

## Next Steps

- [Andrew] The three product calls. Sovereign-gated, not clock-gated.
- [`1.0.0_SA_CTO~Z`] Which reading of `ETFS_INGEST` (ii) is Andrew's -- the literal one requires
  overturning ruling 11382 and nulling every non-equity row.
- [this seat] Nothing outstanding. Available on measurement.
