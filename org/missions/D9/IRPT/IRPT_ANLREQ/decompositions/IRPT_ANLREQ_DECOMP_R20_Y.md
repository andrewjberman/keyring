# IRPT_ANLREQ -- decomposition, round 20, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** the CTO's round-20 analysis `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_20_20261013.md` (msg 6841) answering the round-19 slug, and the CVO's L9 grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_19_L9_GRADE_20261013.md` (AR194-y-AC4J FAIL). Enrichment list: (1) the backstop repair (W59-S1) with the CVO's negative controls, then r19.1's two-leg release; (2) the status rule's all-eight pair (W54-S5, W55-S1, W55-S25); (3) the portal notice for `SHEETS_NOT_READ` (W57-S5).

## Cells

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-y-211` | the r19.1 account-header backstop repaired (attribute words on the abbreviated root; a digits-only run needs a separator-free column), `READER_VERSION` r19.2, the CVO's cases as tests | `intake/template_reader.py` and its tests | LOCAL (built, not released) |
| `AR-y-212` | the status rule rebased on the LIVE packages of pin group A (`irpt-performance-adapter`, `irpt-narrative`, `irpt-status`): per function the live manifest, a holds-only control that reproduces the live CodeSha256, the release that moves `served.py` only, narrative's test staging moved to the new pin | the worker's deliverables, narrative's tests | LOCAL (read-only live read) |
| `AR-y-213` | the same for pin group B (`irpt-directory-search`, `irpt-ycharts-generate`, `irpt-export-render`, `irpt-holdings`, `irpt-49f-reporting-read-lambda`) | the worker's deliverables | LOCAL (read-only live read) |
| `AR-y-214` | a portal candidate that shows the `SHEETS_NOT_READ` notice on the upload answer's face, branched from `origin/DEV`, with a test that fails without it | the portal repository (a branch and a worktree outside the tree), the worker's deliverables | LOCAL |

## Edges and chains

- `AR-y-211`, `AR-y-212`, `AR-y-213`, `AR-y-214` are independent (four chains). `AR-y-212` and `AR-y-213` together feed ONE pair (the CTO: one `served.py`, both pin groups, together); `AR-y-211` feeds the r19.2 reader's own two-leg release. M = 4 chains.

fanout: 4 of 4 chains, cap 8, reason: four independent build-and-prove cells; the two status groups are split by pin group so each worker holds at most five functions.
