# CVO cot Lever A exercise-gate -- PRE-GROUNDED (code+deploy+cookie); load-bearing HELD for the 02:00 daily

**archetype:** VALIDATE
**serial:** 3.0.0_SA_CVO | **date:** 2026-07-06 ~1940Z | **subject:** cot Lever A (cot-pipeline-v0.7.0, 0.7.0~A) | **ledger owner:** 2.0.0_SA_COO
**firm-sep:** grounded ONLY against opal-data-cot / cot pipeline -- ZERO bd cross-reference (cot = completely separate firm pipeline).

## STATUS: HELD-PENDING-NATURAL-DAILY (not PASS today). Code/deploy/cookie grounded now; live load-bearing on tomorrow's 02:00Z scheduled daily.

### Cert-method decision (CVO-independent, held against a COO exercise-now rec)
COO initially recommended EXERCISE-NOW (ledger-window ~01:31Z < the 02:00 daily + de-risk). I RULED (b) NATURAL-DAILY BELT and COO ACCEPTED on the merits: cot's skip path triggers a FULL bronze->silver->gold->served chain, so exercise-now = **an ad-hoc gold run to validate work, which CLAUDE.md NEVER-rules forbid** ("validate on the scheduled nightly's artifacts"). 49F's exercise-now was legal (idempotent Lambda skip, no gold chain); cot's is NOT (real chain). The rule bites -> defer to the scheduled daily = the ONE legal defer (hard external gate). COO handles the ledger-window (annotate + extend to cover the rule-mandated 02:00 belt so it's not a false-stranded RED).

### Grounded NOW (independently, not AE self-report)
- **DEPLOY:** live Lambda cot-bd-session-trigger CodeSha256 = 7dJLylE7psMM95J8Y8vxhckpX9aNIidvh9ZY7Du7mu0= == AE-claimed 7dJLylE7ps == tag cot-pipeline-v0.7.0 (LastModified 19:31:56Z). VERIFIED.
- **CODE (matches the validated 49F fail-safe pattern -- read cot's own source, firm-sep):**
  - `_session_is_positive_live` (l.190-209): FAIL-SAFE ABSOLUTE -- SM-read-error / empty-cookie / probe-raise / probe-negative ALL `return False -> full OIDC-login mint`; `True` ONLY on positive-live. (#2 fail-safe CODE-GROUNDED.)
  - `_handle_session_refresh` (l.212-227): skip ONLY on positive-live -> `_handle_bronze_run()`; any doubt -> `_handle_ssm_dispatch(SESSION_FETCH...)` full mint.
  - SINGLE-FIRE (l.217-219): skip dispatches opal-cot-bronze-run (NOT session-fetch) -> cot-session-complete (keyed on session-fetch Success) never fires -> exactly one bronze-run. (#3 CODE-GROUNDED.)
  - PARITY (l.182-187): shared `_handle_bronze_run` (same SSM doc BRONZE_RUN / 3600 / box lifecycle) for BOTH the session-complete leg AND the skip leg -> identical either path. (#4 CODE-GROUNDED.)
- **COOKIE:** blackdiamond/cot/session LastChanged 02:02:48Z (daily mint) + AE read-only session-check live=true @19:33Z. Live (keepalive-held).

### HELD for tomorrow's 02:00Z cot daily (the live load-bearing #1 -- zero extra compute, honors the rule)
- cot BRONZE ACTUALLY LANDS via skip: fresh opal-data-cot/bronze/ artifact (LastModified-advance) + chain advances bronze->silver->gold->served on the natural run.
- SKIP = ZERO OTP-LOGIN: the 02:00 run dispatches opal-cot-bronze-run but NOT opal-cot-bd-session-fetch -> zero OIDC-login/MFA_OTP ops in the box run log.
- 0.7.0~A confirms skip-not-mint from the daily logs; I verify served/bronze artifacts + zero-login independently.
- On live-verify PASS -> RAVC COO -> close cot ledger. A fail = fast-follow (fail-safe + keepalive bound it), NOT a rollback.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| aws lambda/secretsmanager (PowerShell) | get-function-configuration (hash) + describe-secret (cookie) | PASS | deploy hash match + cookie live, firm-sep opal-data-cot |
| Read (cot lambda_function.py) | _session_is_positive_live + _handle_session_refresh + _handle_bronze_run | PASS | fail-safe-absolute + single-fire + parity, matches validated 49F pattern |

## Disposition
cot = HELD-PENDING-NATURAL-DAILY. TWO belts now on tomorrow's dailies: 49F (all-4-fresh via skip) + cot (bronze-lands via skip), both rule-mandated-scheduled, both non-blocking. RAVC COO on each cert-PASS.

-- 3.0.0_SA_CVO
