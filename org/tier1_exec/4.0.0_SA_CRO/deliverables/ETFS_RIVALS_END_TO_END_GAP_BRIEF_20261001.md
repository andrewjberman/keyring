# ETFS_RIVALS (/rivalfunds): end-to-end trace brief, ingestion to the MCP page

Prepared by `4.0.0_SA_CRO~RV` on 2026-10-01, read window 17:30Z to 18:15Z. This is a read-only assessment with proposed
closure requirements. I made no application change, no vendor call, no deployment and no schedule change. One surprise
row was filed: ETFS_RIVALS-Z-S10 @4add024498.

**State moving under the read.** `2.0.0_SA_COO~RV` was applying round 4 (RIV-d-5) during this trace. Every Lambda read
here is the round-3 build of 10:53Z. Hops marked "round 4" change when d-5 lands, and should be re-read then.

## Andrew's three questions, answered first

| Question | Verdict | Why, in one line |
|---|---|---|
| 1. Is the methodology sound? | **The core is sound. Three defects make served trades wrong today.** | The flow-factor residual separates the index fund's quarterly rebalances correctly. But equal-value swaps are erased as "identifier changes", the flow factor has no sanity bound (INEQ reads f = 0 and books 102 false trades), and dividends and corporate actions are frozen at 2026-09-30. |
| 2. Is the comparison base adequate for Opal and non-Opal ETFs? | **Rivals: yes. Opal funds: no. Sectors: no. The comparison layer itself: not built.** | Rivals hold 91 to 501 genuinely new reports each, back to two years or to inception. IDVZ and PFOE hold 22 each, from 2026-08-21/24, although PFOE has traded since 2025-12-31. GICS sector is 0% filled for both Opal funds and four rivals. The tables that compare (G7 to G13) and the AI step do not exist. |
| 3. Are all pipelines and schedules set up? | **Mostly. One leg is a silent no-op, and GQGU is not yet collected.** | Three schedules are live and fired today. The morning enrichment step reports "landed" but pulls nothing (row S10). GQGU's issuer route is merged but not deployed (d-5). The Bloomberg leg has one scheduled day of history. |

## Design finding

The surface tracks two peer groups:
- **IDVZ group:** IDVZ with TXUE, BIDD, CGIC, INEQ and SCHY, where SCHY is the index control.
- **PFOE group:** PFOE with WCMG, GQGU, TSEL, BASG, ETFT and PCLG.

It collects each fund's published daily holdings, keeping the source bytes. It then:
1. coalesces the holdings into one master shape (G1);
2. infers each fund's trade schedule from consecutive genuine reports (G5), clean of flows, income and corporate actions;
3. serves a dated page at `mcp.opalinvest.dev/rivalfunds`.

On top of the trade schedule the design adds deterministic comparison tables:
- outcomes (G7, G8);
- the style read (G9);
- projections (G10);
- the peer comparison (G11).

AI text (G12, G13) only explains figures those tables computed. Sources:
- issuer sites first for the PFOE group;
- Bloomberg for the IDVZ group;
- the existing Positioning pull for the two Opal funds;
- dividends, prices and GICS from scripted Bloomberg enrichment.

**How far the build is from that:** the ingestion-to-trade-schedule spine works and is scheduled. Keep it: bronze, silver
and G1/G2/G5/G6 over 502 dates, markers and triggers, a published page with guardrails and read-back. What the design
calls the product, comparing an Opal fund with its rivals on the same measures (FWD-6, 7, 10 and 11), has no code. The
spine also carries three method defects and two data-depth gaps that would distort any comparison built on it now.

## Current measurement

Everything below was read from the live plane at the times stated, with no writes. The evidence JSON is
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ETFS_RIVALS_END_TO_END_GAP_EVIDENCE_20261001.json`.

**Lambdas** (`get-function-configuration`): all five were last modified at 2026-10-01T10:53Z, the round-3 apply.

| Function | CodeSha256 |
|---|---|
| `etfs-rivalfunds-fetch-holdings-lambda` | `CpDqOmM1...` |
| `rivalfunds-build-silver-lambda` | `+49y0oZq...` |
| `rivalfunds-build-canonical-shape-lambda` | `rgGYTa1q...` |
| `rivalfunds-publish-page-lambda` | `JJwGbNdv...` |
| `etfs-rivalfunds-daily-lambda` (the sweep) | `2ntvxiLm...` |

I did not download the zips or diff them against source. The comparison of deployed bytes to source is the d-5 ledger's
job.

**Schedules** (`scheduler get-schedule`), both ENABLED:
- `etfs-rivalfunds-daily`: cron(0 7 ? * MON-FRI *) New York, targeting fetch-holdings.
- `etfs-rivalfunds-sweep-daily`: cron(0 9 ...), targeting the sweep.

The Windows task `OPAL_BBGTML_daily_pull` runs daily at 07:00 local; its last run was 10/1 07:00:01 with result 0.

**What fired** (S3 batch markers):
- **Issuer fetch:** fired by the schedule on 09-30 at 11:00:34Z and on 10-01 at 11:00:33Z. The chain ran on markers
  through silver, canonical shape, trade schedule, coverage and the page (publish marker 11:01:38Z).
- **Bloomberg leg:** first scheduled run on 10-01 at ~11:13Z, exit 90.
- **Sweep:** fired at 13:00:18Z and wrote only the peer-group-map marker, because the day's page already existed.

**Served page** for 2026-10-01: `status: published`, 13 funds in total, 12 updated (GQGU not), `readback: true`, every
threshold PROVISIONAL. The current object is a d-4 worker act (batch `d4-publish-r3b`, 11:16:08Z) over the scheduled
11:01Z revision. Its three sections are "Most recent trades, by Opal fund", "Latest holdings by fund" and "Data status".

**Gateway:** `server.py:997-1001` routes `/rivalfunds`, `/rivalfunds/archive` and `/rivalfunds/{day}`. A signed-out probe
returns 302 to Entra for every path, including `/rivalfunds/nonexistent-zz`. It proves nothing about the route, so I did
not count it.

## Adapter map

| Fund (group) | Policy in the map | What actually supplies it today | Gap |
|---|---|---|---|
| BASG (PFOE) | issuer_first | issuer site (`adapters/basg.py`), 326 reports since 2025-06-13 | identity resolved 0% on the newest date (round-4 alias RIV-i-2 not yet deployed) |
| GQGU (PFOE) | issuer_first | **nothing served**; `adapters/gqgu.py` merged, 305-day archive import in d-5 | Andrew 2026-10-01: GQGU began in July 2025, so the archive (2025-07-14 onward) is its whole life once imported |
| WCMG, TSEL, ETFT, PCLG (PFOE) | issuer_first | **Bloomberg** (no issuer adapter exists) | the policy says issuer-first and the world is Bloomberg-only; Bloomberg repeats an old report often (TSEL 42, WCMG 18, PCLG 13 repeat days) |
| TXUE, BIDD, CGIC, INEQ (IDVZ) | bloomberg_primary | Bloomberg, 417 to 498 new reports | GICS sector 0-4% filled |
| SCHY (IDVZ, index control) | bloomberg_primary | Bloomberg, 501 new reports | GICS 0% |
| IDVZ, PFOE (home) | home_producer | the Positioning pull, read; 22 reports each from 2026-08-21 / 08-24 | PFOE has ~9 months of earlier history (launched 2025-12-31); IDVZ's launch date is unmeasured (the BQL probe errored on `fund_inception_date`); identity 0% resolved |
| every fund | enrichment | G3 one QA import (09-30); G4 one date (09-29) | the scheduled pull is a no-op (row S10) |

One fund's success does not certify another's: the three sources fail differently.

## Start-to-finish walk

### 1. Peer-group map -> every stage (G0) -- MISMATCHED

What exists: `data/etfs/scripts/rivalfunds/peer_groups.json` (map_version 1, 13 entries) and `gold_peer_group_map.py`. A
group is data, not code (FWD-12 holds).

The mismatch, on method:
- **Undeclared peer selection.** No document states why these funds are the peers (category, region, active vs passive,
  size, launch date). The IDVZ set came from one email (`INTAKE_IDVZ_PEER_GROUP_20260930.md`); the PFOE set came from
  the original brief.
- **No index control for PFOE.** SCHY is IDVZ's control, and the PFOE group has none. FWD-10's label gate
  (`control_passed`) has nothing to pass for PFOE's peers.
- **The issuer_first policy is unimplemented for 4 of the 6 PFOE rivals.**

Close: a one-page peer-selection note (criteria, each fund's fit and launch date), Andrew's choice of a passive control
for the PFOE group added as one map entry, and the source policy of WCMG/TSEL/ETFT/PCLG set to what is true
(`bloomberg_primary`) or given issuer adapters.

### 2. Issuer sites -> issuer bronze (07:00 ET, AWS) -- INCOMPLETE

What exists: `collector_issuer.py` and `adapters/{basg,gqgu}.py`. Schedule `etfs-rivalfunds-daily` fired both trading
days since enable.

The mismatch: the deployed code fetches BASG only. GQGU's route is merged (RIV-q-1) but deployed only by d-5.

Close: d-5 lands; then the next trading day's 07:00 marker names both BASG and GQGU bronze objects.

### 3. Bloomberg (terminal box) -> Bloomberg bronze (07:00 ET local task, ~07:13) -- INCOMPLETE

What exists: the `:rivalfunds_bbg_leg` of `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` and
`collector_bloomberg.py`.

The mismatches:
- **One scheduled day of history.** 10-01 was its first scheduled run: exit 90, one bronze object for as-of 09-30.
- **The run time differs from the PRD.** The PRD's C-SOURCE-POLICY says 08:03 ET; the vehicle runs at 07:00. The
  fallback order (issuer first) holds only because the issuer fetch finished at 11:00:34Z, before the leg at ~11:13Z.
  That is timing, not a dependency.
- **Bloomberg-sourced funds lag by a day.** ETFT, PCLG, TSEL and WCMG show `gap` at 09-29 as well as 09-30.

Close: 5 consecutive trading days of exit 90 read from the logs and S3 alone (FWD-3). The CTO either aligns the PRD's
time to the vehicle or the leg checks the issuer marker before choosing funds.

### 4. Positioning pull -> home-fund silver (IDVZ, PFOE) -- INCOMPLETE

What exists: `home_producer.py` reads the Positioning constituents landing (C-HOME-PRODUCER v0.5, Andrew's "1b").

The mismatch: 22 reports per Opal fund against 91 to 501 per rival.
- RIV-m-1 recorded the shortfall as a stated LIMIT, capture-forward from 2026-08-21.
- PFOE has traded since 2025-12-31, so about 9 months of its history exist and are not used.
- PFOE publishes as a Pathfinder ETF on the Filepoint website platform, under the `OpalCap` client namespace
  (`pathfinderetfs.com/assets/data/FilepointOpalCap...`; DS log 2026-05-18). That is the same platform class as GQGU's
  measured issuer route. Its holdings file and archive depth are UNMEASURED.
- **Correction (2026-10-01 ~18:1xZ, on `1.0.0_SA_CTO~Z` msg 28012):** this brief first named "Opal's custodial data
  (`data/black_diamond` / `data/cot` positions cubes)" as PFOE's history. That is wrong on two counts:
  - those cubes hold CLIENT ACCOUNTS' units of PFOE (the 2025-12-31 seeding journals), not PFOE's own holdings;
  - `cot` is a separate firm, which CLAUDE.md forbids a pipeline tree to reference.
- Identity resolution on home rows is 0% (`crosswalk:miss` on all 41 IDVZ and 23 PFOE lines), so G4's GICS join cannot
  reach them.

Close: an **Andrew call** (below) on a history source for the two Opal funds that does not touch the Positioning pull.
The first act is a read-only reachability and archive-depth probe of each fund's own issuer files, run from AWS like
RIV-r-1: PFOE on Filepoint, IDVZ on its TrueShares page. Then a backfill read into home-producer silver, under its own
provenance, back to each fund's launch. The predecessor fund PFOE was seeded from is kept distinct (FWD-2).

### 5. Bronze -> typed silver -- WORKS

The marker rules `rivalfunds-build-silver{,-bloomberg}-on-marker-created` chained on both scheduled days.

Close: none on the thread.

### 6. Bloomberg enrichment -> G3 corporate_actions, G4 security_market -- MISSING (on the schedule)

What exists: `enrichment_bloomberg.py` (`handler_entry`, modes daily / market / import).

The mismatch: the vehicle runs `python -m rivalfunds.enrichment_bloomberg --mode daily`, and the module has **no
`__main__`**. It imports and exits 0, and the log prints `94 -- landed`. As a result:
- G3 is one QA import (09-30), and G4 holds one date (09-29).
- Every dividend, split and GICS value after those dates is missing.
- C-INCOME-CLEAN and the share-change gate silently degrade as G3 ages.

This is row **ETFS_RIVALS-Z-S10** (BLOCKING/ARMED, disarm owner `2.0.0_SA_COO~RV`).

Close: a CLI entry calling `handler_entry({"mode":"daily","date":<as-of>})` with the collector's 0/1/2/3 exit contract.
Then one scheduled run, read on S3 as a new G3 and a new G4 object for that day.

### 7. Silver -> G1 canonical_shape -- INCOMPLETE

What exists: `gold_canonical_shape.py`, 502 dates (2024-09-30 to 2026-09-30), with every source column kept.

The mismatch, on the newest date (non-cash lines):
- **GICS sector fill:** IDVZ, PFOE, BASG, BIDD, INEQ and SCHY 0%; CGIC 2.6%; TXUE 4.1%; WCMG 10%; ETFT 48%; TSEL 54%;
  PCLG 66%.
- **GICS industry and sub-industry:** 0% for every fund. C-SHAPES promises all four levels.
- **Identity resolved:** 0% for BASG, IDVZ and PFOE. G1 itself is complete in rows and identifiers; the classification
  and resolution are what is missing.

Close: once hop 6 runs daily, the G4 market pull covers every non-cash security across all dates held (a one-time
backfill of G4 over G1's distinct securities), and the gold join's fill per fund is printed in the page's Data status.

### 8. G1 -> G2 holdings_coverage -- WORKS (12 of 13 funds)

502 dates, with new/repeat/gap per fund and source; GQGU is absent until d-5. FWD-2's data exists. Its rendering is a
"Data status" section, which I did not grade.

Close: GQGU appears after d-5.

### 9. G1 + G3 -> G5 trade_schedule, G6 flow_reconciliation -- MISMATCHED (method)

What exists: `gold_trade_schedule.py` v2.
- The flow factor `f` = median of q_t/q_{t-1}.
- The residual floor is 0.2% of prior shares.
- Income and corporate-action cleaning precede the residual.
- 19,165 trades over 3,656 fund-windows served.

**Evidence the core works:** SCHY's six busiest windows are 2026-03-23, 2025-03-24, 2026-06-22, 2024-12-23, 2025-12-22
and 2026-09-21, each with 100 to 124 trades. They are the index's quarterly rebalance Mondays, so the method sees a
systematic manager's signature.

The defects, each measured on served G5/G6:

- **(a) False identifier changes erase real swaps.** An exit and an entry whose market values agree within 1% become ONE
  `ID-CHANGE` row with 0 shares traded (`_id_changes`, `:315`). Nothing relates the two securities to each other.
  - 2 of the 3 served ID-CHANGE rows are real trades, both in Opal's own funds (names from G1 `security_name`):
    - PFOE on 2026-09-28 sold Universal Music Group (`91377B109`, 423,306 shares) and bought Quanta Services
      (`74762E102`, 5,388 shares) at the same 4.0% weight;
    - IDVZ on 2026-09-23 sold UBS Group (`H42097107`) and bought Lenovo Group (`526250105`) at ~1.9-2.0%.
  - The page reads both as no trade.
  - The third (BP plc, `55622104` -> `055622104`, a dropped leading zero) is a true ID change.
  - Funds near equal weight swap at equal value routinely, so this bites the home funds hardest.
- **(b) The flow factor has no sanity bound.** 7 of 3,656 windows have f below 0.5 or above 1.5.
  - INEQ reads f = 0.000 on 2025-08-29 (100 trades) and 2025-11-28 (102 trades). At f = 0 every holding is an "add" of
    its whole position, for example `1878 JP` at 4,498 -> 5,298 shares books 5,298.
  - TXUE reads f = 83.0 (2025-04-14) and TSEL 3.8 (2025-01-16).
  - These are bad reports (partial or zero quantities), not flows. They pass into served trades because the backfill
    never ran the page guardrails.
- **(c) A fund paired with the wrong prior date** (W1-S27): live until d-5. The code fix (RIV-t-5) is merged.
- **(d) The confidence label carries little information.** `UNRESOLVED` takes precedence and covers most rows: BASG 822
  of 839, CGIC 7,828 of 9,263, SCHY 3,553 of 4,186. The window-stable key makes trades correct without resolution, so a
  reader learns little from the label.
- **(e) The price band is null on every row** (`bloomberg-band-enrichment`); it waits on hop 6.

Close:
- (a) Only an identifier relation makes an ID-CHANGE: a G3 or issuer-published identifier event, a shared CUSIP-6
  issuer root, or an ISIN/SEDOL crosswalk hit. Equal value alone stays an exit plus an entry.
- (b) Refuse a window whose f falls outside a measured band, or where the share of zero-quantity lines exceeds a floor.
  The refused window is recorded in G6 and the trades are not inferred. Then run the replay through the same
  guardrails the page uses.
- (d) Report key resolution as its own column and drop it from the confidence precedence.

Each close is a CTO ruling, then a COO cell, with a replay under a never-widen pair.

### 10. G5 -> G7-G13 (outcomes, rollups, style read, projections, peer comparison, AI) -- MISSING

`comp-find` for `openai|research_hypotheses|style_read|trade_outcomes|peer_comparison|trend_projection|outcome_rollup`
over the package and the Lambda tree: **0 hits across 71 files.** FWD-6, FWD-7, FWD-10 and FWD-11 have no producer. This
is the comparison Andrew asked about. Building it on hops 4, 6, 7 and 9 as they stand would compare 22 days of Opal
against 2 years of rivals, by sector with no sectors, from a trade list that loses Opal's swaps.

Close: build G7, G8, G9 and G11 (deterministic) after hops 4, 6 and 9 close, with G9's gate tested first on SCHY (it
must read systematic) and on a PFOE-group control. G10, G12 and G13 (AI) come after, per C-AI-GROUNDING.

### 11. G0/G1/G2/G5/G6 -> platinum page -- WORKS (FWD-1 scope)

What exists: `publish_page.py` / `render.py`. The 10-01 page is published with all six pre-publish checks, read back,
grouped by Opal fund, and archived by day with a `revisions/` trail. All thresholds are PROVISIONAL
(`guardrails_config.json`); d-5 sets the identity floors from measurement.

The page shows trades, holdings and data status. It has no comparison section, because hop 10 does not exist.

Close: the thresholds come from 20 trading days of scheduled data (C-GUARDRAILS), with each value's provenance recorded.

### 12. Platinum -> `mcp.opalinvest.dev/rivalfunds` (the MCP page) -- INCOMPLETE (not provable from outside)

What exists: `infra/aws/ec2/opal-gateway/app/rivalfunds_view.py` and `server.py:997-1001`, behind Entra sign-in
("any signed-in account"); the read grant is `infra/aws/terraform/opal-gateway/rivalfunds-iam.tf`.

The mismatch: no signed-in read exists in any record of FWD-1. The CTO's round-3 analysis lists it as Andrew's own act,
and the signed-out probe cannot tell the route from a miss.

Close: **one signed-in `/rivalfunds` read by Andrew** after d-5 lands, picking a rival trade and following it to its
two reports and the issuer bytes. That read is the live thread.

### 13. Schedules, end to end -- INCOMPLETE

The chain is issuer fetch (07:00 ET, AWS) -> silver -> G1 -> G5/G6 -> page, all by marker; then the Bloomberg leg
(~07:13 ET, box) -> silver -> G1 ...; then the sweep (09:00 ET) as backstop. All three fired on 10-01. The Positioning
pull for the home funds rides the same box task (its constituents leg, exit 0 on 09-29, 09-30 and 10-01).

The gaps:
- enrichment (hop 6);
- only one scheduled Bloomberg day;
- the box task depends on a logged-in Terminal (accepted as "fragile" by Andrew);
- no day yet whose page the schedules alone produced. The 10-01 page was overwritten by a worker act at 11:16Z.

Close: five consecutive trading days whose pages carry a scheduled batch id (an execution-id UUID or the sweep's) and
no worker batch.

## Recommended completion sequence

1. **The live thread.** Andrew, signed in, reads `/rivalfunds` on the deployed stack after d-5, once per group: IDVZ
   with its peers, then PFOE with its peers including GQGU. He follows one rival trade back to its two reports and the
   issuer bytes, recorded as ONE trace. Owner of the first hop (gateway sign-in): the deployed gateway.
   **Crosses hops 2, 5, 7, 9, 11, 12.**
2. **Disarm S10** (enrichment CLI) and backfill G4 over every held security. Hops 6 and 7: dividends, splits and GICS
   become current.
3. **Fix the three method defects** (hop 9 a, b, d) and replay G5/G6 under a pair. The trade list then stops losing
   swaps and stops booking bad reports.
4. **Opal history** (Andrew call 1): PFOE and IDVZ back to launch. Without it no comparison is fair.
5. **Peer method** (Andrew calls 2 and 3): a selection note, a PFOE-group control, and source policy matching reality.
6. **Build the comparison layer** G7, G8, G9 and G11, deterministic, SCHY-gated. Then the AI (G10, G12, G13).
7. **Day-over-day proof:** five scheduled trading days with no worker act, then set the thresholds from 20.

## Calls only Andrew can make

**ANSWERED by Andrew 2026-10-01 ~18:2xZ.** The verbatim record is
`ANDREW_DIRECT_20261001_182xZ_ETFS_RIVALS_THREE_CALLS_ANSWERED.md`:
1. IDVZ and PFOE go through the same rivalfunds Bloomberg pull, in the same queue as the other Bloomberg-sourced funds.
2. Russell 2000 is the PFOE group's control and ACWI the IDVZ group's.
3. No peer-selection criteria are needed: the asset management team pre-decides the sets, so hop 1's "undeclared peer
   selection" finding is withdrawn.

The recommendations below are kept as written at the time of asking.

1. **A history source for IDVZ and PFOE.** My recommendation (corrected, see hop 4): the funds' own published
   holdings files, reached from AWS. That means PFOE on Pathfinder's Filepoint platform (the `OpalCap` namespace, the
   same platform class as GQGU) and IDVZ on its TrueShares page, read back to launch with their own provenance, after a
   reachability and archive-depth probe. The Positioning pull stays untouched. The Positioning pull lands only from
   2026-08-21, so the history would come from a second source for the early dates. That reverses the "stated limit"
   RIV-m-1 recorded under C-HOME-PRODUCER, so it needs Andrew's word and a CTO ruling on "never two producers" (for
   example, the issuer file for dates before 2026-08-21 and the Positioning pull from then on).
2. **A passive control for the PFOE group**, the counterpart of SCHY. My recommendation: one broad international equity
   index ETF matching PFOE's mandate; the CRO names candidates on request.
3. **Confirm the peer sets** against a written criterion (or name the criterion). My recommendation: same region and
   mandate, actively managed, at least 12 months live, with the control as the one passive member.

## Acceptance

One reconciled trace per case, each following a trade from the page to G5/G6, G1 rows on both dates, silver, the
bronze bytes and the source. The cases are:
- {BASG, GQGU (issuer), TSEL (Bloomberg), SCHY (control), IDVZ, PFOE (home)}
- x {a clean add or trim, an entry/exit swap at equal value, a dividend window, a split window}
- x {a daily window, a widened window}
- x failure cases {a bad report (f out of band), a Bloomberg repeat, a missing day, a failed guardrail}.

The surface is complete when these reconcile on scheduled data, not when tests pass.

## Evidence anchors and limits

Source was read at CLOUD 74f12b3092; the live plane at 17:30Z-18:15Z 2026-10-01; this brief commits after 4add024498.

**Verified fresh:**
- the schedules;
- the Lambda configurations;
- the S3 markers and gold objects (502 G2 objects, 501 G5 and G6 objects, newest per date);
- the 10-01 page manifest and HTML;
- the box-task logs (10-01, 09-30 and 09-29);
- the enrichment module's lack of an entry point.

**Not verified:**
- the deployed zip bytes against source;
- a signed-in page read;
- the rendering of the Data status calendar;
- G1 before 2026-09-28 for classification fill;
- IDVZ's launch date;
- the round-4 state after d-5.

Paths:
- `data/etfs/scripts/rivalfunds/gold_trade_schedule.py` (`_id_changes` :315, flow factor :426-428)
- `data/etfs/scripts/rivalfunds/enrichment_bloomberg.py` (no entry point)
- `data/etfs/scripts/rivalfunds/peer_groups.json`, `guardrails_config.json`
- `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` (`:rivalfunds_bbg_leg`, `:rivbbg_enr`)
- `infra/aws/terraform/etfs-rivalfunds/generated.auto.tfvars.json`
- `infra/aws/ec2/opal-gateway/app/server.py:997-1001`
- `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md` (v0.7), `ledger/ROUND_ANALYSIS.round3.md`,
  `decompositions/ETFS_RIVALS_DECOMP.md` (round 4)

## Andrew-direct request -- verbatim record

Channel: terminal, session of `4.0.0_SA_CRO~RV`, 2026-10-01 ~17:24Z (record
`ANDREW_DIRECT_20261001_172xZ_ETFS_RIVALS_CLOSER_TRACE_GAP_ANALYSIS.md` @b7622c0b5a).

> I want you to take a look at the current implementation of the ETFS_RIVALS project. That is going to be your sole
> work for this session. I want you to run a gap analysis from ingestion to mcp page, /closer trace ETFS_RIVALS
> project with that directive. My goal is to first make sure that the methodology is sound and we have an adequate
> base of comparison for both Opal and Non-Opal ETFs and all data pipelines and schedules are set up. Go now.

Same channel, mid-trace (~18:0xZ):

> GQGU only started in July of 2025, so that is one aspect of this worth keepin mind
