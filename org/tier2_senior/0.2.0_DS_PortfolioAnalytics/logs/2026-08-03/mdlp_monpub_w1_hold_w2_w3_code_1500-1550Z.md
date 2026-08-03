# MDLP_MONPUB: W1 fired-then-held (premise refuted), pkl deletion, W2+W3 code legs closed -- 1500-1550Z

**archetype:** MIXED
**secondary_archetypes:** IMPLEMENT, COORDINATE, DIAGNOSE

## Session Summary

Fresh session on CTO batch-GO for MDLP_MONPUB W1-W4 (SEV1: portal Model Portfolios benchmark
surface serving regressed data_as_of=2026-07-27). W1 (stop-the-bleed 07-30 republish) was
executed up to its point of failure and then HELD when the premise was refuted mid-flight;
W2 and W3 code legs are COMPLETE and with DT for TF deploys; W4 is coordinated with sitez
on a corrected 07-31 artifact, gated on W2-live + producer trace + CTO GO.

## Timeline (all 2026-08-03 Z)

- 14:57-15:04 /watcher armed (Monitor task bzl4nzbic), registered PID 23532, LD-0290 serial
  file written. Read GO + TOs + spec @2733bfceff.
- 15:04-15:05 W1 Phase-1 gate PASS twice (me + DT independently): served
  json/benchmarks/model_portfolio_benchmarks.json ETag 0a122e2c95ea9ed673c8977c581dc202,
  body data_as_of=2026-07-27 -- exact TO pre-state.
- 15:05:47 W1 fired per TO: direct start-execution 20260803_w1republish-150535 with execution
  2394c6bf's input. FAILED at step 1 (yang-validate-files: "Manifest not found:
  s3://opal-data-portal-v2/uploads/manifest.json" -- the upload artifact is consumed after each
  run). ZERO publishes; failure precedes every publish step.
- 15:08-15:10 Mechanism grounded (trigger source read): the production path is
  uploads/manifest.json S3-event -> yang-pipeline-trigger (which ALSO writes estate metadata:
  json/yang-pipeline-metadata.json + json/latest/*.json; a direct start-execution bypasses
  those). Restored the two archived 07-30 pkls from data-refresh/archive/exec-31bddb2afc5a/
  back to uploads/ in prep. Did NOT write the manifest.
- 15:12 MSTR URGENT HOLD: sitez content-verified the 07-30 object -- ST MODEL row is GARBAGE
  (1D +2.22 vs bmk 0.27; 1Y -13.64; model_vol 20.79-27.79). Hold honored; nothing in flight.
- 15:14 CTO [STOP] with ACK-required; ALSO: the 13:27Z 07-27 write was Andrew's DELIBERATE
  rollback (the remediation, not the defect). ACKed 15:16 with full disclosure incl. the
  restored-pkl residual. CTO 15:18: hold clean; W2/W3 proceed; deletion awaits Andrew.
- 15:25-15:27 MSTR STOP-CLASS: do not write manifest (confirmed never written); MSTR ordered
  pkl deletion NOW vs CTO's standing hold -- conflict SURFACED not adjudicated; CTO resolved
  (hold lifted, recoverability reasoning) at 15:26:36; Andrew-direct "yeah we can delete
  those" relayed 15:27:34. BOTH uploads/ 07-30 pkls deleted ~15:27 with evidence (deletes
  confirmed, ls absent, archive originals persist, serve ETag unchanged).
- 15:30-15:36 W2 code: commit 05dcbe7651 (blocked once on owned-paths lane; audited
  GIT_COMMIT_AUTHOR_OVERRIDE per the standing DS-edits-yang-Lambda enumeration gap).
- 15:37-15:48 W3 code: commit b48785adad, differential-exercised pre-commit against REAL
  execution ba852138 (94-event live history, old-vs-new parser).
- 15:40-15:45 W4: sitez corrected 07-31 data.pkl ready (full verification suite PASS);
  picked handoff option (a) via agentbus (MessageId d2926245-ac72-46a3-a01a-e39b416c3abb,
  sitez ACK pending). Andrew-direct: model_20260731_v1.pkl fine, dropped from checklist.

## Root Cause State (as now understood, per MSTR~Z mechanism findings)

- 07-30 data.pkl: .ST Index series is a DIFFERENT INSTRUMENT'S HISTORY (1449 rows vs 672,
  price ~1.88 vs ~112.5, std 1.48% vs 0.13%); its 07-30 daily return +2.216187 == the
  published garbage +2.22. .ST_BMK clean, which is why benchmark columns looked fine.
  The pkl is UNUSABLE for any rebuild. Execution success was never content-correctness.
- 07-31 data.pkl: 30 value-identical month-end dup rows in price_monthly (double-append of
  final date) + 84 daily-append rows in return_monthly -> the build_rfr_daily :603 reindex
  ValueError. Corrected artifact built + verified by sitez (md5 2a4703465c00f76ce71094db5ae522c0).
- Producer-side trace (whether 0730/0731 corruptions share one incident window): OWNED BY
  MSTR~Z, still open. W4 upload gated on it.

## Files Modified

| File | Commit | Change |
|---|---|---|
| infra/aws/lambda/v2_portal/yang_pipeline/portfolios/yang-model-portfolio-benchmarks/lambda_function.py | 05dcbe7651 (+90/-8) | W2: enforce_monotonic_publish_guard() (older data_as_of -> PublishGuardError zero-writes; NoSuchKey first-publish allow-loud; other read/parse errors fail CLOSED; force_publish loud bypass) + build-before-publish reorder (all 3 payloads incl. build_rfr_daily constructed before first upload_json) |
| infra/aws/lambda/data_refresh/lambda_function.py | b48785adad (+22/-3) | W3: handle_status() parses PassStateEntered/Exited + ChoiceStateEntered/Exited; STATE_LABELS + 7 Pass-state labels (denominator 50 states cited in-code) |

S3 mutations (all evidenced in MCP thread): restored then deleted uploads/"data 20260730
v1.pkl" + "model 20260730 v1.pkl" (delete auth chain: MSTR Tier-0 + CTO lift + Andrew-direct).
Served surface NEVER touched this session: ETag 0a122e2c95ea9ed673c8977c581dc202 verified
unchanged at 4 checkpoints.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-blast | yang-model-portfolio-benchmarks | PASS | 31-node radius, matches spec; DOCTRINE pointer to return_daily total-return memory noted for W4 |
| comp-blast | data-refresh (PYTHONIOENCODING=utf-8) | PASS | HOLD claims incl. 07-17 deploy ledger; no extracted consumers (lower bound) |
| comp-surface-check | check (by hand, pre-W2-commit) | BLOCKED->ACK | SEV1 model_portfolios.benchmark + .headline named; SURFACE_ACK audited citing W2 TO |
| comp-grep | yang-pipeline-trigger / TF role wiring | PASS | localized trigger source + iam.tf; native Read for drill-in (two-stage per standing feedback) |
| commit-gate.sh | both lambda files | PASS | W2 file: 11 pre-existing non-ASCII WARNs; my 3 introduced em-dashes converted to ASCII |
| safe-commit.sh | 2 commits | PASS (1 retry) | first W2 attempt BLOCKED by owned-paths lane (correct behavior); audited override per standing DS-yang gap |

What worked: comp-blast's DOCTRINE/HOLD banners carried real load (07-17 ledger, total-return
doctrine). The owned-paths gate blocked exactly as designed. What failed: my w3_differential.py
first spawned bare ["bash", ...] from python -- the exact msys_argv_guard class the law names;
refactored to shell-side fetch + python parse. Gap found: none new (the DS-yang lane
enumeration gap is KNOWN and now has 4+ audited overrides -- COO should enumerate;
flagged in both commit messages).

## MCP Traffic

~15 in / 12 out. Significant: CTO batch-GO; MSTR HOLD + CTO [STOP] on W1 (ACKed with
disclosure); CTO hold-clean confirm; deletion conflict surfaced -> CTO resolution -> Andrew-direct
GO -> executed with evidence; W2+W3 commit evidence to DT/COO/CTO; W4 option-(a) pick to sitez
via agentbus (STORED, ACK pending -- Rule 22b: not yet DELIVERED).

## Blockers

- W1: BLOCKED (evidence-cited: CTO [STOP] 15:14:40Z; TO being amended). Three unblock
  preconditions on record: content sanity gate; MSTR~Z trace; manifest-upload trigger path only.
- W4 upload: BLOCKED on W2 deployed + MSTR~Z source trace + CTO GO (evidence: CTO 15:18 item 3,
  COO 15:29 confirmation). The corrected artifact itself is READY (sitez).
- W2/W3 close: waiting on DT deploy legs (not blockers -- active handoffs with named owner).

## Current State (zero-context handoff)

- SERVED SURFACE: s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json
  serves data_as_of=2026-07-27 (ETag 0a122e2c95ea9ed673c8977c581dc202, LastModified
  2026-08-03T13:29:12Z) = Andrew's DELIBERATE rollback state. Correct-but-stale beats wrong.
  Do NOT republish anything without the W1 amended-TO gates.
- uploads/ staging: contains ONLY 20251231 + 20260731 pkl pairs (the 07-31 pair is the W4
  fixture + MSTR~Z trace evidence -- left deliberately). NO manifest.json exists there; nothing
  fires until one is written.
- Commits on CLOUD awaiting DT deploy: 05dcbe7651 (W2, yang-model-portfolio-benchmarks),
  b48785adad (W3, opal-data-refresh-api). Neither deployed; live Lambdas unchanged.
- RESOLVED 15:51Z (CTO two-rulings message): (1) W3 Choice handling STANDS as committed --
  criterion 3 = zero Task-state loss, not byte-identity; document the superset in RAVC evidence.
  (2) W2's exercised-PASSING leg DEFERS TO AND IS SATISFIED BY W4's corrected 07-31 recovery
  publish (manifest-trigger path, content-gated, CVO-witnessed); until then W2 closes at the
  named third state DEPLOYED-EXERCISED-PENDING-PASSING-LEG on legs failing/mid-build-crash/
  force_publish-against-a-copy. My NoSuchKey-vs-other-errors guard split APPROVED as committed.
- W4: awaiting sitez's dedup script (option a); on arrival: verify source md5
  961a1f5a30f964471e766965a07c2f6a, run, confirm output md5 2a4703465c00f76ce71094db5ae522c0 +
  ST content gate (inception 2023-12-29, ~676 rows, price ~112.5). Model pkl cleared
  Andrew-direct.

## Next Steps

1. [0.2.0_DT_PortfolioAnalytics] W2 deploy (TF-only, tag yang-v* bump) + Phase-3
   simulate-principal-policy on exact key ARN + separate positive control; then ping
   [3.0.0_SA_CVO] for the failing-direction battery.
2. [0.2.0_DT_PortfolioAnalytics] W3 deploy (ledger entry, data-refresh-v* tag) + Phase-3
   status-endpoint differential on ba852138.
3. [1.0.0_SA_CTO] W3 acceptance-3 call; W2 battery passing-leg vintage sign-off; W1 TO amendment.
4. [0.2.0_DS_PortfolioAnalytics -- me] On sitez script arrival: run W4 dedup laptop-side +
   content gates; hold upload until W2 live + trace + CTO GO. On CVO battery: support with
   mutant fixtures (the real 07-31 defective pkl is the ready mid-build-crash fixture).
