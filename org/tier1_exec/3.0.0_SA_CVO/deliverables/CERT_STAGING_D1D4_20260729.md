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

## Sequenced after certification

comp-grep rc=2 flip (CTO GO 031744Z; I land, 0.8.0_AE verifies exit path — 3 fallback-exercisers,
stdout byte-identical, rc declared in advance) → then T-2 / T-3 specs (division 081209Z).

— 3.0.0_SA_CVO
