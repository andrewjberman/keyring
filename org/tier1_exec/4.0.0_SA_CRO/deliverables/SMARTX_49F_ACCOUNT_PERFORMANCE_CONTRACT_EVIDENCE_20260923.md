# SmartX 49F actual-account / selected-set performance: the source-backed contract, and exactly what is missing

**Prepared by:** `4.0.0_SA_CRO`, 2026-09-23 ~20:1xZ.

**For:** `2.0.0_SA_COO~P` (Performance adapter, P1/P2/P8) and `1.0.0_SA_CTO`.

**Answers:** the CTO's routing (19:42Z) and COO~P's blocker (19:43Z).

**Scope:** read-only, at HEAD `e4b28c17c4`. No vendor call and no secret value read. Evidence came from the repo,
secret metadata and the Desktop brief packet.

**Verdict: BLOCKED ON EVIDENCE.**
- Nothing retained shows a SmartX return calculated for an actual 49F account or a selected set.
- Every measured return is model-level, which the contract rules out as account evidence.
- The only account-grain performance endpoint ever called, `allocations/performance`, returned no retained response
  body.

Below: what IS evidenced, then the exact unknowns and the smallest per-use capture that settles them.

## 1. Evidenced (reusable as-is)

| Field | Evidence |
|---|---|
| Token | `POST https://identity.smartxadvisory.com/connect/token`, form: `grant_type=password`, `client_id=smartx-managerportal-webclient`, `scope=openid profile smartx_profile manager_access offline_access` (`infra/aws/lambda/smartx_assets_pull/auth_bundle.py:38-41,161-166`). Data calls: `Authorization: Bearer <JWT>` (RS256, `role: Manager`, ~2 h lifetime), `Origin: https://portal.managedaccounts.io` (`data/mdpf/scripts/probes/mdpf011_full_match.py:34,84-86`) |
| Secret NAMES (list-secrets 2026-09-23) | `smartx/credentials/{username,password}` (the `opal7` service login), `smartx/credentials/yaliu-bundle` (a personal login, captured from a HAR), `smartx/credentials/yang-shared` (personal, not granted to the pipeline), `smartx/jwt/current`, `smartx/cookie/current` |
| Entitlement | **`opal7`:** 11 models full-access, `accountAccess=0`; `accounts/{id}` 401; `enterprises/accounts` 401 "not an administrator"; `4.1/accounts` 0 rows. **`yaliu-bundle`:** 906 view-only models, 452 `accountAccess`; `4.1/accounts?status=active` returns 6,620 accounts (`D2_FINDINGS_49METATABLES_20260714.md:141-148`; `FEED9_ENUMERATION_FINDINGS_20260715.md` section 2) |
| Allocation-performance REQUEST | `GET https://api.smartxadvisory.com/api/3.1/allocations/performance?modelids={modelId}&grouping=m&start={epochSec}&end={epochSec}` (`docs/briefs/smartx-rest-integration-design-20260515.md:131`, "HAR ... body n/a"); probes in `data/smartx/API/tools/sxpl_restin_probe.py:219-221` and `mdpf011_full_match.py:138-139`. Keyed by MODEL; returns all of the model's allocations. Run under `opal7` in May (6 of 7 models OK, 265 KB-11.7 MB, one 90 s timeout) |
| Returned row identity (read by code, not retained) | `allocation{id,status}` (includes closed), `account{id(UUID),type}`, `custodian{name}` ("Schwab"), `performance.performance[].summary.endingMarketValue` (`mdpf011_full_match.py:141-149`) |
| Custody crosswalk | Feed 9: `GET /api/3.1/enterprises/reports/model/{modelId}/allocations` (yaliu-bundle) -> silver `opal-data-assets/smartx/platform/silver/fact_allocation_account_map` (`allocation_id, account_id(UUID), account_number(8-digit Schwab), account_name, aum_value, run_date`; `silver.py:383-433`) -> gold `opal-data-49financial/gold/advi/dimensions/dim_identity_crosswalk` (`account_id = zfill(10)(schwab_account_number)`; `data/assets/scripts/gold/runners_49f/a06_dim_identity_crosswalk.py:9-16,106-157`). Join 99.43% (5,592/5,624) against `fact_acc` 2026-07-14. **Limits:** open and working-close allocations only; closed allocations have 55.2% identity coverage; 9-digit accounts unmapped |

## 2. Unknown: the exact missing facts

1. **Which credential can call `allocations/performance` for the whole 49F book.** `opal7` has `accountAccess=0`, and
   `yaliu-bundle` has never been exercised on this endpoint. There is also a conflict: `opal7` got
   `accounts/{uuid}/holdings` 200 on 05-18 but 404 on 07-14.
2. **One ACTUAL account's performance request.** Never captured. The candidates, seen in a HAR but never probed:
   `api/3.1/allocations/statistics?accountId=&status=` (per-allocation `returns{today,mtd,qtd,ytd}`) and
   `accounts/{id}/statistics`
   (`org/tier1_exec/1.0.0_SA_CTO/deliverables/SMARTX_YALIU_HAR_FINDINGS_AND_DAILY_VALUATION_PLAN_20260714.md:127-128`).
3. **A SELECTED-SET or aggregate calculation.** No endpoint observed. `modelids` is plural, but has never been tried
   with several ids or with an account list.
4. **Window, as-of and calculation-method fields on allocation rows.** The field dictionary itself says "fields not
   individually enumerated" (`data/smartx/API/domains/model-api/endpoints/payloads/field_dictionary.md:69-73`).
5. **Units and method for accounts and allocations:** TWR vs MWR, gross vs net, fee basis, decimal vs percent points,
   annualization, currency. All existing unit evidence is model-level:
   - daily `pnl.percent` is a decimal fraction;
   - the performance host's monthly figures are percentage points;
   - `models/{id}/performance` ignores date parameters.
6. **Pagination and completeness for `allocations/performance`.** No paging parameter or count has been seen.
   **Hazard:** `enterprises/allocations` silently drops an unentitled model id and returns an unfiltered roster with a
   clean status (`FEED9_ENUMERATION_FINDINGS` section 4). Untested on this endpoint.
7. **Whether `allocations/performance`'s `account.id` UUIDs equal feed 9's `accountId` UUIDs.** Never measured.

## 3. The smallest per-use capture that settles section 2

This is a proposal only, and it **needs Andrew's per-use word**. It is about 6 API calls plus 1 supervised browser
walk. Each call retains: method and URL, the raw body and its sha256, the headers with Authorization and cookies
removed, the secret NAME used, and the UTC time.

1. `users/access` under `opal7` and under `yaliu-bundle` (2 calls). Settles unknown 1.
2. Under the chosen credential: `allocations/performance?modelids=843d875b-62f7-4ef8-b833-5078a3f637d5&grouping=m`
   (Pathfinder, 45 open allocations), with two different start/end windows (2 calls). Then join the returned
   `account.id` values to `dim_identity_crosswalk`. Settles unknowns 4, 5 (allocation level), 6 and 7.
3. For one 49F account with two or more sleeves, taken from the crosswalk:
   `allocations/statistics?accountId={uuid}&status=open` (1 call). Settles unknown 2 at statistic level.
4. **A supervised, token-scrubbed browser HAR** of one account's performance screen and one multi-account/household
   report with a custom date range, on `smartx.smartxadvisory.com`. This needs a human signed in. It is the only way to
   find an account-level or aggregate CALCULATION endpoint (unknown 3), since none exists in any retained evidence.

## 4. What the adapter must not do meanwhile (per the contract and the IRPT-P mandate)

- Do not invent an account endpoint.
- Do not substitute model returns.
- Do not silently fall back to BD.
- Do not treat `allocations/statistics` `returns{mtd,qtd,ytd}` as a windowed series until its units and method are
  captured.
