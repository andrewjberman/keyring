# SPLIT — comp-tool refinements: `3.0.0_SA_CVO` / `3.0.0_SA_CVO~B`

**Authority:** Andrew-direct, CVO terminal, 2026-08-05 — CVO~B was spawned to assist with tool
fixes/registrations; split the refinement work between the two seats.
**Purpose (his):** fix these tools so the input we give Kimi *"actually uses the cool stuff we
built, not just obvious stuff"* — deterministic high-signal strata as the basis for real insight.
**Companion:** `SPEC_kimi_call_subdivision_and_insight_strata_20260805.md` @58505c291 (the strata
this work must make trustworthy).

---

## The cut: SIGNAL layer (me) / TRUST layer (~B)

Two questions at the same grain, mutually exclusive, one intent each:

| | Question | Seat |
|---|---|---|
| **SIGNAL** | Does this tool *emit what a stratum needs* — the disagreement rows, a denominator, an input vintage? | `3.0.0_SA_CVO` |
| **TRUST** | Is this tool *honest and registered* — does it declare what it does, and does it hold up to a cold reader? | `3.0.0_SA_CVO~B` |

## Why P8 goes to ~B by CONSTRUCTION, not by preference

Every dial carries a **P8 independent descent**: a NON-DIALER cold-exercises the tool from its docs
alone. **I dialed all six. I am structurally disqualified.** `DIAL_RECORD_comp-pipescript` states it
in its own words: *"P8 independent descent | NOT RUN — by definition needs a non-dialer."*

This is the builder-verifier seam applied to my own work. A dialer running their own P8 measures
whether the tool matches the mental model they built while dialing it — which is exactly the thing
P8 exists to test. **~B is the only seat that can produce this evidence.**

Measured state (denominator: 6 dial records): P8 **OPEN — ROUTED** on comp-depth, comp-heat,
comp-kuzu, comp-trace; **NOT RUN (needs non-dialer)** on comp-pipescript; comp-blast carries
"Residue (open, owned)" instead — ~B confirms its P8 state rather than assuming it.

---

## MY HALF — SIGNAL (strata-critical, sequenced D-first per the spec)

| # | Tool | Work | Feeds |
|---|---|---|---|
| S1 | `comp-estate` | **Semantic-vertical attribution — THE substrate.** 10 of 357 paths chain-resolved today; 318 to `area:*` fallback. This is the direct cause of the proposal class Andrew rejected twice. | **Group D** (lifts A/B/C) |
| S2 | `comp-heat compare` | Verify CONVERGING/DIVERGING/PARALLEL + half-life emits a *rate* a stratum can carry; close **CH-4** (stale reciprocal link) | Group B temporal |
| S3 | `comp-cochange` | Verify `matrix`/`pair` at `--grain type\|serial` emits co-movement with shared-denominator | Group B behavioral |
| S4 | `comp-blast --overlap-sweep` | Verify pairwise overlap emits the *disagreement* cells (coupled-but-one-side-changed; co-moved-with-no-edge), with population denominator | Group B structural |
| S5 | `comp-pipescript deployed` + `comp-heat drift` + `comp-freshness` | Verify the propagation ladder rungs emit per-rung denominators; **trading-day basis mandatory** on freshness | Group A |
| S6 | `comp-heat freshness` cold-subtrees × `comp-estate --fe-reachability` | Verify the cold-AND-cited cell is computable (the 08-04 dated-briefs reversal cell) | Group C |

**Why these are mine:** I authored the stratum contract, I hold the dial context, and every item is a
judgment about whether an emission is *decision-useful* — which is the verification question, not a
registration one.

## ~B's HALF — TRUST

| # | Item | Scope |
|---|---|---|
| T1 | **P8 independent descents** | The dialed set (6 records). Cold-exercise from docs alone; every point where the doc misleads is the finding. **~B is the only seat that can do this.** |
| T2 | **11 standing subcommand-drift rows** | `comp-chainrun`(+2), `comp-constants`(+1), `comp-coverage`(+1), `comp-drift`(+1), `comp-iam`(+2), `comp-pii`(+3), `comp-routes`(+3), `comp-shell`(+1) … — re-derive from `comp-manifest-check completeness`, never from this list |
| T3 | **Output-contract backfill** | 44 pending of 70 tools_index tools. **PRIORITIZE the strata-feeding tools** (S1–S6 above) — those contracts are what let a stratum declare its denominator+vintage. Includes **DEPTH-0**. |
| T4 | **comp-iam residuals** | multi-account loop unbuilt (self-declared single-account); `_provenance.py:405` hourly-vs-event-driven contradiction NOT-REACHED |
| T5 | **Self-route WARNs** | ~11 tools surface only in comp-which's near-tie list, never rank-1 — a routing tool that cannot rank-1 its own members is a discoverability defect |

**T3 is the seam between our halves and it runs ~B → me:** ~B backfills the contract, I verify it
carries what the stratum needs. Neither of us marks our own work.

---

## The standing rule for both seats

**A tool feeding a stratum must be able to distinguish "nothing to report" from "I found nothing
because I was pointed at the wrong universe."** Several of these returned clean zeros for whole
classes of question on 08-04. Andrew has ruled we throw every angle at the wall and filter on real
output — correct — but that means a broken instrument would produce **confident wrong insight**,
strictly worse than today's obvious-but-harmless output.

Same shape as the frozen-corpus defect found this morning: `degraded_sources: []` was the strongest
possible all-clear precisely because presence was the only predicate. **Do not rebuild it one layer
up.**

## Boundaries

- Neither seat certifies its own work. ~B's P8 findings land at me; my S-items get ~B's cold read.
- Neither seat edits `estate_report_runner.py` — CTO~B's lane.
- Naming acts (e.g. comp-pipescript **F2** universe) stay open at Andrew; neither seat resolves one.

-- 3.0.0_SA_CVO
