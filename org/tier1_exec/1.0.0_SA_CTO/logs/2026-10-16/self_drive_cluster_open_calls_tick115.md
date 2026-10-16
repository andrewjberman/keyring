# self-drive cluster open calls -- tick 115 (2026-10-16 ~16:3xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 115
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~16:32Z: 4 boxes read. 10 open (0 fork, 10 act), 295 closed.
  By box: laptop 2, sitez 7, dell1 0, dell2 1.
- Open cross-adjudications: 0 (46 in total). Inbox: 0 unread. Msgs 109720, 109723, 109727 and 109728 were acked.

## Driver acts and results since tick 114

- **NFRA_CTLPLN round-29 analysis @ae11f384bd**, on CVO v33 (msg 109720). Its rulings:
  - source-map stage 2 is ONE atomic cell that re-runs the census at its cut (this disarms C-S102);
  - `_last_deploy_recorded` is dropped;
  - two `.owned-paths.yaml` lines;
  - sweep-before-merge goes into the L6 template;
  - C-S103 stands;
  - FWD-11 is graded on the overnight reboot.
  It was sent to `2.0.0_SA_COO~C` and `3.0.0_SA_CVO~L`.
- **CVO v34 @3960a7a1ff (msg 109727):** FWD-11, FWD-4, FWD-12 and FWD-22 are REALIZED, so **17 of 28**. FWD-11 was graded on the laptop's
  00:54-00:58Z reboot with round 24 in flight; no deliberate reboot is owed, and Andrew's 10-14 hold is not touched. ADVANCED: 2, 6, 7, 10,
  14, 21, 27.
- **`XA-20261016T160537Z-f98b` (`dell2 2cc0`, IRPT_ANLREQ AR-v-32), @b7647b5bf2.** Ruling: YES, with one transient synthetic staff
  user. The condition added: the staff role only, no firm entitlement, and the role set printed before removal.
- **TCKT trade-form firm-bucket access is LIVE.** `0.7.0_AE_CloudOps~TF` applied `ADVI_FIRMBKTS.TO-FB-n-1`: apply b156a4a2b4, 3/3/0, AC1
  PASS, ledger closed.
  - This seat's live read: all 3 policies name `opal-ticket-api-role`, and CORS on each is exactly the 3 origins.
  - `2.0.0_SA_COO~B1` validated it from its own live read (d6e120b094).
  - `~TF` stopped (rule 34 (a)).
  - V2 was told that the R18/R19 gate is cleared. `2.0.0_SA_COO~C` was told for row W89-S3.

## Calls this tick

No open calls in scope (tick 115). The cluster holds 0 forks and 0 open cross-adjudications.

## Acts only Andrew can do (each with its citation)

- `sitez 21d9` (+ `21c5`, `8ed7`, `f0d2`): his sitting and his Opal Bloomberg sign-in.
- `sitez bd68`: his 10-08 word against a live grant. REC: narrow it.
- `sitez 5b35`: a named person's call.
- `laptop b87f` (also NFRA_CTLPLN FWD-14), `laptop 44eb`: person acts.
- NFRA_CTLPLN FWD-2 (a new machine), FWD-6 (a client-facing PROD push), FWD-27 (logins from rc and muse, and off the tailnet).
- TCKT_MTADTA: the unified audit-log check with IT.
- Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK, 4 of 4 boxes.
- `xadj.py show/rule/list`: OK.
- `.tools/aws s3api get-bucket-policy/get-bucket-cors` (3 buckets): OK.
