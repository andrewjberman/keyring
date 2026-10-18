# /self-drive dell1 box -- ticks 107-108 (`1.0.0_SA_CTO~DELL1`, 2026-10-18 06:48Z-07:48Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec.
Covers everything since the tick-106 log (@7b8d160be3). **state: ARMED.**

## Inbox (0.8)

0 unread at 07:48Z. Read and acked: 7942, 7945, 7948, 7955.

## Acts taken

| project | act | hash |
|---|---|---|
| gateway lineage | site Z CTO 35640 (MSTR relay 7942): gateway LIVE is aa2efa2cf3, whose parent is cg-3. Ruled: any dell1 gateway release sets `DEPLOY_BASE_REF=aa2efa2cf3`. W1 and MSTR told | (msg 7943/7944) |
| AMGT_HARVST r94 | CVO 7945 MAY-CLOSE: W165-S3 REMEDIATED (0 of 109), W170-S3 graduated (the slash-key split). Ruled the dossier rebuild: YES for non-slash names under its own pair; slash keys wait on W170-S3. Round-95 list of 5 | 428b762698 |
| AMGT_HARVST r95 | cj-4 CTO half (75 non-slash dossiers), binds 35e368f3 @845b69a8cc. Read `dossier.py:1185-1250` (the newest landed model-block stamp, read raw). Added a guard: block SERVED, a newer stamp, valued rows not lower, so that a failed read cannot pass the subset check. KMB stays out | b9e244d5a9 |
| AMGT_RESAPP r117 | bx-5 CTO half (pack Summary, currency and passages redeploy), binds 60734f0e @871379e429. Pin 9ab6d36305 changes 1 member; `_cleared_passage:913-929` read; added a negative control (an uncleared block prints nothing) | 2a3c57d709 |

## Open calls (Step 1)

The list has 145 rows, 3 open, all acts only Andrew can do. No open calls in scope dell1 box (tick 108).

## ACTS ONLY ANDREW CAN DO

- **0cf5:** confirm ADVI_COTBOOKS's 6 DONE WHEN lines. Citation: L2, rule 27.
- **89c9:** the SOC2_MSLOGS round-2 re-derive. Citation: it needs his MFA session.
- **e1ee:** restart the dell2 box manager. Citation: physical presence at the machine.
- **FWD-10 PROD push:** the page is client-facing. Citation: the portal PROD exception.

## Watch

- 08:00Z: the dell2 recheck.
- ~11:30Z: the Cottonwood silver run.
- 13:30Z: the MDPF fire.
- Next BD fire: SECCLASS e116b.
- RESAPP bx-5 apply.
- HARVST cj-4 apply and W170-S3.
- Site Z landing its gateway commits.
- The ms ack.

## Completion test

NOT DONE. Box projects are in flight.

## Compiler Tools

None run. These were signing reads of named files and refs (`git diff --stat`, blob `rev-parse`, `sed -n`, native Grep on one file);
no infra or code change from this seat.
