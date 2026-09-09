# 4.0.0_SA_CRO — 2026-09-09 15:00–16:10Z — a dead MCP client at load, the Python 3.12-vs-3.14 question settled on measurement, and the machine act delivered by a DT in an elevated shell

**archetype:** MIXED
**secondary_archetypes:** DIAGNOSE, COORDINATE, VALIDATE

**Date:** 2026-09-09 · **Task Order:** ad-hoc (Andrew-direct, record @fc93ef9dbe) · **Status:** IN PROGRESS (Codex half open)
**Serial:** 4.0.0_SA_CRO (base) · **Session:** `419450b8-4a74-436e-b9a0-c036733d4e68`, registered PID 1548 via the broker LIBRARY (the MCP client is dead this session)
**Window:** 15:00Z → 16:10Z · **Commits (mine): 1** (`fc93ef9dbe`) · **MCP: 4 in / 6 out** (out via the library, not the tool) · **Deploys: 0**

## Objective

Come up reachable, then answer Andrew's word: *"clean and clear on what python version we are using"*, jointly with `1.0.0_SA_CTO~X` (Codex), acceptable to both harnesses.

## What happened

### 1. Load: `opal-agent-comms` CONNECTION_CLOSED, cause measured in one call
`.mcp.json` launches `python org/mcp/server.py`; bare `python` resolved to `C:\Program Files\Python314` (site-packages = pip only; tree written 12:30Z today), and `server.py:46` died on `import mcp`. Python 3.12 (310 packages incl. `mcp` 1.26.0, `websockets` 16.0, `PyYAML`) sat second on PATH. The broker daemon on :7800 was up. Recovery, same shape `2.0.0_SA_COO~A` used at 14:47Z: a scratchpad `heartbeat_loop.py` importing `server as comms` under Python 3.12, run under a Monitor (`bk9pi7it9`), registered PID 1548 and heartbeats every 45 s; one-shots (`get_delivery_state`, `ack_messages`, `send_message`) through a sibling script after `comms._ensure_broker()`. Inbox Monitor `btdbry9ld` armed (parent-tied pid 450719), confirmed by a live `[INBOX]` event. Delivery ledger since 09-03: 78 of 78 READ after acking `94475`. Memory entry written for the recovery recipe.

### 2. Andrew-direct 15:2xZ, recorded verbatim @`fc93ef9dbe`, broadcast to CTO/COO/MSTR
Two false starts, both mine: four sends refused because my one-shot passed the recipient in `send_message`'s `from_agent` slot (the identity guard did its job); fixed with `from_agent=""`.

### 3. The measurement (denominators in the request to `1.0.0_SA_CTO~X`, msg 15:30Z)
- 3.12: user install (2025-10-27), USER PATH, 310 packages. 3.14.7: all-users install TODAY (InstallDate 20260909, python.org bundle, no Intune footprint), MACHINE PATH via its "Add to Path" component. **Windows resolves machine before user PATH, so no user-scope act could fix it** — the fact that turned "re-order PATH" into "elevated act".
- Estate declares: no `pyproject`/`.python-version`; `requirements.txt` inventory (83 pkgs, `mcp>=1.2.0`); commit gate `ruff --target-version py39`; 309 Lambda `runtime` declarations, values 3.9/3.11/3.12, none above. Nothing needs 3.14.
- Bare-`python` sites: `.mcp.json` ×2, `settings.json` hooks ×2, `start-codex-seat.ps1` ×6, `codex-send.ps1`, `codex-seat-status.ps1`. `ajb.ps1`/`ajb2.ps1` touch neither PATH nor python.
- `py` launcher ignores `.python-version` here (tested); `py -3.12` works.
- **`1.0.0_SA_CTO~X` was never provisioned**: its runtime dir shows heartbeat dead on `mcp`, turn-bridge dead on `websockets`, no `bridge-state.json`; Andrew's paste of the launcher's FAILED COMPONENT throw confirmed it. My request sits in its inbox for its first load.

### 4. The act: `0.3.0_DT_TradingOperations`, elevated shell, on my brief
Brief's option A named two artifacts (Settings ARP row; cached bundle exe) that did not exist on this device — a defect of the brief. The DT uninstalled by MSI product code; the Standard Library MSI crashed `msiexec` (STATUS_STACK_OVERFLOW) twice and its rollback briefly restored a 3.14 that could not boot; the DT finished the removal and hand-edited the two machine PATH entries, disclosing the bad window. Report `94545` **validated three ways with different instruments**: DT (fresh-PATH child, real MCP initialize + tools/list = 16), CTO `94547` (registry read), me (registry read from a different process + a Git Bash child importing `mcp`/`yaml`/`websockets` under 3.12.10). Residue disclosed: one surviving MSI row ("Add to Path" {B591DE94…}) whose self-repair could re-add the entries; falsifier adopted. Inert `Python314` directory and `PythonCore\3.14` key stay pending Andrew's word on recursive deletion.

### 5. A wrong line of mine, refuted by my own negative control, corrected everywhere
Brief said "RESTART, never `/mcp` reconnect". With the exe removed, a stale PATH falls through to Python312: measured at my seat, then at the DT's (its own stale-PATH session, `which -a python` → one hit). Correction sent to DT, CTO, COO, MSTR; the DT withdrew the line itself (`94555`). Reconnect suffices; restart is merely unnecessary.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| `comp-read --enumerate` | `.claude/settings.json` 'python'; `CODEX_INBOX_MONITOR.md`; `server.py` (guard tokens) | PASS / PASS / ABSENT (correct: the guard lives in `cvo_send_guard.py`) | Enumerate gave the bare-`python` sites with line numbers and a denominator. |
| `comp-read --for` | `ADHC_BASHFIX.md` | PASS, low salience | Confirmed the doc is about bash utilities, not the interpreter; unread ledger printed. |
| `comp-find` | `runtime\s*=\s*"python3\.[0-9]+"` (309 hits); `requires-python\|target-version` (452); `--name '*codex*'`, `start-codex-seat*`, `ajb*`; 'python' over the Codex ps1s | PASS | The 309-declaration Lambda census is the load-bearing "nothing above 3.12" number. |
| `comp-find` | 'python' over `.tools/start-codex-seat.ps1` | `0 across 0 files` = OUT-OF-CORPUS (file lives in `org/mcp/`) | The zero was read as absence-of-file, not absence-of-term, per the rule; `--name` found it. |

**What worked.** `comp-read --enumerate` on the hooks config and `comp-find` on the runtime declarations gave denominators I could hand to two other seats unchanged. The identity guard and the LD-0529 worker guard both refused correctly; the second told me which tokens to drop ("RAVC", imperatives, "NOW").
**What failed.** Three of my Bash calls were rail-blocked for piping `comp-find` into `tail`/`grep`; the fix was `--limit` and splitting calls. `comp-find` over `org/mcp/inbox/.../read` returned page 1 of 6 for 'custodian' and I did not page it (the custodian item stays unrouted, stated as such).
**Gap found.** None in the tools. In the brief: option A named artifacts I had not verified exist (ARP row, cached bundle). A brief that names an artifact should have read it.

## MCP traffic

**In (4):** `94475` CTO Andrew-direct (L2 confirmed, nothing asked) · `94545` DT act report · `94547` CTO validation · `94555` DT correction. All READ-acked from their Msg-ID lines.
**Out (6, via the library):** request to `1.0.0_SA_CTO~X` (15:30Z) · broadcast CTO/COO/MSTR (15:30Z) · broadcast CTO/COO/MSTR follow-up with the reconnect correction (16:01Z) · ACK/close to the DT (16:03Z; first cut refused by the LD-0529 guard, recut act-free).

## Files Modified

`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260909_152xZ_PYTHON_VERSION_CLEAN_AND_CLEAR_CLAUDE_AND_CODEX_WITH_CTOX.md` @`fc93ef9dbe` (new). This log. Memory dir (untracked): one new reference entry + index line. Scratchpad (TEMP, not durable): `heartbeat_loop.py`, `comms_oneshot.py`, `summary.txt`, message bodies.

## Blockers

**NONE owned by this seat.** Sequence state, each with its holder:
1. **[Andrew]** relaunch `1.0.0_SA_CTO~X` with `ajb2` from a new shell; its reply is the Codex half of the joint answer.
2. **[Andrew]** `/mcp` reconnect in today's Claude sessions; word on deleting the inert `Python314` directory.
3. **[CTO lane + CRO, after 1]** the design half: a load-time interpreter guard for both harness startups (`XXX.md` A.3 + `start-codex-seat.ps1` preflight), never an absolute path (LD-0405). Proposed, not built.

## Current State

*For a reader with zero prior context.* Bare `python` on this device resolves to 3.12.10 in any process, old or new. Python 3.14 is removed except one inert MSI row, an empty directory tree, and a registry key. This seat is registered LIVE (PID 1548) through a library heartbeat under Monitor `bk9pi7it9`; its MCP client stays dead until Andrew reconnects it. Inbox Monitor `btdbry9ld` live. Zero crons. The base seat's 09-04 and 09-05 work has no session log under this folder (commits are the record); not chased this window. The 49F custodian answer from the 09-03 log is still unrouted, pending whether Andrew still wants it.

## Next Steps

1. **[4.0.0_SA_CRO]** on CTO~X's reply: reconcile its Codex-side measurement with mine, write the agreed text, carry it to Andrew with both serials on it; then the guard proposal to the CTO lane as a brief if Andrew wants it built.
2. **[Andrew]** items 1–2 under Blockers.
3. **[4.0.0_SA_CRO]** a `/log` covering 09-04/05 base-seat work, when there is a gap.

## Archetype rationale

**MIXED.** DIAGNOSE for the interpreter fault (one import, one registry read, one PATH-scope fact), COORDINATE for the four-seat round (CTO~X request, DT brief, three validations, two corrections), VALIDATE for the RAVC-4 close by different instruments and for the negative control that refuted my own restart claim. No build, no deploy.
