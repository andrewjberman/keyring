# self-drive cluster open calls -- ticks 135-136 (2026-10-17 ~02:3xZ to ~03:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 135-136 (135 was quiet, appended to `org/mcp/drive_ticks/1.0.0_SA_CTO.md`)
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements (tick 136, ~03:02Z)

- 4 boxes read. 10 open (1 fork, 8 act), 318 closed. By box: laptop 2, sitez 5, dell1 0, dell2 3.
- Open cross-adjudications: 0 (58 in total). Inbox: 0 unread. Msgs 109789 and 109790 were acked.
- Dell2 closed `2031`, `d95f`, `9bfe` and `f3d4`.

## Driver acts since tick 134

- **`XA-20261017T024251Z-a7a7` (`sitez bd68`, NFRA_OPLGTW), @1690dbffe0.** Ruling: YES, enforce Andrew's 10-08 word "no downloads needed
  yet". A narrowing never-widen act removes `download_filtered` from `alyssa@`'s gateway grant, one key.
  - Before the write: a usage-count read. If she has used it, the act still lands and the count goes to Andrew, who can reverse it
    with one word.
  - Read-back: the download is REFUSED and another operation ANSWERS (positive control).
  - No seat contacts the firm.
  - `bd68` leaves Andrew's act list.
- **SOC2_MSLOGS for Andrew** (dell1 project, read through the globgrph door; no data in the repo):
  - The collector was read live: the EventBridge rule `m365-metadata-trino-collector-hourly` is ENABLED at `rate(1 hour)` and has
    been invoked every hour since 10-16 07:00Z. Errors before 13:16Z were pre-consent. Errors from 20Z to 00Z were catch-up timeouts
    after the all-accounts reframe. The latest fires are `complete=True`, fetching about 15 blobs each.
  - Andrew asked dell1 (MSTR msgs 109788 and 109789, Andrew-direct "lets get the actual enriched stuff") to enrich the door's
    `timeline` with full records (detail=true) and hourly paging. It was live at 02:36Z, and the CloudShell block landed in
    Downloads (msg 109790).
  - Andrew-direct ~02:4xZ: "I need a solution to have agents run in and download big parts rather than be manually scripting, its too slow".
    This seat built a laptop-local puller OUTSIDE every repo (`C:\Users\AndrewBerman\m365_pulls\`):
    - `mfa.sh` stores a 36-hour MFA session from his code in the local profile `m365-door`. The door's MFA gate is unchanged.
    - `pull.py` pages by the hour through the door's member alias and writes the records, the attribution CSV and a per-account
      report.
    - It is not committed. No activity data enters git.

## Calls this tick

No open call for this seat. `dell2 3c22` is HELD for Andrew (C-V1).

## Acts only Andrew can do (each with its citation)

- `dell2 3c22`: lift IRPT_YCDGEN C-V1 (PRD line 312) for the AR variants. REC: yes, after r34j.
- The CRM zip landing as `Andrew_Berman_Console` through the break-glass role (X15 condition 1).
- His MFA code once a day, `bash ~/m365_pulls/mfa.sh <code>`, so the agents can pull through the door. It is his MFA device.
- `laptop 2396`: the CA-n-3 retest.
- One answer: did he close agent windows around 01:01Z?
- `sitez 8ed7` and `sitez f0d2`; `sitez 5b35`.
- `laptop b87f`.
- NFRA_CTLPLN FWD-2, FWD-6 and FWD-27.
- The TCKT_MTADTA audit-log check with IT.
- Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK.
- `xadj.py show/rule/list`: OK.
- `.tools/aws` reads: events describe-rule, lambda get-function-configuration, cloudwatch metrics, logs filter-log-events. OK.
