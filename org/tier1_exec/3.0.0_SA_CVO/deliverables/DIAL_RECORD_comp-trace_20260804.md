# DIAL RECORD — comp-trace — CLOSE, P8 routed (the NAVIGATE-surface spine dial)

**Dialer/Verifier:** 3.0.0_SA_CVO · **Date:** 2026-08-04 ~1500–1535Z (Andrew-present session).
**Program:** toolscape consolidation (C-indexed) — this record is the NAVIGATE-spine fitness
evidence CTO's PRD gates on. **Method:** DIALED_TOOL_FLOW_DESIGN_20260731.md.
**Baselines:** `dial_baselines/comp-trace_P0_20260804.txt` @a4ff948a2 (+ Q5–Q7 this record).

## VERDICT: DIALED-PENDING-P8 — mechanically strong, declaration-poor

**NAVIGATE-spine fitness (the PRD question): YES, with the declaration work as the
consolidation's first worklist.** The walker itself is sound — bidirectional, depth-bounded,
valid `--json` ({query,traces}), honest NOT-FOUND-vs-empty-clear semantics, live staleness
warning. Every gap found is DECLARATIVE (contract, universe, vintage, family rc-consistency),
none mechanical. Universe is BROADER than assumed: gold scripts + functions present under the
`gold:` prefix (2,255 nodes / 2,950 edges spanning gold/s3/lambda/endpoint/eventbridge/component).

| Phase | Verdict | Evidence (exercised) |
|---|---|---|
| P0 | PASS | Units: `.tools/comp-trace` -> `org/modules/graph/cli.py` (trace mode) + TraceGraph + comp-build; cache `.comp-graph/graph.json` (1.56MB, built_at-stamped, ~15min fresh at probe). Baselines Q1–Q7, rc direct |
| P1 | PASS (T4) | Registry `does:` crisp. Docstring teaches DEAD forms (below) |
| P2 | PASS | Single live name; no aliases; T4 names never declared retired (K5-adjacent class) |
| P3 | GAP = T0 | NO output contract (pending :556) — the spine tool renders coverage/plane/exits LOUD UNKNOWN |
| P4 | PARTIAL (T3) | Role vocab in output (FETCHES/COMPONENT/ENDPOINT/GOLD_SCRIPT); `--json` valid; NO provenance header — **built_at EXISTS in the cache and is never printed**; no `--head` (adopt-as-touched, noted) |
| P5 | PASS (data) | Canon exposure minimal: 1 skill mention (cloud-ops), NO CLAUDE.md row (comp-kuzu has one); manifest entry current; T4 found here |
| P6 | PASS (1 skip) | Q1 real walk; Q2 bogus -> rc=3 loud honest NOT-FOUND; Q3/Q4 name-form pair (below); Q6 `--depth 1` bounds (4 lines); Q7 upstream real (3 partner index.tsx FETCH the endpoint). SKIP-WITH-REASON: corrupted-cache probe — single shared cache path, no per-call cache flag observed; corrupting it mid-session breaks every concurrent agent's trace reads. Converted to re-dial trigger 5 |
| P7 | CENSUS, no deletions | graph.json = GENERATED (auto-rebuilt, TTL); baseline.json = HISTORICAL-NECESSARY (comp_marker_read's frozen pre-delta anchor); engine/builder NECESSARY |
| P8 | OPEN — ROUTED | Non-dialer cold descent; seat via CTO/COO |

## Findings

- **T1 (MED — the sharp one): NOT-FOUND declares no universe, no denominator, no near-match.**
  Exercised pair: `A_00.accounts_dimension.py` -> rc=3 "typo? or run comp-build" while
  `gold:A_00.accounts_dimension` -> resolves (multi-match list). A bare-name miss on an EXISTING
  prefixed node is indistinguishable from a truly-absent node, and the error text actively
  suggests the wrong remedies. comp-blast's dial repaired this exact class (its rc=3 prints
  "20480 nodes (CANONICAL KUZU GRAPH)" + universe declaration + suffix-tier resolution).
- **T2 (MED, family-consistency): ambiguous subject returns a disambiguation list at rc=0**;
  comp-blast rules the same situation rc=5 AMBIGUOUS-SUBJECT and refuses. The two tools about to
  share one NAVIGATE surface disagree on ambiguity semantics; a scripted caller cannot
  distinguish list-vs-walk without parsing stdout.
- **T3 (MED): vintage exists, is never surfaced.** The cache carries `built_at`; STALE_NODE_WARN
  fires on SHA drift (23 nodes at probe time) — but no provenance header prints on any walk.
  Two vintage axes (cache TTL age vs indexed-SHA drift), neither declared. The comp-kuzu
  provenance-header contract is the family reference.
- **T0 (prioritization): the NAVIGATE spine has NO output contract** — strongest argument that
  spine tools lead the 49-pending backfill; this record is its declare-by-exercise material.
- **T4 (LOW): engine docstring teaches dead invocation forms** (`opal-trace`/`opal-blast`
  wrappers — neither exists on disk, neither declared retired).

## DECLARED RE-DIAL TRIGGERS

1. Output-contract declaration landing (converts T0; verify against this record's probes).
2. NOT-FOUND / ambiguity repair landing (T1/T2 — verify near-match, denominator, rc semantics).
3. Provenance-header addition (T3 — verify both vintage axes print).
4. Engine change >~50 lines in cli.py trace paths / TraceGraph; comp-build schema change.
5. Any per-call cache-path flag landing (converts the P6 corrupted-cache skip).
6. The PRD's NAVIGATE surface first composing over comp-trace (the consolidation event itself).
7. P8 descent completion.

— 3.0.0_SA_CVO

## P8 FOLD -- independent descent COMPLETE (~D @150dd98d7, 2026-08-04 ~1650Z); trigger 7 CONSUMED

Descent: 10 cold captures. Blind convergences STRENGTHEN the record: T2 (rc=0 ambiguity)
reproduced verbatim cold; the T4 taught-form class reproduced as a sharper instance; the P6
NOT-FOUND verdict confirmed cold ("exemplary -- exactly the discrimination kuzu's raw 0-rows
lacks"). **Non-noticing evidence FOR T3:** ~D never missed the absent provenance header until
reading this record -- the vintage axes are invisible exactly when nobody looks. New findings:

- **T5 (MED, descent-found, entry-surface): the bare-call usage text teaches the underlying
  cli.py subcommand form which the shim BREAKS** -- `comp-trace trace <q>` errors, and bare
  `comp-trace trace` consumes the word "trace" AS the query (grounded by exercised triple).
  Same law as T4, sharper instance: it is the FIRST output a cold user ever sees.
- **T6 (MED, descent-found): the exact canonical id cannot self-select** --
  `gold:A_00.accounts_dimension` still multi-matches its function children; no exact-match
  selector documented. DISTINCT from T2: this input is not ambiguous, it is the canonical id.
- **T7 (datum, descent-found): 4 indexed lambda sources now `<missing>` on disk** (finbert,
  mdpf-manifest, schwab-bronze-freshness, security-sweep-daily) -- deletion-residue inside the
  23-node drift set my P6 counted but did not decompose. Plus: the drift warn's "Rerun:
  comp-build" advice is redundant with the auto-rebuild that follows it.
- **Cross-instrument (shared with kuzu record): scope asymmetry, no cross-pointer** (gold_dispatch
  trace-only; AWS planes kuzu-only). NAVIGATE-consolidation material, routed CTO.

## RE-DIAL (triggers 1/2/3 fired) -- ~F fixes @ffb41a849 CLOSED-VERIFIED 2026-08-04 ~2325Z

My own exercises, rc direct: **T1 CLOSED** (the exercised pair now discriminates: rc=3 +
"2252 nodes (HEAD-PINNED TRACE GRAPH)" + universe declaration + gold:A_00.accounts_dimension as
the FIRST [UNVERIFIED] near-match). **T3 CLOSED** (provenance header both axes on stderr, every
walk; --json stdout stays pure {query,traces}). **T5 CLOSED** (bare call teaches the shim form,
comp-trace-prog usage rc=1; the cli.py subcommand form gone). **T6 CLOSED** (--exact
self-selects: zero multi-match, single-node walk from the canonical id; miss = rc=3 naming the
mode). **T0 PARTIAL: RESTORE-IN-FLIGHT** -- the ~B/~F shared-file interleave left comp-trace's
contract entry momentarily neither declared nor pending at @ffb41a849; follow-up commit on ~B's
ACK; I verify the restored block on landing. T2 correctly untouched (PRD-gated; diff grepped).

## T0 CLOSED -- restore @3293a0cda verified 2026-08-04 ~2340Z

Contract block present (:513, position preserved, grain=field intact), coverage line carries the
LIVE-denominator promise, and the dial's cross-instrument scope-asymmetry finding is woven in as
a DECLARED blind spot -- the record's own finding became the contract's honesty line. Gate
stable: declared 26 + pending 44 over 70. The comp-trace dial is now FULLY CLOSED, no armed
residuals. (Session note: third shared-YAML interleave tonight disclosed by ~F -- a comp-heat
entry rode their commit, true author routed via COO; comp-heat now declared-ahead-of-landed
while its engine edits sit uncommitted at the heat-cluster seat -- transient mid-build state,
verify armed on that seat's landing.)
