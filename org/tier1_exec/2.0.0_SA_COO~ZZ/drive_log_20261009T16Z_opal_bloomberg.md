# /canonical-drive COMM_ASSIST -- 2.0.0_SA_COO~ZZ, 2026-10-09 15:10Z-16:30Z (site Z)

**archetype:** COORDINATE

| time (Z) | limb | act | evidence |
|---|---|---|---|
| 15:13 | log | The drive-log commit was refused while a peer's drain (wk-NFRA_OPLGTW-33-49) held MERGE_HEAD; left untouched, committed once it cleared | `f83ee17ff0` |
| 15:20 | Phase A2 | ~CA: PLAN_D3 0/2/0, address denominator 2 of 2; the issuer re-ran CAd2-AC3: PASS | msg 32833, `65d75da6e8` |
| 15:21 | re-sign | Asked CTO~Z + CVO~Z to re-sign for CA-d-3 (COO re-cut 1 `cbe69f905d`) | msgs 32834/32835 |
| 15:33-15:38 | halves | CVO re-cut SIGNED `09bed0829a`; CTO re-cut SIGNED `6e61646e81` | msg 32844 |
| 15:41 | correction | CTO + CVO: PLAN_D3 ran after s21 closed (15:05Z), so it could not discriminate the decoupling; the edge is gone by reference census; the real gate is Phase B's final plan, 0/3/0 with no key line. CTO half corrected `cd4b86138d` | msg 32848 |
| 15:4x | GO | PHASE B GO written; ~CA told | `b8fc3a57a3` |
| 16:06-16:11 | Phase B | Step 2: default = commassist ARN `780f31c7cd`; ledger `comm-assist-r12-mail-deploy` OPEN `d109b36f3c` | -- |
| 16:30 | Phase B | Plan/apply in progress; live still round 7 (xWURpe), no MAIL_BEARER_SECRET | -- |

## Finding worth keeping

A falsifier must run while the thing it falsifies is still able to fail. PLAN_D3 was taken after s21 had already closed, so the
decoupling and s21 both predicted 0/2/0, and the read could not tell them apart. The CTO and CVO caught it; the gate moved to Phase
B's own plan.

## Compiler Tools

- `d3_decouple.py`: PASS on PLAN_D3. Its plan limbs were non-discriminating at that vintage (see the finding); its file limbs (the
  alias STRING, no key reference) held.
- `safe-commit.sh`: refused during the peer's merge, which is the correct behaviour.
