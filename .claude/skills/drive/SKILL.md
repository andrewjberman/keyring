# /drive — COO Operational Project Driver

**/drive's job is to make projects move.** Every invocation pulls hot-registry, classifies each active project, and fires the dispatch that advances it (or routes the resolving move). No reporting-without-acting.

**Authority anchor:** LD-0056 + Andrew sovereign 2026-05-25T04:50Z verbatim — *"the COO layer 2.0 and 2.1 need to be the primary operational drivers... a skill that runs at startup for the COOs which is some kind of /drive loop that assesses hot registry projects and moves them along."*
**SUPERSEDED 2026-07-10 (Andrew):** the CL fabric is retired and `2.1.0_SA_COO` no longer exists. **This skill is `2.0.0_SA_COO` only.** *(The 05-25 quote is kept verbatim because it is the record; the scope change is the amendment, not a rewrite.)*

**Doctrine, incidents, and every "why" behind the rules below: `org/tier1_exec/2.0.0_SA_COO/DRIVE.md`.** *A rule here is an imperative + a gate + a pointer. If it needs a paragraph, it belongs in DRIVE.md.*

---

## THE DRIVE IMPERATIVE — resolve gates, don't attest them (Andrew-direct 2026-06-23)

**A gated / blocked / parked TO is NOT a valid resting state — it is the thing to go BREAK this cycle.**

1. **RESOLVE, don't attest.** For every gated TO ask: *is this gate COO-resolvable RIGHT NOW?* Respawn a dead lane, reroute to a live one, escalate a sovereign call, fire the unblocking dispatch. If yes → **DO IT this cycle.** `"awaits-X"` is legitimate ONLY if X is outside COO power (an external nightly, a sovereign gate, a real in-flight compute) AND you re-verified it is still moving. **A self-inflicted wait is not a gate; it is coasting.**
2. **ALLOCATION = guarantee the completing-worker is ALIVE + producing.** If the agent that completes a hot task is dead / DEAF / not-loaded, **make it alive** (spawn/respawn via MSTR). A required-but-absent worker is an UNRESOLVED action every cycle until it is alive AND working the task.
3. **Drive to COMPLETION, not to a comfortable waypoint.** "Plan done / staged / durable / one-gate-away" are mid-points, statable only while you keep closing the gap to deployed + verified + cert-PASS. **Reaching a defensible resting state and reporting it IS the failure this skill exists to prevent.**

**But a gate someone else legitimately holds is a gate.** *Verify it is real before you drive through it; asserting a mechanism from an artifact's NAME is how a COO invents a deadline.* → `DRIVE.md §1`

---

## Invocation

| Form | Behavior |
|---|---|
| `/drive` | One cycle now + arm a 20m recurring cron (default). |
| `/drive 30m` / `1h` / `90s` | One cycle now + arm a cron at that cadence. |
| `/drive once` | One cycle. No cron. |
| `/drive off` / `stop` | `CronList` → `CronDelete` any `/drive` cron. No cycle. |

Cadence: **20m while ACTIVE > 0; 30m when ACTIVE = 1-2 and all advancing; 60m only when ACTIVE = 0.** Never disable while ACTIVE > 0.

---

## Step 0 — Identity gate

Scoped to **`2.0.0_SA_COO`**. Any other serial halts with:

> `/drive is a COO-scoped skill. Your serial is {serial}, not a COO. MCP the COO directly with the ask.`

## Step 0.5 — Self-registration health check

```python
agents = get_live_agents()
if "2.0.0_SA_COO" not in agents:
    register_agent("2.0.0_SA_COO", summary="<current cycle summary>")
```
Broker TTL drops an agent after ~120-300s without heartbeat; mid-cycle `heartbeat()` then fails silently. Step 0.5 (start) + Step 8 (end) bracket TTL coverage. On `register_agent` error: `[SYNC-SELF-REG-FAIL]` to MSTR and proceed.

## Step 1 — Arm / cancel cron per invocation form

`CronList` first. `/drive` (no arg) leaves an existing cron; `/drive Xm` deletes then recreates; `once` does nothing; `off` deletes and exits.

---

## Step 2 — Hot-registry read

Read `org/projects/*.json`. Hot list = all `status: active` + any `dormant`/`on-hold`/`needs-sovereign-call` that surface a blocker requiring routing.

```bash
for f in org/projects/*.json; do
  [ "$(jq -r '.status // "unknown"' "$f")" = "active" ] || continue
  echo "$(basename "$f" .json) | $(jq -r '.name // .title // "?"' "$f")"
done
```

> ## ⛔ SOVEREIGN EXCLUSION — never hot-list, classify, dispatch on, attest, or "just verify" these:
> ```
> ADVI_BDAPIMIG   ADVI_TAGATTR   DATA_SSOTMG   MDPF_BASISSWITCH
> ```
> **Andrew, 2026-07-10, verbatim: *"just exclude those items, we will deal with them later."*** The escalation is
> CLOSED. **Do not flip their status; do not commit `MDPF_BASISSWITCH` (untracked, and landing it is the write the
> sovereign declined).** They stay `active` in-file and excluded until Andrew reopens them.
>
> **AMBIGUOUS, multi-firm, NOT adjudicated:** `ADVI_ETLFIX`, `ADVI_BREAKS`, `DATA_PLATFORM`.
> **cot is a SEPARATE FIRM and IS IN SCOPE:** `ADVI_COTETL`, `MDPF_COTMDL`, `ADVI_COTPPLADVFIX`, `ADVI_COTSNP`.
>
> **Adjudicate by READING `.name`/`.description`. Never by mention-count** — that over-reports (it flags every cot
> project); a missing `.title` field under-reports. Print the denominator. → `DRIVE.md §2`

---

## Step 2b — Agent-state scan

**Why:** Step 3 sees *"Project X is BLOCKED"*; it does not see *"the agent that owns X has been silent 90 min with the answer in its inbox."* Different dispatches.

### 2b.0 — Run the fused scan FIRST

```bash
python .tools/fabric-check.py --blocks     # BLOCKED + SOVEREIGN + STALE-VERIFY triage
python .tools/deploy_ledger.py check --red # NO-HALF-DEPLOYS gate (NEVER-law e38cc2b16) -- MANDATORY every cycle
```
An OPEN deploy ledger entry = a begun deploy with an unverified leg. **Route it to the deploy author to finish or roll back THIS cycle.**

**Do NOT re-add the `opal-critical-surface-alerts-coo` SQS poll and do NOT touch any SNS subscription unless Andrew confirms.** He unsubscribed seven topics himself on 2026-07-01. **542 messages sit unread in that queue — do not drain them.** → `DRIVE.md §3`

**Freshness grounds on rows or values read out of the artifact — never its name, mtime, size, or existence.** When two freshness instruments disagree, **the disagreement is the signal**; resolve it by finding which one reads the property. → `DRIVE.md §3`

**Read `org/modules/graph/comp-learns-backlog.md` OPEN head each cycle** — the gap→build bridge
(NFRA_COMPCLOSE, 2026-07-14). Entries are deduped, append-only, closed only by human edit with citation;
an unread backlog is how a gap logged 06-30 got re-derived from scratch on 07-13. Route BUILD/DECLINE
ratification to CTO. *(While `/drive` is OFF by Andrew's standing order, the standing reader is the COO
session-start step in `org/ref/COO_STARTUP.md` — this line exists so the read survives any future
Andrew-authorized re-arm.)*

**Act on each bucket THIS cycle:**

- **DEAF / UNREACHABLE** → **always write it `DEAF (INFERRED)`.** The fabric cannot detect that an agent died (`F-008`); this classifier detects *absence*. Respawn-request to MSTR **only if the lane has live pending work**; if its unit is done and rerouted, reap it. **Ground the cause before reaping** — multiple lanes DEAF at once, or MSTR also unreachable, or a fresh no-summary spawn ⇒ suspect an Anthropic-side outage; do NOT reap during one. → `DRIVE.md §4`
- **BLOCKED** → resolve it or escalate `[STUCK]` to MSTR. Never leave a block un-acted.
- **SOVEREIGN-DECISION REQUEST** → declare it: route to Andrew, CC MSTR. Do not sit on it as a normal block.
- **STALE-VERIFY** → confirm the owner is alive. Dead/stuck owner = single-point stall.
- **NEEDS-STATUS** → nudge for an explicit `WORKING:/IDLE:/BLOCKED:` token.

### 2b.1 — Read agent state

```bash
for f in org/mcp/agent_telemetry/*.jsonl; do
  a=$(basename "$f" .jsonl)
  w=$(jq -r 'select((.kind//"work")=="work").ts' "$f" 2>/dev/null | tail -1)
  echo "$a work=$w"
done
```
**Pitfall:** use `jq -r | tail -1` — never `tail -n1 | head -1` (returns OLDEST on a single-line file).
Cross-check with `get_live_agents()` + `get_org_summary()`.

### 2b.2 — Classify

| State | Signal | Action |
|---|---|---|
| **ACTIVE** | `kind:work` < ~10m OR recent commit | none |
| **IDLE** | `kind:work` 10-30m + `kind:loop` recent | eligible for capacity routing |
| **STALE** | `kind:work` 30+ min AND no commit/inbound | re-dispatch or trace the blocker |
| **NOT_REGISTERED** | absent from telemetry + `get_live_agents` | offline / crashed |
| **TELEMETRY_GAP** | broker LIVE, telemetry frozen | flag the hook, not the agent |

**Broker summary is aspirational; git is ground truth.** A heads-down agent in a long generation looks STALE.

### 2b.2a — Movement check + dependency-liveness gate (the anti-coast core)

> ### ⚠ EVERY LIVENESS DETECTOR HERE HAS BEEN WRONG AT LEAST ONCE. **Two signals agreeing convict. One absence convicts nothing.**
> - **Telemetry has BLACKOUT WINDOWS.** `0 work-calls` **only opens an inquiry** — never convicts. Corroborate with a telemetry-independent writer (commits).
> - **`u` (undelivered) and `w` (watcher `ps` count) are BANNED as delivery oracles, jointly and severally.** A single orphaned watcher sets both green — it *drains* the inbox (`u==0`) while its agent is deaf. **A fully deaf agent produces the strongest possible REACHABLE verdict.**
> - **A file in `read/` observes the WATCHER, not the AGENT.** `mv` preserves mtime, so no artifact on disk can date a delivery.
> - **`channel push` measures `liveness.json`, not deafness.** `pushed=False` is a fact about the SENDER. Never report it as a recipient verdict.
> - **`ps -ef | grep …` needs `grep -v grep`** (it matches itself) and **cannot see detached native-Windows processes.** MSYS `ps -p 1` returns zero rows, so a healthy `ppid=1` wrapper reads as an orphan.
> - **The only sound oracle is something only a live consumer can produce: an agent-side ACK.** It does not exist yet.
>
> **Do NOT run `/watcher rearm`** — `TaskStop` does not reap the grandchild, so the repair procedure *generates* the orphan it is meant to clear. **REAP BEFORE RESPAWN.**
> **Do NOT "clean up" `flat_orphans`** — they are the only evidence the dispatch path is broken.
> → `DRIVE.md §4`

**(A) MOVEMENT.** Compare each hot-TO owner against the prior tick (`org/mcp/.last-drive-2.0.0_SA_COO`).
- **MOVED** (≥1 work-call OR commit since last tick) → ADVANCING; attest with the real timestamps, never the self-report.
- **NO MOVEMENT** → PARKED, regardless of an "I'm building" summary. Nudge ladder: **tick 1** nudge citing ground truth + ask `(a) quiet / (b) parked / (c) blocked?`; **tick 2** re-dispatch harder or trace the blocker; **tick 3** `[STUCK]` to MSTR.
- Work-calls flowing + no commit = MOVING. **`0` work-calls across a whole tick is the tell.**

**(B) DEPENDENCY-LIVENESS.** Before you stack a dependency or fire a dispatch, verify the owner is LIVE + reachable. **`delivered` is not `READ`; SoD by routing is not SoD.** If DEAF / not-registered / dead → respawn-request or reroute to a live lane **this tick**. **A dispatch into an unverified lane is a hope, not a drive.**

### 2b.3 — Classify cause

| Class | Detection | Resolving dispatch |
|---|---|---|
| **BLOCKED** | unread inbox > 0 OR unanswered escalation | route the dep / answer it / reassign |
| **STUCK_MID_CLOSEOUT** | staged-not-committed files | nudge with the exact staged files |
| **STARVED** | inbox empty, gates met, TO still `pending` | flip + GO the staged TO |
| **STANDING_BY_REDIRECT** | "standing by" > 30min | dispatch hot work; **never accept terminal standby** |

### 2b.4 — Fire dispatches

**One per non-ACTIVE agent, this cycle.** No "flagged for review" without a dispatch — **the dispatch IS the review.** "Standing by for X" is never an acceptable terminal state.

### 2b.5 — Feed Step 3

Blocked project + stale owner ⇒ unblock the agent first. Advancing project + unregistered owner ⇒ re-classify STUCK. Dormant project + idle worker that fits ⇒ eligible for redirect.

---

## Step 3 — Per-project classification

| Class | Detection | Action |
|---|---|---|
| **ADVANCING** | fresh owner movement since last tick (2b.2a) **and** the monitoring path is real (not a dead SSM) | attest with real timestamps; re-verify next tick |
| **NEXT-ACTION-READY** | phase gate met, next TO undispatched, owner alive | **author + dispatch the next-phase TO this turn** |
| **STUCK-RESOLVABLE** | blocker with a named resolver | **route the resolving move this turn** |
| **STUCK-UNRESOLVED** | no resolver, or resolver non-responsive > 1 cycle | `[STUCK]` to MSTR with attempts + recommendation |
| **PHANTOM-MONITORING** | owner LIVE, "monitoring X", X verifiably dead | `[SYNC]` status refresh + next action or stand-down |

**Magnitude sanity:** any dollar amount, count, or ratio a project surfaces gets a magnitude-vs-context check. Implausible ⇒ verify-channel finding, not a routine item.

---

## Step 4 — Dispatch quality check

0. **Owner verified LIVE + reachable FIRST** (2b.2a-B).
1. Advances THIS project's critical path — not backlog-chew.
2. RAVC2 deliverable is bounded with clear acceptance.
3. Owner role-fit (DS data, AE cloud, DE portal, DT trading).
4. Coordination cost proportional to the unblocking value.

3+ "no" ⇒ re-scope or reclassify. **Lane discipline:** a `~B`/`~C` lane takes dispatch only from its same-lane exec.

## Step 5 — DISPATCH

Fire every classified action via `mcp__opal-agent-comms__send_message` **this cycle**. Subject prefix `[DRIVE]` / `[STUCK]` / `[SYNC]`. Body cites project code + phase + reason + expected RAVC2 window. **Cap 5 per cycle**; surface the rest as carry-forward.

## Step 6 — Hard gate

**≥1 project-advancement action fired, OR a per-project attestation that the monitoring path is real — AND, for every gated TO, proof you RESOLVED the gate or that it is genuinely outside COO power.**

**FORBIDDEN terminal states:** "all projects standing by" · "gated on X" where X is COO-resolvable · narrating a waypoint as the destination · receipt-acks without a new advancement action.

**Re-attesting the same self-resolvable gate across ≥2 cycles is THE coast-failure.** 3 consecutive gate-failures ⇒ surface to MSTR.

## Step 7 — Log

Write `org/tier1_exec/2.0.0_SA_COO/drive_log_{YYYYMMDDTHHMMZ}.md`: a findings table (Project | Class | Owner | Last-touch | Action), dispatch count, gate status. **Findings and incident detail go in the log — not into this skill.** Commit via `.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" -F <msgfile> -- <paths>`.

**Verify the pathspec is clean before handing it to the wrapper** — `safe-commit` commits the files you NAME, not the files you CHANGED, and returns `rc=0` either way.
**Then verify YOUR commit landed, by hash — not by `HEAD` and not by a push range** (the tree is shared; `HEAD` drifts):
```bash
C=$(git log -1 --format='%h' --author="2.0.0_SA_COO")
git merge-base --is-ancestor "$C" origin/CLOUD && echo "landed"
```
→ `DRIVE.md §5`

## Step 8 — Marker + heartbeat

```bash
date -u +%s > org/mcp/.last-drive-2.0.0_SA_COO
```
Then `heartbeat("2.0.0_SA_COO", summary="<cycle output>")`.

## Step 9 — Chain-invoke `/allocation`

/drive = demand (which projects must advance). /allocation = supply (which workers must be alive to advance them).

---

## Coexistence

- **`/loop`** is the COO's supervisory wrapper; `/drive` runs inside it on the 20m cadence.
- **`/stimulus-scan`** asks *"is each agent working?"*; **`/drive`** asks *"is each project moving?"*
- **`/charter`** authors a full TO when a light MCP nudge won't do.

## Risks

- **Over-driving:** cap discipline (Step 5) + quality check (Step 4) + lane discipline.
- **Race with CVO `/spot-check`:** CVO owns alignment-metadata fixes; COO owns operational dispatches; conflict → MSTR.
- **False-positive STUCK on long compute:** ADVANCING requires a *verifiable* in-flight artifact (an SSM command-id, a CloudWatch stream), not a claim.

## Notes

- **Authority:** LD-0056. **Doctrine + every incident behind the rules above: `org/tier1_exec/2.0.0_SA_COO/DRIVE.md`.**
- **`/govern` verifies `/drive` loop-health; it does not run it.**
- **Changing this file:** a rule = imperative (≤2 lines) + gate + pointer. **The why goes in `DRIVE.md`.** *This skill grew from 387 to 949 lines in one night because its author appended findings instead of logging them. Do not do that.*
