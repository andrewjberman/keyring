# ANDREW-DIRECT 2026-09-15 ~18:0xZ -- MDPF_TAXSMA: the workbook identity is opalbloomberg@opalinvest.com; membership keys off a new "active" field in the spreadsheet

**Seat:** `0.0.0_AB_MSTR` (laptop) · **Channel:** typed at this terminal · **Recorded:** the same turn it was given.
**Answers:** the two MDPF_TAXSMA calls this seat carded through /open-calls at ~18:0xZ:
- CALL 1: G-A, the one named person for the unattended workbook read (PRD §3.9, S16, `TX-r-3`).
- CALL 2: the authorized operator who records `CONFIRM_EFFECTIVE_MEMBERSHIP` (PRD §2 :177, A03; decomposition finding 6).

## VERBATIM AND ENTIRE

> "id have the opalbloomberg@opalinvest.com sitez terminal account do it. also we can just ask that they make a field in
> the spreadsheet for "active" and key off that."

## WHAT IT SETTLES, READ NARROWLY

- **CALL 1 (G-A) ANSWERED:** the identity is **opalbloomberg@opalinvest.com**, the site-Z terminal account. The "do it"
  in his sentence refers to CALL 1's act, the unattended read, and this seat reads the sentence as that authorization.
  G-A's carrier, "Andrew's recorded word naming the one Opal person and authorizing the unattended content read"
  (decomposition s.6), is this record.
- **CALL 2 ANSWERED BY A DESIGN CHANGE, not by naming an operator.** Membership keys off a new **"active"** field in the
  spreadsheet, and the workbook's maintainers ("they") are asked to add it. That replaces v1's ATTESTED-only operator
  disposition as the membership trigger. It is a scope change to the PRD, so it lands as a PRD addendum by the PRD owner
  (`1.0.0_SA_CTO~A`), not by this seat.

## WHAT THIS SEAT MEASURED, AND WHAT IT DID NOT (for the PRD owner, not adjudicated here)

1. **The account exists as an Entra identity.** integrations/bloomberg/READ_HERE.md:67 names
   `opal/mcp/opalbloomberg-login` as "the MS Entra login for the same seat", a different credential from the Bloomberg
   terminal login. Nothing here reads or prints it.
2. **UNMEASURED: whether that account already has access to TAX/Tax SMA Accounts.xlsx.** PRD §3.9 requires a person
   "who already has access". If it does not, granting access is a human SharePoint act, and it is Andrew's to route.
3. **The workbook has no "active" column today.** The contract's header list (MDPF_TAXSMA_DATA_CONTRACT.json :40-50
   region) holds Index ... Ready, Inception Date, Last Trade Date, Traded, Instruction, Comment. The projection is exactly
   seven columns (:52-60), and §3.9's permission is scoped to those seven. Keying off "active" therefore touches:
   - projected_columns;
   - the §3.9 permission text;
   - header/schema-version recognition;
   - S03 membership (`TX-m-1`), whose acceptance lines are cut against the CONFIRM_EFFECTIVE_MEMBERSHIP rule.
4. **An "active" flag is a state, not a date.** v1 membership is effective-dated: the first inclusive day, never
   backdated. Which date an "active" flip carries is the PRD owner's to state. Candidates include the snapshot date on
   which the flip is first observed, or a paired date field. The choice is recorded as open, not chosen here.

## ROUTE

MCP broadcast to `1.0.0_SA_CTO~A` (PRD owner, addendum), `2.0.0_SA_COO~T` (L5 decomposition just landed @62cf5796fc; L6 not
yet cut) and `1.0.0_SA_CTO`, with push state.
