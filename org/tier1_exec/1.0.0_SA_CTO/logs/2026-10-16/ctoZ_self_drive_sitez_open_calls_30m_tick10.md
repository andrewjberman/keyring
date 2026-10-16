# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 9-10 (2026-10-16 ~05:56Z to 06:56Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## Acts and rulings

| input | act | record |
|---|---|---|
| relay 34756: muse asks for OpalGateway MCP access (mail and Teams) | MSTR~Z seated 4.0.0_SA_CRO~Z for a read-only scope; muse acked by mail through the Gmail connector | Gmail 1a143609c696d900 |
| CRO~Z 34773: the scope | ruling: route C, a muse-only narrowed client (reads + create_draft, no irreversible send), as an OPLGTW cell after 22:00Z; route A (sign in as Andrew) is Andrew's act only, row 8f44; muse answered | @d5be3853aa; Gmail 1a1436bda8a3035e |
| CRO~Z 34789: Andrew-direct "ok i want the COO~O to have this work folded in to OPLGTW, let CTO~Z know that." | confirms route C's placement; COO~O told | @6a73be1bba (record @66f25c55e2) |
| COO~MI 34780: r18 ASSETS, 91 no-tool rows | rec RATIFIED: OUT per group, each with a reopen condition; 9 market-data rows to the ETFS tool question | @33d41059d9 |
| COO~O 34761: OG-ap-26 (GetItem moves to the internal reader) | CTO half SIGNED; the CVO half relayed; all three signed | @4d0a8d3c0d |
| Andrew-direct ~06:2xZ "approve 92c0 and delete both scratch folders" (relay 34763) | SCRATCH3 and SCRATCH_TARGET_Z DELETED (before EXISTS, after ABSENT); ae72 **CLOSED** ruled-by andrew | record @1e88a05fd3 |
| COO~O 34784: OG-ap-23 code batch release | CTO half **REFUSED**: the claimed tar-line edit is absent, so the staged app/refs files never reach the archive and untracked worktree copies would ship; the trigger blobs are stale | @5ffc9f2262 |
| CVO~Z 34790: OG-ap-23 CVO half REFUSED (client_* NATIVE, against v3.1 Ruling 2) | PRD v3.14: client_* go in DATA_GRANT_TOOLS + TIER_ADMITTED_TOOLS (master_admin only, fail-closed) with a served negative arm; a per-firm grant shape is the next increment. Relayed with my tar fix: one re-cut carries both | @f2b066d9ad |

**Self-correction:** my 06:53Z message to COO~O cited "msg 34782" for the muse cell. I held no such id, and corrected it in msg 34796.

## Scope state

7 open on site Z, all acts only Andrew can do, each with its citation:
- a519: one Teams message from his own account;
- 21c5, f0d2, 8ed7, 21d9: one MC Portal sitting, including his login as Opal Bloomberg;
- def4: one sitting with Alyssa;
- **8f44 (new):** his word, only if muse should carry his full gateway reach before route C lands. This is an entitlement beyond any
  grant this fabric holds.

**The 22:00Z finish rides on the OG-ap-23 re-cut** (the tar fix plus v3.14), after which all three halves re-sign.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| git diff / show / rev-parse | OG-ap-23 release read (parent, 31A/13M/0D, tar line, hunks, blobs) | found the missing tar edit and the stale blobs |
| open-calls.py | add 8f44; close ae72 | OK |
| rm -rf (on Andrew's word) | two named scratch paths only | before/after existence printed |

