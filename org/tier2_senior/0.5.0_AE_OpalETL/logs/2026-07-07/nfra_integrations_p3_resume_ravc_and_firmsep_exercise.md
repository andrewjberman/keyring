# NFRA_INTEGRATIONS-003 P3 STORAGE -- resume: ground-truth RAVC + firm-sep deploy-gate EXERCISED

**archetype:** VALIDATE
**Date:** 2026-07-07 | **Serial:** 0.5.0_AE_OpalETL | **TO:** NFRA_INTEGRATIONS-003 (P3 storage, COO DRIVE 2026-07-07T05:49Z)

## Context
Wave-2 NFRA resume (Andrew-direct). COO fired a DRIVE TO to "execute NOW / build the P3 storage
schema -> CTO gate -> CVO round-trip cert" to close NFRA_INTEGRATIONS 3/3, believing thread-003 was
"self-filed staged / un-landed."

## Ground-truth finding (the key correction)
P3 STORAGE is NOT un-started. The schema was authored, folded, committed, and RAVC'd on 2026-07-02:
- **commit bbd766bc2** -- STANDARD.md NEW sec 9 "Storage & dependency model" (9.1 two dependency
  models gateway-venv vs pipeline-Lambda-layer + don't-cross; 9.2 persisted-data firm-separation
  invariant GROUNDED; 9.3 spec.hosts egress + SCTY_PREMCP SSRF). Status v1.3, CTO-APPROVE-PENDING.
- Working tree clean; all 6 TO reqs covered (surgical, net-new only -- code-location/tool_prefix/
  one-SM-secret already canonical in sec2/4/5/8, not restated).
- Prior authoring lineage: 13fe36aa3 (draft) -> 6f742253c (firm-sep re-grounded) -> bbd766bc2 (fold).

So the remaining path to CLOSE is TWO gates, both others' actions, which I drove this session:
1. CTO arch-gate APPROVE of sec9 (pending since 07-02).
2. CVO exercise-cert.

## Work this session
1. Startup: /watcher (registered PID 27464, persistent Monitor task bjirsb4e8 armed), org/XXX.md
   protocol, session-serial file, comp-graph context, comp-to set to the P3 TO.
2. Grounded the full P3 state via git log (schema committed, approve-pending) + read STANDARD.md sec9
   + the seed draft (already RETIRED->pointer) + project JSON thread-003.
3. **EXERCISED the firm-separation deploy-gate** (sec9.2 leg-1) to answer COO's "prove it BITES, not
   a config-read" -- ran `safe_deploy_core.file_to_s3_target` live:
   - bucket is a PURE FUNCTION of the firm-tree dir: black_diamond->opal-data-bd, cot->opal-data-cot,
     inf->opal-data-inf (each only).
   - a bd script -> opal-data-cot? FALSE; -> opal-data-inf? FALSE. No override arg exists.
   - foreign/unmapped trees (data/schwab, data/evil, notdata/bd) -> None (REJECTED, deploy refuses;
     NOT defaulted). => cross-firm deploy structurally impossible, not policy.
   - Leg-2 (runtime IAM explicit cross-firm Deny, DenyCrossFirmBuckets) is the defense-in-depth 2nd layer.
4. RAVC'd COO with the ground-truth correction + the exercise result (20260707T055225Z).
5. Requested CTO arch-gate APPROVE of sec9 (20260707T055241Z), CC context to COO.

## Handoffs / next
- **CTO:** approve sec9 (open loop since 07-02). On approve I flip v1.3 -> v1.3-CTO-APPROVED.
- **CVO exercise-cert (teed, dispatched AFTER CTO approve -- correct sequence):** since NO integration
  persists data today (YCharts read-only-passthrough; kuzu/nessie/iceberg read-only in-estate), the
  "round-trip that proves the contract bites" = exercising the firm-sep ENFORCEMENT: leg-1 deploy-gate
  DONE (above); leg-2 = live `aws iam get-role-policy` on the firm role to confirm the DenyCrossFirmBuckets
  Deny-overrides-Allow is APPLIED (Rule 22a applied-truth). Concrete target handed to CVO post-CTO-approve.
- This closes NFRA_INTEGRATIONS 3/3 on those two gates.

## Compiler Tools
| Tool | Result | Note |
|---|---|---|
| comp-to | OK -- session TO_ID = NFRA_INTEGRATIONS.P3... | race-free per-session TO attribution |
| safe_deploy_core.file_to_s3_target (PIPELINE_MAP) | EXERCISED -- firm-sep deploy-gate bites structurally | direct grounding of sec9.2 leg-1 per the TO's compiler mandate ("ground the rule-13 PIPELINE_MAP"); confirmed cross-firm deploy structurally impossible + foreign-tree reject |

No comp-iam run this session: leg-2 (runtime IAM cross-firm Deny live-apply) is the CVO exercise-cert
leg (handed as the concrete target), not the AE authoring portion; the AE schema deliverable was
committed 07-02 and this session's AE contribution was exercising the deploy-gate leg (my own tooling).
