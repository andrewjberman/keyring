# AMGT_CORPUS -- L5 decomposition v35.0 -- ROUND 35 (unit families for the 52, the re-pin's explicit interpreter, the dry-run repair)

**Issuer:** `2.0.0_SA_COO~X`, 2026-10-04 ~00:5xZ.

**Source:** `1.0.0_SA_CTO~Z` round-34 analysis `ledger/ROUND_ANALYSIS.round34.md` @`83cd052a9c` s.3, the enrichment list. Relay
msg 29092 (READ-acked). The rectangle is its three items. Rulings 1 and 3 are LOCAL with at most three mechanical criteria;
ruling 2's map write is the served move, so it takes a pair. Round 34's decomposition is kept as
`AMGT_CORPUS_DECOMP.round34.md`. Base: CLOUD `bad41f3f91`.

## 0. What this round IS

| # | item (analysis s.3) | cell | path | risk |
|---|---|---|---|---|
| 1 | Unit families for the 52 round-34 mnemonics, decided on the landed values; the census test GREEN | `CRPS-ak-1` | worker `0.9.0_WK_AMGT_CORPUS~1` | LOCAL |
| 2 | `schedule_induction.ps1` names its interpreter explicitly and refuses a non-blpapi python | `CRPS-ak-2` | worker `0.9.0_WK_AMGT_CORPUS~2` (worker-light) | LOCAL |
| 3 | The scheduled entry's dry run reads rc 0 with its plan printed and 0 writes | `CRPS-ak-3` | worker `0.9.0_WK_AMGT_CORPUS~3` (worker-light) | LOCAL |
| 4 | The map rebuild for the 52, one re-derive of each served block, and the re-pin to the commit carrying the map | `CRPS-ak-4` | the issuer's paired act after ak-1 and ak-2 drain | SERVED |

**Chains:** `ak-1 -> ak-4`, `ak-2 -> ak-4` and `ak-3` (alone). `ak-4` consumes ak-1's families and re-pins through ak-2's
script. Write sets are disjoint:
- ak-1: `integrations/bloomberg/research/build_unit_map.py` + one new test file;
- ak-2: `lib/research/corpus/schedule_induction.ps1`;
- ak-3: `lib/research/corpus/induction_scheduled.py` + its test;
- ak-4: `field_map.json`, the served blocks, the Scheduled Task pin, the ledger entry.

## 1. The cells

**CRPS-ak-1 (ruling 2, row Z-W1-S29).**
- **The defect:** all 52 sit in no family of `build_unit_map.py`. A map rebuild could only write "not in any known field family",
  and the served figures carry the pointer unit: 32,826 figures over 96 blocks (`evidence/r34_aj2_leg_v_census.txt`).
- **The act:** place each of the 52 in a family by Bloomberg's own definition (the producer's `FIELD_BASIS` text). The magnitude
  rule must discriminate on the landed values. A field whose landed values do not discriminate gets UNRESOLVED-ON with its
  reason, never a guess. Dates and names get a family that says so.
- **Checks** (`checks/round35/`), at the base:
  - `ak1_check.py`: build 0/2 (52 unfamilied; 130 of 156 landed entries read "not in any known field family"), control 2/2;
  - `test_build_unit_map_families.py`: 1 failed.

  All as expected.

**CRPS-ak-2 (ruling 1, row Z-S85).**
- `schedule_induction.ps1` takes `-Python <path>`. The interpreter precedence is that parameter, then the live task's own
  interpreter, and never PATH resolution alone.
- `-Plan` and `-Register` refuse an interpreter that cannot import blpapi.
- **The plant:** with this machine's PATH (Python314 first), `-Plan` still plans Python311.
- **Check** `ak2_check.sh` at the base: b1 FAIL (plans Python314), b2 FAIL (rc 1, no refusal line). As expected.

**CRPS-ak-3 (ruling 3, row Z-S84).**
- In `--mode dry-run`, `induction_run`'s `install_poison()` replaces `boto3.client`, `subprocess.run`,
  `socket.create_connection` and the vendor loader, and never restores them. The model-block steps then fail with rc 1.
- **The repair:** the scheduled entry keeps step 1's poison for step 1 and restores the originals before the model-block steps.
  Their dry runs read only (list/get), so the run reads rc 0, prints its plan and attempts 0 writes.
- **Check** `ak3_check.py` at the base: build 0/2 (admit rc 1, refresh rc 1, no plan lines), control 1/1 (0 writes). As expected.

**CRPS-ak-4 (the issuer's paired SERVED act).** This runs after ak-1 and ak-2 drain, and after the 2026-10-04 13:00Z scheduled
fire is read as FWD-22's acceptance (on the round-34 pin, which the CVO graded).
1. A serializing dry run: `build_unit_map.py --population crosswalk --dry-run`, plus a temp-map census per new mnemonic (MEASURED /
   UNRESOLVED, with reasons).
2. The pair. The COO half is signed here; the CTO half is owed by `1.0.0_SA_CTO~Z`.
3. One NEVER-2 entry, slug `amgt-corpus-r35-ak4`.
4. Legs:
   - (m) the map write, committed;
   - (d) one re-derive per registered name from its newest raw stamp, `sa_fallback=False`;
   - (r) re-pin `amgt-induction-daily` to the commit carrying the map, through ak-2's script;
   - (v) verify: the pointer-unit census reads 0, or each remaining entry carries its reason. BA's Model tab is looked at.

## 2. Found at the cut (rows, not cells)

None new. Z-S86 is routed to AMGT_RESAPP by the analysis (ruling 4).

## 3. Coverage

| cell | order | slot |
|---|---|---|
| CRPS-ak-1 | `AMGT_CORPUS.TO-CRPS-ak-1.unit-families-for-the-52.md` | `~1` |
| CRPS-ak-2 | `AMGT_CORPUS.TO-CRPS-ak-2.repin-explicit-interpreter.md` | `~2` |
| CRPS-ak-3 | `AMGT_CORPUS.TO-CRPS-ak-3.dry-run-reads-rc0.md` | `~3` |
| CRPS-ak-4 | the issuer's paired act (no order) | -- |
