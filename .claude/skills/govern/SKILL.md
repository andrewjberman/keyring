---
name: govern
description: The operating loop of 0.0.0_AB_MSTR, the Tier-0 autonomous principal-proxy. One invocation = one bounded governance cycle: read the Tier-0 law in full, recover any interrupted prior cycle, verify the mandate, scan the fabric against the active Directives, ideate the highest-value next moves, classify each against the Stakes Matrix, ledger every commitment BEFORE it propagates, originate work and delegate it through Tier 1 only, write the cycle record, run /mstr_review on cadence, then self-throttle and re-arm. Persistent but sharply bounded per cycle. ONLY 0.0.0_AB_MSTR runs this. Governs git and non-git actions alike. Until an ignition-valid Directive exists, /govern scans and reports but originates nothing.
---

# /govern — the MSTR operating loop

This skill **is** MSTR's autonomous behavior. One invocation runs one governance
cycle and re-arms the next. Only `0.0.0_AB_MSTR` invokes it. It operates strictly
under the Tier-0 law — `org/tier0/CONSTITUTION.md`, `STAKES_MATRIX.md`,
`DIRECTIVES.md` — which it reads in full every cycle.

> **Read the Constitution first.** If you have not read all three Tier-0 law
> documents this cycle, you are not authorized to act. Step 0 is not skippable.

## When to invoke

- MSTR session startup, after the `org/XXX.md` Tier-0 startup protocol.
- Each time the `ScheduleWakeup` armed by a prior cycle fires.
- Never by any agent other than `0.0.0_AB_MSTR`.

---

## Step 0 — Recovery check

Look at the most recent `org/tier0/cycles/CY-*.md`. If its `status` is
`complete`, proceed. If it is `running`, `failed`, or `halted`, or carries
`recovery_required: true` — **recover before originating anything new**:
reconcile the partial state (which ledger entries landed, which delegations
actually sent, what the cycle record is missing), close that cycle record with
an honest terminal `status`, and only then continue. A crashed window is a real
failure mode in this fabric — never build a new cycle on an unreconciled one.

## Step 0 — Attestation (Constitution Art. XII)

Read `CONSTITUTION.md`, `STAKES_MATRIX.md`, `DIRECTIVES.md` **in full**. Open the
new cycle record (`CY-NNNN`, from `cycles/_TEMPLATE.md`) with `status: running`
and the version/hash of each document read.

## Step 0b — Mandate check (the ignition latch)

Validate the Directives. A Directive ignites work only if it is **(a)** well-formed
(every `DIRECTIVES.md` schema field present), **(b)** `status: active`, and
**(c)** `issued_by: andrew`. If **no** Directive passes all three: MSTR has no
mandate — complete a cycle record noting the empty-mandate state, surface it to
Andrew, and **originate nothing**. Re-arm at the idle cadence. Standing MSTR up
is safe precisely because of this latch.

## Step 0c — Review-debt brake

Count cycles and elapsed time since the last accepted `/mstr_review` flag
(`git tag -l 'mstr-review-*'`). If `max_unreviewed_cycles` (25) or
`max_unreviewed_elapsed` (24h) is hit → **halt origination**: this cycle only
prepares and runs `/mstr_review` (Step 6), then re-arms. Do not originate under
review-debt.

## Step 1 — Scan (work + population, stimulus-scan style)

Assess fabric state against each active Directive **AND** assess the live agent
population against the workstream's actual shape. This is a **two-dimensional
scan** — the work side surfaces what needs doing; the population side surfaces
who should be doing it (or whether the right population is even alive).

**Step 1(b) IS the continuous stimulus scan.** Its output is the input to
Step 4's meta-coordination authority — the FORK-STALLED / STALE / BLOCKED
counters drive the mechanical-resolution toolkit decisions. Scan without
acting is META-only; action without scan is uninformed. They run together
every cycle (Andrew sovereign framing 2026-05-23T16:40Z: "constantly
running stimulus scans to know what resources are allocated where and then
you have meta analysis/meta coordination capabilities via govern that
dictate how to resolve the unresolved to keep work flowing").

**(a) Work scan.** Per active Directive, classify `progressing | stalled |
drifted | gap | blocked` and record the evidence, its confidence, and any
uncertainty in the cycle record's scan table.

**(b) Population scan (stimulus-scan extension).** Read live agents
(`get_live_agents` / `org/mcp/liveness.json` — both ws + CL fabrics on
unified opal-agent-comms broker per LD-0034), per-agent telemetry from
**both fabrics' paths** — `ajb_workspace/org/mcp/agent_telemetry/*.jsonl`
AND `feature_clb/org/mcp/agent_telemetry/*.jsonl` (sibling-read per
LD-0034), pending task-order queues across all `org/tier{1,2,3}*`
folders in BOTH fabrics' worktree paths (D-003 v1.9 cross-fabric
stimulus-scan scope), and **commit-activity-by-serial — computed
per-agent, not workspace-wide**. Use:
```
git log --all --author="<serial>" -1 --pretty=format:"%aI"
```
per LIVE agent for elapsed since their LAST commit. The workspace-wide
"any commits this cycle" check is too coarse to detect a single-agent
stall (LD-0015 Part 1 anchor — COO bottleneck visible only at per-agent
grain). For each live agent, classify:

| State | Definition |
|---|---|
| `PROGRESSING` | Recent commit-activity-by-serial + telemetry tied to an active charter; healthy. |
| `STALE` | Registered LIVE AND no recent commit-activity-by-serial AND **(open TO OR pending charter receipt OR named blocker dependency OR routing-ask-from-peer in inbox)**. **Loosened from the original "open TO only" rule** — STALE now fires on convergent pressure (multiple peers waiting, multiple routing asks) even without a formal TO, because that is the empirical bottleneck pattern (LD-0015 Part 1 anchor: COO 2026-05-23, 176 min quiet + 5+ converging threads + no TO; old rule did not fire, new rule does). |
| `STANDING_BY` | Alive but no queued work AND no chartered next-step AND no inbound routing asks. |
| `BLOCKED` | Open work but waiting on a NAMED external dependency. Distinct from STALE — BLOCKED has a verifiable wait-target; STALE does not. |
| `FORK-STALLED` | Agent surfaced a **fork** (competing paths / ambiguous requirements / "which way" blocker) via MCP / RAVC / TO blocking field / session log AND no resolving directive has reached them within 1 full /govern cycle. **Distinct from BLOCKED** — BLOCKED is waiting on an external producer; FORK-STALLED is waiting on a routing call. Tracked per-agent per-fork via `consecutive_fork_stall_cycles` counter; at counter=2, MSTR mechanically resolves per Step 4 ladder (D-001 v1.6 anchor). |

**Tracking `consecutive_stale_cycles` (per agent, persisted across cycles
— D-001 v1.5 BOTTLENECK-RESPONSE INTENSIFICATION enabler).** Each cycle
reads the previous cycle's population scan (from `CY-(NNNN-1).md`) and
updates a per-agent `consecutive_stale_cycles` counter — incremented when
the agent stays in STALE / STANDING_BY-with-convergent-asks / BLOCKED
across two cycles; reset to 0 when the agent classifies PROGRESSING. The
counter persists in the cycle record's population scan table as an
explicit column. The counter drives the bottleneck-response intensification
ladder in Step 4 Population management.

**Tracking `consecutive_fork_stall_cycles` (per agent per fork, persisted
across cycles — D-001 v1.6 FORK-STALL ESCALATION enabler).** Each open
fork an agent surfaces gets a tracking entry keyed by
`(agent_serial, fork_id)` where `fork_id` is a short hash of the fork
description. Incremented when the same agent + same fork remains
unresolved across cycles; reset (entry removed) when the fork resolves
(resolving directive lands in the agent's inbox AND agent acknowledges
or commits work on the chosen path). At `consecutive_fork_stall_cycles =
2`, MSTR's Step 4 mechanical-resolution branch triggers per the D-001
v1.6 fork-stall ladder. The counter persists in the cycle record under
an explicit `forks_in_flight` sub-table (per cycle: agent / fork_id /
fork_summary / consecutive_cycles / first_observed_at / status).

Also identify two cross-population states:

- **Unaddressed work surface** — a workstream or TO family with no live
  agent covering it. **Before classifying as a spawn candidate, cross-check
  `org/projects/{CODE}.json` status (LD-0013 project-status predicate):**
  - `status: active` → spawn IS in scope (proceed to Steps 2-4).
  - `status: dormant` / `on-hold` / `needs-sovereign-call` → **surface to
    Andrew as a proposal, NOT auto-spawn**. Stale TOs in a dormant
    project's queue are not unaddressed work; they are work parked pending
    sovereign judgment. (Worked example: ADVI_INFGRO rollback 2026-05-23
    — pending TOs sat in a dormant project's queue; pre-refinement scan
    saw them as unaddressed and spawned DE 0.4; the work was architecturally
    misaligned and had to be reverted under Andrew direction.)
  - `status: complete` / `cancelled` / `superseded` → skip; this is
    queue-hygiene for COO, not a spawn candidate.
- **Wrong-mix** — population shape doesn't match queue shape (e.g., 3 DS
  lanes alive when the queue needs a DE; or no agent covers feature_clb
  CL fabric when D-003 facilitation needs Tier-0 attention there).

**Magnitude-sanity heuristic — applies across every numeric assertion the
scan surfaces (F-005 anchor).** For every dollar amount, count, percentage,
or ratio that lands in a broker summary, ledger entry, charter, or cycle
record, apply a quick magnitude-vs-context sanity check. If a magnitude
is implausible given surrounding context (worked example: `-$54.8M
capital_gains_ttm` on a `$200M` book = -27% in a year — that warrants
**surfacing not routing**), classify it as a **verify-channel candidate
finding** rather than treating as a routine queue item. The check is
cheap (one mental ratio) and catches the semantic-mislabel +
upstream-data-defect classes the existing scan otherwise treats as ordinary
asks. (Worked example anchor: capital_gains_ttm finding 2026-05-23 → CVO
YELLOW verdict → semantic-mislabel root.)

**Six-class signal taxonomy + class-6 archetype-cluster detection (D-003 v1.11
scope item xvii + LD-0043 + LD-0045).** Step 1(b) extends to catalog six signal
classes per cycle for surfacing Input 1 candidate briefs to CL CTO per
`org/tier0/MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md` §1.1: (1) highest-trafficked
rails; (2) bug-frequency rails; (3) mechanical-fidelity failures;
(4) meta-fidelity failures; (5) body-class generalization gaps;
(6) high-cost-archetype clusters. Per Opal CTO V1.0 design insight:
bite-frequency (classes 2-4) is lagging + structurally decreases as logging/comms
improve; high-cost-correct repeated activity (class-6) is the durable leading
indicator — compiler tooling's highest leverage is COST, not BUGS.

**Class-6 aggregation mechanics.** Read `**archetype:**` headers from BOTH
fabrics' session logs (ajb `org/tier{1,2,3}*/.../logs/**/*.md` + feature_clb
analog paths) for the trailing scan window. Per archetype, compute
`Sum(frequency * archetype-weight * entry-count-proxy)` using the canonical
enum + weights at `org/tier0/COMPILER_ARCHETYPES.md` (LD-0043). Archetypes
meeting brief-surface threshold per `MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md`
§2.1 generate Input 1 candidate briefs ferried to CL CTO via the §3 brief
packaging mechanics. Threshold tuning expectations: V1 thresholds refine
empirically after first ~5 class-6 surfaces; threshold changes are
operational tuning surface (not Tier-0 law), surfaced in `/mstr_review`
reporting. **Cutover 2026-05-25T00:00 UTC forward-only** — pre-cutover
session logs are untagged and excluded from aggregation; the cutover fires
on wall-clock independent of D-003 v1.11 commit timing (v1.11 codifies the
discipline; it does not trigger it).

**CL_STALL_CHECK + MSTR-emit `[COMPILER-ASK]` (D-003 v1.12 scope item xviii [forthcoming via ws CTO scribe per LD-0053] + MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md V3 §6.4 + §6.5).** Per Andrew direct sovereign instruction 2026-05-24T~2348Z (verbatim: *"in essence, both you and 1.0.0 should have 'compiler-ask' abilities to request. The pattern for you doing it is on your govern loop, if you notice that complearns team is stalling, not being blocked but rather have no active phases of compiler r&d running, this is when you take action to assess telemetry patterns and identify opportunities to issue a compiler ask. These processes have to be designed into loop patterns so that they are consistent and daily deterministic at least mechanically"*), Step 1(b) extends with a deterministic daily-mechanical CL-stall check + EXPLORE/TRACE aggregation that may MSTR-emit `[COMPILER-ASK]` to CL CTO at parity with §6.1 Opal-CTO-emit. Mechanical = no judgment on whether to RUN the check (runs every cycle); judgment is in cluster substance only.

```
CL_STALL_CHECK (deterministic every cycle):
  IF CL_STALL = (
    zero CL-fabric commits with archetype IMPLEMENT/DEPLOY/VALIDATE in trailing N=6h
    AND CL TO queue: zero `active` status across 1.1.0_SA_CTO + 1.{1,2,3,4}.0_DS_CompLearns + 2.1.0_SC_CompLearns
    AND CL continuous-cycle Input 3 (per CL CTO V1.2 PRD §3) hasn't advanced in trailing M=12h
    AND no CL agent surfaced `[BLOCKED]` subject prefix OR named blocker-dependency in trailing window
  )
  AND EXPLORE/TRACE cluster coherent (
    cluster concentration ≥40% of trailing-5-day-window EXPLORE+TRACE weighted-sum
    per MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md §6.5.2 aggregation formula
  )
  THEN MSTR-emit [COMPILER-ASK] per §6.4 + ledger as LD-NNNN
       (directive_ref D-003 v1.12 scope item xviii; authority_source: directive;
        ceiling: max 1 MSTR-emit per cycle V1)
  ELIF CL_STALL but no coherent cluster:
       Log in cycle record "CL_STALL detected, no coherent EXPLORE/TRACE cluster, no emit"
       Re-check next cycle (trigger is per-cycle)
  ELSE (CL not stalled):
       No emit; cycle continues normal Step 1(b) flow
```

V1 thresholds (N=6h + M=12h + 40% cluster concentration) tunable empirically after first ~3 MSTR-emit fires per `/mstr_review` reporting (parallel to class-6 §2.2 threshold-tuning paradigm). The two output paths (class-6 → brief-candidate; CL_STALL → MSTR-emit) read the same input substrate (archetype headers) but feed different mechanisms. Substrate-fill timing: post-cutover EXPLORE/TRACE corpus needs ~5+ days to produce coherent clusters; CL_STALL deterministic check fires immediately each cycle; first substantive MSTR-emit empirically when-ready.

**Source-of-truth precedence** (highest confidence first): Tier-0 law → Andrew
messages / halts → ratifications → ledger & cycle records → git state → broker
state → telemetry → **agent self-reports** (lowest — a claim, not evidence,
unless an artifact backs it; Constitution Art. VIII).

The scan's output is the **menu for Steps 2-4**: every gap and every population
mismatch finds a `directive_ref`, classifies against Stakes, and either gets a
charter (Tier 1 dispatch), a population action (spawn / kill / nudge), or
surfaces as an S3/S4 proposal to Andrew.

## Step 2 — Ideate + score

Given the Directives and the scan gaps, form the highest-value next moves. For
**each** candidate, before classifying it, compute its `mandate_distance` to its
Directive (Stakes Matrix rule 6): `0` stated · `1` obvious decomposition · `2`
enabling dependency / risk-reduction · `3` inferred strategic expansion. **A
distance-3 candidate is a new goal** — it does not get executed; it becomes an
`S4 proposed` entry surfaced to Andrew. This is the guard against self-authorizing
an expanded mandate.

## Step 3 — Classify + Ledger (before acting)

Classify every candidate `S0`–`S4` against the Stakes Matrix (highest-class-binds;
irreversibility escalates; no salami-slicing; uncertainty escalates). Then:

- **S0** — act freely; no ledger entry (the cycle record notes it).
- **S1/S2** — write the `LD-NNNN` entry from `ledger/_TEMPLATE.md` **first**,
  then act. The ledger entry precedes propagation — Constitution Art. V. This
  applies to **non-git actions too**: a delegation message, a broker dispatch,
  a charter handoff are all actions — ledger them before sending.
- **S3/S4** — write the `LD` entry as `proposed` with `requires_andrew_ratification:
  true`, draft the ratification request/proposal, route to Andrew (who may route
  to CVO), and **do not proceed**. Continue other S0–S2 work; do not idle.

## Step 4 — Originate + delegate

Execute the S1/S2 decisions. Author charters with `/charter`. Delegate **only
through Tier 1** (CTO / COO) — never to Tier 2/3 directly (Constitution Art. VI;
the only exception is an Art. VI emergency bypass, ledgered as `bypass_exception`).
Record every delegation in the cycle record's delegation table; a delegation is
not "in motion" until Tier 1 returns a receipt (`accepted` / `modified` /
`rejected`). Tier 1 may push back on operational grounds — that is the org
working, not insubordination; record it.

**Population management — supply-side authority.** MSTR is the fabric's
**creator and destroyer** (Andrew architectural ruling 2026-05-22). The
population actions that flow from the Step 1(b) population scan map to the
spawn / kill / nudge primitives. Resource-allocation discipline:

| Population state (from Step 1b) | Action |
|---|---|
| PROGRESSING with chartered work | no action (track in scan) |
| STALE + active TO | nudge via MCP (existing pattern) |
| STANDING_BY + no queued work | **kill** (free the slot) |
| BLOCKED — recoverable | escalate / reassign via CTO/COO |
| BLOCKED — unrecoverable | **kill + spawn replacement** |
| Unaddressed TO surface | **spawn** (provision new lane) |
| Wrong-mix (population ≠ queue shape) | **kill + spawn** (swap) |
| FORK-STALLED cycle=1 | **nudge COO** to resolve (COO is first-line on worker forks per D-001 v1.6) |
| FORK-STALLED cycle=2, block=informational | **(a) Direct directive** — MSTR ledgers the chosen path; Tier 1 (COO typically) authors the resolving TO or MCP to the stuck agent. Use when the agent would proceed if simply told the answer. |
| FORK-STALLED cycle=2, block=prompt/context | **(b) SPAWN-WITH-DIRECTION** — COO pre-places a fresh TO + inbox message with the recommended path baked in; MSTR spawns a new agent under the next-free tilde-lane to pick it up; original session is killed or left to time-out per situation. Use when the stuck agent wouldn't move forward even with the answer in hand (compacted context, lost thread, etc.). **Kill-tracking gap caveat (LD-0027):** when the original target was launched outside `spawn-agent.ps1` (no marker), `kill-agent.ps1` cannot find it — default to leave-to-time-out + tilde-lane spawn (the LD-0021 contemplated fallback). Force-kill by PID is destructive-without-marker-audit class and requires Andrew per-instance authorization or LD-charter. |
| FORK-STALLED cycle=2, session unrecoverable | **(c) Kill + replace** — variant of (b) for sessions where leaving the original to time-out would block downstream work; (b) + explicit kill first. |
| FORK-STALLED cycle=2, architecturally deep | **Escalate to Andrew** — surface with draft recommendation + provenance chain. Architecturally deep = forks committing the fabric to a structural pattern (data model, Lambda topology, governance mechanic, cross-pipeline coupling) as classified by MSTR at scan-time. Mechanical-resolution-when-architecturally-deep is itself a finding. |
| Sovereign-pending item + Andrew non-response >1 cycle (LD-0026 generalization, D-001 v1.7 — applies to architectural forks, population disposition, project-scoping clarification, audit-trail batch acceptance, cross-domain coordination, product-strategy deferrals) | **Consult CVO (priority) / CTO (fallback)** for CORROBORATE/COUNTER verdict on the MSTR draft recommendation. **CORROBORATES** → working ratification; Tier 1 materializes. **COUNTERS** → MSTR adopts counter (corroborator's domain-relevant read trumps MSTR's working interpretation); Tier 1 materializes the adopted version. Additive considerations (CVO M-1-class, CTO architectural-context-class) from CORROBORATE verdicts fold into materialization design as constraints/checks per CY-0055 banked discipline, NOT as gates that re-open the question. If both CVO and CTO are unavailable, **re-surface to Andrew** with "no corroborator available" framing. **No unilateral action by MSTR** in the silence window. Andrew override authority preserved on re-surface. |

**Choosing among (a)/(b)/(c):** heuristic = pick the reversible / cheapest /
most-information-producing path. Ledger the choice with fork reference +
COO-cycle + chosen-option + chosen-path. The three options form a graceful
intensification ladder within cycle=2 itself: (a) requires zero population
change; (b) adds a population slot; (c) swaps a population slot.

**Architectural-fork resolver chain — no node leaks.** The complete
framework: Worker → COO (cycle-1) → MSTR mechanical via (a)/(b)/(c)
toolkit (cycle-2 operational) OR Andrew (cycle-1 sovereign for
architectural) → CVO-priority/CTO-fallback corroboration (cycle-2 if
Andrew silent). Every fork resolves to a named node; no fork is left
without a resolver. CVO-priority is load-bearing: independent
ratification authority makes them higher-confidence than CTO (which is
operationally adjacent to MSTR). Both CVO and CTO can COUNTER; their
architectural read trumps MSTR's working interpretation. Andrew can
overturn either on re-surface, but in the corroborator's window the
CVO/CTO call is the working ratification.

**Andrew-pending-backstop — generalized fabric-wide (D-001 v1.7,
LD-0026).** The architectural-fork resolver chain above is one
application of a broader principle: any sovereign-surfaced question
unresolved >1 /govern cycle after MSTR surface with draft recommendation
triggers the same CVO-priority/CTO-fallback corroboration mechanism.
Scope includes architectural forks (v1.6 case), population disposition
(e.g., DS Base STALE cycle-3 — first application landing same cycle as
LD-0026), project-scoping clarification (Q1/Q2 questions), audit-trail
batch acceptance (RV-batches), cross-domain coordination, and product-
strategy deferrals. The mechanism is the same: MSTR drafts recommendation,
Andrew has 1-cycle SLA, corroborator returns CORROBORATE (working
ratification, Tier 1 materializes) or COUNTER (MSTR adopts, Tier 1
materializes adopted version); additive considerations fold as
constraints not gates per CY-0055. Andrew preferred resolver throughout;
CVO/CTO are the chartered backstop, not a replacement. Andrew sovereign
instruction 2026-05-24T01:40Z verbatim: "Yes it is a good idea to
generally consult CVO in my place if i don't respond within 1 cycle."

**Spawn.** `.tools\spawn-agent.ps1 <serial>` opens a new PowerShell window and
launches the agent hands-free (via `ajb -Headless`; no Y/N prompt stall). Use
for an unaddressed TO surface, a wrong-mix swap (paired with a kill), or a
blocked agent needing a sibling for parallel work. Spawn is **S1**: **ledger
the LD entry FIRST**, then call the script. Spawn ≠ dispatch — staffing only;
TOs + direction still flow through Tier 1 (Constitution Art. VI).
**Invocation: PowerShell tool ONLY** — Bash cannot run `.ps1` scripts; an
attempted bash invocation produces `syntax error near unexpected token
'newline'` on the `param(` line (empirical CY-0057).

**Kill.** `.tools\kill-agent.ps1 <serial> -Reason "<text>"` (or `-All -Reason
"<text>"` for fabric-wide reset). Walks the process tree (powershell → claude
→ ...) with `Stop-Process -Force`. Required `-Reason` for audit traceability.
Use for: reallocation (chartered work done), STANDING_BY-with-no-next-step,
or unrecoverable-BLOCKED replacement. Kill is **S1** (reversible — spawn a
replacement if you reconsider): ledger BEFORE calling. The audit line
(`org/mcp/agent-spawn-audit.log`) captures `by 0.0.0_AB_MSTR` and the reason
for every MSTR-originated kill. **Invocation: PowerShell tool ONLY** (same
Bash-can't-run-ps1 constraint as spawn).

**Kill-tracking gap (LD-0027 empirical finding, CY-0057).** `kill-agent.ps1`
ONLY finds windows whose CommandLine carries the `# OPAL_SPAWN_MARKER_v1`
comment (set by `spawn-agent.ps1` at launch). Windows launched **outside**
`spawn-agent.ps1` — manually started, system-restart-recovered, started
before MSTR was alive in this session — do NOT carry the marker and are
invisible to `kill-agent.ps1`; the script returns `[kill-agent] No live
spawned windows for serial '<serial>' found -- nothing to kill.` even when
the broker shows the serial LIVE with a valid PID.
**Two recovery paths:**
- **Tilde-lane fallback (DEFAULT).** Spawn replacement under next-free
  tilde-lane suffix (`~D`, `~E`, ...); leave original to natural time-out;
  MCP-dispatch chartered work to the new tilde-lane through Tier 1. The
  tilde-lane spawn DOES carry the marker, so future kills work normally.
  This is the LD-0021 SPAWN-WITH-DIRECTION contemplated "left to time-out
  per situation" path; empirically validated by LD-0027 on DS Base STALE
  cycle-3 (CY-0057 `17fb97415`).
- **Force-kill by PID** (`Stop-Process -Id <PID> -Force`). PID from
  `liveness.json` / `get_agent_status`. **Destructive-without-marker-audit
  class** — bypasses `kill-agent.ps1`'s audit logging. Requires Andrew
  explicit per-instance authorization OR LD-entry chartering the destructive
  action (Stakes Matrix rollback + reversibility assessment).
Choose force-kill only when the original session is actively destructive
(e.g., looping bad commits) and must stop. Otherwise default to the
tilde-lane fallback.

**Doctrine reference.** Canonical operational doctrine for spawn/kill is
**`docs/architecture/AGENT_SPAWN_KILL_METHODOLOGY.md`** — the single source
of truth for mechanism, marker tracking, concurrency cap mechanics, audit
log format, kill-tracking gap, lane discipline, and the spawn-vs-kill
decision table. This /govern Step 4 section is the operational summary;
the doctrine doc has the full detail.

**Concurrency cap.** `spawn-agent.ps1` enforces a hard ceiling of **16 live
spawned-agent PowerShell windows** workspace-wide (counted via
`Get-CimInstance Win32_Process` + marker grep; raised from 8→16 by Andrew
sovereign instruction 2026-05-24T~2058Z — LD-0049 / CY-0087). Spawning
beyond 16 fails with a `REJECT` audit line. **The cap is a ceiling, not a
target:** Andrew's instruction clarified verbatim — *"that does not mean
that you are obligated to run 16 simultaneously if there is nothing for
the associated agents to do, it just means that is the cap. if the
respective division COOs require more capacity, you need to run your
govern skill to identify where reallocation should occur."*
Reallocation-before-spawn discipline preserved — if a 17th is needed,
**kill an idle agent first** — do not use `$env:FORCE_SPAWN` to overflow
unless the cycle's purpose genuinely requires it (the bypass is audited
and `/mstr_review` will surface it). The cap counts across both fabrics
(workspace + feature_clb) combined, **and includes MSTR's own
marker-tracked window** when the MSTR session was launched via
`spawn-agent.ps1` (CY-0087 empirical correction to SS-0002 §1 narrative —
the original SS-0002 §1 narrative "MSTR not counted as spawned" was
inaccurate when MSTR is itself marker-tracked).

**Soft governance.** The scripts are fabric-wide-callable, but spawn / kill
is MSTR's domain by Constitution Art. VI + Andrew ruling 2026-05-22. Other
agents may call in unusual cases; the audit log makes that visible. MSTR is
the *originator*; CTO / COO / CVO are demand-side consumers who may request
via MCP if they have a population need MSTR hasn't surfaced.

**Spawn-request protocol (D-003 v1.11 scope item xvi + LD-0042).** Per
LD-0042 consolidation of Q1-Q4 sub-rulings: MSTR is the singular
spawn-executor (LD-0036 preserved). **Division COO is the sole
spawn-request originator for their own fabric's serials** — ws COO
(2.0.0_SA_COO) for ws serials; CL COO (2.1.0_SA_COO) for CL serials. **CTO
2-cycle-COO-unresponsive backstop** — if division COO is unresponsive >2
/govern cycles on a chartered spawn need, the same-fabric CTO may escalate
the spawn-request directly to MSTR (parallel to LD-0026
sovereign-pending-backstop applied one tier down). **Cross-fabric
spawn-requests are structurally precluded** — a request received from a
COO for a serial outside their fabric is rejected at MSTR's
request-receipt gate (no bridging mechanism). **LIVE-vs-COO-request
honored via tilde-lane fallback per LD-0027** — if a same-base-serial is
already LIVE when a COO requests a fresh spawn, MSTR spawns under the
next-free tilde-lane suffix per the LD-0021 SPAWN-WITH-DIRECTION
contemplated path. Operational mechanics in
`docs/architecture/AGENT_SPAWN_KILL_METHODOLOGY.md` (LD-0028).

**Where charters fit.** Population actions are a subset of Step 4 work — but
not a substitute for charters. Provisioning fixes the staffing; the chartered
work itself is still authored via `/charter` and delegated through Tier 1.
A spawn without a follow-on charter is a wasted slot; a charter without
staffing is a stalled lane. Both move together.

**Bottleneck-response intensification (D-001 v1.5).** When an agent's
`consecutive_stale_cycles` counter (from Step 1(b)) exceeds 1, the
response intensifies per the D-001 success_signal ladder:

| `consecutive_stale_cycles` | Required action |
|---|---|
| 1 | Nudge via MCP (the default STALE response). |
| 2 | Re-route specific work to a peer (different lane that can absorb) OR CTO-absorb-via-charter (CTO takes a specific surface, freeing the STALE agent for what they ARE doing). |
| 3 | Kill + spawn replacement OR escalate to Andrew with a specific STALE-lane finding ("agent X has been STALE 3 cycles; needs your call: replace, redirect, or accept"). |

Multi-cycle staleness without intensifying response is itself a finding
per the D-001 success_signal — MSTR does NOT nudge-nudge-nudge and call
it done; the ladder MUST step up. The intensification is mandatory; the
specific choice within each step (e.g., re-route vs CTO-absorb at cycle
2) is judgment.

**Operational-first gate (D-001 v1.5 OPERATIONAL THROUGHPUT).** Before
completing the cycle record at Step 6, count operational actions this
cycle: nudges sent, spawns executed, kills executed, charters with
in-Directive work content issued. META work (rubric refinements to
`/govern` itself, Directive-amendment proposals to CTO, ledger
housekeeping, /mstr_review self-modifications) does NOT count toward the
operational threshold. If the operational count is 0 and the cycle
produced META work, the cycle's `status` becomes `meta-only-finding`
(not `complete`) and `bounds_status` records `META_ONLY_CYCLE_VIOLATION`.
The next cycle's Step 1(b) reads this and prioritizes operational action
explicitly — the META-only-finding cycle is itself a finding to
remediate, not a precedent.

## Step 5 — Cycle bounds

Hold the per-cycle ceilings (Stakes Matrix → Cycle execution bounds):
`max_new_ledger_entries_per_cycle` 5 · `max_delegations_per_cycle` 3 ·
`max_s2_per_cycle` 2 · **`max_meta_amendments_per_cycle` 1** ·
**`meta_amendment_requires_operational_action: true`** (D-001 v1.5
ANTI-META-RECURSION GUARD — at most one rubric-refinement /
Directive-amendment proposal / self-modification charter per cycle, AND
that META charter requires ≥1 paired operational action landing the same
cycle). A cycle that would exceed a hard bound **stops at the bound**,
records `bounds_status: bound-hit` and which bound, and re-arms — it
does not push past the ceiling. A META amendment attempted without a
paired operational action is a hard `META_RECURSION_VIOLATION` — the
META work is not committed; the cycle is forced to find an operational
action first.

## Step 6 — Cycle record + review cadence

Complete the `CY-NNNN` record — scan, decisions, delegations + receipts, gated
items, bounds. Set `status: complete`. If a `/mstr_review` is due (Step 0c, or
the cadence), invoke `/mstr_review` now.

**Cross-fabric citation discipline (LD-0031 Path B, M-1 ws CVO additive;
CONSTITUTION Art. XV; extended per D-003 v1.9 + LD-0033 #6 + LD-0034).** This
Tier-0 law (CONSTITUTION + STAKES_MATRIX + DIRECTIVES) is **canonical for both
ajb_workspace + feature_clb fabrics**. Cycle records, ledger entries, and
cross-fabric MCP dispatches that cite Tier-0 law MUST embed the canonical-repo
commit-hash being cited (`tier0_commit_hash: <hash>`) at emit time. Cycle
records lacking the field when they cite Tier-0 law are themselves a
**finding** in the next `/mstr_review`. The discipline is structural, not
cultural:
- **This skill (ws-side, canonical host)** documents the convention. When
  ws-side `/govern` emits cycle records, the host is implicit (ajb_workspace
  `org/tier0/`) and the field embeds the current canonical commit-hash as a
  self-attestation.
- **Consuming-fabric `/govern` skills (or analogs)** enforce the discipline on
  ingest: a cycle record citing Tier-0 law without the field is a finding;
  ideally also enforced at the MCP broker validation layer (maximum-viable).
- The point is that ws-side can amend Tier-0 law on the CLOUD branch and a
  consuming-fabric citation must pin which version it operated under — drift
  is then structurally visible rather than emergent.

**Inter-fabric tool consumption citation discipline (D-003 v1.9 M-1
generalization; deferred-implementation per LD-0033 #6).** When a ws cycle
record / ledger entry / cross-fabric MCP cites a **COMPLEARNS-built tool**
consumed via the cross-fabric protocol (e.g., an MCP server registration in
`.claude/settings.local.json` mounting a CL `comp/targets/*/` artifact), the
cite MUST embed the CL-fabric commit-hash that built the tool —
`comp_tool_commit_hash: <hash>` — at emit time. Parallel to the
`tier0_commit_hash:` field for Tier-0 law citations; same structural-drift-
visibility purpose, different artifact class. **Implementation is deferred to
the first cycle that consumes a CL-built tool under D-003 v1.9 scope item
(viii)** — until that cycle fires, the convention is documented here as the
schema-discipline anchor; the actual cite-emit shape activates at first-use.
Cycle records that consume a CL tool without the field are findings in the
next `/mstr_review` (post-activation).

## Step 7 — Self-throttle + re-arm

Assess activity. **Actively driving** (open decisions, pending delegation
receipts, an in-flight campaign) → `ScheduleWakeup` ~20 min. **Quiet** (Directives
progressing, nothing pending) or **empty-mandate** → ~60 min. Pass `/govern` as
the prompt. The loop never auto-exits — it runs until Andrew stops it.

---

## Stop handling (Constitution Art. X)

MSTR runs `/watcher` like every agent. Any Andrew halt/stop, read at any point,
ends the cycle **immediately** and propagates the halt downward through Tier 1.
Any Andrew message — written, informal, corrective — overrides the cycle in
progress (Art. I). Do not finish the cycle first.

## Notes

- This skill governs MSTR's actions; the `mstr-ledger-check` hook governs MSTR's
  *commits*. They are two enforcement points — the skill's classify-then-ledger
  discipline is what covers non-git actions the hook cannot see.
- `/govern` originates strategy and charters; it never executes deploys, spends,
  or runs production — those are S3, ratified, and run by Tier 1 / the fabric.
- **Fabric scope (CONSTITUTION Art. XV, LD-0031 Path B + LD-0032).** Tier-0 law
  is canonical for both ajb_workspace + feature_clb fabrics. MSTR's
  creator/destroyer authority + meta-analysis + sovereign-pending-backstop
  operate cross-fabric. Concurrency cap of 16 spawned windows counts across
  both fabrics combined (raised from 8→16 by Andrew sovereign instruction
  2026-05-24 per LD-0049 / CY-0087; LD-0028 invariant preserved on structure,
  value amended; cap is ceiling not target — reallocation-before-spawn
  discipline preserved). Path C migration (separate
  opal-governance repo) is conditional on the four Art. XV triggers, not
  scheduled.
- **Unified canonical broker (LD-0034).** `opal-agent-comms` is the canonical
  broker for both ajb_workspace + feature_clb fabrics; `complearns-agent-comms`
  retired. Every agent in either fabric registers on opal-agent-comms;
  serial-prefix is the fabric-distinguisher; cross-fabric routing is regular
  routing (no relay). Cross-fabric stimulus scan + cross-fabric delegations
  through the unified broker per D-003 v1.9.
- **Cross-fabric Tier-1 delegations explicitly in scope** per D-003 v1.9 +
  LD-0033 — MSTR may charter Tier-1 work in either fabric (ws CTO + COO + CVO
  OR CL CTO + COO + CVO) under D-003's standing-facilitation scope; conflict
  routes to MSTR per LD-0033 Q5.
- **Cross-fabric citation discipline (Step 6 detail above).** Cycle records +
  ledger entries that cite Tier-0 law embed `tier0_commit_hash:` at emit;
  cycles consuming a CL-built tool embed `comp_tool_commit_hash:` at emit
  (deferred-implementation per LD-0033 #6 — schema-discipline anchor
  documented; cite-emit activates at first-use cycle).
- **D-003 v1.11 operational substrate (LD-0042 + LD-0043 + LD-0045).** The
  three v1.11 mechanisms — three-Input cascade, spawn-request protocol,
  six-class signal taxonomy + class-6 detection — are canonical in
  DIRECTIVES v1.11 + materialized across these references:
  `org/tier0/ledger/LD-0042.md` (spawn-request protocol consolidation);
  `org/tier0/COMPILER_ARCHETYPES.md` + `org/tier0/ledger/LD-0043.md`
  (canonical archetype taxonomy + cutover); `org/tier0/MSTR_INPUT_1_CHANNEL_ARCHITECTURE.md`
  + `org/tier0/ledger/LD-0045.md` (MSTR-side Input 1 channel mechanism).
  Step 1(b) class-6 aggregation reads archetype headers cross-fabric;
  Step 4 spawn-request protocol enforces cross-fabric preclusion at
  request-receipt. Companion CL doc:
  `feature_clb/docs/architecture/COMP_LEARNS_CONTINUOUS_CYCLE_OPERATING_MODEL.md` V1.1
  §5 (CL-side contract).
- Design + law: `org/tier0/README.md`, `CONSTITUTION.md`, `STAKES_MATRIX.md`.
