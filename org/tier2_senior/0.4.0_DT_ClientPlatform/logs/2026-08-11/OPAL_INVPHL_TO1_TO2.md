# 0.4.0_DT_ClientPlatform — 2026-08-11 — OPAL_INVPHL TO-1 + TO-2

**archetype:** IMPLEMENT

## Session scope

Startup (watcher armed, registered, XXX.md protocol), then the OPAL_INVPHL portal-frontend
build: TO-1 (model-portfolio modal) and TO-2 (Philosophy page) on COO's GO 195948Z, which
carried Andrew's ~1953Z approval of the design and all nine decisions. Sequential, TO-1
first, as sequenced — TO-1 establishes the `catalyst/dialog` treatment TO-2 reuses.

## Current State

**TO-1 — BUILT AND VERIFIED.** portal DEV `@84f6b3e2` (5 files, +467/-20).
One `ModelPortfolioModal` on `catalyst/dialog`, two call sites, one shared
`ModelNameTrigger`. Six ruled fields in ruled order; 3-Yr and 2025 appear nowhere in the
diff. Target Return is per-model config beside the model definitions; YTD/1Y/SI from
`getModelPortfolioBenchmarks()`, yield/makeup from `getPositioningData()`. No API field, no
backend, no serving-plane change. All 8 criteria PASS, exercised on both surfaces (5/5
models each).

**TO-2 — BUILT AND VERIFIED.** portal DEV `@335dd198` (5 files, +258/-7).
`/cma` → `/philosophy` with a redirect, header "Investment Philosophy", sidebar
"Philosophy", five-pillar strip above the assumptions panel, five pillar modals. C1–C6 and
C8 PASS; C7 `UNVERIFIABLE-BY-INSTRUMENT` (below). Everything below the strip byte-unchanged,
verified by diff.

Deliverables: `PROOF_OF_SPEC_OPAL_INVPHL_TO1_20260811.json` `@7d47670fe7`,
`PROOF_OF_SPEC_OPAL_INVPHL_TO2_20260811.json` `@7dfd4eb967`, repair `@f778cc0b01`.
Portal main worktree on **DEV** throughout (Rule 19). **No promote** — not in TO scope.

## What the verification actually caught

Three things no static check could have, each caught by a different control:

1. **Wrong model colour (TO-1), caught by the screenshot.** I passed a model CODE to
   `getModelColor`, whose map is keyed by NAMES. `'LT'` matched no exact key and fell to the
   partial-match fallback, which resolved `'Ultra-Long Term'` — because "ultra" contains the
   substring "lt" — so Long Term rendered in Ultra-Long Term's **red**. `tsc`, `eslint` and
   `comp-cache` were all green; both branches typecheck identically. This is the same trap
   `modelPortfolioColors.ts` documents in its own comment block, one layer over. Fixed at
   both call sites by resolving `getCanonicalModelName()` first.

2. **`tsc -p tsconfig.json` is a FALSE GREEN in this repo, caught by asking for a
   denominator.** It exited 0; `--listFiles` printed **0 lines**. `portal/tsconfig.json` has
   `"files": []` and only project references, so it typechecks nothing. The real check is
   `tsc -b`, which I then mutation-proved (a deliberate type error failed it at my exact
   file, rc=2). **portal CI runs the empty form** (`ci.yml:56`) — surfaced to CTO/COO.

3. **My own icon mis-assignment (TO-2), caught by a denominator on the wrong step.** The
   first extraction matched icons to pillars by nearest-title distance; it collided and,
   because the filename came from the match, silently **overwrote** — 3 files for 5 icons. A
   clean "5 of 5 icons found" on the FIND step said nothing about the ASSIGN step. Redone by
   x-position, with slide 9's own 01–05 number boxes as an independent control.

Plus the coupling **no spec named**: `src/lib/firmAccess.ts` is a deny-by-default per-firm
route allowlist requiring exact `<Route path>` matches. Renaming without it would have made
the Philosophy page unreachable for all four partner firms, each silently bounced to
`/market`. Found by asking what *references* the route rather than working the spec's file
list.

## Mutants fired (a passing assertion never mutated has never been tested)

| Mutant | Expected | Observed |
|---|---|---|
| Swap `Long Term` / `Ultra-Long Term` prose keys | exactly those two fail | `3 passed, 2 failed`, rc=1, wrong-model diagnosis printed on both, other three green |
| Deliberate type error in `ModelPortfolioModal.tsx` | tsc fails naming that file | `ModelPortfolioModal.tsx(209,7): error TS2322`, rc=2 |

Both reverted and the revert **verified** (prose pairing re-asserted; no `__MUTANT__`
residue).

## Open at COO / CTO

- **Proof-of-spec gate conflict, confirmed to generalize** — TO-1 INVALID on 2
  artifact-coverage violations, TO-2 on 4, one cause: the checker scans `criterion_id` only
  and wants the artifact stem inside the id, while both TOs pin the id set to `C1..C8` and
  the same script rejects ids outside it. Unresolvable without a false `declared_exclusion`
  or a mis-typed artifact `kind`; neither done. **Both `complete` flips withheld on it — no
  code work outstanding on either TO.**
- **CLAUDE.md Rule 25 amendment (TO-2 C7)** — owned-paths refused (`lane=BASE_EXEC`).
  Routed to COO + CTO in the same turn with the exact substitution. Left in-tree and
  **unstaged** (safe-commit had staged it before the hook fired; a staged law file is the
  F-010 sweep accident). ⚠ Rule 25 names `cma` twice and one is inside **Andrew's verbatim
  quote** — left byte-untouched; only the editorial parenthetical amended. The TO's
  suggested text would have rewritten the quote.
- **Same-commit is structurally impossible across repos** — the rename is in the portal
  submodule, CLAUDE.md in the workspace repo. Unsatisfiable at any lane; template fix.

## Surprise channel (no action taken)

`comp-transform schema-check` returns rc=0 with "Component not found" for anything outside
`portal/src/pages/**`, so 2 of TO-1's 3 mandated components read as a pass while unchecked
(positive-controlled against `FearGreedModal`); `schema-check Tooltip` silently resolves to
`ChartTooltip`. `BenchmarkHeatmap.tsx` is SEV1 and now has no commit-time guard (the
`comp-surface-check` retirement's accepted consequence — no gate manufactured).
`PROOF_OF_SPEC.schema.json`'s `phase` enum has no value for a frontend build. `portal/`
carries pre-existing untracked residue (`.runtmp/`, `org/`, `src/org/`,
`catch404_final.png`). One self-inflicted F-010 instance: backticks in a double-quoted
`python -c` were command-substituted and silently deleted a word from a committed record
(repaired `@f778cc0b01`).

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find` | `PORTFOLIO_NAMES`, `getModelPortfolioBenchmarks\|getPositioningData`, `getAllocationData`, `/cma` sweep | Gave the identity handle for the Positioning trigger (`PORTFOLIO_ORDER[idx]`, since `PORTFOLIO_NAMES` is derived from it) and **surfaced the `firmAccess.ts` coupling** — the finding that would otherwise have shipped the page unreachable for every partner firm. Denominators printed on every call (4/405, 18/405, 5/9). |
| `comp-transform schema-check` | `ModelPortfolioModal`, `BenchmarkHeatmap`, `PositioningSummary`, `CapitalMarketAssumptions` (+ controls `Tooltip`, `FearGreedModal`, `ModelPortfolios`) | `PositioningSummary` and `CapitalMarketAssumptions` clean. The two `src/components/**` files: "Component not found" at **rc=0** — domain limit, established by positive control, **not** counted as a pass. |
| `comp-cache` | `collisions`, `key model-portfolio-benchmarks`, `key positioning-data` | `captured 104 of 104 useQuery call-site(s)` — it saw the new file; `15 shared key(s); 0 with a TYPE MISMATCH`. Both reused keys share their existing `queryFn`, so the modal serves from cache rather than double-fetching. Rule 20(b) discharged for both TOs. |
| `comp-which` | "does clicking a model name have any cached query implication" | No curated rule matched; top fuzzy candidate `comp-cache` (0.48) was in fact right and was then run properly. Recorded as a small catalog gap, not treated as a routing decision — per the tool's own warning. |
| `tsc -b --noEmit` / `eslint` | changed files | Both rc=0. **`tsc -p tsconfig.json` is a false green here** (0 files); `tsc -b` mutation-proved live. |
| `/frontend-dev` | `ui-smoke` pattern extended for interactive state; screenshots read | Caught the wrong-model-colour bug; verified colour law (dark-on-silver), affordance, focus ring, reflow, and the five icons at 3x. |

## Next Steps

- [2.0.0_SA_COO] Rule on the proof-of-spec artifact-coverage conflict → both `complete`
  flips are one word away.
- [1.0.0_SA_CTO or 2.0.0_SA_COO] Land the Rule 25 amendment (substitution supplied;
  keep the verbatim quote untouched).
- [DT] Idle and available, event-driven. No promote requested or performed.
