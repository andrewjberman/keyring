# Release 1 reads 3 and 4 hold on irpt-status revision 6; /original writes nothing -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-11
**Task Order:** IRPT_ANLREQ.TO-AR-y-34
**Status:** COMPLETE

**archetype:** VALIDATE

---

## Objective

Re-run release 1's reads 3 and 4 on the running irpt-status revision (6), by the method of the 2026-10-09 run, and measure
once that the original-file route writes nothing (object versions before and after). Read-only; the laptop principal is the
one that can decrypt irpt-requests.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam / comp-blast / comp-routes / comp-cache / comp-schedule | -- | SKIPPED | the order declares each not applicable or run by reading: read-only, no resource changed |
| proof-of-spec-check | `python .tools/proof-of-spec-check.py <instance> AR34-y-AC1` | see Verification | run after the commit |
| ar3_checks.py | `python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y34-reads` | PASS | printed `Y34-READS-OK` |

**What worked:** reading the 2026-10-09 scripts from the earlier session's scratchpad kept the method identical. The artifact
index row (`ARTIFACT#<id>` in irpt-requests) carries the exact bucket, key and VersionId, so the counted scope came from the
stored rows, not a typed address.
**What failed:** nothing in the reads. My first run died on my own assertion (the word "HTTP" in the method string trips the no-URL
rule) AFTER every read had passed and BEFORE the result file was written; I reworded the string and ran the script again. Both
runs printed the same outcomes (versions 3 -> 3, all reads true); only the second wrote the file.
**Gap found:** none.

---

## Verification

| Step | Result |
|---|---|
| 0 CodeSha256 | `6idtFvAmYk73wJdr5DPRIyEPrLeWgzjlqbdNr5f1wxc=`, LastModified 2026-10-11T04:44:47Z, equals the order's digest |
| 3a | signed link answered; fetched bytes hashed in memory equal the response sha256 and the retained original's `bc9bdfb7...`; link discarded; expiry recorded only |
| 3b | other-firm admin refused on both arms (no selection NOT_AUTHORIZED; selects 49financial FIRM_BINDING); nothing signed |
| 3c | null: 9 of 9 tenant compositions carry browser.input_id, 0 custody lane, 0 unreadable |
| 4_record | route composition.ticket_id equals the stored record's ticket_id; `data` validates against OwnedAnalysisRequest (0 errors, refs resolved from every v1 schema by $id) |
| 4_route | 5 APIs, 133 routes scanned (denominator), `/original` declared 1 time |
| write-nothing | 3 versions before, 3 after, on three artifact directories (1 key each, 1 page each) |

Scope of the version count: the three artifact directories the `original()` code reads for this request in `opal-data-irpt`
(request_compositions, normalized_portfolios, original_holdings, each under `irpt/49financial/state/`). The retained original
is one of the three keys; the other two are what the route reads on the way. A tenant-wide prefix was not counted because other
requests write there and would move the count for reasons unrelated to this route. DynamoDB tables were not counted. The route's
read memo refuses `put_item`/`update_item`/`delete_item` (`read_memo.py`), which is code evidence only; the version counts are
the measurement.

Not measured: read 5 (owed by release 4's order).

---

## Decisions Made

| Decision | Rationale |
|---|---|
| Counted per-artifact directories, not the firm prefix | a firm-wide count moves with unrelated writers; a changed count there would not be evidence against this route |
| Reran the script after the assertion failure | the failed run wrote nothing and every read had passed; the fault was my method text, not a read |

---

## Files Modified

| File | Change |
|---|---|
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y1_reads_3_4_rev6_result.json` | the result (new) |
| `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/IRPT_ANLREQ.TO-AR-y-34.release1-reads-3-4-on-revision-6.proof_of_spec.json` | the proof instance (new) |
| this log | new |

NO AWS resource, policy, object, table row or Lambda was created, modified or deleted. The order's `<status>` flip is the issuer's.

---

## Blockers

None.

---

## Current State

Lane `0.7.0_AE_CloudOps~ANL` is live with one inbox watcher armed and zero crons. Order IRPT_ANLREQ.TO-AR-y-34 is measured; its
check line reads `Y34-READS-OK`. Commit and push state are in the report to `2.0.0_SA_COO~Y2`.

---

## Next Steps

1. `[2.0.0_SA_COO~Y2]` Flip `<status>` on TO-AR-y-34 and close the sending half of crossbox XB-20261011T071438Z-764b.
2. `[0.0.0_AB_MSTR]` Carry the box/laptop commit to CLOUD at the next box-sync; this seat does not push.
