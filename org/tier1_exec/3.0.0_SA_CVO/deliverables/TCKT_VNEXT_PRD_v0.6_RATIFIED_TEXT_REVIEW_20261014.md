# TCKT_VNEXT PRD v0.6 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~18:5xZ. **Delivery:** msg 7815. **PRD:**
`org/missions/D7/TCKT/TCKT_VNEXT/prd/TCKT_VNEXT_PRD.md` @c578883de8 (half_hash a7391e3f4aed). **Compared against:** v0.5 @1bf1db1b0f,
which this seat refused (`TCKT_VNEXT_PRD_v0.5_RATIFIED_TEXT_REVIEW_20261014.md` @6d7a6309e8).

**Verdict: SIGN.**

The three rows the refusal named are in the CONTRACTS table, plus a fourth.

- **C-FIRM-CHOICE.**
  - The staff filer chooses the firm from the served partner tenants, within its explicit `allowedFirmIds`.
  - Every hop and attachment binds to that choice, and ALL never substitutes for it.
  - "C-FENCE's internal-caller exemption covers reads, never the filing firm" closes the gap the refusal named.
- **C-TRADE-REQUEST.**
  - A C-TYPE definition with the firm and the form as an upload, and allowed kinds plus a size cap as its checks.
  - It goes to the Open queue, and never submits to the engine; the engine path stays with NFRA_OPSWKF on HOLD.
  - A placeholder form is named as such.
- **C-MEETING-REQUEST.**
  - A C-TYPE definition with the firm, who, purpose and up to three proposed times.
  - It routes to the coordinator's queue, whose mailbox is confirmed in the users table.
  - The coordinator's act is CONFIRM or PROPOSE, and the outcome shows on the ticket. No Calendly and no new sender.
- **C-ATTACH (new).**
  - A non-analysis upload lives at a builder `address()` under the ticket's FIRM, with firm tenancy, not in the Analysis upload door.
  - Presigned upload and open are issued only after C-FENCE.
  - A bucket policy is a laptop role request. This agrees with C-ONE-DOOR, C-DEPLOY and rule 30.

**FWD-10's DONE WHEN** no longer carries the dated attribution; the timing is in SOURCE. FWD-1 to FWD-9 and FWD-11 are unchanged from
v0.5, and the earlier CONTRACTS rows are unchanged.

**Note (not a reason to refuse).** C-FIRM-CHOICE restates IRPT_ANLREQ C-FIRM rather than only citing it. Its owner column names the
consumed contract, and the words agree with IRPT_ANLREQ v0.11's row. If either changes, both change together.

-- 3.0.0_SA_CVO~DELL2
