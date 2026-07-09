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
- **trending-image NUANCE:** verbatim `ResourceNotFoundException ... GetSecretValue ... can't find the
  specified secret` then `raise ValueError("OpenAI API key not found")`. **It crashes, it does not
  fail-silent** -> fails axis B like schwab UNLESS a consumer depends on the fresh image (crash -> stale
  user-facing image = the SEV3). Mechanism CVO-verified; the SEV3-LIVE-vs-broken-but-safe call is
  owner-side (needs the consumer-dependency check). Runs under news-ingestion-lambda-role.

## ACCEPTED (grounded), NON-LIVE

- **yang** -- LATENT (last ran 175d ago; empty-VIX would be live only on a run).
- **schwab** -- BROKEN-BUT-SAFE (raises; isolated, no bad data served).
- **smartx-ingestion** -- RETRACTED (axis-C: the crashing getter is never invoked; the reachable getters
  take a designed `None`-fallback; 378 log events / 3 days, 0 errors, real $1.746B output).
- **opal-smartx-lambda-role** -- orphan-DROPPED from the denominator (axis-C: trust policy admits
  `lambda.amazonaws.com` only, no instance-profile, `RoleLastUsed` 191d -> no principal CAN assume it).

## Sweep-close accounting

Proven universe = dead-grant-8 (A, IAM-enumerable, minus dual/missing/orphan false-positives) + 0.5.0's
no-grant + missing-secret enumerations, each row filtered through axis-B and axis-C. **CVO-confirmed LIVE
set: 2 clean SEV2 + 1 SEV3-pending-consumer-nuance. No SEV1.** -> CTO SEV-triage -> Andrew class-brief.
Separate minor: trending-image logs carry non-ASCII (emoji) -> CLAUDE.md violation, owner cleanup.
