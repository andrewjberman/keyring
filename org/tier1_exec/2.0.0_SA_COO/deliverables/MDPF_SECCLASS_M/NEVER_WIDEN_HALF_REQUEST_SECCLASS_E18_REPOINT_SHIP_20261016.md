# Never-widen half request -- ship the E_18 repoint and take B_01b out of the canonical chain (cell SC-e-108, rows D1-S42, D1-W93-S2)

**Author:** `2.0.0_SA_COO~M1`, dell1, 2026-10-16 ~05:5xZ. **Cell:** `SC-e-108` (worker `0.9.0_WK_MDPF_SECCLASS~98`), drained @d812b466fd (code commit `c7fd33b654`). **Ruling it serves:** CTO round-26 analysis (msg 6482): "SEED first, then REPOINT, in one round"; the
fold ruling @1b45af4766; the seed pair (CTO half @7b166cf360, COO half @0be4ff09ef). Claim words: `measured` = read this session; `held` = cited from a record.

## What is changed (built, LOCAL on `box/dell1`, not deployed)

Two files in `s3://opal-data-bd/code/gold/`:
- `E_18.detect_new_securities.py`: the known set is the canonical `etf-classifications` key set (`existing_tickers`, `NAME::` keys included) read once with the scheduled module's classifier; the old-list scan, the name-prefix block and the lookup into the planner are removed;
  no line of the file names the old list (worker AC3: 0 lines; the base had 17). The planner's absence test is a snapshot taken before the loop (so `--upload` additions are not read as already present).
- `gold_dispatch.sh`: `CHAIN_CANONICAL="B_00 B_01 E_18 B_02 B_03 C_00 C_01 C_02 C_04"`, `CHAIN_HOLDINGS_SEED="B_01"`, `GROUP_B="B_00 B_01 B_02 B_03"`, the `PHASE_B3: B_01b` block deleted, comments fixed; the registry row `B_01b|...` and the `B_01b` script FILE stay (dead).
Tests: `tests/test_e18_known_set_r27.py` (6 passed, including the difference control that the recorder flags a deliberate old-list call); `check_chain_without_b01b.py` (`CHAIN-NO-B01B ok=True`); the whole gold test folder re-run by the issuer at trunk: 203 passed. Measured at trunk 2026-10-16.

## Preconditions (the act waits for ALL)

1. **The seed is applied and read:** `e107_seeded_check.py` `E107-SEEDED ok=True present=13/13 absent_ok=9/9` and leg G (`seed22_legg_read.py`) read on the first scheduled fire that follows it (the CTO's order: seed first, repoint after; a repoint before the seed creates 22 live candidates with no class).
2. **Served = base (measured 2026-10-16 ~05:5xZ, `head-object`):** `E_18` ETag `a7820a205692444dadb59e526200bff6`, VersionId `wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB`, 2026-10-07T16:54:23Z, 14,802 bytes = md5 of the file at the issuance base `a027dd2c77`. `gold_dispatch.sh` ETag `882a910b27d1a855c5d31547eb44f3a1`,
   VersionId `.bNYVetB5sGV8bZki7EgXBfChCH_uPyE`, 2026-10-14T01:48:58Z, 76,278 bytes = md5 at the base. Built bytes (md5): `E_18` `f5c03ee69eaa1810159aefb6e2145bb4`, `gold_dispatch.sh` `165933f6dd0068a649f9757d9b86f303`. The only `code/gold/` versions written since 2026-10-15T00:00Z are `C_06` (06:47:09Z, SC-e-102's) and `diag_sleeve_fix.py` (18:02:18Z): neither is touched.
3. **Window:** runner stopped, no `gold/trigger-pending.json`, outside a fire window, finished 90 minutes before the next scheduled fire (04:00Z nightly, 23:00Z fallback Monday to Saturday). The deploy itself is outside a gold run.

## The act (by a CloudOps lane, after both halves sign)

Open a ledger; deploy ONLY these two files: `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/E_18.detect_new_securities.py` and `bash .tools/safe-deploy.sh data/black_diamond/scripts/gold/gold_dispatch.sh`; a pre/post census of every key under `code/gold/` shows exactly these two moved (anything else is a STOP with a same-session restore by VersionId).
Nothing from `lib/`, the shared module `_shared/etf_classification_scheduled.py` (its `default_bd_securities_lookup` stays, unused by E_18 and the CLI path nobody passes), a table, a watermark or a data key rides the act. D1-S39 (a pair that ships `code/gold/lib/` names DB-b-181's classifier radius): this ships no `lib/` file and says so.

## Blast radius and what the dry run measured

**Behaviour change in the nightly canonical chain (04:00Z / 23:00Z):** (1) B_01b no longer runs: its outside-model (OpenAI) call and its put into the old list stop; the old list stops growing (CUBE's old row dated 2026-10-11 shows it still writes today). (2) E_18's candidate set is every real-ticker pair absent from the canonical table.
**Measured before the ship (read-only, today):** after the seed, the old-list-only tickers are 13 seeded + 9 held out. Running the shared planner on the 9 held-out names with NO old-list lookup (exactly E_18's post-ship call): **PLANNED 0, UNRESOLVED 9** (the names read as balanced, income-blend, target-date and managed-income funds: no GICS or Schwab source classifies them). So the first night after the ship is expected to **write zero rows** and to print the 9 as unresolved.
Existing rows, B_02 onward, the served mix objects and AUA: not touched by this act. The chain's wall time falls by B_01b's run (to be read; the STOP rule is the chain's launch-to-stop not exceeding the last fire's by more than 30 minutes).

## Writers of the named property

The property: an `etf-classifications` row created by the nightly chain. **N = 1** writer in the chain after the ship: E_18's `--upload` conditional put through the scheduled module (`attribute_not_exists(ticker)`, never an overwrite). Before the ship N = 2 (B_01b's put into the OLD list, not this table, and E_18 into this one); B_01b leaves. Counted by reading `CHAIN_CANONICAL` and the call sites in the two scripts.

## Both branches of the expected outcome

- **Branch 1 (the act's proof, no fire):** the served ETags equal the built md5s (`f5c03ee6...`, `165933f6...`); the census shows only the two moved; `bash -n` accepts the served `gold_dispatch.sh`; and one E_18 DRY RUN on the runner (E_18 alone, no `--upload`, by the runner procedure of TO-SC-e97b amendments 2 to 4: stop the service first, `BD_PLATINUM_MODE=canonical bash /tmp/gold_dispatch.sh --single E_18`, script pulled from S3) exits 0, prints no ERROR, reports the 9 held-out as unresolved and writes nothing.
- **Branch 2 (the first scheduled fire after the ship):** the chain runs B_00, B_01, E_18, B_02 ... without B_01b; E_18 exits 0 (non-fatal either way, its exit is read); zero `etf-classifications` writes except a resolvable NEW ticker (none expected); B_02 onward ran as before; the served mix objects change only as the fire's own data does. A state outside both (a held-out ticker written, an existing key changed, B_02 starting without E_18 having finished, a code key outside the two moved) is a STOP and the rollback.
- **W93-S2 / D1-S42 disarm (CTO round-26 amendment):** E_18 reads the canonical list with 0 old-list-only tickers left and the held-out 9 named as seed_pending Unclassified. The disarm is read on Branch 2's E_18 output.

## Rollback per key

Restore `gold_dispatch.sh` to VersionId `.bNYVetB5sGV8bZki7EgXBfChCH_uPyE` and `E_18` to `wb5QYkh7QEfrvMEscg.EgAui0MeBaNwB`, then `safe-deploy` of each base file's bytes. A code rollback restores behaviour (B_01b runs again, E_18 skips old-list tickers again); it does not undo a night's rows (none expected to be written).

## COO half: UNSIGNED

Left for `2.0.0_SA_COO~M1`, signed after the seed is read.

## CTO half: UNSIGNED

Left for `1.0.0_SA_CTO`. Read: the named files and digests; the preconditions (seed first); the dry-run measurement (PLANNED 0, UNRESOLVED 9); the writer count (N = 1 after); both branches; the rollback per key.
