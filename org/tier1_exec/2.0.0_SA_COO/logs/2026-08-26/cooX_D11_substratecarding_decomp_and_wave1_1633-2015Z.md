# The decomp that kept finding itself in its own findings — 2.0.0_SA_COO~X

**archetype:** COORDINATE
**Session:** 2026-08-26 1633–2015Z · **Serial:** `2.0.0_SA_COO~X` · **Seat:** COO lane X, seated by Andrew-direct
**Project:** `NFRA_SUBSTRATECARDING` (Directive D11) · **Stage:** Rule 27 step 3 — atom-decomp → TOs → wave 1

---

## Objective

Run the Rule 27 stage-3 atom-decomp of `NFRA_SUBSTRATECARDING` and drive wave 1 to delivery: decompose the
operative surfaces before any TO exists, cut and dispatch the TOs, coordinate four `~X` lanes plus a
verifier, and discharge the issuer-owned mechanism cells. Secondary, Andrew-commissioned mid-session:
a briefing standardizing the comp-tool HUD.

---

## Compiler Tools

| Tool | Command | Result | Note |
|---|---|---|---|
| `comp-which` | `comp-which "how do I grep the repo"` | **PASS** — banner produced | A.3 exercise half: resolution is not execution |
| `comp-find` | `-i 'paginated results like all the other comp-tools'` | **2 hits / 26,841 scanned** | Found Andrew's 2026-08-05 edict; the finding that shaped the HUD brief |
| `comp-find` | `--name 'nerves_resolve'` | **2 hits / 28,794 scanned** | Tool reachable; the CARD was the absent thing |
| `comp-find` | `-i 'nerves_resolve' --name 'nerves_resolve'` | **0 hits / 0 scanned** | ⛔ TRAP SHAPE, reproduced deliberately as a control |
| `comp-find` | `--name '*kuzu*'` vs `-i 'kuzu' --name '*kuzu*'` | **65 / 28,795** vs **0 / 0** | The load-bearing pair: 65 known hits collapse to a clean zero |
| `comp-keys` | `prefix s3://opal-estate-report/` ± `--all` | **40 of 129** vs **129 of 129** | ⛔ Default truncation hides `kuzu_nessie_db`; kuzu match count 0 → 1 |
| `comp-kuzu` | `"MATCH (n) RETURN count(n)"` | **27,035 nodes / 58,224 edges**, snapshot `2902399899597701830` | The wave `as_of` pin; provenance header read |
| `jsonschema` | Draft 2020-12 over `SUBSTRATE_CARD.schema.json` | **F-1/F-2/F-3 all VALIDATE**; control REJECTED | The three freeze holes, exercised not read |
| `build_rectangle.py` | `--self-test` | **9 of 9 PASS** | Incl. rectangularity negative control, Rule-13 population arm, grammar arm + its own negative control |
| `safe-commit.sh` | 11 commits, `-F` message files written by the Write tool | all clean | gate2 caught a real `<decomp_ref>` defect in ANNOUNCE mode |
| `proof-of-spec-check.py` | read at source (`:179`, `:327`, `:355`) | — | Source read is what proved my cell ids were invisible to the harvest |

---

## Work Completed

### 1. Stage-3 decomp — 61 cells, generated from the contract
`workflows/atom_decomposition/runs/nfra-substratecarding/20260826T172918Z/` — two **declared** planes
(CARD_MATRIX 8×7 at *subject × card row*; PROJECT_MECHANISM 5 at *project* grain). The split is what
satisfies Rule 24(ii); folding them into one list was the available failure. Rectangle **generated from
`SUBSTRATE_CARD.schema.json`**, never hand-typed, so the cell set cannot drift from the deliverable's
contract. Deterministic, self-tested 9/9.

### 2. Three findings against the freeze — exercised, with a live positive control
The schema **permits** three things Rule 28 forbids: null `coverage.denominator` (F-1), `inferential`
determinism with no `inference_detail` (F-2), and `SOUND` over an unworked row (F-3). **Not fixed** —
qualify-do-not-fix binds the issuer too — so they became `*-AC3/AC4/AC5` on every TO. All three accepted
by the schema owner; v2 landed at the wave boundary.

### 3. Four TOs cut, dispatched, and all four accepted
21 + 21 + 14 cells + the manifest. Alignment verified **with the estate's own harvest regex** rather than a
re-implementation: every TO 100% of refs resolving and a subset of its declared set.

### 4. Wave 1 delivered
**8 cards** (C0/C1/D1/D2/D3/comp-similar QUALIFIED; C2 + C3.i UNSOUND — both cards working), **39 manifest
parts**, and the headline: **22 real persisted graph objects that no wave-1 card names**, including two
`cse_test_*` tables in the production warehouse and a 158MB orphaned rebuild set.

### 5. Two priors overturned by measurement
**D3 was ruled to card empty and did not** (real store, 14 records, two independent instruments).
**`comp-similar` was suspected inferential and measured deterministic** with a control that could have
failed — same-input byte-identical *and* different-subject differs.

### 6. The P1 class — sized at 23 of 56 (41%)
One enum over a unit containing mixed-provenance parts. Four fields, two contracts. **Every lane's detector
under-counted; all three revised UP under author adjudication.** No regex can find it: the class is defined
by what the author *did*, the prose is what they *wrote*.

### 7. HUD brief (Andrew-commissioned, mid-session)
`docs/briefs/COMP_HUD_STANDARD_BRIEF_20260826.md` — 105-tool survey, **1 of 105** carries the full HUD.
Andrew's 2026-08-05 edict **exists** and its premise (*"like all the other comp-tools do"*) was **false when
written**: applied once, to the tool it named, against an empty comparison class.

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Cut TOs against an UNCERTIFIED decomp, stamped on each face | Pipeline's own escape valve; a silent uncertified decomp is its single point of failure. Holding four lanes behind a cert would have been a manufactured gate |
| Bound "EVERY SINGLE GRAPH SURFACE" to census + card lineage | Andrew's ambition for the artifact, not a wave-1 completion bar. An unbounded census has no completion condition — the lane runs until it runs out of context |
| `generator_currency` restated as in-evidence | My authorized KEY form was schema-REJECTED. The v1 freeze holds mid-wave; nobody amends a schema to make my ruling fit |
| Phase-B trigger read as *committed*, not *pushed* | The trigger exists so the manifest can READ the cards; DT~X reads this device's worktree. "On origin" would have made phase B wait on an integrator act unrelated to the data |
| Refused to sum lane part-counts; ACCEPTED summing lane row-counts | Parts are shared across lanes (double-count); rows partition cleanly. **The rule is about GRAIN, not provenance** |
| Distributed the reference card with hard framing | Overrode my own "leave it unminted" rec once CTO~X named the argument I missed — the schema had never been exercised against real content |

---

## Files Modified

| File | Change | Committed |
|---|---|---|
| `workflows/.../20260826T172918Z/DECOMP.md` | the decomp face + 5 self-corrections | Yes — `7c5de3e779` … `c8aa46b1a5` |
| `.../build_rectangle.py` + `rectangle.c0.json` | generator + 61-cell rectangle | Yes — `aae317509b` |
| `.../SC-m-4_wave2_derivation.json` | wave-2 derivation + correction chain | Yes — `3cb2e92679` |
| 4 × `NFRA_SUBSTRATECARDING.TO-W1-*.md` | TOs cut, amended, cert-flipped | Yes — `10467ef91a` … `f926e8fd29` |
| `docs/briefs/COMP_HUD_STANDARD_BRIEF_20260826.md` | HUD standard brief | Yes — `4edb1c8883` |

**All LOCAL on CLOUD, riding integration.**

---

## Blockers

None. `SC-m-5` is open by design — `3.0.0_SA_CVO~X` discharges it at wave close **by measurement**.

---

## Current State

**Wave 1 DELIVERED.** All 4 TOs accepted. Decomp **CERTIFIED PASS** (`5b390a5662`) — sealed mutant found
with three discriminators, seal matched on all five fields from two independent derivations.

```
SC-m-1 PARTIAL   the reduced freeze -- NOT back-dated
SC-m-2 MEASURED  exercised: 8/8 on-pin, 0 mismatches, control fired
SC-m-3 COMPLETE  39 parts, both residues with owners
SC-m-4 MEASURED  exercised; 35 candidates, bounded not exact
SC-m-5 OPEN      CVO~X, at close, BY MEASUREMENT
```

---

## ⛔ My Own Errors — the section that matters most

**Nine, all caught, none by me alone.**

1. **Declared `executor_class` populated when 0 of 61 were** — caught by the method's own Rule 13.
2. **Cell ids invisible to the estate harvest regex** — `declared=0 / refs=21`; the bidirectional alignment
   **could never have run** and every lane would have hit a failing gate through no fault of its own.
   Caught by gate2 in ANNOUNCE mode, which I first misread as a formatting nit.
3. **That fix introduced an id collision** (`SC-g-*`), caught by verifying after the edit.
4. **The collision fix introduced a harvest defect** — grammar-conforming boundary ids enter the harvest as
   cells. Caught by the certifier.
5. **Claimed 61 of 61 cells lane-covered; measured 59.**
6. **Cut four TOs on a precondition half-false** — `SC-m-1`'s reference card did not exist. Surfaced by a
   lane refusing to conclude from a zero over a zero denominator.
7. **Told four lanes a trap was "transient" when it is deterministic** — my remedy (widen and re-run) would
   have failed. Corrected by the lane that isolated it.
8. **Authorized a `generator_currency` KEY form the schema rejects** — I issued an amendment against a
   contract I had personally proven three holes in, **on inspection rather than exercise**.
9. **Published 12 of 56 when the true figure is 23** — low by 1.92x.

⛔ **AND THE PATTERN UNDERNEATH TWO OF THEM:** I twice stated a limit of *my vantage* as a property of *the
world* — *"structurally unresolvable"* (true of the strings, false of the identity) and *"unmeasurable from
the artifacts"* (true from outside, false from the author's seat). **"I cannot measure this" is not "this
cannot be measured."** Both corrected by the seat holding the other vantage.

I also **nearly broadcast a false gap** off a wrong-subject control — checked one field, concluded about the
card — the exact error I had broadcast to five seats an hour earlier. Caught by opening the artifact before
sending.

---

## Next Steps

1. `3.0.0_SA_CVO~X` discharges `SC-m-5` by measurement → wave close.
2. `1.0.0_SA_CTO~X` holds the v2 act, now sized at 23 of 56; their commit message cites a superseded 4.
3. **Wave 2 is DERIVED, not enumerated** — 35 candidates from rows 1+4, bounded, awaiting `part_id`.
4. Andrew holds one HUD call: **default-cap vs default-full**, and one estate-wide cap number.

---

## The thing worth carrying

**This project reproduced, in its own artifacts, the defect it exists to measure — four times.** The card
schema permitted three things Rule 28 forbids. My own ruling required a field that schema forbids. The
wave-2 fields carried one concept in six spellings with nothing declaring the mapping. And `basis` claimed
`measured` over held sub-claims in 41% of accepted rows.

**Not one of those was found by the seat that made it.** They were found by lanes auditing their own passed
work, by a gate firing in announce mode, by a certifier hunting a planted mutant, and by peers correcting
each other's scope. **The fabric's error rate was not low. Its correction rate was near total, and every
correction moved in the direction that made the correcting seat's own work look worse.**
