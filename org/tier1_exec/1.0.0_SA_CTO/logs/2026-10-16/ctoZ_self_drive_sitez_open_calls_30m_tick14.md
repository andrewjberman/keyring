# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 13-14 (2026-10-16 ~07:58Z to 08:56Z)

**archetype:** COORDINATE
**secondary_archetypes:** VALIDATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## NFRA_OPLGTW -- the 22:00Z gateway finish

| input | act | record |
|---|---|---|
| CloudOps~Z 34830 / COO~O 34831: OG-ap-23 re-cut, release 3d5c9c8bf1 | CTO half SIGNED after git checks (tar line plus md5 census against trunk; client_* in DATA_GRANT + TIER_ADMITTED and out of NATIVE; 27 tools added, 0 removed). This corrects my earlier md5-vs-blob error | @2665f19c6a |
| CVO~Z 34835: OG-ap-23 CVO half SIGNED | relayed; all three halves signed | msgs 34836/34837 |
| CloudOps~Z commit 3e09a5f923: Phase B | deployed 08:13Z; 23 of 27 tools served; client admission and the CVO's C1/C2 all true; 4 tools AccessDenied on the internal reader. ROLLED BACK 08:28Z cleanly to d577e0e729 (row Z-S164) | 3e09a5f923 |
| my ruling to COO~O | grant the missing prefixes and redeploy the SAME release; fallback is a 23-tool re-cut if the grant is not applied by 18:00Z | msg to COO~O |
| COO~O 34856: is mdpf_get_model_composition's class right? | KEEP NATIVE: model definition, not client account data; Opal principals only; no re-cut | msg 34857 |
| COO~O 34860: OG-ap-27 (internal reader: bbg/, snapshots/, mdpf/etfs/gold/new_securities/, mdpf/feeds/model_composition/) | CTO half SIGNED; each prefix checked against its catalog row. Refusing "silver/*" was right: my message used the family label | @c18e2e007c |

## Other

- **XB-20261016T082054Z-9710 (ms's COMM_ASSIST questions to laptop COO~CA):** opened (body @294f6e3fd3, file @cde63d9338); MSTR~Z
  pushed and SENT it; COO~CA ACKED and had already answered ms by mail. The from side is CLOSED @e62271793d.
- **ms SQS inbox (relays 34848, 34862):**
  - The register edit waits for Andrew's own word.
  - Act row 35b3 is added, and I asked him at this terminal.

## Scope state

6 open on site Z, all acts only Andrew can do:
- 21c5, f0d2, 8ed7 and 21d9: his MC Portal sitting on site Z. COO~MP spawns the headed window on my word that he is at the box.
- def4: HELD (postponed).
- 35b3: his word on making ms a bus destination.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| git diff / show, md5sum | re-cut verification, the census cross-check | PASS; my earlier blob claim corrected |
| crossbox-call.py | open XB-9710; close the from side | OPENED; refused `line` until pushed (by design); HALF-CLOSED |
| open-calls.py | add 35b3 | ADDED |
