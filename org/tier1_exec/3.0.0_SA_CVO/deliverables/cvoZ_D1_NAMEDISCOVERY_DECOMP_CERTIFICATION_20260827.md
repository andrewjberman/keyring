# CERTIFICATION — `D1_NAMEDISCOVERY` STAGE-3 ATOM DECOMP v1

**Certifier:** `3.0.0_SA_CVO~Z` (named certifier on the artifact's own face; alternate base
`1.0.0_SA_CTO`, who DECLINED to execute the alternate because this seat was live)
**Artifact:** `workflows/atom_decomposition/runs/d1-namediscovery/20260826T214534Z/DECOMP.md`
**Read at:** `origin/SITEZ` @ `7805c21c12` · artifact authored @ `bcca23915b` (`2.0.0_SA_COO`,
2026-08-26T21:48:02Z)
**Date:** 2026-08-27 ~17:1xZ

---

## VERDICT: **CERTIFIED WITH FINDINGS.**

The decomp is well-formed. Its denominators reproduce exactly under an independent instrument, every
cited commit resolves, and its boundary section does real work — it correctly absorbed a sovereign
word that landed 11 minutes after authoring. **Four findings, none blocking.** No TO-mint block.

---

## 1. VINTAGE GUARD — and the negative control is the half that matters

```
artifact commit history            bcca23915b  -- ONE commit. NEVER amended.
git diff origin/SITEZ -- <path>    EMPTY  (tree copy byte-identical to the remote)
is-ancestor bcca23915b origin/SITEZ        -> YES
is-ancestor 0aa94d07e0 origin/SITEZ        -> NO      <== THE CONTROL (origin/CLOUD head)
```

**The fourth line is why the first three are admissible.** Without an arm that CAN return NO, three
`ancestor` results are equally consistent with a test that always says yes. `origin/CLOUD`'s head is a
real, known-absent commit — SITEZ lacks 28 CLOUD-only commits — so the control is live, not contrived.

This artifact is **structurally easier to certify than D4's**: D4 moved twice mid-certification;
this one has a single commit and no amendments.

## 2. MECHANICAL CENSUS — reproduced EXACTLY, member-for-member

Instrument: word-boundary **case-insensitive** regex id census over the file bytes, counting DISTINCT
ids and printing each section's members (not just a total), so a missing or extra member is visible.

| section | claimed (line 126) | measured | members |
|---|---|---|---|
| a | 3 | **3** | 1,2,3 |
| b | 2 | **2** | 1,2 |
| c | 3 | **3** | 1,2,3 |
| d | 2 | **2** | 1,2 |
| e | 2 | **2** | 1,2 |
| f | 1 | **1** | 1 |
| inv | 3 | **3** | 1,2,3 |
| g | 4 | **4** | 1,2,3,4 |
| **TOTAL** | **20** | **20** | 26 raw occurrences -> 20 distinct |

**Criterion-bearing: claimed 16, measured 20 − 4(`g`) = 16. CONFIRMED.**

The author's line 128 discloses that this line first read 18/14 and was corrected before commit by a
mechanical census. **That disclosure is itself correct** — I reproduce the corrected figures, not the
withdrawn ones.

**Cited commits — all four resolve AND are ancestors of `origin/SITEZ`:**
`e9990032fe` (project registration) · `958c8e4487` (PRD v2) · `862b6bf35c` ("recs approved") ·
`4b6503cdbd` (18:06Z grain addendum). Negative control: a fabricated hash does not resolve.

**Line 131 (`Criteria: 0 — NOT-YET-EVALUABLE. NO TO IS CUT`) is TRUE as of this reading**, measured on
two instruments: `to-check.py --all` (no `D1_NAMEDISCOVERY` row) and a filesystem sweep of task-order
files. The decomp's own warning that this line becomes false the moment a TO is cut stands, and the
amendment obligation it assigns to whoever cuts round 1 is correct.

---

## 3. FINDINGS

### F1 (P1) — R-n1's ME claim holds only under EXACT whole-string matching, and the decomp mandates a FUZZY matcher

R-n1 asserts *"ME by construction (the four are syntactically disjoint)."* Under exact whole-string
comparison that is true. But **`ND-c-2` mandates fuzzy matching at discovery BY RULING**, and
**`ND-d-1` requires the surfaced provenance to name WHICH FORM the candidate matched.**

Under a fuzzy/substring matcher the string `Opal DIVZ SMA` satisfies **all four** named forms at once
(`bare`, `<token> SMA`, `Opal <token>`, `Opal <token> SMA`). **So the axis the output is required to
report on is not disjoint under the matcher the decomp requires.** The postulate and the mechanism
disagree about the same axis.

Measured: the file contains **no** precedence, tie-break, longest-match, most-specific, or
disambiguation language anywhere. *Positive control: the same grep for `disjoint` returns 1 — the
engine and the file are fine, so the zero is a real absence, not a broken matcher.*

**Consequence:** `ND-d-1`'s `which form` field is ambiguous by construction for exactly the **most
specific and most informative** form — the one a consumer would most want to branch on.

**REMEDY (author's act):** state a form-resolution rule — most-specific-wins is the natural one —
inside R-n1's postulate (i) or as a clause on `ND-d-1`. ⛔ **This does NOT re-open the CE/openness
ruling.** It is about ME among the four NAMED forms only; the fifth open value is untouched.
**Owner:** `2.0.0_SA_COO~Z` (author).

### F2 (P1) — `ND-c-3` names ONE registry; the estate holds at least two more resolution surfaces over the same name space, with OPPOSITE absence policies

`ND-c-3` prohibits resolving a match against the `strategy_id` registry and reading absence as a
negative. That cell is correct and load-bearing. But the same model/sleeve name space is resolved by
at least two other LIVE surfaces:

| surface | keyed on | absence policy |
|---|---|---|
| `data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` @`2d5f8a7f74` (ancestor of `origin/SITEZ`) | `model_id` | **RAISES** on unrecognized, by design (its own F5 rule, set by a prior CVO finding) |
| `portal/src/lib/modelPortfolioColors.ts:189` | **label** | display alias map |
| `strategy_id` registry (the one `ND-c-3` names) | — | absence ≠ negative, by ruling |

**A design that resolves against either of the first two and reads absence as a negative violates
`ND-c-3`'s PRINCIPLE while passing its LETTER**, because the letter names only `strategy_id`.

This is the class `ND-e-2` already anticipates (*"the slice RAISES, the fold SKIPS"*) — but `ND-e-2`
names two different producers, and **neither of them is the crosswalk**, which is the load-bearing
name-resolution artifact in this estate.

**REMEDY:** `ND-c-3` names the CLASS — *any name-resolution surface over the model/sleeve name space* —
rather than one registry; and `ND-e-2`'s enumeration carries the crosswalk's raise policy as a third
live answer already in the estate. **Owner:** `2.0.0_SA_COO~Z` (author).

### F3 (P1) — a live, production-documented LABEL-COLLISION specimen exists for one of the six tokens, and the decomp does not name it. **This is D1's `Opal Satellite 60`.**

`mdpf_revamp_model_crosswalk.py:99-101` records — **in the data plane, not only the docstring**:

> SmartX labels model `843d875b-62f7-4ef8-b833-5078a3f637d5` **"Pathfinder Focused Opportunities"** —
> that is the **PFOE ETF's fund name** — but the model **is** the Opal Equity Growth SMA
> (`opal_growth_sma`, shortName `OpGEGTR000`). *"Resolved by model_id, so the trap never fires."*

**`PFOE` is one of `ND-a-1`'s six tokens.** The crosswalk is immune **because it keys on `model_id`.**
**D1's mechanism is LABEL-based by ruling.** So D1's matcher is exposed to precisely the trap a
production artifact documents and defends against — and the decomp names neither the trap nor the
artifact. Token census against the crosswalk: `PFOE` 2 occurrences; the other five tokens 0
(control: a fabricated token returns 0, so the counter can return zero).

⛔ **NOT P0, and the reason matters:** `ND-inv-2` (discovery never classifies) and `ND-d-1` (provenance
field) **structurally prevent this from becoming a wrong classification** — the mechanism would
surface a PFOE candidate *with its provenance and what was not confirmed*, which is the correct
behaviour. **The gap is a missing FIXTURE, not a broken invariant.** The invariants hold; that is a
point in the decomp's favour, not against it.

**REMEDY:** name `843d875b` / "Pathfinder Focused Opportunities" as the specimen for `ND-c-2`'s and
`ND-d-1`'s oracles — **the exact role `Opal Satellite 60` plays for D4's `SAT-a-2` resolution path.**
A real, live, already-documented collision is worth more than a synthetic fixture.
**Owner:** `2.0.0_SA_COO~Z` (author).

### F4 (P2) — header staleness. Independently re-derived. Header-only, no cell consequence.

Line 5 reads `placement LAPTOP`. **Superseded** by
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260826_2352Z_PLACEMENT_MAP_D8_AND_MP_TO_SITEZ.md`
@`0a96a52989`, committed **2026-08-26T23:56:26Z — 2h08m AFTER** the decomp @`bcca23915b`
(2026-08-26T21:48:02Z). **D1 IS SITEZ.**

`1.0.0_SA_CTO~Z` handed this over as a completed read and explicitly instructed that it be treated as
**a prior under test, not as discharged**. I re-derived it independently and it holds. **No cell
references placement**, so this is a header correction with no cell consequence — which is also
`1.0.0_SA_CTO~Z`'s conclusion, reached separately.

---

## 4. SCOPE-FORK RE-DERIVATION — the half the artifact assigns to the certifier

The decomp closes with: *"Its CE claim has a half-life, and the re-derivation belongs to the
certifier, not to me."* Executed. **The three PRD scope forks (GRAIN · ETF POPULATION · INPUT SPAN)
are UNMOVED. The half-life has not expired.**

Swept **three planes**, because one plane could not have answered it:

1. `ANDREW_DIRECT` file adds on `origin/SITEZ` since 2026-08-26T21:48:02Z.
2. **The same on `origin/CLOUD`** — a genuinely different plane. SITEZ lacks **28** CLOUD-only commits,
   so a sovereign word about the name space could be sitting there unmerged and plane 1 is
   structurally unable to see it.
3. Case-insensitive **commit-message** sweep over BOTH refs for name-space tokens
   (`namediscovery|name space|DIVZ|PFOE|PFDE|IDVZ|muni|sleeve|constituent-level|cottonwood`).
   **Denominator: 491 commits in the window across both refs.**

None of the post-authoring Andrew-directs touches GRAIN, ETF POPULATION, or INPUT SPAN.

### One post-authoring sovereign word DOES touch the model-name space — recorded as ADJACENT, not stale-making

`a757e0568e` (2026-08-26T21:59:18Z — **11 minutes after authoring**) records Andrew's ruling *"Opal
Conservative Growth is the same as the 'LT Model'"* plus an existing display-alias map.

That is an **Opal-side CLASSIFICATION / RESOLUTION act**, which `ND-inv-2` (*discovery never silently
classifies*) and `ND-g-3` (*the classification act itself is downstream and outside*) place **OUT of
D1 by declaration**. **The boundary section absorbed it correctly** — which is positive evidence that
`ND-g-*` is doing real work rather than decorating. It is the SOURCE of F2 above; it is not a
staleness.

---

## 5. THE FOUR-POSTULATE RECORDS

**R-n2 (OUTPUT-STATE AXIS `{CANDIDATE, NO-MATCH, UNKNOWN}`) — SOUND, and it is the stronger of the two.**
(i) CE is the point: a two-value `{CANDIDATE, NO-MATCH}` axis collapses the cannot-answer case into a
clean negative, which is the DIVZ defect mechanised. (ii) same grain — all three are per-(name,
surface) verdicts. (iii) intent coherence — content-kind is **deliberately** not mixed with the
enforcement policy, which is correctly held at `ND-e-2`. (iv) state coherence — `CANDIDATE`/`NO-MATCH`
move on DATA, `UNKNOWN` moves on the MECHANISM'S OWN HEALTH; **one remedy does not move all three, and
that asymmetry is exactly why `UNKNOWN` earns its own value.** No finding.

**R-n1 (VARIANT-FORM AXIS) — CE honest, ME defective under the decomp's own matcher.** See F1. The CE
half is right and, importantly, right for the right reason: the fifth value carries the openness
instead of falsely closing the axis, and (iv) correctly observes that the four named forms and the
open class **move on different remedies with different owners** — which is precisely why the fifth
value must be declared rather than folded in.

---

## 6. A NOTE IN THIS DECOMP'S FAVOUR, MEASURED AGAINST ITS SIBLING

**D1 states its denominators on its own face** (§3) and discloses its own pre-commit arithmetic
correction. **D4's decomp has no alignment-denominators section at all** — verified by listing every
section header in D4 plus a positive control proving the extraction instrument works against D1.

That absence is not cosmetic: it is *why* D4's announcing message could claim **"23 cells"** against an
artifact holding 21 cells + 4 invariants and have it travel unchallenged until a certifier counted.
**Recommend D4 adopt D1's practice.** A decomp that prints its own denominator makes the next census a
comparison instead of a discovery.

---

## 7. WHAT I AM NOT ASSERTING

- **I did not exercise `ND-c-1`'s substring-vs-word-boundary control.** It is a well-formed criterion
  with a stated oracle, and running it would not change this verdict. Named so the absence is a
  declared scope limit, not an unstated gap.
- **I certified the DECOMP against the PRD, not the PRD.** PRD v2 @`958c8e4487` is cited, resolves, and
  is an ancestor; its own correctness is not in scope here.
- **F2's third surface (`modelPortfolioColors.ts`) I read at HEAD, not at a pinned portal submodule
  commit.** The finding does not depend on its exact vintage — it depends on the existence of a
  label-keyed alias map, which is stable across recent history — but the vintage is unpinned and I say
  so rather than implying a precision I did not measure.

## 8. WHAT SHOULD HAVE BEEN ASKED BUT WAS NOT

**The decomp asks whether the mechanism can DISCOVER names. It never asks who CONSUMES a surfaced
candidate, and on what clock.**

`ND-inv-2` correctly makes classification a separate, deliberate, attributable act — that is right.
But **a discovery mechanism whose candidates nobody is obliged to look at produces a queue, not a
finding.** D4's F1 ruling landed on exactly this shape: a declared registry does not self-update, and
it is the drift detector beside it that makes the registry safe. **D1 has the mirror gap.** No cell
names the consuming half of its own output. `ND-inv-3` states the principle — *"the consuming half is
the mechanism"* — for the provenance FIELD, and then does not apply it to the CANDIDATE itself.

That is not a defect in any cell that exists. It is the cell that does not exist.

---

— 3.0.0_SA_CVO~Z

---

## AMENDMENT 1 — 2026-08-27 ~17:2xZ. **F1 AND F4 ARE DISCHARGED.** F2 and F3 remain LIVE.

`2.0.0_SA_COO~Z` repaired both at `669e04f27b` (LOCAL) and — correctly — did **not** assert the
discharge, same discipline as `:118`. Verified at source by this seat, not taken from the report.

```
git show 669e04f27b:<DECOMP.md>
  :102-107  R-n1 postulate (i) — the v1 "ME by construction" sentence REPLACED, and the
            conflation named explicitly: THE VOCABULARY (four patterns are distinct
            specifications — ME, TRUE) vs THE MATCH RELATION (which patterns a NAME
            satisfies — MANY-TO-ONE).
  :60       ND-d-1 now requires **which form(s) — A SET, NEVER A SCALAR**; a single-valued
            `form` field explicitly FAILS the cell.
  :5        header now reads **placement SITEZ** (corrected).
```

**F1 DISCHARGED. F4 DISCHARGED.**

### THE AUTHOR'S REMEDY IS BETTER THAN THE ONE THIS SEAT PROPOSED, AND THE REASON IS MEASURED

F1's remedy line in this deliverable suggested *"state a form-resolution rule — most-specific-wins is
the natural one."* `2.0.0_SA_COO~Z` did **not** take it, and gave a measured reason this seat accepts
in full: **the four forms are NOT strictly nested.** `<token> SMA` and `Opal <token>` are **siblings**
— a name can satisfy both while satisfying neither of the others (`Opal DIVZ Fund SMA` contains
`Opal DIVZ` and matches `DIVZ … SMA`, but not contiguous `Opal DIVZ SMA`). So "most specific wins"
requires an **arbitrary tie-break between siblings**, and *an arbitrary tie-break buried inside a
provenance field is the same defect one level down* — which is the very thing F1 is about.

**A SET needs no tie-break.** A consumer wanting a scalar derives it under its OWN stated rule, where
the arbitrariness is visible and owned rather than baked into the discovery layer. **This seat's
proposed remedy would have re-introduced the defect it diagnosed**; recorded plainly because a
finding and its remedy are two separate claims and only the finding was sound here.

Also carried from the author, and it sharpens why F1 was P1 rather than P2: a builder handed *"name
which form matched"* reports the **first pattern in iteration order — the BARE form, the LEAST
specific.** The field would have discarded exactly the information it exists to carry **while looking
populated**, and a populated wrong field survives review where an empty one does not.

### WHAT REMAINS

| finding | status | owner |
|---|---|---|
| F1 | **DISCHARGED** @`669e04f27b` — `ND-d-1` reports a SET; postulate (i) corrected | — |
| F2 | **LIVE, P1** — `ND-c-3` names one registry; the estate holds ≥2 more resolution surfaces with opposite absence policies | round-1 cut |
| F3 | **LIVE, P1** — name `843d875b` ("Pathfinder Focused Opportunities" / PFOE) as the specimen | round-1 cut |
| F4 | **DISCHARGED** @`669e04f27b` — header reads `placement SITEZ` | — |

`2.0.0_SA_COO~Z` correctly left `Criteria: 0 — NO TO IS CUT` **standing**: the decomp instructs that
whoever cuts round 1 amends that line in the same commit, and amending it before the cut would make
it false in the other direction. **Endorsed.**

**F2 is the one to watch.** The author's own read — *"most likely to be satisfied on paper and
violated in the build"* — matches this seat's: a cell naming ONE registry is satisfied by a builder
who checks that one registry, while the hazard lives in the other two.

**The certification verdict is unchanged: CERTIFIED WITH FINDINGS, no TO-mint block.**

— `3.0.0_SA_CVO~Z`
