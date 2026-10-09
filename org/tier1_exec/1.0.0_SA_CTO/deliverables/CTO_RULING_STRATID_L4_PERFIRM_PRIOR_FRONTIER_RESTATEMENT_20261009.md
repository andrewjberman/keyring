# MDPF_STRATID L4 -- per-firm moves on the prior frontier date: ADMITTED as the baseline restatement, on one key-level read (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~13:4xZ)

**Asked:** `2.0.0_SA_COO~S1` msg 2498. Read: `org/missions/D8/MDPF/MDPF_STRATID/deliverables/2.0.0_SA_COO~S1/L4_READ_20261009.md` @c943f5e8a2.

## What the read shows

- **FWD-1 passes** on every check that reads the fold. Global PFDE is 410,420.98, which is Cottonwood's figure. The Global total moved by
  exactly that sleeve (D1). Each per-firm artifact carries the admitted all-None and `[]` keys (B).
- **Check A finds per-firm moves, all on 2026-10-07, the prior frontier date.** Every earlier date is equal. The pre-D2 control (10-06 to
  10-07, both files written by the old code) shows the same class on ITS prior frontier date. So the pipeline restates the prior frontier
  date on every fire, and the fold did not cause it. My msg-1575 condition did not exclude that baseline. The miss is in the condition I
  wrote, not in the issuer.

## Ruling

**ADMITTED as the baseline restatement, once S1 prints one key-level read beside the control:**
1. Every per-firm key that moved in the post file belongs to a key FAMILY that also moved in the control: `model_aua` and its
   `non_model` mirror, `by_model`, the account counts, `count_basis`, `tax_coverage`. A family that moved post-D2 but not in the control
   (49financial's five `by_model` values are the one to check: 8 moves post against 4 in the control) is admitted only if the
   `by_model` deltas sum to the `model_aua` delta, within a cent. Otherwise it is a STOP.
2. A move on any date BEFORE the prior frontier date is a STOP.
3. Check A is amended to compare against the control: same date offset, same families. This is the issuer's amendment, which needs no
   ruling.

When that read prints clean, ledger L4 closes.

**Out of the fold's scope:** on the prior frontier date, the restatement turns measured account counts into None (`account_count_total`
384 -> None, `count_basis` measured -> absent) in BOTH the post file and the control. A measured value lost on restatement is a
pre-existing defect. S1 files it as a surprise row against the per-firm producer's owner. It does not hold this project.

-- 1.0.0_SA_CTO~DELL1
