---
name: overview
description: Executive, non-technical status of the Opal multi-agent fabric. Read-only, fixed-format, zero dispatches. THREE modes, auto-selected from invoker tier + argument shape. `/overview` (no arg) from a Tier-0/1 agent = whole-fabric briefing (Mode A). `/overview` (no arg) from a Tier-2/3 agent = self-scoped briefing (Mode C-self). With an argument, the Step-0a classifier routes by shape — a **macro code** (e.g., `ADVI`) → all active projects under that macro, combined Mode-B view; a **project code** (e.g., `ADVI_DEMOV1`) → that single project, Mode B; a **bare serial** (e.g., `0.4.0_DS_ClientPlatform`) or a **natural-language agent-status question** (e.g., `what is your current status`, `what is ws COO doing`) → that agent's current work, Mode C-target; any other **free-text topic** → Mode B with REGISTRY narrative resolution. Built for a human operator who needs "what's going on" without technical context. Invoke on-demand. Adapted for ajb_workspace from corporeal's status skill — confirms who is working from the agent_telemetry stream + the opal-agent-comms broker.
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
| `/overview` (no argument) | **Tier 2 or Tier 3** | **Mode C-self — self-scoped** |
| `/overview <argument>` (any shape) | **any tier** | **Step 0a classifier** routes to Mode B or Mode C-target |

Rationale: an exec needs the whole picture; a worker needs *their own* picture. Naming any argument explicitly always wins regardless of who invokes it — the classifier below selects the right mode by argument shape.

## Step 0a — Argument classifier (when an argument is present)

Match the argument against these patterns **in order** — first match wins:

| # | Pattern | Mode | Target |
|---|---|---|---|
| 1 | Bare serial — regex `\d+\.\d+\.\d+_[A-Z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?` (e.g., `0.4.0_DS_ClientPlatform`, `1.0.0_SA_CTO~B`) | **Mode C-target** | that serial verbatim |
| 2 | Bare macro code — exactly 4 uppercase letters matching a known macro in `org/projects/REGISTRY.md` (e.g., `ADVI`, `ADHC`, `MDPF`, `SXIN`, `SXPL`, `TRSB`, `YALP`, `FIND`) | **Mode B (macro)** | aggregate all active projects under that macro |
| 3 | Bare project code — `MACRO_SUFFIX` shape (4 uppercase + underscore + 6 uppercase, in REGISTRY active projects, e.g., `ADVI_DEMOV1`, `FIND_INSURE`, `YALP_MACROS`) | **Mode B (project)** | that single project |
| 4 | Natural-language agent-status question containing `your` / `you` / `my` (e.g., `what is your current status`, `your work`, `my next step`) | **Mode C-target** | self (the invoking agent) |
| 5 | Natural-language agent-status question containing a role-name token — `CTO` / `COO` / `CVO` (with optional fabric prefix `ws` / `CL`) or `MSTR` (e.g., `what is ws COO doing`, `CTO status`, `MSTR posture`) | **Mode C-target** | canonical serial in the active fabric (e.g., `ws COO` → `2.0.0_SA_COO`; `CL CTO` → `1.1.0_SA_CTO`; bare `CTO` from a ws-side invoker → `1.0.0_SA_CTO`). If both fabrics ambiguous and no prefix, ask once before proceeding. |
| 6 | Anything else — free-text topic phrase (e.g., `the scanner`, `deploys`, `Schwab ingest`) | **Mode B (topic)** | REGISTRY narrative resolve |

If the argument matches none of the above and REGISTRY resolves nothing recognizable, fall through to Mode B and emit `topic not recognized` per the existing Mode-B Step-1 honest-fallback (never fabricate).

**Tilde-lane suffix on a serial argument** (e.g., `0.4.0_DS_ClientPlatform~D`) targets that exact lane, not the base.

**Cross-fabric note for row #5:** the active fabric is the one the invoking agent belongs to (ws or CL). If the invoker is Tier-0 MSTR (cross-fabric), default to ws unless prefix specifies CL. `MSTR` is unambiguous — always `0.0.0_AB_MSTR`.

**Ambiguous classification:** if an argument could match #2 (4-letter macro) AND #5 (role-name token) — unlikely, but e.g., a future macro literally named `CTOX` — prefer the explicit role mapping in #5. The classifier is order-sensitive precisely to make these calls deterministic.

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

1. **Resolve the topic by sub-case** (Step 0a has already selected the B sub-shape):
   - **Macro sub-case** (Step 0a row 2 — bare 4-letter macro code): enumerate **all active projects** under that macro from `org/projects/REGISTRY.md`. The topic IS the macro's collective work. Part 1 names the macro in plain English (what surface area it owns) + lists the active projects (plain-English names, not codes). Part 2 aggregates "Who's on it" across all active projects under the macro — one block per confirmed-live agent, even if they work on different sub-projects; their Doing line names which sub-project they hold in plain English. Part 3 Desired-outcome is the macro-level goal. Part 4 Next-steps name the next macro-level milestones (not per-project).
   - **Project sub-case** (Step 0a row 3 — bare `MACRO_SUFFIX` code): the project code resolves directly to its `org/projects/{CODE}.json` + REGISTRY row. Part 1 names the project in plain English from JSON `phase` / `blocking`; standard Mode-B shape from there.
   - **Free-text sub-case** (Step 0a row 6 — any other phrase): map the operator's plain word to the internal project(s) / macro(s) it names (e.g., "the scanner" → Security Scanner project; "the YCharts work" → YALP_MDSRC; "deploys" → in-flight Terraform/PROD-push workstream). Use REGISTRY to resolve. If it maps to nothing recognizable, say so honestly in Part 1 and make Parts 2-4 `n/a — topic not recognized` (optionally: "did you mean <closest 1-2>?"). Never fabricate a topic.
2. **Who's on it.** Run the Mode-A Step-1 broker + telemetry scan for confirmed-live agents; for each, check broker summary / recent commits / pending TOs against the resolved topic; include only those genuinely on it. An agent *gated/waiting on* the topic counts as on it (say so plainly in Doing); an agent that *finished its part* is not "on it" now (mention in Part 4 as a completed dependency if it matters). For the macro sub-case, each agent's project-affiliation appears in their Doing line ("Driving the dashboard validation work on \<sub-project plain name\>") — but kept in plain English, not as a bare code.
3. **Translate technical → executive** — identical mandatory rules to Mode-A Step 2.
4. **Emit exactly per the Mode-B output contract.** Concise — one screen max. For the macro sub-case, if more than ~5 active sub-projects produce >7 confirmed-live agents on Part 2, prefer grouping by Tier-1 lead + the largest sub-project blocks rather than listing every agent (honest aggregation, not omission — name how many agents are not individually shown and why).

---

# Mode C — single-agent-scoped (self OR named target)

Mode C is the **single-agent focus** mode. Two entry points:

- **Mode C-self** — invoked by a Tier-2/3 agent with no argument; target = the invoking agent itself. The operator wants "what is *this* agent doing."
- **Mode C-target** — invoked from any tier with an argument matching Step 0a row 1 (bare serial), row 4 (NL "your"/"you"/"my"), or row 5 (NL role-name token); target = the resolved agent (which may be the invoker, in the "your" case, or a peer).

The output contract is the same shape regardless of entry point — only the agent being described changes. The narrating voice shifts: Mode C-self uses second-person ("you are…"), Mode C-target uses third-person ("ws COO is…").

## Output contract — IDENTICAL every Mode-C invocation, do not deviate

ALWAYS exactly these four parts, in this order, and nothing else:

### Part 1 — Focus summary
1-2 sentences in plain English: what the **target agent** is currently working on, plus its state, one of: **on-track** / **waiting-on-X** / **blocked** / **idle** / **closing-out** / **offline**. No TO numbers, no project codes, no jargon. (Mode C-self: "you are…"; Mode C-target: "\<role/serial\> is…")

### Part 2 — Target work block
Exactly one block — the **target agent** — in this shape:

> **\<TARGET AGENT\>** — \<plain-English role, <=8 words\>
> - **Doing:** \<one plain sentence — current activity in business terms\>
> - **Why:** \<one plain sentence — what it protects or unlocks\>
> - **Next:** \<one plain sentence — immediate next step, or what completes when this finishes\>

If the target holds more than one active task, add one extra **Doing/Why/Next** trio per additional task under the same block — but only genuinely active ones (a `pending` TO mid-execution). A `staged` TO is *not* active — mention staged/queued work in Part 4 instead.

### Part 3 — Dependencies
1-2 lines, plain English, covering ONLY direct dependencies of the **target agent's** work:
- **Waiting on:** the agent(s) the target is blocked by or expecting a hand-off / GO / validation from, and what they need — or `nothing`.
- **Hands off to:** the agent(s) who pick up when the target finishes, and what they get — or `nothing`.
If neither applies: exactly one line — `**Dependencies:** None — self-contained.`

### Part 4 — Bottom line
Exactly one line, this exact shape:
`**Bottom line:** Goal: <what the target's current work delivers>. Status: <where they are>. Watch: <their immediate next event, or the thing blocking them>.`

Nothing before Part 1, nothing after Part 4. No other agents' blocks, no whole-fabric summary, no tables, no timestamps.

## Procedure (Mode C)

1. **Resolve the target** (Step 0a already did this — confirm here):
   - **Mode C-self:** target = the invoking agent (your own serial).
   - **Mode C-target row 1** (bare serial): target = that serial verbatim, including any tilde-lane suffix.
   - **Mode C-target row 4** (NL `your` / `you` / `my`): target = the invoking agent.
   - **Mode C-target row 5** (NL role-name): target = the canonical serial in the active fabric (e.g., `ws COO` → `2.0.0_SA_COO`; `CL CTO` → `1.1.0_SA_CTO`; bare `CTO` from a ws-side invoker → `1.0.0_SA_CTO`; `MSTR` → `0.0.0_AB_MSTR`).
2. **Confirm the target's current work.** Read the target's `task_orders/` directory for `pending` TOs (path: `org/tier{N}_{role-folder}/{target-serial}/task_orders/`), their most recent session log under their `logs/<date>/`, their recent commits (`git log --all --oneline --author="<target-serial-prefix>" --since="6 hours ago"`), their broker summary via `get_agent_status("<target-serial>")`, and their last inbox messages if accessible (filesystem: `org/mcp/inbox/<target-serial>/`). Ground truth is git + TO files — a stale heartbeat summary is aspirational; describe what the commits and TO status actually show. For Mode C-self, "the target" is yourself — use the same sources against your own serial.
3. **Characterize honestly.** If the target is mid-execution on a TO, that is the "Doing". If they are blocked, say `blocked` and name the blocker in Part 3. If they have no active TO and nothing in flight, say `idle` plainly — do not invent activity. If the target is **offline** (no broker entry AND no recent telemetry AND no recent commits), say so in Part 1 (`<target> is currently offline — last observed at <human-readable time>`) and make Parts 2-4 reflect last-known state with the offline caveat. Never fabricate activity for an offline agent.
4. **Identify direct dependencies only.** Check the target's active TO's `<cross_domain_coordination>` block and any RAVC threads in their recent inbox / outbox: who must deliver before they proceed (Waiting on), and who consumes their output (Hands off to). Do NOT enumerate the wider fabric — only the target's edges.
5. **Translate technical → executive** — identical mandatory rules to Mode-A Step 2. The reader is non-technical: gloss every TO ID, project code, Lambda name, and lane suffix.
6. **Emit exactly per the Mode-C output contract.** Concise — well under one screen. (Mode C-self uses "you/your"; Mode C-target uses "\<role/serial\>" + "they/their".)

---

## Constraints (all modes)

- **READ-ONLY.** Zero dispatches, zero messages, zero commits, zero file writes. If action is needed, that is `/stimulus-scan`, not `/overview`.
- **Plain English for a non-technical executive.** A reader who has never seen this codebase must understand every sentence.
- **Fixed format, every time.** Same parts, same labels, same order — scannable at a glance across invocations.
- **Honest.** "Waiting" / "blocked" / "stalled" / "idle" stated plainly; never inflate idle or gated work into apparent progress.
