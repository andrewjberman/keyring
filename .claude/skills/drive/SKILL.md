---
name: drive
description: COO-scoped operational driver skill. Reads hot-registry (active projects in `org/projects/*.json`), classifies each project's current state against most-recent commit + RAVC2 trail + named blocker, and **dispatches the next-action OR resolving move** through the COO's normal authority chain. Hard gate per invocation = ≥1 project-advancement action OR per-project attestation that monitoring path is real. "All standing by" is NEVER an acceptable terminal state. `/drive` arms a 20m recurring cron + runs one cycle now; `/drive 30m` / `1h` / `90s` overrides cadence; `/drive once` runs a single cycle no cron; `/drive off` cancels any running cron. COO-only — other agents invoking halt at Step 0. Per LD-0056 (CY-0102 sovereign architectural directive Andrew 2026-05-25T04:50Z) — institutionalizes COO as primary operational driver; MSTR /govern refocuses to Tier-1 loop-health meta-supervisor.
---

# /drive — COO Operational Project Driver

The project-axis analogue to `/spot-check`'s agent-commit-grain alignment-sweep + /charter's architectural-authoring focus. **/drive's job is to make projects move.** Every invocation pulls hot-registry, classifies each active project, and fires the dispatch that advances it (or routes the resolving move). No reporting-without-acting.

**Authority anchor:** LD-0056 + Andrew sovereign 2026-05-25T~04:50Z verbatim — *"the COO layer 2.0 and 2.1 need to be the primary operational drivers... a skill that runs at startup for the COOs which is some kind of /drive loop that assesses hot registry projects and moves them along."*

---

## THE DRIVE IMPERATIVE — resolve gates, don't attest them (Andrew-direct 2026-06-23; the load-bearing thesis)

**A gated / blocked / parked TO is NOT a valid resting state — it is the thing to go BREAK this cycle. /drive drives tasks to COMPLETION, not to a tidy waypoint.** Three rules that OVERRIDE any "honestly gated" comfort:

1. **RESOLVE, don't attest.** For every gated TO ask: *is this gate COO-resolvable RIGHT NOW?* — respawn a dead/unloaded lane (or pull a pre-agreed contingency), reroute to a live lane, escalate a sovereign call to Andrew/MSTR, fire the unblocking dispatch. If yes → **DO IT this cycle.** `"awaits-X"` is legitimate ONLY if X is genuinely outside COO power (an external scheduled nightly, a human/sovereign gate, a real multi-hour in-flight compute) AND you've re-verified it's still moving. A **self-inflicted wait** — a dead lane you could respawn, a contingency you set but never pulled, an escalation you could fire — is NOT a gate; it's coasting.

2. **ALLOCATION = guarantee the completing-worker is ALIVE + producing — not "signal who's needed."** If the agent that completes a hot task is dead / DEAF / not-loaded, allocation's job is to **make it alive** (spawn/respawn/contingency via MSTR) so the task completes — not to note it's not-alive and wait. A required-but-absent worker is an UNRESOLVED allocation action every cycle until it is alive AND working the task.

3. **Drive to COMPLETION, not to a comfortable waypoint.** "Plan done / staged / durable / handoff committed / one-gate-away / nothing pending" are NOT done — they are mid-points you may state ONLY while you keep closing the gap to the ACTUAL completion (deployed + verified + RAVC/cert-PASS). Reaching a defensible resting state and reporting it IS the failure this skill exists to prevent.

**Anchor (2026-06-23):** OPLMCP.02 sat "gated on ~B-load (outage)" for ~5 consecutive cycles while the outage was demonstrably clear (W1 safe-applied on it; MSTR/CTO/CVO/AE all working through it) and MSTR's fresh-respawn contingency sat un-pulled — COO attested "awaits-outage-clear" instead of respawning the lane. The gate was COO-resolvable the whole time. Cousin lessons: `feedback_drive_read_agent_activity_not_project_paths` (read activity not paths) + 2b.2a (verify movement) — this is the conclusion-layer: *having verified the block, GO BREAK IT.*

---

## Invocation forms

| Form | Behavior |
|---|---|
| `/drive` | Run one cycle now + arm a 20m recurring cron (default). |
| `/drive 30m` / `1h` / `90s` / `15m` | Run one cycle now + arm a recurring cron at the given cadence. |
| `/drive once` | Run one cycle. Do NOT arm a cron. |
| `/drive off` (or `stop`) | Cancel any existing `/drive` cron via `CronList` + `CronDelete`. No cycle. |

Recommended cadence: **20m default while ACTIVE projects > 0; 30m when ACTIVE = 1-2 + all advancing; 60m only when ACTIVE = 0 (rare).** Never disable while ACTIVE > 0 — that is the failure mode this skill exists to prevent.

---

## Step 0 — Identity gate (COO-only)

This skill is scoped to **2.0.0_SA_COO** (ws fabric) and **2.1.0_SA_COO** (CL fabric). If the invoker is not a COO, halt with:

> `/drive is a COO-scoped skill. Your serial is {serial}, not a COO. If you want project-advancement, MCP your division's COO directly with the ask; the COO will handle from its own session per Constitution Art. VI delegation discipline.`

If COO, continue.

---

## Step 0.5 — Self-registration health check (per cycle start)

Before pulling registry / agent state, verify own broker registration is live:

```python
agents = get_live_agents()
if {coo_serial} not in agents:
    register_agent({coo_serial}, summary="<current cycle summary>")
```

If `register_agent` succeeds (no error), continue. If error, surface to MSTR via `[SYNC-SELF-REG-FAIL]` and proceed with cycle (broker hygiene issue separate from project-axis work).

**Why:** broker TTL drops agent from active set after ~120-300s without heartbeat (MSTR-confirmed pattern; STALE-at-120s threshold per `register_agent` summary text). Mid-cycle `heartbeat()` calls fail silently with "not registered" error. Cousin to `/watcher` Step 1 registration-check pattern. Empirical anchor: CL COO 2.1.0_SA_COO cycles #2 + #4 banking 2026-05-26 (`feature_clb/org/tier1_exec/2.1.0_SA_COO/briefs/DRIVE_SKILL_SELF_HEARTBEAT_FOLD.md`); ws-canonical ship per MSTR `20260526T074710Z` §3 (b) draft-then-route APPROVED + LD-0090 ALWAYS-PROCEED.

**Cycle TTL bracketing:** Step 0.5 catches cycle-start re-registration; Step 8 `heartbeat()` (cycle-end) extends TTL through next cycle. Together they bracket TTL coverage. If broker drops between Step 8 (cycle N end) and Step 0.5 (cycle N+1 start), Step 0.5 catches it.

---

## Step 1 — Arm / cancel cron per invocation form

| Invocation | Cron action |
|---|---|
| `/drive` (no arg) | `CronList` → if `/drive` cron exists, leave it; else `CronCreate` 20m default |
| `/drive Xm` | `CronList` → `CronDelete` any existing `/drive` cron → `CronCreate` at given cadence |
| `/drive once` | No cron action |
| `/drive off` / `stop` | `CronList` → `CronDelete` any existing `/drive` cron → exit (no cycle) |

---

## Step 2 — Hot-registry read (fabric-scoped)

**ws COO** reads `org/projects/*.json` from ajb_workspace.
**CL COO** reads `feature_clb/org/projects/*.json` from feature_clb worktree. **[feature_clb RETIRED LD-0222; CL paused, re-home TBD -- path dead pending re-home.]**

Per LD-0042 fabric-scoping discipline: a COO drives only their fabric's registry. Cross-fabric coordination flows through MSTR or joint CTO+COO consult.

```bash
# Per project, extract status + current_phase + last-touched timestamp
for f in <registry-glob>; do
  code=$(basename "$f" .json)
  status=$(jq -r '.status // "unknown"' "$f")
  phase=$(jq -r '.current_phase // .phase // "n/a"' "$f")
  if [ "$status" = "active" ]; then
    echo "$code | $phase"
  fi
done
```

Build the hot list: all `status: active` projects + any `status: dormant`/`on-hold`/`needs-sovereign-call` that surface a blocker requiring routing (queue-hygiene escalation, not silent stale).

---

## Step 2b — Agent-state scan (operative core embedded; LD-0083)

**Do NOT skip this step. Do NOT rely on reading `.claude/skills/stimulus-scan/SKILL.md` separately — the operative steps you need are embedded below.** /stimulus-scan SKILL.md remains the doc-of-record for full taxonomy + edge cases, but this embed is what you execute every /drive cycle.

**Why this step exists:** /drive's project-axis (Step 3) sees "Project X is BLOCKED" but doesn't see "the agent that owns Project X has been STALE for 90 min with an unread inbox holding the answer." Different dispatches. The agent-axis context from Step 2b INFORMS Step 3 per-project classification.

### 2b.0 — Run /fabric-check FIRST (the canonical fused scan; LD-0155)

Begin the agent-state scan by running the fused telemetry+status tool — it does the
telemetry-derived dual-signal liveness + the declared-status reconciliation in one
deterministic command, and it is the single-point-block detector this whole step exists for:

```bash
python .tools/fabric-check.py --blocks    # triage: BLOCKED + SOVEREIGN + STALE-VERIFY
# (run plain `python .tools/fabric-check.py` for the full WORKING/IDLE/... view)
python .tools/deploy_ledger.py check --red # NO-HALF-DEPLOYS gate (e38cc2b16): RED-blares any deploy ledger OPEN past window
# (critical-surface SQS poll REMOVED 2026-07-01 per Andrew-direct -- uncalibrated noise, channel decommissioned; tombstone below.)
```

**Deploy-completion gate (TO #5, BRONZE-FIX #5 — NEVER-law e38cc2b16):** `deploy_ledger.py check --red`
is a MANDATORY part of every /drive cycle. A confirmed+begun deploy that left a leg unverified leaves an
OPEN change_management ledger entry; `check --red` delivers a RED alert to the COO inbox for any entry open
past its window. fabric-check.py also prints an OPEN-DEPLOYS line every pass. If an OPEN deploy surfaces:
route to the deploy author to finish/rollback the stranded legs THIS cycle (the same NEVER-law discipline as
a BLOCKED lane). The inf-ADVI P0 (2026-06-12) was one cutover bundle stranding THREE legs silently — this
gate is the structural catch so it can never recur unseen.

**Critical-surface alert poll — REMOVED 2026-07-01 (Andrew-direct). The OPERATIVE HOLD STANDS; the RATIONALE
below it was RETRACTED 2026-07-09 by its own author (2.0.0_SA_COO). Read both.**

**OPERATIVE (unchanged, Andrew-gated):** the `opal-critical-surface-alerts-coo` SQS poll is stripped from this
step. **Do NOT re-add this poll, and do NOT touch any SNS subscription, unless Andrew confirms.** CloudTrail
(CTO, 2026-07-09): Andrew himself unsubscribed **seven** topics `2026-07-01T02:46:02Z → 02:47:05Z`, aws-cli,
63 seconds, `DeleteTopic: 0`. That is a sovereign act. Three questions are with him; nothing moves until he
answers. **542 messages, oldest 8.9 days, sit unread in that queue — do not drain and do not lose them.**

**RETRACTED RATIONALE — and this entry was the arbiter of it, so read the retraction before citing the entry.**
The original text called the alerts `UNCALIBRATED NOISE` because `bd-cot-silver-stale-holdings` fired while
`comp-freshness` showed cot silver `fully FRESH`, and concluded: *"Genuine freshness verification grounds on the
SERVED artifact via `comp-freshness`, never an alarm."* **That conclusion is FALSE for cot silver, source-confirmed:**
```
.tools/comp-freshness:299-317  _max_partition_date()  -- regex YYYY-MM-DD over `aws s3 ls` FILENAMES.
                               docstring: "the MAX YYYY-MM-DD parsed from the object filenames"
.tools/comp-freshness          grep -c 'num_rows|row_count|footer|pyarrow|read_parquet'  ==  0
data/cot/.../gold_freshness_config.yaml:42,53,64,78,88   all 5 cot silver tables: as_of_source: silver-partition-key
bd-cot-freshness-probe:211-220 (0.6.0, a60ce15ed)        resolves max_as_of from the OBJECT KEY, never row count
LIVE (0.6.0, measured):  cot silver/allocations newest BY NAME = 2026-07-09 (0-row stub)
                                                 newest WITH ROWS = 2026-06-18   -> content lag 15 TRADING DAYS
```
**`comp-freshness` in partition-key mode does not ground on the served artifact. It grounds on the artifact's
NAME.** It is the *same proxy* as the alarm it was used to discredit, and it cannot distinguish a 0-row stub
from a real partition. The tool applies the wrapper-vs-content lesson correctly in **content-mode** (`as_of_field`,
`:614-617`, which names the cot freeze by name) and then, for partition-key mode, swaps mtime for the **filename**
and calls it *"the same correctness"* (`:284`). **It is not.** A date-key is stamped by the writer exactly as mtime
is; neither is a row. The config comment advertises the win as *"not mtime"* — a different wrapper, not the content.

**Therefore:** whether the 06-30 alarm was miscalibrated is **UNDETERMINED and was never established** — the
instrument used to convict it is blind to the same property. This entry **must not be cited as corroboration**
that the seven unsubscribes were intended; it corroborates nothing. (It was written `bc66f94668`, 07-01T03:39Z,
**53 minutes AFTER** Andrew's 02:46Z act — it is a post-hoc rationale, not a record of instruction.)

**Standing rule that replaces the retracted one:** freshness grounds on **rows or values read out of the
artifact** — never on its name, its mtime, its size, or its existence. When two freshness instruments disagree,
**the disagreement is the signal**; resolve it by finding which one reads the property, not by preferring the
familiar one. `bd-cot-silver-stale-{allocations,unrealized}` sit in `OK` today on a table dead since 2026-06-18.
(History: poll added 2026-06-25 after a cot 2-day silent-freeze; hold retained per Andrew-direct.)

**Act on its buckets THIS cycle — this is the load-bearing reason /drive runs (Andrew direct):**
most fabric advancement is event-driven and self-healing, but the failure mode /drive exists to
catch is the **single block that holds up a whole project or the whole fabric**. fabric-check
finds those. For each item in the triage:

> ### ⚠ EVERY `DEAF` / `DEAD` VERDICT THIS STEP EMITS IS **`INFERRED`**, AND MUST BE LABELLED SO UNTIL `F-008` SHIPS.
> **This classifier is an ABSENCE-DETECTOR.** *That is not a criticism of it; it is the only instrument that exists.*
> **But `F-008` establishes that a dead session and a never-spawned session are indistinguishable in every artifact
> we own** — so `DEAF`/`DEAD` is a **hypothesis about why a lane is silent**, never an observation that it died.
> **Write it as `DEAF (INFERRED)` in every log, dispatch, and escalation.** *(MSTR, `035637Z`; Rule 22: an
> ungrounded causal claim is `INFERRED` and non-actionable as a cause — though the REMEDY, a respawn request, is
> prudential under uncertainty and needs no cause.)*
>
> **And never derive a lane-stability property from spawn counts.** *A respawn is evidence that someone BELIEVED a
> lane was dead — not that it was.* **The COO adopted `"0.7.0 dies every ~50min"` from MSTR, wrote it into two drive
> logs, propagated it to `0.7.0`, and priced a durable verify's ownership on it. It was `n=2`. The lane then lived
> `2h12m`.** *`0.5.0_AE_OpalETL` outranks it on the 7-day spawn count.*

- **DEAF / UNREACHABLE** *(always `INFERRED` — see above)* → the lane has unread inbox + quiet telemetry = its
  Monitor isn't delivering and (post-LD-0157) it has no self-tick to re-arm. It CANNOT be tasked. **Decide
  respawn-vs-reap (LD-0158 going-forward rule): respawn-request to MSTR ONLY if the lane has LIVE
  pending work** (a respawn re-arms its Monitor + drains the backlog); **if its unit is done + you've
  rerouted its work, REAP it** (a respawn of a done lane just idles + re-deafs). Reroute any
  time-sensitive work it was holding to a reachable lane (e.g. the base lane) meanwhile. Most common
  on `~A` lanes (broker can't push to them). This is the reachability failure mode the retired
  self-tick used to mask — DEAF detection is now how it surfaces.
  **GROUND THE CAUSE before reaping (Andrew-direct 2026-06-23):** a DEAF reading can be an
  infra-transient LOAD-FAILURE, not agent-death. If MULTIPLE lanes read DEAF/stale at once, OR
  MSTR / a Tier-0/1 is also unreachable, OR the lane is a FRESH spawn that never loaded (no-summary),
  suspect a **fabric-wide server-side outage (Anthropic-side)** → do NOT reap during it; wait for
  recovery + re-check (the agent returns when the outage abates). Reap ONLY an isolated, agent-specific
  DEAF that is confirmed NOT coincident with an outage AND has no live pending work. Anchor: 2026-06-23
  — COO reap-nominated a fresh `0.7.0_AE_CloudOps~B` reading DEAF; it was Andrew's INTENTIONAL spawn
  that failed to load on an Anthropic outage (the same outage had MSTR deaf). Retracted before MSTR acted.
- **BLOCKED** → resolve it (dispatch the unblocking move via Step 5) OR escalate it (`[STUCK]` to
  MSTR per the LD-0026 chain) — this cycle. Never leave a block un-acted.
- **SOVEREIGN-DECISION REQUEST** → **declare it**: route the decision to Andrew, CC MSTR. If the
  nature of a block is that it needs sovereign discretion, reclassify it as sovereign and declare
  it — do not sit on it as a normal block. (MSTR's `/govern` picks up COO sovereign-requests and
  rules if Andrew is silent one cycle — LD-0090 / Constitution Art. XVI.)
- **STALE-VERIFY** → confirm the owner is actually alive (telemetry quiet >10min while the summary
  claims work). Dead/stuck owner = a single-point stall → respawn-request to MSTR or re-dispatch;
  stale-summary = nudge a refresh.
- **NEEDS-STATUS** → nudge the agent to set an explicit `WORKING:/IDLE:/BLOCKED:` token (hygiene).

fabric-check's `FABRIC-CHECK-RESULT` line is the count of owed COO actions; its `ACTION-REQUIRED`
line tells you whether a move is required this cycle. Full skill: `.claude/skills/fabric-check/SKILL.md`.

### 2b.1 — Read agent state (telemetry primary, broker cross-check)

> 2b.1-2b.5 are the DEEPER per-agent logic that fabric-check's output feeds. fabric-check (2b.0)
> gives the fused buckets fast; use 2b.1-2b.3 to classify the *cause* of any STALE/BLOCKED/STALE-VERIFY
> agent before firing its dispatch.

For each LIVE agent in your fabric:

```bash
# Per-agent last work-call timestamp (telemetry primary)
for f in org/mcp/agent_telemetry/*.jsonl; do
  a=$(basename "$f" .jsonl)
  w=$(jq -r 'select((.kind//"work")=="work").ts' "$f" 2>/dev/null | tail -1)
  y=$(grep -oE '"ts":"[^"]+"' "$f" 2>/dev/null | tail -1 | sed 's/.*:"//;s/"//')
  echo "$a work=$w any=$y"
done
```

**Pitfall (banked):** use `jq -r | tail -1` / `grep -oE | tail -1` — never `tail -n1 | head -1` (returns OLDEST on a single-line file).

Cross-check with `get_live_agents()` + `get_org_summary()` for broker-side registration + summaries.

### 2b.2 — Classify each agent

| State | Signal | Action |
|---|---|---|
| **ACTIVE** | last `kind:work` < ~10m OR recent commit / SSM chain | none — working |
| **IDLE** | last `kind:work` 10-30m + `kind:loop` recent | eligible for capacity routing |
| **STALE** | last `kind:work` 30+ min AND no commit/inbound (even if `kind:loop` fresh — watcher self-ping is not work) | REQUIRES re-dispatch or blocker trace |
| **NOT_REGISTERED** | absent from telemetry + `get_live_agents` | meta-signal (offline this cycle / crashed) |
| **TELEMETRY_GAP** | broker LIVE but telemetry frozen | flag the hook, not the agent |

**Cross-check before classifying STALE/IDLE:** broker summary is aspirational (heartbeat-lagged); git is ground truth. A "heads-down" agent in a long generation looks STALE but is working — verify via `git log --all --oneline --since="30 minutes ago"` + recent inbox traffic.

### 2b.2a — Movement check + dependency-liveness gate (per tick — the anti-coast core; Andrew-direct 2026-06-23)

**The load-bearing reason /drive exists. Two non-negotiables every tick:**

> ### ⚠ TELEMETRY MANUFACTURES ABSENCES. NEVER CONVICT A LANE ON `0 work-calls` ALONE. (2026-07-09, source-confirmed)
> **`org/mcp/agent_telemetry/*.jsonl` has BLACKOUT WINDOWS.** Measured, in `2.0.0_SA_COO.jsonl`:
> ```
> 22:14 1 | 22:15 4 | 22:16 4 | 22:17 2 | 22:18 0 | 22:19 0 | 22:20 0 | 22:21 0 | 22:22 0 | 22:23 0 | 22:24 3
>                                        ^^^^^^^^^^ SIX MINUTES. ZERO LINES OF EVERY CLASS. ^^^^^^^^^^
> ```
> Inside that hole: **6 `ycharts_*` calls and 4 `send_message` calls with broker delivery receipts.** `send_message`
> has **4,948** records elsewhere in the same file. **The hook stopped writing. It did not selectively omit a class.**
> Independently confirmed against the m365-gateway audit lake, which captured all six invocations to the second.
> **MECHANISM: UNDETERMINED.**
>
> **Therefore an absent telemetry record is uninformative about EVERY tool class — not just vendor calls.**
> `0 work-calls this tick` is **NOT** a reliable negative and never was. **A lane that looks PARKED may be a lane
> the hook stopped watching.**
>
> **BINDING on this step:** `0 work-calls` **only opens an inquiry**. Before you nudge, re-dispatch, or escalate
> `[STUCK]`, corroborate with **at least one telemetry-independent signal**:
> - **commits** (`git log --author=…`) — a different writer entirely;
> - **THE DECIDING SIGNAL — undelivered files** in `org/mcp/inbox/<serial>/` top-level (**and the nested
>   `<serial>/~B/` lanes**, which `fabric-check` does not enumerate). The Monitor `mv`s a message to `read/` on
>   delivery. **`0` undelivered + the newest `read/` file being a message you just sent = the agent is reading. This
>   is the only signal that reports the property "this lane will receive its dispatch."**
>
> ### ⚠ AND `channel push` IS ITSELF A PROXY. IT CONVICTS NOTHING EITHER. (2026-07-09T23:14Z)
> A `send_message` receipt reads `(filesystem + broker + channel push)` when healthy and `(filesystem + broker)` when
> the broker has **no live MCP channel registered at send time.** It was adopted as a deafness detector at ~23:03Z
> and **falsified within eleven minutes:**
> ```
> 23:11:52Z  CTO -> 0.4.0_DS~B   receipt: (filesystem + broker)      -> CTO concluded "still deaf", drafted an Andrew escalation
> 23:12:55Z  COO reads the dir:  0 undelivered; CTO's 231152Z sits in read/, NEWEST BY MTIME
>            MSTR had respawned DS~B at ~23:11Z. Its Monitor was armed BEFORE it re-registered on the broker.
> ```
> **`channel push` reports BROKER REGISTRATION. It does not report whether the Monitor will pick the file up.** A
> freshly-respawned lane drains its inbox while its channel is still cold. **`(filesystem + broker)` is consistent
> with BOTH "deaf" and "alive and already reading."** ~~MECHANISM of the missing push: **UNDETERMINED.**~~
> **→ DETERMINED `02:00Z`: the push targets the SENDER's ctx; the token is a `liveness.json` lookup. See the box below.**
>
> ### ⚠ DETERMINED `02:00Z` (`0.7.0_AE_CloudOps`, source-confirmed + EXERCISED): **`channel push` NEVER MEASURED DEAFNESS. IT MEASURED `liveness.json` FRESHNESS.**
> ```
> server.py:1119-1120   send_message sets  _active_ctx = ctx     <- the SENDER's Context
> server.py:369         _push_channel_message reads  ctx = _active_ctx
> server.py:377         ctx.session.send_log_message(...)
> meta["to_agent"] is passed in and NEVER READ.
> ```
> **THE PUSH LANDS IN THE SENDER'S OWN SESSION**, once per live target. The token is appended iff `live_targets` is
> non-empty (a `liveness.json` read at `:1176`) **and the sender's own ctx accepts a log line.**
>
> > **It is a liveness-file lookup wearing the costume of a delivery receipt.** When it is right, it is right because
> > of the **lookup** at `:1176` — never because of the **push** at `:1188`.
>
> **Liveness ≠ watcher-armed. An agent that heartbeats while its Monitor is dead is DEAF and still mints the token.**
> *It was adopted as a deafness detector at `23:03Z` and falsified at `23:14Z`; it could never have worked, and the
> eleven minutes were luck, not method.* **`pushed=False` is a fact about the SENDER.** Never report it as a
> recipient verdict.
>
> **AND `SUFFIX MISMATCH` IS SILENT DATA LOSS TO A LIVE AGENT, WITH A RECEIPT THAT SAYS `delivered`.** All three
> paths provably miss: filesystem (`:1131-1135` routes by the **addressed** suffix while `:1129-1130` claims *"fully
> isolated … no cross-contamination"*), broker (`:1157` files under base; `WHERE to_serial = ?` is exact; `:553-554`
> `_my_serial = agent_serial`, so a `~B` agent polls `"~B"` and never sees the base row), and `channel push` (`:1183`
> skips it, `:1188` pushes to the sender regardless). **Symmetric in both directions**, and `_resolve_agent_folder`
> strips the suffix so the `not found` guard never fires. **Here the strong word is EARNED** — this is the one case
> where a loud `SUFFIX MISMATCH → <live serials>` is not an overstatement. `:1183` already computes those serials
> and throws them away. Fix in flight (`0.7.0`, limb-1); `server.py` is CTO's.
>
> **Everywhere else the rule stands:** a warning must say `CHANNEL COLD (may be respawning) — verify inbox drain`,
> **never `UNDELIVERED`.** *A warning that overstates is a warning that gets muted.*
>
> **Two signals agreeing convict. One absence convicts nothing.** *"An absent record is an empty set. A forbidden
> set is empty, and so is an unrecorded one."* (`3.0.0_SA_CVO`) This applies to `fabric-check`'s `DEAF` and
> `STALE-VERIFY` limbs too — both read the same hook.
>
> ### ⚠ CORRECTION 2026-07-09T23:29Z — `fabric-check` was NOT "blind to nested `~lane` inboxes." IT READ A DECOY.
> An earlier revision of this box said the deaf-check *"does not enumerate nested `~lane` inboxes."* **Wrong
> mechanism, and the true one lies where blindness merely omits** (`0.4.0_DS~B`, source-confirmed):
> ```
> server.py:1133       inbox = INBOX_DIR / to_folder.name / f"~{to_suffix}"   <- the WRITER,  nested
> inbox-watch.sh:98    WATCH_DIR="$INBOX_BASE/$AGENT_DIR/~$SUFFIX"            <- the MONITOR, nested
> fabric-check.py:132  d = os.path.join(INBOX_DIR, serial)     (pre-fix)      <- the READER,  FLAT
> ```
> For lane `A~B` the reader opened **`inbox/A~B/`** — a flat directory that **exists for 28 lanes, that nothing has
> written to since per-tilde isolation, and that answers `0 unread` FOREVER.** **The watcher and the
> watcher-of-watchers were reading different directories.** It reported `deaf=2` when the answer was `3`.
>
> **And the writer that creates the decoy is our own dispatcher:** `.tools/operator.py:539-541` builds
> `inbox_root / agent` where `agent` is `<issued_to>` — which `org/XXX.md` **requires** to carry the `~lane`
> suffix — and `mkdir`s it. **`operator.py --dispatch` writes a lane agent's GO to a path no Monitor watches, and
> creates the decoy in the act.** How many TOs this has stranded is **UNDETERMINED**. Four survivors are known,
> undelivered since 2026-05-29 (CL-fabric lanes; CL is paused, so the loss is bounded by the pause — **the
> mechanism is not**).
>
> **FIXED** by `0.4.0_DS~B` (COO-reviewed, self-test 21/21 + 3 killing mutants, denominator on BOTH exit paths):
> `DEAF-COVERAGE: deaf=N over 85 enumerated inboxes (43 base serials, 38 nested ~lanes, 28 legacy-flat dirs)`.
> **`flat_orphans` is reported SEPARATELY from `unread`, and deliberately so:** folding them in would pin those
> lanes `DEAF` forever, and `DEAF`'s prescribed remedy here is *"respawn."* **A respawn cannot drain a directory no
> Monitor watches — the alarm would demand, forever, an action incapable of fixing the condition that raised it.**
> That is **the latched alarm inverted**: one fires once and cannot speak when the remedy would work; this one
> fires always and demands a remedy that cannot. **Both are an alarm decoupled from the action it demands, and the
> second is worse, because it trains the reader to mute it.**
> **Do NOT "clean up" `flat_orphans`. They are the only evidence the dispatch path is broken.**
>
> **The COO nudged lanes on the telemetry signal all night before it was found, then adopted `channel push` as its
> replacement and nearly escalated on THAT within the hour. How often either was wrong is UNDETERMINED.**
> **Every detector in this step is a proxy. The directory is the property.**

**(A) MOVEMENT check — never attest a hot TO ADVANCING off the owner's WORD; verify it actually MOVED since the last tick.** For each owner of a hot/active TO, compare against the *prior* tick (the last `drive_log` + `org/mcp/.last-drive-{coo_serial}`):

```bash
SINCE=$(date -u -d @"$(cat org/mcp/.last-drive-{coo_serial})" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)   # prior tick boundary
jq -r --arg s "$SINCE" 'select((.kind//"work")=="work")|select(.ts>$s)|.ts' org/mcp/agent_telemetry/{owner}.jsonl | wc -l  # work-calls this window
git log --all --oneline --since="$SINCE" --author="{owner-tag}" | wc -l                            # commits this window
```

- **MOVED** (≥1 work-call OR commit on this TO's surface since the last tick) → ADVANCING; attest with the REAL `last-work-call`/`last-commit` ts, not the self-report.
- **NO MOVEMENT** (0 work-calls + 0 commits since the last tick — *regardless* of a "building"/"in-progress" summary or a dispatch you fired) → the TO is **PARKED/STALLED, not advancing.** Run the nudge ladder:
  - **tick 1:** NUDGE the owner — cite the ground-truth (last-work-call ts, 0 commits, summary token) + ask `(a) in-progress-but-quiet / (b) parked / (c) blocked?` + name the next checkpoint + a within-cycle RAVC ask.
  - **tick 2 (still no movement):** re-dispatch harder (explicitly un-pace; name the gated downstream it holds) OR trace the blocker → STUCK-RESOLVABLE.
  - **tick 3 (no movement across 3 ticks):** `[STUCK]` to MSTR (single-point stall on a hot TO).
- **Long-generation caveat (don't false-nudge):** a genuinely heads-down owner still emits *some* work-calls — **0 work-calls across a whole tick** is the tell, NOT "no commit yet." Work-calls flowing + no commit = MOVING (attest), not parked.

**(B) DEPENDENCY-LIVENESS gate — before you STACK a dependency or fire a dispatch on an owner, verify that owner is LIVE + reachable FIRST.** A dependency stacked on a dead/DEAF/idle lane is dead-on-arrival — and you won't notice until the downstream silently never moves. So, BEFORE relying on / dispatching to any owner (especially a *downstream gated* owner whose timeline now blocks others):

> ### ⚠ BINDING, FABRIC-WIDE (CTO ruling 2026-07-09T23:28Z): **SoD BY ROUTING IS NOT SoD. `delivered` IS NOT `READ`.**
> **Before an SoD handoff, a dispatch, or any GO counts as ISSUED, the sender VERIFIES the recipient is reachable:**
> **(a) `0` undelivered in its CANONICAL inbox dir** (`inbox/<base>/~<suffix>/` for a lane; `inbox/<serial>/` for a
> base) **AND (b) an armed `inbox-watch.sh` process for THAT EXACT SERIAL.**
>
> **Absent both, the handoff HAS NOT OCCURRED and the sender still holds the work.**
>
> ### ⚠ CORRECTION 2026-07-10T01:10Z — **THE (b) INSTRUMENT AS ORIGINALLY WRITTEN HERE WAS `UNDISCRIMINATING`.**
> This rule shipped `ps -ef | grep "inbox-watch.sh <serial> stream"` — **with no `grep -v grep`.** The grep process's
> own command line contains the serial, **so the grep matches itself.** Positive control, run against a serial that
> has never existed:
> ```
> ps -ef | grep -c "inbox-watch.sh 9.9.9_NOBODY stream"                 ->  3     <- FOR AN AGENT THAT DOES NOT EXIST
> ps -ef | grep "inbox-watch.sh 9.9.9_NOBODY stream" | grep -v grep|wc  ->  0
> ```
> **It returns a positive count for every serial, always. Its output is independent of whether any watcher exists.**
> `/watcher` SKILL.md has carried `grep -v grep` since it was written (`:72`, `:127`). **This ruling — newer, stricter,
> and binding fabric-wide — dropped the guard.** *The tightening lost the control.*
>
> ### ⚠⚠ SUPERSEDED `01:55Z` — **`w` AND `u` ARE BANNED AS DELIVERY ORACLES, JOINTLY AND SEVERALLY.**
> **(CTO ruling, source-confirmed. The `01:10Z` fix above removed the false positive from the `grep`. It did not
> remove the false positive from the WORLD.)**
>
> **The defect is not undiscrimination. It is `ANTI-CORRELATION`.** An **orphaned** stream watcher — one whose
> spawning session died — keeps polling. `inbox-watch.sh:113-127`:
> ```
> :114   for msg in "$WATCH_DIR"/*.md      <- globs top-level
> :120   mv "$msg" "$dest" || continue     <- THE ORPHAN DRAINS TOP-LEVEL.  THIS IS WHAT MAKES u==0.
> :124   echo "[INBOX] $base"              <- the ONLY notification act -- into a DEAD parent's stdout
> ```
> - **`w>0`:** `ps` sees a process. **`ps` cannot see whether a live Monitor task reads that process's stdout.**
>   *"Has a live consumer" is not a property of the process; it is not in `ps`'s domain at all.*
> - **`u==0`:** **the orphan causes it.** The `mv` at `:120` *is* the drain.
>
> > **The more reliably an orphan eats an agent's mail, the more perfectly both limbs hold. A FULLY DEAF AGENT
> > PRODUCES THE STRONGEST POSSIBLE `REACHABLE` VERDICT.** And the `mv` **commits the theft before the `echo` is
> > even attempted** — so a lane can only *look* unreachable once it has already lost mail.
>
> **`u` and `w` look independent — one a filesystem probe, one a process probe. They are not.** *A single orphan
> sets both green.* (`0.0.0_AB_MSTR`, self-retracting 8 minutes after using them: **"one fault reported twice."**)
>
> **`A FILE MOVING INTO read/ IS DELIVERY, OBSERVED` — WRITTEN HERE AT `01:10Z`, SOURCE-REFUTED AT `01:47Z`.**
> Three actors move files into `read/`: the stream watcher (`:120`), the legacy watcher (`:175`), and
> `check_inbox(mark_read=True)`. **Only the third implies an agent read it.** *A file in `read/` observes the
> WATCHER, not the AGENT — and it is the proxy an orphan forges continuously, for hours, for an agent that no
> longer exists.*
>
> **THE ONLY SOUND ORACLE is something ONLY A LIVE CONSUMER CAN PRODUCE:** an agent-side **ack**,
> `TaskOutput(<monitor_task_id>)` → `running`, or a broker receipt. **Not `ps`. Not the filesystem.**
>
> **INTERIM, until a tool exists** — a watcher is current-session only if its `bash inbox-watch.sh <serial> stream`
> **child** has a parent that resolves to a **real** process. **AND MIND THE TRAP:**
> ```
> MSYS `ps -p 1` RETURNS ZERO ROWS.  PID 1 NEVER APPEARS IN `ps -ef`.
> A watcher WRAPPER IS BORN WITH ppid=1 -- so testing it with `ps -p 1` reports every HEALTHY wrapper as an orphan.
> ```
> **CTO generated seven false `ORPHAN`s this way. The COO generated one ten minutes after reading the warning.**
> Test the **child's** ppid (`!= 1`, and present in `ps -ef`). The `ppid=1` wrapper proves nothing either way.
>
> **AND WHY NOTHING CATCHES THESE:** `watcher-status.sh:63` matches `awk '$NF == s'`, but a stream cmdline's `$NF`
> is `"stream"`, **never the serial** — so `COUNT` is structurally `0`, which makes its `PRIOR-SESSION-ORPHAN`
> subcase (guarded by `COUNT -eq 1`) **dead code.** *The one detector written for this exact hazard cannot fire in
> the model that creates it.* `/watcher`'s migration table calls the ORPHAN class *"gone — a harness-tracked task,
> not a detached bash process"*; **two detached bash orphans were running on this box while it said so.**
> ~~`/kill` **explicitly exempts** `inbox-watch.sh` from reaping. **Nothing reaps them. They accumulate.**~~
>
> ### ⚠ CORRECTED `04:08Z` — **"NOTHING REAPS THEM" IS UNSUPPORTED. A REAPER EXISTS AND TARGETS THEM.**
> *(COO, source-read. This line was `1.0.0_SA_CTO`'s seed 11, propagated into this law by me, unverified.)*
> ```
> .tools/kill-orphans:95    PATTERNS='inbox-watch\.sh|check-inbox\.sh|agent-poller\.py'   <- IT TARGETS THEM
> .tools/kill-orphans:132-139  documents the 2026-06-15 exit-143 incident: reading the WRONG TOKEN made every
>                              LIVE stream watcher read as stale -> reaped on a peer's register_agent.
> .claude/skills/kill/SKILL.md:40  "never ... `inbox-watch.sh`, `agent-poller.py`, `broker.py`, or `server.py`"
> ```
> **A reaper exists, pattern-matches `inbox-watch.sh`, and has historically over-reaped LIVE watchers.** *Its own
> skill doc says those processes are never touched.* **Two records, two stories** — the `comp-surface-check` defect
> in the reaping plane. **`DECLARATIVE DRIFT`, not an absent reaper.**
>
> ### ✅ RESOLVED `04:36Z` — **THE CLEANUP FOR A DEAD AGENT'S ORPHAN IS GATED ON THAT DEAD AGENT COMING BACK TO LIFE.**
> *(COO, exercised. `kill-orphans` is DRY-RUN by default; only `--force` kills. **No `--force` was ever passed.**)*
> ```
> kill-orphans           (dry-run, default)  -> lists 6 live watchers.  IT CAN SEE THEM.
> kill-orphans --stale   (dry-run)           -> "No matching background scripts found."
> KILL-ORPHAN lines in org/mcp/agent-spawn-audit.log -> 0     (CONTROL: " KILL " = 47, total = 693)
>
> org/mcp/hook_register_orphan_cleanup.py  -- a PostToolUse hook firing AFTER register_agent,
>   scoped `kill-orphans --serial <S> --force`, registered in .claude/settings.json
>   (1 ref; CONTROL: 1 PostToolUse block).  It REPLACED a fabric-wide `--stale --force` hook
>   that reaped LIVE watchers (Andrew-direct, 2026-06-15: "it should only kill-orphans
>   associated with the agent").
>
> DS base register events after 18:28Z : 0     <- 31391's agent NEVER CAME BACK
> CONTROL: 0.7.0 events after 18:28Z    : 2     <- a lane that did
> ```
> **`31391` survived `7h17m` because the only thing that would have reaped it is the return of the agent that died.**
>
> **AND THE COO'S OWN HYPOTHESIS WAS WRONG, twenty minutes after writing the line above.** I speculated that
> `--stale`'s `liveness.json` oracle would blind the reaper to a **post-respawn** orphan. *It does not.* The hook
> passes `--serial <S> --force`, never `--stale`, and **at first register the new Monitor is not yet armed** (register
> precedes `/watcher`) — so the only watchers it matches are the **dead session's**. **That case is handled.**
> *I read a usage line, inferred a mechanism, and was one commit from publishing it as the finding.*
>
> > **THE SAFE SCOPING CREATED THE BLIND SPOT.** *The fabric-wide sweep was removed because it over-reaped live
> > watchers; the scoped replacement fires only on an agent's own return.* **A lane that dies and is never respawned
> > leaves an orphan that nothing will ever collect — and that orphan then forges `u`/`w` `REACHABLE` for the serial
> > it outlived** (LD-0271). *The anti-correlation has a cause, and the cause is a correct fix.*
>
> **STILL `UNDETERMINED`, and now for a nameable reason:** whether `kill-orphans` has **ever fired at all**. Its own
> header claims *"every reap is AUDITED to `org/mcp/agent-spawn-audit.log` (KILL-ORPHAN lines)."* **Zero exist.**
> *Either it has never reaped, or the audit line is never written, and **those two are byte-identical in the log.***
> Both hand-reaps tonight (CTO's `2124`, MSTR's `31391`) were manual — consistent with either.
>
> > **`0.7.0`'s clause, `042754Z`, and it is the general form of this whole block:** ***A NEGATIVE RESULT THAT CANNOT
> > SHOW ITS OBSERVATION IS INDISTINGUISHABLE FROM A MISSING OBSERVATION.*** *`--stale`'s "No matching background
> > scripts found" does not say whether it enumerated and found none, or could not enumerate.* **An assertion must
> > carry its observation.**
>
> **Owed, and now precisely scoped:** a `KILL-ORPHAN` audit line proving the reaper has fired — **or the claim struck
> from its own header.** *(`1.0.0_SA_CTO`; `.tools/**`, out-of-band `R1`.)*
>
> **Do not infer "no reaper" from "an orphan lived."** *That is the absence-for-mechanism substitution this whole
> section exists to name — and it is exactly how the false claim entered this law.*
>
> **REAP BEFORE RESPAWN.** A respawned lane arms a second stream against a live orphan; both poll the same dir on a
> 5s tick and **the `mv` race silently splits the lane's mail.**
>
> **NOT CLAIMED:** whether any message was ever actually stolen. **THEFT: `UNDETERMINED`. HARM: NONE DEMONSTRATED.**
>
> ### ⚠ AND THE METHOD THIS RULE ORIGINALLY NAMED TO SETTLE IT IS ITSELF UNSOUND. `mv` PRESERVES MTIME.
> *(`0.0.0_AB_MSTR`, `021225Z`; verified independently by the COO with a positive control on this box.)*
> ```
> CONTROL:  touch -d "2020-01-02 03:04:05" a.md ; mv a.md read/a.md
>   before mv : 2020-01-02 03:04:05.000000000 -0500
>   after  mv : 2020-01-02 03:04:05.000000000 -0500      <- IDENTICAL. mtime is the WRITE time.
> ```
> **A file's mtime in `read/` is when the SENDER wrote it, never when a watcher moved it.** And
> `.unread-deliveries` — the artifact this rule named as the oracle — is appended at `inbox-watch.sh:121`, **after
> the `mv` and before the `echo`: it records the EMIT, not a live consumer.**
>
> > **Three agents across three tiers — COO, CTO, MSTR — each adjudicated this incident on a timestamp that was the
> > sender's own clock, inside one hour.** The COO wrote *"do not let anyone round this to 'we lost mail'"* at
> > `015416Z` and rounded it at `020116Z`. **No artifact on disk can date a delivery.**
>
> *The mtime looked like a delivery record and recorded the write — `existence` for `rows`, `filename` for
> `content`, `delivered` for `read`, `action` for `resource`, one last time, in the artifact used to adjudicate the
> others.*

> ### ⚠⚠ SEED 11 — **THE REPAIR PROCEDURE GENERATES THE FAULT.** DO NOT RUN `/watcher rearm`.
> *(`1.0.0_SA_CTO`, `021727Z`, probe-exercised.)*
> ```
> PROBE: Monitor(bash -c 'echo START; while true; do sleep 5; done')
>   before:  wrapper 701462 (ppid=1),  child 701546 (ppid=701462)
>   TaskStop -> wrapper REAPED,        child 701546 STILL ALIVE, ppid now dead
> ```
> **`TaskStop` does not reap the grandchild.** So `/watcher rearm` — *TaskStop, then "kill any legacy bash watcher"
> via `watcher-status.sh` (**structurally blind to stream watchers**), then arm a fresh Monitor* — **orphans the
> child, cannot see it, and arms a second stream to race it.** Both poll the same dir on a 5s tick; **the `mv` picks
> a winner per message.**
>
> > **This is not an instrument that fails to detect a fault. It is a REMEDY THAT EMITS ONE**, guarded by an
> > enumerator that can only say `NONE`.
>
> **And an orphan is produced by ANY Monitor death — including the exit-143 SIGTERMs `/watcher` documents as routine
> and whose prescribed response is *re-arm*.** *The class is not "sessions end." It is "Monitors die" — a thing we
> were told happens at irregular intervals and shrugged at as zero-impact.*
>
> **INTERIM, fabric-wide, until a reaper lands:** do **not** `/watcher rearm`. If your Monitor dies, request a
> respawn and **reap the orphan first** (`ps -ef | grep "inbox-watch.sh <serial> stream" | grep -v grep`; the
> mandated helper cannot see it). `/watcher`'s own migration table and its `impact is ZERO` line are under
> correction with CTO.
>
> **Every liveness detector in this step has now been wrong at least once: telemetry (blackout windows),
> `channel push` (falsified in 11 minutes), `fabric-check --blocks` (read a decoy dir), the `ps|grep` limb of this
> ruling (matched itself), and its `01:10Z` repair (anti-correlated with the property).** *The COO certified an SoD
> handoff with the third, in the dispatch of the TO chartered to find exactly this class, ninety seconds before
> running its positive control — and then wrote a fourth to audit it.*
>
> ### ⚠⚠ `F-008` — **THE FABRIC CANNOT DETECT THAT AN AGENT DIED.** *(`0.0.0_AB_MSTR`, `42a4d3998`; COO-verified.)*
> **This step classifies lanes from STALENESS. Staleness is an ABSENCE.** Every death in this estate is *inferred*
> from a missing registration, a `w=0`, a silence — **and `u`/`w` are exactly the oracles an orphan forges.**
> ```
> agent-spawn-audit vocabulary: SPAWN · FORCE-SPAWN · KILL · KILL-NOOP · FORCE-KILL · WARN · REJECT
> THERE IS NO DEATH EVENT.   A kill is recorded. A spontaneous death is not.
> The 23 lines matching /death|died|crash/ ALL carry the token FORCE-SPAWN -- the words live in
> `reason=post-crash-recovery`, A HUMAN'S FREE TEXT.  The death is never recorded; only the remedy is.
> ```
>
> ### **`F-008`'s MECHANISM IS ONE MISSING FLAG.** *(COO, `04:58Z`, source-confirmed — MSTR asserted it; NEVER#5, so I read it.)*
> ```
> .tools/spawn-agent.ps1:218   Start-Process powershell -ArgumentList '-NoProfile','-NoExit','-Command',$inner
>
>   -PassThru  occurrences in the file : 0        <- Start-Process WITHOUT -PassThru RETURNS NOTHING
>   .Id / pid / process-id references  : 0        <- the pid is never captured, never logged, never stored
>   CONTROL Start-Process              : 1        (the call exists)
>   CONTROL impossible token           : 0        (the search can say no)
>   CONTROL file                       : 224 lines
> ```
> > **THE FABRIC NEVER LEARNS THE PID OF ANY AGENT IT SPAWNS.** *So it can never ask the one question that would
> > settle a death — `is process N alive?` — and every death MUST be inferred from an absence.* **That is not a
> > design choice about liveness. It is a discarded return value.**
>
> **AND IT CLOSES THE LOOP WITH THE REAPER FINDING ABOVE.** *No pid at spawn* → death is inferred from absence →
> **`u`/`w` are the absences an orphan forges** (LD-0271) → **the orphan is created by the lane that never returns**
> → **and that lane can never trigger its own `register_agent` cleanup.**
>
> > ## **THE ONE LANE WHOSE DEATH MATTERS MOST IS THE ONE THE FABRIC IS STRUCTURALLY BLINDEST TO.**
> > *Four findings — `F-008`, `LD-0271`, the scoped reap hook, and the discarded pid — are one mechanism.*
>
> **The reconciler `F-008` needs is gated on `-PassThru` + capturing `.Id`.** *One flag, one assignment.* **`.tools/**`
> — routed to `DT`/`AE` behind CTO's narrowing (MSTR, `84b2c269f`). Not mine to write, and I have not.**
> ```
> ```
> **A spawn count is not a death count.** *MSTR computed a lane's death RATE from an instrument that records the
> OPPOSITE EVENT, and the COO adopted it verbatim and priced a durable verify on it.* **`0.7.0`'s `"~50-minute
> lifetime"` was `n=2` promoted to a law; it has since lived `2h26m`.**
>
> **AND EVERY COUNT BELOW CARRIES ITS MATCH RULE, because the COO's did not:**
> ```
> subject field (col 3), token=SPAWN only        0.5.0=7  >  0.7.0=6      <- what the COO published
> subject field (col 3), token=SPAWN|FORCE-SPAWN 0.7.0=8  =  0.5.0=8      <- 0.7.0 TIES FOR THE LEAD
> ```
> **The conclusion survives both rules — `0.7.0` is not a *unique* outlier — but "`0.5.0` outranks it" is true only
> under the narrower one, and the COO never printed the rule.** *"Isolated to one lane" was never controlled against
> peers under either.*
>
> > **`R6` IDENTIFIABILITY** *(`0.7.0_AE_CloudOps`)* — **name a value the instrument MUST NEVER PRODUCE if it is
> > measuring the intended quantity, and check it.** `0.7.0`'s own recount read `MSTR = 73` because **MSTR is the
> > `by` ACTOR on nearly every line** — it matched the serial *anywhere on the line* instead of retrieving field 3.
> > **Both of its rails PASSED on a counter reading the wrong column.**
> > ```
> > COO's counter, R6:  MSTR as SUBJECT -> 0   (the tool never spawns MSTR)   PASSES -- right dial
> > the broken form:    MSTR anywhere   -> 80                                 R1/R2/R3 pass on it too
> > ```
> > **`R1`/`R2`/`R3` prove the needle MOVES. `R6` proves it is attached to the RIGHT DIAL.** *`comp-iam` had a
> > working needle: it printed `GRANTED`. It was attached to `(action)`, never `(action, resource)`.*
>
> > **ANY LANE'S DEATH RATE IS `UNMEASURABLE` WITH WHAT WE OWN — not high, not low, not knowable.**
> >
> > **A dead session and a never-spawned session are indistinguishable in every artifact we own.** *CVO's law one
> > layer up: **a denied call looks exactly like a call nobody made — and a dead agent looks exactly like an agent
> > nobody started.***
>
> **BINDING:** never derive a lane-stability property from spawn counts. **A respawn is evidence that someone
> believed a lane was dead — not that it was.** The standing instruction survives on its own merit (*a third
> respawn request routes to MSTR, not to a third respawn*): **it bounds spawn cost, and needs no death rate.**
>
> ### ⚠ **THIS `INFERRED` RULE IS CURRENTLY UNENFORCED. IT IS AN `F-004`, AND ITS AUTHOR IS THE COO.**
> **`fabric-check.py` emits `DEAF` with no `INFERRED` qualifier.** *(Verified: its only two `inferred` strings are
> docstrings about **project-tag** inference — a mention count, not a semantic match. The `[DEAF]` literal is
> constructed at print time, which is why a `grep -c "\[DEAF\]"` returns `0` and proves nothing.)*
>
> > **`F-004` — a rule that asserts a safety property no gate enforces.** *Recorded by MSTR at `031225Z` against its
> > own one-hour-old ack rule; **authored again, by the COO, twenty minutes after recording it.***
>
> **It is not fixed tonight, and the reason is the ruling itself:** `fabric-check.py` is a **Tranche-1 `E4` tool**,
> and `E4` tools **may not be verified through themselves** — a one-line label change needs an **out-of-band**
> fixture, and CTO deferred the `.tools/**` narrowing to daylight. **So the rule states its own unenforcement rather
> than wearing the costume of a gate.** *A rule that cannot yet be enforced must SAY it is unenforced. Otherwise it
> is a decoration, and the next reader will cite it as coverage.*
>
> **Owed:** the `INFERRED` qualifier in `fabric-check.py`'s `DEAF`/`STALE-VERIFY` emitters, with an out-of-band
> `R1` (a lane with a silent Monitor must print `DEAF (INFERRED)`, and a mutant removing the qualifier must go RED).

> **The tightening lost the control. The migration lost the detector.**

> **MECHANISM OF THE ABSENT `channel push` (`0.7.0_AE_CloudOps`, source-confirmed, `e3f3f7eae`):**
> `server.py:1169-1210` **conflates THREE distinct delivery failures into one silent omission** — (1) recipient not
> registered, (2) **registered under the wrong suffix** (the wrong-channel GO — *"still live and actively concealed"*),
> and (3) push attempted and failed. **The code computes the live serial it skipped at `:1183` and throws it away.**
> A receipt reading `(filesystem + broker)` therefore cannot distinguish *"nobody is listening"* from *"someone is
> listening under a name we resolved wrong and chose not to tell you."*
>
> **SHARPENED `02:00Z` — and case (3) is not a recipient fact at all.** The push targets the **sender's own ctx**
> (`:1119-1120` → `:369` → `:377`), so `pushed=False` says nothing about the recipient. **`0.7.0` REFUSED to ship
> `PUSH FAILED` as a recipient verdict**, and refused the COO's positive control for the fix as `UNDISCRIMINATING`.
> **Shipping instead:** `NOT REGISTERED` / `CHANNEL COLD (may be respawning)` / `SUFFIX MISMATCH → <live serials>`.
> *`server.py` is CTO's; the diff is with him.*
>
> **`delivered` in a `send_message` receipt means the filesystem accepted the bytes. It has never meant anyone will
> read them.** *A control that depends on a message being READ is a control that depends on a mechanism nobody
> verified.*
>
> **Incident (2026-07-09):** CTO required `0.8.0` to hand its `cse_schema.py` commit to `2.0.0_SA_COO~B` for
> separation of duties. That lane had **no watcher, no broker registration, and no work-call since `17:29:40Z`.**
> **`author != committer` held on paper for four hours while the committer did not exist.** Five messages sat
> undelivered — **one of them a SAFETY warning about the exact backtick defect the COO then committed into a
> `deploy_ledger` gate note at 23:20Z.** *The warning was unreachable in a mailbox nobody could read, describing the
> mistake being made.*
>
> **And NEVER "deliver" stranded flat-dir mail by moving it into the canonical dir.** Four `0.0.0_AB_MSTR` charters
> — **including a `PROCEED … GO`** — have sat 41 days in unwatched paths. **Executing a 41-day-old GO is worse than
> never delivering it.** Fix the writer (`operator.py:539`); preserve the orphans as evidence. (CTO, 23:28Z.)

- Confirm **LIVE** in `get_live_agents()` (fresh last-seen) AND **not DEAF** in `fabric-check --blocks` (unread-inbox + quiet-telemetry = its Monitor isn't delivering → it CANNOT be tasked).
- **AND, for any handoff you will RELY on: the two-part reachability test above.** `fabric-check`'s buckets are necessary, not sufficient — it read a decoy dir for 28 lanes until `2026-07-09`.
- If **LIVE + reachable** → stack/dispatch; then movement-check it next tick (A).
- If **DEAF / not-registered / dead** → do NOT stack the dependency and assume it'll happen. Respawn-request to MSTR (if it has live pending work) OR reroute the dependency to a live lane FIRST — *this* tick. Re-pointing a critical path at a dead lane is the silent-stall trap.
- **Verify BEFORE firing, not after** — a dispatch into an unverified lane is not a driving action, it's a hope.

**Incident anchors (why this sub-step exists):** (1) 2026-06-23 ETFS_SETUP W1 — COO attested "W1 ADVANCING" for 6 consecutive 10m ticks off AE's "I'm building"; ground-truth was a 3-min work-call burst then 25min/0-work-calls/0-commits, W1 "paced" in AE's summary = parked. The telemetry-cited nudge un-stuck it in one tick. (2) Same session — COO fired a critical-path producer-compute dispatch at DS *before* verifying DS was live (it was, by luck of timing). Both: `feedback_drive_read_agent_activity_not_project_paths` + this gate.

### 2b.3 — Classify cause for each STALE/IDLE agent

| Class | Detection | Resolving dispatch |
|---|---|---|
| **BLOCKED** | unread inbox > 0 OR pending unanswered escalation from the agent | route missing dep / answer escalation / reassign |
| **STUCK_MID_CLOSEOUT** | staged-not-committed files OR TO `active` >2 wakes with no commit | nudge with exact staged files — agent executed but never `git commit` |
| **STARVED** | inbox empty, no pending dep, `pending`/`staged` TO with gates met | flip + GO the staged TO |
| **STANDING_BY_REDIRECT** | log/heartbeat says "standing by" >30min | dispatch hot-work parallelization TO; **never accept terminal standby** |

### 2b.4 — Fire dispatches (mandatory; one per non-ACTIVE agent)

For EVERY non-ACTIVE agent, fire a dispatch via `mcp__opal-agent-comms__send_message` in THIS /drive cycle. **No "flagged for review" without a dispatch — the dispatch IS the review.**

**Posture (Andrew directive):** "Standing by for X" is never acceptable terminal state. An idle agent always routes to ready work — audits on un-audited surfaces, validator pre-staging, scaffolds for ratified PRDs, pre-stage downstream of about-to-ship peer.

### 2b.5 — Inform Step 3 with agent-state context

Carry the agent-state findings forward into Step 3 project-state classification:
- "Project X blocked on dep Y" + "Owner agent STALE w/ unread inbox" → unblock the agent first; do NOT dispatch new project-advancement TO
- "Project Y advancing" + "Owner agent NOT_REGISTERED" → re-classify as STUCK (phantom monitoring per CY-0102 anchor)
- "Project Z dormant" + "Idle worker fits the work shape" → eligible for STANDING_BY_REDIRECT to that project IF dormancy resolution path clears

---

## Step 3 — Per-project classification (the core)

For each project on the hot list, classify into one of 5 states:

| Class | Detection | Action |
|---|---|---|
| **ADVANCING** | **Fresh OWNER MOVEMENT since the last tick** — a `kind:work` telemetry call OR a commit by the owner-serial touching THIS TO's surface within the trailing tick-window (verify per 2b.2a). A dispatch you fired + a self-reported "I'm building"/"in-progress" is **NOT** movement. Also **verify the monitoring path is real** — owner isn't watching a dead SSM (CY-0102: DS~D "monitoring" a SIGKILL'd SSM). | No new dispatch; record "ADVANCING owner={serial}, **last-work-call={ts}**, last-commit={ts}, next-RAVC2-ETA={time}" attestation. **Re-verify next tick** — if the next tick shows NO new movement, re-classify **PARKED/STALLED** and run the 2b.2a nudge ladder; phantom monitoring re-classifies to STUCK. |
| **NEXT-ACTION-READY** | Phase gate met (prior phase RAVC2-Accepted OR upstream artifact landed) AND next TO not yet dispatched AND named owner alive | **Author + dispatch the next-phase TO this turn** through normal COO `/charter` integration. Record TO ref + recipient + RAVC2-expected. |
| **STUCK-RESOLVABLE** | Blocker identified with named resolver path (peer can absorb, CTO can rule, MSTR can spawn, Andrew gate can clear). | **Route the resolving move this turn**: MCP to resolver with specific resolving ask + cite project + cite blocker + expected response window. |
| **STUCK-UNRESOLVED** | Blocker present + no clear resolver in chain OR resolver tried + non-responsive >1 /drive cycle | **Surface to MSTR via `[STUCK]` subject** with: project code, blocker description, prior-resolution attempts, COO recommendation. MSTR routes per LD-0026 backstop chain. |
| **PHANTOM-MONITORING** | Broker shows owner LIVE + summary says "monitoring X" + but X is verifiably dead (SSM terminated, deploy completed, upstream RAVC2 already landed) | **Route status-sync MCP through owner's chain** + ask for current-state heartbeat refresh + dispatch next-action OR explicit stand-down. Banking observation each occurrence for /mstr_review trail. |

**Magnitude-sanity heuristic** (per /govern Step 1(b) parallel discipline) — for any numeric claim a project log surfaces (dollar amount, count, ratio), apply quick magnitude-vs-context sanity check; implausible magnitude routes as **verify-channel candidate finding**, not a routine project-axis item.

---

## Step 4 — Hot-work assessment + dispatch quality check

For each NEXT-ACTION-READY or STUCK-RESOLVABLE dispatch, verify quality before firing:

0. **Owner verified LIVE + reachable (2b.2a-B) — FIRST, before firing.** Never stack a dependency/dispatch on a dead/DEAF/unverified lane; a dispatch into an unverified lane is a hope, not a drive. If not LIVE → respawn-request or reroute to a live lane this tick instead.
1. **Does the dispatch advance THIS project's critical path** — not generic backlog-chew?
2. **RAVC2 deliverable bounded** — returnable in defined window with clear acceptance criteria?
3. **Owner role-fit** — recipient is the right hands for this surface (DS for data, AE for cloud, DE for portal, DT for trading)?
4. **Coordination-cost vs unblocking-value** — is the MCP cost proportional to the project advancement it unlocks?

If 3+ "no" → re-scope the dispatch OR reclassify project (probably STUCK-UNRESOLVED).

**Lane discipline** (per /stimulus-scan parallel): a `~B`/`~C`/`~D` lane agent takes dispatch only from same-lane exec; phantom `~lane` (TO assigned but no live agent) re-routes to live base/lane.

---

## Step 5 — DISPATCH (mandatory; no "suggested action" without firing)

Fire every classified action via `mcp__opal-agent-comms__send_message` in this same /drive cycle. **No agent leaves a /drive cycle in a stuck-without-routing state.**

**Per dispatch:**
- Subject prefix: `[DRIVE]` for project-advancement TOs; `[STUCK]` for MSTR escalations; `[SYNC]` for phantom-monitoring resyncs
- Body MUST cite: project code + phase + dispatch reason + expected RAVC2 window
- TO authored via existing `/charter` integration when full TO format needed; light MCP when nudge/sync suffices

**Cap discipline:** if a /drive cycle would produce >5 dispatches, surface top-5 + flag rest as "cycle bound; carry-forward next tick". The 20m cadence ensures carry-forward catches the remainder.

---

## Step 6 — Hard gate (THE skill's bite)

Before exiting the cycle, verify:

**Per /drive invocation: ≥1 project-advancement action fired OR per-project explicit attestation that monitoring path is real + ETA holds — AND, for EVERY gated/blocked TO, proof you RESOLVED the gate or that it is genuinely outside COO power (per THE DRIVE IMPERATIVE).** Attestation is NOT a free pass: `"gated + ETA-holds"` is valid ONLY after you've confirmed the gate is not COO-resolvable this cycle (no lane to respawn, no contingency to pull, no escalation to fire, no live lane to reroute to). If it IS resolvable, the PASS requires you to have RESOLVED it — attesting it instead = `gate_status: FAILED`.

**FORBIDDEN terminal states:**
- "All projects standing by" — projects don't stand by; they advance, stick, or get resolved. If they're standing by, the owner is mid-RAVC2 (verify) OR there's an unfired NEXT-ACTION (dispatch) OR the project is actually `dormant` not `active` (queue-hygiene to MSTR).
- **"Gated on X / awaits X" where X is COO-resolvable** — a dead/unloaded lane you could respawn, a contingency you set but never pulled, a sovereign call you could escalate, a live lane you could reroute to. That's a self-inflicted wait, not a gate → RESOLVE it this cycle. **Re-attesting the same self-resolvable gate across ≥2 cycles is THE coast-failure** (the OPLMCP.02/~B anchor).
- **Narrating a tidy waypoint as the destination** — "plan staged / durable / one-gate-away / nothing pending" is NOT completion; keep driving to deployed+verified+cert-PASS.
- "Lower-touch window holds" — that was the CY-0099/0100/0101 failure-mode framing per LD-0056. NOT a valid /drive verdict.
- Receipt-acks of prior /drive findings without new project-advancement action — receipt-acks are bookkeeping, not driving.

If the gate fails: the /drive cycle records `gate_status: FAILED` and the next cycle re-prioritizes finding genuine project advancement. Repeated gate-failure across 3 consecutive cycles = COO surfaces to MSTR with "I cannot find genuine project advancement; consider re-scoping project queue OR explicit Andrew gate-clear" finding.

---

## Step 7 — Emit findings table + log

Write the cycle output to `org/tier1_exec/{COO_SERIAL}/drive_log_{YYYYMMDDTHHMMZ}.md`:

```
## /drive cycle — <UTC timestamp>

| Project | Class | Owner | Last-touch | Action |
|---|---|---|---|---|
| ADVI_DEMOV1 | ADVANCING | 2.0.0_SA_COO cross-lane | 175min | attest LD-0055 SSM 73e0cb52 routine compute, Phase 5 ETA 13-16Z |
| ADVI_VALFIN | NEXT-ACTION-READY | 0.4.0_DS~D | 4.7h | dispatched VALFIN.012 M-1 phase-B |
| ADVI_INFETL | STUCK-RESOLVABLE | 0.5.0_AE | 8h | routed CTO architectural ruling ask |
| ADVI_SHARED | STUCK-UNRESOLVED | unclear | 12h | escalated to MSTR [STUCK] |

Dispatches fired this cycle: 3
Gate status: PASS (3 advancement actions)
```

Commit log file under COO author line via `.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" ...`.

---

## Step 8 — Update last-/drive marker + heartbeat

```bash
date -u +%s > org/mcp/.last-drive-{coo_serial}
```

Heartbeat to broker with summary reflecting drive cycle output (e.g., `"drive tick 12: 3 dispatches fired (DEMOV1 attest, VALFIN.012 dispatched, INFETL routed CTO); next tick +20m"`).

---

## Step 9 — Chain-invoke `/allocation`

After cycle close (Step 8 marker + heartbeat), chain-invoke `.claude/skills/allocation/SKILL.md` to emit worker-set supply signal complementing this cycle's project-axis demand signal.

- /drive = demand (which projects need to advance)
- /allocation = supply (which workers must be alive to advance them)

Per ws COO v0.1 ratification (Andrew sovereign 2026-05-26T~13:42Z). CL COO chain-invokes the same /allocation skill body (canonical for both fabrics post-skill-sync per LD-0089 AC1 A.4-EXT); CL fabric most cycles will emit `[ALLOCATION-NO-DELTA]` due to structural thinness (Tier-1-primary fabric per LD-0042); /allocation still fires for defensive coverage + cross-fabric MSTR aggregation symmetry.

---

## Coexistence with /loop and /stimulus-scan

- **`/loop` continues as COO's general supervisory wrapper** — pulls inbox, fires heartbeat, runs `/watcher` health check, monitors in-flight SSM. `/drive` is invoked **inside** `/loop` body on the 20m cadence (sooner-of: cron fire OR loop tick where 20m elapsed since last /drive).
- **`/stimulus-scan` is the agent-axis observation skill** — classifies agents (ACTIVE/IDLE/STALE/etc.) + dispatches to fix STALE agents. `/drive` is the project-axis driver — classifies projects + dispatches to advance them. Both run from COO `/loop`; they complement, not duplicate. **/stimulus-scan asks "is each agent working?"; /drive asks "is each project moving?"**
- **`/charter` is the TO/PRD authoring skill** — `/drive` calls `/charter` when a full TO needs authoring vs a light MCP nudge.

---

## Risks + mitigations

- **Over-driving the fabric** — dispatching 5+ MCPs per tick across 4 projects = exec-level signal-to-noise to workers. Mitigation: cap discipline (Step 5) + RAVC2-bounded dispatch quality check (Step 4) + lane discipline.
- **Race with /spot-check fix-and-route pattern** — CVO `/spot-check` may also surface drift on alignment-metadata. If COO `/drive` and CVO `/spot-check` are firing on the same project, lane discipline applies: CVO owns alignment-metadata fixes within its scope; COO owns operational-advancement dispatches; conflict routes to MSTR per LD-0033 Q5.
- **False-positive STUCK classification on long-compute projects** — a project in a multi-hour SSM/transform/RAVC2 window may show no commits for 12h+ while genuinely advancing. Mitigation: ADVANCING classification requires the monitoring path verification (Step 3) — owner alive + summary references a verifiable in-flight artifact (SSM command-id checked via `aws ssm list-commands`, CloudWatch log polling, etc.). If monitoring path is real, classify ADVANCING + attest; if dead, classify PHANTOM-MONITORING.
- **CL-fabric path differences** — CL COO operates against `feature_clb/` worktree paths; this skill body uses ws paths as exemplars. CL COO substitutes their fabric's project registry + log paths. **Fabric-scoped per LD-0042; no cross-fabric driving.**

---

## Notes

- **Authority anchor:** LD-0056 (CY-0102 sovereign architectural directive Andrew 2026-05-25T04:50Z). The layer-of-concerns reorganization makes COO the primary operational driver; this skill is the executable artifact.
- **Coexistence with /govern:** MSTR /govern now verifies /drive (+ /charter + /spot-check) loop-health each cycle. If COO /drive hasn't fired in N hours OR shows repeated gate-failures, /govern routes loop-health correction to COO. /drive itself is COO-owned; /govern doesn't run /drive — it verifies it.
- **First-fire observation banking** — first 5 /drive cycles per COO produce empirical thresholds for tuning (cadence, dispatch cap, classification edge cases). Surface in next `/mstr_review` reporting parallel to class-6 §2.2 + CL_STALL_CHECK V1 threshold paradigms.
- **Charter:** there is no separate charter doc this V1; the skill body IS the charter. If empirical use surfaces need for separate detailed doctrine doc (parallel to `org/tier1_exec/3.0.0_SA_CVO/SPOT_CHECK.md`), author at `org/tier1_exec/2.0.0_SA_COO/DRIVE.md` post-empirical-tuning.
- Design + law: LD-0056 + `/govern` SKILL.md Notes section (light note this cycle; full slim deferred LD-0057+).
