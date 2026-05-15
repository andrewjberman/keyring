# ADVI_TXNAMG.001 — Join-Key Probe + Column-Correspondence Audit + Historical Schema-Parity

**Author:** `0.4.0_DS_ClientPlatform~D`
**Date:** 2026-05-15
**TO:** `ADVI_TXNAMG.001.dsd-join-key-probe-column-audit` (COO-issued 2026-05-15)
**Type:** Read-only investigation. No code ships here.
**Audience:** `2.0.0_SA_COO` (RAVC2), `1.0.0_SA_CTO` (CC).
**Gates:** TO-3 (`ADVI_TXNAMG.003`, the amalgamating writer) — `dispatch_held` until this brief is validated.
**Probe artifacts:** `txnamg001_probe.py` + `txnamg001_result.json` (workspace root, untracked).

---

## TL;DR — the three verdicts

1. **JOIN KEY — CONFIRMED.** REST `id` ≡ Custom-Report `Transaction ID`. 100.00% match (20,212/20,212) on the primary window, and 100% on three of four cross-era windows. `orderId`/`tradeOrderId` are **100% NULL in REST bronze** — not even candidates. The join is `REST.id == CustomReport."Transaction ID"`.
2. **JOIN COLUMN SET — 11 columns carried.** Of the 29 Custom-Report CSV columns: 17 are aliases of REST columns (not joined), 1 is a borderline encoding-variant (recommend not carried), and **11 are genuinely Custom-Report-unique → carried by the join.** Every column classified empirically by value inspection on 20,212 overlap rows.
3. **SCHEMA PARITY — CONFIRMED IDENTICAL.** All 14 sampled `bronze/orion-api/*/transactions.csv` files from 2020-05-26 → 2026-05-14 (backfill-era and daily-era) carry the **identical 29-column header**. No per-era delta. TO-3 needs no per-era reconciliation.

**One scope flag for TO-3 (not a blocker):** the REST spine is *not* a complete superset of Custom-Report history — it excludes transactions on accounts closed before the pull date. See §1.2.

---

## §1 — Join-Key Probe (AC1)

**Method:** Loaded REST bronze `bronze/transactions/2026-05-15.parquet` (1,299,335 rows, full 2020→2026-05-14 history snapshot). Loaded Custom-Report bronze `bronze/orion-api/2026-05-13/transactions.csv` (20,212 rows, all `TransDate`=2026-05-13). Intersected the CR `Transaction ID` set against REST `id`, `orderId`, and `tradeOrderId`.

### 1.1 — Primary window result

| CR `Transaction ID` matched against | Match | Rate |
|---|---|---|
| REST `id` | 20,212 / 20,212 | **100.00%** |
| REST `orderId` | 0 / 20,212 | 0.00% — `orderId` is 100% NULL in REST bronze |
| REST `tradeOrderId` | 0 / 20,212 | 0.00% — `tradeOrderId` is 100% NULL in REST bronze |

**Verdict: the join key is `REST.id == CustomReport."Transaction ID"`.** `orderId`/`tradeOrderId` are entirely empty in the REST payload and are definitively *not* the key. Non-joining rows on this window: **0**.

### 1.2 — Cross-era robustness + the spine-coverage finding

| CR window | CR rows | matched REST `id` | rate | non-joining |
|---|---|---|---|---|
| 2026-05-13 (primary) | 20,212 | 20,212 | 100.00% | 0 |
| 2026-05-08 | 437 | 437 | 100.00% | 0 |
| 2024-06-14 | 138 | 138 | 100.00% | 0 |
| 2023-06-15 | 87 | 87 | 100.00% | 0 |
| 2021-06-15 | 657 | 621 | 94.52% | **36** |

The 36 non-joining 2021 rows were traced: they belong to **4 accounts (87, 100, 331, 759) entirely absent from the REST spine's `accountId` set**. The REST pull (`/api/v1/Portfolio/Accounts/{id}/Transactions`) iterates *currently-existing* Orion accounts, so transactions on accounts closed/merged-out before the pull date never appear in the REST spine. The transaction types are ordinary (Buy/Sell Exchange, Income Reinvested, etc.) and `fkTradeStatus=1` (Complete) — legitimate history, just on now-closed accounts.

**This is not a join-key defect.** The key (`id`) maps perfectly *wherever the account still exists in REST*. It is a **REST-spine-coverage property**: TO-3's left-join (`REST spine ⟕ CR-unique columns`, per PRD §4.1) bases output on the REST spine, so closed-account CR transactions are simply absent from the amalgamated output — not mis-joined. **Flag for TO-3 / PRD:** if the amalgamated silver must preserve closed-account transaction history, the REST spine alone is insufficient and those CR rows would need a UNION, not just a left-join. PRD §4.1 currently specifies left-join-onto-REST-spine; this finding does not contradict it but should be a conscious decision, not a silent drop. Recent-era coverage is 100% (few accounts close); only the deep backfill tail is affected (~5% at 2021).

---

## §2 — Column-Correspondence Audit (AC2)

**Method:** Inner-joined the 20,212-row CR window to REST bronze on `Transaction ID == id`. For every one of the 29 CR CSV columns, compared values against the REST counterpart on all 20,212 overlap rows (dollar/numeric/date-aware comparison). ALIAS ≥ 99% value match; DISTINCT < 70%; PARTIAL between. Ambiguous cases resolved by inspecting actual mismatched values.

> Note — CSV header hygiene: the CR CSV header contains `' Reg ID'` with a **leading space**. The current `convert_orion_api_to_silver.py` `keep` dict maps `'Reg ID'` (no space), so `reg_id` is silently dropped from the deployed CR silver (31 cols, not the 44 the repo code would emit). Immaterial to TO-3 (`Reg ID` is an alias — not carried — see below), but **TO-3 must `.str.strip()` the CR CSV headers** when reading the join source.

### 2.1 — ALIAS columns (17) — NOT joined; REST already carries the value

Confirmed by 100% value match on 20,212 overlap rows unless noted:

| CR CSV column | REST equivalent | Evidence |
|---|---|---|
| `Transaction ID` | `id` | the join key — 100% (§1) |
| `Client ID` | `clientId` | 100.00% |
| `Reg ID` | `registrationId` | 100.00% |
| `Account ID` | `accountId` | 100.00% |
| `Reg Name` | `registrationName` | 100.00% |
| `Reg Type` | `registrationCode` | 100.00% — ambiguous case RESOLVED: same value |
| `AcctCode` | `accountNumber` | 100.00% — ambiguous case RESOLVED: same value |
| `Product Name` | `productName` | 100.00% |
| `Ticker` | `ticker` | 100.00% |
| `TransDate` | `transDate` | 100.00% |
| `TypeDesc` | `trans_type_desc` | the REST silver writer derives `trans_type_desc` from `transTypeId` via the `TRANS_TYPE_DESC` dict — same decoded label (`Buy Exchange`, etc.) |
| `TransAmount` | `transAmount` | 100.00% |
| `NoUnits` | `noUnits` | 100.00% |
| `NAVPrice` | `navPrice` | 100.00% |
| `TranNotes` | `notes` | 100.00% — ambiguous case RESOLVED: same value |
| `Description` | `productName` | ambiguous case RESOLVED: CR `Description` == CR `Product Name` 100% — it is the **security description, a duplicate of Product Name**, NOT a transaction description. (REST `transactionDescription` is a *different* field carrying the txn-type label `Buy Exchange`; CR `Description` is not its alias and not unique either — it dupes `productName`.) |
| `Rep ID` | `rep_id` | REST silver joins `rep_id` from `accounts_v2`; the REST silver already carries it. |

### 2.2 — Borderline: `fkTradeStatus` (1) — RECOMMEND not carried

| CR CSV column | REST candidate | Finding |
|---|---|---|
| `fkTradeStatus` | `status` | 0% raw match — but the **same concept**. CR `fkTradeStatus` is the integer FK (`1`); REST `status` is the decoded string (`Complete`). On the overlap window, `1 ↔ Complete` for all 20,212 rows. REST `status` is the **richer** representation (6 decoded values across full bronze: Complete, Rejected, Pending, Reversed, Pending Corporate Action, Inactive). |

**Recommendation: classify ALIAS — do NOT carry.** REST `status` demonstrably carries the trade-status concept, more completely than the integer FK. `fkTradeStatus` carries no information genuinely absent from REST. This is consistent with Andrew's directive (carry what is *unique*; the integer encoding is not unique). **Limitation:** the probe window contained only `status=Complete` rows, so the full integer↔label map was not observed — but the classification rests on "REST carries the concept," which holds regardless. **TO-3/CTO may override** if the raw integer FK is wanted; this is the single borderline case in the audit.

### 2.3 — CARRY columns (11) — the definitive Custom-Report-unique join column set

Every column below is **100% non-null** on the overlap window and has **no REST counterpart** (verified — see evidence). Per AC5 and Andrew's directive (PRD §1), all are carried regardless of current consumer count.

| # | CR CSV column | suggested silver name | Why genuinely unique (empirical) |
|---|---|---|---|
| 1 | `LName` | `accountLname` | REST has no account-holder name field of any kind |
| 2 | `Activity Category` | `activityCategory` | REST has no activity-category bucket. 6 distinct values seen (`Exchange In/Out`, `Misc Charge`, `Net Dividends/Interest/Gains Withdrawn`, `Dividends and Interest`, `Contributions`) — the 14-bucket Custom-Report taxonomy. Distinct from `transTypeId`/`trans_type_desc`. |
| 3 | `Dwnld Symbol` | `downloadSymbol` | A **distinct identifier**, not an alias of `ticker`: 93.81% equal `ticker` but 6.19% carry a numeric CUSIP (`922908363`, `316067107`) where `ticker` carries the symbol (`VOO`, `FDRXX`). Genuinely different field. |
| 4 | `CreatedDate` | `createdDate` | REST has no record-creation timestamp (`executionTime` is trade execution, semantically different) |
| 5 | `CreatedBy` | `createdBy` | REST `orderCreatedBy` exists as a column but is **100% NULL** (1,299,335/1,299,335). The information lives only in CR (`Fidelity Single Line - IWS 18424`, `spimEclipseCreatePendings`, etc.) |
| 6 | `EditedDate` | `editedDate` | REST has no record-edit timestamp |
| 7 | `EditedBy` | `editedBy` | REST has no record-edit author |
| 8 | `RepName` | `repName` | REST carries `rep_id` (joined from `accounts_v2`) but not the rep name |
| 9 | `CurrentAccountValue` | `currentAccountValue` | REST has no per-transaction account-value snapshot |
| 10 | `CurrentCashValue` | `currentCashValue` | REST has no per-transaction cash-value snapshot |
| 11 | `Managed Account` | `managedAccount` | REST has no managed-account flag on the transaction row |

**Naming:** the amalgamated silver is camelCase Rule-17 (PRD §4.1); camelCase names suggested above for consistency with the REST spine. Final naming is a TO-3 call — the *set* (these 11 source columns) is the binding deliverable.

**Sparsity (expected, Rule-17-correct):** Custom Report 28198 is type-filtered + rep-filtered, so it is a strict subset of the REST row set. The 11 carried columns are populated only on REST rows that have a Custom-Report match and NULL elsewhere. This is correct preservation (NULL = "outside Custom-Report scope") — no business-default `fillna`, per PRD §4.1 and Rule 17.

### 2.4 — Audit completeness

29 CR CSV columns = 17 ALIAS + 1 borderline (`fkTradeStatus`, recommend alias) + 11 CARRY. All 29 classified; every ambiguous case named in the TO (`account_code`/`accountNumber`, `trade_status`/`status`, `tran_notes`/`notes`, `download_symbol`/`ticker`, `reg_type`/`registrationCode`, plus `Description` and `CreatedBy`) resolved by value inspection.

---

## §3 — Historical Schema-Parity (AC3)

**Method:** Read the CSV header (column set) of `bronze/orion-api/{date}/transactions.csv` for 14 dates spanning the full range — backfill-era (bulk-written ~2026-05-08–11) and daily-era.

| Date | Cols | Header vs baseline |
|---|---|---|
| 2020-05-26 | 29 | baseline |
| 2020-06-04, 2021-06-15, 2022-06-15, 2023-06-15, 2024-06-14, 2025-06-16 | 29 | IDENTICAL |
| 2026-05-05, 2026-05-07, 2026-05-08 (backfill-era) | 29 | IDENTICAL |
| 2026-05-11, 2026-05-12, 2026-05-13, 2026-05-14 (daily-era) | 29 | IDENTICAL |

**Verdict: schema parity CONFIRMED.** All 14 sampled CSVs carry the identical 29-column header. The backfill-era files and the recent daily files are schema-identical — Custom Report 28198 has not drifted versions. **TO-3 needs no per-era reconciliation logic.**

---

## §4 — Deliverables to TO-3

The amalgamating writer (`ADVI_TXNAMG.003`, `convert_transactions_to_silver.py`) has a no-ambiguity contract:

1. **Join:** `REST.id` (left) ⟕ Custom-Report `Transaction ID` (right). 100% key fidelity.
2. **Carry these 11 Custom-Report columns** (read from `bronze/orion-api/*/transactions.csv`, strip header whitespace): `LName`, `Activity Category`, `Dwnld Symbol`, `CreatedDate`, `CreatedBy`, `EditedDate`, `EditedBy`, `RepName`, `CurrentAccountValue`, `CurrentCashValue`, `Managed Account`.
3. **Do not carry** the other 18 — 17 are aliases of existing REST columns; `fkTradeStatus` is an encoding variant of REST `status` (CTO may override).
4. **No per-era schema branching** — the CSV schema is uniform 2020→present.
5. **Spine-coverage flag (§1.2):** left-join-onto-REST-spine drops closed-account CR transactions (~5% of deep-backfill rows). If full closed-account history must be preserved, that requires a UNION decision at the PRD/TO-3 level — out of scope for this read-only audit, surfaced for the decision.

---

## §5 — Compiler Tools

| Tool | Run? | Disposition |
|---|---|---|
| `comp-pipescript io` | Not run | Per the TO `<compiler_tools_mandate>` and PRD §5.2: the comp graph does not model `manual_api/` pull scripts or the `silver/transactions/` artifact (documented coverage gap). Empirical S3/parquet/CSV probes are the sanctioned authoritative basis for this investigation TO. |
| Phase 2/3 (commit/deploy gates) | N/A | Read-only investigation — no code commit, no deploy. |

Empirical basis: `boto3`/`pandas` content probes against `s3://opal-data-inf` — REST bronze parquet, Custom-Report bronze CSVs, writer-#2/#3 silver parquet schemas. Reproducer: `txnamg001_probe.py`.

---

## §6 — Acceptance Criteria

| AC | Status | Evidence |
|---|---|---|
| AC1 — join-key verdict + empirical match rate | PASS | §1 — `id` ≡ `Transaction ID`, 100.00% on primary window, confirmed cross-era |
| AC2 — definitive CR-unique join column set, every column classified, ambiguous resolved | PASS | §2 — 11 carry / 17 alias / 1 borderline; all 29 classified by value inspection |
| AC3 — historical/daily schema-parity verdict | PASS | §3 — identical 29-col header across 2020→2026, no per-era delta |
| AC4 — deliverable is a brief, not a code ship | PASS | this document; no code shipped |
| AC5 — carried columns NOT re-gated on "find a consumer" | PASS | §2.3 — all 11 genuinely-unique columns carried per Andrew's preservation directive, zero consumer-gating |

— `0.4.0_DS_ClientPlatform~D`
