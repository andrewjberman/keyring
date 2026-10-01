# V1 of the service-principal boundary move (IB-pr-275): 1 of 3 functions holds; 2 of 3 still admit a foreign firm

Run by `2.0.0_SA_COO~Y`, 2026-10-01 05:3xZ, answering `2.0.0_SA_COO~P` 103477 (packet
`org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/NEVER_WIDEN_SIGNOFF_PACKET_IRPT_SERVICE_PRINCIPAL_BOUNDARY_20261001.md`
@d9972c6eb4, section 5 item 4 and CTO condition 8). Ledger `irpt-service-principal-boundary-served-20261001`, leg V1.
Tool `live_walk/v1_boundary_read.py`; full call log `V1_SERVICE_BOUNDARY_20261001.json` (tokens redacted).

## The prints

One login as `svc-irpt-analysis@opalinvest.com` (HTTP 200, token present; `allowedFirmIds` cottonwood). Each request
names an object that does not exist or carries an empty body, so nothing is created and no vendor is reached.

| function | request | `selected_tenant=inflection` | `selected_tenant=cottonwood` | holds |
|---|---|---|---|---|
| `irpt-export-render` | `GET export/{exportId}` | **FIRM_BINDING**, no `business_date` | NOT_FOUND, `business_date` 2026-09-22 | **yes** |
| `irpt-performance-adapter` | `GET performance/{accountSetId}` | **INVALID_INPUT, `business_date` 2026-09-25** | INVALID_INPUT, `business_date` 2026-09-22 | **NO** |
| `irpt-ycharts-generate` | `POST analysis`, empty body | **INVALID_INPUT, `business_date` 2026-09-25** | INVALID_INPUT, `business_date` 2026-09-22 | **NO** |

A refusal AT the boundary carries no business date (the export row shows the shape). On the other two functions the
foreign-firm answer carries Inflection's own business date, 2026-09-25, where Cottonwood's reads 2026-09-22: the request
passed the firm boundary, the operation resolved Inflection's tenant, and only then refused the malformed input. The
service principal is still admitted to a foreign firm on those two functions.

## The cause, read from the deployed bytes (05:3xZ; each zip's sha256 equals the live CodeSha256, 3 of 3)

| function | CodeSha256 | LastModified | bundled `served.py` | bundled `canonical_profile_reads.py` |
|---|---|---|---|---|
| `irpt-performance-adapter` | `XslOsVc9AreO..` | 05:21:01Z | `85f1fd83f0e1`, 4 mentions of `allowedFirmIds` | `3e5868cf2fc0`, **0 mentions** |
| `irpt-ycharts-generate` | `ESedDkLy40en..` | 05:23:14Z | `85f1fd83f0e1`, 4 mentions | `3e5868cf2fc0`, **0 mentions** |
| `irpt-export-render` | `WO5gDeP/fZ4j..` | 05:25:02Z | `85f1fd83f0e1`, 4 mentions | `0ec4a717f2aa` (= CLOUD HEAD), 2 mentions |

`served.py` reads the service principal's limit through the bundled profile reader. On two functions that reader is the
vintage before IB-yr-293 (2704705672): its projection does not name `allowedFirmIds`, so the row comes back without the
attribute, and `served.py` reads an absent attribute as unrestricted. The export function received the reader at CLOUD
HEAD (the packet lists it as an ADDED member) and refuses. This is the whole-bundle rule of CTO rulings batch 61 item 3,
failing OPEN: one module moved against an older sibling.

## What it means

- Not a new exposure: before the move every function admitted the foreign firm (row S238). The move closed it on one of
  three.
- V1 does not hold, so the ledger leg stays open. The repair is the reader at CLOUD HEAD in both bundles:
  `irpt-ycharts-generate` gets it in the whole-bundle move that is this seat's (batch 61 item 2b);
  `irpt-performance-adapter` needs the same from `2.0.0_SA_COO~P`.
- Row S238 and W27 stay closed, as CTO 103464 already ruled.
