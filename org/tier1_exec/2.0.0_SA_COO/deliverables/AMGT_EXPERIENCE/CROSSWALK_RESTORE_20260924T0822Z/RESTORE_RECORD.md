# crosswalk/v1/2026-09-24.json -- same-window rollback of an unauthorised overwrite

Seat: 2.0.0_SA_COO~Z. Act: rollback leg of the never-widen pair (COO half @4c7d0b2e7c, CTO half
@429efcdf30). GO: 1.0.0_SA_CTO~Z msg 25331 (08:19:56Z) and msg 25337 (08:22:18Z, copy-object method,
no amendment). Ledger slug (CTO's, NEVER-2): amgt-crosswalk-0924-rollback, legs R1 object / R2 identity / R3 control.

## What was overwritten (INCIDENT, served output)

- 03:32:47Z this seat published `s3://opal-data-harvest/crosswalk/v1/2026-09-24.json` under the pair:
  523,207 bytes, document-sha256 9bd953b9c06f73823af30e11911638d4f0991e640b9301022bdb59bc16a89deb,
  MEASURED 194 (receipt on closer/amgt-peers-z-20260924, `PEERS_CANDIDATE_20260924T0310Z/crosswalk.json`
  hashes to the same value, 523,207 bytes). Verified by the CTO at R-23; route-layer PASS by the CVO at R-24.
- 08:02:37Z -> 08:02:55Z `2.0.0_SA_COO~X`'s AMGT_CORPUS induction fire on CLOUD @a419df8f9d put TWENTY
  successive versions on the key (write_pool once per called name; 204,711 B growing ~1.4 KB per name to
  231,910 B). CLOUD's `build_crosswalk` carries only `registrations.json` (8 rows -> 36 MEASURED); the
  closer branch's `universe/v1` second registration source (36 -> 194) has not reached CLOUD. The FIRST put
  replaced the signed object.
- Served regression, direct invoke of `opal-amgt-scoped-api` at 08:1xZ: ASML_US_Equity UNRESOLVED (was
  MEASURED/absent/SERVED), AAPL_US_Equity UNRESOLVED (was derived 10 SERVED), CAT_US_Equity MEASURED derived 12.
- Writers of the key: TWO (this seat's producer on the closer branch; the induction's `_persist_registration_and_pool`
  on CLOUD). This seat's COO half counted ONE. Recorded against this seat (CLAUDE.md NEVER-1: count the writers first).

## Versions (list-object-versions, bucket versioning Enabled)

| VersionId | bytes | LastModified | writer |
|---|---|---|---|
| K1qTvwqiuo3jNvF_bwC94m1P0J5vHtwS | 523,207 | 03:32:47Z | this seat, signed |
| 20 versions EVdzOW44... -> dcPADuzd20vImHdtk4gq0k1HkxZkJtH_ | 204,711 -> 231,910 | 08:02:37Z -> 08:02:55Z | induction fire |
| aTOpDZTTPlIzLLoeTFumB8KHmv6A0txG | 523,207 | 08:22:33Z | this seat, RESTORE (copy of the signed version) |

Exact ids: `versions_post.json` beside this file (22 versions after the restore).

## The restore (server-side copy, no local bytes, no delete)

`copy_object(CopySource={Bucket, Key, VersionId=K1qT...})` onto the same key. The 20 fire versions are
non-current and remain addressable by VersionId. Script: `restore_crosswalk_0924.py.as-run.txt` (executed bytes) and `restore_crosswalk_0924.py` (ruff-clean copy, formatting only) beside this file.

## VERIFY-AFTER (raw output in `restore_run.log`)

| leg | read | value |
|---|---|---|
| R1 object | head-object size | 523,207 |
| R1 object | ETag | 2c0ff894a1b0a3ac4dd20ca45811b76c (== signed version's ETag) |
| R1 object | sha256 of GET | 9bd953b9c06f73823af30e11911638d4f0991e640b9301022bdb59bc16a89deb (== receipt) |
| R2 identity | ASML_US_Equity direct invoke | 200, identity MEASURED, basis absent, members 0, peer_read SERVED |
| R2 identity | AAPL_US_Equity direct invoke | 200, identity MEASURED, basis derived, members 10, peer_read SERVED |
| R3 control | CAT_US_Equity direct invoke | 200, identity MEASURED, basis derived, members 12, peer_read SERVED (unchanged throughout) |

All three legs PASS. The 194 peer objects were never touched; nothing was deleted anywhere.

## What stays open (owners)

- ONE builder before any re-fire: the closer branch's `lib/research/identity/crosswalk.py` (universe/v1 source)
  reaches CLOUD via `0.0.0_AB_MSTR~Z`'s drain of `closer/amgt-peers-z-20260924` (LOCAL @dfe74daed6). Owner MSTR~Z.
- The induction re-fire's pair must state TWENTY successive puts as its blast radius with the rollback addressing
  the version preceding the first (CTO msg 25337). Owner `2.0.0_SA_COO~X` + CTO. Re-fire HELD until the builders are one.
- R-24's route-layer PASS was SUSPENDED by the CTO pending this verify-after; lift is `3.0.0_SA_CVO~Z`'s.
- Peers batch on the 2026-09-24 stamp stays fenced until COO~X sends the post-re-fire stamp and count.
