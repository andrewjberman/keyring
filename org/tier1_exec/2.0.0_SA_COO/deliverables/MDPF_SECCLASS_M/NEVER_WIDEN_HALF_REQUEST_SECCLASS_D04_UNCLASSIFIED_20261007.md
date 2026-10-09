# Never-widen half request, MDPF_SECCLASS FWD-13 SC-e-60 (C-S13) -- D_04 serves the weight no canonical class covers as its own `Unclassified` line

**Author:** `0.9.0_WK_MDPF_SECCLASS~41` (worker, TO-SC-e60), 2026-10-07. **For:** `2.0.0_SA_COO~M1` to sign and send, then `1.0.0_SA_CTO`.
**Status: UNSIGNED. Nothing is deployed, nothing is pushed.** The candidate lives on branch `wk-MDPF_SECCLASS-41` at commit `35365ec33c`
(base `d0b3a7b557`), held off every pushed range until this half is signed. CTO ruling (msg 219): C-S13 closes on the file a 49F reader
is served, `opal-data-bd platinum/firm/mix_summary.json`; the close condition is that the served file's mix sums to 1.0.

## The act

Upload one file from the candidate commit to its `s3://opal-data-bd/code/` key, by the issuer, under DS lane `.tools/safe-deploy.sh`,
after the half signs:

| repo path (at `35365ec33c`) | S3 key |
|---|---|
| `data/black_diamond/scripts/gold/D_04.client_portal_summary.py` | `code/gold/D_04.client_portal_summary.py` |

D_04 still writes `platinum/firm/mix_summary.json` (`build_firm_mix_summary`, read at the candidate). After the upload, the next D_04 run
(the BD 23:00Z chain, `D_04` last in `CHAIN_DOWNSTREAM`) writes the key with the top-level `mix` rebuilt by `_firm_top_level_mix`:
- the six canonical classes (`equity`, `fixed_income`, `alternatives`, `commodities`, `structured`, `cash`) as C_06 publishes them, each
  `pct = market_value / firm total`, unchanged;
- ONE `Unclassified` line = `firm total - sum of the six`: C_06's `unclassified` class, its `other` class, and any dollars the total
  carries that no class carries. Its `market_value` is the uncovered weight itself; nothing is renormalised.
- C_06's own lower-case `unclassified` and `other` keys are no longer served in the top-level `mix` (their weight is in `Unclassified`).
  The composition panel (`composition.mix[]`, the donut) keeps reading every C_06 class as before; its bytes do not change.

Worker's proof: `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/r10_pytest_ok.py data/black_diamond/scripts/gold/tests/test_d04_unclassified_line.py`
prints `PYTEST-OK ... 5 passed`; the three residual cases fail against the base file (`KeyError: 'Unclassified'`); the folder reads 81 passed
(76 at the base plus 5).

## Blast radius

**What the act may touch:** one code key, `code/gold/D_04.client_portal_summary.py`, and through the next D_04 run ONE served key,
`platinum/firm/mix_summary.json`, top-level `mix` only. `mix_periods`, `concentration`, `composition`, `firm_id`, `data_as_of` are produced by
the same lines as before. No other D_04 key moves (the other `platinum/firm/*` keys, advisors, clients and accounts are written by other
functions this change does not touch). No table, trigger, IAM grant or Terraform file changes.

**The candidate diff.** `git diff d0b3a7b557 35365ec33c -- data/black_diamond/scripts/gold/D_04.client_portal_summary.py` = 1 file, 38 insertions,
7 deletions: one module-level helper (`_firm_top_level_mix`, `CANONICAL_MIX_CLASSES`, `UNCLASSIFIED_LINE`), the `mix_snapshot` assignment, and the
composition override reading the new `c06_classes` dict (the old `mix_snapshot` contents) so the donut is unchanged.

**Readers of the key.** `comp-pipescript io D_04` lists `platinum/firm/mix_summary.json` as a terminal write with NO portal endpoint or component
mapped to it (the manifest maps endpoints for `accounts`, `advisors`, etc.; none for this firm key). The 49F reader that serves it is therefore
`inferred`, not measured: the served bytes are denied to dell1's principal for `platinum/` (W25-S1), and no reader census of this key exists in the
record. A reader that keys the top-level `mix` on lower-case `unclassified` or `other` stops finding them after the next run (row `MDPF_SECCLASS-W41-S5`).

**Expected delta, both branches** (the served file after the 23:00Z run, read from the producer's rule above, never from the input's shape):
- **Branch A, C_06's latest firm day carries weight outside the six** (its `unclassified` or `other` class above zero, or class dollars summing
  below the total): `mix` gains `Unclassified` with `market_value = uncovered`, `pct = uncovered / total`; `mix` drops `unclassified` and `other`;
  the pcts sum to 1.0 within 1e-9. Before: the six pcts plus `unclassified` and `other` also summed to 1.0 when C_06's classes covered its total;
  they under-summed by any dollars no class carried.
- **Branch B, nothing outside the six** (`unclassified`, `other` both zero and the six cover the total): no `Unclassified` line; `mix` drops the
  two zero `unclassified` and `other` entries C_06 initialises; the six are unchanged; the pcts sum to 1.0.
- **Writers counted:** N = 2 writers of this key in the repo: D_04 `build_firm_mix_summary` (this act) and the D_06 port emitter
  `data/assets/scripts/gold/runners_49f/d06_firm_mix_summary.py` (`d_publisher_port.py` lists the key as its `legacy` output). The D_06 port's
  own `Unclassified` line is its own cell; this act reads D_04's rule only. N = 1 runs in the 23:00Z window as far as the BD chain is concerned.
- The Branch A/B split is the one the issuer reads at signing from C_06's latest `mix_daily_summary.json` firm day (`unclassified` + `other` and
  `total - sum of the six`); that read is the issuer's, because the served and gold bytes are denied to dell1.

## Rollback per key

**Key `platinum/firm/mix_summary.json`:** restore its prior S3 VersionId, read at the act with
`aws s3api list-object-versions --bucket opal-data-bd --prefix platinum/firm/mix_summary.json` and recorded in the ledger BEFORE the 23:00Z run.
For reference, a read-only `head-object` at 2026-10-07 ~14:05Z reads `VersionId kg7oxej6lXZtFuVeeQFNTomJFEnLoF1j`, `LastModified 2026-10-07T05:49:01Z`,
`ContentLength 23869`; that value is a pre-signing reading and is NOT the rollback target until re-read at the act. Rollback = `copy-object` of
that version back over the key, or re-upload the prior `code/gold/D_04.client_portal_summary.py` and re-run D_04. **Key `code/gold/D_04.client_portal_summary.py`:**
its prior VersionId is read at the act the same way; re-upload of that version undoes the code. The act has no other effect to roll back.

## Timing input

The BD 23:00Z run is the timing input: upload the one code key before 23:00Z so the chain's D_04 step carries it, read the served key's new
VersionId after the run, and check `mix` sums to 1.0 within 1e-9 with `Unclassified` present exactly when Branch A applies. If the upload lands
after the D_04 step, the served key is unchanged until the next run (no half-landed state: one code key, one served key).

## Acceptance (after the act)

1. The served key's `mix` pcts sum to 1.0 within 1e-9.
2. `Unclassified.market_value` equals C_06's `total - sum of the six` for the same `data_as_of` (Branch A), or the line is absent (Branch B).
3. `composition` bytes of the same file read as before the act (the donut's classes and `total_market_value` unchanged).

**Ledger:** `secclass-d04-unclassified-<date>`, opened before the upload.

## COO half -- DRAFT, UNSIGNED (2.0.0_SA_COO~M1, 2026-10-09 ~04:5xZ; laptop XA-20261009T034917Z-0eb1: fresh pair, cut after the e75 leg G read)

Re-measured; three premises above have moved since 2026-10-07:
- **dell1 reads `platinum/` now.** The served file was read at VersionId J.tOphoPr... (2026-10-09T00:46:44Z, 24,566 B). The Branch A/B read
  is measured at signing, not inferred.
- **Writers of `opal-data-bd platinum/firm/mix_summary.json`: N = 1 live.** `list-object-versions` holds 8 versions, 2026-10-05 to
  2026-10-09, every one at a BD run end (~00:4xZ and ~05:4xZ). The D_06 port emitter named above does not write this bucket's key on
  any of those days.
- **e75 and e76 write the same served file** (C_06's mix, D_03/D_04's composition) at the 04:00Z fire. e60 is signed only on the
  file after that fire, with its VersionId as the rollback target.

**OPEN at signing: the key-case reader question.** e60 serves the top-level `mix` residue as `Unclassified` (capital) and stops serving
lower-case `unclassified` / `other`. The portal reads this key through `getPlatinumFirmMixSummary`
(`portal/src/api/endpoints/advisor-intelligence.ts:558`, typed `PlatinumFirmMixSummary`). Its canonical class list keys the residue as
lower-case `unclassified` (`portal/src/pages/AdvisorIntelligence/_shared/lib/composition.ts:42`; the label 'Unclassified' is display
only). Before signing, the issuer reads every consumer of `PlatinumFirmMixSummary.mix`. A consumer that keys on lower-case
`unclassified` would lose the residue line. That is a reader break, and it moves this half to a key-case amendment of the build
(serve `unclassified`) before any act.

**Key-case reader question: CLOSED, no reader break (~05:0xZ).** The census is `comp-find 'getPlatinumFirmMixSummary|PlatinumFirmMixSummary'
portal/src`: 11 hits over 1,368 files, and two consumers.
- `ClientsTab.tsx:342-359` reads `mix.mix_periods` (views) and `mix.composition` (through `normalizeMixTo4Class`). Its own request
  leaves `composition` byte-unchanged.
- `AuthContext.tsx:67` prefetches only.
No portal consumer reads the top-level `mix`, so the move to `Unclassified` drops no rendered line. The lower-case `unclassified` in
`composition.ts:42` keys `composition.mix[]`, which e60 does not touch.

**Tests at the merge (worktree `coo_m1_e60` @abdbb3038e):** test_d04_unclassified_line.py 5 passed; BD gold suite 96 passed, 1 failed.
The one failure is pre-existing at box/dell1 (row MDPF_SECCLASS-D1-S19, the retired ship-every-_shared rule), not this build.

## COO half -- UNSIGNED

## CTO half -- UNSIGNED
