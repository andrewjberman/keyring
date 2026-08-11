# GIPS-TWR FEASIBILITY -- atom_decomp of the Schwab fact tables against the GIPS TWR Reconstruction Standard

**Author:** 4.0.0_SA_CRO · **2026-08-11, 0630-0645Z** · **archetype:** TRACE + VALIDATE
**Commission (ANDREW-DIRECT at the CRO terminal, verbatim):** *"I asked GPT for a GIPS-based
standard for TWR calculation from Schwab's raw data, I need to assess if we can do it to GIPS
standard. Here is the doc, run another atom_decomp on the schwab fact tables and let's assess if we
can pull this off: C:\\Users\\AndrewBerman\\Desktop\\GIPS_TWR_Reconstruction_Standard.rtf"*
**The spec IS his document** (converted to text, requirements taken from it verbatim -- never from
generic GIPS knowledge; the doc's provision citations carried through). Extends instruction-5's
TWR-from-Schwab-components grant with the quality bar attached.
**Run record (schema-VALID):** `workflows/atom_decomposition/runs/gips-twr-schwab-feasibility/20260811T0635Z/`
-- 15 entities (the standard's own discovery checklist + hard-stop sweep + FX boundary) x 6 fields;
census 85 MEASURED / 3 INFERRED / 1 UNMEASURED / 1 NOT_MEASURABLE. Read-only; DRY, UNCERTIFIED
(CVO certifies). **No account values, names, or tax identifiers left scratchpad.**

<a name="domain-bar"></a>**Domain bar:** expected variance = field-population differences between a
one-day content sample and the 525-partition series. FINDING class = a standard requirement with no
satisfying surface, or a hard-stop condition that fires on measured state. Day-sample cells say so.

---

## THE VERDICT: YES -- GIPS-ALIGNED **DAILY TWR** IS ACHIEVABLE FROM THE SCHWAB FACT TABLES

The standard's own final decision rule asks exactly two questions, and both measure YES:

1. **A complete dated fair-value series?** YES -- `dim_balance` is an authoritative PER-ACCOUNT
   DAILY total (`net_mv_plus_cash`, 7,239/7,239 populated on the sampled partition) with the full
   decomposition the standard's sec3 wants beneath it (positions long/short, settled cash, margin,
   money-market, sweep, bank cash) -- **525 daily partitions, 2024-07-08 through 2026-08-07 (T-1),
   no reconstruction needed: this is the "preferred input" branch of sec3.**
2. **A complete, classifiable external-flow ledger at the same boundary?** YES -- `fact_trn`
   (140 cols) carries 100%-populated trade/settle/tran dates, signed amounts + debit_credit, a
   THREE-AXIS code system (tr_cd x sb_cd x tran_srcde, 21 source codes / 11 code pairs on the
   sampled day) with vendor descriptions, **and Schwab's own `transaction_category` already maps
   near-1:1 onto the standard's external/internal split** ('Deposits and Withdrawals' 307 /
   'Electronic Transfers' 54 / 'Security Transfers' 24 = external classes; 'Trades' 1,401 /
   'Dividends and Interest' 115 = internal). Same `account_id` boundary as the valuation series.

**Method tier per the standard's sec5 hierarchy: DAILY TWR** (complete daily valuations + complete
daily-dated flows) -- one tier above the GIPS monthly minimum; Modified Dietz is not needed. True
exact-flow TWR coincides with daily at this granularity (valuations are EOD; no intraday marks
exist), so one documented flow-timing convention (sec6) is chosen at build, not discovered.
Canonical decision 1 (use a source-computed return) is UNAVAILABLE BY MEASUREMENT -- no
computed-returns table exists across all 20 silver tables (~A's RECON-2 enumeration) -- which is
precisely the branch where the standard prescribes decision 2, and decision 2 is what the estate
supports. **Consistent with, and now quality-barred by, Andrew's instruction-5 grant.**

## HARD-STOP SWEEP: NONE FIRE. ONE CONDITIONAL.

All eight hard-stop conditions swept against measured state (rectangle entity HS): denominators
exist daily; the ledger is complete on dates/amounts/direction; aggregates include cash, shorts,
margin; cost basis is nowhere proposed as value (the attribution family is validation-only, per
canonical decision 4); flow dates 100%; the boundary is distinguishable at account grain.
**The single conditional: 55 empty-category + 5 OTHER rows on the sampled day are unresolved
transaction classes -- a hard stop ONLY if their effect is material. Measuring that materiality is
build task #1**, and the code universe is small (21 source codes) and enumerable.

## THE FIVE REFINEMENT CELLS (named, none blocking feasibility)

| # | Refinement | Size/shape | Grounding |
|---|---|---|---|
| 1 | **Transaction-code classification table** (incl. mgmt-fee code identification) over the 21-code universe; classify-or-count the empty/OTHER residue; materiality gate | small, bounded; THE first build task | fact_trn day sample |
| 2 | **Parse `fact_fam`** -- it IS the account->family/grouping map (content-shape decoded: 7,186 rows ~one per account; col_4 = 8-digit account, col_1 = 19 grouping ids, col_5 = names) sitting as an unparsed positional passthrough. Account-grain TWR needs only fact_acc; HOUSEHOLD-grain composites wait on this parse | small schema-application build | fact_fam content-shape read |
| 3 | **Transfer both-sides linkage**: `swb_from/to_account` columns exist but are SPARSE (3 and 2 non-empty of 1,961; 1 of 385 transfer-class rows) -- derivation = swb where present, else cross-account pair-matching on (date, cusip, qty, +/-amount); ~24 security-transfer rows/day | small matching problem; multi-day swb-population scan = one at-rest read | empty-string-corrected counts |
| 4 | **Accrued income for the 112 rate-bearing assets**: position-level `a_i` is 0/95,879 populated and txn `accrued_interest` zero-on-day -- the vendor ships the DERIVATION INPUTS (fact_sec: interest_rate, 1st_cpn_date, dividend_interest_frequency, next_pay_date) but not the accrual. Materiality-gated: one weighted-position read decides derive-vs-documented-exclusion | 112 of 2,313 assets | fact_rps/fact_sec/fact_trn reads |
| 5 | **Reversal-mechanism specimen**: linkage columns (r_dc/r_cc/r_cy, tranproc_date, cycle_id) exist with ZERO specimens on the sampled day -- rare events; scan the 525-partition series for one specimen before relying on the columns. Absence-on-one-day is not mechanism-absence | one at-rest scan | corrected counts |

## BOUNDARIES, STATED

**USD-only book by construction** -- zero currency/FX columns across all 8 pulled tables; the
standard's FX fields are N/A-BY-BOUNDARY and the sec10 output contract documents base-currency=USD.
**History floor:** daily valuations from **2024-07-08** (25 months, 525 trading days); realized-lot
history deeper (fact_rld to 2023-07-12, 773 partitions); monthly period tables beside the daily core
(fact_rly/rty, 37 month-ends to 2026-07-31). **The doc's own scope note carries through: this
establishes GIPS-ALIGNED CALCULATION feasibility, not firm-wide GIPS COMPLIANCE** (composites,
policies, disclosures, track-record presentation are out of scope here). Cadence-gap scan of the
525-partition series (trading-calendar-resolved) is a build-time check, marked INFERRED-continuous
today. Content cells are one-day samples (date=2026-08-07) and say so; schema+cadence cells are
full-series. Sampling wider is cheap at build.

## WHAT THE ASSESSMENT DID NOT DO

No TWR was computed; no gap-scan, materiality measurement, or reconciliation battery was exercised
(build-time acts, deliberately -- the rectangle's one UNMEASURED cell is that statement in status
form); the standard's numbered provisions were taken on the doc's authority, not re-derived from
the GIPS handbook; certification is CVO's. One instrument self-catch disclosed: my first
fixed-income probe keyed on `maturity_date` non-empty, which is sentinel-populated on ALL rows --
discarded, replaced with `interest_rate` nonzero (112). The empty-string counting correction
(bare notna() reads 100% on string columns) inverted two cells before publication and is now a
mechanical constraint (M2) in the rectangle itself.
