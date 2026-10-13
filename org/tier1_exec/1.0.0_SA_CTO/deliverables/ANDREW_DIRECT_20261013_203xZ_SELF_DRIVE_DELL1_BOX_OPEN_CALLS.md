# ANDREW DIRECT -- /self-drive on dell1's open calls, 60m loop (2026-10-13 ~20:3xZ) -- ARMING RECORD

**Channel:** Andrew at the laptop, relayed by `0.0.0_AB_MSTR` (laptop) to `0.0.0_AB_MSTR~DELL1` (bus 08c62bb9), dell1 msg 5153 to `1.0.0_SA_CTO~DELL1`. **Verbatim:**

> ON, 60m loops for /self-drive, /canonical-drive, /govern for the relevant agents. CTOs on each box should have /self-drive loop on their entire box, i.e. any open-calls that appears on that box they need to adjudicate.

The cloud switch is ON for scan and empty_tick on all four boxes (set 20:34:07Z, read back by MSTR).

## ARM TERMS

| term | value |
|---|---|
| driver | `1.0.0_SA_CTO~DELL1` |
| scope | **dell1's whole box**: every open call on `org/devices/state/dell1/open_calls.json`, plus every call that reaches this seat (inbox, slugs, packets, project `blocking` fields) for a project placed on dell1 |
| cadence | 60 minutes (cron, session-only; this record is the durable carrier) |
| call routing | Step 1 of `/self-drive`: the driver rules every call on its REC; design forks get CRO research first; governance forks go to `3.0.0_SA_CVO`; a needed seat is asked of `0.0.0_AB_MSTR~DELL1` |
| acts listed for Andrew | only an act only he can perform, each with its citation (a never-widen signature of his, a login or MFA, a vendor use no word of his names, spend beyond his grants, lifting a hold he set by name). Decisions are never listed |
| paired_with | the dell1 COOs' `/canonical-drive` 60m loops, which Andrew armed in the same word (relayed by MSTR); they are not cut by this loop |
| stop-condition | Andrew's stand-down word. A box has no DONE in the register sense; the loop runs while the box carries work, and HELD-AT-STOP applies if only unreachable calls remain |
| logs | `org/tier1_exec/1.0.0_SA_CTO/logs/2026-10-13/DELL1_self_drive_box_tick{N}.md`, delta-driven, at least hourly when anything moved |

**State: ARMED** at commit.

-- 1.0.0_SA_CTO~DELL1
