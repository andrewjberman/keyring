# IRPT_ANLREQ: CVO adjudication, round 3 (workstream TICKET, ~V2): the ticket page reads a hop failure

<sweep_watermark>2026-10-16T08:16Z</sweep_watermark>

L8 compile, L9 grade and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T08:16Z, on msg 9189 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/L8_PACKET.TICKET.R3.md` @25a849d023, blob b2bc6aad49). One order, TO-AR-v31 (LOCAL in the workspace; the portal change landed on portal DEV at dc057891b086, which `git merge-base` reads in origin/DEV and not in origin/PROD). The mechanical criteria were re-run here against a scratch portal worktree at dc057891 (dependencies linked to the shared portal's node_modules, removed after; the shared node_modules confirmed intact): AR31-v-AC1 `V31-FAILURE-OK pass=13`; AR31-v-AC2 `PORTAL-TSC-OK rc=0`; AR31-v-AC3 `MUTANT-FIRES` (restore verified); the TicketCenter suite 196 tests across 31 files, 0 fail. No pixel render: the page would need a signed-in internal session and a ticket in a failure state, and ui-smoke has no validated fixture for it. Port 5174 was free, and no dev server was started. No remediation row.

**L9 -- AR31-v-AC4J: FAIL (UNPROVEN, not refuted).** The criterion asks that the ticket page (1) names the failed step and what happens next, only while no package is attached; (2) for a ticket with or without a draft; (3) makes no call it should not; (4) leaves no blank row when there is nothing to say; (5) never breaks the page; and (6) adds no route, write, principal or colour.

Clauses 2, 3, 4 and 6 are shown on the artifacts.
- **(2):** the tests for neither-draft-nor-package and for draft-plus-failure pass, and the DOM markup shows one row in each case.
- **(3):** both call-count tests read 0, and the mutant fires on the package gate.
- **(4):** the DOM markup for no draft, no package and no failure reads `tr count 0`.
- **(6):** the diff adds no fetch, route or write; the only read is the existing `getJobStatus` on the existing client. The block's classes are the file's existing tokens: `#C4CBDB` hairline (7 uses at base; DESIGN.md `palette.mutedTint`), `INK` navy, `bg-white`. There is no band and no light text.

Clause 1 is shown in code only. The page renders the route's last `NONE` label verbatim, and the producer's `FAILURE_WORDS` (`infra/aws/lambda/investor-reporting/ops/status.py:194`) name the step and what happens next for every code. But no job row carries `hop_failure` yet. So the page has never shown words that a real failure delivered through the released `irpt-status`, and `DELIVERIES_EXHAUSTED` is not reachable from the producer as written.

Clause 5 is shown only against a stubbed rejection, not a real failed route.

What would prove 1 and 5:
- Each failure code driven on purpose against the released status route, with an internal login's ticket page then showing that code's words. Rendered and READ per the portal law (CANVAS `rgb(244, 246, 250)`), a screenshot path recorded.
- One real failed status read (the route refusing or erroring) with the page intact.

This is FWD-4's live arm, after the r34 resident writers and ~T2's commentary writer. The cell is built correctly as far as an artifact can show; the judgment cannot PASS until a real failure has been shown on the page.

**Client-facing:** the failure block renders only on the internal board. The partner branch of `TicketCenter.tsx` (from `if (partner) {`, line 579) returns its own markup without `AnalysisPackageRow`. But the Ticket Center PAGE is one a partner login opens (the AR-y-283 partner form and list live in the same file). By the workspace rule ('a portal PROD push that changes a CLIENT-FACING page ... waits on his word'; 'Unsure = client-facing'), this file's PROD promote waits on Andrew. The packet's 'nothing client-facing' is true of the block, not of the page.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-C-S2",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T08:16:00Z",
  "one_line": "Round 3 TICKET (~V2). AR31-v-AC1, AC2, AC3 PASS on the landed DEV tree (13 of 13; tsc rc 0; MUTANT-FIRES; TicketCenter 196 of 196). L9: AR31-v-AC4J FAIL (UNPROVEN, not refuted). The no-call, no-blank-row, with-or-without-draft and no-new-route/write/principal/colour clauses are shown by the tests, the DOM markup and the diff. 'Names the failed step' and 'never breaks the page' are shown only against stubbed envelopes, because no real hop failure exists yet; they need FWD-4's live arm, a rendered and read page per the portal law, and one real failed status read. The Ticket Center page is one a partner login opens, so the PROD promote of TicketCenter.tsx waits on Andrew, although the failure block itself renders only on the internal board. Dispositions accepted: D2-W270-S1 (BLOCKING draft-axis gap, disarmed by AMENDMENT 1; the two tests pass), S2 (the firm field, not a defect), S3 (WAIT and NONE share one adapter action, not a defect for this cell), S4 (stale mutant, replaced by AMENDMENT 3; the new mutant fires here).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W270-S1",
   "IRPT_ANLREQ-D2-W270-S2",
   "IRPT_ANLREQ-D2-W270-S3",
   "IRPT_ANLREQ-D2-W270-S4"
  ],
  "spec_asserts": "Spine L9: a judgment criterion is graded on the artifacts, never self-graded. Portal law: a page change is rendered and READ. Workspace rule: a portal PROD push that changes a client-facing page waits on Andrew's word.",
  "world_is": "The reader is on portal DEV (dc057891), not PROD; it has never shown a real failure, because no job row carries hop_failure yet.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T08:0xZ on a scratch portal worktree at dc057891b086: V31-FAILURE-OK pass=13; PORTAL-TSC-OK rc=0; MUTANT-FIRES (restore verified); bun test src/pages/TicketCenter 196 pass 0 fail across 31 files",
    "git -C portal merge-base --is-ancestor dc057891b086: origin/DEV yes, origin/PROD no",
    "git -C portal diff 34a6baf8 dc057891 -- src/pages/TicketCenter: 3 files +410 -9; no new fetch, route or write; HOP_FAILURE_BLOCK uses #C4CBDB, INK, bg-white (existing tokens)",
    "org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~270/render_markup.txt: tr counts 1 / 0 / 1 for the three states",
    "infra/aws/lambda/investor-reporting/ops/status.py:194 FAILURE_WORDS (step and next-step words per code)",
    "TicketCenter.tsx at dc057891: partner branch from line 579 returns without AnalysisPackageRow; the board renders AnalysisPackageRow at line 908",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/L8_PACKET.TICKET.R3.md @25a849d023 blob b2bc6aad49 (msg 9189)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The four worker rows are dispositioned by the issuer's amendments and verified here. The judgment's FAIL is unproven evidence, not a defect row: the round stays REFUSED until FWD-4's live arm shows the page on a real failure."
 }
]
```
