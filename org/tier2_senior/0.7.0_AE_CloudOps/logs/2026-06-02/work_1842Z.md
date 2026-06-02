# work cycle — 0.7.0_AE_CloudOps — 2026-06-02 ~1842Z

## TO: ADVI_INFPRM.W2 (getClientsTab firmId-fallback, Symptom 2) — IMPL-COMPLETE + DEPLOYED

Session arm: /watcher (orphan watcher cleared, re-registered LIVE PID 37876, tracked
watcher relaunched) -> /cloud-ops one-shot -> CronCreate /work 20m (dec2b98f) -> /work.

### AC-W2-confirm — PASS (CONFIRM-FIRST gate)
Confirmed the P0 bifurcation against live infra before building:
- static-S3 (shared-advisor-router index.mjs:87-88) self-scopes firmId from the X-Firm-Id
  header injected by auth-validator-edge:388 from validated JWT -> external users fine;
  ?firm= consulted only for opal-capital (:184-198).
- opal-partners-data: firm_id ONLY from ?firmId= (:1685 advisor-intelligence, :1778 books)
  -> 400, no JWT fallback; user_firm_id already read from authorizer at :1626. THE bug.

### Fix (commit 15d500737)
Added authorizer-firmId fallback to BOTH ?firmId= gate blocks: `if not firm_id: firm_id =
user_firm_id`. Fires ONLY when ?firmId= absent (explicit-firmId callers unaffected);
is_authorized() still gates the resolved firm (no cross-tenant leak). ds-commit-gate PASS.

### BLOCKER raised + COO ruling A (deploy-scope)
Caught that opal-partners-data deploys terraform-from-repo and live prod (sha WYPa2dd...) was
BEHIND repo HEAD by the stranded INFLFE.005 Part A delta (94f8d45f9, COO-accepted 2026-05-05
but never deployed) whose cloudwatch:PutMetricData grant is absent from both live role AND
repo iam.tf -> deploying HEAD would ship INFLFE.005 non-functional (AccessDenied, caught) +
log-spam. Routed [BLOCKED-ASK] to COO. COO ruled **A (ISOLATE W2)** + is tracking INFLFE.005
separately as a premature-closure/undeployed-tail finding (-> CTO+DT).

### Deploy (isolated, COO ruling A)
Built W2-isolated artifact = LIVE base (downloaded from live get-function, sha-verified) +
the 2 W2 fallback blocks ONLY (deterministic Python transform; 3 sibling modules byte-identical;
INFLFE.005 excluded). Hash dMa8oXxOP2FDd12GYDzy7/V0rSFLTPftAMFTvaMVp9s=.
- Uploaded to S3 (content-sha256 metadata) -> terraform plan = single in-place source_code_hash
  update -> .tools/safe-apply.sh (HALTGT passed silently) -> 0-diff full plan verified.
- source-map updated honestly (artifact_sha256 ground-truth + deploy_note documenting the
  deployed!=any-commit provenance + INFLFE.005 tracked-elsewhere); commit e7f16a12b [skip ci].
- Tagged partners-api-v1.16.2 + push --follow-tags. comp-iam no-gap (W2 adds no AWS call).

### Functional + regression + security (live Lambda invoke, read-only GETs)
| Test | Scenario | Result |
|---|---|---|
| T1 (FIX) | external inflection, no firmId | 200, firm_id=inflection (was 400) |
| T2 | explicit firmId=inflection | 200, firm_id=inflection — unchanged |
| T3 | 49financial external, no firmId | 200, firm_id=49financial |
| T4 | internal opal-capital, explicit firmId | 200, firm_id=inflection — unchanged |
| T5 (security) | inflection user requests ?firmId=demo | 401 "Access denied to this firm" — authz preserved |

### Remaining (handed off in RAVC2)
CVO cross-tenant regression matrix (pairs with RD~C W1) + Andrew/CTO FE visual smoke (Peter
sees Firm Overview render). FE visual smoke is human-only (headless-chrome blocked fabric-wide).
RAVC2 sent to CTO + COO + CVO.

### Next
INFNNA W6.2 checker Lambda (QUEUED, landed; reuse mdpf-freshness-checker pattern) — started
scaffold study (canonical artifact s3://opal-data-inf/platinum/firm/advisor_nna_canonical.json).
