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

## PAIRED MODE — `/drive <scope>`: the ACTUATE half of a DRIVE PAIR (Andrew-ratified 2026-08-27)

**Contract + row schema: `org/ref/DRIVE_PAIR_PROTOCOL.md`. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260827_DRIVE_PAIR_SETUP.md`
(his word: engaging `/self-drive` on CTO means instituting `/drive` on COO tied to the SAME target).**

`/drive <scope>` armed as a pair-half differs from estate `/drive` in exactly four ways:

1. **SCOPE = the pair's register predicate**, re-resolved each tick exactly as the CTO half resolves
   it (never a pinned list). Step 2's hot-registry read FILTERS to it.
2. **THE OBLIGATION IS SCOPED — and an empty tick is LEGAL.** Each tick: (a) read the pair's verdict
   ledger since the cursor (`org/{tier}/{driver_base}/drive_pairs/<scope>/VERDICTS.jsonl`) and
   convert each unconsumed `unblocks` row into its dispatch (GO pairing, TO cut FROM DECOMP CELLS,
   re-seat ask via MSTR), writing the `consumed` field with the receipt; (b) run the drive imperative
   over measured in-scope blocks ONLY. **Empty ledger + no in-scope blocks = a legal no-op tick** —
   the deliberate, DESIGNED exception to the all-standing-by-is-failure gate, and the reason a paired
   `/drive` cannot break a hold on a timer (the @014de1937 class this skill's OFF-by-default exists
   to prevent). Outside a pair, nothing here changes: bare estate `/drive` keeps its standing rules
   and its standing OFF.
3. **CADENCE: the pair's offset** — this half ticks +15m after the CTO half (30m default each, off
   the :00/:30 fleet marks) so verdicts land before the sweep reads them.
4. **CARRIER + STOP: the SHARED clause** in the arming driver's XXX.md row (`paired_with:` names this
   half). This half arms on the SAME operator word as the CTO half, never separately; a struck clause
   read at tick-top stands this half down (final log, CronDelete, done). The cursor lives in this
   seat's own drive log; lost state re-derives from the ledger's `consumed` fields.

5. **NO SHARED MARKER — the cursor and the movement window are LOG-DERIVED, per lane (2026-08-27,
   CTO fix on COO~X's tick-2 finding @506d7744d9, MSTR-concurred).** A paired tick neither WRITES nor
   READS the base-keyed `org/mcp/.last-drive-<base>` marker: two lanes running paired drives (base +
   ~X, measured live) clobber one base-keyed file, and the failure direction is UNDER-REPORTED
   movement -> PARKED -> nudge ladder -> a false [STUCK] conviction manufactured on a timer. The
   movement window for 2b.2a classification derives from the seat's OWN latest drive log + the
   ledger's `consumed` timestamps — lane-scoped by construction, survives session loss. Estate
   (unpaired) `/drive` keeps its legacy marker untouched. Any [STUCK] escalation states its window's
   PROVENANCE (log-derived vs marker-derived); marker-derived windows are untrustworthy by
   measurement while two lanes are live.

**Everything else is unchanged /drive law:** resolve-don't-attest within scope, completing-worker
alive, Rule 27 (TOs from decomp cells only, seats via MSTR), identity gate, RAVC on every dispatch.

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

⛔ **`jq` IS NOT INSTALLED IN THIS SHELL (CLAUDE.md Rule 16 class) — use python. A `jq` call under `2>/dev/null` returns CLEAN EMPTY STDOUT, so the reads below would render "no active projects" / "no work rows" out of a missing binary.** → `DRIVE.md §2`

```bash
python -c "
import json,glob,os
n=0
for f in sorted(glob.glob('org/projects/*.json')):
    d=json.load(open(f,encoding='utf-8'))
    if d.get('status')!='active': continue
    n+=1; print('%s | %s' % (os.path.basename(f)[:-5], d.get('name') or d.get('title') or '?'))
print('DENOMINATOR: %d active of %d project files' % (n, len(glob.glob('org/projects/*.json'))))
"
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

**Counts `kind:work` rows SINCE THE LAST TICK — that count IS the movement check (2b.2a-A), so it must not be
faked by a broken read. `jq` is ABSENT here; python only. Prints its own denominator.**

```bash
python - <<'PY'
import json, pathlib, datetime
now = datetime.datetime.now(datetime.timezone.utc)
tick = int(open('org/mcp/.last-drive-2.0.0_SA_COO').read().strip() or 0)
rows = 0
for f in sorted(pathlib.Path('org/mcp/agent_telemetry').glob('*.jsonl')):
    last, since = None, 0
    for line in f.open(encoding='utf-8', errors='replace'):
        line = line.strip()
        if not line: continue
        try: r = json.loads(line)
        except Exception: continue
        rows += 1
        if r.get('kind') != 'work': continue
        last = r.get('ts')
        if r.get('ts_unix') and float(r['ts_unix']) >= tick: since += 1
    if not last: continue
    age = (now - datetime.datetime.fromisoformat(last.replace('Z','+00:00'))).total_seconds()/60
    if age < 240: print('%-38s last=%s age=%.1fm since_tick=%d' % (f.stem, last, age, since))
print('DENOMINATOR: %d telemetry rows scanned' % rows)
PY
```
⛔ **NEVER `2>/dev/null` this read, and never take `$?` after a pipe (it is the PIPE's rc).** Measured
2026-08-11: `jq … 2>/dev/null` printed nothing for all 13 agents and I read it as **telemetry dead
fabric-wide** — a false outage one step from convicting live lanes as PARKED. The truth was
`jq: command not found`, with **18,190 healthy work rows** and the newest 47 seconds old. The
non-parsing `tail -2` showed it instantly. **A silent-empty retrieval reads exactly like a quiet
fabric, and this instrument's empty answer is the input to a conviction.** → `DRIVE.md §4`

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

## Step 7 — Log (SUBSTANTIVE ticks only — Andrew-direct 2026-08-27 ~22:1xZ at the COO terminal, verbatim: "we do not need a committed log with every tick")

**A committed drive log is written ONLY on a SUBSTANTIVE tick:** ≥1 dispatch fired, a ledger row newly consumed, a classification CHANGED (a seat entering/leaving PARKED/STUCK, a project changing class), or a finding surfaced. **A quiet tick writes NO file** — marker + heartbeat only (Step 8), the `/log` no-delta precedent. Each substantive log's delta line covers the quiet ticks since the last one, so the record stays gapless without the noise files. Gate: a `[STUCK]` escalation or a PARKED conviction still requires a logged tick — convictions never rest on an unlogged window. → `DRIVE.md §5`

When a log IS written: `org/tier1_exec/2.0.0_SA_COO/drive_log_{YYYYMMDDTHHMMZ}.md` — findings table (Project | Class | Owner | Last-touch | Action), dispatch count, gate status. **Findings and incident detail go in the log — not into this skill.** Commit via `.tools/safe-commit.sh --author "2.0.0_SA_COO <2.0.0_SA_COO@opal.agent>" -F <msgfile> -- <paths>` (the message file by a NON-SHELL writer — `python -c` is a shell-parsed region, measured 2026-08-27).

**Paired-mode cursor note (composes with rule 5 @46f4a0563e):** with quiet ticks unlogged, the movement window derives from the LAST SUBSTANTIVE log + the ledger's consumed timestamps; a widened window over-includes movement, which errs toward ACTIVE — the safe direction. It can never manufacture a PARKED.

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
