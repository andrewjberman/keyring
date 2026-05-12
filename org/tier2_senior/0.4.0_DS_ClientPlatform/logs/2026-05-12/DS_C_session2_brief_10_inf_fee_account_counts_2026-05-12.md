# DS~C 2026-05-12 — Brief #10 INF firm-level fee-earning account-count fields

**Agent:** 0.4.0_DS_ClientPlatform~C
**Window:** ~17:35Z 2026-05-12 → ~17:45Z 2026-05-12 (~10 min focused, post-boot)
**Trigger:** DE 0.4.0_DE_ClientPlatform Brief #10 (20260512T171310Z, INFLEC_FIRM_OVERVIEW_FEE_VALIDATION). Companion to DS~D's 49F Brief #9 Part B commit `8bb342de4`.

## TL;DR

Mirrored DS~D's 49F account-grain fee-paying split into Inflection. Single commit `eea448321`, +41/-7 lines, INF_D_04 only. INF_D_00 unchanged per brief's explicit note that its headline is intentionally minimal and INF_D_04 backfills via `header_metrics.json#total`. SHA-MATCH deployed via `safe-deploy.sh` pre-push hook; RAVC2 to DE delivered.

## Brief

Andrew 2026-05-12 directive: Firm Overview "Fee-Paying / Non-Fee-Paying" cards switch from client grain to account grain. Clients can hold a mix of fee-paying and non-fee accounts (taxable + held-away IRA canonical case) — client-grain forces an arbitrary one-or-the-other call. Account grain is unambiguous and aligns with what Books tab L1 already exposes via per-advisor billing block (line ~2878 `fee_earning_account_count` from `book_summary['billing']`).

Portal `5a31973b` (DEV) already relabels the cards + reads new fields with em-dash fallback until DS emits them.

## Files Modified

| File | Change |
|------|--------|
| `data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | 4 edits: `_derive_fee_earning_aggregates` signature + body (line 619+, account_count kwarg + 2 new fields); `build_header_metrics` call site (line 1067) + `header_total` emit (line 1083+); `build_clients_tab_slim` signature + dual-source headline emit (line 3020+, 3069+); `main()` capture header_metrics return + thread into slim. |

INF_D_00 unchanged. Brief's required-change #3 explicitly says: "INF_D_00 doesn't have billing aggregation in scope today — its headline is intentionally minimal and INF_D_04 backfills via header_metrics. For this brief: just confirm INF_D_04's `header_metrics.json#total` is the source slim reads from..." — mirroring that note rather than re-pluming billing into INF_D_00.

## Per-edit detail

### Edit 1: `_derive_fee_earning_aggregates` (line 619)

New `account_count=None` kwarg. After computing `fee_earning_accounts = int(b.loc[fee_mask, 'account_id'].nunique())`, derive `non_fee_earning_accounts = max(0, int(account_count) - fee_earning_accounts) if account_count is not None else None`. None-pass-through when caller omits keeps the function signature-compatible with any prospective future callers that don't need account-grain.

`null_block` extended with both new keys (`fee_earning_account_count`, `non_fee_earning_account_count` = None) so the billing-empty fallback path returns the full 6-key shape rather than a partial dict.

Docstring updated with the methodology note: account grain is unambiguous; client grain ambiguous when a household holds a mix.

### Edit 2: `build_header_metrics` call site (line 1067) + `header_total` (line 1083+)

Pass `account_count=int(headline.get('account_count', 0))` to `_derive_fee_earning_aggregates`. `headline` here is `dashboard.get('headline', {})` from `build_dashboard`, where `account_count = int(holdings['account_id'].nunique())` (line 692) — firm holdings-derived account count, authoritative for the denominator.

Add `'fee_earning_account_count': fee_block['fee_earning_account_count']` + `'non_fee_earning_account_count': fee_block['non_fee_earning_account_count']` to `header_total` immediately after the existing `fee_earning_client_count` / `non_fee_earning_client_count` emit. Keeps the dict shape and ordering parallel to DS~D's 49F D_04 emit.

### Edit 3: `build_clients_tab_slim` signature + headline emit (line 3020+, 3069+)

New `header_metrics=None` kwarg. In the slim headline dict, dual-source:

```python
hm_total = (header_metrics or {}).get('total', {})
...
'fee_earning_account_count':    src_headline.get('fee_earning_account_count',
                                                  hm_total.get('fee_earning_account_count')),
'non_fee_earning_account_count': src_headline.get('non_fee_earning_account_count',
                                                  hm_total.get('non_fee_earning_account_count')),
```

`src_headline` first (forward-compat: if INF_D_00 ever extends its headline, slim picks up automatically without code change), falling back to `header_metrics['total'][...]`. Same dual-source override pattern that DG-1 uses for `total_aua` (line 3046+).

INFCTSLIMFIX (brief #7, commit `12cae4086`) established the precedent of INF_D_00's headline being intentionally minimal and INF_D_04 supplying the canonical values via `header_metrics.json#total` — this commit follows the same pattern for the two new account-grain fields. Brief #10's #3 explicitly endorsed this approach.

### Edit 4: `main()` plumbing

`build_header_metrics(...)` already returns `header` (the full dict, line 1142). Captured the return into `header_metrics`; threaded `header_metrics=header_metrics` into the `build_clients_tab_slim(...)` call.

## Acceptance

Post-next-chain (gold-d or full) Inflection outputs:

```bash
aws s3 cp s3://opal-data-inf/gold/artifacts/summary/header_metrics.json -
# total.fee_earning_account_count: <int>
# total.non_fee_earning_account_count: <int>
# sum == total.account_count = 818

aws s3 cp s3://opal-data-inf/platinum/firm/clients-tab-slim.json -
# headline.fee_earning_account_count: <int>  (mirrored via header_metrics fallback)
# headline.non_fee_earning_account_count: <int>
# sum == headline.account_count
```

Pre-flight expectation per brief: `fee_earning_account_count >= 700` (per-advisor billing sum 521+63+138+10 = 732 floor at line ~2878). Slight drift expected: firm-grain uses billing_dim's is_fee_earning column directly (one row per account); per-advisor uses the same column re-aggregated through account_team join, so any account with null advisor_key is excluded from per-advisor sum but counted at firm grain.

## Compiler Tools

| Tool | Run | Result |
|---|---|---|
| `ds-commit-gate.sh data/orion/scripts/gold/INF_D_04.client_portal_summary.py` | 1× pre-commit | PASS — py_compile + ds-precommit-check + ruff py39 clean |
| `safe-commit.sh --author 0.4.0_DS_ClientPlatform~C` | 1× | Clean (no owned-paths violation, no contamination) |
| `safe-deploy.sh` pre-push hook | 1× | DEPLOYED + verified |
| Manual `aws s3 cp` + `hashlib.sha256` SHA verify | 1× | MATCH `69fe4db9df5103ee429f044594b08968832c74521647f44df1a2d3cb153185ea` |
| `comp-pipescript deployed INF_D_04` | 1× | N/A — comp-pipescript scope is `opal-data-bd` only; not built for opal-data-inf. SHA-256 byte compare used instead. |
| `comp-pipescript io INF_D_04` | 0× | Skipped — pure additive emit; no new column accessed, no portal consumer schema delta beyond DE-confirmed FE shape. |

No owned-paths blocks. No commit gate failures. No SHA mismatches. No pre-commit hook bypasses.

## Deploy Evidence

| Step | Result |
|------|--------|
| Pre-commit gate | PASS (py_compile + ds-precommit + ruff py39 all exit 0) |
| Commit SHA | `eea448321` |
| Author | `0.4.0_DS_ClientPlatform~C <0.4.0_DS_ClientPlatform~C@opal.agent>` |
| Push | `origin/CLOUD` advanced `8bb342de4..eea448321` |
| S3 upload | `s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py` (LastModified `2026-05-12T17:43:17Z`, ContentLength 154157) |
| S3 SHA-256 vs local | MATCH `69fe4db9df5103ee429f044594b08968832c74521647f44df1a2d3cb153185ea` |
| RAVC2 to DE | Delivered `20260512T174429Z_0.4.0_DS_ClientPlatform_C_RAVC__Brief__10_INF_firm-level_fee_earni.md` |

## Next Steps

| Recipient | Item |
|-----------|------|
| **AE 0.6.1 / AE 0.7** | Next gold-d or full chain picks up INF_D_04. Chain #18 already booted at 16:47Z with prior INF_D_04 bundle (`fad5fd9a5` brief #8); brief #10 lands at chain #19 or via solo INF_D_04 SSM. |
| **DE 0.4.0_DE_ClientPlatform** | Post-chain: confirm `clients-tab-slim.json#headline.fee_earning_account_count` + `non_fee_earning_account_count` populate via header_metrics fallback path; em-dashes on the 5a31973b cards clear once outputs redeploy. |
| **DS~C self** | Idle on Brief #10. Watching for COO GO on `ADVI_ROLLUP.SL-P2` (sleeve promote-to-production) — unblocked 2026-05-11 but awaits explicit GO for reader-visible change. |

## Pacing

Single-brief session, ~10 min. Brief was well-scoped from DE with explicit DS~D reference commit (`8bb342de4`) to mirror. No discovery required beyond confirming INF_D_04's data flow (which existing INFCTSLIMFIX comments already documented thoroughly). No retraction; no scope creep; no cross-lane coordination needed (INF_D_00 explicitly out of scope per brief).
