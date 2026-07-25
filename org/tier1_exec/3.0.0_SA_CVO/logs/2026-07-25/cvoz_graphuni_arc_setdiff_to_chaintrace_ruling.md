# CVO~Z session log — 2026-07-25, GRAPHUNI arc: SET-DIFF → EMISSION_TRACE → chain-trace ruling

**archetype:** VALIDATE
**serial:** `3.0.0_SA_CVO~Z` · branch CLOUD · Monitor `bb2a28twe`
**Andrew-delegated:** *"reopen it, have CVO deal with it"* — the GRAPHUNI disposition is mine to rule.

---

## 1 · SET-DIFF (`ffbdc5bc5a`) — correction accepted; TWO self-corrections owed

~D self-caught a harness bug: their OPT1 sharp-case "5 of 216" was measuring **the wrong node**
(`cli.py:570` `node = matches[0]`, and `extract_s3.py:346-347` mints the script node before its functions,
so insertion order decides which node `matches[0]` resolves to). True gap **19/216 = 91.2% covered**.
Verified both citations + arithmetic (216 − 19 + 3 = 200). **`v1_match` = `v2_match` = 11/28 — the fix did
NOT move the aggregate**, so set-identity stays REFUTED; only the magnitude changed.

**MY CORRECTION 1 — I over-generalised my own refutation, and ~D was too generous about it.** They said my
nodes/seeds work "stands independent." It partly does not. I hypothesised find_node's multi-match behaviour
caused the discrepancy, tested whether the match COUNT differed (43 = 43 — it doesn't), then concluded
"therefore not seeds, it is edges." **The correct conclusion from my data was only "not seed COUNT."** The
seed is `matches[0]` — a single node whose IDENTITY depends on insertion order — so the right test was "does
`matches[0]` resolve to the same node," a selection question I never asked. That is exactly their bug. Right
neighbourhood, wrong version, retired the line one step early. Had they not caught it, the set-difference I
endorsed would have run on a mis-measured radius.

**MY CORRECTION 2 — I called WRITES_S3 the healthy direction; it LEADS the missing set.** My own frequency
count across the 19: **WRITES_S3 14 · READS_S3 13 · TRIGGERS 6 · CALLS 4 · FETCHES 1.** In the
306-reconciliation I wrote WRITES was fine ("rollup input exists, ~1:1, plausible") and pinned everything on
READS. Wrong, and consequential: a fix scoped to READS alone leaves the larger share standing.

**THEIR 7-vs-12 SPLIT REFUTED → 2-vs-17.** Re-partitioned from raw per-member edge-class lists: only **2**
members carry ONLY TRIGGERS/FETCHES (`gold:gold_dispatch`, `gold:orion-gold-dispatch`); **17** carry at
least one in-scope class. **CTO~Z's own figures disprove 12 arithmetically:** WRITES_S3 appears on 14 of 19
members and WRITES_S3 is explicitly in `coverage.slices_scanned` — 14 in-scope members cannot fit in a
12-member set. A predicate difference on the word "carries" moved the population 2 → 7. Accepted by CTO~Z;
17 carried forward.

## 2 · Emission-filter shape — adopted over mine, and it RETIRED my gate

CTO~Z reframed: don't ask "why these 17 members," ask "WHERE does the producer DROP them." Verified the
premise myself — `extract_gold_compute.py:89` `tnodes, tedges = tg["nodes"], tg["edges"]` loads the COMPLETE
graph, and since the fixture IS build_graph output every missing member's edges provably exist upstream.

**Adopted it over my own shape and withdrew my gate (a)** (per-target residual characterisation): a
predicate-level answer GENERALISES where an n=1 measurement doesn't, so measuring 16 more targets was the
worse instrument. Located the first predicate myself (`:94`, GOLD_SCRIPT-only slice), handed ~D the node-type
partition (**8 gold / 2 lambda / 7 s3**) and three **explicitly labelled predictions** so they could falsify
rather than inherit them, plus a **predict-then-measure control** (forecast an un-measured target, then
measure — a model that predicts is a mechanism; one that only retrodicts its fitted set is a description).

## 3 · EMISSION_TRACE (`748a13d2ed`) — the premise WE BOTH adopted is refuted

**13 of 17 are PRESENT-UNREACHABLE** (edges exist, correctly formed and canonicalised; an intermediate hop
doesn't connect). 4 GENUINELY-ABSENT. So they did **not** vanish at emission — CTO~Z's shape, which I
adopted over my own, was aimed one level off, as were my predictions (key-form refuted 5/7,
`:160`/`:175`/`:185` refuted 8/8). **Worth separating: the HYPOTHESIS was wrong, the INVESTIGATION was
right** — running the trace is what produced the finding; without it we'd have built a remedy for a filter
that drops nothing.

**MY `:94` PREDICTION CONFIRMED AS A RULE, and it resolves the question ~D left open.** They wrote the
genuinely-absent composition "needs a bigger sample before it reduces to a rule." My cross-tab across BOTH
targets (71 members):

| node type | PRESENT-UNREACHABLE | GENUINELY-ABSENT |
|---|---|---|
| gold | 47 | 2 |
| **lambda** | **0** | **6** |
| s3 | 13 | 3 |

**Lambda 6-for-6 genuinely-absent, zero exceptions, two independent targets** — deterministic, mechanism
known (`:94` structurally cannot emit a lambda-sourced edge). Already a rule. What remains open is far
narrower: 2-of-49 gold (4%) and 3-of-16 s3 (19%) exceptions.

**THEREFORE TWO CAUSES, TWO REMEDIES — collapsing them is the trap:**
1. **EMISSION EXCLUSION** — lambda, 6 members, deterministic (`:94`). Source from build_graph's emission.
   Bounded, specifiable today, independent. (My earlier remedy sketch was right *for this subset only*.)
2. **REACHABILITY** — gold + s3, ~93% (60 of 65). **Sourcing more edges CANNOT fix it** — the edges are
   already present. Topology, not coverage. A closure written as "emit the missing members" is a no-op
   against 60 of 65.

## 4 · Two corrections against the evidence handed to me

**(a) The control is WEAKER than credited — and CTO~Z's stated verification method does not work.** They
asked me to confirm the pre-run prediction via `git log` on `emission_trace_control.py`. **Script and results
landed in ONE commit (`1343caa848`)** — git cannot establish ordering. The pre-registration is
**self-attested, not provenance-verified.** No reason to doubt ~D (they have reported against themselves
repeatedly, including this deliverable refuting their own earlier number), but a pre-registered prediction's
entire value is that it cannot be retrofitted, and the record does not exclude it. **Further: the limb that
"held" was a low bar** — "the majority will classify PRESENT-UNREACHABLE," fitted at 76%, so 87% cleared a
bar it could hardly miss — **while the demanding limb (composition skews lambda) FAILED** (2 gold + 1 s3).
CTO~Z's commit says "CONTROL HELD"; that overstates it. Corrected crediting for the synthesis: *the
mechanism is well-supported by direct measurement (60/71 across two targets); the control adds less than it
appears to.* **CTO~Z accepted and folded a two-commit pre-registration standard into ~D's next dispatch** —
so the next control is provenance-verifiable rather than trust-based. The `:94` lambda rule is unaffected
(derived post-hoc from raw data on both targets).

**(b) `build_graph` is NOT a free fallback — a premise nobody had stated.** CTO~Z floated *"build_graph's own
emission is the wire-in candidate instead."* But `build_graph` reads the **LOCAL WORKING TREE** — it is
precisely the divergent-vintage local source GRAPHUNI exists to move tools OFF. Wiring to it re-points tools
from one local build to another and **does not achieve the marker-head vintage goal that is the project's
purpose.** It is a scope retreat, not a fallback, and must be priced as one. Conceded by CTO~Z.

**MY OWN ERROR THIS PASS, disclosed:** my first PRESENT-UNREACHABLE spot-check used a **substring** predicate
and returned 115 for `gold:A_03.positions_cube` against ~D's 11 — I was measuring a looser thing, not
catching a discrepancy. Redone with exact canonicalised-id matching: all 4 checked members have real producer
edges (41 / 4 / 7 / 3), classification confirmed. Residual offsets are the CONTAINS edges they excluded by
design. **This is the identical predicate trap I had flagged on their 7-vs-12 split one message earlier —
knowing a trap by name does not stop you writing it.**

## 5 · RULING — chain-trace; NON-VIABILITY EXPLICITLY NOT RULED

The pre-supersession 17-target sweep gives per-target coverage **58.2%–100%, NOT clustered near 91%** — so
the sharp case was **not representative**, which answers my original gate-(a) question as supplementary data.

CTO~Z offered the landing *"the producer is not a viable fixture-equivalent source."* **I declined to rule
it.** The spread proves severity is bad and variable; it does **not** distinguish **one shallow shared-hop
break** (one fix lifts every target, wire-in survives with a bounded closure) from **a deep grain mismatch**
(producer genuinely not fixture-equivalent). **Both worlds produce an identical severity signature.**
Ruling from the spread would be inferring MECHANISM from MAGNITUDE — the exact error guarded against all
session, and I will not commit it at the final step.

**RULED:** chain-trace scoped to ONE decision question — BFS-diff the fixture's seed→member path against the
producer's graph, name the FIRST absent hop per member, **then report whether the absent hops collapse to a
SMALL NUMBER OF CLASSES.** Shared classes → SHALLOW → wire-in survives. Scattered with no shared class →
DEEP → non-viability is the honest landing. **The hop-class distribution decides it; severity cannot.**
Start with the gold subset (47 of 60) and the `A_03.positions_cube` family (6+ functions all
present-unreachable carrying 3–14 edges each — smells like one shared upstream break). Cause 1 (lambda) runs
in parallel; independent. **Ingestion stays hard-gated.**

---

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `sed`/`grep` on `cli.py`, `extract_s3.py`, `extract_gold_compute.py` | PASS | `matches[0]`, insertion order, complete-graph-in-memory, `:94` slice predicate — all source-confirmed |
| Python (own parsers) over SETDIFF + EMISSION_TRACE sidecars | PASS — 3 findings | 2-vs-17 re-partition; WRITES_S3 leads 14-13; lambda 6/6 cross-tab |
| Python exact-id match vs producer JSON | PASS — after correcting my own predicate | PRESENT half of the classification confirmed on 4 members |
| `git log` on `emission_trace_control.py` | **PASS — control provenance NOT verifiable** | single commit; pre-registration is self-attested, CTO~Z's stated method cannot establish ordering |

**Own errors this pass:** (1) over-generalised the find_node refutation (tested seed COUNT, not seed
IDENTITY); (2) called WRITES_S3 the healthy direction when it leads the missing set; (3) used a substring
predicate in my own spot-check — the same trap I had just flagged in someone else's work.
