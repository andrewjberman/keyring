---
name: exec-sum
description: Executive-summary snapshot of the multi-agent fabric, loop-friendly. Runs the two grounding instruments -- /stimulus-scan (per-agent telemetry + broker + git = who is doing what) and /comp-state (BM25 record-drift linter, self-test-gated) -- then renders a TWO-PART product, CARD FIRST: (1) a NON-TECHNICAL exec card at the very top in plain English -- what the fabric is actually doing right now and WHY it matters, a 10-second read with no serials/commits/jargon, a health line, and the one thing waiting on the human; (2) BELOW it, a house-style /draw two-plane ASCII diagram of agent roles + real activity + how that work feeds back into the card's narrative. Read-FIRST: it reports, it does not drive -- at most it surfaces genuine idle-capacity/blockers to the drive-coordinator (COO), never lane-dispatches. Designed for `/loop [interval] /exec-sum` as a recurring exec dashboard that flags what changed each fire; bare `/exec-sum` is a one-shot. A `--macro <CODE>` mode (also triggered by a bare macro or macro_project code, e.g. `/exec-sum OPAL` or `OPAL_ASSETS`) reskins the same card+draw as a PROGRAM CLOSE-OUT view: what remains to close the INTENT of every open project under a macro, each project's state + owner (and whether staffed right now) + the one gate/decision that closes it, grouped into thematic clusters. Any agent may run it; the whole-fabric vantage (MSTR / COO / CTO) is primary. Sits above /overview (prose status) and /fabric-check (agent-axis) by leading with a business-legible card and grounding it in a diagram.
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
| `/exec-sum --macro <CODE>` | **Macro / macro-project CLOSE-OUT view.** `<CODE>` = a macro (`OPAL`) -> every `OPAL_*` project, or a macro_project (`OPAL_ASSETS`) -> that one. Re-scopes BOTH the card and the draw to *what remains to close the intent* of the macro's open projects: per-project state, owner + whether staffed now, and the one gate/decision that closes each, grouped into thematic clusters. A bare `<MACRO>` / `<MACRO_PROJECT>` code routes here too. Distinct from `--project` (which keeps a whole-fabric card). Full spec: "Macro / macro-project close-out mode" below. |

## Step 0 — Scope + posture

- **Any agent may run it** (read-only status product). The **whole-fabric vantage — MSTR / COO / CTO
  — is primary**; a Tier-2/3 agent gets a self-scoped view.
- **READ-FIRST.** /exec-sum reports; it does not drive. Aggressive dispatch is /stimulus-scan's job.
  The most /exec-sum does to the fabric is **surface** genuine idle-capacity or a blocker **to the
  drive-coordinator (COO)** in one message — never a lane-dispatch (that would violate the
  create -> coordinate -> gate -> verify separation the card itself describes). A scan where every
  agent is ACTIVE or legitimately gated is a clean **zero-surface** run.
- **Two card scopes.** Default (and `--project`) = a **whole-fabric health** card. `--macro <CODE>`,
  or a **bare macro / macro_project code** (`/exec-sum OPAL`, `/exec-sum OPAL_ASSETS`), = a
  **program CLOSE-OUT** card scoped to one macro's intent. When the argument is a macro-shaped code,
  route to the "Macro / macro-project close-out mode" section below (it reuses Steps 1-2 grounding,
  adds Step M1, and renders with the Step M3 variants in place of 3a/3b). Same read-first posture.

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

## Macro / macro-project close-out mode (`--macro <CODE>`)

`/exec-sum --macro OPAL` (or a bare macro / macro_project code, with or without the flag) reskins the
product as a **program close-out view**: not *"what is the whole fabric doing"* but *"what must be
completed to close the INTENT of every open project under this macro — which project is in what
state, who holds it (and is it staffed right now), and what one gate or human decision closes it."*
Same READ-FIRST posture and grounding discipline; the CARD and the DRAW are re-scoped to the macro.
It reuses Step 1 (activity) + Step 1b (comp-state, `--project <MACRO>` scoped) unchanged, adds **Step
M1**, and renders with the **Step M3** variants instead of 3a/3b.

**Scope resolution (mirror /overview's Step-0a classifier):**
- Bare `<MACRO>` (`OPAL`, `NFRA`, `ADVI`) or `--macro <MACRO>` -> enumerate EVERY project yourself:
  `ls org/projects/<MACRO>_*.json`. Miss none — list from the filesystem, never from memory.
- A `<MACRO_PROJECT>` code (`OPAL_ASSETS`) -> that one project's close-out (its phases/TOs are the
  "projects"). A macro with an underscore-suffix family (`OPAL_TAXSMA`, `_PT2`, `_REGISTRY`) — include
  the whole family.
- Distinct from `--project <CODE>`: that scopes the *draw* but keeps a whole-fabric-health card;
  `--macro` makes the *card itself* the macro's close-out narrative.
- Honor any live DO-NOT-DISTURB / sovereign-suspension state on a project — report its state, never
  re-open or re-close it (this is a read lens, cf. Step 0 read-first).

### Step M1 — per-project grounding (in addition to Steps 1a/1b)
Build a grounded per-project table. **Never trust the registry's own say-so for "done"** (Rule 22) —
cross-check status against phase text + commits + open TOs:
```bash
for f in org/projects/<MACRO>_*.json; do
  code=$(basename "$f" .json)
  status=$(python -c "import json,sys;print(json.load(open(sys.argv[1],encoding='utf-8')).get('status','?'))" "$f")
  owner=$(python -c "import json,sys;print(json.load(open(sys.argv[1],encoding='utf-8')).get('owner','?'))" "$f")   # owner-less lean schema is not a defect
  lc=$(git log -1 --format='%cd' --date=short -- "$f")
  echo "$code | $status | owner=$owner | last=$lc"
done
python .tools/to-check.py --all 2>&1 | grep -E "^Project: <MACRO>"    # open-TO count per project
```
For each project derive FOUR fields:
1. **STATE** — active / shipped-with-residual / superseded-into-X / dormant / suspended. Ground on
   status + phase + commits together, not the label alone (a "complete" with a live phase, or an
   "active" with month-stale commits + a done phase, is drift worth naming).
2. **OWNER + staffed-now?** — map the owner serial to the LIVE-agent read from Step 1a:
   `WORKING-NOW` (owner live + recent commits on this thread) / `owner-live-elsewhere` (live but on a
   different thread) / `UNSTAFFED` (no live owner). This is Andrew's "who is working on them."
3. **THE ONE CLOSING GATE** — the single residual that closes the project: a human decision, a
   real-world event (first real use / acceptance sign-off), a dependency (behind another project's
   gate), or a remaining build workstream. If none remains -> it is closeable NOW (say so).
4. **CLUSTER** — group the projects into 3-6 thematic clusters (typical: the live P0 spine ·
   superseded/folded predecessors · shipped-tools tail waiting on a real-world event · active build
   queue · polish/dormant). The clusters ARE the macro's intent decomposed; they become the draw's boxes.

### Step M3 — render (replaces 3a/3b for this mode)

**The CARD** — scoped to the MACRO's intent, still 10-seconds and jargon-free (no serials/hashes):
- 2-4 sentences: **what is this program trying to achieve**, and **what is the one thing the live
  team is actually driving right now** versus what is queued or waiting-on-a-person.
- `HEALTH:` on track / blocked / **concentrated** / mixed + why (e.g. "concentrated — nearly all
  capacity on one thread; the rest gated/queued, not blocked").
- `WAITING ON YOU:` the human decisions that gate close — the co-signs / confirmations only the human
  can give, distilled to the shortlist.

**The DRAW** — the per-project close-out map (still two planes, /draw house style):
1. **Work plane = the clusters.** One labeled box per cluster; inside, one line per project:
   `PROJECT [owner / staffed?] STATE -> the ONE gate`. Draw the **live-spine cluster first** with its
   real critical path as a gate chain (gate 1 -> gate 2 -> the human co-sign), show **superseded
   predecessors folding into** their successor, and mark each shipped-tail box with the single event
   that closes it. Pin real commits/versions where they ground a claim.
2. **Governance plane** = create -> coordinate -> gate -> verify -> **DECIDE(human)**, ending in a
   concrete one-line ANSWER: *the macro's live critical path + "everything else is gated on a human
   event or queued behind it — nothing engineering-blocked"* (or the true state if not).

**Analogy table:** the same create -> coordinate -> gate -> verify roles **plus a DECIDE row for the
human**, each naming what it owns in *this macro's* close-out this window.

**Close with the HOLISTIC CLOSE-OUT STORY:** the ordered moves (1 -> 2 -> 3 ...) that close the whole
macro's intent — the sequence a reader can act on ("finish the streak + co-sign -> the shipped tail
closes on its human events -> the build queue drains"), plus the one-line trust statement
(git+telemetry-grounded, comp-state self-test passed, every card claim traceable to a box above).

**Discipline for this mode:** it is still READ-FIRST — it maps close-out, it does not close anything.
If M1 surfaces a genuinely-closeable project (no gate left) or a real registry drift, that is a
one-line **surface to the coordinator (COO) / owner**, exactly as Step 2 — never an edit from this
skill. A close is the owner's grounded state change, not a status lens's.

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
  exec-sum is the card-first, business-legible one. The `--macro` close-out mode mirrors /overview's
  Step-0a classifier (macro code -> all projects under it) but renders the card+draw close-out
  product instead of prose.
- `/loop` — the recurrence wrapper (`/loop [interval] /exec-sum`).
