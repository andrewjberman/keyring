# AE Brief — inf-portal-advisor-publisher v1.7.54 (orphan-bucket drop)

**Author:** 0.4.0_DS_ClientPlatform~C
**Date:** 2026-05-13
**Commit:** `52478bb3a`
**Lambda:** `inf-portal-advisor-publisher`
**Terraform module:** `infra/aws/terraform/inf-pipeline/`
**Build flag / artifact:** `bash infra/aws/terraform/build-and-upload.sh inf-portal-advisor-publisher` (existing pattern from v1.7.52 / v1.7.53)
**Version label:** v1.7.54 (next after v1.7.53 `dba29da4e`)

## Why

RD 0.4.2 Brief (IWM book.json data gaps) routed via Andrew. Empirical diagnosis of `s3://opal-data-inf/platinum/advisors/inflection_wealth_management/book.json` (generated 2026-05-13T07:11:41Z) found 3 of 4 alleged gaps already populated. The 1 real bug: the Lambda's `_client_list` synthesises a phantom `clients[0]` from IWM's unallocated bucket (19 accounts / $284K AUA / `household_id=null` / `display_name=""` / `relationship_since=null`), which sorts to position [0] by AUA and triggers the FE "Pending DS emit" placeholder on the Newest Relationship card. IWM is the only impacted advisor — peter_lee (201 clients / 0 orphans), patrick_scanlan (73 / 0), joe_brandenburg (small / 0).

## Diff scope

Single function: `_client_list` in `infra/aws/lambda/inf-portal-advisor-publisher/lambda_function.py` (L504-525 pre-fix, L504-534 post-fix). Adds `if _hh_int is None: continue` immediately after the existing `_hh_int = None if (pd.isna(hh_id) or str(hh_id) == 'unknown') else int(float(hh_id))` resolution. Also drops two dead `if _hh_int is not None else None` ternaries on `client_key` and `relationship_since` (unreachable post-fix).

**12 insertions / 2 deletions on one file.** No schema changes, no new fields, no removed fields. `clients[]` shrinks by exactly the orphan row(s) per advisor — IWM goes from 11 → 10 clients in the artifact. `summary.account_count`, `summary.total_aua`, `headline.*`, `composition.*`, `top_holdings.*` are all unaffected (the orphan's $284K stays in those totals because they aggregate from `adv_df` directly, not from `clients[]`).

## Verification (post-deploy)

After your `terraform apply` lands the new Lambda image, fire the next regular chain (or hit the Lambda directly per the inf-pipeline pattern). Then:

```bash
aws s3 cp s3://opal-data-inf/platinum/advisors/inflection_wealth_management/book.json - 2>/dev/null | \
  python -c "
import json, sys
d = json.load(sys.stdin)
clients = d.get('clients', [])
n_orphan = sum(1 for c in clients if c.get('household_id') is None or not c.get('display_name'))
print(f'clients: {len(clients)} (expect 10, was 11 pre-fix)')
print(f'orphan rows: {n_orphan} (expect 0)')
c0 = clients[0]
print(f'client[0]: hh_id={c0.get(\"household_id\")} name={c0.get(\"display_name\")!r} rs={c0.get(\"relationship_since\")}')
# expected post-fix: hh_id=1342 name='Richard L Thompson & Cheryl L Thompson' rs='2026-04-15'
print(f'summary.total_aua: \${d.get(\"summary\",{}).get(\"total_aua\",0):,.0f} (expect ~\$536K, unchanged)')
print(f'summary.account_count: {d.get(\"summary\",{}).get(\"account_count\")} (expect 41, unchanged)')
"
```

Expected post-fix:
- `clients: 10` (was 11)
- `orphan rows: 0`
- `client[0]: hh_id=1342, name='Richard L Thompson & Cheryl L Thompson', rs='2026-04-15'`
- `summary.total_aua: ~$536K` (unchanged)
- `summary.account_count: 41` (unchanged)

Hard sentinel: `clients[0].relationship_since is not None` post-fix.

## Out-of-scope (separate investigations to flag)

1. **19 IWM accounts have `household_id=null` in `account_team`.** Real data-quality gap from INF_C_07 or upstream silver. Not a regression — pre-existing. DS investigation pending; not blocking this fix.
2. **`headline.historical_quarters` 2025-Q4 entry = $1.19.** Caused by `_quarter_ends_from_timeseries` picking the latest-row-on-or-before-quarter-end which lands on a 2025-12-01 row with `total_aua=$1.19` and `account_count=1`. There are 31 rows under $100 in IWM's Q4 '25 timeseries (legitimate reorg-window volatility — accounts being reassigned out of and back into the catchall). Not a fix for this commit; needs RD/Andrew product call on whether the strip should suppress small-magnitude periods or pick median/mode instead of last.
3. **8 of 11 IWM households show $0 current AUA** but valid `relationship_since` dates back to 2023-10. Stale relationships where accounts dropped to zero holdings. Same upstream-data question as (1).

## Sequencing

- DS: pushed commit `52478bb3a` to `origin/CLOUD` already.
- AE: `build-and-upload.sh inf-portal-advisor-publisher` → upload as `v1.7.54` → `terraform plan` (expect single Lambda function change, no IAM/EC2/route changes) → `terraform apply` → tag.
- AE → DS: ACK with build-output ETag + terraform apply timestamp.
- DS: validates next chain run output against the sentinel above; RAVC2 to RD with pre/post numbers.

No layer changes. No new IAM. No new env vars. Drop-in replacement.
