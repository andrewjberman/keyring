# IRPT_BCKEND: CVO adjudication, round 1 (workstream ~PK, two repairs: exemption receipts and unkeyed split rows)

<sweep_watermark>2026-10-15T15:47Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T15:47Z, on msg 8408 (the combined packet `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_1_PJ_PK_DRAIN_END_20261015.md` @a245739457; this file grades the ~PK lane, ADJUDICATION_v121 grades ~PJ). Two orders, both risk LOCAL, issued @45decb9c92 and complete. IB-pr-582 (merged @df174ee533): `holdings_snapshot.py` plus `tests/test_absent_at_source_receipts.py`. IB-pr-583 (merged @18812065e6): `holdings_performance.py` plus `tests/test_split_unkeyed.py`. Re-run here at HEAD: IB219-1-AC1..AC3 and IB219-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 1 --workstream "~PK"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**What the repairs close.** IB-pr-582 answers v120's held D2-W420-S1: the exemption's evidence reads are re-taken after the gate when the provider read anything, and are carried into `_source_objects` and the source-set revision digest. A run that read nothing is byte-identical. IB-pr-583 answers v120's held D2-W421-S2 in part. A split row with no key is counted per day (`unkeyed_split_rows`) and the day reads `SPLIT_RATIO_ABSENT` (not graded); a blank cusip falls back to the ticker; grading is unchanged. The producer writes one manifest per day, so the totals are sums the reader makes (W425-S1). Nothing deployed: both changes are repository-only, and the live producers were read at base bytes in v120. No 2026-10-15 ledger entry names them.

**The 21 failures:** shared with ~PJ. At HEAD 5aefc342bf (both ~PK merges included) the failing ids equal v120's set, 0 new (v121 section 3). The ~PK suites, `test_absent_at_source_receipts.py` and `test_split_unkeyed.py`, are inside the two suites run and pass.

**D2-W424-S1 (the commit gate's client-data check printed WARN and checked nothing for 381be2ca6c).** Read here: the commit's three files carry no account-id-like digit run. The only 8+ digit run is inside the record's `base_commit` hash. The standing of that WARN-only gate on dell2 is Andrew's record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md`, the same disposition as IRPT_DASHBD v72 and IRPT_BCKEND D2-W374-S1.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S30",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T15:47:00Z",
  "one_line": "Round 1 ~PK. IB-pr-582 puts the exemption's evidence reads into the source receipts and the revision digest (closes v120's held D2-W420-S1); IB-pr-583 counts unkeyed split rows per day, marks such days SPLIT_RATIO_ABSENT and falls back to the ticker for a blank cusip (answers D2-W421-S2). 6 of 6 criteria PASS re-run; repository-only, nothing deployed; same 21 failing test ids as v120 (v121). Dismissed (6): D2-W420-S1 (ARMED; closed by IB-pr-582), D2-W421-S2 (ARMED; answered by IB-pr-583), D2-W424-S1 (ARMED; the commit's files carry no account-like digit run, the gate's WARN-only standing is Andrew's record), D2-W425-S1, -S2, -S3 (readings, including the stale-pyc difference-control trap).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W420-S1",
   "IRPT_BCKEND-D2-W421-S2",
   "IRPT_BCKEND-D2-W424-S1",
   "IRPT_BCKEND-D2-W425-S1",
   "IRPT_BCKEND-D2-W425-S2",
   "IRPT_BCKEND-D2-W425-S3"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "The two repairs v120 held are built and tested at HEAD, repository-only. The never-widen pairs (exemption; 49F split) and the apply remain the next acts.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T15:3xZ of the invocations in IB-pr-582 and IB-pr-583: IB219-1-AC1..3, IB219-2-AC1..3 PASS, exit 0 each; round-close-check ~PK round 1 MAY-CLOSE",
    "git diff --name-only df174ee533^1 df174ee533 and 18812065e6^1 18812065e6: holdings_snapshot.py + test_absent_at_source_receipts.py; holdings_performance.py + test_split_unkeyed.py",
    "git show 381be2ca6c: 0 eight-or-more digit runs in the test file; 1 in the record, inside base_commit",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md",
    "pytest at 5aefc342bf: investor_reporting/tests failing ids equal to v120's set; irpt_holdings_performance/tests 83 passed (ADJUDICATION_v121)",
    "investigation rows D2-W420-S1, D2-W421-S2, D2-W424-S1, D2-W425-S1..S3, D2-S203",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUNDS_1_PJ_PK_DRAIN_END_20261015.md @a245739457 (msg 8408)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two held hazards closed by the repairs built and tested here, a client-data WARN with no client data and a recorded standing, and three readings."
 }
]
```
