# /self-drive ~O fabric -- ticks 62-63 (11:46Z-12:05Z), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** a call at Andrew changed class, from a cost note to a live served-access item.

## Call 1 re-carded: W3-S22 is now a LIVE served-access item with NO seat able to rule it

`2.0.0_SA_COO~O` (file 20260927T120052Z) measured the path to OPLGTW's `leads.cto` (~A) at 11:58Z:
- the laptop agentbus queue holds 5 messages and 0 in flight, so nothing on the laptop is consuming;
- COO~O's carry of W3-S22 (2ffc52fb, to `1.0.0_SA_CTO~A`) is among them;
- site Z's queue reads 0.

W3-S22 (the `/sprint` roster fails OPEN on the live host: `SPRINT_VIEW_ALLOWED_EMAILS` is set 0 times,
`sprint_view.py:172-174` returns True on an empty roster, and the deploy's `.env` rewrite never writes the key) therefore
reaches NO CTO seat that can rule it. This seat cannot: CVO~O's verdict @e470835e7c gives ~O the OPLGTW COO leg only.
Andrew's call 1 (re-seat OPLGTW's CTO and CVO legs to ~O) is now the only path. Andrew was notified by push at ~12:05Z.
The card is carried as a live served-access item, not a cost note.

REC for whichever CTO rules, unchanged: add `SPRINT_VIEW_ALLOWED_EMAILS` to the `deploy-to-ec2.sh:196` literal, then flip
the check to fail closed, in one release under a never-widen sign-off.

## Also

MX-s-8 complete-accepted by COO~O @2f6277a1c0 (AC1/AC2 4/4 on CLOUD after the drain @18bc4ffe30).

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE. Open orders: MX-s-4, MX-s-6 (MCPINDEX); OA-t-1, OA-t-3 (OPALAI).

state: ARMED

## Compiler Tools

Inbox read only.
