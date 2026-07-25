# F4: the router mis-route was a BAND INVERSION, not missing vocabulary — 0.8.0_AE_CloudComp~C

**archetype:** DIAGNOSE
**Date:** 2026-07-25
**Task Order:** CTO~Z F4 dispatch 170603Z ("fix the routing so the decommission intent reaches the
decommission tools" + the binding condition: *add the case that would have caught this*)
**Status:** COMPLETE — landed @a27628d386, pushed
**Cycle wall:** ~17:06Z ACK → ~17:32Z reported

---

## Objective

`comp-which "find deprecated unused or overlapping AWS resources"` returned **comp-transform** — a
React component field-render tool — at rank-1, score 1.85, **VETTED** (no fuzzy-guess banner), while
the decommission family sat at 0.46 / 0.21 / 0.19.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| `comp-which` | the dispatch query | **mis-route reproduced** | pre-fix rank-1 comp-transform 1.85 |
| `comp-grep` / `comp-glob` | locate router + tests | PASS | comp-glob again self-flagged 0-hits as non-absence (gitignored `.comp-graph/`) |
| extractor probe | `_run_extractors` attribution | **root cause** | curated 0.50 vs surface-first 0.85 |
| `commit-gate.sh` | 2 `.py` | **BLOCKED then PASS** | caught my over-fire — see below |
| `comp-system` | regenerate 06 | PASS | gate-required; "managed spans already current (0 changed)" |
| `pytest` | routing suite | 27 passed / 1 xfailed; 96 across which+route | 0 regressions in 18 pre-existing cells |

**What worked:** attributing the score to an extractor instead of reasoning from the ranked output.
The ranked list said "comp-transform, vetted" and invited a vocabulary fix; the attribution said the
curated layer was *fine* and something else was outranking it. **The visible artifact pointed at the
wrong layer.**

**What failed (mine, disclosed):** my non-vacuity cells guarded comp-transform and **missed
comp-tool-health**, whose use_case says *"KEEP, FIX, PROMOTE or RETIRE"* — my bare `"retire"` token
stole its self-route. The **universal self-route invariant** caught it at commit time. My
enumeration covered 1 tool; the gate covered 68. I did not add a bespoke cell afterwards — doing so
would imply my enumeration saved it, and it didn't.

Session line appended to `org/compiler-tools-log.md`.

---

## Root cause — not the assumed one

Both the dispatch and my ACK assumed missing curated vocabulary. Attribution refuted it:

```
curated_extractor       -> comp-aws 0.50, pipescript 0.50, comp-pipescript 0.50   CORRECT
surface_first_extractor -> comp-transform 0.85                                     the hijack
```

`surface_first_extractor` mints VETTED at **0.85**. Curated's real confidences are
`min(1.0, score/6.0)` — score 4 → **0.667**, score 5 → **0.833** — and a flat **0.5** for the weak
cascade-step-6 hit. **So surface-first outranked every curated hit except a perfect score-6 rule.**

Its docstring claimed *"below curated's 1.0"* — **wrong about that number**: `1.0` is
`_VETTED_OFFSET`, which `comp_route.py:381` adds to *every* vetted candidate identically.
`fuzzy_extractor`'s docstring states the intended cascade (*"strong-curated > surface-first >
fuzzy"*); `comp-which:44` states it a third time. **Three assertions of the invariant, constants
implementing its inverse, and nothing comparing them.**

**Vocabulary alone could not have fixed this** — a new rule would still lose to 0.85 unless cranked
to score 6, i.e. gaming the scorer to beat a mis-banded competitor. The re-band was a
**precondition**, and (being a global precedence change to a shared router) is flagged for CTO~Z to
ratify or reverse.

## Work Completed

1. **Regression cells FIRST, proven RED** (5 failed / 5 passed) before any routing edit — so the fix
   is demonstrably what turns them green, not my edit judged against my own verdict (the 142116Z
   tautology, not repeated in the commit that fixes a router).
2. **Band corrected** — surface-first `0.85−0.15·rank` → `0.60−0.05·rank` floor `0.52`: below
   strong-curated, above confident-fuzzy, exactly as documented. Band written into the docstring so
   the next editor can *check* it rather than infer it.
3. **New curated rule** — estate DECOMMISSION sweep. `"deprecated"` and `"overlapping"` existed
   **nowhere** as curated keywords estate-wide. Multi-tool by design (four coldness/overlap planes).
4. **comp-iam-usage spelling gap** — carried only hyphenated forms (`still-used`, `who-can-reach`),
   so the way an agent types it lost to comp-iam (grant-correctness) on a lifecycle question.

## Files Modified

| File | Change | Committed |
|---|---|---|
| `org/modules/graph/comp_which_signals.py` | surface-first band + documented band table | @a27628d386 |
| `.tools/comp-which` | decommission rule + comp-iam-usage spaced forms | @a27628d386 |
| `org/modules/graph/tests/test_compwhich_toolpass_rules.py` | F4 cells + non-vacuity + live xfail | @a27628d386 |
| `infra/system/06_current_state.{md,json}` | gate-required regen (scope verified pre-stage) | @a27628d386 |

## Blockers

None.

## Residuals (named, not absorbed)

- **(a)** The cross-sense **drill** collision remains — comp-transform still drills on `"unused"` for
  an AWS query. Made subordinate, **not removed**.
- **(b)** `unused field audit for a component` → **comp-adapter-audit**: separate, **pre-existing**
  (RED before my rule, unchanged after). Three co-equal fuzzy `0.500`s tie-broken **alphabetically**
  at `comp_route.py:384` — wins on the letter 'a'. The neighbour tranche-1 (`comp-which:161`) was
  written to beat: **that hardening has silently regressed.** Left as a **live xfail** (not deleted,
  not skipped) so it flips to XPASS when the precedence is ruled on — above this lane.
- **(c)** `ms cloud estate overview` detects MS-CLOUD but drills **zero** tools. Isolation-probed as
  pre-existing + band-independent — it *looked* exactly like a regression I had caused.

## Next Steps

1. **[1.0.0_SA_CTO~Z]** Ratify or reverse the global band change; rule on residual (b)'s
   weak-curated-vs-confident-fuzzy precedence, which unblocks the xfail.
2. **[0.8.0_AE_CloudComp~C]** Event-driven, reachable.
