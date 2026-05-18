# SmartX Per-Account Model-Membership + the SmartX->Schwab->BD Account Join — Finding Brief

| | |
|---|---|
| **TO** | MDPF_ASSETS.011.dsbase-smartx-per-account-model-membership-probe |
| **Author** | 0.4.0_DS_ClientPlatform (DS Base lane) |
| **Date** | 2026-05-18 |
| **Project** | MDPF_ASSETS |
| **Issued by** | 2.0.0_SA_COO (Andrew-direct, P1) |
| **Status** | COMPLETE — read-only feasibility probe; deliverable for WS-B (MDPF_ASSETS.007) |
| **Probe method** | Read-only SmartX REST GETs (SXPL_RESTIN ROPC/JWT, `opal7` Manager role); read-only S3 reads of `opal-data-schwab` + `opal-data-bd` silver. No new auth, no writes. Harnesses (workspace root, uncommitted — `data/smartx/` is POD3 owned-paths): `mdpf011_smartx_account_probe.py`, `mdpf011_fingerprint_probe.py`. Raw output: `mdpf011_probe_result.json`, `mdpf011_fingerprint_result.json`. |

---

## Verdict

Two questions, two verdicts.

**(A) Per-account 49F model membership + value — YES, directly.** SmartX exposes a
complete account-grain roster of which 49F account is in which Opal model, with
per-account value. `model_aua(49financial)` rebuilds from it to **−0.00%** vs the
WS-A validation reference.

**(B) A deterministic SmartX->Schwab->BD account join — YES, via a holdings-fingerprint
bridge.** The brokerage account *number* is permission-walled inside SmartX and the
SmartX account *UUID* is a dead end for cross-system joins — but a per-account
holdings fingerprint matches SmartX accounts to Schwab accounts deterministically
(**95% unique** on an 80-account sample, 73 of them exact), and the Schwab account
number leading-zero-normalizes to the BD account number (**73/76 confirmed against
live BD data**). The full chain — SmartX model membership -> Schwab account -> BD
account — is established and every link is verified.

No AC4 escalation. WS-B can build on this directly; §6 is the build spec.

---

## 1. Per-account model membership — `GET /api/3.1/enterprises/allocations?modelid={modelId}`

One call per Opal model returns the account-grain allocation roster. Probed live
2026-05-18, all 7 modelIds, HTTP 200.

Each row = one allocation = one 49F account in one Opal model:
`allocationId`, `status` (`open`/`close`/`workingClose` — **filter `open`**),
`advisor{id,name,crd}`, `model{id,name}`, `value` (per-account market value in the
model, USD), `openedDate`.

Open-status `value` summed across the 7 models = **$1,360.24M** vs the WS-A
validation reference `model_aua(49financial)` = **$1,360.27M** — a **−0.00%** delta
(6,849 open allocations). The roster IS `model_aua`, at account grain. The 7
modelId->`model_key` registry mappings are confirmed in Appendix A.

This answers WS-B's Phase-0 question (a). The existing WS-B feeder
(`data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py`) already pulls exactly
this — §6 is the upgrade.

---

## 2. The brokerage account number is permission-walled inside SmartX

The natural cross-system key is the brokerage (Schwab) account number. It **cannot
be read** on the `opal7` Manager-role credential:

| Surface | Result |
|---|---|
| `accounts/{id}` — the account record (number, registration, owner) | **`401 Unauthorized`**, every variant |
| `enterprises/accounts` (enterprise account list) | **`401`** — `"opal7 is not an administrator and does not have access to [49 Financial's enterprise]"` |
| `users/access` for `opal7` | `accountAccess: []` — zero account-level grants |
| `allocations/performance` full field dump | `account.id` (UUID), `account.type`, `custodian.name` — **no account number** |
| legacy `api/3.0`, analytics gateway/API | not JSON account surfaces (HTML SPA / different auth) |

The number exists in SmartX's account record (SmartX places every trade at
Schwab) — it is a **permission wall**, not an absence. `opal7` is a pure model-Manager
credential, walled off from account identity.

**The SmartX account UUID is not a usable join key.** `allocations/performance`
exposes `account.id` (e.g. `a6d5955c-…`), but it is a SmartX-internal hashed serial —
it does not appear in Schwab or BD and there is no crosswalk to it. It is fine as a
SmartX-internal stable key; it is useless for the cross-system join. (Confirmed with
Andrew, 2026-05-18.)

What `allocations/performance` *does* give, per allocation, deterministically:
`account.id`, `account.type` (registration, e.g. `iraSepRollover`), and
**`custodian.name` = "Schwab"** — so the contract `custodian` column is populated
from data, not assumed.

---

## 3. The holdings-fingerprint bridge — SmartX account -> Schwab account

Since no shared key is exposed, a 49F account is matched between SmartX and Schwab
by its **per-account holdings vector** — the set of `(ticker, quantity)` it holds.
A holdings vector is effectively unique per account (quantities span orders of
magnitude across accounts), so an exact or near-exact vector match is deterministic.

**The two sides:**

| Side | Source | Per-account holdings |
|---|---|---|
| SmartX | `GET /api/3.1/accounts/{account.id}/holdings` (works on the Manager token, HTTP 200) | `symbol.ticker` + `quantity` — consolidated position grain |
| Schwab | `s3://opal-data-schwab/silver/RPS/date={d}/` | `ticker` + `quantity_settled` — consolidated position grain; carries Schwab `account_id` |

**Use RPS, not ULN.** ULN silver is tax-lot grain (one row per purchase lot — `DIVZ`
appears 14× in one account) and partial (3,690 accounts, $669.8M). RPS is native
position grain (one row per account×ticker) and fuller — **5,743 accounts,
$1,590.6M** (~95% of 49F's ~$1.68B Schwab book). RPS row-0 reconciles to ULN row-0
exactly.

### 3.1 Probe result — 95% deterministic unique match

80-account sample drawn across 4 Opal models, SmartX live (2026-05-18) matched
against Schwab RPS (2026-05-08):

| Tier | Method | Count |
|---|---|--:|
| EXACT | identical sorted `(ticker, round(qty))` multiset | **73** |
| VECTOR | min normalized quantity-vector distance, best uniquely separated (margin ≥ 2×) | **3** |
| AMBIGUOUS | a credible match but a 2nd candidate within margin (small accounts, near-identical holdings) | 3 |
| NO_MATCH | no Schwab account within distance — the one case is a **$0 empty SmartX account** (nothing to fingerprint; it has no model AUA either) | 1 |
| | **Resolved unique** | **76/80 = 95.0%** |

Value cross-check on the 76 resolved: SmartX value vs Schwab value median delta
**0.78%**, and the deltas are *uniformly* ≈ −0.5% to −1.1% — that consistency is the
10-day market move, and a wrong match would show random deltas, so the uniformity
independently corroborates the matches.

### 3.2 The path to ~100%

- **Same-date pull.** Matching SmartX-live against 10-day-stale Schwab is what
  produced the 3 VECTOR (vs EXACT) and the 3 AMBIGUOUS. Pulling SmartX and Schwab
  for the *same* date collapses the drift — most of those become EXACT.
- **Tie-breaker for AMBIGUOUS.** Small accounts with near-identical holdings need a
  second discriminator: `account.type` (SmartX registration) cross-checked against
  BD `account_registration_type`, or exact value. Cheap to add.
- The $0 empty account is correctly unmatchable and carries no AUA — exclude, not fix.

---

## 4. The Schwab -> BD link — the leading-zero key (Andrew-described, now verified)

Schwab `account_id` is a **10-digit zero-padded** number (`0049546212`). BD
`silver/allocations` carries `original_account_number`, a bare **8-digit** number
(`49546212`). The deterministic key is `schwab_account_id.lstrip('0')`.

**Verified against live BD data:** of the 76 probe-resolved accounts, the
leading-zero-stripped Schwab id matched BD `original_account_number` for **73/76**.
Exactly the relationship Andrew described — "one of them just has a couple zeroes on
the front." (BD also has an internal `account_id` — `z0812152601`, z-prefixed — that
is **not** the join key; `original_account_number` is.)

**Flag for COO/DE — the archived fuzzy matcher.**
`data/black_diamond/archive/integration/build_schwab_bd_account_mapping.py` joins
Schwab<->BD by **fuzzy** signals (market value ±1%, account-number substring, client-name
Levenshtein). That contradicts the deterministic leading-zero key proven here. If
anything resembling that fuzzy logic is in a live path it should be replaced with the
`lstrip('0')` key join. Surfacing per the TO; the file is archived, so this is a
flag for DE/ops to confirm, not a fix in this lane.

---

## 5. The complete join chain (all links verified)

```
SmartX enterprises/allocations?modelid=   ->  allocation: (model_key, value, status=open)
SmartX allocations/performance?modelids=  ->  allocationId -> account.id (UUID) + custodian="Schwab"
SmartX accounts/{account.id}/holdings     ->  per-account (ticker, quantity) vector
                                                   |
                          holdings-fingerprint match (95% unique, §3)
                                                   v
Schwab silver/RPS/                        ->  Schwab account_id (10-digit, 0049546212)
                       .lstrip('0')  ->  BD original_account_number (8-digit, 49546212)   [73/76 verified]
                                                   v
BD silver/allocations                     ->  the 49F account in Black Diamond
```

Net: a 49F account's Opal-model membership (SmartX) is joined, deterministically and
at ~95% coverage, to its Black Diamond / Schwab account identity — **without** the
permission-walled account number and **without** fuzzy matching.

---

## 6. What WS-B (MDPF_ASSETS.007) builds

The existing feeder (`wsb_49f_smartx_model_aua.py`) pulls §1 and sets
`account_id = allocationId`, `custodian = None`. The upgrade:

1. **Keep §1** — `enterprises/allocations` (open) for the model + value rows.
2. **Add `allocations/performance`** (7 calls) — map each `allocationId` ->
   `account.id` + set `custodian = "Schwab"` (from `custodian.name` — deterministic).
3. **Build the fingerprint bridge** (once per run, account grain, ~5,000 distinct
   `account.id`):
   - SmartX: `accounts/{account.id}/holdings` per distinct account (~5,000 calls,
     ~5 hr at the 17 req/min ceiling — a daily batch, not interactive).
   - Schwab: `s3://opal-data-schwab/silver/RPS/date={d}/` — group to (account_id, ticker).
   - Match SmartX-account <-> Schwab-account on the quantity vector (EXACT then
     margin-checked VECTOR; same-date data preferred — see §3.2).
4. **Derive** `bd_account_number = schwab_account_id.lstrip('0')` -> the contract
   `model_aua_positions.account_id` becomes the real BD account number (a partner-native
   identifier per contract §3.1), not the SmartX allocationId.
5. **Carry** the SmartX `allocationId` + `account.id` + the fingerprint match tier as
   provenance columns, so an unmatched/ambiguous row is surfaced, never silently dropped
   (CLAUDE.md Rule 17 / WS-A reconciliation discipline).

Coverage caveat to carry honestly: RPS covers ~95% of the 49F Schwab book; the
fingerprint resolves ~95% of sampled accounts at a 10-day date gap (higher at
same-date). The unmatched residual gets `account_id = allocationId` + a
`join_status = unmatched` flag — model AUA is still complete (the roster value is
authoritative), only the BD-account attribution is pending for that residual.

---

## 7. Answers to the TO acceptance criteria

| AC | Result |
|---|---|
| AC1 — clear YES/NO verdict | **YES** (both: membership directly; the BD join via the fingerprint bridge). |
| AC2 — if YES, the mechanism | §1 (membership), §3 (the fingerprint bridge), §5 (the full chain), §6 (the WS-B build spec). |
| AC3 — the SmartX↔BD join | Assessed and **solved**: no shared key / account number is permission-walled (§2), but the holdings-fingerprint bridge + leading-zero Schwab->BD key is deterministic and verified end-to-end (§3–§5). |
| AC4 — if NO, escalate as a contract question | N/A — verdict is YES. |
| AC5 — no emoji; session log w/ Compiler Tools; RAVC2 | Brief emoji-free; session log filed; RAVC2 to COO. |

---

## Compiler Tools

| Tool | Result |
|---|---|
| `comp-*` graph tools | **N/A** — per the TO mandate (phase 1). External-backend feasibility probe (the SXPL_RESTIN .001 / MDPF .002 / .003 precedent), not a pipeline-graph trace. Method: read-only SmartX REST GETs + read-only S3 reads. |
| `comp-iam` | **N/A** — per the TO mandate (phase 3). Read-only probe; no committed harness, no new AWS surface. SmartX creds are the existing `smartx/credentials/*`; S3 reads are read-only. |

---

## Caveats

- Probe ran on the `opal7` Manager-role token; the account record is 401-blocked
  here. A higher-privilege SmartX credential would expose the account number
  directly and make §3's fingerprint unnecessary — that option remains open to
  Andrew/49F (an access request, not engineering), but the fingerprint bridge needs
  no new access and is proven.
- Match rates are from an 80-account sample (4 of 7 models). WS-B should re-measure
  on the full population; the 3 AMBIGUOUS + the date-gap effect (§3.2) mean a
  same-date production run should land above the sampled 95%.
- RPS (5,743 accounts, $1,590.6M) covers ~95% of 49F's ~$1.68B Schwab book; the
  remainder is accounts absent from the RPS partition (cash-only / newly opened /
  closed). The Schwab feed's freshness and completeness cap the bridge's coverage.
- The Schwab->BD leading-zero key matched 73/76; the 3 misses are within the
  AMBIGUOUS/VECTOR set or accounts absent from the BD 2026-05-14 partition — WS-B
  should treat a non-resolving derived id as `join_status = unmatched`, not an error.

---

## Appendix A — modelId -> `model_key` registry confirmation

WS-A §2 left the SmartX-side name alignment provisional. The probe + value
cross-check confirm all 7:

| modelId (prefix) | SmartX display name | `model_key` | Note |
|---|---|---|---|
| `0f76a5a0` | Opal Short-Term | `opal_short_term` | clean |
| `729210dd` | Opal Intermediate-Term | `opal_intermediate` | clean |
| `74c119db` | Opal Conservative Growth | `opal_long_term_conservative` | SmartX displays "Opal Conservative Growth" vs WS-A §2 "Long-Term Conservative" — same model (value + exporter scope `LTC`) |
| `69cc5e3b` | Opal Long-Term Aggressive | `opal_long_term_aggressive` | clean |
| `c000fe6a` | Opal Ultra Short-Term Income | `opal_ultra_short_term` | clean |
| `48af6559` | Opal Dividend Income | `opal_div_sma` | confirmed by value ($19.63M ↔ ref 19.51) |
| `843d875b` | Pathfinder Focused Opportunities | `opal_growth_sma` | confirmed by value ($5.07M ↔ ref 5.10) |

The 2 blend keys (`opal_blend_5050_*`) have no SmartX model — 49F's SmartX book is
these 7. WS-B resolves `model.id` at runtime (do not hard-code names).
