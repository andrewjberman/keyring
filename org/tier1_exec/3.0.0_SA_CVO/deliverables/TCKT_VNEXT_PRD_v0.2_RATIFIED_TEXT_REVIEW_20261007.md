# TCKT_VNEXT PRD v0.2 -- ratified-text half review (L4-R)

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~17:2xZ. Subject: `org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` v0.2
@99eb4053c2, read as the diff against v0.1 @a6978b2ac2, which this seat refused (review @003801aeb8). Asked by msgs 908/909.

**Verdict: SIGN.** Both required corrections are made, and P1 is taken as an owned dependency. Two P2 notes follow.

## The corrections

- **R1 (FWD-2):** DONE WHEN now reads "a sign-in belonging to a different firm (a test account at that firm, made for the purpose) tries
  both and is refused, and the attempt can be repeated on demand for Andrew to watch". It no longer waits on his presence.
- **R2 (FWD-1, FWD-3, FWD-4):** each is driven on DEV by an Opal sign-in, or by a stated bad and good sheet, with Alyssa's real use and her
  two sheets as the organic arm. The SOURCE lines still cite her as the first requester, on Andrew's word.
- **P1:** C-ONE-DOOR names the door's on-behalf refusal (`uploads.py:193, :227-234`) as an owned dependency. Its ruling: admit an internal
  principal whose `allowedFirmIds` names the owner firm, record both principals, and refuse everyone else as now. It is requested from
  IRPT_BCKEND's COO at L5 and never written from this project.

## P2 notes (not blocking)

- **FWD-2's test account is an auth-plane write.** Making a sign-in at another firm writes the production user tables, which an order may
  not do on its own (IRPT_BCKEND-S382), and the portal's user-add act runs on Andrew's ask. So the account is made once, on his word.
  After that, the refusal is repeatable on demand. Name that one act in the round that cuts FWD-2.
- **The door ruling widens who may file.** Admitting an internal principal acting for a firm it is allowed to see changes an authorization
  rule in another project. When IRPT_BCKEND cuts it, it needs a never-widen pair, and its refusal arm is tested exactly as today: an
  internal principal not allowed the owner firm, and a client principal of another firm.

-- 3.0.0_SA_CVO
