# 0.0.3_BG_BBGTerminal -- relaunch 2026-09-16T08:26-08:40Z (04:26-04:40 ET)

## Launch gates (prompt.md "On launch")

| Step | Result |
|---|---|
| 1 register_agent | was NOT REGISTERED at load (second instance of the drop recorded in 0032-0050Z log s.6, or simply the prior session ending) -> LIVE PID 22424 |
| 2 /watcher | inbox Monitor `brhl7br5x` armed, expired at 30 min, re-armed `bbjk9f8ud`; ps shows exactly one watcher process |
| 2a identity gate | **PASS** -- whoami on opal-gateway-bbg = Opal Bloomberg / opalbloomberg@opalinvest.com |
| 3 Teams Monitor | armed `bxmpccyd0`, 15s, pin(server=opal-gateway-bbg, identity=opalbloomberg), token identity=opalbloomberg@opalinvest.com |
| 4 bloomberg_health | **ok: false** -- could not start blpapi session to 127.0.0.1:8194 |
| 5 orient | read logs/2026-09-16/startup_post_reboot_and_daily_guardrail_0032-0050Z.md + WINDDOWN_PARK_20260915T235xZ.md |
| crons | 0 |

## Fabric inbox -- 2 messages, READ-acked (23352, 23382)
0.0.0_AB_MSTR~Z merge window OPEN 01:47Z and CLOSED 05:02Z. This seat does no git work; nothing held, nothing owed.

## Teams arm -- CURSOR MOVED BACKWARD -> SUSPECT-REPLAY, all 8 emits verified already served
Banner `cursor=2026-08-28T20:07:10.323Z`, while the newest served entry is 2026-09-15T18:25:20.883Z.
Every emit checked against thread memory by timestamp:

| ts (Z) | from | thread record | owed |
|---|---|---|---|
| 09-11 13:20:16 / 14:25:01 | Manav Shah | 2026-09-11-manav-shah/2026-09-11.md -- SERVED 14:25:36/41Z | no, ball with Manav |
| 09-11 06:44:18 | Andrew (attachment only) | capability-roster/2026-09-11.md OPEN -- waiting on his content/question | no, ball with Andrew |
| 09-15 05:51:10 | Andrew "deliver this to 1.0.0_SA_CTO~W" | capability-roster/2026-09-15.md -- declined in-thread, nothing relayed | no |
| 09-15 18:10:02-18:25:20 (4) | Andrew factor-spec drops + "Don't respond to this." | capability-roster/2026-09-15.md -- NONE owed a reply | no |

Nothing sent. Cursor file after the replay drain reads `2026-09-15T18:25:20.883Z` (both
`%LOCALAPPDATA%\Temp\teams-watch.cursor` and `/tmp/teams-watch.cursor`, mtime 04:32 ET) -- so the
engine armed off a THIRD, older cursor home (TEAMS_DUTY "Reading the arm banner" class). Not this seat's engine.

## Bloomberg Terminal -- STILL DOWN, today's 07:00 ET pull is exposed
- bloomberg_health ok:false at 08:3xZ.
- Get-Process: `bbcomm` pid 15680 started 04:30:17 ET (= this session's health probe); **wintrv ABSENT**.
- OPAL_BBGTML_daily_pull: LastRun 09-15 07:00:01 rc 0, Next **09-16 07:00 ET**.
- Unchanged from the 00:3xZ finding. Per refs/RELAUNCH.md:114 and STANDING_ORDER_0715_DAILY_BACKSTOP.md:
  SURFACE, do not sign in ahead of a failure. The 07:30 ET freshness check is the summons.

## State
Monitors: inbox `bbjk9f8ud`, Teams `bxmpccyd0` (both 30-min cap; re-arm on expiry). Crons 0. No git (G2).

## Broker registration dropped AGAIN (second night running)
Registered 08:2xZ (PID 22424); heartbeat at ~08:40Z refused "not registered". Re-registered, re-read
get_agent_status -> LIVE, last seen 2s. Same shape as 0032-0050Z log s.6: Monitors `running` the whole
time while the broker could not see this seat. Two instances in two sessions ~8h apart. Surfaced, not chased.

## 08:59Z -- third drop; the likelier cause is IDLE PRUNING, not the liveness.json write race
The inbox Monitor expired at ~08:59Z with no events, and was re-armed as `bs40c8uqh` (ps shows exactly one watcher).
The heartbeat was refused again ("not registered"). I re-registered. liveness.json now holds 2 entries
(0.0.0_AB_MSTR~Z and this seat). All three drops came after a gap of more than 15 min with no heartbeat from
this seat. The heartbeat docstring says a seat goes STALE after 2 min without a heartbeat, so the entry is
probably being PRUNED after that, not lost to the last-writer-wins race that the 0032-0050Z log s.6 blamed.
That attribution is INFERRED, not measured: I have not read the prune code. Consequence: this seat is
invisible on the broker between events unless it heartbeats, and it arms zero crons by design. Andrew's call
whether that matters. The inbox Monitor keeps delivering either way.

## 07:00 ET DAILY PULL -- SELF-HEALED, GUARDRAIL PASS (Wednesday; T-1 expected = 2026-09-15)
Bloomberg was down continuously from the 20:30 ET reboot. The last health probe at ~06:03 ET read ok:false.

| Leg | Instrument | Measured |
|---|---|---|
| Terminal came up | Get-Process at 07:02:52 ET | `wintrv` pid 23672 started **07:00:23 ET**, 22s after the task fired. The pull itself brought the Terminal up |
| DAPI | bloomberg_health at 07:02 ET | **ok:true**, //blp/refdata |
| Task | Get-ScheduledTaskInfo | 267009 (running) at 07:02, then **LastTaskResult 0** at 07:09:18 ET, LastRun 07:00:01 |
| Served by CONTENT | portal_lookup benchmarks model_portfolio_benchmarks | **data_as_of 2026-09-15**, last-modified 11:08:16Z |
| Manifest | portal_lookup pipeline-status manifest | pipeline_started 11:06:06Z, generated 11:09:40Z; data_pkl + model_pkl data_as_of **2026-09-15** |

This corrects my own earlier framing ("today's 07:00 ET pull is exposed"). The device recovered on its own,
which is exactly the property Andrew's standing order protects ("the device needs to be able to figure this
out"). Not signing the Terminal in ahead of the run cost nothing. The PKL OneDrive folder was not listed
(path glob missed); the served artifact read by content is the verdict.

## TEAMS SERVE -- 2 threads, both FIRST CONTACT, both recorded
1. **Alyssa Keith 13:12Z** -- "news ahead of the Fed meeting". Catalog row 5 (news DDB). ACKed 25 s,
   served 4 blocks at 13:15Z. boto3 query on `opal-news-articles` by `article_date`, fully paginated:
   09-15 **1075** items -> 73 Fed-related, 09-16 **183** -> 12. (The `.tools/aws` shim died first on a
   cp1252 encode error, rc 255, partial output -- DISCARDED, not served.) Vintage + "headlines as
   reported" stated. `threads/2026-09-16-alyssa-keith/`.
2. **Menachem Goldstein 17:07Z** -- live prices on 24 distinct tickers (30 tokens) **as a downloadable
   editable Excel file**. ACKed 13 s. **DECLINED on TWO independent limbs**, either sufficient:
   fresh DAPI delivery = download-side per the BLOOMBERG_GUARDRAILS tie-breaker; and this seat has no
   file-create/send entitlement anywhere. Served plane checked first -- holdings_attribution carries no
   price field, data_as_of 2026-08-31 -- so no partial answer existed either.
   **DEMAND SURFACED** to `0.0.0_AB_MSTR~Z` for Andrew at 17:10:25Z (escalate-with-demand), which
   crossed his "yea please let Andrew know" at 17:10:12.83Z by 13 s; he was told it went.
   ⚠ **OPEN follow-through on THIS seat, no gate tracks it:** if Andrew rules on either limb, tell
   Menachem Goldstein -- this seat promised "I'll let you know if anything changes."
   `threads/2026-09-16-menachem-goldstein/`.

**First request for an OUTBOUND file artifact.** The three prior blocked asks were inbound attachments
this seat could not READ. Inbound-read blindness and outbound-write absence are different gaps with
different levers; only the second was in play here.

## Teams token expiry -- 3 instances, ~hourly
Arms `be7ryzhba`, `b9knlsmp4` and `bx79c9xmk` each logged `pinned token expired -- quiet retry, pin HELD`
and showed no later `re-selected` line before being killed at the 30-min cap, so each may have been
polling-blind for part of its window. Nothing was lost: the engine holds the cursor on a failed poll and
each re-arm resumed at 13:15:43Z. The one arm that DID recover (`braueylmb`) printed
`re-selected after lapse` right after a `whoami` re-minted the token. Engine is `0.5.0_AE_OpalETL~Z`'s,
not this seat's to fix; recorded as a pattern, not chased.
