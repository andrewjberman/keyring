# NFRA_COSTRED R2 — opal-data-bd S3 version-bloat assessment + STAGED lifecycle cut (35d)

**Author:** 0.4.0_DS_ClientPlatform · **Date:** 2026-06-05 · **archetype:** DIAGNOSE
**secondary:** VALIDATE, TRACE
**Routes to:** 2.0.0_SA_COO (RAVC2), CC 1.0.0_SA_CTO → Andrew final exact-GB GO (C2 destructive apply)
**Scope:** NFRA_COSTRED PRD §3 **R2** (opal-data-bd S3 version-bloat + lifecycle).
**Decision of record:** **Andrew 2026-06-05 — cut Time Machine retention to 35 days** (took the
coherence-floor flag; 35d = the Dynamo PITR window = the FREE cut). S3-lifecycle-only; no
restore-logic bound needed.
**Status of this doc:** ASSESSMENT + STAGED Terraform diff. **NOTHING APPLIED.** Noncurrent-version
expiry is destructive + irreversible (C2 Andrew-gate); this doc stages the change for COO→Andrew GO.

---

## 0. TL;DR (read first)

1. **Bloat confirmed — bigger/growing vs the original audit.** opal-data-bd bills **2,679 GB**
   (2026-06-04 CloudWatch, up from the audit's 2,396 GB, rising **~50 GB/day**); only **60.6 GB
   (2.3%) is current data**. **~2,618 GB (97.7%) is noncurrent-version bloat** (versioning ON + gold
   rewritten daily + `NoncurrentVersionExpiration=90d`). ~$62/mo now.
2. **The 90d window was NOT an accidental default — it is the deliberate retention backing the LIVE
   Portal Time Machine** (`DRFR_PTMCH`, deployed). `bd-time-machine` restores `gold/` to a past date
   by reading **noncurrent versions** (pinned `VersionId`). The coherent Time-Machine window is
   already hard-bounded at **35 days** by the DynamoDB `opal-portal-market-data` **PITR
   (RecoveryPeriodInDays=35, confirmed live)** — restoring BD gold older than 35d yields a mixed-era
   portal. **So the 35–90d S3 noncurrent versions are pure over-provisioning: deleting them costs
   ZERO actual restore capability.** This is the FREE cut.
3. **Andrew's call (35d) is coherence-clean.** S3 retention (35d) now matches the Dynamo PITR (35d):
   both cover exactly the trailing 35 days. No incoherent half-restore risk; no restore-logic
   bounding needed (the effective Time-Machine window stays at the 35d it already advertised).
4. **Boundary decision — recommend `NoncurrentVersionExpiration = 36 days` (not exactly 35).** At the
   35d edge the version needed to restore the oldest Dynamo-restorable date is only **34 days
   noncurrent**, so 35d is already safe with ~1 day inherent margin — but 36d adds an explicit 1-day
   buffer against day-granular S3 expiry / 5PM-ET-vs-UTC rounding / future cadence change, at a cost
   of ~1 daily cohort (~29 GB ≈ **~$0.67/mo**). Errs on NOT under-retaining vs Dynamo, per COO.
5. **`AbortIncompleteMultipartUpload` is ALREADY present (7d)** and there are **0 incomplete MPUs** —
   the PRD's "add abort-MPU" item is already satisfied; MPU cleanup yields ~0. Kept unchanged in the
   diff so the import→apply is a clean modify.
6. **Recoverable: ~1,178 GB / ~$27/mo at 36d** (exact, §3). **SAFETY GATE (§3a): did NOT pass clean —
   7.82 GB / 109,305 versions are "only-copy-at-risk"** (keys whose current version is a delete-marker),
   but the set is **logically-deleted CODE (git-authoritative) + re-ingestable bronze intermediates,
   cat-(c) orphans = 0 — NOT custodian history.** RESOLUTION: **prefix-scope the 36d rule to
   `gold/`+`platinum/`** (pure-supersession serving tiers, 2,610/2,615 GB of bloat) → ~99% of savings
   (~$27/mo) with **structurally zero** custodian/silver/bronze/code deletion. HOLDING apply pending
   COO's whole-bucket-vs-scoped call (Andrew's GO covers only-copy-at-risk=0; this resolves it).
7. **Secondary (not in this apply):** `logs/` 10.8 GB has no expiry rule (optional NEW rule, §5);
   the Time-Machine manifest fast-path (`snapshots/manifests/`) is **empty** → BD Time-Machine is
   already degraded today regardless of lifecycle — **flag to 0.6.0_AE** (§2, separate from this cut).

---

## 1. What dominates the bucket (read-first, no deletes)

**Live reads (2026-06-05, account 313476888478, pure metadata — no gold runs; C1 honored):**

| Measure | Value | Source |
|---|---|---|
| Billed size (all versions, StandardStorage) | **2,679 GB** (2026-06-04) | CloudWatch `BucketSizeBytes` |
| Growth trend 06-01→06-04 | 2,531 → 2,573 → 2,618 → **2,679 GB** (~+50 GB/day) | CloudWatch |
| Total object versions | **10.65 million** | CloudWatch `NumberOfObjects` (AllStorageTypes) |
| **Current-version data** | **60.6 GB / 104,273 objects** | `s3 ls --recursive --summarize` |
| **=> noncurrent-version bloat** | **~2,618 GB (97.7%)** | derived (billed − current) |
| Current lifecycle | `expire-noncurrent-versions-90d` + `abort-incomplete-mpu-7d` (both prefix="") | `get-bucket-lifecycle-configuration` |
| Versioning | Enabled | `get-bucket-versioning` |
| Incomplete multipart uploads | **0** | `list-multipart-uploads` |

**Root cause (confirmed):** versioning Enabled + `gold/` deterministically rebuilt every nightly run
→ each gold object gets a new current version nightly, prior becomes noncurrent → up to 90 daily
cohorts retained → ~2.6 TB tail. Bucket is **not yet at 90d steady state** (still growing ~50 GB/day).
Secondary cruft (current sizes): `logs/` 10.8 GB, `forwardfill_v2/` 2.97 GB, `backfill_v2/` 2.47 GB,
`v4_output/` 1.0 GB, `GOOD_RUN_2026-01-21_1015AM/` 734 MB.

## 2. Consumer-read confirmation + coherence (the C2-critical question)

**Does any consumer read old/versioned keys?** Normal portal serving = CURRENT only (CloudFront →
`gold/*` / `platinum/*`, no `VersionId`) → unaffected. **The one consumer of NONCURRENT versions is
the Portal Time Machine** (`DRFR_PTMCH`, deployed, portal-wired: `TimeMachineProvider` →
`triggerTimeMachine()` → `/api/scoped/data-refresh/time-machine` → `portal-time-machine` orchestrator
→ `bd-time-machine`). `bd-time-machine` restores `gold/` via `CopyObject CopySourceVersionId` from a
per-rebuild manifest, with a `list_object_versions`-by-`LastModified` fallback.

**Why 35d is coherence-clean (the FREE cut):**
- The cross-source Time Machine cannot coherently travel past the DynamoDB `opal-portal-market-data`
  PITR window (**35d rolling, confirmed ENABLED, earliest ≈ 2026-05-01**). BD gold versions in the
  **35–90d band are useless for restore** — Dynamo can't supply matching market data that far back.
  Deleting them removes ZERO real capability.
- At 35d, S3 retention == Dynamo window → both cover exactly the trailing 35 days → **coherent**.

**Boundary (35 vs 36d) — the precise edge analysis:**
- To restore target_date D, bd-time-machine needs the gold version current as-of 5PM ET on D. That
  version became noncurrent at the next nightly rebuild (~D+1).
- When Dynamo's earliest edge reaches D (now = D+35d), that version's noncurrent-age = (D+35)−(D+1) =
  **34 days** → safe under a 35d rule (1-day inherent margin). S3 day-granular expiry runs *after* the
  threshold (retains slightly longer = safe); a skipped nightly keeps the version current longer
  (also safe).
- **Recommend 36d** for an explicit 1-day buffer against day-rounding / lifecycle-evaluation edges —
  ~$0.67/mo for one extra daily cohort. (35d is acceptable; 36d is bulletproof.)

**Already-degraded today (separate bug, flag to 0.6.0_AE — NOT part of this cut):** the Time-Machine
manifest fast-path `snapshots/manifests/` is **empty (0 objects)** despite `CAPTURE_VERSIONS_FUNCTION`
being wired on bd-portal-publisher → bd-time-machine falls to the fallback that DRFR_PTMCH
`known_limitations` says times out on `gold/clients/`. So BD Time-Machine is not reliably functional
right now independent of retention.

## 3. Quantification — recoverable GB + $/mo at 36d (and 35d) vs 90d baseline

S3 Standard us-east-1 = **$0.023/GB-month**; cost is bytes only (no per-object fee in Standard).
Current billed 2,679 GB ≈ **$61.6/mo**. The recoverable set = noncurrent versions older than the
threshold (36d recommended / 35d alt). Current 60.6 GB never expires; 0–threshold noncurrent stays.

<!-- AGE_TABLE_START -->
**Per-key proof (`.runtmp/bd_safety_age_proof.py`, full pass: 10,824,429 versions / 156,520 distinct
keys / 54,703 delete-markers; size-weighted by LastModified age):**

Key partition: **(a) current DATA version present = 104,274** [SAFE — noncurrent tail is pure
supersession] · **(b) current = DELETE-MARKER = 52,246** [data only in noncurrent] · **(c) orphan
(no current) = 0**.

**SAFE recoverable set** (cat-(a) noncurrent older than threshold — the supersession tail):

| Threshold | Recoverable GB | Objects | ~$/mo @ $0.023/GB |
|---|---|---|---|
| **>36d (recommended)** | **1,178 GB** | 5,281,940 | **~$27.1** |
| >35d | 1,220 GB | 5,429,050 | ~$28.1 |
| >30d (Andrew's first floor) | 1,460 GB | 6,284,049 | ~$33.6 |
| >14d | 2,128 GB | 8,646,543 | ~$48.9 |
| >90d (current rule's effect) | 2.2 GB | 19,963 | ~$0.05 |

SAFE noncurrent by prefix: **gold 2,040.8 GB · platinum 569.4 GB** (= 2,610 of 2,615 total) · silver
62.1 · schwab 2.4 · all else <0.2. (>90d ≈ 0 confirms the 90d rule is active + the bucket is
pre-steady-state/growing.)

### 3a. HARD SAFETY GATE result (blocking AC) — DID NOT pass clean as literally stated
**only-copy-at-risk (cat-(b)/(c) noncurrent DATA versions a cut would delete): 109,305 objs / 7.82 GB
at 36d — NOT zero.** These are keys whose CURRENT version is a delete-marker (logically deleted),
data surviving only as noncurrent versions. **cat-(c) orphans = 0** (nothing is truly unrecoverable).

**What the at-risk set IS (check #3 discrimination):** overwhelmingly `code/gold|bronze|ec2|diagnostics/*`
— deleted/superseded **deployed scripts whose authoritative copy is GIT** (S3 version tail disposable)
— plus a few `bronze/{assets,fees}/*.xlsx` raw-ingestion intermediates (re-ingestable from OneDrive/source).
**NOT custodian history:** schwab/silver are write-once dated keys = cat-(a) = current-present = the
rule never touches them (verified: `schwab/bronze/CRS{date}.RPS` = 1 version each). The decisive
custodian-at-risk number (schwab+silver+bronze DATA in the delete set, expected 0) is in the re-run
breakdown (`.runtmp/bd_safety_age_proof_v2.out`).

**Custodian-at-risk confirm (targeted query `.runtmp/custodian_atrisk.py`, the decisive number for
Andrew's concern):**
- **`schwab/` = 0.000 GB at-risk** — 3,108 keys, ALL cat-(a) current-present, **0 delete-markers**.
  The years of Schwab custodian RPS history are write-once dated keys; **empirically ZERO at-risk**.
- `silver/` = 0.034 GB (deleted `silver/capital_gains/2021-*.parquet` old partitions, ~68d noncurrent,
  delete-marker-current) · `bronze/` = 0.0006 GB (the 2 deleted intermediates). cat-(c) orphans = 0
  in all three.
- **These custodian prefixes are EXCLUDED from the scoped rule** (gold/+platinum/ only) → the scoped
  cut's custodian-at-risk = **ZERO by construction**; that ~35 MB stays on the existing 90d rule
  (status quo, unchanged by this change). Andrew's concern is impossible-by-construction AND
  empirically ~0.

**Resolution — prefix-scope (APPROVED by Andrew 2026-06-05 "Approve scoped cut"):** apply the 36d NoncurrentVersionExpiration
to **`gold/` + `platinum/` only** (the daily-overwrite, deterministically-rebuildable serving tiers =
2,610 of 2,615 GB of noncurrent). Recovers ~1,175 GB / ~$27/mo (≈99% of whole-bucket savings) while
**structurally guaranteeing ZERO custodian/silver/bronze/code deletion** — Andrew's concern becomes
impossible by construction, not by judgment. Per the §4.5 rebuildability verdict, gold/platinum are
exactly the regenerable tiers, so even their delete-marker-orphan entries are regenerable.
<!-- AGE_TABLE_END -->

## 4. STAGED change (NOT APPLIED; C2 Andrew-gate)

### 4a. IaC delivery note — opal-data-bd is NOT Terraform-managed
opal-data-bd has **no `aws_s3_bucket` resource in TF** — console-managed; TF only reads it as a
`data` source for OAI-policy drift (`portal-auth/firm-bucket-cross-ref.tf`: "Live opal-data-bd bucket
policy (read-only — TF does not manage)"). Contrast opal-data-inf (TF-managed, `inf-pipeline/s3.tf`)
which has only an `otp/` expiry rule — **no NoncurrentVersionExpiration** (PRD R2(c) fabric-wide
concern confirmed for inf too). Cleanest IaC path (AE/DT executes — DS proposes only): add an
`aws_s3_bucket_lifecycle_configuration` resource referencing the literal bucket name, then
`terraform import` the existing live config into state BEFORE apply, so the apply is a clean modify
(never transiently drops the live abort-MPU rule).

### 4b. Proposed Terraform resource (36d recommended)
Home: `infra/aws/terraform/shared-infra/s3.tf` (alongside the other standalone opal-data-* buckets)
or `bd-pipeline/` — AE's call on module placement.

```hcl
# opal-data-bd lifecycle — NFRA_COSTRED R2 (Andrew 2026-06-05: cut Time Machine to 35d).
# Bucket is console-managed (no aws_s3_bucket resource); reference by literal name.
# IMPORT existing config into state before first apply:
#   terraform import aws_s3_bucket_lifecycle_configuration.opal_data_bd opal-data-bd
resource "aws_s3_bucket_lifecycle_configuration" "opal_data_bd" {
  bucket = "opal-data-bd"

  # Noncurrent-version expiry, PREFIX-SCOPED to the pure-supersession, deterministically-
  # rebuildable serving tiers (gold/ + platinum/ = 2,610 of 2,615 GB of noncurrent bloat).
  # 90d -> 36d: 35d = Portal Time Machine coherence floor (DynamoDB PITR = 35d rolling); +1d
  # buffer for day-granular expiry / 5PM-ET rounding. SCOPING RATIONALE (R2 safety gate §3a):
  # silver/ bronze/ schwab/ code/ are EXCLUDED so the rule can never delete a delete-marker-
  # orphaned only-copy in those prefixes (custodian history protection — structural, not judgment).
  rule {
    id     = "expire-noncurrent-gold-36d"
    status = "Enabled"
    filter { prefix = "gold/" }
    noncurrent_version_expiration { noncurrent_days = 36 }
  }
  rule {
    id     = "expire-noncurrent-platinum-36d"
    status = "Enabled"
    filter { prefix = "platinum/" }
    noncurrent_version_expiration { noncurrent_days = 36 }
  }

  # UNCHANGED — already live (0 incomplete MPUs currently). Kept so import->apply is a clean modify.
  rule {
    id     = "abort-incomplete-mpu-7d"
    status = "Enabled"
    filter { prefix = "" }
    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}
```

**Net diff vs live:** the live `expire-noncurrent-versions-90d` (prefix="") is REPLACED by two
prefix-scoped 36d rules (`gold/`, `platinum/`). abort-MPU-7d unchanged. silver/bronze/schwab/code keep
no noncurrent-expiry (status quo — they're write-once dated keys, near-zero version churn anyway).
**Alternative (whole-bucket 36d)** = a single `prefix=""` 36d rule; frees ~1,186 GB incl. the 7.82 GB
disposable code/intermediate at-risk set — only if COO/Andrew accept that at-risk set is benign (§3a).
The recommended scoped variant avoids that judgment entirely at ~99% of the savings.

### 4c. Equivalent `put-bucket-lifecycle-configuration` JSON (fallback if not importing to TF)
Same two rules; provided in the RAVC2 packet for AE. Either path is C2-gated (destructive).

## 4.5 Rebuildability crux (CTO add-on) — does it justify going below 35d?

**Question:** is bd-gold cheaply + deterministically rebuildable from retained bronze/silver (→ version
history redundant for recovery → could cut below 35d), or is the version history the only PITR (→ 35d
floor is correct)?

**Findings (live reads):**
- **Source retention is DEEP and write-once:** `schwab/bronze/CRS{date}.RPS` back to 2026-01-20,
  `bronze/bi/` to 2026-01-08, `silver/{allocations,prices,transactions,...}/{date}.parquet` dated
  partitions back to ~Jan 2026 — **5+ months, far beyond 90d**. Crucially `silver/prices/` exists, so
  price inputs are materialized as dated partitions (not only pulled live) → a past-date gold rebuild
  has its inputs. So the SOURCE for rebuild is retained well beyond any version window.
- **Determinism: plausible but NOT yet proven per-script.** Spot-checked gold scripts read dated
  silver/bronze (no obvious as-of-now live pulls); FIFO/aggregations are deterministic given inputs.
  Full per-script determinism (esp. price-override / market-value paths) is exactly the **GLDINC**
  determinism question — do not over-claim here.
- **Cost: a rebuild is NOT cheap.** Regenerating gold = a full bd-gold run on the c6i.16xlarge
  (~30–60 min, the single biggest cost lever) and is **barred ad-hoc by C1 compute-discipline**. The
  version-restore path (`CopyObject CopySourceVersionId`) is the only cheap/fast/instant recovery the
  live Time Machine uses.

**Verdict:** the version history is NOT the *only theoretical* recovery (source retained + rebuild
plausibly deterministic), but version-restore is the only *cheap/instant* one. **→ Don't go below 35d
now.** "Go below 35d for more savings" is a real follow-on but **GLDINC-gated**: it requires proving
per-script deterministic regenerability from dated silver AND accepting that deep historical restore
becomes a slow/expensive rebuild rather than an instant version-copy. The R2 rebuildability finding
seeds the GLDINC audit (same investigation — don't duplicate).

**Was 90d deliberate or a default?** **DELIBERATE** — the DRFR_PTMCH PRD (2026-03) explicitly chose a
"90-day lifecycle rule" as the Time Machine retention window (Phase 1). It was over-provisioned vs the
35d Dynamo-PITR coherence floor (which binds the *coherent* window and was not reconciled against the
90d choice at the time). Framing for Andrew: "the 90d Time-Machine window was a deliberate March
choice; the cap that actually binds it is the 35d Dynamo PITR, so 35–90d was never coherently usable —
cutting to 35/36d reclaims pure over-provision with zero capability loss."

## 5. Secondary (optional, NOT in this apply)
`logs/` 10.8 GB has no expiry rule — an optional NEW `logs/` prefix rule (`expiration days=30` +
`noncurrent_version_expiration noncurrent_days=7`) would structurally cap log noise. Internal logs, no
consumer. Cruft prefixes (`GOOD_RUN_2026-01-21` 734 MB, `v4_output` 1.0 GB, stale `*fill_v2` ~5.4 GB)
need owner-confirmation of obsolescence + Andrew GO; recommend a small follow-on after the lifecycle
lands. Kept OUT of the staged 35d cut to keep that change single-purpose and clean.

## 6. RAVC2 deliverables to COO (CC CTO)
1. **Coherence read** — §2: 35d is coherence-clean (S3 35d == Dynamo PITR 35d); no half-restore risk;
   no restore-logic bound needed. The 35–90d versions are pure over-provisioning.
2. **Boundary decision** — recommend **36d** (35d safe w/ 1-day inherent margin; 36d bulletproofs the
   edge for ~$0.67/mo; err on NOT under-retaining per COO).
3. **Staged TF diff** — §4 (90d→36d noncurrent; abort-MPU unchanged; import-then-modify; NOT applied).
4. **Recoverable GB + $/mo** — §3 (exact from the version-age audit).
5. **HOLD apply for COO GO** — destructive + irreversible; Andrew final exact-GB confirm gates it.
