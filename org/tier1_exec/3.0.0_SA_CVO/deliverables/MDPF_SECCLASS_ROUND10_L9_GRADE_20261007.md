# MDPF_SECCLASS round 10 -- L9 judgment grades (3.0.0_SA_CVO, dell1)

**Packet:** `org/missions/D8/MDPF/MDPF_SECCLASS/deliverables/2.0.0_SA_COO~M1/DRAIN_END_R10_20261007.md` @d9ce041409 (msg 308).
**Round branch:** `coo-m1-secclass-r8` @4a5b15ee4f. Graded 2026-10-07 ~14:3xZ.

## SC10-e58-AC2 -- PASS

Criterion: "the named failing hop is the true first break of the journey, and no hop is graded PASS on a read that could not see it."

Trace: blob f624ffb58a (`BD_PAGES_THREAD_TRACE_20261007.json`, 0.9.0_WK_MDPF_SECCLASS~41, base 3a11e67c20).

| hop (data order) | trace grade, claim | this seat's read | holds |
|---|---|---|---|
| canonical_source | PASS, measured | get-item rows GLD/PHYS commodities/Metals, VXX structured/Hedge (worker); matches what this seat read for C-S13 from the served mix | yes |
| classifier_lib | PASS, inferred | the worker diffed deployed `s3://opal-data-bd/code/gold/lib/etf_classifier.py` against the repo (equal, 16,901 bytes), so the code read sees the running bytes; the downstream measured hops corroborate it | yes |
| gold_producer | PASS, measured | corroborated by the measured platinum key | yes |
| platinum_key | PASS, measured | this seat read the same object at 10:0xZ (C-S13): composition top_holdings carry asset_class_canonical and sub_asset_class_canonical | yes |
| api | PASS, inferred | **this seat's own read:** `aws lambda get-function opal-partners-data` (LastModified 2026-06-03, CodeSha256 jbQNErp0...) code package downloaded from AWS; `lambda_function.py` 81,165 bytes and `pseudonymizer.py` 5,841 bytes are equal to the repo (diff 0 lines; control diff of two different files = 2,057 lines). The code read therefore sees the deployed path: serve_s3_json pass-through, and a pseudonymizer that touches no class field | yes |
| page | FAIL, inferred (code path) | composition.ts:204-213 drops asset_class_canonical and sub_asset_class_canonical; ConcentrationItem has no sub-class field. A FAIL on a code path is sound: the code cannot render a field it never maps | yes |
| silver_dim | FAIL, measured | off the page chain (B_01 reads its cusip column only); not the first break of this journey | yes |

Judgment: FWD-1 ACCEPT needs VXX to read as Hedge (TO-SC-e59 AC2 text: "VXX as a hedge"), and the page renders the class slice only. So
the page is the true first break, and the grading note's alternative (class-only as sufficient) does not apply. Every PASS rests on a read that sees the
running bytes or the served object. **PASS.**

Caveat carried to round 11 (not a hop break): for client z08327149, VXX is absent from the served concentration top-10 and appears only in
`mix.structured`. A fixed page shows VXX per security only if the served list carries it (W46-S1 item 3).

## SC10-e59-AC2 -- NOT YET GRADABLE

Criterion: the Advisor Intelligence page, read on the laptop after review, shows GLD and PHYS as commodities (Metals) and VXX as a hedge
for a real BD client. The fix is on the held portal candidate `wk-MDPF_SECCLASS-46-portal` @c0ec00e6, waiting for the laptop CTO review
and then DEV. There is no served page to read, so the criterion stays open. It is graded on the first read after the DEV landing.

-- 3.0.0_SA_CVO

## SC10-e59-AC2 -- PRE-READ after the DEV landing (2026-10-07 ~15:4xZ); still NOT GRADED

e59 is on portal DEV @fc18e50bc4 (Andrew's word ~15:1xZ; 0.0.0_AB_MSTR~DELL1 msg 371). This seat's reads from dell1:

- **Code at DEV fc18e50b:** `lib/composition.ts:185-186, 245-249` carries `asset_class_canonical` and `sub_asset_class_canonical`
  from the served item; `panels/ConsolidatedOverviewPanel.tsx:470-472` renders `item.sub_asset_class_canonical` beside the label.
- **Served bytes:** all 3,349 `s3://opal-data-bd/platinum/clients/*/summary.json` read (local scratch, not kept). `concentration.items`:
  GLD commodities/Metals on 2 clients (z08373330, z08398063); PHYS commodities/Metals on 1 (z0893406); VXX structured/Hedge on 12
  (e.g. z08123628, data_as_of 2026-10-05); 1 VXX item without canonical fields (a stale client). No single client lists VXX together
  with GLD or PHYS, so the read needs two clients.
- **Not done:** a rendered page. The criterion says "read on the laptop", and the walker account's arm writes `opal-users-v2` and SSM
  from the laptop's profile. This seat did not render the page from dell1 or move the shared portal checkout (8ddfe409, behind DEV).

On code and bytes the page should pass. The grade waits for a render: routed to 1.0.0_SA_CTO~DELL1 to name the reading seat.

## SC10-e59-AC2 -- PASS (firm-level view, per 1.0.0_SA_CTO~DELL1 msg 433), 2026-10-07 ~17:0xZ

**Evidence form ruled (msg 433):** page words, URL, time and each screenshot's sha256; images stay in `tmp/`.
**Render:** `org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_SC10_E59_FIRM_VIEW_RENDER_20261007.md` @616a6f85e8 (laptop
3.0.0_SA_CVO). On `http://localhost:5174/advisor-intelligence` built from portal DEV `fc18e50b` (0 changed files), Books tab, FIRM
OVERVIEW, 49 Financial, as of 2026-10-05:
- Commodities pressed (16:50:25Z): "GLD Metals 21.7%", "PHYS Metals 4.1%"; sha256 `57e8374a...e876ac`.
- Structured pressed (16:50:40Z): "VXX Hedge 82.1%"; sha256 `97208c09...652308`.

**Do the changed lines draw the word? Read by this seat in portal git:** the panel titled "Top <class> Holdings" is
`ConsolidatedOverviewPanel.tsx:294` (fc18e50b), mounted by `CanonicalBookView.tsx`. At `ba391aff` (DEV before e59) that panel has no
`sub_asset_class_canonical` reference (the only `subClass` hits there are CSS class names, `:320`). At `fc18e50b`, `:470-472` render
`item.sub_asset_class_canonical` beside the label (hookup fc18e50b, fed by 26987884's `composition.ts:245-249`). The page and the served
bytes both read GLD/PHYS commodities/Metals and VXX structured/Hedge, and they agree with my pre-read.

**Grade: PASS** on the firm view.

## FWD-1 -- NOT GRADED REALIZED

FWD-1 ACCEPT is an advisor reading a client's holdings. No client page or advisor Book view was reached, because the Book view's
platinum-summary call answers 403 for the walker (row MDPF_SECCLASS-S60 @bcd60149e4). The firm view shares the module and the served
classes, so the remaining unknown is access, not classification. FWD-1 grades REALIZED when S60 closes on a real advisor's 200 read
of a client page that shows the sub-class.

## Correction (2026-10-08 ~03:3xZ)

The "row MDPF_SECCLASS-S60 @bcd60149e4" above was never merged: its id collided with 2.0.0_SA_COO~M1's S60 (COT multi_asset). The
walker 403 is carried by M1's row S61, explained @f77d1c8d7e (local vite proxy past CloudFront), fixed @91a899001f (walker 200 on
the advisor and three client summaries), and dismissed in ADJUDICATION_v10. FWD-1 still grades on a rendered client page read.
