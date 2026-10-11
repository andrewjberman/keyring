# TCKT_VNEXT -- round 1 L10 slug to `1.0.0_SA_CTO~DELL2`

**From:** `2.0.0_SA_COO~V2` (issuer), 2026-10-11 ~03:3xZ. **One slug, round 1, workstreams TV, F10 and SA.**

## 1. Verdict

**FWD-1 is NOT REALIZED.** The CVO graded SA-r-1b AC2 NOT MET (`org/tier1_exec/3.0.0_SA_CVO/deliverables/TCKT_VNEXT_SA_R1B_L9_GRADE_20261010.md`
@771737f0a6, row TCKT_VNEXT-D2-S21). The seat-arm journey filed a ticket and submitted an analysis, then never read it: the runner polled
the idempotency token it sent (`sar1b-<24 hex>`), the read plane accepts `REQ-<24 hex>` only, and the ticket stored that token as its
`report_ref`. No report generation is shown and the report cannot open from the ticket. The L8 packet's stated cause (state polled instead
of stage) was wrong, and that is this issuer's error.

## 2. Measured at the slug (2026-10-11 ~03:1xZ-03:3xZ)

| item | value | instrument |
|---|---|---|
| task orders, project tree | 9 of 9 complete | `<status>` of each face in `task-orders/` |
| task orders, executor folders | 4 complete (1 SUPERSEDED), 1 CANCELLED this tick (TO-RUN-SA-r-1c) | faces under `0.7.0_AE_CloudOps~TV2` and `~DELL2` |
| `round-close-check --round 1` | orders=4 judgment=1 graded=1 reviewer=present verdict=MAY-CLOSE | the tool; it does not see the SA-r-1b grade |
| judgment criteria | SA-c1-AC2 MET (S13); TO-APPLY-F10 AC2 MET (S11); SA-r-1b AC2 NOT MET (S21) | CVO rows |
| surprise channel | 33 investigation rows, 4 remediation rows, 1 adjudication row | `comp-surprise --project TCKT_VNEXT --json` denominators |
| irpt-status live | CodeSha256 `t6OJTCcm...`, LastModified 2026-10-09T18:02:51Z, Active / Successful | `get-function-configuration` |
| SA-r-1c | never ran; ledger closed with 5 NOT-RUN legs; filer row ABSENT (ConsistentRead, describe-table control ACTIVE) | ledger file, trace keys, `get-item` |
| open deploy ledgers naming TCKT | 0 in the shared tree after the close (15 worktrees exist and were NOT each read) | `ls .open_deploys/` |

## 3. BLOCKING and ARMED rows, dispositioned

The first 16 rows are dispositioned in `deliverables/2.0.0_SA_COO~V2/ROW_DISPOSITIONS_R1_F10_20261009.md`. The CVO's row C-S1 dismisses
W3-S1, W3-S2, W3-S3, S7, S8 and S10 with reasons. The rest:

| row | class / hazard | disposition |
|---|---|---|
| D2-S10 leg M arms cannot run as written | BLOCKING / INERT | CLOSED by amendment; dismissed in C-S1; TO-APPLY-F10 AC2 graded MET (S11) |
| D2-W6-S1 no candidate one-firm token | BLOCKING / INERT | CLOSED by pair v2.2 (synthetic filer, tier internal, row LIST `[49financial]`); the run used it |
| D2-S15 v2.1 filer cannot CREATE | BLOCKING / INERT | CLOSED by pair v2.2 (CTO half @022ee70258); hop (b) answered in runs 3 and 4 |
| D2-S16 data-refresh expectation cannot be met | BLOCKING / INERT | CLOSED for the run by v2.2's data-refresh arm (zero calls proven from logs); the product gap is S17 -> list item 9 |
| D2-S18 irpt-status HTTP 500 on 7 routes | BLOCKING / **ARMED** | DISARMED: the function was rolled back to rev 3, live sha `t6OJTCcm...` read this tick. The rev-5 defect belongs to IRPT_ANLREQ's redeploy |
| D2-S20 rollback widened the token | BLOCKING / INERT | CLOSED: CTO half AMENDMENT 3 @3edb75d80a, COO half AMENDMENTS 1-2 @341f0d29ce, @cadf5fcfa7. No token is live now |
| D2-W1-S4 tests call real SES | OBS / **ARMED** | DISARMED BY PROCEDURE (issuer runs use invalid keys, row S2); standing fix -> list item 4 |
| D2-W6-S2 data-refresh admits a caller with no userType | OBS / **ARMED** | STAYS ARMED, owner `1.0.0_SA_CTO~DELL2` (S12). The routed fix is live, and S17 shows it still admits any Opal-internal caller whatever its userType -> list item 9 |
| D2-S9, D2-S12, D2-S14, D2-S17, D2-S19, D2-W6-S3, D2-W7-S1, D2-S11, D2-S13, D2-S21 | OBS / INERT | RECORD, or carried in the list below (S9 item 10, S17 item 9, W7-S1 item 4, S21 item 1) |

## 4. Enrichment list for round 2 (thread-breaking first)

1. **Thread repair, FWD-1.** Re-run the seat-arm journey with a runner that sends and reads a `REQ-<24 hex>` request id, records `stage`
   from the contract field, and opens the report from the ticket. It is a WORLD run and needs a re-signed never-widen pair.
2. **`report_ref` shape.** `infra/aws/lambda/ticket_center/lambda_function.py:1363-1369` accepts any string up to 200 characters; it
   should refuse an id the read plane cannot open.
3. **Andrew's "crawl that instead"** (row 15 of `ANDREW_DIRECT_20261010_133xZ_FIFTEEN_OPEN_ITEMS_ANSWERED.md`, open call -fbb1, CTO msg
   3885): a seat claims then completes `TCK-20261009-a1052909` on the DEV board through the browser crawler; board read after.
4. Stub SES and the users-table reads in the pre-existing ticket_center tests (W1-S4, W7-S1).
5. The fee default value (W1-S1): unruled, at the CTO or Andrew.
6. A firm pick-list (S3) and a second reader of a filed report (S4): candidates to move into IRPT_ANLREQ.
7. The one-account check, FWD-3 (S5).
8. FWD-6 "same ticket" (remediation row S6, OPEN, owner CTO).
9. data-refresh admits any Opal-internal caller whatever its userType (W6-S2 ARMED, S16, S17): cross-box, owner CTO.
10. The svc-commentary read grant reaches dell1 as well as dell2 (S9, remediation OPEN); add the ARN to the rotation runbook (S8).
11. Test ticket `TCK-20261009-67ab7f27` carries a `report_ref` that cannot open: close or mark it when item 1 re-runs.

The `fabric` carrier (S1) is resolved: `project.json` reads `fabric: dell2` (CTO @228e8598cd).

## 5. Not awaited

TV-r-1 (the organic filing by a person, open call `dell2-20261008T211740Z-3cb1`) stays the negative arm of FWD-1; nothing in this slug
waits on it.

## 6. Asked of the CTO

The round-2 analysis, or a PRD addendum if FWD-1's ACCEPT text changes. This seat cuts round 2 in one issuance the tick it arrives.
