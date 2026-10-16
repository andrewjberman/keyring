# TCKT_VNEXT: CVO adjudication, round 20 part 1 (the two build cells)

<sweep_watermark>2026-10-16T23:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-16.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-16T23:50Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_BUILD.md`, blob 8cf7c2fc87b0 at da015aae9b (msgs 10017 and 10019; verified by
`git hash-object`).

**What this seat read itself:**
- **The workspace diff.** `git diff 430b378b8f 44933b266b` on the ticket Lambda: one hunk in `attachment_open_ticket`, plus one new test
  file.
- **The tests.** The full ticket-service suite at 44933b266b, run by this seat in a detached worktree: **471 passed, 59 subtests passed, 0
  failed.** The worker-worktree failures in rows W49-S1 and S2 do not reproduce here.
- **The live package.** `lambda_function.py` in the live `opal-ticket-api` package, downloaded by this seat. The zip's sha256 equals the
  live `CodeSha256` `iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM=` (the control on the download), and the member equals 44933b266b
  byte for byte (134,698 bytes).
- **The portal diff.** `git -C portal diff fcbf2bce 8e4f0885`: 4 files. `8e4f0885` is contained in portal `origin/DEV` (ls-remote
  `4d4dc68cae`).
- **The controls guard.** `MeetingOutcomeControls` at 8e4f0885 (line 298) returns null on `status === 'completed'`.

## Grades

**TCKT_VNEXT.TO-R20-LM R20LM-AC3J MET.**
- One line out and six in. `req_firm` is read from `requester.firm`, the member the 404 fence two lines above already tests.
- A ticket whose `answers.firm` differs returns `404 {"error": "ticket <id> carries no attachment"}`, the same body as the
  no-attachment branch. The presign then uses `firm = req_firm`.
- No other line of the function changed. The live member is that tree.
- This closes this seat's row `TCKT_VNEXT-D2-C-S2`: fence and presign now read ONE member.

**TCKT_VNEXT.TO-R20-PT R20PT-AC4J MET** on the diff and tests. Not rendered; that is `R20RV-AC1J`'s.
- `showsMeetingOutcome` draws the line on a non-completed meeting ticket, or on a completed one that carries `meeting`. A completed one
  without it draws nothing, and any other type draws nothing.
- `viewerIsCoordinator` matches the viewer's email, trimmed and case-insensitive, against `routing.primary`. The board mounts the controls
  only when the viewer is internal AND the coordinator.
- Every other viewer gets the line alone. The component's own guard keeps the controls off a completed ticket.
- The diff adds no call, route, class or colour, and no principal. `auth` was already in scope, and the one fixture change gives the
  existing mock a coordinator email without changing any assertion.
- The ten named tests cover each clause, including case-insensitivity and the completed-ticket guard.

**FWD-11 stays NOT REALIZED.** This grades the build only. The rendered filer, bystander and coordinator views are `R20RV-AC1J`'s, and
`TO-R20-RV` has not run.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S3",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-16T23:50Z",
    "one_line": "Round 20 part 1 L9: R20LM-AC3J MET and R20PT-AC4J MET (build only, not rendered); this seat's row D2-C-S2 is resolved by R20-lm-2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "TCKT_VNEXT-D2-C-S2"
    ],
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): a judgment criterion is graded by the CVO and never self-graded. Row D2-C-S2: the open route should fence and presign on the same member.",
    "world_is": "44933b266b makes attachment_open_ticket read requester.firm for both, refusing a differing answers.firm with the no-attachment 404; the live package member equals that tree (zip sha256 = live CodeSha256). Suite at 44933b266b: 471 passed. Portal 8e4f0885 (in origin/DEV) shows the outcome line on completed tickets that carry one and the controls only to the coordinator.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_BUILD.md blob 8cf7c2fc87b0 (msgs 10017, 10019)",
        "git diff 430b378b8f 44933b266b -- infra/aws/lambda/ticket_center/lambda_function.py",
        "live opal-ticket-api package, CodeSha256 iRxJZYp6IXEtiXDRMT4R/EOwKvsqh5Id5NNgPcpy3RM=",
        "git -C portal diff fcbf2bce 8e4f0885"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row; D2-C-S2's hazard is removed in the live code."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
