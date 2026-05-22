# Session Log -- MDPF_ASSETS.011 SmartX <-> Schwab account-match (full session)

**Agent:** 0.4.0_DS_ClientPlatform (DS Base lane)
**Date:** 2026-05-18
**TO:** MDPF_ASSETS.011 (dsbase-smartx-per-account-model-membership-probe), issued by 2.0.0_SA_COO
**Project:** MDPF_ASSETS
**Origin:** Andrew direct -- "see if there is a mechanism through the SmartX backend
to start putting the pieces together on which 49 accounts are in what models."

The session ran Andrew-direct across the day, extending well past the original TO scope
(which COO had pre-cancelled mid-session believing it redundant to the WS-B acceptance).
Andrew kept driving it into the per-account ID join, full-population accuracy, BD
validation, the rigor checks on grain/sleeve/mechanics, and finally the scoping refocus
to Schwab-only canonical. All work below is one Andrew-direct arc.

---

## Outcome

CANONICAL deliverable: `mdpf011_match.py` -- Schwab-only matcher.

Final numbers, full-population (5,286 SmartX accounts, $1,335.5M Opal AUA, vs
Schwab RPS 2026-05-15):
- **RESOLVED: 5,119 / 5,286 = 96.84%   $1,275.2M = 95.48% Opal AUA**
- **Validation (SmartX_holdings_sum vs Schwab_market_value):**
  TIGHT (<=1%) 5,087   OK (1-3%) 29   DRIFT (3-8%) 1   SUSPECT (>8%) 2
  **-> Triangulated <=3%: 99.94% of resolved count, 99.89% of resolved AUA**
  gap distribution: median 0.078%, p90 0.129%, p99 0.760%, max 21.836%
- **Per-account non-Opal AUA discovered:** 399 accounts carry non-Opal positions
  on the same Schwab account, summing to **$120.2M** -- the WS-A non_model_aua
  residual at account grain, Schwab-canonical.

Brokerage account number derivation: `schwab_account_id.lstrip('0')` ==
BD `original_account_number`. Verified earlier in the session 73/76 against
live BD `silver/allocations`.

---

## Phase 0 -- absorb

Read SXPL_RESTIN design brief (`docs/briefs/smartx-rest-integration-design-20260515.md`)
+ SXPL_RESTIN.001 per-model matrix + WS-A contract (`docs/architecture/MDPF_ASSETS_WSA_CONTRACT.md`).
Identified candidate up-front: `enterprises/allocations?modelid=` (design brief
section-6.2 "account-level allocations into the model"; .001 had only depth-shaped
the schema, never confirmed account-grain or an account identifier).

## Phase 1 -- membership probe

`enterprises/allocations?modelid={modelId}` x 7 (`opal7` Manager ROPC JWT,
SXPL_RESTIN auth, no new provisioning). All 200, account-grain confirmed.
**Open-status value sum across 7 models = $1,360.24M vs WS-A reference
$1,360.27M (-0.00% delta).** 6,849 open allocations.

## Phase 2 -- the account-number permission wall

The brokerage account NUMBER is permission-walled on `opal7`. Probed:
`accounts/{id}` -> 401 every variant; `enterprises/accounts` -> 401
"opal7 is not an administrator and does not have access to [49 Financial
enterprise]"; `users/access.accountAccess` -> []; `allocations/{id}` -> 400
leaks `"AccountId 'c103c702-...'"` (the SmartX-internal account UUID, distinct
from allocationId, but Andrew-confirmed useless cross-system -- not a join key).
HAR (`~/Downloads/portal.managedaccounts.io.har`) mined for account endpoints:
none -- the manager portal itself never queries account detail.

## Phase 3 -- holdings-fingerprint bridge (sample feasibility)

Andrew chose holdings-fingerprint as the no-new-access path. v1 -> v2 -> v3
matcher progression on an 80-account sample:
- v1: no Schwab tax-lot aggregation -> 0/60 match.
- v2: aggregate ULN to (account,ticker) + exact-set match -> 41/75 = 54.7%.
- v3: switch to RPS (5,743 accounts, native position grain, $1,590.6M) +
  quantity-vector matcher with margin -> **76/80 = 95.0% unique**.

Decisive root cause: Schwab ULN is tax-lot grain (one row per purchase lot);
RPS is consolidated position grain. RPS row-0 == ULN row-0 reconciled per-account.

## Phase 4 -- Schwab -> BD leading-zero key verified

Schwab `account_id` 10-digit zero-padded; BD `silver/allocations.original_account_number`
8-digit bare. **`schwab_account_id.lstrip('0')` matched BD original_account_number
for 73/76 of probe-resolved accounts** -- exactly Andrew's "couple zeroes on the
front" relationship.

## Phase 5 -- initial finding brief + persistence

Brief: `docs/briefs/mdpf-assets-011-smartx-per-account-model-membership-probe-20260518.md`
(commit `292d2ef84`). Methodology + probe scripts persisted under MDPF-owned
tree at `data/mdpf/scripts/probes/` (commit `5cc17e482`):
- `README.md` -- 7-step methodology
- `mdpf011_smartx_account_probe.py` -- backend probe (the membership + permission wall)
- `mdpf011_fingerprint_probe.py` -- 80-account feasibility

Andrew-direct: DELETE the archived fuzzy matcher at
`data/black_diamond/archive/integration/build_schwab_bd_account_mapping.py`
(fuzzy market-value+Levenshtein; contradicts the deterministic leading-zero key
proven here). Routed to COO -> DT 0.4 removed it (`51059ea69`).

RAVC2 to COO sent. COO subsequently reconciled their stale ".011 cancelled"
view -- summary now records ".011 ran Andrew-direct to a YES/YES close --
account-join solved."

## Phase 6 -- full-population match

`mdpf011_full_match.py` (commit `33e9305b0`) -- resumable holdings puller +
matcher, token re-mint, incremental cache. Initial design at 3.2 s/call (the
SXPL_RESTIN-asserted "20 req/min per SmartX agreement") -> 4.6 hr estimate
for 5,209 holdings calls.

Andrew pushed on the throttle. **Controlled ramp test** (20 -> 60 concurrent
requests against `accounts/{id}/holdings`): **15-26 req/s sustained, zero 429s,
zero Retry-After.** The "20 req/min" was a docstring-attested config assumption
never empirically verified -- off by ~50-75x. Rewrote pull as
`ThreadPoolExecutor(max_workers=20)` (commit `5c73662c6`); **5,209 calls in
~3 minutes** instead of 4.6 hr.

Roster caching (commit `15819424a`) -- subsequent matches are zero SmartX
API calls; the cached 2026-05-18 SmartX snapshot is the frozen reference.

**Full-population result vs Schwab RPS 2026-05-08 (10-day stale):**
5,002 / 5,286 = 94.63% count, $1,231.6M / $1,334.2M = 92.31% AUA.

## Phase 7 -- fresh Schwab data + re-match

Coordinated AE 0.6.1 to upload + convert the missing Schwab RPS files
(20260511..20260515 raw -> silver). Canonical silver landed at
**`s3://opal-data-bd/schwab/silver/rps/date={d}/data.parquet`** (the
post-BUCKDR migration path; raw still at `s3://opal-data-schwab/01_raw/CRS{d}.RPS`).

`mdpf011_rematch.py` (cache-only re-match, commit `9b694ba95` + ruff fix
`7f714c127`) supports both silver and raw-parse fallback. Result vs Schwab
**5/15 (3-day stale):** 5,109 / 5,286 = **96.65% count, 95.04% AUA**
(EXACT 5,063 / VECTOR 46 / NO_MATCH 59 / AMBIGUOUS 108 / CONFLICT 8 /
EMPTY 2). Date-gap collapse drove EXACT +189, AMBIGUOUS -89, CONFLICT -14.

## Phase 8 -- BD allocations as third-source validator (research)

`mdpf011_bd_validate.py` (research artifact, commit `11c5d51e8`, refactored
`286b67bf0`) -- explored BD `silver/allocations.account_market_value` as an
INDEPENDENT third valuation source keyed by `original_account_number`.

Initial run flagged 439 "suspect" matches at >8% gap to BD value. Diagnostic
on the suspects revealed: **SmartX `accounts/{id}/holdings` returns the FULL
custodial account holdings** (Opal + non-Opal), not just the Opal sleeve. The
gap between SmartX-roster-value (Opal-only) and BD-account-market-value
(whole custodial) IS the per-account non-Opal AUA -- not a false-positive
match. The matches themselves were correct; the validation metric was wrong.

Refactored to use full holdings_sum vs BD (correct triangulation). 95.21%
count / 96.94% AUA triangulated; 130 BD_ABSENT, 48 actual suspects >20%.

## Phase 9 -- rigor pass (Andrew-driven, "we have to know for sure")

Definitive checks on three sharp questions:

**Q1 -- Is SmartX `account.id` full custodial or a sleeve?** Remainder test:
`(Schwab_market_value - matched_SmartX_holdings_sum) / Schwab_value` across
all 5,115 resolved -- min -0.218, p5 -0.0014, median -0.0008, p95 -0.0001,
max +0.094. **Only 1 of 5,115 matched Schwab accounts has > 5% remainder.
ZERO have > 20%.** Conclusion: SmartX `account.id` = the full custodial
Schwab account. Resolved.

**Q2 -- Are unresolved SmartX accounts sleeves of already-matched parents?**
Earlier heuristic (subset by ticker) said 337 of 414 unresolved were sleeves
of matched parents. **Strict remainder test: 0 of 414** unresolved match a
matched-Schwab remainder within distance. The 337 was a false positive --
Opal-model accounts share the same ticker set so subset-by-ticker is plentiful
even when coincidental. **The 167-171 unresolved SmartX accounts are NOT
hidden sleeves of matched parents** -- they are genuinely outside the
matchable surface (not in Schwab RPS, drifted, or empty $0).

**Q3 -- Match mechanics, CUSIP-aware?** Fingerprint key per account: sorted
multiset of `(uppercase normalized ticker, round(quantity, 0))`. Schwab side:
RPS `ticker` + `quantity_settled`. SmartX side: `accounts/{id}/holdings.symbol.ticker`
+ `quantity`. **CUSIP is NOT used as the join key.** SmartX occasionally
surfaces a CUSIP in its `ticker` field when the security's company name is
unknown -- **45 accounts / $3.85M / 90 distinct cusip-like tickers, 90 of
which are in Schwab.cusip but 0 in Schwab.ticker**. Without translation
those would miss. Wired CUSIP fallback (commit `286b67bf0`): build
`cusip -> ticker` map from Schwab RPS, translate SmartX symbols before
fingerprinting.

**Variance decomposition (the punchline):**
- SmartX(5/18) vs Schwab(5/15) gap: median **0.078%**, p90 0.130%, p99 1.388%.
- Schwab(5/15) vs BD(5/14) gap: median **2.381%**, p90 3.152%, p99 19.739%.
- **The 4.79% "validation gap" against BD was BD-vs-Schwab pricing/valuation
  noise, not match noise.** The match itself is essentially perfect where
  it lands.

## Phase 10 -- canonical refocus to Schwab-only (Andrew-direct)

Andrew-direct: drop BD from the canonical model-portfolios pipeline. BD has
known 49F data-quality issues (temporality, missing transactions); the
variance decomposition proved BD adds 2.4%-median noise vs Schwab. Domain
is Schwab-exclusive for 49F model portfolios; SmartX <-> Schwab already
agrees to 0.08% median -- the match is its own validation.

`mdpf011_match.py` (commit `4f631c309`) -- CANONICAL Schwab-only matcher.
Cache-only, CUSIP fallback, EXACT + VECTOR + VALUE_TIEBREAK (Schwab value),
Schwab-based conflict resolution, validation tiering by SmartX-Schwab gap,
per-account non-Opal AUA via Schwab. Validation tiers: TIGHT <=1%, OK 1-3%,
DRIFT 3-8%, SUSPECT >8%. README updated to mark `mdpf011_match.py` canonical
and `mdpf011_bd_validate.py` as a research artifact (the investigation that
surfaced BD issues and led to the scoping decision).

Final canonical numbers in the Outcome section above. 99.94% of resolved
triangulate <=3% to Schwab; gap p99 0.76%.

---

## Files

### Committed -- `data/mdpf/scripts/probes/` (MDPF-owned, persistent)

| File | Purpose | First commit |
|------|---------|--------------|
| README.md | Methodology + script index + final result table | `5cc17e482` -> `4f631c309` |
| mdpf011_match.py | **CANONICAL** Schwab-only matcher | `4f631c309` |
| mdpf011_full_match.py | One-time holdings puller (concurrent, ramp-tested) | `33e9305b0` -> `5c73662c6` -> `15819424a` |
| mdpf011_rematch.py | Earlier cache-only re-match (basic EXACT+VECTOR) | `9b694ba95` -> `7f714c127` |
| mdpf011_bd_validate.py | Research artifact -- BD third-source validation | `11c5d51e8` -> `286b67bf0` |
| mdpf011_smartx_account_probe.py | Backend probe -- membership + permission wall | `5cc17e482` |
| mdpf011_fingerprint_probe.py | 80-account feasibility probe | `5cc17e482` |

### Committed -- `docs/briefs/`

- `mdpf-assets-011-smartx-per-account-model-membership-probe-20260518.md` (`292d2ef84`)
  -- the finding brief: verdict, mechanism, BD-join assessment, WS-B build spec.

### Workspace-root, NOT committed (carry real 49F account data)

- `mdpf011_smartx_holdings_cache.json` -- 5,286 accounts' holdings, 31.6 MB, frozen 2026-05-18
- `mdpf011_smartx_roster_cache.json` -- account -> Opal AUA + custodian, 542 KB
- `mdpf011_match_result.json` -- latest canonical match output
- `mdpf011_bd_validate_result.json` -- BD validator output (research)
- `mdpf011_fingerprint_result.json` -- 80-account feasibility output
- `mdpf011_probe_result.json` -- initial backend probe output
- `mdpf011_full_match.log` -- background-run log

### S3 paths consumed (read-only)

- `s3://opal-data-bd/schwab/silver/rps/date={YYYYMMDD}/data.parquet`
  -- CANONICAL Schwab RPS silver (post-BUCKDR; converter authored by 0.6.0_AE_PartnerETL,
  conversion run by AE 0.6.1 during this session for dates 20260511..20260515).
- `s3://opal-data-schwab/01_raw/CRS{YYYYMMDD}.RPS`
  -- raw Schwab RPS (`mdpf011_rematch.py` raw-parse fallback when silver lags).
- `s3://opal-data-bd/silver/allocations/{YYYY-MM-DD}.parquet`
  -- BD allocations (research only; out of canonical scope post Phase 10).
- `s3://opal-data-schwab/silver/scripts/convert_schwab_rps_to_parquet.py`
  -- the canonical Schwab RPS converter (referenced when raw-parsing).
- AWS Secrets Manager `smartx/credentials/{username,password}`
  -- SmartX ROPC creds (`opal7`, Manager role).

### Deleted this session

- `data/black_diamond/archive/integration/build_schwab_bd_account_mapping.py`
  -- archived fuzzy matcher (market value +/-1% + name Levenshtein). Wrong methodology.
  Deletion routed Andrew -> COO -> DT 0.4 (commit `51059ea69`).

---

## Commits (chronological)

| Commit | Description |
|--------|-------------|
| `292d2ef84` | brief + initial session log |
| `5cc17e482` | methodology + probe scripts persisted |
| `33e9305b0` | full-population matcher (initial, 4.6 hr serial design) |
| `5c73662c6` | concurrent holdings pull (4.6 hr -> ~3 min, ramp-tested) |
| `15819424a` | roster cache -- zero SmartX API on re-runs |
| `9b694ba95` | rematch.py (cache-only re-match across any Schwab date) |
| `7f714c127` | rematch.py ruff fix (E741) -- prior commit had ds-commit-gate masked by `\| tail` |
| (DT)  `51059ea69` | archived fuzzy matcher deleted (DT 0.4) |
| `11c5d51e8` | BD validator initial (research) |
| `286b67bf0` | CUSIP fallback + 3-source variance decomposition |
| `4f631c309` | mdpf011_match.py CANONICAL Schwab-only + README scope update |

---

## Cross-pod coordination (MCP messages)

| To | When (Z) | Purpose |
|----|---------:|---------|
| COO 2.0.0 | 17:10:34 | ACK MDPF_ASSETS.011 GO |
| COO 2.0.0 | 18:57:22 | RAVC2 -- MDPF_ASSETS.011 YES/YES close (account-join solved) |
| DS~A (shared inbox) | 19:03:16 | WS-B handoff -- build spec from brief section-6 |
| COO 2.0.0 | 19:03:27 | Methodology persisted + DELETE the archived fuzzy matcher |
| DS~A (shared inbox) | 19:04:54 | DS~A handoff retry (subject-tagged for ~A lane) |
| COO 2.0.0 | 19:05:03 | Reconcile -- ".011 cancelled" stale vs Andrew-direct extension |
| AE 0.6.1 | 19:14:26 | Heads-up -- consume the silver/rps partition once it lands |

State by end of session: COO summary updated to ".011 ran Andrew-direct to a
YES/YES close -- account-join solved" -- reconciliation accepted.

---

## Compiler Tools

| Tool | Result |
|------|--------|
| `comp-*` graph tools | N/A -- external-backend feasibility probe (SXPL_RESTIN .001 / MDPF .002/.003 precedent), not a pipeline-graph trace. Documented per the TO mandate phase 1. |
| `comp-iam` | N/A -- read-only probe, no new AWS surface. Reads existing `smartx/credentials/*` Secrets Manager entries + read-only S3 reads of `opal-data-schwab` / `opal-data-bd`. Documented per the TO mandate phase 3. |

---

## Process notes for the record

- `ds-commit-gate.sh` chained with `| tail -3` masks the gate's non-zero exit code
  (the pipe's exit is `tail`'s = 0). Caused one commit with 2 ruff E741 errors
  (`mdpf011_rematch.py`); fixed in the next commit. Won't pipe gate output again
  via `| tail` -- it has to surface its own exit.
- SmartX "20 req/min per SmartX agreement" config assumption was empirically
  off by 50-75x (ramp-tested 15-26 req/s zero 429s). Documented in
  `mdpf011_full_match.py` CONCURRENCY const comment. Memory feedback parallel
  to the existing "docstring-attested API constraint is an assumption" pattern.
- BD `silver/allocations` is account-grain (1 row per account); no model
  membership field (`investment_strategy_name` all single-valued
  "No Investment Strategy Defined"). The validator value is BD's
  `account_market_value`, which the variance decomposition showed differs
  from Schwab by ~2.4% median -- BD has known 49F data-quality issues
  (temporality, missing transactions). Hence Phase-10 scope refocus.

---

## Next Steps

| Recipient | Item |
|-----------|------|
| **DS~A (WS-B)** | Build on `mdpf011_match.py` -- fold the canonical Schwab-only matcher into `data/mdpf/scripts/feeders/wsb_49f_smartx_model_aua.py`. `model_aua_positions.account_id` becomes the BD `original_account_number` (`schwab_account_id.lstrip('0')`); provenance columns: SmartX `allocationId` + `account.id` + match tier. Brief section-6 + the probes README are the build spec. |
| **DS~A / WS-E** | Per-account non-Opal AUA discovery (399 accounts, $120.2M, Schwab-canonical) feeds WS-E's `non_model_aua` residual at ACCOUNT grain -- richer than the firm-level scalar in the original WS-A contract. |
| **COO 2.0.0** | All RAVC2s complete. No follow-up actions outstanding. |
| **AE 0.7.0** | Chain #2 INFGRO.007/.002/.009 verification still pending (orthogonal to this TO). |
| **Self** | Standing by for Chain #2 ping or further Andrew-direct work. |
