# L4-R review -- MDPF_TAXSMA v0.4, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** 3.0.0_SA_CVO. **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @d317a65ec7
(1.0.0_SA_CTO~A). **Half hash:** da428d318d04. **Delivered:** msg 97204, 18:48:22Z.
**Prior:** v0.3 SIGNED (review @1a7f21c29e, stamp @294bd175ce).

## VERDICT: REFUSE -- on R1 and R2, both in the "Gateway delegated identity" row. Each fix is a line.

The Traded and named-identity content is faithful to Andrew's two records, and the ENDPOINT is intact. The refusal
comes from the one row that changed shape. It dropped an operative guard-ordering constraint, and it names the
unattended-read identity only by email. The Gateway's own PRD forbids keying authorization on email.

## R1 -- an operative constraint was dropped: the route's own guard before generic `/ms/*` handling

- v0.3's row @61748ba2e0 carried: "The new route has its own guard before generic `/ms/*` handling."
- v0.4's row @d317a65ec7 does not carry it, and the rewritten row has no equivalent.
- This seat searched the whole v0.4 PRD and `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` 0.4.0 for `/ms/*`,
  "generic /ms" and "own guard". There are 0 hits in either. So it is not moved elsewhere; it is gone.
- `capability.credential_boundary` still carries the route-only bearer: "valid only for this exact route ... its bearer
  authorizes no other route". That limits what the bearer opens. It does not fix the ORDER of the guards.
- The ordering is live, not academic. `IDENTITY_ACCESS_PROOF_97190.json` @d317a65ec7 records `get_site_item` refused
  by "the per-identity Gateway tool guard before Graph". That is the generic path. The capability route must be guarded
  on its own terms before that handling, or its behaviour depends on whichever generic guard runs first.
- **Remedy:** restore the sentence in the row, or its equivalent in `capability` in the data contract.

## R2 -- the identity is named by email, and no binding form is stated; the Gateway's PRD keys grants by tid/oid

- v0.4 names the identity `opalbloomberg@opalinvest.com`. The PRD row says so, and so do the data contract's
  `capability.identity_selection` ("Exactly opalbloomberg@opalinvest.com") and `capability.named_identity`.
- Nowhere in the half or the contract does it say how the Gateway binds that identity. There are 0 hits for tid, oid or
  object id in the contract.
- The route rides the Gateway that `NFRA_OPLGTW` is rebuilding now. `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md`
  v0.2 at HEAD says:
  - :131, "Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata only";
  - :145, "Key grants by tid/oid, not email";
  - acceptance A3 at :255, "tid/oid mismatch denied even with same email".
- Read literally, "Exactly <email>" invites an email comparison in the new route's guard. That is the class NFRA_OPLGTW
  row W3-S9 is removing from the Gateway: "every authorization decision after the guard still keys on the email".
- **Remedy:** state that the named identity is bound by its Entra tid/oid principal. The email is Andrew's designation
  and display/audit metadata. Name `NFRA_OPLGTW` PRD v0.2 as a counterpart in the row.

## NOT GROUNDS, fix in the same bump -- the counterpart pins were dropped

- v0.3 pinned `docs/architecture/NFRA_OPLMCP_PRD.md@33c581d223e2e3bac5e44a37abb407b5f79f82de`, sections 1, 2 decision 1
  and 6, and CTO 96946 in `GOVERNING_CONTRACTS.md@d971e17752`.
- v0.4 cites "NFRA_OPLMCP / CTO96946" with no vintage.
- NFRA_OPLMCP_PRD.md has 0 commits since 33c581d223, so the substance agrees and the loss is a citation's. A citation
  without a vintage is not a citation, though, so restore both pins when the row is touched for R1 and R2.
- The dropped "No app-only Graph permission, second token store, copied research credential, or generic caller
  identity" is carried in substance by v0.4's "No default identity, copied token, app-only grant, second store ...".

## WHAT HOLDS (so the re-review is one read of the changed row)

- **ENDPOINT is byte-identical to v0.3: 4,024 bytes.** All 8 DONE WHEN / ACCEPT / SOURCE lines stand.
- **The Traded key is faithful to Andrew's record ~18:3xZ @1729cef85e** ("'Traded' signifies that the account is live,
  thats what we use to count an active account"; "We dont need a human we use a key"):
  - Traded=Yes alone asserts membership, and Ready does not gate it;
  - initial human CONFIRM_EFFECTIVE_MEMBERSHIP is retired;
  - no new column, and no request goes to the workbook maintainers.
- **The PRD owner's choices** stay inside the room the record left for them:
  - FIRST_OBSERVED_UTC dating, with unknown earlier history explicit;
  - the live count computed before custodian and value filters;
  - value coverage kept separate.
- **The endpoint still stands:**
  - FWD-1 -- a funded account that is not Traded stays outside;
  - FWD-2 -- candidates are not live automatically;
  - FWD-3 -- a controlled Traded change and its correction reach a dated inclusion with no manual list patch;
  - FWD-5 -- `business_active_accounts` is nullable, and "Null means unknown, never zero".
- **The named identity is faithful to Andrew's record ~18:0xZ @f95470f384:** "id have the opalbloomberg@opalinvest.com
  sitez terminal account do it". Only its G-A half stands, as the addendum says.
- **Access is carried as Andrew stated it: "believed but UNMEASURED".** He said "I think that email already has
  access". No probe or widening is ordered, and a failed read at TX-r-3 does not activate.
- **No artifact address moved.** The 0.3.0 -> 0.4.0 contract diff touches no `/artifacts/*/args`, so this seat's v0.3
  builder run stands: 13 of 15 MATCH, 2 pending gateway.
- **Rows outside the Gateway row are unchanged**, apart from the Workbook row, the addendum paragraph and the preamble's
  version string, all read above.
- **Carried from v0.3:** N5 (the gateway registry row, now triggered by LGIC_ENFORCE round 2 EN-r-5) and N6 (Andrew's
  open ~14:0xZ Gold-placement question, not a ruling).
- **The v0.3 sovereign prerequisite is now answered in part.** Andrew named the person. The unattended content read is
  authorized per the ~18:0xZ record's reading of "do it". The controlled read at TX-r-3 still has to measure access.

This refusal binds to half hash da428d318d04. The remedy touches CONTRACTS only, so it re-opens this half and no other.
