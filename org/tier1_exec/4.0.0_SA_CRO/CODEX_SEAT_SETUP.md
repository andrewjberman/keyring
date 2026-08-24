# CODEX SEAT SETUP — read this if you are a Codex agent on a CRO lane

**Why this file exists.** A Codex seat does not get the Claude harness's `/watcher` skill, the Monitor
tool, or automatic broker registration. Everything the harness does for a Claude seat, you do by
hand. The first two Codex seats on this lane (`~A`, `~B`, 2026-08-24) each spent startup time
re-deriving the same four things. **This file is so the third one does not.**

Every command below was **run and verified** by `4.0.0_SA_CRO~B` on 2026-08-24, and the paths were
independently re-checked by base CRO before this file was written.

---

## 1. Register on the broker

Registration makes you visible on the live-agent roster. **It is optional for comms and worth doing
anyway** — filesystem delivery works without it (verified both directions), but a seat absent from
the roster reads as not-present to every other agent.

```
# Terminal 1, from the workspace root:
cd C:\Users\AndrewBerman\Desktop\ajb_workspace
python -i

# At the Python prompt:
import asyncio; from org.mcp import server as comms
print(asyncio.run(comms.register_agent("<YOUR_FULL_SERIAL>", summary="Starting Codex session")))
```

Expected receipt begins `Registered <serial> as live` … `Broker: connected (port 7800)`.

⛔ **KEEP THAT PYTHON PROCESS OPEN. Its PID owns the registration.** Close it and you are gone.

⛔ **USE YOUR FULL SUFFIXED SERIAL** — `4.0.0_SA_CRO~A`, never the base. Registering under the base
serial means your lane inbox is never watched and you silently miss every message addressed to you.

## 2. Heartbeat — NOT optional, and this was learned the hard way

```
# Every 30–60s while working, from the SAME Python prompt:
print(asyncio.run(comms.heartbeat("<YOUR_FULL_SERIAL>", summary="WORKING: <current task>")))
```

**Registration is one-shot; liveness is not.** `~B` registered, did not heartbeat, and went STALE on
the roster in **187 seconds**. Worse, and this is the part worth knowing: **once past the liveness
threshold, `heartbeat` itself returned "not registered"** — they had to re-run `register_agent`. So a
missed heartbeat is not a cosmetic lapse; it drops you off and then the obvious recovery call fails.

## 3. Arm your inbox watcher

```
# Terminal 2, from the workspace root:
bash .tools/inbox-watch <YOUR_FULL_SERIAL> stream
```

`.tools/inbox-watch` is a shim to `org/mcp/inbox-watch.sh`. A serial **with** a `~suffix` watches
**only** the nested lane dir, strictly isolated from the base and from sibling lanes — so filesystem
routing alone makes every message in your watched dir unambiguously yours.

## 4. ⛔ THE INBOX PATH — the one that silently swallows mail

| | path | |
|---|---|---|
| lane serial | `org/mcp/inbox/{base}/~{lane}/` | ✅ **CANONICAL — NESTED** |
| lane serial | `org/mcp/inbox/{base}~{lane}/` | ⛔ **NEVER. INVISIBLE TO THE ENTIRE FABRIC.** |

**The trap is substitution.** For a lane serial, `inbox/{serial}/` *is* the dead flat path. Split your
serial into `{base}` + `~{lane}` before building any inbox path; never paste the whole serial into a
`{serial}` slot.

**An empty flat dir for `~A` exists on disk right now** (residue, 2026-08-18). Its presence is not
evidence it is used. Nothing writes it, nothing reads it, and a message placed there is delivered to
nobody and reported missing by nothing.

*Scope: this rule is about INBOXES ONLY. Your agent FOLDER under `org/{tier}/` uses the FLAT form —
`org/tier1_exec/4.0.0_SA_CRO~A/` — and there substituting the whole serial is correct. The two
families use opposite forms; do not carry one rule across.*

## 5. Comp-tools do not resolve bare in PowerShell

Measured by `~B`: **PowerShell resolves 0 of 102 bare `comp-*` tools.** The `~/bin` forwarders reach
Git-Bash shells, not PowerShell.

Use an explicit interpreter and path:
```
python .tools/comp-which "<plain-English question>"     # NOT: comp-which "..."
bash   .tools/comp-kuzu  "MATCH ..."                    # comp-kuzu is BASH
python .tools/comp-state --self-test                    # comp-state is PYTHON
```

⚠ **The tools are not uniformly one language.** `comp-kuzu` is bash; `comp-state` is Python. Invoking
either through the wrong interpreter fails loudly — a cascade of shell syntax errors, or a Python
`SyntaxError` on a bash line. Both failures cost seconds. **The expensive failure is the one that
returns a well-formed answer to the wrong question**, so when a tool errors, read the error rather
than reaching for the other interpreter reflexively.

## 6. Acknowledge by naming contents, not by confirming receipt

There are three different clocks and this estate has repeatedly conflated them:

| clock | what it proves |
|---|---|
| a file exists in your inbox | **SENT** |
| your watcher moved it to `read/` | **EMITTED** — a watcher acted, not an agent |
| you name something from inside it | **READ** — the only one an orphan cannot forge |

**So: ACK by naming a specific item from the message body.** "Received" and "acknowledged" prove
nothing that a dead watcher could not also produce. `~A`'s first ACK named four decisions and the
first act; `~B`'s named the three duplication acts. Both closed the clock properly.

## 7. What you still owe that the harness would have done for you

- **Read `org/XXX.md`** — the startup protocol. All of it.
- **Write your session serial file** (XXX.md Step 1b A.1) if `CLAUDE_CODE_SESSION_ID` is set.
- **Check BOTH inbox probes** — the filesystem dir *and* broker status. Each reads only one surface.
- **Run `to-check.py --all --assignee <your full serial>`.** `--all` is load-bearing; the default view
  hides TOs whose project PRD has aged out, which are exactly the ones stalled longest.
- **Arm zero crons.** Loops are operator-initiated, every serial, no exception.

---

*Authored 2026-08-24 by `4.0.0_SA_CRO` from `~B`'s verified sequence plus base re-checks. If a command
here fails, that is a defect in this file — report it rather than working around it, because the next
Codex seat will hit the same thing.*
