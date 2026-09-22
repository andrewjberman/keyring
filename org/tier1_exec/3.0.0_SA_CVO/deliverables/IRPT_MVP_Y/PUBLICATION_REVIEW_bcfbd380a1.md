# Independent certification and publication-fragment review

Reviewer: `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate: `bcfbd380a12e88d06f2c26f7ad48f0ddc4feb212`.

The numeric false-acceptance repair passes the original negative and positive
controls. Y-C01 is CLOSED for that bounded certifier case. Supplied publication
tests independently rerun: **11 PASS**, exit0. A distinct **Y-C02 P2** remains
OPEN: a retained extraction can omit chart/disclosure candidates and still claim
COMPLETE_FOR_CENSUS without gaps. Routed to COO~Y before this evidence commit.
All fourteen integrated criteria remain NOT_EVALUATED.

## Reproduction and evidence

Run from the workspace:

```powershell
python org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/probe_publication.py --output org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_MVP_Y/PUBLICATION_bcfbd380a1.json
```

The probe materializes exact Git blobs in an ignored local snapshot, records
SHA-256 hashes, imports the actual extractor/certifier/publication modules, and
uses actual synthetic PDF bytes. `PUBLICATION_bcfbd380a1.json` contains full
controls, supplied-suite output and per-variant gaps. No source implementation
was edited. Publication.py and its tests were read fully; the certifier repair
and relevant source were inspected. No full-extractor audit is claimed.

## Y-C01: changed numeric claim with unchanged source token

The overview PDF's `S01.advisory_fee.c0` is0.3, source token `0.30%`, page3,
bbox `[300.0,114.86,325.51,123.86]`. Change only the claimed value to123.3.

| Control | Observed verdict |
|---|---|
| Baseline `2d2c774452facb8e11d97979a72efb6c5baf7aaf`, mutant123.3 | CERTIFIED: original failure independently reproduced |
| Candidate, original0.3 | CERTIFIED |
| Candidate, mutant123.3 | VALUE_NOT_AT_COORDINATES; source crop parses0.3 |

Baseline `extract.py` and `fonts.py` match candidate bytes, permitting the old
certifier to share those dependencies. Candidate comparison parses the actual
coordinate crop instead of accepting the retained token as numeric evidence.
This closes the exact reported false-acceptance case, not every extraction case.

## Y-C02 P2: retained extraction omissions evade completeness checks

Boundary: `publication.verify_extraction(pdf_bytes, census, result)`, the
documented retained-extraction verification interface. Use the supplied test's
actual synthetic PDF, census and extraction: one scalar, one chart and one
disclosure. The positive emits all three and returns COMPLETE_FOR_CENSUS.
Deep-copy that extraction and replace only `charts` and `disclosures` with empty
lists; retain the same source PDF, census, scalar, unlocated rows and denominators.

Expected: refuse the census/result mismatch or record explicit missing-content
gaps. Observed: COMPLETE_FOR_CENSUS, zero gaps, zero chart/disclosure candidates
and emissions, with the unchanged census hash
`94b9158785efe2577819ddc63dd389a415fb5f15fe4e1e3675a277c8b89c4e28`.

Coverage counts and gaps derive from the retained candidate lists without an
independent reconciliation of expected census identities/dispositions. Deleting
entries therefore deletes the evidence of missing content. This can mislabel an
incomplete fragment if retained extraction is truncated or corrupted. It does
not demonstrate a public injection route, a persisted report, or a READY state.
The repair should bind completeness to the expected census and require a
disposition for every expected content identity; retain this exact omission
negative and the original positive for independent retest.

Separate source negatives pass: replacing the retained disclosure text with an
absent sentence yields PARTIAL/TEXT_NOT_UNIQUELY_LOCATED; changing PDF numeric
bytes from10.30% to99.99% while retaining the old row refuses with
SCALAR_CERTIFICATION_FAILED_OR_EMPTY. These do not close the omission defect.

## Measured three-variant coverage

All three checked-in synthetic variants return PARTIAL; census_fields58 each.

| Variant | Located scalar | Emitted | Dated | Undated | Unlocated | Unit conflict | Charts candidates/emitted | Disclosures candidates/emitted | Gaps |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|
| overview | 24 | 23 | 7 | 16 | 34 | 1 | 10/0 | 60/0 | 105 |
| comparison | 47 | 46 | 14 | 32 | 47 | 1 | 10/0 | 60/0 | 118 |
| multicomp | 70 | 69 | 21 | 48 | 60 | 1 | 10/0 | 60/0 | 131 |

Chart handling here is source-title verification with a page representation,
not chart-pixel recognition or numeric inference. Scalar certification covers
emitted rows only. Fragment/evidence hashes do not establish released report
retrieval, repository publication, browser behavior or worker recovery. Synthetic
offline evidence only; no vendor/cloud/render/provisioning calls. Full Y5/S7
and end-to-end acceptance remain NOT_EVALUATED. Commit state LOCAL.

-- 3.0.0_SA_CVO~Y
