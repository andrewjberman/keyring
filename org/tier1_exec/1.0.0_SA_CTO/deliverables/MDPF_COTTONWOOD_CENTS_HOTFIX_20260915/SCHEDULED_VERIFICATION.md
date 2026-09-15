# Cottonwood cents hotfix: scheduled Gold proof, publisher pending

Author: `1.0.0_SA_CTO~A`. Observed 2026-09-15 13:28-13:36 UTC.

**The scheduled Gold run healed Cottonwood and Global category views and AUM. Six of the seven named dated families advanced. The full verification leg remains open:** the 13:50 UTC publisher has not yet run, and Cottonwood's standalone dated account-units output still carries value_date2026-09-10.

## Measured run

- Fresh before snapshot13:28:13-17Z; after snapshot13:31:34-38Z, with VersionIds and content hashes. Evidence: `scheduled-gold-1330-verification.json`.
- Request `996aa948-5808-444e-a408-85bb3b1fad7a`, scheduled13:30:36Z to13:31:10Z, duration33430.16ms. All283 log events in that run's observed window:0 SCOPE FAILED,0 [ERROR],0 Traceback. New artifacts declare `_provenance.trigger=scheduled` and process_time13:30:36Z.
- Cottonwood category-views, aum-metrics and account-distribution: value date2026-09-14. Global category-views and aum-metrics:2026-09-14; Global account-distribution: its producer's period2026-09-15. Each is read from content/provenance, not inferred solely from a key or upload time.
- At13:34:20Z the live Lambda is Active/Successful with exact hotfix CodeSha256 `evIYCXURor4V++Ci4HsgwE8zIPZva/BAL+ICaLJIiAE=` and revision `15eda5c8-d1ab-40d3-ac79-3dc0292d4575`.
- Platinum remains at its pre-publisher versions in this observation. No manual invocation or production write was made by this observer.

## Existing standalone account-units gap

The pair builder did write `s3://opal-data-assets/gold/mdpf_revamp/cottonwood/account_units.json` at13:30:49Z, version `tTAbT_v3sMuvYqnea4UnEyniBnEbLNXP`, SHA256 `52440d2deeadf357222fcce6ef38dfbeb80fe37d0910e8c85672a097e8a30dc7`. But the latest canonical dated key remains `portal/gold/mdpf/cottonwood/account-units/2026-09-10.json`, whose body declares assignment_date09-11 and value_date09-10.

I read the exact deployed ZIP. `mdpf_gold_consolidator.py:1181-1184` invokes the pair with staging upload; its dated emit loop at1516-1519 contains only aggregate-aua-timeseries, aum-metrics, account-distribution and category-views. It does not emit standalone account-units. This member is byte-identical to the preserved pre-hotfix ZIP, so the omission predates the whole-cents change.

I downloaded and hash-verified the actual deployed publisher ZIP (CodeSha256 `7X50uR1HrGyeEHZ4FWyHBNwTxt/XXJq5GNmR/eFfWE0=`, revision `9523e457-8aac-4eeb-a23b-154b47076c65`). `lambda_function.py:118` still declares Cottonwood/account-units as an expected R12 extra. Its derive_publish_set and publish path read the latest **canonical dated Gold** key, not the staging sidecar. It therefore cannot carry the new staging units forward by itself. A stale13:50 units result is an inference from these measured writers, pending observation of that run.

Global/account-units remains absent in Gold and Platinum, as measured before and after; nothing was created or deleted. The signed seven-family expectation is not rewritten as six-family success. No code deployment, manual copy or retirement is authorized by this evidence note.

## Unaffected-scope control limit

49 Financial and Inflection naturally created new dated Gold during the same scheduled run: category views/AUM now09-14 and distributions09-15. A before/after daily comparison cannot certify unchanged bytes or attribute those normal changes to the cents fix. The package's existing scope-isolation code is unchanged; the only functional package change remains the approved pair-builder whole-cents comparison. This observation does not pretend to be a same-input counterfactual test.

## Next action

CTO and COO~D received the measured six-of-seven result and dated-emission gap at13:35:04/06Z. Keep ledger L5 open. Observe the scheduled publisher at13:50Z, compare its manifest and exact served VersionIds/content dates with these Gold inputs, then report actual success and remaining gaps. A remedy for the dated standalone account-units emission requires its own concrete scope disposition; this note does not widen the cents-only deployment.
