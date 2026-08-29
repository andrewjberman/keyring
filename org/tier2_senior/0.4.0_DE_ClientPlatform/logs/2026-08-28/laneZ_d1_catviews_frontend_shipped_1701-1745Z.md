# 0.4.0_DE_ClientPlatform~Z -- 2026-08-28 17:01-17:45Z -- D1_CATVIEWS ASSET CLASSIFICATION FRONTEND

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

Post-reboot session, seated by `2.0.0_SA_COO~Z` 16:59:55Z under Andrew-direct ~16:5xZ: *"the much
higher priority is getting Asset Classifcatin frontend sorted"*. Delta since
`laneZ_prereboot_delta_1600-1605Z.md`. Rule 27 project: `D1_CATVIEWS`, one project, one seat.

---

## Commits (all portal, branch DEV, all `npx tsc -b` rc=0)

| hash | what |
|---|---|
| `d3487fc9` | docs(D1_CATVIEWS): two stale carriers retired -- comments only |
| `79212837` | fix(D1_CATVIEWS): engineer vocabulary off the advisor page + the headline gate |
| `192b0865` | feat(D1_CATVIEWS.TO-S1-DE): L1/L2 presence suppression |

Per-file detail: see commit messages. PUSH STATE, MEASURED by `ls-remote`: **LOCAL**, origin/DEV
`9957410e`, AHEAD 3 / BEHIND 9. Overlap set against the 9 incoming (ADVI_PERFRP) is **EMPTY** --
12 files theirs, 3 mine, `comm -12` returns nothing. Push routed to `0.0.0_AB_MSTR~Z` (LD-0367).

---

## OK: THE MEASUREMENT THAT CHANGED THE SESSION -- my first render was the FAILURE STATE

The `/frontend-dev` render on the default stub token showed *"Category views are not available at
this scope"* and looked like a finding about global. It was a 401 at all four scopes. Re-rendered
with a real RS256 bearer (committed `internal_admin` cred, `POST /auth/login`, TTL 900s).

**THREE-ARM CONTROL on `/api/general/mdpf/global/category-views.json` via the dev proxy** -- the
third arm is the load-bearing one, because 200-with-a-bearer alone is equally consistent with an
ungated endpoint:

```
  real bearer   -> 200 (4442 bytes)
  no auth       -> 401
  BOGUS bearer  -> 401      <- proves the signature is VERIFIED, not merely present
```

Global serves a real object and renders a real tree. Every claim below was read off a rendered PNG.

---

## What was actually wrong, and what shipped

**RENDER-SIDE (this lane's), all four GO'd by `2.0.0_SA_COO~Z` 13534 + 13544 s.3:**

| id | defect | fix |
|---|---|---|
| R1 | The emitter's own prose shipped to advisors verbatim -- a Python list literal `HELD BY: ['cottonwood']` and *"the reader can see which firm to chase"*, in the loudest box on the panel | Replaced with observational copy; raw field to `console.warn` |
| R2 | `unavailable` is returned for ANY non-404 failure incl. a 401, and drew *"not available at this SCOPE"* -- a transport failure reported as a property of the reader's scope | Cause-neutral string; `aum.ts:895-897` already logs scope+status. **Fixed AS A PAIR with the adjacent `absent_by_scope` branch** |
| R3 | *"VIEW-PLANE CHECK Displayed L0 total $2.09B vs total AUA minus Insurance -- closes"* on a client page | Off the DOM; `console.error` on breach |
| R4 | `CategoryCard` gated its CHILDREN on the predicate but rendered the FIGURE unconditionally -- a held node printed `$290.43M` with a panel beneath saying that figure is unavailable | Headline gated too; **no placeholder, no `$0.00`, no em-dash** |

R4 decides nothing: the producer already serialises `predicate: "unavailable"` and names the
holders. The renderer was not honouring a declaration in an object it had already parsed.

WARN: R3 REVERSES A DELIBERATE PRIOR REMEDY, recorded so it is not re-litigated blind. That block
was made loud ON THE PAGE precisely because a money invariant whose failure looks like its success
is a control nobody reads. That remedy is what put the vocabulary in front of advisors. Same
control, right plane -- not a weakening.

---

## TO-S1-DE -- BUILT. The TO-M1-DS ordering is enforced BY THE DATA

13335's hazard verified BEFORE building, not after: **0 of 15 L2 members carry an `aum` at either
scope**; `MODELS > PRIMARY` expands to five rows all rendering `--`. A flat "suppress null or zero"
would delete the entire L2 layer at every scope -- the rule working perfectly and removing the
feature, with no error state and nothing to alert on.

`visibleConstituents()` -- one predicate, L1 + L2 + the drill affordance -- asks a prior question:

```
  NOTHING at this level carries a value  -> producer has not mapped it. SUPPRESS NOTHING.
  SOMETHING does                          -> a null/zero beside it means "not held". SUPPRESS IT.
```

EXERCISED BOTH DIRECTIONS:
- **LIVE 49financial:** `Custom $0.00` GONE, `Client - Opal Unsupervised $0.00` GONE (fires);
  `MODELS > PRIMARY` still expands to all five `--` rows (layer survives); L0 set unchanged,
  Models $1.47B + Client $290.43M intact (TS1-AC4, no regression).
- **FIXTURE** carrying M1's post-landing shape, one block holding both arms:
  `812.00M / 431.50M / 0.0 / 228.82M / null` -> RENDERED 3, SUPPRESSED 2. Predicted before the
  render, matched exactly.

**DEVIATION FROM TS1-AC1, NAMED NOT BURIED -- and ACCEPTED by `2.0.0_SA_COO~Z` 13573 as that
seat's own wording defect.** AC1 says null and zero both suppress; AC1's null is Andrew's *"that
model doesnt exist for them"* (this client does not hold it). Today's L2 nulls are the other kind,
unmapped for everyone -- the TO's own s.3 says so. AC1's wording is being amended to the
sibling-guard predicate; the implementation stands.

Chose a data guard over a feature flag deliberately: a flag puts the ordering in a seat's MEMORY
and needs someone to remember to flip it. This arms itself when M1 lands, no code change, and
gates nobody's work (so it is not an agent-made gate).

---

## WARN: CORRECTING MY OWN CONTRIBUTION TO A RETRACTED MECHANISM

I reported `global.Client == 49financial.Client` identical to the cent as CONFIRMING the
aggregation defect, with *"a DIFFERENT instrument"* in the subject line. The measurement stands.
The framing does not, and the flaw is mine independently of the four seats who shared it:

**A RESIDUAL ON A HELD NODE PREDICTS THAT EXACT EQUALITY JUST AS WELL AS AN AGGREGATION BUG DOES.**
So the number never discriminated between the two mechanisms -- I offered as corroboration
something consistent with BOTH hypotheses, which is the one thing evidence must not be. I
corroborated a MAGNITUDE while `predicate: "unavailable"` sat unread in the same object I had
already parsed and printed fields from.

Recorded in `79212837`'s commit body as well, so the retraction travels with the code and not only
the thread.

---

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-which` | A.3 startup exercise | PASS | forwarder RAN (own banner); PATH 105 of 105 resolve bare |
| `commit-gate` (via safe-commit) | 3 commits | WARN | *"checked 0 of N files"* on every frontend diff -- NOT a clean gate, cited as such nowhere |
| `tsc -b` | after each of the 3 commits | PASS | rc=0; the language-appropriate instrument the gate is not |
| `ui-smoke.mjs` | 9 renders, 2 scopes + 401 state + expanded + fixture | PASS | the only instrument that can see a display defect |
| `risk-reflex` (comp-pulse diff) | pre-commit on `d3487fc9` | WARN-READ | HOLD on ModelPortfolios.tsx; citation read as instructed -- a 2026-06-17 baseline/scan-scope mismatch, CTO-adjudicated NOT a real removal. Benign, dispositioned. |

**What worked:** the three-arm bearer control -- it is the whole reason this session did not report
a 401 as product behaviour. **What failed:** `to-check.py --assignee` returned 6 TOs for the base
serial and NONE of them is `TO-S1-DE`; the known notation defect, my TO came from the dispatch
message as XXX.md says it must. **Gap found:** `safe-commit` passes `--author` but never sets a
committer, and the portal submodule had no identity -- rc=128 on every portal commit. Surfaced,
owned and fixed by `2.0.0_SA_COO~Z` (13539) within the session.

---

## Blockers

**None at this seat.** `TS1-AC2`'s literal worked case (Opal Fixed Income RENDERS for cottonwood,
ABSENT for inflection) needs real per-strategy dollars and is gated on `D1_CATVIEWS.TO-M1-DS`,
whose pin is mid-deploy at `0.7.0_AE_CloudOps~Z` with its ledger OPEN as of 17:25Z. The fixture
proves the RULE, not that case, and is explicitly NOT the release condition -- 13335 and 13573
both say a peer's completion claim is not either. `2.0.0_SA_COO~Z` 13573: *"NEXT AT YOUR LANE:
nothing new from me. Hold for M1 landing."*

---

## Current State (written for zero prior context)

- `portal/src/components/CategoryViewTree.tsx` carries all four render fixes plus
  `visibleConstituents()` (the L1/L2 presence predicate + the systemic-absence guard).
- `portal/src/api/endpoints/aum.ts` and `portal/src/pages/ModelPortfolios.tsx` carry the two
  corrected carriers. The `enabled`-guard asymmetry on the category-views `useQuery` is
  DELIBERATE and now documented at the call site -- **do not "restore symmetry"**; that would
  re-bake the withdrawn per-firm-only ruling `aum.ts:857-869` removed on purpose.
- Portal local HEAD `192b0865` on DEV, 3 ahead / 9 behind `origin/DEV` `9957410e`, overlap EMPTY.
- Dev server left running on :5175 so a certifier can re-render. Bearer is minted per-render from
  `portal/.frontend-dev/auth/credentials.json` (`internal_admin`), TTL 900s -- mint-then-render is
  ONE act.
- Screenshots in this session's scratchpad (not the repo): `live_global`, `live_49f`,
  `exp_49f_primary`, `after_global`, `after_401`, `after_gate_global`, `after_gate_49f`,
  `s1_49f_expanded`, `s1_l2_fixture`.

---

## Next Steps

- [`0.0.0_AB_MSTR~Z`] Push leg -- 3 commits LOCAL, clean pull-merge (overlap EMPTY, measured).
  NEVER a rebase on DEV.
- [`0.7.0_AE_CloudOps~Z`] `D1_CATVIEWS.TO-V1-AE` pin advance; `TO-M1-DS` follows it.
- [`0.4.0_DS_ClientPlatform~Z`] `TO-M1-DS` -- the moment per-strategy dollars land, this lane's
  guard arms itself and `TS1-AC2` becomes measurable at a real scope.
- [`2.0.0_SA_COO~Z`] Amending `TS1-AC1`'s wording to the sibling-guard predicate so a certifier
  scores what was built. Producer-side residual on a held node (13544 s.4) is that seat's.
- [`3.0.0_SA_CVO~Z`] `TS1-AC2` stays UNDISCHARGED; no proof-of-spec instance filed on purpose --
  a partial instance risks a false VALID on a criterion that never ran.
- [this seat] Hold for M1, then render a real scope and close `TS1-AC2`.
