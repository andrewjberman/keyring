# MOLECULE: the 7 LAMBDAMAP-suspect Lambdas (deploy-parity)   (scale: MESO x7)
**archetype:** DIAGNOSE

## Unit + expected role
The 7 Lambdas comp-lambdamap sha flagged as non-MATCH: 4 SHA_DRIFT (bd-portal-publisher, cot-bd-session-trigger, opal-market-regime-classifier, opal-portal-volatility-fetcher) + 3 CORRUPT_RECORD (bd-price-update, inf-etf-ownership-daily, yang-generate-macro-timeseries). Expected role of each: a deployed pipeline Lambda whose LIVE code should equal what infra/aws/lambda/ci/lambda-source-map.json records. Question Andrew set: **establish TRUE parity per asset** — is each a half-landed/out-of-band DEPLOY drift (reconcile) or a RECORD defect (re-record)? Held the source-map record SUSPECT (Dimension 1 tests whether it's even true).

## VERDICT (headline): ALL 7 ARE CODE-PARITY-OK. ZERO half-landed deploys. Every defect is in the RECORD/TOOLING layer.
Grounded against live AWS CodeSha256 + the actual S3 deploy artifacts (downloaded + hashed), not the source-map self-report.

## 1. Composition — deployed-vs-record drift (the knowledge-parity read)
Two distinct record-defect mechanisms, both proven against live:

**CLASS 1 — CORRUPT_RECORD = MSYS path-mangle of a leading-`/` base64 sha (3 Lambdas).** AWS CodeSha256 is base64 and can start with `/`. record-terraform-deploy wrote the sha through a shell that path-converted a leading `/`, rewriting it to `C:/Program Files/Git/`:
| fn | LIVE CodeSha256 | recorded artifact_sha256 | de-mangle? |
|---|---|---|---|
| bd-price-update | `/Y5g7vUfwqvPd/ReMN3SifMOZE48rPcUUBoKiwuSIpE=` | `C:/Program Files/Git/Y5g7vUfwqvPd/ReMN3SifMOZE48rPcUUBoKiwuSIpE=` | identical, leading `/`→`C:/Program Files/Git/` |
| inf-etf-ownership-daily | `/rv265WL26+ehwkdPmkfRe3ys2cmpcm1Do3QbnI/hpg=` | `C:/Program Files/Git/rv265WL26+ehwkdPmkfRe3ys2cmpcm1Do3QbnI/hpg=` | identical, same mangle |
| yang-generate-macro-timeseries | `/BZvlPsU1NYvCYgA7B6If4ZZz+gTLwdmXi1r7lZvNYA=` | `C:/Program Files/Git/BZvlPsU1NYvCYgA7B6If4ZZz+gTLwdmXi1r7lZvNYA=` | identical, same mangle |
→ The recorded value IS the live sha with the leading `/` corrupted. Deployed code = exactly what was recorded; only the WRITTEN RECORD is mangled. **Code parity PERFECT.**

**CLASS 2 — SHA_DRIFT = stale source-map sha; live == the actual current S3 artifact (3 Lambdas).** Downloaded each S3 deploy artifact at its recorded `artifact_s3_key` and hashed it (base64 sha256 = the CodeSha256 basis):
| fn | LIVE CodeSha256 | S3-artifact sha (computed) | recorded artifact_sha256 | live==S3? |
|---|---|---|---|---|
| bd-portal-publisher | `VEMK3JYTCF/Py5XN…EGo=` | `VEMK3JYTCF/Py5XN…EGo=` | `MesmIWU8…zII=` (stale) | **YES** |
| cot-bd-session-trigger | `jVnve5FH…4AQ=` | `jVnve5FH…4AQ=` | `8LzEjSqQ…uuc=` (stale) | **YES** |
| opal-market-regime-classifier | `YZ6uO7ck…F78=` | `YZ6uO7ck…F78=` | `cwZD6iI8…uMA=` (stale) | **YES** |
→ Live is running the EXACT current S3 deploy artifact in all 3. The recorded `artifact_sha256` matches NEITHER live NOR the S3 artifact = a stale/wrong record value. **Code parity OK** (live == the deployable artifact); the record is wrong.

**CLASS 3 — already-dispositioned intentional-leave (1 Lambda).** opal-portal-volatility-fetcher: live CodeSha256 `DCzdNd8l…`, LastModified 2026-02-23 (matches its source-map `_note`). The `_note` (NFRA_GRAPHS.D8-FP/inc-2a, disposition (c) 2026-06-17) documents: live = the correct 58MB bundled scipy/numpy package; the S3 artifact (`RxfpdVqaz`, 6350B) is a STALE deps-less re-zip that must NOT be applied (would drop bundled deps). **Parity OK-BY-DESIGN**; the SHA_DRIFT flag is a known false-positive the sha tool raises because it doesn't read the disposition.

## 2. State — live snapshot
All 7 `State=Active`, healthy. LastModified per fn confirms the timeline (Class-2 detail below). volatility-fetcher invokes daily, 0 errors per its _note.

## 3. Position in the chain (lineage)
Source-map → record-terraform-deploy (the writer, the Class-1 root cause) → comp-lambdamap sha (the reader, surfaced the suspects). Each Lambda sits in its pipeline thread (bd-pipeline / cot-pipeline / market-overview / inf-pipeline / yang-pipeline). The seam to hand to /seams: record-terraform-deploy → lambda-source-map.json (the WRITE seam where the mangle happens) and source-map → comp-lambdamap (the READ seam where it surfaces).

## 4. Behavior — what the deployed path does
Not re-exercised per-Lambda (parity, not function-behavior, was the question). Evidenced healthy: all Active; volatility-fetcher daily/0-err (_note); the live CodeSha256 reads ARE the behavior-relevant ground truth here (what code is actually running).

## 5. Semantic quality + smell pass
The deep read inverts the surface signal: comp-lambdamap classified 7 "suspects" implying possible deployed drift; the decisive live-vs-S3-artifact test establishes **0 deployed-code problems** — all 7 resolve to record/tooling-layer defects. The sharp test that bound: downloading + hashing the actual S3 artifact (not trusting the recorded sha or the live-vs-recorded delta) — it discriminated stale-RECORD from half-landed-DEPLOY, which the surface tool cannot.

## Smell findings
| Smell | Rating | Evidence | Why it caught my eye |
|---|---|---|---|
| record-terraform-deploy MSYS-mangles a leading-`/` base64 sha into `C:/Program Files/Git/...` | **DIG** | live==record(de-mangled) for all 3 Class-1 | a real tooling bug (the CLAUDE.md MSYS_NO_PATHCONV footgun); will recur on every ~1/64 deploy whose sha starts with `/` until guarded |
| Class-2 source-map recorded a NEWER last_deployed_at + sha than what actually landed | **DIG** | cot-bd-session-trigger record says deploy 2026-06-25 sha 8LzEjSqQ, but live+S3 = the 2026-06-09 jVnve5FH artifact; market-regime record says 06-03 cwZD6iI8 but live+S3 = 04-05 YZ6uO7ck | a recorded-deploy that did NOT change the deployed artifact — the record bumped a date+sha that never landed; the record-writer recorded an intended sha, not the deployed one |
| comp-lambdamap sha has no disposition-awareness (flags the dispositioned volatility-fetcher) | **WATCH** | volatility-fetcher SHA_DRIFT vs its own `_note` intentional-leave | same class as the comp-iam condition-blindness I co-verified today — a tool flagging a known-dispositioned divergence; a `_note`/disposition read would suppress the FP |
| live==S3 but record-sha matches neither (Class 2) | NOTE | the 3 Class-2 recorded shas match no artifact on disk or live | the recorded sha is a build-time sha of an artifact that was never the one at the key — consistent with the date/sha-bump-without-deploy smell above |

## Assessment
**True parity is ESTABLISHED: every one of the 7 is running correct, intended code — there is no half-landed deploy and no deployed-estate action to take.** The 7 "suspects" are a record/tooling problem, not a deploy problem. Two DIG smells route to the owner (0.7.0_AE, who owns comp-lambdamap + record-terraform-deploy):
1. **Fix record-terraform-deploy's MSYS path-mangle** (guard the sha write with MSYS_NO_PATHCONV / quote-and-no-pathconv) — root cause of the 3 CORRUPT_RECORD; then **re-record** those 3 (their live shas: bd-price-update `/Y5g7v…`, inf-etf-ownership-daily `/rv265…`, yang-generate-macro-timeseries `/BZvlP…`).
2. **Re-record the 3 Class-2 stale shas** to the live==S3 truth (bd-portal-publisher `VEMK3JYTCF…`, cot-bd-session-trigger `jVnve5FH…`, opal-market-regime-classifier `YZ6uO7ck…`) — and investigate WHY the source-map carried a newer date+sha than the landed artifact (a record-writer recording the intended-not-deployed sha is the upstream of this whole drift class).
3. **volatility-fetcher: no action** — disposition (c) intentional-leave stands; optional comp-lambdamap enhancement = read the `_note`/disposition to suppress this known FP (the conservative-correctness pattern, same as the comp-iam condition-fix).
This is the bounded molecule exception's edge: the fix is a RECORD/tooling correction, but the source-map is CI-source-of-truth (infra authoring lane) AND requires re-running record-terraform-deploy (not a hand-edit) — so it ROUTES to AE, not a CVO direct edit.

## grounding: field (Rule 22)
- "all 7 are code-parity-OK / 0 half-landed" — **SOURCE-CONFIRMED** (live `aws lambda get-function-configuration` CodeSha256 + downloaded+hashed S3 artifacts: Class-1 live==record-de-mangled by exact string identity; Class-2 live==S3-artifact byte-identical; Class-3 live==_note-documented bundled package). PROVABLE — reserved word legal: the parity is source-confirmed against live + artifact bytes.
- "record-terraform-deploy MSYS-mangles the sha" — **SOURCE-CONFIRMED** (the 3 records are exactly `C:/Program Files/Git/` + the live sha sans leading `/`; deterministic MSYS path-conversion signature). The downstream fix (guard the write) is the INFERRED remedy until AE confirms the exact write-site — flagged to owner.
- "record bumped a date+sha that never landed" (Class-2 smell) — **SOURCE-CONFIRMED** as state (record last_deployed_at/sha vs live+S3 LastModified/sha); the WHY (record-writer records intended-not-deployed sha) is **INFERRED (live-state-only)** — routed to AE to confirm at the writer.

## Knowledge-parity delta + residual
- Believed (surface): 7 suspect Lambdas, possible deployed drift incl. up-to-4 half-landed. True: 0 deployed-code defects; 6 record defects (3 MSYS-mangle + 3 stale-sha) + 1 dispositioned-FP.
- Record corrected this pass: NONE directly (source-map is infra-lane + needs the tooling fix not a hand-edit) — ROUTED to 0.7.0_AE with the grounded per-fn truth.
- NOT exercised: per-Lambda function behavior (out of scope — parity, not behavior, was the question); the record-terraform-deploy write-site source (handed to AE to locate the exact mangle line).

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| comp-lambdamap sha | the surface classification (input) | 128/4/3/0 | surfaced the suspects; cannot do live-vs-S3-artifact (the parity test) |
| live aws lambda get-function-configuration | CodeSha256 + LastModified x7 | PASS | the live ground truth |
| aws s3api head-object + s3 cp + sha256 | the 3 Class-2 S3 artifacts | PASS | the decisive live==S3 byte-identity test (stale-record vs half-landed discriminator) |

— 3.0.0_SA_CVO
