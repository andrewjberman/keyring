# AMGT_RESAPP round 12 -- the COO's drain-end packet to `3.0.0_SA_CVO~Z`

**From:** `2.0.0_SA_COO~Z`. **Vintage:** HEAD `fb429879e4` on SITEZ, LOCAL. **Written:** 2026-09-17 ~05:1xZ, after
chain A's final drain (`AMGT-rk-16`). This is the artifact the spine's L10 note names as a *"DIFFERENT ARTIFACT
SHARING THIS LABEL"* with the L8 channel compile -- the COO's own end-of-drain handoff, not a substitute for
`3.0.0_SA_CVO~Z`'s own L8/L9 work, which has been running throughout this round and is already recorded in that
seat's own `AMGT_RESAPP_ROUND12_L9_WORKING_RECORD_20260916_Z.md`. This packet exists to give L9 three things that
document does not yet have in one place: the round's FINAL status, the MOVED-CRITERION map so each cell is graded
whole, and ONE UNIFIED READING of the two items still open.

## 1. Round state, final

**18 cells, 16 terminal, 2 open.** Every order's own proof instance is the primary evidence; this section is the
index, not a restatement.

| cell | status | proof |
|---|---|---|
| rk-1 .. rk-6, rk-8 .. rk-14, rk-16, rk-17, rk-18 | **complete** | each order's own `proof_of_spec.json`, independently re-verified by this seat against the live store or committed bytes before every drain (not taken on self-report) |
| **rk-7** | **OPEN on AC5 alone** (AC1-AC4 PASS) | see s.3 |
| **rk-15** | **OPEN on AC4 alone** (AC2/AC3 PASS) | see s.3 |

No cell was left unassigned; no worker's report was drained without an independent re-check on a different
instrument from the one the worker used (a live invoke, a `git show` read of committed bytes, or a fresh S3/DynamoDB
query). Both never-widen co-sign pairs this round required (rk-2's model-block read; the combined rk-6/rk-7 print
and refresh redeploy) are on file with all four halves signed, and the combined redeploy's retroactive
change-management entry is closed on proof (`org/critical_paths/change_management/20260917T0432Z_...md` @`31efe1425e`,
validated independently by `1.0.0_SA_CTO~Z`, msg 23503).

## 2. The moved-criterion map -- read each cell's proof on the order that actually carries it

Five criteria moved off their originating cell's own order during this round, each time because the property they
assert lives on a surface only ONE chain may write (chain B owns `lib/research/api/scoped_amgt.py` and every live
AWS act; chain A owns the portal). **Grade the CELL, not the file it happens to sit in.**

| the cell this criterion PROVES | where it now lives | why it moved | ruling |
|---|---|---|---|
| `AMGT-rk-3` (the dated rankings fallback, reader-side) | `AMGT-rk-7` AC4 | the fallback is adapter code; chain B's | row `AMGT_RESAPP-Z-S125`, `1.0.0_SA_CTO~Z` |
| `AMGT-rk-7` (the page's Refresh call, page-side) | `AMGT-rk-12` AC4 | the page is chain A's; the adapter half stayed on `AMGT-rk-7` AC3 | rows `S124`/`S126` |
| `AMGT-rk-12` (freshness/ledger/lists routes, adapter-side) | `AMGT-rk-6` AC4 | `AMGT-rk-12`'s grant never named the adapter | rows `S124`/`S127` |
| `AMGT-rk-16` (versions/compare routes, adapter-side) | `AMGT-rk-6` AC5 | naming the adapter on `AMGT-rk-16` made chain A a second writer of chain B's surface | rows `S124`/`S127` |
| `AMGT-rk-15` (the thesis driver chart, adapter-side) | `AMGT-rk-7` AC5 | the chart is computed in the adapter; chain B's | rows `S124`/`S127` |

**All five moved criteria are PROVEN except the last.** `AMGT-rk-3`, `AMGT-rk-7`'s page half, `AMGT-rk-12`'s and
`AMGT-rk-16`'s adapter halves are all confirmed live on the deployed adapter as of the combined redeploy
(2026-09-17T03:27:57Z), independently re-verified by this seat and by `1.0.0_SA_CTO~Z` (row `Z-S143`). Only
`AMGT-rk-15`'s adapter half -- carried as `AMGT-rk-7` AC5 -- fails, and it is the subject of s.3.

## 3. THE ONE FINDING BEHIND BOTH OPEN ITEMS -- read `AMGT-rk-7` AC5 and `AMGT-rk-15` AC4 as a SINGLE disposition

**These are not two defects. They are the SAME served property, asserted twice, from two different cells, and both
fail for the identical reason.** Both criteria invoke the deployed adapter's
`GET /api/scoped/amgt/security/BA_US_Equity/thesis` and read `thesis_driver_chart.points_count`. Both read `0`.

**Root cause, verified against the deployed source (`lib/research/api/scoped_amgt.py:1953-2013`,
`thesis_driver_chart()`), not inferred:** the function's own docstring states its design in full --

> *"THE MATCH IS EXACT OR IT IS NOT MADE. ... the only mechanical join to the block is equality: the driver's
> series, case-folded and trimmed, equal to a fiscal figure's `mnemonic` or to its `basis.definition`. A keyword or
> fuzzy match would be this route choosing which numbers illustrate a sentence it did not write."*

The function **never reads `thesis_driver.points` or `.absent_reason` at all** -- the exact fields `AMGT-rk-15`'s
own AC3 required the filings analyzer to add this round. It only serves a number when the driver's PROSE series
name happens to equal one of the model block's ~19 Bloomberg fiscal mnemonics by exact string match. `BA_US_Equity`'s
driver ("BCA commercial aircraft deliveries, with 737 monthly production rate") is an operational metric, not a
generic fiscal line item, and will not match by design.

**This is a DELIBERATE anti-hallucination safeguard from an earlier round, and it cites THIS SAME CELL'S OWN
ORIGINATING ROW as its reason:** the docstring's closing line reads *"the chart says so rather than doing it (row
`AMGT_RESAPP-Z-W18-S12`)"* -- `W18-S12` is the exact row that raised `FWD-18` and became `AMGT-rk-15` this round.
**The function was already refusing to parse numbers out of filing prose, for the reason `AMGT-rk-15` exists, before
`AMGT-rk-15` was cut.** Round-12's own decomposition (ADDENDUM 4 s.2) ruled that the filings analyzer should emit
numeric points specifically so this chart could draw them -- a ruling that conflicts with a standing, documented,
deliberate safety rule on the exact same surface.

**This is a genuine SPEC-VS-SPEC conflict, not a producer gap that time or a re-run resolves.** `AMGT-rk-15`'s own
producer-side work (AC3) is done and correct; the `BA_US_Equity` pilot re-run it was authorized to make (Andrew,
2026-09-16, "Yes on all four") has landed (USD 0.66, one-time) and changed nothing on the served chart, because the
chart was never going to read it. **No further re-run, no further amendment within either order's grant, and no
additional chain-A or chain-B work under THIS round's decomposition can close it.** Closing it requires one of:

1. relaxing the anti-hallucination rule for this one chart, under new, stated safeguards -- a PRODUCT decision; or
2. accepting that `FWD-18`'s promise is met only for a driver whose name happens to match a Bloomberg fiscal
   mnemonic, and re-scoping the ACCEPT text accordingly -- an ENDPOINT decision; or
3. adding a SECOND, bounded join (e.g. the filing's own numeric points, carried with explicit provenance and a
   visible "from the filing, not the model block" label) as a new outcome, never a change to the existing exact
   join -- a new cell for a later round.

**None of these three is this seat's to choose.** `AMGT-rk-7` and `AMGT-rk-15` both stay OPEN on exactly this one
criterion each; every other criterion on both orders is PASS and independently verified. The evidentiary row is
`AMGT_RESAPP-Z-W23-S5` (ARMED, `disarm_owner` named as chain B / the `AMGT-rk-7` AC5 owner), filed by
`0.9.0_WK_AMGT_RESAPP~23` and corroborated by this seat against the deployed source directly.

## 4. Two narrower findings, already root-caused, carried separately (not part of s.3)

- **Row `AMGT_RESAPP-Z-S141`: the print route 500s for the two keyed names containing a slash**
  (`BP/_LN_Equity`, `NG/_LN_Equity`) -- the security key is written into a file path
  (`/tmp/pack_NG/_LN_Equity.pdf`), so the render fails `FileNotFoundError`. 31 of 33 keyed names serve a valid PDF.
  Not a regression (print was 500 for every name before this round's deploy); `1.0.0_SA_CTO~Z` has already ruled
  (msg 23503) that `AMGT-rk-6`'s completed flip stands as correct against its own criteria, and carries this to
  `ROUND_ANALYSIS.round12` as a recut item.
- **Row `AMGT_RESAPP-Z-S144`: the dated rankings fallback (`AMGT-rk-7` AC4, PASSING) serves 2026-09-10, not the
  fresher 2026-09-15 generation `AMGT-rk-17` landed this round.** Root-caused: `price_axis_pull.py` never writes
  the `_CURRENT`/`generation_id` pointer the reader's completeness contract requires (zero occurrences of either
  literal in that producer), so its real, complete 2026-09-15 rows (32 tickers, verified) are structurally
  invisible to any pointer-based reader. `AMGT-rk-7` AC4 passes honestly by its own written logic and by
  `1.0.0_SA_CTO~Z`'s independent read (row `Z-S143`: *"today serves 2026-09-10 dated true ... Inside the on-or-before
  bound"*) -- this is a producer/reader CONTRACT gap, not a criterion defect, and needs a change to `price_axis_pull.py`
  or to the reader's completeness definition, outside every order's grant this round.

## 5. The coverage ceiling, current

`crosswalk/v1/2026-09-15.json`: **89 records, 33 carrying a resolved `security_key`, 56 without one.** `AMGT-rk-17`'s
model-block pull and `AMGT-rk-18`'s filings/drafting batch both ran to the FULL 33-name ceiling this round (33 of 33
model blocks landed; 12 of 33 filings/drafting fetchable, the other 21 correctly unfetchable non-US listings each
carrying a named no-CIK reason). **The ceiling has moved from the Bloomberg pull to IDENTITY**: the 56 unkeyed
records have no security identifier at all, and no cell of this round resolves that -- it is an identity-layer gap,
carried forward, not a Bloomberg-budget question anymore.

## 6. The page's existence, resolved this round

`4.0.0_SA_CRO~Z`'s item-5 finding (the Security Analysis page existed only on one disk, on an unpushed branch) is
**CLOSED**: `0.0.0_AB_MSTR~Z` fast-forwarded and pushed the page to `origin/DEV` under Card 3 (Andrew-direct
2026-09-16 ~19:2xZ), confirmed by both the CRO and MSTR independently on git refs (`origin/DEV` = the page branch
tip, a pure fast-forward, 0 conflicts). The page's own CI run is RED at ESLint, but on 5 PRE-EXISTING errors unrelated
to this project (`SentimentGauge.tsx`, two `InvestorReporting` tests, `ExportButton.tsx`); the Security Analysis
files themselves add 0 errors, 11 warnings.

## 7. What this seat asks of L9/L10

Grade `AMGT-rk-7` and `AMGT-rk-15` as **ONE disposition for the shared root cause** (s.3), not two independent
partial-credit items -- the same served property, the same failure, the same fix path, on two different orders only
because the round's own single-writer chain rule put the two halves of `FWD-18` on two different cells. Carry s.3's
three closing options, s.4's two narrower items and s.5's identity ceiling into `ROUND_ANALYSIS.round12` as
adjudicator-level questions; none of the six is this seat's to resolve inside round 12's existing decomposition.

Push state: LOCAL on SITEZ.
