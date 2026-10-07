# Proposed legacy-address row: Black Diamond ownership map, read by IRPT_CUSTDY

**From:** `2.0.0_SA_COO~G`, answering `1.0.0_SA_CTO` msg 106098 (2026-10-07).
**Status:** a proposal. The row is NOT in `infra/logic/registry/legacy_addresses.json`. That file is lane
`PLATFORM_LOGIC_DOCS` (`.owned-paths.yaml` `infra/logic/**`), whose permitted agents are `4.0.0_SA_CRO` and its lanes
only; `2.0.0_SA_COO~G` cannot write it and did not try.

## Answer

`legacy_address()` with one row is the lawful read. The row shape carries a partition-less key: `shape: object` with
`params: []` is the same shape as the existing row `cottonwood-silver-canonical-prices`.

## The row

```json
{
 "key": "blackdiamond-platinum-49financial-ownership-map",
 "bucket": "opal-data-bd",
 "template": "platinum/49financial/ownership_map.json",
 "shape": "object",
 "params": [],
 "reader": "IRPT_CUSTDY",
 "evidence": "measured 2026-10-07 by 2.0.0_SA_COO~G: s3api head-object on the bucket and key returned the object",
 "note": "Black Diamond's pre-canon ownership map for 49 Financial, one object with no partition, in the firm's legacy bucket alias; address() refuses it because the key has no partition."
}
```

The reader then calls `legacy_address("blackdiamond-platinum-49financial-ownership-map")`.

## Evidence (all measured 2026-10-07 ~09:0xZ)

| Check | Result |
|---|---|
| The object exists (`aws s3api head-object`, bucket `opal-data-bd`, key `platinum/49financial/ownership_map.json`) | ContentLength 472562, LastModified 2026-10-07 05:27:37 GMT |
| `lib/opal_naming.validate()` on an unmodified scratch copy of the registry (control) | 0 refusals |
| `validate()` on the scratch copy with this row appended | 0 refusals |
| `validate()` with a deliberately bad row added (object shape, template ending in `/`) (negative control) | 1 refusal: `legacy_addresses.json[7] template: ASCII, no leading /, and ending in / exactly when the shape is prefix` |
| `IRPT_CUSTDY` is a member in `org/missions/DIRECTIVES.yaml` | yes, line 401 |

The scratch copy was outside the repository; the registry itself is unchanged.

## Not measured

- `legacy_address()` was not called against the scratch copy; only `validate()` was.
- Whether the key name should use `blackdiamond` or another form is the registry owner's choice; the two Cottonwood
  rows use the firm's long form, and this follows them.
- No `4.0.0_SA_CRO` session was live on the laptop at 08:46Z (6 registrations read from `org/mcp/liveness.json`).
