---
name: exec-sum
description: Executive-summary snapshot of the multi-agent fabric, loop-friendly. Runs the two grounding instruments -- /stimulus-scan (per-agent telemetry + broker + git = who is doing what) and /comp-state (BM25 record-drift linter, self-test-gated) -- then renders a TWO-PART product, CARD FIRST: (1) a NON-TECHNICAL exec card at the very top in plain English -- what the fabric is actually doing right now and WHY it matters, a 10-second read with no serials/commits/jargon, a health line, and the one thing waiting on the human; (2) BELOW it, a house-style /draw two-plane ASCII diagram of agent roles + real activity + how that work feeds back into the card's narrative. Read-FIRST: it reports, it does not drive -- at most it surfaces genuine idle-capacity/blockers to the drive-coordinator (COO), never lane-dispatches. Designed for `/loop [interval] /exec-sum` as a recurring exec dashboard that flags what changed each fire; bare `/exec-sum` is a one-shot. Any agent may run it; the whole-fabric vantage (MSTR / COO / CTO) is primary. Sits above /overview (prose status) and /fabric-check (agent-axis) by leading with a business-legible card and grounding it in a diagram.
---

# /exec-sum — executive-summary fabric snapshot (card-first, loopable)

The one-call answer to *"in plain English, what is the whole team of agents actually doing right
now, why does it matter, and is anything waiting on me?"* -- grounded in real telemetry + git, not a
prose recollection. It runs the two grounding instruments, then renders a two-part product whose
**top is a non-technical card a busy human reads in ten seconds**, and whose **body is the /draw**
that backs the card with real names, roles, and activity.

> **What makes this different from /overview and /fabric-check:** /overview is prose status;
> /fabric-check is the agent-axis + project-axis lens. **/exec-sum leads with a business-legible
> CARD** (what + why, no jargon) and then *earns* that card with a grounded diagram. The card is the
> deliverable; the instruments and the draw are how it's made honest.

## Invocation forms

| Form | Behavior |
|---|---|
| `/exec-sum` | One-shot. Run the sweep now, render card + draw. |
| `/loop [interval] /exec-sum` | Recurring exec dashboard. Each fire re-runs the sweep and **leads with a WHAT-CHANGED delta** before the current-state card. (`/loop [30m] /exec-sum` is the typical cadence.) |
| `/exec-sum --project <CODE>` | Scope the comp-state + draw to one project/macro (e.g. `NFRA`, `OPAL_ASSETS`). The card still reads whole-fabric health. |

## Step 0 — Scope + posture

- **Any agent may run it** (read-only status product). The **whole-fabric vantage — MSTR / COO / CTO
  — is primary**; a Tier-2/3 agent gets a self-scoped view.
- **READ-FIRST.** /exec-sum reports; it does not drive. Aggressive dispatch is /stimulus-scan's job.
  The most /exec-sum does to the fabric is **surface** genuine idle-capacity or a blocker **to the
  drive-coordinator (COO)** in one message — never a lane-dispatch (that would violate the
  create -> coordinate -> gate -> verify separation the card itself describes). A scan where every
  agent is ACTIVE or legitimately gated is a clean **zero-surface** run.

## Step 1 — Gather the two instruments (ground the card, never recollect it)

### 1a. Activity (the /stimulus-scan data half)

Per-agent telemetry is the finest signal; broker + git are the cross-checks.

```bash
NOW=$(date -u +%s)
# last kind:work ts per agent (staleness) + last-any (alive-but-loop-only)
for f in org/mcp/agent_telemetry/*.jsonl; do
  a=$(basename "$f" .jsonl)
  w=$(jq -r 'select((.kind//"work")=="work").ts' "$f" 2>/dev/null | tail -1)
  y=$(grep -oE '"ts":"[^"]+"' "$f" 2>/dev/null | tail -1 | sed 's/.*:"//;s/"//')
  echo "$a work=$w any=$y"
done
# git = GROUND TRUTH for "is this agent actually working" (heartbeat summaries are aspirational)
git log --all --oneline --since="30 minutes ago" --pretty=format:"%aI %an %h %s"
```
Then `get_live_agents()` for registration + one-line summaries. Classify each LIVE agent
**ACTIVE / IDLE / STALE / gated** per /stimulus-scan's taxonomy. **A stale broker summary + a recent
commit = WORKING** (git wins). Only the LIVE agents matter for the card; the telemetry file also
lists dozens of dead historical serials — ignore them.

### 1b. Record-drift (the /comp-state half)

```bash
comp-state --self-test        # MUST print PASS 3/3 -- if not, say so and DO NOT trust the report
comp-state                    # drift-only (BEHIND / POST-CLOSE); add --project <CODE> when scoped
```
**Triage, do not auto-edit.** BM25 is a recall layer: most BEHIND rows are lexical false-positives
(the evidence commits are about a *different* project). Keep only the drift whose evidence commits
are genuinely *about that record*, and note whether it is **actively being reconciled** (an owner is
touching it now = transient fast-landing lag, not a stall) vs **QUIET+pending+old** (a real stall
smell). The card cares about stalls; it does not care about noise.

## Step 2 — Surface (light, coordinator-routed; optional)

If 1a/1b found **genuine** idle capacity or a blocker, send **one** message to the drive-coordinator
(COO) — capacity picture + the forward decision — and `date -u +%s > org/mcp/.last-stimulus-scan`.
**Do not lane-dispatch, do not manufacture work.** If everything is ACTIVE or legitimately gated,
skip this step and say so in the card's health line. (This mirrors what a real /exec-sum run does:
the value is the surface to the person who drives, not a flurry of TOs.)

## Step 3 — Render the product (TWO parts, in THIS order)

### 3a. THE EXEC CARD (top, MANDATORY, non-technical) — the whole point

A boxed card in **plain English for a human who does not know the serials**. Hard rules:

- **No serials, no commit hashes, no tool names, no TO/LD/RV ids, no acronyms** the reader would have
  to look up. If a term needs the fabric's vocabulary to parse, it does not belong in the card — it
  belongs in the draw below.
- Answer, in 2-4 sentences: **WHAT is the team of agents collectively working toward right now, and
  WHY does it matter** (to the product, the data, the business). Name the *purpose*, not the mechanism.
- One **HEALTH** line: `on track` / `blocked` / `winding down` / `mixed` + a half-sentence why.
- One **WAITING ON YOU** line: the single most important open decision for the human, or
  `nothing — running clean`.
- A 10-second read. If it takes longer, it is too technical — cut it.

```
╔═══════════════════════════════════════════════════════════════════════╗
║  WHAT THE FABRIC IS DOING RIGHT NOW                       <UTC time>   ║
╟───────────────────────────────────────────────────────────────────────╢
║  <2-4 plain-English sentences: the one thing the team is collectively  ║
║   driving toward, and why it matters. Purpose, not mechanism.>         ║
║                                                                       ║
║  HEALTH:        <on track | blocked | winding down | mixed> — <why>    ║
║  WAITING ON YOU: <the one decision, or "nothing — running clean">     ║
╚═══════════════════════════════════════════════════════════════════════╝
```

### 3b. THE /draw (below the card) — the grounding

Invoke the **/draw** house style (two numbered planes, labeled edges, real names/pins, one analogy
table, concrete answer, closing "story" sentences). For a fabric exec-sum the two planes are:

1. **The work plane** — the roles producing the work: how a directive/goal becomes landed threads.
   Show the live lanes/agents, what each is actually shipping (real project names + commit pins from
   Step 1a's git), and the controls it passes through (who gates, who verifies).
2. **The coordination/governance plane** — how the human reaches the state: the driving/gating/
   verifying spine, ending in a concrete "ANSWER back in your terminal" that **restates the card's
   claim in the fabric's own vocabulary** (this is the feedback loop Andrew asked for — the draw must
   visibly *back* the card).

Mandatory analogy table: the **create -> coordinate -> gate -> verify** role separation (or whatever
the session's real control structure is), one row per role naming what it owns *this* window.
Close with 1-3 "story" sentences (the freshness story / the control story) naming what the reader can
now trust.

**The draw exists to make the card honest** — every plain-English claim in 3a must be traceable to a
real box/edge/pin in 3b. If a card claim has no grounding in the draw, one of them is wrong.

## Step 4 — Loop delta (only when looped)

On a looped re-fire, **lead with what changed** before the current-state card:

```bash
# what landed since the last exec-sum
LAST=$(cat org/mcp/.exec-sum-state 2>/dev/null | head -1)   # last recorded HEAD
git log --all --oneline ${LAST:+$LAST..}HEAD --since="45 minutes ago" --pretty=format:"%an %s"
git rev-parse HEAD > org/mcp/.exec-sum-state                # record for next fire
```
Render a 1-3 line **CHANGED SINCE LAST** block (threads closed, new lands, new blockers, health
flips) directly above the card. A quiet interval with no material change is a healthy one — say
"no material change since <time>" in one line and still print the current card (the human may be
reading this fire cold).

Fixed-interval `/loop` handles the recurrence (the cron re-fires the prompt); /exec-sum itself arms
nothing. In dynamic `/loop` mode, pick a fallback heartbeat of 1200-1800s.

## Discipline / risk notes

- **The card is non-technical or it is broken.** The #1 failure mode is a "summary" that is just the
  draw's jargon in prose. If the reader needs to know what `~C` or `LD-0314` is to parse the card,
  rewrite it. The serials live in the draw.
- **Ground it, never recollect it.** The card's claims come from Step 1's telemetry + git + comp-state,
  not from what you remember happening this session. A fabric snapshot asserted from memory is the
  stale-record failure this skill exists to avoid.
- **comp-state self-test is a gate.** No PASS 3/3 -> the drift half is untrusted; say so, lean on the
  activity half.
- **Read-first; the coordinator drives.** At most one capacity-surface to COO. Never lane-dispatch,
  never manufacture backlog work to make an idle agent look busy — an honest "winding down, freed
  capacity, your scope call" is a better card than a fake-busy one.
- **git wins over the broker summary.** An agent heads-down in a long build looks stale on the broker
  and is ACTIVE in git. Classify on git + telemetry, not the aspirational "Working on" line.
- **Loop-friendly, idempotent.** Every fire re-derives from live state; nothing it writes
  (`.last-stimulus-scan`, `.exec-sum-state`) is load-bearing beyond delta-display.

## Cross-references

- `/stimulus-scan` — the activity-classification + dispatch instrument (Step 1a data half; exec-sum
  uses its read, not its dispatch mandate).
- `/comp-state` — the BM25 registry/TO/PRD drift linter (Step 1b; self-test-gated).
- `/draw` — the house-style two-plane ASCII diagram (Step 3b).
- `/overview` (prose status) and `/fabric-check` (agent + project axis) — sibling status lenses;
  exec-sum is the card-first, business-legible one.
- `/loop` — the recurrence wrapper (`/loop [interval] /exec-sum`).
