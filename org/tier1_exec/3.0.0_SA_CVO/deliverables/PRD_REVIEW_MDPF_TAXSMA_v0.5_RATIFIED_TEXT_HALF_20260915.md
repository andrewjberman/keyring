# L4-R review -- MDPF_TAXSMA v0.5, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** 3.0.0_SA_CVO. **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @5061a43a46
(1.0.0_SA_CTO~A). **Half hash:** ab7f2488ad92. **Delivered:** msg 97208, 19:27:41Z.
**Prior:** v0.4 REFUSED on R1 and R2 (review @91875c897c, stamp @4bac56b200).

## VERDICT: SIGN

Both grounds are closed, in the ratified text and in the normative contract. The dropped pins are restored. Nothing else
in the half moved except a date-comparison clarification, which states the existing UTC choice.

## WHAT CHANGED, v0.4 @d317a65ec7 -> v0.5 @5061a43a46 (this seat's diff of the half)

**The whole half grew from 18,024 to 20,707 bytes: 4 lines changed and 10 added. ENDPOINT is byte-identical.**

**R1 is closed: the guard ordering is restored.**
- The Gateway row reads: "**The new route has its own guard before generic `/ms/*` handling.**" That is v0.3's sentence
  verbatim.
- `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` 0.5.0 adds `capability.guard_order`. It requires the exact path and
  method, the route-only bearer, the tid/oid binding, revocation and resource controls to all pass "before
  delegated-token fetch or Graph access", with no fall-through to generic guards on a capability failure.
- `identity_binding.controlled_proof` requires route-dispatch controls proving that the capability guard runs first and
  cannot be skipped.

**R2 is closed: the identity is bound by its immutable principal.**
- The row binds the Andrew-designated account "by its **validated Entra tid/oid principal** ... email is
  designation/display/audit metadata only, never an authorization key". It adds: "Missing, forged or mismatched tid/oid
  fails before delegated-token fetch/Graph, even with the same email".
- The contract backs this:
  - `identity_selection` is rewritten to match;
  - `identity_binding.configuration` holds exactly the approved tid and oid, never caller headers;
  - `trust_source` states that an email match or an unvalidated decode is not proof;
  - `deny` refuses a same-email, different tid-or-oid request, and forbids any email-keyed fallback;
  - `controlled_proof` changes only the tid, then only the oid, and expects 0 token fetches.
- The counterpart is now named and pinned: `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md@f0aa50dbc0`, C1, C2
  and A3. Read at that commit, v0.2:
  - :131 "Carry validated `tid` and `oid` in signed principal context; email is display/audit metadata only";
  - :145 "Key grants by tid/oid, not email";
  - :255 A3 "tid/oid mismatch denied even with same email".
  The file has 0 changes from f0aa50dbc0 to HEAD. So the half now agrees with the counterpart that governs the Gateway it
  rides.
- `activation_proof` now says "The relayed whoami email MATCH is not proof of this immutable binding."

**The pins are restored** in the row and in `capability.counterpart_refs`:
- `docs/architecture/NFRA_OPLMCP_PRD.md@33c581d223e2e3bac5e44a37abb407b5f79f82de`, sections 1, 2 decision 1 and 6;
- CTO 96946 at `GOVERNING_CONTRACTS.md@d971e17752`.
v0.4's review measured NFRA_OPLMCP_PRD.md at 0 commits since 33c581d223.

**The date comparison adds no new choice.**
- `membership.date_comparison` compares the UTC calendar date of source_observed_at to the exchange-session
  valuation_date as ISO dates: start <= valuation_date < end.
- Its example is 2026-09-16T00:30Z, which is September 15 at 20:30 EDT, with the membership boundary on September 16.
- That is FIRST_OBSERVED_UTC made explicit. It carries the CRO's non-blocking note from the v0.4 brief review.
- It is consistent with the endpoint:
  - FWD-3 -- a controlled change reaches a dated inclusion;
  - FWD-5 -- an earlier unverified session stays explicit, never zero.

**Unchanged:** `/artifacts/*/args` (this seat's diff finds 0 changed). The v0.3 builder run stands: 13 of 15 MATCH, and 2
wait on the gateway registry row. The Traded key and the named identity, verified faithful at v0.4, are unchanged in
substance.

## CARRIED, NOT BLOCKING

- **N5.** The gateway registry row. Its trigger is LGIC_ENFORCE round 2 EN-r-5. This seat grades the two gateway
  addresses against builder output at L9.
- **N6.** Andrew's ~14:0xZ Gold-placement question stays open. It is not a ruling.
- **N7.** Workbook access for the designated account stays UNMEASURED, as Andrew stated it. TX-r-3 must prove the
  tid/oid binding and one controlled read before activation. A failure neither activates nor widens anything.
- **N8.** NFRA_OPLGTW is mid-round. Its principal model (durable tid/oid profiles, W3-S9's email-keyed tiers still
  being removed) lands before MDPF_TAXSMA's Gateway cells should be cut against it. The row's "shared Gateway
  sequencing" condition and the recut's Gateway ordering carry this. This seat checks the cut at L9.

The stamp binds to half hash ab7f2488ad92. A header-only bump re-opens nothing. A change to ENDPOINT or CONTRACTS
re-opens this half.
