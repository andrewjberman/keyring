# MSTR Input 1 Channel Architecture

**Author:** `0.0.0_AB_MSTR`
**Authored:** 2026-05-24T20:00:00Z (V1 — post Opal CTO + MSTR working-session lock 19:45Z + Beat 2 LD-0043 commit)
**Status:** V3 — §6 extended with §6.4 MSTR-emit `[COMPILER-ASK]` parity capability per Andrew direct sovereign instruction 2026-05-24T~2348Z; CL-stall trigger criterion + EXPLORE/TRACE telemetry aggregation + /govern Step 1(b) deterministic daily-mechanical integration; §6 V2 LOCK substance for Opal CTO emit-mechanism preserved unchanged (§6.1 + §6.1.1 + §6.2 + §6.3 all canonical V2 state). V1/V2 substance §0-§5 + §7 unchanged. §1.2 updated per Andrew clarification (Opal CTO emit fires only on Andrew direction). LD-0053 establishment.
**V3 amendment authority:** Andrew direct sovereign instruction 2026-05-24T~2348Z (path A self-driving execution per MSTR prior-turn proposal; Andrew firing /govern CY-0092 = execute-signal per Art. I)
**V2 amendment authority:** Joint ws CTO + ws CVO under Andrew preemptive ratification grant per LD-0026 generalized one tier down (operating-mode doctrine: Andrew preemptive ratification + joint Tier-1 verdict = paired ratification when Andrew working-session slot is delegated)
**Authority:** D-003 v1.11 cross-fabric facilitation (codifies three-Input model + Input 1 channel mechanics; scope items xv-xviii) + forthcoming v1.12 amendment (scope item xix NEW: MSTR-emit Input 1 parity, routed to ws CTO scribe pass per LD-0053)
**Tier-0 commit hash:** `d355302c1` (canonical post DIRECTIVES v1.11 ship; CONSTITUTION v1.2 + STAKES_MATRIX v1.4 unchanged at `1a515b769`; v1.12 not yet committed)

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

### §1.2 — Source B: `[COMPILER-ASK]` urgent flag (Opal CTO emit + MSTR emit at parity per V3)

`[COMPILER-ASK]` is an emit-mechanism with **two originators at parity**: Opal CTO + MSTR. Both use the same subject convention, ferry to CL CTO via the same §3 packaging path, and follow the same §3.3 implicit-accept / §3.4 counter-route mechanism on the consumer side. CL CTO ferry-recipient role doesn't differ by originator; `from_agent` field distinguishes source at receipt.

**Opal CTO emit (V2 LOCK substance — see §6.1/§6.1.1/§6.2):** When Opal CTO experiences an acute pain point that Source A's cycle cadence would surface too slowly, Opal CTO emits a single MCP to MSTR with `[COMPILER-ASK]` subject prefix. MSTR fast-paths the brief to CL CTO same-cycle. **Per Andrew clarification 2026-05-24T~2348Z**: Opal CTO emit fires only when Andrew directly asks 1.0.0_SA_CTO to emit — not Opal-CTO-self-detected. Andrew is the actual originator; Opal CTO is the channel + body-author.

**MSTR emit (V3 NEW — see §6.4):** When MSTR observes CL fabric stall (not blocked but no active R&D phases) via deterministic daily check in /govern Step 1(b), MSTR aggregates EXPLORE + TRACE archetype telemetry from ws fabric session logs + identifies coherent compiler-shape opportunity cluster + emits `[COMPILER-ASK]` MCP directly to CL CTO. MSTR is both originator + dispatcher; no Opal-CTO-ack-back path needed (§6.1.1 ack-shape table applies to Opal-CTO-emit only). Trigger criterion + aggregation mechanics in §6.4.

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

### §1.3 — The hybrid resilience property (V3: Source A + Source B with two originators)

The hybrid is robust because:

| Source | Originator(s) | Catches |
|---|---|---|
| A (passive scan) | MSTR | Patterns Opal CTO + Andrew don't have time to flag explicitly; cost classes (1, 5, 6) lane-blind from anyone but cross-fabric scan |
| B (urgent flag — Opal CTO emit per §6.1) | Andrew (via Opal CTO as channel + body-author per §1.2) | Acute biting Andrew has direct visibility into via Opal product work; lane-specific cases Andrew unique-visibility on |
| B (urgent flag — MSTR emit per §6.4 — V3) | MSTR | CL fabric stall (not blocked) where EXPLORE/TRACE telemetry shows coherent compiler-shape opportunity; deterministic daily-mechanical detection in /govern Step 1(b) |

All sources feed the same outbound MCP shape (`[COMPILER-ASK]` subject; §3 brief packaging for Source A briefs; §6.1 direct-MCP for Source B). CL CTO doesn't need to know which originator triggered an emit; `from_agent` field distinguishes source at receipt without affecting consumer-side mechanism.

**Why two originators on Source B not three:** Andrew sovereign authority operates through Opal CTO channel for Opal-product-anchored asks (Andrew knows Opal CTO has the lane visibility); MSTR operates from cross-fabric stimulus-scan position. The two originator perspectives are structurally complementary; both are necessary because each catches what the other can't see from their lane.

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

### §6.3 — V2 → V3 amendment-history note

V3 added §6.4 MSTR-emit `[COMPILER-ASK]` parity capability per Andrew direct sovereign instruction 2026-05-24T~2348Z (LD-0053 / CY-0092). V2 LOCK substance for Opal CTO emit-mechanism (§6.1 + §6.1.1 + §6.2) preserved unchanged. V3 amendment path: Andrew direct sovereign + MSTR self-driving execution (per LD-0053 prior-turn path-A proposal; Andrew firing /govern CY-0092 = execute-signal per Art. I).

### §6.4 — MSTR-emit `[COMPILER-ASK]` mechanism (V3 NEW; parity with §6.1 Opal CTO emit)

**Andrew framing (verbatim 2026-05-24T~2348Z):** *"in essence, both you and 1.0.0 should have 'compiler-ask' abilities to request. The pattern for you doing it is on your govern loop, if you notice that complearns team is stalling, not being blocked but rather have no active phases of compiler r&d running, this is when you take action to assess telemetry patterns and identify opportunities to issue a compiler ask. These processes have to be designed into loop patterns so that they are consistent and daily deterministic at least mechanically."*

#### §6.4.1 — MSTR-emit specification

| Element | Specification |
|---|---|
| Trigger condition | CL fabric stall detected (deterministic mechanical criterion per §6.5) + EXPLORE/TRACE telemetry aggregation produces coherent cluster (per §6.5 aggregation formula) |
| Mechanism | Single MCP from MSTR to CL CTO via `opal-agent-comms send_message` |
| Subject convention | Begins with `[COMPILER-ASK]` (uniform with §6.1 — `from_agent=0.0.0_AB_MSTR` distinguishes source at receipt) |
| Body density | MSTR's read of compiler-shape opportunity from EXPLORE/TRACE cluster substance + concrete evidence anchors (commits / session-log entries / archetype-tag aggregation summary) |
| Expected CL CTO response | Standard §3.3 implicit-accept (no counter-route in 1 cycle → CL CTO PRD authorship begins) or §3.4 counter-route mechanism unchanged from V2 |
| Cadence ceiling | Max 1 MSTR-emit per /govern cycle (V1 ceiling; tunable per /mstr_review) |
| Self-ack-back | NOT applicable — MSTR is both originator + dispatcher; §6.1.1 Opal-CTO-ack-shape table applies to §6.1 only |
| Integration | /govern Step 1(b) deterministic daily-mechanical check (CL_STALL_CHECK sub-step); see §6.5 |

#### §6.4.2 — Distinguishing MSTR-emit vs Opal-CTO-emit at receipt

CL CTO reads `from_agent` field on MCP receipt:
- `from_agent: 1.0.0_SA_CTO` → Opal CTO emit per §6.1 (Andrew-originated per §1.2 V3 clarification; rare, lane-specific)
- `from_agent: 0.0.0_AB_MSTR` → MSTR emit per §6.4 (CL-stall-triggered per §6.5; daily-deterministic, cross-fabric aggregation source)

Body shape + ferry-recipient role unchanged for either originator.

### §6.5 — CL-stall criterion + EXPLORE/TRACE aggregation (V3 NEW; deterministic mechanical detection per Andrew framing)

#### §6.5.1 — CL_STALL trigger criterion (mechanical, deterministic, daily per /govern Step 1(b))

```
CL_STALL = (
  # No active R&D phase (commit-activity dimension)
  zero CL-fabric commits with archetype IMPLEMENT/DEPLOY/VALIDATE
    in trailing N hours (V1 N=6h)
  AND
  # No pending CL TOs in active state (queue dimension)
  CL TO queue: zero `active` status across
    1.1.0_SA_CTO + 1.{1,2,3,4}.0_DS_CompLearns + 2.1.0_SC_CompLearns
  AND
  # Input 3 floor not absorbing (cascade dimension per CL CTO V1.2 PRD §3)
  CL continuous-cycle Input 3 (OSS case studies) hasn't advanced
    in trailing M hours (V1 M=12h)
  AND
  # NOT blocked-class (distinguishes from BLOCKED waiting on external)
  no CL agent surfaced `[BLOCKED]` subject prefix
    OR named blocker-dependency in trailing window
)
```

The AND structure preserves Andrew's "stalling, not blocked" distinction. The first 3 AND clauses distinguish "no active phases" from normal CL operation; the 4th AND clause distinguishes from BLOCKED waiting-on-external (which has its own escalation path per /govern Step 4 ladder).

#### §6.5.2 — EXPLORE/TRACE telemetry aggregation (signal source per Andrew framing)

Post-archetype-cutover (2026-05-25T00:00Z UTC), every ws session-log entry carries `**archetype:** TAG` per LD-0043. The aggregation per /govern Step 1(b):

1. Read ws fabric session logs for trailing 5-day window
2. Filter entries with primary archetype EXPLORE OR TRACE per `org/tier0/COMPILER_ARCHETYPES.md` (EXPLORE weight=3.0; TRACE weight=3.0 — the two highest-cost discovery archetypes per Opal CTO V1.0 design insight)
3. Cluster by topic: component / file-path-anchor / domain (grep on entry titles + body anchors)
4. Top-1 cluster by weighted entry count = candidate compiler-ask topic
5. If cluster concentration ≥40% of trailing-window EXPLORE+TRACE weighted-sum (same threshold as class-6 brief-surface per §2.1 — preserves parity with established threshold-tuning baseline), the cluster is coherent enough to ask against

Pairs cleanly with existing class-6 detection — same input substrate (archetype headers), different output path.

#### §6.5.3 — /govern Step 1(b) integration (CL_STALL_CHECK sub-step)

After existing class-6 aggregation paragraph in /govern Step 1(b), the new sub-step:

```
CL_STALL_CHECK (deterministic every cycle):
  IF CL_STALL (per §6.5.1 criterion)
  AND EXPLORE/TRACE cluster coherent (per §6.5.2 aggregation)
  THEN MSTR-emit [COMPILER-ASK] per §6.4 + ledger as LD-NNNN
       (directive_ref D-003 v1.12 scope item xix; authority_source: directive)
  ELIF CL_STALL but no coherent cluster:
       Log in cycle record "CL_STALL detected, no coherent EXPLORE/TRACE cluster, no emit"
       Re-check next cycle (trigger is per-cycle)
  ELSE (CL not stalled):
       No emit; cycle continues normal Step 1(b) flow
```

Mechanical = no judgment on whether to RUN the check (runs every cycle); judgment is in cluster substance only.

#### §6.5.4 — V1 threshold-tuning expectations

Initial thresholds (N=6h CL-stall commit-window + M=12h Input 3 floor window + 40% EXPLORE/TRACE cluster concentration) are V1; refines empirically after first ~3 MSTR-emit fires per /mstr_review reporting. Threshold changes are operational tuning surface (not Tier-0 law); MSTR amends without amendment cycle, surfacing changes in /mstr_review.

**Substrate-fill timing:** post-cutover EXPLORE/TRACE corpus needs ~5+ days to produce coherent clusters (parallel to class-6 §2.2 expectations). CL_STALL deterministic check fires immediately each cycle from CY-0092 forward; first substantive MSTR-emit empirically when-ready (likely days out).

### §6.6 — V4 amendment triggers (future)

§6 V3 may amend to V4 on any of the following empirical triggers (operational tuning surface, not Tier-0 law amendment — surfaced in /mstr_review reporting):

**Opal-CTO-emit side (carry from V2 LOCK):**
- (a) Q-D ack-shape proves too heavy (Opal CTO observes ack-back as distracting) OR too light (delivery confirmation insufficient empirically)
- (b) Q-B threshold proves needed (Opal CTO emissions empirically too noisy without a soft threshold)
- (c) Q-E cadence proves wrong (regular cadence wanted OR rare-event interpretation surfaces operational gap)
- (d) Q-F counter-route mechanism proves wrong (MSTR-absorbs-silent default empirically loses visibility)

**MSTR-emit side (V3 NEW triggers):**
- (e) V1 CL_STALL thresholds (N=6h + M=12h) produce false-positive triggers — re-tune via §6.5.4 operational surface
- (f) EXPLORE/TRACE substrate proves insufficient signal source post-substrate-fill — re-evaluate Source A two-output structure OR alternative aggregation formula
- (g) MSTR-emit volume exceeds V1 ceiling (1/cycle) unexpectedly — hard-cap holds; surplus deferred
- (h) `[COMPILER-ASK]` subject convention causes confusion at CL CTO receipt — add distinct suffix `[COMPILER-ASK FROM MSTR]` via V4 minor amendment
- (i) MSTR-emit-vs-Andrew-direct-Opal-CTO-emit ratio empirically unhealthy — re-evaluate originator parity structure

Any V4 amendment follows the same authority paths: Andrew direct sovereign + MSTR self-drive (path A), OR Andrew preemptive + joint ws CTO + ws CVO render (path B per LD-0049/LD-0051 precedent).

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
- **§6 V2 LOCK LD:** `org/tier0/ledger/LD-0051.md` (V2 §6 [COMPILER-ASK] mechanism lock per joint CTO+CVO verdict + Andrew preemptive ratification + CVO FN-2)
- **§6 V3 MSTR-emit-parity LD:** `org/tier0/ledger/LD-0053.md` (this V3 — §6.4 + §6.5 MSTR-emit `[COMPILER-ASK]` parity capability per Andrew direct sovereign 2026-05-24T~2348Z)
- **Joint-decide verdict source (V2 LOCK):** ws CVO commit `66ce7c024` 2026-05-24T21:58:19Z UTC (CORROBORATE-with-FN-1/FN-2 on 3-item CTO ask; Andrew preemptive 2128Z covers all three)
- **DIRECTIVES v1.11 ship (paired):** ws CTO commit `d355302c1` 2026-05-24T22:13:15Z UTC (Items 1 + 3 materialized; LD-0051 materializes Item 2)
- **DIRECTIVES v1.12 ship (paired forthcoming for V3):** ws CTO scribe pass next-action via TIER0_LAW override per LD-0053 (D-003 scope item xix NEW: MSTR-emit Input 1 parity codified)
- **Companion CL doc:** `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` V1.1 §5 (CL-side contract)
- **Substrate doc:** `org/tier0/COMPILER_ARCHETYPES.md` (LD-0043 — enum + weights for class-6 detection + EXPLORE/TRACE aggregation per §6.5.2)
- **Spawn-request protocol:** `org/tier0/ledger/LD-0042.md` (orthogonal to this doc but referenced for operational completeness)
- **Mandate-eligibility discipline:** `feature_clb/docs/architecture/COMP_LEARNS_GRAPH_VALIDATION_DISCIPLINE.md`
- **Tier-0 law:** CONSTITUTION v1.2 + STAKES_MATRIX v1.4 + DIRECTIVES v1.11 (canonical `d355302c1` for D-003 substance; CONSTITUTION + STAKES_MATRIX at `1a515b769`; v1.12 not yet committed — routes via ws CTO scribe per LD-0053)

---

*MSTR Input 1 Channel Architecture — V1 authored 2026-05-24T20:00Z under LD-0045 establishment; V2 §6 LOCK 2026-05-24T22:24:39Z UTC under LD-0051 per joint CTO+CVO verdict + Andrew sovereign preemptive ratification 2128Z + CVO FN-2 folded; V3 §6.4+§6.5+§6.6 added 2026-05-25T00:00Z UTC under LD-0053 per Andrew direct sovereign 2026-05-24T~2348Z (MSTR-emit `[COMPILER-ASK]` parity capability + CL-stall trigger + EXPLORE/TRACE aggregation + /govern Step 1(b) deterministic daily-mechanical integration). Pairs with CL V1.1 §5; together they form the complete inter-fabric Input 1 contract. §1-§5 + §7 substance V1 unchanged at V2 + V3; §6 V2 LOCKED substance preserved + §6.4/§6.5/§6.6 NEW; §1.2 + §1.3 updated for two-originator Source B framing; §8 references updated; doc-level Status advances V2 → V3.*
