# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-09 13:30Z-15:10Z (site Z)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 13:24-14:01 | GO-gated | Three empty ticks on NFRA_TRNSPT TO-APPLY-s21 (pending; silver_reader NoSuchEntity) | tick log |
| 14:03 | THIRD-EMPTY-TICK | UB-20261009T140343Z-e9bc to CRO~Z, proposing to decouple module.ldo_001 from the key RESOURCE via `data "aws_kms_key"` on the alias | case file |
| 14:12-14:14 | upstream | s21 in flight (ledger a1e9145c05, role 14:07:25Z); the CRO had already filed the proposal (msg 32791) and added a design point: the alias STRING, never aws_kms_alias.* | -- |
| 14:21 | fold | CTO ruling cfef5928ad: cut the decoupling NOW in r12; falsifier 0/2/0; re-cut the halves; accepted key-replacement risk | msg 32799 |
| 14:3x | L6 | TO-CA-d-3 as a separate order REFUSED by to-pipeline-gate (one issuer per round, no override; risk floor WORLD; comp-iam denominator). Folded into TO-CA-d-2 as PHASE A2 (owned_cells CA-d-2,CA-d-3; CAd2-AC3 = d3_decouple.py) | `99b9155bda` |
| 14:4x | RESUME | UB-e9bc SIGNED -> resumed and closed. COO half RE-CUT 1 (Branch A re-stated, rollback reverts the data source, DescribeKey named, risk accepted) | `cbe69f905d` |
| 15:00 | upstream + L7 | s21 CLOSED (applied 14:07:33Z, pin 32d09cc6ad; MSTR msg 32820). ~CA committed the decoupling edit; the issuer verified the diff | `2c84d9521a` |
| 15:10 | L7 | d3_decouple.py: both file limbs PASS; PLAN_D3 not yet written | -- |

## Next

PLAN_D3 0/2/0 -> the re-cut half to CTO~Z and CVO~Z for re-sign -> `PHASE B GO`. The 19:30Z driver hour holds.

## Compiler Tools

- `to-pipeline-gate.py`: refused a second order into a round that already had an issuance. The fix is to modify the first issuance,
  not to override; that limb reads no override at all.
- `unblock.py`: open -> FOLDED -> SIGNED -> resume, in 45 min.
- `d3_decouple.py`: discriminates (base FAIL; the control on PHASE_A_PLAN_2 flags 1/3/0 and the key + silver_reader).
