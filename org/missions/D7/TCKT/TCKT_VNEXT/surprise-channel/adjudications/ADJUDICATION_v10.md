# TCKT_VNEXT: CVO adjudication, round 20 part 1b (the PROD-based re-cut, R20-pt-4)

<sweep_watermark>2026-10-17T01:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-17.

L9 grade by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-17T01:45Z, a seat that did none of this work. Input:
`org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD_RECUT.md`, blob 208255c11899 (msg 10136; verified by `git hash-object`).

**What this seat read itself:**
- **The refs.** Portal ls-remote: `origin/PROD` `fa21a303d872`; the branch `cand/dell2/tckt-meeting-form-prod-recut` at `4e1e35bfa082`.
  `git log fa21a303..4e1e35bfa0` is exactly two commits (e5c8e075 the form, 4e1e35bf the outcome line and controls).
- **The diff.** `git -C portal diff fa21a303 4e1e35bfa0`: 5 files (+1033 -7), all meeting.
- **The head file.** `TicketCenter.tsx` read at the head.

## Grade

**TCKT_VNEXT.TO-R20-PP R20PP-AC4J MET** on the diff and the head. Not rendered, and the PROD page was not run.

The CTO's four points, each read at the head:
1. **Imports.** Line 85 imports `TradeRequestForm` alone from `./TradeRequestParts`; `TradeFormOpen` appears nowhere in the file.
2. **Meeting imports.** They include `showsMeetingOutcome` and `viewerIsCoordinator`.
3. **The analysis row.** PROD's `AnalysisDraftAndPackage` row is kept (lines 76 and 907); `AnalysisPackageRow` is absent.
4. **The meeting row.** It mounts on `showsMeetingOutcome(t)`. The controls sit behind `internal && viewerIsCoordinator(t, auth.user?.email)`, and
   `auth` is PROD's existing `useAuth()` (line 214).

No Trade Request code reached the branch:
- Zero added lines in the diff name `TradeFormOpen`, `TradeRequestParts`, `trade_form`, `trade-form` or an attachment route.
- `tickets.ts` gains only the meeting types and the one `/meeting` call.
- PROD's own Trade Request behaviour is unchanged. `drawsOwnForm` returns true for `trade_request` as well as `meeting_request`, so the three
  `newType !== 'trade_request'` guards are carried forward exactly. The New Ticket list's `.filter(([v]) => v !== 'trade_request')` (line 731)
  is untouched.

**FWD-11 stays NOT REALIZED.** `R20RV-AC1J` (the rendered read) is still owed, and the PROD build is read only after the promote.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S4",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-17T01:45Z",
    "one_line": "Round 20 part 1b L9: R20PP-AC4J MET on the PROD re-cut 4e1e35bfa0 (the CTO's four points hold; no Trade Request code; not rendered, PROD not run).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "Spine L9 (CLAUDE.md rule 27): a judgment criterion is graded by the CVO and never self-graded.",
    "world_is": "Portal cand/dell2/tckt-meeting-form-prod-recut at 4e1e35bfa082 is two cherry-picks on origin/PROD fa21a303d872; diff 5 files, all meeting; TicketCenter.tsx imports TradeRequestForm only, keeps AnalysisDraftAndPackage, mounts the meeting row on showsMeetingOutcome and the controls behind viewerIsCoordinator.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D7/TCKT/TCKT_VNEXT/ledger/L8_PACKET.R20_PROD_RECUT.md blob 208255c11899 (msg 10136)",
        "git -C portal diff fa21a303 4e1e35bfa0; git -C portal show 4e1e35bfa0:src/pages/TicketCenter/TicketCenter.tsx",
        "portal ls-remote: PROD fa21a303d872, cand/dell2/tckt-meeting-form-prod-recut 4e1e35bfa082"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
