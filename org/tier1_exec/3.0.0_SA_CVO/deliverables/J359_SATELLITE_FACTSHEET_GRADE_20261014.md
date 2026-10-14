# Remote job J359 -- grade of the 2.0.0_SA_COO~J1 report (satellite factsheet)

**archetype:** VALIDATE
**Grader:** 3.0.0_SA_CVO (dell1), 2026-10-14 ~16:2xZ. Asked by 0.0.0_AB_MSTR~DELL1 msg 5638.
**Report graded:** 2.0.0_SA_COO~J1 msg 5637, `org/mcp/inbox/0.0.0_AB_MSTR/~DELL1/read/20261014T155312Z_2.0.0_SA_COO_J1_J359_built__satellite_factsheet_on_cand_.md`.
**Artifact:** portal `cand/dell1/satellite-factsheet` @eb80c92f (not on DEV).
**The ask (brief, sha256 dc418997...8260, as recorded in `.tools/.remote-job.json`):** "Build a factsheet-style template to host each satellite
model, populated from the currently served data and shown in the popups." CHECK: "CW/Yang can open each satellite model's popup on
'Positioning' and see the factsheet filled in from the currently served data." Design frame: the CRO review
`org/tier1_exec/4.0.0_SA_CRO/deliverables/J359_SATELLITE_FACTSHEET_DESIGN_REVIEW_20261014.md` (findings A-E).

## Verdict: PASS

The build does what the ask and the CRO's frame require, on this seat's own reads. The CHECK itself is a post-landing read by the
requester. Landing is client-facing, so it waits on Andrew's approval under the CLAUDE.md Portal law (fcdfc34843).

## What this seat read, and what each read shows

| # | Read | Result |
|---|---|---|
| 1 | `git diff <merge-base 97c66c93> eb80c92f --stat` | 4 files, all under `src/components/` (SatelliteModal.tsx, satelliteFactsheet.ts, SatelliteFactsheetSections.tsx, satelliteFactsheet.test.ts); +596 / -44. No `fetch`, `apiRequest` or `/api/` line added: no new fetch or route (CRO E). |
| 2 | `bun test src/components/satelliteFactsheet.test.ts` in a detached worktree at eb80c92f | 6 pass, 0 fail, 17 expect() calls. |
| 3 | `bun x tsc --noEmit -p .` (same worktree, portal's node_modules) | rc 0. |
| 4 | `bun x eslint` on the four files | rc 0. |
| 5 | `satelliteFactsheet.ts` read whole | Computes no measure; display aggregation only (weight by class and sub-class); null kept distinct from zero; every measure and every return window carries `coverage` from the producer's `coverage.weight_with_value`; return windows are only those served (1D..1Y); top 10 holdings with served names, yield and fee. Sections the template has and the satellites do not serve (calendar years, risk statistics beyond beta, sectors, market cap, style, fundamentals) are not drawn: CRO option (i). |
| 6 | `SatelliteFactsheetSections.tsx` | Returns under "Trailing Returns of Current Holdings", labelled "Hypothetical: today's holdings at today's weights over each period. Not the satellite's realized ..." -- the satellites' own method, not the PDF's (CRO B). Each figure prints "covers N% of weight", with "Partial:" below 50%, and a note that sums are not scaled up (CRO C). |
| 7 | Live served data, `s3://opal-data-cot/platinum/satellites/{characteristics,holdings,registry}.json` (LastModified 2026-10-14 13:15Z-13:26Z) | The fields the module reads are served: `coverage.weight_with_value` = {fee, yield, duration, beta, returns{1D..1Y}}; `returns` for the same 8 windows; holdings rows {asset_class, sub_asset_class, ticker, weight} (16 rows on the first satellite); `tickers` block of 26. `SatelliteBook.served` is the existing contract in `satelliteSet.ts` (unchanged by this diff). |

## Limits, stated

- **The rendered popup was not read by this seat.** The report says a dist render with the served 2026-10-14 files was read for
  Satellites 15, 50 and 90. No screenshot of it is on disk, so that read is the issuer's. The requester's CHECK after landing is the
  render read that counts.
- **Open for Andrew, as the report names:** (a) the disclosure text. CRO D says it needs an owner; the build carries method notes,
  not a disclosure paragraph. (b) The coverage floor: the build prints partial figures labelled "Partial:" below 50%. It does not
  withhold them. Satellite 90 duration covers 7%.
- Whether Yang and CW confirmed CRO option (i), omitting the unserved sections, is not on record here. The build follows Yang's word
  "no need to generate additional data".

## Cleanup

The worktree used for reads 2-4 was removed. Its node_modules junction was unlinked first, and portal/node_modules was checked intact.

-- 3.0.0_SA_CVO
