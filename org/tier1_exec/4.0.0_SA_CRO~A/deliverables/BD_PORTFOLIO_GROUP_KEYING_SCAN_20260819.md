# THE PORTFOLIO-GROUP KEYING SCAN -- transcript intel + landed census + live BD probe (4.0.0_SA_CRO~A, 2026-08-19)

**Authority:** Andrew-direct ~1830Z at this terminal (verbatim record
`ANDREW_DIRECT_20260819_BD_SCANNING_EGRESS_PORTFOLIO_GROUP_KEY_BI_ENDPOINT.md`): scanning egress on
BD, transcript review first, then "try using that same shape but keying based on portfolio_group."
**Egress acts under the grant (all read-scoped):** one catalog pass via the estate's own
`bd_endpoint_sweep.py` (spec-hunt + querytypes 1..25 + roster + sweep; result staged
`s3://opal-data-bd/code/bronze/endpoint_catalog/`) + one qt6 group-keyed sample run (template
`OPAL_CROA_Probe_GroupKey_qt6` id 517678 persisted in BD per the DS-probe precedent -- deletable on
word; run 517679, Completed, 636-row export read + scratch deleted). The grant is CONTINUING
("keep scanning") -- acts logged here as exercised, grant not consumed.

---

## 1. TRANSCRIPT INTEL (Data Discussion, Mike Little, 2026-08-19 -- the rulings that ground everything below)

1. **Portfolio Group = the advisor's book at 49F.** Mike verbatim: *"portfolio group is like it is
   specific for the advisor, so this is the Mitch Johnson portfolio group... his book, essentially"*;
   Andrew: *"the portfolio group is really like advisor key... not based on a strategy"*; Mike:
   *"Right. Yes... it's not how 49 is using it."* Exception: division groups ("49 Private Wealth,"
   2-3 advisors + support, <10% of assets).
2. **Advisors live on the Business Intelligence dashboard** (book-grain view); PDF report templates
   are one-offs; **Client View** = per-relationship dashboard for meeting prep; no BD report goes to
   clients (custodian statements only -- Schwab, now some **Fidelity**, a new custodian mention).
3. Advisor visibility = accounts/relationships ASSIGNED (entitlements, "a different space").
4. Admin exports "come out divided up by portfolio group" -- the group is the admin-side unit too.
5. Client portal usage ~11% ever-logged-in ("Black Diamond's portal kind of sucks") -- the
   client-facing opportunity is greenfield, gated on compliance not tech (Andrew's B2B-first framing).
6. Advisor ask on record (local ops): model membership per account (the SmartX join, already queued).
7. Mike's hypothesis: Salesforce may be source-of-record for advisor roles/locations; Andrew's
   traffic-freshness principle applied. UNTESTED -- a future source-of-record question.

## 2. THE LANDED CENSUS (allocation_390224 export, 2026-08-18 -- no egress needed)

**201 groups | 6,155 accounts | 5,579 accounts (90.6%) sit in 2+ groups.** Groups are OVERLAPPING
VIEWS, never a partition: the same account appears in its advisor's group + "- Local Ops" role
groups + division groups + "49F Schwab AUM." ⛔ **NEVER sum across groups** (the 08-18 all-group MV
sum is ~$10.2B against a ~$1B book -- overlap, not error). Naming carries role semantics: bare
advisor-name groups (the books), "X - Local Ops" (operational views), division/support groups.
**The disambiguator exists in the catalog: `Primary Portfolio Group` (dim id 436, Portfolio level)**
-- BD natively distinguishes membership from PRIMARY assignment; the primary is the partition-like key.

## 3. THE CATALOG SCAN (live, 49f, via bd_endpoint_sweep.py)

- Surface unspec'd (swagger 403/404), OIDC discovery present. Query types live for 49f: qt1-4, 6, 7;
  qt5 (Allocation) 500s on the catalog call for this firm (the persisted 390224 template still runs
  -- the catalog gap is the qt id, not the capability). qt8+ empty.
- **qt6 "BI Billing" is the group-keyed table the ask wanted:** level hierarchy Date -> Team ->
  Relationship -> Client -> **Portfolio Group** -> Portfolio -> Account -> Holding; 150 dims,
  **16 measures incl. BMV, EMV, Net Additions/Flows (incl/excl fees), Fees, Net Gain, Income, New
  Accounts** at month grain. The "BI" in its name is BD's own branding: **this is the Business
  Intelligence dashboard's data model, exposed as a query type** -- the level hierarchy IS the
  dashboard's grouping model from the transcript. The BI dashboard APP itself remains an unmapped
  domain in `data/black_diamond/API/` (only datamining/billing_ar/insurance are cataloged) -- but
  qt6 appears to BE its data; mapping the app's own endpoints is a residual scan target.

## 4. THE GROUP-KEYED PROBE (the "try it" -- executed, Completed)

Template: qt6, dims = Month/Year/**Portfolio Group** (ids 5139/5141/**1140**), measures =
BMV/EMV/Net-Flows-excl-Fees/Fees (49/50/66/55), window 06/01-08/18. Result: **636 rows = 216 groups
x 3 months** -- the entire firm's book economics at advisor-book grain in a 34KB export.

**THE HEADLINE -- the Travis test resolves the attribution gap:**

| basis | Travis Penfield "book" |
|---|---|
| our role-attribution (his meeting words: "tagged as architect to...") | $373M |
| his logical inference in the meeting | "~$460M" |
| the 08-18 allocation-export census (group rows, account-MV sum) | $405.4M |
| **BD's own group-keyed qt6, Aug EMV (as-of 08-18)** | **$456.8M** |

**The vendor's native group-grain number vindicates the logical inference almost exactly** -- the
group definition captures the private-wealth/house-bucket assets the per-account role tagging
misses (his exact Travis example from the meeting, now measured). The allocation-export census
under-reads because that export filters (open, grouped accounts) -- another instance of
its-scope-is-not-the-universe. Monthly shape verified: BMV chains to prior EMV correctly
(423.6 -> 424.0 -> 444.8 -> 456.8 with flows +0.8/+21.2/+6.0M). Fee values returned but
quarterly-cycle shaped -- a longer window is needed before quoting fee numbers (not quoted here).
qt6 also sees 216 groups vs the export's 201 -- the group-keyed read is WIDER than the landed export.

## 5. WHAT TO THREAD IN (recon -> specs; suggestions for CTO frame / COO staffing, not dispatched)

- **T1 -- the book-tie-out oracle (smallest, highest immediate value):** a monthly (or on-demand)
  qt6 group-grain read = the number the ADVISOR SEES on their BD dashboard. Use it as the
  pre-registered tie-out for our ADVI leaderboard/book figures -- the Travis-class discrepancy
  ($373 vs $457) becomes a measured, explainable delta instead of a credibility surprise. Tiny
  surface: 636 rows/quarter. (Exactly Andrew's own meeting words: "do our account levels for this
  advisor view add up to the portfolio group view.")
- **T2 -- dim_portfolio_group + the membership bridge:** the group->account map already LANDS DAILY
  in the allocation export; a gold `dim_portfolio_group` + `bridge_group_account` (with
  `Primary Portfolio Group` as the partition key) gives the estate the advisor-book definition as
  data. Closes the rep-layer vocabulary gap the fam cross-reference left open -- the BOOK is the
  group, roles are attributes on it.
- **T3 -- attribution upgrade (decision for Andrew, framed by CTO):** adopt group membership
  (primary-group for partition, full membership for visibility) as the ADVI book definition,
  replacing/augmenting per-account role-tagging. This is what makes our numbers match what advisors
  expect -- and it is a SERVED-semantics change (P4-class through CTO, never a quiet swap).
- **Residual scan targets under the standing grant:** the BI dashboard app's own endpoint domain
  (unmapped); a qt6 pull at Portfolio-Group + Relationship grain (the Client View parallel);
  the qt5 catalog-500 oddity (surfaced, not chased).

**Routes:** CTO (frame T1-T3) · COO (ledger; T1/T2 are small builds when staffed) · Andrew's card
(T3 + the Travis vindication). PII: client-level data never printed; probe export was group-grain;
scratch deleted.
