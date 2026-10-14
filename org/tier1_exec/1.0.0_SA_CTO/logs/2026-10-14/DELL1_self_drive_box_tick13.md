# /self-drive dell1 box open calls -- tick 13 (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~11:30Z)

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261013_203xZ_SELF_DRIVE_DELL1_BOX_OPEN_CALLS.md` @bcd3be8ec3. Cron 4e032862 (:17). **state: ARMED**

## Measured

- **Box list:** rows=72, **open=0** (11:26Z).
- **Cross-adjudications:** 14 of 14 RULED.
- **Inbox:** 0 unread. Msgs 5455 and 5460 since tick 12 were acked and acted on.
- **Project blocking fields:** 18 dell1 projects scanned (by `fabric`/`placement`), 10 active, 4 naming the CTO.
  - AMGT_RESAPP: bm-4 needed "a DT the CTO names". Ruled below.
  - ETFS_RIVALS: the apply window was already ruled. Owed by the COO.
  - ADVI_FIRMBKTS: a superseded fence line. Not a call.
  - MDPF_CANON: each wait already has an owner.

## Acts since tick 12

| item | ruling / act | record |
|---|---|---|
| Approval faa4 (`~R1` msg 5455; bm-1 @84fd6461bb re-registered; f376 was bound to 4eb56d57d2) | **CLOSED approved.** origin head read 84fd6461bb, the head the approval ledger names | `AMGT_RESAPP/ledger/CTO_APPROVAL_PORTAL_CAND_PE_BASIS_AND_REASONS_20261014.md`; reply msg to `~R1` |
| MDPF_HEALGAP round-5 close (`~G1` msg 5460) | **COMPLETION_GRADES.round5.json: 6 of 6 REALIZED.** The schema reads 0 errors and an R6 dry-run reads 0 violations. FWD-6 rests on round-4 ADDENDUM 1. The HG-t-18 FT code is merged but not deployed, and the FT hold binds any deploy of it. `~G1` has since flipped `dep_stage` to CLOSED | @f0014df3dc; msgs 5464/5465 |
| `~G1` re-seat (DIRECTION_DELL1 section 4) | **HELD.** Slot 1 (the RESAPP AI fill) is held by `~R2`. Slot 2 (YCharts) is unregistered: its L1 brief is still at the CRO | msg 5465 to MSTR~DELL1 |
| AMGT_RESAPP bm-4 DT | **Named `0.4.0_DT_ClientPlatform`** (the same DT as bk-7, bl-2 and ar-6). It is NOT REGISTERED, so MSTR~DELL1 is asked to seat it. The page is Opal-internal, so no word from Andrew is needed | msgs 5466/5467 |

## Completion test

Box scope: **NOT DONE**. The stop is Andrew's stand-down. REACHABLE calls 0, UNREACHABLE 0.

## ACTS ONLY ANDREW CAN DO (cited)

- **Sign in at the dell1 console after the NFRA_CTLPLN restarts** (his login).
- **One session from his own work Claude through the gateway** (NFRA_OPLGTW FWD-21: his identity and login).
- **The MDPF_SECCLASS client-facing BD Mix PROD push** (CLAUDE.md push law).
- **Lifting the ASTN FT hold** ("Dont attempt FT until I return": a hold he set by name).

## Compiler Tools

`open-calls.py list/close --decision approved`; `xadj.py list`; `active-commitments.py`; `comp-find --files` (bm-4: 1 hit
of 565 scanned); `jsonschema` plus `missions-tree-index.close_violations` (an R6 dry-run of the grades);
`get_agent_status` (DT liveness). **Rail:** two comp-rail denials, an R1 recursive grep and an R6 pipe that would cut
the denominator; each was re-run as RUN NEXT. **Gap:** project.json has no single `device` key (it is `fabric`/`placement`),
so a scan keyed on `device` read 0 of 0. The positive control (HEALGAP's own keys) exposed that.

-- 1.0.0_SA_CTO~DELL1
