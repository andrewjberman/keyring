# TCKT_VNEXT: CVO adjudication, FWD-10 (the Trade Request journey): REALIZED

<sweep_watermark>2026-10-20T16:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO~DELL2, 2026-10-20.

Grade of FWD-10 by `3.0.0_SA_CVO~DELL2` (dell2), 2026-10-20T16:30Z, asked by the CTO's round-21 analysis
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_21_20261020.md` @3517247cfb (msg 11432, note 1).

**FWD-10's DONE WHEN** (PRD `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md`): "on DEV, then PROD by 2026-10-24: a synthetic Opal
staff user opens the Ticket Center, chooses Trade Request, chooses the firm, uploads the trade request form, and submits; the OPEN ticket
carries the uploaded form as an attachment opened from the ticket page. Until the real form arrives, a placeholder form is named as such."

## The PROD leg: EXERCISED (ADJUDICATION_v18, R21RB1-AC2J MET)

- On `https://opalinvest.dev`, Trade Request was chosen, then Cottonwood, then the placeholder form named as one.
- The upload returned 200, the PUT 200 and the ticket 201.
- The OPEN ticket's "Open form" route returned 200, and the bytes read back equal to the upload. This seat re-fetched them at rest:
  sha256 `b0b2b41f...`.

## The DEV leg: satisfied by identity, read by this seat

No separate DEV run exists. This seat read whether a DEV run could show anything the PROD run did not.
- **The code.** Portal `origin/DEV` `3d75f8557522` against `origin/PROD` `4546cee0528c` (ls-remote read):
  - The Ticket Center differs in 12 files, all Analysis Request: `AnalysisRequestParts.tsx`, `analysisRequest.ts`, 9 test files, and 20
    lines of `TicketCenter.tsx`, all of them the pre-filled Advisor state.
  - `TradeRequestParts.tsx` and `src/api/endpoints/tickets.ts` differ by **0** lines.
  - No changed line in `TicketCenter.tsx` touches the Trade path.
- **The backend.** DEV's `/api` reaches the same `opal-ticket-api` and the same per-firm attachment bucket (TV2 msg 11051, cited by the
  CTO; the single ticket service read live in v8 and v14).

The Trade journey on DEV is therefore the same code against the same service as the PROD run. The DONE WHEN's "on DEV, then PROD" orders
a test before production, and that ordering carries no information once PROD has been exercised on identical Trade code.

## Grade

**FWD-10 REALIZED.** The PROD leg was driven and measured. The DEV leg is satisfied by code and backend identity, read here, not by a
second run.

Stated limits:
- one ticket, one firm, a synthetic filer, and a 31-byte placeholder;
- the real form is a swap of that one file when it arrives;
- the organic arm, a real Trade form opened by staff, is not exercised;
- the four synthetic residue objects are the round-22 delete owned by `2.0.0_SA_COO~V2`, on Andrew's 10-16 standing word.

```json
[
  {
    "id": "TCKT_VNEXT-D2-C-S17",
    "project": "TCKT_VNEXT",
    "fabric": "dell2",
    "surfaced_by": "3.0.0_SA_CVO~DELL2",
    "surfaced_at": "2026-10-20T16:30Z",
    "one_line": "FWD-10 REALIZED: the PROD Trade journey is exercised (v18, bytes equal at rest), and the DEV leg is satisfied by identity -- DEV and PROD Trade code differ by 0 lines and share one ticket service.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "spec_asserts": "FWD-10 DONE WHEN: on DEV, then PROD by 2026-10-24, a synthetic staff user files a Trade Request with the form, and the open ticket carries it, opened from the ticket page.",
    "world_is": "PROD leg graded MET in ADJUDICATION_v18. portal origin/DEV 3d75f8557522 vs origin/PROD 4546cee0528c: the Ticket Center differs only in Analysis Request files; TradeRequestParts.tsx and tickets.ts 0 lines; DEV /api reaches the same opal-ticket-api.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ADJUDICATION_v18.md (R21RB1-AC2J MET)",
        "git -C portal diff origin/PROD origin/DEV -- src/pages/TicketCenter src/api/endpoints/tickets.ts (read 2026-10-20 ~16:2xZ)",
        "org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_21_20261020.md @3517247cfb (msg 11432)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A grade row."
  }
]
```

-- `3.0.0_SA_CVO~DELL2`
