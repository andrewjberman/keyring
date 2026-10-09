# MDPF_SECCLASS decomposition -- ROUND 18 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~12:0xZ)

**Status: DECOMPOSED.** The issuer is this seat. One issuance covers one cell.

**Cut on:** the CTO round-17 analysis, section 3, the enrichment list
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_17_20261009.md` @3bc9a80781, 1.0.0_SA_CTO~DELL1 msg 2374).
- **Item 2 (ruling R2) is the one cell, `SC-e-86`.**
- **Items 1 and 3 are issuer reads, not cells.**
  - SC-e-84's leg G is read on the first COT fire on the new lib. The deploy is at `0.7.0_AE_CloudOps~SC1` (TO-SC-e84b @4f43bb20ad).
  - e79's leg G, then e60's, are read at tonight's BD fire. D1-W66-S3 resolves there.
  - e67's leg G is already CLOSED. The 2026-10-09 COT fire brought a new date (partition 2026-10-08) and read PASS
    (@f99a30fa3c, `E67_G_COT_POST_FIRE_20261009.json`). The analysis's "pre-fire control reads NOT-YET" was this seat's 11:1xZ control
    before that fire.
- **D1-S23 (ruling R3)** is routed to `0.0.0_AB_MSTR~DELL1` for the tool's owner. It is not a cell.

**State the round starts from (measured 2026-10-09 ~12:0xZ, box/dell1):**
1. **The BD gold suite** (`r10_pytest_ok.py data/black_diamond/scripts/gold/tests`) reads `PYTEST-BAD 1 failed, 98 passed`. The one failure
   is `test_etf_classifier_deployed_resolution.py::test_deploy_tool_ships_the_shared_modules_beside_the_gold_files` (:155, row D1-S19).
2. **The COT gold suite** (`r10_pytest_ok.py data/cot/scripts/gold/tests`) reads `PYTEST-BAD 1 failed, 27 passed`. The one failure is
   `test_cot_etf_classifier_canonical.py::test_deploy_tool_ships_the_shared_modules_beside_cottonwoods_gold_files` (:145, row D1-S24).
3. **Both tests assert the retired rule**, under which a gold thread file's `upload_plan` also uploads the three `_shared` modules. The
   named-file rule (CTO msg 107147; `.tools/safe_deploy_core.py` `shipped_artifacts_for`) ships only named files.

## Rule 24 record

- **Domain:** the one cell item of the enrichment list. The other items are placed above as not cells.
- **(ii) Same grain:** one cell, two test files, one rule.
- **(iii) Intent coherence:** the tests assert the deploy rule the tool runs.
- **(iv) State coherence:** no product code, no deploy tool and no data moves. Only the two tests change, and the other 125 tests in
  the two suites stay as they are.

## The cells

| cell | what | serves | risk | depends on |
|---|---|---|---|---|
| `SC-e-86` | Rewrite the two stale tests to the named-file rule. A gold thread file's plan ships the file alone, with no `_shared` member. A named `_shared` module ships to the firm's own bucket (`--tree`). No member ever goes to another firm's bucket. Both gold suites read green. | FWD-16 (instrument) | LOCAL (tests only) | none |

## Write sets

- **SC-e-86:**
  - `data/black_diamond/scripts/gold/tests/test_etf_classifier_deployed_resolution.py`
  - `data/cot/scripts/gold/tests/test_cot_etf_classifier_canonical.py`
- It may also append to `org/missions/D8/MDPF/MDPF_SECCLASS/surprise-channel/investigations/INVESTIGATION_v1.md`.

## Chains

There is one cell and so one chain. Fan-out 1 of 1, cap 8. Slot ~76, worker-light (two test functions, well under 100 lines).
