# IRPT_BCKEND outcome grade at portal PROD c69b4747 -- FWD-1..FWD-13 (3.0.0_SA_CVO, 2026-10-04 ~23:0xZ)

Asked by 1.0.0_SA_CTO msg 104973 (analysis ec2fe1f9a0 section 4). **0 of 12 REALIZED** (FWD-6 vacant). The body below is
the delegate's evidence record; this seat re-read three load-bearing facts itself at ~23:0xZ: (1) `c69b4747:src/App.tsx`
:105 and :460 gate /investor-reporting to admin + internal + Dev (Andrew-direct 2026-09-22); (2) the directory
`_refresh` manifests read FAILED / HAND_OVER_RUNNER_OFFLINE at 49F and INF on 09-29, 10-01, 10-02 and COT on 10-02
(row IRPT_BCKEND-S323); (3) scheduler irpt-intake-poll DISABLED. Rows filed: IRPT_BCKEND-S323 (directory refresh), IRPT_BCKEND-S324 (READY export without the
v0.24 refs). Not rowed, for the CTO's analysis: FWD-3's no-flow wording vs the served cash-flow-adjusted 49F method (a PRD
question); ~P's orders tag work with FWD numbers that do not match the PRD; the refresh manifest records 09:00 ET while
the live schedule is 09:30 ET.

---

# IRPT_BCKEND -- consolidated outcome grade FWD-1..FWD-13 at portal PROD c69b4747 (PREPARED, read-only)

Prepared for 3.0.0_SA_CVO (owed to 1.0.0_SA_CTO, msg 104973; CTO analysis
org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_BCKEND_ROUNDS_42_46_P_20261004.md section 4).
Reads taken 2026-10-04T21:40Z-22:20Z (UTC). Workspace CLOUD; nothing committed, edited, invoked, applied or messaged.
Standard: the ENDPOINT block of org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md at HEAD (prd_version v0.25;
endpoint_outcomes FWD-1..5, 7..13; FWD-6 vacant). Addenda v0.18-v0.25 read for how an outcome is read (rulings 19-24).
Builds on: org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_BCKEND_FAST_PIN_GRADES_20261001.md (pin grades 10-01..10-04),
ADJUDICATION_v23 / REMEDIATION_v19 (sweep 8), and CTO round-28 analysis (last outcome read, one hop).
No consolidated FWD grade exists after round 28 (searched CVO deliverables, CTO deliverables and the project dir).
Trading-day frontier (lib/trading_calendar.py, NYSE/pandas_market_calendars): expected_last_trading_day(2026-10-04) =
2026-10-02 (Friday). A morning T-1 producer's newest expected partition on Sunday 10-04 is 2026-10-01.

## Result

| FWD | verdict | one-line reason |
|---|---|---|
| FWD-1 | NOT REALIZED | PROD gates /investor-reporting to Opal admin + internal + Dev users, so no firm advisor can search on PROD; and every firm's served directory is 5-8 trading days old because the daily refresh has FAILED at every firm since 09-29 |
| FWD-2 | NOT REALIZED | the full swapped-identifier replay (incl. revoked grant vs warm cache, PDF and export routes) was last run 09-17/18 on bytes since replaced; 21 scoped routes now, several added since; S238 still ARMED in the channel |
| FWD-3 | NOT REALIZED | Cottonwood has no holdings-basis figure served (gold ends 09-25, no schedule, adapter has no Cottonwood grant); 49 Financial now serves PATH B (IRPT_DASHBD flow-adjusted total return), not FWD-3's no-flow holdings basis; no Inflection PDF export exists |
| FWD-4 | NOT REALIZED | 13 READY analyses, all Cottonwood under the service principal; no single-Comparison READY since S194 (09-29 READY printed no comparison); no Opal-branded Analysis export exists (0 receipts); S318/S321 ARMED: READY analyses of the easy template read Unavailable on the page |
| FWD-5 | NOT REALIZED | the holdings publication is current at all three firms (date=2026-10-01), but the replay on the current publication is owed (~M's two walks open; 49F and COT reconcile not re-read since 10-01) and the page is Dev-gated on PROD |
| FWD-7 | NOT REALIZED | the five-arm controlled-clock drive (IB-rte-5, CVO PASS at ADJUDICATION_v2) ran on refresh bytes q7O3GGjK, replaced 09-24 by DXuzx9jp; the served search bundle carries no over-age (expiry) branch; live directories are past the declared 2-trading-day ceiling and served with their as-of only |
| FWD-8 | NOT REALIZED | the only READY export (49F, PROD, EXP-e29b5415) carries no narrative packet, selects no sections, and pins brand/template/renderer/disclosure versions as "unknown"; irpt-narrative last ran 2026-09-20 |
| FWD-9 | NOT REALIZED | the intake schedule irpt-intake-poll is DISABLED; irpt-intake-poller has no log streams; irpt-checkpoints and irpt-outbox hold 0 items -- no forwarded email has ever become a request |
| FWD-10 | NOT REALIZED | nothing has been ingested from a sender domain (FWD-9 off), so the firm-from-sender binding and its failure arms have not been exercised on the served intake |
| FWD-11 | NOT REALIZED | one READY export exists across all firms (49F); no report-and-export pair at a second firm; no recorded global-vs-firm-scoped figure comparison |
| FWD-12 | NOT REALIZED | 49F: scheduled run produced 10-01 (PASS for that firm); Inflection: no scheduled fire yet (schedule created 10-02 21:05Z, first fire Mon 10-05 14:00Z; 10-01 landed by hand); Cottonwood: no function or schedule, gold ends 09-25; the ABSENT-day and missing-price arms were driven only in local harnesses |
| FWD-13 | NOT REALIZED | 49F comparison landed at 2 points with both bases named; Inflection, which has landed official performance, has 0 comparison objects |

0 of 12 REALIZED at portal PROD c69b4747.

## The served world read (common to several FWDs)

- Portal PROD: `git -C portal ls-remote origin PROD` = c69b474716f2 (tag portal-v2.1.199). `gh run list --workflow
  deploy.yml --branch PROD`: run 37231846084 for c69b4747 conclusion success (created 20:22:35Z); no later PROD run.
  CloudFront EVTSA9VEHNZVH (opalinvest.dev) default origin S3 bucket opalinvest-portal: index.html LastModified
  2026-10-04T20:24:56Z, sha256 86391ead4d0cf580; https://opalinvest.dev/index.html returns the same sha256 (x-cache Miss).
- PROD gate: `git show c69b4747:src/App.tsx` lines 105 and 460: `/investor-reporting` is
  `requiresAdmin, requiresTier internal, requiresDev` and the route `<ProtectedRoute requireAdmin requireInternal
  requireDev>`; nav filter at 336-371 drops it unless `claims.userType === 'Dev'`. Source comment: Andrew-direct
  2026-09-22 "marked in tsx for admin and isDev only". The print route (612) adds allowRenderClaim.
- Lambdas (get_function_configuration, 16 functions): CodeSha256 vs infra/aws/lambda/ci/lambda-source-map.json
  deployed_code_sha256 equal for irpt-holdings, irpt-holdings-performance-lambda, irpt-inf-holdings-performance-lambda,
  irpt-performance-adapter, irpt-status. Lagging or absent deploy record: irpt-ycharts-generate (live uFTONal/Rh, map
  FgZcBjJuwu -- row S320), irpt-directory-refresh (live DXuzx9jpOP, map d5fqVJ0fgA in both fields), irpt-directory-search
  (live AVSIaHEhm+, map deployed o9Qu0Jm7ji, artifact equal), irpt-export-render / irpt-intake-poller / irpt-narrative /
  irpt-holdings-refresh-lambda / opal-portal-authorizer (deployed record None, artifact equal), and the three
  irpt-49f-reporting-* functions (no map row). This is E3's population.
- API 7k3ed8px20: 112 routes, 21 investor-reporting, all under /api/scoped/, all CUSTOM authorizer (analysis 7,
  directory 3, export 3, reporting 2, status 2, performance 1, selections 1, narrative 1, holdings 1).
- Schedules (EventBridge Scheduler): irpt-holdings-performance-daily ENABLED cron(30 7 MON-FRI) America/New_York;
  irpt-inf-holdings-performance-daily ENABLED cron(0 14 MON-FRI) UTC, created 2026-10-02T21:05:01Z;
  irpt-directory-refresh ENABLED cron(30 9 MON-FRI) America/New_York; irpt-holdings-snapshot ENABLED cron(15 10 MON-FRI);
  irpt-intake-poll DISABLED cron(0/15 8-23 * * ? *); three irpt-49f-reporting-* ENABLED. No Cottonwood
  holdings-performance schedule or function exists.

## Per FWD

### FWD-1 -- NOT REALIZED
DONE WHEN (verbatim): "EXERCISED -- an advisor who has never used the workspace has searched, selected, and been shown
the relationship and its permitted accounts".
Decisive reads:
1. PROD gate (above): only an Opal admin, internal tier, userType Dev reaches the page. A firm advisor cannot search on
   PROD by construction (Andrew-direct 2026-09-22). This alone holds the outcome.
2. Directory freshness, s3 `investor-reporting/directory/` in opal-data-bd / opal-data-inf / opal-data-cot:
   latest.json points to as_of 2026-09-24 (49F, 4,620 entries), 2026-09-25 (INF, 292), 2026-09-22 (COT, 258), all
   written 2026-09-25T13:30Z. `_refresh/<day>/manifest.json`: REFRESH_FAILED on 09-29, 09-30, 10-01, 10-02 at 49F and
   INF (4 of 4 trading days) and on 10-02 at COT; notes "dispatch failure token HAND_OVER_RUNNER_OFFLINE (HAND_OVER
   half)", delta.build_command_status "start issued, no build sent". Runner i-02448edb624a7a7cf (mdpf-daily-runner):
   stopped, "User initiated (2026-10-04 16:41:18 GMT)", no SSM registration listed.
3. irpt-directory-search logs: 153 `BucketUnmapped` events in 7 days, 88 of them on 2026-10-04 (the CVO's F-1, a
   designed refusal answered as UNEXPECTED, still live).
Realizes on: Andrew's act opening the page to a firm advisor (or naming an advisor test principal), the refresh
dispatch repaired so each directory is inside its ceiling, then one signed-in advisor walk.

### FWD-2 -- NOT REALIZED
DONE WHEN: "EXERCISED -- an unauthorized request has been replayed and revealed nothing" (PROOF: swapped firm, advisor,
account, relationship, report and PDF identifiers, including a revoked grant against a warm cache).
Decisive reads:
1. The replay batteries (TO-IB-sb-3, TO-IB-rtb-1, complete 09-17/18) ran against the routes and bytes then deployed.
   Every serving function has moved since (directory-search 10-01, holdings 10-01, status 10-03, adapter 10-03, export
   10-03, generate 10-04, authorizer 10-03), and routes were added (the /pdf route, the export routes, the reporting
   series routes). No full-route replay on the current bytes is recorded.
2. Partial live evidence on current bytes, held from the CVO's FAST pin grades (10-01..10-02): service-principal
   foreign-firm requests answer UNAVAILABLE FIRM_BINDING on comparisons, POST analysis, sections, status, history, pdf.
   These are the service class only; the advisor class and the revoked-grant-vs-warm-cache arm are unread.
3. Channel: S238 (BLOCKING, ARMED, disarm owner 1.0.0_SA_CTO) still reads ARMED; its condition (the CTO's re-read of a
   foreign-firm refusal on deployed bytes) appears met by the reads in item 2 but has no clock.
Realizes on: one replay battery across all 21 scoped routes on current bytes with both principal classes and the
revoked-grant arm; then S238 clocked.

### FWD-3 -- NOT REALIZED
DONE WHEN: "EXERCISED -- one invested account per firm (49F, INF, COT) has been computed from landed holdings, carried to
the rendered view and the PDF at one gold revision, and reproduced by hand from that day's holdings".
Decisive reads:
1. Cottonwood: s3 opal-data-cottonwood/irpt/cottonwood/gold/holdings_performance_daily/ has 75 partitions,
   2026-06-10..2026-09-25 (last written 2026-09-29T10:53:50Z), 5 trading days behind the frontier; no function or
   schedule produces it. The adapter role irpt-performance-adapter-role has 2 holdings-gold read statements (49F and
   INF) and 0 for Cottonwood. HEAD `performance/retained.py:78` COMPOSED_FIRMS = (COT, INF) with the comment "Only
   Cottonwood reaches this [vendor-calculated] path now (COT never carries a holdings source)"; that path is refused
   (no approved vendor use). So no Cottonwood figure is served.
2. 49 Financial: PATH A retired for 49F (CTO batch 201; B3 closed 2026-10-03T18:44:32Z). The tab, print and export read
   PATH B, IRPT_DASHBD's account_return_daily (flow-adjusted, method_version 2). FWD-3's CONSTRAINT says "NO
   INFLOW/OUTFLOW LOGIC". CTO batch 178 says IRPT_DASHBD's FWD-1, FWD-2 and FWD-8 "hold the Performance outcomes", but
   IRPT_BCKEND's ENDPOINT still carries FWD-3 as written. This is an ENDPOINT question for the CTO, not a defect.
3. Inflection: holdings gold served to the adapter (IB-pr-221; three hand reproductions accepted, row S254); but
   opal-data-ycharts/firms/inflection/ holds no generations at all, so no Inflection PDF export exists.
Realizes on: a Cottonwood holdings-basis producer and schedule plus the adapter grant; an Inflection export READY; and a
CTO addendum saying whether 49F's FWD-3 is now read on PATH B.

### FWD-4 -- NOT REALIZED
DONE WHEN: "EXERCISED -- an approved report variant has been replayed from an analyst-approved input through its captured
request/job/result chain to the tab and the PDF" (PROOF: "replay each approved variant end to end"; ruling 19: the upload
lane counts).
Decisive reads:
1. irpt-jobs (33 items) joined to irpt-requests `analysis#` records and their retained compositions
   (opal-data-irpt/irpt/<firm>/state/request_compositions/, by VersionId): READY 13 = Overview 9, Multi-Comp 2
   (REQ-a1d9abc0 10-01, REQ-329a5618 10-03), Comparison 2 (REQ-e4b7f5ab and REQ-7ea49c2d, both 2026-09-29). ATTENTION 18
   (incl. one 49F and one Inflection Overview). Every READY job is Cottonwood, OPAL_GLOBAL service principal.
2. No single-Comparison READY since 09-29. Row S194 (BLOCKING, ARMED): the 09-29 Comparison went READY while its PDF
   printed no comparison; its remedy needs the fix served and one live Comparison PDF printing the chosen model.
3. The Opal-branded Analysis export (IB-pr-282 / E4): opal-data-ycharts/firms/cottonwood/generations/ holds no EXP-
   receipt; across all firms 1 receipt exists (49F performance). E4_ANALYSIS_EXPORT_READINESS_20261002.md lists the
   gaps; none is shown served.
4. S318 (ARMED) and S321 (ARMED, uncompiled, surfaced 21:05Z): a READY analysis of the YCharts easy template reads
   "Unavailable -- analysis status date basis unavailable" on the page; S321 measures the cause in the template's cells
   outside A/B. Held from the rows; no page walked here.
Realizes on: one Comparison READY on served code with the chosen model printed; the Analysis export served and one
downloaded; S318/S321 cured on the page.

### FWD-5 -- NOT REALIZED
DONE WHEN: "EXERCISED -- dated holdings and model snapshots have been replayed for all three registry client firms".
Decisive reads:
1. Holdings gold s3 opal-data-<firm>/irpt/<firm>/gold/holdings/: newest date=2026-10-01 at 49F, Inflection and
   Cottonwood (current for the Friday 10:15 ET run). irpt-holdings live tS/APci3Mz = map (deployed and artifact).
2. The replay on this publication: the CVO re-read Inflection only (FAST pin grades, 10-02 15:0xZ: 857 accounts sum, 0
   withheld, 71 split accounts). STATUS~M.md "Next proof": the Inflection split-account walk and the Cottonwood SPYI/PSLV
   walk are owed (ledger legs S open); 49F and COT reconcile-before-and-after not re-read since.
3. Page Dev-gated on PROD (above). Nominally open rows: S100 (BLOCKING ARMED, owner ~B, 09-19), S182 (COT multi-account
   identity, ARMED).
Realizes on: the two owed walks plus a before/after reconcile read with denominators at all three firms on the served
publication.

### FWD-7 -- NOT REALIZED (at current bytes)
DONE WHEN: "EXERCISED -- a DRIVEN exercise on a CONTROLLED CLOCK against source fixtures, covering the FAILURE arms, with
NO REAL-CALENDAR WAIT anywhere in it".
Decisive reads:
1. History: TO-IB-rte-5 (complete 2026-09-18) drove 5 of 5 arms; ADJUDICATION_v2 R55-AC2 PASS, verified against live
   irpt-directory-refresh q7O3GGjK. Live is now DXuzx9jpOP (applied 2026-09-24T20:59:50Z, the S125 fix). The exercise is
   on replaced bytes.
2. Served read path: the live irpt-directory-search zip (downloaded, sha256 = CodeSha256 AVSIaHEhm+E7, 22 members) has
   no expiry.py and no over-age branch; `served.py` takes the vintage "FROM THE ARTIFACT, NEVER FROM A CLOCK". HEAD
   `directory/expiry.py:47` MAX_AGE_TRADING_DAYS = 2. Live directories are 5-8 trading days old (FWD-1 item 2), and 0
   DIRECTORY_OVER_AGE log events in 7 days. So an over-age directory is served with its as-of but without the declared
   expiry answer (inferred from bytes; not exercised).
3. The FAILED arm is distinguishable live (REFRESH_FAILED manifests, 4 consecutive trading days), which meets one ACCEPT
   clause, but "becomes visible within the declared refresh window WITHOUT anyone asking" does not hold today.
Realizes on: re-running deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_4_controlled_clock.py against DXuzx9jp and the served
search, with the over-age arm on the served read path; the refresh dispatch repaired.

### FWD-8 -- NOT REALIZED
DONE WHEN: "EXERCISED -- a KNOWN drawdown window has been replayed against the dated topic history and the same inputs
selected the SAME inflection points twice".
Decisive reads:
1. The one READY export: opal-data-ycharts firms/49financial/generations/EXP-e29b5415a06f90f943481c41a1a4821b/
   receipt.json: job_state READY, page_count 11, validation PASSED, created 2026-10-03T22:13:14Z. Its bundle
   (exr_5f3c0b757a054bffbe31b431/.../bundle.json): no narrative_packet_ref, no analysis_report_ref, selected_sections [],
   approved_assets 0, versions.template/renderer/disclosure and render_options.brand_revision all "unknown";
   render_guard template performance-landscape-letter, 0 vendor requests, 0 foreign origins of 20. The 09-27/09-29
   bundles carried narrative_packet.json (45,266 B each); the READY one does not.
2. irpt-narrative last log activity 2026-09-20T11:43Z.
3. Not to be confused with IRPT_DASHBD's FWD-8 (tie-out vs Black Diamond), which the CVO graded REALIZED 10-03.
Realizes on: an export carrying the narrative page at dramatic moves, a twice-replayed drawdown window, and the
MISSING HISTORY arm, on served bytes.
Observation: ADDENDUM v0.24 says a bundle carrying neither ref "is refused"; the READY PATH B bundle carries neither.

### FWD-9 -- NOT REALIZED
DONE WHEN: "EXERCISED -- a real forwarded message with its attachment has become a request an advisor can see and correct".
Decisive reads: schedule irpt-intake-poll State DISABLED; /aws/lambda/irpt-intake-poller has no log streams; DynamoDB
irpt-checkpoints 0 items, irpt-outbox 0 items. Ruling 19 (v0.22) placed FWD-9 after the Analysis thread.
Realizes on: enabling intake (a served move) and one real forwarded message.
Observation: ~P's orders IB-pr-193..IB-pr-298 carry outcome_ref "FWD-9" for export and Analysis-export hops, and the
rounds 42-44 drain end calls the PROD export "the FWD-1 export hop". Neither matches the ratified ENDPOINT (FWD-9 =
email intake). An outcome-driven next analysis has to re-key these.

### FWD-10 -- NOT REALIZED
DONE WHEN: "EXERCISED -- a request has been ingested, bound to its firm from the sender's domain, and every failure mode
driven with no effect on a second firm".
Decisive read: no request has been ingested from email (FWD-9 reads). The poller packages
firm_destination_policy.json and firm_registry.json (env IRPT_FIRM_DESTINATION_POLICY), and IB-s-5 / IB-s-16 / IB-s-17
passed their batteries in September, but the served intake has never run.
Realizes on: FWD-9's first real ingestion, then the failure arms driven on served bytes.

### FWD-11 -- NOT REALIZED
DONE WHEN: "EXERCISED -- an Opal user has opened the global view, picked a client at a second firm, and run a report and an
export".
Decisive reads: export receipts in opal-data-ycharts firms/*/generations/: 1 in total (49F). Retained reports in
irpt-requests REPORT records: PERFORMANCE 49F 121, COT 2, INF 1 (no owner class recorded); ANALYSIS 13, all COT,
OPAL_GLOBAL (5 distinct principals, hashed). No report-and-export pair exists at a second firm; no global-vs-firm-scoped
comparison is recorded. The Dev gate admits Opal Dev admins, so the view is reachable by an Opal user.
Realizes on: an Opal user's report and export at two firms, the firm-advisor refusal replay, and the same-figure check.

### FWD-12 -- NOT REALIZED
DONE WHEN: "EXERCISED -- a scheduled run has produced one trading day for every firm, a deliberately withheld silver
partition has produced an ABSENT day, and a deliberately missing price has produced a named per-position exclusion".
Decisive reads:
1. 49F: /aws/lambda/irpt-holdings-performance-lambda 2026-10-02T11:30:08Z INIT, "computing date=2026-10-01", "rows=7570
   LANDED ... complete=True", REPORT 11:30:18Z; partition date=2026-10-01 written 11:30:18Z. PASS for 49F.
2. Inflection: newest partition 2026-10-01 written 2026-10-03T03:17:55Z (the hand landing, row S294); the schedule was
   created after Friday's slot; first scheduled fire Mon 2026-10-05 14:00Z. No scheduled-run partition yet.
3. Cottonwood: no function, no schedule; gold ends 2026-09-25.
4. Manifests carry not_computable_reasons (NO-PRIOR-HOLDINGS, NON-POSITIVE-BASE, ALL-HOLDINGS-EXCLUDED,
   IMPLAUSIBLE-RETURN, FOLLOWS-DISCONTINUITY). The absent-day and missing-price arms were exercised only in local
   harnesses (round 36 D1/D2, FAST pin grades 10-03 07:4xZ), not driven on served bytes.
Realizes on: Monday's Inflection fire read back; a Cottonwood producer and schedule; the two deliberate arms on served
bytes with the organic run as the negative arm.

### FWD-13 -- NOT REALIZED
DONE WHEN: "EXERCISED -- for each firm with landed official performance, the comparison has been produced at its pre-set
points and the difference read with both bases named".
Decisive reads: opal-data-49financial/irpt/49financial/gold/holdings_performance_comparison/: date=2026-06-30 (1 row,
restricted) and date=2026-08-28 (5,317 rows, 5,277 compared, 40 not comparable with reasons), written 2026-09-29; both
manifests name vendor_basis and opal_basis. Inflection: 0 objects, though ruling 8 names the landed weekly Orion household
factors as its points. Cottonwood: 0 objects, correctly NOT COMPARED (no landed pull). Ruling 8 names "the 4 landed Black
Diamond pulls" for 49F; 2 points exist. The 49F comparison predates the v0.21 re-emission of the 49F gold.
Realizes on: Inflection's comparison at its Orion points, and 49F's points reconciled to the four pulls, each read by
the CVO.

## Open BLOCKING or ARMED rows bearing on a FWD (nominal state at CLOUD HEAD)

Census (my parse of every JSON row in INVESTIGATION_v1 and REMEDIATION_v1..v19, with adjudication dispositions
subtracted): 667 investigation rows; 286 not closed (77 BLOCKING); 6 uncompiled. Owners of the not-closed: ~B 136, CTO 61,
~P 44, ~Y 25, ~M 9, other 11. As the CTO notes, many nominal ARMED states are stale (clocks advanced elsewhere).

| FWD | row | class / state | note |
|---|---|---|---|
| FWD-1, 2, 5, 7, 8, 11 | S50 | BLOCKING ARMED (CTO, 09-12) | runner-role IAM widening; likely stale |
| FWD-1, 2 | S90 | BLOCKING ARMED (~B, 09-19) | firm-advisor requests refused UNEXPECTED; unread since |
| FWD-2 | S238 | BLOCKING ARMED (disarm CTO) | condition looks met by FIRM_BINDING reads; no clock |
| FWD-3 | S237, S239, W100-S2 | BLOCKING ARMED | perfrp served figure; parked on the ADVI_PERFRP D2 hold |
| FWD-3 | S147 | ARMED | 49F read past the 30 s gateway cap |
| FWD-4 | S318, S321 | ARMED (~Y) | READY easy-template analysis reads Unavailable on the page |
| FWD-4 | S194 | BLOCKING ARMED (~Y) | no Comparison READY since its fix |
| FWD-4 | S284 | BLOCKING ARMED (~Y) | condition met by Y-5 V1 READY 10-04 02:28Z; no disarm row |
| FWD-4 | S218, S229, S232 | BLOCKING ARMED | conditions look met by READY jobs under svc-irpt-analysis; stale |
| FWD-5 | S100 (BLOCKING), S182 | ARMED | holdings loader pointer; COT multi-account identity |
| FWD-12 | S165, S257 | ARMED | COT login box has no retry; INF schedule timing (disarms on first fire) |
| FWD-7, 1 | none | -- | the refresh failures since 09-29 have no row (S126 was dismissed at C-S223 after one good fire) |

## Findings for the record (not filed: this preparation writes no row)

1. Directory refresh REFRESH_FAILED HAND_OVER_RUNNER_OFFLINE at 49F and INF on 4 of 4 trading days 09-29..10-02, COT on
   10-02; no open row. Bears on FWD-1 and FWD-7.
2. The refresh manifest's own `schedule.expression` reads cron(0 9 ? * MON-FRI *) while the live schedule is
   cron(30 9 ...); a missed-trigger reader of that field reads the wrong slot.
3. The served directory-search has no over-age branch (FWD-7 arm e not on the served read path).
4. The READY PATH B export bundle carries neither narrative_packet_ref nor analysis_report_ref, against ADDENDUM v0.24.
5. Lane outcome_refs ("FWD-9" for export hops, "FWD-1 export hop") do not match the ratified ENDPOINT numbering.
6. FWD-3's ENDPOINT (no-flow holdings basis for every firm) and the served 49F PATH B (flow-adjusted) diverge; the PRD
   has no addendum re-reading FWD-3 for 49F.

## What I could not read

- Any signed-in page or API response (no principal; reading a secret is out of bounds), so: the page states behind S318/
  S321, the advisor-class refusals, the revoked-grant arm, and what a user sees for an over-age directory.
- The resident host (no SSM command run), the vendor side, and any PDF's contents.
- irpt-directory-search REPORT counts beyond 5,000 events (the census stopped there); over-age behaviour is inferred
  from the zip's bytes, not exercised.
- IRPT_FNTEND's halves of FWD-1, 3, 4, 5, 8, 11 were not graded here.
- Several S3 reads timed out and were retried; every figure above is from a read that completed.

-- prepared for 3.0.0_SA_CVO, read-only
