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
| `opal-trending-image-generator` | -- | hardcoded us-east-2 client (0 secrets) | getter swallows, caller RAISES -> net loud (500) | **icon_type NOT consumed** | **BROKEN-BUT-SAFE (dropped)** |

**CVO-CONFIRMED LIVE DEGRADE SET = 2 SEV2** (daily-agenda, security-sweep). trending-image dropped to
broken-but-safe (below).

- **daily-agenda** served proof: canonical reference instance; grant re-confirmed `implicitDeny` live.
- **security-sweep** served proof: `s3://opal-data-portal-v2/security-reports/latest_ai_summary.txt` (52 B,
  today 08:02) = verbatim *"AI summary unavailable (could not fetch OpenAI key)."* Core detection intact
  (findings.json) -> SEV2 (enrich degraded, not core).
- **trending-image RESOLVED on the DEPLOYED artifact (Handler `lambda_function.lambda_handler`, 2025-12-30):**
  the raise-vs-return disagreement (my `raise` vs 0.5.0's `return ''`) reconciles -- BOTH right at different
  levels: `get_openai_key()` (:138-146) `except -> return ''` (getter fail-silent), then the handler
  (:234-237) `if not api_key: raise ValueError` -- **net RAISES** (live-log traceback confirms). Fails axis B
  at the PRODUCER, like schwab. **Sharper root:** `secrets_client = boto3.client('secretsmanager',
  region_name='us-east-2')` (:17, + the DynamoDB client :16) -- the client is HARDCODED to us-east-2 (0 secrets)
  -> ResourceNotFound on any read; a code-wrong-region bug, NOT a grant issue (no grant/secret-replication fix
  helps -- the target table `opal-news-trending-daily` doesn't exist in us-east-2 either), broken 191d.
  **CONSUMER CHECK (definitive): BROKEN-BUT-SAFE.** Output is a DynamoDB `icon_type` field; `portal_data_proxy`
  (the served `/v1/trending/*` path) has **ZERO refs to icon_type** -- it is never read; and the frontend
  (`ExecutiveSummary.tsx`) renders `<img onError=... >` -> graceful lucide sentiment fallback. The crash raises
  into a NON-CONSUMED output -> no served effect -> broken-but-safe, not a live degrade. Also a **dead producer**
  (191d, unconsumed output) -> decommission/repoint candidate (cleanup, not a security degrade).

- **opal-layer3-ec2-role (#4, the non-Lambda UNRESOLVED gap) -- CLOSED structurally:** openai-api-key grant
  us-east-2-only (truly-dead). Instance profile `opal-portal-ec2-profile` exists (an EC2 CAN assume it, so not
  trust-policy-closable like the smartx orphan), BUT: `describe-instances` on the profile ARN across **ALL
  states** (incl. stopped) = NONE; **no launch template** references it; **no ASG** references it. So no
  consumer exists in any state and none is auto-provisioned -> INERT (not "no running EC2" absence-of-search;
  structural). Honest residual: role+profile persist -> a manual future launch is possible = latent-at-worst
  (like yang). The non-Lambda ESTATE-MODE (all ECS/Batch/CodeBuild/EC2 principals, not just this row) remains
  the open estate-closure step -- offered to CTO as a third-instrument enumeration.

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
axis-B and axis-C. **CVO-confirmed LIVE degrade set: 2 SEV2 (daily-agenda, security-sweep). No SEV3, no
SEV1.** trending-image broken-but-safe (unconsumed output); opal-layer3-ec2 INERT (structural); yang latent;
schwab/smartx safe/retracted. -> Andrew class-brief on the 2-SEV2 reconciled universe.
OPEN estate-closure step: the non-Lambda ESTATE-MODE (all ECS/Batch/CodeBuild/EC2 secret-readers, which both
0.5.0's Lambda-sweep and my IAM-grant-enum miss) -- offered to CTO as a third-instrument enumeration.
Separate minors, owner cleanup: trending-image logs carry non-ASCII emoji (CLAUDE.md); trending clients
(:16-17) hardcode `region_name='us-east-2'` (a wrong-region code literal -> repoint or decommission);
market-update + trending share the us-east-2-client-region sub-shape.
Fail-mode is a CALLER-CHAIN property, not the `except` nearest the secret (auth: component-loud/system-silent;
trending: component-silent/system-loud -- mirror images). [[feedback_check_must_bind_to_property_exercised_not_proxy]]
