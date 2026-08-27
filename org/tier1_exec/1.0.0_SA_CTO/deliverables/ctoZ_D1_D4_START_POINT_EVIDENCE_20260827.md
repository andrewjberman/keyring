# D1 / D4 START POINT — two measured findings

**Author:** `1.0.0_SA_CTO~Z`, 2026-08-27 ~16:4xZ.
**Authority:** Andrew-direct 2026-08-27, VERBATIM: *"let's get this all done so we can have a clear
start point from which to run D1 and D4"* + *"run the 13:30Z acceptance read"*.
**Scope:** two findings that existed only in MCP messages. Both are measured, both carry their
denominators and controls, and both change what the next TO cut should say.

---

# PART 1 — D1: THE 2026-08-26 13:30Z ACCEPTANCE READ

**Provenance of the obligation:** escalated on close-out by the `~N` lane
(`org/tier2_senior/0.4.0_DS_ClientPlatform/logs/2026-08-26/session_close_0825T2324-0826T0308Z_LANE_N_d1catviews_cut.md`,
next-steps item 3, VERBATIM): *"**[`1.0.0_SA_CTO`]** the 2026-08-26 13:30Z scheduled acceptance for
the global repair, and the remaining D1-i-2 hold, both theirs."* Unowned ~27h until now.

## VERDICT: **FAILED at the 08-26 acceptance. SELF-RESOLVED by 08-27.**

Source: the run manifests, `trigger.kind = scheduled` / `detail.source = aws.events` on both —
**production evidence, not an ad-hoc read** (the ad-hoc rule's own distinction).

| | 08-26 13:30:37Z | 08-27 13:31Z |
|---|---|---|
| writes / errors | **8 / 2** | **16 / 0** |
| scopes written | 49financial 3, inflection 3 | **all four × 3** |
| cottonwood | ⛔ absent | ✅ |
| global | ⛔ absent | ✅ |

**THE TWO ERRORS, VERBATIM:**
```
cottonwood: ValueError: no canonical by_model key for Cottonwood model 'Opal Fixed Income'
            -- adding one is a REVIEWED EDIT in build_cottonwood_mdpf_slice.py (auto-slugging
            would silently add a row to the served Global union)

global:     SystemExit: global fold SKIPPED: contributing leg(s) ['cottonwood'] failed this
            cycle -- the ruled composition (I-1 leg pins) requires them; an ineligible fold
            is recorded, never fabricated
```

## WHAT THE READ ESTABLISHES

1. **FINDING 1's REPAIR PASSED.** No `ImportError` on `mdpf_category_registry` — the package loaded
   and wrote 6 objects. `88f687c7a5` did its job. *(Separable from the rest and worth stating alone:
   the lane's own summary was "LOADABLE, not CORRECT", and LOADABLE is confirmed.)*
2. ⛔ **THE GLOBAL REPAIR FAILED ITS ACCEPTANCE, AND NOT ON ITS OWN MERITS.** Global was **skipped**
   because cottonwood aborted. That is **Finding 2's mechanism — *"the `:1190`-before-`:1228`
   ordering that lets ONE scope abort ALL FOUR"* — demonstrated in production.** The lane escalated
   it with `[NOT ESTABLISHED]` intact; **it is now measured, not suspected.**
3. **THE CODE REFUSED TO FABRICATE, AND THAT DESERVES RECORDING AS MUCH AS THE FAILURE.** *"an
   ineligible fold is recorded, never fabricated"* — global declined to serve a firm-wide union
   missing a contributing leg rather than quietly serving three-quarters of a firm. **A pipeline that
   fails loudly beat one that would have served a plausible wrong number.**

## ⛔ THE D1-i-2 HOLD IS **NOT** LIFTED BY THIS READ

Two reasons, both deliberate:
- **WHAT FIXED THE MAPPING IS UNESTABLISHED.** A green run does not distinguish *someone made the
  reviewed edit* from *the input changed shape*. Those take opposite follow-ups.
- **FINDING 2's ORDERING DEFECT IS UNTOUCHED.** The next scope failure aborts the fold again. **The
  hold was against a CLASS; one instance clearing is not the class clearing.**

**Owner of the remaining ruling:** `2.0.0_SA_COO` (Finding 2 — float noise vs real upstream cent,
opposite fixes), plus the **ownerless control** that ruling requires: the lane correctly refused to
build the control validating its own finding.
⚠ **CHECK COO 72259 BEFORE RE-RULING** — a laptop CTO tick log suggests the sole blocker may already
be ruled (*"RECON_TOLERANCE form adopted, control/repair independence split"*). **Unconfirmed; I am
not closing another seat's item on a third seat's log.**

---

# PART 2 — D4: `children[]` DOES NOT ENCODE HOLDS-A

**Provenance:** `3.0.0_SA_CVO~Z`'s certification F1 (P1) named
`rebalancer_model_detail.hierarchy.children[]` as the remedy for the unsatisfiable
`SAT-inv-2` / `SAT-b-2` pair, and **honestly marked it INFERRED**: *"I did NOT verify that children[]
separates the sets. Candidate, not remedy."* **I verified it.**

## VERDICT: **FALSIFIED. The candidate does not work.**

Source: `blackdiamond/cottonwood/bronze/rebalancer_model_detail/2026-08-27/` — **84 detail files,
synced whole, not sampled.** Recursive walk of `hierarchy.children[]`.

```
DENOMINATOR: 121 child nodes across 84 models.  MAX DEPTH REACHED: 1
             (measured, so there is no deeper nesting the sweep missed)
child nodes whose id IS one of the 9 canonical satellite ids: 0
name-based test: all 9 satellites AND all 5 blends -> satellite-children = 0

POSITIVE CONTROL: 18 distinct child ids appear; 18 of 18 resolve to top-level
                  models in the same feed. THE TEST RESOLVES EVERY CHILD IT SEES.
                  It simply never resolves one to a satellite.
```

## WHAT THE BLENDS ACTUALLY HOLD — this is the reframe

`Opal Sat 50+ 15% cash` children, verbatim from the feed:

| child | absoluteAllocation |
|---|---|
| `Opal Intermediate-Term` | 0.50 |
| `Opal Short-Term` | 0.15 |
| `Opal Ultra Short-Term Income` | 0.35 |

**It does not reference `Opal Satellite 50` at all.** It is independently composed from the same
COMPONENT models a satellite is built from.

> ⛔ **SO ANDREW'S CRITERION — *"they merely are allocating to a Satellite"* — IS A BUSINESS
> DESCRIPTION, NOT A STRUCTURAL RELATION PRESENT IN THIS FEED.** The criterion is correct. It is
> **not evaluable against the rebalancer data at any depth**: not on the roster (CVO's finding, the
> page is flat) and not on the detail (this finding). **The blends do not HOLD satellites; they hold
> the satellites' ingredients.**

## CONSEQUENCE FOR THE v1 TO CUT

CVO's framing stands and sharpens: *"v1 had a computable predicate that was wrong; v2 has a correct
criterion that is not yet a predicate, and nine names standing in for it."* With the detail source
eliminated, v1's options are:

- **(a) SHIP THE DECLARED NINE-NAME LIST AS DATA** — named owner, review trigger, and `SAT-inv-2`
  stating on its face that this is a **declared set, not a derived predicate**.
- **(b) find a source outside rebalancer carrying composition.** **UNKNOWN whether one exists — I did
  not look and am not asserting one does.**

**RECOMMENDED: (a) for v1.** `SAT-a-2` already rules the population OPEN by sovereign word; a declared
list with a review trigger is COHERENT with that, and a fake predicate is not. **An honest list beats
a predicate that cannot mean what it claims.** Certifier's call, not mine.

## WHAT I AM NOT CLAIMING

That no structural source exists anywhere — I measured **one feed at one date**.
⚠ **ONE LEAD FOR WHOEVER OWNS THE TO:** `hierarchy.components` was `list[0]` — **empty on every model
read**. An array named `components` that is universally empty, on a composition question, is either
unused or unpopulated, **and those take different remedies.** Worth exactly one look before (a) is
final.

---

## THE PATTERN BOTH HALVES SHARE

**Each finding is a case where a correct-sounding claim had never been run against the thing it was
about.** The acceptance was an obligation nobody executed for 27 hours; the remedy was a candidate
its own author flagged as unverified. **Both took one measurement to settle, and both settled the
opposite way from the comfortable assumption** — the acceptance had failed, and the remedy does not
work. Neither would have announced itself.
