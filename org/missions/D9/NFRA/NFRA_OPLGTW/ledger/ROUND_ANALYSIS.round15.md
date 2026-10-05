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

## 6. Correction ~22:1xZ -- R10's Z-S46 claim was too wide (`3.0.0_SA_CVO~O` msg 29037)

- **The claim was too wide.** "REMEDIATED as observed" was true of the branch I observed: the general refusal post-check
  at `safe-commit.sh` :1117-1127. It was false of the surprise-row-gate refusal branch (:877-881), which reset with
  `2>/dev/null || true`, printed "files unstaged" unconditionally, and exited before that post-check. The CVO's
  2026-10-02 refusal on that branch left a file staged with no warning.
- **Fixed by this seat** in the commit that carries this section. The branch now checks each gate file with
  `git diff --cached --quiet` after its reset. A file still staged is reported with the same REMAIN STAGED warning, and
  a failed read counts as still staged. No gate is added.
- **Exercised in a scratch repo:**
  - positive (reset succeeds): `stuck=0`, 0 staged after;
  - negative (`.git/index.lock` present, reset fails): `stuck=1`, 1 still staged.
  - `bash -n` passes.
- Z-S46 is REMEDIATED on both branches as of that commit.
- **Z-S50, second correction (`3.0.0_SA_CVO~O` msg 29046).** The @bee7c817d7 fix reset and checked the GATE files
  only. A non-gate path in the same pathspec stayed staged under "none remains staged".
  - The branch now covers everything THIS call staged (staged-now MINUS the lock-entry baseline, the same set as the
    general post-check). An unreadable index is reported, never read as empty.
  - **Exercised:** a pre-staged foreign file is untouched; the call's gate file and its non-gate file are both
    unstaged (`reset=2 stuck=0`); with `.git/index.lock` both are reported (`stuck=2`).

## 7. Addendum ~00:3xZ -- R9a, the one-page duplicate check (`2.0.0_SA_COO~O` msg 29084, row Z-W22-S4)

**The gap R9 opened.** The single-page rows path (`integration.py:687-705`) refuses `duplicate_source_grain` only when
the request's columns carry EVERY grain field. R9's `quantity_cash_settled` is not a served field, so no request can
carry it, and for `dim_position` the single-page check can never fire. The multi-page path is unaffected:
`:742-752` calls the cached snapshot check `_grain_unique` (`:536-555`, one aggregate job per snapshot digest).

**R9a -- option (b), narrowed.**
- **The fallback.** In the single-page rows path, when the dataset's grain includes a column that is NOT a served field,
  so that no request can carry it, the per-result check is replaced by `_grain_unique` on the snapshot. That is the
  same cached check paging already runs. A non-unique snapshot refuses with the same `duplicate_source_grain` code.
- **Nothing else changes.** Every other shape keeps today's behaviour: a request whose narrower column set merely omits
  a SERVED grain field, and aggregate mode. Widening the fallback to them would newly refuse requests that work today
  (`dim_balance`'s grain is unmeasured). That stays the separately filed NOT-ENFORCED row, as its code comment says.
- **Why not (a).** Serving `quantity_cash_settled` is a contract change, and existing grants would not name the field,
  so their requests still could not carry it.
- **Why not (c).** Losing the single-page check on `dim_position` drops the never-serve-a-wrong-row property for every
  one-page answer.
- **Cost:** at most one aggregate job per snapshot digest, cached, and shared with paging. There is no new data exposure.
- **Write surface.** It sits in `integration.py`, so the issuer re-cuts OG-gr-3 to include it.
- **Acceptance:**
  - `test_ogq2_ac20` is restated to plant a full-grain duplicate and see a single-page `dim_position` request REFUSED;
  - a control shows a narrow-column `dim_balance` single-page request unchanged.
- **The release.** OG-rl-5's halves cover it as served behaviour.

## 8. Addendum ~20:5xZ 2026-10-04 -- R12, the live Schwab gap (`2.0.0_SA_COO~O` msg 29216, rows Z-W15-S33, Z-W15-S34)

**S33 is a carrier defect, not a spec change.** PRD v1.7 C3 already makes `silver/dim_transaction/` data-readable
(ratified-text half signed @779e8e7f59). The contract JSON never got the matching prefixes. MX-r-6 step 0 (@32ebe6bee6)
added the dataset under ruling B4, and this seat's v1.7 addendum ratified the prefix but never carried it into the JSON.
The miss is this seat's.
- **Cure, by this seat, in the commit that lands this section:** `org/standards/NFRA_OPLGTW_CONTRACT.json`
  `data_prefixes` gains exactly `schwab/08242234/silver/dim_transaction/` and `schwab/08335338/silver/dim_transaction/`.
  - No other byte changes, and `contract_version` stays 1.3 (precedent @32ebe6bee6).
  - Before the edit, CLOUD's contract equalled live `af2d762970`'s (`git diff` empty).
  - No PRD addendum and no re-sign: the ratified text does not move.
- **Tests on the edited tree.**
  - 80 passed in the schwab suites: catalog, c3_rules, wiring, query, grain_r9, asset_policy, semantics, transactions,
    ssavail_contract.
  - `tests/acceptance` passed 15 of 15 when run alone.
  - Run in one process after the other suites, the acceptance tests error at setup (RuntimeError, 20 errors). That
    interaction was not attributed in this session.
- **Since when: not established.** The zero is MEASURED only on live `af2d762970`, on 10-04 (SSM 81eb1a24, 2e7cda61).
  Before @32ebe6bee6 (released 2026-09-30 at 18:33Z), `catalog.py:605-607` rejected a closure's `dim_transaction`
  table for the opposite reason: the contract did not carry the dataset. So any date whose closure already named that
  table was rejected either way. When closures began to name it is unmeasured.

**S34: retire the query path's placeholder guard; the download paths keep theirs.**
- `self._asset_policy is None` is OG-q-2's placeholder (@c3728d6bdb). OG-q-5 half one built the C3 holdings
  restriction inline on the query path (`integration.py:622-654`, `sem.qualify_asset_plan`). It covers rows and
  aggregate mode, and it runs before any engine job. The attribute itself is never read.
- `build_default_service()` (`:1060`) passes no policy, so `:569-570` refuses every served `dim_asset` query.
- `prepare_download` (`:818-819`) and `export_query` (`:895-896`) apply NO holdings restriction. On those paths the
  guard is the only barrier between a `dim_asset` grant and an unrestricted CUSIP list, so lifting it there would widen
  served output beyond C3.
- **Ruling:**
  - Delete `:569-570` only.
  - `:818-819`, `:895-896`, `build_default_service()` and the `asset_policy` parameter stay byte-identical, so the
    acceptance seam still works.
  - `dim_asset` downloads stay UNAVAILABLE `asset_policy_selection_unavailable`, which is fail-closed.
  - The C3 restriction on the download paths is a round-17 enrichment item, not an rl-5 rider.
- **What acceptance must show,** through the served construction with no seam:
  - a `dim_asset` rows query on a qualified snapshot returns only CUSIPs held by the grant's accounts for that
    master/date, and a planted unheld CUSIP is absent;
  - `dim_asset` `prepare_download` still refuses `asset_policy_selection_unavailable` (the control).

**(a) or (b): (a), one widened OG-rl-5 release.**
- (a) is the measured state: rl-5's counterfactual (SSM 02bc6129) ran this code with these prefixes and served 56
  snapshots, with the R9 columns present and 0 blank.
- (b) ships a state nobody measured. It restores the catalog, but a multi-page `dim_position` read still refuses
  `paging_refused_no_unique_grain` (rl-5's PAGING BEFORE read, counterfactual contract), and it costs two deploy acts.
- **Write surfaces.** The issuer amends OG-rl-5; this is the same mechanism as R9a's A2 on gr-3. The release tree takes:
  - the contract whole from CLOUD at this commit (live plus the two strings);
  - gr-3's hunks, as before;
  - the two-line deletion and its tests.
- **Never-widen.** The release moves served output: Schwab snapshots go from 0 servable to servable at both masters,
  and `dim_asset` queries become servable under the C3 holdings restriction. This seat's half names that blast radius
  at Phase B. No grant changes: capability is not authorization, and per v1.7 every `dim_transaction` grant beyond the
  one authorized act needs Andrew's word.
- S33 and S34 keep `2.0.0_SA_COO~O` as disarm owner; each disarms on the release's post-act read.
