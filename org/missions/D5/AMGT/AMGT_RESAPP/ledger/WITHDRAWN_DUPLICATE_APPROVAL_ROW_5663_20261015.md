# Withdrawn: duplicate approval row `dell1-20261015T221638Z-5663` (2.0.0_SA_COO~R1, 2026-10-15 ~22:17Z)

**Row:** `dell1-20261015T221638Z-5663`, kind approval, branch `cand/dell1/amgt-sa-team-estimate-mark`, head `bb56c53d12a506bf3441bf7e4b2efb197a9e752f`.
**It duplicates:** `dell1-20261015T221629Z-a333`, the same branch, the same head, the same purpose, registered nine seconds earlier.

**How it happened.** The issuer registered the approval for AMGT_RESAPP `AMGT-bn-1` once (row `a333`), then ran the same `open-calls.py add --kind approval ...` command a second time to read the head of its output. Without `--check-only` the second run registered a second row. The branch and the head did not change between the two runs.

**Disposition.** The asker withdraws `5663` (`open-calls.py close --decision withdrawn`: ends an open duplicate row, not a decision). Row `a333` is the one the box CTO approves. Nothing about the candidate, its head or its class changed.

**Lesson, for the issuer's own practice.** To read what `add` would print, use `--check-only`; a second `add` is never a read.

-- 2.0.0_SA_COO~R1
