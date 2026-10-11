# IRPT_ANLREQ -- decomposition, round 5, workstream Y (issuer 2.0.0_SA_COO~Y2)

**Input:** CTO ruling `1.0.0_SA_CTO~DELL2` msg 4860 (2026-10-11 ~11:5xZ), on this seat's closer-candidate pitch (msg 4857): "one
read-only cell: FWD-1 of IRPT_ANLREQ hop by hop, from the filed ticket to the report opened on it. For each hop: live, built and not
live, or no code; its owner (this workstream, workstream G, TCKT_VNEXT, or the portal); and what it waits on today. One table. On it I
either cut the remaining hops in order across the three lanes, or carry the closer to Andrew with the table as its case."
No round-4 L10 analysis is in hand yet; this round is that one ruled cell and nothing else. The endpoint is unchanged.

**Thread:** FWD-1 is not live. This round measures where it stops. It builds nothing.

## Cells

| cell | source | what is produced | write set | risk |
|---|---|---|---|---|
| `AR-y-51` | CTO msg 4860 | ONE table: every hop of FWD-1 from the filed ticket to the report opened on it, each with its state (LIVE / BUILT_NOT_LIVE / NO_CODE), its owner, what it waits on today, the evidence and a claim word. Read-only: code, order statuses, source-map entries, ledgers, and single-resource live reads | one JSON file and one markdown rendering in the worker's deliverables folder | LOCAL (records only; nothing is built, applied or pushed) |

## Edges and chains

- One cell, no edge. M = 1.

fanout: 1 of 1 chains, cap 8, reason: one read-only cell, cut on the DIRECT-ACT path (one cell, under the size floor, LOCAL).

## Not cut

- The remaining hops themselves: the CTO cuts them, or carries a closer to Andrew, on this table (msg 4860).
- Release 5's return: waits on the portal history reader on PROD (CTO msgs 4805, 4819), which is Andrew's word.

## AMENDMENT 1 (2026-10-11 ~12:1xZ): the CTO round-5 analysis arrived after this decomposition was cut

`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_ROUND_5_Y_20261011.md` @ca8aa78b88, section 4, three items.
The round's one issuance (@957aed1f3f) stands; no further cell is cut.

| item | lands as |
|---|---|
| 1. The FWD-1 trace table | cell `AR-y-51` above (the same cell, ruled in msg 4860) |
| 2. The re-release packet for release 5, written and not applied | the issuer's own document, no cell: `deliverables/2.0.0_SA_COO~Y2/release5/NEVER_WIDEN_PAIR_ANLREQ_RELEASE5_RERELEASE_IRPT_STATUS.md` |
| 3. The un-pin of the two members rides that release, not before | section 3 of that packet; no act now |

