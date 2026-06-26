# Session Log -- 0.5.0_AE_OpalETL -- ASTN CEO-brief outage (root-cause+fix) + comp-iam FALSE-MISSING collision (root-cause+fix shipped)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, IMPLEMENT, COORDINATE
**Date:** 2026-06-26 | **Window:** ~14:00Z -> 15:05Z (Andrew-direct, continuous)

## Summary

Andrew-direct: "did the ASTN WSJ&FT brief go out to Austin this morning? find it + forward it to me."
Answer: it did NOT. Root-caused to a half-landed IAM deploy, fixed + live-verified. Forwarded the
last real brief (06-24) to andrew@ via SES. That diagnosis also surfaced a comp-iam tool defect --
which Andrew escalated ("get to the bottom of this, serious; report to CTO + CVO"). Root-caused the
comp-iam FALSE-MISSING to a cross-file TF resource-name collision (CORRECTING my own + CTO's "stale
cache/census" mis-framing), built + committed the fix under CTO arch-gate.

## 1. ASTN CEO brief -- did NOT send 06-26; half-landed orchestrator IAM (FIXED + verified)

GROUNDED (live CloudWatch /aws/lambda/astn-wsjft-orchestrator): the 3am orchestrator fired but failed
at `_ec2.start_instances` -> UnauthorizedOperation: astn-wsjft-orchestrator-role not authorized for
ec2:StartInstances. Runner never started -> no fetch/digest/SES. No 06-25/06-26 audit artifacts in
s3://opal-data-astn/email/ (last real render = 06-24). comp-iam: role missing all 8 ops --
aws_iam_role_policy.orchestrator DECLARED in orchestrator.tf, NEVER APPLIED live (half-landed deploy,
Lambda shipped 06-25 13:08, policy never landed = the NEVER-rule failure mode).

FIX (astn-pipeline TF root, CTO arch-gated lane; Andrew-direct + AE IAM/EC2 competency):
- A plain apply wanted to REPLACE the EC2 (associate_public_ip_address false->true on the stopped host
  -- the etfs-reports ephemeral-IP drift class), and the IAM policy ARN refs the instance, so any apply
  bundled an instance destroy. Commit 58a2211: lifecycle ignore_changes=[associate_public_ip_address].
- safe-apply (HALT_ACK=1): 0 added / 2 changed / 0 destroyed; instance id UNCHANGED. role_policy landed.
- VERIFIED LIVE (authoritative get-role-policy, NOT comp-iam): full policy present (ec2:Start/Stop +
  ssm + sns + s3 + logs). Ledger 0c715e034 CLOSED.
- E2E (real send) deferred to tomorrow's 3am run per Andrew (no off-schedule CEO send; 4am absence-guard
  backstops). Forwarded 06-24 brief to andrew@ via SES (MessageId 0100019f0449049f-...).

## 2. comp-iam FALSE-MISSING -- root-caused to a cross-file TF resource-name COLLISION (fix SHIPPED)

CORRECTION (mine + CTO's): NOT "stale cached live snapshot" / "census staleness". comp-iam
service/gaps NEVER read live (TF-DESIRED only; iam_cli source-confirmed). The astn all-MISSING was
INVARIANT to my apply -> a static parse defect.

ROOT CAUSE (extract_iam.py, source-grounded + reproduced): role_tf_to_name keyed by the BARE tf
resource label, last-writer-wins, not module-namespaced. astn-pipeline + etfs-reports both declare
`aws_iam_role "orchestrator"`/`"scheduler"` -> the later-scanned (etfs) wins the key -> astn's inline
policy statements attach to the WRONG role -> astn roles credited 0 statements -> every action
FALSE-MISSING. Reproduced: isolated parse=7+1 correct (parse fine, LINKAGE is the bug); full build =
astn roles 0 stmts, etfs winner double-counted (16 = its 9 + astn's 7 mis-attached).

BLAST (rigorous pre/post action-set diff, all 114 roles): exactly 2 roles changed (both astn,
false-MISSING). NO false-GREEN materialized (winner's own policy independently covers the same actions
-> action verdict unchanged). CVO's "5 keys" / my raw-grep "9" reconcile: extras are OUT of comp-iam's
scan scope (_parse_terraform_iam globs only infra/aws/terraform/**; multi-account/ + ec2/*/terraform +
org/threads doc-refs never scanned) or single-module -> none corrupted a verdict. (Scan-scope hole =
separate coverage gap -> CVO campaign.)

FIX (commit d7ccc029e, CTO arch-gate GO 145903Z): key role_tf_to_name by (module_dir, tf_resource) +
resolve role refs module-locally (all 4 sites) + loud collision guard (stderr NOTE on bare-label reuse,
fired on orchestrator+scheduler) + `import sys`. POST-commit estate scan: astn-orchestrator 7 stmts,
ec2:StartInstances [GRANTED]; 0 false-missing. Regression test (org/modules/graph/tests/, GREEN: 3 pass
post-fix, reproduces bug pre-fix, generic lambda_role divergent-policy case) -- EXEC-LANE blocked for AE,
routed to CVO to commit during independent verify. Ledger-leg "IAM grants live-verified before close"
drafted to CTO (co-author).

REPORTS: brief e4866f07f -> CTO (144428Z) + CVO (144508Z). CTO owns the conflation; CVO blessed the
interim posture (ground IAM verification on live get-role-policy until fixed) + banked the
knowledge-parity catch (CLAUDE.md overstates comp-iam as "TF-vs-live reconcile" -- service/gaps are TF-only).

## Compiler Tools

| Tool | Call | Result |
|---|---|---|
| comp-iam | service/role astn-wsjft-orchestrator (pre+post fix) | pre: all-MISSING (the bug); post: GRANTED -- fix verified |
| comp-iam | service etf-ownership-dashboard | ses UNMODELED (earlier SES validation) |
| comp-which/comp-grep/comp-glob | route + locate extract_iam, role collisions, astn TF | found the collision set + producer files |
| comp-freshness | chain bd / chain inf | bd fresh (earlier MDPF verify) |
| pipescript | mdpf / --resource | producer arch (earlier MDPF) |
| terraform | plan (targeted+full) / safe-apply / 0-diff | astn IAM apply 0-destroy; instance not replaced |
| ds-commit-gate | extract_iam.py + test | PASS (py_compile + ruff clean) |
| pytest | test_iam_role_label_collision.py | 3 passed post-fix; reproduces bug pre-fix |

**What worked:** verify-against-LIVE (get-role-policy) was the only ground truth -- comp-iam's
DESIRED verdict was itself the defect. Rule-22 discipline: falsified the "stale cache" hypothesis by
reading source, repro-confirmed the real mechanism (collision) before asserting. Pre/post action-set
diff gave the authoritative blast radius (2 roles), reconciling the 2-vs-5-vs-9 count confusion.
**What failed:** my first framing ("stale cached snapshot") was wrong -- comp-iam never reads live;
caught + corrected on source read. The regression test hit an exec-lane owned-paths block (AE can't
write org/modules/graph/tests/) -> routed to CVO rather than --force past the guard.
**Gap found:** (1) the comp-iam collision bug itself (FIXED). (2) comp-iam scan-scope: only globs
infra/aws/terraform/** -> multi-account/ + ec2/*/terraform roots get NO IAM gap-check (-> CVO campaign).
(3) CLAUDE.md overstates comp-iam as live-reconcile (-> CVO flagged to CTO).

## Current State

- ASTN CEO brief: orchestrator IAM RESTORED + live-verified (commit 58a2211 + apply + ledger 0c715e034).
  E2E pending tomorrow's 3am run; 4am absence-guard + dual-alert (andrew@ + opal-critical-surface) backstop.
  Forwarded 06-24 brief to andrew@.
- comp-iam collision fix: LANDED d7ccc029e (CLOUD). extract_iam.py module-namespaced. Regression test
  in working tree, routed to CVO (exec-lane) to commit during independent verify.
- Earlier this session: MDPF aggregate_aua freeze RESOLVED+verified (COO-accepted, disambiguation on
  tonight's INF run); ETFS-SES RAVC closed (push gated on Andrew list); 3 comp-coverage gaps -> CTO.

## Next Steps

- **[3.0.0_SA_CVO]** independently verify d7ccc029e + COMMIT the exec-lane regression test
  (org/modules/graph/tests/test_iam_role_label_collision.py); own the comp-tools scan-scope campaign.
- **[1.0.0_SA_CTO]** wire the IAM-applied-verification ledger-leg into the deploy-completion template.
- **[0.5.0_AE_OpalETL / self]** post-3am tomorrow: verify the ASTN brief sent (served artifact +
  SES) -> RAVC COO; verify MDPF 06-26 vs the 06-24/25 step -> backfill-or-not -> RAVC COO.
- **[Andrew/0.7.0]** ETFS SES recipient list -> activate dashboard push.
