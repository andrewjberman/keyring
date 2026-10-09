# Session log -- `1.0.0_SA_CTO~Z`, 2026-10-09 ~02:0xZ to ~04:0xZ: after the DELL1 move

**archetype:** COORDINATE
**Context:** the `/self-drive` loop ended STOPPED-BY-OPERATOR at ~02:0xZ (final log @334aa39ab6), with all five AMGT/DSGN/RIVALS projects
on DELL1. This seat now rules site-Z calls and signs site-Z halves for dell1's producer-path acts (`1.0.0_SA_CTO~DELL1` msg 1267). It
drives no project.

## Andrew-direct in this window (records by the receiving seats)

| when | words | record |
|---|---|---|
| ~02:4xZ | "yes" to the CLAUDE.md egress edit | `org/tier0_exec/0.0.0_AB_MSTR/deliverables/ANDREW_DIRECT_20261009_024xZ_LAW_EDIT_CLAUDE_MD_EGRESS_OPEN_EXCEPT_BBG.md` @662dc43595 |
| ~03:2xZ | "opal-gateway-bbg should be an exact copy of opal-gateway for now ..." | `deliverables/ANDREW_DIRECT_20261009_032xZ_OPAL_GATEWAY_BBG_MIRRORS_OPALGATEWAY.md` @4fb7326f67 |
| ~03:3xZ | "it should only accept inquiries from opal capital users however, no external users, should not even respond at all ..." | `deliverables/ANDREW_DIRECT_20261009_033xZ_BBG_CONCIERGE_OPAL_USERS_ONLY_GATE.md` |
| ~03:5xZ | "why is DELL1 sending deployment orders here? They should be able to run deploys on their own box" | relayed, msg 32342 |

## Acts and rulings

| item | act | carrier |
|---|---|---|
| CLAUDE.md egress law edit | committed with the order as `ANDREW_LAW_EDIT_ORDER`. The record's exact block exceeded the 30,720-byte budget (30,807), so the same three elements went in at 30,705 bytes, stated in the commit and to `0.0.0_AB_MSTR~Z`, who broadcast it (msg 32294) | @4d77a9c3ea |
| RESAPP Bloomberg calls 107a, 493c | CLOSED ruled_by andrew, citing this seat's record of his "route them through backfill queue" | open-calls list; record @0953984a75 |
| Producer-order issuer (msg 32270) | each project's own issuer orders site-Z acts; `2.0.0_SA_COO~O` takes OPAL_BBGTML-Z-S13 | msg 02:10:50Z |
| Who files the two RESAPP queue requests (msg 32280) | dell1's `2.0.0_SA_COO~R1` | msg 02:31:19Z |
| HVST-bs-2 installer merge | site-Z CTO half SIGNED | `deliverables/CTO_HALF_AMGT_HARVST_BS2_INSTALLER_MERGE_20261009.md` @8630dee4ff |
| RESAPP dd-1 filing-cutter merge | site-Z CTO half SIGNED, plus C3: the COO census said N = 3; 6 importers exist, none scheduled on Z | `AMGT_RESAPP/ledger/NEVER_WIDEN_ROUND80_DD1_SITEZ_CTO_HALF.md` @f1a7df146f |
| HVST-bs-3 continuous runner | site-Z CTO half SIGNED, plus C-e: the process GC exempts only `wk-*` worktrees, so the pin is named `wk-harvest-runner-pin-c1be67f53c` and a GC dry run must list the runner exempt | `deliverables/CTO_HALF_AMGT_HARVST_BS3_RUNNER_ACTIVATION_20261009.md` @37aefc2855 |
| DEMQUE meter (msg 32306) | one issuer, dell1's DEMQUE COO. One site-Z uploader of the existing `bbg_budget` JSONL ledger (`data/etfs/scripts/rivalfunds/bbg_budget.py`), with no producer edited; OPAL_BBGTML is a named gap | msg 03:14:39Z |
| Rule 27 collision (msg 32324) | my "one producer owner" amended to per-project CloudOps lanes seated on demand; dell1's same proposal ruled YES (msg 32328): `~ZQ`, `~ZV`, `~ZC`, `~ZW`, `~ZR` | msgs 03:31:09Z, 03:31:44Z |
| `~Z` residue (msg 32342) | NFRA_OPLGTW keeps `0.7.0_AE_CloudOps~Z` (2 pending orders). MX-s-19 (gated since 10-01) gets a lane when it ungates; the earliest-issued rule is set aside to avoid moving two live orders. aw-1 goes to `0.7.0_AE_CloudOps~DELL1` on Andrew's word; its halves stand | msg 03:54:18Z |
| Bloomberg seat sender gate (`1.0.0_SA_CTO~O` msg 32329) | `bbg-teams-assist` step 0b: no send of any kind unless a returned field shows `@opalinvest.com`. Today only `from_name` is returned, so it fails closed until the gateway shows identity or its gate is live | @ef8c4e57a1 |
| tc-1 merge CTO half | deferred until tw-1's J1 reads MET | msg 03:31:09Z |

## Open, owed by this seat

- tc-1's site-Z CTO half, when V1 re-asks after tw-1 J1.
- The DEMQUE uploader's site-Z half, when asked.
- Amend `bbg-teams-assist` step 0b when the gateway returns sender identity or confirms its pre-filter.

## Compiler Tools

- `git diff --stat` and `--numstat`, `merge-base --is-ancestor`, `ls-tree` on every half's branch. Each half carries its own reads.
- PowerShell scheduled-task and process reads: the Continuous Cycle task ABSENT, 0 harvest processes, both OpalResearch tasks Disabled.
- `kill-maint.ps1:215-293` read for the GC exemption rule. It found the bs-3 hazard before the act.
- safe-commit's byte-budget refusal on CLAUDE.md, which worked as built.
