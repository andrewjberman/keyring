# CTO check 8 -- NFRA_CTLPLN package intake, batch intake-20261015-duckdb (one file): SIGNED

**Author:** `1.0.0_SA_CTO`, 2026-10-15 ~19:5xZ. **Record read in full:**
`org/devices/intake/records/intake-20261015-duckdb/duckdb-1.5.0-cp314-cp314-win_amd64.whl.check.json`, merged at 3c3d04d4ec.
**Approval it rests on:** `CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_DUCKDB_20261015.md` @29a69ec1c5. One wheel was fetched, the
cp314 one, matching dell1's tag; the cp312 line was not used.

## What checks 1 to 7 show (read from the record, not the summary)

| check | verdict | what it rules out |
|---|---|---|
| 1 sha256 and size equal the index's published values (`11ae50aa...`, 13,575,130 bytes), re-read from disk | passed | a file altered in transit or served by an impostor |
| 2 the name, version and tags are exactly `duckdb==1.5.0` `cp314-cp314-win_amd64`, on the approved list | passed | a near-name package; a substituted version |
| 3 the same version is installed on the laptop | passed | a brand-new release nobody has used |
| 4 the release is 220 days old, with 145 earlier releases, and not yanked | passed | a package or release published days ago |
| 5 the build attestation is present on the index | passed | a file uploaded by hand from a stolen account |
| 6 41 of 41 `.py` files are byte-identical to the installed copy; 1 compiled file named; no new hook | passed | code added outside the compiled files |
| 7 an enabled, current on-access scanner left the file unchanged after 20 s | passed | a file the scanner removes on sight |

## What they leave, accepted for this one job

- **Check 3** compares against the laptop's cp312 build, not a cp314 build of the same version.
- **Check 6** names the compiled `_duckdb.cp314-win_amd64.pyd` and does not compare it, so code inside it is not ruled out.
- **Check 7** does not show that the antivirus inspected the file; no test-virus control was planted.
- **No check rules out a taken-over maker account,** though check 5's attestation narrows that to a build pipeline compromise.

**Why these are accepted here:**
- the use is one read-only query by one dell1 lane, writing nothing to S3 (approval conditions);
- the attestation ties the file to the project's own build;
- the package is long-lived, with a large release history.

A wider use, such as a pipeline dependency or a second lane, is a new batch and a new check 8.

## Signature

**CHECK 8 SIGNED -- release, pack and taildrop may proceed for this one file.** `1.0.0_SA_CTO`
