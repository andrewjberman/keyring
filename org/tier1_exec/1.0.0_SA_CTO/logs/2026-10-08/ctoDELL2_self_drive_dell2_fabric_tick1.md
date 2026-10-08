# /self-drive dell2 fabric (7 projects, 30m) -- tick 1 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_172xZ_SELF_DRIVE_30M_DELL2_ALL_FABRIC_PROJECTS.md` @33d7de3039
**Ticks covered:** tick 1 (~17:28Z). It also carries the event-driven work since the last log under the superseded 60m record (tick 32 @e34e392f57).
**state: ARMED** | cron b0f6db2a (:07/:37) | the 60m cron bbc6284c is deleted, and SUPERSEDED is appended to its record

## Scope state (~17:28Z)

All 7 projects are `active` / EXECUTING with no `blocking` field: IRPT_CUSTDY, ADVI_COTBKF, IRPT_BCKEND, IRPT_YCDGEN, IRPT_DASHBD,
NFRA_TRNSPT and TCKT_VNEXT. The 13 dell2 seats are LIVE. Sequence: NEEDS-SLOT on IRPT_CUSTDY and ADVI_COTBKF (as at tick 32).
Inbox: 0 unread; 1313 to 1330 are acked.

## Calls closed and acts (since tick 32)

| input | ruling or act | carrier |
|---|---|---|
| `~M2` 1316: 49financial off expectation after the 10-08 fire; rollback or hold? | **HOLD.** AMENDMENT 2 covers later fires under a per-fire NO-WORSE rule. e56 acceptance item 1 stays NOT MET. | @a0d336b0ab; counter-signed by the COO @9cf13be89a |
| `~M2` 1328: NO-WORSE test (iv) reverts a firm on a new unclassified buy | **ADOPTED** as AMENDMENT 2.1: grade the securities held at the pin only (`no_held_security_lost_class`). | @b3f3996a72 |
| SC-e-56 root cause | Routed to dell1 `~M1` through MSTR (bus 13060199). It is PARKED at dell1 because `~M1` is not live (msg 1325). | msgs 1321, 1323, 1325 |
| `~Y2` 1318: real filer entitlement for X-1 after-read 1 | A test filer stands in (msg 944 (2)). The real entitlement is Andrew's act and does not hold release 2. | msg 1320 |
| `~Y2` 1327: release 2 pair | **CTO half GIVEN**, with 3 conditions added: no login identity for the test filer; the put only after the equality read; live code re-read at start. | @6d24511482 |
| CVO slug 1326: IRPT_BCKEND sweep 17 | **Round analysis** @0a91529221: E1 is the custody release (`~P2`), E2 is release 2 (`~Y2`), E3 is the S388 HoldingsSnapshot share (`~M2`). S334 gets an interim per-order TAGAUTHZ override, and the fix is routed to laptop `0.5.0_AE_OpalETL` through MSTR. | msgs 1334-1336; MSTR route |
| `~D2` 1330: IRPT_DASHBD round 28 MAY-CLOSE | The analysis follows the CVO's L8 compile, which is next in the CVO's queue (its own summary). | -- |
| NFRA_TRNSPT round 4 (`~T2` 1177, 01:02Z) | The CVO's L8 compile has been owed since 01:02Z, and the CVO's queue did not list it. Pointed the CVO at it. The analysis follows the slug. | msg to `3.0.0_SA_CVO` |
| `~G2` row D2-S1: the F1 retry cannot be both seat-made and free of YCharts calls | **Portfolio half ruled.** A real Cottonwood account is taken from Opal's served platinum holdings (a seat act). **Principal half** goes to Andrew (below). Until then, no run as the service principal. | msg to `~G2` |

## Acts only Andrew can do

1. **Put `svc-irpt-analysis@opalinvest.com` on `OPAL_PRODUCER_PRINCIPALS` for one run** (the IRPT_YCDGEN F1 dell2 retry). This lifts a hold
   set by name: `resident_worker.py:115-120`, "the list changes only on Andrew's word ... No other principal goes on this list". REC: yes,
   for one run, with the entry removed after. The alternative is his own run (the organic arm).
2. The real X-1 filer entitlement: which person may file for which firms (msg 944 (2)). It does not hold release 2.
3. The BD Taildrop for IRPT_CUSTDY E3 (his device; MSTR coordinates).
4. The print page's DEV and PROD landings (IB-pr-356 at 63b9382a), after the custody release.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `release-census.py` at f7a9d0b34f (irpt-ycharts-generate): `changed_members=3`, which matches the pair.
- `get_live_agents`: 13 dell2 seats LIVE. `fabric-check.py --json` piped to python printed nothing, because the shape was assumed;
  `get_live_agents` was used instead.
- `comp-find '"IRPT_BCKEND-S334"'`: 2 hits across 59 files.
