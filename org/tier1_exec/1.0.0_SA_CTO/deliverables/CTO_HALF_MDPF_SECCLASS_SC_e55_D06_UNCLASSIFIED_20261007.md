# CTO never-widen half -- MDPF_SECCLASS SC-e-55, 49 Financial's firm mix serves its residual as its own "unclassified" line (d06 twin)

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-07 ~17:1xZ, release mode request 5. **Request:**
`org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/NEVER_WIDEN_HALF_REQUEST_SECCLASS_D06_UNCLASSIFIED_20261007.md` with ADDENDUM 1
(COO half SIGNED), on `secclass-r12-rel-e55` (port `b359a829d7`).

## VERDICT: SIGNED -- the merge, the push's two-key upload (d06 MOVED, the test NEW), and the later twin publish under the release precondition.

## Read by this seat

- **The question the request flagged ("double-show"), answered at DEV fc18e50bc4:** `platinumToComposition` maps every `mix` entry to one
  row, and its literal `unclassified: {count: 0, market_value: 0}` field has NO reader in `src/pages/AdvisorIntelligence/**`. `git grep
  "\.unclassified\b"` there returns 0 lines; positive control `"\.mix\b"` returns 52. The only other hit is the type declaration
  (`types.ts:1558`). The pages already list `unclassified` as a class key (AdvisorAnalytics:671, PartnerAnalytics:87,
  ConsolidatedOverviewPanel:391). So the new `mix.unclassified` renders once, as one row. No double-show.
- **What a reader sees changes only after a repoint.** The portal reads the legacy key (`ADVI_REPOINT.mix_summary.state = held`). The
  twin moves only at a d06 publish, which needs `OPAL_ADVI_PUBLISH_GRANT=1`, after the release precondition's live dry run reads
  `D06-MIX-SUM ok=True`. C-S13's served key is still D_04's, carried to round 10 per msg 219, unless the port retires it.
- The push scope is two 49F `_code` keys: d06 MOVED (64c18614 -> 52b9c843), and the test key NEW and inert (S57's shape; the 49F chain
  entry point references `tests` 0 times, msg 383). `d00_census_out.json` has no S3 target.
- The census edit rides the same branch, so branch B (shape-freeze refusal) is unreachable from the line as committed.

## Conditions

1. A laptop seat reads the d06 key's IsLatest VersionId and ETag before the push and writes them into the ledger entry. No push
   happens on an unread rollback key.
2. The push gate reads exactly d06 (new md5 52b9c843) plus the one NEW test key. Any other key stops the push.
3. **No twin publish without the release precondition:** the live dry run on a laptop seat, `D06-MIX-SUM ok=True`, then acceptance
   1-2 read after the publish.
4. The repoint of `ADVI_REPOINT.mix_summary` from `held` is NOT covered here. It is its own act with its own pair.
