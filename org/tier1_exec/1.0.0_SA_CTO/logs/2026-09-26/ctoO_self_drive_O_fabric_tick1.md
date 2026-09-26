# /self-drive ~O fabric -- tick 1 (2026-09-26 ~03:3xZ)

- Driver: `1.0.0_SA_CTO~O`, site Z. Arming record:
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d.
- Cron: job 9999d604, minutes 7 and 37. The superseded `/loop` cron 886bf96f is deleted.
- state: ARMED

## Scope
D6 (NFRA_OPALAI, NFRA_MCPORTAL) plus NFRA_MCPINDEX and NFRA_OPLGTW (D9). 4 projects: all `active`, `EXECUTING`, no
`closer_contract`. Sequence: NFRA_MCPINDEX PLACED stage 0, no flags; the other three UNPLACED.

Open task orders, read from the order files this tick (last `<status>` tag):

| project | non-terminal orders |
|---|---|
| NFRA_OPALAI | OA-f-2 (release), OA-t-1, OA-t-3 (held for the switchover) |
| NFRA_MCPORTAL | MP-a-1 (writer apply; G-PYPI given, owner key owed) |
| NFRA_MCPINDEX | MX-c-1, MX-c-5, MX-d-2, MX-r-3, MX-s-1, MX-s-2, MX-t-8, MX-v-6 |
| NFRA_OPLGTW | OG-v-4, OG-v-5 (own gates G-C/G-D, G-E/G-F) |

## Inbox this tick
2 read: `2.0.0_SA_COO~O` msg 25986 (decision request) and `1.0.0_SA_CTO~Z` 20260926T032914Z (egress term, no ask).

## Calls, decided or routed
1. **NFRA_OPALAI-Z-S23, Alyssa's grant (COO~O msg 25986).** Decided on REC: **(B)**, issued now as addendum A2, not
   in round 2. (A) names Schwab custodial accounts, which breaks Andrew's "portal figures only" (call 2 of record
   `ANDREW_DIRECT_20260926_022xZ_CTO_O_OPEN_CALLS_1_TO_6_ANSWERED.md`). Design direction, from the build ladder
   (rung 2, the estate already has it): extend the existing grant grammar to admit zero Schwab masters plus a
   portal-dataset scope that `opal_asker_query` honours, never a second grant store. Alyssa's Entra oid is resolved
   from the directory by the operator path. Sent: msg 20260926T033321Z.
2. **D9's LAPTOP device stance vs this fabric's work (GOVERNANCE fork).** Pitched to `3.0.0_SA_CVO~O` with REC keep
   driving and route the register fix to `0.0.0_AB_MSTR~Z`: msg 20260926T033451Z. Verdict pending.
3. **Scope overlap on D6.** `1.0.0_SA_CTO~Z` armed sitez directives as a whole (@f3b85ff6a5), which includes D6.
   Asked to carve D6 out so that one CTO rules per project: msg 20260926T033403Z. Goes to the CVO only if contested.

## Acts
- Z-S21 disarmed as row NFRA_OPALAI-Z-S22 @19ad8abc17. origin/CLOUD 079fbf7d8e names the served 0af72fb1d0 and
  carries the laptop's Teams fixes. The manifest release_note is stale and is left to OA-f-2.
- Loop instructions: `/canonical-drive 30m` over the four projects, COO MODE at `2.0.0_SA_COO~O`
  (msg 20260926T033555Z) and CVO MODE at `3.0.0_SA_CVO~O` (msg 20260926T033650Z).
- Scope statement to `0.0.0_AB_MSTR~Z`: msg 20260926T033921Z.

## Completion test
NOT DONE: 0 of 4 projects `complete` (read from each project.json). Reachable: 4 of 4.

## Held at Andrew
None. The switchover sitting's identity-bound steps (the Analyst's gateway sign-in as Opal Bloomberg, and Andrew's
own oid for the owner key) are acts, not calls. They stay his hands; see the arming record.

## Compiler Tools
None run this tick.
