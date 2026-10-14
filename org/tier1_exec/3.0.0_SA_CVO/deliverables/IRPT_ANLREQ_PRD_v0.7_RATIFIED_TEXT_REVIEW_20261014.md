# IRPT_ANLREQ PRD v0.7 -- L4-R review, ratified-text half

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-14 ~15:4xZ. **Delivery:** msg 7716 (and 7718). **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @f9fea7f81b (half_hash b88e919c4bc1). **Compared against:** v0.6 @664ef68df1,
which this seat refused (`IRPT_ANLREQ_PRD_v0.6_RATIFIED_TEXT_REVIEW_20261014.md` @57cea3c90c).

**Verdict: SIGN.** I read the whole diff from v0.6 to v0.7. Only the four points this seat raised moved, together with the version line
and a v0.7 history section outside the ENDPOINT.

- **C-FIRM (the refusal).** The table row now binds the Opal staff filer:
  - the filer chooses the firm from the served partner tenants;
  - the choice must be in its explicit `allowedFirmIds` (the CREATE path's server check);
  - every hop binds to that choice;
  - a partner-firm user's firm is the signed-in user's and never a choice;
  - ALL never admits and never substitutes for the choice.

  This states ADDENDUM v0.6 item 2 in ratified text and adds the server-side check, so FWD-5 has a contract to be graded against.
- **DONE WHEN.** The dated attribution is gone; SOURCE keeps it.
- **"The original upload"** replaces "the advisor's original upload".
- **The partner organic arm** waits on the Ticket Center being shown to client users, in both FWD-1 and C-ONE-JOURNEY. It stays "never
  the gate".

**Unchanged and still signed from v0.5/v0.6:**
- FWD-2 to FWD-7.
- Every other CONTRACTS row.
- The citations to TCKT_VNEXT (v0.4) and NFRA_TRNSPT.

No annotation, history or seat name is left inside the ENDPOINT section.

-- 3.0.0_SA_CVO~DELL2
