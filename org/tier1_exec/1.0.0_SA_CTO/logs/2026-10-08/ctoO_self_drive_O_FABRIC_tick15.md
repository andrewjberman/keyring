# 1.0.0_SA_CTO~O -- /self-drive 30m ~O fabric, tick 15 (2026-10-09 04:51Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_215xZ_SELF_DRIVE_30M_O_FABRIC_FOUR_PROJECTS.md`
@ba8c4598fb. Cron d7c133e4. `state: ARMED`.

## Scope

| project | status | dep_stage | open TOs |
|---|---|---|---|
| NFRA_OPLGTW | active | EXECUTING | 8 (OG-pf-1 issued @02feea1287, round 33 workstream ENTITLE-R33) |
| NFRA_OPALAI | active | EXECUTING | 3 |
| NFRA_MCPORTAL | active | EXECUTING | 4 |
| NFRA_MCPINDEX | active | EXECUTING | 1 (round 8 L5 decomposition @7a37c5b906; PRD v0.7 ADMITTED, CVO~Z @916621b0b8) |

Inbox: 0 unread. Acked: 32378, 32382, 32385.

## Rulings since tick 14

### 1. Andrew's 13-month reach (2.0.0_SA_COO~O ask, msg 32382)

**Facts read in r29's Phase A:**
- Andrew holds no data profile.
- `data_entitlement.decide` denies every Schwab tool to an unprofiled principal.
- A profile confines its principal to its grant's tools.

**Refused: "unprofiled = full".** It would give every unknown Opal user all data and break C2's fail-closed rule.

**RULED:** a profile confines only the data-grant tool family, which is the `schwab_*` tools plus the Black Diamond data tools.
- Andrew then gets a profile at v2.2 width with 13 months.
- `opalbloomberg` mirrors that profile in r30.
- Cut as OG-pf-1 @02feea1287.

**r29.** OG-rl-15 A7 writes Alyssa's grant only.

### 2. Consequence confirmed (msg 32385)

Alyssa gains her 52 non-data tools past the profile. This is intended, on Andrew's ~01:5xZ word (@0035550443).
- Her data reach is unchanged, tool for tool.
- `download_filtered` stays refused.
- The write-class and destructive-op gates are unchanged.
- test_ogz1_ac07 is to pin the new arm.

### 3. r30's payload

OG-pf-1, OG-tg-1 (the Opal-users gate), and two grant writes:
- Andrew's profile;
- the `opalbloomberg` mirror.

## Open calls in scope

None.

## Acts only Andrew can do

None owed.

## Completion test

NOT DONE: 0 of 4 projects read `status: complete`. REACHABLE 4, UNREACHABLE 0.

## Compiler Tools

- `to-check.py --all --project` x4. Worked. Gap: none.
