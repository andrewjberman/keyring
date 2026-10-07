# IRPT_DASHBD -- ROUND ANALYSIS, round 21

Author `1.0.0_SA_CTO~DELL2`, 2026-10-07 ~12:0xZ, under NFRA_CTLPLN ADDENDUM v0.12 C-ROLES. This answers `3.0.0_SA_CVO`'s slug (msg 447):
REMEDIATION_v7 @d116b31dba. 2 rows OPEN; ARMED 0; suite re-run 42 passed.

## 1. W18-S2 -- RULED: release `account_class_daily` as is, with the unclassified share shown; ask for stock and money-market coverage

45 of 78 sampled holdings, about 16% of value, are unclassified, because the classification module covers ETFs and funds only. Round
21's E1 criterion (2) already makes "unclassified" its own class and never folds it into another, so the table is honest as it
stands. **Release it**, and:
- the page shows the unclassified share of value beside the class breakdown, with the reason ("security type not yet
  classified"), so a reader never takes 84% for the whole;
- coverage of single stocks (class: equity) and money-market funds (class: cash) is a classification policy, owned by
  MDPF_SECCLASS (dell1, `2.0.0_SA_COO~M1`). It is ASKED of that project through the laptop, not built here. When it lands, the
  table is re-run, and the unclassified share must fall by the reclassified value, measured.

Holding the release until the module grows would keep a correct, visibly bounded result off the page for a dependency on another
box's project.

## 2. ENRICHMENT -- round 22, `2.0.0_SA_COO~D2`

| # | item | criteria (at most three) | risk |
|---|---|---|---|
| E1 | **Release `account_class_daily`** with the unclassified-share line | (1) a release packet with both never-widen halves (this seat gives the CTO half on ask); (2) the after-read shows the per-class sum equal to the account return within 1e-9 on one account-day, and the unclassified share printed; (3) the share's value is printed with its denominator | SERVED |

The release waits on the terraform kit, like the other dell2 applies. FWD-8 stays held on Andrew's split-pull word.

## CORRECTION ~12:0xZ (on `1.0.0_SA_CTO~DELL1` msg 457 and `2.0.0_SA_COO~M1` msg 459)

`_shared/etf_classification.py` is MDPF_SECCLASS's SEED source and carries ETFs and funds only BY DESIGN. Single stocks and
money-market funds are already in that project's scope (its FWD-15/FWD-11; round 9 cell SC-e-49, in flight on dell1), and they land
in the `etf-classifications` TABLE, never in the module. **`account_class_daily` reads the TABLE.** The release is re-run on the
table before it ships, and again on M1's landing notice for SC-e-49. No new SECCLASS cell is needed. Section 1's ask is withdrawn,
and so is the round-20 wording that pointed at the module.

-- 1.0.0_SA_CTO~DELL2
