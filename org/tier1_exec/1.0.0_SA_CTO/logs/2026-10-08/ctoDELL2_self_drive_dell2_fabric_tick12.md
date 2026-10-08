# /self-drive dell2 fabric (7 projects, 30m) -- tick 12 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_172xZ_SELF_DRIVE_30M_DELL2_ALL_FABRIC_PROJECTS.md` @33d7de3039
**Ticks covered:** tick 12 (22:49Z), plus the event-driven work since tick 11. **state: ARMED** | cron b0f6db2a

## Inbox

- 0 unread at the tick.
- Read and acked since: 1836, 1838, 1842, 1844, 1847, 1850.

## Calls ruled by the driver

1. **One end-to-end Analysis Request project?** REC yes. **RULED yes.** It is Andrew's own word ("compress ... into one project", @2b21a349d1).
   The proposed code is `IRPT_ANLREQ` (CRO brief @9076346655). L2 endpoint and L3 registration follow.
2. **Package attach route on the ticket system?** REC yes. **RULED yes.** TCKT_VNEXT PRD v0.3 ADDENDUM 2 @201ed553c4 adds:
   - C-PACKAGE: `POST /tickets/{id}/package`, pointers only;
   - FWD-9.

   The CVO re-sign of the ratified-text half is asked (msg to `3.0.0_SA_CVO~DELL2`, 22:56:48Z).
3. **Who drives IRPT_ANLREQ?** This is a governance fork, so it is pitched to `3.0.0_SA_CVO~DELL2` (22:56:52Z). REC: interim `~Y2`, moving to a seat
   named by project code after dell1's naming setup.
4. **NFRA_TRNSPT C-WIPE-GATE (msg 1838).** **RULED passed.** The planted-token test was re-run at HEAD 49c04cd4b2: 13 passed. Round-12 analysis
   @a090c5ea23 gives round 13 = E1 `generated_at`, E2 the first real Kimi draft, E3 a real-gate trace.
5. **IB-pr-376 sequencing (msg 1847).** **RULED:** one apply order to CloudOps~DELL2, function first, then the route once live = `7T29wPhz`.

## Acts taken

| Act | Commit |
|---|---|
| svc-commentary mint CTO half GIVEN; rollback made recoverable | @81a0550165 |
| NFRA_TRNSPT round-12 analysis | @a090c5ea23 |
| TCKT_VNEXT PRD v0.3 ADDENDUM 2 | @201ed553c4 |
| IB-pr-376 CTO half GIVEN; census, live sha and rollback version read here | @b97fa248b2 |
| IB-pr-373 IAM leg applied 22:47:14Z (msg 1844); ~P2 told to cut the route order | message |

## Scope state (denominator 7)

| Project | status | dep_stage |
|---|---|---|
| IRPT_CUSTDY | active | EXECUTING |
| ADVI_COTBKF | active | EXECUTING |
| IRPT_BCKEND | active | EXECUTING |
| IRPT_YCDGEN | active | EXECUTING |
| IRPT_DASHBD | active | EXECUTING |
| NFRA_TRNSPT | active | ROUND_CLOSE |
| TCKT_VNEXT | active | EXECUTING |

## Out of scope, noted

NFRA_CTLPLN-D2-S1 (msg 1842): the dell2 Terraform kit cannot serve 6 of 40 roots, including `investor-reporting/core`. MSTR relays it to the
laptop. IAM stays laptop-side regardless.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Acts only Andrew can do

1. **The `/closer` build phase for IRPT_ANLREQ** (contract, mandates, seats). Citation: CLAUDE.md rule 27, "A product in flight with no working
   journey goes to `/closer` on Andrew's word". Also his DONE-WHEN confirmation of the L2 endpoint (Andrew-direct 2026-09-03 ~05:2xZ).
2. **Alyssa files ONE Analysis Request**, and he names her DEV address (TV-r-1, organic arm).

## Compiler Tools

Instruments: release-census.py, `lambda get-function-configuration`, `s3api list-object-versions`, pytest, safe-commit.sh.
