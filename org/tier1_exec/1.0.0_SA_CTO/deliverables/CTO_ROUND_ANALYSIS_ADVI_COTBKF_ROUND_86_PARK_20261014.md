# CTO ROUND-86 ANALYSIS -- ADVI_COTBKF -- PARK (2026-10-14 ~00:3xZ; self-drive dell2 box)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** 3.0.0_SA_CVO msg 7374, `surprise-channel/remediations/REMEDIATION_v51.md` @239f84375d (CB85cg1-AC3
PASS). **Governs:** pivot direction `XB-20261013T180328Z-d4a5` O4: the active-set cell, then PARK. Andrew's ADVI memo ranks this backfill
"deep, deep, deep" historical. **No PRD addendum.**

## What the project leaves

**The active Cottonwood set V2 and reverse match V3** (commit `4d427d3bbb`), carried to dell1's MDPF_DEMQUE:
- **Active:** open at Black Diamond on the latest snapshot, cash included. 860 accounts, of which 91 are cash-only; 139 zero-unit accounts
  are excluded.
- **Keys:** raw account ids, one key space (Andrew 10-09).
- **Reverse match:** 460 matched, 13 near, 387 none, each with a reason.
- **Rule for dell1:** former clients are excluded from every draw.

**Records:**
- W155-S1 DISARMED: the served price errors reach no page (`route_not_live`, row D2-S135).
- The UNVERIFIED-Yahoo label is built and counted. Its pair and apply are a precondition on the ARD route ever going live.
- The (ticker, asset_name) key fix is round 83's.
- dell1's quote call `XB-20261012T024430Z-8522` was ACKED and closed SERVED. It sat unread for 45h.

## The one condition before the park (CVO)

Round 85's build scripts are uncommitted scratch. `2.0.0_SA_COO~C2` commits them, re-runs them from the commit, and shows both files re-hash
equal (`5cef7ab0...`, `0783f088...`). Then the park takes effect.

## PARK

- ADVI_COTBKF is PARKED. No round 87 is cut.
- `2.0.0_SA_COO~C2` stands down after its worker branches drain (direction section 8, MSTR act 3).
- The register's PARKED row is carried by `0.0.0_AB_MSTR~DELL2`.
- **Un-park condition:** Andrew's word, or the ARD route to a page being applied (that carries the UNVERIFIED label's pair and the price
  correction).

-- 1.0.0_SA_CTO~DELL2
