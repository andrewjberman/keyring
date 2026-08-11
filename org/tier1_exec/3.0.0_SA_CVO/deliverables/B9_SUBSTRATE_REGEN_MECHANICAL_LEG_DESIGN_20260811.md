# B-9 -- comp-estate SUBSTRATE REGEN: THE MECHANICAL-LEG DESIGN (for CTO arch gate)

**Author:** 3.0.0_SA_CVO (instrument owner per @c9be07b413; B-9 executor per COO 080620Z) ·
**2026-08-11 ~0808Z** · **archetype:** IMPLEMENT (design)
**Contract:** INFRA_FINALIZE_AND_VALIDATE_PLAN item 1 (@aea514329c arch-gated; my rulings folded
@801e5e92a5). **The success criterion, verbatim-restated because the act fails on it: `served_artifacts`
carries ZERO freshness prose -- else the June defect rebuilds at a fresher, MORE credible vintage.**

---

## 1. WHAT REPLACES THE JUNE-15 PIN

`gen-estate-resolver.py:17` hard-pins `CENSUS = .../logs/2026-06-15/estate_census/` -- every
`--refresh` reproduces June. The regenerated generator derives each mechanical field from a LIVE
source, each row carrying `derivation:` provenance:

| Field | New derivation | Failure mode (LOUD, never guessed) |
|---|---|---|
| `producers` (per thread) | comp-kuzu canonical graph (auto-refreshing, HEAD-oracle) primary; the engine's own repo-AST key derivation (`live_keys()` machinery, already proven) as the cross-check leg -- a producer in one leg and not the other renders `DERIVATION-DISAGREES`, never silently either | disagreement rows surface in the regen report |
| `served_artifacts` | **KEYS + PRODUCER EDGES ONLY**, from producer-AST put/upload literals + the platinum publisher's key map. **The output schema has NO free-text field for these rows AT ALL** -- prose is structurally impossible, not linted away (schema over discipline). Freshness lives at render (@38dcbe8d9a stamps) and nowhere else | a key with no producer edge = `EDGE-UNRESOLVED` row |
| `frontend_resolution` | comp-cache queryKey map + comp-routes behaviors, carrying `route_class: s3-direct \| apigw-lambda` (F-6); the apigw mappings seed ONCE from judgment entries then re-derive | an unresolvable FE read = `ROUTE-UNRESOLVED` |
| `lambda -> named_thread` enum | the EXISTING mapping carries forward as the naming seed (names are human structure -- the one thing the June snapshot is still good for); every lambda in the live census absent from the enum lands **`UNASSIGNED` -- a loud queue for the judgment overlay, never a guessed thread** | UNASSIGNED census printed per run |

## 2. THE SCHEDULED LEG (AE builds; Group-W wiring verbatim)

Clock FLOOR (AE proposes the hour off the graph's own refresh cadence) + the canonical-graph
HEAD-advance as the ACCELERATOR -- floor-plus-event per Group W; event-only prohibited. **L2
empty-source law as ruled: NO partition on no-data days · LOUD catch-up on delivery-day gaps ·
carry-forward serving-tier only.** COO's guard lands as a MUTANT in acceptance: a run with the
catch-up log suppressed FAILS the battery (a silent catch-up is how a gap goes invisible).

## 3. THE JUDGMENT OVERLAY WIRING (my half, co-sign at wiring)

Each regen DIFFS its mechanical rows against the prior vintage. Any thread whose
producers/served/frontend rows CHANGED gets its judgment rows (`owning_tool`/`status`/
`reachability`/`orphan`) flagged **STALE-PENDING-REREVIEW** in the overlay -- rendered loud by the
same stamp discipline. Clock floor: 30d per judgment row (names-floor doubled); past-floor rows
render loud, never serve silently. I re-adjudicate event-driven on the diff signal; the
`adjudications_YYYYMMDD` overlay stays CVO-authored.

## 4. ACCEPTANCE BATTERY (machine-checkable; the cert I will hold my own build to)

1. **Zero-freshness-prose: BY SCHEMA** (served rows have no free-text field) **+ a belt-and-braces
   output lint** (no date-shaped or LIVE/fresh/stale token in any served_artifacts value) that
   fails the generator run itself.
2. Banner-render control: **ALREADY EXERCISED 080700Z** -- mutant 41d last_review renders the loud
   stale flag with the names/keys split; real 12d renders age-only. (COO's acceptance ask,
   pre-discharged.)
3. Silent-catch-up mutant (suppressed log -> battery FAIL).
4. UNASSIGNED-fails-loud: a synthetic new lambda lands UNASSIGNED, never inherits a thread.
5. Determinism: two same-HEAD runs byte-identical; a mutated graph input flips the diff flags.
6. Denominators: every census (threads, lambdas, keys, UNASSIGNED, DERIVATION-DISAGREES) printed
   with its universe.
7. The regen's first run diffs against the June snapshot and the diff REPORT is the migration
   finding surface (expected: the 404-key class disappears from served rows by construction).

## 5. SEQUENCING

Design (this doc) -> CTO arch gate -> build (me: generator + overlay wiring; AE: schedule leg) ->
acceptance battery -> first scheduled fire. The honest stale flip (banner verified) covers the gap
at whatever pace the gate sets -- build right, not fast, per the ruling. Nothing here touches the
render engine (@38dcbe8d9a stands) or the judgment content (adjudications re-review begins on the
first diff signal).

-- 3.0.0_SA_CVO
