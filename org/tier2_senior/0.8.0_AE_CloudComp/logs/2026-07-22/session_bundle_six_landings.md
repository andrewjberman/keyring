# Tool-gap bundle: SIX of nine items landed in one window (5, 4+1+3, 2, 6)

**archetype:** IMPLEMENT
**secondary_archetypes:** VALIDATE, DIAGNOSE

Window 2026-07-22 ~21:2xZ -> ~22:5xZ, continuing `session_reinstantiation_*.md`. Andrew-direct
scoped release @1910b1594; postmortem handover @7cc6376e5 grew the bundle to nine.

## Landings (all pushed, all CTO-accepted same-window)

| Item | Commit | What | Verification |
|---|---|---|---|
| 5 | `fe19d46ff` | monolith silver artifacts = graph nodes (name-grain, live-derived edges); + fan-in walk dedup fix (blast OVER-COUNTED on multi-path reach) | CTO re-verified live; PRD v1.16 standing warning: re-derive pre-fix blast numbers |
| 4+1+3 | `c628e7b54` | pipescript assets-gold/silver registration; io MONOLITH SILVER READS section (1:1 with DS S4 SS3); converter family resolvable; extractor precision hardened (33->17 name-by-name audit) | CTO re-verified live; PRD caveat FULLY CLOSED v1.18 |
| 2 | `b6e4a784c` | false-presence resolver: extract_ts_source.strip_comments state machine wired into extract_routes + extract_api; getAccountDistribution regression pin | CTO re-verified live; F-4 closed PRD v1.21; naming ruling LEGITIMATE |
| 6 | `bdc4512a8` | danger-map AUTO-REFRESH on stale read (lock, timeout, degrade-never-block) | exercised both directions live (40h-backdate -> healed same invocation; fresh no-op); landing commit's own reflex ran on healed map |

Census + interim map rebuild earlier: @e7952ccba / custody @472906b5d (CTO line).

## Defects found IN my own work this window (all self-caught, all locked)

1. **False-presence phantoms from my item-5 first cut** — minted nodes from a docstring explicitly
   saying tables were NEVER declared (etf_schemas.py:17), a dict key, prose mentions, and a
   concatenation fragment (`fact_model_`). Fixed by usage-form acceptance (PATH/CALL-ARG/ENUM/
   ARROW); population audited name-by-name 33->17, each drop individually verified. The exact
   class the bundle fixes, committed by its fixer, caught within the hour.
2. **Negative control read 0 off discarded stderr** (blast NOT-FOUND prints there) — the
   put-the-control-on-the-retrieval class, rerun honestly.
3. **Wrong test premise** — asserted a consumer edge for fact_rps; the S4 contract maps none
   (producer-only). Test fixed to the contract, not the code.

## Cross-checks that held

- Auth column on getAccountDistribution grounded on RAW TF (cloudfront-distribution.tf:696-708),
  not the instrument under repair: edge-JWT YES is TRUE; DE's wrong-auth = wrong-URL-therefore-
  wrong-row.
- 29 pre-existing graph-suite reds: all 16 failing files touch zero build_graph paths —
  structurally unreachable by my changes (differential dependency check; stash blocked correctly
  by the shared-tree gate, discriminated by dependency instead).
- owned-paths blocked ts_source.py -> renamed INTO the enforced engine family (extract_*.py) with
  loud disclosure; CTO ruled LEGITIMATE ("renaming a NON-engine file in would be gaming; this is
  not that").

## Compiler Tools

| Tool | Call | Result | Note |
|---|---|---|---|
| comp-blast | 11-table battery + producer + negative, pre/post | PASS | was NOT-FOUND x6+; fact_rps correctly no-consumers-not-provably-zero |
| comp-pipescript | io x3 surfaces post-fix | PASS | silver reads 1:1 with DS S4 SS3 |
| comp-routes | trace getAccountDistribution pre/post | PASS | live URL post-fix; origin-type tag NIT queued |
| comp-build | x3 rebuilds | PASS | 2256 nodes; SHA index 1897/1897 |
| comp-pulse | diff (every commit) + the live stale-heal exercise | PASS | AUTO-REFRESHED 41.4h->0.0h same invocation |
| commit-gate | every commit | PASS | caught 1 real F401 |
| pytest | 3 new suites | 23/23 | + mutant on denylist (load-bearing proven) |

**Gap found:** nerves_lexical.py:321 non-atomic map write (flagged to ~Z, their file); origin-type
tag mislabel (queued); `safe-commit` timeout during concurrent multi-agent pushes left an
ambiguous state once — resolved by reading git state, commit had landed (b6e4a784c).

## Current State / Next

- Bundle: 6 of 9 landed. NEXT: item 7 (comp-constants polyglot + --complete-over against ~Z's
  LIVE data/firm_registry.json; scope filter FIRST — CTO false-FAILed on portal-only mockadv
  exercising preflip; extract_ts_source.py is the polyglot seed; acceptance targets
  firm-config.mjs + firmAccess.ts), then 9 (TRIGGER_LAYER verdict shape), 8 (landed-catalog mode
  default, live pulls per-use word, mode declared), 06-coregen re-fire (report also to CVO~Z), G3.
- Standing at CTO (not urgent): whether the danger map stays a tracked artifact (my comp-iam
  census precedent argues TTL artifacts do not belong in git).
