# Outcome -- E3, the Multi-Comp arm on the st9 resident (2026-10-01): the job is READY and traces clean; E2 saved nothing

**Author and operator:** `2.0.0_SA_COO~Y`. **Packet:** `WINDOW_PACKET_E3_MULTICOMP_20261001.md`, both halves
@ac3444aec5 (pre-signature blob `3bb44f8e03`). **Ledger:** `irpt-e3-multicomp-20261001`.

## Conclusion

1. **The Multi-Comp job is READY**: `REQ-a1d9abc0bc037ea3d9e4a7ed`, Cottonwood, report
   `RPT-4acc921aa79afda98766192d4803f551`, variant `multicomp` (template 14141847), comparisons `opal_short_term` and
   `opal_intermediate_term`. Case trace: 22 links, 20 MATCH, 0 MISMATCH, 2 not evaluated (the page and the export,
   which are other seats' reads). It is NOT called live here: the CTO half's item 3 reserves that for the grade of
   `3.0.0_SA_CVO` and the page walk of `2.0.0_SA_COO~D`.
2. **E2 did not do what it was built for.** The job took 19 minutes 53 seconds from the K5 POST to the chain's READY
   read and used three receives. The same measure on st8 (`REQ-a69e5751d42c374f1d2354f9`, an Overview) was 16 minutes
   42 seconds and two receives. The second receive, 122 seconds after the first, was challenged on its FIRST
   request, before the status read was reached.
3. **The premise E2 rested on is falsified.** E2 assumed the second status GET of a receive draws the challenge. Today
   the request after a job's first status read was challenged whatever it was: a status GET 15 seconds later (3 of 3
   jobs on st7 and st8) and a report-template GET 122 seconds later (1 of 1 on st9). A request about 900 seconds
   later was answered in 4 of 4. The cause is not read; what is measured is a span after the first receive, longer
   than 122 seconds and not longer than about 900, in which the next request is challenged.

## The legs

| leg | when (UTC) | result |
|---|---|---|
| P, one liveness GET | 15:15:41 | `PROBE_VERDICT=LIVE` (HTTP 200, JSON, no WAF action; stored session fence 21, stored 08:21:20Z). `LEG_P_OUTPUT_20261001.txt` |
| S, operator sign-in | -- | NOT RUN (P read LIVE). Sign-ins in this window: 0. The stored session's `LastChangedDate` after the window is still 2026-10-01T08:21:20Z |
| J, the attempt | 15:16:26 to 15:36:32 | one login to Opal (200); ONE K4 POST 200, upload `NORMALIZED` at 15:16:33 (the resident's `RESOLVE state=READY code=-` at 15:16:32, first receive); ONE K5 POST 200 `QUEUED` at 15:16:39. 3 POSTs in the call log, no retry. `E3_multicomp_cottonwood.json` |

## Every receive of the job (the st9 half's item 1)

Resident journal, unit `irpt-analysis-resident`, pid 380185, root `481166a8f2-st9`. The job row's `fence_token` ends
at 3 and its intents carry fence 1 (upload, creation) and fence 3 (report creation); fence 2 for the middle receive is
inferred from that, not printed.

| receive | time | what the vendor answered | what the worker did |
|---|---|---|---|
| 1 | 15:16:41 to 15:16:47 | holdings upload claimed 15:16:41, portfolio creation 15:16:43 (job row intents); then the ONE status GET: `step=read_back status=200 portfolio_status=calculating source=status polls=1 wall_s=1.5` | `retained_for_retry class=ReadBackPending code=READ_BACK_PENDING:CALCULATING`; the message came back 122 seconds later, so the 120-second visibility took effect |
| 2 | 15:18:49 | `step=template status=202`: the receive's first request, the report-template GET, drew a WAF action. The status read was not made | `code=READ_BACK_PENDING:WAF_CHALLENGE`; the message kept the receive's 900 seconds |
| 3 | 15:33:55 to 15:36:10 | 906 seconds later: `READ_BACK_DONE step=read_back status=200 portfolio_status=available source=saved_portfolio polls=1 wall_s=3.7 tolerated=level_as_of_type=custom_date`; report creation claimed 15:33:57; PDF retrieved 15:34:42 | `TOLERANCE_TYPE type=Static as_of=Custom name=whole`; certified and published; `POLL handled=1` at 15:36:10 |

No dead-letter, so no redrive was made. Both queues read 0/0 after the job.

## Against the packets' stops

- The st9 packet, section 3, third outcome, in my words there: "the single GET of the second receive is challenged ...
  the message waits out 900 s as today and the job finishes at the third receive; E2 is then withdrawn". That is what
  happened, with one correction to my own table in that section: it said the next receive "makes one status GET". The
  receive makes the report-template GET first, and that was the request challenged.
- The CTO's condition reads "if the single status read of a later receive is challenged, E2 is withdrawn". The status
  read of the second receive was never made. Whether the condition is met is the CTO's reading, not mine; the
  measured effect is the one the condition exists for.
- st9 against st8 on this evidence: the same one challenged request per job, about 2 minutes slower, one more of the
  queue's five receives used. Nothing else differs.

## The Multi-Comp variant on served code (first time today)

- The printed-type check read this job's own row with its name WHOLE (the Overview's row was cut by the vendor; this
  template prints it in full); no refusal, so no PDF was kept outside the artifact store.
- Certification and publication of a Multi-Comp PDF passed: retained PDF 865,346 bytes, sha256 `cf2aeb74c2c889ba..`;
  certification `297c96e94552231b..`; report revision `ad7751ad2f002df8..`.
- Case trace (`CASE_TRACE_20261001.json`): the variant is the recipe's for two comparisons; each key's frozen identity
  equals the catalogue's (`P:1728415`, `P:1728315`); of the catalogue's portfolios the PDF prints exactly the two
  chosen (each on 17 pages); saved-portfolio settings 7 of 7 with the one tolerated row; 100 sections, 98 scalar
  values re-read at their own page and coordinates 98 of 98, 2 charts.
- Status route as the service principal (`STATUS_ROUTE_READ_20261001.json`): with the dates capability header
  `READY / ANALYSIS_READY`; without it `UNAVAILABLE / ANALYSIS_STATUS_DATE_BASIS_UNAVAILABLE`, which is the contract
  (E1, withdrawn); the sections route serves the document. `DOCUMENT_VERDICT=SERVED`.

## Values

Each output file was read for token, cookie and password shapes before commit: 0 of each in the leg P output, the
call log, the status read and the case trace. No PDF is in the repo.

## Not claimed

- Why the challenge falls where it does. Two readings fit all four jobs and are not separated by today's evidence: a
  span of time after the upload and portfolio creation, or something the first receive's requests set that clears
  later. One attempt with a release between 122 and 900 seconds would bisect the first.
- That the page renders this report (the walk is asked of `2.0.0_SA_COO~D`) or that its content is right as a product
  (the grade is `3.0.0_SA_CVO`'s).
- Any comparison of Multi-Comp against Overview run time: one job of each.
