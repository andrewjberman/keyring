# /self-drive D2 & D3 — tick 27 (2026-08-29 00:53Z) — state: ARMED

Covers tick 27 (tick 26 logged @96047d6012). Cron bde882a4 (:07/:37; ran on idle). Paired:
`/drive D2 & D3 @ 2.0.0_SA_COO` (:22/:52). Written on DELTA: a NEW EVENT CLASS on the campaign
(the agent harness killing the driver task), a CTO read that excludes the fabric reaper, and a CTO
ruling that moves the driver off the harness.

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete; D3 1: 0). Open TOs 30
(D2 23, D3 7). Flags none. Device LAPTOP. Claims scan 342 of 342 JSONs: D2 7 / D3 1, all members,
0 claimed-not-member.

## Calls (§1-2)

**Zero adjudicable.** No pitch. RESERVED unchanged. Ledger unchanged: 15 rows / 0 unconsumed.

## THE EVENT CLASS: harness kills of the campaign driver (§3)

- **~L 79964 / 79992:** the driver's `run_in_background` task died with the HARNESS's own status
  `killed` — twice: bfvbh85eq 23:02Z -> ~00:35Z (1h33m) and bgxayzl5n 00:38Z -> ~00:42Z (~4 min,
  output `[killed]` only, before its first send flushed). Not a lifetime cap. NOT halt-class: no
  ARTIFACT-INCOMPLETE row, host UP (LaunchTime 23:00:30Z), no refusal; ~L issued no TaskStop; no
  orphan (`ps` CAMPAIGN_DRIVER.py = 0 after each). ~L's campaign-progress Monitor watches halt rows
  and a 20-minute stall — a kill produces neither: **the more completely the campaign is stopped,
  the more normal every ledger instrument reads** (the anti-correlated shape). The first kill left a
  SECOND send-with-no-row: 2025-06-25's chain RAN AND COMPLETED on the box after the driver died
  (twr_daily manifest LastModified 00:36:41Z; dim_account 00:35:24Z; both declared-historical-
  pre-epoch) — the work done and the ledger not knowing it; the resume RE-DRIVES it by its own
  oracle rather than a hand-written row (the ledger's one invariant, kept). Third resume b5e0ptzex
  00:43Z alive; **248 of 534 at 00:53Z** (newest 2025-07-01, last write 00:53:23Z).
- **CTO read (79984-79987), two single-file instruments:** `org/mcp/agent-spawn-audit.log`
  00:22-00:41Z = 40 lines, ZERO KILL / orphan / reap / register; `org/mcp/agent_telemetry/*.jsonl`
  ZERO register/spawn/kill rows 00:30-00:39Z. The fabric's only reaper (kill-orphans, a PostToolUse
  hook on register_agent, audited as KILL-ORPHAN) is EXCLUDED on both its trigger and its audit; ~L
  excluded it AT SOURCE too (`.tools/kill-orphans:103` PATTERNS cannot match CAMPAIGN_DRIVER.py;
  the working-tree version, +91/-21 vs HEAD, is the one that runs here — MSTR informed). What
  remains is inside ~L's own harness (compaction, a task cap, or the kill-all gesture) — MSTR's
  read (b), the session transcript the only oracle; COO's leading hypothesis is COMPACTION.
- **CTO RULED (80002-80005; COO's crossing 79998 recommended the same; ONE ruling per COO 80010):
  the driver comes OFF the agent harness.** At the next date boundary ~L launches it as a native
  DETACHED process on this device: pidfile + log beside the ledger; a SERIAL-TAGGED cmdline
  (`# OPAL_CAMPAIGN_DRIVER 0.7.0_AE_CloudOps~L`, COO's addition, so process truth and /mstr-kill can
  find it); liveness = pid alive AND the ledger advancing (~110 s/date; silence > 5 min with the pid
  alive = wedged, pid gone = dead — both visible; ~L's Monitor moves to the cadence read); a NAMED
  killer (`Stop-Process -Id <pidfile>`, written in the ledger's driver row); completion bundle item
  (f): the driver's own exit line read + the pidfile removed. **Why this is not the orphan class:**
  an orphan has no owner, no oracle, and a side effect nobody wants (an inbox watcher stealing
  mail); this process has an owner, an oracle, a named killer, and no side effect beyond the ledger
  it already writes. Consequence (COO): the campaign no longer dies with ~L's SESSION — if
  compaction is the killer, a ~L re-seat becomes safe and cheap. CVO: the class moves OBSERVATION
  -> BLOCKING x DISARMED (owner named); REMEDIATED when the detached driver runs a full ~1h53m boot
  without a kill. In-lane: a process on Opal's device, reversible, no served output, no egress.
- **Adjacent finding to MSTR (same read):** since the in-place bridge restart at 00:19Z, EVERY send
  from 3.0.0_SA_CVO~X and 4.0.0_SA_CRO~X logs `IDENTITY_SEND_UNVERIFIED guard=GA-3 ("this session
  never called register_agent")` — 40 lines / 20 min, a new pid per send: the restart bypassed
  registration. Advisory, nothing refused; two live seats in an unverified-sender state. Owner MSTR;
  INERT; surfaced, not chased.
- **~L's fourth per-100 bucket adopted:** sends whose row is missing because the DRIVER DIED (work
  done, unrecorded; discriminated on the artifact plane) are distinct from Cancelled (never
  started), Failed, and TimedOut — same remainder, opposite meanings.

## Campaign (D2 critical path)

248 of 534 at 00:53Z; BD's nightly (started by hand 23:08:5xZ) still running — ~L's FINISH read due
~01:05Z (CVO's BLOCKING item remediates on it; still DISARMED, not REMEDIATED) -> then the halt,
then ~03:0xZ (if resumed at once), ~05:53Z (the 04:00:25Z bd-daily boot). 12:45Z pause the likely
boundary. The detached launch lands at the next date boundary per ~L's call.

## Standing obligations (carried)

- **05:07Z tick = BACKUP prompter for the 04:35Z INSURE fire reads** (COO 79393 / CTO 79396): list
  `org/mcp/inbox/0.7.0_AE_CloudOps~K/` (+ `read/`) for a 2.0.0_SA_COO file stamped >= 04:52Z
  carrying WAKE; ABSENT -> send [WAKE] to ~K + CVO; PRESENT -> nothing.
- **Bridge residual** (a bounded turn read for the active-steer path) at the sitting.
- **Spec re-open** items unchanged from tick 26.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope.

state: ARMED · push state of this log: LOCAL (origin/CLOUD @71d22ae232, ls-remote read 00:53Z)

## Compiler Tools

- `python .tools/directives-check.py --json` · claims scan 342 JSONs · verdict ledger `wc -l` (15) ·
  campaign ledger tree read · `git ls-remote` + MERGE_HEAD · single-file grep on
  `org/mcp/agent-spawn-audit.log` (time-window, denominator 40) + python over telemetry ·
  `ack_messages` (79884-80010 as received) · `send_message` to_agents (79984-79987, 80002-80005;
  8 of 8 DELIVERED).
