# 0.4.0_DE_ClientPlatform~Z -- 2026-08-28 22:35-23:00Z -- THE PIXEL RUNG ON PROD, AND FOUR CRITERIA CAUGHT

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE, SCRIBE

**DELTA LOG.** Prior windows are logged at `laneZ_d3d4_render_defects_2130-2230Z.md` @`d1a970af35`
and `laneZ_promote_marker_set_2220-2235Z.md` @`bbfbbe96f7`; neither is re-narrated here. This window
is the production verification plus four criterion defects, and it is written to a FILE because the
whole of it currently exists only in mail -- `1.0.0_SA_CTO~Z` 14461 s.2: *"a broadcast reaches
whoever is live now; a deliverable reaches whoever comes next."*

---

## Commits

**None.** No code written this window and none was wanted -- `2.0.0_SA_COO~Z` 14424 s.1 did not seat
this lane on increment 2. Prior commits: `db3df0b2` (portal DEV, **ON origin/DEV**, is-ancestor with
a positive control), `d1a970af35` (**origin/SITEZ tip**), `bbfbbe96f7` (**LOCAL**).

---

## OK: THE PIXEL RUNG -- TAKEN BECAUSE IT WAS EXPLICITLY LEFT UNCLAIMED

`1.0.0_SA_CTO~Z` 14395 s.4: *"NOT CLAIMED BY ME: the visual render. I verified the DATA the page
consumes, through the page's own route. Whoever runs the pixel check owns that rung."* This lane had
offered it twice (14343 s.4, 14380 s.5). The promote landed, so it was taken.

Real RS256 bearer minted from PROD `/auth/login` (`sub=michael@opalinvest.com`, exp 22:51:46Z),
rendered `https://opalinvest.dev/portfolios`, **screenshots READ**. A default-stub render is the
FAILURE state; this was not one, and it certifies its own plane -- `$2.09B` Total AUA, 8,265 holdings
and the real per-firm bases are values only the authenticated route returns.

```
  GLOBAL       Models $1.80B . SMAs $22.79M . Client (no fee box, not an empty card)
  MODELS > CUSTOM, real data:
      50/50 INT/LTC  $36.17M  teal        <- alias resolved via getCanonicalModelName
      50/50 ST/INT    $7.30M  chartreuse
      Fixed Income    $8.43M  PURPLE      <- and it MATCHES the AUA Trend legend on the
                                             SAME page. The cross-panel consistency Andrew
                                             asked for, visible in one screenshot.
  49FINANCIAL  Models $1.47B . SMAs $22.79M . Client $267.63M
                                             > Client - Opal Supervised $267.63M
```
**All four of Andrew's defects confirmed on the production page.** D-1 resolved with **zero render
change**, exactly as the reclassification predicted: three rows, three figures, **no `--` anywhere**,
and they reconcile to the parent on screen ($36.17 + $7.30 + $8.43 = $51.90M).

**`3.0.0_SA_CVO~Z` RATIFIED @`a16e317b9e`** (AC1/AC2/AC3/AC5) and cited this render. It then named the
**49financial render** as one of three things NOT ratified; this lane rendered it, closing that gap.

## OK: TS1-AC2 -- PASS AT THE LIVE EDGE, WITH THE GATE NAMED

```
  scorer --from-edge https://opalinvest.dev   (bearer via PORTAL_BEARER env, not argv)
  [cottonwood]  written_at 2026-08-28T22:17:55Z (the reland's publish)  freshness OK
                Opal Fixed Income  state=VALUE  -> RENDERS at gate G5
  [inflection]  state=NULL                      -> ABSENT  at gate G5
                "suppressed by the L2 sibling guard while 2 of 4 siblings carry a mapped
                 value -- this is Andrew's rule firing"
  RESULT: PASS, both directions, absence ON-RULE at G5
```
Andrew's own worked case, both directions, on production. **The absence is proven BY NAMING THE GATE**
-- the distinction the amended AC2 exists to enforce.
⚠ Does **NOT** discharge `TS1-AC3`: that needs a matched rendered BEFORE/AFTER and my pre-reland
render was against a FIXTURE, a different plane. Not claimed.

## WARN: FOUR CRITERION DEFECTS THIS WINDOW, AND THE PATTERN IS THE POINT

1. **`CATV-TOF1-AC2`, verified in production.** The null member is ABSENT and zero dashes remain --
   so the amended form passes **and the original would have scored this correct, Andrew-ruled page as
   FAILED**, on the same pixels.
2. **My own promote marker died.** I measured OLD=`origin/DEV` tip; a promote's BEFORE is what PROD
   SERVES (`2858e7f5ff`). The string went `0 -> 1 -> 0` inside the DEV gap and never reached PROD, so
   its pass condition was already met un-promoted. Caught by `3.0.0_SA_CVO~Z` running my own
   mandatory-control demand against the live bytes. **Replacement found against the correct referent:
   `"Net Worth - Accounts"` `0 -> 1`, a real `PanelHeader title` needing no minification inference --
   but it proves THE PROMOTE shipped, not that D-4 shipped, and I flagged that conflation.**
3. **`AC-REMOVAL` struck** (`1.0.0_SA_CTO~Z` 14468) on this lane's 14466. *"One fewer branch than
   before"* had **no pinned BEFORE**, and anchored to my 14432 it was **unsatisfiable** -- a correct
   build scores FAIL. AC-DERIVATION already is the removal check: absent tokens with a working
   positive control satisfy the ruling whether the branch was deleted or never written.
4. **`AC-NON-FLATTENING`'s render half, measured and SPLIT** (for `3.0.0_SA_CVO~Z` 14451 s.2):
```
  AXIS HALF   COMPLIANT BY CONSTRUCTION -- reads `children` (one axis), never draws `held_axes`
  LABEL HALF  NOT synthesized (:183 renders the block's label verbatim) BUT WIDTH-DEPENDENT:
              `truncate` at :399 / :267 is CSS ellipsis and can clip the perspective word.
              DID NOT FIRE at 1440px on the 49F PROD render. LATENT, not observed.
  THE NEGATIVE TEST: narrow viewport + all three labelled buckets; REFUSE on any ellipsized label.
```

## WARN: I RAISED A CONCERN AND WITHDREW IT ON THE SOVEREIGN ANSWER

I flagged (14435) that 49F's page makes an exhaustive claim -- the single visible row EQUALS its
parent, so the page asserts Client is *entirely* Opal-Supervised. **Andrew ruling (a) makes that claim
CORRECT** (*"49F just counts the 0824 account and that whole thing is supervised"*). Withdrawn
explicitly so it does not sit in the record as doubt about a correct page.
⚠ Carrying `1.0.0_SA_CTO~Z`'s qualifier rather than dropping it: the `0824`/`0833` -> Schwab-code
mapping is **UNVERIFIED**. The withdrawal rests on the RULING, not on that mapping.

## WARN: TWO OFFICES ASSERTED THIS SEAT'S STATE WITHOUT CHECKING

14441 and 14446 described this lane as *"mid-work"* / *"mid-write"* on CATV2-a and instructed it to
delete a firm-lens leg from *"your two writes plan"*. **None of it was true** -- not seated, zero code
since `db3df0b2`, and 14432 was a fact about the render gate addressed TO the seated executor, naming
no artifact or lens. Corrected in 14454; **both offices corrected themselves in writing**
(`1.0.0_SA_CTO~Z` 14461 s.3, `3.0.0_SA_CVO~Z` 14457 s.4). Recorded because a stated fact about another
seat's state is unverifiable by its readers and gets believed -- **and because a bar aimed at the
wrong lane can leave the real executor un-barred.**

---

## Compiler Tools

| tool | invocation | result |
|---|---|---|
| `ui-smoke.mjs` | `portfolios --origin https://opalinvest.dev --token @<jwt> [--clicktext Custom \| --select 49financial]` | PASS -- 3 PROD renders, all READ |
| scorer `--from-edge` | `D1_CATVIEWS.TS1-AC2_score_served_render.py --from-edge https://opalinvest.dev` (bearer via env) | PASS -- both directions, gate named |
| `git grep -c` | `-F <tok> {2858e7f5ff,4dde6df344,db3df0b2} -- src` | PASS -- found the replacement marker; **also the instrument that MISLED me: it counts FILES, not occurrences** |
| `comp-find` | `'AC-REMOVAL' --corpus raw`, **both pages read (25+17=42 of 42)** | PASS -- never reached a TO face/decomp/proof-of-spec |

**What worked:** running the bearer through `PORTAL_BEARER` rather than argv (keeps a live credential
out of process lists and transcripts); reading BOTH comp-find pages rather than concluding from page 1.
**What failed:** `--bearer "@file"` is not supported by the scorer -- it passed the literal `@path` and
returned 401. Read the arg parser instead of guessing a second time.
**Gap found:** `comp-find` searches the WORKTREE and structurally cannot read a non-checked-out commit,
so a two-vintage question needs `git grep`. That deviation from Rule 21's default is stated at the call
site (14380 s.4) rather than left for a reader to notice.
⚠ **A denominator caveat worth carrying:** `org/mcp/comp-which-rail.log` logged my own AC-REMOVAL search
*as it ran*, so that search is a hit for itself. The corpus records its own tests; a re-run returns a
higher count for a reason that has nothing to do with the estate changing.

---

## Blockers

**None at this lane.** Increment 2's remaining items are blocked UPSTREAM and none is mine
(`2.0.0_SA_COO~Z` 14499 s.3-4): item 1 on the cot Rebalancer STOP, item 3 on a sovereign scope call
plus an unscheduled bronze plus a `tax`-vs-`muni` attribution gap. **All routed to Andrew by the COO.**

---

## Current State (written for zero prior context)

**The product is live and verified on the pixel plane.** `D1_CATVIEWS.TO-F1-DE` is closed at this seat
-- AC3 + AC4 PASS, AC1 N/A (struck on this lane's 60/60 measurement), AC2 and AC5 UNCOMPUTABLE for
stated reasons. Instance at
`org/tier2_senior/0.4.0_DE_ClientPlatform/deliverables/D1_CATVIEWS.TO-F1-DE_PROOF_OF_SPEC.json`,
`proof-of-spec-check` **VALID, 0 violations**, coverage 5/5.
The `$22,794,766.25` that was being shown to advisors as an affirmative "TRUE ZERO" is a visible card
on the production page. **NOT proven:** the SCHEDULED pipeline -- Monday 2026-08-31's 13:30Z fire is
the only thing that settles it, and it must be scored STRUCTURALLY (the literal is market-valued).

---

## Next Steps

- [`0.0.0_AB_MSTR~Z`] Push leg for `bbfbbe96f7` + this log; earlier commits are already on origin.
- [`2.0.0_SA_COO~Z`] The AC5 headline word -- **and item 1 may dissolve the question entirely**, since
  a predicate-available Client card renders like 49F's already does. Urgency withdrawn, not the reasoning.
- [`1.0.0_SA_CTO~Z`] Surprise S1 go/no-go (`IDVZ`/`PFDE` both `#f43f5e` in one card). Still ARMED.
- [`0.4.0_DS_ClientPlatform~Z`] When item 1 unblocks: `CategoryViewTree:312` runs the predicate gate
  BEFORE reading children, so populating children without flipping the predicate ships an invisible
  tree. Routed as 14432.
- [this seat] Available for the render half of any increment-2 item **when a measurement says one is
  needed** -- not because rows look empty.
