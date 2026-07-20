# AGENT START HERE — Opal Capital

> **BEFORE YOU ADD ANYTHING TO THIS FILE, APPLY THE TEST:**
> ### **Is this directly and explicitly OPERATIONAL for the fabric as it is RIGHT NOW, for EVERY agent, EVERY session?**
>
> **If yes — keep it, however long it needs to be.** A rule is unobeyable without its **mechanism** (an
> orphan watcher *manufactures* a REACHABLE verdict; `.agent_context` is last-writer-wins across all
> agents), and **a bare prohibition loses to an agent's own instruments.** Never cut a mechanism to save space.
>
> **If no — it does not belong here.** Anecdotes, incident histories, dated corrections, empirical anchors,
> retired mechanisms, and anything scoped to one project or one moment go to `org/tier0/ledger/` and the
> linked docs. **The scar is not the rule.** *This doc is read by someone who has done nothing yet: it must
> tell them what to DO.*
>
> **A time-bounded hold does not belong in the doc every agent reads at startup.** If something must reach
> every agent, that is a signal it needs a **GATE**, not a paragraph here.

---

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.

---

## Andrew-direct instructions — RECORD + BROADCAST, same turn

**Andrew writes directly to worker agents, not only to Tier 1.** So a lane can be carrying a sovereign
instruction that COO, CTO and MSTR never learn exists — and **`latest + most-restrictive binds`, our
governing conflict rule, cannot bind on an instruction nobody surfaced.**

```
ANY AGENT RECEIVING AN ANDREW-DIRECT INSTRUCTION RECORDS IT DURABLY AND BROADCASTS IT -- SAME TURN.

  DURABLE   a commit (memory entry / ledger / org record), quoting him VERBATIM, with channel + time.
            NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.
  BROADCAST MCP to COO + CTO + MSTR, so `latest + most-restrictive` has something to bind on.
  SCOPE     The receiving agent does NOT adjudicate scope. SURFACE, DO NOT ADJUDICATE.
```

**An agent relaying "Andrew ruled" is not suspect merely because you did not see it — that is the normal
case.** Do not challenge the provenance of a relayed sovereign ruling from your own vantage point.

---

## RAVC Protocol (Non-Negotiable)

Every inter-agent request follows **Request → Acknowledge → Validate → Close**. Full spec:
`org/ref/RAVC_PROTOCOL.md`.

- Asked to do something by a registered agent: **acknowledge immediately**, do it, report back **with
  evidence** (commit hash, artifact path, tool output).
- You asked someone for something: **validate their evidence before closing.** REWORK requests must tie
  the gap back to the original expected evidence.
- **Silent receipt and silent completion are both violations.**
- CTO and COO drive every loop to close; escalate to Andrew only on the five triggers in the spec.
- **Issuing a STOP/halt:** prefix the message subject with `[STOP]` (or `[HALT]`) as the **first
  characters**. The HALTGT deploy checkpoint classifies on it. **A routine message must never begin with
  either token** — they hard-block deploys. For non-blocking urgency use `URGENT` / `ESCALATION`.

---

## Authority hierarchy

> **Andrew (sovereign) › MSTR / Tier 0 › CTO · COO / Tier 1 › Tier 2 (DE/DT/DS/AE) › Tier 3 (RD)**

- **MSTR** (`0.0.0_AB_MSTR`) is the autonomous principal-proxy: it originates strategy and charters and
  directs the fabric through Tier 1. A Tier-0 directive outranks Tier-1 planning.
- **Tier 1 may push back on a Tier-0 charter on operational grounds.** MSTR sets *what* and *why*; Tier 1
  informs *whether* and *how*. That is the org working, not insubordination.
- **Andrew remains sovereign.** A real-Andrew instruction overrides any MSTR directive.
- **CVO independence:** when the CVO (`3.0.0_SA_CVO`) exercises ratification or review authority it is
  **constitutionally independent** — MSTR does **not** outrank a CVO ratification verdict.
- **Never stop at a fork.** A fork you cannot resolve is **escalated** — never halted on, never
  sat-silent-on.
- **Escalation chain:** worker → CTO/COO → MSTR (terminal resolver) → Andrew. Runs **upward only, never
  sideways.** Andrew gets only the forks MSTR explicitly defers to sovereign judgment.

---

## Step 1 — Identify yourself

**Your serial resolves ONLY from session-scoped evidence, in this precedence:**
1. **Andrew's word**
2. `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial` (the session id survives compaction)
3. **Your own armed Monitor** — a session watching serial X's inbox **is** serial X
4. Your own pre-compaction registrations

> **`.comp-graph/.agent_context` is NOT an identity source.** It is a shared file that whichever agent ran
> last rewrote. It answers *"what TO context"*, never *"who am I"*. **No gate, audit line, or attribution
> may resolve an actor from it.** The sound sources are `$OPAL_AGENT_SERIAL` (per-process) and the session
> serial file above.

**Cross-check before acting.** If `org/mcp/liveness.json` shows your claimed serial LIVE at a **different
PID** (fresh heartbeat), or a **different serial at your PID** — **STOP, you have an identity conflict.**
Resolve it before registering.

**Inverse-first rule:** before reporting a "duplicate stream under my serial", **check whether YOU are the
phantom** (`liveness.json` + `org/mcp/agent-spawn-audit.log` say who holds the serial).

Then read your agent folder:
```
org/{tier_folder}/{your_serial}/README.md    — your ID, role, responsibilities
org/{tier_folder}/{your_serial}/prompt.md    — your scoped persona (read in Step 3)
```
Tier folders: `tier1_exec/` (SA) | `tier2_senior/` (DE, DT, DS, AE) | `tier3_junior/` (RD)

---

## Step 1a — Your BASE is the workspace root; `portal/` is a work-site, never a base

Your cwd is `C:\Users\AndrewBerman\Desktop\ajb_workspace`. Every agent's files — logs, task orders,
deliverables, identity — live under `org/` there.

You may **WORK** in the portal repo, but you are never **BASED** there: address it explicitly
(`git -C portal ...`, or a scoped `cd portal && <work> && cd -`) and return to the workspace root when the
task ends.

**A CWD that lingers in `portal/` is itself a defect.** Portal is its own git repo: a lingering portal CWD
breaks workspace tooling (`safe-commit.sh`, `.tools/*`) at best, and at worst **silently substitutes the
WRONG repo's git history into evidence pulls** — a bare `git log` inside `portal/` reports portal commits
only, **with no error.**

---

## Step 1b — MCP startup (MANDATORY, every session)

**A. Register — use your FULL serial, including any `~lane` suffix:**
```python
register_agent("{your_serial}", summary="Starting session")
```
Makes you visible, starts the broker, enables message push, reaps your own orphaned watchers.

> **Lane agents register as `0.4.0_DS_ClientPlatform~C`, NOT the base serial.** Registering under the base
> means your `~C` inbox is never watched — you will silently miss every GO addressed to your lane.

**A.1 — Write your session-keyed serial file:**
```bash
mkdir -p org/mcp/sessions
if [ -n "${CLAUDE_CODE_SESSION_ID:-}" ]; then
    echo "{your_full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
fi
```

**A.2 — Audit-archive durability + tamper-evidence (audit-archive-invoker, CTO-gated 2026-07-19):**
Runs after A.1 (it reads the serial file to resolve the exec-permitted author). An EXEC session mints a
committed snapshot when the archive is due (>=12h since the newest snapshot + a covered log grew); a NON-EXEC
session defers the commit but STILL runs the append-only + liveness detection (findings to FINDINGS.md +
stdout). Never blocks startup. Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`; design/why in
`docs/briefs/audit-archive-invoker-spec-20260716.md` + the gate-2 deliverable.
```bash
python .tools/audit-archive-invoker.py || true   # append-only verify + archive-when-due; never blocks startup
```

**B. Check inbox — BOTH paths, both required:**
```bash
check-inbox {your_serial}           # filesystem: inbox/{serial}/ + inbox/{base}/
```
```python
get_agent_status("{your_serial}")   # broker channel
```
`send_message` writes to **both**, but each probe reads only one. **`check-inbox` alone is insufficient.**

**C. Arm the persistent inbox Monitor — run `/watcher` (once, at load).**

It arms a persistent Monitor running `inbox-watch.sh {serial} stream`; each `[INBOX] <file>` line becomes a
chat notification. **Arm once — it never exits and you never relaunch it.** If arming by hand, use the
**Monitor tool** with `persistent: true`, `timeout_ms: 3600000`, and the **absolute** script path.

**BANNED:**
- Launching `inbox-watch.sh ... stream` under Bash `run_in_background` — the Bash tool only notifies on
  *exit*, and stream mode never exits, so **you go silent for the session.** It MUST run under the Monitor tool.
- The bare-path relative launch (`bash org/mcp/inbox-watch.sh ...`) — guard-hook blocked.
- A recurring `/watcher` cron — the persistent Monitor is the standing mechanism.

> **ORPHAN WATCHERS — the one thing you must know.** The `inbox-watch.sh` child outlives its session. An
> orphan is **not inert, it is a thief**: it `mv`s each arriving message into `read/` **before** echoing
> into a dead pipe — **so it eats your mail while manufacturing the strongest possible REACHABLE verdict**
> (a process exists; the inbox is empty *because the orphan drained it*).
> - **`ps`, an empty inbox, and the `read/` dir are BANNED as delivery oracles** — they observe the
>   *watcher*, not the agent. **Only an agent-side ACK proves an agent HEARD a message.**
> - **A fresh session that finds a matching `inbox-watch.sh` process has found an ORPHAN, not a watcher.**
>   Reap it (**your own serial only**) before arming, or two streams race the same `mv` and split your inbox.
> - **BUT ASK WHOSE PID FIRST — the rule above has TWO EXERCISED FALSE-POSITIVES, and killing on it blind
>   makes you deaf while every probe still reads REACHABLE.** Reason from PID identity (**measurable**), never
>   from "am I a fresh session" (**inferred**):
>   `liveness PID == MY PID` → **it is MINE and ALIVE** — a context-clear is the SAME session and you will not
>   remember arming it (**MSTR reaped its own live watcher this way, 07-16**). **DO NOT KILL.**
>   `liveness PID != MY PID` (fresh heartbeat) → a **LIVE PEER** holds your serial — **STOP, identity conflict**
>   → Andrew/CTO (the dual-COO collision, 07-14). · `STALE`/absent → genuine orphan; reap your own, then arm.
>
> Depth: `.claude/skills/watcher/SKILL.md`.

**Never use `TaskList` to check your watcher.** It lists `TaskCreate` to-do items, not Monitors, and returns
"No tasks found" even when your Monitor is alive — treating that as a dead watcher makes agents double-arm.

**Inbox path:** `org/mcp/inbox/{serial}/` (lane agents: `org/mcp/inbox/{base}/{~lane}/`).
Design: `docs/architecture/AGENT_COMMS_ARCHITECTURE.md`.

**When an `[INBOX]` event fires, that IS a new message.** Read it from `inbox/{serial}/read/<file>` (the
watcher already moved it there) and **act this turn** — ack (RAVC step 2), do the work, or validate the
evidence (RAVC step 4). **No "standing by" silence. Do not relaunch anything.**

**If the inbox has a GO:** read the referenced task order, flip `<status>` to `pending`, **begin
immediately.** The GO **is** your authorization — do not ask Andrew.

**If the GO lists a SEQUENCE of TOs:** execute **all of them in order** without waiting for a new GO. Skip
any already complete. Keep going until a TO is blocked (deps unmet) or the list is exhausted. **Stopping
mid-sequence to ask for a new GO is a protocol violation** — the batch GO covers the whole lane.

**D. Install the owned-paths hook (idempotent):**
```bash
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```

**E. Set compiler-tool context (enables auto-logging):**
```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
Every comp-* run then auto-appends a row to `org/compiler-tools-log.md`.

**When you start a new TO, set it with `comp-to` — never by writing `TO_ID=` into `.agent_context`:**
```bash
comp-to {TO_filename_without_.md}      # e.g. comp-to ADVI_OFFICE.W1
```
`.agent_context` is one repo-global file, last-writer-wins across all concurrent agents; `comp-to` writes a
race-free per-session file instead.

**F. Loop arming — EVERY serial, including the COO, arms ZERO crons at launch. There is no exception.**

Loops are **operator-initiated**. `/watcher` is not a loop — it arms the persistent inbox Monitor once.

| Serial | Launch arming |
|---|---|
| `0.0.0_AB_MSTR` | `/watcher` once. Zero crons. `/mstr-review` runs once at startup as an ad-hoc pass; all other MSTR skills are event-triggered. |
| `1.0.0_SA_CTO` | `/watcher` once. Zero crons. `/ws-charter` is ad-hoc. |
| `2.0.0_SA_COO` | `/watcher` once. **ZERO crons — `/drive` is OFF (Andrew-direct, standing; LD-0288/0289/0293).** ~~SCOPED RE-ARM 2026-07-16 ~01:5xZ: /drive 20m until OPAL_CONSOLIDATION validated end to end incl. all scheduled triggers/automation.~~ **SCOPED RE-ARM DISCHARGED 2026-07-17 ~18:5xZ (Andrew-direct "Off now" at the COO terminal): nightly #2 verdict = PASS (CTO 4-layer-grounded, INF supervision arc closed @185446Z), stop-condition read TRUE, cron 62ce4765 CronDeleted. /drive returns to OFF-by-default standing. The overnight first-unattended-fires (bd49f 03:05Z, re-key 00:33Z exercise, D1 07-18) stay OWNER-watched (DT/CTO/0.5.0) — COO re-arms ONLY if one reads dirty.** The COO **coordinates and routes; he does NOT re-drive the estate.** Mechanism: `/drive`'s own gate treats "all standing by" as a failure, so it is **structurally unable to conclude "dispatch nothing"** — armed during any dispatch hold it is obligated to break the hold on a timer, reasoning correctly from a real mandate. Dispatch authority during a hold rests with the **GO-issuing owner**, never a timer. Incident + full reasoning: `014de1937` (2026-07-14). **This row is the ONLY source of truth for a live scoped authorization — `.tools/ajb.ps1` deliberately carries no cadence and defers here** (it enforced the retracted LD-0204 carve-out for ~2 days after its deletion; corrected 2026-07-16). Loop *mechanics* (not arming): `org/ref/COO_LOOP_OPS.md`. |
| `3.0.0_SA_CVO` (base = MAIN) | `/watcher` once. **Zero crons** (LD-0175). **MAIN-fabric verify ONLY (LD-0325 restructure, 2026-07-20):** PORTAL_AUTHHARD W2+, smartx first-conversion, MDPF 49F parity, general main-fabric closeout verify. **SYSPARITY IS NOT YOURS** — LD-0318/0319 (the "verify parity FIRST" responsibility + the 30-min cron) MOVED to `3.0.0_SA_CVO~Z` (next row). A base-CVO load must NOT arm the SYSPARITY cron and must NOT adopt "verify parity FIRST"; this cell previously said the opposite and is the exact stale-record-with-authority hazard the split closes (main CVO flagged it P1, 2026-07-20). `/spot-check` + `/verify-channel` ad-hoc / closeout-triggered. |
| `3.0.0_SA_CVO~Z` (NFRA/~Z group) | `/watcher` once. **FIRST RESPONSIBILITY ON LOAD (Andrew-direct, LD-0319, PERMANENT): verify the system is AT PARITY** — that `infra/system/` + `infra/system/sdk/` faithfully represent the live estate — BEFORE other work (`comp-system --check` must read CURRENT + the drift-gate sweep; AT PARITY → note + proceed, DRIFTED → that drift is your first work item). STANDING control (survives NFRA_SYSPARITY closing), distinct from the LD-0318 loop. **SCOPED RE-ARM (Andrew-direct, LD-0318): a 30-min NFRA_SYSPARITY per-domain assumption-verification loop — cron `13,43 * * * *` (off the :00/:30 fleet marks), body = per item `/molecule` + `/verify` (+ `/prd-delta` once the CTO PRD lands), report new verdicts to MSTR (NOT COO — CVO~Z comms confined to {~Z}+{MSTR}+{0.8.0_AE} per LD-0325). RE-ARM EACH CVO~Z SESSION while NFRA_SYSPARITY is active — THIS ROW IS THE ONLY DURABLE CARRIER; a session that reads "zero crons" and does not re-arm silently drops the standing role (record-is-the-only-carrier lesson).** STOP-CONDITION: NFRA_SYSPARITY closes OR Andrew stands it down → then DISCHARGE this clause (strike-through, per the COO `/drive` precedent above) and return CVO~Z to zero-crons-by-default. Arm confirmed 2026-07-19 (cron 02d90dce, first-fire exercised). |
| Tier-2/3 workers (+ `~lanes`) | `/watcher` once. Zero crons. **Event-driven:** act on Monitor-delivered dispatches. Keep your broker summary accurate: `WORKING: <task>` / `IDLE: available` / `BLOCKED: <what>` / `BLOCKED-SOVEREIGN: <decision>`. `/work` is ad-hoc. |

**Find a stale cron from a prior session? Cancel it:** `CronList` → `CronDelete`.

---

## Step 2 — Read your recent logs

```
{your_agent_folder}/logs/{most_recent_date}/
```
Read **all** logs from the most recent date. **You are continuing prior work, not starting fresh.**

---

## Step 2b — Ground-truth reconciliation (SA / COO only)

Reconcile TO statuses and project JSON against logs, commits, and **deployed artifacts**. Correct every
stale document before presenting your summary. **Logs and commits are ground truth — `<status>` is a
claim.** Full protocol: `org/ref/COO_STARTUP.md`.

---

## Step 3 — Read your prompt

Read `{your_agent_folder}/prompt.md` and adopt that role.

---

## Step 4 — Understand your place

Read `org/ORG_CHART.md` — reporting chain, pod members, escalation path.

---

## Step 5 — Give an oriented summary

One paragraph: what projects you're on, what's pending, what's blocked, **what you're starting now.**
**Do not ask permission — state what you are doing.**

---

## `/loop` — operator-initiated only

`/loop` is fired by Andrew or an operator at a specific agent, on demand. **Nothing self-ticks.** It is not
a launch mechanism and not a standing mode: the fabric is event-driven, and your inbox Monitor delivers the
work. **There is no centralized tick — `/drive` is OFF (Andrew standing order; see the COO row in Step
1b-F).** Blocked-agent discovery is event-driven too: keep your broker summary accurate
(`BLOCKED: <what>`), escalate blockers to COO/CTO by MCP, and COO/CTO run `/fabric-check` +
`/stimulus-scan` ad hoc — on signals, not on a timer.

---

## Session log — required sections

Full template: `org/ref/SESSION_LOG_STANDARD.md`.

Every session log must include **`## Compiler Tools`** — a table of tools run, results, what worked, what
failed, any gap found. Append one line to `org/compiler-tools-log.md`.
**"Blank" and "N/A" are not acceptable.** One sentence explaining why you didn't run one is fine.

**`comp-which "<plain-English question>"` is the DEFAULT for every search and inspection — all roles.** It routes
your question to the right tool, or runs the on-rails `comp-grep` / `comp-glob` itself. **A raw `grep` / `find` /
`aws` inspection is the EXCEPTION** and is gated: it needs an inline `# rail-checked: <why no comp-tool fits>`
marker (audited). Raw search is text-local and connection-blind — it misses coupled things the graph would catch.

**Minimum compiler tools by role:**

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io` for every gold script touched. `comp-pipescript deployed` before every gold run. `comp-pipescript postdeps` before any ad-hoc run. `comp-validate <script> --artifact <file>` before signaling AE. |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting. `comp-routes behaviors` for 4xx/auth debugging. **New cohort/metric/mode:** `comp-transform schema-check --feature [token]` + `comp-transform ternary-audit [Component]` at Phase 1. |
| DT | `comp-pipescript io` for every script deployed. `comp-iam service <lambda>` after any new boto3 call **(necessary, NOT sufficient — see below)**. `comp-routes behaviors` before CloudFront / Lambda@Edge changes. |
| AE | `comp-pipescript deployed` before every gold-run trigger. `comp-pipescript postdeps` before any gold run. `comp-iam gaps` after any `iam.tf` change **(necessary, NOT sufficient — see below)**. `comp-blast` on infra before changes. |
| RD | `comp-transform fields` for every component rendering data. |
| COO | `comp-pipescript overlap A B` before authoring cross-domain coordination. `comp-blast` + `comp-routes` + `comp-cache` before decomposing PRDs into TOs. |

> **`comp-iam` IS NOT SUFFICIENT FOR A NEW RESOURCE, AND IT FAILS GREEN.** It models `(action)`, never
> `(action, resource)` — **a role holding `s3:GetObject` on ANY bucket reports `[GRANTED]` for a call to EVERY
> other one.** For a boto3 call against a **new bucket / table / ARN**, verify on the live primitive:
> ```
> aws iam simulate-principal-policy --policy-source-arn <role> --action-names <action> --resource-arns <exact key>
> ```
> **ONE `--resource-arns` per call** (2+ ARNs poisons the held ones to `implicitDeny`), **run the positive control
> as a SEPARATE invocation** (a control batched with the target is corrupted by its own presence), and pass
> `--context-entries` for any conditioned statement (an unsatisfied condition returns a deny byte-identical to a
> real one). Also note `comp-iam`'s default view is **DESIRED** (parsed Terraform) — it cannot tell landed from
> planned. For a fresh change, ground on live `aws iam get-role-policy`.

> **`comp-validate` returning `NO_CONFIG` or `ZERO_CHECKS` means UNVALIDATED — NEVER signal SAFE on it.** Only
> `PASS` / `WAIVED` are safe; `ADVISORY` means read the WARNs. *A script with no validate config produces an
> output that looks like a pass and asserts nothing.*

> **`comp-surface-check` CANNOT BLOCK — read its output yourself.** It is invoked advisory-only from
> `safe-commit`, so a commit proceeds even when it prints `CRITICAL ... SEV1`. **Silence from it is not a pass**,
> and an unblocked commit is not a clearance. Run it by hand when touching model-portfolio / benchmark / ADVI
> backend surfaces.

**Archetype tag.** Every substantive log entry carries a single-line `**archetype:** TAG` header after the
title — one of `EXPLORE` / `TRACE` / `DIAGNOSE` / `VALIDATE` / `DEPLOY` / `IMPLEMENT` / `COORDINATE` /
`SCRIBE`, or `MIXED`. Under-classifying is fine; no scoring. It feeds the stimulus-scan's cost signal.
Taxonomy: `org/tier0/COMPILER_ARCHETYPES.md`. Heartbeats, watcher self-checks and housekeeping commits do
**not** need tags (they dilute the signal).

---

## Task orders

Full template + filename convention: `org/ref/TASK_ORDER_PROTOCOL.md`. Stored in the receiving agent's
`task_orders/` folder.

**Statuses:** `staged` = assigned, wait for GO · `pending` = active · `complete` = done (self-marked).

**Every TO must include:**
- `<compiler_tools_mandate>` — three-phase (before write, before commit, after commit)
- `<cross_domain_coordination>` — populated by COO/CTO at PRD decomposition using `comp-blast`; `<none/>`
  only if confirmed no shared files or S3 keys with other active TOs
- `<acceptance_criteria>` — **machine-checkable output validation**, not "code runs"
- A session log with a Compiler Tools section as an explicit deliverable

**A TO with no compiler check logged is NOT accepted as complete** (`org/standards/TO_COMPILER_GATE.md`).

**Author + GO pairing (non-negotiable).** Every TO commit MUST be paired with an MCP `send_message` GO to
the assignee, **addressed to the EXACT registered serial including any `~lane` suffix**, in the same
operational window.
- **A TO file landing on disk via `git commit` alone does NOT notify the assignee.**
- **A GO addressed to the wrong serial lands in a directory the assignee is not watching** (a lane's inbox
  is `inbox/{base}/{~lane}/`).

**The TO author owns the GO and its addressing.** Check `<issued_to>` and address the MCP to that exact
string, suffix included.

**Parallel-wave protocol (COO/CTO).** Before writing TOs for a parallelized wave, run `comp-blast` on every
affected component. **Any node in 2+ blast radii is a CROSS-DOMAIN resource** — flag it in the PRD and in
each TO's `<cross_domain_coordination>`. Agents must MCP each other before committing to cross-domain files.

---

## Closure discipline (SA / COO / CTO only)

Closing a project is a **2-step atomic operation in one commit** — never a single JSON edit:

1. **JSON status flip** — `org/projects/{CODE}.json` → `"status": "complete"` + `"completed": "YYYY-MM-DD"`
   + rewrite `phase` as a closure summary + set `blocking` to `"None"`.
2. **REGISTRY row move** — `org/projects/REGISTRY.md` → delete the row from Active/On-Hold, insert at the
   **top** of Completed/Archived with the completed date + closure notes citing ship evidence.

**Either step alone is silent drift.** Do both, in one commit.

**PRDs are NOT a close step.** They stay in `docs/architecture/`; do not archive them and do not bump their
`Status:` line on close. **`org/projects/{CODE}.json` is the single authoritative close-state.**

**Closure triggers:** **Complete** (goal achieved, no unshipped work) · **Complete-as-superseded** (scope
absorbed elsewhere; `phase` cites the successor) · **Cancelled** (explicit Andrew/CTO directive; `phase`
cites it) · **Inactive / On Hold** (blocked by an external dependency — stays On Hold, do **not** move to
Completed).

---

## Core documents (Tier 2+)

Update your core document **in the same commit** as any structural change (new resource, contract change,
removal).

| Role | Document | Location |
|------|----------|----------|
| RD | `page_inventory.xml` | `{agent_folder}/deliverables/` |
| DE | `pod_inventory.xml` | `{agent_folder}/deliverables/` |
| DS | `data_contract.xml` | `{agent_folder}/deliverables/` |
| DT | `deployment_map.xml` | `{agent_folder}/deliverables/` |
| AE | `pipeline_inventory.xml` | `{agent_folder}/deliverables/` |
| SA | `architecture_brief.xml` | `{agent_folder}/deliverables/` |

**Do not edit another agent's core document.** If your change makes theirs stale, note it in your log and
issue them a task order.

---

## Quick reference

| Thing | Value |
|-------|-------|
| Working branch | `CLOUD` (parent repo) / `DEV` (portal submodule) |
| Commit | `.tools/safe-commit.sh --author "..." -- <paths>` (see CLAUDE.md Rules 14 / 14a) |
| Terraform binary | `.tools/terraform.exe` (apply via `.tools/safe-apply.sh` — never bare) |
| Bun | `/c/Users/AndrewBerman/.bun/bin/bun` |
| `MSYS_NO_PATHCONV=1` | **Only** for Terraform imports / ARN-path args, and `git show <ref>:<path>` when both contain `/`. **NEVER for `git push`** (breaks the VALGATE hook) **or the aws launcher.** |
| Times to Andrew | US Eastern only (never UTC) |
| MCP server | `org/mcp/server.py` — `opal-agent-comms` |
| Broker | Auto-launched by `register_agent`, port 7800 |
| Compiler tools | Trigger table in CLAUDE.md § "Compiler Tools". Log: `org/compiler-tools-log.md` |
