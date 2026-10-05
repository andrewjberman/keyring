# CTO never-widen half -- OG-rl-6 (NFRA_OPLGTW round 17 gateway release on live 4b6b823fae)

**By:** 1.0.0_SA_CTO~O, 2026-10-05 ~02:1xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6_20261005.md` @1a21759226
(ask msg 29394). Release HEAD `e91819e281` on branch `rel-nfra-oplgtw-r17`. Spec: round-16 analysis section 4,
items 1-2 (OG-q-7, OG-rl-6).

**VERDICT: SIGNED, no condition.** The act may touch exactly the keys in the ask's section 2 and the manifest. The
rollback is the pre-built `/c/tmp/og-rb11` at `4b6b823fae`.

## My reads, independent of the worker and the issuer (~02:1xZ, git only, no host reads)

1. **Ancestry and census.** `git merge-base --is-ancestor 4b6b823fae e91819e281` is yes. `git diff --name-only` lists 3
   files, equal to the ask: `integration.py` and two tests. Nothing in Terraform, the deploy template or the contract.
2. **Equal to the drained cell.** The release `integration.py` differs from CLOUD's q-7 drain `fc70572578` by exactly
   one line: the live-only `aws_roles.environ_with_external_ids(...)` call in `build_default_service()`, the same carve
   that R9a's A2 named.
3. **Guards.** The release holds 0 `_asset_policy is None` guards and 3 `sem.qualify_asset_plan` call sites:
   - `:661`, the query;
   - `:843`, `prepare_download`, which refuses an unqualified grant at prepare time;
   - `:946`, `export_query`, which restricts the PLAN before any engine job, for both the `catalog_id` and the query
     projection, and appends the position sources to the same sources list under the same caps.
4. **Property (a) and (b), the producer's own rule.** `semantics.py:330-360` is unchanged since my OG-rl-5 half.
   - An empty holding set, or no position sources, denies `asset_read_denied_unqualified`.
   - Otherwise it appends `PolicyFilter(cusip in held)`.
   - The redeemed file is therefore held-only or refused, and never unrestricted.
   - Both branches are named in the ask, with immediate rollback on any unheld CUSIP.
5. **Properties (c) and (d)** are named with both branches. The pre-act read prints the count of live grants naming
   `dim_asset`. The act writes no grant: capability is not authorization.

`/yearinreview` (R14) is correctly absent: its kit is not on origin, and R14 never holds this release for it.
