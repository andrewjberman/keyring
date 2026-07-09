# DECISION BRIEF: the 49F portal "Account Type" filter is a three-way inconsistency

**Status:** OPEN -- awaiting a **served-surface product decision** (Andrew, routed via COO)
**Severity:** S2 -- live client-facing broken control; **no incorrect monetary value**
**Author:** 0.4.0_DS_ClientPlatform~B, 2026-07-09
**Rulings that produced this:** CTO `20260709T215910Z` (S2 accepted; severity bound to blast radius, not reader identity), CTO `20260709T220052Z` (the inversion is the ruling; `A_00` enrichment fix BLOCKED on this decision)
**Blocks:** any fix that populates `accounts_dimension.account_type` (fabric-wide prohibition, effective 2026-07-09)

---

## 1. What is broken, on the served artifact

`gold/artifacts/filters/dimensions.json` (LastModified `2026-07-09T09:53:12Z` -- today's scheduled gold):

```
architect     column=architect            values=56
region        column=local_ops            values=19
implementor   column=implementor          values=50
account_type  column=account_owner_type   values=0    <-- EMPTY
tax_status    column=tax_status           values=3
state         column=client_state         values=49
```

One filter control of six renders with **zero options**. No AUA, no certification, no served total, no monetary
value is affected. That is why this is **S2 and not P0**, notwithstanding that it sits on the same served plane
as the AUA freeze.

## 2. The mechanism, source-grounded

```
A_00.accounts_dimension.py     writes gold/dimensions/accounts_dimension_latest.parquet
                               account_type              0 / 10,545 non-null   (verified live)
                               account_registration_type 0 / 10,545 non-null   (same enrichment, same ride)

D_00.portal_aggregates.py:355  _load_parquet(ACCOUNTS_DIMENSION, [... 'account_type' ...])
D_00.portal_aggregates.py:822  _dim_values(series) = series.dropna()...        -> all-null yields []
D_00.portal_aggregates.py:844  'account_type': {'label':  'Account Type',
                                                'column': 'account_owner_type',
                                                'values': _dim_values(adim['account_type'])}
D_00.portal_aggregates.py:818  build_filters() -> gold/artifacts/filters/dimensions.json   [SERVED]
```

**Root** (one stub, not three bugs): `A_00` joins its enrichment off the `sorted()[-1]` newest-**by-name**
allocation snapshot, guarded on **object existence** rather than **row count**. The newest-by-name partition is a
0-row stub. `A_00` prints `0 accounts with type/registration data` and **proceeds**. Same existence-is-the-proxy
defect as `C_02`'s certification path; `rows` is the property.

## 3. The three-way inconsistency -- why no two-way fix is safe

The filter's three fields disagree with each other:

| field | value | domain |
|---|---|---|
| `label` | `"Account Type"` | -- |
| `column` (what is filtered) | `account_owner_type` | `{Sole, Joint, Trust}` + 3,286 nulls |
| `values` (what is offered) | `adim['account_type']` | 30 distinct: `IRA, Brokerage, RothIRA, ...` |

Measured overlap (dimension vs `silver/allocations/2026-07-08`, the last real partition):

```
in BOTH  -- would work BY COINCIDENCE :  Joint, Trust                                (2 of 30)
values-only -- select ZERO rows        :  401K 403B 529 Annuity Bank Brokerage Charitable Corporate
                                          CreditCard EducationSavings Estate Guardian HSA IRA
                                          InheritedIRA InheritedRothIRA Insurance LLC Loans Mortgage
                                          "No Account Type Assigned" Other RothIRA SEP SIMPLE Savings
                                          TermLife UTMA                              (28 of 30)
column-only -- never offered           :  Sole   (6,063 accounts -- the LARGEST cohort)
```

## 4. THE INVERSION: the null column is currently an accidental safety

**Populating `account_type` -- the obvious `A_00` fix -- makes this strictly worse.**

- **Today:** the dropdown is **empty**. Visibly broken. It cannot mislead anyone.
- **After the "fix":** the dropdown fills with 30 options. **28 of them select zero rows.** `Joint` and `Trust`
  work by coincidence. `Sole` -- 6,063 accounts, the largest cohort -- is never offered.
  A user selects `IRA`, sees an empty result set, and **believes it.**

**A visibly-broken control becomes a silently-wrong one.** This is the third instance tonight of the same move
(the others: `fabric-check`'s deploy gate, where fixing the false-REDs alone would have made the gate permanently
silent; and the `DryRun` SSM parameter). CTO: *"loud -> quiet is becoming the most expensive move we make."*

**Therefore `A_00`'s enrichment fix is BLOCKED on this decision, fabric-wide.** The prohibition lands on the
dangerous half only:

> **AUTHORIZED and encouraged:** `row_count > 0` guard + **ABSTAIN** + a loud alarm in `A_00`. This keeps
> `account_type` **null** and makes the producer **loud**. Loud-and-null is exactly the state we want while the
> semantics are open.
>
> **PROHIBITED:** anything that populates `account_type` before the filter semantics are settled.

## 5. The decision -- these are two different products, not two implementations

**Option A -- make the control WORK.** Repoint `values` to `adim['account_owner_type']`.
- Filter offers `Sole / Joint / Trust`; every option matches rows. Correct, immediately.
- The label "Account Type" now describes **ownership structure**, which is arguably what it always filtered.
- Cheapest, no producer dependency, unblocks `A_00` immediately.
- Loses the ability to filter by `IRA / Brokerage / RothIRA / ...` -- a capability the portal never actually had.

**Option B -- make the control MATCH ITS LABEL.** Repoint `column` to `account_type`, and fix `A_00` so the
column is populated.
- Filter offers the 30 real account types and filters on them. This is probably what a user expects from a
  control labelled "Account Type".
- **Depends on the `A_00` enrichment fix**, which depends on a real allocations partition -- currently a 0-row
  stub on most dates (see the `bd-allocation-processor` / `silver/allocations` stub issue).
- Strictly more capability; strictly more upstream fragility. If the enrichment silently nulls again, the filter
  silently empties again.

**Option C -- both, distinctly.** Two filters: `Ownership` (`account_owner_type`) and `Account Type`
(`account_type`). Most correct, most work, and the second is still gated on the enrichment.

**This is a served-surface product decision.** It is not DS's, not CTO's, and it should not be "fixed" inside a
gold script by whoever touches `A_00` next. It routes to **Andrew, via COO**, with the two domains printed above.

## 6. Consumers -- what was traced, and what was NOT

Method (per CTO's ruling, *"string co-occurrence in a file is not dataflow"*): every `account_type` reference in
`data/black_diamond/scripts/gold/*.py` resolved to **the frame it is read from**.

**Real consumer of the DIMENSION's copy (1):**
- `D_00` -> `filters/dimensions.json` (served). Confirmed above.

**Grep false positives -- they read the POPULATED silver allocations column, not the dimension (4):**
- `C_02:319/325` (`silver[...]`), `C_04:130/141` (`silver_df[...]`), `E_19:121/131` (`silver_df[...]`),
  **`D_04:3267/3528`** (`alloc_df` / `silver_agg`). `D_04` was a named P0-trigger script and does not touch the
  dimension's copy at all.

**Loads-and-discards (1):**
- `D_00b:1314` loads `account_type` in its column list and **never references it again.** Reads as a consumer to
  any column-list / loader-based trace; emits nothing.

**Propagates the null internally, not served via this path (2):**
- `B_01` enriches `holdings_lots` with the null column. `C_05` carries it into `client_tax_liability`; `D_00`
  does **not** select `account_type` out of `CLIENT_TAX_LIABILITY`.
- `A_04` derives `client_dimension.account_types` -> **0 / 3,771 non-blank**, and **no `D_*` script reads
  `account_types`.** A dead field that dies in the dimension.

### What this trace would NOT have surfaced -- the negative is a claim about the query
`D_00` is a **confirmed** served consumer. **"Nothing else consumes it" is NOT a claim made here.** Unread:
- dynamic column access -- `df[col]` with a computed `col`, `df.filter(regex=)`, `**kwargs`, `getattr`.
  `B_01:450` does `available = [c for c in keep if c in df.columns]`; it was traceable **only because `keep` is a
  literal list.** A computed list would have been invisible to the method that found the bug.
- `merge()`-and-carry: the whole dimension pulled into a downstream frame and written out without ever naming
  the column (including `_x` / `_y` suffix survivors).
- the **portal frontend** reading `filters/dimensions.json` directly; Lambdas; Athena/SQL; notebooks.
- **the cot tree, entirely untraced** (COO reports 828 cot accounts nulled the same way).
- whether `B_01`'s null-enriched `holdings_lots` reaches any served artifact -- **not verified, flagged.**

## 7. File as one root

`account_type` (0/10,545), `account_registration_type` (0/10,545), and `client_dimension.account_types`
(0/3,771) are **one stub, not three bugs**: a single existence-guarded join onto a 0-row partition in `A_00`.
