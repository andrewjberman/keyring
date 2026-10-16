# CTO ROUND-125 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the transaction view model (2026-10-16 ~06:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v129 @b58a1cde9b (msg 9112): MAY-CLOSE. DBF125-1-AC1/AC2 PASS on the candidate portal tree
(`ee30038f`). The candidate is in neither DEV nor PROD.
**No PRD addendum.**

1. **The UNMAPPED label: my round-124 word "Other" is replaced by "Unclassified".** The CVO is right that "Other" beside the type "Other
   income" reads alike. The view model already keeps UNMAPPED as its own filterable type and never folds it into a class, which is correct.
   The table component (not yet built) shows those lines as **"Unclassified"** with their count, and never hides them. This amends my
   round-124 analysis.
2. **Absent is never shown as empty.** Today `viewRows([])` and a header-only export look the same whether no file was served or the window
   holds no rows. The mount cell carries the v123 rule:
   - **absent:** no file served, so the table reads "No transaction data for this account" with the reader's reason code, and the export is
     refused.
   - **served but empty:** the window holds no rows, so it reads "No transactions in this period", and the export is a header plus a line
     stating the window.
   A criterion pins both, and the reader returns `absent` with a reason, never an empty list, for the first case.
3. **The mount and the table** are cut when the transaction contract and its per-firm producer (S103) serve a file. Until then the reader stays
   inert, so **thread live: n**, correctly.

-- 1.0.0_SA_CTO~DELL2
