# ETFS_RIVALS round 7 -- deploy never-widen pair, CTO half (five Lambdas + sweep input at CLOUD 75ad1e4d2e; 10-02 republish once; one deliberate sweep; the vehicle's LONG_COMP_NAME from 10-05)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~23:5xZ.
**COO half:** `deliverables/2.0.0_SA_COO~RV/round7/NEVER_WIDEN_HALF_COO_ROUND7_DEPLOY.md` @76f548ce47 (msg 28809).
**Authority:** round-6 analysis @94f682c868 (C-S24 lead; the organic-trigger rule).

## What I read

- **Act 2 (`safe-apply`):** the plan reads 0/6/0.
  - Five `source_code_hash` changes, with the before hashes equal to round 6's live set (read at 23:5xZ).
  - The sweep schedule input gains `"run_path": "scheduled"` (pv-1).
  - No role, policy, secret, environment or trigger change.
- **Act 3:** ONE republish of 2026-10-02. It stamps "ad_hoc", and the AI step reads SKIPPED_EXISTS (2 account objects exist), so
  there is no vendor call.
- **Act 4:** ONE deliberate invoke with the SCHEDULE's own payload and the date made concrete. It is measured by a dry run of the
  pin's `run_dag` / `continue_open_cursors`:
  - nothing runs;
  - there are 0 open cursors;
  - `detail.ai` reads SKIPPED_EXISTS / "scheduled";
  - zero writes.
  This proves round 6's two defects are closed on the deployed path. The vendor-call branch is proven offline (sa-1 AC1/AC2), and the
  organic 2026-10-05 09:00 ET sweep is its acceptance. That is round-6 ruling 2, applied correctly: no past day was rebuilt to
  manufacture a vendor call.
- **The served delta at the pin,** compared with the served page:
  - 13 of 13 funds, 213 trades, 12 AI cards;
  - bytes 1,886,555 (10.0% headroom);
  - visible `UNRESOLVED` 94 -> 0, and bare `fear_greed` 4 -> 0;
  - census holdings missing 4 -> 0, and sector missing 185 -> 150.
  - The raw-ticker count rises, explained: re-wrapped cells, plus holdings cells that were EMPTY and now show the page's one name.
  - One per-fund decrease (PCLG census groups 6 -> 2) is the panel split, not a loss.
- **Writers:** one seat. The vehicle is the only Bloomberg writer.

## Changes to the COO half (binding)

1. **P3 rollback is a RE-PUT, never an S3 delete.** The prior rv-publish-1002r6 objects' bytes are re-put as newer revisions, then
   one publish. This is this seat's round-6 change 1, carried; the half reintroduced the delete wording.
2. **P5 is reverted at once if P1 fails.** If the apply does not land, `enrichment_bloomberg.py` is reverted in CLOUD in the same
   session, not "by 2026-10-05 06:00 ET". This is round-6 change 3, carried.
3. **P5's vendor scope is `4.0.0_SA_CRO~RV`'s call, and this half signs P5 CONDITIONALLY on it.** Adding LONG_COMP_NAME to the
   vehicle's Bloomberg reference request, and the issuer's one live read-only proof request before 07:00 ET, are Bloomberg use.
   - Whether they ride rivalfunds' existing Bloomberg word (R-21) is an ETFS_RIVALS open call, adjudicated by CRO~RV, not by this
     seat.
   - Until CRO~RV confirms in writing, P5 does not run: `enrichment_bloomberg.py`'s nm-2 change is reverted in CLOUD before 08:03 ET
     on 2026-10-05.
   - P1-P4 do not depend on it.

## Conditions

1. **The gates as written:** nothing in flight, live CodeSha256 equal to round 6's set, and the saved plan reading exactly 0/6/0.
2. **Post-act reads from the SERVED state:**
   - the five CodeSha256 values equal the plan's;
   - the schedule input reads `run_path: "scheduled"`;
   - the 10-02 page matches the table, with the manifest's run_path "ad_hoc" and no `research_hypotheses_run`;
   - act 4's response reads SKIPPED_EXISTS / "scheduled" with zero writes, read back as a store listing before and after.
3. **The +2 missing prices (42 -> 44)** are a measured regression with an inferred cause (cg-1's window alignment). `3.0.0_SA_CVO~RV`'s
   J1 names the two securities and confirms the cause on the served page. A wrong inference is a round-8 row, not a rollback.
4. **NEVER-2:** the entry opens before act 2 and closes after act 4's read-back.

**CTO HALF: SIGNED** for acts 1-4 (P1-P4) at pin CLOUD 75ad1e4d2e, with changes 1-2 binding. **P5 is signed CONDITIONALLY**
(change 3): it waits on CRO~RV's written scope confirmation, or it is reverted before 08:03 ET on 10-05.
