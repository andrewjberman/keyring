---
name: drive-mode
description: Arm, end, hold or read the MODE LEASE that picks a project's driver -- FAST (Andrew present; the seat builds directly under /closer-drive) or FULL (the default; /canonical-drive). `/drive-mode <CODE> fast [2h] --surface <dir> [--seat <serial>]`; `/drive-mode <CODE> full`; `/drive-mode <CODE> hold`; `/drive-mode status`. Fail-closed to FULL; the one refusal is a surface another driver already holds. Any seat, on Andrew's word.
---

# /drive-mode -- which driver runs a project right now

Authority: report 2 (RCN-0017) C1 and calls 1, 2, 3, 5, 6, approved by Andrew 2026-09-24, record
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md`.
Spine: the Closer subsection, FAST mode. Engine: `.tools/drive-mode.py` (`--self-test` must print ALL HOLD).

## Forms

| Form | Does |
|---|---|
| `/drive-mode <CODE> fast [Nh] --surface <dir> [--surface <dir>] [--seat <serial>]` | `python .tools/drive-mode.py arm <CODE> --surface <dir> [--hours N] [--seat <serial>] --by <who>`. Default 2 h. The seat defaults to the caller. |
| `/drive-mode <CODE> full` | `python .tools/drive-mode.py full <CODE>` -- ends the lease now; the project reads FULL. |
| `/drive-mode <CODE> hold` | `python .tools/drive-mode.py hold <CODE>` -- both drivers pause; its open orders stop counting as a driver. |
| `/drive-mode <CODE>` (read) | `python .tools/drive-mode.py read <CODE>` -- prints FAST, FULL or HOLD. |
| `/drive-mode status` | `python .tools/drive-mode.py status` -- every live lease: seat, surface, claims, expiry, overlaps. |

## What the lease is

- `org/mcp/drive_mode/<CODE>.json` in the MAIN worktree, device-local and gitignored. Every arm, end, hold and lapse
  appends one line to `org/mcp/drive-mode.log`, which is committed with the seat's record batch.
- **It fails closed to FULL.** Absent, expired or unreadable reads FULL, so a forgotten FAST lapses by itself.
- **Presence (call 1):** while `org/mcp/presence/*.last` is under 30 minutes old, a live lease extends. The stamp is
  written by a UserPromptSubmit hook (0.0.0_AB_MSTR's lane). Without the hook, the lease runs its stated length.
- **Rail (call 6):** `read`, run by the lease's own seat, mirrors a live FAST lease into that session's `/freeform`
  marker, so the comp-tool search rail stands down for the lease's life. Every safety gate stays armed.
- **One seat per project.** A lease names one seat and its surface: a directory or package, e.g.
  `portal/src/pages/InvestorReporting`.

## The one refusal

`arm` refuses a surface that overlaps another live FAST lease, or another project's open task order `<paths>`. A
project under HOLD is excluded. It prints each overlap.
- You resolve it: `/drive-mode <OTHER> hold`, or a narrower `--surface`.
- It runs only when a lease is armed; it is not a standing gate.

## After arming

Tell the seat, or let its next tick read it: `/canonical-drive` reads the lease first, and FAST runs `/closer-drive`.
The seat runs the FULL -> FAST boundary act in `/closer-drive`. It needs no re-arm and no hand-over.
