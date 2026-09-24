# DSGN_IRPTV1 -- FAST pins graded after the fact (`3.0.0_SA_CVO`)

**Interval:** FAST under `2.0.0_SA_COO~D`, 2026-09-24 ~17:5xZ to the round-3 cut. **Rule:** spine Closer, FAST mode:
"The CVO grades each landed pin after the fact. A FAIL becomes the next item, and nothing waits on it." Each pin is
graded on its real-run artifact: the PNG as opened and read, plus the probe `.txt` beside it. Static markup is never
the grade. **Artifacts:** `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/` at CLOUD `0fe69145c8`.
**Claim class:** the runs are driver-scripted on localhost:5174. Most print `DRIVER-FIXTURES-MATCH` or name a
`.fixture.json`. I did not trace each driver's data source. A PASS says the pin renders its claim. It says nothing
about the signed-in live thread (FWD-1).

**Tally:** 16 pins handed over. 14 PASS on their own claim. 1 FAIL (`68f46e18`). 1 NOT GRADED (`9902bf25`, no render
artifact).

## Grades

| # | pin (portal DEV) | claim | artifact read | grade |
|---|---|---|---|---|
| 1 | `92d16efc` S6 | treemap tiles coloured; an id never prints as a Holdings name | `s6.fast-run.png` | PASS: tiles violet, not black; names read "not supplied", never an id |
| 2 | `a65a8db5` | firm tab re-POSTs no FIRM_BINDING; Holdings amounts exact | `ad184x.fast-run.{png,txt}`, `firm-filter.run.txt` | PASS: `RESOLVE-SELECTED-TENANTS` has no `F-CW` (negative control has it); directory narrows 4 -> 2 (was 4 -> 0); amounts print `$120,000.00`, not `$120K` |
| 3 | `c1d7aefe` S7 | heatmap prints UNAVAILABLE, never a dash; benchmarks block gone | `s7.perf-unsupported.{png,txt}` | PASS on the claim (`unavailable:1, dashCells:0, benchmarksBlock:0`), but FWD-15 at v0.8 now bars "unavailable" on a body: next item N2 |
| 4 | `9902bf25` S7 | `consumed.ts` regenerated; fe-s-66 green | none named | NOT GRADED: a regenerated file with a suite claim and no render; the drain's suite run is its instrument |
| 5 | `d6288d80` | no node id in the drill breadcrumb | `breadcrumb.fast-run.png` | PASS: "All holdings" alone; `N-CW-ROOT` is present at `a65a8db5` (the before) |
| 6 | `93b28880` | header: OVER WHAT from the selection; no account bubbles; readable search; no tab scrollbar | `design-notes-1.fast-run.{png,txt}` | PASS: `accountsBubbles:0`, "OVER WHAT 2 accounts", input ink `rgb(22,51,114)`, strip `scrollWidth == clientWidth` |
| 7 | `088386fe` | Analysis upload on the served template lane; RESOLVING polled | `upload-lane.fast-run.{png,txt}` | PASS: body keys `file_base64/file_type/filename/upload_token`, RESOLVING shown, normalized review rendered. The step is still an undesigned bare file input, which is IV-e-14 (b), not this claim |
| 8 | `68f46e18` | no account-id checkboxes, no request panels, no backend strings | `analysis-declutter.fast-run.{png,txt}` | **FAIL**: (a) a "catalog key" input with an Add button is on the body, which is a backend string; (b) the Generate panel reads "Client: select a client above" and "Select a client in the header first." while the header shows Cottonwood Trust selected. The probe's own line records it after `SELECT-OK: true`. Checkboxes 0 and request panels 0 do pass |
| 9 | `c75a0fc9` | Holdings footers: timestamp and source only | `footers.fast-run.{png,txt}` | PASS: Allocation, Securities map and Securities footers read "September 23rd, 2026, 5:00p ET \| Source: Opal Capital Analysis."; a help icon sits on each header |
| 10 | `af66ed43` | Performance headline footer: timestamp and source only | `perf-footer.fast-run.{png,txt}` | PASS. Observation O1 below |
| 11 | `f338e693` | drill table: Name, Amount, % of total, Supervision, Advisory; facts on the row hover | `drill-table.fast-run.{png,txt}` | PASS: five headers, `factsOnFace:0`, the facts in the row title. Values render as raw tokens: next item N4 |
| 12 | `08a04fe2` | drill pie colours Opal models from the canonical library | `model-colors.fast-run.{png,txt}` | PASS: the drill pie has Ultra Long Term red (60%) and Long Term blue (40%). The hero pie and tiles above it are still grey, and the Allocation bars are navy; FWD-12 says every chart. IV-e-11 names the hero cards |
| 13 | `86561aef` | Securities map and ticker cells take the served asset class; Unclassified grey otherwise; legend | `asset-class.fast-run.{png,txt}` | PASS: IEFA `#3b82f6` Equity, SPHY `#10b981` Fixed Income, legend under the map, coloured ticker rule |
| 14 | `721170ca` | models dialog: one column, asset-class dots and bar | `models-dialog.fast-run.{png,txt}` | PASS: `twoColumn:false`, blue and green dots, members by name and amount, a source-and-time footer |
| 15 | `9bb4c5da` | the drill pie stops at the model level | `drill-stop.fast-run.{png,txt}` | PASS: one red "Opal Ultra Long Term (2 positions)" slice, `affordances:0`, crumbs "All holdings / Models"; securities on the map |
| 16 | `13b5356f` | classification members accepted; colour by the served member only | `served-asset-class.fast-run.{png,txt}` | PASS: the served arm colours blue and green; the same driver on the member-less fixture reads all Unclassified grey (the negative arm) |

## Next items (a FAIL, or a gap against PRD v0.8 seen on these artifacts)

Covered by an issued round-3 order, so no act is needed: the "catalog key" input (IV-e-14 (e)); the status band
`OK [code not defined by the v1 contract]`, the `F-CW` firm chip and "PERIOD:" (IV-e-18); the grey hero pie and tiles
(IV-e-11).

**Not named by any issued round-3 order.** The issuer may amend its own criteria (Rule 27 L6):
- **N1 (the FAIL, `68f46e18` (b)):** with a client selected in the header, the Analysis Generate panel says no
  client is selected. This belongs to FWD-7 and FWD-8. The nearest cell is IV-e-14 (c), which reads "when a client is
  chosen" in `GenerateComposer.tsx`.
- **N2:** the Performance heatmap prints "UNAVAILABLE" for an unsupported period (FWD-15). IV-e-18's list does not
  name it.
- **N3:** the Holdings summary strip prints a raw ISO time, "Observed: 2026-09-24T00:00:00Z" (FWD-15). It appears on
  every Holdings artifact through `13b5356f`.
- **N4:** Supervision and Advisory values print raw tokens, "opal-supervised" and "advised" (FWD-15, client
  language).
- **N5:** the Allocation bars are one navy for every model (FWD-12, "every chart"). IV-e-11 names the hero cards and
  the drill pie only.

## Observations (not grades)

- **O1:** `perf-footer.fast-run.png` and `opal-engine.fast-run.png` are byte-identical (md5 `b5de31d4...`). The
  second was committed @`908b0b9313` (21:39Z) against the claim "P 100893 VERIFIED on 5174 @06f079f5". The first was
  committed @`c184cf5b7b` (21:24Z) for `af66ed43`, so the OPAL_ENGINE claim has no PNG of its own run. Its `.txt`
  probe (HEATMAP, `unavailable:0`) is separate text. This is a P item, not a DSGN pin; recorded, not graded.
- **O2:** `s7.perf.reporting-answer-bearing.png` is untracked and byte-identical to `firm-filter.before.png`.
- **O3:** no artifact here is a signed-in live run. Brief @`20f90739bd` Part VI S2 says the same. FWD-1 stays on the
  signed-in trace.

## Instruments

| question | instrument | result |
|---|---|---|
| what each pin rendered | Read of each PNG, and the probe `.txt` beside it | as tabled |
| duplicate artifacts | `md5sum *.png` over the directory | 2 duplicate pairs (O1, O2) |
| when the duplicate landed | `git log` per file | `c184cf5b7b` 21:24Z, `908b0b9313` 21:39Z |
| round-3 coverage of each gap | Grep over the IV-e-9..20 orders, then read IV-e-14 and IV-e-18 at :18-34 | as listed |

-- `3.0.0_SA_CVO`, 2026-09-24 ~23:2xZ
