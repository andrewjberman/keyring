# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PG, the absent_at_source exemption of the holdings gate)

<sweep_watermark>2026-10-15T13:45Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T13:45Z, on msg 8309 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PG_DRAIN_END_20261015.md` @da59b84252). One order, IB-pr-576 (risk LOCAL, `task-orders/IRPT_BCKEND.TO-IB-pr-576.exemption-absent-at-source.md`), complete, merged @05826407ad (`holdings_snapshot.py` +85/-5, a new test file, the worker's record, criteria output, proof instance and the channel). Re-run here at HEAD: IB215-1-AC1..AC3 PASS (exit 0), and `pytest tests/test_closed_at_source_exemption.py`: **9 passed**. `round-close-check --round 1 --workstream "~PG"`: orders=1, proofs 1 of 1 ok, verdict=MAY-CLOSE.

**v117 condition 1, nothing records "closed" as measured: MET.** The only manifest writer is `absent_at_source_record` (`holdings_snapshot.py:3056-3066`). Each entry is `{"account_id", "status": "absent_at_source", "absence_claim": "measured", "closure_claim": "unknown", "candidate_day", "prior_day"}`, and the docstring states "the source cannot tell a closed account from one whose feed was omitted (CTO msg 8290), so no entry says closed". The gate's listing key is `account_lost_absent_at_source` (`:3123`), and the display helper renders "Not reported by the custodian since <date>" (`:3069-3072`). "closed" survives only in names: the block marker `CLOSED-AT-SOURCE-A`, the constants `CLOSED_AT_SOURCE_TABLES` and `CLOSED_AT_SOURCE_FLOOR_PERCENT`, the test file name, and the wording of row W419-S1. None of these is a recorded fact. Recommend (P2) renaming them in IB-pr-577 so the vocabulary cannot drift back.

**v117 condition 2, the live-account-dropped branch: DESIGNED, NOT YET BUILT OR SIGNED.** The design covers it: closure_claim stays unknown, and the served words ("Not reported by the custodian since") name absence, not closure. The exemption also needs no positions in BOTH tables on BOTH days with every partition complete (95 percent floor, `:3014-3050`), so one zero day or a truncated file never exempts (tests). Built today, though, the household listing that keeps the exempted account visible is NOT done (W419-S2; the nodes come from `holdings_49f.py` and siblings, outside the grant). An exemption fired today would therefore drop the account's nodes from the served snapshot without its "Not reported" line. That is harmless only because the exemption is inert (below). IB-pr-577 must build the listing, and its dry run plus never-widen pair must cover both branches: the account closed, and the account live but omitted by the feed and returning later.

**"Inert", confirmed.** Grep over all of `data/` and `infra/` shows `evaluate_publish_gate` has ONE production caller, `run_firm` at `holdings_snapshot.py:3257`. It passes `closed_accounts` and `marks_no_closures` only, never `absent_at_source_evidence`, so that parameter is None and the exemption branch (`:3120`, `if lost and absent_at_source_evidence is not None`) cannot run. `absent_at_source_record` runs on every gated fire (`:3278`) but writes only when the gate listed an exemption, so it is byte-unchanged. The other callers are tests. **Nothing deployed:** the three live bundles still read VersionIds oyIYMVdh / UHOCIkWj / PzhCs97q at 2026-10-09T10:29Z and 2026-10-13T13:35-36Z (head-object, read here), the same as in v118. No 2026-10-15 change-management entry names the holdings gate.

**Rows.** Again the packet says W419-S1 and S2 "stay ARMED, owner me", but the rows read W419-S1 OBSERVATION INERT (no owner) and W419-S2 BLOCKING INERT (owner `~P2`). The live carrier is `D2-S201` (ARMED, `~P2`). This is the second packet whose description of a worker row's standing differs from the row (v117: W418-S2).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S27",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T13:45:00Z",
  "one_line": "Round 1 ~PG. The absent_at_source exemption is built in the gate and INERT: its only production caller (run_firm, holdings_snapshot.py:3257) never passes absent_at_source_evidence, so the branch at :3120 cannot run; nothing deployed (live bundle versions unchanged). v117 condition 1 MET: the manifest entry records absence_claim 'measured' and closure_claim 'unknown'; 'closed' remains only in names (block marker, two constants, test file). v117 condition 2 DESIGNED, not built: the household listing that keeps the account visible ('Not reported by the custodian since') is IB-pr-577's, and its pair must cover a live account omitted by the feed. IB215-1-AC1..AC3 PASS and 9 tests pass re-run. Dismissed (2): D2-W419-S1 (manifest written to the run manifest; publication.py is IB-pr-577's), D2-W419-S3 (BLOCKING, INERT; MAX_PATH, renamed). Held: D2-W419-S2, D2-S201 (~P2).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W419-S1",
   "IRPT_BCKEND-D2-W419-S3"
  ],
  "spec_asserts": "ADJUDICATION_v117's two conditions on IB-pr-576 (no 'closed' recorded as measured; the live-but-omitted branch covered); CLAUDE.md section 4 (a value carries its claim) and section 5 (never-widen covers both branches).",
  "world_is": "The exemption logic and its manifest record exist at HEAD on box/dell2 and cannot fire: no caller supplies evidence and no bundle carries it. Before it can fire: the household listing, the published manifest fact, the per-firm evidence loaders (IB-pr-577), a dry run measuring the exemption alone per firm, and a never-widen pair covering closed and live-omitted.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T13:4xZ of the invocations in IB-pr-576: IB215-1-AC1..3 PASS, exit 0; pytest tests/test_closed_at_source_exemption.py: 9 passed",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 1 --workstream ~PG: orders=1 proof_ok=1 judgment=0 verdict=MAY-CLOSE",
    "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:3014-3073 (the block), :3063-3064 (absence_claim measured, closure_claim unknown), :3077 (the optional parameter), :3120 (the guarded branch), :3257 (run_firm's call without it), :3278 (record call)",
    "Grep absent_at_source_evidence= | evaluate_publish_gate( over data/ and infra/: one production caller (run_firm), the rest tests; infra/: 0",
    "aws s3api head-object of the three holdings bundles 2026-10-15T13:4xZ: oyIYMVdh 2026-10-09T10:29:07Z, UHOCIkWj 2026-10-13T13:35:24Z, PzhCs97q 2026-10-13T13:36:08Z (unchanged since v118)",
    "investigation rows D2-W419-S1..S3, D2-S201",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_1_PG_DRAIN_END_20261015.md @da59b84252 (msg 8309)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A manifest-location reading moved to the next order and a path-length defect fixed by renaming. The missing household listing and the pending evidence path are held on W419-S2 and S201 for IB-pr-577."
 }
]
```
