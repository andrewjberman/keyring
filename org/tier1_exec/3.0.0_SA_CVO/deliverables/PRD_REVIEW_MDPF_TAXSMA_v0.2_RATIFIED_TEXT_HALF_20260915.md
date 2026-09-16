# L4-R review -- MDPF_TAXSMA v0.2, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** 3.0.0_SA_CVO. **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @8ab2dc2bc6
(1.0.0_SA_CTO~A). **Half hash:** fed0ad5c18f3. **Delivered:** msg 96990, 08:32Z.
**Prior:** v0.1 REFUSED on R1 (review @e53b06bd38, stamp @8699f4ba7c).

## VERDICT: SIGN

R1 is closed, and N1 and N2 are taken. Nothing else in the half moved apart from the data-contract version reference,
and its target changed consistently.

## WHAT CHANGED, v0.1 @48befbfcbf -> v0.2 @8ab2dc2bc6 (this seat's section diff)

**ENDPOINT is byte-identical: 4024 bytes, 0 changed lines.**
- The v0.1 check stands: DONE WHEN, ACCEPT and SOURCE match 8 of 8 against the approved
  `ENDPOINT_PROPOSAL.md` @8e8afed454 ("Approve all eight bars", @e61a60b46f).
- The headings are equal once markdown is stripped: 8 of 8.

**CONTRACTS: exactly 3 changed lines. There are no others.**
1. The preamble names the data contract as `v0.2.0` instead of `v0.1.0`.
   - `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` @8ab2dc2bc6 reads version 0.2.0.
   - A JSON diff against v0.1.0 changes exactly 4 paths: `/version`, `/categories/wire_extension/version`, a new
     `/membership/effective_date_rule`, and `/status_axes/membership_date_status`, which drops `SOURCE_PROVEN`.
   - The new rule is: initial effective membership is ATTESTED-only; only an authorized operator's
     `CONFIRM_EFFECTIVE_MEMBERSHIP` disposition, with a full account_key and effective_date, sets it.
   - This agrees with the CONTRACTS row "Workbook business claims" ("`Traded=Yes` ... does not independently prove
     historical activation").
   - The response boundary, limits and error vocabulary are unchanged.
2. **N2 is taken.** The "Canonical naming and tenancy" row cites CTO disposition 96960 through
   `GOVERNING_CONTRACTS.md@48befbfcbf`, and that file at that commit carries 96960.
3. **R1 is closed, and N1 is taken.** The "Zero, unknown and incomplete display" row:
   - keeps `@fe76e3e036` ONLY for the L1 $0-when-a-sibling-is-valued rule, and says L2 is not amended;
   - cites `ANDREW_DIRECT_20260915_025xZ_DSGN_REBRND_ROUND_TO_10K_AND_49FINANCIAL_TAX_SMA.md@39aae459ed` for the rounding:
     "rounds known amounts to the nearest $10,000 at display, so a known amount under $5,000 prints "$0"". This matches
     that record's text as this seat read it at v0.1's review.
   - adds that unknown or stale Tax "is never rounded/coerced to $0 or hidden", and that the canonical value keeps its
     cents, so a rounded "$0" changes neither value nor status. That is FWD-5's unknown-versus-zero distinction, held.

Everything v0.1's review found holding is unchanged, because those lines did not move. That covers the MDPF_CANON :178,
:179 and DEC-2 pins, the NFRA_OPLMCP and D1 pins, 96939, 96944 and 96946, "These work i like it", the freeze record, and
the reuse targets.

## CARRIED, NOT BLOCKING

- **N3.** The 13:30 floor and 13:50 publisher were read as DESIRED, in Terraform, not APPLIED.
- **N4.** MDPF_CANON v2.3:177-179's prose update waits for its owner's next bump. The category-view artifact addition is
  routed to that owner.
- **The sovereign prerequisite stands as written:** Andrew names the person, and authorizes the unattended content read,
  before activation. This sign-off grants neither.

The stamp binds to half hash fed0ad5c18f3. A header-only bump re-opens nothing, and a change to ENDPOINT or CONTRACTS
re-opens this half.
