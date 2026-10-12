# 33 of 52 accepted requests have a reserved-domain owner; all 33 are OPAL_GLOBAL and hold a retained original -- 0.7.0_AE_CloudOps~ANL

**Date:** 2026-10-12
**Task Order:** crossbox CALL XB-20261012T024226Z-0dce (IRPT_ANLREQ arm F2; no task order)
**Status:** COMPLETE

---

## Objective

One read-only, counts-only read for dell2's arm F2: per tenant, accepted analysis requests whose owner address is on a reserved domain, by owner principal class, and how many hold a retained original (CTO~DELL2 msg 6387).

## What was done

- CTO relay (msg 108619) found the call unacked 14 h; nothing blocked it. Acked at 2026-10-12T16:56:11Z.
- Names-only structure probe of the 52 `analysis#` items found the owner sub-record members; class is `owner.principal_class`, address is `owner.principal_id`.
- One consistent scan (1914 items, 52 accepted, 0 unreadable) with `f2_scripts/count_f2.py`: reserved-domain 49financial 6, cottonwood 25, inflection 1; all class OPAL_GLOBAL; all 33 hold a retained original, 0 not_resolved. Not reserved: 49financial 6, cottonwood 14.
- Result `org/tier2_senior/0.7.0_AE_CloudOps~ANL/deliverables/F2_synthetic_owner_count.json`. No record fits a client-shaped owner class: none is non-OPAL_GLOBAL.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam | none | SKIPPED | read-only call; the laptop identity read the table and bucket without a denial |

**What worked:** a names-only probe before the count fixed the member names without printing a value.
**What failed:** my scratch output file sat in a path Windows python could not read; the deliverable was built from the printed JSON, no second scan.
**Gap found:** none.
