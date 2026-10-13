# IRPT_BCKEND: CVO adjudication, round 181 (workstream ~P)

<sweep_watermark>2026-10-13T16:28Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:28:00Z, on msg 7064 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_181_P_DRAIN_END_20261013.md`). One BUILD-ONLY order, no judgment criterion, nothing applied.
The irpt-directory-search apply is HELD by Andrew's word (D2-S139). 2 rows dismissed below; D2-S139 graduates ARMED to the laptop
1.0.0_SA_CTO in `remediations/REMEDIATION_v56.md`.

```json
[
 {
  "id": "IRPT_BCKEND-C-S365",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T16:28:00Z",
  "one_line": "Round 181 (~P). Dismissed: D2-W365-S1 (a stale OPEN deploy marker on two worktree HEADs while the ledger reads CLOSED; folded into D2-S139's apply precondition: measure the artifact on every worktree) and D2-S138 (the issuer's disposition record). Graduates ARMED: D2-S139 (the apply HELD by Andrew's word, with the portal condition made precise by this seat's read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W365-S1",
   "IRPT_BCKEND-D2-S138"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-515 is complete (order file read; merge 23fb169341 on HEAD). Nothing applied: irpt-directory-search reads tvrsQ+w8 (12:34:28Z), this seat's read. The refreshed pair has the COO half signed and the CTO half unsigned. Andrew's word holds the apply and the dell2 CTO's IRPT_BCKEND analysis; this compile and slug are this seat's ordinary acts and are not inside that word's scope.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W365-S1, D2-S138",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_181_P_DRAIN_END_20261013.md (msg 7064)",
    "this seat's reads 2026-10-13T16:2xZ of portal origin/DEV f6ef1d25 and origin/PROD 15c97549: header/selectionRequest.ts:8-18 identical on both (an ACCOUNT-kind row that is not narrowedToAccount throws 'Choose a client, relationship or account.'); header/search.ts:277 on PROD sets narrowedToAccount = entry.kind === 'account' && entry.accountId !== null"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A marker folded into the graduating row's precondition, and a disposition record."
 }
]
```
