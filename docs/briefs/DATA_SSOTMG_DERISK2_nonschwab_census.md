# DATA_SSOTMG / DERISK-2 — Non-Schwab & Held-Away Account Census (49F)

**TO:** `SCHWAB_SSOT.DERISK-2` (= DATA_SSOTMG PRD TO-5) · **Lane:** 0.4.0_DS_ClientPlatform~B
**Date:** 2026-06-29 · **Status:** COMPLETE — read-only; RAVC2 -> 2.0.0_SA_COO, CC 1.0.0_SA_CTO (PRD input)
**As-of data:** BD silver `2026-06-24` (freshest POPULATED partition; **06-26..06-29 are empty** — the frozen-silver state the PRD §5 flagged). Schwab RPS `date=20260624`.
**Purpose:** bound the residual BD bridge for the Schwab-SSOT cutover (PRD §2, §10 risk, D5 Fidelity decision).

---

## 0. Headline (what bounds the bridge)

- The **non-Schwab universe = 998 accounts / $253.2M** (BD accounts with no Schwab fee-mapping). Matches the prior reverse-ETL chunk-2 grounding (979 / $244.0M @ 06-18) on fresh data.
- Split into the two PRD cohorts via the only available custodian signal (`rep_code`, since **there is no explicit custodian field** — confirmed):
  - **FULLY-NON-SCHWAB (Fidelity / other-custodian / unattributed): 513 accts / $166.3M** — vs Andrew's ~$156M estimate = **+6.6%** (within estimate tolerance).
  - **HELD-AWAY-IN-SCHWAB: 485 accts / $86.9M** (narrow) .. **$124.9M** (broad, incl. fee-mapped-but-unpositioned) — Andrew's ~$109M estimate **sits squarely between the two defensible definitions**.
- **The genuinely irreducible BD bridge is the FULLY-NON-SCHWAB $166M** (no Schwab path exists; needs a Fidelity feed — PRD D5). The HELD-AWAY-IN-SCHWAB cohort is **Schwab-side** (rep_code = the Schwab master `08242234`) and is **~97% live** — it should arrive with the Schwab-SSOT cutover itself, NOT a separate BD bridge.
- **Within the irreducible $166M:** ~$69M is *live* (transacting Fidelity/other accounts that feed BD) and ~$96M shows **no BD transactions** — but for non-Schwab custody **"no BD txn" is a feed-coverage artifact, not economic dormancy** (BD does not receive the transaction feed for held-away / other-custodian assets). See §4 caveat — this is the load-bearing nuance for the D5 decision.

---

## 1. Method & grounding (read-only)

| Step | Source artifact (live S3) | Logic |
|---|---|---|
| Account universe + AUA | `s3://opal-data-bd/silver/allocations/2026-06-24.parquet` (6,811 accts, 1 row/acct, 92 cols) | `account_market_value` = current AUA; account dimension (type, registration, tax_status, rep_code, architect). |
| Schwab-custody flag | `s3://opal-data-bd/gold/dimensions/schwab_bd_account_mapping.parquet` (7,027 rows) | Schwab-custodied := has a non-null `schwab_account_id` (mapping_source = fee_file). |
| Custodian inference (cohort split) | `rep_code` in allocations | `rep_code == 8242234` = the Schwab master account `08242234` (49F's Schwab rep). No explicit custodian field exists (confirmed via 49F_RECONCILIATION_2026-05-01 §5 + this census). |
| Held-away (Schwab, broad) | `s3://opal-data-bd/schwab/silver/rps/date=20260624/data.parquet` (91,200 rows) | Fee-mapped accounts whose Schwab id has **no RPS position** = 450 / $38.0M (held-away / cash-only / closed). |
| Last transaction-activity | `s3://opal-data-bd/silver/transactions/*.parquet` (1,818 daily partitions, each a ~90-day rolling window) | Quarterly-spaced scan (32 partitions @ 75-day stride — windows overlap at 90d => no coverage gaps), 2020-03 -> 2026-06-24; max `trade_date` per account. |

**Why the cohort method is defensible, not invented:** Explore-confirmed the PRD's $156M/$109M are **Andrew's working estimates** (first appearance commit `5b4943f92`, 2026-06-29) — there is **no prior documented split methodology**; DERISK-2 *is* the task to produce one. So this census defines the method, computes the cohorts, and reconciles to the estimates with variance flagged (AC#3).

---

## 2. Cohort reconciliation (AC#3)

| Cohort | Accts | AUA (computed) | Andrew estimate | Variance | Verdict |
|---|---|---|---|---|---|
| FULLY-NON-SCHWAB (Fidelity/other/unattributed) | 513 | **$166.3M** | ~$156M | +$10.3M (+6.6%) | RECONCILES |
| HELD-AWAY-IN-SCHWAB (narrow: non-mapped, Schwab rep_code) | 485 | **$86.9M** | ~$109M | −$22.1M (−20.3%) | bracket-low |
| HELD-AWAY-IN-SCHWAB (broad: + fee-mapped-but-no-RPS-position, 450/$38.0M) | 935 | **$124.9M** | ~$109M | +$15.9M (+14.6%) | bracket-high |
| **Non-Schwab universe (cohort 1 + narrow cohort 2)** | **998** | **$253.2M** | $265M ($156M+$109M) | −$11.8M (−4.5%) | RECONCILES |

**Variance explanation (AC#3):** the held-away figure depends entirely on whether you count Schwab-fee-mapped accounts that hold *no custodied position* ($38.0M) as "held-away." Andrew's ~$109M lands between the narrow ($86.9M) and broad ($124.9M) definitions — i.e. the estimate is sound; the ambiguity is definitional (the mapping boundary), not a data error.

---

## 3. rep_code & account-type breakdown of the non-Schwab universe ($253.2M)

**rep_code (custodian inference):**

| rep_code | meaning | accts | AUA |
|---|---|---|---|
| `No RepCode Assigned` | unattributed / house (largest uncertainty) | 483 | $125.7M |
| `8242234` | **Schwab master** -> HELD-AWAY-IN-SCHWAB | 485 | $86.9M |
| `G44515989` | other-custodian rep (Fidelity-class) | 18 | $20.8M |
| `8345209` | other (single $11.4M PCRA-custodial acct) | 1 | $11.5M |
| `8403355`, `8315598`, `17055299`, `8296224`, `8094433` | other small | 11 | $8.4M |

**account_type (held-away-product nature within non-Schwab):** Insurance $57.7M (103) · IRA $49.0M (236) · Brokerage $37.1M (177) · 401K $30.0M (48) · Trust $26.4M (36) · Corporate $12.1M (9) · Joint $8.0M (44) · RothIRA $5.0M (88) · Annuity $4.0M (4) · LLC $3.8M (2) · TermLife $2.1M (15). The classic "held-away products" (Insurance + Annuity + TermLife + DAF/Charitable) total ~$64M and almost never feed BD transactions (§4).

---

## 4. Live-vs-dormant — the bridge-bounding signal (AC#2)

**Non-Schwab universe ($253.2M):**

| Dormancy (last BD txn vs 2026-06-24) | Accts | AUA |
|---|---|---|
| ACTIVE <=30d | 557 | $153.3M |
| ACTIVE 31-365d | 17 | $0.9M |
| DORMANT >365d | 53 | $5.6M |
| NO BD TXN EVER | 371 | $93.4M |
| **LIVE (txn <=365d)** | **574** | **$154.2M (61%)** |
| **DORMANT / NO-TXN** | **424** | **$99.0M (39%)** |

**Dormancy x cohort (AUA):**

| Cohort | ACTIVE<=30d | 31-365d | DORMANT>365d | NO BD TXN |
|---|---|---|---|---|
| FULLY-NON-SCHWAB | $69.2M | $0.9M | $5.6M | **$90.6M** |
| HELD-AWAY-IN-SCHWAB | $84.1M | $0.0M | $0.0M | $2.8M |

**CRITICAL CAVEAT (grounding-honest, Rule-22):** for **non-Schwab-custodied** accounts, **absence of a BD transaction is a feed-coverage artifact, not economic dormancy** — BD's transaction feed comes from the custodian feeds it ingests, and it does **not** receive transactions for held-away / other-custodian (Fidelity, insurance, annuity) assets. So the $90.6M "NO BD TXN" in FULLY-NON-SCHWAB is dominated by held-away products + unattributed accounts that *cannot* transact through BD by construction — **all 998 are present with a current non-zero AUA in the 06-24 snapshot, i.e. live holdings.** The BD-txn dormancy signal is reliable for the held-away-in-Schwab cohort (Schwab-fed, ~97% active = genuinely live) and for the live Fidelity sub-set ($69M active), but it **understates** activity for the no-feed remainder. Do NOT read "$99M dormant" as retirable bridge — read it as "$99M for which BD-txn cannot measure activity."

---

## 5. Implications for the cutover (feeds PRD §10 + D5)

1. **The held-away-in-Schwab cohort ($87-125M) is not a true BD-only bridge need.** It is Schwab-side (Schwab master rep_code) and ~97% live — it should come across with the Schwab-SSOT data itself once fee-mapping/positions are reconciled. Confirm these accounts appear in the Schwab ACC/RPS feeds at cutover; they do not require the Fidelity bridge.
2. **The irreducible BD bridge = the FULLY-NON-SCHWAB $166.3M** — no Schwab path. This is the real scope of the residual BD dependency and the D5 Fidelity-Data-Delivery decision.
3. **The bridge is NOT mostly dormant** (contra the optimistic PRD §10 framing) — at least ~$69M is demonstrably live, and the ~$90M "no-txn" remainder is held-away product/unattributed that BD cannot measure, not proven-dormant. **Recommendation: do not assume the bridge shrinks to near-nothing on dormancy; size the Fidelity decision against the full ~$166M (with ~$64M of it static insurance/annuity/DAF product that may need a holding-snapshot, not a transaction feed).**
4. **To firm up the split permanently:** adopt the long-standing recommendation `ADVI_49FRECN.006` — ingest an **explicit custodian column** into silver/allocations from the BD bronze feed (today it is rep_code-inferred). That removes the −20%/+15% definitional ambiguity in §2 and the no-RepCode $125.7M uncertainty.

---

## 6. Deliverables (AC#1)

Account-level lists (account id/number/name, relationship, cohort, rep_code, type, tax_status, AUA, cash, last_txn_date, days_since_txn, dormancy, architect, state):

- `docs/briefs/derisk2_census/census_fully_non_schwab.csv` — 513 rows
- `docs/briefs/derisk2_census/census_held_away_in_schwab.csv` — 485 rows
- `docs/briefs/derisk2_census/census_non_schwab_all.csv` — 998 rows (both cohorts)

---

## 7. Grounding (Rule-22) + residuals

- **State (served/live-grounded):** every figure reads live S3 (`silver/allocations/2026-06-24`, `gold/dimensions/schwab_bd_account_mapping`, `schwab/silver/rps/date=20260624`, `silver/transactions/*`) — not source/self-report.
- **Mechanism (source-confirmed):** custodian is rep_code-inferred (no explicit field) — confirmed in `docs/architecture/49F_RECONCILIATION_2026-05-01.md` §5 and re-confirmed here (no string column carries "Fidelity"/"custodian"). The $156M/$109M are Andrew estimates (Explore: commit `5b4943f92`), not a prior derivation.
- **Residuals / INFERRED:** (1) **As-of 06-24** — BD silver is frozen 06-26+; census reflects the last live day. (2) The **no-RepCode $125.7M** is the largest custodian-attribution uncertainty (could include some Schwab-but-unrepped) — flagged, not silently allocated. (3) **BD-txn dormancy understates activity** for no-feed custody (§4) — the honest bound, not a defect. (4) Cohort split is **rep_code-inferred**; ADVI_49FRECN.006 (explicit custodian field) would make it exact.
- **comp-rail:** comp-which (routed) -> pipescript advi-bd (estate) + comp-grep (canonical-doc trace); native Reads; live data-access via boto3 (off-rail per Rule-21 row data-access). No raw repo-grep.
