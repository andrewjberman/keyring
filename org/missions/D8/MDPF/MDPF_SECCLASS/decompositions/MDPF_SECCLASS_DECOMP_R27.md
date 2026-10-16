# MDPF_SECCLASS decomposition -- ROUND 27 (2.0.0_SA_COO~M1, dell1, 2026-10-16 ~04:5xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers two cells; the served acts that follow are the issuer's own and are stated below.

**Cut on:** the CTO round-26 analysis, sections 2 and 3
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_26_20261016.md`, `1.0.0_SA_CTO~DELL1` msg 6482, answering the CVO's slug msg 6480 and this seat's input msg 6481
@3db88a77dc). The ruling: the old-list classes are ACCEPTED as source rows, each seeded row carrying its provenance (source `bd-securities` and its date); the order is SEED first, then REPOINT, in one round;
the seed is a served change under a never-widen pair priced per firm on D_04 and C_06; W93-S2 disarms when E_18 reads 0 old-list-only tickers; and B_01b's state is stated in the cut. The list:
1. The 22-row seed under its pair, then the E_18 repoint.
2. FWD-4 / FWD-5's B_01b, if round 26 did not close it.
3. `firm_mix_summary` sort order, if round 26 named its writer.
4. e57e61 stays outside the round under its hold.

## What is a cell and what is the issuer's own act

- **Item 1a is cell `SC-e-107`: the seed's SCRIPT and PLAN, not the write.** The machinery exists (`plan_rows` with the old list as its first source, a conditional `write`); E_18 never calls it for these 22 because it skips
  every pair in the old list. The worker builds `seed22.py` (`plan` read-only, `apply` behind a signed-pair file, `selftest` on stubs) and runs `plan` once for real. **The write is the issuer's act**, not a worker's: below.
- **Item 1b is cell `SC-e-108`: the E_18 repoint and B_01b out of the chain (a build, nothing deployed).** E_18's known set becomes the canonical key set (`existing_tickers`), the name-prefix read and the lookup go, the file names
  the old list nowhere; `gold_dispatch.sh` stops running B_01b. It is a SERVED path (the ship is a later order to a CloudOps seat), so it takes the full limbs. The seed cell and this cell are independent as BUILDS (no edge);
  the order the CTO ruled binds the SERVED ACTS, which are the issuer's.
- **Item 2, B_01b's state (stated as the CTO asked):** round 26 recorded `DECISION-B_01b: RETIRE-FROM-CHAIN` (B_02 reads no bd-securities; the old list's only writer in the gold tree is B_01b's outside-model put, and CUBE's old-list row dated
  2026-10-11 shows it still writes). SC-e-108 takes B_01b OUT OF THE CHAIN. Its FILE STAYS (dead, still in the registry row) until the shipped chain has run, then a later round deletes it with its carriers
  (`README_BUILD_SEQUENCE.md`, `manifests/data_lineage.json`, the `lib/s3_layout.py` watermark entry) and adds the standing FWD-4 test. The shared module's `default_bd_securities_lookup` stays this round (a Lambda-shared
  artifact; no caller after SC-e-108).
- **Item 3, `firm_mix_summary`: CLOSED, no cell.** Round 26 named its writer (`D_04.client_portal_summary.py:578`) and found no order-dependent reader (`NO-ORDER-DEPENDENT-READER`, CVO ADJUDICATION_v26): "if no reader depends on it, record
  that and close" (round-25 analysis).
- **Item 4:** `TO-DEPLOY-e57e61` unchanged (outside the round).

## The issuer's served acts, in the CTO's order (after both cells drain)

1. **The seed pair** (request, CTO half, COO half): the 22 tickers, the old-list class and the dollars of each, the expected per-firm move (D_04 and C_06 readers: the 22 tickers' dollars leave `Unclassified` for their class on the 49financial Black Diamond tree;
   the cottonwood tree is separate and is checked in the pair for its own use of the old list), the conditional put, the restore (delete the 22 keys), the outside-model provenance of the values, and the folding of any sub-class the canonical vocabulary lacks.
2. **The GO to `0.7.0_AE_CloudOps~SC1`** (a staged order carrying `<paths>` for the ledger and sentinel) to run `seed22.py apply`, then the first scheduled fire reads D_04 / C_06 (leg G, the moves equal the pair's).
3. **The ship pair for E_18 and `gold_dispatch.sh`**, after the seed is applied, then the first scheduled fire of the shipped chain: E_18 reads the canonical list with 0 old-list-only tickers left (W93-S2's disarm condition).

## Rule 24 record

- **Domain:** the CTO's four items; two cells; three issuer acts.
- **(ii) Same grain:** SC-e-107 is one script plus one plan file; SC-e-108 is one script's known-set read, one shell file's chain lines and one test.
- **(iii) Intent coherence:** the plan check recomputes the candidate set from a committed baseline and the live tables, never from the plan; the chain check parses the shell file's assignments.
- **(iv) State coherence:** SC-e-107 writes only repo files and reads AWS; SC-e-108 deploys nothing. Neither moves a served object. The seed moves the classification of 22 tickers' dollars once, under the pair.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-107` | `R27_CHECKS/seed22.py` (`plan`, `apply` behind a pair file, `selftest`) and the real `SEED22_PLAN.json` for the 22 tickers, provenance copied from the old rows | FWD-1, FWD-5 | LOCAL, direct act | none |
| `SC-e-108` | E_18 reads the canonical key set as `known`, drops the name-prefix read, the lookup and every mention of the old list; `gold_dispatch.sh` runs the canonical chain without B_01b; new test with a difference control | FWD-4, FWD-5 | SERVED | none (as a build) |

Each acceptance check is a committed script under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/` (read-only to the workers), dry-run at the base, with green and negative arms.

## Write sets (disjoint)

- **SC-e-107:** `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R27_CHECKS/seed22.py`, `deliverables/0.9.0_WK_MDPF_SECCLASS~97/SEED22_PLAN.json`.
- **SC-e-108:** `data/black_diamond/scripts/gold/E_18.detect_new_securities.py`, `data/black_diamond/scripts/gold/gold_dispatch.sh`, `data/black_diamond/scripts/gold/tests/test_e18_known_set_r27.py` (new).
- Both also append to the project's surprise channel.

## Chains

Two cells, no edge: two chains. Fan-out 2 of 2, cap 8. Slots ~97 (SC-e-107) and ~98 (SC-e-108), `worker`, haiku (treatment box, MP-20261010). SC-e-107 is cut with `<direct_act>true</direct_act>`; SC-e-108 is SERVED and takes the full limbs.

## Carried (not cut)

The client-facing Black Diamond Mix PROD push (Andrew's); the DEMQUE<->SECCLASS sync cell (arrives with the CTO's CONTRACTS rows); `TO-DEPLOY-e57e61` (held); the B_01b file deletion, the shared-lookup removal and the standing FWD-4 test (a later round, after the shipped chain has run).
