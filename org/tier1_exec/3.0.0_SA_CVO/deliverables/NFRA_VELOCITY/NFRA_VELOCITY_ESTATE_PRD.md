# NFRA_VELOCITY_ESTATE — PRD: the contracts, the estate, the measurement (main fabric)

**Program:** NFRA_VELOCITY (see `NFRA_VELOCITY_PROGRAM.md` — thesis, seam, metrics, constraints live
there and are cited, not copied). **Author:** `3.0.0_SA_CVO`, Andrew-direct commission + plan-review
approval 2026-07-29. **Canonical home:** `docs/architecture/NFRA_VELOCITY_ESTATE_PRD.md` (landed by
base CTO from this staged copy).
**Owner:** `1.0.0_SA_CTO` (arch-gate) · **Decompose/drive:** `2.0.0_SA_COO` · **Build:**
`0.7.0_AE_CloudOps` (infra/triggers), `0.4.0_DS` + `0.5.0`/`0.6.2` (pipeline contracts),
`0.2.0_DT` (portal/promote surfaces), 0.8.0-adjacent lanes where comp-tooling touches ·
**Verify:** `3.0.0_SA_CVO` · **Inter-fabric comms:** `0.0.0_AB_MSTR`.
**Constitution:** `docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md`.
**Founding statement:** `docs/briefs/NFRA_DEBTLOOPS_ANDREW_VOICE_MEMO_20260729.md` — *"we need to
figure out a comprehensive infrastructure solution so that we can lever up our development and be
able to produce fast and efficiently without getting caught up in verifying wild goose chases …
A big problem is type two errors where we do not have full recall. This is our highest priority at
this moment."*

## §0 Scope in one sentence

Make the live estate SAY what it promises (contracts), FIRE in the order it promises (triggers),
SHED what it no longer intends (retirement), and MEASURE itself honestly (telemetry + recall
denominators + archetype dynamics) — consuming CORE's type system and feeding CORE the live world
that validates it.

**Absorbs (closed as superseded, open work re-homed here):** NFRA_TOOLBHVR (→ WS-E6, R8 shared with
WS-E4), NFRA_COMPLEARN's reopened amendment scope (→ WS-E4), the NFRA_COMPDEBT design (→ WS-E3,
adopted verbatim as the safety layer), LIVELEARN's estate-side coverage half (→ WS-E5), MSBEFF
R4/R6/R8 (→ WS-E6/E4). NFRA_DEBTSCAN stays closed; its scan capability is reused by WS-E3.

---

## WS-E1 — Live contract declaration (the estate learns to say what it promises)

Declare D3 contracts for the live estate in a versioned, machine-readable, main-owned registry
(proposed home: `org/modules/graph/estate-contracts/`; git-carried; graph-materialized): per
artifact/process → `(writer, cadence, completeness_scope, canonical_source, successor?, lifecycle)`.
The **single-writer principle becomes a contract term** (a second writer at one `(key, grain)` is a
typed violation). Firm separation binds: bd/cot/inf contracts are declared per-firm and never
mirrored; 0824/0833 never-sum/never-substitute constrains contract content; each module's
consumer-anchored `PURPOSE` declaration is the contract's intent_source.

**Order of attack (value-ordered, coverage denominator printed every wave):**
1. **The specimen chain** — eclipse→silver→gold mdpf (inflection + cottonwood), the memo's live
   bronze-after-gold case measured same-evening on two firms.
2. The mdpf channels (fresh from the flip; contracts known).
3. bd/inf/cot gold chains.
4. Triggers + Lambdas + served surfaces.

Starts on WS-C1's **draft** D3 grammar and hardens at ratification — the specimen chain is the
vocabulary's test bed (one co-evolution round-trip budgeted; divergences feed back to WS-C1, not
worked around locally).

*Acceptance:* the specimen chain fully contracted end-to-end; **the bronze-after-gold violation
falls out as a type error** (or the rails are wrong — a WS-C1 feedback, loudly); coverage
denominator printed (contracted / total per tree).

## WS-E2 — Trigger-graph re-sequencing

Derive the full trigger graph (seed: `docs/briefs/TRIGGER_GRAPH_AND_RUNTIME_MAP.md`) with a
**two-system denominator** — EventBridge rules AND EventBridge Scheduler (the `aws events
list-rules` structural blindness is specimen #2; ~143 + 11 at last measure). Type every trigger
edge against the declared D2 paths. Violations: edges firing against the topological+temporal
order; **pipelines whose only trigger is another pipeline's success** (the schedule-floor law
already in CLAUDE.md — event-driven is an accelerator, never the only path); event-paths with no
cron floor. Fixes land under existing change management (safe-apply, deploy-completion ledger,
never-widen where serving changes).

*Acceptance:* the trigger graph is a queryable surface with its two-system denominator printed;
zero unscheduled production pipelines; the specimen-class mis-sequence structurally impossible
without a loud typed violation; every fix **exercised** — the re-sequenced run observed firing in
order from the run's OWN log (never manufactured; NEVER#4 governs ad-hoc runs as QA-only).

## WS-E3 — The debt retirement engine

Kill lists become **derived, never censused**: `expired_obligation ∪ superseded_with_live_successor`,
walked from WS-E1 contracts — the recall answer for debt (the population is enumerable from above,
so full recall is by construction, not by better scanning). The COMPDEBT design is adopted verbatim
as the safety layer:

- **Keep-dormant guard first:** Tier-A intent annotations (`keep-dormant.yaml`,
  `opal:lifecycle=keep-dormant`, re-arm annotations, rollback ledger entries, wired-fallback
  branches) → KEEP-DORMANT, near-sufficient alone; Tier-B corroborates; **Tier-C mechanical
  signals (bare DISABLED, 0 invocations, no consumer, git-cold) are NEVER sufficient** — they ARE
  the debt signals, and a deliberate belt and a corpse are identical on every one of them.
- **DEBT-DECOMMISSION requires ≥2 CONFIRMED signals + no contradicting live-use + guard ruled
  out**; a single confirmed signal stays advisory. Default FAIL-SAFE = KEEP-DORMANT (a missed
  corpse is recoverable; a decommissioned belt is the named failure mode).
- **Execution discipline:** the unit of retirement is the WRITE, not the producer (LD-0330 —
  identity_2-class live-gate preservation checked per retirement); never-widen sign-off where a
  served surface is touched; every retirement exercised, not inferred.

**THE TRANSIENT TRAP (~C item 3 — binding on this workstream):** derivation supplies INTENT, which
mechanical signals provably cannot — but derivation cannot supply TRANSIENCE. A live
written→consumed→deleted trigger marker (`gold/trigger-pending.json` class) is **absent from S3 at
every moment you look**, and it independently reads absent AND dormant AND reader-less — so the
≥2-CONFIRMED bar passes on two signals that are both wrong, on a live pipeline trigger. **No
retirement executes against a key whose contract lacks a lifecycle value; a `TRANSIENT`-contracted
key is exempt from existence-based signals entirely** (WS-C1 carries the vocabulary; the
comp-legacywriter TRANSIENT-MARKER guard @d51f6b38a0 is the stopgap until it lands).

**E3.0 — THE SAFE SLICE, PULLED TO P1 (~C item 4):** the Tier-A subclass needing no contract
registry and carrying near-zero blast radius BY CONSTRUCTION — `archive/` + `diagnostics/` +
`test_*` writers targeting keys holding NO OBJECT (nothing to delete, nothing to re-point, no
reader to break). Retire that slice at P1: it exercises the retirement gates while the stakes are
trivial (prove the loop on the safe population, not first on something that matters) and gives the
program an early visible win against an otherwise back-loaded payoff.

**First adjudicated population: the 353 dead surfaces** from `comp-legacywriter --census`, joined
against contracts as they land.

**RECALL SCOPING (~C clean-read finding 2 — binding):** "full recall by construction" holds OF THE
CONTRACTED SET — the derivation's recall EQUALS contract coverage, which starts near zero and grows
through P1–P3, while today's debt lives precisely in the uncontracted complement (the 353 were
derived from SOURCE; none is contracted yet). The derived engine and the census cover
**complementary populations** (contracted+intent vs all-source-visible+no-intent). Retiring the
census while coverage is partial makes actual recall FALL at the moment the program reports it
rising — the denominator-shrinks-and-looks-like-progress shape inside the workstream built to
prevent it. **The census retires when the coverage gap is zero, not when the engine works.**

*Acceptance:* E3.0 safe-slice retirements executed clean at P1 (the gates exercised, denominator
printed); the derived kill list exists with its derivation printed; **every wave states BOTH
numbers — the derived-from-contracts count AND the census-only count (surfaces the derivation
structurally cannot see), with the gap named as coverage debt**; ≥N contract-derived retirements
executed under gates at P3 (N set at decomposition); **zero new C-SILENT residents going forward**
— a resource created without a contract is a commit-gate warning ramping to a deny
(announce-then-enforce); zero retirements against uncontracted-lifecycle or TRANSIENT keys.

## WS-E4 — The measurement plane (can we answer "are we improving?")

1. **Land the M3/telemetry fix as already gate-approved** (main CTO via MSTR, three binding
   conditions): the verdict set DERIVED from declared exit contracts via the registration
   invariant, never a frozen list; **UNKNOWN-CONTRACT is a loud verdict, never defaulted** (with
   the required mutant: one deliberately undeclared tool surfaces as UNKNOWN); supersession history
   recorded; historical rows re-baselined so trend claims stand on corrected data — **preserving
   the ORIGINAL rows alongside the re-baselined ones under a `verdict_basis` version column** (~C
   clean-read finding 3): a rewritten-only history cannot separate "the verdict logic changed"
   from "the estate changed" — both move a re-baselined series identically, and the discriminating
   residue is unrecoverable if not kept now. Every trend claim re-derivable under either basis,
   which also makes the §8 no-aggregate-headline rule checkable ACROSS the re-baseline boundary.
2. **Separate the FAIL column's three meanings** — deliberate negative-control probes · tool usage
   errors · genuine findings — the two-meaning-null that currently makes "are we getting better?"
   unanswerable in either direction.
3. **Re-derive C5 independently** (the aggregate-FAIL mix-shift: 12.14%→6.14% headline over
   offsetting per-series moves) — the taxonomy handoff's V2 — and make **per-series decomposition
   the standing form**: no aggregate headline without it.
4. **Stand up the program metrics baseline** (program doc §5) so every later claim has a P1 anchor.

*Acceptance:* the three meanings separated in the machine record; "are we improving" answerable
per-series with denominators; baseline published.

## WS-E5 — Estate sensors and recall denominators

**Framing (~C item 1):** this is the measurement-time quadrant — the estate's commit-time gating is
dense and demonstrably catches; measurement-time control is near-zero, and it is where 2026-07-29's
control failures all lived. This workstream fills the empty quadrant; it does not add commit-time
gates.

Apply the recall standard (WS-C7; ships against L0a's boundary-report type as-is — it is DONE — and
migrates when C7's registration invariant lands) to **estate detectors**: freshness, drift, debt,
trigger checks, deploy verifies. Every detector emits address space + traversal residue + failure
direction; a detector that cannot state what it could not have seen prints that as its first line.
The **nine same-day false-negative specimens** become the estate-side conformance suite:
AccessDenied-indistinguishable-from-absent · list-rules Scheduler blindness · name-substring
predicates · UTC-4 LastModified misreads · terraform "No changes" as success · rc=0 PASS/STALE
conflation · not-due default literals · the two self-authored unfailable acceptance criteria.

**THE ENFORCEMENT MECHANISM (~C clean-read finding 1 — without this the invariant below is a diary
entry by this PRD's own TRIGGER_LAYER clause):** estate detectors are not comp-tools — no
comp-manifest-check ever sees a freshness Lambda, an EC2-side gold check, or a deploy verify, so
there is no registration event to gate and no detector registry to attach an invariant to.
Resolution (registry-reuse, not a parallel one): **an estate detector IS a contracted process — it
registers in the WS-E1 estate-contract registry, and its contract carries its boundary
declaration.** The WS-E3 C-SILENT commit-gate ramp (warning → deny on the producer trees) then
covers detectors exactly as it covers writers: a new/edited detector lacking a contracted boundary
declaration trips the same gate. One registry, one gate; E5's enforcement is therefore a stated
dependency on E1's registry, which precedes it in the phase order.

*Acceptance:* N of M estate detectors emitting boundary reports (count printed; target set at
decomposition); the nine-specimen suite green estate-side; **no new detector past the gate ramp
without a contracted boundary declaration carrying its recall denominator — enforced by the WS-E1
registry + WS-E3 commit gate, not by prose.**

## WS-E6 — Behavioral / harness (the last mile, measured)

TOOLBHVR executed where the harness lives (the four selection paths — memory / HUD / rail / router
— streamlined as ONE system):

1. **R8 conversion instrument first:** a route id carried into the subsequent run so route→run is
   joinable; comp-which self-reports into telemetry (closing the 295× under-report). Until
   conversion is measurable, every behavioral claim is unfalsifiable.
2. **R4 trigger binding:** closeout→`comp-state`, deploy→`comp-pipescript deployed` — the unrun
   tools move from *available* to *fires-at-a-moment-of-work* per TRIGGER_LAYER; firing
   mutant-proven; output lands as an owned item, not a log line.
3. **Path tuning:** with conversion measured and queries typed (WS-C6), map query-layer →
   selection-path → correct-tool rate; reduce friction on paths that work; retire nudges that
   misfire. **Protect the memorized head** — never insert a router hop where memory already routes
   correctly (a forced hop is a latency tax that trains skimming).

*Acceptance:* router conversion rate reportable with a denominator; both bound triggers
demonstrably fire at their moments (mutant-proven); ≥1 friction reduction validated against the
measured map.

## WS-E7 — Live error intake + archetype dynamics (Andrew-direct at plan review; the ESTATE half of WS-C9)

The intake side of the living schema: every error surfacing in the fabric — a telemetry FAIL (with
WS-E4's three meanings separated), a gate denial, a CVO/verification finding, a postmortem entry —
carries a mechanism classification **at occurrence**, cheap, while the context exists (never
archaeology later; the ~34,000-documents-of-evidence vs 14-of-doctrine ratio is what
classify-at-intake closes). On top of intake, the **archetype weight + dynamics report**: the
standing per-window distribution of error mass by mechanism class — which archetypes carry the
weight, which grow, which shrink, the N-SELF rate, the D1-vs-D4 catch share.

This is the program's steering signal, indefinitely: a **growing** archetype is a measured demand
signal into WS-C3's pattern inventory and WS-C4's synthesis queue (the next tool/gate, ranked by
weight); a **shrinking** one is a gate visibly absorbing its class (the PREVENTION ruling working);
a class no gate is absorbing is a standing finding with an owner. Deterministic-first
(rc/gate/telemetry joins classify mechanically where they can; judgment classifies the rest via the
intake form); renders as a report + owned items per TRIGGER_LAYER — **never a notification** (the
moratorium holds).

*Acceptance:* every error-surfacing channel feeds intake (channels enumerated; coverage denominator
printed); the dynamics report renders per-window with per-class trend; ≥1 tool-evolution decision
demonstrably driven by archetype weight (the ranked queue cites the distribution); the loop is
closed — a deliberately introduced error class (mutant) appears in intake, in the weights, and in
the queue.

---

## Phases

**P1** = E4.1 telemetry fix + E1 specimen chain (starts on WS-C1's draft grammar) + **E3.0 safe-
slice retirements** (~C item 4 — the gates exercised on the zero-blast population first) →
**P2** = E2 triggers + E1 breadth →
**P3** = E3 contract-derived retirements + E5 sensors →
**P4** = E6 tuning →
**P5** = E7 (live intake + dynamics — last, and then standing forever).
*(PLACEMENT RULED — Andrew-direct 2026-07-29 ~23:2xZ, verbatim: "the reason it is at the end, is
because it is going to steer the fabric/estates velocity infrastructure in perpetuity." P5 stands;
~C item 7 resolved: construction-time ranking uses the static corpus weights (taxonomy 210 +
MSBEFF 718 + 187 override-demand), current at program start by construction; E7 takes over the
ranking at P5 and keeps it current forever.)*

## Governance

Base CTO arch-gates; COO decomposes to TOs (with `comp-blast` cross-domain flags per the parallel-
wave protocol) and drives; workers per lane; base CVO verifies; MSTR carries inter-fabric comms per
program doc §4 (per-wave summaries to MSTR~Z, relayed to each CTO). Vocabulary questions route to
~Z's ratification chain via the bus — never patched locally. comp-tool STANDARD changes gate at
main CTO. Program-level constraints (alarm/monitor moratorium, LD-0175 event-driven-only,
TRIGGER_LAYER, firm separation, deterministic-first, announce-then-enforce gate ramps) bind per
program doc §6. Sovereign holds unchanged: no bd/49F/Schwab scope beyond what standing rulings
permit; client-data pipelines stay T-1-defaulted under the trading calendar (NEVER#1) — a WS-E2/E5
finding about timing is resolved against the trading calendar before it is called a defect.
