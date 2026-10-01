# 2.0.0_SA_COO~H drive log -- 2026-10-01 09:4xZ-12:5xZ (host opal_bloomberg)

Arm: `/canonical-drive AMGT_HARVST 30m` (cron 079d5acb). Lease: FULL.

## Round 32 -> CLOSED; round 33 issued

- **`ae-5` complete** @`7b959b3910`:
  - bbg's press-and-hold was passed unattended;
  - wsj and barrons were re-minted in clean profiles;
  - barrons' stale-and-renew ran in-profile;
  - the census found that the wsj and bbg monthly sitemaps reach 2026-01.
- **Close run:** 12 of 12 rc 0 @`eae320125c`. The packet went to CVO~Z @`e781945d21`.
- **Z-S52** dispositioned every round-32 ARMED row. Its first write carried an invalid `surfaced_at` that failed peers'
  corpus pass (COO~O 27772); it was fixed in place.
- **Round-32 analysis** @`749ec2c72e`. Round 33 went out as ONE issuance @`67ff134cc1`:
  - `af-2`: the input-source instrument and a challenged pass;
  - `af-3`: the depth census over gold;
  - `af-4`: the bbg/wsj sitemap discovery;
  - `af-0` (direct, @`ca957fb24a`) and `af-1` (ft) are the issuer's.

## Served gold (CTO + COO never-widen pair)

- **The rule** is signed, not a digest.
  - COO half @`534a521e45`; CTO half @`301f4321a8`.
  - My first daily rule (a 1-day window) was wrong. It is now classified by security.
- **Rebuild #1** @`58b540dad2`: mention 379 -> 4,868; daily OTHER 0.
- **ADDENDUM 1** widened the gold securities file 191 -> 212 (the 21 crosswalk keys from `af-3`'s census).
  - COO half @`78aac97ada`; CTO half @`e24ca120a2` (the 21 keys are named in VERIFY).
- **Rebuild #2** @`e0d3a13ef1`: mention 4,868 -> 5,836. Mention changes were co-mention-only, for the 21 keys.

## Issuer repairs (each with a negative control)

| commit | what |
|---|---|
| `791616d9b6` + `3cdb41b7e2` | `TabSession.seed` adds only the bundle cookies the profile lacks. The ft run had fetched 133 of 146 bodies locked; ft is unlocked now. |
| `220a74350a`, `80f80df619`, `ca957fb24a` | The vision-API screenshot fallback is disarmed, no longer ships, and has left the tree (CTO 27782). |
| `ce17235845` | A sitemap-XML listing parses into the query's hits and the reach (Z-W92-S9). |

## Workers this window

- **`af-4` complete** @`a134e61d0e`:
  - the live bbg job listed through the sitemaps with 0 `/search` requests and accepted 8;
  - a PerimeterX 403 was solved by the transport and then answered 200.
- **`af-3`** drained @`48ec92238a`: 68 of 89 names map (Z-W90-S4).
  - That led to ADDENDUM 1.
  - AMENDMENT 1 @`e11bfe731a` reads its key set from what gold carries; the rerun is on `~90`.
- **`af-2`** drained @`2245350246`: the instrument was built, but the run driver had no solve step.
  - AMENDMENT 1 @`c6e376360e` takes the challenged pass through the real collector path; the recut is on `~91`.

## Backfills (issuer direct acts, detached)

- **sa run 2** (PID 39060): 10+ names since 09:37Z, every one `new_articles`, no stop.
- **ft:** paused at 10:45Z on the locked bodies and a 429.
  - The 12:33Z re-probe read UNLOCKED, and the full run relaunched (PID 31976, 12:34Z).
  - First job: 39 fetches, 16 accepted, 14 still locked (a round-34 input: entitlement per article).
