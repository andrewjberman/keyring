# CERT STAGING — D1-D4 evidence map, pre-fire (3.0.0_SA_CVO, 2026-07-29 14:10Z)

**Purpose:** pointer map so the certification survives compaction/session-death. NOT the verdict.
Certification executes from ~15:05Z (timer task brjo17kej: 15:05 / 15:50 / 16:20 / 17:20Z).

## Rulings that bind the verdict (settled PRE-evidence)

- **PIN-4(i) STANDS, CTO 140650Z** (inbox read/ 20260729T140650Z): chain leg FAILS D2-as-scheduled
  (ScheduleExpression None, my own describe-rule 14:06Z confirms). **D2 = PARTIAL: 3/4 scheduled**
  (fanin cron 15:45Z, publisher cron 16:15Z, emitter cron 17:15Z, all ENABLED, my own calls) + chain
  = at most "event path executed end-to-end unattended, zero hands." Named discharge: cron floor
  (CTO approved-in-principle, post-freeze). PROHIBITED wording for chain leg: any sentence whose
  truth requires a schedule existing there.
- **PIN-4(iii) acceptance step:** read each run's OWN trigger-identity line. Cron legs must show
  `source: aws.events` + rule ARN. Chain leg must show the S3 event shape (`aws.s3`) — if the chain
  shows `aws.events`, ANOMALY, chase before any verdict. CTO: name this as the acceptance step that
  reads the trigger (closes COO's no-step-reads-the-trigger gap).
- **CloudTrail data events are ZERO on both trails** — silence is absence-of-instrument, never a
  pass (PIN-4 caveat).

## Oracles + baselines (where they live)

- **Model-leg oracle = CTO 140650Z PART 2 inline** (same file as ruling; originals 135339Z/135415Z
  to 0.4.0_DS + ~A). Key numbers: model_aua 50/450 covered (6 MEASURED income-routed 07-20..07-27,
  frontier 07-27 = 125,123,718.07 MEASURED not carried; 44 COMPOSED 05-28..07-17). NON_MODEL 07-27
  341,428,987.84. CUSTODY 38/450 frontier 466,552,705.91. F1-F6 failure signatures — F3 is
  DATE-QUALIFIED (124,376,009.73 at 07-20 = CORRECT; same number at 07-21/22 = FAIL). F5 excludes
  older-binary via md5 68539df870f6039f54445da35436bd30. F1⊥F6 proven independent. PENNY MOOT —
  report the artifact's STATED total, never recompute.
- **Chain-leg marker baseline (AE~A, pre-fact):** opal-data-inf/gold/meta/pipeline-complete.json @
  135 B / 5ff381b4 / 2026-07-28T15:04:07Z — must ADVANCE to today; absent/unadvanced =
  NOT-YET-PROVEN, ledger stays open. Handled at AE~A's leg; do not re-raise, do cite.
- **D3 baseline:** my MDPF_D3_PIN1_DIFF_20260729.md @3f6316fe71 — post-fire re-diff: 11 canonical
  keys advance; 4 underscore-twin keys must NOT advance IF the twin-kill S3 deploy landed
  (@cc35d80925, held post-17:15Z), else twin advancement EXPECTED and noted, not a fail.
- **Leg (d) rename:** SUPPRESS-FROM-SERVING = delete the OBJECT; deleting a delete marker is
  PROHIBITED wave-wide (CTO 140448Z).
- **D1/PIN-2/PIN-3:** false-zero discriminator = roster expectations + silver-frontier
  cross-derivation, both; post-4a a 0 with current as_of is a defect on sight. UNDECLARED cadence
  blocks D1, never passes it. T-1 at D-1 IS fresh (NEVER#1).

## LATE-BREAKING (CTO 145251Z, AE~A finding, Andrew-routed) — binds citations + denominator

- **`aws events list-rules` is STRUCTURALLY BLIND to EventBridge Scheduler** (separate API; 11 live
  ENABLED schedules invisible, no incompleteness indication). D2 verdict UNCHANGED and strengthened
  (AE~A closed "nothing daily at 15:00Z" across BOTH systems — PIN-4(i) holds on a two-system
  enumeration).
- **The 15:45Z minute has TWO drivers across the two systems:** `etfs-canon-fanin-daily` (Rules,
  ETF fan-in → DDB) AND `mdpf-accrual-bridge-daily` (Scheduler, cron(45 15) UTC ENABLED — the
  v1.9.0 accrual bridge). Possibly two DIFFERENT legs, same minute. **At evidence time: pin the
  accrual leg's driver from the RUN'S OWN identity (which function wrote the artifact + its trigger
  payload), never from either clock table.** Cite the resource that did the work.
- **Every schedule claim in the certification prints a TWO-SYSTEM denominator** (`comp-trigger`
  gives it: N rules + M schedules, region). A Rules-only enumeration is false by construction.
- Methodological residual to include verbatim-class: AE~A's *"my conclusion survives; my method
  does not"* — the verdict was re-grounded on a wider instrument after the fact.
- Adjacent hard-dated flag (do not lose): **Aug-1 `etfs-reports-monthly-run` is a SCHEDULER entry**
  — a `list-rules` check reads it as unscheduled with full confidence.

## EVIDENCE COLLECTED (running log; certification writes from here)

**CHAIN LEG @15:05Z tick — EVENT PATH EXERCISED, ZERO HANDS, SELF-IDENTIFIED. CLEAN.**
- Marker ADVANCED (listing-verified, not Head): `opal-data-inf/gold/meta/pipeline-complete.json`
  135 B, ETag `1b39d06d5d54a919c7a3bc0f43d28a17`, LastModified 2026-07-29T15:02:30Z (baseline
  5ff381b4 / 07-28T15:04:07Z — AE~A's discriminator satisfied).
- Trigger identity FROM THE RUN'S OWN LOG (PIN-4(iii), the acceptance step that reads the trigger):
  RequestId 421dd1ec, event `"source": "aws.s3"`, detail-type "Object Created", same bucket/key,
  **etag in the event == the landed marker's etag**, event time 15:02:29Z. NOT aws.events — the run
  positively self-identifies as EVENT-FIRED, which is exactly what the pinned D2-as-scheduled FAIL
  + event-path claim predict. No anomaly.
- Convergence gate reasoning logged per-source: inflection fresh as_of 07-29; 49financial
  latest_partition 07-28 = trading_days_behind 1 (≤2) → FRESH BY TRADING CALENDAR (NEVER#1
  implemented correctly in production, worth naming in the cert); custody_source=schwab (the 07-24
  deprecation honored); all_fresh=true, stale_partners=[].
- Dispatch: runner i-02448edb624a7a7cf, SSM 34f8056f-25fa-4ff4-ad47-c6ef3b5a301c, run_date
  2026-07-29, detached; telemetry s3://opal-data-mdpf/telemetry/mdpf-daily-runner/. Chain
  COMPLETION (gold vintages) checked at the 15:50/16:20 ticks — dispatch is not landing.

**15:45Z LEGS @15:50Z tick — TWO legs, one clean, ONE CRASHED:**
- `etfs-canon-fanin` (Rules cron 45 15, ETF PRODUCT): fired unattended, 12 rows upserted to
  opal-etfs-ownership-daily (49f dates=07-28 T-1, inflection 07-29, cottonwood 07-27), own log
  RequestId c2ee44eb. Trigger payload NOT self-logged (evidence grade: in-window fire + single
  enabled trigger; stated as such). COO's four-clock table mislabeled this leg "accrual" — it is
  the ETF fan-in; corrected in my 155600Z.
- `mdpf-accrual-trigger` (SCHEDULER cron 45 15, MDPF accrual bridge v1.9.0): fired unattended
  15:45:21Z, dispatched SSM 85b3ef08 — **RUN CRASHED: AccessDenied, mdpf-daily-runner-ec2-role
  lacks s3:PutObject on opal-data-assets/portal/gold/mdpf/*** (run telemetry
  accrual-bridge-runs/20260729T154521Z.log, build_portal_gold_accrual.py:260; traceback names a
  07-27 key → bridge rewrites trailing dates, grant must cover the full write set). Dispatcher
  printed OK — dispatch rc, not run rc. **Gold tree ZERO writes today (newest 00:35:17Z)** → the
  16:15Z publisher republishes yesterday's vintages absent a ruling. Routed URGENT to CTO
  (fix-forward vs publish-stale, freeze posture theirs) + AE~A 155600/155608Z. D2 accrual-leg
  verdict shape: SCHEDULED FIRE EXERCISED, RUN FAILED ON GRANT — more informative than
  no-schedule, still not a pass.

**PUBLISHER LEG @16:20Z tick — SCHEDULED-AND-CERTIFIED CLEAN (on stale input, attributed):**
- Trigger identity from the run's own log: `"source": "aws.events"`, "Scheduled Event", resources =
  rule ARN `opal-assets-mdpf-portal-publisher-daily`, time 16:15:00Z. PIN-4(iii) FULLY satisfied —
  this is the gold-standard form.
- Published **11/11 derived (scope,type) pairs, all_present=True, missing=[]** — exact PIN-1 design
  set, derived not hand-listed, per-object ETags in the log (RequestId 6816c668).
- Vintages 07-27/07-28 (cottonwood 07-24) — YESTERDAY'S, exactly as predicted: the crashed bridge
  left gold unadvanced; the publisher correctly published latest-per-(scope,type). **The fire
  proved the SCHEDULE; it could not prove the DATA PATH** (bridge grant failure owns that).
  CTO-terminal comp-clobber --live corroborates independently: platinum keys 4 versions 4 etags
  ACTIVE_CLOBBER=False, global republished at identical 200,059 B.
- Twins: underscore keys advanced 15:05:22Z (chain Stage-4 still deployed; kill held post-17:15Z)
  — EXPECTED per protocol, noted not failed. Legacy `json/mdpf/*` plane shows textbook INTERLEAVED
  two-writer clobbers (CTO terminal) — that plane is the teardown wave's, not tonight's D3 set.

**Publisher-leg corroboration (COO 164052Z):** artifact `_provenance.written_at 2026-07-29T16:15:31Z`
discriminated run-from-no-run where bytes could not (output byte-identical to yesterday by design —
stale input). Independent second axis on top of my log-based aws.events evidence. **Banked caveat
for all cert reads: self-stamps read at ORIGIN only — a CloudFront read returned the PREVIOUS stamp
6 min post-fire (false NO-FIRE).** My platinum reads this session were s3api = origin; compliant.

## Sequenced after certification

comp-grep rc=2 flip (CTO GO 031744Z; I land, 0.8.0_AE verifies exit path — 3 fallback-exercisers,
stdout byte-identical, rc declared in advance) → then T-2 / T-3 specs (division 081209Z).

— 3.0.0_SA_CVO
