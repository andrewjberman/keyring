# Data-Integrity Finding: the dead-reach x fail-silent x reachable CLASS
**For:** Andrew | **From:** 1.0.0_SA_CTO | **2026-07-09** | **Status:** Lambda universe PROVEN; estate (non-Lambda) OPEN

## It is a CLASS, not incidents
A recurring pattern surfaced while exercising the credential firm-separation work: a consumer holds a credential
grant that is DEAD (or absent), a reader SWALLOWS the resulting failure instead of failing loud, and the code path
is LIVE with a downstream consumer -- so the system silently ships degraded output at HTTP 200 / a clean-looking
exit. Three independent axes; a row is a live degrade only if it fails ALL three:

- **A -- dead reach**: the credential can't be read. Three sub-shapes -- dead-grant-by-region (grant in us-east-2,
  client calls us-east-1), no-grant-at-all (role never granted it), missing-secret (grant aligned, secret absent in
  the client's region).
- **B -- fail-silent reader**: the reader swallows the denial (`except: return None/''`) instead of raising.
- **C -- reachable with a dependent consumer**: the degraded path actually executes and something downstream
  depends on its output. (A dead reach on an unreachable path, or with a designed fallback, or with no consumer, is
  not a degrade -- it fails C.)

## Lambda universe: 2 live fail-silent degrades, none SEV1
Every row hand-verified against the deployed artifact, live IAM, and the Lambda's own logs, and independently
cert-verified by the CVO:
1. **security-sweep-comprehensive (SEV2)** -- the meta-instance: the security scanner itself runs with no OpenAI
   key and still reports success. Grounded on the SERVED artifact: the AI leg is ENRICHMENT (the 77KB
   findings.json proves deterministic detection ran independently), so there is NO detection blind spot. The defect
   is that it reports success with a dark leg, and the artifact announcing the failure is one nobody reads.
2. **daily-agenda-generator (SEV2)** -- a region-mismatched dead grant on the GitHub token; the daily agenda
   silently omits private-repo commit data. Logged-but-unwatched.
These are NOT fail-silent degrades -- the discipline that kept the class to two, not four:
- **Broken (LOUD) but unwatched**: opal-trending-image-generator -- it CRASHES (HTTP 500 + traceback every run,
  191 days), so it fails LOUD, not silent -- a reliability finding, not a silent degrade. Root: both boto3 clients
  are hardcoded to `region_name='us-east-2'` (zero secrets, and the target table lives in us-east-1) -- a
  region-literal CODE bug, not a grant/IAM issue; no grant fix or secret replication helps, only repointing the
  region. It was first read as fail-silent by binding axis B to the getter's `return ''`; corrected when an
  independent read of the caller showed the caller raises on that '' -- the fail-mode is a property of the whole
  caller chain, not the `except` nearest the secret. (The exact inverse of the auth-path finding, where a loud
  reader is silenced by a swallowing caller.)
- **Latent**: yang-generate-volatility (grant aligned, secret absent, 175 days dormant).
- **Broken-but-safe**: schwab-anonymizer (fails LOUD -- raises; never ran; no PII path). Identical dead-reach to
  the security scanner, opposite fail-mode -- which is the whole point: the grant does not determine severity, the
  reader's fail-mode (and reachability) does.

## The pattern ALSO appears on the AUTH path -- the highest-stakes instance
The portal login handler (`authenticateRequest`) swallows a secret-read failure into a generic 401 with no log
line. LATENT today (the jwt grant is intact, simulate-proven), but if that grant were ever lost, every
authenticated request would silently 401 -- indistinguishable from users mistyping passwords, invisible in
CloudWatch: a silent auth-outage. Same class, on the auth path.

## Honest scope: the estate is NOT fully swept
The instrument (comp-deadgrant) enumerates Lambda functions ONLY -- it is structurally blind to EC2, ECS, Batch,
CodeBuild, and human/CI principals. So:
- The **Lambda universe is PROVEN** (stabilized: a clean re-run finds no new true positive; five false-positive
  shapes removed).
- The **estate (non-Lambda) dead-grant half is now CLOSED** -- two independent instruments (a CVO IAM-denominator
  of 17 non-Lambda secret-readers, and a 0.5.0 enumeration of 23 EC2 instance profiles) converge on exactly ONE
  dead grant (opal-layer3-ec2-role), which is inert (zero instances in any state, no launch-template, no ASG =
  nothing can carry it). No dead grant hides in EC2/ECS/Batch/CodeBuild.
- The **no-grant + missing-secret half on non-Lambda is still OPEN** -- a non-Lambda consumer whose code reads a
  secret it lacks a grant for needs a code-side scan of what those instances pull from S3 (the analogue of the
  Lambda deployed-zip scan). That is the post-NFRA estate-mode. So the estate is dead-grant-half-proven-clean,
  no-grant-half-bounded-but-not-swept.
- A firm-sep item fell out of the EC2 sweep: cot-gold-layer-ec2-role holds cot firm-credential read grants with
  zero instances (an orphan standing grant on a firm credential) -- routed to the CVO for a firm-membership
  grounding (same-firm = a least-privilege cleanup; cross-firm = a NEVER#1 escalation even though inert).

## Fixes (all post-NFRA)
- **Fail-loud, not fail-silent** (the load-bearing fix): security-sweep + the auth path must distinguish
  infra-failure (key unavailable) from an expected negative, and log/alarm the former -- so a future
  credential-loss is VISIBLE, not a silent 200/401.
- Repoint the region-mismatched grants (daily-agenda) / replicate the missing secrets.

## Why the set is two, not four
Two instruments and two readers, adversarial. The detector emitted wrong rows in several distinct ways --
false-negative (code-shape enumeration), false-positive (a comment mention), wrong-mechanism (a stale in-zip copy
shadowing the live handler's region), wrong-action (testing read on a write-only name), and getter-level fail-mode
(reading the `except` nearest the secret, not the caller chain). One false-positive would have accused a FIRM
credential (orion/eclipse_jwt). Beyond the tool, careful HAND-VERIFICATION bound the wrong PROPERTY twice -- smartx
(missed axis C: the crashing path is never reached) and trending-image (missed the caller chain: the getter
swallows but the caller raises). Every one was caught by grounding against the verbatim logs, the source, and the
live simulate BEFORE routing -- and by an independent cert reading the artifact the finder hadn't. The result is a
smaller set we can defend over a larger one we cannot -- and the tool now prints CANDIDATES, not findings, refusing
to name a property it cannot prove.
