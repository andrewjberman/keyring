# Deck Generation Lambda API Deployment — 1.0.0_SA_CTO

**Date:** 2026-03-26
**Session:** 11

## Objective

Deploy the deck-generation orchestrator as a Lambda Function URL API
so colleagues can generate branded PPTX decks via HTTP.

---

## Work Completed

### 1. MCP Server Verification (Carryover from Session 9 Crash)

Session 9 crashed mid-test. Verified all 4 MCP tools are operational:
- `generate_deck` — full pipeline: bundle JSON -> PPTX + manifest
- `validate_bundle` — dry run validation
- `list_visual_forms` — 11 forms with slots/skeletons
- `list_deck_goals` — 5 goals with sequences

### 2. Test Deck Generation

Generated `Tax_Deferred_Investor_v2.pptx` (6 slides, 6 unique forms,
6 unique skeletons, fit audit pass, 0 errors). Identified v1 issues
(skeleton residual text, zero-mapping on skeleton 60, heavy fitter
compression) and resolved by choosing better forms and shorter content.

### 3. Lambda API Build

**Handler** (`deck_generation/lambda_api/handler.py`):
- 5 routes: `POST /` (generate), `POST /validate`, `GET /forms`,
  `GET /goals`, `GET /health`
- Cold-start: downloads slide library (29MB) from S3 to `/tmp`
- Output PPTX uploaded to S3, presigned download URL returned (15 min TTL)
- Local test harness at `lambda_api/test_local.py` — all 5 routes
  verified against the real engine with mocked S3

**Lambda Layer** (`deck-generation-deps`):
- python-pptx 1.0.2, PyYAML 6.0.2, lxml 5.3.1, Pillow 11.1.0
- Built from manylinux2014_x86_64 wheels (pip download)
- Zip: 11MB, uploaded to `s3://opal-313476888478-lambda-layers/`
- requirements.txt at `infra/aws/lambda/layers/deck-generation-deps/`

**Build Script** (`infra/aws/lambda/ci/build-deck-generation.sh`):
- Custom build — bundles engine/, index/, prod/, brand_spec/, lambda_api/
- Uses PowerShell for zip (Windows Git Bash)
- Artifact: 710KB -> `s3://opal-313476888478-lambda-artifacts/deck-generation-pipeline/`

### 4. Terraform Deployment

**Pipeline:** `deck-generation-pipeline`
**State key:** `deck-generation-pipeline/tfstate`
**Tag:** `deck-generation-v1.0.0`

Resources created (7 total):
| Resource | Name/ID |
|----------|---------|
| Lambda | `deck-generation` (1024MB, 120s, 512MB ephemeral) |
| Layer | `deck-generation-deps:1` |
| Function URL | `https://7dvozvbxxblaicvzkdqrkrp7640zxeta.lambda-url.us-east-1.on.aws/` |
| IAM Role | `deck-generation-lambda-role` |
| IAM Policy | S3 read (slide library) + S3 write (output) + CloudWatch |
| Log Group | `/aws/lambda/deck-generation` (14 day retention) |
| Permission | Function URL invoke (IAM auth) |

### 5. Issues Encountered and Resolved

**SLIDE_LIBRARY path copies (critical fix):**
`assembler.py` and `architect.py` both `from engine.skeleton import SLIDE_LIBRARY`
which copies the module-level Path value. Patching `skeleton.SLIDE_LIBRARY` at
runtime didn't propagate. Fix: added `SLIDE_LIBRARY_PATH` env var override in
`skeleton.py` + explicit patching of all three module copies in the handler.

**Org SCP blocks public Function URLs:**
`authorization_type = "NONE"` returned 403 Forbidden even with correct
`lambda:InvokeFunctionUrl` resource policy. Switched to `AWS_IAM` auth.
Colleagues use `awscurl` with their AWS credentials.

**CORS allow_methods validation:**
AWS Function URL rejects `["GET", "POST", "OPTIONS"]` (member length >6).
Fixed by using `["*"]` wildcard.

**MSYS path conversion:**
`MSYS_NO_PATHCONV=1` as command prefix mangles the `aws` script path on
this machine. Used `python -m awscli` for all S3 operations.

**S3 artifact metadata:**
`source_code_hash` from `data.aws_s3_object.metadata["content-sha256"]`
failed (empty metadata). Used `.etag` instead.

### 6. Live Validation (All Passed)

| Endpoint | Method | Result |
|----------|--------|--------|
| `/health` | GET | `{"status": "healthy"}` |
| `/forms` | GET | 11 visual forms returned |
| `/goals` | GET | 5 deck goals returned |
| `/validate` | POST | Dry-run validation, success, correct resolutions |
| `/` | POST | 4-slide deck generated, S3 upload, presigned URL works |
| `/` | POST (bad JSON) | Clean 400 error with message |

Full generation test: 4 slides, 4 unique skeletons, fit audit pass,
0 compressions, PPTX downloaded from S3 (4.3MB).

---

## How Colleagues Use It

```bash
pip install awscurl

# Generate a deck
awscurl --service lambda --region us-east-1 -X POST \
  -H "Content-Type: application/json" \
  -d @bundle.json \
  https://7dvozvbxxblaicvzkdqrkrp7640zxeta.lambda-url.us-east-1.on.aws/

# Response includes download_url (presigned, 15 min expiry)
```

---

## S3 Artifacts

| Path | Size | Purpose |
|------|------|---------|
| `deck-generation-pipeline/slide-library.pptx` | 29MB | Slide library template |
| `deck-generation-pipeline/deck-generation.zip` | 710KB | Lambda function code |
| `deck-generation-deps.zip` (layers bucket) | 11MB | Lambda layer |
| `deck-generation-pipeline/output/{ts}/{name}.pptx` | ~4MB | Generated decks |

---

## Commits

| Hash | Description |
|------|-------------|
| `52bd21a2` | feat: Lambda API + Function URL + Layer + Terraform |
| `0ca26e97` | fix: SLIDE_LIBRARY env override, IAM auth, path patching |
| `1f69d98f` | fix: eliminate duplicate media zip entries in copy_slide |

**Tag:** `deck-generation-v1.0.0`

---

## 7. PowerPoint "Repair" Prompt Fix (Session 11b)

**Problem:** Every generated PPTX prompted "This file is damaged and
needs to be repaired. If you trust the source..." on open in PowerPoint.
User reports this has occurred on ALL generations since the engine was built.

**Root cause:** `copy_slide()` in `engine/skeleton.py` used
`new_slide.part.relate_to(source_part, rel.reltype)` to link media from
the source presentation. Since source and target are separate python-pptx
`Presentation` objects (even though both loaded from the same PPTX file),
`relate_to()` treated the source part as new and added it to the target
package — creating duplicate zip entries. PowerPoint validates zip entry
uniqueness on open and triggers the repair dialog when it finds duplicates.

**Diagnostic evidence:**
```
DUPLICATE ENTRIES: {'ppt/media/image5.svg': 2, 'ppt/media/image4.png': 2}
```

**Fix:** Before `relate_to()`, build a lookup of all parts already in the
target package via `target_prs.part.package.iter_parts()`. For each source
relationship, check if the target package already has a part with the same
partname. If so, relate to the existing target part instead of the source
copy. This prevents python-pptx from adding duplicate entries.

**Result:** 69 zip entries (down from 71), zero duplicates, no repair prompt.
Fix deployed to Lambda (`1f69d98f`).

---

## Remaining Work

- **Simplify colleague access:** `awscurl` requires AWS credentials +
  pip install. Consider a thin wrapper script or a web form that calls
  the API.
- **Skeleton residual text:** Assembler doesn't blank unmapped shapes.
  Code fix in `engine/assembler.py` or `engine/content.py` would
  improve all generated decks.
- **Planner diversity constraint:** Architect should detect skeleton
  reuse across slides and swap to alternates automatically.
