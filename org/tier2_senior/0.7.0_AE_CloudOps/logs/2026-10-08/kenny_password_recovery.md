# Kenny's account is complete; two password-recovery defects repaired - 0.7.0_AE_CloudOps

**archetype:** DIAGNOSE
**Date:** 2026-10-08, approximately 11:55 AM-12:25 PM Eastern
**Authority:** Andrew direct, recorded verbatim in `deliverables/ANDREW_DIRECT_20261008_KENNY_LOGIN.md`.
**Status:** Backend repair DEPLOYED and VERIFIED. Kenny's own final sign-in remains a user confirmation.
**Push state:** LOCAL; origin CLOUD was `37a4a9454cc928cd3d672ec788159290301d77f9` at first measurement. No push by this seat.

## Objective

Explain and correct the internal error reported by new Cottonwood employee Kenneth (Kenny) Cusick while establishing his dashboard password. Compare account records and verify the live recovery path.

## Work Completed

1. Exact Codex seat loaded; OPAL_AGENT_SERIAL matches. Readiness oracle passed all nine arms, inbox reported zero unread mail. Launcher helpers retained without duplication.
2. Read Kenny's profile, unique email-index entry, firm membership and partner row. Actual email is `kenny.cusick@cottonwoodmail.com`; no account at the supplied `cottonwood.mail` spelling. Actual table is `opal-partner-cottonwood`.
3. Compared all three other real Cottonwood members. Required fields/types, role, firm and tier match. MFA differences are ordinary user choices. No missing required fields, duplicate identity, corrupt hash shape or partner-row defect was found. No account write was needed or performed.
4. Kenny's successful login was October 7 at 12:47:48 PM Eastern. Password remained at its provisioning timestamp, with mustChangePassword=true. Server logs immediately afterward reject fewer than 12 characters; another rejection occurred October 8 at 11:52:04 AM. Logs omit identity, so the relationship to Kenny is temporal, not a request-level identity proof.
5. Confirmed backend/frontend policy mismatch: both password pages still advertise eight characters, but the server requires 12. Generic validation Error fell through to HTTP 500. A public synthetic-token/short-password request reproduced the 500 without touching an account.
6. Found a second independent defect: reset completion called the Opal-only administrative listUsers(), excluding Cottonwood and every other partner. Replaced it with a paginated, filtered reset-token lookup, preserving email uniqueness, checking expiry, rejecting ambiguous identities, and returning clear validation errors.

## Deployment Sequence

| Step | Evidence |
|---|---|
| Source commit | `5b06664303` - typed PasswordValidationError, all-firm token lookup, handler mapping, seven regression tests |
| Type check | auth-handler TypeScript `tsc --noEmit` passed |
| Build | Canonical build-nodejs-lambda.sh; seven tests passed again in the build gate; ESM handler export validated |
| Artifact/ledger commit | `6a54007e88`; source-map SHA and both deploy-ledger carriers |
| Plan | Full root showed auth code plus pre-existing WAF rule drift. Incident-targeted plan asserted exactly one aws_lambda_function.auth_handler update, only code SHA, object version and last_modified fields |
| Apply | safe-apply.sh passed applicable gates; zero added, one changed, zero destroyed |
| Verify | Auth-only plan exit 0 / No changes. Full-root replan confirms auth no-op and only the same pre-existing WAF rule drift |
| Artifact parity | Live Lambda, downloaded S3 zip SHA256, S3 metadata and source map all equal `mzQH2HZl+PKF97zQ5abEjh82fkX9E/eeyLFJT2iQdLA=` |
| Served validation | Public opalinvest.dev reset endpoint: short password -> 400 with 12-character guidance; common password -> 400 with unique-passphrase guidance; invalid token + compliant password -> 400 Invalid or expired reset token |
| Real-record lookup | New helper, read-only against DynamoDB, resolves Kenny's existing reset token to his Cottonwood profile, with password hash unchanged |
| Deploy record | record-terraform-deploy.sh scoped to opalinvest-auth-handler only; portal-auth-v1.23.1; six other pipeline function rows untouched |

## Verification boundaries

Seven tests cover short/common passwords, successful Cottonwood recovery with bcrypt verification and removal of the forced-change flag, empty-page pagination, expired/missing/malformed expiry, missing/replaced tokens, ambiguous tokens across pages and an empty-token no-scan case. Live public probes test deployed error handling and actual DynamoDB scan permission; a successful real password write was exercised with synthetic records in tests, not against Kenny's account. No reset email was sent and no credential was retrieved or exposed. Kenny must complete his own sign-in to confirm the final browser journey.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-which | Used before investigation; several free-form startup/auth questions produced no-fit or ties. Did not mistake these for an authoritative route |
| comp-find | Startup exact-contract search was slow and broad; direct required-file reads completed afterward |
| comp-trace auth-handler | Rebuilt stale graph; auth-handler has no modelled path edges. Named coverage limit |
| comp-routes behaviors | Confirmed declared /auth/* API Gateway path |
| comp-blast opalinvest-auth-handler | Eleven downstream estate nodes; reviewed before source changes |
| comp-iam service | No service match: TypeScript auth handler is not covered. Used direct live IAM simulation instead: dynamodb:Scan on opal-users-v2 allowed |
| comp-diff | Ran before commit; basename matching produced unrelated graph hits. Source-scoped diff and Terraform JSON supplied actual change bounds |
| comp-estate | Located portal-infra resource chain |
| safe-commit | First refusal was a synthetic fixture under test/; moved fixture suite to documented tests/ context, retained test/ build discovery wrapper. Passed without overrides. Normalized edited source files to repository LF before commit |

**What worked:** live account comparisons, exact deployed artifact download, public before/after probes and explicit Terraform JSON assertions.
**What failed:** stale .tools/terraform.exe path; canonical safe-apply fallback to terraform on PATH used. Provider initialized from shared cache. Initial PowerShell target argument required quoting. Source-map risk-reflex referenced an absent memory file; no untracked production source was deployed.
**Gap found:** no compiler IAM model for the auth handler; frontend password minimum is stale; full root contains unrelated WAF rule drift. None was represented as a clean global check.

## Current State and Next Steps

Backend is live and the misleading 500 is repaired. Ask Kenny to request a fresh reset link for `kenny.cusick@cottonwoodmail.com` and choose a unique password of at least 12 characters, or sign in with his original temporary password and complete the required change. The attempted replacement was not saved. Confirm his actual login before claiming user-journey completion.

Frontend owner follow-up: `portal/src/pages/auth/ChangePasswordPage.tsx` and `ResetPasswordPage.tsx` still locally validate and advertise eight characters; align the rule and helper text to 12. Backend now gives the actionable error even with that old UI. CloudOps seat contract excludes frontend commits, so this incident makes no portal commit or deployment.

The broader portal-auth Terraform root retains its pre-existing WAF rule drift. This code-only deployment intentionally did not apply it. No IAM, CloudFront routing, password, MFA preference or partner membership was changed by this repair.

Deployment record commit: `434af083f8`. Both ledger legs CLOSED. Core inventory has a pre-existing XML parse error at line 275 column 65 (same error in HEAD before this edit); this scoped auth-entry update does not repair unrelated XML.
