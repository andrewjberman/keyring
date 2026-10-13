# IRPT_BCKEND: remediations, round 181 (workstream ~P)

<sweep_watermark>2026-10-13T16:28Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:28:00Z. Follows ADJUDICATION_v82. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_181_P_DRAIN_END_20261013.md` (msg 7064). No judgment criterion.
Graduated, round label v182: 1 row, OPEN, ARMED, owner the laptop `1.0.0_SA_CTO`: HELD by Andrew's word. Before any apply, every ACCOUNT entry
the new tail search returns must carry a non-null accountId, or the portal fix goes first (PROD carries the same throw as DEV).

```json
[
 {
  "id": "IRPT_BCKEND-D2-S139",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "mechanism": "HELD by Andrew's word (relayed by 1.0.0_SA_CTO~DELL2, msg 7066): the irpt-directory-search apply and the IRPT_BCKEND round-181 analysis wait for the laptop CTO or Andrew; the portal consumer point (selectionRequest.ts:18 throws for an unnarrowed ACCOUNT-kind row) must be cleared before the apply.",
  "evidence": [
   "investigation row D2-S139",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_181_P_DRAIN_END_20261013.md",
   "this seat's reads 2026-10-13T16:2xZ of portal origin/DEV f6ef1d25 and origin/PROD 15c97549: header/selectionRequest.ts:8-18 identical on both (an ACCOUNT-kind row that is not narrowedToAccount throws 'Choose a client, relationship or account.'); header/search.ts:277 on PROD sets narrowedToAccount = entry.kind === 'account' && entry.accountId !== null",
   "row D2-W365-S1 (folded: the stale OPEN marker on two worktree HEADs)"
  ],
  "remedy": "HELD by Andrew's word ('I will deal with this on the laptop device, not here', relayed by 1.0.0_SA_CTO~DELL2 msg 7066): no seat applies the irpt-directory-search pair until the laptop 1.0.0_SA_CTO or Andrew releases it. Before any apply, the portal point, now made precise by this seat's read: PROD (15c97549) carries the same throw as DEV, and it is reached only by an ACCOUNT-kind row whose accountId is null (search.ts:277). So the pair's packet must show that every ACCOUNT entry the new tail search returns carries a non-null accountId; if any can be null, the portal fix precedes the apply. The apply also measures the artifact on every worktree (W365-S1).",
  "owner": "1.0.0_SA_CTO",
  "round": "v182",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO",
   "round": "v182"
  },
  "closed": false,
  "disarm": {
   "state": "ARMED",
   "owner": "1.0.0_SA_CTO",
   "at": null
  }
 }
]
```
