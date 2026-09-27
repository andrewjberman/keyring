# The certifier's cross-firm name check (CTO 102151), and the comparison grant that goes with it

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~22:1xZ.

## 1. The check: Y @ecc0cb6a29, `P_FOREIGN_FIRM_NAME_CHECK_20260927.patch` (4 files, apply-check rc=0 on P `65957b8afc`)

A report whose firm is not 49financial fails publication (`PublicationRefused FOREIGN_FIRM_NAME_IN_REPORT`) if its
retained vendor PDF's text carries "49F" or "49 Financial".
- It is the cross-firm data rule applied to the product's own output: the Opal comparison models return a 49F-named
  benchmark, and a template change could print it.
- `extract/publication.py`:
  - `FIRM_NAME_MARKERS` holds 49financial's pattern, case-sensitive and not inside a longer token, because our own
    portfolio names carry lowercase hex (`REQ-<hex>`).
  - `foreign_firm_names(pdf_bytes, firm)` returns the other firms whose names appear.
- `generate/publisher.py` runs it before `build_publication`, on the same refusal path as every certification
  failure: no REPORT#, and the job is not READY.

Tests:
- `test_foreign_firm_names` 7/7:
  - "49F", "49 Financial" and "(49F)" are found on cottonwood and inflection reports;
  - a firm's own name is never foreign;
  - lowercase hex ids, "A49F0", "149F", "49Fx" and "49 financial" do not trip it.
- `test_resident_worker`, 2 tests through the real publisher. The test world is 49financial: its own "49F" reads READY,
  and another firm's printed name refuses with no transaction.
- Resident suites 57 passed, 8 skipped. ruff clean.

Real PDFs: window 15's Overview for cottonwood, and the certified research Overview, Comparison and Multi-Comp for
cottonwood and inflection, all give `[]`.

Cost: about 11 s (23 pages) to 16 s (31 pages) of extra pdfplumber reading per publish. Window 15's publication took
about 47 s.

## 2. The comparison grant: Y @991ee7fca9, `P_COMPARISON_CATALOGUE_GRANT_20260927.patch` (apply-check rc=0 on P `65957b8afc`)

P already carries v2 (`4b563c98a0`, identical to Y @c5aa93d60e). The grant step sets, on all 4 entries, per M 102154:
- `entitlement_status GRANTED`;
- `permitted_firm_ids` 49financial, inflection and cottonwood;
- `permitted_principal_classes` FIRM_ADVISOR, FIRM_OPERATIONS and OPAL_GLOBAL.

**Cross-checked with M's own consumer** (`irpt-m-comparison-consumer` @5dede2f029, loaded in-process on Y's file):
- the version matches, and all 4 policy hashes MATCH M's pins;
- cottonwood/OPAL_GLOBAL, inflection/FIRM_ADVISOR and 49financial/FIRM_OPERATIONS are admitted;
- another firm, or a CLIENT principal, is refused "not permitted for this firm or principal".

## One release (P)

M's consumer branch, the grant patch and the check ship in generate AND the resident together (M 102157). The check
moves the served publication path, so it rides that release's ledger and halves (CTO 102151).
