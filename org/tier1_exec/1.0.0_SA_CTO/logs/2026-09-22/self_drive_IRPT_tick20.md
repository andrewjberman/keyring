# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 20 (~01:4xZ 2026-09-22)

| Field | Value |
|---|---|
| Arming record | carrier `c9ccd9f4e3` |
| Cron | `46e545b7` |
| State | **ARMED** |
| Projects | 2, both `active` / EXECUTING |
| Sequence | no flags |
| COO lanes | 2 of 3 live |
| Inbox | 0 unread. Read and acked since tick 19: 99340, 99341, 99347, 99349, 99356, 99360. |

## Driver acts

- **IB-rtj-2 (L4 fence probe) -- CTO half SIGNED @`088669b331`.**
  - Signed against packet blob `e2f521e5`, for role `irpt-fence-probe-l4-role`.
  - I read the live bucket policies (`# rail-checked`: resource policies are out of comp-iam's scope). The role ARN matches 0 of 4 ArnNotLike entries on each fenced bucket.
  - The control bucket carries no Deny.
  - The attribution-control arm is accepted.
- **CRO down -- Andrew mid-turn: "CRO is having 529 timeouts".**
  - `0.0.0_AB_MSTR` peeked the seat (msg 99356): its last 3 turns ended in API 529 Overloaded, and it is retrying.
  - This seat substituted `2.0.0_SA_COO~F` for the second half, under Andrew-direct 2026-09-11 ("If CRO is not online, can do COO in their stead"). The substitution was sent with `send_override` citing Andrew's words (msg 99357).
  - `2.0.0_SA_COO~F` signed after its own read @`580fd0f374`.
  - Both halves are now at HEAD, and `0.7.0_AE_CloudOps~V` may execute.
- **IB-rtj-1 (capture tool second publish) -- CTO half SIGNED @`1b2acac213`.**
  - Signed against packet blob `2450320a`.
  - Exactly one key changes: the cjs file, sha256 `defcb585`, which I verified against the HEAD blob. The sh file is unchanged at `17ae44f0`.
  - I read the diff directly. The redirect chain of the initial `page.goto` is now walked hop by hop.
  - README step 2 copies the files and checks their sha256 before step 3 invokes them.
  - Live S3 still holds the rti-1 version `ea60b932`, which is the rollback target.
  - The COO half is @`5b67db0397`, corrected @`5b82db7a31`. The packet blob is unchanged.
- **rti-6 un-park condition (1):** MET at code level. Its final part is met only when the S3 readback equals `defcb585`. The ask to Andrew waits on that readback.

## State

- **IRPT_BCKEND round 10:**
  - rtj-1 and rtj-4 are drained.
  - rtj-2 is ready to execute.
  - The rtj-1 publish arm is being re-handed by `2.0.0_SA_COO~B`.
- **IRPT_FNTEND round 11:**
  - Wave 1 is drained: FE-s-65 (the instrument), FE-s-66 (fixtures) and FE-s-73 (census).
  - Wave 2 is next.

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

- `.tools/aws s3api get-bucket-policy` (rail-checked), with an fnmatch check against the ArnNotLike entries.
- `.tools/aws s3 cp`, then `git hash-object`.
- `git show | sha256sum`.
- `git diff`.
