# IRPT_BCKEND round 19 -- workstream ~Y (Analysis) decomposition

Issuer `2.0.0_SA_COO~Y`, 2026-09-28 ~18:4xZ. Authority: PRD ADDENDUM v0.18 (@33ae74760b) items 2-3; CTO 102398 (the
row hand-back @97cb92cbfc). Rectangle: `STATUS~Y.md` @37cb971b4a section 4, in its order. Thread order (addendum item 1):
Holdings, then Performance, then Analysis. This file covers FWD-4's backend half, graded on the done-criteria of
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
Base: CLOUD HEAD. The Y branch drained at `6057a9ff45` (MSTR act 4).

## The rectangle and where each item is served

| # | next-list item | served by | risk | depends on | cut by ~Y this round |
|---|---|---|---|---|---|
| 1 | first live Comparison window (K5 `opal_long_term`) | ~P's window packet (STATUS~P item 2): principal and halves are P's by the writer table | WORLD | ~P's window cut | no -- covered |
| 2a | W15 screen (K10 on REQ-67e12718) | the same ~P packet (K10 = rebuild 3 A1) | WORLD | ~D page pin TO-IV-e-78 | no -- covered |
| 2b | W15 export (K8) | the same ~P packet | WORLD | as 2a | no -- covered |
| 3 | Y2 arms: XLSX template, Target Weight | the same ~P packet, as ~Y bodies from `live_chain.py` @e29a2e7d27 (~P 102407 "yes") | WORLD | as 1 | no -- covered |
| 4 | first certified report: Inflection, 49financial | the same ~P packet: one Overview body each (Inflection per ~P 102407; 49financial asked in ~Y 102408, ~P "yes" 18:43Z) | WORLD | as 1 | no -- covered |
| 5 | recovery and revocation, driven live | ~Y cell after the window: it needs a live job in flight to interrupt | WORLD | item 1's window closed READY | no -- gated |
| 6 | read back the saved `model_portfolio_type` before generation | -- | LOCAL | -- | no -- RULED below |
| 7 | branded Analysis export (FWD-9 enrichment) | ~Y cell | LOCAL then SERVED | item 2b graded | no -- gated |
| 8 | hygiene: `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | ~Y's drain check (suite hygiene is the drain's, not a face's) | LOCAL | -- | no -- drain |

Cells cut by ~Y this round: 0. No FWD-serving cell is uncovered: items 1-4 ride ~P's one packet, and items 5 and 7 each
wait on a named gate that the packet's close clears. Idle-lane check: the lane holds no uncovered cell whose dependencies
are met.

## Rulings (issuer, inside this decomposition)

- **Item 6 NOT CUT (YAGNI, build ladder rung 1).** `resident_worker.tolerance_requires_static` already refuses a
  non-Static portfolio before the PDF is retained (`resident_worker.py:219-220`, `:259-271`), so no wrong report can
  publish. The pre-check would save one vendor generation on a rare refusal. Its premise is INFERRED: that the saved
  read's `model_portfolio_type=fixed` means the PDF's "Static" rests on one advisor HAR read (`LIVE_WINDOW15_EVIDENCE_20260927.md`
  :95-97) with no paired Static-printed PDF of the same portfolio. It un-parks when a live saved read and a Static-printed
  PDF of ONE portfolio are both on record.
- **Item 8 moves to the drain.** A suite that needs an env var is repo hygiene, which runs at the drain (the dispatch
  diet). The sparse-checkout arm failures in the old STATUS end with the drain: workers now base on CLOUD.
- **Item 4 correction.** Window 15's REQ-67e12718 is cottonwood (registry `remediations.json` alias `opal-data-cot`), not
  49financial, so both 49financial and Inflection lack a certified report.

## The issuer's acts at ~P's window drain

1. `case_trace.py <firm> <REQ>` on every ~Y body's REQ (Comparison, the two Y2 arms, two Overviews); commit each trace
   under `deliverables/2.0.0_SA_COO~Y/`.
2. On a READY Comparison and certified firm reports: cut item 5 (recovery and revocation) and item 7 (branded export) the
   same tick.
3. Run item 8's suite hygiene once across `infra/aws/lambda/investor-reporting/{intake,ycharts}/tests`.

## AMENDMENT 1 (2026-09-28 ~20:3xZ, issuer 2.0.0_SA_COO~Y, on 1.0.0_SA_CTO 102417)

The CTO read ADDENDUM v0.18 item 1 as ranking, not holding: cut the independent cells now (items 5, 6, 8 on its read).
This amendment supersedes the item 6 and item 8 rulings above. No gate limb graded the ruling text; the issuance's
orders are graded by `.tools/to-pipeline-gate.py` at the cut.

| cell | item | outcome served | risk | worker | depends on | checks (base dry-run at CLOUD 810a66317f) |
|---|---|---|---|---|---|---|
| `IB-yr-1` | 6: a saved type other than `fixed` refuses a tolerated setting BEFORE generation; absent or `fixed` defers to the printed-type check | FWD-4 (no vendor generation spent on a report that must refuse) | WORLD (floor inferred from the infra/ path; no served move) | `~63` | none | `R19_CHECKS/test_r19_y1_pregen_static.py`: AC1 FAIL as expected, AC2 PASS as expected |
| `IB-yr-2` | 8: the lookup-capture test runs from pinned fixtures in the test tree | FWD-4 suite hygiene | WORLD (floor inferred from the infra/ path; no served move) | `~64` | none | AC1 FAIL as expected (1 failed, 23 passed); `R19_CHECKS/r19_y2_fixture_copies.py` AC2 FAIL as expected (3 MISSING) |

Edges: none (disjoint write sets: ycharts/generate vs intake/tests). fanout: 2 of 2 chains, cap 8.

**Item 5 NOT cut as an independent cell (issuer ruling, evidence):** at unit level the resident's revocation and
recovery are already covered on source equal to the served bytes (row IRPT_BCKEND-S178, B3 388/388):
- `ycharts/generate/tests/test_resident_worker.py` `:451` grades current authority at every phase, `:468` refuses before
  any claim or vendor call, and `:403` covers a revoked actor during cross-firm publication;
- `:227` covers retained-PDF recovery without a second vendor acquisition, and `:276` covers redelivery resume;
- recovery by redelivery also ran at the real entry point on st2 (`GRANT_RELEASE_ARMS_20260928.md`) and live in
  window 15 (the organic case, 16:07 release, 16:22 resume).
What remains is the DELIBERATE live drive: revoke the principal's authority while a real job runs. That needs a live job
and the walk principal, which are ~P's, so it is asked of ~P as one more arm in the same window packet (the organic
case, window 15, is the negative arm).
