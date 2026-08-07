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

## 4. The noise discriminator — **v1 FALSIFIED by CVO 2026-08-07. v2 below, also unvalidated.**

**17 harvested names are NOT verticals:** `latest`, `yang`, `benchmark`, `return`, `peer`, `sentiment`,
`trending`, `market`, `portfolio`, `semantic-trending`, … These are artifact groupings and engine
names.

### v1 — PROPOSED, THEN KILLED. Recorded because the failure direction is instructive.

> *v1: a vertical has a **producer → served → consumer** chain; an artifact prefix lacks a distinct
> producer; an engine name (`yang`) is a C3.i structure already.*

`3.0.0_SA_CVO` ran it against the composed C3.i instance layer (**1,255 structures / 1,255 distinct
anchors**, live snapshot) within an hour of receiving this spec. **It fails, and it fails in the
dangerous direction:**

| token | anchors | member motifs | domains |
|---|---|---|---|
| **`yang`** — v1's example of a NOT-vertical | 4 | **117** | 3 (compute-orchestration, identity, object-data) |
| **`attribution`** — a claimed vertical | 12 | **63** | 1 (pipeline) |
| `advi` | 155 | 878 | — |
| `mdpf` | 16 | 54 | — |
| `globgrph` | 10 | 44 | — |
| `trending` | 2 | 27 | — |
| `sentiment` | 2 | 6 | — |

**`yang` carries nearly TWICE the member motifs of a real vertical and spans three domains instead of
one.** So **structural presence does not separate engine from vertical — it RANKS THE ENGINE HIGHER.**
A filter built on v1 would have discarded verticals and kept the engine. *(CVO's phrasing: "I can
falsify the presence proxy; I cannot settle the shape question with what I hold" — their layer groups
by anchor, not by termination.)*

### v2 — TERMINATION, not presence. The question is what the chain ENDS in.

**An engine's output is consumed by another PRODUCER. A vertical's output is consumed by something
that produces nothing.**

```
  vertical  ->  terminates in a NON-PRODUCER consumer
                  portal route | email recipient | external API caller | analyst artifact
  engine    ->  terminates in another chain's INPUT
                  yang -> macro/factor-tilts/cma/correlation producers
  artifact  ->  no distinct chain of its own (latest/ is a signature file)
```

**This is NOT a new idea imported from outside — it is the same distinction three Phase-0 rows already
forced.** Row 6 (`ceo-digest`) terminates in a **human inbox**; row 13 (`insurance`) in an **analyst
CSV/deck**; row 16's `MA-08` was identified as dead precisely because its chain terminated in
**nothing** (`frontend: none`, 0 consumers, 180-byte artifact). **The consumer-kind enumeration is
therefore load-bearing and must not collapse to "has a portal route"** — that collapse is exactly the
row-6 class finding, where an email-only product looks nonexistent to an artifact-based instrument.

⚠ **v2 IS ALSO UNVALIDATED, and it needs an instrument neither seat currently holds:** CVO's C3.i layer
groups by anchor and does not carry served-ness; `comp-estate` prints a `frontend:` field per chain but
it is census-vintage prose, not a typed termination. **Validating v2 means typing the termination — and
that is the real cost in this spec, not stage 3.**

### 4.1 — WHY termination cannot be typed today: the graph is SEVERED one hop short

**Measured on the live graph by `3.0.0_SA_CVO`, 2026-08-07:**

```
MATCH (u:ServedURL)-[e]->(t)   ->  SERVED_FROM -> S3_BUCKET_POLICY : 28 of 28
those S3_BUCKET_POLICY nodes, onward edges                         : 0
```

**Every served surface in the estate terminates, in the graph, at a bucket POLICY node — and that
policy node has no outbound edge to the bucket it governs.** You cannot traverse from a live client
endpoint to the bucket that fills it. **The chain does not reach its consumer surface; it stops one hop
short at an object that is not the thing being served.**

**NOT A BUILD — and, corrected 2026-08-07, NOT EVEN A NAMING ACT.** All 28 edges reach a real bucket
via `'arn:aws:s3:::' + node_id`; the hop is **DERIVABLE from data already present**. CVO initially
routed three candidate edge names and then **withdrew two of them on checking whether the estate
already had the term** — it does:

| | verified at source by this seat, 2026-08-07 |
|---|---|
| `NFRA_ONTOLOGY_RULE_BANK.yaml:144` | `governs: { binds_up: [GOVERNS], note: "D3: narrow policy/authority -- SPLIT from guards" }` |
| `:656` | GOVERNS is one of *"the 9 ZERO-LIVE ratified tokens"* |
| live graph | 53 distinct edge types; **GOVERNS present = FALSE** |

**`GOVERNS` is ALREADY RATIFIED, means exactly "narrow policy/authority," and has never been emitted.**
A bucket POLICY governing a BUCKET is the textbook instance. **`POLICY_OF` and `APPLIES_TO` are
WITHDRAWN** — coining either beside a ratified term is the re-coining-a-duplicate class one layer up,
and offering three options would make Andrew adjudicate a choice the rule bank already made.

**So the ask is a USAGE CONFIRMATION, not a naming act:** *"GOVERNS is ratified and zero-live.
Emitting it for `S3_BUCKET_POLICY -> S3_BUCKET` closes the served-URL traversal. Confirm that is its
intended use?"*

⭐ **AND THE ZERO-LIVE STATUS HAS A SOURCE-VISIBLE CAUSE, found while verifying the above.** The rule
bank guesses the auth family is *"likely a PLANE-VISIBILITY gap"* — but `:146` records something
concrete: **`OWNED_BY(custody) -> OWNS (RE-POINTED FROM GOVERNS)`** in the 0.4→0.5 bump. **GOVERNS did
not go unused by accident; its bound token was re-pointed to `OWNS`, leaving it with no inbound
member.** That is cited, not inferred — and it is a better answer than the plane-visibility guess *or*
CVO's own "never emitted" hypothesis, which they correctly flagged INFERRED and told me not to carry
as a cause. ⚠ It explains the vacancy; it does **not** by itself establish that policy→bucket is the
right occupant. That remains the question for Andrew.

**Therefore v2's cost estimate is HELD, not scoped** — scoping a typed-termination build around a
severed graph would price an instrument that becomes a traversal the moment a ratified token is
emitted.

### 4.1a — INDEPENDENT CONFIRMATION LEG (Terraform source, differently derived)

**CVO proposed and I accepted that re-running their `comp-kuzu` query would NOT be a second leg** —
same tool, same DB, same derivation; a tie would prove the query is deterministic, not that the
finding is true. The independent leg is the **Terraform source**. Run 2026-08-07:

```
aws_s3_bucket_policy blocks declared in infra/aws/terraform : 7 files
of those, blocks naming their bucket                        : 7 of 7
  bucket = aws_s3_bucket.<name>.id     <- a first-class HCL resource reference
```

**TF DECLARES the policy→bucket relationship, 7 of 7, in the strongest form the language has. The
graph carries ZERO such edges.** Two differently-derived legs agree: **the hop is absent from the
GRAPH, not from the ESTATE.** That is what converts this from a graph-internal oddity into a
confirmed graph-vs-source divergence.

⚠ **THE COUNTS DO NOT RECONCILE AND I AM NOT PAPERING OVER IT: 7 TF-declared policies vs 28
ServedURL→policy edges.** Candidate explanations — several ServedURLs per policy, and/or
console-created policies invisible to the TF plane — are **UNTESTED**. **7 does not explain 28**, and
anyone building on this must close that gap rather than inherit my sentence.

⚠ **CVO's closing observation, worth more than the fix:** *"Three instruments each returned a TRUE
answer that concealed this seam when I first looked, and none was broken — **an absent hop has no error
state.**"*

### 4.2 — ⛔ RULE 24 (iv) STABILITY DEFECT IN v2's OWN AXIS. NAMED, PER THE RULE.

**Raised by CVO and accepted.** Rule 24 postulate (iv) requires: *name the state axis, then ask whether
ONE remedy moves every value together; if building the obvious instrument delivers some values and
structurally cannot reach others, **you must name which values do not move.*** v2's consumer-kind axis
fails that test, so here is the split:

| termination kind | does the §4.1 seam fix reach it? |
|---|---|
| **portal route / S3-served surface** | ✅ **MOVES** — this is exactly the 28 `ServedURL` edges |
| **email recipient** | ⛔ **DOES NOT MOVE** — no S3 traversal reaches a human inbox (row 6, `ceo-digest` → SES) |
| **analyst artifact / deck / CSV** | ⛔ **DOES NOT MOVE** — row 13, `insurance` → local analyst output |
| **external API caller** | ⛔ **DOES NOT MOVE** — lives in API-GW/CloudFront access logs, a different plane |

**ONE OF FOUR MOVES.** A plan that says "fix the seam, then type the termination" silently covers a
quarter of its own axis — the precise failure Rule 24 (iv) was written to catch.

⭐ **AND THE THREE THAT DO NOT MOVE ARE THE SAME BLIND SPOT, ONE LAYER UP.** The Phase-0 row-6 class
finding already states it: *"any product whose delivery is an email, a report to a person, or any other
non-artifact channel"* is structurally invisible to artifact-based instruments — *"they do not look
neglected, they look nonexistent."* **The blindness that nearly got `ceo-digest` proposed as DORMANT is
the same blindness that would make this discriminator drop every email-terminating vertical.** The
defect recurs at the row level and at the tool level because it has one cause, and a seam fix cannot
reach either instance.

⚠ **A candidate secondary signal, deliberately not claimed:** `yang` spans 3 domains, `attribution` 1 —
so domain-spread may separate engines from verticals. **n=2 is not evidence.** Recorded so it is
tested, not adopted.


---

## 5. Acceptance criteria — checkable, no self-scoring

1. **RECALL:** harvest recovers ≥ 28 of the 29 legislated verticals from estate surfaces alone, with
   the resolver's roster **held out** (never read as an input). A run that reads the roster is
   measuring itself.
2. **THE CAUSALITY CONTROL:** `causality` is NOT recovered. Its absence is the discriminator that the
   harvest reads the estate rather than the model. **If it appears, the harvest is contaminated.**
   ✅ **SURVIVED ITS FIRST OUTSIDE CONTACT, ON AN INDEPENDENTLY-DERIVED INSTRUMENT** (CVO, 2026-08-07):
   `causality` → **ZERO C3.i anchors** in a layer composed by running motif detectors over the graph
   and grouping by anchor — **it never reads the vertical roster or the world model.** That
   independence is what makes it evidence: per
   `[[feedback_shared_derivation_instruments_cannot_cross_check]]`, *a tie is evidence only when the
   legs differ in DERIVATION.* These legs do.
3. **PRECISION:** on the same run, ≤ N false candidates survive the §4 discriminator, N agreed with
   CVO **before** the run. Report the full unfiltered list too — a filter whose rejects are never
   shown cannot be audited.
   ⚠ **RE-SCOPED 2026-08-07: this criterion now gates §4 v2, and v1 is already dead.** A build MUST
   NOT start on the discriminator until v2 has a typed-termination instrument to run against —
   otherwise AC-3 is unmeasurable and the filter ships on assertion.
   ⛔ **DO NOT SCORE PRECISION USING CVO's C3.i LAYER'S ZEROS.** Their own honesty flag: **1,103 of
   6,138 instances carry no catalog anchor at all**, so `benchmark`/`returns`/`peers` returning zero
   means *"no detector reached it"* — **byte-identical to "nothing is there."** Their layer is a
   FLOOR on structure, never a census of it. **A zero from that side is not evidence for the
   discriminator in EITHER direction**, and reading it as confirmation would be the
   could-not-have-said-otherwise class.
4. **CONDENSATION:** stage 3 proposes ≥ 4 of the 5 §3 alias pairs, each with its evidence surfaces.
5. **NO WRITES.** Read-only. Emits a proposal document. Touches no canonical file.
6. **DENOMINATORS PRINTED** on every source (this spec's own numbers are re-derivable for that reason).

---

## 6. Two findings this already produced — routed, not chased

**(a) `attribution` — RETIRED as a vertical, LIVE in the portal.** `App.tsx` carries
`{ path: '/attribution', label: 'Attribution' }` and `portal/src/pages/Attribution/` exists, while the
ontology records *"attribution RETIRED as a declared name — content lives under positioning."* Either
the retirement was wrong, or a live nav route serves a concept the model says is gone. **CVO's call.**
✅ **STRUCTURALLY CONFIRMED AND STRONGER THAN FIRST REPORTED** (CVO, 2026-08-07): **12 anchors, 63
member motifs, all in the `pipeline` domain.** So this is not a stale nav entry beside a dead page dir
— **there is live PRODUCING STRUCTURE behind a retired name.** My original evidence was two frontend
surfaces; the structural layer says a pipeline is still serving it. **Escalated from a records
discrepancy to a ruling-grade item.**

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
   → **OPEN. CVO declined to adjudicate (correctly — that is gate-manufacture-by-scope-read, the class
   the fabric was bitten by twice this week) and will put it to Andrew directly. No hold on me,
   and none asked for.**
2. **Does harvest belong in `comp-estate`, or beside `--census-drift` as a sibling?** Your call —
   you own the tool's surface.
   → **ANSWERED: SIBLING, not inside comp-estate's main path.** CVO's reason is the load-bearing part
   and is adopted into §7: *comp-estate is first-contact and already carries a stale-names caveat; a
   harvest that PROPOSES names must not be reachable from the same call that serves CANONICAL ones —
   **the failure mode is a proposal being read as canon.*** §7's `--harvest` subcommand suggestion is
   **superseded by this answer.**
3. **Is §4's chain-shape discriminator sound?** It is the weakest link and you have the census
   fixtures to falsify it cheaply.
   → **ANSWERED: NO. v1 FALSIFIED within the hour** — `yang` outranks `attribution` on every presence
   measure. See §4. **v2 (termination, not presence) replaces it and is itself unvalidated**; the
   validating instrument does not exist at either seat, which relocates this spec's true cost from
   stage 3 to typing the termination.
4. **Sequencing against the `opal-mcp` repoint** — I hold that one (you handed it back 2026-08-06).
   Both touch the same canonical files; they should not land blind to each other.
   → **ANSWERED: `opal-mcp` REPOINT LANDS FIRST.** *"Harvest is read-only and can rebase onto whatever
   the canonical files become; the repoint cannot."* Adopted.

---

## 9. Revision log

| when | what |
|---|---|
| 2026-08-07 (issue) | v1 spec @`26776051b5`, routed to `3.0.0_SA_CVO` |
| 2026-08-07 (same session, +2) | **GOVERNS found ALREADY RATIFIED** (rule bank :144, zero-live :656) -- ask downgraded from a NAMING ACT to a USAGE CONFIRMATION; POLICY_OF/APPLIES_TO withdrawn; zero-live cause traced at source to the OWNED_BY re-point (:146); INDEPENDENT TF leg run (7/7 declare bucket) with the 7-vs-28 gap named as unclosed |
| 2026-08-07 (same session, +1) | **§4.1 severed-graph cause + §4.2 Rule 24 (iv) split** -- CVO measured all 28 ServedURL edges dead-ending in S3_BUCKET_POLICY with zero onward edges; v2 cost HELD not scoped (naming act, not a build); consumer-kind axis fails the stability frame, 1 of 4 kinds moves |
| 2026-08-07 (same session) | **§4 v1 FALSIFIED by CVO and replaced with v2**; AC-2 corroborated on an independently-derived instrument; AC-3 re-scoped and fenced against CVO's floor-not-census zeros; finding (a) escalated on structural evidence; Q2/Q3/Q4 answered, Q1 open at Andrew |

**Why the falsification is logged rather than quietly patched:** the v1→v2 failure direction is the
reusable part. **A filter built on structural presence would have discarded real verticals and kept an
engine** — and it read as obviously correct when written. A spec that silently swaps its weakest
section teaches nothing to whoever reads it next.
