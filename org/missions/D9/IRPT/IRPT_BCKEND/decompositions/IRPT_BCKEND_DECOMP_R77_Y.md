# IRPT_BCKEND round 77 -- workstream ~Y decomposition (release 6: the custody factory goes live)

Issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~03:2xZ.

**Pair:** `deliverables/2.0.0_SA_COO~Y2/release6_custody/NEVER_WIDEN_PAIR_RELEASE6_CUSTODY.md` (blob a3c54ba263). This issuance signs
the COO half.

**CTO half:** `deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_YCG_RELEASE6_CUSTODY_CTO_HALF.md` @96e03f8ba1, GIVEN (msg 2269). Its
conditions:
- release 5b is live first;
- the symbol closure is re-run on the uploaded zip;
- the policy reads back with exactly the 11 ARNs;
- the read-3 objects are listed for Andrew's delete word;
- the IAM write is reported via `0.0.0_AB_MSTR~DELL2`.

The E2a principal (`svc-custody-statement`) is ~K2's, under its own pair. This release grants it nothing.

**Source:** round 76 (IB-yr-761, drained @2ae4d86e00). Pin `bea2a2ceb3`, on origin (fetched read).

**Applier:** `0.7.0_AE_CloudOps~DELL2`, queued BEHIND `TO-APPLY-Y75` (release 5b). Its step 0 refuses unless live reads `5FRkux2o...`.

ONE issuance, one cell, no edges.

| item | cell | cut? |
|---|---|---|
| Release 6 apply (code, the custody-factory policy, the pandas layer) and after-reads 0-4. Roll back to `5FRkux2o...` and revert the policy and layer on any failure. | `IB-ya-771` (was `APPLY-Y77`) | **CUT** to `0.7.0_AE_CloudOps~DELL2` |

| criterion | invocation | base reading |
|---|---|---|
| Y77-1-AC1 | `python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~Y2/checks/r77/y77_cells.py . Y77-1-AC1` | FAIL (no file) |
| Y77-1-AC2 | `... y77_cells.py . Y77-1-AC2` | FAIL (no file) |
| Y77-1-AC3 | `... y77_cells.py . Y77-1-AC3` | FAIL (no file) |

Risk WORLD.

## Four-postulate record

(i) Domain: one function, one inline policy and one layer. (ii) One release. (iii) One intent: a Performance client statement
submission is accepted, not refused. (iv) The prospect path, every other function and every other policy do not move.

fanout: 1 of 1 chains, cap 8, reason: one item.

**AMENDMENT (issuer `2.0.0_SA_COO~Y2`, 2026-10-09 ~10:5xZ, rows IRPT_BCKEND-D2-S21 and the applier's msg 3172):** cell `APPLY-Y77` is registered as `IB-ya-771`, an id
matching CELL_ID_RE, so `proof-of-spec-check` and `to-decomp-ref-lint` can join it. Same cell, same scope.
