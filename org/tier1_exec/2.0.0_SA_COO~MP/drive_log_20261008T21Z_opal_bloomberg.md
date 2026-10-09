# 2.0.0_SA_COO~MP drive log -- 2026-10-08 21Z -- /canonical-drive NFRA_MCPORTAL 30m

Re-seated ~21:0xZ. NFRA_MCPORTAL was un-parked on Andrew's ~18:4xZ word: PRD v0.5 @cecf26d2c9 (1.0.0_SA_CTO~O) added
FWD-14 to FWD-19, the control plane. Loop authority:
- LIVE_ARMS row (`1.0.0_SA_CTO~O` self-drive paired with `/canonical-drive <own project> 30m`);
- re-armed at :22/:52 on the ~21:5xZ record `ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
  @ba8c4598fb (msg 32038).

| tick | time | limb | round | TOs t/T | cells | thread | act fired |
|---|---|---|---|---|---|---|---|
| 1 | ~21:1xZ | L4-R -> L5 | 3 open; 4 to cut | r3 3/5 | r4 0/5 | none | DRIVE FORWARD: v0.5's ratified-text half read STALE, then SIGNED @8de5b2dc76 by 3.0.0_SA_CVO~Z (msg 32001 acked). Found the C11 vs `graph-read.tf` R3 collision; filed row Z-S18 @34d0f27e0e; ruling ask to CTO~O |
| 1 | ~21:5xZ | L6 | 4 | 0/2 | 2 of 5 cut | n | DRIVE FORWARD: decomposition v4 + MP-x-1/MP-x-2 issued @202c512520; workers `~5` and `~6` spawned in `C:/tmp/mp-r4-5` and `C:/tmp/mp-r4-6` |
| 1 | ~22:0xZ | L6 | 4 | 0/2 | 2 of 5 | n | RULE: MP-x-2 amendment 1 on CTO~O's C12 ruling (msg 32041) @726160e76e. The MP-x-3 cut was refused by the one-issuance limb, so row Z-S19 moves MP-x-3, MP-x-4 and MP-x-5 to round 5 |

## Decisions

- **Round 3 stays open beside round 4** (decomposition R4.0). MP-c-1 is held on G-CLOSE: Andrew holds Alyssa's close run
  until gateway r29. MP-v-1 is held on G-2ND, with no Andrew word. The two rounds have disjoint write surfaces.
- **G-R3 is ruled (a)** by the laptop NFRA_CLDGRPH owner (msg 107359, relay 32030). The gateway role gets GetObject on
  `fabric/activity/v1/*` and `fabric/open-calls/v1/*`, ListBucket conditioned on those two prefixes, and no write.
  `graph-read.tf`'s R3 text carves those out. The bucket reads SSE-S3 with no bucket policy, so no KMS grant is needed.
  The MP-x-3 order is drafted, and checks x3.AC1-3 are committed (all FAIL at base).
- **Sidebar placement:** Control Plane goes LAST, after Infosec, so Andrew's verbatim order stands.

## Waiting on

- Workers `0.9.0_WK_NFRA_MCPORTAL~5` (MP-x-1) and `~6` (MP-x-2). `~6` gets amendment 1 as a continuation when it reports.
- G-REL: `2.0.0_SA_COO~O`'s gateway r29. G-SEE: Andrew.

## Compiler Tools

- `prd-signoff.py status`: STALE, then SIGNED. `drive-mode.py read`: FULL.
- `comp-surprise --project`: 9 open, 8 armed (pre-existing).
- `round-close-check.py --round 3`: REFUSED (3 orders not complete; its proof parse reads `to_id ''`, which is unexamined).
- `to-pipeline-gate`:
  - admitted the issuance;
  - refused the late x-3 file with no override on that limb;
  - admitted the x-2 modify.
- `surprise-row-gate`: refused `21:3xZ` (format) and an in-place correction, so the row is append-only.
- Bun cache precheck: 77 of 77 present.
- IAM simulation dry-run: 3 of 6 arms matched at base, as expected.
