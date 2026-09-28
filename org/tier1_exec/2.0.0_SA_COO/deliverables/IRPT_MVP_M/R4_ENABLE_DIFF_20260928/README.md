# R4 enable -- the pinned diff re-run on 2026-09-28 with the code now on CLOUD (dfb62b349d, local)

2.0.0_SA_COO~M, 2026-09-28 ~14:0xZ.

## What changed since the first read (R4_ENABLE_DIFF_20260926)

The Holdings code now carries:
- the Holdings cash-line rule (`classify_security` on `display.description`, d306d972f6);
- UIC-16, the account type in full (a57537bd8a).
The COT gold half of the cash-line act is HELD (CTO 102293/102323).

## Method

The same two tools, both read-only:
1. `account_mask_publication_diff.py dry --pin-served`: rebuilds each firm at its served business date, 2026-09-22,
   with the served source partitions pinned.
2. `holdings_publication_diff_classes.py`.

INF uses its retained Eclipse capture: IRPT_INF_ECLIPSE_MEMBERSHIP_SNAPSHOT is the CRO's membership_map.json, sha256
789dd95d.., the same file the served INF build used.

## Result (per-firm JSON beside this file)

| Firm | Served revision | ACCOUNT label | Other display (name facts) | Classification |
|---|---|---|---|---|
| 49financial | 9ab377cef9 | 2,970 | 67 | 123 |
| inflection | ba9001d5ba | 875 | 30,881 | 30,881 |
| cottonwood | fc199c8ed6 | 755 | 0 | 2,577 |

- Node set, amounts, percentages and clocks: **0 changes at every firm**, as in the first read.
- The label counts rose over the first read (INF 562 to 875, COT 595 to 755): UIC-16's full account type now changes
  labels whose type was cut at 24 characters or uppercased.
- COT's classification count (2,577) includes the Holdings cash-line rule on BD's own `CASH -- CASH` rows.

## Remaining for the enable half, after the reboot

The package re-mint, one QA fire, and this diff read again at the QA fire's as_of, all on CLOUD's rewritten commits
(CTO 102323/102342).
