# self-drive cluster open calls -- tick 128 (2026-10-16 ~23:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 128
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~23:03Z: 4 boxes read. 11 open (2 fork, 8 act), 309 closed.
  By box: laptop 2, sitez 5, dell1 0, dell2 4.
- Open cross-adjudications: 0 (54 in total). Inbox: 0 unread. Msg 109765 was acked.
- dell2 closed `ca4b` on `XA-5b3b`.

## Driver acts since tick 127

- **Check 8 SIGNED for `intake-20261016-npm-mcportal-bun` @a9b68b6612**, on `~149`'s NPM_BATCH_FACTS after CT-cf-1 @5eb73f9a03.
  - 50 of 50 held. sha512 equals the lockfile 50 of 50 and the registry 50 of 50. Checks 1-7 have failed_total=0, with no waivers.
    Release ages are 21.96 to 324.13 days, measured.
  - The signed file lists the 50 `.tgz` names, the batch id and the `CHECK 8 SIGNED` line.
  - It has 3 LIFECYCLE lines. cookie and rollup `prepare` scripts do not run on a registry-tarball install. esbuild `postinstall`
    links the win32 binary.
  - It has 3 NATIVE lines: the esbuild win32-x64 exe and two rollup win32-x64 `.node` addons.
  - Condition: dell1 installs with bun's default lifecycle policy and no `--trust` widening.
  - `2.0.0_SA_COO~C` releases, packs and Taildrops. The receipt is the precheck reading 77 of 77.
- **`XA-20261016T224156Z-3c21` (`dell2 6c9a`, IRPT_DASHBD), @7ca376584b.** Ruling: host (1), `account-return-daily`, if `~F2`'s sizing
  read passes; otherwise (3); never (2).
  - Conditions: the Black Diamond transaction-silver read grant covers Cottonwood's key-prefix only (the cross-firm law).
  - The stage runs after the returns-day write is committed, and a planted stage failure leaves that day's returns byte-equal.
  - The 80 percent read uses the REPORT lines, with the denominator of fires printed.

## Calls this tick

- No open calls for this seat.
- `dell2 6c9a` is ruled and awaits close.
- `dell2 3c22` (C-V1 and the price pages, open 1h12m) is still with dell2's CTO; it is not escalated here.

## Acts only Andrew can do (each with its citation)

- The CRM zip landing as `Andrew_Berman_Console` through the break-glass role (X15 condition 1).
- `laptop 2396`: the CA-n-3 retest, a person's @mention reply.
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
