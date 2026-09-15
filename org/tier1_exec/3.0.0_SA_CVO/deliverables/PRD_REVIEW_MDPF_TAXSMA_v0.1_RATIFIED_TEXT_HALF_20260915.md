# L4-R review -- MDPF_TAXSMA v0.1, ratified-text half (ENDPOINT + CONTRACTS)

**Reviewer:** 3.0.0_SA_CVO. **PRD:** `org/missions/D8/MDPF/MDPF_TAXSMA/prd/MDPF_TAXSMA_PRD.md` @48befbfcbf (1.0.0_SA_CTO~A).
**Half hash:** c4a17524e8f0. **Delivered:** msgs 96966 and 96968, 07:56Z.

## VERDICT: REFUSE -- one defect, R1

**R1. The "Zero, unknown and incomplete display" CONTRACTS row carries a SUPERSEDED rounding rule.**

- **The row says:** it cites Andrew's L1-only amendment `ANDREW_DIRECT_20260915_024xZ_DSGN_REBRND_WHOLE_DOLLARS_AND_ZERO_L1_BUCKETS_SHOWN.md`
  @fe76e3e036, "with whole-dollar presentation".
- **Andrew's later word supersedes it:**
  `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260915_025xZ_DSGN_REBRND_ROUND_TO_10K_AND_49FINANCIAL_TAX_SMA.md`
  @39aae459ed reads: "Asset Category Views amounts round to the nearest $10,000. This supersedes ~02:4xZ's nearest
  dollar"; and "under $5,000 prints "$0"". The words were his, at ~02:5xZ.
- **What still stands:** the zero/null-L1-shown-as-$0 half of @fe76e3e036. The ~02:5xZ record was built with it.
- **Why it blocks:** CONTRACTS is what a worker implements. A worker reading this row builds whole-dollar Tax
  presentation, and that rule has been overruled by the sovereign.
- **The fix, one line:**
  - cite @39aae459ed for the rounding: nearest $10,000, with "$0" under $5,000;
  - keep @fe76e3e036 for the L1 $0-when-a-sibling-is-valued rule;
  - or state that presentation rounding is the D1_CATVIEWS consumer's rule and not part of this contract.

## CHECKED AND HOLDING (read by this seat at the pins named)

**ENDPOINT, verbatim against the approved text.**
- The approved text is `TAXSMA_D8_PIPELINE_20260915/ENDPOINT_PROPOSAL.md` @8e8afed454, approved by "Approve all eight bars"
  in `ANDREW_DIRECT_MDPF_TAXSMA_ENDPOINT_APPROVED_20260915.md` @e61a60b46f.
- DONE WHEN, ACCEPT and SOURCE are identical: 8 of 8 each.
- The 8 FWD headings are equal once markdown is stripped: 8 of 8. The PRD states that only the heading layout was
  normalized.
- The only seat-like tokens inside the section are the approved SOURCE paths (`org/tier1_exec/1.0.0_SA_CTO/...`), not
  annotations. The section carries no history.

**CONTRACTS, against each counterpart.**
- MDPF_CANON_PRD.md @8d12b77adb:
  - :178 the gold artifact reads "parquet only; one partition per day ... history is never rewritten";
  - :179 the served JSON is "by the publisher alone", with its leaf enumeration (the category-view omission the row
    names);
  - DEC-2 :203-207 reads no dual-write, no shadow prefix, no standing parity comparator.
- The pins resolve: NFRA_OPLMCP_PRD.md @33c581d223, D1_ASSET_CATEGORY_VIEWS_PRD.md @5d356cc426,
  D1_CATVIEWS_SMA_LIVE_PRD.md @42fb68944b, and `org/standards/MDPF_TAXSMA_DATA_CONTRACT.json` @48befbfcbf (version
  0.1.0).
- CTO dispositions 96939, 96944 and 96946 are carried in GOVERNING_CONTRACTS.md @d971e17752, as the PRD cites.
- "These work i like it" is at @3fd386598f, in 4.0.0_SA_CRO's record, line 15.
- The frontend-freeze record is at @65a535f194.
- The existing code the contracts tell a worker to reuse exists at HEAD:
  - `b00_canonical_valuation.py`, which carries `net_mv_plus_cash`;
  - `opal-gateway/app/ms_ingest.py`;
  - `opal-assets-mdpf-portal-publisher`;
  - the 13:30 UTC Gold floor at `mdpf-pipeline/scheduled-floor.tf:133`;
  - the 13:50 publisher at `opal-assets/mdpf_portal_publisher.tf:228`.
- The sovereign prerequisite is stated rather than assumed: Andrew names the person, and authorizes the unattended
  content read, before activation.

## NON-BLOCKING NOTES

- **N1.** Under the $10,000 rounding, a true Tax value under $5,000 prints "$0", like a true zero. FWD-5's
  unknown-versus-zero distinction survives only because unknown or stale Tax is a dated exception (CTO 96939). The row
  would be clearer if it said rounding applies to known values only.
- **N2.** CTO disposition 96960 is cited by message time, and its message carrier is gitignored. Its durable carrier is
  GOVERNING_CONTRACTS.md @48befbfcbf, so cite that pin.
- **N3.** The two schedules were read as DESIRED, in Terraform. Their APPLIED state was not read.
- **N4.** The canonical naming row records MDPF_CANON v2.3:177-179 as stale, pending its owner's prose update at the next
  bump. That is carried, not verified as done.

The stamp binds to half hash c4a17524e8f0. A header-only bump re-opens nothing, and a change to ENDPOINT or CONTRACTS
re-opens this half.
