---
name: mstr-spawn
description: Provision a new agent session by serial via spawn-agent.ps1: concurrency-cap pre-check, optional first-message direction, broker-registration verification, audited bypass for legitimate overflow. Invoked by 0.0.0_AB_MSTR or 2.0.0_SA_COO (base or ~lane). Sibling to /mstr-kill.
---

# /mstr-spawn — provision an agent session

The fabric's structural mechanism for **population creation**. The invocation
`/mstr-spawn {serial}` IS the per-instance authorization within skill body for
spawning a session; `/mstr-spawn {serial} --force "<reason>"` is the
charter-blanket authorization for the audited concurrency-cap overflow path
(parallel to /mstr-kill's blanket force-kill authorization).

**Invokers: `0.0.0_AB_MSTR` and `2.0.0_SA_COO`, each with or without a `~lane` suffix.**
Andrew-direct 2026-08-28 ~15:32Z at the `1.0.0_SA_CTO` terminal, VERBATIM: *"/mstr-spawn and
/mstr-kill should be a COO function in addition to 0.0.0_AB_MSTR, I think it is a natural fit for
them to handle these things directly rather than having to coordinate through another agent. MSTR
should just be online as a device/fabric infra manager as well as handling cross-device
cross-fabric comms and so on."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260828_1532Z_D2D3_RESUME_AND_SPAWN_KILL_TO_COO.md`.
The skill keeps its `mstr-` name so every existing citation still resolves; the name is a stable
id, not an ownership claim. **A COO seat spawns directly — it no longer files a spawn request with
MSTR.** MSTR retains the primitive for device/fabric infra work (respawn after a device reboot,
fleet relaunch, cross-fabric seats).

> **Spawn != dispatch** (Constitution Art. VI). This skill provisions the
> session. Direction still flows through Tier 1. A first-message hint via
> `--say "<text>"` is allowed for fast-orient (see SPAWN-WITH-DIRECTION
> canonical pattern, memory `feedback_spawn_with_direction_fast_orient_pattern`)
> but the substantive TO/charter authoring stays at Tier 1.

## When to invoke

- Andrew direct: `/mstr-spawn {full-agent-serial}` — symmetric to `/mstr-kill`; covers initial provisioning + respawn after kill.
- COO (`2.0.0_SA_COO` base or lane): seating a lane for a decomp cell / TO that has no live instance, a `/drive` or `/allocation` finding that a class is needed and no seat holds it, respawning a dead lane whose open TO is still live. The COO still authors the TO (spawn != dispatch); it now also provisions the seat that will hold it, in the same turn.
- MSTR autonomous: device/fabric infrastructure population action — respawn after a device reboot or fleet relaunch, cross-fabric / cross-device seats, `/mstr-review` scan findings (unaddressed work surface, wrong-mix swap, FORK-STALLED SPAWN-WITH-DIRECTION fallback per /govern Step 4 table) — LD-charter governs; ledger LD-NNNN before invocation per Stakes Matrix (spawn is S1 per spawn-agent.ps1 line 19).
- Never invoked by any seat outside `{0.0.0_AB_MSTR, 2.0.0_SA_COO}` (+ lanes). A CTO / Tier-2 / CVO seat that needs a session asks its COO (or MSTR for infra-class spawns).

---

## Step 0 — Parse + identity gate

Parse the argument:
- Must be a full agent serial matching `^[0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(~[A-Za-z0-9]+)?$`.
- Tilde-lane suffixes (`~B`/`~C`/`~D`) included as needed — they are distinct sessions from the base serial.
- Optional flags:
  - `--say "<text>"` → first-message hint appended to ajb invocation (SPAWN-WITH-DIRECTION pattern; max ~200 chars to keep CommandLine sane).
  - `--force "<reason>"` → audited concurrency-cap bypass; mandatory reason string.

**Identity gate:** confirm the caller serial is `0.0.0_AB_MSTR` or `2.0.0_SA_COO`, either with an optional `~lane` suffix — read `$env:OPAL_AGENT_SERIAL` (per-process) or the session serial file `org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial`; **never `.comp-graph/.agent_context`** (shared, last-writer-wins — not an identity source, `org/XXX.md` Step 1). Any other invoker halts here with an error. The caller serial is what `spawn-agent.ps1` writes into the audit line (`by <serial>`) and what the rate cap is keyed on.

## Step 1 — Pre-flight checks

Four checks before spawning. Each surfaces as a clean refuse-with-reason rather than an opaque script error.

> **1a and 1b BOTH read the fabric's own bookkeeping and are BOTH BLIND to an Andrew-launched session**
> (no `register_agent` call yet + no spawn marker, because spawn-agent.ps1 never launched it). Two signals
> agreeing from the same source of truth is ONE signal counted twice. **1pt (process truth) is therefore
> MANDATORY, never skippable** — it reads the OS, the only layer an Andrew-launched session cannot be
> absent from. Incident: LD-0303 (2026-07-16, MSTR spawned `0.2.0_DT` over Andrew's live terminal on a
> clean 1a+1b read). Caught-live validation: 2026-07-17 ~17:2xZ, the identical class recurred on
> `0.8.0_AE_CloudComp` (Andrew-launched ~1 min before a COO spawn request; 1b read 0 markers = "clear";
> 1pt found the live claude.exe) and the spawn was correctly REFUSED. Andrew-direct affirmation same hour:
> *"honestly this is a success in my opinion because you identified there was already an 0.8.0 live and
> did not spawn a redundant one."*

### 1pt — PROCESS TRUTH (mandatory, run FIRST — the only check independent of fabric bookkeeping)

```powershell
$rx = '"\s*([0-9]+\.[0-9]+\.[0-9]+_[A-Za-z]+_[A-Za-z0-9]+(?:~[A-Za-z0-9]+)?)'
$procs = @(Get-CimInstance Win32_Process -Filter "Name='claude.exe'")
$hits = @($procs | Where-Object { $_.CommandLine -match $rx -and $matches[1] -eq '{full-target-serial}' })
```

**EXTRACT the serial token, compare with `-eq` — never `-like "*serial*"`** (a base serial is a substring
of its own lanes; over-broad matching inflates NON-ZERO reads and poisons the positive control — LD-0303
§3 direction rule: a ZERO from this scan is trustworthy, a non-zero on a base serial must be judged
per-hit).

- `hits.Count > 0` → **REFUSE the spawn.** A live claude.exe carries the serial regardless of who launched
  it.
- `hits.Count > 0` with NO spawn marker → **ANDREW-LAUNCHED SESSION: REFUSE, and the session is
  presumptively RESERVED** (Andrew-ratified 2026-07-17, LD-0305). Andrew direct-spawns a session when he
  has a specific task for it (his verbatim: *"usually if I spawn an agent direct rather than having it go
  through you by way of COO, I usually have a specific task i want that agent to do and probably don't
  want them borrowed unless additional tasks are directly relevant to what I asked them to do"*).

  **DISPOSITION DEFAULT — do not redirect the requested work into the base session.** Instead:
    1. Read the session's own broadcasts (the record+broadcast law makes Andrew's tasking visible within
       minutes of launch) to judge DIRECT relevance.
    2. DIRECTLY RELEVANT means: the requested work is an INPUT to or DELIVERABLE OF what Andrew asked
       that session to do. Adjacent-topic, same-domain, or "it would be efficient" all FAIL the test.
    3. Fails the test — or no broadcast yet to judge from (unjudgeable defaults to reserved) → spawn a
       TILDE LANE for the fabric work; base session untouched.
    4. Passes the test → still surface to Andrew before merging work into his session; his silence
       ≥1 /govern cycle → the LD-0026 corroboration path, never a silent merge.
  **TIE-BREAK: when in doubt, LANE.** A lane is reversible (merging later is one message); a distracted
  sovereign session is not. Andrew overrides any of this with a word, either direction.
  Requester guidance (not a gate): a spawn request that names its intended task (COO 172203Z is the model
  — task + staged TO + gate + first-message plan) is what makes the relevance test judgeable in minutes.
- `hits.Count == 0` → proceed to 1a/1b (they still catch the just-spawned-window-not-yet-claude case and
  the concurrency census).

### 1a — Already-live check

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
```

If `LIVE` AND last seen < 120s → **a session already exists**. Default action: **refuse the spawn** (avoid double-provisioning the same serial; CommandLine marker scan would detect the second window as a v1-marker-collision risk). Surface to Andrew: "{serial} already LIVE at PID {pid}; spawn would create a duplicate. Kill first via `/mstr-kill {serial}` or pass `--force "intentional-duplicate"` if a duplicate is intended."

If `STALE` / `NOT_REGISTERED` / not found → safe to proceed.

### 1b — Marker scan (authoritative AMONG FABRIC-SPAWNED sessions — LD-0105, scope narrowed by LD-0303: blind to Andrew-launched sessions; 1pt is the overall authority)

```powershell
$selfPid = $PID
Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object {
    $_.ProcessId -ne $selfPid -and
    $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1: {serial}*"
  }
```

**This is the AUTHORITATIVE pre-spawn live-state check** per LD-0105 Andrew sovereign 2026-05-26T~22:00Z. Step 1a (broker `get_agent_status`) is supplementary; the broker `opal-agent-comms` has a **suffix-strip semantic** that returns base-serial state for tilde-lane queries — meaning `get_agent_status("0.1.0_DS_MarketIntelligence~D")` returns the base serial registration, NOT the tilde-lane registration. The marker scan above uses the FULL tilde-suffixed serial in its match pattern, so it disambiguates accurately.

Empirical anchor for the elevation: 2026-05-26T~21:38Z /allocation #12 BATCHED-2 spawn of DS 0.1.0~C + ~D — both ws COO `get_live_agents()` read AND MSTR Step 1a `get_agent_status` returned NOT REGISTERED for the tilde-lanes, but the lanes WERE alive from prior /allocation #10 batch (16:30Z) that Andrew countermanded "let it go." Visual collision surfaced 2026-05-26T~21:50Z.

**Mandatory refusal:** If marker scan returns count > 0 (post-`$PID` exclusion + tilde-suffix-sensitive match) → **refuse the spawn**. Surface to spawn-requester: "{full-tilde-suffixed-serial} already LIVE at PID {pid}; spawn refused per LD-0105 authoritative-marker-scan gate. Either redirect the proposed work to the existing LIVE agent OR pass `--force "intentional-duplicate <reason>"` if a genuine duplicate is needed (audited bypass per existing discipline)."

The audited `--force "intentional-duplicate <reason>"` bypass remains for rare cases (e.g., reverse-engineering a prior session crashed mid-init that left a zombie marker). Scanner-self false-positive protection per LD-0100 retained via `$PID` exclusion.

**Tilde-suffix-sensitivity discipline:** the `*# OPAL_SPAWN_MARKER_v1: {serial}*` pattern requires the FULL serial including any tilde-suffix verbatim. Passing the BASE serial when a tilde-lane is the proposed target will miss the disambiguation — always interpolate the full target serial into the pattern.

**Scanner-self false-positive (empirical 2026-05-26).** The `$_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1: {serial}*"` pattern matches the scanner's OWN PowerShell process because the search-pattern literal is embedded in the scanner's CommandLine. Without the `$_.ProcessId -ne $selfPid` exclusion above, every fresh-spawn pre-check returns count=1 (the scanner itself) → false-positive refuse. The `$PID` exclusion eliminates the self-hit. **Diagnostic fallback if a count still surfaces:** inspect each hit's `ProcessId` + `CreationDate` + `CommandLine` — a legitimate spawn-marker window is a long-lived `powershell.exe -NoProfile -NoExit -Command "$Host.UI.RawUI.WindowTitle = '{serial}'; ..."` whose command line ENDS with the marker; a one-shot scanner is short-lived + has the marker EMBEDDED IN ITS Where-Object filter argument. Sister-pattern to memory `feedback_b_lane_orders_only_from_b_agents` family of "structural-self vs other distinction" empirics.

### ⛔ 1d — TO-ENCUMBRANCE: is the lane already holding a DIFFERENT project's open TO?

**RUN THIS FOR ANY TIER-2 SPAWN. Every check above reads a PROCESS or a BROKER RECORD, and NONE of
them can see an open TO addressed to a lane.** A lane letter can be free on process truth, free of
markers, and NOT REGISTERED on the broker — and still be **encumbered by an open task order**, which
at a **TIER-2** seat is a **`ONE PROJECT PER TIER-2 SEAT INSTANCE` collision at seating time**
(Andrew-direct 2026-08-24 ~19:29Z, protecting THE SEAT'S CONTEXT; enforced by
`.tools/to-decomp-ref-lint.py`'s seating check).

> ⛔ **CITATION REPAIRED 2026-09-10 by `1.0.0_SA_CTO`.** This line previously read "a Rule 27
> one-project-per-instance collision". **CLAUDE.md Rule 27 never said that**, and the phrase had
> dropped the words **TIER-2** — the scope that is the entire point of the rule. A Tier-1 seat twice
> declined to seat a Tier-1 lane on the generalised version. **Whether the constraint should reach
> TIER 1 is ANDREW'S call and is not taken here**; this heading's own "FOR ANY TIER-2 SPAWN" is the
> scope that applies. The check below is unchanged and still worth running.

```bash
python .tools/to-check.py --all --assignee "{full-target-serial}"
```

- **0 open TOs** — the lane is genuinely free. Proceed.
- **Open TOs on the project you are about to seat** — fine, that is continuity.
- **Open TOs on a DIFFERENT project** — ⛔ **DO NOT SEAT.** Either pick another letter, or have the
  COO re-address the encumbering TO FIRST. Seating over it silently creates the exact violation.
- **`--all` IS LOAD-BEARING** (the default view scopes to PRDs <=14d old, so a stale-PRD project's
  open TO is invisible), and `--assignee` is a SUBSTRING match, so read the rows rather than the count.

⭐ **ALSO CHECK THE BASE SERIAL, NOT ONLY THE LANE.** A TO addressed to the bare base
(`0.4.0_DS_ClientPlatform`, no suffix) belongs to no lane and will collide with whichever instance
someone reads it onto.

*MEASURED 2026-08-27, and this step exists because the spawn that needed it was mine.* Seating three
Tier-2 lanes for D1/D4, I ran 1pt/1a/1b/1c, got a clean read on `0.4.0_DS_ClientPlatform~Z`, and
seated it on D1_CATVIEWS — **while it still held `ETFS_INGEST.TO-6`, addressed to it since 08-24.**
Two projects on one instance, created by a pre-flight that passed every check it had.
`2.0.0_SA_COO~Z` caught it in a seat-census minutes later and re-addressed TO-6 to `~P`.
**A LANE LETTER FREE ON PROCESS TRUTH CAN STILL BE ENCUMBERED BY AN OPEN TO.** The planes the
pre-flight reads answer *"is anyone running as this serial"*; Rule 27 asks *"does this serial already
OWE anything"* — a different question, and no process-plane instrument can answer it.

⛔⛔ **WIDENED SAME DAY, BECAUSE THE FIRST VERSION OF THIS STEP WAS TOO NARROW AND THE
NEXT MEMBER OF THE CLASS GOT THROUGH IT WITHIN THE HOUR.** 1d originally censused **open TOs only**.
It was written after a TO-encumbrance miss, scoped to the artifact class that had just caused the
miss — and **a `disarm_owner` is not a TO**, so it caught nothing when the same failure recurred on
a different artifact.

>> **THE GENERAL FORM: A RECORD KEYED ON A SERIAL GOES STALE THE MOMENT THAT SERIAL IS RE-SCOPED,
   RE-SEATED, OR CLOSED — AND NO GATE FIRES.** The record stays well-formed and confidently wrong:
   real serial, real field, reads as owned. Nothing errors. Only a census finds it. <<

**SO CENSUS EVERY SERIAL-KEYED OBLIGATION, NOT JUST TASK ORDERS**, before AND after a seating that
scopes a lane:

```bash
comp-find -i "{full-target-serial}" --all          # -i: this estate capitalises its load-bearing words
python .tools/to-check.py --all --assignee "{s}"   # open TOs
grep -rn "{s}" org/surprise_channel/               # disarm_owner / surprise-item ownership
grep -rn "{s}" org/projects/ org/missions/         # coo_lane, owner, seat fields
```
Read the HITS, not the count — a serial appears as author, as recipient, and as OWNER, and only the
third is an obligation. **Any row naming the serial as an OWNER of work outside the project you are
seating it on is a stale ownership row: it must be re-addressed by the COO BEFORE or IMMEDIATELY
AFTER the seating, and the seat must be told it is barred from acting on it.**

*MEASURED 2026-08-27, three instances in one afternoon, none caught by a gate:*
*(1) `ETFS_INGEST.TO-6` still addressed to `~Z` from 08-24 — found by seat-census;*
*(2) `ETFS_INGEST.TO-7` carrying an executor CLASS and no INSTANCE for three days;*
*(3) **11 of 40** `disarm_owner` rows in one surprise-channel file naming lanes that had just been*
*scoped away from that project — so 11 ARMED items had **an owner who was constitutionally barred***
*from acting, while every row read as owned. Instance (3) was created by the seating act itself,*
*minutes earlier, by the MSTR who had written step 1d after instance (1).*

⭐ **AND A CLASS IS NOT AN ASSIGNEE.** Same census found `ETFS_INGEST.TO-7` carrying an executor
CLASS (*"DS (producer code) + AE (deploy)"*) and **no instance**, for three days — rendering as
`(unassigned)` while every other field looked complete, including a sovereign word and a CTO
sequencing ruling naming it FIRST. **A TO with a class and no instance READS AS ISSUED AND IS HELD BY
NOBODY.** When you seat a lane, check that the TOs you are handing it name an INSTANCE.

### ⛔ 1d-ii — THE COMPLETION LIMB: an `[ACTIVE]` TO is not evidence of UNFINISHED WORK

**1d above answers *"does this serial already OWE anything"*. IT CANNOT ANSWER *"is that work still
UNDONE"*, and the two look identical in the output.** Closing a TO face is the ISSUER's act and
nothing closes it automatically, so a face outlives its work indefinitely.

```
encumbered by OPEN work            [ACTIVE]  -> do not seat
a STALE FACE over FINISHED work    [ACTIVE]  -> seating is pointless; the work is DONE
```

**SO, WHENEVER YOU SEAT A LANE ON TOs THAT ALREADY EXIST (every RESUME / re-seat / continuity case),
MEASURE THE ARTIFACT, NOT THE FACE:**
```bash
git log --oneline <the TO's build commits>              # do they exist?
git merge-base --is-ancestor <sha> origin/<branch>      # are they ON ORIGIN?
```
plus look for an acceptance / certification record. **World-done -> route to the ISSUER to CLOSE the
face. Never seat, never re-execute** — a re-execute of an accepted round is a REWIND (CLAUDE.md
NEVER-2, which already says measure the artifact before acting on an open entry; **a TO face IS an
open entry**).

⛔ **AND DO NOT WRITE A WORK-STATE ASSERTION INTO A `--say` HINT YOU HAVE NOT MEASURED.** The hint is
read by the seat as fact.

*MEASURED 2026-08-28, and the dispatch was mine. `0.4.0_DS_ClientPlatform~Q` was seated to "RESUME
D1_NAMEDISCOVERY TO-1/TO-2/TO-3 ... blocked on NOTHING, take them in order." All three were built,
ACCEPTED 15/15, CERTIFIED and ON ORIGIN (`fd15cd5cf3`, `b0ea4d8ff7`, `20dda51bd3`) ~7h earlier. 1d
passed it as clean continuity. The seat refused to execute and was right to.*
⚠ **THE DETAIL THAT MAKES THIS WORSE THAN THE BANKED FALSE-ZERO:** the query returned
`total=3 ... unresolved_serials=0`. **The lane-blindness false zero did NOT fire — the count was
TRUSTWORTHY AND WRONG ABOUT THE WORLD, and nothing in the output flags that.** A false zero
eventually announces itself; a true count of stale faces never does.
**COST:** one whole spawn. **COST OF THE CHECK:** two git commands, and only on re-seats — it does
not apply to a lane being seated on a NEW TO, which is the common case.

### 1c — Concurrency-cap headroom (informational; spawn-agent.ps1 enforces)

```powershell
$selfPid = $PID
$live = @(Get-CimInstance Win32_Process -Filter "Name='powershell.exe'" |
  Where-Object {
    $_.ProcessId -ne $selfPid -and
    $_.CommandLine -like "*# OPAL_SPAWN_MARKER_v1*"
  }).Count
```

If `$live >= 20` → spawn-agent.ps1 will reject (`spawn-agent.ps1:159` `$concurrencyCap = 20`, enforced `:164`). ⛔ **THIS DOC SAID 16 UNTIL 2026-08-29 AND SOURCE SAID 20** — measured while answering a capacity question; a plan built on the doc's number understates headroom by 4. **Read the cap at source before quoting it.** ⛔ **AND THE COUNTER IS NOT `claude.exe`:** the cap counts MARKER-TRACKED spawned PowerShell windows, so an Andrew-launched session does NOT consume a slot. Measured 2026-08-29 14:4xZ: 9 marker-counted windows of cap 20 while 15 `claude.exe` were live — **headroom 11, not 1.** Either kill an idle session first (`/mstr-kill {idle-serial}`) OR re-invoke with `--force "<reason>"` (audited bypass).

(Same `$PID` exclusion as Step 1b applies; the scanner's CommandLine contains the marker literal verbatim. Pre-fix 2026-05-26 empirical (**cap was 16 then; it is 20 now** — the ratio is history, the denominator is not current): `CONCURRENCY_LIVE=7/16` was actually 6 spawned agents + 1 scanner-self. The exclusion ensures the cap-headroom signal reflects only true spawned-agent windows.)

Surface the count in the Step 6 report regardless — useful context for population-management decisions.

## Step 2 — Spawn

```powershell
.tools\spawn-agent.ps1 {serial} [<say-text>]
```

If `--force "<reason>"` was passed, set the env var first:

```powershell
$env:FORCE_SPAWN = "<reason>"
.tools\spawn-agent.ps1 {serial} [<say-text>]
$env:FORCE_SPAWN = $null
```

The script:
- Loose serial sanity check (regex match).
- Concurrency rate cap (3/spawner/60s, 5/global/60s) — only enforced when `$env:OPAL_AGENT_SERIAL` is set (the agent-as-spawner case — every invocation of this skill, MSTR or COO; the per-spawner cap is keyed on the caller serial).
- Live-window cap (**20** simultaneous marker-tracked windows; `spawn-agent.ps1:159`).
- Both caps bypassable via `FORCE_SPAWN` env var with reason → writes `FORCE-SPAWN` line to audit log.
- Opens new detached PowerShell window via `Start-Process powershell -NoProfile -NoExit`.
- Dot-sources `.tools\ajb.ps1`; runs `ajb -Headless {serial} [extra]`.
- `-Headless` drops the `--dangerously-load-development-channels` flag (memory `feedback_spawn_drop_dev_channels_flag` — silent-ignore per server.py:299-300).
- Appends `SPAWN` audit line to `org/mcp/agent-spawn-audit.log`.
- Marker `# OPAL_SPAWN_MARKER_v1: {serial}` baked into the spawned window's CommandLine (kill-tracking + cap-counting contract).

**Read the script's output:**
- `[spawn-agent] launched {serial} in a new window` → success. Continue.
- `spawn-agent: ... cap exceeded` → cap rejection. Either re-invoke with `--force` OR kill an idle session first. Surface in report; do not silently retry.
- `spawn-agent: 'X' does not look like an agent serial` → typo. Surface to Andrew; do not retry.

## Step 3 — Wait + registration verify

The spawned window takes ~10-30s to: launch PowerShell, dot-source ajb, start `claude`, run startup protocol per `org/XXX.md`, register with broker. Wait for registration, do not assume immediate.

Polling loop (max 60s, 5s interval):

```
for attempt in 1..12:
  status = mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
  if status.liveness == "LIVE":
    break
  sleep 5s
```

Expected: `LIVE` within ~30-45s. If still not LIVE at 60s, the spawn may have failed silently (claude crashed, ajb path missing, dev-channels flag not dropped, startup loop hung). Surface to Andrew with diagnostic context (marker scan, last few lines of any visible window output if accessible). Do not retry-spawn — investigate root cause first (memory `feedback_spawn_drop_dev_channels_flag` is the most common historical cause and is already addressed by `-Headless`).

## Step 4 — Optional first-message direction

If `--say "<text>"` was passed AND the agent registered LIVE, send the directing message via broker:

```
mcp__opal-agent-comms__send_message(
  to="{serial}",
  from="{caller-serial}",            # 0.0.0_AB_MSTR or 2.0.0_SA_COO[~lane] -- whoever invoked the skill
  subject="[SPAWN-DIRECT] startup hint",
  body="<text>"
)
```

This is the SPAWN-WITH-DIRECTION fast-orient pattern (memory `feedback_spawn_with_direction_fast_orient_pattern`) — empirically ~40min from spawn to first substantive RAVC2-Request when the bootstrap message lands at agent startup with the chosen path baked in. The agent's `/watcher` Step 5 inbox-pull picks it up on the first cycle.

Note: the `--say` text already went into the ajb invocation extras (Step 2). The send_message is the **broker-side** counterpart — robust against the agent missing the CommandLine extras during early startup. Belt + suspenders.

## Step 5 — Verify-after

Confirm population state matches intent:

```
mcp__opal-agent-comms__get_agent_status(agent_serial="{serial}")
mcp__opal-agent-comms__get_live_agents()
```

Expected: `{serial}` appears in `get_live_agents` output, broker `liveness=LIVE`, last_seen < 60s. If `--say` was sent, the message should be in the agent's read or unread inbox depending on whether the watcher fired.

(Note: the broker DB is suffix-clean — it keys every entry by the FULL serial, tilde lanes included. LD-0202 confirmed the "suffix-strip" was a `server.py` query/write-layer bug (now fixed), NOT a broker-DB property. The Step 1b process-marker scan remains the authoritative pre-spawn duplicate check because it reads live process command-lines — process-truth, independent of broker registration timing. Step 5 broker verify is base-serial confirmation + freshness ack.)

## Step 5b — RETIRED (LD-0202 D1)

The `live_agents_by_marker.json` artifact is **retired** (LD-0202 D1). Its only justification was papering over a "broker suffix-strip" that never existed in the broker DB — LD-0202 ground-truthed the broker as suffix-clean and root-fixed the real `server.py` query/write conflation. So: **no post-spawn artifact write.** The Step 1b process-marker scan remains the authoritative pre-spawn duplicate check; COO `/allocation` consumes the suffix-clean broker live-set directly (repointed by COO `b93c4f193`).

## Step 6 — Report

Print the fixed report:

```
/mstr-spawn {serial}
  PRE-CHECK:    no-duplicate | marker-clean | concurrency {N}/20
  SPAWN:        launched (script said: ...) | FORCE-SPAWN reason="<>" | rejected reason="<>"
  REGISTER:     LIVE after {N}s | NOT-LIVE after 60s (INVESTIGATE)
  DIRECTION:    --say sent via broker | (none)
  AUDIT:        org/mcp/agent-spawn-audit.log
```

Then surface any population-context the spawn affects — concurrency count after, which workstreams the new session is expected to take up, any TOs that should now flow via Tier 1 to the freshly-provisioned session. This is the LD-0074 generalized lesson: a spawn is a population state change with routing implications, not just a process action.

---

## Discipline / risk notes

- **Per-invocation scope.** One `/mstr-spawn` = one spawn of one serial. A second spawn same turn = a second invocation. Skill is not a session-wide spawn license.
- **--force scope.** The `--force "<reason>"` blanket-authorizes ONE FORCE-SPAWN audit line. It does not lower the cap; it bypasses it for one spawn with forensic record. Outside this skill, FORCE_SPAWN still requires explicit Andrew per-instance auth or new LD-charter.
- **Spawn != dispatch.** Constitution Art. VI: MSTR provisions the session; TO authoring and direction flow through Tier 1. `--say "<text>"` is a startup-orient hint (the SPAWN-WITH-DIRECTION pattern when the direction is already worked out — e.g., a CORROBORATE/COUNTER verdict to execute), not a TO body. Substantive direction at agent-startup should be a Tier-1-authored TO/inbox message; `--say` is the bootstrap hint that tells the agent which TO to read first.
- **Already-live default = refuse.** Avoids double-provisioning the same serial which would create a marker-collision and confuse `/mstr-kill` and the concurrency cap. Override via `--force "intentional-duplicate"` if a duplicate is genuinely needed (rare; e.g., a tilde-lane spawn under a different lane suffix is the normal pattern instead).
- **Registration timing.** ~30-45s is normal first-time spawn latency. Do not retry-spawn before 60s — the first attempt may still register. Premature retry is how cap exhaustion happens.
- **Self-spawn.** A seat spawning its own serial (MSTR respawning `0.0.0_AB_MSTR`, a COO respawning `2.0.0_SA_COO~<lane>`) is legitimate (e.g., after a self-kill or a crashed prior session); no `--self-ack` flag needed for spawn (the symmetry with `/mstr-kill --self-ack` is intentional — kill ends a session, spawn creates one, only the destructive direction needs the extra confirmation). Step 1pt/1a/1b still run: a self-spawn over a live incumbent is the dual-COO collision class.
- **Who spawns what (division of the primitive, Andrew-direct 2026-08-28).** COO: work-population seats (lanes for TOs / decomp cells, respawns of dead lanes holding live TOs). MSTR: infrastructure population (device reboot / fleet relaunch respawns, cross-fabric and cross-device seats, `/mstr-review` mix corrections). Overlap is legal — the audit line records who acted — but a COO does not need MSTR's coordination to seat a lane, and MSTR does not route a COO's seating need back through Tier 1.

## Cross-references

- `.tools\spawn-agent.ps1` — the underlying spawn mechanism + concurrency caps + audit (Step 2).
- `.tools\kill-agent.ps1` + `/mstr-kill` — sibling destruction primitive; spawn/kill are paired population primitives per LD-0069 + Andrew architectural ruling 2026-05-22.
- `org/mcp/agent-spawn-audit.log` — forensic trail for SPAWN / FORCE-SPAWN / REJECT / KILL / FORCE-KILL / KILL-NOOP / WARN.
- LD-0061 (fabric-wide kill empirical; companion population-action context).
- LD-0069 (MSTR thin architecture; `/mstr-spawn` listed as event-triggered skill — this materializes it).
- LD-0070 (telemetry-derived liveness; will tighten Step 3 registration polling once Phase 2 lands).
- LD-0075 (`/mstr-kill` skill scribe; this skill mirrors its structural pattern).
- Memory `feedback_spawn_drop_dev_channels_flag` (the `-Headless` flag rationale — silent-ignore push mechanism per server.py).
- Memory `feedback_spawn_with_direction_fast_orient_pattern` (SPAWN-WITH-DIRECTION canonical anchor; the `--say` flag use case).
- Memory `feedback_mstr_creator_destroyer_coo_coordinator` (the 2026-05-22 supply/demand split — **SUPERSEDED 2026-08-28**: the COO invokes spawn/kill directly; MSTR is the device/fabric infra + cross-device comms manager).
- Memory `feedback_concurrency_cap_ceiling_not_target` (cap = ceiling not target; reallocate before overflow-bypass).
- Memory `reference_agent_spawn_kill_methodology` (canonical methodology; this skill is the structural channel for it).
- CLAUDE.md "Agent Autonomy" + concurrency-cap discipline.

## Rollback

A spawn is not destructive at fabric level — the new session can be killed via `/mstr-kill` if it should not have been provisioned. Recovery from a wrongful spawn is one `/mstr-kill {serial}` turn; the audit trail preserves both the spawn and the kill.

If the skill itself produces wrong behavior (e.g., 1a/1b pre-checks false-positive refuse legitimate spawns), revise SKILL.md or temporarily fall back to `.tools\spawn-agent.ps1 {serial}` direct invocation while iterating.
