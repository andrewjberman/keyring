# NFRA_CTLPLN TO-APPLY-14: Dell identity step E

Seat: 0.7.0_AE_CloudOps. Device: laptop. Recorded before apply: 2026-10-08T17:57:05.583495+00:00.

Authorization: GO Msg-ID 107058, exact order in this seat's task_orders home. COO half @9a8758bddf and CTO half @ee3578d886 both SIGNED and read in full. GO states both Dell managers acknowledged the extended before-rule. Andrew was informed in this turn that the grant enables Dell seats to act as the platform. CLOUD HEAD 049d81ffa65d1128a8b29322c32a259642eee008 contains merge e80238bdab; root status empty. No shared-branch push.

EXPECTED OUTCOME before ledger opening: apply the saved, untargeted, default-variable plan once through safe-apply. Exactly two additions (platform-secret policy and attachment), three in-place policy updates, zero destroys and no other address. Group increases from six to seven attached policies. The 28 platform keys become readable; named resource-policy permissions become allowed. Audit-stop, audit-bucket lifecycle, protected-function deployment, IAM writes and the two withheld-secret reads remain refused. Bus send and own-queue receive remain allowed. Re-plan must exit 0. If any preflight shape/count differs, apply nothing. Status remains APPLIED until both Dells supply their own graph-query evidence.

Pre-plan simulation: POLICY-SIM allowed_ok=22/22 denied_ok=15/15 passrole_ok=5/5 protected_ok=8/8 freed_allowed=72/72 freed_excluded=3 undo_freed=167/167 undo_still_denied=443 selfsim_ok=9/9 ssm_ok=15/15 routes_ok=5/5 vendor_ok=245/245 all_ok=True.

Plan gate: 2 add / 3 change / 0 destroy across exactly the five authorized addresses. Added-line counts: secret ARNs 28; quoted iam actions 0; Secrets Manager PutResourcePolicy 0; DeleteResourcePolicy 0. Saved plan SHA256 674e6eda03b3eb8febe6c359b709fa73f3bd1d12a6686f2e965a08743fee39ec. Evidence: plan-gate.json, plan-before.txt and simulation-before.txt beside this log.

BEFORE: before-iam.json contains the group's six attachments and policy documents. Saved defaults: cloudops-dell-agent-deploy-policy v3; cloudops-dell-agent-create-policy v2; cloudops-dell-agent-respol-allow-policy v1.

Rollback: detach and delete the new cloudops-dell-agent-platform-secrets-policy, then restore the three saved default versions; alternatively safely re-apply this root at e80238bdab^1. The record does not claim this reverses any secret read or resource-policy change a Dell makes during the interval. No secret value or resource policy will be read or changed by this seat.

Tool scope: comp-which routing inspected; comp-iam help/simulate interface inspected (role-oriented); the mandated cell simulator supplies the desired-policy battery. Live verification will use one resource per aws iam simulate-principal-policy invocation, with separate admin positive controls for denials and resource-existence reads. Sequence: NFRA_CTLPLN placed at active stage 0. No schedule change; comp-schedule N/A.

MEASURED RESULT: applied 2026-10-08T18:00:17Z (five CloudTrail IAM events), 2/3/0 and exit 0; 26/26 live arms, 6/6 isolated admin controls, 10/10 plan/live policy documents, 7 group attachments, retained rollback versions 3/3, and exact AC2 exit=0. No rollback. APPLIED pending Dell graph queries. Readback transport fixes were diagnostic-only; one apply total. Detailed report: org/tier2_senior/0.7.0_AE_CloudOps/deliverables/NFRA_CTLPLN.TO-APPLY-14.step-e-report.md

CLOSURE: governing-order-bound proof VALID rc=0, 2/2 acceptance rows, zero violations. All three ledger legs CLOSED; sentinel removed. Full report and evidence committed together; final hash accompanies the peer closure message. No task-order status edit (issuer owns it).
