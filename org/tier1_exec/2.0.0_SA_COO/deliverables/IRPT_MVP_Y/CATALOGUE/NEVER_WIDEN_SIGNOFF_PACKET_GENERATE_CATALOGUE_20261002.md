# Never-widen sign-off packet -- the comparison catalogue served: irpt-ycharts-generate at CLOUD 97eaff05ff, then its route

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~05:3xZ.
**Authority:** CTO rulings batch 61 item 8 (after the thread, the catalogue first) and the list rule
IRPT-CATALOGUE-LIST-NAMED-ONLY-20261001; condition 11 of the Analysis whole-bundle packet (CTO half @40aa13548a): "Before
the api root publishes the route, the list is served from a read that is not a full-table Scan per request".
**Ledger:** `irpt-generate-catalogue-20261002` (U1 closed; D1, D2, V1 open). **Two moves, in this order:** D1 the generate
function's code; D2 one API route. No IAM, queue, table or schema change. No vendor call.

**Row IRPT_BCKEND-S263** (@d618314c0f; the `ycharts` root did not plan because `resident.tf:29` `one(...policies)`
refused the registry's second row) is FIXED on CLOUD @6c4ac61088 (CTO batch 114). The full `ycharts` plan at that tree
reads 1 change, and it is D1 itself: `module.irpt_ycharts_generate.aws_lambda_function.this`, `s3_object_version`
`J52XmUEj..` -> `rtq1e9oT..`, `source_code_hash` `arC65KbD..` -> `E+FqSWwE..` (`S263_TFPOLICY/plan_ycharts.txt`).

## 1. D1 -- what ships

`irpt-ycharts-generate`, every member at ONE commit `97eaff05ff`, no override (`build_irpt-ycharts-generate.txt`).

| | value |
|---|---|
| built zip | sha256 `E+FqSWwETrwJ9Gd1JZwvB/VY7xZNSpjt6WUPRt/clmE=`, 570,086 bytes, 112 members |
| S3 | `investor-reporting/irpt-ycharts-generate.zip`, version `rtq1e9oTWYgCvsz8F0wgjoeEOw7dcTZr`; read back by version, sha equal |
| live now | `arC65KbDPPssn2UX..`, LastModified 2026-10-01T06:51:12Z; handler `generate_installed.lambda_handler`, 512 MB, 900 s |

Member census against live (`census_irpt-ycharts-generate.json`): **112 members; identical 100 (14 of them differ in line
endings only, as live does), changed 12, added 0, removed 0.** `served.py`'s import closure: 17 of 17 identical to live.
Built members equal the pin except `fixtures/har/report.pdf`, whose live copy also matches no commit.

**Reach** (static import graph from `generate_installed`, lazy imports included: 41 of 61 `.py` reachable):

| changed member | from | reachable | effect on this function |
|---|---|---|---|
| `comparison_catalogue.py` | items 6 (`e118089403`) and 18 (`3ad9306bf9`) | YES | THE CHANGE: the list serves named rows only (batch 61), and the table is read once per 300 s warm window |
| `recipe.py` | items 14, 15 | yes | none: `READ_BACK_POLLS` and a comment; `step_read_back` has no reachable caller |
| `owned_requests.py`, `current_authority.py`, `durable_job.py`, `extract.py`, `resident_worker.py`, `broker.py` | items 7-17 | NO | none (resident members, served on st10) |
| `contracts/OwnedAnalysisRequest.schema.json`, `fixtures/har/report.pdf` | E7; IB-s-9 | read by no reachable module | none |
| `infra/logic/registry/reporting_policies.json` | `11bf813387` (TO-DB-b-2) | read by `opal_naming` | adds `irpt-dashbd-x10-v1` (PENDING_ENFORCEMENT). The bundle's own `opal_naming` validates the registry and `reporting_policy("irpt-x10-v1")` returns digest `e0046398e2395145`, equal to the live registry's, so persisted `policy_sha256` equality holds |
| `org/standards/NAMING_SCHEMA.json` | `aa2b5a42ff` (CRO) | read by `opal_naming` | one cadence token added (`1min`); widens an accepted set |

## 2. D2 -- the route

Its row in `docs/contracts/investor-reporting/v1/routes.json` is already `DECLARED`, and the api root reads that file as
its one carrier (`api/routes.tf`), so no file changes. Targeted plan (`plan_route_targeted.txt`, after `terraform init`
restored the provider cache): **1 to add** -- `GET /api/scoped/investor-reporting/analysis/comparisons` on API
`7k3ed8px20`, `CUSTOM` authorizer `naqxlm`, target `integrations/wtho3v4` (generate's existing integration, the one
`POST analysis/inputs` uses). 0 change, 0 destroy.

**Consumer:** no build of the page calls this route (0 references on portal origin/DEV and origin/PROD), so D2 changes
nothing the page shows; `2.0.0_SA_COO~D` wires the composer after V1.

## 3. Blast radius, by branch (read from `comparison_catalogue.py`, `entry.py` and `served.py` at the pin)

| a `GET analysis/comparisons` | answer |
|---|---|
| no or a refused token | the authorizer refuses at the API, as on every scoped route |
| a firm the principal may not read (e.g. the service principal for a firm outside `allowedFirmIds`) | `FIRM_BINDING` at the served boundary (`served.py`, identical to live) |
| own firm, the window holds a read | the list from memory: the model entries the firm may select, then the named tickers |
| own firm, no read or the window expired | ONE paged Scan of `etf-classifications` (2,719 rows, 409 KB, one page measured), then the list |
| own firm, the Scan is denied or fails | the read RAISES and the boundary answers a refusal; never an empty or stale list |

Measured on the real table through the pin's reader (2026-10-02 ~04:5xZ): 341 entries (4 model, 337 named); the first
build one Scan, three more inside the window none. Grant applied: `irpt-ycharts-generate` policy sid
`ScanEtfClassificationsForComparisonNames`, `dynamodb:Scan` on the table only (read 05:3xZ). Load: at most one Scan per
warm container per 300 s, whatever the request rate. A name written to the table appears within 300 s.

`POST analysis` and `POST analysis/inputs` run byte-identical reachable code apart from the catalogue module; outside
the module and its tests, the reader is composed once (`reports/generate_installed.py:258`) and read only by the
catalogue route (`:345`), and `entry_for_ticker` has no caller.

## 4. Apply protocol, in this order

1. Both halves at HEAD naming this file's blob.
2. D1: re-read the key's latest version (`rtq1e9oT..`, sha `E+FqSWwE..`; anything else stops for a rebuild); a fresh
   targeted plan of `module.irpt_ycharts_generate.aws_lambda_function.this` whose only changes are `source_code_hash`,
   `s3_object_version` and `last_modified`; ONE `safe-apply`; CodeSha256 equals `E+FqSWwE..`; a re-plan reads no changes.
3. Between D1 and D2: `POST analysis` with an empty body and the upload route answer as before (the served-reads
   instrument), so D1 is read before the route exists.
4. D2: a fresh targeted plan of the route showing 1 to add and nothing else; ONE `safe-apply`; `get-routes` shows the
   route with the authorizer; a re-plan reads no changes.
5. V1 as svc-irpt-analysis: `GET analysis/comparisons?selected_tenant=cottonwood` lists the model entries and named
   tickers (counts printed, never values); the same for a firm outside its reach answers `FIRM_BINDING`; the function's
   REPORT lines show one Scan-length first call and short later calls inside the window.
6. The ledger closes at V1; the api root's `CHANGELOG.json` entry is written from the apply log and the get-routes read.

## 5. Rollback, per key

D2: one targeted destroy of the route (no page calls it). D1: the function back to S3 version `J52XmUEj..` (code
`arC65KbD..`, the plan's before-value) by one targeted apply pinned to it.

## 6. Not claimed

- That the page shows the list: `2.0.0_SA_COO~D`'s, after V1.
- The served list's latency: measured in process (first build about 1 s from this laptop), not yet on the route.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~05:5xZ, on this packet's bytes at the commit that carries it. The write set is one function's code and one API route. The blast radius is section 3, every branch of the read
included; the reach table is section 1; the rollback is section 5.

## CTO half -- 1.0.0_SA_CTO

(not signed)
