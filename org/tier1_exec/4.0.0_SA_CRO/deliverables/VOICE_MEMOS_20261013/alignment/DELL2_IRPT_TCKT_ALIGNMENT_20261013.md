# DELL2 alignment -- Andrew's voice memo of 2026-10-13 vs the dell2 projects (Investor Reporting + Ticket Center)

Audience: Andrew Berman and the laptop CTO. Read-only report. As of 2026-10-13 ~15:3xZ. Workspace HEAD read: box/laptop @9aa0e9523a.
Portal refs read: origin/DEV f6ef1d25 (2026-10-13 13:39Z) and origin/PROD 15c97549 (2026-10-13 15:04Z), both local remote-tracking
refs (last fetch time not read).

**Conclusion.** IRPT_ANLREQ's charter already describes Andrew's workflow, and its C-ABSORB contract already pulls in the
other three projects' parts. No hop has run end to end. The block is not a missing project. It is four joins that no
active cell is cutting:
1. the producer allow-list routes every ticket-filed request to the stopped YCharts path;
2. the form's "Add commentary" box never reaches the flag that starts the drafter;
3. the ticket and the analysis request do not reference each other for a partner-firm filer;
4. every lane waits on one Opal-staff test filing, and Andrew says Opal staff do not use the Ticket Center.

---

## 1. What Andrew asked for (ranked)

Source: `org/tier1_exec/4.0.0_SA_CRO/deliverables/VOICE_MEMOS_20261013/DELL2_IRPT_TCKT_REVIEW_TRANSCRIPT.md` (auto-transcript, line 11).

**P1, the singular priority: one programmatic Analysis Request workflow, end to end.**
- Priority: "the singular priority for this device, is to establish a programmatic method for a single workflow" ... "we need
  to get this done immediately" ... "putting all resources towards getting this done" ... "Any blockers in the way of that
  need to be [...] cleared" ... "that needs to be put on speed mode".
- The form:
  - Variant: "is it going to be an overview, variant one, ... a direct comparison variant two or a multi comparison variant three".
  - Models and tickers: "an Opel model, which should be selectable. I would suggest using a check box" and "some kind of
    ticker fill in for others like SPX".
  - Upload: "that same CSV that's uploaded there [the Investor Reporting analysis tab], we just need to port all of that".
  - Firm: "based on the user's domain ... we already know who it's for ... they don't need to fill that out". He also said
    "an Opel user would never use the ticket sensor".
- Automatic chain: "when the analysis request comes in ... it should automatically run that report generation and automatically
  sequence behind it and run the investor commentary".
- The deliverable has four attachments on the open ticket: "they should see the CSV or XLSX that the advisor uploaded. They should
  see the form ... the generated report that we built internally based off the YTrots report. And they should be able to see
  the commentary that we AI generated."

**P1b, the commentary hop inside P1 (NFRA_TRNSPT):** "This project should not even be hard" ... "putting an AI layer on the
output of the YCDGEN" ... "We don't want to overly complicate this" ... "I would recommend using Astra for this personally".

**P2, IRPT_DASHBD (high, but below P1):** "decide what the default performance report is going to look like and what
information is going to have" ... "use the templates that we took from 49 ... those were sent last week ... see what state
that is in".

**P3, everything else on the box:** "backfill solutions and analysis and ... whatever else is on this box. But the point is that
these functions are priority."

---

## 2. Workflow hop table

| hop | what Andrew wants | what exists today (path; live or not) | owner project | gap |
|---|---|---|---|---|
| 1. Form fields | Variant 1/2/3; Opal models as checkboxes; free tickers; firm from the login, no picker | EXISTS. `portal/src/pages/TicketCenter/AnalysisRequestParts.tsx` (origin/DEV): report type Overview / Comparison / Multi-Comp (`analysisRequest.ts:54-63`); model checkboxes from the served comparison catalogue (`:114`); "Other ETFs" field resolved against the catalogue, max 5 comparisons (`:124`, `analysisRequest.ts:215-230`); "Add commentary" checkbox (`:134`); advisor, household, fee, needed-by. Server type: `infra/aws/lambda/ticket_center/lambda_function.py:98-125`. Firm: auto-selected and locked when the caller has exactly ONE allowed firm (`chosenFirm` `:67-70`, select disabled `:96`); Opal staff get a picker of all READY firms (`TicketCenter.tsx:81-105`). The file is also on origin/PROD. | TCKT_VNEXT / IRPT_ANLREQ (both write it) | Close to spec. A multi-firm user still sees a picker. The staff picker serves a persona Andrew says does not file. Variant is inferred from the number of comparisons on the one-step path (`reportTypeForKeys`, `analysisRequest.ts:251`), not taken from the select. Typo-check and swap (ANLREQ FWD-2) are partial: an unknown ticker is refused in words, and the backend swap is unverified (`KIMI_WEB_SEARCH_UNVERIFIED`, ANLREQ PRD section 6 row 4). |
| 2. Upload | The same CSV/XLSX format as the Investor Reporting Analysis tab | EXISTS, LIVE. The form posts .csv/.xlsx up to 1 MB through the SAME Analysis upload door (`analysisRequest.ts:5-9`, `uploadAnalysisInput`; backend `infra/aws/lambda/investor-reporting/intake/uploads.py`). A ticket is created only on NORMALIZED. Release 20 is live in all eight packagers (`CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` s1). | IRPT_ANLREQ (`~Y2`) | Effectively met. Rounds 10-21 went to hardening this reader (box report, IRPT_ANLREQ block). |
| 3. Ticket -> report trigger | Filing the ticket starts generation automatically | EXISTS ON DEV, IN THE BROWSER. `fileAndRequestAnalysis` (`analysisRequest.ts:304-322`, origin/DEV) runs upload -> create ticket -> POST analysis with `ticket_id` -> record the request id on the ticket (`POST /tickets/{id}/report`, `lambda_function.py:1381`, the "one-step filing"). NOT ON PROD: origin/PROD `analysisRequest.ts` has 0 occurrences of `fileAndRequestAnalysis`. | TCKT_VNEXT + IRPT_ANLREQ | (a) No server-side orchestrator. If the record step fails, the ticket stays filed with no report (stated in the code). (b) The route table admits only internal humans and named services to CREATE and REPORT; partner-firm humans reach only SUBMIT (`lambda_function.py:8-17`). Whether a partner-firm advisor's filing gets its request id onto the ticket is NOT READ (`src/api/endpoints/tickets.ts` unread). This is the mutual-reference gap below. |
| 4. Report generation | The internal YCharts-style report (YCDGEN) runs on the ticket's inputs | Opal engine EXISTS but is SWITCHED TO ANDREW ONLY. The resident release st32 has been on the runner host since 2026-10-11 (box report, YCDGEN block). C-SWITCH picks the producer by signed-in principal from an allow list that ships with Andrew's sign-in only; every other principal takes the YCharts path (`IRPT_YCDGEN_PRD.md` C-SCOPE/C-SWITCH; test `ycharts/generate/tests/test_resident_worker.py:769`, `..._shipped_allow_list_is_andrews_sign_in_only_and_the_other_principal_takes_ycharts`). The YCharts path is stopped: the 2026-10-11 fifth run failed NO_AUTHENTICATED_PROBE (@77f135f74f). The vendor firewall challenge is on record for the 2026-10-04 runs and recurs on the 7th request of any run (`IRPT_YCDGEN/surprise-channel/investigations/INVESTIGATION_v1.md` rows S3, S6). YCDGEN FWD-1 NOT MET and not run (`CTO_ROUND_ANALYSIS_IRPT_YCDGEN_ROUND_17_20261011.md` s1). | IRPT_YCDGEN (`~G2`) | A ticket-filed request today goes to a producer that cannot run. The fix is Andrew's word to add the ticket path's principal (`svc-irpt-analysis`, `IRPT_YCDGEN_PRD.md:248`) to the allow list. CONTRADICTION: IRPT_ANLREQ FWD-7 says "no YCharts call end to end", while YCDGEN keeps YCharts as the default producer until its own FWD-11. |
| 5. Commentary | AI commentary runs automatically after the report | BUILT, LIVE, NEVER FIRED. Drafter `data/transcripts/scripts/commentary/lambda_handler.py` takes `analysis_ready`. All three functions are on one digest and the route is at the front door, with 0 drafts posted (`CTO_ROUND_ANALYSIS_NFRA_TRNSPT_ROUND_24_20261012.md` s1-2). READY sends `analysis_ready` only for a request with a ticket id AND `commentary_requested` exactly true (@dddafd6832; `ycharts/generate/tests/test_ready_signal_commentary_gate.py`); acceptance copies the member (`ycharts/generate/acceptance.py:138-139`). Ticket routes `/commentary-draft` and `/commentary-sent` are live (`lambda_function.py:21-24`, @220e5ef457 2026-10-11; deployed bytes equal the source map at 12:45Z today per the box report). Model: Kimi K3 under the standing word C-KIMI. | NFRA_TRNSPT (`~T2`), absorbed by IRPT_ANLREQ C-ABSORB (c) | (a) THE FLAG NEVER LEAVES THE FORM. "Add commentary" is stored as the ticket answer `add_commentary`, but the analysis body the form posts has no `commentary_requested`: 0 occurrences in origin/DEV `analysisRequest.ts`; only the wire type `AnalysisSubmissionRequest.ts` has it. ANLREQ left this un-cut, waiting on IRPT_BCKEND's release, which waits on Andrew's sitting or allow-list word (ANLREQ PRD ADDENDUM v0.4 enrichment item 5). (b) The draft route needs the ticket's `report_ref.request_id` to equal the request's. Of 27 tickets, 3 carry a `report_ref` and none forms a usable pair, so TR-dp-24 is PARKED (`NFRA_TRNSPT/deliverables/2.0.0_SA_COO~T2/R24_TR_DP24_CANDIDATE_READ_20261012.md` @022d5eb3b4). (c) Andrew prefers "Astra"; the build uses Kimi. |
| 6. Attachments on the open ticket | Four items on the open ticket: upload, form, report, commentary | ROUTE LIVE, NEVER EXERCISED. `POST /tickets/{id}/package` records pointers by ONE principal, `svc-irpt-packager`, firm-bound (`lambda_function.py:18-20, :120, :1462`). The ticket page opens four kinds: report, pdf, commentary, original (`AnalysisRequestParts.tsx:236-241`). ANLREQ FWD-1 has never run live (box report). | IRPT_ANLREQ (C-PACKAGER) | 3 of Andrew's 4 map to a package kind (original upload, report, commentary). "The form" is the ticket's own answers, not an attachment. Whether the ticket page renders the answers as a readable form was not read. ANLREQ defines the package as report + branded PDF WITH commentary + original Excel, which is not Andrew's four separate items. |
| 7. Staff see it in the open queue | Opal staff see new requests among open tickets | EXISTS, LIVE: `GET /api/scoped/tickets` for internal humans (`lambda_function.py:10`). The C-FENCE firm refusals are live (box report, TCKT_VNEXT block). | TCKT_VNEXT | None. |

---

## 3. Project table

Box status report (CRO rec column) = `C:\Users\AndrewBerman\Desktop\today_report\BOX_STATUS_REPORT_dell2_20261013.md`, written by
the dell2 CRO, as of 13:20Z. A copy is in `org/tier1_exec/4.0.0_SA_CRO*/deliverables/`. Its rows match
`AGGREGATE_4_of_4_20261013.txt` lines 20-29.

| project | Andrew's intent (memo) | chartered outcomes | delivered / live (evidence) | coverage | CRO rec | recommended move |
|---|---|---|---|---|---|---|
| IRPT_ANLREQ | The whole P1 workflow | PRD v0.4 FWD-1..7. FWD-1 = form to finished package on the same open ticket, no person in between. C-ABSORB moves in YCDGEN (engine), TRNSPT FWD-10/11 (commentary) and TCKT's analysis scope (`IRPT_ANLREQ_PRD.md:98`) | 0/7 REALIZED. 21 rounds; FWD-1 never run live. Release 20 (reader) live 2026-10-13. Round 21 is reader r19.3, a CI script fix and a status-rule exercise (`CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_21_20261013.md` s3), none of them a journey hop | COVERED on paper, NOT delivered. Partly CONTRADICTED: (a) FWD-1's driven arm needs an Opal staff filing (open call 2e30), while Andrew says Opal users never file; (b) the package is 3 items with commentary inside the PDF, while Andrew asked for 4 separate items | KEEP | KEEP + REPOINT: FWD-1 becomes the only open thread. Stop reader rounds. Drive FWD-1 with a synthetic partner-firm advisor identity under a never-widen pair (precedents: TCKT_VNEXT R2-cw-1 crawl identity; ANLREQ round 21 synthetic identities). Cut cells for joins J1-J3 (section 4). Amend FWD-1's package to Andrew's four items. |
| TCKT_VNEXT | The ticket form and the attachments | PRD FWD-1..9 (box report: v0.4). FWD-1 = an Opal person files with a holdings file and opens the report from the ticket | 0/9. C-FENCE refusals live (rounds 7, 9). Two test tickets closed today. Round 16 cut nothing; "the next act is still a person's" (`CTO_ROUND_ANALYSIS_TCKT_VNEXT_ROUND_16_20261013.md` s3). FWD-1 not run since round 6 | PARTLY | MERGE_INTO:IRPT_ANLREQ | MERGE_INTO:IRPT_ANLREQ (agree), on one condition: the ticket-side joins (report-ref recording for a partner-firm filer; package principal) move over as named cells, not as history. Both projects already write `portal/src/pages/TicketCenter/` and `ticket_center/lambda_function.py` (box report). |
| IRPT_YCDGEN | Hop 4: the internally built report, run automatically from the ticket | PRD v0.13 FWD-1..23. FWD-1 = Andrew himself submits one real portfolio and opens an Opal Overview. C-SWITCH: Opal engine for Andrew only until FWD-11 | 0/22 (box report). st32 on host. The ticket-gated worker is merged but dormant (@dddafd6832). No Opal report has reached Andrew. Round 17 cut nothing, with PART 2 behind four other projects' changes (r17 analysis s3) | PARTLY, and CONTRADICTED on routing: the memo wants ticket filings to run it; C-SWITCH sends them to YCharts | KEEP narrowly, then PARK after the W312-S3 release | REPOINT, then MERGE_INTO:IRPT_ANLREQ (C-ABSORB (b) already says "IRPT_YCDGEN whole"). Change FWD-1 from "Andrew's sitting" to "the ticket-filed Overview". On Andrew's word, put the ticket path's principal on the C-SWITCH allow list. Keep `~G2` seated through the first ticket-filed report. |
| NFRA_TRNSPT | Hop 5: "an AI layer on the output of the YCDGEN"; "should not even be hard" | PRD FWD-1..11. FWD-1..9 = the transcripts/mail database; FWD-10/11 = the commentary drafter and its ticket | 2/11 (FWD-4, FWD-7). Hourly transcript pull landing unaided. Drafter live, 0 posts. TR-dp-24 parked on the ticket/request pair (@022d5eb3b4) | Commentary: PARTLY (built, never fired; the trigger flag is never set). Database: outside the memo's P1 | PARK | REPOINT (CONFLICTS with the CRO PARK). Split it. The commentary workstream (FWD-10/11) stays seated as IRPT_ANLREQ's `~T2` lane (C-ABSORB (c)). The database workstream (FWD-1..9) parks with its pulls still firing. Parking the seat stalls hop 5 of P1. |
| IRPT_DASHBD | P2: the default performance report, starting from the 49 Financial templates | PRD v0.11 FWD-1..20. FWD-12 = one advisor's quarter-end reports. FWD-14 = each firm's reports in its own template (merged from IRPT_CUSTDY 2026-10-09). No FWD is called "default performance report" | 0/20 (INFERRED, box report). Gold Lambda release today, ledger L7 open until the 2026-10-14 fire. FWD-1 measured 5,288 ms against a ~2 s target. The 49 Financial template was built in IRPT_CUSTDY: TO-CU-a-4 (template data fixture `data/assets/scripts/gold/irpt_custody/tests/fixtures/report_template_firm_a.json`, complete 2026-10-07) and TO-CU-e-2 (portal `ClientReportDocument` print document, complete 2026-10-07). `ClientReportDocument` is on portal origin/DEV and origin/PROD; IB-pr-356 (2026-10-09, portal 32e34d59) mounts the retained custody report on the print page | PARTLY | KEEP | KEEP + REPOINT: add one outcome, "the default performance report", whose starting layout is the IRPT_CUSTDY 49 Financial template. Name the template's approver; C-TEMPLATE leaves "who approves a template" OPEN at Andrew (`IRPT_CUSTDY_PRD.md:110`). |
| IRPT_BCKEND | Not named. Supporting backend; its release gates the commentary flag | PRD v0.53, 13 FWDs | 0/13 after 178 rounds. Two open orders (holdings apply, a parked read) (box report) | Supporting | KEEP | KEEP + REPOINT its next cell to the ONE release P1 needs: the submission/acceptance half of YCDGEN PRD v0.13 (carries `commentary_requested`), ahead of other enrichment. |
| DSGN_IRPTV1 | Not named (P3) | FWD-1..23, page remediation | 0/23. 0 open orders. Waits on `account_id` and the PROD promote | NOT COVERED by the memo | PARK | PARK (agree). |
| NFRA_OPSWKF | Not named (P3); it shares the Ticket Center | FWD-1..10, trade submission | 3/10. Unseated. Waits on Andrew's sitting with the operations lead | NOT COVERED | PARK | PARK (agree). |
| ADVI_BILLING | Not named (P3) | FWD-1..6 | 1/6. Unseated since 2026-10-09 | NOT COVERED | PARK | PARK (agree). |
| ADVI_COTBKF | "backfill solutions" ranked below P1 | FWD-1..9 | 5/9. Seated `~C2` today on Andrew's card 6, "We have the room to do this, yes" (`ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`) | NOT COVERED by P1 | PARK | PARK after the round-80 drain, unless Andrew confirms card 6 still holds against "all resources" (question 6). |
| IRPT_CUSTDY | (template source for P2) | merged into IRPT_DASHBD FWD-12..14 | status closed (project.json) | n/a | (laptop aggregate: CLOSE) | CLOSED already; nothing to do. |

**Where the memo conflicts with the dell2 CRO's recommendations:**
1. **NFRA_TRNSPT PARK.** Andrew names the commentary as part of the top workflow ("automatically sequence behind it and run
   the investor commentary"). A seat park stalls hop 5, including TR-dp-24 and the flag wiring. Park the database
   workstream only.
2. **IRPT_YCDGEN "park after the W312-S3 release".** The engine is hop 4, and the C-SWITCH change plus the first
   ticket-filed run still remain. Parking it then removes the hop's only owner before the hop works.
3. **IRPT_ANLREQ KEEP, which names Andrew's staff filing (2e30) as the FWD-1 blocker.** The memo says Opal users would never
   use the Ticket Center. The test persona should be a partner-firm advisor, and an agent can drive that (rule 27, "NO FWD IS
   A WAIT").
4. **ADVI_COTBKF PARK** agrees with the memo's ranking but conflicts with Andrew's card-6 seating word from earlier today.
5. Consistent: the TCKT_VNEXT merge (with the condition above), IRPT_DASHBD KEEP, and PARK for DSGN_IRPTV1, NFRA_OPSWKF and
   ADVI_BILLING.

---

## 4. Gaps no project owns (the joins)

| id | join | why it is orphaned (evidence) | proposed owner |
|---|---|---|---|
| J1 | Form "Add commentary" -> `commentary_requested` on the analysis submission | Not on any lane's open order: ANLREQ's ADDENDUM v0.4 item 5 left it un-cut, behind IRPT_BCKEND's release, which waits on Andrew. Without it the built drafter never starts for a ticket filing (READY gate @dddafd6832) | IRPT_ANLREQ `~Y2` (form) + `~P2` (the one acceptance release) |
| J2 | Ticket <-> analysis request mutual reference for a PARTNER-FIRM filer | REPORT and CREATE admit internal humans and named services only (`lambda_function.py:8-17`). Every test plan so far uses an Opal staff filing (2e30). TR-dp-24 parked for exactly this (@022d5eb3b4). The advisor path's recording step was not read | IRPT_ANLREQ (absorbing TCKT_VNEXT `~V2`) |
| J3 | Producer selection for the ticket path | C-SWITCH is YCDGEN's. FWD-7 "no YCharts" is ANLREQ's. Neither has cut the allow-list change, which needs Andrew's word (`IRPT_YCDGEN_PRD.md:248`; r17 analysis s4) | Andrew's word, then IRPT_YCDGEN `~G2` |
| J4 | Orchestration is in the browser and on DEV only | `fileAndRequestAnalysis` runs client-side. PROD lacks it (origin/PROD 15c97549). No server-side step retries generation after a failed POST (FWD-4 only requires naming the failure) | IRPT_ANLREQ (decide: keep client-side for v1, or move to the submit path) |
| J5 | Packager run after the commentary (`svc-irpt-packager`, package poll) | Built and tested (`ycharts/generate/tests/test_package_poll.py`); live wiring not read; never exercised | IRPT_ANLREQ C-PACKAGER |
| J6 | "The form" as the 4th attachment | No package kind for it. Answers live on the ticket record | IRPT_ANLREQ (portal ticket page) |
| J7 | Commentary model | C-KIMI (Kimi K3) is wired; Andrew prefers "Astra" | Andrew (question 3) |

---

## 5. Fast defined outcomes (speed mode)

**O1. One synthetic partner-firm advisor files one Analysis Request on portal DEV. With nobody touching it, the open ticket
shows the advisor's upload, the form answers and an Opal-generated Overview report.**
- Missing:
  - Andrew's C-SWITCH word for the ticket path (J3);
  - the report-ref recording for a firm filer (J2);
  - a never-widen pair minting and deleting the synthetic advisor identity (R2-cw-1 precedent).
- Owner: IRPT_ANLREQ `~Y2` as the one driver, with `~V2`'s ticket work merged in and `~G2` on the engine.
- Proof: one ticket read showing `report_ref` set and the report opened from the ticket page.

**O2. The same ticket gains the AI commentary draft automatically, with no action after filing.**
- Missing:
  - the form sending `commentary_requested` (J1);
  - IRPT_BCKEND's acceptance release;
  - TR-dp-24 driven on O1's ticket.
- Owner: IRPT_ANLREQ `~T2` (the commentary workstream, kept seated), plus `~P2` for one release.
- Proof: the `COMMENTARY-POST` line, the route's 200, and the draft visible on the ticket.

**O3 (P2). The IRPT_DASHBD default performance report: one 49 Financial account rendered in the IRPT_CUSTDY-built 49
Financial template from Opal gold, read by Andrew.**
- Missing:
  - the outcome itself (no FWD names it);
  - Andrew naming which "templates sent last week" he means, and who approves.
- Owner: IRPT_DASHBD `~D2`, after the 2026-10-14 ledger read.

---

## 6. Resourcing

- **Seats live on dell2 at 13:00Z: 15** (box report). MSTR 1, CTO 1, CVO 1, CRO 1, COO 7, CloudOps 4. The COO and CloudOps
  seats map to projects as follows:

  | seat | project |
  |---|---|
  | COO `~Y2` | IRPT_ANLREQ |
  | COO `~V2` | TCKT_VNEXT |
  | COO `~G2` | IRPT_YCDGEN |
  | COO `~T2` | NFRA_TRNSPT |
  | COO `~P2` | IRPT_BCKEND |
  | COO `~D2` | IRPT_DASHBD and DSGN_IRPTV1 |
  | COO `~C2` | ADVI_COTBKF |
  | CloudOps `~AQ2`, `~YC2` | IRPT_ANLREQ |
  | CloudOps `~TV2` | TCKT_VNEXT |
  | CloudOps `~IB2` | IRPT_BCKEND and IRPT_DASHBD |

- **P1 already holds 4 of 7 COO seats and 3 of 4 CloudOps seats.** The shortfall is direction, not headcount:
  - ANLREQ rounds 10-21 hardened the reader;
  - YCDGEN round 17 cut nothing;
  - TCKT_VNEXT round 16 cut nothing;
  - TRNSPT TR-dp-24 is parked;
  - three of them wait on the same human act (open call 2e30).
- **Account:** dell2 runs on a fresh account after the first account's weekly limit. The limit and the Oct 17 reset are
  recorded in "fc10 addendum 1" (box report line 31; that record was not read). Seat health was INFERRED from heartbeats, and
  usage was not measured. With a fresh weekly budget, seats outside P1 cost against P1.
- **Recommendation for "all resources toward this":**
  - Keep `~Y2` (driver), `~G2` (engine), `~T2` (commentary only) and `~AQ2`/`~YC2`.
  - Fold `~V2`/`~TV2` into ANLREQ (the merge).
  - Point `~P2` at the one acceptance release before other BCKEND work.
  - Keep `~D2` on IRPT_DASHBD (P2).
  - Drain and park `~C2`.
  - This is about 4 COO seats on P1 instead of 4 COO seats waiting on P1.

---

## 7. Questions only Andrew can answer

1. **Should the ticket path use the Opal engine now?** This puts the Ticket Center's service principal on the C-SWITCH allow
   list (`IRPT_YCDGEN_PRD.md:248`). Rec: YES for ticket-filed requests only. The YCharts path is stopped, so without this no
   ticket can produce a report.
2. **May an agent drive the FWD-1 test as a synthetic partner-firm advisor**, minted and deleted under a never-widen pair, in
   place of your Opal-staff filing (2e30)? Rec: YES. It matches "an Opel user would never use the ticket sensor" and removes
   the one wait three lanes share. Keep your own filing and the advisor's organic request (3cb1) as the organic arm.
3. **Commentary model: Kimi K3 (wired, standing word C-KIMI) or "Astra"?** Rec: ship O2 on Kimi now and switch the model as a
   one-setting change after the first draft lands. Please also name what "Astra" refers to.
4. **Attachments: four separate items (upload, form, report, commentary), or ANLREQ's branded PDF with the commentary
   inside?** Rec: four separate items as you said. The branded PDF can come later.
5. **"The templates we took from 49 ... sent last week": the IRPT_CUSTDY-built 49 Financial template (2026-10-07), or files
   the firm sent?** Also, who approves a template (C-TEMPLATE OPEN)? Rec: start from the IRPT_CUSTDY template and name one
   approver at the firm.
6. **ADVI_COTBKF: does card 6 ("we have the room") stand against "all resources toward this"?** Rec: drain round 80, then park.
7. **Portal PROD:** the one-step filing is on DEV only. Rec: smoke and promote only after O1 passes on DEV (a client-facing
   page, so your word is needed).

---

## 8. Method

**Read, with paths:**
- The transcript (in full).
- 52 of 52 `org/missions/D*/*/*/project.json`, scanned. 11 carry placement DELL2: 10 active, plus IRPT_CUSTDY closed.
- The full project.json for the 10 active projects.
- The dell2 box status report and the AGGREGATE_4_of_4 dell2 rows (Desktop `today_report`).
- PRDs:
  - IRPT_ANLREQ PRD lines 1-260 (ENDPOINT, C-ABSORB, ADDENDUM v0.4);
  - TCKT_VNEXT PRD section index;
  - IRPT_YCDGEN PRD FWD list and C-SWITCH;
  - IRPT_DASHBD PRD FWD list and FWD-12..14;
  - IRPT_CUSTDY PRD C-SHAPE/C-TEMPLATE.
- CTO analyses:
  - IRPT_ANLREQ round 21;
  - TCKT_VNEXT round 16;
  - IRPT_YCDGEN round 17;
  - NFRA_TRNSPT round 24 (s1-5).
- `ANDREW_DIRECT_20261013_122xZ_ANSWERS_TO_NINE_DELL2_CARDS.md`.
- `R24_TR_DP24_CANDIDATE_READ_20261012.md`.
- Code:
  - `infra/aws/lambda/ticket_center/lambda_function.py` (routes, type definition, report_ticket);
  - portal origin/DEV `TicketCenter/analysisRequest.ts` and `AnalysisRequestParts.tsx` and `TicketCenter.tsx` (by grep);
  - origin/PROD presence checks;
  - `investor-reporting/ycharts/generate` (by grep).
- Three IRPT_CUSTDY task orders (status and template lines).
- `git log -4` per code for the five named projects.
- One live read: a mailbox search "49 Financial report template", which returned 10 messages, none about report templates.

**Denominators:**
- 52 project.json files.
- 27 tickets (from @022d5eb3b4, not re-read).
- 165 IRPT_DASHBD order files (26 mention FWD-12..14).
- 201 commits on origin/DEV not on origin/PROD.

**Not read, and why:**
- `portal/src/api/endpoints/tickets.ts`: decides J2 for a partner-firm filer; budget.
- Live Lambda or API state (0 AWS reads). Liveness is taken from the box report and the CTO analyses.
- The fc10 usage record.
- Whether the ticket page renders the form answers.
- The packager's live wiring.
- Whether open call e7f2 (PROD promote) closed with today's origin/PROD move to 15c97549.
- The drafter prompt's inputs, so whether transcripts feed it is unknown.
- TCKT_VNEXT PRD body beyond headings.

**Caveats:**
- Portal refs are local remote-tracking refs.
- Several fwd_realized figures are the box report's INFERRED values.
