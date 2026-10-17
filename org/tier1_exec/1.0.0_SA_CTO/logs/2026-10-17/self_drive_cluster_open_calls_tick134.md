# self-drive cluster open calls -- tick 134 (2026-10-17 ~02:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 134
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~02:04Z: 4 boxes read. 14 open (5 fork, 8 act), 314 closed.
  By box: laptop 2, sitez 5, dell1 0, dell2 7.
- Open cross-adjudications: 0 (57 in total). Inbox: 0 unread. Msg 109786 was acked.

## Driver acts since tick 133

- **The account-id list for `client-data-check.py`** (site Z msg 35317 via MSTR 109786; this seat owns the gate edit, per dell2's
  containment ruling item 8). Ruled @3ffa142af0 (`CTO_RULING_ACCOUNT_ID_HASH_LIST_PRODUCER_20261017.md`).
  - The list is HMAC-SHA256 under one builder-named secret, not plain sha256: served ids are low-entropy, so a plain hash can be
    reversed by trying candidates.
  - The producer writes to one non-repo key (address() output). Boxes pull it to `~/.opal/`.
  - The hook refuses on an absent list once the first list is produced.
  - Relayed to `1.0.0_SA_CTO~Z` and `1.0.0_SA_CTO~DELL2`.
- **`XA-20261017T020038Z-755e` (`dell2 9bfe`), @c70fc4ceab, with ruling addendum 1.** Per-firm HMAC lists, each produced by that
  firm's own directory or ownership step under the firm's own role, so there is no cross-firm read. Each step writes to ONE shared
  non-firm product prefix keyed by firm token, so boxes need no per-firm fence exemption.
- **Andrew's question** ("I only use Andrew_Berman_Console ... maybe ill try to reup the pw on the andrew berman one").
  - Read: `Andrew_Berman` has a console login profile (created 2025-11-05), `PasswordLastUsed` 2026-10-17T02:03:04Z, and one MFA
    device, `mfa/Andrew_Phone`.
  - The door group `globgrph-trino-access-group` has exactly one member, `Andrew_Berman`.
  - REC given to Andrew: reset the password from `Andrew_Berman_Console` (an admin) rather than adding the Console user to the door
    group. The latter is his call.
- **dell1's Taildrop** (the SOC2_MSLOGS timeline CloudShell steps from `2.0.0_SA_COO~S1`) was located in Downloads and summarized
  for Andrew. Off git.

## Calls this tick

- No call for this seat.
- `dell2 2031`, `d95f` and `9bfe` are ruled and await dell2's close.
- New `dell2 f3d4` (the 5174 handover sha after Andrew's DB-b-309 smoke) is dell2's own-box call.
- `3c22` is HELD for Andrew.

## Acts only Andrew can do (each with its citation)

- `dell2 3c22`: lift IRPT_YCDGEN C-V1 (PRD line 312) for the AR variants. REC: yes, after r34j.
- The CRM zip landing as `Andrew_Berman_Console` through the break-glass role (X15 condition 1).
- The SOC2_MSLOGS timeline read as `Andrew_Berman` with MFA. The door admits only that user.
- `laptop 2396`: the CA-n-3 retest.
- One answer: did he close agent windows around 01:01Z (laptop) and earlier on dell1?
- `sitez 8ed7` and `sitez f0d2`; `sitez bd68` (REC: narrow); `sitez 5b35`.
- `laptop b87f`.
- NFRA_CTLPLN FWD-2, FWD-6 and FWD-27.
- The TCKT_MTADTA audit-log check with IT.
- Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK.
- `xadj.py show/rule/list`: OK.
- `.tools/aws iam` reads (login profile, MFA, group members): OK.
