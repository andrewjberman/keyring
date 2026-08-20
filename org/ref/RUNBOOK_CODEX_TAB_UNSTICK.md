# RUNBOOK — unsticking a Codex CLI lane stuck at a terminal approval prompt

**When to use:** a Codex CLI lane (file-direct channel, no MCP) goes file-and-message silent
mid-session. Root cause with high recurrence: Codex's per-command approval mode re-fires on repo
tools during any long lane session, and the lane sits turn-starved at a numbered prompt until a
human keys the approval. First exercised 2026-08-20 (both ATOM_LAYER0 lanes, ~60 min starved;
~A confirmed resumed on this procedure at 1721Z).

**Precondition (load-bearing):** the Codex tabs are TITLED WITH THEIR LANE SERIALS at creation
(Windows Terminal `suppressApplicationTitle: true` pins the creation title). This is what makes
positive per-tab identification possible — an untitled tab reads as the profile default and can
only be identified negatively. State the convention at instantiation: title every Codex tab
with its serial.

**Diagnosis before acting:** turn-starvation reads as (a) unconsumed inbox files accumulating
for the lane, (b) zero artifact changes since the stall time. Confirm both; a lane mid-long-turn
shows (a) without (b) and needs no unstick.

**Mechanism facts:** all agent terminals are top-level windows of ONE WindowsTerminal process;
a window's TITLE FOLLOWS ITS ACTIVE TAB. So a background tab is reached by focusing its window
and cycling tabs (Ctrl+Tab), reading the window title after each switch — the title IS the
positive identification.

## Procedure (PowerShell, from any harness seat)

1. **Enumerate windows** via user32 `EnumWindows` (visible, titled) — `Get-Process`
   MainWindowTitle shows only one window per process and is insufficient.
2. **Focus the hosting window**: `ShowWindow(hwnd, 9)` (restore) + `SetForegroundWindow(hwnd)`;
   then **verify** `GetForegroundWindow() == hwnd` — ABORT before any keystroke if focus did
   not land or is later stolen (a keystroke into an arbitrary window is an uncontrolled input).
3. **Cycle tabs**: `WScript.Shell.SendKeys('^({TAB})')`, sleep ~600ms, re-read the window title.
   Stop when the starting title reappears (full cycle) or after a sane cap.
4. **On a tab titled with a Codex lane serial**: re-verify foreground, then
   `SendKeys('1{ENTER}')`. One tab at a time; never send into a tab whose title you have not
   positively matched.
5. **Cycle home** and report. **Success oracle is consumer-side, never the keystroke**: the
   lane's queued inbox count drops and it messages its base per protocol. A lane that does not
   resume within ~10 min either sat at a differently-shaped prompt (the "1" landed in its input
   buffer — harmless, visible in its next turn) or needs a human look at that specific tab.

**Cautions carried from the first exercise:** Ctrl+Tab is a WT-level binding and never reaches
the tab's application — cycling through live agent tabs is safe. A stray "1"+Enter into a
non-prompting Codex tab submits "1" as chat input — harmless, but say so in the resumption read.
The procedure steals the operator's desktop focus for its duration — run it only on an
operator's ask or with their knowledge.

**Reference implementation:** the 2026-08-20 session transcript (MSTR, ~1712Z) — EnumWindows
P/Invoke + focus-verify loop + SendKeys, ~30 lines of PowerShell, no dependencies.
