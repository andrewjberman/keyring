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

**(a) Work scan.** Per active Directive, classify `progressing | stalled |
drifted | gap | blocked` and record the evidence, its confidence, and any
uncertainty in the cycle record's scan table.

**(b) Population scan (stimulus-scan extension).** Read live agents
(`get_live_agents` / `org/mcp/liveness.json`), per-agent telemetry
(`org/mcp/agent_telemetry/*.jsonl`), pending task-order queues across all
`org/tier{1,2,3}*` folders, and **commit-activity-by-serial — computed
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

**Spawn.** `.tools/spawn-agent.ps1 <serial>` opens a new PowerShell window and
launches the agent hands-free (via `ajb -Headless`; no Y/N prompt stall). Use
for an unaddressed TO surface, a wrong-mix swap (paired with a kill), or a
blocked agent needing a sibling for parallel work. Spawn is **S1**: **ledger
the LD entry FIRST**, then call the script. Spawn ≠ dispatch — staffing only;
TOs + direction still flow through Tier 1 (Constitution Art. VI).

**Kill.** `.tools/kill-agent.ps1 <serial> -Reason "<text>"` (or `-All -Reason
"<text>"` for fabric-wide reset). Walks the process tree (powershell → claude
→ ...) with `Stop-Process -Force`. Required `-Reason` for audit traceability.
Use for: reallocation (chartered work done), STANDING_BY-with-no-next-step,
or unrecoverable-BLOCKED replacement. Kill is **S1** (reversible — spawn a
replacement if you reconsider): ledger BEFORE calling. The audit line
(`org/mcp/agent-spawn-audit.log`) captures `by 0.0.0_AB_MSTR` and the reason
for every MSTR-originated kill.

**Concurrency cap.** `spawn-agent.ps1` enforces a hard ceiling of **8 live
spawned-agent PowerShell windows** workspace-wide (counted via
`Get-CimInstance Win32_Process` + marker grep). Spawning beyond 8 fails with
a `REJECT` audit line. If a 9th is needed, **kill an idle agent first** —
do not use `$env:FORCE_SPAWN` to overflow unless the cycle's purpose
genuinely requires it (the bypass is audited and `/mstr_review` will
surface it). The cap counts across both fabrics (workspace + feature_clb)
combined.

**Soft governance.** The scripts are fabric-wide-callable, but spawn / kill
is MSTR's domain by Constitution Art. VI + Andrew ruling 2026-05-22. Other
agents may call in unusual cases; the audit log makes that visible. MSTR is
the *originator*; CTO / COO / CVO are demand-side consumers who may request
via MCP if they have a population need MSTR hasn't surfaced.

**Where charters fit.** Population actions are a subset of Step 4 work — but
not a substitute for charters. Provisioning fixes the staffing; the chartered
work itself is still authored via `/charter` and delegated through Tier 1.
A spawn without a follow-on charter is a wasted slot; a charter without
staffing is a stalled lane. Both move together.

## Step 5 — Cycle bounds

Hold the per-cycle ceilings (Stakes Matrix → Cycle execution bounds):
`max_new_ledger_entries_per_cycle` 5 · `max_delegations_per_cycle` 3 ·
`max_s2_per_cycle` 2. A cycle that would exceed a hard bound **stops at the
bound**, records `bounds_status: bound-hit` and which bound, and re-arms — it
does not push past the ceiling.

## Step 6 — Cycle record + review cadence

Complete the `CY-NNNN` record — scan, decisions, delegations + receipts, gated
items, bounds. Set `status: complete`. If a `/mstr_review` is due (Step 0c, or
the cadence), invoke `/mstr_review` now.

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
- Design + law: `org/tier0/README.md`, `CONSTITUTION.md`, `STAKES_MATRIX.md`.
