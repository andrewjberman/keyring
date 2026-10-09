# L8 drain-end packet -- MDPF_SECCLASS round 18 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~12:1xZ)

**For:** 3.0.0_SA_CVO. **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R18.md`.
**Issuance:** @052863d1ec. **Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 18`: `orders=1 judgment=0 verdict=MAY-CLOSE`.

| cell | order | slot | risk | drained | criteria (issuer re-run on the worker's tree) | rows |
|---|---|---|---|---|---|---|
| SC-e-86 | TO-SC-e86 | ~76 | LOCAL | a84384722d | AC1 `PYTEST-OK 99 passed` (BD gold suite); AC2 `PYTEST-OK 28 passed` (COT gold suite); `.tools/` untouched (0 paths in the diff) | none |

**Rows closed by this cell:** D1-S19 (BD) and D1-S24 (COT). Each test now asserts the named-file rule from the tool's own data:
- a thread file plans alone;
- a named `_shared` member rides with its firm's tree to its own bucket;
- the negative arms are kept (no other firm's bucket, and silver ships nothing extra).

Both gold suites read green at HEAD for the first time since 2026-10-08.

## The enrichment items that are reads, not cells (status at the packet)

- **SC-e-84's leg G** is read on the first COT fire after the three-file deploy (`TO-SC-e84b` at `0.7.0_AE_CloudOps~SC1`; ledger
  `secclass-e84-cot-name-port-sc1-20261009` open). It is read under COO conditions 2-3 and CTO conditions 5-6.
- **e79's leg G, then e60's** (e60 ADDENDUM 1), are read at the next BD fire. D1-W66-S3's 32 ticker-no-row securities resolve there or
  are listed. remap-b's leg G reads the same fire.
- **e67's leg G is CLOSED** (@f99a30fa3c) on the 2026-10-09 new-date COT fire.
