# NFRA_VELOCITY — the program: one objective function, two PRDs, two fabrics, one seam

**Author:** `3.0.0_SA_CVO`, Andrew-direct commission + plan-review approval, 2026-07-29 (~22:1x–22:4xZ, Andrew's terminal)
**Status:** program architecture of record (plan approved by Andrew at review; this renders the approved plan)
**Canonical home:** `docs/architecture/NFRA_VELOCITY_PROGRAM.md` (ANY_CTO-gated — landed by base CTO from this CVO-staged copy)
**Constitution:** `docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md`
**The two PRDs:** `NFRA_VELOCITY_CORE_PRD.md` (~Z site fabric) · `NFRA_VELOCITY_ESTATE_PRD.md` (main fabric)

---

## §0 Andrew's charter, VERBATIM (CVO terminal, 2026-07-29)

The founding intent (~22:0xZ):

> "The goal is to warp our infrastructure on the graph and tooling side with one explicit goal, which
> is to rapidly accelerate production. The issue with rapidly accelerating production is that you
> create debt. You get out of pattern, you pivot a lot, resources aren't cleaned up, stuff is laying
> around everywhere and this confuses agents and makes code spaghetti and the opposite of speed and
> robustness. … I want to figure out how to work NFRA_ONTOLOGY2, and from the ground up consolidate
> ontology and all of our product, to create an absolute weapon for agentic engineering and
> development."

The commission (~22:3xZ):

> "wrap all of this into one mega project, called NFRA_VELOCITY. I want all the best ideas from these
> unfinished projects wrapped into it. Because it is really important that we do this right, i want
> you to plan it out in depth, and I will review it. That plan will become the PRD. The PRD needs to
> be big, it needs to have a lot in it, because what I'd like to do is run our fabric, and the ~zsite
> fabric on the terminal on this at the same time, which means the project really needs to be two
> PRDs covering different surface areas that work synergistically together. the relevant MSTR agents
> from each side will maintain inter-fabric comms with their progress, which they will share with
> their respective CTOs for the sake of facilitateing organized collaboration as they grow."

The plan-review addition (~22:4xZ — the standing-evolution requirement, WS-C9/WS-E7):

> "when errors inevitably still come up, there needs to be a classification schema for errors, so we
> can continue to drive the evolution of the tool based on error archetype weight and dynamics as the
> loop/fabric proceed indefinitely. This is a P2/P3, it should be at the very end of the respective
> CORE and ESTATE group's work, but it is essential to keep the loop alive and the velocity
> accelerating."

**Source artifacts (the three corpora that converged 2026-07-29):**
`docs/briefs/NFRA_DEBTLOOPS_ANDREW_VOICE_MEMO_20260729.md` (the founding voice memo — highest priority:
*"type two errors where we do not have full recall"*) ·
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/INCIDENT_TAXONOMY/` @31a038f0f (210 incidents, 14
mechanisms, 55% carried by four; designed controls caught 2.4%; 80% fail toward PASS) ·
the NFRA stack (ONTOLOGY2 / TOOLARCH / TOOLSEM / TOOLBHVR charters, the COMPLEARNS/GRAPHLEARNS L0–L3
loop, MSBEFF R1–R8, LIVELEARN, TOOLUNIFY, the COMPDEBT design).

## §0b Sovereign rulings received at plan review (2026-07-29, recorded + broadcast)

| Ruling | Answer |
|---|---|
| Fabric split | **CORE at the ~Z site fabric / ESTATE at the main fabric** |
| Absorbed projects | **Close as complete-as-superseded**, citing NFRA_VELOCITY, open work re-homed |
| Corpus intent (the question MSTR fenced as Andrew's alone — 00_SUMMARY §6, prevent vs metabolise) | **PREVENTION** — the doctrine collapses into mechanism-laws + gates; doctrine SHRINKS as gates absorb classes |

## §1 The thesis

**Velocity = throughput × certainty.** The estate loses velocity two ways, and they are the same law
at two timescales:

- **In space (the incident class):** an agent reasons correctly inside a sample whose edge it cannot
  see — the sensor bounds the oracle; 80% of recorded failures are silent false-cleans (Type II /
  recall).
- **In time (the debt class):** a pivot changes intent without re-enumerating the denominator; the
  abandoned half keeps existing, keeps writing, keeps matching greps — and every future agent pays a
  search tax on residue nothing marks as dead. **A legacy writer is yesterday's intent still
  executing inside today's denominator.**

The remedy is one type system and one loop:

- **The type system (CORE):** the ratified C0–C3 ladder + the D1 (value/grain), D2 (path/flow +
  cadence), D3 (contract/obligation) rails + **the lifecycle/supersession extension to D3**: every
  contracted resource/process carries `(intent_source, obligation, successor?, expiry_condition?)`.
  Then a legacy writer, a clobber, and a bronze-after-gold mis-sequence are *typed violations* — by
  definition, not by heuristic.
- **The loop (both fabrics):** the archetypal learning loop — denominators pinned to version heads;
  head advance → re-derive → delta → Route A (autonomous) / B (instrument fix, mutant-proven) /
  C (model change, inference-gated under the machine-runnable output contract). Determinism computes
  the residue; inference is rationed to naming new axes and pays for itself in new determinism.
  **Recall stops being a scanning problem when the population is derivable.**

**The bar (Andrew's, from MSBEFF §0, extended):** a light query against standing Opal context makes
both the intent and the completing context immediately obvious — *and a pivot leaves nothing behind
that a future agent must archaeologize.*

## §2 Program architecture

```
                    NFRA_VELOCITY  (this program doc)
                    constitution: INTENT_DENOMINATOR_SYNCHRONIZATION.md
        ┌──────────────────────────────┴──────────────────────────────┐
        │                                                             │
  PRD-1: NFRA_VELOCITY_CORE                    PRD-2: NFRA_VELOCITY_ESTATE
  ~Z SITE FABRIC                               MAIN FABRIC
  (CTO~Z design/gate · 0.8.0_AE+~lanes build   (base CTO arch-gate · COO decompose ·
   · 0.8.0_AE~C rule-bank · CVO~Z verify        0.7.0/0.5.0/0.4.0/0.2.0 workers ·
   · MSTR~Z inter-fabric comms)                 base CVO verify · MSTR inter-fabric comms)
        │                                                             │
  The TYPE SYSTEM + the LOOP + the TOOLS       The CONTRACTS + the ESTATE + the MEASUREMENT
  WS-C1 rails D1/D2/D3 + lifecycle             WS-E1 live D3 contract declaration
  WS-C2 expressiveness validation (3 corpora)  WS-E2 trigger-graph re-sequencing
  WS-C3 archetype census + pattern inventory   WS-E3 debt retirement engine
  WS-C4 stability grader + tool synthesis      WS-E4 measurement plane (telemetry fix + metrics)
  WS-C5 learning loop L2 + L3 inference gate   WS-E5 estate sensors / recall denominators
  WS-C6 typed routing (comp-which successor)   WS-E6 behavioral/harness (triggers + conversion)
  WS-C7 recall standard (boundary reports)     WS-E7 live error intake + archetype dynamics
  WS-C8 doctrine collapse (PREVENTION ruling)     (P5 both sides — the standing evolution loop)
  WS-C9 living error-classification schema
        │                                                             │
        └────────────────────────── THE SEAM ─────────────────────────┘
          artifact plane: git (origin/CLOUD, shared by both sites)
            vocabulary flows Z→main as VERSIONED RULE-BANK HEADS
            evidence flows main→Z as CONTRACTS + TELEMETRY + SPECIMENS
          coordination plane: agentbus (same-principal device bus)
            MSTR(base) ↔ MSTR~Z · COORD-ONLY (Andrew 07-29: ~Z never routes
            work to main; routing stays inside each fabric's governance) ·
            each MSTR relays to its own CTO
```

**Why this split is safe:** it follows the standing fabric shape exactly (~Z is chartered
NFRA/ontology-only and fenced off main routing; main owns estate, deploys, pipelines). File-surface
collision is structurally low: CORE writes `org/modules/graph/`, `infra/system/ontology/`, `.tools/`
synthesis machinery; ESTATE writes `infra/aws/`, pipeline contracts, trigger config, the telemetry
appender. The two shared surfaces have single owners: the rule bank is Z-owned (main re-pins);
doctrine/law surfaces are authored anywhere but **landed only via main CTO**.

## §3 Consolidation map — where every unfinished project went

| Project | Disposition |
|---|---|
| NFRA_ONTOLOGY2 | Absorbed → WS-C1/C2. The "not a new graph / derivable from existing contracts" clause is **explicitly superseded**: declaring the contracts IS the work (WS-E1). Closed as superseded. |
| NFRA_TOOLARCH | Absorbed → WS-C3/C4. Closed as superseded. |
| NFRA_TOOLSEM | Absorbed → WS-C6. Closed as superseded. |
| NFRA_TOOLBHVR | Absorbed → WS-E6 (harness surfaces live on main), R8 shared with WS-E4. Closed as superseded. |
| NFRA_TOOLSTACK program doc | Superseded-by-VELOCITY header; stays as provenance. |
| NFRA_MSBEFF | Audit complete; R1/R3→WS-C7 · R2→D2 query (WS-C1/E1) · R4→WS-E6 · R5→WS-C4 · R6 landed · R7→WS-C6 · R8→WS-E4/E6. Closed complete. |
| NFRA_PSTMRT | **Stays open as dependency** (firm-registry SSoT + completeness gate = first live enforcement of the constitution). Revisit fold-in at program P2. |
| COMPLEARNS/GRAPHLEARNS L0–L3 | Absorbed → WS-C5 (the loop is VELOCITY's engine); `infra/system/ontology/` design docs are CORE's substrate. |
| NFRA_COMPLEARN (Trino tool_activity) | Absorbed → WS-E4; AMD scope re-cut there. Closed as superseded. |
| NFRA_LIVELEARN | Absorbed → WS-C5/E5 (its bar becomes loop acceptance). Closed as superseded. |
| NFRA_TOOLUNIFY | Absorbed → WS-C7 (provenance register, negative-declaration axis, O2 contract adoption = the recall standard). Closed as superseded. |
| NFRA_COMPDEBT (design) | Absorbed → WS-E3 (keep-dormant guard + ≥2-CONFIRMED bar adopted verbatim; the six signals corroborate UNDER the lifecycle derivation). |
| NFRA_DEBTSCAN | Stays closed; scan capability reused by WS-E3. |
| INCIDENT_TAXONOMY corpus | The validation corpus + WS-C8 input; the base-CTO follow-on project = WS-C8's main-side landing lane. |
| DEBTLOOPS memo | The founding statement. Its A/B/C: A=WS-C3 · B=WS-C4/E1 · C=WS-C5. |

### §3b The absorbed open-work ledger (anti-opacity control — ~C item 6)

Absorbing 8 projects converts eight visibly-stalled records into one opaque one; if VELOCITY stalls
at P2, "absorbed" reads as "handled" — the stale-record-with-authority class applied to the
consolidation itself. Control: **this ledger stays current in the program index; a stall stays
visible at the grain someone can act on.**

| Absorbed project | Open work carried | Home | Named owner |
|---|---|---|---|
| ONTOLOGY2 | P1 rail authorship → P4 typed routing | WS-C1/C2 | CTO~Z + 0.8.0_AE~C |
| TOOLARCH | census → inventory → grader → synthesis | WS-C3/C4 | CTO~Z + 0.8.0_AE |
| TOOLSEM | parser → router → gap-feed | WS-C6 | CTO~Z + 0.8.0_AE |
| TOOLBHVR | R8 conversion · R4 triggers · path tuning | WS-E6 (R8 w/ E4) | base CTO/COO + 0.7.0/hook lane |
| COMPLEARN | AMD loop-closure scope (re-cut) | WS-E4 | COO + assigned build lane |
| LIVELEARN | fresh-when-consumed + prove-loop-closes cycles | WS-C5/E5 | CTO~Z (C5) / base CVO (E5 verify) |
| TOOLUNIFY | provenance register · PENDING slots (E/B verdicts, MATCH spot-checks) · negative-declaration axis · O2 adoption | WS-C7 | CTO~Z + 0.8.0_AE |
| MSBEFF | R-cells per §3 row; M3 telemetry re-baseline | WS-E4/C7/C6 | per row; E4.1 = main CTO gate-approved build |

## §4 The seam — four protocols

1. **HEAD-ADVANCE NOTICE (Z→main).** CORE publishes a new rule-bank/type-system head
   (`meta.version`) → MSTR~Z notices MSTR(base) (version, delta, migration notes) → base CTO
   re-pins estate consumers. Estate consumers carry version pins, so a missed notice reads STALE
   loudly.
2. **EVIDENCE REQUEST (Z→main, fulfilled by main).** CORE needs estate measurements → request over
   the bus → COO dispatches main workers → results land in git → pointer back. Never a ~Z spawn on
   main surfaces.
3. **GATE-CROSSING CHANGES.** comp-tool STANDARD changes → main CTO gate BEFORE landing (standing
   MSBEFF §6 carve). Vocabulary → Z ratification chain. Doctrine/CLAUDE.md/law surfaces → landed
   only via main CTO. Registration-invariant extensions (WS-C7) → main CTO gate.
4. **PROGRESS SYNC.** Per-wave MSTR↔MSTR summaries (workstream, delta, next gate, blockers), each
   relayed to its own CTO — Andrew's stated collaboration shape. Joint state review at each program
   phase boundary. Every cross-fabric message carries `(prd, workstream, head_version)`.

**Collision control:** `.owned-paths.yaml` amended at registration (CORE surfaces → ~Z-side authors;
ESTATE surfaces → main-side authors); one owner per file, the other fabric consumes via git.

**Hard cross-PRD dependency edges:** E1 starts on C1's **draft** D3 grammar and hardens at
ratification (the specimen chain is the vocabulary's test bed — one co-evolution round-trip
budgeted) · E3's kill-list derivation needs C1 lifecycle ratified · E5 ships against L0a as-is and
migrates to C7's standard · C2's specimens are already in hand · C6's conversion acceptance needs
E4's R8 instrument.

## §5 Program metrics (baseline at P1; per-series with denominators, never an aggregate headline)

1. **Time-to-certainty** — typed answer or honest empty; proxies: rail-override rate (187/mo
   baseline), wild-goose-chase sessions, router honest-empty rate (0 today).
2. **Recall denominators exist** — % of tools/detectors emitting boundary reports (≈0 today).
3. **Catch distribution shifts** — D1 designed-control catches rise from 2.4%; D4 somebody-read-it
   falls from 57%. The PREVENTION ruling, made measurable. **Read 2.4% as a PLACEMENT failure, not
   a design failure** (~C, 2026-07-29, evidence-grounded): the estate's commit-time gating is dense
   and catches constantly — those catches never become recorded incidents, so the incident-derived
   D1 share structurally under-counts them; the empty quadrant is **measurement-time** controls,
   which is exactly what boundary reports (WS-C7/E5) are. The program aims at the gap, not the
   strength — more commit-time gates is NOT the licensed conclusion.
4. **Debt population derived and shrinking** — contracted coverage rises; derived kill list shrinks
   **paired with retirements EXECUTED under gates** (a shrinking list alone is Goodhart-able by
   narrowing the predicate — ~C item 5); zero new uncontracted writers past the gate ramp; the 353
   dead surfaces adjudicated.
5. **Doctrine shrinks as gates absorb** — byte-count + per-file self-violation rate, **paired with
   the count of M-laws carrying a NAMED GATE that absorbs their class** (byte-count alone falls by
   moving text to references/, which WS-C8 explicitly does — ~C item 5).
6. **The specimen never recurs** — bronze-after-gold structurally impossible without a loud typed
   violation.
7. **Telemetry answers "are we improving"** — per-series FAIL decomposition, three meanings
   separated.
8. **Archetype dynamics steer the program** (WS-C9/E7, standing) — per-window error mass by
   mechanism class with trend; the synthesis/gate queue demonstrably ranked by it; a class's weight
   falling after its gate lands is the program's proof-of-work, indefinitely.

## §6 Standing constraints (bound into both PRDs)

- **Alarm/monitor moratorium (Andrew 07-28):** every deliverable lands as a GATE, a TYPED CHECK, or
  an OWNED BLOCKING ITEM — never SNS/SES/alarms/`*-monitor`-named functions. This commissioning
  authorizes the sensing machinery named in these PRDs; anything notification-shaped still requires
  Andrew's explicit word.
- **LD-0175 zero crons:** the loop is event/consumption-driven. Any server-side scheduled runner is
  infrastructure, CTO-gated, and must itself carry a D3 schedule contract — the program dogfoods its
  own law.
- **TRIGGER_LAYER:** a finding that cannot fail a gate is a diary entry.
- **Firm separation:** bd/cot/inf contracts never mirror; 0824/0833 never-sum/never-substitute binds
  contract content.
- **Deterministic-first:** no LLM in classification loops; inference rationed to the gate; output
  must be machine-runnable (the persistence rule).
- **Gate ramp discipline:** new coverage gates enter announce-then-enforce (warn → deny with audited
  override), the COMPRAIL precedent.

## §7 Verification regime

CVO~Z verifies CORE once across the family; base CVO verifies ESTATE. At each program phase
boundary, each CVO runs one adversarial pass on the OTHER PRD's phase deliverable — fresh eyes
across the seam (two instruments sharing a sensor is one measurement counted twice; the law applied
to verification itself).

## §8 Risks (named, with mitigations)

Wrong-grained rails (the expensive wrong-C) → WS-C2 expressiveness validation before freeze + the E1
specimen round-trip; CTO~Z review concentrates here. · Contract-declaration stalls at breadth →
value-ordered attack, coverage denominator printed every wave, gates ramp only with coverage. · Seam
drift → version pins on every cross-fabric claim. · The collapse deletes something load-bearing →
nothing deleted (instances become rows; dated material → references/); nothing Andrew called good is
cut without his word; main-CTO gate on every law-surface land. · Retirement harms a live path →
COMPDEBT fail-safe defaults + ≥2-CONFIRMED bar + never-widen sign-off + exercised-not-inferred per
retirement — **and the TRANSIENT lifecycle trap** (a live written→consumed→deleted trigger marker
reads absent AND dormant AND reader-less — two confirmed signals, both wrong; closed by the WS-C1
TRANSIENT vocabulary requirement, ~C item 3). · **Consolidation opacity** (8 stalled records become
one opaque "absorbed" — ~C item 6) → the §3b open-work ledger with named owners, kept current. ·
**Steering signal arrives after the voyage** (C9/E7 at P5 means the synthesis queue is
judgment-ranked all program — ~C item 7) → proposed minimal hand-classified intake at P1,
**FLAGGED PENDING ANDREW's word** (he placed the schema at the very end; the P1 form is an intake
slip, not the schema build).
