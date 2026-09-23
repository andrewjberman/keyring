# R-P10 strict publication digest validation

Authority: IRPT_MVP_COMPLETION_20260922/CONTRACT.md and CTO's
20260923T003337Z R-P10 assignment. Independent source reproduction is separately
attributed to CVO M `9b1d9abbbc`; packaged reproduction is CVO P `142e5a27a4`.

`HoldingsPublication.validate_reference` now requires `sha256` to be a string
before applying the existing exact 64-character lowercase hexadecimal grammar.
It no longer coerces a number or other object into a digest string. Location,
version, size, whole-inventory validation, selected read bounds, and byte/hash
verification are unchanged. No storage address or packaging change is included.

Twenty new parameterized controls exercise the real guarded Entry through the
versioned publication reader. For each of Gold and an unselected partition they
repin the enclosing manifest and index with correct versions, lengths and hashes,
so the digest field is the changed constraint. The original code reproduces both
64-digit integer failures: 18 PASS / 2 FAIL. Negative controls also cover float,
boolean, null, array, object, short string and uppercase string. Both all-digit
and mixed lowercase hexadecimal strings remain accepted metadata. No unselected
partition or Gold bytes are fetched; invalid metadata refuses before any part GET.
These positive metadata controls do not claim verification of unfetched bytes.

The initial working-tree holdings suite passed 119 tests, including three tests
from the separate uncommitted legacy-read patch. Clean-checkout validation is
recorded below separately; that patch is excluded from this repair commit.

A fresh detached checkout of parent `6ad86009fe5d42d57235095dcda2cffd7b952078`
received only the new test file first: the focused digest matrix reproduced
18 PASS / 2 FAIL. Adding only the `publication.py` repair then passed the entire
holdings suite: **116 PASS**, including all 20 new controls. Commands:

```text
python -m pytest infra/aws/lambda/investor-reporting/holdings/tests/test_publication_entry.py -k inventory_digest_type -q --tb=short
python -m pytest infra/aws/lambda/investor-reporting/holdings/tests -q --tb=short
```

Independent source-boundary review and rebuilt-package review remain required.
The consumer HOLD is retained until its renewed package proof. This repair does
not close economic reconciliation, final-index timeout/versioning ambiguities,
live verification, deployment or full product acceptance. Push state: LOCAL.
