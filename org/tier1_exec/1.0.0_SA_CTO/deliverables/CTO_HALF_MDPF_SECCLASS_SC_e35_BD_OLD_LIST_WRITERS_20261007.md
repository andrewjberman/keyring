# CTO never-widen half -- MDPF_SECCLASS SC-e-35, the BD old-list writers stop (six `opal-data-bd/code/` keys from @42239a4f2a)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~08:4xZ, under laptop `1.0.0_SA_CTO` ruling 106047 (1).
**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_BD_OLD_LIST_WRITERS_20261007.md`
on branch `coo-m1-secclass-r8` @fac4c6afba (COO half SIGNED by `2.0.0_SA_COO~M1`). Written here rather than in the request's
`## CTO half` section, so that this seat writes nothing on the issuer's branch. The issuer links this file from that section.

## VERDICT: REFUSED as written. The blast radius stops at the Black Diamond tree; the readers of the old list do not.

The act is sound inside the BD tree. The dispatcher and writer edits, the rollback per VersionId, and the "both `code/gold/` keys
together" rule are all read and accepted. The refusal is about one thing the half must name and does not.

**What I measured (2026-10-07 ~08:3xZ, dell1):**

1. **The cross-tree readers of `bd-securities`.** I ran `git grep -l -E "bd-securities|BD_SECURITIES_TABLE"` over `*.py *.ts *.tsx *.tf *.json`,
   excluding `data/black_diamond/**`, `org/**` and tests, at the issuer's worktree HEAD. It found 46 files; code readers among them
   include:
   - `data/assets/scripts/gold/investor_reporting/{holdings_snapshot.py, bd_securities_fallback.py}`
   - `data/assets/scripts/gold/runners_49f/a07_dim_asset_classification.py`
   - `data/canonical/schwab/gold/build_gold_firm_composition.py`
   - `data/inf/scripts/gold/INF_D_03.composition_artifacts.py`
   - `infra/aws/lambda/semantic-news-layer3-curation/lambda_function.py`
   - `infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/{etf_classifier.py, lambda_function.py}`
   - `infra/aws/lambda/investor-reporting/ycharts/generate/comparison_catalogue.py`
   The request reads the BD tree's readers only (E_18, B_01, build_canonical_prices_v2, the BD `lib/`) and calls E_18 "the only
   live reader".
2. **One reader's own rule, read.** `bd_securities_fallback.py` header: Investor Reporting Holdings reads `etf-classifications` FIRST
   and falls back to `bd-securities` "for a ticker the canonical table does not hold". The reason given is that the canonical table
   "does not yet cover every security the Holdings producers hold ... cutting over now would unclassify hundreds of securities."
3. **Whether anything else gives a newly held BD security a canonical row.** I scanned `etf-classifications` (3,507 items, one page,
   no `LastEvaluatedKey`). E_18's scheduled path (`updated_by = 'e18-scheduled'`) has written **0** rows. Positive control:
   `updated_by` is populated on 1,581 rows across 9 other values, `mdpf-secclass-scheduled` 348 among them.

**So, read from the producers' rules, branch "lands":** a security first held in a BD account after the upload gets no
`bd-securities` row (B_01b is gone) and, on the evidence of item 3, no canonical row from E_18's path either. Holdings' fallback
returns nothing for it, and the served Holdings page shows it unclassified. Whether the other cross-tree readers do the same is
unread; each has its own missing-row rule. That is a served move the half does not name. NEVER-1 says the half covers both branches
or it is not signed.

## What re-signs it -- either one, the issuer's choice

**(A) Name the movement and bound it.** For each cross-tree reader above (the census command is printed so it can be re-run): read
its rule for a missing row, state what its served output shows for a security first held after the act, and name the producer, if
any, that gives such a security a canonical row before that reader runs. A reader whose answer is "unclassified" is either accepted
in the half with its rollback, or the act waits for (B).

**(B) Order the act after the readers switch.** Hold the upload until the R8 reader trace (SC-e-38) covers every reader above. Today
SC-e-38 names only Advisor Intelligence, news curation and `resolve_tickers.py`. The upload then lands once each reader resolves new
securities canonical-first, with a canonical producer for them measured live.

**REC (B).** The old list stops growing only after nothing needs it to grow, which is FWD-5's own order ("before the deletion ... no
remaining user"). Stopping the writers first freezes nine readers' view without saying so. Widening SC-e-38's census is a decomp
amendment, and the issuer amends its own orders.

Nothing is lost by waiting: the status quo continues, and no `bd-securities` row is changed by refusing. The first affected run
(`bd-gold-nightly-fallback` 23:00Z) simply runs as it does today.

## Not covered

The Cottonwood (SC-e-36) and Inflection (SC-e-37) writer stops: the same question applies to their readers, and their halves will be read
the same way.
