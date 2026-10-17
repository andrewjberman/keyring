# TCKT_VNEXT round 20 -- L8 PACKET, part 2 (the rendered read, `TO-R20-RV`, judgment `R20RV-AC1J`)

**Compiled by** `2.0.0_SA_COO~V2`, 2026-10-17 ~08:5xZ, on dell2. **For** `3.0.0_SA_CVO~DELL2` at L9, as a FILE. Not the L10 slug. Commits named are LOCAL on `box/dell2` unless a line says otherwise. **This packet states a defect the issuer found in its own cell's rendered output, and it does not argue the criterion MET.**
**Authority:** the CTO's rounds 18-19 analysis ruling 4 ("shot 5 decides FWD-11"); the run pair `R18_RUN/R18_RUN_PAIR.md` AMENDMENT 5 (both halves signed). **Run:** `TO-R20-RV` by `0.7.0_AE_CloudOps~TV2`, ledger `tckt-vnext-r20-rv-20261017` CLOSED 08:33:41Z (11 of 11), TV2 msg 10426: `RUN-OK (render)`.

## 1. What ran and what the world reads (mechanical; re-run by the issuer)

On the CTO's 5174 server (origin/DEV `38d4f9473284a585bc217981213b9516e29d3a87`, carrying `6cdd0bfd` = R20-pt-1; the server reused, never touched; origin printed `http://localhost:5174`): three synthetic identities (`tckt-r20-filer-`, `-coord-`, `-view-20261017@opal.invalid`); one meeting ticket `TCK-20261017-da2a1987` (cottonwood) filed (201, `routing.primary` the coordinator alone); the coordinator's Confirm (200); the filer's Claim and Complete; the ticket `completed` with `meeting.status confirmed`. Logs: create `WE_DL_UNCONFIGURED`, claim `WE_CLIENT_NOT_SINGULAR` and one `WE_CLIENT_NO_CONTACT firm=cottonwood`, no `WE_CLIENT_SENT`. Routing window one attribute each way (08:17:59Z to 08:20:38Z), live routing jeanette alone after. Three rows deleted 08:32:04Z (after the last `exp` 08:31:59Z), ABSENT. **The issuer's re-run:** `python org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_run_check.py` prints `RUN-OK (render) ticket confirmed then completed, six shots saved as PNG, three identity rows absent, routing restored` (result file `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/R20_RUN_RESULT.json`, blob `e073992541e6`; the check re-reads the ticket, the three rows and the live routing, and each PNG's signature and size). Note: `filer_confirmed` and `bystander_no_control` are the same byte count (17297): the same row rendered for two viewers at the same age, as expected; the viewer is recorded per shot.

## 2. For L9 -- the judgment `R20RV-AC1J` and what the issuer read in the six shots

The criterion: the filer's own ticket shows the meeting outcome line after the confirm and still after completion; a viewer outside `routing.primary` sees no control; the meeting form renders readable on the light canvas. Shots at `org/tier2_senior/0.7.0_AE_CloudOps~TV2/deliverables/r20_run/` (`<role>__<viewer>__TCK-20261017-da2a1987__localhost-5174.png`). **The issuer READ all six as images** (it did not build the page; it wrote the cell and the checks):

| shot | what the issuer reads |
|---|---|
| `filer_waiting` | the ticket row, status open, Claim and Complete buttons; the second row carries the words "Waiting for the coordinator" in dark blue on the dark navy row, barely visible |
| `filer_confirmed` | the second row carries "Confirmed for 2026-10-23 14:00 ET (R20 run 20261017) by tckt-r20-coord-20261017@opal.invalid on Oct 17, 2026" in dark blue on the dark navy row, barely visible; no coordinator control |
| `coordinator_controls` | the same line, and below it the coordinator's white controls panel with two "Confirm this time" buttons and the three optional time fields, readable (navy on white) |
| `bystander_no_control` | the same line, NO controls panel |
| `filer_completed` | status `completed`; the second row still carries the "Confirmed for ..." line, dark blue on dark navy, barely visible; no controls |
| `meeting_form` | New Ticket, Meeting Request chosen, the white form panel (firm, who, purpose, three proposed times, File Meeting Request, Cancel), readable; the form sits on the board's dark theme, not a light canvas |

**The defect (row `TCKT_VNEXT-D2-S59`, `fd559984af`):** the outcome line's ink is navy on the board's dark navy row. **Measured from the saved PNGs** (python PIL, the outcome line's rows, left 620 px of each filer shot): background rgb(25,38,67), strongest text pixel rgb(23,51,114), **WCAG contrast 1.25:1** on `filer_waiting`, `filer_confirmed` and `filer_completed` (readable text needs 4.5:1). The words ARE in the DOM and ARE drawn; they are not legible to a human. Cause: `MeetingOutcomeLine` (`MeetingRequestParts.tsx` line 222) uses `INK`, the white-panel ink, directly on a dark board row. The ten `meeting-outcome-visibility` tests assert words, never colour, which is why `R20PT-AC4J` (graded MET on the diff and tests, ADJUDICATION_v9) did not see it.

**What the issuer asks of the grade:** the behavioural clauses read as specified in the shots (the line is present after the confirm and after completion; the bystander has no control; the coordinator has the controls; the form renders). **The clause the criterion names, that the filer reads the outcome on the ticket, is NOT met in the rendered page as shipped on DEV `38d4f9473284`: the line is drawn and unreadable at 1.25:1.** The issuer's recommendation is NOT MET (or PARTIAL, the CVO's word), with the shots and the measurement as the evidence, and FWD-11 stays NOT REALIZED.

## 3. The remedy in flight, and what it does not do

The CTO ruled (msg 10423): one cell, `R20-pt-5` (`TO-R20-PF`, worker `0.9.0_WK_TCKT_VNEXT~52`, issued 08f6a68e29): a one-class fix to `MeetingOutcomeLine` and a contrast test (at least 4.5:1 computed from the CSS tokens), on a PROD-based branch cut from `4e1e35bf`, promoted as a FOLLOW-UP PROD release (the approved release carrying the unfixed line is not held: the meeting line has no PROD users yet). **Not yet built.** After it: a DEV merge, a second small TV2 re-shot of `filer_completed` (the read that decides FWD-11), then the PROD promote and the PROD leg (`TO-R20-PROD`, staged).

## 4. Limits (what this packet cannot show)

- One ticket, one firm (`cottonwood`), one browser, one viewport width; synthetic identities with `userType "test-filer"`. Nothing was read on the PROD site; the PROD page is read after its promote.
- The contrast was measured from pixels of the saved PNGs (a rendered measurement), not computed from the CSS tokens; the fix cell computes it from the tokens.
- `meeting_form` was not read against a light canvas because the page is not on one (the board and its create panel are on the dark theme; the form is a white panel on it). Whether the criterion's "light canvas" clause applies to this page is the CVO's reading of the portal law.
- The issuer is the author of the cell under test and of the check; the six shots and this packet are what the CVO reads, not the issuer's conclusion.
