# CTO fold-in -- the three IRPT briefs (Performance, Analysis, Holdings) into the COO workstreams

By `1.0.0_SA_CTO`, 2026-10-02 ~17:2xZ, on Andrew's word ("distributing these to CTO for immediate fold in to the relevant COOs
workstreams"). The word is recorded in
`org/tier1_exec/4.0.0_SA_CRO~X/deliverables/ANDREW_DIRECT_20261002_145xZ_IRPT_THREE_SURFACES_STATUS_AND_THREE_BRIEFS.md`
@fc46925968, with addenda @c56606d5ce and @25c40b0035. The briefs, all @80fa729b0e, are in the same folder:
`IRPT_BRIEF_1_PERFORMANCE_...`, `IRPT_BRIEF_2_ANALYSIS_...` and `IRPT_BRIEF_3_HOLDINGS_...`. Rulings: batch 178.

**How it folds in.** IRPT_DASHBD's ENDPOINT already holds the Performance outcomes: FWD-1 is one account loading, FWD-2 is
"any account of any firm the gold covers loads the same way", and FWD-8 is "total return, before advisory fees and labelled
so". So no ENDPOINT changes and no half re-opens. Every outcome below is an ENRICHMENT the named COO cuts under Rule 27, or a
FAST item for a lane under a live lease. This seat cuts no order.

## 1. Performance (`2.0.0_SA_COO~P`; the portal half is `2.0.0_SA_COO~D`)

| item | outcome | where | order |
|---|---|---|---|
| P-4 | The figure says what it is. The served PATH A stamps `fee_basis = "NET"` on a no-fee price return (`performance/holdings_gold.py:270`). That is a DEFECT serving today: file the row and fix the label now. PATH B labels gross of fees (FWD-8) | IRPT_BCKEND, `~P` | 1, now |
| P-2 | Every 49 Financial account in the holdings population gets a published manifest and series; then Inflection and Cottonwood, each when its reporting gold serves. Andrew's 14:5xZ words are the deliberate act that `reporting-gold/handler.py:18-19` waits for: "all of that has to be designed in a manner that it is precomputed. There cannot be any lags in this functionn" | IRPT_DASHBD round 3, `~P` | 2 |
| P-3 | The picker reads ONE precomputed per-client summary, not one PATH A request per account (`ReportingTab.tsx:614-640`). Every new address is `lib/opal_naming.py address()` output, cited in the cell (rule 30). Backend summary at `~P`; the page at `~D` | IRPT_DASHBD round 3, `~P` + `~D` | 3, with P-2 |
| P-1 | Acceptance for P-2 and P-3: an advisor opens the Performance tab for any 49 Financial client, and the picker and chart paint in under 2 s; a window change computes nothing on the backend. Measured by a signed-in walk on port 5174 | `~P` grades, `~D` walks | with P-3 |
| P-6 | No two paths: when PATH B covers every 49 Financial account, PATH A's 49 Financial route is retired IN THE SAME WINDOW. This is Andrew's standing veto on build-alongside paths. The same holds per firm | IRPT_BCKEND + IRPT_DASHBD, `~P` | 4, at P-2's close |
| P-5 | One population tie-out of the served figure against Black Diamond's performance endpoint, on like day sets, per period, with the band stated before the run. It runs on the figure P-2 publishes. A population pull is a fresh vendor pull beyond card 4's five accounts, so it waits on Andrew's per-use word (section 4) | IRPT_DASHBD, `~P` | 5, after P-2 |
| P-7 | Naming: section 3, ruling 3 | -- | -- |

## 2. Analysis (`2.0.0_SA_COO~Y`; the page and walker are `2.0.0_SA_COO~D`'s; `3.0.0_SA_CVO` grades)

Each case uses the files on the laptop at `C:\Users\AndrewBerman\Downloads`, cited by sha256 prefix in brief 2 section 4. Runs go
one at a time (the solo gate). No YCharts browser sign-in is allowed during a run (row S233).

| item | outcome | needs | order |
|---|---|---|---|
| Y-1 | Case A: the easy file (99 rows), variant 1 Overview, from the page; open the READY report; each page hop joined to its backend log lines by `UP-`/`REQ-` id. This also settles brief 2 item 4.1 (the `M:` mutual-fund form) on a real answer | today's code + the harness (Y-H) | 1 |
| Y-B | Baselines on today's code: the typo file and Case D each reach `NEEDS_CORRECTION` as described, recorded before the gates change | today's code | 1 |
| Y-2 | Case B: easy file, variant 2 against Opal Ultra Long-Term: a READY Comparison | brief 2 item 2.1 (`~D`: the composer stops forcing an upload to Overview) and the backend accepting comparisons with an upload (`~Y`) | 2 |
| Y-3 | Case C: easy file, variant 3 against ULT and IWM: a READY Multi-Comp | ruling 4 (a ticker is admitted as a comparison) + 2.1 | 2 |
| Y-4 | Typo: the page names row 2 `APPL` as a likely typo and offers `AAPL`; accepting continues without a new upload | ruling 5 (the gates wired) + the page's suggestion UI (`~D`) | 3 |
| Y-5 | Case D: rows 14-17 are named real but untracked; a proxy is offered for each; the user approves one (the expected choice, stated before the run: SGOV, as Alyssa Keith chose) and gets a READY Overview | ruling 5 | 3 |
| Y-6 | Reliability: each case passes twice in a row, run by a service agent walking the page and capturing backend operations; submit-to-READY and open-to-sections times recorded per run | all of the above | 4 |
| Y-H | THE HARNESS: a page-walk submit mode that uploads and submits ONE named case under a packet, captures the page's network requests, and joins them to the backend lines. `/ui-walk` stays read-only by its own contract; the submit mode is a separate script under `~D`'s deliverables. `~Y` supplies the backend join: the log groups `irpt-ycharts-generate` and `irpt-status`, and the YCharts job log over SSM | `~D` + `~Y` | 1 |

## 3. Holdings (Andrew mapped it to `2.0.0_SA_COO~M`; the map's code is `2.0.0_SA_COO~D`'s, by every commit to the file)

| item | outcome | where |
|---|---|---|
| H-1 | The Securities map shows every security in the view as its own tile, with no "Other Securities" / "Smaller Holdings" tile, legend entry or footnote. Drop `groupSmallIntoOther` and retire `TOP_HOLDINGS_COUNT`, `OTHER_TILE_*`, the legend entry and the footnote (`HoldingsTreemap.tsx:252,265,400,485,639,642`). Re-golden the three tests that pin the grouping. The one-tile-per-security merge (UIR-43) stays. `DrillTree.tsx`'s wedge-label rule is untouched. Andrew's 14:5xZ word supersedes his 09-30 grouping word | `~D`, DSGN_IRPTV1 lease (`tabs/holdings`) |
| H-2 | Hovering any tile, the smallest included, shows the security's name, class, weight and amount | `~D` |
| H-3 | The tiles' weights sum to the selection's securities total | `~D` |
| proof | A signed-in walk on port 5174 at 49 Financial's largest client and one Cottonwood client: screenshots, plus a DOM tile count equal to the distinct securities in that served snapshot | `~D` walks; `~M` reads the snapshot count |
| record | `STATUS~M.md` still names the 10-01 pin; `~M` brings it current. Brief 3 item 1.4(d), the TARGET fold, comes back as its own ask with its measurement once H-1 lands | `~M` |

## 4. Rulings on the briefs' calls (batch 178), and the one act only Andrew can do

1. **Net or gross (brief 1, call 1): GROSS.** Andrew's 2026-09-30 words stand: "Yes gross of fees is correct, we're not dealing with
   these fuckers fees because we don' tknow their fee methodology". Today's "net and gross" describes what he had heard, not a new
   order. The label is fixed (P-4). The fee rail is built when a fee field exists.
2. **Widen the precomputed path (call 2): YES.** All 49 Financial accounts first, then each firm as its gold serves (P-2). PATH A is
   retired per firm in the same window (P-6).
3. **Naming (call 3):** the nine request-path Lambdas were served before this word, so they are EXISTING pipelines. Each reaches
   conformance through its own R19 migration, never as a rider on another packet, and none is an R20 departure.
   `irpt-performance-adapter` is RETIRED by P-6 rather than renamed. The migration for the other eight is registered as a project
   later, through `0.0.0_AB_MSTR`.
4. **Tickers as comparisons (brief 2 item 2.3): IN SCOPE.** Andrew named Case C "against ULT and IWM". `~Y` admits an ETF the
   classification table holds as a comparison key, through the same identity check as an uploaded symbol. If that changes the
   meaning of a CONTRACTS row (`AnalysisSubmissionRequest`'s comparison-key domain), `~Y`'s packet names the row and this seat
   writes the PRD addendum.
5. **The two gates (brief 2 section 3): WIRE BOTH.** The check gate offers a typo's likely ticker. The swap gate offers similar ETFs
   AND accepts a user-named proxy ticker that YCharts verifies, so Case D's stated proxy (SGOV) is reachable whatever the gate
   suggests. Vendor: Kimi is covered by Andrew's 2026-10-02 ~13:1xZ word "Yes Kimi can be called freely" (record @59df408d14), and
   YCharts by his 2026-09-27 word "yes you can run as many analysis attempts as needed".
6. **The ONE act only Andrew can do (P-5): a population pull of Black Diamond's performance endpoint** over Opal's gap-free segments
   for the 49 Financial population, after P-2 publishes. Citation: CLAUDE.md "NEVER call an external vendor API without Andrew's
   explicit per-use word". Card 4's word covers five accounts, not a population. REC: yes, after P-2.

-- 1.0.0_SA_CTO

## Correction (2026-10-02 ~17:4xZ, `4.0.0_SA_CRO~X` msg 104331)

Brief 2 is folded at @8a961a8573, not @80fa729b0e. Its section 3.3 had said that wiring the gates needed Andrew's word; Kimi is
whitelisted as VEW-3, "can be called freely" (`org/ref/VENDOR_EGRESS_WHITELIST.yaml`). Ruling 5 above already reached the same
conclusion, so nothing in the fold-in changes.
