# Andrew-direct 2026-10-13 ~13:1xZ (laptop, 4.0.0_SA_CRO terminal) -- the Dell boxes get the permissions they need; no cross-box CloudOps work

## VERBATIM

> "I do not want CloudOps agents from one box working on projects that are otherwise based on another box, because its
> unnecessary separateion in 99% of cases. THis is why I ask if those are residue because I thought we have already moved past
> this after giving the Dell Boxes the ability to handle their own resource.s"

Then, on the proposed ask: "Yes you should send CTO this note, that the Dell Boxes need the necessary permissions so this cross-box
behavior is not necessary."

## What was measured (laptop, 2026-10-13 ~13:1xZ)

Two laptop CloudOps seats work Dell-placed projects. The orders show this is not residue: each one names a permission the Dell
identity lacks.

| laptop seat | Dell project | the gap, as the order states it |
|---|---|---|
| `0.7.0_AE_CloudOps~ANL` | IRPT_ANLREQ (dell2) | "kms:Decrypt on the IRPT key is denied to dell2" (`org/tier2_senior/0.7.0_AE_CloudOps~ANL/task_orders/IRPT_ANLREQ.TO-READS-Y10.stored-input-recount-at-the-window-laptop.md` line 41); cross-box orders 552a (2026-10-12 20:58Z) and e261 (2026-10-13 05:30Z) |
| `0.7.0_AE_CloudOps~FBL` | ADVI_FIRMBKTS (dell1) | the protected edge functions are bound to the laptop identity (NFRA_CTLPLN round-3 analysis ADDENDUM 7, cited in `ADVI_FIRMBKTS.TO-FB-f-19.act4-edge-leg.md` line 14); "dell1's identity cannot simulate" (`ADVI_FIRMBKTS.TO-FB-f-21.inflection-fence-admit-apply.md` line 77) |

## The ask (routed to 1.0.0_SA_CTO; NFRA_CTLPLN's Dell identity policy)

Give each Dell identity the permissions its own projects need, so no Dell-placed project routes work to a laptop seat:

1. dell2: `kms:Decrypt` on the IRPT key.
2. dell1: `iam:SimulatePrincipalPolicy` (and the read it pairs with) for the firm-bucket pairs.
3. dell1: admitted to the protected edge functions (`shared-advisor-router`, `shared-advisor-router-response`,
   `auth-validator-edge`). This reverses the round-3 ADDENDUM 7 binding, and Andrew's word above covers it.

When the grants are live, the laptop seats `0.7.0_AE_CloudOps~ANL` and `0.7.0_AE_CloudOps~FBL` stand down. The CTO rules on the
scope and the order; this record decides nothing beyond Andrew's stated intent.
