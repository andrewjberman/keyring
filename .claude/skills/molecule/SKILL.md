---
name: molecule
description: Deep ANALYSIS of one unit -- a function, field, S3 artifact, gold script, Lambda, table, portal component or small pipeline segment: what exactly is going on here and where it sits in the chain (composition, live state, lineage, real behavior) plus a smell pass. Grounds against the deployed/served artifact, never self-report. Analysis, not the verification process (that is /verify-channel); /seams is the edge between molecules; /spot-check the wide shallow sweep. `/molecule <target>` or `--dimension <d>`. Any agent.
---

# /molecule — Atomic-Granularity Deep Analysis

A molecule is a **unit**: the thing itself, examined all the way down — a function, an object, a field, an S3 artifact, a gold/silver/bronze script, a Lambda, a DynamoDB table, a portal component, a small pipeline segment. `/molecule` is a **deep analysis** that answers, with ground truth: **what is EXACTLY going on with this unit, and where does it sit in the chain?** — then runs a **smell pass** for anything notable, *whether or not it's a problem*.

**molecule is ANALYSIS, not a verification process.** It characterizes — understands what's there, maps where it sits, notices what's off. The formal *verification process* — rendering a delivery verdict, running a project's closeout, gating, emitting — is a **separate function** that lives in `/verify-channel`. molecule **feeds** that process (deep-analyze the suspect unit, hand over what you found); it is not that process and borrows none of its machinery.

The verification family, each its own thing:

| Skill | Unit of analysis | What it is |
|---|---|---|
| **/molecule** (this) | the **node** — one unit, deep | **analysis**: "what is *exactly* going on here, where does it sit, does anything smell?" |
| **/seams** | the **edge** — the bond between two units | **pass/fail**: "is this joint sound — mechanical / declarative / semantic?" |
| **/verify-channel** | a pipeline/artifact's delivery + a project's closeout | **the verification process**: "does it DELIVER fresh usable data; is the project closeable?" (the 4-check, the closeout machinery, the verdicts/emissions) |
| **/spot-check** | recent commits, wide + shallow | **sweep**: "any alignment drift across the fabric right now?" + metadata fix |

`/molecule` and `/seams` compose directly: a `/molecule` deep-dive produces the chain-position map (Dimension 3) that names exactly which **seams** to hand to `/seams`. Node + edges = the whole graph. When the question is the *formal delivery/closeout verdict*, that's `/verify-channel` — run it (and molecule's findings feed it). Don't reimplement its process here.

---

## The smell-pass doctrine (the distinctive part)

Most checks ask "pass or fail?" `/molecule` also asks **"does anything smell funny?"** — and *a smell is not an accusation.* A smell is anything notable, unexpected, inconsistent, or simply *interesting* the deep look surfaced. It may be a benign-but-surprising design choice worth recording, a latent fragility not yet a bug, or the first thread of a real defect. The point is to put it **on the record** so the fabric reaches knowledge parity about what's actually there — not to indict.

Rate each smell, don't bury it:
- **NOTE** — benign / explained, but worth recording (an unusual-but-correct pattern; a deliberate choice future-you will wonder about).
- **WATCH** — not wrong now, but a latent edge / fragility / assumption that could bite under drift.
- **DIG** — actually-off; warrants a `/seams` pass, a `/verify-channel` verdict, or a follow-up — stated as an observation with evidence, not a verdict.

A clean `/molecule` says: "here is exactly what this is, here is where it sits, and here is everything that caught my eye, with ratings." Surfacing a benign-but-surprising thing is a *success*, not noise — it's how latent issues get caught before they're incidents (the BMKAUD class: structurally fine, semantically wrong, caught only by a careful look).

---

## Core principles (the grounding spine — bind every dimension)

The recurring failure this discipline exists to catch is **config-OK != reality**: a cron ENABLED, an `exit=0`, a partition existing, a `status: ok`, a TO `complete`, a *prior finding's status* — none prove what's actually going on.

1. **Ground truth = the DEPLOYED / LIVE / SERVED artifact — never source, self-report, or stale memory.** Read the running Lambda package, the served S3 object, the live graph, the deployed dispatcher. *Committed != deployed; "ran fine" != landed; a days-old "open" status != current* ([[reference_reverify_prior_finding_fix_status_against_deploy_not_stale_open_framing]], [[feedback_verify_against_served_artifact_not_partial_proxy]]).
2. **Read the artifact, never the self-report.** A producer's "ran fine, N rows" is not evidence; your own read of the actual state is.
3. **Sharpest-test-binds.** A coarse look that misses a sharp defect launders a problem into "clean" — when a sharp probe surfaces something, it binds.
4. **Decision-useful != mechanically-present.** Fresh + scaled + non-frozen + structurally-non-degenerate is necessary, never sufficient. The deepest question is whether the unit is actually *meaningful for its consumer*.

`/molecule` is **characterize-not-fix**. It deep-reads, surfaces smells, renders an analytical assessment; it does not repair code/runtime and does not gate (route fixes to the owning lane; route formal verdicts/closeout to `/verify-channel`). The one bounded exception, for an agent that holds the authority (e.g. CVO /spot-check scope): correcting a stale *record* to parity is the declarative repair — the code/runtime fix still routes to the owner.

---

## The deep-analysis body — five dimensions

Run these on the target. Each grounds against live/deployed state. Not every dimension applies to every unit (a pure function has no S3 state); skip with a one-line "N/A because…", never silently.

### Step 0 — Pin the unit
State precisely: WHAT the unit is, its SCALE (micro = one function/field/object; meso = one script/Lambda/artifact/segment), and its EXPECTED role from the most authoritative source — *and hold that suspect*; Dimension 1 tests whether the record is even true.

### Dimension 1 — COMPOSITION: what it actually is
Read the real implementation/content (**deployed, not repo**). What does it *actually* do or contain vs what its name/doc/registry/memory claims? This is the knowledge-parity read: surface any **declared-vs-actual drift** — a name that lies about the computation (the `capital_gains_ttm`=delta-unrealized class), a docstring claiming a removed gate, a status stale vs deployed. Drift here is a rated smell *and* a record to correct to parity.

### Dimension 2 — STATE: read and characterize the live snapshot
Read the unit's **actual current state** at the path consumers resolve (`comp-platinum reverse` / `comp-pipescript consumers` finds the real consumer path — often `latest/`, not the producer's dated write) and *characterize* it: is it present, recently/honestly fresh (a freshness stamp reflecting real data vintage, not write-time or an unconditional `CURRENT_DATE`), in-family in scale, genuinely-distinct content (ETag/hash, not size) — and does anything about the snapshot look off? Timezone: head-object UTC, not host-local `s3 ls`; read only after expected-landing + margin or early-absence is a false alarm.

This is the *analytical* state-read — enough to understand what's there and smell trouble. The **formal delivery-verification PROCESS** (the rigorous 4-check EXISTS/FRESH/SCALED/NOT-FROZEN run to a PASS/CONCERN/CONDITIONAL **verdict**, plus the project-closeout body) is **`/verify-channel`'s separate function** — when "does it deliver" is the whole question, run `/verify-channel`; here, the state read is one dimension of the deeper look, and a smell here is a reason to *route* to that verdict, not to render it.

### Dimension 3 — POSITION IN THE CHAIN (the "where does it sit"): lineage + reach
Map the unit's neighborhood — half of what a deep analysis means:
- **Upstream:** what feeds it (producers, source inputs, the DAG branch). `comp-pipescript io` / `comp-estate <name>` / `comp-kuzu "MATCH (up)-[:...]->(n)"`.
- **Downstream:** what consumes it (served paths, portal components, derived artifacts, other scripts). `comp-blast <fn>` / `comp-pipescript consumers` / `comp-platinum reverse`.
- **Dependencies + reach:** shared libs/defaults it inherits ([[reference_bucket_ref_rederive_trace_shared_lib_defaults_not_per_script_grep]]), IAM it needs, what breaks if it changes.
- **Position smell:** orphan (no live consumer)? single-point-of-failure? co-located with differently-owned things? does the live graph's `drift_class` say something the doc doesn't? Each is a rated smell.

The chain map is itself a deliverable — "exactly where this sits" — and it names the **seams** to hand to `/seams` next.

### Dimension 4 — BEHAVIOR: what actually happens on the real path
Don't infer behavior from source — **exercise-or-evidence** it. Either trigger the unit and observe the effect in live state, or find evidence it fired (a real event, a fresh LastModified, a log of the actual traversal). A configured path is not a firing path ([[reference_ssm_runcommand_eventbridge_detail_type_schema]] — ENABLED rule, 0 events). For a Lambda: what does the **deployed** code actually do on each event class, *including the unhappy paths* (a delete that no-ops, an error swallowed)? Catch the **committed-but-not-deployed** gap here.

### Dimension 5 — SEMANTIC quality + the smell pass
The unit is present and behaves — but is its content the *right* content, and does anything smell?

**Sharp structural probe** (for join/aggregate/cohort/derived data): ask "what is the strongest degeneracy this could still have that a coarse look would NOT catch?" and probe THAT.
- **Aggregate-identity masking** — `agg == sum(parts)` can hold to-the-cent while a residual silently absorbs others' errors ([[feedback-identity1-masks-absolute-value-class]]). Per-component series-walk, not the identity.
- **Join degeneracy** — exact headline counts over a near-cartesian; test within-group completeness.
- **Freshness-stamp honesty** — every "fresh today" row provably NOT byte-identical to the last frozen snapshot.
- **Dead-column class** — a uniform/all-0/all-NULL column on fresh rows: scope to the CLASS (the semantic subfamily), enumerate every column on the dead side, assert distinct >> 1; check a rich SIBLING family to discriminate broken-compute vs absent-data; follow the cascade into derived artifacts.

**Decision-useful read** (the deepest smell): is the output meaningful for its consumer, or mechanically churning? (i) Gate-coverage honesty — would any structural check even cover this class (scores/embeddings are outside exact-match by construction). (ii) Quality-erosion — did a "make it pass/faster" arc quietly slash a lookback/sample/K/tolerance while every status stayed GREEN? (iii) Consumed-output meaning — run-to-run stability of the *consumed* decision (top-K membership, cohort labels, the rendered number's day-over-day plausibility). **Honest-limit:** a structural assessment is not an empirical measurement — assert only what's assertable, name the empirical probe as next step, never fake it, never silently drop it.

**META-CHECK smell heuristic** (the curious pass — apply to any number/value the unit emits): magnitude-vs-context (fits the book/asset-class/prior?), sign expectation (a "growth/gain" wrong-signed?), naming-vs-semantic (field name match what the code computes?), vintage (data_as_of vs the firm-wide settled date, cross-checked against siblings), units/grain. A mechanically-functional output that fails the META-CHECK is the BMKAUD class (fresh + valid-float + semantically wrong) — the highest-value smell to surface.

---

## The molecule report (output — on the record)

Write it so the analysis is **citable** and the smells + chain-map are preserved. Default: the invoker's `logs/{YYYY-MM-DD}/molecule_{HHMMZ}_{unit-slug}.md`. For a critical/recurring unit, also/instead a durable `org/molecule/{unit-slug}.md` so deep analyses accrue into a knowledge base. Commit under your own author line via `.tools/safe-commit.sh`.

```
# MOLECULE: <unit>   (scale: MICRO|MESO)
**archetype:** EXPLORE   (or DIAGNOSE/TRACE/VALIDATE per dominant work)

## Unit + expected role
## 1. Composition — what it actually is (vs declared); knowledge-parity drift
## 2. State — live snapshot characterized (numbers, not "looks fine"); N/A-with-reason if no state
## 3. Position in the chain — upstream / downstream / deps / reach (the lineage map) + seams to hand to /seams
## 4. Behavior — what the deployed path actually does (exercised or evidenced)
## 5. Semantic quality — sharp structural probe + decision-useful read

## Smell findings
| Smell | Rating (NOTE/WATCH/DIG) | Evidence (file:line / live state) | Why it caught my eye |

## Assessment
A plain-language read of what this unit IS and how it's doing — and, for any DIG smell, the explicit route (a /seams pass / a /verify-channel verdict / an owner finding). NOT a formal pass/fail gate — that's /verify-channel's function; molecule's output is the characterization + the smells.

## grounding: field (Rule 22 — per CAUSAL claim)
Pure characterization (Dimensions 1–2: what the unit IS + its live state) is STATE — grounded vs the live snapshot, no field. But any MECHANISM/causal claim — a smell "why", a chain-position causal ("X feeds Y because"), an Assessment "this is off because Z" — carries `grounding: SOURCE-CONFIRMED <file:line | comp-tool+output>` or `grounding: INFERRED (live-state-only)`. An INFERRED mechanism may PROMPT a /seams or source-check (its value) but is non-actionable and may NOT use the reserved words (proof / provably / root cause / definitively); absent field on a causal claim = not-accepted. Spec: `org/tier1_exec/3.0.0_SA_CVO/GROUNDING_FIELD_EMISSION_FORMAT.md` (Rule 22 / 53919cb32).

## Knowledge-parity delta + residual
Believed-vs-true; what record was corrected (commit) / routed to owner; what was NOT exercised.

## Compiler Tools
```

**Discipline:** could-not-verify = the finding "UNVERIFIED, here's why," never an assumed clean. Characterize-not-fix: route a code/runtime fix to the owner, a formal delivery/closeout verdict to `/verify-channel`; correct a stale *record* to parity yourself only if you hold that authority.

---

## Scope notes

- **Any agent** may run `/molecule` — it's a deep-analysis tool, not a gated role. Verification-minded agents (CVO) are heavy users.
- **Scale:** micro (one function/field/object) and meso (one script/Lambda/artifact/segment) are `/molecule`'s home. A whole-pipeline/project **closeout verdict** — the per-AC grid, Input 0 emission, Constitution-drift, ferry-review, REPAIR-AMENDMENT — is **`/verify-channel`'s** process, separate from molecule. molecule *feeds* it.
- **Not a launch cron** (LD-0175 — CVO arms zero crons). Invoked on demand.

## Invocation

| Form | Meaning |
|---|---|
| `/molecule <unit>` | Deep-analyze one function/object/field/artifact/script/Lambda (all five dimensions + smell pass). |
| `/molecule <unit> --dimension composition\|state\|chain\|behavior\|semantic` | Run one dimension (e.g. a fast chain-position map). Default = all five. |
| `/molecule <unit> --smell-only` | Skip to the curious pass — surface what catches the eye, lighter on full characterization. |

## One-line reminder

`/molecule` answers "what is *exactly* going on here, and where does it sit" — composition, state, chain-position, behavior, meaning — and writes down everything that caught its eye, because the benign-but-surprising thing you record today is the incident you don't have tomorrow.
