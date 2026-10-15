# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PH, the exemption wired with its listing; the 49 Financial split adjustment)

<sweep_watermark>2026-10-15T14:52Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T14:52Z, on msg 8337 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PH_DRAIN_END_20261015.md` @986c1f0e5d). Two orders: IB-pr-577 (risk WORLD) merged @95ca50c91e, and IB-pr-578 (risk LOCAL) merged @07f60f52f3. Both were issued @476d0ed981 and are complete. Re-run here at HEAD: IB216-1-AC1..AC3 and IB216-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 1 --workstream "~PH"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**(1) Wired WITH the listing: v119's silent-drop risk is closed at HEAD.** `run_firm` now hands the gate `absent_at_source_evidence=_absent_provider(absent_captured, firm_id, inputs, snapshot, served)` (`holdings_snapshot.py:3477`). The block `ABSENT-AT-SOURCE-B` (`:3086-3286`) keeps an exempted account in the served snapshot as a zero-value node carrying "Not reported by the custodian since <date>", with no current amount. The published manifest (`publication.py`) records it as `absent_at_source` with `absence_claim` measured and `closure_claim` unknown. The "closed" names are renamed (`test_no_closed_names_remain`). The live-account-dropped branch from v117 is covered IN CODE: `test_reappearing_account_is_included_normally`, `test_second_fire_exempts_again_with_the_same_since_date` and `test_run_firm_publishes_with_the_account_still_listed`, plus fail-closed loaders (`test_loader_error_keeps_the_refusal`, `test_evidence_missing_prior_partition_fails_closed`). Its SERVED effect still needs the dry run and the never-widen pair the packet names as next. That pair must state the household-total change for both branches (closed; live and omitted). Held: D2-W420-S1 (ARMED, `~P2`): the exemption's prior-day reads are not in the manifest's source objects or the source-set digest, so receipts must cover them before release to a firm.

**(2) The split adjustment, read in the bytes.** At base, line 816 of `holdings_performance.py` printed `* (g0.loc[earning, "_p1"] / g0.loc[earning, "_p0"] - 1.0))`. At HEAD the same expression sits at line 990, and the fix is upstream of it. The new `SPLIT-ADJUST-A` block (`:958-969`) divides `_p0` by the measured ratio for a security with status OK and sets it to NaN (unpriced, excluded) for `SPLIT_RATIO_ABSENT`. So the factor now multiplies a split-restated basis. Keyed only where the key exists: `sources.json` declares `split_adjust` on ONE entry, `schwab_08335338` (49 Financial: `tran_srcde`=`STK`, "STOCK SPLIT" text, `cusip`, 0.5 percent clean-ratio tolerance, 90 percent agreement). The `orion` (Inflection) and `blackdiamond_z09` (Cottonwood) entries carry none, and the diff touches only the 49F entry. Held: D2-W421-S2 (ARMED, `~P2`): the ratio applies by identifier, which falls back to `ticker_symbol` when `cusip` is blank, so a split holding with a blank cusip would not be adjusted.

**(3) The 21 failures, compared by test id.** Both suites were run here in two clean detached worktrees, base @476d0ed981 (the round's issuance) and HEAD @2982fd8c55 (which contains both merges); the worktrees were removed afterward.
- `data/assets/scripts/gold/investor_reporting/tests`: base 21 failed / 443 passed; HEAD 21 failed / 457 passed. The failing ids are IDENTICAL: 0 new at HEAD, 0 fixed.
- `data/assets/scripts/gold/irpt_holdings_performance/tests`: base 60 passed; HEAD 73 passed; 0 failures.
- `infra/aws/lambda/investor-reporting/holdings`: base 182 passed; HEAD 182 passed.

No new failure hides in the count. The 21 pre-existing failures are not this round's and are unowned here.

**(4) Nothing deployed, read live.** The three holdings bundles still read oyIYMVdh (2026-10-09T10:29:07Z), UHOCIkWj (2026-10-13T13:35:24Z) and PzhCs97q (2026-10-13T13:36:08Z), unchanged from v118. `irpt-holdings` (which packages `publication.py`) was last modified 2026-10-13T12:47Z, and its deployed `publication.py` is the base blob 9b169a9e, not HEAD's e5775f94. `irpt-holdings-performance-lambda` was last modified 2026-10-15T06:06Z by IRPT_DASHBD's DB-c-9 (the shared zip, member diff exactly `handler.py`, ledger CLOSED). Its deployed `holdings_performance.py` is blob ccd1d988 = the base (commit 718716fb60), with 0 `SPLIT-ADJUST` lines. So the split adjustment is NOT live.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S28",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T14:52:00Z",
  "one_line": "Round 1 ~PH. (1) run_firm passes absent_at_source_evidence (holdings_snapshot.py:3477) and an exempted account stays listed as a zero-value node 'Not reported by the custodian since <date>' (closure_claim unknown): v119's silent drop is closed at HEAD; the live-but-omitted branch is covered by tests (reappearing account included normally), its served effect still owed to the dry run and pair. (2) Base line 816's p1/p0 factor (now line 990) multiplies a split-restated p0 (SPLIT-ADJUST-A :958-969); split_adjust declared on schwab_08335338 (49F) only, orion and blackdiamond_z09 untouched. (3) Failing ids compared at base 476d0ed981 vs HEAD 2982fd8c55: the same 21 in investor_reporting/tests, 0 new, 0 in the other two suites. (4) Nothing deployed: bundles, irpt-holdings publication.py and irpt-holdings-performance-lambda's holdings_performance.py are all base bytes (read live). 6 of 6 criteria PASS. Dismissed (5): D2-W420-S2, -S3, D2-W421-S1 (BLOCKING, INERT; ruled by amendment @7c8acc5500), -S3, -S4 (readings or issuer defects fixed). Held: D2-W420-S1, D2-W421-S2, D2-S202 (~P2).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W420-S2",
   "IRPT_BCKEND-D2-W420-S3",
   "IRPT_BCKEND-D2-W421-S1",
   "IRPT_BCKEND-D2-W421-S3",
   "IRPT_BCKEND-D2-W421-S4"
  ],
  "spec_asserts": "ADJUDICATION_v117/v119 conditions (no silent drop; the live-but-omitted branch covered); CLAUDE.md rule 22a (deployed bytes compared by content to the build input); a 'same failures at base' claim is graded by test id, not by count.",
  "world_is": "At HEAD the exemption is wired with its visible listing and the 49F split adjustment is built; neither is deployed. Before either moves served numbers: a producer dry run measuring the exemption alone per firm and the split adjustment before and after, then never-widen pairs covering both branches, the receipts covering the exemption's reads (W420-S1), and the blank-cusip ticker fallback (W421-S2).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T14:4xZ of the invocations in IB-pr-577 and IB-pr-578: IB216-1-AC1..3, IB216-2-AC1..3 PASS, exit 0 each; round-close-check ~PH round 1 MAY-CLOSE",
    "holdings_snapshot.py at 2982fd8c55: :3086-3286 ABSENT-AT-SOURCE-B, :3477 run_firm passes _absent_provider; tests/test_absent_at_source_wiring.py test names listed",
    "git show 476d0ed981:data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py line 816 printed; HEAD :958-969 SPLIT-ADJUST-A, :990 the factor",
    "sources.json at HEAD: split_adjust only under schwab_08335338; diff 9a6cf90e04..07f60f52f3 adds lines in that entry only",
    "pytest in detached worktrees at 476d0ed981 and 2982fd8c55: investor_reporting/tests 21 failed each, comm of FAILED/ERROR ids: 0 new, 0 fixed; irpt_holdings_performance/tests 60 vs 73 passed; infra/aws/lambda/investor-reporting/holdings 182 vs 182 passed",
    "aws s3api head-object of the three holdings bundles (unchanged); aws lambda get-function irpt-holdings (LastModified 2026-10-13T12:47:20Z; publication.py blob 9b169a9e = base) and irpt-holdings-performance-lambda (2026-10-15T06:06:08Z; holdings_performance.py blob ccd1d988 = base, 0 SPLIT-ADJUST lines)",
    "org/critical_paths/change_management/20261015T0423Z_irpt-dashbd-cottonwood-holdings-performance-20261015_deploy_completion.md: CLOSED, member diff exactly handler.py",
    "investigation rows D2-W420-S1..S3, D2-W421-S1..S4, D2-S202",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PH_DRAIN_END_20261015.md @986c1f0e5d (msg 8337)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings and issuer defects fixed by amendment. The receipts gap, the blank-cusip fallback and the round's disposition row stay held with ~P2 before any release."
 }
]
```
