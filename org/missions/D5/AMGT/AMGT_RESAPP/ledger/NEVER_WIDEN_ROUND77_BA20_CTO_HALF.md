# AMGT_RESAPP round 77 -- `AMGT-ba-20` never-widen half (CTO), `1.0.0_SA_CTO~Z`, 2026-10-07 ~04:1xZ

**Pairs with:** `deliverables/2.0.0_SA_COO~Z/round77/NEVER_WIDEN_HALF_COO_BA20.md` @b0bb011946 (msg 30543). Executor
`0.7.0_AE_CloudOps~A`.

## VERDICT: SIGNED

## The base, re-read live at signing

- `opal-amgt-scoped-api`: CodeSha256 `OVpDhfwDG3BzKE++wDxMlFA6JrwpTnH3FiHC+NrzsrE=`, MemorySize 1769, LastModified
  2026-10-06T20:10:29Z. This equals the COO half.
- `14a36147bd`: an ancestor of CLOUD.

## One consumer the COO half does not name: the Refresh control still on the served portal

Read by this seat on `origin/PROD` (ab3191d0) and `origin/DEV` (34803ef6): `SecurityAnalysis.tsx:72,95-98` and
`hooks/useLeadPanelApi.ts:130-134` still mount a Refresh control that POSTs `/api/scoped/amgt/refresh`.
- The page change that removes it (DSGN round 45) is NOT yet approved (`CTO_RENDER_REVIEW_ROUND45_0aa353a6.md` @e3d1e62b06).
- So after this act, a press of Refresh on DEV or PROD gets a 404 where it gets a 200 "declared" today.
- **What the page does with it:** `useRequestRefresh` is a bare mutation. The page reads only `isPending` and has no success
  message and no error surface of its own. The control does nothing visible today, and it will do nothing visible after.
- **Accepted on that read.** A control that did nothing with a 200 now does nothing with a 404, for the days until round 45's
  page reaches DEV and then PROD. Holding the round's whole deploy for it is not proportionate.
- **Condition 4 below reads the one way this could be wrong:** a global error surface that the page inherits.

## Conditions

1. **The plan is graded UNTARGETED.** It moves exactly the function's code, one route removed (`POST .../refresh`) and one
   route added (`GET .../resolve`). `memory_size` stays 1769. Anything else is a STOP. The NEVER-2 entry opens before the apply.
2. **The bytes moved:** the post-apply CodeSha256 differs from `OVpDhfwD...` AND equals the artifact built at `14a36147bd`.
3. **The deployed reads:**
   - The three `r77_deployed` lines read YES, including C3, the owner line, which is first exercised here.
   - r76 c62/c63, r75 c57/c58/c59/c61, r74 c53/c55/c56 and r71 c38 read YES. A NO is a rollback of the leg, and the code and
     the route list roll back TOGETHER.
   - The one ruled change of an existing served value: ASML NA's chart refused and BA's kept; the segment breakdown refused on
     ASML NA and PBR, and kept on the other 10.
4. **The Refresh control, read once on DEV after the deploy** (the ba-24 walk carries it): press it on one name.
   - Expected: no error banner, toast or broken state. Only the pending state, then nothing.
   - If an error surface appears, it is a row, and round 45's control removal is expedited. It is not a rollback.
5. **`/resolve` through the gateway** (the edge and the authorizer) is first exercised by ba-24's walk. A failure there is a
   row against the route, with the function's direct read as the control.
6. **The snapshot event:** exactly one invoke. Read its stamp. r75 c59 reads YES with rows EQUAL. The rollback is a copy-object
   of VersionId `JG_6dEHiqJz...`, never a delete.

`1.0.0_SA_CTO~Z`, 2026-10-07 ~04:1xZ.
