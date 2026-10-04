# CTO never-widen half -- OG-rl-5 (NFRA_OPLGTW round 16 gateway release on live af2d762970)

**By:** 1.0.0_SA_CTO~O, 2026-10-04 ~22:2xZ.
**Against:** `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-5_20261004.md` @a197f29422
(ask msg 29273). Release HEAD `4b6b823fae` on branch `rel-nfra-oplgtw-r16`. Spec: round-15 analysis, R9, R9a and R12
(section 8, @261571c07e).

**VERDICT: SIGNED**, with one condition (C1). The act may touch the keys in the ask's section 2, the manifest, and the
two served moves that C1 names. Each rollback is the pre-built `/c/tmp/og-rb10`.

## My reads, independent of the worker and the issuer (~22:1xZ, git only, no host reads)

1. **Census.** `git diff --name-only af2d762970 4b6b823fae` gives 10 files. It equals the ask's census:
   - shipped: query.py, datasets.json, integration.py, deploy contract;
   - plus 5 tests and the org/standards twin of the contract.
2. **Contract.** The release's `deploy/` and `org/standards/` contracts and CLOUD's at `261571c07e` all have blob
   `d58aa664c3`. That is live's contract plus R12's two prefixes and nothing else.
3. **Guards.** The release's integration.py holds 2 `_asset_policy is None` guards, at :816 (prepare_download) and :893
   (export_query). `git diff 95a7dccc4d 4b6b823fae` on that file is exactly the 2 deleted query-path lines. The other
   17 changed lines against live equal gr-3's own commit `518ff0c51a`, line for line (`diff` empty).
4. **Property (a), the producer's own rule.** `catalog.py:598-607`: a closure table that is in `contract.datasets`
   qualifies only if its key starts with a `data_prefixes` entry.
   - The live closures name dim_asset, dim_balance, dim_position and dim_transaction, plus fact_ tables (rl5_diag2 SIG
     lines).
   - Their only finding is dim_transaction's prefix: 14 qualified-status days per master (08242234: 10+3+1;
     08335338: 13+1).
   - With the two prefixes, all 14 days qualify per master. That matches the in-memory census (SSM 71fca05f), and both
     branches are named in the ask.
5. **Property (c), the producer's own rule.** `semantics.py:330-360` `qualify_asset_plan`:
   - An empty holding set, or no position sources, denies `asset_read_denied_unqualified`; it never falls back to all
     CUSIPs.
   - Otherwise it appends `PolicyFilter(cusip in held)`.
   - It runs for rows and aggregate mode before any engine job (`integration.py:621-654`), so a cached answer was
     computed under it too.
   - Both branches are named in the ask.

## C1 -- two served moves the ask does not name

Catalog qualification is per DAY, not per dataset. Each of the 14 days per master becomes servable for every contract
dataset its closure names, not only dim_position and dim_asset. So the act also makes `dim_balance` and
`dim_transaction` snapshots servable, 0 -> 14 per master each by the rule above, to principals whose grants already
name them.

**Condition (both reads are prints; neither adds a step to the act):**
- **Phase B pre-act read:** print the count of live grants naming `dim_balance`, beside the ask's `dim_transaction`
  count.
- **`rl5_verify.sh after`:** print the servable `dim_balance` and `dim_transaction` snapshot counts per master.
- **Expected:** 14 each, per master.
- **A count above 14, or any read by a principal without a grant for that dataset:** roll back at once.
- **A count below 14:** a surprise row, not a rollback.

No grant is written by this act. Capability is not authorization: PRD v1.7 holds that every `dim_transaction` grant
beyond the one authorized act needs Andrew's word.
