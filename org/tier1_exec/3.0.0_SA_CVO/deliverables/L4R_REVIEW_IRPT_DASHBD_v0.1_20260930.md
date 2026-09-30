# L4-R review -- IRPT_DASHBD PRD v0.1, ratified-text half (`3.0.0_SA_CVO`)

**Delivery:** `1.0.0_SA_CTO` message 103250, 2026-09-30T14:02:13Z. **PRD:**
`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md` @`2cb022f549`, half_hash `15dee59be554`, FWD-1..FWD-10.
**Verdict: SIGN.** One wording note (W1), four items for L5 (Q1-Q4). None re-opens the half.

## The review limbs

| limb | result | evidence |
|---|---|---|
| ENDPOINT verbatim against the ratified pin | PASS | the PRD's FWD block against `ENDPOINT_FORWARD_REPORTING_DASHBOARD_20260930.md` @9a3afb2f9c (its only revision), both by `git show`, both 88 lines: 0 differing lines. FWD ids 1-10, all present |
| Andrew's word for the outcomes | PASS as stated | the six messages in `ANDREW_DIRECT_20260930_06xxZ_REPORTING_DASHBOARD_TWO_BRIEFS_SCOPE_ANSWERS.md` (request, five answers, gold is the Opal shape, conservative GIPS, gross of fees, the fee rail, the two-methodology question); a separate DONE WHEN confirmation was not asked, and the PROVENANCE block says so with its rule |
| every operative constraint present | PASS | the alert moratorium is C-MORATORIUM; the per-use vendor word is C-TIEOUT ("no new vendor pull without Andrew's per-use word"); rule 30 is C-NAMES with builder output printed; the cross-firm rule is C-FIRM; no shadow pipeline is C-SHADOW; the tiering is C-TIERS under annex 17c @1fef5f680e (commit read); the taxonomy law is cited by C-COVERAGE (see Q1) |
| no annotation, history or seat name inside the section | PASS with W1 | the section is the endpoint's bytes; its SOURCE lines carry "COO~P record" and seat-free brief references, which is the endpoint's own provenance format |
| CONTRACTS agrees with the counterpart PRDs | PASS | IRPT_BCKEND PRD v0.21 FWD-3 CONSTRAINT ("NO INFLOW/OUTFLOW LOGIC ... the only inputs are end-of-day asset holdings values", Andrew-direct 2026-09-28) is left unchanged and consumed as the guard rail (C-GUARD, C-SHADOW); the narrowing is stated as this project's only, on Andrew's message 4. MDPF_SECCLASS is consumed, not written (C-CLASSES). C-LEASE matches `org/ref/LIVE_ARMS.md`'s ~D row (FAST lease routes ticks to `/closer-drive`; FULL keeps the canonical body) |

## Checks this seat ran (14:1xZ)

- **C-NAMES reproduces from the builder.** `lib/opal_naming.address()` and `name()` return byte-for-byte the eight
  outputs the cell prints (three firms' gold `account_return_daily`, the platinum `series.json.gz` and
  `manifest.json`, `irpt-49f-reporting-adapter-lambda`, `irpt-49f-reporting-publish-lambda`,
  `irpt-49f-reporting-publish-daily`). Both refusals reproduce: `scope 'opal' resolves to no scopes.json row` and
  `partition must be a non-empty ASCII string with no '/'`.
- **C-SOURCES holds.** `infra/logic/registry/reporting_policies.json`: 0 occurrences of each of the eight table names
  and of `"reporting"` (top keys `schema_version`, `policies`).
- **C-LABEL's two citations are at the lines named.** `MethodAndSources.tsx:32-63` carries `TIME_WEIGHTED: 'Time-weighted'`
  and `net: 'net of fees'`; `infra/aws/lambda/investor-reporting/performance/holdings_gold.py:259` is
  `result.method, result.fee_basis, result.annualization = "TIME_WEIGHTED", "NET", "NONE"`. (The PRD names the file
  without its path; it lives under the investor-reporting Lambda, not the gold script tree.)
- **C-CLASSES' portal side is at the lines named.** `assetClass.ts` declares eight `HoldingAssetClass` values and the
  IV-e-115 order (Cash first, then Fixed Income, Equity, Structured, Alternatives, Commodities, Other, Unclassified),
  which is C-DESIGN's display order.
- **Register row** `project.json` @7ae82f3532 carries the two workstreams, Andrew's seating and the endpoint pin.
- **The lease surface today.** `org/mcp/drive-mode.log`'s last ARM (2026-09-30T01:40:50Z, 2-hour term, lapsed) covers
  the whole `portal/src/pages/InvestorReporting` tree, which contains F's two paths. C-LEASE's "the next DSGN_IRPTV1
  lease arm excludes those two paths or holds" is therefore live at the very next arm, not later.

## Wording note (not blocking; the endpoint's bytes)

- **W1.** FWD-1's SOURCE line names `COO~P record`. SOURCE lines are provenance by format, so this is not an
  annotation in the sense the limb guards; a later endpoint revision may cite the record path instead of the seat.

## What you should have asked but did not

- **Q1. C-COVERAGE is one column with one value, and its members are not one intent.** `FEE_RAIL_UNUSED` is true of
  every row today, so a single-valued `coverage` cannot say `PARTIAL_HISTORY` or `NO_LOTS` beside it; the list mixes
  history scope (`PARTIAL_HISTORY`, `MISSING_HISTORY`), a null's reason (`NO_LOTS`, `FEE_RAIL_UNUSED`) and a day's
  quality (`FLOW_UNRECONCILED`, `SOURCE_LAG`). C-GUARD's `LARGE_FLOW` and `NOT_MEASURABLE`, and `return_basis`'s
  `HOLDINGS_INCOME_FALLBACK`, are markers no closed vocabulary in the PRD names. The cell cites rule 24 but ships no
  four-postulate record. The round-1 contract file (`IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`) is where the enum
  is actually proposed: it must carry the record, decide whether `coverage` is a set or a per-column reason, close
  `return_basis`, and move the fee-rail fact to `dim_return_method.fee_basis`, where it already lives. Under Andrew's
  proportionate rule this is a CONTRACTS wording matter, so it does not withhold the half.
- **Q2. FWD-8's ACCEPT reads as a wait on Andrew.** "Agree within a tolerance Andrew accepts" is a wait the L2 rule
  says must be qualified or removed. C-GUARD sets the daily guard tolerance from the data; the tie-out tolerance is a
  different number and has no owner. L5 should cut it as a measured proposal (the 49 Financial sample's agreement
  distribution against Black Diamond) ruled by the CTO under the self-drive rule, with Andrew's word recorded when he
  gives it.
- **Q3. The asset-class vocabulary's owner is not a file the PRD names.** `org/standards/MDPF_SECCLASS_CONTRACT.json`
  v0.3.0 carries `instrument_kind`, `identifier_namespace` and `classified_by`; no asset-class value list surfaced
  under the keys this seat walked. The five classes plus three are today held by the DynamoDB rows and the portal's
  `assetClass.ts`. The `account_class_daily` contract should cite the vocabulary's owning file, or state that the
  portal's type is the authority until MDPF_SECCLASS lands one.
- **Q4. The general platinum home has two candidate rules.** `infra/logic/02_DOCTRINE.md` R6 (line 397) names
  `opal-data-portal-v2/platinum/` as general platinum; line 409 says a general-tenancy scope serves platinum from its
  own bucket. C-SOURCES leaves the choice to the round that builds FWD-6, correctly, but that round should cite which
  of the two it applied and print the builder's answer.

## Not verified by this seat

The `held` citations from the briefs (`holdings_performance.py:12-29`, `ReportingTab.tsx:450-484`, the silver
inventories, the 6.7 s latency baseline, the news tables), the Orion and Black Diamond endpoint claims, and the
SURFACE MANIFEST's `unmeasured` rows. They are outside the ratified-text half.

-- 3.0.0_SA_CVO
