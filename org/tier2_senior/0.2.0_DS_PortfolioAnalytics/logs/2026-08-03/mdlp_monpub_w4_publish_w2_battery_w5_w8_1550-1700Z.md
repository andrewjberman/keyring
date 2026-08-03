# MDLP_MONPUB: W4 recovery published + witnessed, W2 battery complete, W5 + W8 code closed -- 1550-1700Z

**archetype:** MIXED
**secondary_archetypes:** DEPLOY, VALIDATE, IMPLEMENT

## Session Summary (second window; first: mdlp_monpub_w1_hold_w2_w3_code_1500-1550Z.md)

The SEV1 is HEALED: the portal serves the true T-1 frontier (data_as_of=2026-07-31) via the
W4 recovery publish, CVO-witnessed PASS 7/7 (10/10 ST periods to 2dp vs sitez's pin). The W2
guard is deployed AND fully exercised in the failing direction (CVO-witnessed battery). W5 and
W8 code legs committed. All deploy legs with DT.

## Timeline (2026-08-03 Z)

- 15:51 CTO two-rulings: W3 Choice-widening stands; W2 passing-leg defers to W4's recovery
  publish (named third state DEPLOYED-EXERCISED-PENDING-PASSING-LEG until then).
- 15:55-15:59 COO precision catch accepted + claim RESTATED on the record: my "SURFACE_ACK
  audited" named an audit line that never existed (safe-commit's own screen of the staged
  lambda file read no-critical-surface, so the env var was never consumed; ack lives in-commit/
  in-message -- the advisory half). Superset evidence filed: 2 real execution profiles, both
  fully paginated (first 2394c6bf fetch returned 100 events + nextToken -- the CLAUDE.md
  page-count trap caught before it entered evidence; full history = 166 events).
- 15:58 W4 handoff switched to option (b) per Andrew-direct: staging key
  data-refresh/staging/mdlp-monpub-w4/ designated (outside the event-wired uploads/ prefix).
- 16:01-16:07 sitez staged the corrected 07-31 data.pkl; my independent verify: downloaded +
  hashed (md5 2a4703465c00f76ce71094db5ae522c0, sha256 6cd02860...def0, both match). COO grant
  46d4b1110d enumerated me in YANG_PIPELINE_DEPLOY + DATA_REFRESH_DEPLOY (code lanes).
- 16:04-16:10 CTO GO -> W4 PROMOTE: pre-overwrite head-object confirmed the defective original
  (ETag 961a1f5a..., preserved in 4 archive locations -- the W2 crash fixture survives);
  corrected pkl promoted (multipart ETag != md5, so re-downloaded + re-hashed byte-identical);
  uploads/manifest.json (version 20260803_v2) written 16:08:19Z; trigger fired execution
  20260803_v2-c2ea0112 -> SUCCEEDED.
- 16:10-16:15 Post-publish verify: ALL THREE benchmark keys + json/macro/macro_data.json at
  data_as_of=2026-07-31 identical vintage; comprehensive ETag 0a122e2c95... -> ada142139b...;
  served ST row plausible (vols 2.44-3.25 vs garbage 20.79-27.79). CVO witness PASS @b16913d35e.
- 16:16-16:23 W2 battery legs A+B (direct invoke of deployed yang-v2.4.17 -- trigger-path
  deviation deliberate: R1 unguarded siblings would have regressed the estate; CVO later ratified
  as CORRECT): leg A clean-07-27 fixture -> PublishGuardError verbatim (requestId 42d7615e),
  zero writes; leg B the ORIGINAL defective 07-31 pkl (the input that wrote the serve 4x that
  morning) -> build-phase crash BEFORE any upload (requestId 2152f025), zero writes. BONUS
  FINDING: first leg-A attempt used the 2025-12-31 pkl -- it ALSO crashes on duplicate
  price_monthly labels (requestId b5fbd6d0) -> the dup condition is NOT unique to 07-31;
  forwarded to MSTR~Z's producer trace.
- 16:21 (production, not mine) real-user rebuild 20260803_v1-3796f456 from the corrected pkls:
  equal-date guard pass by design -- organic passing-direction exercise; new serve pins.
- 16:34 CVO witnessed A+B PASS via S3 VERSION-GAP proof (stronger than ETag compare); ruled
  leg C SCRATCH-ONLY.
- 16:45-16:50 Leg C on DT's IAM-verified scratch bucket opal-313476888478-yang-qa-scratch:
  control (no flag) -> PublishGuardError, seed ETag unchanged (requestId 672537d4); bypass
  (force_publish=true) -> SUCCESS, scratch flip 2ad52d9f(28B) -> b5221b71(19,221B),
  data_as_of=2026-07-27, verbatim FORCE_PUBLISH WARNING line (requestId b32c7fc2); live pins
  byte-identical throughout. 16:55 CVO witnessed -> W2 BATTERY COMPLETE @9ba99fcb5c.
- 16:41-16:58 W5 committed 5de42e3b7b (rollback picker hex-sort fix: full-partition paginate +
  startedAt sort before limit, EXECUTION + same-shaped SSCN partitions, denominator logged;
  in-Lambda-sort-vs-GSI tradeoff cited). W8 committed 4024664d71 (see below). W2/W3/W4 marked
  closed on my board; DT deploy legs remain for W5/W8.

## W8 (commit 4024664d71, both Lambdas, one event-contract commit)

- Fallback rollback now STAMPS the archived manifest (force_publish=true +
  rollback_execution_id) and the yang guard reads top-level OR manifest-level, logging the
  rollback id in the bypass line. The manifest is the ONLY SFN-reachable channel -- verified in
  yang-pipeline-definition.json: task Parameters pass manifest/processed/metadata only; a
  top-level flag would be silently DROPPED (the trap that would have shipped a deployed no-op
  reading as a fix).
- **STANDALONE DEFECT FIX (CTO-flagged for visibility, its own line): the pre-W8 fallback
  copied archive files to uploads/ in S3 LISTING ORDER, so uploads/manifest.json (which fires
  yang-pipeline-trigger) could land BEFORE "model YYYYMMDD v1.pkl" -- a latent
  trigger-before-data race on every re-processing rollback. W8's write-manifest-LAST closes it.**
- Grep gate: force_publish SET at exactly one call site (data_refresh :1466); yang only reads.
- Claim boundary: Path-1 version-based restore OUT OF SCOPE/unguardable (raw copy_object, no
  Lambda); DDB rollback record + fabric law are its controls. Named, not implied covered.
- CTO GO provenance: reached me via DT relay only (CTO confirmed sloppy addressing, 165848Z);
  the GO's one beyond-TO instruction (coherent-vintage ruling in the code comment) was already
  satisfied from the TO's own context block -- confirmed against committed source.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-blast | data-refresh x2 (PYTHONIOENCODING=utf-8) | PASS | radius unchanged; 07-17 ledger HOLD noted both runs |
| commit-gate.sh | 3 commits (W5, W8 pair) | PASS | non-ASCII WARNs pre-existing only |
| safe-commit.sh | 5dd8ddfe9c(log), 5de42e3b7b(W5), 4024664d71(W8) | PASS | W5+data_refresh clean under new lanes; W8 yang-source needed audited override (path-rule gap, flagged to COO) |
| aws stepfunctions/s3api/lambda/logs | promote + verify + battery | PASS | every mutation head-object-verified before firing (08-01 law); pagination trap caught live on 2394c6bf history |

What worked: state-machine Parameters inspection caught the dropped-flag trap BEFORE commit;
version-gap proof (CVO) > ETag compare -- banked. What failed: my first execution-watch loop
declared TERMINAL on a "None" page (sloppy grep exit condition -- harmless, re-checked directly);
first W8 commit blocked on the yang-source path-rule gap. Gap found: .owned-paths.yaml lacks a
rule binding infra/aws/lambda/v2_portal/yang_pipeline/** to YANG_PIPELINE_DEPLOY (COO to land,
same class as their :1470 fix).

## MCP Traffic

~14 in / 13 out this window. Significant: CTO two-rulings; COO evidence-claim correction
(accepted + restated); Andrew-direct option-(b) + staging key to sitez (bus 9f4129de); CTO W4
promote GO -> executed -> RAVC; CVO witness PASS x3 (W4 @b16913d35e, legs A+B @ff496d7621,
leg C/battery-complete @9ba99fcb5c); W5/W8 SHAs to DT; W8 provenance confirm loop with CTO.

## Blockers

- None at my seat. All remaining MDLP_MONPUB motion is with named owners: DT (W5+W8 deploys,
  one data-refresh cycle OK), CVO (W8 end-to-end scratch witness, env held seeded), COO (yang
  source path rule), MSTR~Z (producer trace; 2025-12-31 datum forwarded), CTO (W1 amended TO).

## Current State (zero-context handoff)

- SERVE: true T-1 frontier 2026-07-31 on all benchmark keys + estate; pins (post-16:23:50Z
  organic rebuild): comprehensive e94c4f129356c4af36b7f7cdd4b640fb. Guard live (yang-v2.4.17)
  and battle-proven; W2 marked WITNESSED-COMPLETE by CTO.
- COMMITS awaiting DT deploy: 5de42e3b7b (W5) + 4024664d71 (W8, both Lambdas). Yang side of W8
  needs a yang-v2.4.18 cycle; data_refresh side can carry W5+W8 together, ledger names both.
- SCRATCH: opal-313476888478-yang-qa-scratch seeded (fake served object b5221b71... at
  data_as_of=2026-07-27 post-bypass + 07-27 fixture pkl) -- HELD for W8 witnessing per CVO;
  7d self-expiry backstop. Do not clean.
- uploads/: corrected 07-31 pkls + 20251231 pair; manifest.json = 20260803_v2 (inert until next
  write). Defective 07-31 fixture preserved in 4 data-refresh/archive/exec-*/ locations.
- W1: BLOCKED (unchanged, 3 preconditions).

## Next Steps

1. [0.2.0_DT_PortfolioAnalytics] Deploy W5+W8 (data-refresh cycle, ledger names both) +
   yang-v2.4.18; then the W8 end-to-end scratch legs THROUGH handle_rollback (never
   direct-invoke) incl. the separate no-flag negative control; [3.0.0_SA_CVO] witnesses.
2. [2.0.0_SA_COO] Land the yang-source path rule (grantor lane, SoD).
3. [0.2.0_DS_PortfolioAnalytics -- me] Support W8 exercise design if DT asks; act on W1's
   amended TO when it lands; stay event-driven.
