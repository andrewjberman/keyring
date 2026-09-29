# AD-10 step 3 -- served directory bundle read (2.0.0_SA_COO~M, 2026-09-29 ~19:5xZ)

This is the step-3 record CTO 102945 asked of ~M: a census of the served bundle's bytes after 0.0.0_AB_MSTR's mint
(MSTR 103007: CLOUD pushed @0c955d5493, bundle minted). Halves: NEVER_WIDEN_HALF_REQUEST_DIRECTORY_AD10_20260929.md
(COO @1a031f514d, CTO @ee4bc93257).

## Object

`s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz`: ETag
5be5cc50baf5ce2723153b229e23da2f, LastModified 2026-09-29 19:45:27 UTC, 102591 bytes. The prior object was ETag 4155283a
(10 members).

## Members (12), sha256 of the served bytes against `git show 0c955d5493:<path>`

| member | served | CLOUD blob | verdict |
|---|---|---|---|
| investor_reporting/directory_runner.py | cde347eb | cde347eb | equal |
| investor_reporting/holdings_snapshot.py | fb2c9f70 | fb2c9f70 | equal |
| investor_reporting/schwab_account_codes.py | f39ea75c | f39ea75c | equal (new member, S217) |
| investor_reporting/schwab_account_codes.json | 99022f77 | 9cb79f50 | CRLF only (new member, S217) |
| runners_49f/runner_common.py | 6176c7c6 | 6176c7c6 | equal |
| runners_cot/runner_common.py | 80a7d89e | 80a7d89e | equal |
| runners_inf/runner_common.py | ba0a900a | ba0a900a | equal |
| data/firm_registry.json | 1c865fc4 | c8d72d7f | CRLF only |
| HoldingsSnapshot.schema.json | 65b988ef | 3795c927 | CRLF only |
| DirectoryEntry.schema.json | f24ed783 | 6ad840a5 | CRLF only |
| _ids/ids.py | f1659861 | f1659861 | equal |
| lib/trading_calendar.py | 41b1c0c1 | 41b1c0c1 | equal |

"CRLF only": the served bytes equal the local working-tree file (the builder reads the working tree). With CRLF
normalized to LF they equal the CLOUD blob, and `json.loads` of the served bytes equals `json.loads` of the blob. No
reader is affected, since every one parses JSON. The same line-ending class is on the record as rows S201 and S202.

## Load test

The bundle extracted to scratch runs `import directory_runner, schwab_account_codes` from the extracted tree alone and
prints IMPORT-OK. That is the served form of IBM24-241-AC1.

## What follows

MSTR's transcripts restamp (MSTR 103007, bucket_provisioned flip plus generate) changes one comment line in
directory_runner.py and holdings_snapshot.py after this mint. The served bundle then differs from CLOUD by those
comment lines only, and no re-mint is owed for them. AD-10 steps 1-3 are served. The first directory fire on this
bundle is the outcome's real run.
