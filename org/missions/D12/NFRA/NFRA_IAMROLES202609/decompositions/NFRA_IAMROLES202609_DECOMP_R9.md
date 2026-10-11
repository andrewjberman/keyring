# NFRA_IAMROLES202609 -- L5 DECOMPOSITION, ROUND 9 (narrow the dead global bucket names; schwab's dead reader first)

**Cut by** `2.0.0_SA_COO~ZI` **at L5, 2026-10-11.**
**Consumes:** `1.0.0_SA_CTO~Z`'s round-8 analysis `ledger/ROUND_ANALYSIS.round8.md` @`d14162158d` (ENRICHMENT LIST E1-E4,
the rulings table; msg 33361), and `deliverables/0.7.0_AE_CloudOps~IR/round8/DEAD_BUCKET_SWEEP.md` @`4aaba2fa6a`.

Rounds 1-8 stay in place. This is a ninth file, not an edit. FWD-4 stays REALIZED; this round is enrichment.

---

## 1. THE RECTANGLE

| cell | item | names / roles (live read at the cut, section 2) | surface | issued to | risk |
|---|---|---|---|---|---|
| `IAM-z-1` | E1: narrow 5 dead names, resource grain, write-bearing first | `ajb-workflow`, `opal-data-portal-s3` (workspace-sync-lambda-role); `opal-data-smartx-v2` (infrastructure-ops-lambda-role, smartx-exporter-role-2025..., smartx-ingestion-lambda-role); `opal-market-update` (FredIngestionLambdaRole); `opal-data-smartx`, read-only (smartx-exporter-role-2025...) | `shared-infra/iam_legacy.tf`, `smartx-pipeline/iam.tf`, `fred-pipeline/iam.tf`, or the IAM API where a role is not declared | `0.7.0_AE_CloudOps~IR` | WORLD |
| `IAM-z-2` | E2: schwab -- (a) the canonical builder's dead read out, THEN (b) the Allow narrowed; the skill's description line corrected | `opal-data-schwab` (bd-exporter-ec2-role) | (a) `data/canonical/schwab/build_canonical_daily.py`, by its owner, routed through `0.0.0_AB_MSTR~Z`; (b) `bd-pipeline/iam.tf`; `.claude/skills/49-schwab-conv/SKILL.md` | `0.7.0_AE_CloudOps~IR` (b + skill); the owner (a) | WORLD |
| `IAM-z-3` | E3: `opal-market-data-v2`'s declaration (TF-debt A7) and its one Allow, one pair | market-data-generator-lambda-role | `market-overview/s3.tf`, `market-overview/iam_legacy.tf`, `infra/aws/terraform/tombstones.json` | `0.7.0_AE_CloudOps~IR` | WORLD |
| `IAM-z-4` | E4: READ-ONLY census of the `opal*`, `opal-*`, `opal-data-*` wildcard grants | every principal holding one | deliverables only | `0.9.0_WK_NFRA_IAMROLES202609~14` (COO worker subagent) | LOCAL |

**Carried, no cell (the analysis):** the R20 bridge (NFRA-IAMROLES-R20-01/02, cutoff 2026-12-31). It retires when dell1's
FWD-8 is in box/sitez. That act is 1.0.0_SA_CTO~Z's.

**Cell ids:** `IAM-z-1` .. `IAM-z-4`, checked against `CELL_ID_RE` (`.tools/to-decomp-ref-lint.py:65`).

## 2. THE BATTERY (2026-10-11 ~18:4xZ, base HEAD at the cut)

```
live grant read    get-account-authorization-details (35.7 MB) through the issuer's check
                   deliverables/2.0.0_SA_COO~ZI/checks/round9/allow_names.py: DENOMINATOR principals=357 documents=652.
                   ajb-workflow=1, opal-data-portal-s3=1, opal-data-smartx-v2=3, opal-market-update=1, opal-data-smartx=1,
                   opal-data-schwab=1, opal-market-data-v2=1; control opal-data-portal-v2=38 (the sweep's 38). Every
                   principal matches the sweep's section 7.
comp-iam           219 IAM roles parsed (round-7 cut read); it models (action) only, so the live read above answers.
declarations       Grep of infra/aws/terraform/*.tf: infrastructure-ops-lambda-role at shared-infra/iam_legacy.tf:43
                   (S3InfraWrite :74 names opal-data-smartx-v2/*); smartx-ingestion-lambda-role and smartx-exporter-role at
                   smartx-pipeline/iam.tf:21,116 (:52-53, :152-153 smartx-v2; :164-165 smartx); FredIngestionLambdaRole at
                   fred-pipeline/iam.tf:10 (console-created, a data reference at :63); bd-exporter-ec2-role at
                   bd-pipeline/iam.tf:341; market-data-generator-lambda-role at market-overview/iam_legacy.tf:16 (:50, :59),
                   the bucket at market-overview/s3.tf:6. workspace-sync-lambda-role: no declaration found -> IAM API.
                   ALSO: smartx-v2-bucket-lifecycle/main.tf:34 declares a lifecycle on opal-data-smartx-v2, which is 404.
comp-adversary     premises re-derived 3 of 4, 1 CORRECTED. E2's citation `build_canonical_daily.py:154-156` has aged: the
                   date picker dates_to_build() was re-pointed to monolith bronze @3b01132271 (2026-07-24). The dead read
                   that REMAINS is latest_rps_date() at :141-145 (Bucket=SRC_BUCKET, Prefix 01_raw/), with SRC_BUCKET =
                   "opal-data-schwab" at :48, called at :228 when --date is absent. The ruling stands on the corrected
                   lines. The skill's line-3 description and its Step-7.5 KNOWN DEFECT block both still cite the old state.
comp-schedule      PARTIAL_OR_BLIND at the round-7 read; the assignee reads .open_deploys/ per module before each entry.
```

## 3. BOUNDS, and the STANDING RULES (Z-S40, Z-C-S36)

```
z-1, z-2(b), z-3 are WORLD, two phases each: PHASE A reads and plans, applies nothing; PHASE B only on the issuer's GO
after both halves of that act's never-widen pair are SIGNED. ONE PAIR PER MODULE OR IAM-API ACT (the analysis).
Only dead ARNs leave. Nothing is added. No trust, tag or role change. No bucket is ever created.
-target in every module that carries unrelated pending adds (shared-infra: restricted_breakglass).
STANDING (Z-S40)    every half re-reads the baseline it quotes at signing, or names its read time and makes the act
                    re-read it; the apply refuses if the plan's NOT-SIGNED set differs from the signed one.
STANDING (Z-C-S36)  any table that may recommend HOLD on a byte difference first diffs CONTENTS at the named commit.
G-21 / G-25         no alert, monitor, schedule; no Access Analyzer.
```

## 4. DEPENDENCY EDGES

```
IAM-z-1     <- (none)                         PHASE B order inside the cell: write-bearing names first, opal-data-smartx last
IAM-z-2(b)  <- IAM-z-2(a) landed at HEAD      measured: grep -c 'Bucket=SRC_BUCKET' build_canonical_daily.py reads 0
IAM-z-2(a)  <- the owner, via 0.0.0_AB_MSTR~Z (routed by the issuer at this issuance)
IAM-z-3     <- (none)
IAM-z-4     <- (none)                         read-only; its census feeds round 10 (each wildcard -> an explicit list)
```

`fanout: 4 of 4 chains, cap 8`. z-1, z-2(b) and z-3 share one seat and serialize on `.open_deploys/`; their PHASE A
surveys run first, together.

## 5. RULE 24 -- THE FOUR-POSTULATE RECORD

**(i) MECE.** Domain = the analysis's E1-E4 and the carried R20 item. Subtraction from the sweep's 7 ABSENT names: z-1
takes 5, z-2 takes `opal-data-schwab`, z-3 takes `opal-market-data-v2`; 7 - 7 = 0. Its 3 wildcard names go to z-4.
**(ii) SAME GRAIN.** One analysis item per cell. **(iii) INTENT.** z-1..z-3 remove grants on names that do not exist;
z-4 measures. **(iv) STATE.** z-1..z-3 move policy documents and one declaration. They do NOT move the 34 OURS names,
any wildcard grant, or the orphaned market-data-generator role itself (named in the sweep section 6a, not retired here).

## 6. WHAT THE ROUND CANNOT CLAIM

- The live read is a snapshot. A name 200 today can be deleted tomorrow.
- z-2(a) is another owner's act. Until it lands, z-2(b) stays at PHASE A, and the cell is not complete.
- z-4 names wildcards; it narrows none. The replacement is round 10's.

---

## 7. ADDENDUM 1 (2026-10-11 ~20:4xZ) -- IAM-z-6, workstream FRED_RETIRE, on the CTO's ruling @3e091a9436

**Consumes:** rows Z-S45 (@ad17fa128f) and Z-S48 (@5fae0d16af), and
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_IAMROLES_FRED_DESTINATION_RETIRE_RAW_WRITE_20261011_Z.md`
@`3e091a9436` (msg 33394).

| cell | item | surface | issued to | risk |
|---|---|---|---|---|
| `IAM-z-6` | fred-data-ingestion retires its raw-series write to the 404 `opal-market-update`, so the daily yield-curve fold runs again and `opal-data-portal-v2/json/macro/yield_curve_fred.json` (frozen since 2026-08-05) resumes | `infra/aws/lambda/fred-data-ingestion/lambda_fred_ingestion.py`; artifact `s3://opal-313476888478-lambda-artifacts/fred-pipeline/fred-data-ingestion.zip`; `fred-pipeline/lambdas.tf` (Terraform deploy) | `0.7.0_AE_CloudOps~IR` | WORLD |

**Battery at the cut:**
- The handler raises in process_frequency() at `:130`/`:144`, behind `:257`, before the fold at `:276-291`.
- The deploy reads an S3 artifact by version and content-sha256 (`lambdas.tf:15-32`); its build is
  `infra/aws/lambda/ci/build-and-upload.sh fred-pipeline fred-data-ingestion`.
- The daily schedule is `cron(0 23 * * ? *)` (`eventbridge.tf:17`).
- `opal-data-portal-v2` versioning reads Enabled (19:4xZ read), so the served key's rollback is a prior version.

**Edges:** `IAM-z-6 <- (none)`. It serializes with z-1, z-2 and z-3 on `.open_deploys/`; z-1's narrowing of the
`opal-market-update` grant is independent of it. `fanout: 6 of 6 chains, cap 8`.

**Rule 24:** a sixth item, at the same grain (one ruling, one cell). It moves one served key and the function's code. It does NOT move
`fred-macro-ingestion`, the weekly and monthly schedules' targets, or any IAM document.
