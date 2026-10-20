# NFRA_MCPINDEX -- ROUND-23 ANALYSIS (L10 answer; the round-24 enrichment list)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-20 ~12:3xZ.
**Answers:** `2.0.0_SA_COO~MI`'s slug, msg 36113 (20:28Z 10-19). It was addressed to `1.0.0_SA_CTO`, the laptop base, not this
seat, and sat QUEUED for 16 h; it was found by this seat's outcome-check.
Evidence: `deliverables/2.0.0_SA_COO~MI/round23/evidence/BATTERY_SUMMARY_20261019.md` and `BATTERY_GRADED_20261019.json`.
**Issuer:** `2.0.0_SA_COO~MI`. **PRD:** v0.19 @7c42c0c743.
**Routing note for every future slug:** this seat is `1.0.0_SA_CTO~Z`. A slug to the base serial has no reader here.

## 1. As read

- **Round 23 is terminal:** 19 of 19 orders complete, MAY-CLOSE.
- **FWD-23 (routing):** 127 tools, 13 MISROUTED.
  - 10 are class `link`.
  - 3 are class `code`: `client_get_allocation`, `client_get_fees`, `client_resolve_account`. These went to `2.0.0_SA_COO~O`,
    whose batch16 (OG-rl-17, window 2026-10-21 06:00Z) carries D1-D3.
- **FWD-23 (coverage):** refusals fell from 104 to 36. All 36 are member (b) with an owner named and no row yet.
- **FWD-24 (battery):** PASS 38, EMPTY-CORRECT 4, FAIL 85. The 85 by class:

  | Class | Count |
  |---|---|
  | `source_unchecked` | 35 |
  | `not_run` | 32 |
  | `misrouted` | 11 |
  | `tool_error` | 3 |
  | `source_disagrees` | 2 |
  | `unexpected_empty` | 1 |
  | `route_unproven` | 1 |

  - **67 of the 85 are the battery's own coverage, not a tool fault.** Those are `source_unchecked` plus `not_run`.
  - **The tool or route defects are 18.**
- **FWD-25:**
  - Adam Muller's sheet is written. 15 of 17 roster people have no live profile, and nothing is delivered.
- **Generated `serves` is withheld from the catalog,** because it over-approximates: it removes nothing on the 7 tools that
  already carry `serves`. This is correct.

## 2. Ruling -- a round-N analysis, no addendum

### The round-24 list (ONE issuance; fan out by class; cap 8)

1. **`source_unchecked` (35):** add the source comparison for each tool. Read the routed row's source (S3 key, store or
   integration) and compare it with the answer. A tool whose source cannot be read gives its reason, and stays FAIL until it
   has one.
2. **`not_run` (32):** run each one, or give it a (c) reason.
   - Send tools run ONE real message to the tester's own mailbox or chat, on Andrew's c5c2 yes (@65a05f6658).
   - A tool that needs an input gets a real input from the catalog.
   - A tool that cannot run without a write elsewhere is `PREVIEW-ONLY`, named.
3. **`misrouted` link (10):** fix the catalog rows here, then re-run the routing script.
4. **The 7 remaining FAILs** (`tool_error` 3, `source_disagrees` 2, `unexpected_empty` 1, `route_unproven` 1): name each one by
   tool.
   - A code fault goes to `2.0.0_SA_COO~O` as a defect row.
   - A catalog fault is fixed here.
5. **Coverage (36 member b):** write each row, or move the tool to (c) with its reason. Each row goes through its named owner.
6. **Generated `serves`:** fix the generator so that it writes the traced set only, which REMOVES pairs the code does not
   reach. Then write it. It stays withheld until it can remove a pair.
7. **FWD-25:**
   - A person with no profile is on the legacy path. Their current access is that path's admit set: harvest, etfs, portal and
     news.
   - Generate a sheet for each of the 17. The 8 people with no recorded role get the placeholder relevance (Andrew's yes on
     5ccb and 8cdf, @50bd4a33b4).
   - Write the sheets to the default SharePoint folder named in v0.18.
   - Sending a sheet to its person is held for Andrew's word on the delivery channel. The folder is ready for him.
8. **After batch16 is live (2026-10-21 06:00Z):** re-run the battery and the routing script on opal-data-assets. They grade
   D1-D3 and the 3 `code` misroutes.

**Battery concurrency:** at most 2 calls at a time until batch16's in-flight guard is live (CTO round-46 analysis).
