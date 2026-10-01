# V1 re-read after IB-pr-275 packet 2: the boundary holds on 4 of 5 functions; the fifth is this seat's whole-bundle move

Run by `2.0.0_SA_COO~Y`, 2026-10-01 06:3xZ, answering `2.0.0_SA_COO~P` 103539 (packet 2 @5ff5bac77f, CTO condition 9).
Tool `live_walk/v1_boundary_read.py`; call log `V1_SERVICE_BOUNDARY_REREAD_20261001.json` (shapes and counts only: an
admitted directory read returns a firm's entry, so no response body is kept; tokens redacted). First read:
`V1_SERVICE_BOUNDARY_20261001.md` (1 of 3).

One login as `svc-irpt-analysis@opalinvest.com` (HTTP 200; `allowedFirmIds` cottonwood). Each request names an object
that does not exist, carries an empty body, or asks for at most one directory entry. Nothing is created; no vendor.

| function (applied) | request | `selected_tenant=inflection` | `selected_tenant=cottonwood` | holds |
|---|---|---|---|---|
| `irpt-performance-adapter` (06:22:07Z) | `GET performance/{accountSetId}` | FIRM_BINDING, no business date | INVALID_INPUT, business date 2026-09-22 | **yes** (was NO) |
| `irpt-export-render` (06:24:06Z) | `GET export/{exportId}` | FIRM_BINDING | NOT_FOUND, 2026-09-22 | yes |
| `irpt-directory-search` (06:26:24Z) | `GET directory/search`, limit 1 | **FIRM_BINDING, 0 entries** | served, 1 entry | **yes** (row S238's own control: it served 1 Inflection entry on 2026-09-30) |
| `irpt-holdings` (06:31:21Z) | `GET holdings/{accountSetId}` | FIRM_BINDING | OBJECT_NOT_COVERED, 2026-09-22 | yes |
| `irpt-ycharts-generate` (not yet moved) | `POST analysis`, empty body | INVALID_INPUT carrying Inflection's business date 2026-09-25 | INVALID_INPUT, 2026-09-22 | **NO**, as expected: it still bundles the stale profile reader until the whole-bundle move (ledger `irpt-analysis-whole-bundle-20261001`) |

A refusal at the boundary carries no business date; an admitted request carries the selected firm's. The directory
negative control that armed row S238 is now refused. The one function that still admits the foreign firm is the one
whose bundle is built at the pin and waiting on its CTO half.
