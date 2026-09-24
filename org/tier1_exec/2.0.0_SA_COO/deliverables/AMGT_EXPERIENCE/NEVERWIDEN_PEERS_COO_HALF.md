# COO never-widen half: Peers B04/P1 pool publication (crosswalk re-mint + one batch)

SIGNED by `2.0.0_SA_COO~Z`, 2026-09-24. This is the COO half for ONE act: publishing the exact candidate bytes
in `PEERS_CANDIDATE_20260924T0310Z/` to the pool `s3://opal-data-harvest`. It pairs with the CTO half
(`1.0.0_SA_CTO~Z`, requested with the review handoff citing this file at its commit). No pool write was
performed to produce this half; the candidate was built with `cloud_writes: 0` (manifest.json).

## Artifact bound (by content, with its durable location)

| Item | Exact identity |
|---|---|
| Candidate directory | `PEERS_CANDIDATE_20260924T0310Z/` beside this file (manifest, batch log, crosswalk, Boeing object, OBJECT_INDEX) |
| Crosswalk bytes | sha256 `9bd953b9c06f73823af30e11911638d4f0991e640b9301022bdb59bc16a89deb`, pool key `crosswalk/v1/2026-09-24.json` |
| Peer objects | 194, one per MEASURED crosswalk key, sha256 per object in `OBJECT_INDEX.json`, pool key `peers/v1/<security_key>/2026-09-24T0310Z.json` |
| Input: identity universe | `s3://opal-data-harvest/universe/v1/2026-09-16.json`, sha256 `5d3ba4cd412ad8da...` (manifest `inputs.union.json`) |
| Input: prior crosswalk | `crosswalk/v1/2026-09-22.json`, sha256 `da53b89cce05ea0b...` |
| Input: candidate universe | `amgt/harvest/gold/candidate_universe/date=2026-08-06/candidate_universe.json`, sha256 `934ba4783731f431...` (1,000,578 bytes) |
| Input: prior pool keys | the 191 keys of partition `2026-09-17T0240Z` |
| Producer source | branch `closer/amgt-peers-z-20260924`, the commit this file lands in |

The 194 object bytes exist in this device's scratchpad only until the act; per CONTRACT 5a the pool key IS the
durable location, so the upload is the custody. Different bytes (a rebuilt candidate) need a renewed half:
`prepare_peers_candidate.py` refuses if the retained universe/v1 has moved.

## What the act touches, both branches

**Writers of the named properties, counted.** `crosswalk/v1/*`: three writers (`crosswalk.main --write-pool`,
`add_security.py`, `build_universe.py union_main`), all through `crosswalk.write_pool`, which puts a NEW key with
`IfNoneMatch: *` and refuses an overwrite. `peers/v1/*`: one writer, `engine.run_batch --write-pool`, which puts
a NEW stamp and reads back. The route (`scoped_amgt.py`) reads the LATEST key of each prefix by key sort.

**Adds 1 + 194 keys. Overwrites nothing. Deletes nothing.** Every prior partition stays in place.

**What changes at the served route, measured on the candidate:**
- 33 keys already resolvable today get a NEW latest object from the same producer at the same universe vintage
  (2026-08-06), now carrying `price`, `ev`, `ey` on each member (Boeing: 12 members, 5 of 5 present columns at n=12).
- 158 keys UNRESOLVED at the route today become resolvable (111 of them carry a derived set; the rest an explicit
  absent arm with its reason, e.g. `ASML_US_Equity` "no classification").
- 3 crosswalk names with no object today (`6861_JP_Equity`, `CAT_US_Equity`, `CSL_AU_Equity`) gain one
  (derived 4, 12, 12).
- 60 coverage rows UNRESOLVED in the crosswalk stay UNRESOLVED; 59 universe rows without a measured key are
  refused with reasons (crosswalk `identity_universe.refusals`). No key is guessed.
- Denominators: crosswalk MEASURED 194 = batch keys 194 (EQUAL); prior keys 191 of 191 MEASURED; derived 145 +
  absent 49 = 194; SHARED-DEFECT ADMIT, 0 violations.

**Partial failure branch.** The batch prints `UPLOADED n of 194` with per-object read-back. A partial upload
leaves the new stamp present for the written keys and absent for the rest; the route serves each key's own
latest, so a partial batch is INCONSISTENT ACROSS KEYS, not broken per key. Remedy: finish forward with the same
candidate bytes (re-running puts identical objects; the crosswalk write is idempotent on `document-sha256`).

**Rollback per key, additive.** Publish the prior crosswalk content under a later date and the prior peer
objects under a later stamp; the route's latest-by-sort then serves the old bytes again. An S3 delete of the
`2026-09-24*` keys is the other rollback and needs Andrew's word (unrecoverable class); this half does not
pre-authorise it.

**Propagation, disclosed.** `crosswalk.load_crosswalk` memoises the pool object per process; a warm Lambda
container keeps answering from `2026-09-22.json` until it recycles. The identity block's `source` field names
which object answered, so a stale read is visible, not silent.

## Scope and what this half does NOT lift

No function deploy (deployed `opal-amgt-scoped-api` CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`
is untouched), no portal deploy, no vendor or Bloomberg call, no scanner-universe refresh (asOf stays
2026-08-06), no schedule, no delete, no IAM or routing change, no shared-branch push. Live acceptance (E0, P1) is
not claimed here: it is graded by `3.0.0_SA_CVO~Z` on the served stack after the act. This half expires on
completion of the named act.
