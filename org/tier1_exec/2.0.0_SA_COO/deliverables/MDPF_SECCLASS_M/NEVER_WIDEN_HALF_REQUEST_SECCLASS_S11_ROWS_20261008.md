# Never-widen half request, MDPF_SECCLASS -- the D1-S11 row set: 106 new rows and 34 remaps to alternatives (FWD-16, FWD-17, cell SC-e-77)

**Author:** `0.9.0_WK_MDPF_SECCLASS~67` for `2.0.0_SA_COO~M1`, 2026-10-08 ~19:4xZ. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED (2.0.0_SA_COO~M1); CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.
Source: `BD_UNCLASSIFIED_TRACE_D1S11_20261008.json` groups B (25 securities) and D (81 securities); Andrew-direct 2026-10-08 ~19:0xZ, verbatim: "Hedge funds, private funds, real estate funds, all of this falls to Alternatives."; the set `S11_ROW_SET_20261008.tsv`; the CVO grades every class and every `rule=andrew-alternatives` mark at L9.

## The act (by the issuer, after both halves sign)

`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R15_CHECKS/s11_rows_write.py --write --half <this file> --snapshot <snapshot.json>`

On table `etf-classifications` (us-east-1), per line of the set:

- **NEW (106 lines):** one `PutItem` conditioned on `attribute_not_exists(ticker)`. Item: `ticker` (the B ticker or the D `NAME::` key), `asset_class`, `sub_asset_class` (only where the set names one), `classified_by = scheduled`, `updated_by = mdpf-secclass-s11-rows`, `name = clean_name(<trace name>)`, `identifier_namespace = NAME` for a `NAME::` key (absent for a ticker), `last_updated`.
- **REMAP (34 lines):** one `UpdateItem`: `SET asset_class, updated_by, last_updated` and `sub_asset_class` set to the new value or REMOVEd when the set names none; `CONDITION attribute_exists(ticker) AND asset_class = <the current class the set read>`.
- Every class is one of the six; every non-empty sub-class is in the contract's closed list (`MDPF_SECCLASS_CONTRACT.json` 0.8.0 `values_by_class`); a line outside either is refused before any call. No other table, no S3 object, no code, no deploy.
- **Dry run** (read this session, live table, `s11_rows_write.py` with no flag): `S11-ROWS-DRY-RUN new=104 remap=34 refused_present=2 refused_stale=0 puts=0` (amendment 2, 2026-10-08 ~20:22Z; before amendment 2 it read `new=105 remap=11 refused_present=1`). The present keys are **`OXYWS`** (group B, $4,958; live `equity/Energy`, `updated_by mdpf-secclass-model`, `last_updated 2026-10-08T20:08:38Z`, landed by the e49 runner after Amendment 1; the set's line reads `equity`, the same class; row `MDPF_SECCLASS-D1-W67-S3`) and **`RAL`** (group B, $70): the live row reads `equity/Information Technology`, `updated_by mdpf-secclass-model`, `last_updated 2026-10-08T19:01:52Z`, so it landed after the trace was cut. The set's line for it reads `equity`, the same class, so the write would change nothing; the issuer drops the `RAL` line from the set at signing (then the dry run reads `new=104 ... refused_present=0`) or lets the writer refuse it. The writer wraps the client with a counter of every mutating call, a mutating call in a dry run raises, and the run asserts `puts=0`.

## Blast radius

Table `etf-classifications`: up to 106 new keys and 34 existing keys. A NEW put cannot touch an existing key (the condition refuses it). A REMAP moves only `asset_class`, `sub_asset_class`, `updated_by` and `last_updated` of a row that still reads the class the set read.

### Each line's before and after

NEW lines (before: no row; after: the pair shown; `rule` marks Andrew's alternatives rule; $ is the trace's market value on the 2026-10-06 partition):

| key | grp | after (class/sub) | rule | $ |
|---|---|---|---|---|
| DFUS | B | equity |  | 1,316,334.00 |
| NAME::CAIS PRIVATE EQUITY CORE II LP | D | alternatives | andrew-alternatives | 860,935.14 |
| NAME::PROSPERA INCOME ETF | D | fixed_income |  | 850,581.64 |
| NAME::CNL STRATEGIC CAPITAL LL C CLASS A 1G | D | alternatives | andrew-alternatives | 344,785.04 |
| NAME::BLACKSTONE - BXPE ESC | D | alternatives | andrew-alternatives | 300,000.00 |
| SDVY | B | equity |  | 274,277.74 |
| NAME::INDEXED ANNUITY | D | structured/Hedge |  | 228,506.75 |
| NICHX | B | alternatives |  | 171,424.76 |
| UWMC | B | equity |  | 97,688.84 |
| SCBP1 | B | equity |  | 95,805.22 |
| NAME::SCHWAB CHARLES FAMILY FD GOV SECURITIES | D | fixed_income |  | 90,129.61 |
| NAME::CALL BE 00105 | D | structured/Options Income |  | 82,002.60 |
| NAME::JHANCOCK BALANCED R6 | D | equity |  | 73,466.02 |
| NAME::CALL IREN 00010 | D | structured/Options Income |  | 72,513.00 |
| FYC | B | equity |  | 71,151.16 |
| USERX | B | commodities/Metals |  | 60,170.69 |
| NAME::KKR PRIVATE EQUITY CONGL OMERATE LLC CLASS U | D | alternatives | andrew-alternatives | 56,653.23 |
| NAME::FIRST TRUST MULTI-STRATEGY CL I | D | alternatives |  | 55,749.06 |
| NAME::FIDELITY ADVISOR STOCK SELEC MID CP M | D | equity |  | 54,640.79 |
| NAME::VARIANT ALTERNATIVE INCOME INSTITUTIONAL | D | alternatives |  | 53,835.67 |
| NAME::STEPSTONE PRIVATE MARKETS I | D | alternatives | andrew-alternatives | 53,492.83 |
| NAME::FS MVP PRIVATE MKTS FD CL I | D | alternatives | andrew-alternatives | 51,493.09 |
| NAME::NUVEEN CHURCHILL PRVATE CAP SHS CL I | D | alternatives | andrew-alternatives | 46,223.71 |
| NAME::HARTFORD BALANCED INCOME F | D | equity |  | 45,153.03 |
| NAME::BUFFALO GROWTH INCOME INST | D | equity |  | 43,030.61 |
| NAME::LORD ABBETT GLOBAL EQUITY I | D | equity |  | 35,619.51 |
| SCII1 | B | fixed_income |  | 34,511.29 |
| NAME::FRANKLIN ETHEREUM ETF | D | commodities/Commodities |  | 27,070.80 |
| XVV | B | equity |  | 25,438.96 |
| SKWD | B | equity |  | 24,427.50 |
| NAME::CONSERVATIVE PORTFOLIO | D | equity |  | 21,270.39 |
| NAME::JPMCB SMARTRETIREMENT DRE 2040 CF-D | D | equity |  | 16,747.36 |
| NAME::S P 500 ANN LOCK 5YR -10 | D | structured/Hedge |  | 15,766.16 |
| NAME::SCHWAB TARGET 2025 INDEX | D | equity |  | 14,637.78 |
| NAME::EATON VANCE STRATEGIC INCOME CLASS I | D | fixed_income |  | 12,169.44 |
| NAME::PROSHARES BITCOIN ETF | D | commodities/Commodities |  | 11,620.00 |
| SCGK1 | B | fixed_income |  | 10,414.08 |
| NAME::INVESCO VARIABLE RATE PREFERRED ETF | D | fixed_income |  | 9,488.00 |
| NAME::AMERICAN FUNDS INCOME FUND OF AMER 529A | D | fixed_income |  | 9,024.85 |
| NAME::VORNADO RLTY TR PFD SER L 5 40 | D | equity |  | 8,712.50 |
| NAME::S P FUTURES 3 IDX PTPT W | D | structured/Hedge |  | 8,409.66 |
| GTOP | B | equity |  | 7,466.91 |
| NAME::RALLIANT CORP COM | D | equity |  | 6,819.82 |
| NAME::BD949S99 | D | equity |  | 5,679.65 |
| NAME::ARK 21SHARES BITCOIN ETF | D | commodities/Commodities |  | 5,072.00 |
| NAME::FRANKLIN XRP ETF | D | commodities/Commodities |  | 4,968.21 |
| OXYWS | B | equity |  | 4,958.05 |
| NAME::VANECK BITCOIN ETF | D | commodities/Commodities |  | 4,164.12 |
| NAME::MORNINGSTAR DEFENSIVE BOND | D | fixed_income |  | 4,103.37 |
| NAME::PIMCO ALL ASSET I2 | D | equity |  | 3,707.15 |
| HEAL | B | equity |  | 3,501.21 |
| NAME::TQQQ AUG 09 24 82 CALL | D | structured/Options Income |  | 3,240.00 |
| NAME::BDDNL2V4 | D | equity |  | 2,967.63 |
| NAME::BD9AS499 | D | fixed_income |  | 2,757.79 |
| NAME::IGV JUL 17 26 114 CALL | D | structured/Options Income |  | 2,700.00 |
| NAME::PIMCO TRENDS FUND INSTITUTIONAL | D | alternatives |  | 2,453.84 |
| PQTIX | B | alternatives |  | 2,430.34 |
| NAME::INVESCO DB US DOLLAR INDEX BULLISH FUND | D | alternatives |  | 2,126.48 |
| PPLT | B | commodities/Metals |  | 1,639.00 |
| COMP | B | equity |  | 1,430.10 |
| BINC | B | fixed_income |  | 1,281.59 |
| NAME::BDP134X3 | D | alternatives |  | 1,259.60 |
| GSRTX | B | alternatives |  | 1,084.72 |
| NAME::BDP10C6I | D | alternatives |  | 999.99 |
| NAME::BDO6GHW8 | D | fixed_income |  | 908.80 |
| NAME::FIDELITY WISE ORIGIN BITCOIN FUND | D | commodities/Commodities |  | 856.38 |
| NAME::GOLDMAN SACHS MANAGED FUTS STRAT INV | D | alternatives |  | 831.51 |
| ASFYX | B | alternatives |  | 795.76 |
| NAME::ISHARES TRUST ISHARES USD GREEN BOND ETF | D | fixed_income |  | 774.94 |
| NAME::VOLATILITY SHARES 2X BITCOIN ETF | D | commodities/Commodities |  | 740.91 |
| NAME::BD7UD5HA | D | equity |  | 730.38 |
| NAME::CLOV NOV 28 25 4 CALL | D | structured/Options Income |  | 720.00 |
| NAME::INCOME INDEX POOL | D | fixed_income |  | 603.53 |
| BITX | B | commodities/Commodities |  | 440.56 |
| NAME::ISHARES ETHEREUM TRUST ETF | D | commodities/Commodities |  | 199.68 |
| MPNGY | B | equity |  | 171.00 |
| NAME::SCHFDX0 | D | fixed_income |  | 170.92 |
| NAME::BD7I9FCG | D | equity |  | 114.39 |
| RAL | B | equity |  | 69.79 |
| NAME::BDV4IISI | D | fixed_income |  | 47.56 |
| NAME::BDVR693I | D | equity |  | 47.17 |
| NAME::BDYXF3XU | D | equity |  | 46.69 |
| NAME::BDMRCIX0 | D | equity |  | 45.88 |
| NAME::VICTORY PIONEER STRATEGIC INCOME Y | D | fixed_income |  | 37.34 |
| NAME::HERTZ GLOBAL HLDGS INC WT EXP 063051 | D | equity |  | 28.68 |
| NAME::BDPU6036 | D | equity |  | 19.68 |
| NAME::DARKHORSE TECHNOLOGIES INC COM SHS | D | equity |  | 17.34 |
| NAME::BDP10C63 | D | alternatives |  | 15.59 |
| NAME::BDP134X6 | D | alternatives |  | 12.13 |
| NAME::BDPD3F76 | D | fixed_income |  | 11.76 |
| NAME::BDP10C60 | D | alternatives |  | 1.95 |
| TSEOQ | B | equity |  | 0.70 |
| CMWAY | B | equity |  | 0.14 |
| NAME::COHEN STEERS PREFERRED SEC INC I | D | fixed_income |  | 0.00 |
| NAME::SHAW PARK PRIVATE MARKET S 2021 LP | D | alternatives | andrew-alternatives | 0.00 |
| NAME::TEMPLETON WORLD A | D | equity |  | 0.00 |
| NAME::BOW RIVER CAPITAL EVERGR EEN FUND CLASS I | D | alternatives | andrew-alternatives | 0.00 |
| NAME::THOMPSON BOND | D | fixed_income |  | 0.00 |
| NAME::OCEAN PARK TACTICAL ALL ASSET INSTL | D | equity |  | 0.00 |
| NAME::PRINCIPAL DIVERSIFIED INCOME INSTL | D | fixed_income |  | 0.00 |
| NAME::MORNINGSTAR MULTISECTOR BOND | D | fixed_income |  | 0.00 |
| NAME::AMERICAN FUNDS 2040 TRGT DATE RETIRE A | D | equity |  | 0.00 |
| NAME::AMERICAN BEACON AHL MGD FUTS STRAT Y | D | alternatives |  | 0.00 |
| NAME::TFI INTL INC COM | D | equity |  | 0.00 |
| NAME::PIMCO ALL ASSET INSTL | D | equity |  | 0.00 |
| NAME::ORION PROPERTIES INC COM | D | equity |  | 0.00 |

REMAP lines (11 from the original cut, then the 23 liquid-alt mutual-fund lines added by amendment 2, `evidence` strategy phrase per line in the set; before: live class read this session; after: the pair shown; all carry `rule = andrew-alternatives`):

| key | before (class/sub, updated_by) | after (class/sub) | $ in the trace |
|---|---|---|---|
| REM | equity/Financials, mdpf-secclass-model | alternatives/Real Estate | not in the trace (UNREAD) |
| NAME::COHEN STEERS GLOBAL REALTY I | equity/Global, mdpf-secclass-old-list-reclassify | alternatives/International Real Estate | not in the trace (UNREAD) |
| NAME::FLEXSHARES GLOBAL QUALITY REAL ESTATE INDEX FUND | equity/Global, mdpf-secclass-old-list-reclassify | alternatives/International Real Estate | not in the trace (UNREAD) |
| NAME::T ROWE PRICE REAL ESTATE | equity/US Large Cap, mdpf-secclass-old-list-reclassify | alternatives/Real Estate | not in the trace (UNREAD) |
| NAME::PACER DATA INFRASTRUCTURE REAL ESTATE ETF | equity/US Large Cap, mdpf-secclass-old-list-reclassify | alternatives/Real Estate | not in the trace (UNREAD) |
| NAME::FIRST TRUST S P REIT INDEX FUND | equity/US Large Cap, mdpf-secclass-old-list-reclassify | alternatives/Real Estate | not in the trace (UNREAD) |
| NAME::PENDER REAL ESTATE CREDIT I1 | fixed_income/Structured Credit, mdpf-secclass-old-list-reclassify | alternatives/Real Estate | not in the trace (UNREAD) |
| NAME::SHAW PARK MULTI STRATEGF OFFSHORE FUND LP | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CCA EIGER OPPORTUNITY LP CAPITAL VALUES | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::BLACKSTONE PRIVATE CREDIT FUND SHS CL I | fixed_income/Structured Credit, mdpf-secclass-model | alternatives | 85,410.26 |
| NAME::CARLYLE TACTICAL PRIVATE CREDIT N | fixed_income/Structured Credit, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::AB SELECT US LONG SHORT ADVISOR | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::AQR LONG-SHORT EQUITY I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CROMWELL LONG SHORT INVESTOR | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CALAMOS HEDGED EQUITY I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::JPMORGAN HEDGED EQUITY 2 R6 | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::JPMORGAN HEDGED EQUITY A | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::JPMORGAN HEDGED EQUITY I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::JPMORGAN HEDGED EQUITY R6 | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::TOEWS HEDGED U S FD | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CALAMOS MARKET NEUTRAL INCOME I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CALAMOS MARKET NEUTRAL INCOME R6 | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::VICTORY MARKET NEUTRAL INCOME I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::EATON VANCE GLBL MACR ABSOLUTE RETURN I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::EATON VANCE GLBL MACRO ABS RET ADVTG A | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::GOLDMAN SACHS ABSOLUTE RET TRCKR INSTL | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::ABSOLUTE CONVERTIBLE ARBITRAGE INSTL | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| ARBIX | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::FIRST TRUST MERGER ARBITRAGE CL I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::NEXPOINT MERGER ARBITRAGE Z | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::BLACKROCK EVENT DRIVEN EQUITY INSTL | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::BLACKROCK SYSTEMATIC MULTI-STRAT INSTL | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| NAME::CATALYST MILLBURN HEDGE STRATEGY I | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |
| JHEQX | structured/Hedge, mdpf-secclass-model | alternatives | not in the trace (UNREAD) |

### The local candidate served-mix delta (from the trace's dollars)

Basis: the trace's 2026-10-06 partition (`reconstruction`, `claim: inferred`: a local rebuild of C_06's chain, NOT the served bytes). The served file `s3://opal-data-bd/platinum/firm/mix_summary.json` (data_as_of 2026-10-06) reads unclassified USD 140,161,795 (6.94 pct of 2,019,548,568); the reconstruction reads 139,402,747.60. Groups B and D hold USD 5,820,645.24 of it. When the 106 securities read a canonical row, that amount leaves unclassified and enters the class below at each reader's next run; the firm total is unchanged.

| class | NEW securities | USD moving out of unclassified |
|---|---|---|
| equity | 42 | 2,256,223.77 |
| fixed_income | 21 | 1,027,016.51 |
| alternatives | 24 | 2,006,604.44 |
| structured | 8 | 413,858.17 |
| commodities | 11 | 116,942.35 |
| **total** | **106** | **5,820,645.24** |

- Of the alternatives line, the `rule = andrew-alternatives` NEW lines (9 securities) hold USD 1,713,583.04; the rest are the managed futures, alternative-income and opaque-id lines the old map already read alternatives.
- **REMAP dollars:** only `NAME::BLACKSTONE PRIVATE CREDIT FUND SHS CL I` appears in the trace (USD 85,410.26, group A). The other ten REMAP keys are not in the trace (the trace lists only the unclassified), so their held amounts are `UNREAD` here; each moves between two class buckets by its held amount and moves no firm total. The issuer reads them from the compare at signing.
- The named-by-name classes here are judgments, not facts (`claim: inferred`): hedge, private and real estate fund status is graded by `3.0.0_SA_CVO`. Amendment 2 (Andrew-direct ~20:1xZ, "1. Approved."; `ANDREW_DIRECT_20261008_201xZ_LIQUID_ALTS_TO_ALTERNATIVES_ETF_STRATEGY_SLEEVES_ENDPOINT_CONFIRMED.md`) moved the liquid-alt mutual funds into the set as 23 REMAP lines (22 `NAME::`/ticker rows of hedged-equity, long/short, market-neutral, absolute-return, arbitrage, event-driven, multi-strategy and managed-futures mutual funds, `structured/Hedge` to `alternatives`, no sub-class, plus `NAME::GOLDMAN SACHS ABSOLUTE RET TRCKR INSTL`, the share-class sibling of GSRTX which the set already reads alternatives; the 23 include two ticker twins, `ARBIX` and `JHEQX`, of `NAME::` rows in the same set). The set still leaves unmoved the REIT stocks (`CTRE`, `DOC`, `FBRT`, Kimco, Digital Realty), the non-traded REIT issuers (`ARES INDL REIT`, `FS CREDIT REAL ESTATE INCOME TRUST`), volatility notes and ETNs (VXX and its kind), listed option lines, buffer/outcome/defined-outcome ETFs and notes, and the structured/Hedge rows excluded by name in the proof instance and the worker report, as literally not hedge funds, private funds or real estate funds or as outside the ruling; see surprise row `MDPF_SECCLASS-D1-W67-S2`.

### Amendment 2: the served-mix effect of the 23 liquid-alt lines

Each of the 23 keys reads `structured/Hedge` now and `alternatives` after; none is in the trace (the trace lists only unclassified securities), so the held dollars are `UNREAD` here and the issuer reads them from the compare at signing. In any served mix that holds one of them, its held amount leaves the `structured` sleeve (the Hedge sub-class) and enters `alternatives` with no sub-class; the firm total and the unclassified amount do not move, and the other four classes do not move. The two ticker twins (`ARBIX`, `JHEQX`) and their `NAME::` rows move together, so a position read by ticker or by name lands in one class. `NAME::GOLDMAN SACHS ABSOLUTE RET TRCKR INSTL` and `GSRTX` (NEW, alternatives) now agree. `claim: inferred` for the class of each fund (named by strategy in its name); `3.0.0_SA_CVO` grades it at L9.

### The writers that can touch these keys (counted from the live table)

N = 13 distinct `updated_by` values were read from a consistent full scan of `etf-classifications` this session (10,607 rows): `mdpf-secclass-old-list-reclassify` 5,182; `mdpf-secclass-model` 1,652; `mdpf-secclass-clean-names-v2` 1,359; none 1,087; `rivalfunds-backfill` 635; `mdpf-secclass-fwd15-direct` 278; `seed-script` 177; two `seed-etf-constituents` strings 172 and 41; `mdpf-secclass-remap-b` 20; `mdpf-secclass-s62-ascii-names` 2; `mdpf-secclass-cash-row-r12` 1; `mdpf-secclass-scheduled` 1. The REMAP keys' writers are the model (`mdpf-secclass-model`, `classified_by model`) and the e32 reclassify writer (`mdpf-secclass-old-list-reclassify`); each is a conditional writer that does not overwrite a present key, and this writer's own REMAP condition on `asset_class` fails if any of them moved the row first. A write path outside the repo (an ad-hoc seat script) is not enumerable from here and is not claimed absent. The model runner can still land a NEW key first (it did for `RAL`); the put's `attribute_not_exists(ticker)` then refuses and the row stays as the runner wrote it.

## Both branches (read from the writer's own conditions)

- **Branch A, a NEW key is still absent / a REMAP row still reads its set class.** The put or update lands. Output: `WROTE new=<n> of <n>, remap=<n> of <n>; condition failures 0`.
- **Branch B, a key moved first.** A NEW key now present is listed `REFUSED_PRESENT` at the read and `CONDITION FAILED at write` if it lands in between; a REMAP row whose class changed is `REFUSED_STALE`. Nothing is overwritten; the rest continue; the run exits 1 and the issuer re-reads before re-trying. The pair is re-requested if the new state is not the one named above.

## Rollback per key

The snapshot (`--snapshot`, must not exist yet, written before the first call) holds the NEW key list with the class each was put at, and the full pre-state item of every REMAP key. `s11_rows_write.py --rollback <snapshot.json> --write`:

- **a NEW key** is deleted (`DeleteItem`) only while it still reads `updated_by = mdpf-secclass-s11-rows` AND the class this run put; a key another writer changed is skipped and reported;
- **a REMAP key** is restored (`asset_class`, `sub_asset_class`, `updated_by`, `last_updated` each as the snapshot holds it, or REMOVEd if it had none) only while it still reads `updated_by = mdpf-secclass-s11-rows` AND the class this run set.

The dry form (`--rollback <snapshot.json>`, no `--write`) lists what it would do and asserts `puts=0`. Served bytes rebuilt from the changed rows return at the readers' next runs after a rollback.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-08 ~20:4xZ. I re-ran in the worker tree:
- AC1: S11-ROW-SET ok=True, 106/106, remap=34, rule_rows=43.
- AC2: `new=104 remap=34 refused_present=2 refused_stale=0 puts=0`.
- AC3: HALF-READY.
Merged on box/dell1 @9df203a45d.

**Refused-present keys, read by the issuer (amendment 3):** OXYWS (live equity, set equity) and RAL (live equity, set equity). Both are
no-ops. At write time, any further present key the writer refuses is read the same way. A different class is a re-plan.

**Writers of `asset_class` / `sub_asset_class` on these keys, counted: N = 10.** These are the SC-e-74 half's writers of the row. The
put-on-absence writers (seed, constituents, E_18 scheduled, FWD-10, write-model-rows, CUSIP rows, FWD-9, the e32/e49 runner) cannot
overwrite a NEW row once it is put, nor a REMAP row they did not plan. The e49 leg still running can land a group-B key first. The NEW
put then refuses it as present, which is the case above.

**Both branches:** (a) the condition holds, so the NEW put lands and the REMAP moves from current_class to the set's class; (b) the row
moved since the set was built, so it is refused (present or stale), nothing moves, and the line is re-planned.

**Scope, per Andrew-direct:**
- ~19:0xZ (hedge, private and real estate funds are alternatives) and ~20:1xZ ("1. Approved.": liquid-alt mutual funds to
  alternatives, volatility notes stay structured).
- The 7 arbitrage, event-driven, multi-strategy and managed-futures mutual funds are hedge-fund strategies and are included.
- JHQTX (a seed row) goes to the seed source and is not written here.

## CTO half -- UNSIGNED
