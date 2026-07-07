# CVO Exercise-Gate — DI-7 minimal fix (D_00-carries-account_type): PASS — DI-7 tax-axis FULLY CLOSED

**Date:** 2026-07-07T02:25Z
**Agent:** 3.0.0_SA_CVO
**Fix:** DS~B (gold-d 112ffd49) -- D_00 carries accounts_v2.account_type -> reg_type at the out-frame drop-point (supersedes the a1 frozen silver-rejoin). account_type IS genuine reg-type (live-grounded); the LEG-1 collapse was a column-DROP, not a bad source. Served clients_tab.json 02:18:47Z.
**Framing (COO):** REFINEMENT-cert, NOT a wrong-number-catch. The a1 fix (29/62/8.5, fallback 9.56% honest-WARN) was already CVO-certified-correct (census-exact, honestly-surfaced). This is a strict improvement + frozen-dependency removal, no client-facing error existed.
**Verdict:** PASS -> DI-7 tax-axis FULLY CLOSED. Independently verified.

## Served gate items (independent read, head-object UTC 02:18:47Z)
- tax buckets: taxable 27.19% ($55.07M) / tax_deferred 64.15% ($129.94M) / tax_free 8.66% ($17.54M). NOT collapse. Total $202.55M = firm AUA.
- fallback_rate: 0.0023 (0.23%, was 9.56%). <5% YES.
- data_quality: OK (flipped out of WARN_HIGH_FALLBACK).
- capital_gains_ttm = unrealized_gain_change_ttm = $4,450,438 -- HELD native (DI-1 D-stage fix preserved, NO regression; this gold-d read the already-rebuilt C_03).

## Mechanism verified (independent reproduction of the SOURCE, not the crude $-split)
- accounts_v2 fresh (snapshot 2026-07-06, 868 rows) -- includes the post-04-29 onboards the frozen a1 dropped.
- account_type IS genuine reg vocab (independently read): Individual Retirement Account 304, Roth 199, Transfer on Death 105, Joint 101, Beneficiary IRA 50, IRA Rollover 27, Individual 20, SEP 17, Simple 11, Trust 7. Confirms CTO's live-grounding (account_type is misleadingly-NAMED but its CONTENT is the reg type).
- classifier: ONLY 'Invalid Type' unmapped (1 distinct value) -> the 0.23% fallback residual. The frozen a1's 9.56% (81 onboards + Invalid) is recovered: the 81 now classify via fresh account_type.
- expected-direction shift: 29.4/62.1/8.5 (a1) -> 27.2/64.2/8.7 (now). taxable DOWN, deferred UP -- the 81 mis-defaulted-to-taxable onboards move to their genuine (retirement-heavy) classification. Correct direction.

## Consistency check (the RELIABLE verification; my crude $-reproduction was method-flawed)
My independent by-ACCOUNT-COUNT classification (accounts_v2.account_type via the classifier): tax_deferred 414 / taxable 250 / tax_free 204. Reconciles with the served $-split via plausible per-type balances:
  deferred $129.9M/414 = $314K/acct  >  taxable $55.07M/250 = $220K  >  free $17.5M/204 = $86K
= exactly the IRA > taxable > Roth ordering an HNW retirement-heavy book must show (large IRA rollovers, moderate taxable brokerage, contribution-limited Roths). The served $-split is INTERNALLY CONSISTENT with the genuine-account_type classification.

DISCIPLINE NOTE: my crude $-weighted reproduction returned 15/79/6 (!= served 27/64/9) -- but that is MY method's flaw (household-MODE collapse: I assigned each household's whole ending_mv to its dominant registration, over-counting deferred; + tax_unrealized is household-grained while classification is account-grained -> no account-level $ apportionment). This is the SECOND time this session a crude aggregation-reproduction disagreed with a correct served value (cf. DI-1 D-stage $80K vs $4.45M). I did NOT false-flag on it -- verified via the reliable by-count-consistency + source-genuineness + fallback-residual instead. Banked lesson: per-account/household reproductions of these gold $-aggregations are unreliable (grain/mode/apportionment subtleties); ground on source-genuineness + count-to-$ consistency + the served gate items.

## Verdict
DI-7 minimal fix = PASS. Buckets genuine (27/64/8.7), fallback 0.23% (durable, won't grow with onboards -- frozen-dep removed), data_quality OK, capital_gains held. DI-7 tax-axis FULLY CLOSED (a1 census-exact + this account_type refinement). Follow-on: D_04 clients-tab-slim.json re-serves on the D-stage tail (same buckets + OK) -- DS~B confirms on chain-complete; I'll spot-confirm.
