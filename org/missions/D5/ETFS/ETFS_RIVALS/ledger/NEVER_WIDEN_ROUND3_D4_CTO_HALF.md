# ETFS_RIVALS round 3 -- `RIV-d-4` never-widen pair, CTO half (signed BY KEY)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~10:1xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round3/NEVER_WIDEN_HALF_COO_D4.md` @7a17b348a9 (msg 27732).

## What I read myself

1. **The code pin:** `66b1800541` is an ancestor of HEAD.
2. **The measured served delta** (`deliverables/0.9.0_WK_ETFS_RIVALS~1/served_delta_after.json` @9a723d4b81):
   - G1 rows match the COO half's table fund by fund: BASG 11272 = 11272; BIDD 20720 -> 20719 (1 date differs); CGIC,
     ETFT, INEQ, PCLG, SCHY, TSEL, TXUE and WCMG equal; home funds IDVZ 0 -> 935 and PFOE 0 -> 530.
   - New resolved fractions: BASG **0.924**, SCHY **0.982**, IDVZ **0.0**, PFOE **0.0**, all others 1.0.
3. **The identity floor's input** (`i1_identity.json`): only 5 funds (BASG, ETFT, PCLG, TSEL, WCMG), each at fraction
   1.0. Its minimum, rounded down, is **1.00**.
4. **The reader of that floor:** `data/etfs/scripts/rivalfunds/guardrails.py:154-171` `identity_coverage` grades EVERY
   fund's newest report: non-cash lines with `resolution_status == RESOLVED` over all non-cash lines, against
   `min_resolved_fraction`. A FAIL puts the fund in the page's `not_updated` list.

## Rulings by key

| key | verdict | reason / condition |
|---|---|---|
| 1 five stage Lambdas, in-place code | **SIGNED** | as tabled; rollback is the re-apply at e622b2fef9 |
| 2 two read grants (`bbg/*/constituents/`, `gold/security_market/`) | **SIGNED** | read-only, additive; Andrew's "do not modify the existing daily etfs pull for Positioning" is honoured (no write under `bbg/`) |
| 3 terminal identity PutObject on G4 | **SIGNED** | an existing identity, simulated first; the G4 import is a QA-class import |
| **4 identity floor = min over `i1_identity.json`** | **REFUSED as specified** | The floor (1.00) is measured over 5 funds, but the guardrail grades every fund. At 1.00, IDVZ and PFOE (resolved 0.0), BASG (0.924) and SCHY (0.982) would FAIL `identity_coverage` and publish as not-updated. The home funds failing breaks FWD-1. **Re-sign condition:** the floor is the minimum, over EVERY fund the guardrail grades, of the newest-report resolved fraction, read from the same G1 the guardrail reads, rounded down. Alternatively, home funds (C-HOME-PRODUCER, identity by their own producer) are exempted by name in `guardrails.py`, with the floor taken over the rest. Either way, the act's page read shows **no fund newly not-updated because of `identity_coverage`.** |
| 5 issuer re-capture control (one landed BASG date) | **SIGNED** | retain, never delete; the earlier object stays |
| 6 new gold G1/G2/G5/G6 + platinum revisions | **SIGNED** | served delta within the table's classes; a non-home fund outside its row STOPs |
| 7 G4 `security_market` | **SIGNED** | new prefix, 0 objects before |
| 8 state markers | **SIGNED** | new markers only |

## Branch A, one sub-item withheld

- **Allowed:** the PRD's scheduled `market` pull after a Terminal sign-in. That is FWD-3's Andrew-approved Bloomberg
  fallback.
- **NOT covered by this half:** the ONE scripted GQGU BQL request. It is a new, ad-hoc vendor request that no word of
  Andrew's names (CLAUDE.md vendor per-use word).
- **Consequence:** GQGU stays UNMEASURED (row Z-S6) until Andrew names it. The item is listed for him.

**CTO HALF: SIGNED for keys 1, 2, 3, 5, 6, 7, 8; key 4 REFUSED as specified (re-sign on the condition above); the GQGU
BQL request withheld.** The act may run once key 4 is either amended and re-signed, or left at PROVISIONAL (unchanged
from today) for this act.
