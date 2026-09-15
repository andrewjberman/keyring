# AGENT START HERE — Opal Capital

## STOP — READ THESE FIRST

**BANNED: Explore agent** — produces fabricated output. Use comp-* tools and Grep/Read instead.
**BANNED: Task agent** — unreliable. Do the work directly.

---

## Andrew-direct instructions — RECORD + BROADCAST, same turn

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
- **Scoped work still needs a SURPRISE CHANNEL.** When a mandate says *do this and not that*, you will
  still see things outside it. **Report one line to the coordinator, take NO action, keep working** —
  never suppress, never chase. **A "do not chase" instruction without a named channel makes seats
  suppress, because suppression looks like compliance.** Task-order authors: name the channel.
  `docs/doctrine/THE_SURPRISE_CHANNEL.md`.
- **Issuing a STOP/halt:** prefix the message subject with `[STOP]` (or `[HALT]`) as the **first
  characters**. The HALTGT deploy checkpoint classifies on it. **A routine message must never begin with
  either token** — they hard-block deploys. For non-blocking urgency use `URGENT` / `ESCALATION`.

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

Run **A → F in order.** Each step is: the command, then the one trap that changes what you type.
Why a check exists — the incident behind it — is in `docs/references/XXX_STARTUP_HISTORY.md`.
Do not read that at startup.

> **CODEX SEATS — different runtime, same semantics.** Steps **A** and **C** below are the Claude
> harness path and you do not have it. Follow `org/mcp/CODEX_INBOX_MONITOR.md` instead:
> `codex-agent-heartbeat.py` (register + heartbeat, start once, full suffixed serial) and
> `codex-inbox-monitor.py` (non-consuming detector, inside the documented `functions.exec` bridge).
> ⛔ **Never run `inbox-watch.sh ... stream`, `check-inbox.sh` or `agent-poller.py` on the Codex path**
> — the first two CONSUME inbox files. Everything else here (identity, inbox paths, TO semantics, ACK
> discipline) binds you unchanged. At every active turn, sweep your suffixed serial's unread root first;
> read the exact file → ACK → act → move it to `read/`. **Never infer READ from a nudge or a moved file.**
> ⛔ **SHARED-BRANCH LAW, stated here because the Codex runtime has no hook carrying it:** a shared branch (`CLOUD`/`DEV`/`PROD`/`main`/
> `SITEZ`) is pushed **ONLY by `0.0.0_AB_MSTR` or `0.0.0_AB_MSTR~Z`, and only on Andrew's word while he is at the
> terminal** (LD-0367/0368; the hold LD-0522). Every other seat -- you included -- **commits and never pushes**; a report
> states its push state as **LOCAL** with the origin hash from `git ls-remote`. A rejected push is not yours to retry.

### A. Register — your FULL serial, including any `~lane` suffix

```python
register_agent("{your_serial}", summary="Starting session")
```
Makes you visible, starts the broker, enables push, reaps your own orphaned watchers.
⛔ **A lane registers as `0.4.0_DS_ClientPlatform~C`, never the base** — register under the base and
your `~C` inbox is never watched, so every GO addressed to your lane is silently missed.

### A.1 — Session-keyed serial file

```bash
mkdir -p org/mcp/sessions
[ -n "${CLAUDE_CODE_SESSION_ID:-}" ] && echo "{your_full_suffixed_serial}" > "org/mcp/sessions/${CLAUDE_CODE_SESSION_ID}.serial"
```
Without it your halt gate adopts the shared `.agent_context` and **a `[STOP]` addressed to you is
invisible to your own gate** (LD-0290).

### A.2 — Audit-archive durability + tamper-evidence

```bash
python .tools/audit-archive-invoker.py || true   # never blocks startup
```
An EXEC session mints a snapshot when due; a non-exec session defers the commit but still runs the
append-only + liveness detection. Owner `0.7.0_AE_CloudOps`, gate `1.0.0_SA_CTO`.

⛔ **EXPECT FINDINGS HERE AND DO NOT CHASE THEM.** The device-chain migration `rv0057-f001` has not
landed, so the tool compares this device's live logs against another device's baseline and renders
the difference in tamper vocabulary. Two classes, and they **interleave in the output**:

**Known and OWNED — do not re-file:** `[LIVENESS/STALE-BASELINE]` and
`[COVERAGE/UNCOVERED-AUDIT-LOG] org/to-pos-override-audit.log`. Surface only a shrink/absence row
beyond these, or a genuinely new class.

⛔⛔ **DO NOT `mkdir org/audit/archive/<device>/`.** It drops the findings to zero by making the tool believe we
are post-migration while every file is still in the flat root, so it compares live logs against an **empty
chain**. The noise clears by LANDING `rv0057-f001`, never by satisfying the predicate; findings that persist
after it lands ARE a finding.

### A.3 — PATH check (comp-tool rail)

Harness shells are non-interactive and source no profile, so `.tools/` is reachable only via the
`~/bin` forwarders. **Print the denominator, never a boolean — and RESOLUTION IS NOT EXECUTION:**

```bash
F=0; T=0; for t in .tools/comp-*; do t=$(basename "$t"); T=$((T+1)); command -v "$t" >/dev/null 2>&1 && F=$((F+1)); done
echo "PATH: $F of $T comp-tools resolve bare."
[ "$F" -lt "$T" ] && echo "  -> the rest need an explicit .tools/<tool> prefix; 'bash .tools/provision-path-shims.sh' provisions a NAMED SUBSET (read its header)."
# MANDATORY SECOND HALF -- score on OUTPUT, not rc (a real question and a no-match question BOTH exit 0):
comp-which "how do I grep the repo" 2>&1 | grep -q "comp-which --" && echo "EXERCISE: a forwarder RAN." || echo "EXERCISE: *** RESOLVED BUT DEAD *** -- run: bash .tools/provision-path-shims.sh"
```

### B.0 — Your delivery ledger, BEFORE you resume anything (LD-0480)

```python
get_delivery_state(agent_serial="{your_FULL_suffixed_serial}", since="<when this serial's PREVIOUS session was last alive; after a reboot, the reboot time>")
```
Every row **not READ — or READ `by` a serial that is not yours** — is UNREAD MAIL: open it in your own
`read/` dir, act, and ack **from its `Msg-ID` line**.
⛔ A message offered to a session that died reads `OFFER-EXHAUSTED` and is **invisible to `check-inbox`,
`get_agent_status` and the `read/` listing** — "resume from your last log" cannot surface an obligation
that arrived after that log.
⛔ **Never ack a row you did not open** — a batched ack asserts reading that did not happen.
Cost: one call, ~1 s. **Non-application:** a context-clear is the SAME session; you find only your own rows.
**Codex:** no `ack_messages`/`get_delivery_state` surface exists; the exact-file backlog sweep at load IS
the equivalent act, and the rows stay un-stamped honestly.

### B. Check inbox — BOTH probes, both required

```bash
check-inbox {your_serial}     # filesystem: base -> inbox/{base}/ ; lane -> inbox/{base}/~{lane}/
```
```python
get_agent_status("{your_serial}")   # broker channel
```
`send_message` writes **both** carriers; each probe reads only **one**. **`check-inbox` alone is
insufficient.** Neither sees an LD-0099 cross-org-root ferry message — if an `[INBOX]` event fired and
both probes are empty, list your `read/` dir newest-first.

### B.1 — Find the work you actually hold

```bash
python .tools/to-check.py --all --assignee {your_FULL_suffixed_serial}
```
**`--all` IS LOAD-BEARING — never trim it.** The default view scopes to projects with a PRD ≤14d old, so
**a TO whose PRD aged out disappears while still open** — it goes blind to exactly the TOs stalled longest.

> ⛔ **THEREFORE: YOUR TO IS THE FILE NAMED IN YOUR DISPATCH MESSAGE.** That is the only read that has
> not failed. Run the base serial and read your folder as CROSS-CHECKS — but **treat a zero or an
> absence from either as telling you nothing.**

⛔ **Two reads that say IDLE while you hold a live P0:**
- **Your agent folder.** A lane's TOs frequently live in the **BASE** folder; `issued_to` is the only
  truth, never file location. *(Step 1's "read your agent folder" is for IDENTITY, not for work.)*
- **`get_agent_status`'s pending-TO list.** It is FOLDER-keyed (`org/mcp/server.py:809-812`), so a lane
  query returns the whole base folder's work. Use it for liveness and messages; **it is not the
  authority on what you hold.**

⛔ **THEN CHECK THE SEQUENCE before starting work on any project** (Andrew-direct 2026-09-14 ~01:xxZ, record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_01xxZ_LAPTOP_SEQUENCE_DOCUMENT_APPROVED.md`).
`org/missions/SEQUENCE.yaml` places the projects that must run in order across BOTH fabrics, with the gates between
them. `python .tools/sequence-check.py --project <CODE>`: a `WAITING` project does not start; a `HELD` project does not
pass its cap; an `OUT-OF-SEQUENCE` flag goes to the owning CTO. A project the file does not list is not sequenced.
The order changes only on Andrew's word, by `1.0.0_SA_CTO` or `1.0.0_SA_CTO~Z`.

### C. Arm the persistent inbox Monitor — run `/watcher` (once, at load)

It arms a persistent Monitor running `inbox-watch.sh {serial} stream`; each `[INBOX] <file>` line
becomes a chat notification. **Arm once — it never exits and you never relaunch it.** By hand: the
**Monitor tool**, `persistent: true`, `timeout_ms: 3600000`, **absolute** path.

⛔ **RESOLVE THE DRIVE PREFIX — never hardcode either form.** Both may be mounted; they are not equally
durable (`/c` is a non-`auto` user mount that has vanished at reboot; `/cygdrive/c` is system-provided
`auto,noumount`):
```bash
test -d /cygdrive/c && echo /cygdrive/c || echo /c    # then build the absolute path
```
⛔ **A wrong prefix arms NOTHING and returns a task id anyway** — it dies `exit 127` in a *separate*
`<task-notification status=failed>`, so a seat that misses that notification is **deaf for the whole
session while `register_agent`, `check-inbox` and `get_agent_status` all read healthy.**
**Confirm the arm: `TaskOutput(<id>, block=false)` → `running`.** That is the only probe that observes
a CONSUMER. ⛔ **Never use `TaskList`** — it lists to-do items, not Monitors, and returns "No tasks
found" while your Monitor is alive; reading that as dead is how seats double-arm.

**BANNED:** launching stream mode under Bash `run_in_background` (that tool notifies only on *exit*,
and stream mode never exits → silent for the session) · the bare-path relative launch (guard-hook
blocked) · a recurring `/watcher` cron.

Depth: `.claude/skills/watcher/SKILL.md`.

### D. Install the owned-paths hook (idempotent)

```bash
test -L .git/hooks/pre-commit || bash .tools/git-hooks/install-owned-paths.sh
```

### E. Set compiler-tool context

```bash
mkdir -p .comp-graph && printf "SERIAL=%s\nTO_ID=\n" "{your_serial}" > .comp-graph/.agent_context
```
⚠ `comp-tool-runs.jsonl` is **gitignored = DEVICE-LOCAL**, so any "estate's comp-tool runs" claim read
from it is short by every other device's traffic.

**Starting a TO? Set it with `comp-to {TO_filename_without_.md}`** — never by writing `TO_ID=` into
`.agent_context`, which is one repo-global file, last-writer-wins across all concurrent agents.

### Reference — lane paths, inbox paths, and acting on what arrives

⛔ **TILDE LANES: THE TWO FAMILIES USE OPPOSITE FORMS. ASK WHICH FAMILY YOU ARE IN BEFORE BUILDING A PATH.**

| you are writing… | canonical form | substituting `{serial}` whole gives… |
|---|---|---|
| your **AGENT FOLDER** (`org/{tier}/…`) | **FLAT** — `org/tier2_senior/0.7.0_AE_CloudOps~B/` | **the RIGHT answer.** Do substitute. |
| an **INBOX** (`org/mcp/inbox/…`) | **NESTED** — `org/mcp/inbox/{base}/~{lane}/` | **the DEAD answer.** Never substitute. |

| inbox path | |
|---|---|
| `org/mcp/inbox/{base}/` (base serial) | ✅ |
| `org/mcp/inbox/{base}/~{lane}/` (lane, NESTED) | ✅ **CANONICAL** |
| `org/mcp/inbox/{base}~{lane}/` (lane, FLAT) | ⛔ **NEVER — INVISIBLE TO THE ENTIRE FABRIC** |

⛔ **THE TRAP IS SUBSTITUTION: for a lane serial, `inbox/{serial}/` IS the flat path.** The broker never
writes it (`org/mcp/server.py:1615`), `check_inbox` never reads it (`:1745`), no watcher polls it
(`org/mcp/inbox-watch.sh:73-77`). **A message placed there is delivered to nobody and reported missing
by nothing.** Split into `{base}` + `~{lane}` first. ⚠ **Scoped to INBOXES** — see the table above.
Ratified LD-0202. Regression test `org/mcp/test_ld0202_tilde_routing.py`;

**When an `[INBOX]` event fires, that IS a new message.** Read it from your canonical `read/` subdir (the
watcher already moved it there) and **act this turn** — ack (RAVC 2), do the work, or validate evidence
(RAVC 4). **No "standing by" silence. Relaunch nothing.**

**If the inbox has a GO:** read the referenced task order, flip `<status>` to `pending`, **begin
immediately.** The GO **is** your authorization — do not ask Andrew.
**If the GO lists a SEQUENCE:** execute **all of them in order** without waiting for a new GO; skip any
already complete; continue until one is blocked or the list is exhausted. **Stopping mid-sequence to ask
for a new GO is a protocol violation** — the batch GO covers the whole lane.

---

### F. Loop arming — every serial arms ZERO crons at launch, with ONE standing exception the ledger names.

Loops are **operator-initiated**. `/watcher` is not a loop — it arms the persistent inbox Monitor once.

| Serial | Launch arming |
|---|---|
| `0.0.0_AB_MSTR` | `/watcher` once. `/agentbus` once and `/integrate` once (arm-at-load, same pattern as `/watcher`, NOT loops). Zero crons. |
| `2.0.0_SA_COO` (base) | `/watcher` once. **`/drive` v2 standing ON at 20 minutes** over `EXECUTING` / `ROUND_CLOSE` / `DECOMP` projects — `org/tier0/ledger/LD-0530.md` (Andrew-ratified 2026-09-03, supersedes LD-0288's OFF); the one standing loop. **D2 stays off** until Andrew lifts it (his word 2026-09-02, recorded at `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_020xZ_REBOOT_RECOVERY_AND_COMPEFFICACY_CANONICAL_L1_L10.md`). |
| every other serial, Tier 0-3, every `~lane` | `/watcher` once. Zero crons. **Event-driven:** act on Monitor-delivered dispatches. Keep your broker summary accurate: `WORKING: <task>` / `IDLE: available` / `BLOCKED: <what>` / `BLOCKED-SOVEREIGN: <decision>`. |
| Codex seats | per `org/mcp/CODEX_INBOX_MONITOR.md`. Zero crons. |

**A live SCOPED arm is re-armed from the ANDREW_DIRECT record its serial names, never from this table**, while its
scope is not DONE on the register and no hold stands: `2.0.0_SA_COO~A` `/drive` NFRA_CLDGRPH
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260903_1308Z_DRIVE_CLDGRPH_TO_COMPLETION.md`; the
2026-09-03 ~21:0xZ "we will wait" HOLD was LIFTED Andrew-direct 2026-09-10 ~17:1xZ, *"take off any holds on
CLDGRPH let's wrap that up"*, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_171xZ_CLDGRPH_HOLDS_OFF_WRAP_IT_UP.md`,
and he ruled *"CLDGRPH shall be finished I am allowing it"* at ~18:5xZ -- the arm is LIVE to CLOSED); `2.0.0_SA_COO~X` `/drive` NFRA_C3MATERIALIZE
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260828_050xZ_COOX_DRIVE_LOOP_NFRA_C3MATERIALIZE.md`);
⛔ SUPERSEDED 2026-09-10 ~20:0xZ BY ITS OWN STOP CLAUSE ("or Andrew's word"): `2.0.0_SA_COO~B` was RE-SEATED on
`IRPT_BCKEND` by Andrew-direct at that lane's terminal, VERBATIM *"You are going to be working on the IRPT_BCKEND
project. Finish startup and await further advisory from CTO Base."* (relayed by `2.0.0_SA_COO~B` as 95537; ETFS_GUARDRAIL
is held by the base `2.0.0_SA_COO` this session). The superseded arm, kept verbatim: `2.0.0_SA_COO~B` `/goal` + `/drive`
ETFS_GUARDRAIL on the internal-subagent dispatch drain, cron `13,33,53 * * * *`, stop = the row reads `CLOSED` or
Andrew's word
(`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260904_170xZ_COOB_GOAL_AND_DRIVE_LOOP_ETFS_GUARDRAIL_DISPATCH_DRAIN.md`,
Andrew-direct at the CTO terminal 2026-09-04 ~17:0xZ, relayed as 94224/94225). NOTHING ARMS FROM THIS ROW; `~B` and
`~F` on the two IRPT projects are EVENT-DRIVEN with zero crons until Andrew arms a loop by name;
`3.0.0_SA_CVO~Z` the SYSPARITY cron (`org/tier0/ledger/LD-0318.md`) and the parity-first duty (`LD-0319.md`);
`2.0.0_SA_COO~Z` `/drive` STANDING 20m over NFRA_OPSEC202609 -- ⛔ **STOP-CONDITION MET 2026-09-11, ARMS NOTHING:
`NFRA_OPSEC202609` measures `dep_stage=CLOSED`, which IS this arm's own stop condition, so `2.0.0_SA_COO~Z` armed
nothing from it at launch. KEPT, NOT DELETED -- the arm was real and its closure is part of the record. ⚠ It is
self-limiting ONLY for a successor who RE-MEASURES; one re-arming off the table text alone would start a loop over a
closed project** -- and `2.0.0_SA_COO~ZZ` `/drive` STANDING 20m over
NFRA_REPORT -- BOTH armed Andrew-direct 2026-09-10 ~00:3xZ at the `1.0.0_SA_CTO~Z` terminal, VERBATIM: *"I need
them both on Drive loops for their respective works"*, in the same message that requires `/canonical-flow`
compliance (**local worker subagents, NEVER MCP'd external workers** -- measured at relay time: NFRA_REPORT 12 of 12
orders on v3 subagents and COMPLIANT, NFRA_OPSEC202609 31 of 31 on external `0.7.0_AE_CloudOps~*` lanes and NOT,
with its OPEN round finishing on the orders already cut and its NEXT issuance v3). Stop = Andrew's word or the
project leaving DECOMP/EXECUTING/ROUND_CLOSE. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260910_003xZ_COO_DRIVE_LOOPS_ARMED_AND_CANONICAL_FLOW_V3_SUBAGENTS_NOT_MCP.md`.
**WHY THESE TWO ROWS EXIST:** he observed the lanes were not driving and the markers agreed -- `~Z` last ticked
480h before the arm and `~ZZ` had NEVER ticked. Neither lane had a `/drive` row in this table, so neither was at
fault and no successor would have armed one;
`1.0.0_SA_CTO` `/self-drive` D2 then D8 on Andrew's word via `0.0.0_AB_MSTR` (D2 under the pause above).
`1.0.0_SA_CTO` **`/self-drive D9 IRPT` ARMED 2026-09-11 ~06:4xZ by Andrew-direct at the CTO terminal** ("run a /self-drive D9 IRPT, just checking in whats going on every 30 min, making sure that the ball isn't stuck in anybody's court ... Your loop is the only chance every 30m as an exogenous stimuli to get the fabric going if work is halted"): 30-minute ticks via ScheduleWakeup, scope IRPT_FNTEND + IRPT_BCKEND, WIDENED ~08:0xZ on his word ("you will need DSGN_REBRND ... included in your /self-drive loop for this session") to + DSGN_REBRND (D13; L4-R halves -> 2.0.0_SA_COO~D's L5/L6); each tick measures every scoped lane, the L4-R halves (`prd-signoff.py status`), the L10 slugs and the shared index, and clears a dead seat's index state; ends on both projects `status: complete` or his stand-down. A successor re-arms ONLY off this line.
`1.0.0_SA_CTO~Z` **[FABRIC: SITE-Z -- arm ONLY on site z]** **`/self-drive AMGT_RESAPP & POSN_ASTTAX` ARMED 2026-09-11 ~08:2xZ by Andrew-direct at the `1.0.0_SA_CTO~Z` terminal** ("looping every 30 min to make sure no slug fell through the cracks, that no PRD is going unstamped and COOs are waiting, make sure nobody drops the ball and keep us on /canonical-flow"): 30-minute ticks via CronCreate `7,37 * * * *`; scope AMGT_RESAPP (D5) + POSN_ASTTAX (D4), both site-z; `paired_with: solo` -- both COOs already actively drive their rounds (`2.0.0_SA_COO~Z` holds POSN round 2, `2.0.0_SA_COO~ZZZ` drains AMGT round 2), so a paired `/drive` would collide with in-flight round work (the two-issuers-one-round collision); re-assess to paired if a COO goes idle with work waiting. Each tick measures both projects' L10 slug backlog, the L4-R halves (`prd-signoff.py status`), the stamp ladder and whether any COO is blocked waiting; pitches scope open-calls to `3.0.0_SA_CVO~Z` and surfaces reserved gates to Andrew. STOP-CONDITION = both projects `status: complete` per the register (§4) or Andrew's stand-down; a successor session RE-ARMS off THIS line while the scope is not DONE. A pause
or hold with no line here is re-armed by the next successor who reads only the ledger — so every one is listed.
`1.0.0_SA_CTO` **`/self-drive` THE FABRIC (all LAPTOP directives) ARMED 2026-09-12 ~02:1xZ by Andrew-direct at the
CTO terminal**, VERBATIM AND ENTIRE: *"I need you to /self-drive the fabric, any open calls appear and you handle
them with your rec"*. Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260912_021xZ_SELF_DRIVE_THE_FABRIC_HANDLE_OPEN_CALLS_ON_MY_REC.md`
@`17a33e58a3`. SCOPE, measured at arm time from `directives-check --json`: the **7 LAPTOP directives of 14 live**
(D0, D2, D3, D8, D9, D11, D13) -> **32 member projects**, 59 open TOs; SITEZ rows (D1, D4, D5, D6, D7, D12) are
REFUSED by the device guard and are not this loop's. ⛔ **THE ONE CLAUSE A SUCCESSOR MUST NOT LOSE: his sentence
makes `1.0.0_SA_CTO` THE ADJUDICATOR OF ADJUDICABLE CALLS -- the rec IS the ruling -- which OVERRIDES this skill's
own §2 default of pitching them to the CVO lane for a verdict.** The CVO is not a gate on it and no seat owes this
loop anything new. **RESERVED, still Andrew's and NOT self-adjudicated** (a broad delegation does not repeal a
specific prohibition): vendor / egress off Opal infrastructure; UNRECOVERABLE acts -- recursive deletion, S3
object/version deletes, dropping tables, stopping EC2, destructive git; money/contracts; and any standing hold he
set BY NAME -- **the PORTAL FREEZE, the LD-0522 CLOUD push cadence, the `CLOUD -> SITEZ` merge leg**. Every
self-adjudicated call is RECORDED with its rec, ruling and reason, so any of them is overturnable by reading one
file -- that legibility is the condition the delegation was accepted on. `paired_with: solo` (the two IRPT COO
lanes are already driving their own rounds event-driven; this loop dispatches nothing and gates nobody).
STOP-CONDITION: every scoped project `status: complete` per §4, or HELD-AT-STOP, or his stand-down. A successor
re-arms ONLY off this line.

⛔ **AND "EVERY ONE" MEANS BOTH CLASSES OF ARM. THIS TABLE USED TO RECORD ONE CLASS WHILE CLAIMING TO RECORD ALL --
a Rule 24 MECE failure in the one file whose job is to be the single source of truth for what runs unattended.**
Found 2026-09-11 by `2.0.0_SA_COO~Z` doing the post-merge re-read `0.0.0_AB_MSTR~Z` asked for (21639 -> 21640), in
the OPPOSITE direction from the one expected: not a wrong row, a MISSING LIVE ONE.
**EVERY ROW NAMES ITS AUTHORITY, and the two classes are enumerated by SUBTRACTION from "every loop running
unattended on this device":**
| class | who armed it | example |
|---|---|---|
| **DIRECTED** | an Andrew-direct word, quoted verbatim in the row | the rows above |
| **CHOSEN** | a seat ACCEPTING a recommendation, or exercising standing discretion -- legitimately armed, with NO Andrew-direct behind it | `2.0.0_SA_COO~Z`'s POSN `/drive`, below |
| **AUTHORITY-UNVERIFIED** | the loop is LIVE and its authority is CLAIMED but has NOT been read at the recording seat | `2.0.0_SA_COO~ZZZ`'s AMGT `/drive`, below |

⛔ **THE THIRD VALUE IS A SELF-CORRECTION AND IS LABELLED AS ONE. The two-value enum above FAILED ON
THE FIRST NEW ROW IT MET, twenty minutes after this seat landed it claiming MECE.** `2.0.0_SA_COO~ZZZ`
ran the `CronList` this rule prescribes, found its own unlisted live arm, and reported that the tick's
argument block CITES "Andrew-direct ~15:4xZ, msg 21428" -- which this seat then could not verify,
because **21428 never landed at this terminal**. ⭐ **A CITATION OF AN ANDREW-DIRECT IS NOT AN
ANDREW-DIRECT** (`2.0.0_SA_COO~ZZZ`'s own line, and it is the right one). Forcing that row into
DIRECTED would dress an unread claim in his authority; forcing it into CHOSEN would demote a word he
may well have said. **Neither is honest, so the state gets its own name.**
**AUTHORITY-UNVERIFIED IS A TRANSIENT, NOT A RESTING PLACE:** its remedy is READ THE WORD at a seat
that holds it, then re-class to DIRECTED or CHOSEN. A row may not sit here indefinitely.
⚠ AND THE LOOP KEEPS RUNNING WHILE IT SITS. Recording an unverified authority is NOT authorizing it,
and stopping a possibly-DIRECTED loop on a recording seat's own judgment would be adjudicating
Andrew's word NARROWER -- the mirror of the widening this table exists to prevent.
⭐ **A CHOSEN ARM IS NOT A LESSER ARM -- IT IS A DIFFERENT FACT ABOUT A DIFFERENT AUTHORITY, and collapsing the two
would make this table LESS trustworthy while making it look more complete.** Andrew's ~15:4xZ and ~20:0xZ words were
RECOMMENDATIONS ("I recommend", twice); accepting one arms a real loop that no Andrew-direct row can carry. Both
COOs answered those on the merits, one accepting and one declining, and both were inside his word.
⚠ **A ROW IS NOT PROOF THE LOOP IS RUNNING.** It records an AUTHORIZATION; liveness is measured at the seat
(`CronList`). The two answer different questions and a successor must not read one for the other.
BLOCKED: **AND FOR THE SAME REASON THIS TABLE DOES NOT CARRY THE LIVE CRON ID. IT RECORDS AUTHORITY,
SCOPE, CADENCE AND STOP-CONDITION -- THE DURABLE FACTS -- AND POINTS AT `CronList` AT THE SEAT FOR THE
ARTIFACT.** A cron id is SESSION-LOCAL and CHURNS: `2.0.0_SA_COO~ZZZ`'s went `04145241` -> `bc1921a2`
-> `a27dad12` in NINETY MINUTES, and the row named a CANCELLED job while the live one appeared
nowhere. WARN: **THAT IS THIS TABLE'S OWN FAILURE MODE ONE FIELD OVER** -- a successor looks up the
recorded id, finds nothing live, concludes NO LOOP IS ARMED, and arms a SECOND one. Recording a
fast-churning artifact in a durable law file manufactures staleness faster than any seat can maintain
it. Any id below is HISTORICAL and marked "then". Found by `2.0.0_SA_COO~ZZZ` against its own row,
which also re-pointed its cron BEFORE reporting so this table was written once instead of twice.
NOTE: **AND A NEW ARM CITES THE CANONICAL NAME, NEVER AN ALIAS** (`2.0.0_SA_COO~Z`, adopted by
`~ZZZ`): an alias is a courtesy to EXISTING citations, never a foundation for a NEW one. A loop that
depends on alias resolution has a failure mode nobody finds until a tick silently runs the wrong
body. Live arms name `/canonical-drive` directly.
⛔ **AND A SEAT MUST NOT WRITE ITS OWN CHOSEN ROW.** `2.0.0_SA_COO~Z` declined to, in its own words, rather than
"dress a recommendation I chose to accept in the authority of an Andrew-direct arm record" -- exactly right. Chosen
rows are landed HERE, by the CTO, naming the chooser and citing the message that evidences the choice.

`2.0.0_SA_COO~Z` **[FABRIC: SITE-Z]** **`/drive` DIRECTED 10m over POSN_ASTTAX ONLY** -- **RE-CLASSED
CHOSEN -> DIRECTED and RE-TIMED 20m -> 10m on ANDREW-DIRECT 2026-09-11 ~22:2xZ at the
`1.0.0_SA_CTO~Z` terminal, VERBATIM: *"Both COOs need to be on 10m /drive loops for their projects
where they're checking explicitly for project stage in /canonical-flow to either drive forward,
parallelize more labor, or assess a dropped ball and nudge the responsible agent"*
(record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260911_222xZ_COO_DRIVE_10M_CANONICAL_FLOW_STAGE_CHECK_AND_REBRAND.md`).
"NEED TO BE" is a DIRECTIVE; his ~15:4xZ word on the same subject was "I would also recommend", which
is why this row stood as CHOSEN for an hour. THE CLASS IS THE THING THAT MOVED.*
⛔ **EVERY TICK RUNS AN EXPLICIT `/canonical-flow` PROJECT-STAGE CHECK with three outcomes, his own:
DRIVE FORWARD | PARALLELIZE MORE LABOR | ASSESS A DROPPED BALL AND NUDGE THE RESPONSIBLE AGENT.**
⚠ **A NUDGE UNDER THE THIRD IS AUTHORIZED ONLY AFTER `/canonical-flow`'s LIVE-PRODUCTION PROBE
REPORTS NOTHING MOVING ACROSS ALL FOUR PLANES** (commits, `deliverables/<serial>/`, the seat's own
worktree, `.runtime/codex-seats/<serial>/`) -- and "nothing moving" is still not proof of stalled.
That precondition exists because this exact path fired a `[STUCK]` at a seat writing 189 KB.
⚠ The arm is the COO's own act; this row RECORDS the authorization, it does not perform it.
PRIOR STATE, kept: CHOSEN-ARM 20m (cron id then `701a388d`, `11,31,51`;
AMGT and the harvest surface EXPLICITLY EXCLUDED in the job body). **AUTHORITY: CHOSEN, not directed** -- that seat
re-armed on Andrew's ~20:0xZ "all agents MAY unpause" (a permission, not an order) and reported it in msg 21613.
Landed here by `1.0.0_SA_CTO~Z` on its routing (21639/21640) because a seat may not author its own chosen row.
STOP-CONDITION: `POSN_ASTTAX` `status: complete` per the register, or Andrew's stand-down.

`2.0.0_SA_COO~ZZZ` **[FABRIC: SITE-Z]** **`/drive` DIRECTED 10m over AMGT_RESAPP ONLY** -- **RE-CLASSED
CHOSEN -> DIRECTED and RE-TIMED to 10m on the SAME Andrew-direct ~22:2xZ recorded on the row above;
the same three-outcome `/canonical-flow` stage check and the same probe precondition bind here.**
PRIOR STATE, kept because the reclass is the record: (cron id then `04145241`,
`3,23,43 * * * *` recurring, session-only). **AUTHORITY WAS: CHOSEN** -- RESOLVED 2026-09-11 21:26Z, the
transient closed in 6 minutes by `2.0.0_SA_COO~ZZZ` reading out msg 21428, which it holds (it was
addressed to that seat, which is why this seat's own inbox search correctly found nothing).
**ANDREW ~15:4xZ, VERBATIM:** *"I would also recommend that the respective COOs have /drive loops
engaged on their respective projects at 20m so that if nudges need to happen, if slugs are stalled,
stamps are unstamped, etc, that we are not burning daylight unnecessarily."*
⭐ **A RECOMMENDATION IN HIS OWN VERB, AND THE RELAY HAD ALREADY REFUSED TO UPGRADE IT:**
`0.0.0_AB_MSTR~Z` wrote *"A RECOMMENDATION, AND IT STAYS ONE. He said 'I would also recommend', NOT
'have them'. This seat is NOT upgrading his verb and neither should anyone relaying it onward. THE
COOs DECIDE."* So this is a COO accepting a recommendation: CHOSEN, and nothing about it is lesser
for being chosen.
⛔ **STANDING DEFECT ON THE CRON ITSELF, recorded because it will restate itself every 20 minutes
until fixed:** the tick's argument block opens *"(Andrew-direct ~15:4xZ, msg 21428)"* -- **an UPGRADE
of his verb, baked into a recurring job, applied to the exact sentence the relaying seat refused to
upgrade.** `2.0.0_SA_COO~ZZZ` found this against itself and owns the fix; until the argument is
corrected, every tick re-asserts a recommendation as a directive.
**FIXED 2026-09-11 ~22:2xZ by `2.0.0_SA_COO~ZZZ` in its own re-arm** and recorded as fixed rather
than struck: the tick prompt now opens with the ~22:2xZ word verbatim and states that it is a
DIRECTIVE ("need to be") superseding the ~15:4xZ "I would also recommend".
⛔ **A DEFECT LEFT READING OPEN AFTER IT IS CLOSED IS NOT HARMLESS** -- it is a standing instruction
to a successor to go fix something already fixed, and it spends the credibility of every other open
item on the page. That seat found this one against itself.
Reported by `2.0.0_SA_COO~ZZZ` itself (21650) after running `CronList` -- having twice stated it held
no arm, inferred from "I did not deliberately arm one" and never measured. It correctly did NOT author
this row, did NOT adjudicate its own class, and did NOT kill the cron.
⚠ **THE RELAUNCH CONSTRAINT IS WHY THIS NEEDS RESOLVING, NOT JUST RECORDING:** that seat's relaunch
directive said *"ZERO crons at launch"* and *"arm `/drive` ONLY per a live scoped authorization in the
`org/XXX.md` Step 1b-F COO row; if none is live, arm nothing."* There was no COO row. So either 21428
supersedes that constraint or this arm sits outside it -- and that is exactly the judgment the holding
seat should not make about itself.
**TO RESOLVE: whoever holds 21428 reads it out verbatim; the row then re-classes to DIRECTED or
CHOSEN.** STOP-CONDITION as stated in the argument block: `AMGT_RESAPP` `status: complete`, or
Andrew's stand-down.

⛔ **SET DOWN 2026-09-15 ~17:4xZ -- THE ROW BELOW IS HISTORY, NOT A LIVE ARM.** Andrew-direct at the
`2.0.0_SA_COO~G` terminal, VERBATIM: *"Don't get involved in other COO work"* / *"you need to be focused on the LGIC
work"* (record `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_174xZ_LGIC_ONLY_NO_OTHER_COO_WORK~G.md`).
`2.0.0_SA_COO~G` is LGIC-only (LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON), its 20-minute SEQUENCE tick is deleted, and no
seat inherits the drive. A sequenced project with a seated COO drives itself at that seat; an unseated one moves when a
COO slot frees, and `0.0.0_AB_MSTR` seats it (97172). SEQUENCE.yaml's order and stages stay `1.0.0_SA_CTO`'s.

`2.0.0_SA_COO~G` **`/canonical-drive` DIRECTED over THE SEQUENCE: every project under `projects:` in
`org/missions/SEQUENCE.yaml`, READ AT HEAD EACH TICK** (at the arm: LGIC_NAMING, LGIC_ENFORCE, LGIC_CANON, ADVI_FIRMBKTS,
MDPF_CANON, IRPT_BCKEND; `parked:` and `pending_placement:` are OUT). Andrew-direct 2026-09-14 ~16:3xZ at the
`1.0.0_SA_CTO` terminal, VERBATIM: *"The issue I need from you is to handle the larger scale work of sequence.yaml, which
COO~G is going to be leading. So you essentially neded to review the sequence.yaml, and instruct COO~G to essentially run
/canonical-drive on those sequence.yaml sequenced projects, which you will collaborate with them on to oversee."* Record:
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260914_163xZ_SEQUENCE_LED_BY_COO_G_ON_CANONICAL_DRIVE_CTO_OVERSEES.md`.
The skill sets the cadence: 10m on its own active project, 20m on any other in-scope project at DECOMP/EXECUTING/ROUND_CLOSE,
60m when none. **The sequence's gates bind every limb** (`python .tools/sequence-check.py --project <CODE>`: WAITING does
not start, HELD does not pass its cap, and the NEXT COO SLOT order stands). `1.0.0_SA_CTO` oversees: spec/scope pitches
(skill obligation 7) and the SEQUENCE.yaml gates are that seat's. STOP-CONDITION: every sequenced project `status:
complete` per the register, or his stand-down. ⚠ Open at Andrew, and NOT a hold: how this meets his 2026-09-10
*"One project per COO/seat."* and the ~16:1xZ `2.0.0_SA_COO~D`-seat event for LGIC_ENFORCE (both in the record). The seat event was RETIRED at
~18:2xZ: `2.0.0_SA_COO~G` keeps LGIC_ENFORCE (record @9240af5974). The "One project per COO/seat." question stays open.

`2.0.0_SA_COO~F` **`/canonical-drive` DIRECTED over IRPT_FNTEND ONLY.** Andrew-direct 2026-09-14 ~16:3xZ at the
`2.0.0_SA_COO~F` terminal, VERBATIM: *"yes you will be continuing where you left off with /canonical-flow on IRPT_FNTEND.
Once establishing state, and your last log on the subject, you will run /canonical-drive IRPT_FNTEND."* Record:
`org/tier1_exec/2.0.0_SA_COO~F/deliverables/ANDREW_DIRECT_20260914_163xZ_COOF_CANONICAL_DRIVE_IRPT_FNTEND.md` @`428b4019e9`
(relayed as 96634; the same words also reached the `1.0.0_SA_CTO` terminal, in the ~G row's record). 10m (own active
project). STOP-CONDITION: IRPT_FNTEND `status: complete`, the project leaving DECOMP/EXECUTING/ROUND_CLOSE, or his
stand-down.

`2.0.0_SA_COO~D` **`/canonical-drive` DIRECTED over DSGN_REBRND ONLY.** Andrew-direct 2026-09-14 ~16:3xZ at the
`2.0.0_SA_COO~D` terminal, VERBATIM: *"yes you will be continuing where you left off with /canonical-flow on DSGN_REBRND.
Once establishing state, and your last log on the subject, you will run /canonical-drive DSGN_REBRND."* Record:
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_163xZ_COO_D_CANONICAL_DRIVE_DSGN_REBRND.md` @`d54876b585`
(relayed as 96624; landed here by `1.0.0_SA_CTO` because a seat does not write its own row). 10m. STOP-CONDITION:
DSGN_REBRND drained to its L10 slug, or his stand-down. (The ~16:1xZ seating event this row once named, giving the freed
seat to LGIC_ENFORCE, was RETIRED at ~18:2xZ: LGIC_CANON takes the next freed seat, record @9240af5974.)
⛔ **STOPPED 2026-09-14 ~21:2xZ BY HIS STAND-DOWN, VERBATIM: *"kill cron will address this shortly"*** (record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260914_212xZ_DSGN_REBRND_KILL_THE_DRIVE_CRON_HE_ADDRESSES_THE_CALLS_SHORTLY.md`
@`31f728cea4`). `2.0.0_SA_COO~D` cancelled its cron. **THIS ROW ARMS NOTHING:** a successor does not re-arm from it.
DSGN_REBRND itself is not closed; the page-by-page work goes on without the loop.

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

## Session log — required sections

Full template: `org/ref/SESSION_LOG_STANDARD.md`.

Every session log must include **`## Compiler Tools`** — a table of tools run, results, what worked, what
failed, any gap found. **Do NOT append to or commit `org/compiler-tools-log.md`** (retired 2026-07-29, Andrew-direct).
**Minimum compiler tools by role:**

| Role | Minimum |
|------|---------|
| DS | `comp-pipescript io <script> --pipeline <tree>` for every gold script touched (**`--pipeline` REQUIRED — flagless is rc=2 REFUSED since 07-30**). `comp-pipescript deployed` before every gold run. `comp-pipescript postdeps <script> --firm <firm>` before any ad-hoc run (flagless silently defaults to bd). `comp-validate <script> --artifact <file>` before signaling AE. |
| DE | `comp-transform schema-check` before touching data props; `comp-blast` before deleting. `comp-routes behaviors` for 4xx/auth debugging. **New cohort/metric/mode:** `comp-transform schema-check --feature [token]` + `comp-transform ternary-audit [Component]` at Phase 1. |
| DT | `comp-pipescript io <script> --pipeline <tree>` for every script deployed (**`--pipeline` REQUIRED — flagless is rc=2 REFUSED**). `comp-iam service <lambda>` after any new boto3 call **(necessary, NOT sufficient — see below)**. `comp-routes behaviors` before CloudFront / Lambda@Edge changes. |
| AE | `comp-pipescript deployed` before every gold-run trigger. `comp-pipescript postdeps <script> --firm <firm>` before any gold run (flagless silently defaults to bd). `comp-iam gaps` after any `iam.tf` change **(necessary, NOT sufficient — see below)**. `comp-blast` on infra before changes. |
| RD | `comp-transform fields` for every component rendering data. |
| COO | `comp-pipescript overlap A B` before authoring cross-domain coordination. `comp-blast` + `comp-routes` + `comp-cache` before decomposing PRDs into TOs. |

> **`comp-validate` returning `NO_CONFIG` or `ZERO_CHECKS` means UNVALIDATED — NEVER signal SAFE on it.** Only
> `PASS` / `WAIVED` are safe; `ADVISORY` means read the WARNs. *A script with no validate config produces an
> output that looks like a pass and asserts nothing.*

**Archetype tag.** Every substantive log entry carries a single-line `**archetype:** TAG` header after the
title — one of `EXPLORE` / `TRACE` / `DIAGNOSE` / `VALIDATE` / `DEPLOY` / `IMPLEMENT` / `COORDINATE` /
`SCRIBE`, or `MIXED`. Under-classifying is fine; no scoring. It feeds the stimulus-scan's cost signal.
Taxonomy: `org/tier0/COMPILER_ARCHETYPES.md`. Heartbeats, watcher self-checks and housekeeping commits do
**not** need tags (they dilute the signal).

---

## Task orders

Full template + filename convention: `org/ref/TASK_ORDER_PROTOCOL.md`. Stored in the receiving agent's
`task_orders/` folder.

**Statuses:** `staged` = assigned, wait for GO · `pending` = active · `complete` = done (self-marked) · **`superseded` = the NEED WAS MET ANOTHER WAY (name what superseded it)** · **`cancelled` = the NEED WENT AWAY, a ruling killed it (cite the ruling)**. The last two are set by **COO or the ISSUER, never the assignee alone**, and a terminal status **without its pointer is the rot with a tidier label**.

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
| Times to Andrew | US Eastern only (never UTC) |
| MCP server | `org/mcp/server.py` — `opal-agent-comms` |
| Broker | Auto-launched by `register_agent`, port 7800 |
