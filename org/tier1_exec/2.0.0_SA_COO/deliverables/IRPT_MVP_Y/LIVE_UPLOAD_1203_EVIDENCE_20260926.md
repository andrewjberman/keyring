# First live Analysis upload (12.03), NORMALIZED -- K4 evidence

Author `2.0.0_SA_COO~Y`, 2026-09-26 ~14:0xZ.

**Authority:** packet v3 blob `07b7a000`, K4 (CTO `b70ede1756`, CRO `a157c45762`); principal from P 101191; ledger
`irpt-ui-walk-principal-20260926`.

**Principal:** `irpt-uiwalk-1790430787@opal.test`. The password was read by name from SSM into memory and never printed.

**Log:** `LIVE_UPLOAD_1203_20260926_RUN2.json` (this folder), scrubbed.

## Outcome

NORMALIZED. The input is `irpt-normalized-portfolio.v2`:
- total_dollars 12.03: AAPL 10.01 and VNQ 2.02, USD;
- valuation_basis INPUT_VALUES; currency DECLARED_TEMPLATE_CONTRACT;
- security checks: AAPL = "Apple, Inc." (C12), VNQ = "Vanguard Real Estate ETF" (C7974).

## The HTTP calls (denominator 2)

| at (UTC) | request | status |
|---|---|---|
| 13:54:51 | POST `/auth/login` | 200 |
| 13:54:56 | POST `/api/scoped/investor-reporting/analysis/inputs?selected_tenant=cottonwood` (the ONE POST) | 200, state RESOLVING |

There was no second `/analysis/inputs` request. Everything after the POST was read directly from DynamoDB, S3 and the
resident's journal (over SSM).

## Timeline

- 13:54:56Z: the POST answers RESOLVING. `upload_id` `UP-a0046a8a81c2e66a5bb2b1e654d3fc2c5174ac09fc12562cbb46dde2163d864e`,
  `dispatched_at` 1790430900.
- 13:55:02Z: the resident journal on `i-0167fd745ad906a66` logs `IRPT_RESIDENT_POLL handled=1`, the only non-zero poll
  from 13:54:40Z to 13:58:02Z. The service is active.
- 13:55:02Z: the YCharts provider-operation lease row `observed_at` equals this second (see "The one vendor call").
- 13:55:36Z: the NORMALIZATION# row reads NORMALIZED, with `input_id` set.

## The write set, named (K4 retention: all kept)

Table `irpt-requests`, tenant `cottonwood`, 7 rows. The baseline at 13:41Z was UPLOAD# 0, NORMALIZATION# 0 and INPUT# 0
(control: SELECTION# 14, which is 14 after as well). After the run, ARTIFACT# and RETENTION# each count 2 for the tenant,
and both of each belong to this run.

| row | note |
|---|---|
| `UPLOAD#UP-a0046a8a81c2e66a5bb2b1e654d3fc2c5174ac09fc12562cbb46dde2163d864e` | source_lane TEMPLATE_UPLOAD, owner OPAL_GLOBAL, firm cottonwood, home_firm opal-capital |
| `NORMALIZATION#UP-a0046a8a...d864e#21d47c44de4c5caade3b879a6520826391bbf5579cf199fdbd13e4176ed05721` | state NORMALIZED |
| `INPUT#portfolio_99e76df8b63be3bccbaa0903586d46269dc13d7befd25a6b5983460d8444d68a` | the frozen input |
| `ARTIFACT#ART-8485fe3bf549f7c02a3f9b9c6ce9d91d9945a5a66e5b56f0be269c761a4b8be9` | the original's index row |
| `ARTIFACT#ART-390ffa94fb4e6f11f35b6ffaf5a6a35cba957fd8188f4956a30c7cbf4d1a32bd` | the normalized input's index row |
| `RETENTION#RET-8485fe3bf549f7c02a3f9b9c6ce9d91d9945a5a66e5b56f0be269c761a4b8be9` | policy irpt-x10-v1 |
| `RETENTION#RET-390ffa94fb4e6f11f35b6ffaf5a6a35cba957fd8188f4956a30c7cbf4d1a32bd` | policy irpt-x10-v1 |

Bucket `opal-data-irpt`, 2 objects:

| key | version | bytes | sha256 |
|---|---|---|---|
| `irpt/cottonwood/state/original_holdings/ART-8485fe3b.../bb079cbf....csv` | `kKsT2kvuep1c63DjEL9P9kHmsutMIwIn` | 35 | `bb079cbf53aaa2be7ce3fb6beb44e55eaeb0695cd168661d5fb78488a0960ddc` |
| `irpt/cottonwood/state/normalized_portfolios/ART-390ffa94.../99e76df8....json` | `ZkuKydXrjP4jWx8ml7_sd6GLcCWbAKgf` | 4548 | `99e76df8b63be3bccbaa0903586d46269dc13d7befd25a6b5983460d8444d68a` (re-hashed by Y from the downloaded object; equals the input id) |

Queue `irpt-generation`: ONE `resolve_upload` message, consumed (`handled=1`).

**Correction to Y's write-set file @5d70021540:** that file named the S3 objects but not their index and retention
rows. `ArtifactRepository.put` (`reports/repository.py:344-362`) also writes one `ARTIFACT#` row and one `RETENTION#`
reservation per object. Both pairs are listed above and are covered by K4's "rows and objects ... kept".

## The one vendor call

Neither the resident journal nor this log records the GET line itself.

The evidence is the lease row in `irpt-jobs`, key `{tenant: _opal, job: PROVIDER_OPERATION#971ab38a...}`, which is
`ycharts` for the enrolled account (`ycharts/session/resident_session.py:95`):
- `version` 4, `fence` 1;
- `observed_at` 13:55:02Z; `next_allowed_at` 13:55:03Z;
- released (no holder, `expires_at` 0).

This is the session's own bookkeeping row, which already existed. The pre-run `version` was not read, so this record does
not prove that exactly one operation ran from the lease counter alone. The one-operation bound comes from the code path:
`resolve_upload` makes one batched `securities_info` call. It is corroborated by the frozen input's two
`security_checks` entries.

## What this does not prove

- Nothing after hop 3. No submission and no Generate ran (not admitted by K4).
- The portal UI path. This was the API; ~D's walk is separate.
