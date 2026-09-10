# CODEX SEAT SETUP — read this if you are a Codex agent on a CRO lane

**Why this file exists.** A Codex seat does not get the Claude harness's `/watcher` skill, the Monitor
tool, or automatic broker registration. Everything the harness does for a Claude seat, you do by
hand. The first two Codex seats on this lane (`~A`, `~B`, 2026-08-24) each spent startup time
re-deriving the same four things. **This file is so the third one does not.**

Every command below was **run and verified** by `4.0.0_SA_CRO~B` on 2026-08-24, and the paths were
independently re-checked by base CRO before this file was written.

---

> ⛔ **SECTIONS 1–3 WERE REWRITTEN 2026-09-10 by `1.0.0_SA_CTO` (doc-gate act). AS AUTHORED
> 2026-08-24 THEY WERE ARMED AGAINST YOU.** Old §3 told you to run
> `bash .tools/inbox-watch <SERIAL> stream`, which `org/mcp/CODEX_INBOX_MONITOR.md:47` and
> `org/XXX.md`'s Codex block both **FORBID on the Codex path** — it is a CONSUMING watcher.
> `inbox-watch.sh:120` does `mv "$msg" read/` and only then `:124` echoes the notification. You have
> no Monitor to receive that echo, so the move — **which commits the theft** — happens and nothing
> tells you. **You would drain your own mail into `read/` and read healthy on every probe you have.**
> Old §§1–2 hand-rolled registration and heartbeat in a `python -i` prompt, which the launcher now
> owns; running your own is the duplicate the doctrine names. Found by `4.0.0_SA_CRO` at its own
> startup — the only place it was findable.

## 1. Registration and heartbeat — THE LAUNCHER OWNS BOTH. Do not hand-roll them.

**`org/mcp/codex-agent-heartbeat.py` registers your full serial and maintains the broker and liveness
heartbeats** (`CODEX_INBOX_MONITOR.md:42`). **The launcher starts it.** Your job is to CONFIRM it is
running under YOUR full suffixed serial, not to start a second one.

⛔ **Registration is NOT optional.** The older text here said it was. It is not: an inbox is a
per-recipient slice, and a seat that is not on the roster is not merely invisible — mail addressed to
it gets no bounce, no ack and no staleness signal, and reads as delivered to the sender.

⛔ **USE YOUR FULL SUFFIXED SERIAL** — `4.0.0_SA_CRO~A`, never the base. Under the base serial your
lane inbox is never watched and you silently miss every message addressed to you.

⛔ **DO NOT START A SECOND HEARTBEAT.** If liveness looks wrong, verify which process holds your
serial before launching anything: two heartbeats on one serial is an identity conflict, not redundancy.

**Why liveness is not one-shot — keep this, it was paid for.** `~B` registered, did not heartbeat, and
went STALE in **187 seconds**. Worse: **once past the liveness threshold, `heartbeat` itself returned
"not registered"** — recovery required a fresh `register_agent`. A missed heartbeat drops you off *and
then the obvious recovery call fails*. That is why the launcher owns this and you confirm rather than
improvise.

⚠ **A known recovery gap, measured 2026-09-10 by `3.0.0_SA_CVO` under Andrew-direct repair
authorization:** the shared heartbeat refreshes LOCAL liveness and ignores the broker's response, and
the broker returns OK even when its UPDATE matched no row — while the Codex companion re-registers
only when the LOCAL entry is missing. **So a lost BROKER row with surviving LOCAL liveness had no
recovery path.** Repair was in progress at that date; if your mail stops arriving while every local
probe reads healthy, this is the shape to suspect.

## 2. Arm the NON-CONSUMING detector — never the stream watcher

**`org/mcp/codex-inbox-monitor.py` is the REQUIRED detector** (`CODEX_INBOX_MONITOR.md:41`). It emits
root-level `[HARD-NUDGE] <filename>` **without reading, moving, deleting or ACKing** your mail. **The
turn bridge starts it; do not launch a duplicate.**

⛔ **NEVER run any of these on the Codex path** (`CODEX_INBOX_MONITOR.md:47-53`):

| tool | why |
|---|---|
| `org/mcp/inbox-watch.sh ... stream` (and the `.tools/inbox-watch` shim) | CONSUMING — moves mail BEFORE notifying |
| `org/mcp/check-inbox.sh` | CONSUMING — consumes mail during a check |
| `org/mcp/agent-poller.py` | Claude lifecycle; its inbox companion is consuming |
| a second `codex-inbox-monitor.py`, or the old `notify()` / `yield_control()` bridge | duplicate |

**Your read discipline instead:** at every active turn, sweep your suffixed serial's unread root
first, read the exact file, ACK, act, then move it to `read/` yourself. **Never infer READ from a
nudge or from a moved file** — see §6, which is correct as written and unchanged.

## 3. Lane isolation still holds, and it is the useful half of the old §3

A serial **with** a `~suffix` addresses **only** the nested lane dir, strictly isolated from the base
and from sibling lanes — so filesystem routing alone makes every message in your watched dir
unambiguously yours. That was true before this rewrite and is unchanged by it; only the tool you point
at that dir has changed.

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

> ⚠ **OPEN QUESTION, NOT RESOLVED, 2026-09-10.** `4.0.0_SA_CRO` reported that this section contradicts
> the launcher's bare comp shims. `1.0.0_SA_CTO` re-measured in a plain PowerShell session on this
> device and got **0 of 4 sampled bare `comp-*` resolving** — which CORROBORATES the text below rather
> than contradicting it. The two readings are not in conflict if the LAUNCHER's environment differs
> from a plain shell, and that environment is not observable from the CTO seat. **Left as written and
> flagged rather than "fixed" on an unverified report:** the seat that sees the launcher's own PATH
> should settle it and edit this section. Do not assume either way; run the check in YOUR shell.

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

*§§1–3 rewritten 2026-09-10 by `1.0.0_SA_CTO` as a doc-gate act, on `4.0.0_SA_CRO`'s startup finding
and with `2.0.0_SA_COO`'s disposition (95134 §4) that it lands here rather than as a cell. §5 flagged
open, not edited. The defect was ARMED — the old §3 pointed the one class of seat that cannot survive
it at a CONSUMING watcher — and it was found only because a seat followed its own setup file and
reported the contradiction instead of working around it, which is exactly what the paragraph above
asks for. **This file is normative for a CRO Codex seat but it is NOT the authority: `org/XXX.md` and
`org/mcp/CODEX_INBOX_MONITOR.md` are. Where this file disagrees with either, THEY WIN and this file is
the defect.***
