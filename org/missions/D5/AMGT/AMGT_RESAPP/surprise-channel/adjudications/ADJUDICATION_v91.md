# AMGT_RESAPP ROUND 76 -- L8 + L9 -- FWD-18 REALIZED on ASML NA (board 21 of 30); FWD-7 NOT REALIZED (95 of 95 flagged, nothing to single out); FWD-1 NOT REALIZED (segments on 12 of 95, and the name this seat picks shows a reason); L10 precondition MET

**Seat:** `3.0.0_SA_CVO~Z` - **Written:** 2026-10-06 ~22:2xZ (drafted under MSTR~Z's HOLD, msg 30373; committed on RELEASE)
**Input:** `2.0.0_SA_COO~Z` `round76/DRAIN_END_PACKET.md` @`a74117fb6a` (64 lines, read to EOF), msg 30334. 6 of 6 orders are terminal. The deployed function is `OVpDhfwD`, and the walk is on portal DEV `6b4e89a8`. The round ran on PRD v0.40; v0.41 binds round 77.

## This seat names the companies (v0.40)

This seat's own read was `read_thesis_bundle` over the 242 keys of `read_coverage_freshness` (0 errors):

| read | result |
|---|---|
| a driver chart is SERVED from the filing | **2 names: BA US and ASML NA.** 240 read ABSENT |
| the segment breakdown has rows | **12 names.** 230 read a reason |
| of those 12 | ASML NA's 5 rows are share-capital items (authorized capital, treasury shares, holders). PBR US's 8 rows carry the one label "Other" |

- **FWD-18: this seat names ASML NA.** The names that serve a chart are two, and the walk covered both. ASML NA is the weaker of the two.
- **FWD-1: this seat names AMD US,** a covered name outside the 12, as v90 said it would.

Both were walked on DEV in this round (`WALK_ROUND76.md`; captures 012-021).

## The walk, per outcome (az-6 AC3)

| FWD | read | CVO grade |
|---|---|---|
| 18 (v0.40) | **ASML NA, capture 017, read by this seat.** Pressing "2023: 393421721 -- show the filing passage" opens the passage in place. It shows the row "Issued ordinary shares with nominal value of EUR0.09", the three values, and the cite "From the filing: TABLE / period 2023". This is a filing-derived figure clicked through to its passage on the deployed page | **REALIZED** on its DONE WHEN |
| 7 (v0.39) | **Capture 001, read by this seat.** The page is on DEV and lists 95 companies with a Last refreshed date. Every row reads Last refreshed 2026-10-06. Every row is flagged stale: 92 read "Seeking Alpha has never been read" and 3 read "last read 2026-09-11". The header says "95 of 95 ... stale" | **NOT REALIZED**: "finds a stale one" has nothing to find against |
| 1 (v0.40) | **AMD US, capture 013.** The description and the Model tab open. The segment panel reads "No filing analysis is stored for this name yet, so no segment breakdown is shown" | **NOT REALIZED**: the segment breakdown is not on screen for the named company |
| 16, 12 | az-2 serves `top_band` and `input_provenance` on 95 of 95 (c62 and c63 YES on the deployed function). The page work is not on DEV | not graded this round |

### FWD-18 -- findings beside the grade (the ACCEPT is still far off)

- **Coverage is 2 of 95.** The ACCEPT's "one chart, chosen for that company" exists for BA and ASML only.
- **ASML's chart is the wrong driver.** It plots issued ordinary shares. ASML does not live or die on that. BA's chart (BCA deliveries) is the right kind.
- **The passage renders three times** after one press, and each copy cites "period 2023".
- **The y-axis ticks read "00000000"** (clipped).
- **BA's passage is flat table text** with no column labels for its five numbers.

### FWD-7 -- why it is not realized

- **The flag does not discriminate.** A flag set on 95 of 95 rows cannot single one out. The round shows no row that reads not-stale, so the page's ability to tell the two apart has never been exercised.
- **The date column contradicts the flag.** "Last refreshed" shows the newest input (2026-10-06 on every row), while the flag keys on the oldest (Seeking Alpha). A reader sees "refreshed today" and "stale" on the same row.
- **92 rows are flagged for a source that was never collected for them.** If Seeking Alpha is not an input the firm collects for a name, "never read" is not staleness. Whether to exclude never-collected sources from the flag or to collect them is the CTO's call. The same holds for the all-"Not collected" Web search column, which the CTO has already asked to hide.
- **First paint was 4,116 ms** on the first visit (2,665 ms for the read; round 75 read 694 ms). The packet calls the gap unexplained.
- **What closes it:** one visit in which at least one row reads not-stale beside one that reads stale, and the stale one is found from the page.

### FWD-1 -- why it is not realized

- **83 of 95 covered names serve a reason, not a breakdown.** AMD is one of them.
- **Among the 12, two are not business segments:** ASML (share capital) and PBR (every row "Other").
- **On BA** the label repeats on each of 11 interleaved rows, where one heading per segment would read better.
- **The remedy is already authorized:** the Bloomberg segment pull for 83 names (Andrew's word @`b5f90bbf8d`, ruling 1). This seat re-reads AMD after that pull.

## Rows

- `Z-W266-S1`, `-S2`, `-S3` (the walk's three, INERT): GRADUATED here; REMEDIATION_v22 is OPEN on each.
- `Z-S360`, `Z-S361`, `Z-W262-S1/S2`, `Z-W263-S1`, `Z-W265-S1..S3`: for the analysis, as the packet states them.
- The 109 TRIAGE citing rows (`Z-W264-S1..S109`) and the two ruling tables (CTO @`4a89bef967`, COO @`fb9ca91ad5`; msgs 30363 and 30367): this seat's citing rows from those tables follow in their own commit after RELEASE.

## L10 PRECONDITION

Every order is terminal, and az-5's NEVER-2 entry is closed. `comp-surprise --armed --project AMGT_RESAPP` read **17** ARMED at 22:1xZ, the same 17 as round 75. All are older than this round and are held by their owners. This round filed no ARMED or BLOCKING row. **MET.**

```json
[
 {
  "id": "AMGT_RESAPP-Z-C-S466",
  "project": "AMGT_RESAPP",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-06T22:20:00Z",
  "one_line": "Round 76 L9 on deployed OVpDhfwD and portal DEV 6b4e89a8 (board 21 of 30): FWD-18 REALIZED on ASML NA, named by this seat -- a filing figure clicks through to its passage and cite on the deployed page (the chart is served on 2 of 95 names, ASML's plots share count, the passage renders three times); FWD-7 NOT REALIZED -- 95 of 95 rows are flagged stale with one Last refreshed date, so nothing can be singled out and no not-stale row has ever been shown; FWD-1 NOT REALIZED -- AMD US, named by this seat, shows a reason in place of a segment breakdown (rows on 12 of 95; ASML's are share-capital items, PBR's all read Other).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "read_thesis_bundle over the 242 security keys of read_coverage_freshness (0 errors): thesis_driver_chart SERVED/filing 2 (BA_US_Equity, ASML_NA_Equity), ABSENT 240; segment_breakdown rows on 12, reason on 230; ASML_NA labels Authorized share capital / Board holdings / Major holders / Other / Treasury shares; PBR_US 8 rows labelled Other",
    "deliverables/0.9.0_WK_AMGT_RESAPP~266/captures/017-fwd18-ASML-passage-open.png: '2023: 393421721 -- SHOW THE FILING PASSAGE' open, 'Issued ordinary shares with nominal value of EUR0.09', 393,421,721 / 393,283,720 / 385,417,665, 'From the filing: TABLE / period 2023', the block repeated under each of the three links; y-axis ticks '00000000'",
    "captures/001-fwd7-freshness-first.png: '95 of 95 covered companies have an input that is stale'; Last refreshed 2026-10-06 on every row; Stale 'Seeking Alpha has never been read' on 92, 'Seeking Alpha last read 2026-09-11' on 3 (BABA, BA, COST)",
    "WALK_ROUND76.md: AMD segment panel 'No filing analysis is stored for this name yet, so no segment breakdown is shown'; first paint 4,116 ms, /freshness read 2,665 ms",
    "round76/DRAIN_END_PACKET.md @a74117fb6a (64 lines)"
   ]
  },
  "disposition": "GRADUATED",
  "adjudicates": [
   "AMGT_RESAPP-Z-W266-S1",
   "AMGT_RESAPP-Z-W266-S2",
   "AMGT_RESAPP-Z-W266-S3"
  ],
  "spec_asserts": "FWD-18: a filing-derived figure clicks through to its passage on a company the grading seat names; FWD-7: a seat finds a stale company in the one place; FWD-1: a named covered company shows model numbers, description and segment breakdown.",
  "world_is": "The click-through works on the deployed page for the 2 names that serve a chart. The freshness page flags every company. 83 of 95 covered names serve no segment breakdown.",
  "notes": "FOR THE ROUND-76 ANALYSIS: (1) FWD-7 -- decide whether a source never collected for a name flags it stale, and make Last refreshed and the flag read the same input; the closing act is a visit with a not-stale row beside a stale one; the 4.1 s first paint and the 2,665 ms read need a cause. (2) FWD-1 -- this seat re-reads AMD US after the authorized Bloomberg segment pull; ASML's and PBR's rows are not business segments. (3) FWD-18 is REALIZED on its DONE WHEN, and its ACCEPT is not near: 2 of 95 charts, ASML's driver is a share count, the passage triplicates, the axis clips, BA's passage has no column labels."
 }
]
```

-- 3.0.0_SA_CVO~Z
