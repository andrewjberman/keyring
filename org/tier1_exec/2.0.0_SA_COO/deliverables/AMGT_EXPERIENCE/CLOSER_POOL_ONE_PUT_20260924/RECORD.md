# Closer cell (Peers B04/P1 track) -- ONE pool put per run, and the universe input on add_security's path

Seat: 2.0.0_SA_COO~Z. Branch: closer/amgt-peers-z-20260924 (fast-forwarded to CLOUD 85543bf200 before the edit; MSTR~Z drains
it as before). Authority: CTO R-38 (msg 25348 (3)) + R-40 (msg 25357, precondition 4), acceptance = 2.0.0_SA_COO~X's discriminator
(msg 25354) adopted verbatim. Surface: `lib/research/identity/add_security.py` (+ its tests). No served write was made by this
cell; the live acceptance below is READ-ONLY (one S3 list + one get of universe/v1).

## What changed (add_security.py)

1. `--batch <file>`: a JSON list of `{"folder", "bloomberg"}` requests landed in ONE run. Each request still makes its ONE
   reference_data call, lands its raw object and its registrations.json row (the rk-114 in-memory-build-first property kept per
   row); the pool document is built and put ONCE at the end with the complete set (`_mint_pool`, `pool_puts=1` on the OK line,
   `BATCH: requested N landed L bloomberg_calls C pool_puts P` summary). Single-request mode (`--folder`/`--bloomberg`) is unchanged
   in behaviour and also puts once (N=1).
2. The retained universe/v1 identity input is read ONCE per run (`_identity_universe`, `--identity-universe <path>` pins a local
   file, exactly crosswalk.main's shape) and handed to EVERY build on the path: the collision check (the old `:392` bare
   `build_crosswalk(as_of)`) and the pool document (`_persist_registration_and_pool`'s bare build). A run that cannot read it is
   REFUSED (rc 5) before any Bloomberg call.
3. `_pool_client()` hook so a test injects a counting S3 fake; `_persist_registration_and_pool` kept for the pre-batch callers.

## Acceptance

Unit arms (`lib/research/identity/tests/test_add_security_batch.py`, boto3.client patched to RAISE so an uncovered hook fails loud):
- one put for N=1 (`IfNoneMatch: *` on a first mint); ONE put for N=20 with all 20 keys in the ONE document (registered 20,
  MEASURED = coverage 1 + universe 2 + 20); single mode one put; a second identical run mints nothing (0 calls, 0 puts).
- the pool document carries universe + registrations (MEASURED 1+2+1, `universe_registered` 2, `identity_universe.source` the
  fixture); NEGATIVE CONTROL with the universe withheld reads 1+1; a FOLDERED request colliding with a universe-measured key is
  REFUSED rc 4 before any call (the collision check reads the pool's population); an unreadable universe refuses rc 5.
- `--batch` refusals (empty entry, duplicate) and a dry-run batch writes nothing.
Whole identity test directory: **89 passed** (was 76 + 13 new); the two pre-existing modules that call `main()` now pin the universe
(`_universe_pinned`) -- before this cell they silently reached S3 for it after the patch, which is how the network read was found.

Live acceptance on CURRENT inputs (`acceptance_precondition_4.py`, log beside it), the CTO's numbers exactly:
```
universe s3://opal-data-harvest/universe/v1/2026-09-16.json names=250; registrations rows=8
ARM before-any-registration  MEASURED=194 records=254 registered=7 universe_registered=158
ARM after-3-fake-registrations MEASURED=197 records=257 registered=10
NEGATIVE universe-withheld       MEASURED=36 records=96 registered=7
VERDICT PASS
```
The one-version-per-run discriminator at the re-fire (list-object-versions before/after, exactly ONE new version, N>1 names) is
run by 2.0.0_SA_COO~X under its pair; this cell provides the unit arm and the mechanism.

## For the induction (2.0.0_SA_COO~X), two things

1. Call shape: ONE `add_security.main(["--batch", <requests.json>, "--as-of", <today>, "--write-pool"])` for the run, the file a list
   of `{"folder": <folder>, "bloomberg": "<root> <cc>"}` (both, as amendment 2 already requires). Per-name output lines are unchanged
   (MEASURED / UNRESOLVED / RAW LANDED / bloomberg_calls / mode); `OK: uploaded ...` prints ONCE at the end, then the BATCH line.
   Twenty per-name `--write-pool` calls would still put twenty times -- the property is structural only through `--batch`.
2. A semantic question this cell did NOT decide, surfaced for the induction's pre-flight: the collision rule is the module's
   standing one -- a key already MEASURED on a DIFFERENT folder is REFUSED (rc 4), never merged. A universe/v1 record carries NO
   folder, so a corpus request `--folder X --bloomberg "R CC"` whose key the universe already measures is REFUSED under that rule
   (it now sees the 158 universe keys it could not see before). If the induction's population overlaps the universe, those names
   read as collisions; whether a corpus folder should instead ENRICH a universe record (folder association + LEI/CIK) is a design
   call for the induction's owner and the CTO, not a rider on this cell. The negative control for that decision is one dry run of
   the batch with the universe pinned, counting `REFUSED: security_key ... already MEASURED` lines.
