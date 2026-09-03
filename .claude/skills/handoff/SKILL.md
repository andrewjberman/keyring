---
name: handoff
description: Emit a REINSTANTIATION TEXT BLOCK so a fresh session of this seat (or a successor) resumes with zero ramp -- gate-forward (what is waiting on whom), self-scoped, grounded on hashes and artifacts. Bare `/handoff`; `/handoff brief`; `/handoff <CODE>`; `/handoff save` (persists to org/{tier}/{serial}/handoffs/). Not /log (the durable record) and not /overview (fabric status). Any agent.
---

# /handoff — reinstantiation text block

Produce the paste-block a fresh session needs to CONTINUE your work seamlessly. The reader has
done nothing yet and has none of your session context — the block must carry everything load-bearing:
who you are + standing mode, the live state, the ACTIVE WORK with its gates, **the decisions/blocks
waiting on whom**, the standing directives learned this session, and what YOU pick up first.

**It is not a status report and not the durable log.** `/overview` is human status; `/log` writes
the record. `/handoff` is optimized for one job: paste it into a fresh session and that session
resumes as if it never restarted. When the two overlap, `/log`'s "Current State (zero-context
handoff)" section is the SOURCE; `/handoff` distills it into a bounded, gate-forward block.

## Invocation forms

| Form | Behavior |
|---|---|
| `/handoff` | Emit YOUR full reinstantiation block now, in chat. No commit. |
| `/handoff brief` | The compact version — identity + standing mode + the live gates + the do-first queue. Drops the per-project detail. |
| `/handoff <CODE>` | Scope to ONE project/thread (e.g. `/handoff OPAL_TAXSMA_PT2`): that project's state + gates + next action only. |
| `/handoff save` | Emit the full block AND persist it to `org/{tier_folder}/{serial}/handoffs/{YYYY-MM-DD}_{HHMM}Z.md`, committed under your author line (durable continuity artifact). |

## Step 0 — Anchor, identify, scope

- **Anchor to base** (mechanical): `cd /c/Users/AndrewBerman/Desktop/ajb_workspace && git rev-parse --show-toplevel`. No agent is BASED in `portal/`; a lingering portal CWD silently feeds the wrong repo's history.
- **Serial:** your full registered serial INCLUDING any `~lane` suffix.
- **Scope:** default = your whole current working context (this session). `<CODE>` narrows to one project. `brief` narrows the DEPTH, not the topic.

## Step 1 — Gather the material (hot context first; safety-net pulls only if uncertain)

**Hot context IS evidence.** If the session's state is in your working context (the normal case),
write the block directly. The pulls below are the SAFETY NET for a compacted session, a long window,
or any gate you are not certain still holds:

```bash
# Your latest durable log — its "Current State" + "Next Steps" are the block's spine
ls -t org/{tier_folder}/{serial}/logs/*/ | head; # newest log file -> read Current State
# Live fabric (who is up, on what)
```
```python
get_live_agents()          # (MCP) live roster + one-line work summaries
get_org_summary()          # (MCP) active projects + pending TOs
```
```bash
git log --oneline --author="{serial}" --since="<session start>"   # what you shipped (hashes for the block)
```
Plus, if relevant to your lane: `deploy_ledger.py check --red` (open deploys), your staged/pending
TOs (`list_task_orders`), and the sovereign calls pending at Andrew (mentally, or `/open-calls`).

**Ground the load-bearing bits.** A gate that changes what the next session DOES must cite its holder
and, where it turns on a fact, a commit/artifact (`@hash`, an S3 key, a TO id). A stale gate in a
handoff sends the next session to work an already-closed decision — verify anything you are not certain
of against live state (broker / git / the artifact), not memory. **Uncertain > wrong:** mark a gate you
could not re-verify as `(unverified)` rather than assert it.

## Step 2 — Compose the block (bounded, gate-forward, ASCII)

Fill the template below. **Discipline:**
- **Gate-forward.** The `*** LIVE GATES ***` block is the highest-value content — every item names WHO
  holds it (Andrew / CTO / a serial / an external signal) and what unblocks it. If you cut for length,
  cut prose, never a gate.
- **Bounded.** A handoff is a distillation, not a log dump — aim for something a reader absorbs in under
  a minute. Point to the latest `/log` for full detail; do not reproduce it.
- **Do-first is the payload.** The `SELF DO-FIRST` list is what the fresh session executes in its FIRST
  turn — make it concrete and ordered.
- **Plain ASCII**, fenced as a code block so the human can copy it verbatim. No emojis.
- **Role-agnostic.** The template fits any tier — a DS lists its silver/gold + parity gates, an AE its
  deploys + IAM gates, an exec its dispatch threads + rulings. Keep only the rows you have.

### Template

```
=== {ROLE} SESSION HANDOFF — {YYYY-MM-DD} ~{HHMM}Z ({full_serial}) ===

ROLE / STANDING MODE: {one line — role + any standing order: loops on/off, reserved, drive OFF, etc.}
STARTUP: {what a fresh session must do first — /watcher, XXX.md Step-1b, session-serial file, Step-2b
          reconcile; plus any agent-specific first move.}

FABRIC (live, terse): {serials up + their current work in a few words each — only what you coordinate
          with or depend on. Note reserved sessions + dead-but-needed lanes.}

ACTIVE WORK: {per project/thread/TO you own or drive — one block each:}
- {CODE / thread}: {state in a phrase} @{hash where load-bearing}. GATE: {who holds it / what unblocks}.
  {owner/lane}. {next concrete step}.
- ...

*** LIVE GATES (what is waiting on whom — the load-bearing section) ***
- AT ANDREW: {each sovereign decision/word pending — the minimal ask + who is blocked by it}.
- AT {CTO / peer / external}: {each gate + what it unblocks}.
- AT SELF: {anything only you can resolve that is not yet done}.

STANDING DIRECTIVES (this session — a fresh session would not know these from the docs):
- {each new ruling / prohibition / staffing law learned this session, with its authority + scope}.

SELF DO-FIRST (the reinstantiation payload — execute in the first turn, ordered):
1. {concrete action} — {trigger/gate}.
2. ...

CARRIED (non-blocking): {items parked at Andrew/CTO that are not urgent}.
POINTERS: latest log @{hash}; {key artifacts / PRDs / ledgers the next session will open}.
=== END HANDOFF ===
```

## Step 3 — Emit (and optionally persist)

- **Default / `brief` / `<CODE>`:** print the block in chat inside a fenced code block. No commit — it
  is a view for the human / the next session to paste.
- **`save`:** ALSO write the block to `org/{tier_folder}/{serial}/handoffs/{YYYY-MM-DD}_{HHMM}Z.md`
  (create the `handoffs/` dir if absent) and commit it under your author line, pathspec-scoped, from the
  workspace root:
  ```bash
  .tools/safe-commit.sh --author "{serial} <{serial}@opal.agent>" -F <msgfile> \
    -- org/{tier_folder}/{serial}/handoffs/{date}_{HHMM}Z.md
  ```
  (Use `-F <msgfile>`, never `-m` with a backtick/`$(` — commit messages are an execution vector,
  CLAUDE.md Git / LD-0276.)
- Then `heartbeat("{serial}", summary="<one-line current state>")`.

## Report (end of every invocation)

```
/handoff {serial}
  MODE:  full | brief | scoped <CODE> | saved <path>@<hash>
  BLOCK: emitted in chat{ + persisted <path>}
  GATES: <N> live (AT ANDREW <a> / AT CTO/peer <b> / AT SELF <c>)
```

## Notes

- **Self-scoped.** You emit YOUR handoff — the continuity of YOUR working context. You cannot fully
  know a peer's session state, so `/handoff <other-serial>` is not a form; scope by PROJECT instead.
- **Not a substitute for `/log`.** The durable record is `/log`; if you are closing a session, run `/log`
  (which writes the Current State the block distills) and then `/handoff` for the paste-block. `/handoff
  save` persists the block but does not replace the canonical log.
- **Refresh, don't recycle.** A handoff written an hour ago is stale — regenerate from current state each
  time. The block is a snapshot; date/time-stamp it so a reader knows its vintage (a stale handoff asserts
  closed gates with authority — the same failure class the fabric guards against elsewhere).
- **Compaction-safe.** Because it grounds on the durable log + live broker + git, `/handoff` works after a
  context compaction — the safety-net pulls in Step 1 reconstruct what hot context lost.
