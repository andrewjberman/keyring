# /self-drive dell2 projects -- tick 13 (1.0.0_SA_CTO~DELL2)

**archetype:** COORDINATE

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_072xZ_SELF_DRIVE_60M_DELL2_IRPT_CUSTDY_IRPT_BCKEND_ADVI_COTBKF.md` @66a57498d9
**Ticks covered:** the event-driven work since tick 12, plus tick 13 (19:16Z). **state: ARMED**

## Scope state (19:16Z)

| project | status | dep_stage | sequence flag |
|---|---|---|---|
| IRPT_CUSTDY | active | EXECUTING | NEEDS-SLOT (known tracker gap) |
| IRPT_BCKEND | active | EXECUTING | none |
| ADVI_COTBKF | active | EXECUTING | NEEDS-SLOT (known tracker gap) |
| IRPT_YCDGEN | active | EXECUTING | none |
| IRPT_DASHBD | active | EXECUTING | none |
| NFRA_TRNSPT | active | EXECUTING | none |
| TCKT_VNEXT | active | PRD in the register (ADMITTED v0.2; round 1 issued by `~V2`) | none |

Denominator: 7 projects, 7 active. Inbox: 0 unread.

## Calls closed and acts

| input | ruling or act | carrier |
|---|---|---|
| MSTR 976 / 981 (bundle) | The rebuild ask was struck: the bundle moved at 18:33Z. This seat read both VersionIds: 12 members, exactly 2 changed as signed. `~M2` read the same independently | @d4b8c3d355 |
| `~V2` 989 (TV-d-1 release) | CTO half SIGNED. Scope corrected: the stack is Environment=Production on the shared portal API, so this changes the live Ticket Center for every portal. After-reads added | @b9b072decd |
| `~V2` 990 (TV-p-1 portal f7fa7fb1) | PASS for DEV. 3 rows: the firm is free text; the report read is owner-only; where is the one-account-per-file check | msg 19:12Z |
| `~Y2` 942 (X-1 closed in production) | `~P2` cuts the interactive_access cell; "ALL" never admits; the on-behalf entitlement is Andrew's grant | msg 18:1xZ |
| `~K2` 946 (portal 6d84304d, break 3) | PASS | msg 18:21Z |
| MSTR 950 / 962 (transcripts key, conditions 6-7) | NFRA_TRNSPT v0.2: FWD-8 and C-READERS name the Dell readers; no raw content in any record | @3aef5982b9 |
| `~P2` 972 (break 6: no custody read route) | Ruled (a): a scoped GET reusing `retained_export.resolve`; WORLD, under a pair | msg 18:39Z |
| `~G2` 994 (F1 stop, row S16) | REC taken: fix `response_envelope` once; lane IRPT_LIVE_SCOPE_P, so `~P2` cuts it; WORLD pair with a handler census | msg 19:0xZ |
| `~C2` 996 | YES: ADVI_COTBKF round 16, FWD-3 cells B-D built on stubs | msg 19:09Z |
| MSTR 991 (Andrew's first-day question) | Friction brief written and carried | @e5b9f1bc26 |
| MSTR 992 (Andrew: vendor egress, the Python installer, the store) | Relayed verbatim to 11 dell2 seats | msgs 1001-1011 |

## Acts only Andrew can do

1. The IRPT_CUSTDY portal DEV landing of 6d84304d (his word for portal landings).
2. **PROD promote of the print page** with the custody template (portal PROD is gated).
3. **The on-behalf filing entitlement:** which Opal person files for which firms. This is a grant beyond the current grants;
   TCKT_VNEXT's X-1 admits only firms named explicitly.
4. TCKT_VNEXT:
   - the portal DEV landing of f7fa7fb1;
   - confirming FWD-1 to FWD-8's DONE WHEN lines.
5. Lifting his PROD advisor hold, and whether a partner firm is told of the pre-fix export residual.
6. NFRA_TRNSPT:
   - the 14 flagged words;
   - the second reader;
   - Alyssa's corpus into bronze.
7. ADVI_COTBKF: sending the near-match page to Cottonwood.
8. Answers asked: R13; FWD-17 to FWD-23.

Removed this tick: the Bloomberg share (approved, msg 988) and the vendor-word items for the Dells. Andrew: "The Dell Boxes have vendor
egress as needed". Each vendor use is still named in its own order.

## Completion test

NOT DONE: 0 of 7 complete. 7 REACHABLE, 0 UNREACHABLE.

## Compiler Tools

- Reading the Terraform stack's `Environment` tag and `portal_api_id` caught a "DEV" scope that was PROD.
- Asking the repository (`git log -1 -- <file>`), not the `safe-commit` output, caught two silent non-commits.
