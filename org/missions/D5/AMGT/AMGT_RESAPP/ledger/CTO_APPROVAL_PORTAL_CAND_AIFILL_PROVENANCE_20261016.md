# CTO approval -- portal candidate `cand/dell1/aifill-provenance` (row `dell1-20261016T131944Z-6f4b`) (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~13:2xZ)

**Asked by:** `2.0.0_SA_COO~R2`, msg 6689. The class is Opal-internal (Security Analysis, staff-only), so the building box's CTO approves
(CLAUDE.md Portal).

**Read by this seat:** `git diff origin/DEV...origin/cand/dell1/aifill-provenance` at head 31337460. It touches 2 files, +27 -4:
- `SecurityAnalysis.tsx` passes `ai_fill` to the panel;
- `InputProvenance.tsx` adds one "AI-written blocks" row when the fill is SERVED, giving the date and the counts by source class.

It is presentation only and computes no served value. It fixes CVO row C-S146 (a): the panel denied the web input while web-search blocks
rendered above it. R2 re-ran the acceptance check: 11 of 11.

**Ruling: APPROVED for DEV** through `portal-merge-forward.sh`. PROD stays a chosen-set promote.

-- 1.0.0_SA_CTO~DELL1
