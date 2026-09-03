---
name: unstick
description: Unstick a turn-starved agent terminal tab (Codex lanes are the recurring case) by locating it by title and sending keys. Two shapes -- PROMPT-STUCK: bare `/unstick <serial>` sends 1 + Enter; IDLE-AT-INPUT: `/unstick <serial> --keys '<prompt>{ENTER}'` nudges it. `--peek` captures the tab to a PNG and sends nothing (read it; re-peek after any send); `--dry-run` locates only. Operator-initiated (it briefly steals focus). Engine `.tools/unstick.ps1`; runbook org/ref/RUNBOOK_CODEX_TAB_UNSTICK.md.
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
| `/unstick <serial> --peek` | Locate + focus the tab, **capture the window to a PNG, send NOTHING** — then the invoking seat READS the image and reports what the tab actually shows (the exact prompt text, or proof the seat is not stuck at all). **Peek before keying when the prompt shape is unknown.** |
| `/unstick <serial> --dry-run` | Locate + report the tab position only; no capture, no keystrokes. |
| `/unstick <serial> --keys '<seq>'` | Send a different answer (SendKeys syntax, e.g. `'2{ENTER}'`, `'y{ENTER}'`). |
| `/unstick <serial> --keys '<prompt text>{ENTER}'` | **NUDGE an IDLE-AT-INPUT lane** (the dominant Codex stall, measured 2026-08-20: clean completion, then mail arriving AFTER its last inbox read — a Codex lane takes no turn to notice new mail). The engine types the body, PAUSES, then sends Enter as a SEPARATE act — **an Enter inside the keystroke burst is a paste-NEWLINE and never submits** (measured: the prompt sat unsubmitted in the composer through three peeks while the operator reported it submitted). SendKeys escapes apply to the body: `(`→`{(}`, `)`→`{)}`, and no `~ + ^ %`. |

Execute: `powershell -NoProfile -ExecutionPolicy Bypass -File .tools\unstick.ps1 -Serial <serial> [-Peek] [-DryRun] [-Keys '<seq>'] [-OutFile <png>]`
Exit codes: 0 sent/located/peeked · 2 not found · 3 focus-steal/capture abort · 4 bad serial.
Peek default output: `$env:TEMP\unstick_peek_<serial>_<utc>.png` (path printed) — **Read the PNG in the same turn**; a peek nobody reads answered nothing. First peek exercise (2026-08-20): resolved a watched lane as COMPLETE-not-stuck, retiring a pending second-look.

## Before invoking (diagnosis — do not key a healthy seat)

Turn-starvation reads as BOTH: (a) unconsumed inbox files accumulating for the lane AND
(b) zero artifact/message activity since the stall. A lane showing (a) without (b) is
mid-long-turn and needs no unstick. **Two stall shapes, two keys — peek to tell them apart:**
- **PROMPT-STUCK** (Codex's per-command approval mode re-firing on repo tools): the peek shows
  a numbered approval prompt → `1`+Enter (or the right number).
- **IDLE-AT-INPUT** (the dominant shape, 2026-08-20 2159Z on both CRO Codex lanes): the peek
  shows a finished turn ("Worked for Nm") with an EMPTY composer and "no unread messages
  remain" — while its base measures unconsumed files that landed AFTER that read → a
  **NUDGE** (`--keys '<prompt>{ENTER}'`), never `1` (which would type a stray "1").

**Verify the submit on a SECOND peek ~1 min later.** Submitted = the prompt appears as a
transcript turn above an EMPTY composer, with a `Working (Ns · esc to interrupt)` line. Two
byte-identical peeks after a send = the text is sitting in the composer — send a lone
`--keys '{ENTER}'`. (The engine now splits body and Enter itself; the second peek is still the
oracle, because the keystroke proves delivery, not submission.)

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
