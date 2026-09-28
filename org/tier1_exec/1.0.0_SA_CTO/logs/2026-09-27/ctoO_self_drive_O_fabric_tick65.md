# /self-drive ~O fabric -- tick 65 (12:20Z-13:0xZ), 1.0.0_SA_CTO~O

**Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_O_FABRIC.md` @56050d290d
**Why written:** an Andrew word executed, and two corrections of this seat's own claims.

## Andrew-direct "recs approved" (~12:2xZ) -- executed

- **Call 1 (re-seat OPLGTW's CTO and CVO legs to ~O): DONE @6fba157e76.** `project.json` leads cto ~A->~O, coo->~O, cvo->~O;
  placement LAPTOP->SITEZ; fabric laptop->site-z; the index entry written alone (check 1 violation -> 0). This meets the
  un-park condition of CVO~O's verdict @e470835e7c. Broadcast: COO~O and CVO~O by file; the laptop's CTO~A and MSTR by
  agentbus (MessageId ea3003c5; not delivered until acked, and that queue is unconsumed).
- **Call 2 (D9 moves to site Z): (a) NO.** D9 stays where it is; the per-project placement fields carry placement.

## W3-S22, ruled as OPLGTW's CTO @244cd0d80f -- and this seat CORRECTS itself twice

1. **My call-1 card and the ~12:05Z push OVERSTATED W3-S22** as "the sprint view is open to any signed-in user". That is
   the RULED design: `sprint_view.py:1-17` and `config.py:99-101` at `110d93fb73` say "The wall is the TENANT ... ruled
   tenant-wide". I had relayed COO~O's framing ("fails open") without reading the module. The row's real gap is that the
   email-only browser routes (`/login`, `/sprint*`, legacy `/callback`) cannot see tid/oid restricted profiles. My roster
   REC is WITHDRAWN (it would narrow a tenant-wide ruled surface and not close `/login` or `/callback`). The fix stays the
   round-2 email-keyed deny cell, due before the next restricted profile; routed to COO~O.
2. **My OA-g-2 CTO half missed a branch.** Any profile record restricts that principal (`data_entitlement.py:28-44`,
   `decide()` `:364-376`), so OA-g-3's portal-only grant also removed Alyssa Keith's OWN native gateway tools. Measured over
   6,895 audit records (2026-09-25..27): her 92 are all `ms_site_children` at 02Z, `ok` after the grant; 0 MCP tool calls.
   So it is latent, not observed. Corrected on the sign-off's bytes; carried to Andrew as an entitlement card.
   OA-g-3 also broke W3-S22's round-1 withholding policy (AC12: no restricted profile for an ALB-login account).

## Card at Andrew (entitlements are his class)

Should a portal-only asker grant also remove the colleague's own gateway tools, as it does today for Alyssa Keith?

## Completion test

NOT DONE -- 0 of 4 projects `complete`. All REACHABLE. Open orders: MX-s-4, MX-s-6 (MCPINDEX); OA-t-1, OA-t-3 (OPALAI).

state: ARMED

## Compiler Tools

`missions-tree-index.py check/derive` (read-only); boto3 over `s3://opal-mcp-audit/audit/dt=2026-09-2{5,6,7}/` (6,895
objects), after the `aws s3 sync` shim wrote 0 files with rc=0 (the known converted-path trap).
