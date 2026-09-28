# 2.0.0_SA_COO~M -- IRPT_BCKEND~M session close (reboot checkpoint), 2026-09-25 19:00Z -> 2026-09-28 14:15Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, VALIDATE, COORDINATE

Seat 2.0.0_SA_COO~M on lease IRPT_BCKEND~M (FAST, /closer-drive). The goal is
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_224xZ_COO_M_GOAL_HOLDINGS_SNAPSHOT_MODEL_OVERLAY_LOOP_20M.md`,
and it is done when /verify is SOUND. This log is the reboot-checkpoint log that CTO msg 102346 asks for (record @6abf6b9c2a).
The window holds 116 commits by this author since the prior log
(`logs/2026-09-25/irpt_m_holdings_producer_cot_classes_labels_0020Z-1900Z.md`).

## Andrew-direct in window (verbatim, recorded)

- "VNQ is alternatives, it's a REIT". Recorded @65cf24d6af.
- "we should bring all these onto main branch", then "rec approved" (option b). Recorded @2c0624a986.
- The following arrived via the CTO:
  - "call 1 yes": the Comparison/Multi-Comp permission.
  - "The only classification table that matters is whatever ETFClassifier is connected to ... THat is the canonical table." Recorded @871b7458ec.
  - "Purge now, then push".
  - The reboot checkpoint, recorded @6abf6b9c2a.

## Work landed (see commit messages for per-file detail)

| Item | Result | Commits |
|---|---|---|
| Goal /verify on ~D's firm-tab HARs | MECHANICAL PASS, DECLARATIVE PASS, BROKEN@SEMANTIC on COT: the BD cash line is served as equity. The fix is served at R4 publication | 5e76b53fbc |
| COT cash-line act (D_03 `positive_rows`) | On irpt-m-cot-cash-line-act @0deac23f1e. Half request addenda 2-7. HELD by S173 | e41d507767, 9926d14a9d, dda9a80465 |
| S155 (was S152), COT mix_views admits cash/other | Re-cut alone on irpt-m-s152-cloud @ff63895521. Period-view identity recorded | 9926d14a9d |
| ~X's surprise rows landed under free ids S153-S156 | done (CTO 101771) | 92244581d2, 4f5b957ab5 |
| UIC-16: account type in full | irpt-m-uic16 @9ddc01dbc5. directory_runner.py is generator output | 15dec62901, 9ddc01dbc5 |
| Comparison catalogue v2 validated, and its consumer | Consumer at @d7c97910d9. Firms are resolved through lookup(). Shipped in ~Y's GRANT release | 176f783d9c, a450dc4cf2, 3b9b0bd9b0 |
| S173 ARMED: the COT gold host cannot read bd-securities, so every run classifies with empty maps | Row filed, and the Monday COT acts are blocked | 4b099fc076, ba3461598d |
| etf-classifications coverage census | Covers COT 39.7% and BD 68.1% of served dollars. No firm-tagged attribute | 9ab15461ca |
| R4 Holdings code: cash rule + UIC-16 | Merged into CLOUD locally | d306d972f6, a57537bd8a, dfb62b349d |
| R4 N1: cross-firm principals over SSM | 4 of 4 correct: cross-firm refused, own-firm allowed. Ledger CLOSED | 95ec2ca2dc |
| R4 enable diff re-run on 09-28 | 0 node/amount changes. Labels 2,970/875/755; classes 123/30,881/2,577 | c1ed5b9e1b |
| STATUS~M checkpoint | post-reboot order written | eabff0c495 |

## Deployment Sequence + Verification

There were no deploys in this window. The one live act was N1 under ledger irpt-holdings-principals-dispatch-m-20260925. It ran over SSM on the runner host, command da369659:
- COT principal on opal-data-bd: refused.
- 49F principal on opal-data-cot: refused.
- Each principal on its own firm: allowed.

The ledger is CLOSED @95ec2ca2dc.

## MCP traffic

About 60 messages were handled. The significant ones:
- **CTO rulings:**
  - 101700: S152 tolerance.
  - 101771: renumber.
  - 102106/102111: UIC-15/16.
  - 102169: firm lookup.
  - 102293/102323: R4 proceeds as signed; the re-point of all three producers to etf-classifications waits for the POSN fill.
  - 102342: N1.
  - 102346: reboot.
- **MSTR:** 102312/102332, freeze narrowed; only pushes stay frozen until CLOSE.
- **CRO:** today at 14:09Z I told the CRO that the R4 enable packet moves to after the reboot.

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| commit-gate (py_compile, ruff, ds-precommit, LGIC naming) | PASS after fixes | Refused typed firm ids twice and an edit to a generated file. Fixed with lookup() and generator output |
| surprise-row-gate | PASS with audited override | Needed for landing ~X's foreign rows |
| owned-paths gate | WARN | Refused my copies of ~X's deliverables. They ride ~X's branch drain |
| pytest (Holdings, _scope, COT gold) | PASS | 284 passed on the R4 branch; _scope 206 passed |
| holdings_publication_diff_classes / account_mask_publication_diff | PASS | Pinned diff at c1ed5b9e1b |

- **What worked:** generator output and lookup() clear the naming gate without a workaround.
- **What failed:** `git apply` with bad arguments hung and was stopped.
- **Gap found:** the stale COT gold host role (S173) was invisible in the served output. Only the run logs showed it.

## Blockers

- **BLOCKED (evidence S173, 4b099fc076; CTO 102323):** the COT cash-line gold act, Part 2, runbook A/B/C and ETF B2. They wait on the POSN fill of etf-classifications and then the one re-point act with halves.
- **BLOCKED (MSTR 102332):** no push until MSTR's purge CLOSE.

## Current State

- **CLOUD (local, unpushed; purge pending):**
  - R4 Holdings code @dfb62b349d. It contains the `holdings_snapshot.classify_security` cash rule and UIC-16 in `holdings_snapshot.py` and `directory_runner.py`.
  - The N1 ledger is closed @95ec2ca2dc.
  - The diff is at `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R4_ENABLE_DIFF_20260928/`.
- **Worktrees, all clean at this log:**
  - `../ajb_irpt_m_r4` @a57537bd8a
  - `../ajb_irpt_m_uic16` @9ddc01dbc5
  - `../ajb_irpt_m_cmp` @d7c97910d9
  - `../ajb_irpt_m_s152c` @ff63895521
  - `../ajb_irpt_m_cashline` @ccb9b38dd8
- **Records:**
  - `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/`: MONDAY_20260928_RUNBOOK.md, ETF_CLASSIFICATIONS_COVERAGE_20260928.md and VERIFY_HOLDINGS_GOAL_20260924.md.
  - STATUS: `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~M.md`.

## Next Steps

1. After MSTR's CLOSE: re-sync the worktrees to the rewritten CLOUD with `git reset --mixed HEAD`, per MSTR's CLOSE steps.
2. R4, after the reboot:
   - Re-mint the Holdings packages and the directory bundle under ledgers.
   - Run one QA fire of irpt-holdings-refresh-lambda.
   - Re-read the diff at the QA as_of.
   - Send the ENABLE half to [1.0.0_SA_CTO] and [4.0.0_SA_CRO].
3. Re-run the goal /verify after R4 publishes COT's `CASH -- CASH` as cash.
4. S173: re-point COT gold, BD gold and Holdings to etf-classifications as one act with halves, after the POSN fill. [0.0.0_AB_MSTR] routes the fill to the POSN owner.
5. Drain: ~X's branch and irpt-m-cot-b1 (B1 ledger). Drop ~X's duplicate S150-S153 rows at that merge.
