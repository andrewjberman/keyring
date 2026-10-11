# ADVI_COTBKF decomposition -- ROUND 62 (issuer 2.0.0_SA_COO~C2 on dell2, under /canonical-drive; drafted 2026-10-11T07:51Z)

**Status: DRAFT -> ISSUED in one issuance.**

**Cut on:** `1.0.0_SA_CTO~DELL2` msg 4370 (cut FWD-7's role pair next after the mint) and msg 4433 (the CTO half SIGNED
@9b8eb8c244; applier `0.7.0_AE_CloudOps~CB2` on dell2; "Cut the order"). Row ADVI_COTBKF-D2-S95 (ARMED on this issuer).

- FWD-7's break-glass role and its inline policy exist in code only (cell CB-d-4 planned and simulated, applied nothing). They plan as
  2 adds on every box, so an untargeted apply of the `shared-infra` root creates them as a rider.
- The pair: COO half `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_COO_HALF.md` @fd4e6436cf; CTO half `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_FWD7_RESTRICTED_BREAKGLASS_ROLE_CTO_HALF.md` @9b8eb8c244.

**Rule 24.** Domain: the two addresses of the pair -> one cell.

## Measured constraints (issuer)

1. **Targeted only.** The CTO narrowed its row D2-S92 ruling to untargeted applies; no untargeted apply of this root runs from dell2.
2. **No agent assumes the role.** The proof reads the role and its policy; it never uses them.
3. The Cottonwood mint is complete (CB-al-2 @b589bc4883), so this is the next act of this issuer, as the CTO ordered.

## The cells

| cell | item | serves | risk | depends_on | slot |
|---|---|---|---|---|---|
| `CB-bj-1` | create the restricted-prefix break-glass role and its inline policy by a targeted apply of 2 addresses; read both back; an untargeted plan reads them no-op | FWD-7 | WORLD | none | `0.7.0_AE_CloudOps~CB2` |

**Fan-out:** `1 of 1 chains, cap 8`.
