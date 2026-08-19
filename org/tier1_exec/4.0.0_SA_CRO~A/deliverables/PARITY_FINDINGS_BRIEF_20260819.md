# PARITY FINDINGS BRIEF -- everything measured on BD-vs-us parity, 2026-08-19 (4.0.0_SA_CRO~A)

**Commissioned:** Andrew-direct at this terminal ~1940Z: *"writing a brief on all your findings on
parity thus far here, and take care to write it with detail."*
**Scope:** the full parity arc worked at this seat today under Andrew's egress grants -- identity
plane (fam x BD), organizational plane (portfolio groups), valuation plane (the Travis
decomposition + basis semantics), and the harness/convention consequences. Every number below was
MEASURED this session; each subsection carries its evidence source. Companion deliverables (full
detail): `FINDING_FAM_IS_A_SLOW_DIM_20260819.md` · `FAM_FIELD_SEMANTICS_AND_BD_PLATFORM_OVERLAP_20260819.md`
· `BD_PORTFOLIO_GROUP_KEYING_SCAN_20260819.md` · `TRAVIS_GROUP_DECOMPOSITION_HOW_BD_BUILDS_456M_20260819.md`
(+ closure addendum) · the three ANDREW_DIRECT records (egress ~1450Z SDD, ~1830Z BD scanning,
~1935Z valuation basis).

---

## 1. THE IDENTITY PLANE -- Schwab fam vs BD's native identity model

### 1a. What fam is (per-field, build-verified + measured)
Six columns, ALL identity, zero event content: master grouping id (19 distinct) · firm name (8) ·
rep name (9) · account number (the key; 1 row/account) · holder/registration name (5,084) ·
household key (TIN-shaped, 4,246; consumed as grouping key only, never emitted -- a01 emits a
hashed account-anchor). No dates, amounts, quantities, or prices anywhere in the file.
**Stability:** consecutive publishes 99.75% byte-identical with ZERO value changes on shared
accounts (only membership moved: +18/-2); over a full month, 2 value changes in 7,050 shared
accounts (holder-name corrections), membership churn ~5 accounts/business day. *(Source: silver
fact_fam partitions 2026-07-10 / 08-07 / 08-10; a01_dim_relationship.py:9-22.)*

### 1b. fam x BD value-level cross-reference (5,277 joint accounts)
- **Households NEST inside BD Relationships: 96.8%** of fam households sit wholly inside one BD
  Relationship. The reverse does not hold -- 589 of 2,689 BD relationships span 2+ fam households;
  41.6% of joint accounts sit in a multi-household relationship. Reading: fam = per-taxpayer grain;
  BD Relationship = the client super-grouping (spouses/trusts/entities). Consistent hierarchies.
- **Holder names:** fam col_5 = BD "Client Name" (55.8% identical token-set; 92.1% at >=50%
  overlap; the tail is registration-string formatting). BD "Account Owner" is NOT a holder name (0%).
- **Rep/advisor layer: alignment NOT ESTABLISHED.** Both candidate alignments equal their
  majority-class baselines (Rep Code 82.3% vs 82.1% base; SEC Client Type 98.5% vs 98.5%) --
  honestly discounted as the cannot-fail-instrument class. fam's rep vocabulary and BD's four-role
  model are different languages; the mapping rides the queued householding probe.
- **Coverage:** fam 7,202 accounts | BD allocation export 6,145 | joint 5,277 (73.3% of fam) |
  fam-only 1,925 (Schwab custodial universe beyond BD's grouped/open scope) | BD-only 868
  (other-custody book). Two of fam's nine reps have books entirely absent from BD's export.

## 2. THE ORGANIZATIONAL PLANE -- portfolio groups (the advisor-book key)

- **Semantics ruled by the 49F data person (transcript, recorded):** Portfolio Group = the
  advisor's BOOK -- "the Mitch Johnson portfolio group... his book, essentially"; not strategy.
  Division groups exist (49 Private Wealth, <10% of assets). Advisors live on the BI dashboard.
- **Structure measured:** 201 groups in the daily export (qt6 sees 216 -- the export filters);
  **90.6% of accounts belong to 2+ groups** (advisor + local-ops + division + firm-wide views).
  ⛔ Groups are overlapping VIEWS, never a partition -- summing across groups reads ~$10.2B on a
  ~$1.77B book. The partition-like key exists natively: **"Primary Portfolio Group" (dim id 436)**.
- **qt6 "BI Billing" is the native group-keyed economics table:** level hierarchy Date -> Team ->
  Relationship -> Client -> Portfolio Group -> Portfolio -> Account -> Holding; measures BMV, EMV,
  Net Additions/Flows (incl/excl fees), Fees, Net Gain, Income, New Accounts, at month grain. One
  636-row export = the whole firm's book economics for a quarter at advisor-book grain.

## 3. THE VALUATION PLANE -- the Travis decomposition (every dollar placed)

**The three-way that started it:** role-tagged attribution ~$373M (Andrew's meeting quote) vs
Andrew's logical estimate ~$460M vs **BD's native group number $456.8M** (vindicating the estimate
within 1%). Decomposition of the 456.8, all layers summing:

| component | accounts | value | evidence |
|---|---|---|---|
| Schwab (0833) members matched to our canonical basis | 312 | $420.5M (BD) vs **$420.3M (ours)** | dim_balance date=2026-08-18 |
| -- of which tie within 0.1% | **309 of 312** | net delta **+$146K (+0.03%)** | penny-grade on the outlier |
| held-away/other-custody members (8-digit-shaped) | 23 | $20.2M | BD Custodian dim, per account |
| non-8-digit-id members (same held-away class) | 12 | $16.1M | id-shape census |
| **group total** | **347** | **$456.8M** | member sum ties exactly |

**Held-away subclasses (the ~$36.3M no Schwab-only pipeline can ever see):** Brighthouse annuities
6/$8.69M · National Christian Foundation DAF 1/$5.64M · Lincoln annuity 1/$3.70M · Merrill 401(k)
3/$1.09M · Fidelity 8/$0.99M · Citi 1/~$0 · trivial Schwab strays 3/$0.07M (+ the 12 non-8-digit).

**Attribution mechanics:** BD's number is a pure MEMBERSHIP sum -- no modeling. The role-tagged
view (241 accounts, ~$349M export-basis) is an ATTRIBUTE view; his group additionally carries 96
Schwab accounts with NO Travis role tag (+$88.7M -- the house/private-wealth-bucket class Andrew
described). Role-tagged-but-not-in-group: 2 accounts. BD serves membership.

## 4. BASIS SEMANTICS -- the definitions, proven mechanically

- **qt1 identity: `Market Value == Unaccrued Market Value + Accrual` holds on 100.0% of 120,215
  position rows (max residual $0.00).**
- **qt6 EMV == qt1 Market Value per account** on every accrual-bearing account tested. Therefore
  **BD's EMV = securities MV + free cash + accrued income** (accrual- and cash-inclusive).
- **Schwab's `net_mv_plus_cash` = cash-inclusive, accrual-EXCLUSIVE** -- measured: nmpc equals the
  UNACCRUED value penny-for-penny on income accounts; EMV - nmpc == accrued interest exactly.
- **Cash:** BD carries free cash as a position ($35.2M firm-wide, 7,201 accounts); our fact_rps is
  securities-only (1 cash-like row in 102,797); our canonical law (b00: V(t) =
  dim_balance.net_mv_plus_cash) is cash-inclusive BY DESIGN -- the correct comparison basis.
- **Accrual magnitude in frame:** $88.0K across 155 positions = 0.64% of the $13.7M direct-bond
  sliver (157 DEBT positions) of a $1.77B book (99.2% equities/funds where holder-level accrual
  cannot exist). Specimen: account ...2917 -- accrual $22.47K on $815K (2.8% of account value --
  material per-account, immaterial book-wide).
- **ANDREW RULING (~1935Z, verbatim recorded): NET/REAL basis -- "if the cash is not received it
  shouldnt be counted... the schwab approach is better here."** Carried to CTO's B_02 gate; b00's
  accrued_income=0 placeholder becomes the ruled answer. GIPS nuance surfaced (performance calcs
  may accrue internally where GIPS-grade per-account fixed-income returns are claimed -- design
  option, parked, immaterial at today's allocation).

## 5. THE CORRECTION CHAIN (part of the findings -- what the method caught, in order)

1. **The +2.48% false gap:** my first tie used fact_rps (positions-only) -- true of that table,
   wrong as a BD-vs-us claim; on the canonical basis the gap is +0.03%. Owned in the record;
   CTO registered a HARNESS BASIS RULE making the error inexpressible (compare on nmpc; the
   BD-EMV residual is then the accrual component alone).
2. **The clean 0-of-335 join:** an 8-digit join against the canonical zfill(10) key domain -- the
   wrong-domain class; its tell was the too-clean zero.
3. **Decimal-vs-float arithmetic crash:** our silver preserves vendor decimals (the SILVER-DTYPE
   class, live specimen; folded into TO-D3.1's brief).
4. **Majority-class baseline discounts:** two "alignments" (82.3%, 98.5%) equaled their baselines
   and were discounted -- the cannot-fail-instrument class caught in-pass.
5. **The one-day-offset check that CLEARED:** fact_rps partitions proved CONTENT-dated
   (business_date == partition date on all 102,797 rows), so same-content-date comparison held.

## 6. WHAT IS REGISTERED / PARKED / OPEN (as of ~1940Z)

- **Registered pre-probe at CTO (@a02f9ff5a4 -> @c379cb6521 -> @fee546e533):** C5 as an EXACT-form
  classifier (delta == accrued interest); A1 corrected in-register with the correction chain cited;
  the harness basis rule; specimen ...2917 discharged; held-away subclasses feed the denominator
  call at Andrew.
- **Ruled today:** valuation basis = net/real (Andrew ~1935Z). **Parked:** B_02 formal flip
  mechanics (CTO gate + DS lane); the GIPS layer-split option.
- **Open:** the BD householding one-shot probe (AE fires THU-FRI; gap-coverage decision table
  pre-registered); the BI dashboard app's own endpoint domain (unmapped in data/black_diamond/API);
  the rep-layer vocabulary mapping (rides the probe); the T1/T2/T3 threading recommendations at
  CTO/COO.

**One-paragraph summary:** BD and our canonical valuation agree to +0.03% on the accounts both see;
every residual has a NAMED, EXACT mechanism (free cash inclusion, accrued-interest basis -- now
ruled net/real, held-away custody); the attribution question is a definitions question (membership
vs role-attribute), not a data question; and the identity plane nests cleanly (fam-household inside
BD-relationship) with one vocabulary gap (reps/roles) awaiting the probe. Parity is not a mystery
anywhere we have looked -- it is a set of measured, classified, pre-registered differences.
