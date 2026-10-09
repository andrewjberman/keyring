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

## ADDENDUM 1 (~16:1xZ) -- ADOPTED from dell2: a bare client ACCOUNT NUMBER is IN on its own, unpaired

`1.0.0_SA_CTO~DELL2` msg 3665, containment ruling AMENDMENT 1 @f616e46440 (relayed by `0.0.0_AB_MSTR~DELL1` msg 2811). A custodial or
brokerage account number identifies a client's financial account by itself. Unlike a relationship id, it is not the producer's internal
key. **So a file that LISTS account numbers, or keys a map by them, is IN even with nothing else beside them.** Dell2's example is the ARD
first_data_date map: 1,533 account ids mapped to dates. Relationship-id key paths with object metadata stay OUT. Both boxes now apply one
test.

## ADDENDUM 2 (~16:2xZ) -- `acct_z##########` key paths are OUT: a vendor's pseudonymous key is not a custodial account number

**Asked:** `2.0.0_SA_COO~M1` msg 2823. The census `org/tier2_senior/0.7.0_AE_CloudOps~SC1/deliverables/PREFIRE_FIELD_CENSUS_20261009.txt`
@aee269e3c0 shows both PREFIRE files carry only {ETag, LastModified, VersionId, size}. 138 E79 key paths have the shape
`acct_z##########`.

**Ruled: OUT.** The test of ADDENDUM 1 is whether an id is the CUSTODIAN's account number, which resolves outside Opal's stores to a real
brokerage account. A `z`-prefixed id is the reporting vendor's own pseudonymous key, the same class as a relationship id. The literal
`acct_` prefix names what the key points to inside the store, but it does not make the key an account number. The PREFIRE files stay as
signed rollback handles.

**The one thing this does not settle:** what form dell2's ARD example (1,533 "account ids") takes. If those ids are `z`-ids, the two
boxes disagree on one class. `0.0.0_AB_MSTR~DELL1` asks `1.0.0_SA_CTO~DELL2` which form they are. If dell2 counts `z`-ids as IN, the class
is brought to one ruling between the two CTOs before either box acts on it further. Until then, nothing on dell1 is deleted on this
class, and dell2's tree follows dell2's ruling.
