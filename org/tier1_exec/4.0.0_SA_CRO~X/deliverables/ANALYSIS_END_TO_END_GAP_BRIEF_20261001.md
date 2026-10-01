# Investor Reporting Analysis (FWD-4 with its FWD-9 intake): end-to-end trace brief

**Author:** 4.0.0_SA_CRO~X (Chief Research Officer, lane X)
**Home:** org/tier1_exec/4.0.0_SA_CRO~X/deliverables/
**Asked by:** 1.0.0_SA_CTO, msg 103444, under the self-drive arming record @c48af273cc.

Prepared by 4.0.0_SA_CRO~X on 2026-10-01 (measured 04:31Z to 04:55Z). Read-only assessment plus proposed closure
requirements. No application change, no vendor call, no Lambda invoke, no deployment, no schedule activation, no
secret value read. Two read-only commands ran on the resident host through Systems Manager (ids in the evidence file).

## Design finding

The surface is meant to take a holdings list -- forwarded by email, or uploaded in the Analysis tab -- turn it into
one owned, firm-scoped request, run it through YCharts (upload, portfolio, report generation, PDF), certify sections
out of the vendor PDF, show them in the Analysis tab, and export an Opal-branded PDF. YCharts supplies every analysis
figure; Opal retains the input, the composition, the vendor PDF and the certified sections, and computes none of the
figures.

The upload lane is ONE hop from a live thread. Every hop from the tab's upload to a certified report has carried a
real request at least once (a Comparison on 2026-09-29, window 22). What stops it today is the YCharts session hop:
the last 3 of 3 jobs that reached the vendor died there, and the cause is not named. The email lane is further away:
its poller has never run, its mail credential does not exist, and no code consumes what the poller would emit. Both
ends of the output side are open: a READY report is not yet proven on the page, the vendor PDF cannot be opened, and
the Analysis export is refused by name.

A second finding cuts across every hop: the deployed bytes are behind the source. 42 module copies across five
deployed units (25 in three Lambda packages, 17 on the resident) are older than CLOUD, and several of them are the
fixes for failures already measured live.

## Current measurement

Read from DEPLOYED bytes. At 04:34:43Z the four packages on this surface were downloaded and each zip's sha256
equals the live CodeSha256 (4 of 4). All 11 `irpt-*` functions were re-read at 04:53Z: 0 digests moved. Every `.py`
and `.json` member was compared to CLOUD @b80543a03c; a module that differs was walked back to the commit it equals.

| Deployed unit | Live identity | Code modules behind CLOUD | What the unserved commits carry |
|---|---|---|---|
| `irpt-intake-poller` | `YpE2MyUw..`, 2026-09-11 | 0 of 6 | nothing; it equals source |
| `irpt-ycharts-generate` | `inrij6hL..`, 2026-09-29T15:00Z | 15 | the catalogue GET (IB-yr-261), correction words on the upload answer, allowedFirmIds at the served boundary (IB-pr-271) |
| `irpt-status` | `ZYr+IDMp..`, 2026-09-28T14:04Z | 7 | the CORRECT action words (IB-yr-241), NOT_READY for an absent report blob (IB-yr-282), IB-pr-271 |
| `irpt-export-render` | `BORQ2shb..`, 2026-09-28T12:51Z | 3 | IB-pr-271; a log-wording fix |
| resident `irpt-analysis-resident` on `i-0167fd745ad906a66` | root `/opt/irpt-resident/fe64236bbb-st5`, active since 2026-09-30T05:13:31Z, 0 restarts | 17 (92 own files listed) | allowedFirmIds in `decide()` (IB-yr-293), the terminal state for a permanent authority refusal (62535e0fdc), the vendor endpoint ledger (IB-yr-291) |

Other live state: `irpt-intake-poll` DISABLED (unchanged since 2026-09-11T01:53Z); 0 event-source mappings on any
`irpt` queue or function (6 in the account); `irpt-generation` 0 visible, `irpt-generation-dlq` 2 (baseline was 1);
`irpt-jobs` 17 rows in one page -- READY 5, ATTENTION 8, SUBMITTING 2, and 2 rows with no state; `ycharts/session/current`
last published 2026-09-30T04:58Z; 17 investor-reporting routes of 108 on API `7k3ed8px20`. The served portal at
`opalinvest.dev` was last written 2026-09-29T18:21:28Z, four minutes after PROD @ba8e971f was committed; it is taken
as that build by the time alignment, not by a byte comparison.

NOT invoked, and not claimed: any function, any vendor endpoint, the mailbox, a signed-in page. A configured endpoint
or a secret name is reported as configured, never as executed. Hop states that rest on another seat's live run cite
that run and its date.

The source map's `deployed_code_sha256` for generate (`Ldjdnn..`) and status (`pfAr3u..`) is stale against the live
digest; its `artifact_sha256` is current. The field is `2.0.0_SA_COO~P`'s.

Machine-readable evidence: `org/tier1_exec/4.0.0_SA_CRO~X/deliverables/analysis_trace_20261001/EVIDENCE.json`
(probes beside it: `member_census.py`, `behind_census.py`).

## Adapter map

| Lane | Provider and intended path | Existing work | Gap |
|---|---|---|---|
| Email intake (FWD-9) | Microsoft Graph delta read of the forwarding mailbox -> firm binding -> intake receipt -> request | `intake/poller.py` with checkpoint, outbox and gate, deployed and equal to source | no mail credential, schedule off, never run, and no consumer turns a receipt into a request |
| Upload (the tab) | `POST analysis/inputs` -> normalized input -> `POST analysis` | route, handler, parser, resolution, composition; exercised live | overlapping uploads exhaust the resolve retry; the served words still blame the file |
| YCharts generation | host capture -> `ycharts/session/current` -> resident replay: upload, portfolio, generate, PDF | resident, recipe, transport, read-back, certifier; one Comparison certified live | the session hop fails for an unnamed cause; Multi-Comp, Target Weight, 49 Financial and Inflection have no report |
| Opal output | `irpt-status` sections -> Analysis tab -> export | status and sections routes, native section rendering, the Performance export chain | a READY report unproven on the page; no PDF route; Analysis export refused |

One firm's success does not certify another's: every certified report so far is Cottonwood's.

## Start-to-finish walk

### 1. Forwarded email -> mailbox poller -- MISSING

What exists: `infra/aws/lambda/investor-reporting/intake/poller.py` (lease, delta walk, sender verification, firm
binding through `_gate`, persist-then-mark), deployed as `irpt-intake-poller` and byte-equal to CLOUD (6 of 6).
Configured: mailbox `opalbloomberg@opalinvest.com`, forwarder `requests@opalinvest.com`, secret id
`irpt/graph/app-registration`.

The exact gap: the secret `irpt/graph/app-registration` does not exist (ResourceNotFound; the positive control
`ycharts/session/current` is found). The schedule is DISABLED and unchanged since it was applied. The function has
0 log streams, `irpt-checkpoints` holds 0 items and `irpt-outbox` 0. It has never run.

Close: create the Graph application credential under the configured secret id (an act outside the fabric: the app
registration is Andrew's or IT's), then one driven poller invoke against one real forwarded message, proven by the
checkpoint row, the receipt object and one `irpt-intake` message.

### 2. Intake receipt -> an owned request the advisor can see -- MISSING

What exists: the poller's outbox dispatch of an id-only `irpt_intake_received` row to `irpt-intake`.

The exact gap: nothing reads it. 0 event-source mappings; the only `receive_message` in the investor-reporting tree
is the resident's, on `irpt-generation`; `irpt_intake_received` appears in `poller.py` and nowhere else. The poller's
own header says interpretation "is a later cell's". That cell is not in source.

Close: one consumer that takes a receipt, reads the retained attachment through the SAME parser and resolution the
upload uses (`intake/parse.py`, `intake/upload_resolution.py`), resolves advisor and client inside the bound firm, and
writes the same owned-request row hop 4 writes -- flagged for correction where it cannot read. Proof: the forwarded
message of hop 1 appears in `GET analysis/requests`.

### 3. Analysis tab upload -> `POST analysis/inputs` -> normalized input -- INCOMPLETE

What exists: the route is live and targets `irpt-ycharts-generate` (`upload_entry.py`, `uploads.py`); the served
portal chunk carries `analysis-input-upload`. Exercised on the served build `inrij6hL`: window 24, 2026-09-29T17:26Z,
NORMALIZED in 2 s (`2.0.0_SA_COO~Y`'s evidence, STATUS~Y section 0b).

The exact gap: two uploads that overlap exhaust the resolve retry -- 3 of 5 bodies in window 22 ended
`RESOLVE_RETRY_EXHAUSTED`, and the failure tracks concurrency, not the file (rows S206, S215). The served answer still
offers `REPLACE_FILE`; the corrected words (6b96d460f6) are on CLOUD only. The served portal lacks 7 Analysis-tab
commits that exist on DEV, the upload modal among them.

Close: serialize or queue the resolve so a second upload waits instead of failing, and serve 6b96d460f6. Proof: two
uploads 10 s apart both reach NORMALIZED.

### 4. Normalized input -> composition -> `POST analysis` -> job and queue message -- WORKS

What exists: `submission_service.py`, `request_composition.py`, `durable_job.py`; the route is live; a submitted
Comparison became a job, a queue message and a READY report (window 22, job READY, `case_trace.py` 20 MATCH,
0 MISMATCH, 2 NOT_EVALUATED of 22 links).

Limit: proven for an interactive Opal principal and Cottonwood. 2 job rows read SUBMITTING and were not opened.

Close: none for the thread. Read the two SUBMITTING rows once and name their state.

### 5. Comparison catalogue -> composer -- MISSING

What exists: the catalogue read and its closed v1 contract on CLOUD (f7ae621369, 53bbae9c4f).

The exact gap: the served `entry.py` predates both commits; no catalogue route is among the 17 live routes; the
portal declares no catalogue operation at PROD or at DEV (17 operations each). The composer still takes opaque
comparison keys. An Overview (zero comparisons) does not cross this hop.

Close: serve the catalogue GET, publish its route, add the portal operation and bind the composer to it. Proof: the
composer lists model names and the submitted composition carries the chosen keys.

### 6. Accepted job -> the identity the resident runs it as -- INCOMPLETE

What exists: `current_authority.decide()` resolves each job's recorded principal before any vendor act. The
long-lived principal `svc-irpt-analysis` exists with `allowedFirmIds` cottonwood.

The exact gap, three parts. (a) A per-window principal was deleted while its job was queued: the resident journal
shows 4 `CurrentAuthorityRefused code=ACTOR_NOT_FOUND` lines since 2026-09-30T05:13Z (row S231), and the dead-letter
queue reads 2 against a recorded baseline of 1; the added message was not opened. The fix that ends such a job by name (62535e0fdc) is on CLOUD and not installed. (b) The API
does not enforce `allowedFirmIds`: IB-pr-271 is on CLOUD, not served; its served move, IB-pr-275, is in flight at
`2.0.0_SA_COO~P` (three of six candidates withdrawn at 04:50Z). (c) THE RESIDENT DOES NOT ENFORCE IT EITHER. The
running `current_authority.py` equals d3f612d94d and contains 0 mentions of `allowedFirmIds`; IB-yr-293
(2704705672) is not in the st5 root. Row S238 reads "enforced at the job (resident)"; that is true of CLOUD and false
of the deployed resident. On deployed bytes the service principal's firm limit is enforced nowhere.

Close: one resident build at CLOUD HEAD (it picks up 293, 62535e0fdc and 291), installed in the same window as
IB-pr-275. Proof: the CTO's S238 read (a foreign firm refused at the API, the own firm 200) plus one resident-side
refusal of a foreign-firm job from its own journal line.

### 7. Resident -> an accepted YCharts session -- INCOMPLETE (the blocking hop)

What exists: the host capture (`/opt/investor-reporting-ycharts/run-ycharts-session.sh`, exactly one
`secret-ids.env`), the versioned secret, the resident's one-refresh allowance, and since IB-yr-231 a journal line
naming each eviction verdict. A probe authenticated at 2026-09-30T04:58Z (row S230).

The exact gap: the last 3 of 3 jobs to reach the vendor ended at the session -- two `SESSION_REFRESH_ALREADY_USED` in
window 24 (row S218) and one `CAPTURE_FAILED:AUTH_FAILED` in window 25 (row S225). No job has reached the vendor
since. The cause is not named. Three candidates stand (row S230), plus a fourth: two independent sessions on one
vendor account, the gateway's and this one (row S233). Capture runs on demand only; the host has 0 timers.

Close: ONE solo Overview job on a cold resident with the verdict journal read afterwards. It either produces a report
or names the verdict. It needs no new vendor word: Andrew's standing word at `2.0.0_SA_COO~Y` covers Analysis
attempts, ledgered. The merge question (S233) needs his per-use word and is not on the thread.

### 8. Session -> upload, portfolio, generation, vendor PDF -- INCOMPLETE

What exists: `recipe.py`, `job.py`, `transport.py` with read-back and the saved-type refusal; the resident's
`recipe.py` equals CLOUD. One Comparison ran the whole chain live (window 22: template 14141824, 16 pages).

The exact gap: coverage, not wiring. No Multi-Comp report, no Target Weight report (the upload reached the vendor:
2 rows echoed), no report for 49 Financial, none for Inflection. Each stopped at hop 3 or hop 7, not here.

Close: after hop 7, one job per remaining arm, each traced with `case_trace.py`.

### 9. Vendor PDF -> certified sections -> published report -- WORKS

What exists: `extract.py`, `certify.py`, `publication.py`, `publisher.py`; on the resident all four equal CLOUD. The
window-22 Comparison certified 72 of 72 scalar sections with 0 misses and the foreign-firm name check passed.

Limit: one variant, one firm. The certifier does not yet refuse a Comparison whose PDF prints none of the chosen
names from the catalogue (the round-30 cell, uncut).

Close: none for the thread.

### 10. Published report -> `irpt-status` -> the Analysis tab -- INCOMPLETE

What exists: three live routes on `irpt-status` (request history, request read, sections) and the tab's
`NativeSections`. One request (REQ-67e12718) read READY with 51 section dates through the API on 2026-09-28.

The exact gap: the page has not shown a READY report. Window 22's report answers 200 / UNAVAILABLE / UNEXPECTED on
its sections route, "bundle was not rendered" (row S213). The named-refusal fix and the CORRECT words are on CLOUD;
`irpt-status` is 7 modules behind and was last deployed 2026-09-28. The page walk of REQ-67e12718 is an open ledger
leg (`irpt-status-dates-rebuild3-20260928` A1). Not re-read here: this seat holds no signed-in session.

Close: serve `irpt-status` at CLOUD HEAD, then one walk of one READY request on the local DEV build against the real
backend, sections on screen, recorded as the trace's last link.

### 11. Vendor PDF -> the advisor -- MISSING

What exists: `VendorPdfPreview.tsx` and the report's `protectedArtifact`.

The exact gap: the component prints the artifact reference and the route as text. No live route serves an Analysis
PDF: the only download route is `export/{exportId}/download`.

Close: one authorized same-origin download route for the retained vendor PDF and a link in the preview. Proof: the
bytes downloaded equal the retained PDF's sha256.

### 12. Analysis report -> Opal-branded PDF export -- MISSING

What exists: the Performance export chain (bundle, render dispatch, receipt, download), and the page header's one
Export control, which targets this tab.

The exact gap: the served `retained_export.py:71-72` refuses anything but a Performance report ("only a retained
Performance report over a server-issued selection exports"). The CTO ruled the Analysis export an enrichment under
FWD-9 (101465).

CORRECTION (committed 05:29Z @c621a6f099, same author): this paragraph first also cited the live value `IRPT_EXPORT_RENDERER=unavailable`
as part of the gap. That was wrong. `infra/aws/terraform/investor-reporting/export/lambda.tf:72-77` states the value
is deliberate and permanent: the function is a controller that dispatches the render to a browser host, and has no
renderer of its own. It says nothing about whether an export can render. The refusal above is the whole gap.

Close: admit `ANALYSIS` in the retained-export resolver with its own template, and render it on the host the
Performance export uses. Proof: one exported PDF whose sections equal the report revision on screen.

## Recommended completion sequence

PROPOSAL -- the CTO rules the way forward.

1. **The live thread.** One Opal admin (or `svc-irpt-analysis`), Cottonwood, one CSV upload, Overview with no
   comparison, no export, on the deployed stack: hops 3, 4, 6, 7, 8, 9, 10. It needs ONE build window first, because
   the thread crosses three stale units: IB-pr-275 grants-first, `irpt-status` and `irpt-ycharts-generate` at CLOUD
   HEAD, and the resident at CLOUD HEAD. `2.0.0_SA_COO~P` owns the shared first hop (authorization and the served
   moves); `2.0.0_SA_COO~Y` owns the job and the YCharts read. Then one solo job, its journal, and one page walk by
   `2.0.0_SA_COO~D`. One trace artifact.
2. The remaining variants and firms (hop 8), one job each; the catalogue (hop 5) before Comparison and Multi-Comp are
   offered by name.
3. The resolve concurrency fix (hop 3).
4. The vendor PDF link (hop 11), then the Analysis export (hop 12).
5. Email intake (hops 1 and 2). It is the furthest lane and nothing on the thread waits for it. Its first act is the
   mail credential. One question to settle before building the consumer: the gateway already reads Opal mail through
   its own Microsoft 365 access; whether intake should use that instead of a second Graph registration is the same
   shape as row S233. Not measured here; the gateway is site Z's.

FWD-4's constraint line says the request arrives by email. On the deployed estate the upload is the only lane that
has ever produced a request. If the thread is cut on the upload, FWD-4's text and FWD-9's order are the CTO's to
reconcile.

## Acceptance

One reconciled trace per case, from the advisor's file to the screen and the PDF: input bytes, normalized input,
composition, job, vendor request ledger, retained PDF, certified report, sections served, sections on screen, export.

Cases: 3 firms x 3 variants x 2 input lanes (upload, email) x the failure arms: an evicted session, a deleted or
disabled principal, a foreign-firm job under the service principal, overlapping uploads, a repeated forward, an
unreadable attachment, an absent report blob.

## Evidence anchors and limits

Workspace CLOUD @b80543a03c (the package census); the resident census ran at about @266ecd287b, after 62535e0fdc
landed, so `resident_worker.py` is stated against that commit. The served `firm_registry.json` differs from source
only in its `_generated` stamp (4 of 4 packages). Portal origin/DEV @b336b141, origin/PROD
@ba8e971f. Other seats were committing during the read; `2.0.0_SA_COO~P` is mid IB-pr-275, so live digests may move
after 04:53Z.

Verified fresh: the five deployed units' bytes, schedules, queues, routes, table counts, secret metadata, the served
portal's operations. Not verified fresh: any hop's behaviour under a request. Lane A (a registered client's custody
holdings as the input) was not walked: the ask named email and upload. The served portal build's identity is
inferred from timing.

- `infra/aws/lambda/investor-reporting/intake/{poller.py,outbox.py,upload_entry.py,uploads.py}`
- `infra/aws/lambda/investor-reporting/ycharts/generate/{current_authority.py,resident_worker.py,recipe.py,entry.py}`
- `infra/aws/lambda/investor-reporting/export/retained_export.py` (served copy read from the deployed zip)
- `infra/aws/lambda/ci/lambda-source-map.json`
- `infra/aws/terraform/investor-reporting/api/integrations.tf`
- `portal/src/api/endpoints/investor-reporting.ts`, `portal/src/pages/InvestorReporting/tabs/analysis/`
- `org/missions/D9/IRPT/IRPT_BCKEND/STATUS~Y.md`, `ledger/ROUND_ANALYSIS.sweep5.md`
- `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md` rows S206, S213, S215,
  S218, S225, S229-S233, S238
- Prior trace of this surface: `org/tier1_exec/4.0.0_SA_CRO/deliverables/SENSITIVITY_END_TO_END_GAP_BRIEF_20260922.md`

## Andrew-direct request -- verbatim record

Channel: Andrew at the `1.0.0_SA_CTO` terminal, 2026-10-01 about 04:23Z (12:23 AM Eastern), recorded by that seat in
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261001_042xZ_SELF_DRIVE_60M_LAPTOP_FABRIC_FINAL_SAY_CLOSER_DRIVE_IRPT_FIRST.md`;
reached this seat as msg 103444.

> You have 4.0.0_SA_CRO~X as your research partner so as you see projects developing, if you assess there needs to be
> higher resolution on any part of the development process, you have CRO~X run /closer trace on the given surface and
> assess the strategic way forward.
