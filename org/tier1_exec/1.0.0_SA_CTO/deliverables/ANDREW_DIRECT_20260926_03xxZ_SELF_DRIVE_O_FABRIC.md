# ANDREW-DIRECT 2026-09-26 ~03:0xZ -- /self-drive arming: the ~O fabric's directives as a whole

- Channel: terminal, the 1.0.0_SA_CTO~O session, site Z. Andrew pasted a template "for how you should govern the ~O
  fabric, institute it with your team". Recorded by 1.0.0_SA_CTO~O, same turn, BEFORE tick 1 (skill section 0.5).
- The template carried two placeholders, `<this fabric>` and `<PROJECT(S)>`. This seat filled them (see ARM TERMS);
  the fill is this seat's reading, not his words.

## Verbatim

> Here's a template for how you should govern the ~O fabric, institute it with your team:
>
> /self-drive [30m] <this fabric> directives as a whole. Priority: <PROJECT(S)>.
>
> Arm terms (from Andrew, 2026-09-26):
> - Scope: every live directive on your device (python .tools/directives-check.py --json); drive the priority projects first.
> - Egress is permitted for API calls this session -- no per-use word per vendor call, but every call is ledgered by the seat that makes it. Spend, contracts, entitlements and hold-lifts are NOT covered.
> - Open calls: decide on your own REC the same tick. Design fork -> CRO researches past patterns first. Governance fork -> CVO adjudicates. A needed agent that isn't live -> spawn it.
> - Served output still moves only under a never-widen sign-off (CTO half + a second, non-acting half).
> - COO loops: give every COO its loop instruction now. Prefer /canonical-drive for their segments; a project carrying closer_contract (which /canonical-drive skips) runs /closer-drive on its seat's FAST lease -- re-arm leases long enough to span an unattended night. Use your discretion.
> - Personal acts that would need Andrew's hands (signed-in walks, retries, uploads): have an agent do them with a HAR, on a bounded temporary principal (created, used within 60 min, deleted and verified) under a two-half sign-off.
> - Commit the arming record before tick 1; log only on a substantive delta or hourly; stop on DONE read from the register, HELD-AT-STOP, or Andrew's stand-down.

## ARM TERMS

| term | value |
|---|---|
| driver | `1.0.0_SA_CTO~O`, site Z (device read: `bash .tools/agentbus-sqs.sh device` = sitez) |
| scope | the ~O fabric: directive **D6** (sitez; members NFRA_OPALAI, NFRA_MCPORTAL) plus the two D9 projects this fabric drives, **NFRA_MCPINDEX** and **NFRA_OPLGTW** |
| priority | NFRA_OPALAI, NFRA_MCPORTAL, NFRA_MCPINDEX, NFRA_OPLGTW (the goal of record `ANDREW_DIRECT_20260924_210xZ_CTO_O_GOAL_FINISH_ALL_D6_OPAL_AI.md`) |
| cadence | 30 minutes |
| open calls | decided on this seat's REC the same tick; DESIGN fork -> a ~O CRO researches past patterns first (none live: spawned when the first design fork arises); GOVERNANCE fork -> `3.0.0_SA_CVO~O` adjudicates |
| egress | API calls permitted this session, each ledgered by the calling seat; NOT spend, contracts, entitlements or hold-lifts |
| served output | never-widen sign-off: a CTO half plus a second, non-acting half |
| personal acts | by an agent with a HAR, on a bounded temporary principal (created, used within 60 min, deleted and verified), under a two-half sign-off |
| paired_with | `/canonical-drive 30m` at `2.0.0_SA_COO~O` (COO MODE) and at `3.0.0_SA_CVO~O` (CVO MODE), over the same four projects; none carries `closer_contract` (read from each project.json this turn), so no /closer-drive lease |
| log | on a substantive delta or hourly; quiet ticks append to `org/mcp/drive_ticks/1.0.0_SA_CTO~O.md` |
| stop | DONE read from the register (all four projects `status: complete`), HELD-AT-STOP, or Andrew's stand-down; one stop covers the paired halves |
| supersedes | this seat's 30-minute `/loop` (Andrew 2026-09-24, record `ANDREW_DIRECT_20260924_210xZ_CTO_O_LOOP_30M_DRIVE_OPAL_AI.md`); the goal of that record stands |

## Scope resolution, measured at arm time (~02:5xZ)

```
SELF-DRIVE SCOPE: ~O fabric -> D6 + 2 D9 projects -> 4 project(s) [NFRA_OPALAI, NFRA_MCPORTAL, NFRA_MCPINDEX, NFRA_OPLGTW]
  device: SITEZ   open TOs (register): D6 4, D9 17 (D9 is shared with other projects)   (denominator: 15 live directives)
```

- All four projects read `status: active`, `dep_stage: EXECUTING`, no `closer_contract`.
- Sequence (`python .tools/sequence-check.py --project <CODE>`): NFRA_MCPINDEX PLACED stage 0, flags none;
  NFRA_OPALAI, NFRA_MCPORTAL and NFRA_OPLGTW UNPLACED (their own directive's rules govern them).
- Live ~O seats: `1.0.0_SA_CTO~O`, `2.0.0_SA_COO~O`, `3.0.0_SA_CVO~O`; the DS lane `0.4.0_DS_ClientPlatform~D`
  works NFRA_MCPINDEX orders.

## Reading, narrow

- **"every live directive on your device"** is read through the template's own `<this fabric>`: the ~O fabric drives
  the directives it holds. The other site-Z directives (D1, D4, D5, D7, D12) are the ~Z fabric's; Andrew's standing
  word to this seat is not to take up AMGT or other fabric work. If he meant the whole device, that is a scope change
  for his word.
- **Device finding, surfaced (skill 0.2):** the register reads D9 `device: LAPTOP`, and NFRA_MCPINDEX and NFRA_OPLGTW
  `placement: LAPTOP`, while both are driven on site Z by this fabric (NFRA_MCPINDEX released to ~O by the laptop;
  NFRA_OPLGTW issued by `2.0.0_SA_COO~O`). The skill's guard would refuse them. This is a GOVERNANCE fork and goes
  to `3.0.0_SA_CVO~O` in tick 1, with this seat's REC to keep driving them, because the work is already here and
  Andrew's goal names MCPINDEX. The register fix itself routes to `0.0.0_AB_MSTR~Z`.
- **Personal acts in the switchover runbook:** a bounded temporary principal cannot stand in where the act's point is
  a SPECIFIC identity -- the Analyst's gateway sign-in as Opal Bloomberg (step 5) and Andrew's own `oid` for the owner
  key (step 7). Those stay Andrew's hands. The clause reaches acts whose identity is incidental; each is named when it
  is planned, under its two-half sign-off.
- The egress term does not cover entitlements: an access grant for a colleague still rests on its own word (call 2 of
  record `ANDREW_DIRECT_20260926_022xZ_CTO_O_OPEN_CALLS_1_TO_6_ANSWERED.md`).
