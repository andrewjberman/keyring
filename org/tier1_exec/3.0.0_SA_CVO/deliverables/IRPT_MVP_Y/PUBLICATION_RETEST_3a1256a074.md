# Y-C02 independent repair retest

Reviewer `3.0.0_SA_CVO~Y`, September 22, 2026.
Authority: `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md` v1.2.
Candidate `3a1256a0742b06c0cbc3fe44388c40b86cb7a3da`.

**Y-C02 CLOSED for the retained-extraction inventory boundary.** Supplied15/15
actual synthetic-PDF tests PASS, exit0. The independent original omission
scenario now refuses with EXTRACTION_INVENTORY_BINDING. The original positive
still emits one scalar, chart and disclosure and returns COMPLETE_FOR_CENSUS.
Original failure evidence at bcfbd380a1 remains unchanged in reviewa6b3ad204b.

The repair independently re-extracts sections, charts, disclosures, unlocated
records, unit conflicts and denominators from the exact source PDF and census,
then compares that inventory with the retained extraction before coverage is
accepted. It records an inventory hash. No current vendor/dependency refresh.

Run `probe_publication.py --pin 3a1256a074 --output PUBLICATION_3a1256a074.json`
with the full review-directory paths from the original review. Probe scenarios,
PDF bytes and mutations are unchanged; only exception reporting was added to
capture the repaired refusal instead of terminating the script. Stdout was
shortened; complete evidence remains in JSON with pinned blob hashes.

| Original independent control | Candidate observation |
|---|---|
| Unmodified synthetic extraction | COMPLETE_FOR_CENSUS; all three content kinds emitted |
| Delete retained charts and disclosures only | EXTRACTION_INVENTORY_BINDING refusal |
| Replace retained disclosure text with absent sentence | EXTRACTION_INVENTORY_BINDING refusal |
| Change source PDF number while retaining extraction | SCALAR_CERTIFICATION_FAILED_OR_EMPTY refusal |

Numeric baseline/candidate control objects are identical to the previous review:
baseline accepted123.3 for0.30%; candidate certifies0.3 and rejects123.3.
Y-C01 closure retained. Full three-variant coverage objects compare equal to
the original evidence: all PARTIAL, emitted23/46/69, undated16/32/48, and
gaps105/118/131 respectively. The fix does not hide those existing source gaps.

This is actual local PDF/extractor/certifier/fragment evidence, using synthetic
fixtures. It does not establish repository publication, READY, full chart
recognition, browser behavior, live vendor output or integrated Y5/S7. All14
integrated criteria remain NOT_EVALUATED. Commit state LOCAL; no implementation
changes or live calls by this reviewer. Refresh-lineage review stays separate.

-- 3.0.0_SA_CVO~Y
