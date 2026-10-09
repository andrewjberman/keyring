# IRPT_BCKEND rounds 72-75, workstream ~Y -- L8 COMPILE (release 5 branch B, the co-change repair, release 5b, and X-1 proven)

**By** `2.0.0_SA_COO~Y2` **for** `3.0.0_SA_CVO`, 2026-10-09 ~11:0xZ. Risk WORLD.

`round-close-check.py --project IRPT_BCKEND --workstream ~Y`, rounds 72, 73, 74 and 75: MAY-CLOSE each. Round 73 carries 1 order (complete).
The apply orders sit outside the round scope.

## Round 72 -- release 5, branch B

`TO-APPLY-Y72` ran, and read 4 FAILED: `RetentionPolicy.reference()` arity, because commit `f60e6f1d2a` shipped split
(row `IRPT_BCKEND-D2-S18`). It rolled back the same session to `Un0wVZqj...` (issuer re-read), and the filer was deleted. The order is CANCELLED by
issuer ruling.

## Round 73 -- the co-change repair (`IB-yr-731`, complete, drained @328b73d536)

- **The new instrument:** `deliverables/2.0.0_SA_COO~Y2/checks/r73/cochange_closure.py`. It flags a commit shipped through one staged row while
  another row it touches lags. Base `split=3`, then 0 after.
- **The re-pin:** `retention.py`, `reporting_policies.json` and `ExportBundle.schema.json` re-pinned to `2f3ee8c15b`.

## Rounds 74 and 75 -- release 5b (`TO-APPLY-Y75`, cell `IB-ya-751`, COMPLETE @634da92d06, proof VALID)

**Pair:** `release4_ycg/NEVER_WIDEN_PAIR_RELEASE5B_E11.md`, both halves signed. **Pin:** `328b73d536`, built in a detached worktree at the pin
(AMENDMENT 1), because HEAD had moved to release 6.

**Live:** `5FRkux2o...` at 04:13:59Z. Read 1 re-plan 0, read 2 census `failed {}`, read 3 offline suites pass.
- Read 4 (the X-1 actor) admitted NORMALIZED, with 9 keys.
- Reads 5-7 refused as required.
- The ledger is CLOSED.

**X-1 PROVEN.** The laptop read-back, on keys v3 @4bcebfcb09, returned all TRUE:
- body sha;
- owner firm 49financial;
- owner class `FIRM_ADVISOR`;
- owner label, computed from `principal_id`;
- the acting principal is the filer.

The first two read-backs were not defects: v1 compared the raw owner against the label, and v2 found no email field because `principal_id`
holds the email.

**Cleanup** under Andrew @35fabf20c8: 7 DDB rows and 2 S3 versions deleted, and dell2 re-read both versions absent. Result
`r75/Y75-1_laptop_cleanup_result.json` (sha256 26fbc10f0f87). Row `D2-S17` is closed by `D2-S42`.

**Grades** (`checks/r75/y75_cells.py`, AMENDMENTS 1-3): Y75-1-AC1, AC2 and AC3 PASS. Live has since moved under LATER signed releases of the same
function (IB-pr-390 `ZA0QJ5Wt`, release 6b `tdpterTM`), and the check admits exactly those two.

## Carried, not in these rounds

- **Release 6b** (`TO-APPLY-Y77`, `IB-ya-771`) is LIVE at `tdpterTM`. AC2 and AC3 PASS. AC1 waits on read 5a, the acceptance record's `ticket_id`,
  graded through IRPT_ANLREQ `TO-APPLY-Y1` read 4.
- **Rows filed and disposed:** `D2-S21` (the apply cell ids; fired at the Y75 flip, fixed @7d4318cd3e), `D2-S35` (disposes `D2-S31`) and `D2-S42`
  (disposes `D2-S17`).
- **Open item:** Andrew's word for the S3 deletes of 6b's reads 4-5 prospect objects. They are not yet keyed by name; the laptop can map them.
