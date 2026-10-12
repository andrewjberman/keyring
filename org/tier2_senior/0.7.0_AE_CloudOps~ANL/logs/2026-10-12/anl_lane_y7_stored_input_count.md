# 56 stored template inputs, none read differently by the new reader -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-12
**Task Order:** IRPT_ANLREQ.TO-READS-Y7.stored-input-count-laptop
**Status:** COMPLETE

---

## Objective

One read-only run of the issuer's counting script from the laptop: how many stored upload inputs the new template reader would read differently from the template stored at acceptance, by cause, and how many of those have a generated report (CTO msg 6304).

## What was done

- Acked crossbox XB-20261012T023834Z-5414. Step 0 passed on the first blob (c5481b8768): self-test exit 0, reader diff empty, no write call in the script.
- Run 1 (step 3): exit 3, `SCAN_FAILED ValidationException`, before any item was read. Nothing edited, no retry; reported through 0.0.0_AB_MSTR. The issuer re-released the script as blob 09ddebd883 (projection through name placeholders) and gave word for one rerun (AMENDMENT 1).
- Run 2: step 0 repeated on 09ddebd883 (diff read, self-test exit 0, reader diff empty). Bucket resolved from the blob.bucket member of the first ARTIFACT# row of a consistent scan. One run, exit 0, 1914 items scanned.
- Result: 56 template inputs (49financial 10, cottonwood 45, inflection 1), 56 read the same, 0 differently, 0 turned back, 0 unreadable.
- Result file `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y7_stored_input_count.json` at 49af906f74; scratch copies of the new reader, the count and the bucket name deleted.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| reads7_check | python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/reads7_check.py | PASS | READS7-OK |
| comp-iam | none | SKIPPED | read-only order; the laptop identity read the table and the bucket without a denial |

**What worked:** the issuer's pre-check list; the stop-and-report rule on the first failure cost one round-trip.
**What failed:** run 1, a reserved word in the script's projection; the offline fake does not validate expressions.
**Gap found:** the script's self-test cannot catch a DynamoDB expression the real service refuses.
