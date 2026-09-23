# Repository replacement retest

Reviewer: `3.0.0_SA_CVO~P`; 2026-09-22T21:34:46.848824Z.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.
Candidate LOCAL `0754b10b6c6407da82021f8e475382634804870d`.
Original review/evidence `b333db1b48` against `70598ece96` remains unchanged.

**R-P05 is CLOSED at this replacement pin for the bounded offline primitive.**
The original exact copied-index alias control now refuses the mismatched report
ID. Actual source uses a shared deterministic identity calculation on publication
and retrieval; get also requires the record schema version and immutable flag.
History checks key/ref consistency and reads the exact accepted bytes before
returning a receipt. This is not full S4 or E2E acceptance.

| Evidence | Result |
|---|---|
| Replacement supplied actual-module suite | 23/23 PASS, including get/history alias and corrupt-receipt retry/history/get controls |
| Original reviewer controls replayed without changing their assertions | 5/5 PASS; exact subset/revocation, order/idempotency, report alias, artifact alias, prepublication revocation |
| Additional artifact Decimal boundary control | PASS for put, identical retry, get and head; raw Table byte_length is Decimal; all returned receipt byte lengths are int and JSON-safe; identical bytes/receipt, one row and one blob |

Source SHA256:
`805805dd922e9cd77a9873c4c77aa1f8a857469b2d9440ebed6fd64ec55ed2ba`.
Full candidate module/tests/schema hashes and raw unittest output are retained
in `repository_retest_0754.json`. Reproduce with:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_P/repository_retest_0754.py
```

The runner imports the original reviewer harness, changes only its explicit
candidate pin and output destination, and extracts exact Git source into a
temporary snapshot. Original failure JSON is not overwritten. It then verifies
the actual boto3 serialization/deserialization boundary with the replacement
module and synthetic Table/S3. No live AWS service is contacted.

Y's independent Y-P01 evidence is `b0f8f915f6`; the additional Decimal check here
corroborates the correction, but Y retains its own original-control retest and
closure verdict. Fractional index-count rejection passes the supplied test;
no additional exhaustive numeric-domain claim is made. Financial report values
remain in immutable blob bytes; index conversion handles integral metadata.

## Remaining scope and inherited prerequisites

B-P01 through B-P04 remain open pending their actual entry/browser/export pins.
Full P1-P8 and S1-S7 remain NOT_EVALUATED: production M auth/naming composition,
released Y lineage, custody/vendor data, build/IAM, browser/cache/reload, frozen
exports and protected download require their own assembled evidence. No totals
here combine prior-pin, peer, frontend or deployed tests. Implementer gate2/2
is not independently rerun as a product verdict.

B inherited AC5 FAIL/render NOT PROVEN at `f82fee6aad`, W19-S1 ARMED/CTO and
the existing provisioning/old-flow holds remain. F code baseline `8e6e2e38`
and released claims are recorded, without a new frontend verdict.
S7 ruling `bcd38bba00` remains conditional: canonical record and enforcement,
exact three firms/eleven families with the specified platinum/state split,
concrete retention/expiry and least-privilege IAM/IaC before provisioning or
live writes. CVO~M's review-condition pointer `4446681fc7` is peer evidence,
not permission or a new product grade.

Bare comp-which preceded inspection (weak route); comp-read showed reviewer
harness structure. Git diff compared only the candidate module and tests;
Git show supplied the immutable execution snapshot. No implementation edits,
vendor/cloud writes, deploy or push. Review commit receipt is sent separately.
