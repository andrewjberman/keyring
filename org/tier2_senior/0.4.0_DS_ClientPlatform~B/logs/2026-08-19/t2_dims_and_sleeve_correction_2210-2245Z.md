# T2-DIMS built + the supervision-sleeve correction to shipped T1 work (2210-2245Z)

**archetype:** IMPLEMENT
**secondary_archetypes:** DIAGNOSE, VALIDATE

**Serial:** `0.4.0_DS_ClientPlatform~B` | **Window:** 2210Z -> 2245Z (follows `t1_oracle_build_2115-2210Z.md`)
**Commits:** `8d746d7703` (T2 producer + both deliverables + T1 correction), `c4ae528480` (vintage stamp). Unpushed.

---

## Summary

WP-1 landed @`b885d682f8`, discharging the T2-DIMS gate, so I started it rather than holding. Two
findings dominated the window and neither was the work I set out to do.

**FIRST: the handoff carried a false claim I had to verify before building on it.** DS base's WP-1
message said the silver table includes "Primary Portfolio Group handling". Measured against all 92
vendor columns: **0 contain "primary"**, positive control **"portfolio" = 8**, so the matcher
discriminates and the absence is real. Template 390224 does not select BD dim 436. DS base
independently re-derived 0/2/8 and retracted, naming the mechanism themselves: Rule 17 guarantees
nothing is LOST; it cannot guarantee something was ever SENT. Preservation is not provision.

**SECOND: my two tools disagreed, and the disagreement was right.** The T2 producer and the
already-delivered T1 oracle differed on 14 of 201 group books. The cause was a real vendor grain I
had missed -- `Account Supervised` splits an account into Supervised/Unsupervised sleeves, each with
its own market value -- and **both** tools were keeping one sleeve.

## What was built

`data/assets/scripts/gold/runners_49f/bd49f_dim_portfolio_group.py` (T2-DIMS absorbing WP-2 -- one
producer, one home). Reads the RATIFIED upstream: I ran WP-1's own converter locally
(`--dry-run --local-xlsx`) to materialize `fact_bd_allocation` rather than re-parse bronze into a
second source. Emits `dim_portfolio_group` (GROUP grain, 201) + `bridge_group_account` (MEMBERSHIP
grain, 29,907) + manifest, basis stamped on both.

## Acceptance

T2-1 PASS-as-built, **mint withheld** (WP-1's silver is unminted; `--upload` refuses with its reason).
T2-2 **PASS** -- 29,907/29,907, 0 missing, 0 extra, 100.0000%.
T2-3 **RECORDED FAIL**, deliberately not PASS-with-caveat -- the structural half is delivered (the
bridge carries NO money column; the guard fires at a 5.32x phantom) but the partition half is
undeliverable without dim 436. A PASS there is exactly the wrong-grain claim CTO is gating against.
T2-4 PASS on 4 probes. T2-5 VALID rc=0.

`group_class` MECE per Rule 24 (intent / grain / exclusivity / exhaustiveness all stated):
advisor-book 186, local-ops-view 9, division 5, firm-wide 1.

## The sleeve correction (to already-delivered work)

SUM proven, not assumed: for every sleeve `account_market_value / account_allocation ==
portfolio_group_market_value` **to the cent** -- both sleeves divide the same portfolio total --
positive-controlled against an ordinary single-sleeve account. The corrected key
`(group, account, supervised)` has constant MV on **29,926 of 29,926 keys, zero exceptions**.

**3 accounts, 19 keys, 12 of 201 groups, $24,605,360.68 understated.** Fixed in both tools.
**Travis is not among the 12** -- his $392,556,451.10 and the entire T1 headline stand. That was luck,
not design, and I said so in the report rather than presenting it as a clean result.

Post-fix the two producers **converge across all 201 groups** (max |delta| $0.005, total $0.18 --
the oracle's `round(x,2)` on values ending .725/.755, not a computation difference).

## What I would carry forward

1. **Cross-implementation disagreement caught it, and only because the legs do not share a
   derivation** (bronze xlsx / positional / float vs silver parquet / named / decimal128). Two tools
   sharing a derivation would have agreed on the wrong number.
2. **A mutant result is a statement about the code AT A VINTAGE.** T1's MUTANT 2 "did not fire"
   (0 of 201) was true when reported; after the sleeve fix it fires on **79 of 201**, |delta|
   $206,733,899.92. Change what is aggregated and every control over that aggregation must be
   re-run. The docstring has now been corrected twice on this exact point.
3. **DS base's Rule 17 discipline is what made the sleeve findable.** A silver layer that had slimmed
   to "the fields the bridge needs" would have destroyed the distinction upstream of anyone who could
   notice, and my two tools would have agreed on the wrong number.

## Compiler Tools

| Tool | Invocation | Result |
|---|---|---|
| `comp-find --name` | `"*bd_allocation*"` | PASS -- 1 hit / 27,010 files; with the WP-1 commit file list, located the converter so T2 reads its REAL upstream |
| `comp-find` (content) | importer probes | PASS -- supplied the T2-4 no-consumer denominators |
| WP-1 converter (as an instrument) | `--dry-run --local-xlsx` | PASS -- 30,577 in / 30,577 out, 92+4 cols; materialized the ratified silver shape locally |
| `.tools/commit-gate.sh` | both scripts | BLOCKED then PASS -- caught a real unused-import (ruff), fixed at source, then clean on 2 files |
| `.tools/proof-of-spec-check.py` | T2 + re-run T1 | PASS -- T2 5/5 VALID rc=0; T1 re-validated rc=0 after amendment |

**What worked:** running WP-1's converter as an instrument instead of re-implementing its parse --
that is what made the two tools genuinely independent while still sharing one ratified upstream.
**What failed:** nothing tool-side. **Gap found:** `comp-pipescript` does not model the data/assets
49F tree at all (DS base hit the same wall; control: the shipping `bd49f_dim_conversion.py` is
equally unknown to it), so the DS `comp-pipescript io` minimum is unsatisfiable on this tree.

## Blockers

**None.** Two items are vendor-side residuals, not blocks: dim 436 (T2-3's partition half) and the
qt6 re-run (T1's L1 leg). Both are bd/49f egress held by `4.0.0_SA_CRO~A`'s continuing grant.

## Current State

- `bd49f_dim_portfolio_group.py` @`8d746d7703`; `oracle_book_tieout_qt6.py` corrected at the same commit.
- Neither table minted to S3. `--upload` refuses. `platinum/advi/49financial/` still 0 keys.
- Deliverables + proof instances for T1 and T2 all committed, both VALID rc=0.
- Reported to COO, to DS base (grain amendment), and to CTO (precondition met + the correction).

## Next Steps

1. [`4.0.0_SA_CRO~A`] ONE grant, TWO acts now: the qt6 group-grain re-run (T1's L1 leg) **and** dim
   436 added to template 390224 + re-pull (T2-3's partition half, which also improves the daily feed
   permanently).
2. [`2.0.0_SA_COO`] Gold mint sequencing once WP-1 mints; and the AE publisher invocation-contract call.
3. [`0.4.0_DS_ClientPlatform`] WP-1 grain-statement amendment (+ the supervision term) -- it explains
   their measured-but-unexplained -24 rows.
4. [`0.4.0_DS_ClientPlatform~B`] On dim 436 landing: re-run the producer; `is_primary` populates and
   T2-3's partition half closes with no further build.
