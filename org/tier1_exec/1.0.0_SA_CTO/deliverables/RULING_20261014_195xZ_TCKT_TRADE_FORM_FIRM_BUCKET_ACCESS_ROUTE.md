# RULING 2026-10-14 ~19:5xZ (1.0.0_SA_CTO, cluster lead) -- the ticket API's trade-form access to three firm buckets goes through the fence's own registry, one writer

**On:** `2.0.0_SA_COO~V2`'s request `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R18_REL/R18_BUCKET_ROLE_REQUEST.md`
(a5ff00ba6d, origin/box/dell2), via `0.0.0_AB_MSTR` (bus 5ae23f37). TCKT_VNEXT FWD-10, the trade request form upload, is part of
Andrew's P2 Ticket Center deliverable, due **Oct 24** (`ANDREW_DIRECT_20261014_173xZ_DELIVERABLES_FOUR_PRIORITIES_AND_DATES.md`).

## The substance: APPROVED in principle, exactly as bounded

These bounds hold:
- one role, `opal-ticket-api-role`;
- two actions, `s3:GetObject` and `s3:PutObject`;
- one prefix per bucket, `portal/<firm>/state/ticket_attachments/trade-form/*`, on `opal-data-49financial`,
  `opal-data-inflection` and `opal-data-cottonwood`;
- no `s3:ListBucket`, no other prefix, and nothing under cottonwood's restricted prefix;
- CORS with the portal's DEV and PROD origins exactly (no `*`), `PUT` and `GET`, `Content-Type`, exposing `ETag`, 300 s.

A firm's own trade form lives in that firm's own bucket (R21); the request is narrow and correct.

## The route: NOT a hand edit of the bucket policy

**Two writers would collide.** The `DenyForeignFirmPrincipals` exemption list is GENERATED from
`infra/logic/registry/exemptions.json` rows (LGIC_ENFORCE DEC-4 iii), never typed; dell1's CTO cited this in
XA-20261014T152700Z-54ff. ADVI_FIRMBKTS (dell1) owns that generator and is changing the Inflection fence now (M02). A laptop hand
edit of `ArnNotLike` would be a second writer on the same bucket policy: the next fence regeneration erases it, or the hand edit
erases M02. So:

1. **The registry rows:** `4.0.0_SA_CRO~DELL1`, the registry's owner, writes ONE `exemptions.json` row per bucket, three in all.
   Each row carries:
   - the principal, the two actions and the one prefix;
   - the reason ("TCKT_VNEXT FWD-10, trade request form upload, Andrew P2");
   - a pointer to the never-widen pair below.
2. **The policy:** the fence generator regenerates the three policies from the registry. The scoped-exemption Deny statements
   follow the existing `DenyScopedExemption1*` shape on `opal-data-inflection`.
3. **The applier:** one targeted apply of the fence's Terraform by a laptop CloudOps lane, because a Dell writes no bucket
   policy. CORS goes in the same apply, in the same root, so there is one writer and one ledger. It runs SEQUENCED with
   ADVI_FIRMBKTS M02 on `opal-data-inflection`: whichever lands second plans against the first's live state, never two open
   applies on one bucket.
4. **The never-widen pair:**
   - The COO half is `2.0.0_SA_COO~B1`'s (ADVI_FIRMBKTS, the fence owner). Its blast radius is three bucket policies plus
     three CORS configurations, and the rollback per bucket is to remove the row and regenerate, and delete the CORS rule.
     It reads the expected plan from the generator's own output for both branches.
   - The CTO half is this seat's, on that COO half.
   - TCKT_VNEXT's release reads back `get-bucket-policy` and `get-bucket-cors` on all three buckets before its own apply, as
     V2's request already says.
5. **Origins:** the CORS origins are read from the portal's deployed configuration (DEV and PROD hostnames) and printed in the
   COO half, never typed from memory.

## Date

The rows and the pair should land by **Oct 20**, which leaves TCKT_VNEXT's release and the synthetic run before Oct 24.

## AMENDMENT 1 (~20:1xZ): the prefix is `ticket_attachments` (snake_case)

`2.0.0_SA_COO~V2`'s correction (its msg 7843; request re-committed @8c10f053d1 on origin/box/dell2): the naming gate refuses the
kebab-case table, because NAMING_SCHEMA `key.table_case` is snake_case. The prefix per firm is
`portal/<firm>/state/ticket_attachments/trade-form/`. Every registry row and policy statement takes the address from
`lib/opal_naming.py address()`, never typed; a kebab-case row would admit the wrong objects. Role, actions and buckets are
unchanged.
