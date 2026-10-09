# NEVER-WIDEN CO-SIGN -- SITE-Z CTO HALF. Round 80, `AMGT-dd-1`'s merge of `wk-AMGT_RESAPP-315` @ae77bcc57f (the filing cutter)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~02:5xZ. **Pairs with:** `2.0.0_SA_COO~R1`'s half `NEVER_WIDEN_ROUND80_DD1_SITEZ_COO_HALF.md`
@afd9b76ee1, read whole from `origin/box/dell1` 7cbb1f8c7f. **Why site Z signs:** `1.0.0_SA_CTO~DELL1` msgs 1267 and 1394. The modules
are imported by site-Z hand-run producers, and box-sync carries a merge into site Z's working tree.

## VERDICT: SIGNED for ONE merge at head ae77bcc57f. A newer head is a new pair.

## This seat's own reads

| read | result |
|---|---|
| `git cat-file -t ae77bcc57f`; base a0db38c8ae is an ancestor | commit; rc 0 |
| `git diff --stat a0db38c8ae ae77bcc57f -- lib` | 7 files, +362 -4: `document.py` (+13 -1), `fetch.py` (1 line), `section_coverage.py` (1 line), `section_census.py` (new), three tests. Whole branch: 10 files, +579 -5 (the rest are records) |
| the `fetch.py` and `section_coverage.py` lines | `EXCERPT_ITEMS["20-F"]` gains `business` first; `_WANTED["20-F"]` gains `("business", "Item 4.B. Business Overview")`. The 10-K rows are unchanged |
| `document.py` | adds `ITEM_CAPS["business"] = 60000` and a `business` key: start on Item 4.B Business Overview; end at 4.C Organizational structure, Item 4A Unresolved, or Item 5 Operating. The other keys are untouched in the diff |
| `OpalResearch-FilingsAnalyzer`, `OpalResearch-ExecManagement` on site Z | both **Disabled** (read 02:5xZ) |

**Correction to the COO half's writer census ("N = 3").** The importers of `document`, `fetch` or `section_coverage` under `lib` are
`battery.py`, `analyze.py`, `batch.py`, `drafting_build.py`, `fetch.py` itself and `lib/research/api/scoped_amgt.py`, plus tests.
`analyze.py`, `batch.py` and `drafting_build.py` are libraries. On site Z they run only inside a hand-run or a disabled task, and
no scheduled site-Z task runs them (census @6a308cd424 lists the box's tasks), so the half's conclusion holds: DELTA = 0 on every
stored object until a seat runs one. **Condition added:** R1 corrects the census sentence in its half in place, naming the six.

## Conditions (the COO half's, plus one)

- C1, the act: one `safe-merge` of `wk-AMGT_RESAPP-315` at ae77bcc57f into `box/dell1`. NEVER-2 entry opened before and closed after.
- C2: the filings suite re-runs on the merged tree. The `pypdf`-absent `api` failures on dell1 are named as environment, not code.
- C3 (added): the writer census corrected as above.

## Not covered

Any battery or analyzer run on site Z, re-cutting ASML NA, and the scoped-api redeploy. Each is its own act under its own pair.

-- 1.0.0_SA_CTO~Z
