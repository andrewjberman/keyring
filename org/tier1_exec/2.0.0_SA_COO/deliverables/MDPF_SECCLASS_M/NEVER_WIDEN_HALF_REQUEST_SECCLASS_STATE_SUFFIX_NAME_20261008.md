# Never-widen half, MDPF_SECCLASS -- the CSCO name drops its "/Delaware" incorporation suffix (FWD-14, FWD-3, cell SC-e-74)

**Author:** `0.9.0_WK_MDPF_SECCLASS~64` for `2.0.0_SA_COO~M1`, 2026-10-08. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half SIGNED (2.0.0_SA_COO~M1); CTO half SIGNED (1.0.0_SA_CTO~DELL1 @9eb12e9f88).**
This file is a REQUEST. Nothing in it has been written to any table. The writer refuses `--write` until both headings at the foot read SIGNED.
Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md` FWD-14 ("An advisor reads a properly written security name wherever holdings are listed"); source `1.0.0_SA_CTO~DELL1` msg 1039 and the SECHIST round-1 analysis @0141533760 section 2.2. Same writer, same attributes, same rollback as the signed V2 request `NEVER_WIDEN_HALF_REQUEST_SECCLASS_CLEAN_NAMES_V2_20261007.md`; only the set and the function change.

## The key, before and after

Exactly 1 row of `etf-classifications` carries the suffix (measured by TO-SC-e74's cut). Read by a consistent get-item, us-east-1, 2026-10-08:

| key | field | before | after |
|---|---|---|---|
| `CSCO` | `name` | `Cisco Systems Inc/Delaware` | `Cisco Systems Inc` |
| `CSCO` | `updated_by` | `seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)` | `mdpf-secclass-clean-names-v2` |

The row's `classified_by` reads `legacy`; `asset_class` `equity`, `sub_asset_class` `Information Technology`, `instrument_kind` `single_security`, `management_style` `unknown`, `last_updated` `2026-09-30T00:02:50Z` are not touched.

## The act (by the issuer, after both halves sign)

Write:
`python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py --set org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv --write --half <this file> --snapshot org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_SNAPSHOT_R13_STATE_SUFFIX_20261008.json`

- **Snapshot path:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_SNAPSHOT_R13_STATE_SUFFIX_20261008.json`, written by the writer before the first update (the full pre-state item of `CSCO`).
- **The set:** `CLEAN_NAME_ROW_SET_R13_STATE_SUFFIX_20261008.tsv`, one WRITE line (`table`, `CSCO`), current name read live, clean name from the new `clean_name()`.
- **The update** is ONE conditional `UpdateItem`: `SET name = :clean, updated_by = :by` with condition `name = :current` (`Cisco Systems Inc/Delaware`). `:by` = `mdpf-secclass-clean-names-v2`. A row that moved since the set was built is refused and reported, never overwritten.
- **The function** is `infra/aws/lambda/v2_portal/_shared/security_name.py` `clean_name()` as changed by TO-SC-e74: a trailing "/<US state name or postal code>" or "/NEW" suffix (optionally closed by "/", repeatable, optional spaces around the slash) is dropped, only directly after a corporate-form token; any other slash stays; idempotent. Pinned by `_shared/tests/test_security_name_state_suffix.py` (4 strip cases, 8 unchanged controls, forms and non-suffix cases) and `R13_CHECKS/sc_r13_state_suffix.py` (`STATE-SUFFIX ok=True cases=12 pass=12`).
- **Dry run** (read-only, this worker, 2026-10-08): `CLEAN-NAME-V2-DRY-RUN write=1 custody=0 seed_source=0 unchanged=0 refused_stale=0 puts=0` (the client is wrapped with a counter of every mutating call and the run asserts it is 0).

## Blast radius

One table, `etf-classifications`; one key, `CSCO`; the `name` attribute and the `updated_by` attribute. **No class attribute is touched** (`asset_class`, `sub_asset_class`, `instrument_kind`, `management_style`, `classified_by` all keep their values). No other row, no other table, no S3 object; no row created or deleted.

## Readers that print the name

- **Named from the repo:** `data/etfs/scripts/gold/etf_positioning_publisher.py` `_display_name(ticker, raw)` serves the table row's `name` (registry `name` first), reading it through `ETFClassifier` (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`); after the act it serves `Cisco Systems Inc` for `CSCO` at its next run. The gold `etf_classifier.py` readers use the row for its class, not its name (cited from the V2 half; not re-traced here).
- **Not named, and not claimed:** any other producer or page that reads `name` through a path this worker did not trace. A reader that matches a holding by its name string would see the change; none is ruled out from the repo. The issuer reads this limit at signing.
- **Writers of `name` not counted here.** The V2 half's writers count (N = 8) is not re-counted by this worker; the signing seats read it. Whether a later scheduled seed run re-puts the suffixed name from the seed source (`seed-etf-constituents`) is NOT verified by this worker.
- **Deploy order.** The function change lives in `_shared`; it reaches the Lambdas through the deploy lane. The table write is independent of it.

## Rollback per key

The snapshot holds `CSCO`'s full pre-state item. `python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/clean_name_write_v2.py --rollback org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_SNAPSHOT_R13_STATE_SUFFIX_20261008.json --write` restores it by a conditional update, only where the row still reads `updated_by = mdpf-secclass-clean-names-v2` and `name = Cisco Systems Inc`: `name` goes back to `Cisco Systems Inc/Delaware` and `updated_by` back to `seed-etf-constituents (1.0.0_SA_CTO~Z, Andrew-direct 2026-08-25)`. A row changed by another writer since is skipped and reported. Without `--write`, the rollback lists what it would restore.

## COO half -- SIGNED

`2.0.0_SA_COO~M1`, 2026-10-08 ~18:4xZ. Read: the set (1 WRITE line, CSCO), and the dry run re-run by this seat in the worker tree
(`write=1 custody=0 seed_source=0 unchanged=0 refused_stale=0 puts=0`). AC1 `STATE-SUFFIX ok=True 12/12` and AC3 349 passed were also
re-run here.

**Writers of `name`, counted: N = 10, each rule read.**
- The V2 half's 8.
- Two writers added since:
  - `R10_CHECKS/old_list_reclassify_write.py` (e32/e49): it plans and puts on absence only.
  - `R12_CHECKS/cash_row_write.py` (e68): key CASH only.
- For CSCO, which has `classified_by = legacy` and an existing name, no writer but this act rewrites `name`:
  - `seed-etf-constituents.py` puts only under `attribute_not_exists(classified_by)` (:232), so it cannot re-put the suffixed name.
  - The seed writer writes seed rows only.
  - Writers 3-7 and the e32/e49 runner put on absence.

**Both branches:**
- (a) The condition holds (`name = Cisco Systems Inc/Delaware`): `name` and `updated_by` move on CSCO only.
- (b) The row moved since the set was built: the update is refused (`refused_stale=1`), nothing moves, and the act is re-planned.

Blast radius: one key, two attributes, no class. Rollback per key is as stated above. Readers: the publisher's `_display_name` is the
one served reader named. This seat accepts the limit stated for untraced name-string matchers, since the change is a suffix drop on one
single stock.

## CTO half -- SIGNED

`1.0.0_SA_CTO~DELL1` @9eb12e9f88, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_SECCLASS_SC_E74_STATE_SUFFIX_NAME_20261008.md`
(msg 1053). Conditions:
- write before 2026-10-09 12:30Z;
- read CSCO back by a consistent get-item, and report the before/after line and the refused_stale count;
- a refusal means re-plan, never force.
Recorded here by `2.0.0_SA_COO~M1`.
