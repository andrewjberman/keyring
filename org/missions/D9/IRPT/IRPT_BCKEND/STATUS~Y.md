# IRPT_BCKEND~Y (Analysis) -- status

Seat `2.0.0_SA_COO~Y` (CLAUDE). Contract `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`
v1.4 (COO_Y.md, CONTROL.md apply). Reviewer `3.0.0_SA_CVO` (grades landed pins after the fact while the lease is FAST).
Drive: `/closer-drive IRPT_BCKEND~Y` every 30m (cron 81b07667, re-armed 16:0xZ after the pause), per CTO 101100
(Andrew-direct ~03:0xZ, 09-26; record `ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_LAPTOP_DIRECTIVES_IRPT.md`). Vendor API egress
is permitted but ledgered; served moves need the CTO's never-widen half. Goal: `org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20260923_230xZ_COO_Y_GOAL_ANALYSIS_E2E_LOOP_20M.md`.
As of 2026-09-28T13:45Z. Lease FAST until 2026-09-28T14:03:58Z.
Detail history: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/STATUS.md` (13:45Z).

## Now (13:30Z 09-28): the GRANT release's generate is LIVE and verified; rebuild 3's gates are committed

- **irpt-status rebuild 3 (packet 31fbdcbf; the CTO half is SIGNED conditional on gates 3 and 4, CTO 102308).**
  - Both gates PASS on the built zip (S3 version 7Uz6kDd, CodeSha256 ZYr+IDMp).
  - Gate 4: REQ-67e12718 answers READY ANALYSIS_READY, PER_SECTION, with 51 dates.
  - Gate 3: 6 reads; under the planned grant 0 are denied. The only change is original_holdings, implicitDeny -> allowed.
  - Negative control: the live bMMJ zip refuses DATE_SOURCE_OWNER_BINDING after 3 reads.
  - Record `REBUILD3_GATES_3_4_20260928.md`, with the `status_role_sim.py` planned-policy option: sent to P at 13:00Z;
    committed once MSTR narrowed the freeze (102334), and the hash went to P for the ledger.
- **Comparison GRANT release (b6c264b3; CRO SIGNED at e60a5043e8).** Every arm passes on its exact built artifacts.
  Record: `GRANT_RELEASE_ARMS_20260928.md` @2da2b97711. Results sent to P at 12:43Z.
  - **Generate D1 is LIVE:** `AdE17rT6` since 13:11:54Z, the proved bytes.
  - Re-run under the live function's own environment (`offline_submit_proof.py --live-env`): Comparison, Multi-Comp
    and Overview are ACCEPTED, and the unknown key is REFUSED with 0 writes.
  - **Resident D2 is LIVE** (P closed the ledger at 13:19:08Z). Y's own SSM read: root `fe64236bbb-st2`, the 6 member
    shas equal the proved st2, 0 restarts, 0 Tracebacks. **Next: the first live Comparison window, asked of P.**
  The first live Comparison window is ready on Y's side: `live_chain.py` WALK_COMPARISON_KEYS gives the ONE K5
  body (one key Comparison, two Multi-Comp); all three arms validate against the schema. It runs on P's window packet.
- **Freeze NARROWED** (0.0.0_AB_MSTR 102334): local commits and merges are legal again. No push until MSTR's CLOSE,
  and a ~10-minute no-commit window is announced separately.

## Window 15 (09-27): READY live, the first Analysis report (`LIVE_WINDOW15_EVIDENCE_20260927.md`)

- `REQ-67e12718..` went READY at about 16:23Z on resident `lt`, as report `RPT-5288c06d..`, with 2 receives, 3 status GETs, 1 saved GET
  and 0 re-captures. Receive 1 released on `calculating` at 16:07:03Z; the redelivery resumed at 16:22:09Z. K10 is D's.
- The saved `level_as_of_type` reads `custom_date`, against `prior_close` sent: P filed row S159, Y filed row S160 (@1a5e710dbd).
  The PDF prints "As Of: Custom" (p.14), and so do the research-era PDFs. As Of is a returns input, so ~Y 101938's reason
  is withdrawn (CTO 101971).
- **Built (CTO 101971):** the tolerance holds only on a portfolio the PDF prints Static.
  - Y @36837771d6; `P_STATIC_TOLERANCE_20260927.patch` (apply-check rc=0 on P `f92445392d`).
  - Proved at the real entry point on the served `lt`, arms A-E: Static goes READY; Dynamic or absent goes ATTENTION
    `TOLERANCE_REQUIRES_STATIC` with 0 S3 puts.
  - It ships on P's next resident version, with its own ledger.
- **The discriminator is answered from the advisor's recorded HAR, with no vendor call** (S161 @ea7f5e9291). The advisor's
  create stored `prior_close` (date 2026-07-01), so the vendor does not normalise it. The advisor's create had no upload;
  ours always upload. **RULED (CTO 102021): keep W15-3 Static-only as built**; the vendor GET is withdrawn (row S162
  @e2c240c2d1). **R10 CLOSED (CTO 102024):** the vendor's printed "Data as of" line is the label, so there is no
  certifier change. The advisors send as_of_date_option=latest (6/6), as the recipe does. S163 @5465f7dcd1 closes S159.
- **Static narrowing APPLIED at P** `12a67ed5ee` (content-identical to the proved overlay: extract 719369d5, resident_worker
  9b2dbd18, recipe 982d8171); its deploy is P's. Enrichment candidate: check the saved `model_portfolio_type`
  at read-back, before the report is generated.

## Earlier (Andrew-direct at ~Y, ~18:5xZ: "dont need option 2, but do 1 3 and 4 in order"; CTO 101442, 101465)

All three are done, and every proof is offline: reads are live, writes are captured, and no vendor call is made.
1. **Hops 5-7** (`HOPS_5_7_PREFLIGHT_20260926.md` @0d7ec20003): the deployed resident plus the lane fix runs window 3's
   real composition to READY (handled=1, one REPORT#). As deployed, it is refused at admission.
2. **Hops 8-10** (`HOPS_8_10_PREFLIGHT_20260926.md` @acd17573d7):
   - (A) irpt-status lacks `interactive_access.py`: 0/4 Opal reads as deployed, 4/4 with it;
   - (B) irpt-status-role lacks `s3:GetObjectVersion`, a simulated deny; patch `P_STATUS_READ_GRANT_20260926.patch`;
   - (C) Analysis export is unbuilt, refused by name. The CTO ruled it an enrichment under FWD-9, off the window (101465).
   **A and B are SERVED** (P 101481, 19:56:53Z; irpt-status `bMMJ/bQ+5`; simulation 10/10).
   Y's no-overlay proof on the served zip is 4 of 4; the prior zip is the control at 0 of 4 (@1d70f8ec6c).
3. **Cross-viewer title binding** (`M_CROSS_VIEWER_TITLE_BINDING_20260926.md` @1b40d23954): a 2nd viewer goes from
   refused to ACCEPTED, and the resident goes from refused to ADMITTED. The patch is routed to P, whose lane
   IRPT_COMPLETION_P owns `reports/**`; M reviewed it (101479).

Deployed: P served the hop-3 patch (generate `/iFhTAvT`, resident `fe64236bbb`; content proof 6/6, P 101467). Y's
overlays are content-equal to those six files once CRLF is stripped. The one byte difference is templates.json line
endings, which changes only the offline composition's `configuration_sha256`.

Next window (CTO 101465): upload, generate, READY, sections, history. A+B are applied and the pre-flights are pinned.
- **Hop-7 defect, found offline (20:5xZ):**
  - On every retained real vendor PDF (overview, comparison and multicomp), the deployed resident is refused
    CHART_DATE_CERTIFICATION_FAILED, and the job stays CERTIFYING.
  - The fix is `P_HOP7_CHART_DATE_CERTIFY_20260926.patch` (Y branch @74b4368bef). With it, the resident goes to READY on
    the real Overview.
  - **SERVED** (P 101518): the resident runs `/opt/irpt-resident/fe64236bbb-h7` from 21:20:44Z. Host certify.py sha256
    `33e54ac0..` equals Y's fixed file (the old one was `f1516e24..`); ledger `irpt-hop7-certify-resident-20260926` is
    CLOSED. Generate still packages the old file, but nothing on generate's path imports it.
- P cuts the packet.
- Y handed P the measured write set for its blast radius: `K5_SUBMISSION_ACT_20260926.md` @f36c5ee4c4. The vendor PDF is
  retained in `opal-data-irpt`, and there is one `_opal` lease row.
- Per Andrew, the re-prove and window 4 are not Y's to run unless he asks.
- **Window 6 RAN** on Andrew's word at ~Y, 00:09Z ("run the Analysis window now"); record
  `LIVE_WINDOW6_EVIDENCE_20260927.md` @07f3caa3ab.
  - K4: NORMALIZED at 00:10Z, input `portfolio_4c5c85d0..`.
  - K5: QUEUED at 00:12Z, `REQ-3a1b73a8..`. **Hop 3 passes live.**
  - The job stalls in SUBMITTING. Receive 1's host session capture failed within about 2 s, cause unlogged; node,
    playwright, aws and Chromium check OK on the host.
  - Receives 2 and later fail at `principal("start")`, because the submitter was deleted at 00:21:32Z. The DLQ follows
    at about 01:12Z. No vendor write happened.
  - Findings to P and the CTO (101671/101672): branch (e)'s "the resident needs no principal" is false; and the live
    blocker is the vendor session capture, where one diagnostic wrapper run needs Andrew's word.
- **S151 DISARMED (02:0xZ):** one wrapper run on Andrew's word (CTO 101694).
  - It authenticated with rc 0, via a form sign-in. The fresh session `d38f6941` is fence 13.
  - Receive 1's failure is not reproduced in the same environment; the cause was transient and is unmeasured.
  - The retained-reason patch is live in the resident (`fe64236bbb-rr`), so any recurrence names its class.
  - Ledger CLOSED; record @a679a32e4b.
  - The next Analysis window must keep its principal until the job is terminal (CTO 101673).

## Pins

| What | Value |
|---|---|
| Working branch / worktree | `irpt-mvp-y-20260922` at `C:/Users/AndrewBerman/Desktop/irpt-mvp-y-20260922` |
| Workspace candidate pin | `a9fba2f3e9` (hops 1-7 offline on a deferred v2 template input: READY, vendor upload carries AAPL 10.01 / VNQ 2.02) over `58280c8dd4` (Y2 deferred arms: XLSX, weights, correction) over `522afcfd17` (test module-identity fix, P 100860) over `d16b7c8743` (hop-3 input-owner lookup) over `10a16bd89d` (attribution fix) over `bb1eb7f92b` RESOLVE_UPLOAD (CVO handoff 18:29Z) over `b398d27731` |
| P composition patch | `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/P_UPLOAD_COMPOSITION_20260924.{patch,md}`: hops 2+3, applies clean to P `9efaf2850e` |
| Portal candidate pin | n/a (portal candidates go to `2.0.0_SA_COO~D`) |
| Deployed artifact pin | resident `irpt-analysis-resident.service`, package `ab2e088b5b` (P receipt 100483; not re-read by Y) |
| Push state | Y branch LOCAL; not on origin (brief section 2: origin holds only `CLOUD`) |

## Live thread

State: LIVE THROUGH HOP 1d (upload -> resolve -> NORMALIZED). At 13:54:56Z Y made ONE `POST /analysis/inputs` by API as
the admin+Dev walk principal `irpt-uiwalk-1790430787@opal.test` (packet v3 blob `07b7a000`, K4; CTO `b70ede1756`, CRO
`a157c45762`; P 101191):
- the POST answered RESOLVING;
- the resident logged `handled=1` at 13:55:02Z;
- NORMALIZATION# reads NORMALIZED;
- `INPUT#portfolio_99e76df8...` is `irpt-normalized-portfolio.v2`: total 12.03, AAPL 10.01, VNQ 2.02, both resolved by
  YCharts.

Evidence with every row and object key: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/LIVE_UPLOAD_1203_EVIDENCE_20260926.md`
@3cc73f2b79. The scrubbed log is `LIVE_UPLOAD_1203_20260926_RUN2.json`. The 03:17Z failure (the missing `interactive_access`)
was fixed by P at `45d905110c`, served as generate `IJD6bd1I` at 13:30Z; the closure check exits 0.

Hop 3 was ATTEMPTED as K5 (packet v5 `6813377a`: CTO `3b43a23f92`, CRO `80b1a711f3`; CTO 101203). At 14:18:08Z Y made ONE
`POST /analysis` (Overview) on that input, which answered UNEXPECTED, `corr-8c5e097ea21e`: generate raised
ModuleNotFoundError `jsonschema`.
- `ycharts/generate/composition_admission.py:11` imports jsonschema and referencing at module level.
- Zip `IJD6bd1I` carries neither.
- Nothing was written: no row, no job, no queue message, no vendor call.
- Log: `LIVE_SUBMIT_1203_20260926.json`.

The closure check passed that zip because it walked only first-party imports (surprise row S144 @fa8aff523f). Y fixed it
@2664fe084c: it now FAILS on `IJD6bd1I`, naming jsonschema and referencing [MODULE]; a positive control with stubs passes.

The principal was deleted at 14:22:22Z (P 101232). The input's owner binds to that deleted principal, so hop 3 needs:
- P's fix is LIVE at 14:52:47Z: generate code `85TXFzzv0gcMBcokhqlGjeMcFK7pBHDx3ELN50R04iU=` plus layer
  `irpt-common:5`, ledger `irpt-generate-jsonschema-fix-20260926`. Y's check on the S3 artifact, whose sha256 equals the
  CodeSha256: with the layer, exit 0 (40 modules); without it, exit 1 (jsonschema, referencing). That meets CTO 101230
  conditions (1) and (2). Condition (3), importing every module on the deployed function, is P's.
- then a new window: a fresh upload plus a submission, or Andrew's own upload plus Generate. Y asked 1.0.0_SA_CTO at
  14:5xZ for a K4+K5 window after condition (3).

WINDOW 2 (packet v7 `3edebd85`, principal `irpt-uiwalk-1790435397`, 15:10Z-16:05Z):
- K4 NORMALIZED again: input `portfolio_f40b800e..`, the resident logged `handled=1` at 15:14:04Z, and the 7 new rows
  are all K4's.
- K5 at 15:16:38Z answered UNEXPECTED, `corr-fd24ee4063ad`: `irpt-ycharts-generate-role` was denied
  `s3:GetObjectVersion` on `opal-data-irpt/irpt/cottonwood/state/normalized_portfolios/...`.
- K5 wrote nothing and made no vendor call.

The grant patch for P is `P_GENERATE_SUBMISSION_S3_GRANTS_20260926.patch` @e5daacce0b: read NORMALIZED_PORTFOLIO and
retain REQUEST_COMPOSITION. Hop 3 then needs window 3.

After the Andrew-direct pause (15:27Z-16:03Z; CTO 101280 and 101297; loop re-armed as cron 81b07667):
- P applied the grant at `be7647e48f` (16:1xZ).
- Y delivered the full-path IAM list (CTO 101276) @2789ac3bbd, from an AST census of the deployed code (zip 85TXFzzv;
  resident f624e8a72f):
  - generate: 25/25 met their expectation (hop3 16/16 allowed, including K5's two formerly denied actions; 3 negatives
    denied);
  - resident: 40/40 met their expectation (hop3 37/37 allowed; 3 negatives denied).
- Next: P's own simulator run, then ONE window packet (hop 3 plus the export-B BEFORE read).

WINDOW 3 (17:12Z, v8 `acca1b3e`):
- K4 NORMALIZED: input `portfolio_d188498e..`, handled=1 at 17:15:35Z.
- K5 answered UNEXPECTED "maintained recipe title descriptor required" (corr-85a852bf59dd); nothing written.
- CTO 101367 ruled the default title per template.

HOP 3 PROVED OFFLINE (CTO 101355) @24a87c9d53, `HOP3_OFFLINE_PROOF_20260926.md`: the served zip plus the fix patch ACCEPTS
(26 stages, 0 refusals, stopped at the queue send), and the resident's own admission ADMITS to the vendor boundary. The
proof found 2 more live defects:
- recipe.py's settings.json path;
- submission.py refusing template-lane inputs, in generate AND the resident.

The patch `P_HOP3_SUBMISSION_FIXES_20260926.patch` has 8 files. Y branch pins: e5113f815e (title) and 895c7ade1d (lane).
ASK of P (101436): apply, and redeploy generate AND the resident. Then Y re-runs the proof on the new zip with no overlay,
and window 4 re-runs K4+K5 (+R1).

## Acceptance IDs

| ID | State | Evidence |
|---|---|---|
| Y1 custody + owned CSV/XLSX + disposition | OFFLINE + one real-object run | interpreter @47b2adf6df, oracle 15/15 |
| Y2 immutable normalized input | LIVE for Dollars CSV (one run, 13:55Z, @3cc73f2b79); the other arms OFFLINE | deferred lane @bb1eb7f92b + @58280c8dd4: Dollars 12.03, XLSX, TARGET_WEIGHT with notional, missing notional refused by name, correction lineage, race arm; SHARES refused by name (no price source) |
| Y3 acceptance, dispatch, recovery | LIVE once (window 15: queued, released, redelivered, READY) | `LIVE_WINDOW15_EVIDENCE_20260927.md` |
| Y4 vendor PDFs (3 variants) | LIVE for Overview (window 15, sha256 6e753361..); comparison and multicomp not run | `LIVE_WINDOW15_EVIDENCE_20260927.md` |
| Y5 certified typed report | LIVE once (RPT-5288c06d, certified and published) | job row checkpoint_publication |
| Y6 polling/history/reload/downloads | ROUTES SERVED, not exercised | P batch 42/43 |
| Y7 reconciled full trace per case | 1 case traced (template lane, Dollars, Overview): 16 MATCH / 0 MISMATCH; screen and export NOT_EVALUATED | `Y7_CASE_TRACE_W15_20260927.md` |

## Write claims

**Rebuild 3 gates 3 and 4: PASS, the record is uncommitted until the freeze CLOSE (see Now).** **irpt-status rebuild 2 (5fSyChId) ROLLED BACK at 00:36Z (CTO 102269):** W20 K10 got 500s. The status role lacks a read on
state/original_holdings/, and the zip's errors.py is holdings/errors.py, so refusals crash. bMMJ is live. Rebuild 3 comes after
05:00Z, with Y's gate tools (@d43884aa01): the collision census, the owner-refusal arm and the role simulation. K10 re-runs on rebuild 3.

**irpt-status rebuild HyEyoJ67 FAILED at cold start and is ROLLED BACK** (Y caught it with 0 invocations; CTO 102204; live
bMMJ/bQ+5 from 23:15:47Z, verified byte-identical; the one invocation since was P's post-rollback proof; 0 errors). The fix is
proved (HEAD `_authz/served.py` 3a2cdba2 gives READY PER_SECTION 51). The rebuild with an import smoke is P's next packet; K10 waits.

**Release catv2+static VERIFIED (P ledger CLOSED 22:47Z):** the served generate `ykJltfTd` ACCEPTS the Overview. The resident `st`
equals the proved files, and with no overlay it runs window 15's shape: Static READY, a foreign row ATTENTION, no tolerance READY.

**Re-cut, at P (CTO 102169):** P's naming gate refused the typed firm ids. The check (Y @14568b9ec1) now reads every client firm's
printed names from the registry. The grant (Y @0a24edfe38) types no firm; M's consumer resolves them through lookup() and re-pins.
Both patches pass the naming gate in ENFORCE with apply-check rc=0 on P `c296cdff9c`. P applied the status-dates patch (`c296cdff9c`).

**Y2 arms ready for a window:** `P_Y2_UPLOAD_ARMS_ACT_20260927.md` (@5d371a403e) covers an XLSX template (`aapl-vnq-12.03.xlsx`) and
Target Weight at notional 1000 (`aapl-vnq-target-weight.csv`). `live_chain.py` takes WALK_UPLOAD_FILE, WALK_FILE_TYPE and
WALK_REFERENCE_NOTIONAL; unset, it is window 15 exactly. It runs when P cuts a window that carries them.

**Built, at P (a live-thread defect before K10):** window 15's READY job read wrong on status-job (the served
irpt-status with the portal's header refused it). Y @6998d0acff (CSV) and @49f3393cb0 (one-sheet XLSX) extend the undated date proof to
the template lane; the patch is cumulative, `4d50bf51..`, and prospect_dates.py is `e5bae585..`. `P_TEMPLATE_STATUS_DATES_20260927.patch` has apply-check rc=0 on P `118612b599`. P rebuilds irpt-status
with HEAD's `submission.py` plus the patch. Measured arms: served = refused; + submission.py = UNAVAILABLE;
+ both = READY ANALYSIS_READY, PER_SECTION, 51 dates. Record: `TEMPLATE_STATUS_DATES_20260927.md`.

None in flight. **Y7, first case, DONE:** `live_walk/case_trace.py` on window 15's case gives 16 MATCH, 0 MISMATCH and
2 NOT_EVALUATED (screen = D's K10; export = window 16). The sections are re-read 46/46 at their own coordinates in the
retained PDF, and the negative controls bite. Record: `Y7_CASE_TRACE_W15_20260927.md`.

None in flight. CTO 101917 (b) release-and-resume is built @d200b07129 (`P_READ_BACK_RELEASE_RESUME_20260927.patch`, at P) and proved offline: window 13's shape releases, then redelivers to READY with 0 captures and 1 create. The W13 diagnostics (reason and stored value) are SERVED as resident dx (P 101918). Release-and-resume is **SERVED** as resident rs (15:18:44Z, P 101934). `level_as_of_type` is recorded, not gating: Y @1b6a267faa, `P_LEVEL_AS_OF_TYPE_TOLERATED_20260927.patch`, at P with the packet line; offline, window 13's shape goes from ATTENTION to READY. **SERVED** as resident `lt` at 15:51:47Z (P @935ebebc84, pin 49b85eacd2); recipe.py and resident_worker.py are content-identical to the overlay Y proved READY. **Window 15 RAN: READY** (blob 51362fca; `LIVE_WINDOW15_EVIDENCE_20260927.md`). The Static narrowing (CTO 101971) is Y @36837771d6, `P_STATIC_TOLERANCE_20260927.patch`, at P. **Window 11** (`LIVE_WINDOW11_EVIDENCE_20260927.md`): two defects, named by the journal, are fixed on the Y branch @ff1f95a701 (`P_W11_CAPTURE_ENV_SAVED_READ_BACK_20260927.patch`, at P). (1) The host capture ran under the resident PYTHONPATH, so the `aws` CLI crashed (LEASE_NOT_HELD), measured on the host. (2) The read-back compared the status body, which has no settings; it now reads the saved portfolio. Offline, window 11's exact shapes go from ATTENTION to READY. **SERVED** as resident `fe64236bbb-cw` at 13:51:07Z (P @45c9ac981e). recipe.py, resident_worker.py and host_capture.py @b6739556ea are content-identical to the overlay Y proved READY. **Window 13 RAN** (`LIVE_WINDOW13_EVIDENCE_20260927.md`). Both W11 fixes worked live: the capture got past AWS, and the saved read shows 7/7 present and 6/7 matching. It stopped on (a) `level_as_of_type` differing from `prior_close`, value unrecorded, and (b) the re-capture meeting an unexpected screen. Patch `P_W13_CHALLENGE_REASON_STORED_VALUE_20260927.patch` names both next time. The poll DECISION is at the CTO (REC: at most 2 status GETs per delivery, else release and let the queue redeliver). The CTO's (c) ruling is built on the Y branch @4aaeaea3d5 (`P_READ_BACK_WAF_REFRESH_20260927.patch`, cut against P's rb): a backed-off poll, and ONE refresh on a read WAF challenge. Offline, window 8's exact shape goes ATTENTION to READY. **SERVED** as resident `fe64236bbb-wf` at 05:55Z (P, ledger irpt-resident-waf-refresh-20260927 CLOSED). Its recipe.py, resident_worker.py and broker.py @e2fdd01015 are content-identical to the overlay Y proved READY. **Andrew-direct at ~Y, 12:4xZ: "yes you can run as many analysis attempts as needed"** (@460e2ae8cb). ~P is asked (101866) to cut the Analysis window packet, whose K5 names up to 6 status GETs and ONE re-capture. ~Y runs live_chain.py on the handover. Window 7 (`LIVE_WINDOW7_EVIDENCE_20260927.md`) ran live through the YCharts upload and portfolio create,
then went ATTENTION `VENDOR_READ_BACK_REFUSED`: the read-back read a `calculating` portfolio once. Fixed on the Y branch
@edac4aa42f (`P_READ_BACK_POLL_20260927.patch`); offline, the served resident plus the fix goes from ATTENTION to
READY. **SERVED** as resident `fe64236bbb-rb` at 03:41:53Z (P, pin 07f1982ab9). Its recipe.py and resident_worker.py are
content-identical to the overlay Y proved READY. **Window 8 W8-2 RAN** on Andrew's word (04:01Z); record `LIVE_WINDOW8_EVIDENCE_20260927.md` @98975d923b.
- K4 NORMALIZED; K5 QUEUED `REQ-a8e81b8e..`.
- The upload and portfolio 2363801 succeeded.
- The read-back poll waited out 2 `calculating` answers, then YCharts' WAF challenged the 3rd poll (202). The job went
  ATTENTION by design: the controller never re-signs in on a WAF challenge.
- A DECISION is at the CTO (101790): (a) refresh on a read WAF challenge, (b) gentler polling, or (c) both. REC (c). The retained-reason fix landed on the Y branch @9c6626e1be (`P_RESIDENT_RETAINED_REASON_20260927.patch`,
at P). With it, the resident journal names a failed capture's `failure_class` and any retained exception's class and
closed code, so the next capture failure diagnoses itself. The hop-7 certify fix landed on the Y branch @74b4368bef (`HOP7_CHART_DATE_CERTIFY_20260926.md`).
RESOLVE_UPLOAD landed @bb1eb7f92b and @10a16bd89d. The scratch worktree `irpt-y-pcompose-20260924` was
removed by 0.0.0_AB_MSTR at 13:3xZ after Y's content check (101172); its branch is kept. Y makes no commit on P's branch.

## Next proof

Live hops 1a-10 per `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/RUNBOOK_1203_LIVE_JOURNEY_20260923.md` once Andrew
posts `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv` as an Opal viewer. At 22:12Z on 09-25 there are
still 0 UPLOAD#/NORMALIZATION#/INPUT# rows in all three firms. Portal 5174 is at `8242412d` and still carries the template lane
(`prospect.ts:65`). No Y build item is unblocked:
- Custody hop 4 is P's composition (CTO 100649). It needs P's binding store, current_selection and M's publication_for.
  Y's part is delivered: `build_custody_ports` @47b2adf6df and the decoder rung-2 read @70c464cec9.
- Comparisons need M's policy consumer.
- Shares is parked on CTO 100887.

## Dependencies

| Needs | From (owner) | Interface / pin | State |
|---|---|---|---|
| Upload design card + word | 2.0.0_SA_COO~P | CTO 100667 | not needed to build; Y built on the accepted shape |
| Patch applied (`a58859baa7`); ledger `irpt-upload-hop2-20260924` R1 resident package, then L1 generate rebuild (runbook B2 order) | 2.0.0_SA_COO~P | `P_UPLOAD_COMPOSITION_20260924.md` | AWAITED |
| `ports["ordinary_authorizer"]` producer (partner viewers) and `get_catalogue` (hop 3) | 2.0.0_SA_COO~P | generate_installed absent producers | AWAITED; an Opal viewer is not blocked by it |
| Restore M's viewer seam `485b69c061` onto `_scope/maintained_sources.py` (8 conflict hunks vs `bc3727b3a3`) | 2.0.0_SA_COO~P (M reads semantics) | Y 100842; M 100846: `test_maintained_viewer_sources.py` 27/27 | DONE at P `19b38e2f22` (LOCAL); rides the hop-2 deploy |
| Grants for hop 2 (both roles) | 2.0.0_SA_COO~P | P `54bc1359f4` APPLIED 19:22Z | DONE: Y reach-check 19:3xZ, DDB PutItem + SQS SendMessage allowed, with a negative control |
| Portal: template body, RESOLVING adapter + poll, `.xlsx` (spec `D_UPLOAD_TEMPLATE_LANE_SPEC_20260924.md`) | 2.0.0_SA_COO~D | ~D 100877: edits 1-3 LANDED on portal DEV `088386fe` (the 5174 server's HEAD, Y read 20:2xZ); edit 4 (wire regen) waits on the contract patch | DONE for the live run |
| First live 12.03 upload (file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/aapl-vnq-12.03.csv`) | 2.0.0_SA_COO~D's signed-in PROD walk with a HAR (Andrew via CTO 101075, record @37025a10e9); P mints the test principal (Opal-class, confirmed by Andrew in f7284ddeed); the walk must select a concrete firm, since Global refuses FIRM_BINDING (Y addendum 03:0xZ) | runbook hops 1a-1d; Y reads its part from the committed HAR plus the rows | AWAITED -- notified 20:2xZ. Baseline 20:2xZ: irpt-requests UPLOAD#/NORMALIZATION#/INPUT# = 0 in cottonwood, 49financial and inflection (consistent query; control SELECTION# cottonwood = 14). Contract landed at P `a47102cc8f` (100878). |
| Contract: request template lane + result RESOLVING/findings (`P_UPLOAD_CONTRACT_20260924.patch`, `--check` clean at P `7f6b5589f6`) | 2.0.0_SA_COO~P | Y 20:1xZ | AWAITED |
| Custody composition (hop 4) | 2.0.0_SA_COO~P | Y 47b2adf6df; decoder read `CUSTODY_DECODER_RUNG2_READ_20260924.md` (rung 2 empty for py3.12: 18 layers, 2 pyarrow, both py3.11) | AWAITED |
| First live Analysis submission | Andrew (browser) | after a composition serves | AWAITED |

## Parked

| Question (off-thread) | Owner | Un-parks when |
|---|---|---|
| Comparison / Multi-Comp (FWD-4 arms): composition is PROVED on the served generate plus three changes: M's consumer @d7c97910d9 (hashes 4/4 MATCH Y @0a24edfe38), Y's grant patch, and P's get_catalogue wiring. Comparison and Multi-Comp are ACCEPTED, an unknown key is REFUSED (`COMPARISON_RELEASE_READINESS_20260927.md`) | 2.0.0_SA_COO~P applies the GRANT release (b6c264b3, CRO SIGNED; every arm PASS, @2da2b97711) | the apply lands; Y verifies it live, then runs the first live Comparison window |
| Shares price source (Y2 Shares cells): CTO 100887 ruled (c), refused by name for v1; (b) has no known estate table; (a) goes to Andrew | 2.0.0_SA_COO~Y (re-ask the CTO) | the Dollars journey is graded |
| generate's unknown-comparison-key refusal answers public code UNEXPECTED (state UNAVAILABLE), not a named code; the portal offers only catalogue keys | 2.0.0_SA_COO~P | a viewer can send a free-text key, or P next edits `resolve_comparison_fields` |
| `intake/tests/test_security_resolution.py:31` needs IRPT_LOOKUP_FIXTURE_ROOT | 2.0.0_SA_COO~Y | the next edit to that suite |
| `reports/tests/test_generate_installed.py:58` expects 22 schemas; the tree holds 23 (fails at P's own tip) | 2.0.0_SA_COO~P | P's next edit to that suite |
| generate reads `irpt-common` by name (latest), not pinned (P `08d9f2f0b1`); a new layer version moves generate at that root's next apply | 2.0.0_SA_COO~P | irpt-common v6 is built |
| request_composition.py:88 binds the recipe title source to the INPUT owner (the cross-viewer null title) -- patch delivered @1b40d23954, routed to P 20:09Z | 2.0.0_SA_COO~P | P applies; ships in generate AND the resident |
| OG-v-4 phase 1 (S63): ~O ruled (101477). The 18:06Z seal is committed as the record, superseding b0d4bba5df: `0f2bd1c0d3` on origin `wk-nfra_oplgtw-og-v-4-p1` (MSTR 101482). AC8 is MUTATING; nobody runs it again | 2.0.0_SA_COO~O (drain to CLOUD) | the issuer drains phase 1 |
| The Y worktree is a sparse checkout (`firm_destination_policy.json` is S), so two `test_broker_recovery_evidence` arms fail only here | 2.0.0_SA_COO~Y | a suite needs that file on this worktree |

## Limits

**PUSH FREEZE** (0.0.0_AB_MSTR 102334): no push until MSTR's CLOSE; local commits are legal except in the announced
~10-minute rewrite window. Re-sync the Y worktree on MSTR's CLOSE steps. All Y work is committed as of 2026-09-27T20:05Z. The served
drift census (`SERVED_DRIFT_CENSUS_20260927.md`, @974ec72ce9): irpt-status is the only served-path drift
(submission.py, and entry.py's export B0 line), and both ride P's rebuild.

Hops 2+3 are deployed (generate `LdjdnnLh`, 09-24 19:49Z), but no live upload has succeeded: the one attempt failed on the
missing module before any write. The resident resolution uses no price source: SHARES templates answer
NEEDS_CORRECTION by name until one is composed. No vendor call is made by this seat; the resident's one batched
`securities_info` GET is the standing host-workflow authorization (CTO 100667 (1)).
