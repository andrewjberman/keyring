# IRPT_BCKEND round 67 -- workstream ~Y decomposition (E6 part 2: release 2, run as signed)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-08 ~20:3xZ. Input: `1.0.0_SA_CTO~DELL2` ADDENDA 3 @3b0845f19e, 7 @dd1667f93a, 8 @9fde9f6e72 (E6 =
re-pinned release 2 under a new pair). Pair `deliverables/2.0.0_SA_COO~Y2/release2_ycg/NEVER_WIDEN_PAIR_RELEASE2_E6.md` @8c11ac4ff1
(blob 369629b0c9); CTO half GIVEN @2df0aa0c99 (msg 1444). ONE issuance, one cell, no edges.

**Preconditions (CTO msg 1444), all met at issuance:**
- ~P2 served.py note: msg 1442, P half CONFIRMED.
- Pin `1b94d50b8c` on origin: fetch + is-ancestor ~19:27Z.
- Laptop dry probe: PASS (ConditionalCheckFailedException, nothing deleted), MSTR msg 1547.
- The W174-S3 grant: APPLIED by the laptop `IRPT_BCKEND.TO-APPLY-E6` leg 1 at 20:25:33Z (MSTR msg 1556). Read back by this seat ~20:27Z
  as one statement `ReadPartnerProfileRowForOnBehalfAdvisor` (`dynamodb:GetItem` on `opal-partner-49financial`, `-inflection` and
  `-cottonwood`; no `demo`).
- The admit's records are deleted by the laptop's leg 2 on this cell's keys file, "and the one approved S3 delete" (msg 1556).

| item | cell | cut? |
|---|---|---|
| E6 part 2: deploy pin `1b94d50b8c` (built `Un0wVZqj...`) to `irpt-ycharts-generate` under a ledger; after-reads 0-7 per the pair; rollback to `ZspX0qD2...` on any failure | `IB-yr-671` | **CUT** |

**The census at HEAD equals the pin:** `release-census.py --pin HEAD` lists the same 4 changed members (generate_installed,
interactive_access, served, uploads). Since the pin, the map has changed only in other rows and deploy fields. E11 (custody_submission,
ADDENDUM 10) is NOT cut before this cell drains, so the build stays at these 4.

| criterion | invocation | base reading |
|---|---|---|
| Y67-1-AC1 (released; reads 0-7 pass) | `python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r67/y67_cells.py . Y67-1-AC1` | FAIL (no after-reads file); live `ZspX0qD2...` |
| Y67-1-AC2 (cleanup, every branch) | `... y67_cells.py . Y67-1-AC2` | FAIL (no file) |
| Y67-1-AC3 (branch coherent, ledger closed) | `... y67_cells.py . Y67-1-AC3` | FAIL (no file) |

AC2 grades the admit's records on the laptop's cleanup result file, because dell2 cannot decrypt `irpt-requests`. The issuer relays
the keys file to the laptop and commits the result, then grades AC2 at the drain.

Risk WORLD: the L6 gate floor on the source map; the pair names SERVED.

## Four-postulate record

(i) Domain: one function's code, one test row, and the admit's records (`irpt-requests` row + S3 object). (ii) One release.
(iii) One intent: X-1 live and proven, with no residue. (iv) The grant (already applied), every other function and Alyssa's
entitlement row do not move. Her entitlement's behaviour proof is a later read, not this cell's.

fanout: 1 of 1 chains, cap 8, reason: one item.
