# self-drive cluster open calls -- tick 118 (2026-10-16 ~18:0xZ), 1.0.0_SA_CTO laptop

state: ARMED   cadence: 30m   cron: 9d30d669   ticks covered: 118
arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261011_032xZ_CTO_LEADS_CLUSTER_OPEN_CALLS_LOOP_60M.md`

## Measurements

- Cluster list read at ~18:02Z: 4 boxes read. 10 open (0 fork, 10 act), 297 closed.
  By box: laptop 2, sitez 7, dell1 0, dell2 1.
- Open cross-adjudications: 0 (48 in total). Inbox: 0 unread. Msgs 109729, 109731, 109732, 109734 and 109736 were acked.

## Driver acts since tick 117

- Site Z closed `8e61` on `XA-7acd`.
- **The intake route gains an npm-tarball limb** (`CTO_RULING_INTAKE_NPM_TARBALL_LIMB_FOR_DELL1_BUN_20261016.md`). The trigger was
  dell1 AMGT_HARVST HVST-cc-7: 50 bun packages absent for mcportal@c66ca82952's dashboard build.
  - Measured: `intake_fetch.py:44-45` is PyPI-only, so the route cannot serve npm as built.
  - Ruled @fd88a45129: one NFRA_CTLPLN cell.
    - Fetch from `registry.npmjs.org` only.
    - Each tarball's sha512 must equal both the registry's integrity and the bun.lock line.
    - Lifecycle scripts and native binaries are listed, and named at check 8.
    - The receipt is `bun_cache_precheck` reading 77 of 77.
    - The batch of the 50 lockfile-pinned names is approved in principle.
  - Dell1 withdrew the ask (msg 109732), giving addendum 1 @29d2d2ca3c (not cut, YAGNI), with serials restored @e4a83f521c.
  - Dell1 re-opened it (msg 109736: there is no pre-built-dist route in `deploy-to-ec2.sh`), giving addendum 2 @0c771fe5fb: the
    ruling is reinstated.
  - `2.0.0_SA_COO~C` was told to cut the cell. Dell1's CTO and `2.0.0_SA_COO~W1` were told, through MSTR, that the ask is taken.

## Calls this tick

No open calls in scope (tick 118). The cluster holds 0 forks and 0 open cross-adjudications.

## Acts only Andrew can do (each with its citation)

Unchanged:
- `sitez 21d9` (+3), `sitez bd68` (REC: narrow), `sitez 5b35`;
- `laptop b87f` and `laptop 44eb`;
- NFRA_CTLPLN FWD-2, FWD-6 and FWD-27;
- the TCKT_MTADTA audit-log check with IT.

Postponed: `sitez def4`, `dell2 c02c`.

## Completion test

NOT DONE. The scope ends only on his stand-down.

## Compiler Tools

- `open-calls.py list --all --cloud`: OK, 4 of 4 boxes.
- `xadj.py list --state OPEN`: 0.
