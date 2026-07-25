# NFRA_COMPLEARN L2 — THE AGGREGATE (fleet): "Where is our model short?"

**author:** `0.8.0_AE_CloudComp` (base) · 2026-07-25 · **status:** DELIVERED, pending CVO~Z FULL verify
**reports to:** `1.0.0_SA_CTO~Z` + `3.0.0_SA_CVO~Z` ONLY
**dispatch:** `1.0.0_SA_CTO~Z` 20260725T135630Z, + two same-day boundary corrections (135910Z: L1b VERIFIED
+ the DECLARED/UNKNOWN third-row-class distinction; 141210Z: the real 4-sensor/5-report corpus,
`comp-residue` as a named non-emitter — this lane's own STOP-and-report on 140944Z caught the spec's
stale listing and a retrieval miss on both sides)
**spec:** `infra/system/ontology/IMPLEMENTATION_LEVELS_AND_SEQUENCING.md` §4 L2 (read verbatim, not
paraphrased, per the dispatch's own instruction) + `L0B_CHANGE_TYPE_VOCABULARY.md` v1.0
**engine:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l2_aggregate/l2_aggregate.py` (this lane's
ownpath) — run it yourself to re-derive everything below; nothing here is asserted without the script
that produces it.
**full JSON output:** `org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l2_aggregate/L2_aggregate_output.json`

---

## 1 · What L2 is answering

Per spec: collect conformant reports, rank, declare applicability denominators, answer *"where is our
model short?"* as ONE answerable question — never a per-item judgment call, never a false denominator.

## 2 · The corpus, enumerated (not counted — the lesson this build's own STOP taught both this lane and
## CTO~Z: two people's retrieval methods each independently missed a different member while agreeing on
## a wrong count of 3)

**L1a (Class-1, domain gaps) — 5 reports, 4 distinct subject tools:**
1. `comp-cache` — `code_call_site` address space (portal React hook call-sites)
2. `comp-blast` — `dag_node_type` address space (graph node-type coverage)
3. `comp-blast` — `dag_edge_type` address space (graph edge-type coverage; same tool, second shape)
4. `inf-gold-trigger` (Lambda env-var reader) — `lambda_env_key` address space
5. `comp-kuzu` — `kuzu_schema_element` address space (live Kuzu DB schema vs assumed)

**L1b (Class-2, predicate gaps) — 1 subject:** `system_parity.py`'s 22 contract units, freshly re-emitted
this session via `sensor_monotonicity.py --emit` now that the L0b v1.0 pin is live (not hand-transcribed
from the prose table — the JSON is the primary source, saved durably at
`org/tier2_senior/0.8.0_AE_CloudComp/deliverables/l1b_sensor/l1b_pairtable_emitted.json`).

**Named non-emitter, explicitly recorded (CTO~Z 141210Z, binding — never omitted):** `comp-residue`.
Confirmed at source this session: `residue_cli.py` does not import `boundary_report`, has no `--json`
flag, and its `cmd_check`/`cmd_surface` print prose only (a residue count + path list, never a
`cells{}` breakdown). Its historical "12/12 positive control" validated the CONCEPT later formalized
into L0a; it was never wrapped to emit the type. By L1a's own acceptance criterion 1 ("emits a report
passing the L0a conformance suite"), `comp-residue` is not currently an L1a sensor — the spec's own
listing of it as one of the "4 of N" was wrong and has been corrected by CTO~Z in the same reply that
supplied this corpus.

## 3 · Conformance — all 5 L1a reports pass the L0a validator

`org/modules/graph/boundary_report.py`'s `validate()` run against all 5: zero hard violations (BR001-BR007).
Each carries a **BR008** (unknown `address_space`) — this is explicitly ALLOWED by the type (new shapes
are expected, not a closed set) and is reported here rather than suppressed: `code_call_site`,
`dag_node_type`, `lambda_env_key`, `kuzu_schema_element` are all new address spaces not yet in
`boundary_report.py`'s `KNOWN_ADDRESS_SPACES` set. Recommend a small follow-on to add them once L2's own
build stabilizes — flagged, not fixed here (out of this build's scope; the type file is not this lane's
ownpath change to make unilaterally).

Every report's own accounting reconciles (`applicable_sum == surface_total`) — printed per-report in the
raw accounting lines below, satisfying banked input 4 (a verdict without its raw line removes the
detector; redundant derivation is the control).

## 4 · Raw accounting lines (banked input 4 — every sensor's own reconciliation, not just its verdict)

```
comp-cache (code_call_site): covered=105(traversal) + doc_only=4(mention) + member=0(traversal) + orphan=0(mention)
  applicable_sum=109, surface_total=109, RECONCILES
comp-blast (dag_node_type): covered=3(traversal) + doc_only=N/A + member=0(traversal) + orphan=7(traversal)
  applicable_sum=10, surface_total=10, RECONCILES
comp-blast (dag_edge_type): covered=13(traversal) + doc_only=N/A + member=0(traversal) + orphan=0(traversal)
  applicable_sum=13, surface_total=13, RECONCILES
inf-gold-trigger (lambda env reader) (lambda_env_key): covered=5(mention) + doc_only=N/A + member=1(traversal) + orphan=0(mention)
  applicable_sum=6, surface_total=6, RECONCILES
comp-kuzu (kuzu_schema_element): covered=12(mention) + doc_only=0(mention) + member=0(mention) + orphan=0(mention)
  applicable_sum=12, surface_total=12, RECONCILES
```

## 5 · Per-tool applicability denominators (acceptance 1, literal phrasing)

- of 5 tool-reports, **5** have a `covered` plane, 0 do not (N/A)
- of 5 tool-reports, **2** have a `doc_only` plane, **3 do not (N/A)**
- of 5 tool-reports, **5** have a `member` plane, 0 do not (N/A)
- of 5 tool-reports, **5** have an `orphan` plane, 0 do not (N/A)

**N/A is never rendered as 0 anywhere above or in the engine** — the 3 N/A `doc_only` reports are counted
in the denominator's "do not" side, explicitly excluded from any sum, never silently zeroed.

## 6 · Per-cell aggregate + method-mix bias (acceptance 2+3, banked input 1)

**Aggregation is on `cell` name ONLY across reports — never across `address_space`** (acceptance 2). A
`covered` count from `comp-cache` and a `covered` count from `comp-kuzu` are summed because they are the
SAME cell; their different address spaces (`code_call_site` vs `kuzu_schema_element`) are never
conflated or compared directly.

| Cell | Applicability denominator | Total (where applicable) | Method-mix bias |
|---|---|---|---|
| `covered` | 5/5 tools applicable | 138 | 121 via traversal (EXACT), 17 via mention (UNDER-REPORTS) |
| `doc_only` | **2/5** tools applicable (3 N/A) | 4 | 4 via mention (UNDER-REPORTS) |
| `member` | 5/5 tools applicable | 1 | 1 via traversal (EXACT) |
| `orphan` | 5/5 tools applicable | 7 | 7 via traversal (EXACT) |

**`doc_only`'s bias statement is the one to read carefully**: its entire applicable total (4) is
`mention`-derived, i.e. UNDER-REPORTING by the type's own definition (a mention proves reference, never
proves non-traversal beyond what was named). If the true doc-only surface is larger than 4, this
aggregate cannot see it — that is the bias, stated, not hidden behind a clean-looking number.

**The 3-way `doc_only` split CTO~Z specifically flagged as an asset, not noise** (141210Z): across this
corpus's 5 reports, `doc_only` takes THREE distinct epistemic states, not a binary applicable/not:
1. **Exercised-and-nonzero** (`comp-cache`, count=4, mention-derived) — a real prose plane, partially walked.
2. **Applicable-and-measured-zero** (`comp-kuzu`, count=0) — a real prose plane (the `comment` field,
   corrected from an earlier false "no prose plane" claim) that is EMPTY on canonical, not absent.
3. **N/A-by-shape** (`comp-blast` ×2, lambda-env) — no prose slot exists on these surfaces at all.
   The Lambda case is the sharpest: EMPTY (case 2) and ABSENT (case 3) are DIFFERENT L0b-I members, and
   collapsing them would be exactly the kind of grain error this whole program exists to catch. **This
   is why the design constraint — never design L2 against fewer than 3 mixed shapes — mattered concretely
   here**: a corpus of only `comp-blast`-shaped reports would never have exercised the EMPTY-vs-ABSENT
   distinction at all, and L2 would have shipped never having seen it.

## 7 · Ranking — deterministic proxy only (acceptance 4), self-tested with a positive + negative control

**Proxy: neighbourhood-touch count** — for each `orphan`/`doc_only` item, how many OTHER itemized
addresses across the WHOLE corpus (any report, any cell) share its file/symbol key (the substring before
a `:line:symbol` marker, or the whole address for non-file addresses). Deterministic, re-derivable,
zero per-item judgment.

**Self-tested before trusting it** (`l2_aggregate.py --self-test`), per this program's own repeated
lesson that an instrument only ever seen not-fire is untested:
```
[PASS] POSITIVE control (two synthetic reports sharing a file) -> touch=1
[PASS] NEGATIVE control (two synthetic reports, disjoint files) -> touch=0
```

**Real-corpus result: every one of this run's residue items scored `touch=0`.** This is a genuine
property of the corpus's sparse itemization (each sensor itemizes a small, largely non-overlapping slice
of its own subject — comp-cache's 4 hook call-sites, comp-blast's 7 orphan node-types, etc. — not a dead
instrument, confirmed by the controls above). **Stating this plainly rather than manufacturing a fake
ranking**: with this corpus, the proxy has nothing to differentiate on; a future, larger corpus with
overlapping subjects (e.g. two sensors both touching the same portal file, or a graph sensor and a
lineage sensor sharing a node) is where this proxy will produce a real, non-degenerate order.

## 8 · L1b (Class-2, predicate gaps) — reported separately, never numerically merged with L1a

```
14 SENSITIVE + 11 MONOTONE-BLIND = 25 limbs across 20 pairs (RECONCILES against the sensor's own
prose table and its --emit JSON, cross-checked independently)
```

**DECLARED (2 row-classes) and UNKNOWN (3 row-classes) are excluded from the 25-limb classified count,
kept as distinct cells per CTO~Z's binding 135910Z ruling** — these are OPPOSITE epistemic states:

| Row-class | Epistemic state | Meaning |
|---|---|---|
| `RESEMANT` × every mechanical kind | DECLARED / UNDETECTABLE-BY-DESIGN | nothing mechanical is sensitive to a meaning-only change, by construction |
| `assumption` (inf-intraday-iam) × all 9 change-types | DECLARED / IMMOBILE-BY-CONSTRUCTION | the check returns ASSUMPTION unconditionally — cannot move under anything |
| `metric_current`/`system_current` × all mechanical | UNKNOWN | could not synthesize without executing `comp-system` against a mutated estate (the patched-constant class the spec forbids) |
| `grep_present`/`version_pin`/`derived_count` × REGRAIN | UNKNOWN | no representative regrain synthesizable at these sources' own grain without mutating MEANING |

**Not folding DECLARED into UNKNOWN, or either into the classified count, is the live instance of banked
input 1's principle one level up**: a scalar "25 of 30 possible pairs classified" would blur two
structurally different kinds of non-classification (nothing can ever move it vs. this build couldn't
test it) into one number.

## 9 · Coverage of itself (acceptance 5 — the number GRAPHLEARNS inherits as its ceiling)

- **L1a emitters (4):** `comp-blast`, `comp-cache`, `comp-kuzu`, `inf-gold-trigger` (lambda env reader)
- **L1b emitters (1 subject):** `system_parity`
- **Named non-emitters (1):** `comp-residue` — built, real, invoked in the estate, emits nothing
  boundary-report-shaped. Per the spec's own coupling note (§2): *a tool that emits no sensor report is
  a domain the graph can never learn about.* This is not a footnote — it is the concrete instance of the
  hard ceiling the spec warns is invisible from inside L3.
- **Fleet-wide eligible population: stated as UNKNOWN, not fabricated.** This program has attempted 6
  named subjects total (5 emitters + 1 non-emitter); the true denominator — how many of the ~92-tool
  comp-* fleet COULD emit a boundary report or monotonicity pair-table if wrapped — has not been measured
  by this build. Quoting a fraction of 92 here would be exactly the "N/A rendered as a number" defect the
  whole type exists to forbid, since most of the 92 are not source-traversal-checkable in the L1a/L1b
  sense at all (they are enforcement gates, search primitives, session helpers, etc. — a different
  population than "things with a residue/monotonicity surface").

## 10 · Uncovered limbs (stated, per the dispatch's explicit ask)

- **Banked input 3 (can-ever-match denominators for ranking)** is a design principle this build carries
  forward but did not get to exercise concretely — none of this corpus's 5 reports contain a
  candidate-filter-with-dead-literals shape (the comp-pipescript-class finding it originates from). The
  ranking proxy (§7) is can-ever-match-scoped by construction (it only ever counts addresses that were
  actually itemized), but this corpus never tested the "dead literal inflates apparent coverage" case
  directly.
- **Banked input 5 (symptom-now, mechanism-after-repro)**: this memo and the engine's output are SYMPTOM
  rows throughout — counts, cells, reconciliations, all directly re-derivable from the cited artifacts.
  No `mechanism` field is populated anywhere in `L2_aggregate_output.json`; this build did not attempt to
  explain WHY any residue item exists, only to report that it does, at the denominator it does, per this
  banked input's own discipline.
- `boundary_report.py`'s `KNOWN_ADDRESS_SPACES` set is stale against this corpus (4 of 5 reports carry an
  address space not in that set, all correctly flagged BR008 rather than silently accepted or rejected) —
  flagged in §3, not fixed here (not this build's ownpath).
- Two of `comp-blast`'s cells (`member`) show 0 applicable count on both shapes — not chased further;
  stated as a real zero (applicable=true, count=0), not an N/A, per the type's own distinction.

## 11 · Handoff

- **`1.0.0_SA_CTO~Z`**: the engine + its JSON output are the primary artifact; this memo is the readable
  summary. §6's 3-way `doc_only` split and §9's named-non-emitter framing are the two findings most
  worth carrying into GRAPHLEARNS's eventual scoping (the ownership question is still open at Andrew per
  the spec's L3 section; nothing here presumes it).
- **`3.0.0_SA_CVO~Z`**: everything is re-derivable by running `l2_aggregate.py` (main output) and
  `l2_aggregate.py --self-test` (ranking-proxy controls) directly — no accepted-on-report claims. The
  seam most worth attacking: whether the neighbourhood-touch proxy (§7) is the right shape for "deterministic
  proxy" or whether a within-tool cross-shape signal (e.g. relating `comp-blast`'s orphan node-types to
  its own edge_type report) would be a stronger design — flagged as an open design question, not settled.
