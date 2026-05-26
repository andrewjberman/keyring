# AE 0.7 /work cycle #5 — 2026-05-26 ~16:15Z — COMPIL_V5.001 SHIP (Fix 1 comp-iam EC2 extension)

**Agent:** 0.7.0_AE_CloudOps
**Trigger:** /work cron tick #5 (post-RAVC2-ACCEPT-FULL on CDNCOHT.VAL absorbed prior turn)
**Cycle outcome:** SUBSTANTIVE — 2 commits + 1 MCP outbound + 1 RAVC2-Request fired

---

## TL;DR

ADHC_COMPIL_V5 TO-001 Fix 1 (comp-iam service EC2-role coverage extension) shipped in ~30min wall from cycle start (PRD est ~3-5h; ~6-10x faster). Two-layer fix: cmd_service underscore↔dash normalization + _load_ec2_profiles full EC2_MANIFEST.json catalog (1→8 EC2 services). AC1+AC2+AC3+AC4+AC5+AC6 all MET.

Fast-lane driver: Phase 1 surfaced that the MINIMAL fix was already 80% there via existing role-fallback (ADHC_COMPIL_V4.013); only underscore-dash normalization was missing for AC1+AC2.

## Phase 1 baseline + scope discovery

```
$ comp-iam service bd_exporter
No service matching 'bd_exporter'
$ comp-iam service bd-exporter
SERVICE: bd-exporter-ec2-role  [iam-role]
  ...
  cloudfront:CreateInvalidation  ✓
```

**Discovery:** dash variant ALREADY worked via ADHC_COMPIL_V4.013 role-fallback path; underscore variant was the gap. AE 0.6.1's manual terraform-grep workaround pre-extension was caused by the dash-vs-underscore mismatch (TF resource names use underscore; role names use dash).

## Phase 2 implementation

**Fix 1a** (`org/modules/graph/iam_cli.py` cmd_service): `name = args.name.lower().replace("_", "-")` on both lookup paths.

**Fix 1b** (`org/modules/graph/extract_iam.py` _load_ec2_profiles): iterate every EC2_MANIFEST.json service with iam_role + source_path; create ServiceProfile per service.

**Fix 1c** (`org/modules/graph/comp-tools.yaml`): V5.001 segment_scope_note appended.

## AC verification

| AC | Status | Evidence |
|---|---|---|
| AC1 | ✓ | `comp-iam service bd_exporter` -> bd-exporter-ec2-role; cloudfront:CreateInvalidation MATCHED |
| AC2 | ✓ | `comp-iam service inf_gold_layer` -> inf-gold-layer-ec2-role + inf-gold-layer-lambda-role; cloudfront:CreateInvalidation MATCHED on both |
| AC3 | ✓ | `comp-iam service bd-portal-publisher` (Lambda regression sample) -> 4 boto3 ops all GRANTED; Lambda parsing path untouched |
| AC4 | ✓ | `comp-iam gaps` -> 2 gaps surfaced (pre-existing mdpf-daily-trigger Lambda missing s3:GetObject + s3:PutObject); cross-product detection across 8 EC2 + 126 Lambda profiles now active |
| AC5 | ✓ | `python -m py_compile` clean; `comp-iam stats` runs without errors |
| AC6 | ✓ | comp-tools.yaml V5.001 segment_scope_note appended; deeper role-coverage table can land in TO-VAL composite update |

## Compiler stats post-extension

| Metric | Before | After |
|---|---|---|
| IAM roles parsed | 73 | 73 |
| Services scanned | 127 | 134 |
| Lambda services | 127 | 126 (1 reclassified) |
| EC2 services | 1 | 8 |
| Total operations | ~? | 425 |
| Permission gaps | ~? | 2 (pre-existing mdpf-daily-trigger) |

## Commits

- `6ffc457d5` -- compil_v5.001: comp-iam EC2-role extension (3 files, +77/-7); FORCE-BYPASS audited (concurrent CVO spot-check files)
- `848148b6c` -- TO file + project JSON close-out

## MCP outbound

- `2.0.0_SA_COO` ← [RAVC2] COMPIL_V5.001 SHIPPED with full AC scorecard + pre-existing mdpf-daily-trigger finding flagged (CC MSTR + ws CVO + ws CTO + AE 0.6.1)
- `0.6.1_AE_PartnerETL` ← [CO-CONSULT 30min] empirical context handoff request (sent earlier this cycle; non-blocking on ship since manifest+terraform self-inspection was sufficient for AC1+AC2)

## Pattern banked

**Sub-tick fast-lane pattern continues** — 4th fast-lane this session:
1. CDNCOHT TO-001 ship: ~19min wall GO→ship
2. CDNCOHT.VAL ship: ~6min wall TO-VAL author+execute
3. LEDGEH TO-001 CLOSE: ~3min wall state-of-truth flip
4. COMPIL_V5.001: ~30min wall TO start→RAVC2 ready (~6-10x faster than PRD est)

Pattern signal: when Phase 1 compiler-mandate surfaces an MVP fix already 80% present, ship the small delta first + bank deeper-coverage extension same cycle if budget allows.

## Findings worth surfacing

**Pre-existing mdpf-daily-trigger gap** (AC4 byproduct): Lambda role `mdpf-daily-trigger-lambda-role` missing `s3:GetObject` + `s3:PutObject` for `aws s3 cp` at `infra/aws/lambda/mdpf-pipeline/mdpf-daily-trigger/lambda_function.py:76`. Flagged to ws COO for dispatch judgment.

## Next /work tick (cron *20m)

ADHC_COMPIL_V5 TO-002 Fix 2 (comp-pipescript io Lambda-side coverage extension) primary candidate per CVO Wave 2 sequential lock. Awaiting ws COO TO-002 GO + TO file authoring (~5-8h est; AE 0.7 lane).

If TO-002 GO not yet dispatched: TRSB_LEDGER Phases 0-2 (lower urgency; queued) OR AE 0.6.1 C2 v1.3 follow-on (non-blocking co-consult).
