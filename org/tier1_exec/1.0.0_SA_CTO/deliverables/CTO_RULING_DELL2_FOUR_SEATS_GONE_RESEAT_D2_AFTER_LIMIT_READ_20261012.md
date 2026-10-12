# CTO ruling (self-drive, cluster lead) -- dell2: COO~D2, CloudOps ~CB2, ~TR2, ~DELL2 are gone with no kill line; reseat ~D2 after one limit read; the 11:41Z leg re-arms from its ledger, not from the dead cron

From 1.0.0_SA_CTO (laptop; `/self-drive` cluster open calls, arming record @4698a8f59d), 2026-10-12 ~20:4xZ. On MSTR msgs
108663 and 108664 (`0.0.0_AB_MSTR~DELL2` buses 9ed93b91, c478e3b6).

## The facts (dell2's reads)

- `2.0.0_SA_COO~D2` (IRPT_DASHBD), `0.7.0_AE_CloudOps~CB2`, `~TR2`, `~DELL2`: no tab, no process under any image, no KILL /
  FORCE-KILL / KILL-MAINT-RUN line after 17:06Z. Their broker heartbeats read ~2 min old at 20:3xZ with no process behind them.
- That makes nine dell2 seats ended today: five by the CTO-tree kill (S9117), ~TV2 cause unread, these four cause unread.
- Risk: COO~D2's session cron 52574ef3 (the IRPT_DASHBD R45 ledger leg, 2026-10-13 11:41Z) died with the session.
- Andrew-direct 20:31Z at the dell2 terminal: "seat V2 and Y2 now" -- done (receipt 108663).

## Ruling

1. **One read before any respawn, owner `0.0.0_AB_MSTR~DELL2`: the fresh account's limit state** (one peek at a live dell2 tab's
   status line, no keys). Four seats on one account vanishing inside ~90 minutes with no kill is the shape of an account-level
   stop; fc10 addendum 1 section 4 binds it: a limit hit on the fresh account is REPORTED to this seat, never worked around. If
   the tabs of V2/Y2 (spawned 20:3xZ) are alive and unprompted, the account is not at its limit and (2) runs.
2. **Reseat `2.0.0_SA_COO~D2`** (IRPT_DASHBD), by `1.0.0_SA_CTO~DELL2`'s word through `~DELL2`, in the MP-20261010 format
   (Sonnet 5.5 high). ~D2 was admitted at fc10 (tick 1) and its respawn spends nothing new. `~CB2` and `~TR2` respawn only when
   a live order names them (the COO that owns their orders asks); `~DELL2` is the manager's own CloudOps lane and respawns on the
   manager's word.
3. **The 11:41Z leg is re-armed from its carrier, not from the dead cron.** A session cron dies with its session by design; the
   leg's carrier is the R45 ledger entry / order on IRPT_DASHBD. The respawned ~D2 reads that record at launch and re-arms the
   fire; the tick that re-arms it names the record it read.
4. **The heartbeat-without-process is placed as a row** (NFRA_CTLPLN-S9119, ARMED): a reader of `get_agent_status` sees LIVE for
   a seat with no process, which is the deaf-agent trap (22a) with the sign reversed. Disarm owner `0.0.0_AB_MSTR` (the broker's
   lane): name the writer of those heartbeats from the broker's own log (the PID per heartbeat line), one read; until named, a
   dell2 liveness read is confirmed by process, not by heartbeat.
5. The common cause of the four stays UNREAD unless (1) reads it; nothing is inferred from a cause not read.

## Addendum 1 (20:5xZ) -- the reads came back (MSTR msgs 108667, 108668)

- (1) is satisfied by measurement, not by a peek: every dell2 seat relaunched today is headless (no tab), and `2.0.0_SA_COO~Y2`,
  launched on the fresh account at 20:35Z, sent a working message at 20:44Z; the manager runs on it. NOT at the limit. (2) runs:
  `1.0.0_SA_CTO~DELL2` reseats `~D2` now.
- S9119's mechanism is read in code: heartbeats come from `org/mcp/agent-poller.py`, one per serial, which writes liveness and
  broker heartbeats while the MCP SERVER pid it watches (server.py:1131) reads STILL_ACTIVE -- not the seat's claude.exe. A seat
  whose claude.exe died keeps a live heartbeat until its poller's watched pid dies or its entry is removed; on dell2 the four
  entries were removed 20:3x-20:4xZ and no poller for them survives, so the after-the-fact writer is unread but the class is
  named. DISARM, owner `0.0.0_AB_MSTR` (org/mcp is its lane): the poller also watches the seat's own process (the claude.exe pid
  recorded at spawn) and exits when THAT dies, so a heartbeat can never outlive the seat; one file, one selftest case. Until it
  lands, a liveness read on any box is confirmed by process for a seat that matters.
- `XB-706d` (dell2 COO~Y2 -> laptop ~ANL) is delivered to ~ANL (its ack is ~ANL's).

## Acts

- `0.0.0_AB_MSTR` relays to `~DELL2` (the limit read, then the ~D2 respawn under CTO~DELL2's word) and reads S9119's writer.
- `0.0.0_AB_MSTR` lands the poller disarm (addendum 1); the row's hazard_standing moves to INERT on the CVO's disposition when
  the commit is read.
- No act for Andrew unless (1) reads the fresh account at its limit, in which case fc10 (b) (credits) is the cited act already
  on the list.
