# AMGT_RESAPP -- ROUND 76 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-07 ~00:3xZ

**Input:** CVO slug msg 30463, `surprise-channel/adjudications/ADJUDICATION_v91.md` @3130be0c0c (+ REMEDIATION_v22) and
`ADJUDICATION_v92.md` @b121937bcc (the citing record for the 53 ruled rows). The L10 precondition is MET. The packet is
`deliverables/2.0.0_SA_COO~Z/round76/DRAIN_END_PACKET.md` @a74117fb6a. The round ran on PRD v0.40; v0.41 binds round 77.

## 1. WHAT THE ROUND DELIVERED

- **The redeploy** (az-5): `opal-amgt-scoped-api` D29LJCXh -> OVpDhfwD, under the pair (CTO half @9c5a2a4b61). r75 and r74's
  checks still read YES.
- **/overlay** (az-2) serves `top_band` and `input_provenance` on 95 of 95, with 0 entries disagreeing with /freshness.
- **The triage** (az-3): 109 of 109 OPEN remediation rows carry a citing row, and all 53 BLOCKED are ruled (CTO @4a89bef967 +
  @3bad4be9e0; COO @fb9ca91ad5). ARMED went from 17 to 12.
- **The cold cut** (az-4): the generation read went from 1,964 ms to 548-675 ms locally.
- **The walk on DEV as deployed** (az-6), plus the /freshness page on DEV and PROD.

**Round 76 is CLOSED.**

## 2. THE BOARD (CVO L9): REALIZED 21 of 30

Newly REALIZED: **FWD-18** on its DONE WHEN (ASML NA: a filing-derived figure clicked through to its passage on the deployed page).
NOT REALIZED this round: **FWD-7** (95 of 95 flagged, nothing to single out) and **FWD-1** (AMD US shows a reason, not a
breakdown). Not graded: FWD-16 and FWD-12 (the page work is not on DEV).

## 3. RULINGS

| # | item | ruling | why |
|---|---|---|---|
| 1 | **FWD-7: does a source never collected for a name flag it stale?** | **No.** The stale flag keys only on inputs the firm has collected for that name at least once. A never-collected input reads "Not collected" and never "stale". The page's date column shows the date the flag keys on (the OLDEST collected input), so the date and the flag cannot disagree on a row. The all-"Not collected" Web search column is hidden (already asked @7c328eb0df), and its header line reads at 4.5:1 or better (Z-W262-S2). | "Never read" is not staleness when the firm does not collect that source for the name. A flag on 95 of 95 rows tells a reader nothing. |
| 2 | **What closes FWD-7** | One visit on DEV in which at least one row reads not-stale beside one that reads stale, and the stale one is found from the page. With Seeking Alpha now collecting through the tab (HARVST round 50), the stale population will be real, not empty. If no row is stale on the day, a planted old read on ONE name is the exercise, and it is stated as planted. | The CVO's own closing condition, adopted. |
| 3 | **The /freshness read: 2,665 ms for a 1.07 MB body** (round 75: 694 ms) | **A round-77 measurement cell before any cut.** Attribute the body's bytes by field over the 242 keys the route returns, against the 95 rows the page shows. Then serve the page only the fields and rows it renders. The cold route itself answers in 660-1,047 ms, so the gap is body size, to be shown and not assumed. | The page shows 95 rows and the read returns 242 keys. The likely cause is named, and the cell proves or kills it. |
| 4 | **Cold chatter stays at 2,580-3,137 ms** (Z-S360) | **A phase-COVERAGE read, not another latency run.** Every millisecond of the cold Duration is attributed to a named phase or to "outside every phase", with the sum equal to the Duration. az-4's in-phase saving of about 1.8 s was offset by growth outside the phases, and the label set changed. Provisioned concurrency goes to Andrew only after that read shows the free cuts exhausted, with the measured residual and the monthly cost on the card. | A spend ask on an unexplained number is not a decision he can make. |
| 5 | **FWD-16's news day** (Z-W263-S1: 3 items across 95 names on the "latest trading day") | The top band shows the name's NEWEST day with news inside the last 30 days, dated. A name with none says "No news in the last 30 days". It is never an empty band and never yesterday's absence shown as today's fact. | The last settled day is the wrong window for a per-name band. Most names have no item on any given day. |
| 6 | **FWD-18's findings beside the grade** | One cell: the passage renders ONCE per press (it renders three times today); the y-axis ticks are readable (they read "00000000"); a table passage carries its column labels (BA's five numbers have none). | Defects on a realized outcome. The ACCEPT is still far off, and these are the visible ones. |
| 7 | **A table that is not a business driver or segment** (ASML: share capital served as both the driver chart and the "segments"; PBR: every row "Other") | **A class refusal at the producer.** A share-capital or equity-structure table, and a table whose rows carry one repeated label, is REFUSED as a driver or a segment breakdown. The name then reads its reason. A wrong chart is worse than an absent one. On BA, one heading per segment replaces the label repeated on 11 rows. | ASML does not live or die on issued share count. The page presenting it as the driver is a false claim made well. |
| 8 | **FWD-1 for the 83 names** | The Bloomberg segment pull (round-75 ADDENDUM 3 item 2, Andrew's word @b5f90bbf8d), under its pair. The CVO re-reads AMD US after it. Ruling 7's refusal applies to its output too. | Already authorized. This is its place in the round. |
| 9 | Z-S361 (the burst width) | As the COO ruled: the check's width is repaired at the round-77 cut. | The issuer measured it. |

## 4. ENRICHMENT LIST (round 77, ONE issuance by `2.0.0_SA_COO~Z`; waves by its dependency chains)

1. **FWD-7:** rulings 1-2 (the flag's key, the date column, the hidden column, the contrast). The exercise is ruling 2.
2. **The /freshness body attribution, then the trim** (ruling 3).
3. **The chatter phase-coverage read** (ruling 4).
4. **FWD-16:** the news-day rule (ruling 5); the top band's page work rides DSGN round 45.
5. **FWD-18 repairs** (ruling 6), and **the non-driver / non-segment refusal** (ruling 7).
6. **The three Bloomberg research pulls.** Each is a SERVED act under its own pair, after the 7:00 AM ET vehicle, one at a
   time: segments for 83 (ruling 8), officers for 84 (Z-W227-S1), FWD-2's uncovered name.
7. **PRD v0.41:** remove the `/refresh` no-op and its control. FWD-12 is graded on the provenance half once the page work is on
   DEV.
8. **FWD-14:** the owner line and the out-of-date statement on /freshness (owner: Andrew, both lists). No alert is built.
9. **FWD-20:** the trailing-trend FCF v1 (round-75 ADDENDUM 1).
10. **The remediation cells** (CTO @4a89bef967 + @3bad4be9e0): the identity resolving cell; the comparable / Peers V mapping;
    the CSC present-column fields; the export chart line; the name-search route; the ONE PAGER precedence; the passage
    section coverage; the translated text. Plus the COO's own repair cell (@fb9ca91ad5).

## 5. ACTS FOR ANDREW (cited)

- **Three carried calls** (`CTO_ADJUDICATION_REMEDIATION_ROWS_ROUND76.md` section G): a social source for FWD-11; Peers V on a
  short peer set; the Bloomberg credential rotation.
- **The analyst and PM walker accounts** (entitlements).
- **Provisioned concurrency:** not yet. It comes with ruling 4's read.
