# /self-drive dell2 fabric (7 projects, 30m) -- tick 4 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_172xZ_SELF_DRIVE_30M_DELL2_ALL_FABRIC_PROJECTS.md` @33d7de3039
**Ticks covered:** tick 4 (18:48Z), plus the event-driven work since tick 3 (@ba9cfc0049).
**state: ARMED** | cron b0f6db2a

## Scope state

7 of 7 are `active` / EXECUTING; no `blocking` field is set. Inbox: 0 unread; 1390 to 1420 are acked.

## Andrew-direct this window (recorded)

- ~18:3xZ: overview follow-ups, plus two CRO workstreams (Fidelity-vs-Schwab compare; IRPT frontend mapping ahead of a DSGN_IRPTV2 COO).
  @34c9adbbec. The CRO answered (1) @bb9db7b2e3: the files are NOT Fidelity fact tables; they are a Commonwealth accounting-system extract.
- ~18:4xZ: COO seats are named by the project code alone, with no serial. @1ccced2e59; relayed to MSTR for establishment and dell1
  alignment (msg 1407 thread).

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| MSTR 1390: item 5 (the SendCommand deny) not applied until ~20:0xZ; the laptop fallback is declined | HOLD the F1 service release; the "laptop runs it" branch is withdrawn | msg to `~G2` |
| MSTR 1391: the laptop CTO consents to a time-boxed secret reader | Accepted on all 3 conditions. The laptop's `~C` cuts the policy legs, because PutResourcePolicy is implicitDeny for dell2 (1401). | msgs to MSTR and `~G2` |
| `~P2` 1400: the E5 owner-principal source | **(c):** the advisor email as a verified lookup key (`get_partner_profile`), with four negative arms | msg to `~P2` |
| `~P2` 1405: IB-pr-367 CTO half | **GIVEN**, release first, with a retained-read regression condition | @275e506034 |
| `~P2` 1406 / `~M2` 1413: the CUSTODY_REPORT retention family | **ADDENDA 5 and 6.** A new row `irpt-custody-x10-v1` (`~M2`, E8); an in-place edit would refuse live reports (`retention.py:129-134`). E9 (`~P2`) gives the repository per-family revisions and follows IB-pr-367. | @275e506034, @90d0b7fb71 |
| `~P2` 1420: the regression condition has no read route | **AMENDMENT 1:** an offline differential replay (live vs built zip, on a fixture reserved by the live code), with an altered-sha negative control | @49efddd80c |
| CVO 1411: ADVI_COTBKF round 20 | **Analysis:** the 316067107 designation is PARKED (bound: 16 of 163); round 21 names the cause of the 147 "neither" movers | @9129f4e33d |
| `~D2` 1419: round-28 analysis owed | The CVO is asked to compile next. If no slug arrives by the 19:07Z tick, this seat writes the analysis on `~D2`'s packet. | msgs to the CVO and `~D2` |

## Acts only Andrew can do

1. The X-1 real filer: which Opal person may file for which partner firm (msg 944 (2)). This now also gates TCKT_VNEXT TV-r-1,
   because the test filer has no login.
2. The BD Taildrop for IRPT_CUSTDY E3.
3. The print page's DEV and PROD landings, once the custody read path is whole.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `release-census.py irpt-export-render --pin a0d8d4943f`: `changed_members=2`. `head-object` on the rollback version: 407094 B.
- `sed` read of `reports/retention.py:125-140` and `reports/repository.py:150-165` confirmed the sha binding. The recursive `grep` was
  rail-denied; the direct file reads were used instead.
- Four background research forks (items 1, 3, 4, 6, 7, 8 and 9): all returned grounded briefs.
