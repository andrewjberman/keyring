# comp-blast output structures, walked one by one — and PHANTOM-CONSUMER is a control that cannot fail

**Seat:** `3.0.0_SA_CVO`. **Date:** 2026-08-06 ~21:30-22:15Z. **Andrew-directed** walkthrough:
*"assess if those output structures are actually decision useful on their own in their current state."*
**Method:** every structure exercised. Two findings source-confirmed in `cli.py` /
`comp_blast_universe.py` / `trace_graph.py`, not inferred.
**Companion:** `S4_comp_blast_verification_for_F1_20260806.md` @6f8da8869.

## THE HEADLINE — B4: the phantom sweep is TAUTOLOGICALLY EMPTY

```
PHANTOM-CONSUMER SWEEP: 0 producers with zero EXTRACTED-edge consumers of 926 checked
```

**That zero is not a fact about the estate. It is a fact about the query.** Source-confirmed:

| where | what |
|---|---|
| `comp_blast_universe.py:453` | `PRODUCER_EDGE_TYPES = (WRITES, WRITES_S3, PROJECTS_TO, TRIGGERS, SFN_INVOKES, S3_INVOKES, EVENT_INVOKES, SNS_INVOKES)` |
| `comp_blast_universe.py:478` | *"a producer is a node with at least one outbound PRODUCER_EDGE_TYPES edge"* |
| `cli.py:940` | phantom test: `if not (g.downstream(id, max_depth=1) or g.upstream(id, max_depth=1))` |
| `trace_graph.py:225-243` | `downstream()` walks `self._forward.get(current, [])` — **ALL outbound edges, no type filter** |

**The population is defined as "has ≥1 outbound edge." The test asks "has 0 outbound edges."**
Every member of the swept territory necessarily has ≥1 outbound edge, so `downstream(depth=1)` is
never empty, so the condition is **always False**, so `phantoms` is **always `[]`**.

> **A CONTROL THAT CANNOT FAIL IS NOT A CONTROL.** The sweep whose entire stated purpose is finding
> zero-consumer producers, run over a population defined by having an outbound edge, must return 0
> **by construction** — and it reports that 0 in the same prose it would use for a genuinely clean
> estate.

**AND IT WAS BUILT BY COMPOSING TWO CORRECT DECISIONS.** The both-direction dependent set
(`cli.py:1119-1127`) is a real fix for a real incident — `endpoint:getPlatinumPartnerAnalytics`, 8
live callers, 0 downstream, previously declared **PHANTOM-CONSUMER**, *"a deletion verdict on a live
endpoint."* The producer predicate is a reasonable territory definition. **Neither is wrong. Their
composition is vacuous.** That is the pattern worth carrying: *two individually-correct decisions can
compose into a control with no failing case, and neither author is in a position to see it.*

The output is otherwise scrupulous — it declares itself a LOWER BOUND and calls its results
*"CANDIDATES to verify, not confirmed orphans."* **It can never produce a candidate to verify.**

**Second B4 defect: the documented invocation does not run.**
`comp-blast --check-consumers --all-producers --pipeline all` → **rc=1**, argparse
`error: the following arguments are required: query`. A sweep mode that requires the positional it
exists to replace. It runs only with a throwaway positional (`comp-blast x --check-consumers
--all-producers`) which is then ignored. *(rc=1 is correctly NOT a verdict per the tool's own
convention — the failure is loud, which is the right direction.)*

## The rest, by structure

| | verdict |
|---|---|
| **B1** radius + caller chain | **useful, three presentation defects** |
| **B2** `--direction up` | **clean** — suppresses radius, shows caller chain only, no surprises |
| **B3** `--check-consumers` | **useful; exit-code discipline is a model** |
| **B4** phantom sweep | **BROKEN two ways** (above) |
| **B5** `--compare` | **works**; one denominator inconsistency |
| **B6** `--overlap-sweep` | **best evidence in the tool, unusable ranking** |
| **B8** `--json` | **PASS — no finding** |

### B1 — three presentation defects, no computation defect
- **57% preamble.** 25 of 44 lines before `BLAST RADIUS`. The provenance is load-bearing; the ratio
  still governs whether a tool gets reached for mid-change.
- **CALLER CHAIN MIXES GRAINS.** `CW_ALARM` + `SCHEDULE` (real resources) summed with
  `motif:a-access [C2Motif]` and `system:object-data [C3System]` into **"6 caller(s)."** If the
  question is *what triggers this*, the answer is **2**. Rule 24 (ii) — a count across
  incommensurable things.
- **B1 and B3 print different counts for one node with no reconciliation.** Radius lists 4 and warns
  `affects >= 4`; B3 says `10 dependent(s)`. **Both correct** — B1 shows downstream, B3 evaluates the
  full dependent set — and **nothing in either output says so.**

### B3 — the exit-code discipline is a model; the help text is the defect
`rc=0` CONSUMER-OK / `rc=4` PHANTOM / **`rc=1` explicitly NOT a verdict, "it means the tool failed."**
That is failure≠zero implemented where a gate consumer actually reads it. Passing `--direction` emits
a stderr NOTE that it *"governs DISPLAY only; the consumer verdict is evaluated over the full
dependent set in both directions"* — making the false-orphan **structurally impossible to produce via
a display flag.**

⚠ **`--help` still documents the PRE-FIX contract** (*"Exit 0 if node has >=1 **downstream**
consumer"*). The code deliberately evaluates both directions because **this graph mixes edge
conventions** — WRITES points producer→artifact, CALLS/FETCHES point consumer→producer — **so
"consumer" is not a direction.** I read the help as the contract, measured five nodes, got exact
confirming arithmetic, and was one step from filing a false defect against a correct fix. **On a
verdict that maps to deletion evidence, a stale help string is not cosmetic.**

### B6 — the tool prints the discriminator and does not use it
Per-row evidence is the richest in the estate: blast sizes, raw *and* weighted jaccard, mass,
containment, **`shared BY VERB`**, `!! SHARED WRITE TARGETS` flagged separately, every shared consumer
annotated with estate-wide `df`.

**And the visible ranking is 100% artifact.** All 15 shown pairs are EC2-instance × EC2-instance
(**30 of 30 subject lines**), dominated by `CONTAINS=807` — account membership, not production.

**Mechanically why, and it is structural: all 15 score `WEIGHTED 1.000`.** When `shared == union`,
weighted jaccard saturates at 1.000 **regardless of idf weights** — the ratio maxes out before
specificity can apply. **The idf damping, the tool's whole defense against generic consumers, is
inert exactly where the ranking puts its top results.** Mass does not help (4,510). `shared BY VERB`
names the cause in every row and never reaches the score.

Net: 21,412 candidates, 15 visible (**0.07%**), and the visible window is entirely structural.
**Local fix:** discount membership verbs, or refuse to rank identical-radius pairs.

### B5 — one denominator inconsistency, in a single output
Territory block: `N: 926 node(s) (from 926 role-matched of 20585)`. Two lines later:
`population: 927 producer nodes`. **926 vs 927 in one run.** *(The 20585-vs-20587 universe difference
across runs is legitimate — the graph auto-rebuilt on HEAD advance and the provenance header
discloses it.)*

### B8 — PASS, and I checked rather than asserted
`--json` is valid JSON: `consumers / node_type / provenance / source`. I suspected `consumers` was
downstream-only, which would have let a machine consumer rebuild the false-orphan class. **It is
bidirectional** — S3_BUCKET/IAM_ROLE/SNS_TOPIC/IAM_POLICY **plus** CW_ALARM/SCHEDULE/C2Motif/C3System,
all 10 dependents grouped by node type. Consistent with the verdict logic. Carries `provenance`.
**No finding.**

## What routes where

| finding | severity |
|---|---|
| **PHANTOM-CONSUMER sweep is tautologically empty** | **the one that matters** — the orphan detector cannot detect |
| `--all-producers` documented invocation fails (rc=1) | real, trivial fix |
| `--check-consumers` help documents the pre-fix contract | **real, and it nearly produced a false defect report from me** |
| B6 ranking saturation at `shared == union` | real, local fix |
| B1 caller-chain grain mix; B1↔B3 unreconciled counts | presentation |
| B5 926-vs-927 in one output | minor |

**Nothing here is a computation defect.** comp-blast's trust discipline — three exercised refusal
modes, declared territories with full derivation chains, unprompted blind-spot statements, a
mutation-proven suppression counter — remains the strongest I have measured in this estate. **The
defects are a vacuous control, a stale doc, and a ranking that saturates.**

-- `3.0.0_SA_CVO`
