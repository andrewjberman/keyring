# Closer remedy -- a registration RESOLVES its folder's UNRESOLVED coverage record (AMGT_CORPUS-Z-S16)

Seat: 2.0.0_SA_COO~Z. Branch: closer/amgt-peers-z-20260924 (fast-forwarded to CLOUD 842071008b before the edit). Routed by
`2.0.0_SA_COO~X`'s row AMGT_CORPUS-Z-S16 (ARMED, disarm owner that seat; disarm condition (1) is this remedy, on this seat's surface)
and adopted by the CTO in R-59 ("the chain is adopted as 2.0.0_SA_COO~X sequenced it: remedy on the builder, then ONE re-mint under
a FRESH pair, then the re-ingest, then d-4"). Surface: `lib/research/identity/crosswalk.py` (+ schema, tests). No served write.

## The defect, measured before the edit (CLOUD bytes, in-memory build through add_security's path, read-only)

```
registrations rows 28 | records 274 MEASURED 214 UNRESOLVED 60 registered 27
multi-claimed forms 20 of 521 ; folders with a double claim 20
  security-5f0ff2697ffe2748 -> [('UNRESOLVED', 'AstraZeneca AZN', <coverage>), ('MEASURED', 'AstraZeneca AZN', registrations.json)]
```
The 11:11Z induction fire landed 20 MEASURED registrations, each carrying its corpus FOLDER; `build_crosswalk` appended each beside
the folder's UNRESOLVED coverage record, so both claimed the folder's `security-<hash>` association form, `crosswalk.resolve()`
read those forms AMBIGUOUS, and the re-ingest resolved 0 of the 20 (COO~X, 11:19Z). C-ONE-IDENTITY: one claimant per form.

## The change (crosswalk.py `build_crosswalk`)

A registration record whose `source_row.folder` matches a coverage record that is UNRESOLVED REPLACES that record IN PLACE (same
position, the folder's form kept, the registration's key forms added, provenance `resolves_coverage_record` naming the coverage row it
resolved). A registration on a MEASURED folder, or with no folder, appends exactly as before; a build with no such registration is
byte-identical (the `resolved_folders` denominator is present only when > 0; schema admits it and its description now reads
`records == input_names + registered - resolved_folders + universe_registered`). add_security is unchanged: the builder decides by folder.

## Acceptance -- COO~X's own, verbatim from the row: UNRESOLVED 60 -> 40, records 274 -> 254, MEASURED 214 unchanged, multi-claimed 20 -> 0

Live, read-only, CURRENT inputs (`acceptance_folder_resolve.py`, log `acceptance_after.log`):
```
registrations rows 28 | records 254 MEASURED 214 UNRESOLVED 40 registered 27
multi-claimed forms 0 of 521 ; folders with a double claim 0
```
Unit arms: `test_crosswalk_resolves_folder.py` (in-place replacement, position kept, one claimant per form, unknown-folder and
no-folder registrations still append, a MEASURED folder is still a collision, an UNRESOLVED registration also takes the folder's one
record, byte-identity without such rows, schema validation) and `test_add_security_batch.py::RegistrationResolvesTheFolderOnAddSecuritysPath`
(through the producer's own --batch path). The ENRICH byte-identity arm in `test_crosswalk_enrich_coverage.py` is re-scoped to the
rows the remedy leaves alone (its pinned module cannot resolve a folder). Identity test directory: 97 of 97 (7 new).

## What follows (not this seat's)

(2) ONE re-mint of `crosswalk/v1/2026-09-24.json` through the unified builder (`add_security --batch` with the 20 already registered
reads already-registered and puts once; or `crosswalk.main --write-pool`) under a FRESH never-widen pair whose before-state is 23
versions at MEASURED 214 -- COO~X's half, the CTO's second half; no Bloomberg call. (3) COO~X's re-ingest (expects resolved_folders
53) and the production sequence; d-4 behind it. Precondition on all of it: `0.0.0_AB_MSTR~Z` drains this branch onto CLOUD.
