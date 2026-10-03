# NFRA_OPLGTW -- ROUND 15 ANALYSIS (L10), `1.0.0_SA_CTO~O`, 2026-10-03 ~21:5xZ

**L10 on `3.0.0_SA_CVO~O`'s slug** for rounds 13-15 (msg 29027, `surprise-channel/remediations/REMEDIATION_v3.md`
@d809704b87):
- 7 rows graduated: 2 REMEDIATED, 5 OPEN.
- OGO2-J1 FAIL.
- The channel has 304 of 304 rows dispositioned.

**The issuer's terminal message** is msg 29026: round 15 is terminal on CLOUD @e6a83acc1f, with 4 of 4 complete.

**Issuer: `2.0.0_SA_COO~O`.** ONE issuance, section 4.

## 1. What round 15 did

- **OG-gw-1:** the grant-writer builder stages from `EC2_MANIFEST` `deployed_commit` (R1).
- **OG-gw-2:** the grant writer was redeployed from `af2d762970`'s closure.
  - The live `CodeSha256` is `ZyYCPPyP...`, a code hash only. 11 of 11 files are equal and the environment is unchanged.
  - The ledger is CLOSED. G1, W1 and W2 held: no grant was written.
  - This seat read the live hash at 20:57Z; the CVO's post-act read is @178c9630fa.
- **OG-tf-2:** the opal-gateway root plans `No changes` from a fresh worktree, and the issuer re-grade on CLOUD PASSes.
  - The owner keys are in `gateway/principals/rosters` (R2), behind a closed ledger.
  - The grant-writer archive is built at plan time from the pinned builder, through a locked `hashicorp/external`
    provider.
  - The layer is referenced through a data source.
- **OG-gr-2: GRAIN_FOUND** (`deliverables/0.9.0_WK_NFRA_OPLGTW~22/GRAIN_R15.json`, read-only, 0 writes).

## 2. Outcome grades

The tally is unchanged at **0 REALIZED, 2 NOT_REALIZED, 6 HELD, 0 DEFERRED.**
- **FWD-2 stays NOT_REALIZED** until the grain is adopted and released. `DATASET_GRAINS` (`query.py:155`) is enforced
  before paging. A non-unique grain refuses paging, and today's `dim_position` (`account_id, cusip, l_s`) and
  `dim_asset` (`cusip`) grains collide on measured snapshots.
- **FWD-8 stays NOT_REALIZED.** OGO2-J1 FAILs; the remedy is OG-o-5.

## 3. Rulings

**R9 -- ADOPT the measured grain (option A).**
- **The grain.**
  - `dim_position`: `account_id, cusip, l_s, quantity_settled_unsettled, quantity_cash_settled`.
  - `dim_asset`: `cusip, security_description_line_1`.
- **Why it qualifies.** It meets this seat's adoption rule (round 12, section 3a): unique on every measured snapshot (52
  of 52, plus 4 beyond the basis), and the added column is never blank (0 blank).
- **Why not `accounting_rule_code` (option B).** It is the semantic cash/margin discriminator and is also unique on 28 of
  28. But it is BLANK on master `08335338` since 2026-09-21: 1-3 rows per snapshot, with blank `cusip`, `l_s` and
  `tax_code` and zero quantities. Explaining those rows belongs to the producer's owner. Changing them is a
  data-engineering operation that Andrew-direct 2026-10-03 ~17:3xZ bars without his directive.
  - So B is recorded as the semantic successor, adoptable once the producer's owner explains the blank rows.
  - That finding is routed READ-ONLY. No data or pipeline is changed by this ruling.
- **The failure mode is safe.** A future snapshot that collides under A REFUSES paging, loudly. It never serves a wrong
  row. That is an availability event, re-measured when it fires.
- **What the grain means.** `datasets.json`'s grain notes must say that the grain is a ROW-UNIQUENESS key for paging and
  tie-break, not a business identity. A client must not read two quantities as part of "what a position is".
- **Scope.** This changes the gateway's serving metadata (`query.py` `DATASET_GRAINS`, `datasets.json`), never the
  silver data or its producer.

**R10 -- rows (the slug's OPEN rows routed to this seat).**
- **Z-S46** (safe-commit's unstage message did not match the index) is **REMEDIATED as observed.** On 2026-10-03 ~18:0xZ
  a refused commit of this seat's printed "WARN: 2 file(s) could NOT be unstaged and REMAIN STAGED -- ... Clear them
  yourself", and the index agreed. The message now tells the truth.
- **Z-W17-S4** (keep or retire the layer resource) is **KEPT, closed as design.**
  - Deleting its block destroys live layer v1, and `removed`/`moved` are barred.
  - It is retained build-free, its hash read from the deployed version's data source.
  - Retiring it would be its own act, with a reason that does not exist today.

**R11 -- the issuer's two check defects** (Z-S48, the cone lacked `infra/logic`; Z-S49, the double-zero count) are
accepted as fixed in place at @2255e12631.

## 4. THE ENRICHMENT LIST ROUND 16 CUTS (one issuance, `2.0.0_SA_COO~O`)

1. **OG-gr-3: adopt R9** (LOCAL).
   - `query.py` `DATASET_GRAINS` and `datasets.json` `grain_fields` and grain flags change together (`semantics.py`
     refuses a mismatch at import).
   - The grain notes are worded as above.
   - A test pins uniqueness on one measured snapshot fixture, and a planted collision refuses paging.
2. **OG-rl-5: the gateway release** carrying OG-gr-3 on live `af2d762970`, under CTO, COO and CVO halves. Paging becomes
   available where it refused, so served behaviour changes.
   - Acceptance: a rows-mode page of `dim_position` and of `dim_asset` succeeds on a qualified snapshot for an EXISTING
     grant holder.
   - No grant is created or changed (G1, B2).
3. **OG-o-5:** the runbook section-7 text remedy (already drafted).
4. **Z-W26-S4:** the grant writer's tests run against the pinned staged closure (`build_package.py` output), not HEAD's
   tree.
5. **Aged rows:** the CVO's gate disclosed 25 OPEN rows unmoved for 2 or more rounds. The issuer and the CVO list each
   one with its owner and the condition that moves it. Rows that no condition moves are closed with a reason.

**Owed by this seat:** the closing hash for register row ETFS_RIVALS-W5-S3 goes to `0.0.0_AB_MSTR~Z` this turn.

**Stated dependencies, not cells:**
- OG-v-7 waits on Andrew's own tests, then Alyssa.
- The pilot waits on G-E and on R7's host-side flag.
- Z-S43 waits on the Research Meeting invitation.
- The D9 -> D6 move waits on the joint boundary with NFRA_MCPINDEX.

## 5. What this analysis does not do

It deploys, applies and flips nothing. It re-measured only:
- the live grant-writer `CodeSha256`;
- `query.py`'s `DATASET_GRAINS` and its call sites (`integration.py:539`, `:687`);
- `GRAIN_R15.json`'s verdict, alternatives and caveats.
