# NFRA_TOOLUNIFY — BRIEF

**author:** `3.0.0_SA_CVO~Z` · 2026-07-24 · **issued to:** `1.0.0_SA_CTO~Z` for PRD registration
**sovereign:** Andrew-direct 2026-07-24 (verbatim): *"our goal here is consolidation and packaging. The
ultimate goal is a unified set, with clear denominators, and clear coverage disclaimers."*
**grounding vintage:** all measurements `@ ec07c2ec38` / `68bbf3dd2`, taken today by me, not quoted
**predecessors:** `NFRA_TOOLARCH.CANON` + `.CANON2` (both `pending`, lane `0.8.0_AE_CloudComp~D` idle) —
TOOLUNIFY **supersedes their scope**, absorbs their deliverables, and does not duplicate them.

---

## 1 · Why this project exists

The fabric is told to reach for a comp-tool before it reaches for `grep` or `aws`. That instruction is
correct and it is load-bearing: the comp-tools *are* the shared cognition. But we have never established,
as a measured population, **what the tools read, what they produce, how fresh that is, and what vocabulary
they speak.** We have a list of ~85 executables and a set of beliefs about them.

Today's re-ground of the CANON brief showed the beliefs are not reliable:

- A 12-item audit was **wrong 3 times (25%)** — it cannot tell a *producer* from a *consumer*, nor a
  *routing guard* from a *data source*.
- Its list of floating artifacts is a **hardcoded constant of three filenames**. At least two more
  (`pydeps.json`, `tool_activity_cache.parquet`) exist and have never been asked whether they go stale.
- Its tool-to-source resolution is **one hop deep**. Measured: **18 modules touch the trace cache; the
  method can see 3.** It missed a real member (`nerves_resolve.py:73`, a bare unguarded load).
- Two tools were reading a cache with **no vintage guard at all** — found and fixed today (`68bbf3dd2`).
- And a producer elsewhere in the same cluster had been **hard-failing for 17 days, correctly refusing to
  publish, and telling nobody**, because its hook backgrounds the work and exits 0 unconditionally.

> **THE GOVERNING CLASS, and the reason this is a project and not a cleanup ticket:**
> **A tool that cannot state what it covers, how old that is, and what it would do if its input were
> missing, is not a weak instrument — it is an instrument whose failures are invisible.** Every defect
> above is the same defect: *the answer arrives with no denominator attached.*

**Consolidation is the goal; the audit is how we earn the right to consolidate.** We cannot merge
vocabularies we have not mapped, and we must not re-point tools onto a canonical store whose failure mode
on a mismatch is **empty results, not errors**.

---

## 2 · Scope

**IN:** every `comp-*` executable + `pipescript`; their full backing-module closure; every artifact they
read or write; the vocabularies they speak; the registries that describe them
(`graph-call-manifest.yaml`, `comp-tools.yaml`, `comp-which` routing, `comp-manifest-check`).

**OUT:** the client-data pipeline estate itself (owned elsewhere), the taxonomy plane, and any change to
what a tool *concludes*. TOOLUNIFY changes **where a tool gets its facts and how it discloses them** —
never its business logic. A behavioural change to a tool's verdict is out of scope and must be raised
separately.

**Explicit non-goal:** "one graph." See §5 — the evidence says that would destroy information.

---

## 3 · The core deliverable — the TOOL REGISTER

One row per tool, machine-generated, committed, and regenerable. This schema **is** the "structured
format" the sovereign asked for, and each field exists because a specific failure this year would have
been caught by it.

| Field | Meaning | The failure it closes |
|---|---|---|
| `tool` | wrapper name | — |
| `entry` | wrapper path + backing entry module | — |
| `closure` | **full transitive import closure**, not depth-1 | missed `nerves_resolve.py` |
| `reads[]` | each input, typed (below) + path | the whole question |
| `writes[]` | artifacts produced | **producer-vs-consumer** (`comp-stitch-refresh` FP) |
| `binding` | is each read **ANSWER-BEARING**, or `GUARD` / `ROUTING` / `LABEL` / `CONFIG`? | **guard-vs-source** (`comp-pipescript` FP) |
| `evaluation` | `RUNTIME` (computes at invocation) vs `DERIVED` (depends on a pre-built artifact) | the sovereign's explicit ask |
| `refresh` | for each DERIVED input: producer, trigger, cadence, and **whether anything watches it** | the 17-day silent stitch failure |
| `vintage_discipline` | `GUARDED-REBUILD` / `LOUD-VINTAGE` / **`SILENT`** | the two raw readers fixed today |
| `vocabulary` | entity/node namespace it speaks | the consolidation question |
| `denominator` | what population its answer covers — **and whether it PRINTS it** | Rule 22; "7" was never measured |
| `failure_mode` | on stale/missing/mismatched input: `LOUD` / `FAIL-OPEN` / **`SILENT-EMPTY`** | the catastrophic class |
| `role_flags[]` | `GATE-BLOCKING` / `PRODUCER` / `ADVISORY` / `TEST` (orthogonal, multi-valued) | a tool is often several at once |
| `registry_state` | registered in manifest / routable by `comp-which` / documented | drift between tool and record |
| `owner` | lane | routing |

**`reads[]` type vocabulary:** `LIVE-AWS` · `KUZU-CANONICAL` · `SOURCE-SCAN` (derived from the working
tree) · `FROZEN-SNAPSHOT` (generated once, no live refresh path) · `DERIVED-CACHE` (regenerable, has a
refresh path) · `CONFIG` · `NONE`.

> **Grouping must be by AXIS, not by bucket.** The predecessor audit used one label per tool, so a tool
> reading *both* kuzu and a floating artifact was filed under the kuzu label and vanished from the target
> set. **`reads[]` is a list; `role_flags[]` is a list.** A single-label taxonomy is how coverage gaps hide.

---

## 4 · What is already known to be broken (seed findings, all grounded today)

| # | Finding | State |
|---|---|---|
| 1 | `comp-gitdrill` + `comp-surface-check scan` read the trace cache raw, no vintage guard | **FIXED** `68bbf3dd2`, mutant-exercised |
| 2 | `nerves_resolve.py:73` — third bare `TraceGraph.load()`, reachable only via import | **OPEN**, latent (call-order protected, not guard-protected) |
| 3 | `stitch_graph.json` producer hard-failing 17d on a tripped grain sentinel; hook exits 0, nobody told | **OPEN — the live one.** Inside it, `EXTERNAL_ENDPOINT 0 vs 3` (a collapse to zero) is a different animal from the five 2.66x–4.00x high-side trips |
| 4 | `comp-pipescript postdeps <unknown>` → *"No dependencies declared"* at `rc=0` — an affirmative-sounding negative, in a Rule-13 pre-run check | **OPEN** |
| 5 | `estate-coverage-resolver.json` (25d) census input hardcoded to a date-pinned 2026-06-15 log dir — **never had a refresh path**. Regenerating stamps a fresh mtime over a frozen census and destroys `last_review` | **OPEN — FREEZE, do not "fix" by regenerating** |
| 6 | Artifact vocabulary is a hardcoded 3-name constant; `pydeps.json` + `tool_activity_cache.parquet` uncounted | **OPEN** |
| 7 | `os.path.exists()` returns true for colon-form node ids on Windows (NTFS ADS syntax) in `resolve_files()`; observed transient, **not** reproduced | **UNRESOLVED — record, do not action on one observation** |

---

## 5 · The consolidation question — and my position on it

Andrew asked that if both vocabularies are relevant at different layers, that be discussed. **They are, and
it is the central design ruling of this project.**

**Measured today:**

| `graph.json` (source-scan, 2,255 nodes) | `kuzu CloudNode` (cloud estate, 20,403 nodes) |
|---|---|
| `GOLD_SCRIPT` 1365 | `PipelineFunction` 1201 + `PipelineScript` 133 |
| `COMPONENT` 24 | `Component` 199 + `ReactComponent` 442 |
| `LAMBDA` 333 | `LAMBDA` **191** |
| `S3_ARTIFACT` 321 | `S3Key` 232 |
| `EVENTBRIDGE` 63 | `EVENT_RULE` 141 |
| `SQS_QUEUE` 5 / `STATE_MACHINE` 1 | *absent from the top 40* |

**Three things this table says, none of them "rename and merge":**

1. **The grain differs.** One source type maps to *two* canonical types. `GOLD_SCRIPT` conflates script
   and function; kuzu splits them. A crosswalk is a **remap with a grain decision**, not a dictionary.
2. **The populations disagree in BOTH directions.** The source graph has *more* Lambdas than the cloud
   graph (333 vs 191) and *far fewer* components (24 vs 641). At least one of those is a coverage defect
   in one of our two graphs, **about our own estate**, and it is worth knowing regardless of consolidation.
3. **Each models things the other cannot.** `graph.json` holds code-internal structure — functions, JSX,
   hooks, query keys — that has no AWS existence. Kuzu holds IAM, log groups, alarms, secrets that have no
   source existence.

> **MY POSITION (CTO~Z to rule):** the target is **NOT one graph**. It is **ONE ONTOLOGY WITH TWO PLANES —
> a SOURCE plane and a DEPLOYED plane — joined by an explicit, tested crosswalk at the four entities that
> genuinely exist in both: Lambda, S3 key, Component, Endpoint.** Collapsing to a single store loses either
> function-grain or cloud-grain, and "which is right?" is the wrong question for two planes that are
> *supposed* to differ — **the difference between them is itself a finding** (declared-vs-deployed drift is
> exactly what we want an instrument for). Unify the **vocabulary and the disclosure discipline**; keep the
> **planes**.

**Corollary that must survive into the PRD:** `graph.json` is **not** a stale snapshot — it is SHA-drift-
checked and rebuilt on every read for five of its seven consumers. **Re-pointing it at kuzu buys
architecture, not freshness**, and would trade a source-exact current graph for a 2.2h cloud projection of
a different population. That is a legitimate trade to *consider*; it is not an obvious win, and it is not
urgent.

> ⚠ **THE NON-NEGOTIABLE:** on a vocabulary mismatch a re-pointed query returns **EMPTY, NOT AN ERROR** —
> `comp-blast` would report "no downstream consumers" *confidently*. **Every re-point ships with the
> CANON2 known-present-node adapter mutant**: a fixture that MUST return a known node, and the re-point is
> rejected if it does not. No exceptions, no "it looked right."

---

## 6 · Workstreams

**WS-1 · Build a sound instrument (blocks everything else).**
Replace the regex/text-signal method with **import-closure + AST**: resolve each wrapper's full transitive
module closure; classify reads by *call site*, not by string presence; separate reads from writes; mark
each read `ANSWER-BEARING` vs `GUARD`.
*Acceptance:* on a fixture set it must (a) reproduce all **3 known false positives as negatives**
(`comp-manifest-check`, `comp-graph`, `comp-stitch-refresh`), (b) **find the known missed member**
(`nerves_resolve.py`), (c) print its own denominator and its own coverage disclaimer. **An instrument that
cannot find a known-present instance is a broken instrument reporting silence.**

**WS-2 · Populate the register for all 85.** Machine-generated, committed, regenerable, diffable.
*Acceptance:* 85/85 rows, zero `UNKNOWN` in `reads[]`/`evaluation`/`failure_mode` without a named reason;
**the denominator and its exclusions printed in the artifact itself.**

**WS-3 · Artifact census.** Every artifact any tool reads or writes: producer, trigger, cadence, last
successful production, vintage discipline, and **who is notified on failure**.
*Acceptance:* every artifact has a named producer and a named watcher, **or is explicitly declared
FROZEN-BY-DESIGN with a loud-vintage banner.** Finding #3 is the proof this WS is needed.

**WS-4 · Vocabulary crosswalk + the two-plane ruling (CTO~Z).** Publish the entity crosswalk, decide the
grain at each join, and **investigate the LAMBDA 333-vs-191 and COMPONENT 24-vs-641 disagreements as
findings in their own right.**
*Acceptance:* a committed crosswalk with a conformance suite carrying **one mutant per settled mapping.**

**WS-5 · Repair.** Findings #2, #4, #6 + whatever WS-2 surfaces. #3 routes to NFRA_GLOBGRPH / `0.8.0_AE`.
#5 is **FREEZE, not fix** — de-pin the census before anything regenerates.

**WS-6 · Packaging + coverage disclaimers.** The consolidation payload: every tool states, in its own
output, **what it covers, how old it is, and what it does not see.**
*Acceptance:* a tool with a `SILENT` vintage discipline or an unprintable denominator **fails the standard.**

**WS-7 · Make it a control.** Gate the register against the live tool set so a new/renamed tool cannot land
unregistered, and a new floating artifact cannot land unwatched.
*Acceptance:* exercised — a deliberately unregistered tool and a deliberately unwatched artifact are both
**rejected**, demonstrated, not asserted. **Care is not a control.**

**Sequencing:** WS-1 → WS-2 → (WS-3 ∥ WS-4) → WS-5 → WS-6 → WS-7. WS-1 gates all: **auditing 85 tools with
a method that is 25% wrong produces a register nobody can trust, and a wrong register is worse than none —
a plausible count does not invite suspicion.**

---

## 7 · Risks

1. **Re-point silent-empty** — mitigated only by the mandatory adapter mutant (§5).
2. **Regenerating a frozen artifact to "fix freshness"** — laundering a frozen input as fresh. Finding #5.
3. **Trusting the predecessor audit's numbers** — they are candidates, not verdicts. Re-ground each.
4. **Scope creep into tool business logic** — §2 forbids it; this project moves *sources and disclosure*.
5. **The register itself going stale** — which is why WS-7 exists. A register maintained by care decays
   exactly like the artifacts this project is about.

---

## 8 · What I did not do

Did not modify either predecessor TO, did not re-point any tool, did not regenerate any artifact, did not
touch `~D`'s deliverables, and did not action finding #7 (one non-reproduced observation). Findings #1 is
the only change landed (`68bbf3dd2`, mutant-exercised, gate-clean). Everything else is open and routed.

**Recommended owner:** `1.0.0_SA_CTO~Z` (PRD + the §5 two-plane ruling + WS-4 grain decisions).
**Verification lane:** `3.0.0_SA_CVO~Z` — WS-1's acceptance is a verification bar, and the instrument that
measures the estate must itself be measured by someone who did not build it.
