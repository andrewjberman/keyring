# Secrets-in-Code Scan — Findings (Track-1 Tier-1 #1)

**archetype:** DIAGNOSE
**Author:** 0.7.0_AE_CloudOps
**Date:** 2026-06-03
**Trigger:** Andrew-direct (highest-materiality remediation axis). Scope: tracked files (git grep) + working tree; secret VALUES redacted here (never commit a secret to fix a secret).
**Method:** no dedicated tool available (gitleaks/trufflehog/detect-secrets absent) — high-signal pattern scan + manual true-vs-false-positive disambiguation. Patterns: AWS keys, private keys, provider tokens (sk-/sk-ant-/xox/ghp/AIza/SG./sk_live), password/secret/token literals, connection-string creds, committed .env.

## CLEAN (no exposure)
- **No AWS secret access keys** (the dangerous 40-char half) in tracked files.
- **No private keys** (BEGIN ... PRIVATE KEY) committed.
- **No committed `.env`** files with values.
- **Portal auth = RS256 asymmetric** (`auth-validator-edge/index.mjs`: `jwt.verify(token, publicKey, {algorithms:["RS256"]})`, public key from SM `opal/auth/jwt-public-key`). Public key in SM is correct — not a secret-in-code.

## REAL FINDINGS (true positives)
| # | Sev | Finding | Location | Action |
|---|---|---|---|---|
| 1 | **MED** | **Google CSE API key** (`AIza…`) committed in a doc | `tools/news_scanner/lambda/layer3_gpt_curation/docs/GOOGLE_CSE_INTEGRATION.md:53` | Rotate the key (Google console), remove from doc, move to Secrets Manager + SM-ref the consumer. NEW finding (not in SEC1). |
| 2 | **MED** | **Bright Data scraping-browser creds** (`wss://user:pass@brd.superproxy.io:9222`) pasted inline | committed session log `org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-05-27/work_1800Z_...md:112` | Rotate the Bright Data zone creds, redact the log line. + Process: agents must not paste live creds into session logs (recurring-risk class). |
| 3 | **LOW-MED** | **Known SEC1 secrets still in git HISTORY** (FRED_API_KEY / JWT_SECRET / NEWS_API_SECRET / OPENAI_SECRET in the removed `LAMBDA_SNAPSHOT_PRE_TERRAFORM_*.json`) | git history only (removed from tree by SEC1 4dfeaf85a) | Andrew WONTFIX'd the history scrub. FRED/NEWS/OPENAI = free keys, rotate-opportunistically (already Andrew-deprioritized). **JWT_SECRET**: severity mitigated — portal auth is now RS256/asymmetric, so the exposed HS256 shared secret likely can't forge portal tokens; CONFIRM no live HS256 verifier still trusts it, else rotate. |

## FALSE POSITIVES (cleared — disambiguated, not exposures)
- `inf-jwt-trigger/lambda_function.py:36-37` `SM_ORION_JWT_SECRET` / `SM_ECLIPSE_JWT_SECRET` = Secrets-Manager **reference names** (co-located with SSM-doc-name constants), NOT secret values — the correct pattern.
- `infra/aws/ec2/moltbot/openclaw/clone-workspace-repos.py:35` GitHub URL interpolates a `{pat}` **variable**, not a literal token.
- `infrastructure_monitor/httpx/` + `pydantic/` `password=` hits = **vendored third-party library** doc/test examples (pydantic's `scolvin`/`IAmSensitiveBytes` fixtures, httpx examples).
- `AKIA…` hits across `docs/security/*` + `infra/aws/*_AUDIT*.md` = AWS Access Key **IDs** in security-audit/rotation docs — Access Key IDs are not secrets on their own (the secret key is, and none were found paired).

## HYGIENE finding (bonus, not a secret)
- `infra/aws/lambda/infrastructure_monitor/` has full **vendored** `httpx` + `pydantic` library source committed into the Lambda dir — a CLAUDE.md **Rule 3** violation (deps belong in a Lambda layer, not pip-installed into source) + the source of the password= false-positive noise. De-vendor → layer.

## Severity-ranked remediation
1. **Google CSE key** (#1) — rotate + remove + SM-ref. Real live key in a committed doc. *(recommended first)*
2. **Bright Data creds** (#2) — rotate + redact log + the no-creds-in-logs process note.
3. **JWT_SECRET-in-history** (#3) — confirm no live HS256 verifier trusts it (likely dead under RS256); FRED/NEWS/OPENAI rotate-opportunistically per Andrew.
4. **De-vendor** infrastructure_monitor httpx/pydantic → layer (hygiene).

## Note
A definitive scan would add gitleaks/trufflehog (full git-history entropy scan) to the runner — recommend for the comprehensive Track-2 pass. This pass = pattern + tracked-file + manual-disambiguation, which catches literal/known-format secrets but not high-entropy blobs with no keyword anchor.
