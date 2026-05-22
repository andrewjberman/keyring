---
name: overview
description: Executive, non-technical status of the Opal multi-agent fabric. Read-only, fixed-format, zero dispatches. THREE modes, auto-selected. `/overview` from a Tier-1 agent (CTO/COO/CVO) = whole-fabric briefing: exec-summary intro, per-agent Doing/Why/Next blocks (plain English, no jargon), closing bottom-line. `/overview` from a Tier-2/3 agent (DE/DT/DS/AE/RD) = self-scoped briefing: only that agent's own current work + its direct dependencies. `/overview {topic}` (any tier) = same executive depth scoped to ONE named topic. Built for a human operator who needs "what's going on" without technical context. Invoke on-demand. Adapted for ajb_workspace from corporeal's status skill — confirms who is working from the agent_telemetry stream + the opal-agent-comms broker.
---

# /overview — Executive Status

A **read-only executive briefing** over the Opal multi-agent fabric. This is NOT `/stimulus-scan` (which dispatches work). `/overview` only *reports* — in a fixed format, in plain English, for a non-technical reader who has never seen this codebase.

## When to invoke

- On-demand whenever the operator asks "what's going on" / "is everyone busy" / "status" / "overview".
- Never auto-fired from the loop (it is reporting, not supervision).

## Mode select (Step 0, always first)

`/overview` auto-selects one of three modes from **(a) whether an argument was given** and **(b) the tier of the agent the skill is running inside**.

**Determine your own tier first.** You are an Opal agent — you self-identified at session start. Take your own serial (the one you registered under this session; also in `$OPAL_AGENT_SERIAL`, or `SERIAL=` in `.comp-graph/.agent_context`). Map it to a tier by role code:

| Your role code | Tier | Example serials |
|---|---|---|
| `AB` (Andrew-proxy — the principal-proxy, MSTR) | **Tier 0 (principal)** | `0.0.0_AB_MSTR` |
| `SA` (Systems Architect — CTO / COO / CVO) | **Tier 1 (exec)** | `1.0.0_SA_CTO`, `2.0.0_SA_COO`, `3.0.0_SA_CVO` |
| `DE` / `DT` / `DS` / `AE` | **Tier 2 (senior)** | `0.4.0_DS_ClientPlatform`, `0.7.0_AE_CloudOps` |
| `RD` | **Tier 3 (junior)** | `0.3.2_RD_TradeSubmission` |

Tilde-lane suffixes (`~B`/`~C`/`~D`) do not change the tier — `1.0.0_SA_CTO~B` is still Tier 1.

Then select the mode:

| Invocation | Invoking agent's tier | Mode |
|---|---|---|
| `/overview` (no argument) | **Tier 0 or Tier 1** | **Mode A — whole fabric** |
| `/overview` (no argument) | **Tier 2 or Tier 3** | **Mode C — self-scoped** |
| `/overview {topic}` (argument present) | **any tier** | **Mode B — that one topic** |

Rationale: an exec needs the whole picture; a worker needs *their own* picture. Naming a topic explicitly always wins regardless of who invokes it.

---

# Mode A — `/overview` from a Tier-1 agent (whole fabric)

## Output contract — IDENTICAL every Mode-A invocation, do not deviate

The response is ALWAYS exactly these three parts, in this order, and nothing else:

### Part 1 — Exec summary
2-3 sentences. The single thing the fabric is collectively driving toward right now, plus overall health stated as one of: **on-track** / **waiting-on-X** / **blocked** / **closing-out**. No TO numbers, no project codes, no jargon.

### Part 2 — Per-agent blocks
One block per agent **confirmed live** (Step 1), in a stable order: CTO/COO (exec) first, then Tier-2 agents by serial, then self (the reporting agent) last. Each block is EXACTLY this shape:

> **\<AGENT\>** — \<plain-English role, <=8 words\>
> - **Doing:** \<one plain sentence — the activity in business terms\>
> - **Why:** \<one plain sentence — what it protects or unlocks\>
> - **Next:** \<one plain sentence — the immediate next step, or what completes when this finishes\>

### Part 3 — Bottom line
Exactly one line, this exact shape:
`**Bottom line:** Goal: <X>. Status: <where we are>. Watch: <the next thing that moves it, or the live risk>.`

Nothing before Part 1, nothing after Part 3. No tables, no extra headers, no technical appendix, no per-agent timestamps.

## Procedure (Mode A)

### Step 1 — Who is actually working (confirmed via telemetry + broker)

Two sources, both used:

- **`org/mcp/agent_telemetry/<serial>.jsonl`** — the PostToolUse-hook telemetry stream (`{ts,agent,tool,kind,session_id}`, `kind` work/loop-tagged). This CONFIRMS who is actually working — extract the last `kind:work` ts per agent (`jq -r 'select((.kind//"work")=="work").ts' <f> | tail -1`). An agent whose only recent telemetry is `kind:loop` (watcher self-pings) is NOT actively working — say so honestly.
- **`get_live_agents()`** — every registered agent with its one-line work summary + last-seen. This carries the **what-they're-doing summary** the telemetry stream does not. `get_org_summary()` — active projects + pending TOs.

**Include** an agent if telemetry shows recent `kind:work` OR the broker shows it LIVE with a current summary and it is clearly part of this cycle. **Exclude** any serial not seen this cycle / long-offline — do not list it.

Cross-check before deciding (banked discipline — a heartbeat summary is aspirational, git is ground truth):
- Stale broker summary BUT recent commits (`git log --all --oneline --since="30 minutes ago"`) -> the agent is **working**; include it, describe the commit work.
- Live but heartbeat-quiet on a known long-running or gated task (an SSM chain, a deploy, a cross-agent wait) -> **working/waiting**; include it and say so plainly in "Doing".
- No signal at all and not characterizable -> **omit** it. Never invent activity.

Always include the reporting agent itself (the operator asked what *you* are working on too).

### Step 2 — Doing / Why / Next, translated technical -> executive (mandatory)

For each included agent gather: broker summary, recent commit subjects, last inbox message subject, pending TOs. Then **translate to plain English**:

- NEVER print an internal label without its plain-English meaning. Replace or gloss every: TO ID (`MDPF_ASSETS.024`), project code (`YALP_MDSRC`), macro (`ADVI`), commit hash, Lambda/instance name, S3 key, `~B`/`~C` lane suffix.
- Lead with the business meaning, not the internal name. Good: "Rebuilding the advisor-performance data after a fix, then waiting to independently re-check the numbers." Bad: "running INFINC_REBUILD on INF_C_02 then AC5-verifying."
- **Why** = what it protects or unlocks in business terms (data correctness, unblocking a partner-facing deliverable, preventing a bad PROD deploy, a verification gate).
- **Next** = the concrete next event in plain terms (a chain finishing, an independent check, a hand-off, a go/no-go).
- If an agent is waiting/gated, say so plainly in **Doing** ("Waiting for the data rebuild to finish before it can re-check it"). Waiting IS a status — report it honestly; never dress idle/gated work up as active progress.

### Step 3 — Emit exactly per the output contract

Render Parts 1-3 verbatim per the contract. Concise: exec summary <=3 sentences; each agent block exactly the 3 bullets, one sentence each; bottom line exactly one line. If it does not fit on roughly one screen, it is too long — tighten wording, never add content.

---

# Mode B — `/overview {topic}` (any tier)

Same executive depth and discipline as Mode A, scoped to the ONE topic the operator named. Available to any agent regardless of tier — naming a topic is an explicit override of the tier-based default.

## Output contract — IDENTICAL every Mode-B invocation, do not deviate

ALWAYS exactly these four parts, in this order, and nothing else:

### Part 1 — Topic summary (intro bookend)
1-2 sentences: what this topic IS in plain English (resolved from the operator's word — they will not use project codes) + its current state, one of: **on-track** / **waiting-on-X** / **blocked** / **closing-out** / **not-started** / **done**.

### Part 2 — Who's on it
One block per agent **confirmed live** (Mode-A Step 1 method) **whose current work relates to this topic**, stable order (exec first, then Tier-2 by serial, then self if applicable). Each block is EXACTLY:

> **\<AGENT\>** — \<plain-English role on this topic, <=8 words\>
> - **Doing:** \<one plain sentence — their activity on this topic\>
> - **Why:** \<one plain sentence — why it matters for this topic\>

If NO confirmed-live agent is working the topic, Part 2 is exactly one line: `No agent is actively working on <topic> right now — <plain reason: gated on X / already closed / not yet started>.` Never invent an owner.

### Part 3 — Desired outcome
Exactly one line: `**Desired outcome:** <what "done" looks like for this topic, in business terms>.`

### Part 4 — Next steps (closing bookend)
1-3 short bullets — the concrete upcoming events that move this topic (a chain finishing, an independent check, a hand-off, a go/no-go), plain English. If the topic is blocked, the bullets are what would unblock it and who owns that.

Nothing before Part 1, nothing after Part 4. No tables, no per-agent timestamps, no technical appendix.

## Procedure (Mode B)

1. **Resolve the topic.** Map the operator's plain word to the internal project(s)/macro(s) it names (e.g. "the scanner" -> the Security Scanner project; "the YCharts work" -> YALP_MDSRC; "deploys" -> the in-flight Terraform/PROD-push workstream). Use `org/projects/REGISTRY.md` to resolve. If it maps to nothing recognizable, say so honestly in Part 1 and make Parts 2-4 `n/a — topic not recognized` (optionally: "did you mean <closest 1-2>?"). Never fabricate a topic.
2. **Who's on it.** Run the Mode-A Step-1 broker scan for confirmed-live agents; for each, check broker summary / recent commits / pending TOs against the resolved topic; include only those genuinely on it. An agent *gated/waiting on* the topic counts as on it (say so plainly in Doing); an agent that *finished its part* is not "on it" now (mention in Part 4 as a completed dependency if it matters).
3. **Translate technical -> executive** — identical mandatory rules to Mode-A Step 2.
4. **Emit exactly per the Mode-B output contract.** Concise — one screen max.

---

# Mode C — `/overview` from a Tier-2/3 agent (self-scoped)

When a senior (DE/DT/DS/AE) or junior (RD) agent invokes `/overview` with no argument, the briefing is scoped to **that agent's own current work only** — not the whole fabric. The operator wants "what is *this* agent doing", not an org-wide sweep.

## Output contract — IDENTICAL every Mode-C invocation, do not deviate

ALWAYS exactly these four parts, in this order, and nothing else:

### Part 1 — Focus summary
1-2 sentences in plain English: what this agent (you) is currently working on, plus its state, one of: **on-track** / **waiting-on-X** / **blocked** / **idle** / **closing-out**. No TO numbers, no project codes, no jargon.

### Part 2 — Your work block
Exactly one block — the invoking agent itself — in this shape:

> **\<AGENT\>** — \<plain-English role, <=8 words\>
> - **Doing:** \<one plain sentence — your current activity in business terms\>
> - **Why:** \<one plain sentence — what it protects or unlocks\>
> - **Next:** \<one plain sentence — your immediate next step, or what completes when this finishes\>

If you hold more than one active task, add one extra **Doing/Why/Next** trio per additional task under the same block — but only genuinely active ones (a `pending` TO you are mid-execution on). A `staged` TO is *not* active — mention staged/queued work in Part 4 instead.

### Part 3 — Dependencies
1-2 lines, plain English, covering ONLY direct dependencies of your own work:
- **Waiting on:** the agent(s) you are blocked by or expecting a hand-off / GO / validation from, and what you need from them — or `nothing`.
- **Hands off to:** the agent(s) who pick up when you finish, and what they get — or `nothing`.
If neither applies: exactly one line — `**Dependencies:** None — self-contained.`

### Part 4 — Bottom line
Exactly one line, this exact shape:
`**Bottom line:** Goal: <what your current work delivers>. Status: <where you are>. Watch: <your immediate next event, or the thing blocking you>.`

Nothing before Part 1, nothing after Part 4. No other agents' blocks, no whole-fabric summary, no tables, no timestamps.

## Procedure (Mode C)

1. **Confirm your own current work.** Read your own `task_orders/` directory for `pending` TOs, your most recent session log, your recent commits (`git log --all --oneline --author="<your-serial-prefix>" --since="6 hours ago"`), and your last inbox messages. Ground truth is git + the TO files — a stale heartbeat summary is aspirational; describe what the commits and TO status actually show.
2. **Characterize honestly.** If you are mid-execution on a TO, that is your "Doing". If you are blocked, say `blocked` and name the blocker in Part 3. If you have no active TO and nothing in flight, say `idle` plainly — do not invent activity.
3. **Identify direct dependencies only.** Check your active TO's `<cross_domain_coordination>` block and any RAVC threads: who must deliver before you proceed (Waiting on), and who consumes your output (Hands off to). Do NOT enumerate the wider fabric — only your own edges.
4. **Translate technical -> executive** — identical mandatory rules to Mode-A Step 2. The reader is non-technical: gloss every TO ID, project code, Lambda name, and lane suffix.
5. **Emit exactly per the Mode-C output contract.** Concise — well under one screen.

---

## Constraints (all modes)

- **READ-ONLY.** Zero dispatches, zero messages, zero commits, zero file writes. If action is needed, that is `/stimulus-scan`, not `/overview`.
- **Plain English for a non-technical executive.** A reader who has never seen this codebase must understand every sentence.
- **Fixed format, every time.** Same parts, same labels, same order — scannable at a glance across invocations.
- **Honest.** "Waiting" / "blocked" / "stalled" / "idle" stated plainly; never inflate idle or gated work into apparent progress.
