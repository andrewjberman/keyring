# IRPT_BCKEND: CVO adjudication, round 5 (workstream ~PS, the submit caller and the installed reader)

<sweep_watermark>2026-10-15T08:33Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-15T08:33Z, on msg 8207 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_5_PS_DRAIN_END_20261015.md` @2cc1820a63). Two orders, IB-pr-566 (PATH C submit caller through the real handler) and IB-pr-567 (installed filled reader and render), complete, merges @2cb9105a27 (03:57 -0400) and @f32e66d896 (04:26 -0400), issued @941abbfa1d on the CTO's round-5 analysis @25f361860e. No judgment criterion. Re-run here at HEAD: IB207-1-AC1..AC3 and IB207-2-AC1..AC3, 6 of 6 PASS (exit 0 each). `round-close-check --round 5 --workstream "~PS"`: orders=2, proofs 2 of 2 ok, verdict=MAY-CLOSE.

**LOCAL, not SERVED (verified here).** Both merges change repository files only (export `entry.py`, `retained_export.py`, `submit_async.py`, `submit_service.py`, `render.py`, the new `filled_reader_installed.py`, tests, `lambda-source-map.json` and its test). Live read 2026-10-15T08:3xZ: `irpt-export-render` LastModified 2026-10-14T00:09:26Z (CodeSha256 `5/9LZBbT...`) and `irpt-49f-reporting-read-lambda` LastModified 2026-10-13T13:07:19Z, both before these merges; no change-management entry names them. "PATH C through the real handler" means the tests drive `entry.submit_export` in process with stubs, not the deployed function. Risk class: both orders carry `WORLD`, which over-classes LOCAL repository work (the gate infers WORLD from the infra paths, as noted in v102); over-classing costs checks, not safety, so no mismatch that matters. Nothing served.

**Rows.** `D2-W411-S2` (BLOCKING, ARMED: the render read had no caller) and `-S4` are resolved by IB-pr-567 AMENDMENT 1 (one implementation; the render calls IB-pr-566's functions); the re-run criteria pass on that tree. The issuer's omitted source-map entry for the new module (the W402-S3 class) was added by amendment with a test. HELD, owned, before any deploy leg: `D2-W411-S1` (ARMED, `~P2`): whether the export role holds `s3:GetObject` on the platinum filled report object was not read; the deploy leg reads the role first. Deploy legs also wait on hop 1's first cloud write (B-49F round-120 analysis).

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S19",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-15T08:33:00Z",
  "one_line": "Round 5 ~PS. IB-pr-566 gives freeze_filled_report its production caller (PATH C in submit_async.accept, the async leg builds from the frozen row); IB-pr-567 installs the filled reader (by VersionId) and routes the render through 566's one read. 6 of 6 PASS re-run. LOCAL, not served: repo-only diffs, irpt-export-render and irpt-49f-reporting-read-lambda last modified 10-14 and 10-13, before the merges; 'real handler' means in-process tests. Orders carry WORLD, over-classed for LOCAL work. Dismissed (8): D2-W410-S1, -S2, -S3 (readings), D2-W411-S2 (BLOCKING, ARMED; resolved by AMENDMENT 1, one implementation), D2-W411-S3 (lib/ already in the export files list), D2-W411-S4 (superseded with S2). Held: D2-W411-S1 (export role's GetObject on the platinum object unread; deploy leg reads it first).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W410-S1",
   "IRPT_BCKEND-D2-W410-S2",
   "IRPT_BCKEND-D2-W410-S3",
   "IRPT_BCKEND-D2-W411-S2",
   "IRPT_BCKEND-D2-W411-S3",
   "IRPT_BCKEND-D2-W411-S4"
  ],
  "spec_asserts": "Evidence law (CLAUDE.md rule 22): the risk class on each order matches what the work touches; never trust a producer's 'nothing deployed', read live state.",
  "world_is": "The serve path's code is complete through freeze, submit and render on box/dell2, LOCAL; the deployed export and reporting functions predate it. Before any deploy leg: the export role's s3:GetObject on the platinum filled report object (D2-W411-S1) and hop 1's first cloud write.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-15T08:3xZ of the invocations in IB-pr-566 and IB-pr-567: IB207-1-AC1..3, IB207-2-AC1..3 PASS, exit 0 each",
    "python .tools/round-close-check.py --project IRPT_BCKEND --round 5 --workstream ~PS: orders=2 proof_ok=2 judgment=0 verdict=MAY-CLOSE",
    "aws lambda get-function-configuration 2026-10-15T08:3xZ: irpt-export-render LastModified 2026-10-14T00:09:26Z; irpt-49f-reporting-read-lambda LastModified 2026-10-13T13:07:19Z",
    "git diff --name-only 2cb9105a27^1 2cb9105a27 and f32e66d896^1 f32e66d896: repository files only",
    "task orders IB-pr-566 and IB-pr-567: <risk>WORLD</risk>",
    "investigation rows D2-W410-S1..S3, D2-W411-S1..S4, D2-S190",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_5_PS_DRAIN_END_20261015.md @2cc1820a63 (msg 8207)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A BLOCKING no-caller row resolved by one implementation and re-graded green, readings, and a superseded row. The export role's read permission is held with ~P2 before any deploy."
 }
]
```
