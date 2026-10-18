# /self-drive dell1 box -- ticks 122-123 (`1.0.0_SA_CTO~DELL1`, 2026-10-18 14:18Z-15:18Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_DELL1_BOX_30M.md` @fa59eb8dec.
Covers everything since the tick-121 log (@c599456423). Tick 122 (14:48Z) was quiet. **state: ARMED.**

## Inbox (0.8)

0 unread at 15:18Z. Read and acked: 8080, 8084, 8090, 8098, 8101.

## Acts taken

| project | act | hash |
|---|---|---|
| Cottonwood AUM (ms, on Andrew's word, via MSTR 8080) | Read Andrew's Teams chat with the Cottonwood contact, read-only. Briefed C1 from committed sources; the brief sits in the scratchpad, uncommitted. **Answer: insurance (96 annuity accounts, $8.86M) IS inside the 530m as Supervised; supervised ex-insurance is $521.56M.** C1 wrote and committed the explanation @fffc712e89. I read it end to end and sent it to MSTR for ms (8085) | (msgs) |
| AMGT_HARVST r96 | CVO 8090 MAY-CLOSE: the union read is live; W171-S4 and S6 disarmed and remediated. Ruled: the 4 legacy raw objects stay in place as SUPERSEDED, with no migration (a rename re-creates the ambiguity; a delete is Andrew's act). Round-97 list of 5 | db6c34a7cc |
| AMGT_HARVST r97 | cl-4 CTO half (BP/ and NG/ dossiers after the 13:02Z blocks), binds 512874fb @5fc9ab77eb. Guard read confirmed, with a guard-and-build same-block-key condition. Ruled: a SCHEDULED daily dossier refresh is a round-98 cell | de80883964 |
| AMGT_HARVST r97 | cl-2 CTO half (`pull_enqueue` canonical status key, Terraform), binds a72a3823 @3a2893737e. C-7 ruled YES: ONE real invoke for BP/_LN_Equity through the Bloomberg queue only, accepting a queue refusal without override. The Lambda's copy of the slash rule joins the 105-key drift guard and follows XA-cbaa | 5e345c92f5 |

## Open calls (Step 1)

The list has 146 rows, 4 open:
- 3 are acts only Andrew can do;
- 1 is escalated: 48ae under XA-cbaa, still OPEN at the laptop CTO.

## ACTS ONLY ANDREW CAN DO

- **0cf5:** confirm ADVI_COTBOOKS's 6 DONE WHEN lines. Citation: L2, rule 27.
- **89c9:** the SOC2_MSLOGS round-2 re-derive. Citation: it needs his MFA session.
- **e1ee:** restart the dell2 box manager. Citation: physical presence at the machine.
- **FWD-10 PROD push:** the page is client-facing. Citation: the portal PROD exception.
- **Upcoming:** the SECCLASS partners-data apply, once its pair is signed. Citation: client-visible.

## Watch

- HARVST cl-2 and cl-4 applies.
- RESAPP bz-5 apply, then round 120.
- XA-cbaa ruling.
- The ms ack of the Cottonwood explanation.
- The proof-newest-instance flag reaching CLOUD.

## Completion test

NOT DONE. Box projects are in flight.

## Compiler Tools

None run. These were reads of named files (the findings, the PRD change log, the half files), one Teams chat read through the gateway
(read-only), and signings; no infra or code change from this seat.
