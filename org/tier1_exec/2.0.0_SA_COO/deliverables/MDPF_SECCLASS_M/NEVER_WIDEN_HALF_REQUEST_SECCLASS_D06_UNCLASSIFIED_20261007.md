# Never-widen half request, MDPF_SECCLASS -- 49 Financial's firm mix serves its residual as its own "unclassified" line (TO-SC-e55, remediation C-S13)

**Author:** `0.9.0_WK_MDPF_SECCLASS~38` (worker, L7), 2026-10-07, for `2.0.0_SA_COO~M1` to issue. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
The ship and any publish run are the issuer's acts, never the worker's. The worker edited one shipped gold file on its branch, ran a fixture test, and uploaded nothing.
Records: round-8 analysis section 3 C-S13 (REMEDIATION_v6); FWD-13 (a security the list does not hold is shown as unclassified); surprise rows `MDPF_SECCLASS-W38-S1`, `-S2`, `-S3` (this order's findings, all bear on this half) and `-S4`; order amended by AMENDMENT 1 (`2.0.0_SA_COO~M1`, b6edc29a26: S2 granted, S1 ruled).

## RELEASE PRECONDITION -- the release seat's FIRST step (AMENDMENT 1, moved here from the withdrawn AC2)

Before any ship, a laptop seat whose principal the bucket `s3://opal-data-49financial/gold/advi/` admits (this worker's box is denied, row `W38-S1`) runs the emitter LOCALLY against the live canonical inputs and the live A_07 dim, never uploading:

```
python data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py --date <asof> --canonical-local <canonical root> --a07-root <a07 root> --a07-date <a07 date> \n  --out org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/D06_MIX_DRY_RUN_<yyyymmdd>.json
python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/d06_mix_sum_check.py
```

The seat STOPS, and the ship does not proceed, on `D06-MIX-SUM ok=False` (the check reads the newest `D06_MIX_DRY_RUN_*.json`: four mix keys, pct sum within 1e-5 of 1.0, market values equal `mix_periods[0].total_aua` within 0.01, the new line equal to `composition.unclassified.market_value`). The emitter's own shape check and SUM-IDENTITY guard run inside the same command; either refusing is also a stop. No live dry-run file exists today; every live-value statement below is held, from the CVO's 2026-10-07 measurement, not from a run.

## The act

Merge branch `wk-MDPF_SECCLASS-38` (`data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py`, the fixture test, and `d00_census_out.json`) into a pushed range, **together with the one-key edit to the shape census, already on that branch** (below), after both halves sign. The CLOUD push deploy gate ships `data/assets/scripts/gold/` (a shared repo home) to S3 AT THE PUSH, so the branch stays off every pushed range until both halves sign.
After the ship, the next scheduled d06 publish writes the top-level `mix` with a fourth key `unclassified {market_value, pct}` equal to the residual the emitter already computes and already serves at `composition.unclassified`. The SUM-IDENTITY guard (classes + unclassified == total, cent-exact) is unchanged and still refuses rc=1 on a corrupt class sum.

The local candidate diff: `git diff b55059ee33..wk-MDPF_SECCLASS-38 -- data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` (the `mix` comprehension iterates all four `CLASS_ORDER` entries instead of excluding `unclassified`; the stale "3-class per the frozen shape" comment replaced). No other line of the emitter changed; `composition.mix` (the per-class panels list) and `mix_periods` are untouched.

**Two things the order's words do not cover (rows `W38-S2`, `W38-S3`), each a decision for the signers:**
1. **RESOLVED by AMENDMENT 1 (W38-S2 granted).** The frozen shape census `data/assets/scripts/gold/runners_49f/d00_census_out.json` (family `platinum/firm/mix_summary`, `sampled_schemas[0].schema.mix` = `{alternatives, equity, fixed_income}`) refused the fourth key (`NEW FIELD (prohibited in v1 -- shape freeze)`, `SystemExit` before any write). The branch now carries the one-key edit (`unclassified: {market_value: number, pct: number}`, same shape as its siblings; a 4-line insertion, `git diff b55059ee33..wk-MDPF_SECCLASS-38 -- data/assets/scripts/gold/runners_49f/d00_census_out.json`). The fixture test proves the payload passes the shape check with the committed census, refuses a payload carrying any OTHER new `mix` key, and refuses the real payload against the census with the key removed.
2. Which served key moves. The CVO measured `s3://opal-data-bd/platinum/firm/mix_summary.json`, which the pin file names as the LEGACY key, written by `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` (`build_firm_mix_summary`), a file this order does not touch. The d06 emitter writes its TWIN, `s3://opal-data-portal-v2/platinum/advi/49financial/mix_summary.json`, which the portal holds as `state: 'held'` (nothing prefers a twin) with a publisher schedule its in-source note records as DISABLED (a 2026-08-21 comment, not re-measured). So this change, alone, moves the twin and not the legacy key. The signers decide whether the legacy producer needs its own cell.

## Blast radius

Keys the act may touch: **one object, the twin** `s3://opal-data-portal-v2/platinum/advi/49financial/mix_summary.json`, and only at a publish run after the ship (held: the publish needs `OPAL_ADVI_PUBLISH_GRANT=1` and the port's `--publish`). The legacy key `s3://opal-data-bd/platinum/firm/mix_summary.json` is NOT written by this act. **Delta against d06's base output (b55059ee33), measured on the test fixture (a 4-position firm, one unclassified of $30,000 of $1,000,000):** base emitted `mix` = `{equity 0.60, fixed_income 0.30, alternatives 0.07}`, pct sum 0.97, market values sum $970,000, while `composition.unclassified` carried the $30,000; the change emits `mix` with the fourth key `unclassified {market_value 30000.0, pct 0.03}`, pct sum 1.0, market values sum $1,000,000 = total_aua. The module header already said UNCLASSIFIED emits as its own bucket, but only the period rows (`mix_periods[*].unclassified`) and `composition.unclassified` carried it; the top-level `mix` was the one place that did not. Nothing else in the payload changes: `mix_periods`, `concentration`, `composition` (including `composition.unclassified`) are byte-equivalent in structure and value.

**Writers counted (N printed):** twin key, N = 1 (`d_publisher_port.py` publishing `d06_firm_mix_summary.py`'s payload; read from `d_publisher_port.py` SERVE_BUCKET/SERVE_ROOT/leaf). Legacy key, N = 1 (`D_04.client_portal_summary.py` `build_firm_mix_summary`, other firms' same-named keys are in their own buckets). The twin's one writer's rule was read at signing-prep: the `mix` comprehension above, with the sums the SUM-IDENTITY guard already checks.

**Readers of the served key (every reader found, `comp-find` over `portal/src` and the repo):**
- `portal/src/api/endpoints/advisor-intelligence.ts:558` `getPlatinumFirmMixSummary` (reads `${PLATINUM_BASE}/firm/mix_summary.json` through `adviRead`, which prefers the legacy key today and the twin only when `ADVI_REPOINT.mix_summary.state` flips from `held`).
- `portal/src/api/endpoints/adviKeyRepoint.ts:215` the twin's shape guard `hasAnyKey('mix','composition','views')`: a fourth key under `mix` does not affect it.
- `portal/src/pages/AdvisorIntelligence/_shared/tabs/ClientsTab.tsx:203-205` (`useQuery` of the firm mix summary; typed `PlatinumFirmMixSummary`, whose `mix` is `PlatinumMixSnapshot = {[assetClass: string]: {market_value, pct}}`, an open index, so a fourth key type-checks).
- `portal/src/contexts/AuthContext.tsx:67` (prefetch only, result discarded).
- `portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts` `platinumToComposition` (maps every `mix` entry to a row, label `Unclassified` from `PLATINUM_LABEL_MAP`) and `normalizeMixTo4Class` (`CANONICAL_CLASSES` already lists `unclassified`): the new line renders as an Unclassified row. **Not read by this worker, flagged for the CTO's half:** whether `platinumToComposition`'s hard-coded `unclassified: {count: 0, market_value: 0}` plus the new `mix` row double-shows the residual in a panel; the portal was only read, never run.
- `data/assets/scripts/gold/runners_49f/fit_harness.py` surface `firm_mix_summary` (legacy-vs-twin diff; the value-band registry's D2 row covers `*mix*` surfaces, so the new key is a covered expected divergence, not a new band).
- Readers outside the repo: BLIND.

## Branches (both covered)

**Branch A -- the ship carries the census edit and a publish runs:** the twin gains `mix.unclassified`; `sum(mix.pct)` = 1.0 within 1e-5 and `sum(mix.market_value)` = `mix_periods[0].total_aua` within 0.01 (fixture-proven, `test_d06_unclassified_line.py`, 6 passed). On the 2026-10-05 as-of the residual the CVO measured is `2,007,761,226.11 - 2,001,258,931.56 = 6,502,294.55` (pct sum 0.9967614 before; 1.0 after, by construction). **The live-input dry run was NOT produced by the worker** (row `W38-S1`: the emitter's inputs sit in `s3://opal-data-49financial/gold/advi/`, which answers an explicit-deny AccessDenied to the worker's role; no `D06_MIX_DRY_RUN_*.json` exists). It is the RELEASE PRECONDITION at the top of this half: the release seat runs it and stops on `ok=False`.
**Branch B -- the ship lands WITHOUT the census edit (not reachable from the branch as committed, which carries both files; reachable only by a partial cherry-pick):** every d06 publish refuses (`SystemExit`, `SHAPE-FREEZE REFUSAL`) before any write. Nothing is written; the object keeps its prior bytes; the leaf's run is a loud failure. This was the ARMED hazard on row `W38-S2`, disarmed by the census edit riding the same branch.
**Branch C -- the twin stays held (no publish):** nothing served moves; the act is the code on `CLOUD` only.

## Rollback

Rollback per key: the one key is the twin `.../platinum/advi/49financial/mix_summary.json`. The issuer records the object's `VersionId` and ETag at the pre-act read; rollback restores that version (copy the recorded version over the key, or rewrite from the pre-act GET snapshot where the bucket is unversioned -- the issuer reads versioning first, it was not read here). The code rollback is the revert of the merge commit, which also reverts the census edit as one unit. No other key is touched, so no other key needs a rollback.

## Acceptance (after the act, if run)

1. A GET of the twin reads `mix` keys exactly `{equity, fixed_income, alternatives, unclassified}`, pct sum 1.0 within 1e-5, market values summing to `mix_periods[0].total_aua` within 0.01, and `mix.unclassified.market_value` equal to `composition.unclassified.market_value`.
2. `composition`, `mix_periods` and `concentration` read byte-equal to the pre-act snapshot except `generated_at`/`data_as_of`.
3. `d06_mix_sum_check.py` run against the pre-upload `--out` file prints `D06-MIX-SUM ok=True` (this is the release precondition above, run BEFORE the act and not only after).

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
