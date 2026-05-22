# Session Log — 0.7.0_AE_CloudOps — YALP_MDSRC.SEC1 — 2026-05-22

## Summary

Executed **YALP_MDSRC.SEC1** ITEM 1 (audit) + ITEM 3 (file fate). ITEM 2
(rotation) is held at the Phase-0 STOP — the discovery grep surfaced an
additional plaintext finding, and the audit materially corrects the TO
premise. RAVC1 sent to COO + CTO with the scoping decisions ITEM 2 needs.

## ITEM 1 — Credential audit (read-only; no AWS mutation)

Premise correction: the SEC1 finding cited "FOUR inline plaintext secrets."
Empirically only **TWO** are genuine inline plaintext. The other two env vars
in the snapshot hold a Secrets-Manager secret **NAME** (the correct SM-ref
pattern) — not a plaintext key.

| Key | Consuming Lambdas (live, us-east-1) | Live form | Committed value still live? | Target SM secret |
|-----|-------------------------------------|-----------|------------------------------|------------------|
| FRED_API_KEY | `fred-data-ingestion` (1) | **PLAINTEXT** (32-char) | YES — committed plaintext == live env value | `opal/external-apis` (exists; F4/F5 FRED path) |
| JWT_SECRET | `trade-recon-auth`, `trade-recon-processor`, `trade-recon-authorizer`, `trade-recon-api`, `trade-auth-handler`, `trade-authorizer` (6) | **PLAINTEXT** (64-hex) | YES — committed plaintext == live env value on all 6 | new secret (e.g. `opal/trade-pipeline/jwt-signing-key`) |
| NEWS_API_SECRET | `news-ingestion-scheduler` (1) | **SM-NAME-REF** (`opal/external-apis`) | N/A — env var holds the SM secret NAME, not a key. No plaintext exposure. | already SM (`opal/external-apis`) |
| OPENAI_SECRET | `news-trending-analysis` (1) | **SM-NAME-REF** (`opal/openai/news-trending`) | N/A — env var holds the SM secret NAME, not a key. No plaintext exposure. | already SM (`opal/openai/news-trending`) |

Method: extracted the 4 values from the committed snapshot, classified each by
form (ARN / SM-name-ref / plaintext-secret), and compared against live
`aws lambda get-function-configuration` for every consuming Lambda. Secret
values were never printed — only masked SHA-256 fingerprints. Scripts:
`.runtmp/sec1_phase0_audit.py`, `.runtmp/sec1_phase0_classify.py` (gitignored).

### Additional finding (Phase-0 grep `if_mismatch` — STOP + RAVC1 COO)

The JWT_SECRET plaintext value (64-hex) appears in a **3rd tracked file**:
`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-04-15/post-sprint-1-jwt-drift-reconcile.md`
— a session log that quoted the trade-pipeline JWT during a 2026-04-15 drift
investigation. The committed-plaintext surface for JWT_SECRET is 3 files, not 2.

FRED_API_KEY value: 0 additional files. NEWS/OPENAI "values" appear in 140 / 19
files respectively — but those are the SM secret NAMES (`opal/external-apis`,
`opal/openai/news-trending`), openly-named resource identifiers, NOT secrets.
Not findings.

### JWT blast-radius refinement

The exposed JWT_SECRET is the **trade pipeline's own** signing key
(trade-recon-* + trade-auth-*). The portal auth fabric uses a **separate**
secret `opalinvest/jwt-secret` — already in Secrets Manager, distinct value,
base64 — confirmed by the 2026-04-15 session log. A JWT_SECRET rotation cutover
blast radius is the **trade pipeline only**, NOT portal-auth / partners-api.
The SEC1 `<cross_domain_coordination>` portal-auth concern does not apply to the
exposed key.

## ITEM 3 — File fate

| Action | Result |
|--------|--------|
| `git rm --cached` + delete `infra/aws/terraform/LAMBDA_SNAPSHOT_PRE_TERRAFORM_20260203_125339.json` | DONE — commit `4dfeaf85a`, pushed to origin/CLOUD |
| `.gitignore` rule `LAMBDA_SNAPSHOT_PRE_TERRAFORM_*.json` | BLOCKED — `.gitignore` is owned-paths-locked to the BASE_EXEC lane (CTO/COO); routed to COO. The edit sits uncommitted in the working tree for COO to commit. |
| `worktrees/comp-learns-_stub/` copy | Not touched — separate git worktree on branch `comp-learns/_stub`; already covered by the existing `worktrees/` ignore rule. Out of the CLOUD/AE lane. |

This closes the ongoing-exposure surface (the file being carried forward in
commits). It does NOT scrub git history — SEC1 ITEM 4 is WONTFIX/declined by
Andrew; ITEM 2 rotation is the accepted neutralisation.

## ITEM 2 — Rotation (HELD at Phase-0 STOP — pending COO scoping)

Per the Phase-0 mandate `if_mismatch`, rotation is stopped pending COO ruling
on the widened scope. Surfaced in the RAVC1:

- **FRED_API_KEY** — provider-side key regeneration needs a FRED account login
  (human action; I do not hold provider credentials). New value -> `opal/external-apis`;
  switch `fred-data-ingestion` env to an SM-name-ref + `secretsmanager:GetSecretValue`
  IAM grant; fred-pipeline Terraform.
- **JWT_SECRET** — "rotation" = generate a new 64-hex secret (no provider). Needs
  a COO-signed cutover plan (dual-secret validation window) — invalidates all
  live trade-pipeline JWTs. Switching the 6 Lambdas from a plaintext env var to
  an SM reference is a **per-Lambda code change** (the code currently reads the
  literal `os.environ['JWT_SECRET']`); trade-recon / trade-auth code is the
  TradingOperations (DT) lane — a cross-lane scoping call for COO.
- **NEWS_API_SECRET / OPENAI_SECRET** — already SM-name-refs; no committed-plaintext
  exposure. SEC1 ITEM 2 is effectively a no-op for these. Optional opportunistic
  value rotation per Andrew (free keys) — not a remediation requirement.

## Compiler Tools

| Phase | Tool | Result |
|-------|------|--------|
| 0 (discovery) | `grep -rIl` the 4 key names across infra/aws | Ran — surfaced the 2 known snapshots + many env-name references; refined with a value-exact scan (`.runtmp/sec1_phase0_audit.py`) which found the 1 additional plaintext finding (JWT in the 2026-04-15 session log). |
| 0 (classify) | `.runtmp/sec1_phase0_classify.py` + live `aws lambda get-function-configuration` | Ran — established 2-of-4 genuine plaintext; live-vs-committed comparison per consumer. |
| 1 (`comp-iam service`) | per consuming Lambda | NOT YET — Phase 1 is a pre-rotation step; rotation is held at the Phase-0 STOP. Runs when COO clears ITEM 2 scope. |

## ITEM 2 — Rotation (resolved 2026-05-22, post-COO/Andrew ruling)

COO relayed Andrew's scoped ITEM 2 ruling: 2.1 FRED = rewire-now / defer
regeneration; 2.2 JWT = carved out to a standalone TO (outline only under
SEC1); 2.3 NEWS/OPENAI = confirmed no-op.

### ITEM 2.1 — FRED Lambda Secrets-Manager rewire — COMPLETE

| Step | Action | Result |
|------|--------|--------|
| 1 | Code: `lambda_fred_ingestion.py` | Added `get_fred_api_key()` (reads `opal/external-apis` via `secretsmanager:GetSecretValue`, mirrors the F5 pattern); `lambda_handler` + `__main__` use it; plaintext env read removed |
| 2 | iam.tf | `fred_ingestion_secrets_read` — `GetSecretValue` on the one `opal/external-apis` ARN, least-privilege |
| 3 | lambdas.tf | dropped `ignore_changes=[environment]` so Terraform manages the env empty |
| 4 | Commit | `5fd73c704` (code+TF) |
| 5 | Build | **INCIDENT** — ran `build-and-upload.sh` which zips only `files[]`; fred-data-ingestion is a vendored-deps Lambda (source-map `_build_note`). The deps-less zip broke the function (`No module named 'requests'`). |
| 6 | Recovery | Rebuilt via the documented swap-into-deployed-zip method: pulled the prior deps-bearing S3 version (`agzMMs0o...`, 1MB/195 entries), swapped in the SEC1-rewired `files[]` `.py`, re-zipped, uploaded with `content-sha256` metadata. Source-map sha corrected (`44d3aca69`). |
| 7 | Apply | terraform apply 0-diff (IAM grant created earlier; final apply 1-change). Tag `fred-pipeline-v1.1.1`. |
| 8 | Verify | `fred-data-ingestion` re-invoked (`{"frequency":"monthly"}`) -> StatusCode 200, `success:True`; `Environment` = `null` (no `FRED_API_KEY` plaintext) — the key resolves from Secrets Manager. |

Provider-side FRED key REGENERATION: **deferred by Andrew's ruling** (free key,
low-stakes) — a tracked follow-up, NOT a SEC1 blocker.

**Build-tooling lesson:** always read the source-map `_build_note` before
`build-and-upload.sh` — a vendored-deps Lambda needs the swap-into-zip method,
not the standard build. (The vendored-deps -> Lambda Layer migration is the
separate P3 fred-family cleanup TO.)

### ITEM 2.2 — JWT cutover-plan outline — DELIVERED to COO

The JWT_SECRET rotation is carved out of SEC1 to a standalone CTO-ratified TO.
SEC1 deliverable = the cutover-plan outline (dual-secret 3-phase window, the 6
trade Lambdas, the new SM secret, the cross-lane DT+AE split, the 3rd-file
scrub of the 2026-04-15 session log). Delivered to COO 2026-05-22 (MCP) — COO
authors the standalone TO from it. No secret generated, no trade-Lambda code
touched under SEC1.

### ITEM 2.3 — NEWS/OPENAI — NO-OP (confirmed)

Both env vars already hold Secrets Manager secret NAMES — no committed-plaintext
exposure. Dropped from ITEM 2 scope.

## Compiler Tools (ITEM 2.1 addendum)

| Phase | Tool | Result |
|-------|------|--------|
| 1 | `comp-iam service fred-data-ingestion` | Graph pre-commit-stale; manual enumeration: the one new boto3 call is `secretsmanager:GetSecretValue` on `opal/external-apis` — matched 1:1 by the `fred_ingestion_secrets_read` iam.tf grant (one secret, one action, least-privilege). |
| 2 | `comp-iam gaps` | 0 fred-pipeline gaps. (2 unrelated pre-existing `mdpf-daily-trigger` gaps noted in the C1 log — out of scope.) |
| 3 | `aws lambda get-function-configuration` | `Environment=null` — no plaintext key on the consuming Lambda; resolves via Secrets Manager. PASS. |

## Current State

| Item | Status |
|------|--------|
| ITEM 1 (audit) | COMPLETE — 2-of-4 correction + 1 additional finding |
| ITEM 2.1 (FRED SM-rewire) | COMPLETE — `fred-pipeline-v1.1.1`; verified (invoke `success:True`, env clean) |
| ITEM 2.2 (JWT outline) | COMPLETE — outline delivered to COO; rotation = standalone TO |
| ITEM 2.3 (NEWS/OPENAI) | NO-OP — confirmed already SM-refs |
| ITEM 3 (file fate) | COMPLETE — snapshot removed (`4dfeaf85a`); `.gitignore` rule landed by COO (`e1a094554`) |
| ITEM 4 (history scrub) | WONTFIX — declined by Andrew |

## Next Steps

1. [2.0.0_SA_COO] Author the standalone JWT-rotation security TO from the
   delivered cutover outline.
2. [tracked follow-up] FRED API key provider-side regeneration — deferred by
   Andrew (free key); fold into the P3 fred-family cleanup or rotate
   opportunistically.
3. [~self] SEC1 RAVC2 to COO — SEC1 closes (ITEM 1 + 2.1 + 2.2 + 3 done).
