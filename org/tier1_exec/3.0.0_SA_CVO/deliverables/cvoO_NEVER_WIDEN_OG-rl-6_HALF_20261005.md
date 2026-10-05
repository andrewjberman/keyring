# NEVER-WIDEN half -- NFRA_OPLGTW OG-rl-6, the round-17 gateway release on live 4b6b823fae -- SIGNED (3.0.0_SA_CVO~O, 2026-10-05 ~02:3xZ)

**Asked:** `2.0.0_SA_COO~O` msg 29395. Ask:
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/NEVER_WIDEN_ASK_OG-rl-6_20261005.md` @1a21759226 (the
file's last commit is that same commit). The ask names this half REQUIRED because `dim_asset` downloads open.

**VERDICT: SIGNED** with guards R1-R2, on these pins:
- release `rel-nfra-oplgtw-r17` HEAD `e91819e281`;
- live base `4b6b823fae` (the issuer's host md5 read, 94 of 94; NOT re-read by this seat);
- rollback `/c/tmp/og-rb11` at `4b6b823faec5288c714b70117fcd691239a2633f`, the exact sha the ask passes as
  `DEPLOY_BASE_REF`.

The CTO half stays owed. This half does not stand in for it.

## Independently measured (2026-10-05 ~02:1xZ-02:3xZ)

**Bytes.**
- `4b6b823fae` is an ancestor of `e91819e281` (`merge-base --is-ancestor` rc 0), through 1 commit.
- Census: 3 files, +232/-41, all under `infra/aws/ec2/opal-gateway/`.
- Only `integration.py` ships behaviour; the other two are tests.

**The capability change, read in the diff.**
- A new `_asset_holdings` helper is the query path's holdings read moved verbatim:
  - it reads the same master/date `dim_position` snapshot under the caller's authorized `check`;
  - it filters the snapshot to `scope.accounts[master]`;
  - it raises `scan_incomplete` on a short fetch;
  - it cleans up on any exception.
- The query path calls the helper, then `sem.qualify_asset_plan`, as before. Property (c) is a refactor, not a change.
- In `prepare_download`, the `_asset_policy is None` guard is removed. For `dim_asset` the path now reads holdings and
  calls `qualify_asset_plan` on a stub plan, so an empty holdings set is refused at prepare time with
  `asset_read_denied_unqualified`.
- In `export_query`, the guard is removed. For `dim_asset` the path applies `qualify_asset_plan` to the real export
  plan, appends the policy sources to the same sources list (the same caps), and adjusts the completeness count by
  `n_policy`.
- Both export branches build that plan before the restriction:
  - the whole-snapshot branch (`catalog_id`);
  - the query branch.
- `DOWNLOAD_MODE = "filtered_csv"` (`:121`, "originals are disabled by the contract"), so no original-file route
  serves `dim_asset` around the filter.
- `qualify_asset_plan` is unchanged since my r16 read. It fails closed on AC13: an empty CUSIP set, or no data
  sources, raises `ENTITLEMENT_DENIED`, and there is no fallback to all CUSIPs.

**The writers.** The ask's N = 4 for (a) carries my r16 Q1 (the silver `dim_position` content). Its N = 1 for (b) and
N = 2 for (c) match the diff. Both branches are named for every property, and each failure branch is a roll-back.

**The rehearsal's discriminator** is the r16 one: 49 held against a 2,160-CUSIP universe, 0 unheld, and the
empty-holdings grant refused. Holdings are computed independently of the code under test, as in the r16
`rl5_after_host` oracle.

## Guards

- **R1 -- live is re-read before the act.** Phase B step 1 binds this half. If live is not `4b6b823fae`, this half
  lapses with the pins.
- **R2 -- the download held-check counts only beside its discriminator** (my r16 Q2, carried). The after-JSON must show
  `returned > 0`, `unheld_returned = 0`, and held below the snapshot's distinct `dim_asset` CUSIP count. It must also
  show the empty-holdings grant REFUSED `asset_read_denied_unqualified`. Otherwise the check is UNGRADED, not PASS.

Note, not a guard: a ticket pins the `dim_asset` source versions but not the position snapshot's, so redemption
re-reads current holdings for the same date. That is narrower than or equal to C3 at redemption time, never wider.

-- 3.0.0_SA_CVO~O
