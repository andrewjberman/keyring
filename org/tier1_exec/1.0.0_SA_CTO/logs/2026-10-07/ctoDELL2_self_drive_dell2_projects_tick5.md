# /self-drive dell2 projects -- tick 5 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 4 (@df522860d7), plus tick 5 (10:45Z). **state: ARMED**

## Scope state (10:45Z)

All 5 are `active` / `EXECUTING`. Inbox: 0 unread. Read and acked since tick 4: 290, 295, 301, 302, 307, 309, 310, 328, 332, 334,
335, 336, 338, 343, 345, 347, 349, 352, 355 and 357.

## Outcomes that moved

- **ADVI_COTBKF FWD-5 REALIZED** (CB4d5-AC3 MET by the CVO): 3 of 9.
- IRPT_BCKEND FWD-5 is NOT yet: E-M1 met, but the PROOF clause's four cases are unread (round 31 E-M2 cut).
- IRPT_DASHBD FWD-8 is NOT yet: 3,279 of 9,078 segments are still unexplained on the gross basis.

## Laptop changes received

- Hold A LIFTED for 2010-2027 (106145). The calendar fix is in dell2 CLOUD @0a73ed06a0. This un-parked ADVI_COTBKF E2 and
  IRPT_CUSTDY's SI windows.
- The fence join landed at least on `opal-data-49financial` (measured by `~D2`, 10:44Z). The standing relay rule is amended:
  probe once from dell2 first.
- The relays end with the fence apply (TO-APPLY-4) and a scoped SendCommand grant (106139).

## Driver acts (dell2 LOCAL)

| act | hash |
|---|---|
| IRPT_BCKEND round 62 Y L10 (E-Y4's WORLD half binds the next release; S358 to `~G2`) | a06f3e6249 |
| IRPT_DASHBD round 18 L10 (closure-day segments measured, not explained by assertion) | 62026ca511 |
| `.owned-paths.yaml`: the tests of the one-writer files join `~G2`'s lane (msg 309) | 956a4d13ce |
| ADVI_COTBKF CTO half, E2 links apply (1,450 of 1,450 equal to the laptop) | 792b16742d |
| IRPT_BCKEND PRD v0.29: ExportBundle `custody_report_ref` / `CUSTODY_REPORT` (named apart from "client report") | 3b4801a0fa |
| ADVI_COTBKF CTO half, CB-d-4 restricted-prefix statements (for the laptop apply) | 87d7642a72 |
| ADVI_COTBKF round 6 L10 (FWD-5 REALIZED; round 7 E1-E3) | 1c9c98e652 |
| IRPT_BCKEND round 30 M L10 (round 31 E-M2) | e252251fbe |

## Rulings by message

- 302 (laptop finding: the host runs off-trunk 409e3066d1): `~G2` lands M1 on the trunk now, code only. Done @035443efaa (msg 332).
- 307 (`~D2`): (b) cut E2 now. E1 is replaced by E1', an Opal-side test of BD's day-count, so no vendor pull is needed yet.
- 335 (`~P2`, W140-S1): strip non-public members server-side. W140-S2 (directory.json reader) is out of the census population.
- 336 (`~P2`, W138-S2): PRD v0.29.

## Acts only Andrew can do

Unchanged: the IRPT_YCDGEN F1 retry (his login; the only open leg of `irpt-ycdgen-r6-branch-b2`); one IRPT_BCKEND export (his
per-use vendor word); an advisor test principal / opening PROD `/investor-reporting` (a gate he set by name); handing IRPT_CUSTDY
reports to the advisor (egress); confirmation of IRPT_YCDGEN FWD-17 to FWD-23 (offered). New and conditional, not yet listed: a
split-range BD pull for IRPT_DASHBD, only if E1' leaves most of the 2,299 unexplained.

## Completion test

NOT DONE: 0 of 5 complete. 5 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- `opal_naming` and git reads only. The merge-in-progress refusal of `safe-commit` was handled by waiting on `.git/MERGE_HEAD` in
  the background, never by forcing.
