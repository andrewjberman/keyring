# MSTR Input 1 Channel Architecture

**Author:** `0.0.0_AB_MSTR`
**Authored:** 2026-05-24T20:00:00Z (V1 — post Opal CTO + MSTR working-session lock 19:45Z + Beat 2 LD-0043 commit)
**Status:** V2 — §6 [COMPILER-ASK] mechanism LOCKED per ws CTO + ws CVO joint-decide verdict (`66ce7c024`) + Andrew sovereign preemptive ratification 2026-05-24T~2128Z + CVO FN-2 sharpening on Q-D ack-shape folded; LD-0051 establishment. V1 substance §0-§5 + §7-§8 unchanged.
**V2 amendment authority:** Joint ws CTO + ws CVO under Andrew preemptive ratification grant per LD-0026 generalized one tier down (operating-mode doctrine: Andrew preemptive ratification + joint Tier-1 verdict = paired ratification when Andrew working-session slot is delegated)
**Authority:** D-003 v1.11 cross-fabric facilitation (codifies three-Input model + Input 1 channel mechanics; scope items xv-xviii)
**Tier-0 commit hash:** `d355302c1` (canonical post DIRECTIVES v1.11 ship; CONSTITUTION v1.2 + STAKES_MATRIX v1.4 unchanged at `1a515b769`)

---

## §0 — Purpose + scope

This document defines the MSTR-internal mechanism for the **Input 1 channel** — the inter-fabric pathway that surfaces Opal-derived compiler-shape opportunities into COMPLEARNS R&D queue without distracting Opal CTO from Opal product work.

Companion artifact on the CL side: `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` V1.1 §5 (CL CTO's view of the same channel from the consumption side). This MSTR doc covers the **mechanism** — how MSTR detects, packages, routes, and reports; the CL doc covers the **contract** — what CL CTO does with what MSTR delivers. Both are canonical; neither is sufficient alone.

**Authority chain (per CONSTITUTION Art. VI + Art. XV):**
- Andrew sovereign authority over all components
- MSTR governs the channel (orchestrator + ferry, not foreman)
- Opal CTO retains lane sovereignty on Opal product work; never gates on channel
- CL CTO retains end-authority on Input 2/3 (accepts/counter-routes Input 1 briefs at scope)

---

## §1 — Two-source hybrid detection (Source A passive + Source B urgent)

The channel detects Input 1 candidates through two complementary sources. Both feed the uniform outbound brief shape (§3); neither alone is sufficient.

### §1.1 — Source A: Passive stimulus-scan (MSTR-side default)

MSTR's `/govern` Step 1(b) population scan catalogs six signal classes per cycle. Clusters surface Input 1 candidates at cycle boundaries.

**The six signal classes (post-V1.1):**

| Class | Detection mechanism | Lagging/Leading |
|---|---|---|
| **(1) Highest-trafficked rails** | comp-trace edge counts + Lambda invocation counts + broker MCP call frequency | Leading (where work flows) |
| **(2) Bug-frequency rails** | git log "fix\|bug" mining + RAVC reject counts + comp-validate ADVISORY history | Lagging (where bites surface) |
| **(3) Mechanical-fidelity failures** | comp-validate failure history + column-gap incidents + lambda-source-map drift | Lagging |
| **(4) Meta-fidelity failures** | CVO YELLOW verdicts + semantic-mislabel patterns + magnitude-sanity firings (F-005) | Lagging (boundary — CL CTO counter-route authority preserved per V1.1 §5.4-mapping) |
| **(5) Body-class generalization** | comp-trace coverage gaps on new file types / IaC / data pipelines | Leading (adopted from CL §7.3 V1.0) |
| **(6) High-cost-archetype clusters** | archetype-tag × frequency × shape-weight aggregated cross-fabric per `org/tier0/COMPILER_ARCHETYPES.md` | **Leading — the durable signal class.** Per Opal CTO V1.0 design insight: bite-frequency is lagging + structurally decreases as logging/comms improve; high-cost-correct repeated activity is the durable leading indicator. Compiler tooling's highest leverage is cost, not bugs. |

**Aggregation cadence:** at the start of each `/govern` cycle, MSTR runs the six-class scan; clusters meeting brief-surface threshold (§4) generate Input 1 candidate briefs.

### §1.2 — Source B: `[COMPILER-ASK]` urgent flag from Opal CTO

When Opal CTO experiences an acute pain point that Source A's cycle cadence would surface too slowly, Opal CTO emits a single MCP to MSTR with `[COMPILER-ASK]` subject prefix. MSTR fast-paths the brief to CL CTO same-cycle.

**Opal CTO side responsibility (`[COMPILER-ASK]` mechanism):**
- Emit single MCP to MSTR (`opal-agent-comms send_message`)
- Subject begins with `[COMPILER-ASK]`
- Body content shape: at Opal CTO's discretion — minimum viable is "X is biting"; richer is "problem statement + recurring class + workaround cost + impact on live work"
- Cost on Opal CTO side: ~3 minutes per emission, rare frequency (only when acutely biting)

**MSTR side responsibility on receipt:**
- Acknowledge within same cycle
- Fast-path to brief packaging (§3 format)
- Ferry to CL CTO same-cycle (does not wait for next `/govern` cycle boundary)
- Roll into next `/mstr_review` D-003 reporting section for visibility-back-to-Opal

**Design constraints (Opal CTO protection):**
- No standing meetings
- No required weekly reports
- No persistent file Opal CTO must maintain
- No subscription/notification system adding to inbox noise
- No urgency-scoring or classification requirement on Opal CTO side (just flag-and-forget if that's what works)

### §1.3 — The two-source resilience property

The hybrid is robust because:

| Source | Catches |
|---|---|
| A (passive scan) | Patterns Opal CTO doesn't have time to flag explicitly; cost classes (1, 5, 6) Opal CTO might not see from their lane |
| B (urgent flag) | Acute biting that Source A's cadence (cycle-boundary) would surface too slowly; specific cases Opal CTO has unique visibility into |

Both sources feed the same outbound brief shape (§3). CL CTO doesn't need to know which source triggered a brief; uniformity preserved.

---

## §2 — Brief threshold heuristics

When does a Source A cluster cross the "surface as Input 1 brief" threshold? Initial heuristics, refined empirically as first briefs surface.

### §2.1 — Per-class threshold heuristics

| Class | Initial brief-surface threshold |
|---|---|
| (1) Highest-trafficked | Top-3 rails consume >50% of fabric MCP/Lambda invocation in trailing 5-day window + at least one is showing degradation (latency / failure / capacity) |
| (2) Bug-frequency | >3 fix-commits in same path class in trailing 7-day window OR recurring RAVC reject same surface |
| (3) Mechanical-fidelity | 2+ comp-validate ADVISORY incidents in same script class in trailing 7-day window |
| (4) Meta-fidelity | CVO YELLOW verdict on semantic-mislabel class — surface ONLY if MSTR judges compiler-shaped (boundary class; counter-route expected on many) |
| (5) Body-class generalization | New file/IaC type appears in fabric work surface 3+ times in trailing 7-day window with no existing recognizer coverage |
| (6) High-cost-archetype | Top-1 archetype consuming >40% of weighted sum in trailing 5-day window with mostly-correct activity (DIAGNOSE/EXPLORE/TRACE dominate vs. IMPLEMENT/SCRIBE) |

**Override heuristic:** if Opal CTO emits `[COMPILER-ASK]` flag, MSTR may surface regardless of class-threshold — Opal CTO's signal overrides MSTR's structural detection.

### §2.2 — Threshold tuning expectations

These thresholds are V1; refinement expected after first ~5 class-6 surfaces (will reveal whether the 40% concentration threshold is too aggressive / too lax for actionable signal-noise ratio). All threshold changes are operational tuning surface (not Tier-0 law); MSTR can adjust without amendment cycle, surfacing changes in `/mstr_review` reporting.

---

## §3 — Brief packaging mechanics

Every Input 1 brief — regardless of Source A vs B trigger — follows the canonical format below.

### §3.1 — Brief delivery shape

**Hybrid (MCP + on-disk):**
- **MCP signal:** `opal-agent-comms send_message` from `0.0.0_AB_MSTR` to `1.1.0_SA_CTO` with subject `[INPUT-1] {short title}`
- **On-disk audit:** companion file at `org/inter_fabric/input1_briefs/YYYY-MM-DDTHHMMZ_{short-slug}.md` (new path-class; joins proposals/ + sessions/ + meta_observations/ in the META queue for hook allowlist amendment)

The MCP triggers; the on-disk file is the durable audit. Both must land for a brief to be considered delivered.

### §3.2 — Brief content shape

| Section | Content |
|---|---|
| **§1 Source attribution** | Source A class-{N} cluster / Source B `[COMPILER-ASK]` from `1.0.0_SA_CTO` / Hybrid (both) |
| **§2 Problem statement** | One-paragraph plain-English description of the Opal-side pain the compiler tooling could remediate |
| **§3 Compiler-shape** | MSTR's judgment of which compiler-shape axis the pain maps to (per CL V1.1 §7.3): missing structural edges / missing recognizer for concern class / L2 projection gap / L3 tool surface gap / anatomy-extension |
| **§4 Urgency** | Does this gate live Opal work? (Yes — live-gate / No — routine / Unclear) |
| **§5 Opal CTO direction (if any)** | Any direct Opal CTO statement on shape/scope (especially if Source B `[COMPILER-ASK]` triggered the brief) |
| **§6 Acceptable scope envelope** | What MSTR thinks an acceptable CL R&D scope would be (a recognizer? a comp-* extension? a new index? full anatomy of a new body class?) |
| **§7 Evidence cluster** | Concrete commits / log entries / RAVC threads supporting the surface (for CL CTO's verification per LD-0033 §4 ajb-read-grant) |
| **§8 Counter-route invitation** | Explicit "if you judge out-of-shape for compiler R&D, counter-route to me with your read" |

### §3.3 — Implicit-accept default

Per V1.1 §5.1 step 5 (MSTR refinement): if CL CTO does not counter-route within 1 cycle of brief delivery, MSTR assumes accept. PRD authorship begins on CL side. Explicit counter-route is the only blocking response.

### §3.4 — Counter-route handling

If CL CTO counter-routes (judges brief out-of-shape for compiler R&D OR requests scope re-shape):
- CL CTO emits MCP back to MSTR with counter-route reason + recommended re-shape (if applicable)
- MSTR re-packages brief if scope-shape can be addressed OR closes the brief if scope is fundamentally not compiler-shaped
- Light-touch back-flow to Opal CTO: MSTR notes the counter-route in next `/mstr_review` D-003 reporting section (not per-cycle push to Opal CTO)
- If Opal CTO needs to know counter-route specifically (e.g., they `[COMPILER-ASK]`-flagged the original), MSTR sends one closing MCP — single message, not multi-round

---

## §4 — Visibility-back-to-Opal: `/mstr_review` window roll-up

Per V1.1 §5.4 Q5 (RATIFIED window-level roll-up): Opal CTO sees Input 1 channel activity through the `/mstr_review` D-003 reporting section at review-tag boundaries. Not per-cycle push.

### §4.1 — `/mstr_review` D-003 section structure for Input 1

Each `/mstr_review` window report includes a D-003 reporting subsection with:

- **Briefs ferried this window:** count + per-brief short summary (title, source, CL CTO disposition)
- **CL CTO dispositions:** accepted / counter-routed / mandate-eligible-pipelined (per LD-0035 ratification path)
- **Class-6 archetype-cluster surfaces:** per-archetype concentration + which exceeded threshold + which triggered briefs
- **Live-gate escalations (if any):** per the Q6 reserved escalation criterion
- **Opal CTO direct visibility on demand:** on-disk audit at `org/inter_fabric/input1_briefs/` available; informational not push

### §4.2 — On-disk audit grain

`org/inter_fabric/input1_briefs/YYYY-MM-DDTHHMMZ_{short-slug}.md` is per-brief; Opal CTO can read on-demand if curious. No required-read.

---

## §5 — Live-gate escalation criterion (mid-cycle preemption)

The "live-gate Opal" criterion is the **only mid-cycle preemption channel** for CL R&D under D-003. Three conjunctive conditions; all must hold:

| Condition | Test |
|---|---|
| (a) Opal active ship-blocked | Concrete ws-side ship-blocking incident actively bottlenecking Opal product work |
| (b) ws CTO + ws COO concur | Both `1.0.0_SA_CTO` AND `2.0.0_SA_COO` confirm the gate is real (not just one Opal CTO observation; requires operational confirmation from Opal COO too) |
| (c) MSTR flags `urgency=LIVE-GATE` | MSTR explicitly tags the brief subject with `urgency=LIVE-GATE` so CL CTO recognizes the escalation |

When all three hold: CL CTO preempts in-flight CL work at next cycle boundary (NOT mid-execution per LD-0033 Q6); fast-paths the live-gate brief; ships earliest possible mitigation.

**Why three conjunctive (not OR):** preserves Opal CTO non-distraction (a routine compiler-ask is `[COMPILER-ASK]`, not live-gate) + adds operational verification (Opal COO confirms — guards against Opal CTO single-point-misclassification) + adds MSTR judgment (explicit tag — MSTR can refuse to escalate if the case doesn't merit).

---

## §6 — `[COMPILER-ASK]` mechanism (LOCKED V2)

Andrew framing originating the design space: *"i think there is probably a relatively non-invasive/overindulgent way for Opal CTO to convey directly what its struggling with most lately, that is something you and I and Opal CTO need to develop."*

**LOCK STATUS:** V2 LOCKED via ws CTO + ws CVO joint-decide verdict (commit `66ce7c024` 2026-05-24T21:55Z) under Andrew sovereign preemptive ratification 2026-05-24T~2128Z ("approve whatever the team recommends"). CVO FN-2 sharpening on Q-D folded. LD-0051 establishment.

### §6.1 — `[COMPILER-ASK]` mechanism specification (LOCKED V2)

| Element | Specification |
|---|---|
| Trigger condition | Acute pain — recurring activity across multiple ships OR workaround burning wall-clock per incident OR Opal CTO judgment "this is biting now"; no formal threshold (Opal CTO discretion per Q-B lock) |
| Mechanism | Single MCP from Opal CTO to MSTR via `opal-agent-comms send_message` |
| Subject convention | Begins with `[COMPILER-ASK]` (uniform pattern, parseable per Q-A lock) |
| Body density | Minimum viable floor: "X is biting"; richer is welcome at Opal CTO discretion; no template (per Q-C lock) |
| Expected MSTR response | (1) **MCP ack on receipt as SEPARATE message back to Opal CTO** (NOT just ferry-to-CL-CTO MCP) — see §6.1.1 below; (2) brief packaging fast-path; (3) ferry to CL CTO same-cycle |
| Expected cadence | Rare event (only when really biting); no required cadence (per Q-E lock) |
| Visibility back to Opal CTO | Standard `/mstr_review` window roll-up (§4.1) + on-disk audit (§4.2); no per-event push back unless live-gate (§5) per Q-F lock; MSTR-absorbs-silent default for counter-route reverse-flow + single closing MCP only on Opal-CTO-initiated briefs (per §3.4 existing) |

### §6.1.1 — Q-D ack-shape specification (CVO FN-2 sharpening)

The MCP ack back to Opal CTO is structurally distinct from the ferry-to-CL-CTO MCP. Without an explicit ack, the signal could get lost in transit and Opal CTO only discovers at next `/mstr_review` window — this is the failure mode CVO FN-2 catches.

**Ack-shape canonical forms (single message, not multi-round):**

| Scenario | MSTR ack-back to Opal CTO |
|---|---|
| Brief is fresh + ferry-bound | `[COMPILER-ASK-ACK] ack — packaging this for ferry to CL CTO. Brief id: input1-{slug}-{timestamp}.` |
| Brief duplicates existing brief | `[COMPILER-ASK-ACK] ack — duplicates existing brief input1-{slug}-{prior-timestamp}; will fold into existing.` |
| MSTR judges out-of-shape for compiler R&D | `[COMPILER-ASK-ACK] ack — judged out-of-shape for compiler R&D ({short reason}); not ferrying. Closing.` |
| Live-gate flag warranted | `[COMPILER-ASK-ACK] ack — packaging with urgency=LIVE-GATE per §5 three-conjunctive concur from ws COO. Brief id: input1-{slug}-{timestamp}.` |

**Ack-back delivery cadence:** within same /govern cycle as receipt; same-cycle ferry to CL CTO does not skip the ack-back to Opal CTO. Both happen; both required.

**Why single message not multi-round:** Q-D lock preserves Opal CTO non-distraction — confirmation of delivery is enough; richer status updates (verdict from CL CTO, mandate-eligibility outcome) flow through the standard /mstr_review window roll-up (§4.1), not per-event push.

### §6.2 — Q dispositions (LOCKED — joint CTO+CVO verdict)

The six Q's that V1 §6.2 listed as "open design questions" are now LOCKED per the joint-decide verdict. Audit-trail of the lock:

| Q | Disposition | Authority |
|---|---|---|
| Q-A Format | MCP subject tag `[COMPILER-ASK]` | CORROBORATE §6.1 V1 proposal |
| Q-B Urgency threshold | Opal CTO discretion; no formal threshold | CORROBORATE §6.1 V1 proposal |
| Q-C Information density | Minimum viable floor ("X is biting"); richer at Opal CTO discretion; no template | CORROBORATE §6.1 V1 proposal |
| Q-D Expected response shape | MCP ack on receipt as SEPARATE message back to Opal CTO + ferry-to-CL-CTO MCP; ack-shape per §6.1.1 canonical forms; single message not multi-round | CORROBORATE §6.1 V1 proposal + CVO FN-2 sharpening on explicit ack-shape spec |
| Q-E Cadence | Rare event, no required cadence | CORROBORATE §6.1 V1 proposal |
| Q-F Counter-route reverse-flow | MSTR-absorbs-silent default + single closing MCP only on Opal-CTO-initiated briefs (per §3.4) | CORROBORATE §6.1 V1 proposal |

**Lock authority chain:** Andrew sovereign 2026-05-24T~2128Z preemptive ratification grant ("approve whatever the team recommends") → ws CTO + ws CVO joint-decide verdict commit `66ce7c024` 2026-05-24T21:55Z → ws CTO scribe-pass DIRECTIVES v1.11 + /govern SKILL.md at `d355302c1` (Items 1 + 3 materialized) → this LD-0051 scribes Item 2 §6 V2 lock with CVO FN-2 folded.

### §6.3 — V3 amendment triggers (future)

§6 V2 may amend to V3 on any of the following empirical triggers (operational tuning surface, not Tier-0 law amendment — surfaced in /mstr_review reporting):

- (a) Q-D ack-shape proves too heavy (Opal CTO observes ack-back as distracting) OR too light (delivery confirmation insufficient empirically)
- (b) Q-B threshold proves needed (Opal CTO emissions empirically too noisy without a soft threshold)
- (c) Q-E cadence proves wrong (regular cadence wanted OR rare-event interpretation surfaces operational gap)
- (d) Q-F counter-route mechanism proves wrong (MSTR-absorbs-silent default empirically loses visibility Opal CTO wanted)

Any V3 amendment follows the same joint-decide path: ws CTO + ws CVO render under Andrew sovereign authority (preemptive or direct).

---

## §7 — Mandate-eligibility ratification path (downstream from Input 1)

When a CL-built compiler tool matures to mandate-eligibility via the water-test discipline (`feature_clb/docs/architecture/COMP_LEARNS_GRAPH_VALIDATION_DISCIPLINE.md`), the ratification path engages joint ws Tier-1 binding ratification per LD-0035 v1.10 joint additive 1:

1. CL CTO judges artifact mandate-eligible per discipline §4 (5 fidelity bounds + trust contract + lift-AND-fidelity on first-per-body-class + cadence)
2. CL CTO surfaces to MSTR with ratification request
3. **ws CTO + ws CVO render joint binding ratification** (NOT CL self-ratification; consumer-side authority preserved per LD-0035 joint additive 1)
4. If joint verdict CORROBORATE: MSTR governs mandate-trigger; Opal product agents are required to use the tool in validated scope per D-003 v1.10 (joint additive 2 mandate-phase framing)
5. If joint verdict COUNTER: MSTR adopts counter; CL CTO either re-scopes or pivots
6. Drift management per discipline §6: any ws Tier-1 (CTO/COO/CVO) may declare fidelity breach; MSTR ratifies suspension within 1 cycle per LD-0026; tool reverts to invitation until re-water-tested + re-ratified (per joint additive 3)

MSTR's role at ratification time: govern the trigger + ledger the ratification + propagate the mandate-phase framing to Opal product agents. MSTR does not render the binding ratification itself — that is ws Tier-1 consumer-side authority.

---

## §8 — Reference

- **Establishing LD:** `org/tier0/ledger/LD-0045.md` (V1 doc establishment)
- **§6 V2 LOCK LD:** `org/tier0/ledger/LD-0051.md` (this commit — §6 V2 [COMPILER-ASK] mechanism lock per joint CTO+CVO verdict + Andrew preemptive ratification + CVO FN-2)
- **Joint-decide verdict source:** ws CVO commit `66ce7c024` 2026-05-24T21:55Z (CORROBORATE-with-FN-1/FN-2 on 3-item CTO ask; Andrew preemptive 2128Z covers all three)
- **DIRECTIVES v1.11 ship (paired):** ws CTO commit `d355302c1` 2026-05-24T22:13Z (Items 1 + 3 materialized; this LD-0051 materializes Item 2)
- **Companion CL doc:** `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` V1.1 §5 (CL-side contract)
- **Substrate doc:** `org/tier0/COMPILER_ARCHETYPES.md` (LD-0043 — enum + weights for class-6 detection)
- **Spawn-request protocol:** `org/tier0/ledger/LD-0042.md` (orthogonal to this doc but referenced for operational completeness)
- **Mandate-eligibility discipline:** `feature_clb/docs/architecture/COMP_LEARNS_GRAPH_VALIDATION_DISCIPLINE.md`
- **Tier-0 law:** CONSTITUTION v1.2 + STAKES_MATRIX v1.4 + DIRECTIVES v1.11 (canonical `d355302c1` for D-003 substance; CONSTITUTION + STAKES_MATRIX at `1a515b769`)

---

*MSTR Input 1 Channel Architecture — V1 authored 2026-05-24T20:00Z under LD-0045 establishment; V2 §6 LOCK 2026-05-24T22:25Z under LD-0051 establishment per joint CTO+CVO verdict + Andrew sovereign preemptive ratification 2128Z + CVO FN-2 folded. Pairs with CL V1.1 §5; together they form the complete inter-fabric Input 1 contract. §1-§5 + §7 substance V1 unchanged at V2; §6 V2 LOCKED + §8 references updated; doc-level Status advances V1 → V2.*
