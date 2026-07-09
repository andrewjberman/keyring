# CVO SWEEP-CLOSE VERIFICATION -- freshness-integrity dead-reach LIVE set

**Closes:** the freshness-integrity class-sweep (region-mismatch/dead-grant + fail-silent-reader).
**Verifier:** 3.0.0_SA_CVO -- each row grounded independently against live/served (not on report; 0.5.0 had
5 detector + 1 hand-verify rows wrong tonight, so no rubber-stamp). Date: 2026-07-09.

## The three-axis model (converged this session)

A LIVE degrade = **{dead reach} x {fail-silent reader} x {reachable path with a dependent consumer}**.
- Axis A (dead reach): my dead-grant denominator (8) + 0.5.0's no-grant + missing-secret enumerations.
- Axis B (fail-silent): the reader swallows the failure instead of raising.
- Axis C (reachable-with-consumer): the degraded path actually executes AND something depends on its output.
"A call site's PRESENCE in the artifact is not its REACHABILITY from the handler" (0.5.0's fifth defect
class, self-caught in hand-verification). My orphan-drop = axis-C at the DENOMINATOR; 0.5.0's smartx-retract
= axis-C at the ROW. Same property.

## CONFIRMED LIVE (CVO-grounded)

| row | sev | axis-A (dead reach) | axis-B | axis-C | verdict |
|---|---|---|---|---|---|
| `daily-agenda-generator` | SEV2 | github-token us-east-1 `implicitDeny` (live, fix filed post-NFRA) | fail-silent -> no private-repo data | runs daily | **LIVE, clean** |
| `security-sweep-comprehensive` | SEV2 | openai-api-key (AI-enrich leg) | fail-silent -> 52-byte placeholder | sweep runs (served 08:02 today) | **LIVE, clean** |
| `opal-trending-image-generator` | SEV3 | openai-api-key MISSING (`ResourceNotFoundException`) | **RAISES `ValueError` -- NOT fail-silent** | crashes each run | **mechanism LIVE; SEV NUANCE** |

- **daily-agenda** served proof: canonical reference instance; grant re-confirmed `implicitDeny` live.
- **security-sweep** served proof: `s3://opal-data-portal-v2/security-reports/latest_ai_summary.txt` (52 B,
  today 08:02) = verbatim *"AI summary unavailable (could not fetch OpenAI key)."* Core detection intact
  (findings.json) -> SEV2 (enrich degraded, not core).
- **trending-image RESOLVED on the DEPLOYED artifact (Handler `lambda_function.lambda_handler`, 2025-12-30):**
  the raise-vs-return disagreement (my `raise` vs 0.5.0's `return ''`) reconciles -- BOTH right at different
  levels: `get_openai_key()` (:138-146) `except -> return ''` (getter fail-silent), then the handler
  (:234-237) `if not api_key: raise ValueError` -- **net RAISES** (live-log traceback confirms). Fails axis B
  at the PRODUCER, like schwab. **Sharper root:** `secrets_client = boto3.client('secretsmanager',
  region_name='us-east-2')` (:17) -- the client is HARDCODED to us-east-2 (0 secrets) -> ResourceNotFound on
  any read; a code-wrong-region bug, NOT a grant issue (no grant fix helps), broken 191d. **Output is a
  DynamoDB `icon_type` (us-east-2), not an S3 image.** SEV3-LIVE iff a frontend serves the STALE icon_type
  (raises-into-stale-serving-consumer); broken-but-safe if unconsumed. **CTO finalizes the consumer call.**

- **opal-layer3-ec2-role (#4, the non-Lambda UNRESOLVED gap) -- CLOSED from EC2/IAM:** openai-api-key grant
  us-east-2-only (truly-dead); instance profile `opal-portal-ec2-profile` exists but **NO running EC2 carries
  it** (describe-instances empty; RoleLastUsed 206d) -> axis C fails, no live consumer -> INERT/latent (stopped
  instance = latent-at-worst). The estate gap both code-side instruments (Lambda-only) were blind to, closed
  for this row from the non-Lambda side.

## ACCEPTED (grounded), NON-LIVE

- **yang** -- LATENT (last ran 175d ago; empty-VIX would be live only on a run).
- **schwab** -- BROKEN-BUT-SAFE (raises; isolated, no bad data served).
- **smartx-ingestion** -- RETRACTED (axis-C: the crashing getter is never invoked; the reachable getters
  take a designed `None`-fallback; 378 log events / 3 days, 0 errors, real $1.746B output).
- **opal-smartx-lambda-role** -- orphan-DROPPED from the denominator (axis-C: trust policy admits
  `lambda.amazonaws.com` only, no instance-profile, `RoleLastUsed` 191d -> no principal CAN assume it).

## Sweep-close accounting

Proven universe = dead-grant-8 (A, IAM-enumerable, minus dual/missing/orphan false-positives) + 0.5.0's
no-grant + missing-secret enumerations + the non-Lambda EC2 check (layer3), each row filtered through
axis-B and axis-C. **CVO-confirmed LIVE set: 2 clean SEV2 (daily-agenda, security-sweep); trending-image
producer-RAISES (root: hardcoded us-east-2 client) pending CTO's stale-icon consumer call; opal-layer3-ec2
INERT (no running consumer). No SEV1.** -> CTO SEV-finalize -> Andrew class-brief.
Separate minors, owner cleanup: trending-image logs carry non-ASCII emoji (CLAUDE.md violation); the
trending client is hardcoded to us-east-2 (a Rule-23-adjacent wrong-region literal, not a grant fix).
