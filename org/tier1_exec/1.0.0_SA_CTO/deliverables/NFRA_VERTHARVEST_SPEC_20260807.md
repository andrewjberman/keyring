# NFRA_VERTHARVEST — deterministic candidate-harvest for C3.ii semantic verticals

**Status:** SPEC / PROPOSAL. Not built. Not authorized to build.
**Author:** `1.0.0_SA_CTO~C`, 2026-08-07 · **Routed to:** `3.0.0_SA_CVO` (authored
`NFRA_ONTOLOGY_C2C3_CANONICAL.yaml`; holds the C3.ii deferral)
**Origin:** Andrew-direct at the `~C` terminal, 2026-08-06, VERBATIM:

> *"BUT HOW DO WE GET A FULL LISTING OF SEMANTIC VERTICAL NAMES? ARE THEY REALLY JUST MADE UP? LIKE I
> SHOULD JUST WRITE EVERY SINGLE VERTICAL PRODUCT I AM AWARE OF? THAT SEEMS DISTINCTLY NON-SCALABLE.
> THERE SHOULD BE A WAY TO FEED THIS DETERMINISTICALLY AT SCALE AND AI CONDENSES THINGS THAT ARE
> CLEARLY THE SAME (E.G. MDPF VS MODEL PORTFOLIOS)"*

and, one turn earlier: *"we need a way better method to do that."*

---

## 1. The problem, stated precisely

**It is NOT "C3.ii is made up."** `ESTATE_WORLD_MODEL_PROCESS.md` is coherent and mostly built: naming
is sovereign (L1), adjudication is CVO-verified (L2), enumeration is derived (L3/L4), the join is
mechanical. `comp-estate --census-drift` exists, runs, and works.

**The defect is one conflation, in one table cell.** L1 is marked **"HAND — necessarily,"** justified
by *"there is no fact of the matter until named."* That justification is TRUE of the naming act and
FALSE of candidate discovery — and the doc treats them as one thing. The consequence is that the
roster's completeness has no instrument at all: `--census-drift` answers *"does every resource have a
thread?"* and nothing answers *"does every business function have a name?"*

**Measured consequences, 2026-08-06/07 (all re-derivable):**

| | |
|---|---|
| bridge table `lambda_to_named_thread` | **188** lambdas → **28** threads, **frozen 2026-06-15** |
| `--census-drift` residue (DESIRED plane) | **19** unmodeled + **28** census-only = **47** rows |
| generator's hardcoded `CATALOG_ORDER` | **25** entries vs **29** legislated |
| — contains | `attribution` — **retired by naming act** |
| — missing | `canonical-schwab`, `ceo-digest`, `etf-reports`, `m365-mcp`, `ticketing` |
| catalog-drift failure mode | **SILENT** — unknown names are appended alphabetically, no error |

The `CATALOG_ORDER` row is `[[feedback_a_predicate_is_not_a_roster]]` exactly: *a tool's universe must
be a re-derived predicate over the canonical graph, not a hand-drawn allowlist.*

---

## 2. Non-goals — read before section 3

- ⛔ **NAMING REMAINS SOVEREIGN.** This never auto-names. `ESTATE_WORLD_MODEL_PROCESS.md` §4 already
  rules it: *"The loop SURFACES candidates; ONLY a naming act admits it … auto-naming here would be
  the confident-wrong-answer class."* **This spec agrees with that line and changes nothing about
  it.** It attacks the blank page, not the decision.
- ⛔ **Not a monitor, alarm, checker or notifier** (standing moratorium, 2026-07-28). It is a
  read-and-report harvest, run on demand at review time — the same posture as `--census-drift`.
- ⛔ **Does not replace `--census-drift`.** Different question: drift answers *resource → thread*;
  this answers *what threads should exist*. They compose.

---

## 3. The pipeline — four stages, and the authority boundary sits between 3 and 4

```
  [1] HARVEST          [2] NORMALIZE+CLUSTER      [3] CONDENSE           [4] RATIFY
   deterministic   ->   deterministic         ->   AI                ->  Andrew/CVO
   multi-source        case/sep/plural fold       semantic identity      naming act
   (no judgment)       (no judgment)              (judgment, cheap)      (judgment, sovereign)
   ~28/29 recall       15 clusters measured       mdpf == Model Ptf      unchanged from today
```

**The load-bearing claim, and it is measured, not argued: stages 1-2 recover the roster.**

### Stage 1 — HARVEST (measured recall)

Two source families, and the split matters because each is blind to the other's half:

**(a) PORTAL-FACING** — humans already wrote these names, for humans:

| source | count | note |
|---|---|---|
| `App.tsx` nav `{path, label}` | 15 | **a nav label IS a business-function name**, authored by whoever shipped the product |
| `portal/src/pages/*` dirs | 15 | one dir per product surface |
| `s3://opal-data-portal-v2/json/*` prefixes | 21 | served-artifact grouping |

→ **recovers 12 of 29 legislated verticals.**

**(b) BACKEND / INFRA** — the half no portal surface can see:

| source | count |
|---|---|
| live Lambda names | 196 |
| EventBridge rules | 139 |
| EventBridge Scheduler | 16 |
| S3 bucket names | 30 |

→ **recovers 16 of the 17 verticals that have NO portal surface.**

**COMBINED: 28 of 29.** ⭐ **THE SINGLE MISS IS `causality` — the vertical Andrew RETIRED 2026-08-05,
whose applied plane is measured empty (0 Lambdas, 0 tables).** That is not a gap; **it is a natural
positive control nobody designed: the harvester's only blind spot is the one thing that does not
exist.** Any implementation MUST reproduce this property — a harvest that "finds" causality is
reading the model, not the estate.

### Stage 2 — NORMALIZE + CLUSTER (deterministic, ~10 lines)

CamelCase-split → lowercase → `_`/space→`-` → collapse repeats → crude singularize. Measured output:
**15 clusters**, including the target case:

```
model-portfolio  <- nav:Model Portfolios, page:ModelPortfolios, s3:model_portfolios
valuation        <- nav:Valuations, page:Valuation, s3:valuation, s3:valuations
correlation      <- nav:Correlations, page:Correlation, s3:correlations
capital-market   <- nav:Capital Markets, s3:capital-markets
```

### Stage 3 — CONDENSE (this is where AI belongs, and stage 2 structurally cannot do it)

**Stage 2 got `model-portfolio`. It can NEVER link `mdpf` to it — zero string overlap.** The identities
that require semantics, all live in this estate today:

| alias | canonical | shared characters |
|---|---|---|
| `mdpf` | Model Portfolios | none |
| `cma` | Capital Markets | none |
| `astn-wsjft` | ceo-digest | none |
| `find-insure` | insurance | partial stem only |
| `globgrph` | graph-platform | partial stem only |

**This is precisely Andrew's stated requirement, and the measurement establishes it is REQUIRED rather
than nice-to-have** — normalization provably tops out before it.

**Output contract: stage 3 PROPOSES a merge with its evidence and never commits one.** Every proposal
carries the surfaces that produced each alias, so stage 4 adjudicates on evidence, not on assertion.

### Stage 4 — RATIFY (unchanged)

Naming act by Andrew/CVO. Codify per `ESTATE_WORLD_MODEL_PROCESS.md` §4: name → catalog entry →
manifest rows → regenerate resolver → re-baseline fixtures → gate-b green.

---

## 4. The noise discriminator — the honest weak point

**17 harvested names are NOT verticals:** `latest`, `yang`, `benchmark`, `return`, `peer`, `sentiment`,
`trending`, `market`, `portfolio`, `semantic-trending`, … These are artifact groupings and engine
names.

**Proposed discriminator (mechanical, needs validation):** a vertical has a **producer → served →
consumer** chain; an artifact prefix has served-and-consumer but no distinct producer, and an engine
name (`yang`) is a C3.i structure already. **`latest/` is a signature file. `yang/` is an engine.**
Both are separable on chain shape, not on the string.

⚠ **STATED AS THE RISK, NOT WAVED AT:** this discriminator is UNVALIDATED. If it under-filters, stage
4 gets a noisy list and the human cost lands exactly where this spec claims to remove it. **Acceptance
criterion 3 below exists to measure this before anyone trusts it.**

---

## 5. Acceptance criteria — checkable, no self-scoring

1. **RECALL:** harvest recovers ≥ 28 of the 29 legislated verticals from estate surfaces alone, with
   the resolver's roster **held out** (never read as an input). A run that reads the roster is
   measuring itself.
2. **THE CAUSALITY CONTROL:** `causality` is NOT recovered. Its absence is the discriminator that the
   harvest reads the estate rather than the model. **If it appears, the harvest is contaminated.**
3. **PRECISION:** on the same run, ≤ N false candidates survive the §4 discriminator, N agreed with
   CVO **before** the run. Report the full unfiltered list too — a filter whose rejects are never
   shown cannot be audited.
4. **CONDENSATION:** stage 3 proposes ≥ 4 of the 5 §3 alias pairs, each with its evidence surfaces.
5. **NO WRITES.** Read-only. Emits a proposal document. Touches no canonical file.
6. **DENOMINATORS PRINTED** on every source (this spec's own numbers are re-derivable for that reason).

---

## 6. Two findings this already produced — routed, not chased

**(a) `attribution` — RETIRED as a vertical, LIVE in the portal.** `App.tsx` carries
`{ path: '/attribution', label: 'Attribution' }` and `portal/src/pages/Attribution/` exists, while the
ontology records *"attribution RETIRED as a declared name — content lives under positioning."* Either
the retirement was wrong, or a live nav route serves a concept the model says is gone. **CVO's call.**

**(b) `Advisor Intelligence` is ONE product in the portal and THREE verticals in the roster** —
`advi-bd` / `advi-cot` / `advi-inf`. The nav and page dir present one product; the roster splits by
firm. **This is a Rule 24 postulate (ii) SAME-GRAIN violation: product-grain and firm-scope-grain on
one axis** — and it is the **exact inverse** of the mdpf/model-portfolios merge Andrew ruled by hand on
2026-08-06. ⭐ **He caught that one by eye; the harvest surfaced this one in seconds. That is the
argument for the tool, and it is why it is written here rather than in prose.**

---

## 7. Build-ladder check (CLAUDE.md, run in order)

1. **YAGNI** — no: the completeness question has no instrument, and the roster demonstrably drifted
   (§1) while `attribution` and `advisor-intelligence` sat wrong in plain sight.
2. **Estate already has it?** — `comp-estate --census-drift` answers a **different question**
   (resource→thread, not what-threads-exist); `gen-estate-resolver.py` **consumes** the roster and
   cannot question it; `NFRA_MOTIF_P2_c3_emergence.py` computes C3.i only. **No existing tool answers
   this.** Checked before writing, per the ladder.
3-6. stdlib + existing surfaces only; stages 1-2 are ~10 lines of regex over data already enumerated
   by tools that exist. **Stage 3 is the only new cost.**
7. Minimum: a `comp-estate --harvest` subcommand, not a new binary — it reuses the resolver, manifest
   and census loaders already in that tool.

---

## 8. Open questions for CVO

1. **Scope collision, surfaced not adjudicated.** Andrew deferred C3.ii at your terminal ~2340Z
   (*"Our whole focus here is C2 and C3.i. Do not worry about C3.ii just yet"*) and commissioned this
   spec at mine one turn later. **Both are his; the breadth is his to state.** I am delivering the
   spec as asked and building nothing.
2. **Does harvest belong in `comp-estate`, or beside `--census-drift` as a sibling?** Your call —
   you own the tool's surface.
3. **Is §4's chain-shape discriminator sound?** It is the weakest link and you have the census
   fixtures to falsify it cheaply.
4. **Sequencing against the `opal-mcp` repoint** — I hold that one (you handed it back 2026-08-06).
   Both touch the same canonical files; they should not land blind to each other.
