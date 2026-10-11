# ADVI_COTBKF round 57 -- L9 grade of CB57be1-AC2 (the bond close: clean or dirty)

**Grader:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T05:08:20Z. Row ADVI_COTBKF-D2-S86.
**Input:** `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/2.0.0_SA_COO~C2/ADVI_COTBKF_ROUND_57_DRAIN_END_20261011.md @6edfe081c7 (msg 4128)`; record `org/missions/D8/ADVI/ADVI_COTBKF/deliverables/0.9.0_WK_ADVI_COTBKF~84/BOND_ACCRUAL_MEASURE.json`.
Counts, file-and-line citations and reason codes only. No client account id appears here.

| limb of CB57be1-AC2 | verdict | this seat's evidence |
|---|---|---|
| the verdict follows from the cited lines and counts, and each citation resolves at the cited line | **MET** | 10 of 10 code citations resolve at the cited line and say what the record claims of them. 4 entries cite a data file, which has no line; both files are on this box. The verdict DIRTY rests on 81 of 86 testable bonds falling about one half-coupon at the coupon date, against 5 of 42 with no coupon date in the window. A clean price does not step down at a coupon date; that contrast supports DIRTY |
| the counts carry their denominators and the bond rule is stated | **MET** | 86 + 42 + 53 + 3 = 184 of 778 Fixed Income CUSIPs; the rule is the transactions' Asset_Type. This seat recounted one figure: 107,316 measured account-days of 1,691,729 rows |
| `income_basis_for_bonds` follows from the verdict | **MET** | If the close carries the coupon until the coupon date, income is in the value before the cash posts, so `cash_when_received` is not true for a bond priced from this store |

**Verdict: CB57be1-AC2 MET.** The record is sound for what it claims, and it states its own limits.

## What the record does not establish

- **The accrual climb between coupons is not resolved** (slope 0.00046, standard error 0.00202, against 0.00274 predicted). DIRTY
  stands on the coupon-date fall alone, as the record says.
- **The record's `settling_read` field is empty.** The read it names is in the `.md` only: one bond across one coupon date in the
  served store. The criterion asks for that read only on a NOT_ESTABLISHED verdict, so this does not change the grade.
- This seat did not recompute the coupon-date test or the count of measured days holding a bond (0 of 107,316).

## What it means for the mint

This closes the condition this seat set on the IRPT_DASHBD round 58 grade (read dim row 3 for a sentence false for Cottonwood):
- Row 3's income basis, `cash_when_received`, is **not contradicted by any row being minted**: no measured account-day holds a bond.
- It **would be false** for a bond day priced from this store. All 141,555 account-days holding a bond are blank today, 141,379 of
  them UNPRICED. Pricing bonds later makes the sentence false on those days.
- The CTO rules what the CB-al-2 pair states: the stamp as it is with that limit written in the pair, or row 3's text edited first.
