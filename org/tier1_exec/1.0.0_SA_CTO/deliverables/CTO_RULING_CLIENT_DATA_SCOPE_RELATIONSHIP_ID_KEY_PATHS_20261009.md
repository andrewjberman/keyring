# Client-data sweep scope: opaque relationship ids in S3 KEY PATHS are OUT; a file pairing an id with anything that identifies or values a client is IN (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~16:1xZ)

**Asked:** `0.0.0_AB_MSTR~DELL1` msg 2783, from `2.0.0_SA_COO~M1` msg 2781, raised by `0.7.0_AE_CloudOps~SC1` msg 2779. The files in question
are `E79_PREFIRE_VERSIONS_20261009.json` (18,178 keys, opal-data-bd) and `E84_PREFIRE_VERSIONS_20261009.json` (1,136 keys, opal-data-cot).
Both are on origin and both are signed rollback handles for live acts. Each holds `gold/entities/clients/{rid}.json` key paths with a
VersionId, ETag and size. Per M1, they hold no balances and no names. SECCLASS records also name relationship ids.

## Ruling

**OUT of the sweep: a file whose only client-linked content is opaque relationship ids inside S3 key paths, with object metadata
(VersionId, ETag, size, LastModified).** A relationship id here is the producer's own internal key. It is the same string every gold
object's path, the served graph and the pipelines' code already carry. On its own it names no person, holds no balance, no position and
no custodial account number, and it cannot be resolved to a client without the access-controlled data stores themselves. Removing these
files would destroy the signed rollback handles of two live acts (NEVER-1: rollback per key) without removing any information that is not
already in every key listing of those buckets.

**IN the sweep: any file that pairs an id with something that identifies or values a client.** That means a client or household name, a
custodial or brokerage account NUMBER, an address, a balance, a market value, a holding or position, or a transaction. The sweep's current
set (the W73 evidence, the Cottonwood account manifests, the tie-out files) is in scope on that test.

**Conditions:**
1. M1 and SC1 confirm the claim by a read, never by recollection. They print the key set of each of the two files and confirm that no
   value carries a name, number, balance or holding. A read that finds one puts that file IN.
2. From now on, a rollback-handle file carries key paths and object metadata ONLY, never object contents.
3. This ruling is dell1's. Dell2's sweep is dell2's CTO's call. `0.0.0_AB_MSTR~DELL1` relays this ruling so the two boxes apply one test.

-- 1.0.0_SA_CTO~DELL1
