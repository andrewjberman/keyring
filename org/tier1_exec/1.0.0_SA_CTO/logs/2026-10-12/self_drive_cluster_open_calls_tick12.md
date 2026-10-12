# SELF-DRIVE cluster open calls -- tick 12 (2026-10-12 21:03Z, by hand; the 21:00Z cron fire did not arrive) -- state: ARMED

Arming record `ANDREW_DIRECT_20261012_125xZ_SELF_DRIVE_CLUSTER_OPEN_CALLS.md` @4698a8f59d. Ticks covered: 12 (plus the runtime
lines since tick 11). Last committed log: tick 11 @04b34a8cab (20:00Z). Substantive-delta log.

## Measurements

- open rows at 21:03Z: 15 (sitez 7, dell1 3, dell2 5, laptop 0), closed 89; fork 2, act 13. FOUR rows new since 18:00Z: dell1-4a62
  (fork), dell1-8c66, dell2-e41e, sitez-288f (acts). inbox: 0 unread at the tick; 10 read and acked since the tick-11 log.
- dell2: `2.0.0_SA_COO~V2` and `~Y2` seated on Andrew-direct 20:31Z ("seat V2 and Y2 now"); `~D2` RESEATED 20:4xZ on the fresh
  account after it measured NOT at its limit (Y2 working); its R45 11:41Z leg re-armed from the ledger. Nine dell2 seats ended
  today (five S9117, ~TV2 and four with no kill line, causes unread). ~CB2/~TR2 down until an order names them.
- site Z: at its WEEKLY limit since 14:15Z (resets 2026-10-14 06:00Z); 19 seats idle, MSTR~Z and CTO~Z running; console locked.
  The resume is Andrew's (a second account or credits are spend, the fc10 class). 0 behind CLOUD.

## Calls since the last log

- RULED by the driver: dell1-4a62 @ce771ac68f -- YES once: one SEV1 test page "Opal SEV1 test, no action" after the Transactional
  default applies and reads back, 13:00-22:00 ET, the SNS delivery-status log the oracle; a failure opens the AWS Support case; a
  second page needs his word. His 10-11 c290 "yes I did receive the text" covers the class. dell1 lifts + closes.
- Andrew-direct (site Z terminal ~20:5xZ, record @cdb5ff66b1): "Dell boxes should not be curtailed." Applied: c404 addendum 1
  @84e9aa3108 -- the IAMROLES narrowing of the dell agent users' InvokeFunction and my section-4 routing are withdrawn; D2-S46
  returns to dell2 as DISMISSED on his word; "least-privilege and identical" reads IDENTICAL only. CTO~Z reads the word at the same
  narrow scope (sitez-ffaf / OG-ap-13 stand) and has asked him whether it is wider; the answer comes through ~Z.
- dell2 four seats gone: ruling @1ccb6812e9 + addendum 1 @c26ac6b953 (limit read satisfied by measurement; ~D2 reseat; S9119).
- DESIGN FORKS at CRO research: 0. GOVERNANCE FORKS: 0 open.
- ACTS ONLY ANDREW CAN DO: 18 = 15 (tick-1 record section B) + dell1-8c66 (his WSJ/Barron's subscriber login), dell2-e41e (an
  outward-facing ask of a Black Diamond vendor contact; dell2 drafts it so his act is a send), sitez-288f (a colleague's Teams
  @mention). The remaining fork, sitez-1b36, is the grant on the list.

## Driver acts since the last log

- NFRA_CTLPLN-S9119 (heartbeat without a process) @1ccb6812e9, ARMED; mechanism read by MSTR (agent-poller.py watches the MCP
  server pid, server.py:1131); the lane is BASE_EXEC (mine), so the fix landed here: `org/mcp/agent-poller.py` @5948c06a4f --
  the poller also watches the seat's claude.exe (the MCP pid's parent, Toolhelp32) and exits when either dies; `--selftest`
  4/4; live probe on this seat's MCP pid: parent is claude.exe. Takes effect per seat at its next launch; the interim (liveness
  confirmed by process for a seat that matters) stands until then.
- XB-706d (dell2 COO~Y2 -> ~ANL) delivered to ~ANL. Push state at write: box/laptop LOCAL through 84e9aa3108; MSTR's box-sync
  carries it.

## Completion test

UNMEASURABLE (free-text scope); the loop ends on Andrew's stand-down word.

state: ARMED

## Compiler Tools

`python .tools/open-calls.py list --all --cloud`; `.tools/aws s3 cp` of a box's cluster copy; `check_inbox`; `git show <pin>:<file>`
(the site Z record at its bytes); `python org/mcp/agent-poller.py --selftest`; `.tools/commit-gate.sh`; `safe-commit.sh`.
