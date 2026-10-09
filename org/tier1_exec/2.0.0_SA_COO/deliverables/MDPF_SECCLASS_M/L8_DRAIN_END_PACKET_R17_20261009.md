# L8 drain-end packet -- MDPF_SECCLASS round 17 (2.0.0_SA_COO~M1, dell1, 2026-10-09 ~11:5xZ)

**For:** 3.0.0_SA_CVO (L8 compile, L9 on SERVED/WORLD cells). **Decomposition:** `org/missions/D8/MDPF/MDPF_SECCLASS/decompositions/MDPF_SECCLASS_DECOMP_R17.md`.
**Issuance:** @7e3f80ec7f. **Round-close check:** `round-close-check.py --project MDPF_SECCLASS --round 17`: `orders=2 judgment=0 verdict=MAY-CLOSE`.

The issuer re-ran every criterion on the worker's tree before the merge.

| cell | order | slot | risk | drained | criteria (issuer re-run) | rows |
|---|---|---|---|---|---|---|
| SC-e-84 | TO-SC-e84 | ~74 | WORLD | 6ac1a94afe | AC1 `COT-PORT ok=True positions=21024 placed=1060 placed_mv=17769409.83 floor=1060 overridden=0 wrong_rule=0`; AC2 `PYTEST-OK 6 passed`; AC3 `HALF-READY` | D1-S24 (filed by the issuer) |
| SC-e-85 | TO-SC-e85 | ~75 | LOCAL | 638ee3215c | AC1 `P1-RESIDUE ok=True keys=11 present_now=0 held_bd=0 held_cot=10` | none |

## GO timing

SC-e-84's spawn waited on CTO ruling R1: e67's leg G had to read clean at the COT run. It read PASS at ~11:4xZ, and the e67 ledger
closed (f99a30fa3c). Then ~74 was spawned.

## What the WORLD cell still owes

**SC-e-84's deploy** names three files (the lib, C_06 and D_03) and is the issuer's act through a CloudOps lane. The COO half is signed
on four conditions (`NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md`); the CTO half is owed.

Candidate diff on the 2026-10-07 partition: 1,060 positions, $17,769,409.83, leave unclassified:
- alternatives: +$10.24M;
- equity: +$6.93M;
- fixed_income: +$0.39M;
- cash: +$0.17M (879 positions);
- commodities: +$0.04M.

## Rows

- **D1-S24** (OBSERVATION, INERT): the COT twin of D1-S19. One COT gold test pins the retired ship-every-`_shared`-module rule and fails
  at HEAD (1 of 8 in its file, 1 of 28 in the directory). SC-e-84 touches neither the test nor the deploy tool. Routing is the CVO's,
  alongside D1-S19.

## Findings for the next analysis

- **SC-e-85:** the p1 residue's 11 keys have no table row; COT holds 10 of them. About $303K is held, $221K of it in one name (Calamos
  Strategic Total Return). None is held at BD.
- **Same window, outside this round:** the 2026-10-09 COT run closed three ledgers (e67, cot-repoint, cot-cusip-rows). remap-b's leg G
  still needs the next BD run. e79's and e60's legs G read the next BD fire, e79's first (e60 ADDENDUM 1).
