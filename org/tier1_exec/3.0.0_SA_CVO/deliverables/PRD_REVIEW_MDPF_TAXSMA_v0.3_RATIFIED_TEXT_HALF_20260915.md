# L4-R review -- MDPF_TAXSMA v0.3, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** 3.0.0_SA_CVO. **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @61748ba2e0
(1.0.0_SA_CTO~A). **Half hash:** fb75838bf3ac. **Delivered:** msg 97155 at 16:37:17Z; msg 97157 at 16:37:44Z repeated it.
**Prior:** v0.2 SIGNED (review @20504bde03, stamp @214982df0b, half hash fed0ad5c18f3).

## VERDICT: SIGN

The half moved in three places, and each agrees with its source:
- The data contract's version reference, whose v0.3.0 content matches the addendum.
- The consumer row's exception clause, which matches the R20 register at the cited commit.
- The new LGIC conformance addendum. This seat's own builder run backs every resolvable address it declares.

The only address that does not resolve is the declared pending gateway prerequisite. 1.0.0_SA_CTO's 97152 permits this landing before that prerequisite lands.

## WHAT CHANGED, v0.2 @8ab2dc2bc6 -> v0.3 @61748ba2e0 (this seat's diff of the half, ENDPOINT through CONTRACTS)

**The whole half grew from 12,902 to 15,743 bytes: 2 lines changed and 12 added. There are no other changes.**

**ENDPOINT is byte-identical: 4,024 bytes, 0 changed lines.** The v0.1 and v0.2 checks stand, including DONE WHEN,
ACCEPT and SOURCE at 8 of 8 against `ENDPOINT_PROPOSAL.md` @8e8afed454.

**CONTRACTS, the two changed lines:**
1. The preamble names the data contract `v0.3.0`, and `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` @61748ba2e0 reads
   0.3.0. This seat's JSON path diff against 0.2.0:
   - F1 -- the source is `gateway`. `workbook_snapshot` args are `gateway`; `workbook.source_boundary` names system
     `gateway`, `registry_registration.state PENDING_BUILD_PREREQUISITE`, class PLATFORM_SUBSYSTEM and owner D9. Bronze
     keeps the response body byte-for-byte.
   - F2 -- a new `workbook_silver` artifact, written by S19 and read by S03. It keeps every row and column, typed with
     a kind enum, and refuses rather than coerces.
   - F3 -- `firm_served` drops its builder address. It gains
     `historical_address s3://opal-data-portal-v2/platinum/mdpf/49financial/category-views.json` with
     `exception_ref E1`.
   - `lgic_exceptions` E1 (X7, CONDITIONAL) and E2 (X2, PERMANENT), both GRANTED at 9cf4a274db.
   - The `date=` label is the knowledge_date, never the valuation_date. `membership_dispositions` has no expiry.
   - `operations.l6_release` is HELD pending both v0.3 halves.
   - The response boundary and error vocabulary are not in the changed set.
2. The "Consumer and migration boundary" row keeps the 49financial and Global served keys unchanged, "under granted R20
   entries X7 (conditional) and X2 (permanent) at `9cf4a274db`". Read at that commit:
   - `infra/logic/02_DOCTRINE.md` section 4, lines 341 (X2) and 345 (X7);
   - `infra/logic/06_CONFORMANCE_LEDGER.md` section 6, lines 131 (X2, PERMANENT, GRANTED) and 136 (X7, CONDITIONAL,
     expiring when MDPF_CANON repoints), with counts at line 152;
   - the commit message quotes Andrew's ~14:4xZ "RECS APPROVED" verbatim for cards E1 and E2.
   X7's scope, `opal-data-portal-v2/platinum/mdpf/49financial/`, contains the contract's `historical_address`.

**CONTRACTS, the one new subsection: "LGIC conformance addendum, CTO97115".** It binds the pipeline to Rule 30
(`CLAUDE.md@a3d77717df`) and states F1-F3 as above.

## RULE 30 CHECK -- this seat's own builder run, a different instrument from the author's

Every call in `LGIC_V03_BUILDER_EVIDENCE.json` @61748ba2e0 was re-run through `lib/opal_naming.address()` and `name()`
at HEAD:
- 15 calls: 13 MATCH byte-equal to the recorded output, 0 MISMATCH, 2 REFUSED.
- The 13 matches are: 5 state/gold artifacts, the Global category Gold, the runtime role `mdpf-49f-taxsma-role`, and the
  7 v0.2 correction calls.
- The 2 refusals are exactly the `gateway` Bronze and Silver addresses: "source 'gateway' is not a systems.json key".
  `infra/logic/registry/systems.json` has 16 rows at HEAD, with no gateway row; last touched @a925c8a642.
- Both refusals are the declared pending prerequisite. The contract carries a builder plus args, not a hand-typed
  address. So the form Rule 30 requires is met, and only the output waits on the row.
- The permission is 1.0.0_SA_CTO's 97152, recorded verbatim in `LGIC_LANDING_DIRECTION_97152.md` @61748ba2e0: "The v0.3
  TEXT is correct under LGIC with or without the row."
- The v0.2 correction is right. v0.2's `firm_served` builder address resolves, to the firm bucket's platinum, but it is
  not the home the served route reads. X7 keeps the one existing home.

## CARRIED, NOT BLOCKING

- **N5. The gateway row.** The two gateway addresses stay unverified by builder output until
  `infra/logic/registry/systems.json` carries `gateway`. S02's build cannot begin before then. 1.0.0_SA_CTO's 97152
  commits that seat to re-run the conformance read when the row is at HEAD. This seat grades those two addresses against
  builder output at L9.
- **N6. Andrew's ~14:0xZ Gold-placement question stays open.** It is recorded as "OPEN QUESTION, NOT A RULING" at
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_140xZ_COOT_TAXSMA_GOLD_PLACEMENT_QUESTION_AND_DRAW_THE_FLOW.md`.
  v0.3 keeps `taxsma_assets` in the firm bucket's Gold under 96960. This signature neither answers nor forecloses his
  question. If he rules a change, it arrives as an addendum and re-opens this half.
- **The E1/E2 relay 97126 was not read by this seat.** It is not a tracked record. The R20 carrier at 9cf4a274db holds
  the verbatim quote, and that is the acknowledgment R20 names.
- **N3 and N4 from v0.2 stand, and so does the sovereign prerequisite.** Andrew names the person and authorizes the
  unattended content read before activation. This sign-off grants neither.

The stamp binds to half hash fb75838bf3ac. A header-only bump re-opens nothing. A change to ENDPOINT or CONTRACTS
re-opens this half.
