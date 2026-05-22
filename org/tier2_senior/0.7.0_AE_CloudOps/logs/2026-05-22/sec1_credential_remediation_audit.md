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

## Current State

| Item | Status |
|------|--------|
| ITEM 1 (audit) | COMPLETE — table above; 2-of-4 correction + 1 additional finding |
| ITEM 3 (file fate) | COMPLETE for the snapshot (`4dfeaf85a`, pushed); `.gitignore` line routed to COO |
| ITEM 2 (rotation) | HELD at Phase-0 STOP — RAVC1 to COO + CTO for scope |
| ITEM 4 (history scrub) | WONTFIX — declined by Andrew |

## Next Steps

1. [2.0.0_SA_COO] Rule on ITEM 2 scope: (a) FRED provider-key regeneration owner
   (needs a FRED account); (b) JWT cutover plan + the cross-lane DT call for the
   6 trade-Lambda code changes; (c) confirm NEWS/OPENAI ITEM-2 is a no-op.
2. [2.0.0_SA_COO] Commit the `.gitignore` `LAMBDA_SNAPSHOT_PRE_TERRAFORM_*.json`
   rule (BASE_EXEC lane) — or add `0.7.0_AE_CloudOps` to its permitted_agents.
3. [2.0.0_SA_COO] Decide whether to redact the JWT plaintext from the 2026-04-15
   session log (additional finding) — moot once JWT_SECRET is rotated.
4. [~self] On COO ITEM-2 scoping: run Phase-1 `comp-iam service`, build the
   rotation Terraform, RAVC2.
