---
name: unstick
description: Unstick an agent whose terminal tab is turn-starved at a numbered approval prompt (Codex CLI permission prompts are the recurring case) by locating that tab BY TITLE and sending the approval keystroke. Bare `/unstick <serial>` locates the serial-titled tab across all terminal windows and sends "1"+Enter with foreground-verify + abort-on-steal; `/unstick <serial> --dry-run` locates and reports only; `--keys '<seq>'` sends a different answer. Operator-initiated (it briefly steals desktop focus). Engine `.tools/unstick.ps1`; runbook org/ref/RUNBOOK_CODEX_TAB_UNSTICK.md.
---

# /unstick — answer a stuck terminal tab's approval prompt, by serial

**The maneuver (Andrew-commissioned 2026-08-20, first exercised on the ATOM_LAYER0 Codex
lanes):** agent terminals are top-level windows of one WindowsTerminal process, and **a
window's title follows its ACTIVE tab** — so the target tab is located by exact title match:
either a window already titled with the serial (active tab), or found by focusing each
terminal window and Ctrl+Tab-cycling while reading the title after every switch. The
keystroke goes ONLY to a tab whose title exactly matches the serial, with the foreground
re-verified before every send.

## Invocation

| Form | Behavior |
|---|---|
| `/unstick <serial>` | Locate the serial-titled tab, send `1`+Enter. |
| `/unstick <serial> --dry-run` | Locate + report the tab; send nothing. |
| `/unstick <serial> --keys '<seq>'` | Send a different answer (SendKeys syntax, e.g. `'2{ENTER}'`, `'y{ENTER}'`). |

Execute: `powershell -NoProfile -ExecutionPolicy Bypass -File .tools\unstick.ps1 -Serial <serial> [-DryRun] [-Keys '<seq>']`
Exit codes: 0 sent/located · 2 not found · 3 focus-steal abort · 4 bad serial.

## Before invoking (diagnosis — do not key a healthy seat)

Turn-starvation reads as BOTH: (a) unconsumed inbox files accumulating for the lane AND
(b) zero artifact/message activity since the stall. A lane showing (a) without (b) is
mid-long-turn and needs no unstick. The recurring root cause is Codex's per-command
approval mode re-firing on repo tools during long lane sessions.

## Preconditions + cautions (all load-bearing)

- **The tab must be TITLED with the lane serial at creation** (WT `suppressApplicationTitle`
  pins creation titles). Untitled tabs are correctly NOT found — title every Codex/lane tab
  with its serial when instantiating; that convention is what makes positive identification
  possible.
- **Operator-initiated only.** The procedure steals desktop focus for its duration
  (~seconds) and ends with each cycled window back on its original tab.
- **A seat not actually at a prompt** receives the keys into its input buffer (submitted as
  chat input — noisy, not destructive). That is why the diagnosis step is not optional.
- **Success oracle is CONSUMER-SIDE, never the keystroke**: the tool proves delivery to the
  identified tab; resumption = the lane consuming its queued inbox + messaging its base
  (its coordinator's watcher fires). No resumption in ~10 min → a differently-shaped prompt;
  a human looks at that specific tab (try `--dry-run` first, then a different `--keys`).

## Report

One line per act, from the engine's own output: `SENT '<keys>' to '<serial>' (tab N of
window H)` / `DRY-RUN: located ...` / `NOT FOUND` / `focus stolen -- nothing sent`. Relay
the result to the lane's coordinator (base seat), who owns the resumption confirm.

## Cross-references

- Engine: `.tools/unstick.ps1` (the only mechanism; this doc adds no second path).
- Runbook + first-exercise record: `org/ref/RUNBOOK_CODEX_TAB_UNSTICK.md`, LD-0430.
