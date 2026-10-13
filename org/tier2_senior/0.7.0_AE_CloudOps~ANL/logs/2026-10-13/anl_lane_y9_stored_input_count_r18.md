# 56 of 56 stored template inputs read differently under the widened reader, none turned back -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-13
**Task Order:** IRPT_ANLREQ.TO-READS-Y9.stored-input-count-r18-laptop
**Status:** COMPLETE

---

## Objective

One read-only run of the counting script (blob 09ddebd883) with the base reader as old and the widened reader (a665d34dd3, READER_VERSION r18.1) as new: how many stored template inputs the widened reader reads differently, and which it turns back (round 18, row S29).

## What was done

- Acked crossbox a827 (00:15Z). Step 0 (i) and (iii) passed; (ii) failed on the checkout (self-test exit 1: the checkout's reader is already the widened one). Stopped and reported; no AWS call.
- Crossbox 7c76 (AMENDMENT 1, acked 00:27Z) accepted the self-test in a throwaway worktree at 35c3c4bd45 (exit 0, base reader) as step 0 (ii) and gave word for the one live run. Worktree removed.
- Both readers written outside the checkout; sha256 equal the order's values. Bucket resolved from the first ARTIFACT# row's blob.bucket. One run, exit 0, 1928 items scanned.
- Result: 56 template inputs (49financial 10, cottonwood 45, inflection 1); read the same 0; read differently 56, all one cause OTHER:NON_FINDING_DIFFERENCE; turned back 0; with a report 0; unreadable 0; old reader differs 0.
- Result `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/Y9_stored_input_count_r18.json`; scratch deleted. The first check run failed on a 64-hex string in my own extra member; shortened to a prefix, full hash kept in the required member.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| reads9_check | python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r18/reads9_check.py | PASS | READS9-OK |
| comp-iam | none | SKIPPED | read-only order; the identity read the table and bucket without a denial |

**What worked:** stopping at the failed pre-check; the issuer's amendment cleared it in one round-trip.
**What failed:** the order's pre-check (ii) assumed the checkout's reader plays no part in the self-test.
**Gap found:** the script's --self-test should take an --old-reader argument.
