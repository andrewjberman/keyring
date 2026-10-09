# /self-drive dell2 fabric (7 projects, 30m) -- tick 16 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_172xZ_SELF_DRIVE_30M_DELL2_ALL_FABRIC_PROJECTS.md` @33d7de3039
**Ticks covered:** tick 16 (00:49Z), plus the event-driven work since tick 15 @4aeead6f7d. **state: ARMED** | cron b0f6db2a

## Inbox

0 unread. Since tick 15, read and acked: 1964, 1966, 1979, 1981, 1987, 1991, 1995, 2006.

## Calls ruled and acts taken since tick 15

| Call (msg) | Ruling | Record |
|---|---|---|
| IRPT_DASHBD round 30 drain-end (~D2 1964) | provisional analysis | @4cfe197b0c |
| CVO 1979: round 30 analysed without the L8 compile | correction accepted. `~D2` routes every drain-end to `3.0.0_SA_CVO` | ADDENDUM 1 @b88cc62432 |
| IRPT_DASHBD rounds 30-31 slug (CVO 2006, ADJUDICATION_v16): reader of record; FLOW_TIMING | **`tieout_compound_v2.py` is the reader of record. Flow-start is adopted in the reconciliation reader only, with served values unchanged.** Round 32 = E1 to E3 | analysis @fe8e06016b |
| IB-pr-380 PASS, but rows W188-S1/S2 (~P2 1987) | IB-pr-381: (a) the writer count of latest.json first; 380 and 381 ship as ONE release under one pair before 10-12 | msg 003653Z |

## Standing changes noted

- **Step G applied at 00:29Z** (1981, 1991): the irpt-render public key is readable, and `/mdpf/custody_source` writes are denied (reads allowed).
  The laptop CTO ruled that **DenyCutoverParameterWrites stays**, like DenyShellDocuments. dell2 does not remove either with its step F
  rights.
- **Law edit 538f0f51a7** (1966): `box/*` is a shared branch, and only MSTR or box-sync pushes it. This seat already commits only.
- **GC fix 3be885041e** (1995): long detached jobs are declared with `.tools/detached-job.sh`.

## Scope state (denominator 7)

Six projects are `active`, EXECUTING. NFRA_TRNSPT is `active`, ROUND_CLOSE.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Acts only Andrew can do (unchanged)

1. **A standing word for one Kimi K3 call per Analysis Request.** Citation: NFRA_TRNSPT PRD C-KIMI, and CLAUDE.md vendor egress.
2. **The S3 deletes of release 4's read-4 test upload.** Citation: CLAUDE.md Agent Autonomy.
3. **The `/closer` build word for IRPT_ANLREQ, plus DONE-WHEN.** Citation: CLAUDE.md rule 27, and Andrew-direct 2026-09-03.

## Compiler Tools

`git show --stat` on the round drains; the CVO's ADJUDICATION_v16; safe-commit.sh.
