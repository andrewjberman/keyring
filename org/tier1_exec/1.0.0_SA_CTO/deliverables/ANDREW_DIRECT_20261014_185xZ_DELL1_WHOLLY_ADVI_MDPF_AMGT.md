# Andrew-direct 2026-10-14 ~18:5xZ (laptop, 1.0.0_SA_CTO terminal) -- dell1 is wholly ADVI/MDPF, plus overflow AMGT

## VERBATIM

> "Yes, also I think COTBKF may be better suited on DELL1. Moving all advisor intelligence ops to DELL1. Basically devote DELL1
> wholly to ADVI/MDPF work as well as any overflow AMGT work."

("Yes" confirms the previous turn: the five answers applied, the laptop keeps driving COMM_ASSIST and NFRA_CTLPLN, and the
Black Diamond as-of defect routed.)

## Applied (1.0.0_SA_CTO, L3 placement)

| project | was | now | when |
|---|---|---|---|
| ADVI_COTBKF (the Cottonwood 10-year backfill; on hold) | DELL2 | **DELL1** | now. It is on hold, so no round is in flight. This supersedes the 10-07 "whatever box is doing IRPT_CUSTDY" placement, by his newer word. |
| ADVI_BILLING (executing) | DELL2 | **DELL1** | at its next round boundary. The round in flight drains on dell2 (NFRA_CTLPLN FWD-13: never mid-round). |
| ADVI_FIRMBKTS, ADVI_BDPRCE, every MDPF_* | DELL1 | DELL1 | unchanged |
| AMGT_RESAPP, AMGT_HARVST | DELL1 | DELL1 | overflow only, behind ADVI and MDPF |

Carriers changed together: each tree row's `fabric` and `placement` fields, its `placement_ruling` (with the old ruling kept
after `||`), and its flat index row `org/projects/<CODE>.json`. `.tools/missions-tree-index.py check` reads 0 violations.

## One project that does not fit "wholly"

**ETFS_RIVALS** (active, on DELL1) is not ADVI, MDPF or AMGT. His words leave its home open. It stays where it is and
takes no new round until he names its home or parks it. That question is carded to him.

## Route

- dell1's CTO and MSTR, and dell2's, hear this through `0.0.0_AB_MSTR` after box-sync.
- dell2's COO for ADVI_BILLING hands over at the round boundary with a resume packet, as NFRA_OPSWKF did.
- dell1 seats ADVI_BILLING and ADVI_COTBKF as two lanes, one project per Tier-2 seat. COTBKF stays on hold until Andrew
  un-parks it.
