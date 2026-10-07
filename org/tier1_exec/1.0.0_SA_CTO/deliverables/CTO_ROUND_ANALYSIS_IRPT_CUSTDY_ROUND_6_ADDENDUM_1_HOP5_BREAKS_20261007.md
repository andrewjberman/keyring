# IRPT_CUSTDY round 6 ADDENDUM 1 -- hop 5 is NOT served; its five breaks ruled across IRPT_CUSTDY and IRPT_BCKEND

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~17:3xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. The CTO of both projects on dell2.

**Input:** `2.0.0_SA_COO~K2` msg 912, and row IRPT_CUSTDY-S14 @0f1041a1d0 (DECOMP_INVALIDATING, GROUNDED at HEAD).

## Correction (round 6 section 1 was wrong)

Round 6 said "the server half of hop 5 is served", because IB-pr-349 carries IB-pr-336, the `CUSTODY_REPORT` kind. That read was
wrong. A deployed function that knows the kind is not a served path: this seat checked that the code had shipped, not that a request
could travel the path. The journey breaks at five points before READY (S14):

| # | break | surface | owner |
|---|---|---|---|
| 1 | no route writes a custody document into the retained store; `ReportRepository.persist` has PERFORMANCE and ANALYSIS callers only | export / reports | IRPT_BCKEND |
| 2 | accept raises `KeyError` on `report.dates.actual_end`, which a custody document does not carry (`submit_async.py:137`) | export | IRPT_BCKEND |
| 3 | the export reads `as_of_date`; hop 3 writes `as_of` | the custody producer | IRPT_CUSTDY |
| 4 | `PrintEntry` refuses `custody-report` by name and does not mount `ClientReportDocument` (`PrintEntry.tsx:102-104`) | portal print page | IRPT_BCKEND (the page), IRPT_CUSTDY (the template, @4c10b488) |
| 5 | the render host prints from the PROD portal (`export/main.tf:95`), so a DEV landing alone never reaches it | portal release | Andrew's word for a PROD promote |

There is also the open-by-design S382: no authenticated Opal principal exists to drive a new export to READY.

## Ruling

1. **IRPT_CUSTDY, now:** `~K2` cuts break 3 as a one-key adapter on its side. The custody document carries `as_of_date` as the export
   contract names it. Its first producer is this project, so the contract's name wins; no consumer is asked to read two names.
2. **IRPT_BCKEND, workstream P (`2.0.0_SA_COO~P2`), as its next items after IB-pr-350:**
   - **P-c1 (break 1):** a custody write path that persists a `CUSTODY_REPORT` document in the retained store under its kind. It
     reuses `ReportRepository.persist`, with no second repository.
   - **P-c2 (break 2):** accept reads the business date by kind: `as_of_date` for a custody report, `dates.actual_end` for the others.
     A test drives `accept` itself; the existing test calls `serve_submit` directly and never reached it.
   - **P-c3 (break 4):** `PrintEntry` admits `custody-report` and mounts `ClientReportDocument` from @4c10b488's tree. An unknown kind
     is still refused by name.

   Each item has at most three criteria and is LOCAL until its own release pair.
3. **Break 5 and the principal are acts outside both lanes:**
   - **Break 5:** promoting the print page to PROD is Andrew's word (portal PROD is gated).
   - **The principal (S382):** the first real Opal export.
4. **E2 waits, and is re-scoped.** E2 is cut only when P-c1 to P-c3 are released and the page is on PROD. Until then round 7 runs E1
   (landed on DEV on Andrew's word) and E3 (the field map, once the Black Diamond report arrives by Taildrop).
5. **`/closer`: NO** (`~K2`'s REC, taken). The breaks are cross-project contract gaps with named owners. Re-driving this project would
   not move them.

-- 1.0.0_SA_CTO~DELL2
