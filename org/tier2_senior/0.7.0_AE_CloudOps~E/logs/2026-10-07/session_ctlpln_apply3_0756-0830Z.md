# The Dell create grant and the access-deciding deny-list are LIVE, applied from the laptop -- 0.7.0_AE_CloudOps~E

**archetype:** DEPLOY

**Date:** 2026-10-07
**Task Order:** `NFRA_CTLPLN.TO-APPLY-3.dell-policy-apply-laptop` (issuer `2.0.0_SA_COO~C`, GO msg 106058)
**Status:** COMPLETE
**Workspace CLOUD commits:** `f381720cde` (ledger OPEN) -> `95b6e421cd` (apply + ledger CLOSE)
**Push state:** LOCAL. Origin CLOUD read `4cea56993a` by `git ls-remote` at report time; neither commit is an
ancestor of it. `CLOUD` is pushed only by `0.0.0_AB_MSTR` on Andrew's word -- not this seat's act, and not retried here.

---

## Objective

Apply ONE Terraform root (`infra/aws/terraform/nfra-ctlpln-identity/`) so the two Dell machines may create, update and
tag non-IAM resources while changing no access, cannot update ten access-deciding Lambda functions, and cannot read
API Gateway keys. Andrew-direct 2026-10-07: "Regarding DELLs, they shouldnt need to create or touch IAMs, they should
be allowed to create resources though." It is an IAM-changing apply, so the plan's exact shape gated the apply.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam gaps | `comp-iam gaps` | PASS | Required after any `iam.tf` change. 39 missing / 295 deny-present / 1 coverage-unknown / 3 resource-mismatch across 34 services; 880 calls verdicted over 105 mapped roles, 3 trees, 541 `.tf` files. ZERO lines name `cloudops` or `dell` (`grep -ic` = 0), so this act added no gap on its own objects. |
| comp-find | `comp-find "NON-APPEND-EDIT" --limit 15` | PASS | Run to find an owner for the startup audit-log finding. Exceeded the 120 s foreground limit and had to be backgrounded, but completed `exit 0` with 182 hits (15 shown, 167 paged) and ANSWERED the question: the class is CTO-ruled and owned (`audit-archive-invoker.py:404`, ruling `@4484d55608`), so no row was filed. Slow, but it was the tool that stopped me re-filing an owned class. |
| comp-which (forwarder exercise) | `comp-which "how do I grep the repo"` | PASS | Startup A.3: 104 of 104 comp-tools resolve bare and a forwarder actually RAN (resolved-but-dead ruled out). |
| comp-tool rail (HUD) | 3 denials + 1 advisory | PASS as designed | Gated every raw-`aws` IAM read. Two reads re-run under `# rail-checked:` because no comp-tool returns a managed policy's `DefaultVersionId` or its document bytes; one `comp-find` piped to `tail` correctly refused for erasing its denominator. |

**What worked:** `comp-iam gaps` gave the one answer that mattered -- that the act introduced no gap on its own
objects -- with a printed denominator, and its own banner ("PLANE: DESIRED (Terraform). This does NOT read live AWS")
kept me from citing it as applied-plane evidence. The rail's denial text was itself useful: it named the
phantom-backstop class (a doc citing a Deny that was planned and never applied), which is exactly why CTO condition 2
reads the four round-2 Denies from the LIVE document rather than the repo.

**What failed:** nothing returned a wrong answer. One usability note: `comp-find` on a plain uppercase phrase
exceeded the 120 s foreground limit and had to run backgrounded. It completed correctly, so this is latency rather
than a defect -- but an ownership check that cannot answer inline is one a seat under time pressure will skip, and
skipping it is how an owned class gets re-filed. Worth a `--fast`/name-only mode if the tool's owner agrees.

**Gap found:** no comp-tool exposes an IAM **managed policy's** default-version id, its version list, or its document
bytes. `comp-iam` is Lambda/EC2-role shaped. Every never-widen half that binds on "the live default version equals the
repo bytes" therefore has to leave the rail, and that is the second project in a row where it has. A `comp-iam policy
<name>` verb returning the live default version id, the document, and a repo-equality verdict would put this class
back on the rail; raising it as a gap, not implementing it (CLAUDE.md build ladder, and it is not this cell's).

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Gate the bytes: `git diff --stat eda2919e6b HEAD` and `git status --porcelain` on the root | both EMPTY. **Positive control** beside the absence: the same pathspec against `eda2919e6b^` prints 5 files / 1636 insertions, so a clean-empty from a mangled pathspec is ruled out. `eda2919e6b` is an ancestor of origin CLOUD. |
| 1 | `tests/check_identity.py` | `IDENTITY-STATIC validate=ok no_access_key=True names_from_builder=7/7 policy_size_ok=True ok=True` |
| 1 | `tests/simulate_policy.py` | `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True` |
| 1 | `tests/render_passrole.py --check` | `PASSROLE-RENDER applied=0 named=0 wildcard=0 in_sync=True ok=True` |
| 1 | `tests/derive_protected_functions.py --check` | `PROTECTED-CENSUS functions=233 regions=17 refused_regions=0 protected=10 by_authorizer=1 by_edge=5 ruled_in=4 unruled=0 in_sync=True ok=True` |
| 2 | Live BEFORE read, saved as the rollback reference | deploy policy `DefaultVersionId v1`, the ONLY version, 8 statements; create policy ABSENT (`NoSuchEntity`, corroborated by a census of **42** customer-managed policies with the deploy policy as positive control); group carried 1 attachment |
| 3 | `terraform plan -input=false -no-color` UNTARGETED | `Plan: 2 to add, 1 to change, 0 to destroy.` Exactly **3** resource blocks (`grep -c`, denominator printed), the 3 named addresses, zero `must be replaced` / `will be destroyed` / `-/+` markers |
| 4 | NEVER-2 entry OPENED before the apply, 5 legs, blast radius + rollback-per-key named | `20261007T0811Z_nfra-ctlpln-dell-policy-r3-laptop-20261007`, committed `f381720cde` |
| 5 | `.tools/safe-apply.sh -chdir=... apply -input=false -no-color -auto-approve` (unscoped) | The apply's OWN plan read `2 to add, 1 to change, 0 to destroy`; **`Apply complete! Resources: 2 added, 1 changed, 0 destroyed.`** at ~08:15:50Z |
| 6 | AC1 group attachments | exactly `["cloudops-dell-agent-create-policy","cloudops-dell-agent-deploy-policy"]` |
| 6 | AC2 re-run | `allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True` |
| 6 | AC3 `plan -lock=false -detailed-exitcode` | `No changes. Your infrastructure matches the configuration.` `exit=0`, 12 resources refreshed |
| 6 | Live-vs-repo document equality, both policies | EQUAL=True both; **negative control** (one Sid mutated) reads False both, so an always-true comparator is ruled out |
| 6 | CTO condition 2: four round-2 Denies from the LIVE document | all PRESENT, `Effect=Deny`. Subtraction: 8 statements -> 11, exactly **+3** (the three round-3 Denies), so nothing was removed to make room |
| 6 | Live-principal simulation, `cloudops-dell1-agent-user` | block1 22/22 allowed, block3 5/5 denied, block4 8/8, api-key arms 3/3 |
| 6 | `comp-iam gaps`; entry CLOSED, sentinel removed | all 5 legs proven; committed `95b6e421cd` |

---

## Verification

```
Plan: 2 to add, 1 to change, 0 to destroy.
aws_iam_policy.dell_agent_create: Creation complete after 0s [id=arn:aws:iam::313476888478:policy/cloudops-dell-agent-create-policy]
aws_iam_group_policy_attachment.dell_agent_create: Creation complete after 0s [id=cloudops-dell-agents-group-20261007081550288100000001]
aws_iam_policy.dell_agent_deploy: Modifications complete after 0s [id=arn:aws:iam::313476888478:policy/cloudops-dell-agent-deploy-policy]
Apply complete! Resources: 2 added, 1 changed, 0 destroyed.

LIVE deploy policy v1 -> v2, 11 statements, in document order:
  Allow  S3ObjectsOnOpalBuckets / DeployServices / AgentbusSendToInboundQueues / ReadOnlyForTerraformPlan
  Deny   DenyEveryIamWrite  DenyPassRoleExceptNamed  DenyCloudTrailWrites
         DenyS3DeletesOnProductionData  DenyTableAndDatabaseDeletes  DenyApiKeyReads  DenyProtectedFunctions

V3-LIVE-PRINCIPAL block1_allowed_ok=22/22 block3_denied_ok=5/5 all_ok=True
BLOCK4-LIVE ok=8/8   (six protected-function arms explicitDeny; access-anomaly-scanner + a new
                      function name allowed -- the pair is what makes the deny meaningful)
ADMIN POSITIVE CONTROL, separate invocations: admin=allowed on both protected-function denies and
on apigateway:GET /apikeys/x  ->  those denies are the WORLD, not the instrument.
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Left the rail for two raw-`aws` IAM reads under `# rail-checked:` rather than substituting `comp-iam` | `comp-iam` models `(action)` per-Lambda on the DESIRED plane and returns no managed-policy version id or document. CTO condition 2 requires the four Denies read from the LIVE document, and the rollback key is "re-default the prior version" -- a wrong version id makes that rollback a second change. Substituting the available tool for the required instrument would have produced a confident wrong answer. |
| Ran blocks 2 and 4 of the simulation live, not only blocks 1 and 3 | The order says "first and third blocks"; the COO half's condition 2 says "repeats the four blocks". Where the two documents differ I carried the **wider** one, because the narrower reading would have left the act's own central refusal -- the ten access-deciding functions -- unexercised against the live principal. |
| Recorded block 3 arm 1's inverted expectation instead of smoothing it | `simulate_policy.py` expects `iam:PassRole` on the fixture role ALLOWED, but only under its rendered temporary copy. Live, the named-role list is empty, so every PassRole must be denied. Reporting 4/5 or silently re-labelling would both have been wrong; both halves already assert "no role can be passed, before or after". |
| Measured the prior version id (`v1`) rather than assuming it | The rollback depends on it. It was also the ONLY version, which is why the apply produced `v2` -- stated as measured, not predicted. |
| Did not push | `CLOUD` is a shared branch; `0.0.0_AB_MSTR` pushes it on Andrew's word. Push state reported as MEASURED (`ls-remote`), never defaulted. |
| Imported the arm lists from `simulate_policy.py` for the live run instead of retyping them | A transcription would have made V3 a different test than the one the halves cite. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/critical_paths/change_management/20261007T0811Z_nfra-ctlpln-dell-policy-r3-laptop-20261007_deploy_completion.md` | NEVER-2 entry opened, 5 legs closed with proof, entry CLOSED | Yes -- `f381720cde`, `95b6e421cd` |
| `org/critical_paths/.open_deploys/nfra-ctlpln-dell-policy-r3-laptop-20261007.json` | sentinel created then removed at close | Yes -- `f381720cde`, `95b6e421cd` |
| `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/BEFORE_*_20261007.json` (6) | live BEFORE state, the rollback reference | Yes -- `f381720cde` |
| `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/PLAN_nfra-ctlpln-identity_20261007.txt` | the gating plan | Yes -- `f381720cde` |
| `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/AFTER_*_document_*.json` (2) | live AFTER documents | Yes -- `95b6e421cd` |
| `org/tier2_senior/0.7.0_AE_CloudOps~E/deliverables/V3_*.txt`, `V3b_*.txt`, `COMP_IAM_GAPS_20261007.txt` | live-principal simulation + gaps evidence | Yes -- `95b6e421cd` |

**No file of the Terraform root was edited.** The order's bounds forbid it and `git status --porcelain` on the root
was empty before the apply and is unchanged by it.

---

## Blockers

**None.** Nothing is owed by this seat on this order. The `<status>` flip on the task order is the issuer's act, not
this seat's, and is deliberately left alone.

---

## Current State

NFRA_CTLPLN round 3's Dell policy is LIVE in account 313476888478, applied from the laptop at ~08:15:50Z by
`.tools/safe-apply.sh` on `infra/aws/terraform/nfra-ctlpln-identity/` at commit `df38747760` (root bytes identical to
`eda2919e6b`): managed policy `cloudops-dell-agent-create-policy` minted at `v1` and attached to
`cloudops-dell-agents-group`, and `cloudops-dell-agent-deploy-policy` moved `v1 -> v2` carrying
`DenyPassRoleExceptNamed`, `DenyProtectedFunctions` and `DenyApiKeyReads` on top of its four round-2 Denies. Both live
documents equal their repo JSON under a negative-controlled comparator, a re-plan is 0-diff (`exit=0`), and the live
principal `cloudops-dell1-agent-user` reads 22/22 allowed, 5/5 PassRole denied and 8/8 on the protected-function pair
with an admin control proving those denies are the policy. The NEVER-2 entry is CLOSED with all 5 legs proven and
nothing stranded. **The act's one unmeasured question is answered: the laptop's identity
(`arn:aws:iam::313476888478:user/Andrew_Berman`) DOES hold IAM write on these three objects** -- so the CTO's
"box question returns to this seat" branch never fired. Rollback stays available and measured: deploy-policy `v1` is
retained for a re-default, and removing the two new resources returns the Dells to the deploy policy alone; neither
undoes anything a Dell creates under the grant. Both commits are LOCAL at origin CLOUD `4cea56993a`.

**The live round trip was NOT exercised and is not claimed.** No Dell identity acted and no resource was created --
the order's bounds forbid both, and that is a later act by another route.

---

## Next Steps

1. **[`2.0.0_SA_COO~C`] Flip `<status>` on `NFRA_CTLPLN.TO-APPLY-3`** -- the report landed (msg delivered to
   `2.0.0_SA_COO/~C`, 1284 bytes, already drained to its `read/`). The flip is the issuer's, never the assignee's.
2. **[`0.0.0_AB_MSTR`] Push CLOUD on Andrew's word** -- `f381720cde` and `95b6e421cd` are LOCAL; origin reads
   `4cea56993a`. Not this seat's act.
3. **[NO ACTION -- the startup audit-archive finding is an ALREADY-OWNED class; deliberately NOT re-filed.]**
   `python .tools/audit-archive-invoker.py` returned `rc=1` with **four** `INTEGRITY/NON-APPEND-EDIT` findings against
   `org/mass-deletion-audit.log`, `org/safe-deploy-bypass-audit.log`, `org/mcp/agent-spawn-audit.log` and
   `org/law-edit-audit.log`, in every case live-head **SMALLER** than the 06:02Z baseline (spawn-audit 6161037B ->
   6003052B, first divergence line 12991). I did not halt to investigate (CLAUDE.md section 2) and I ran the
   ownership read before deciding whether to file anything. **It is owned, and the findings are expected:**
   `.tools/audit-archive-invoker.py:404` carries the DEVICE-CHAIN GUARD under **CTO ruling `@4484d55608`
   (2026-08-20), the INTERIM half of the device-axis fix** -- "the shared tracked `.baseline` pins UNTRACKED
   device-local subjects, so a mint on either device manufactures ~18 false findings on the other (measured both
   directions, MSTR Msg 63017)", and "DETECTION IS DELIBERATELY UNTOUCHED ... findings all still run against the
   legacy chain" until the per-device `archive/<device>/` migration lands. Four shrinks at once against a shared
   baseline is that signature exactly, and `4fa3178718` merged a dell2 candidate into laptop CLOUD this morning.
   Corroborating prior disposition: `3.0.0_SA_CVO` logs of 2026-09-03 record "19 findings, 18 device-axis (every
   NON-APPEND-EDIT a shrink)". **So per XXX.md A.2 this is an owned class and I did NOT file a surprise row or a
   finding** -- re-filing it would have added noise to a question already ruled.
   One thing worth stating rather than assuming: these four **survived** the invoker's CRLF normalisation
   (`:185-205`, which exists precisely to discriminate a benign `core.autocrlf` checkout artifact from a real edit),
   so they are real content divergence on the device axis, not line-ending noise. That is consistent with the ruled
   class and is not a separate finding. The residual exposure is named in the ruling itself, not by me: while the
   migration is pending, a genuine tamper on one of these four logs would arrive wearing the same shape as the
   device-axis false finding, and an audit log is the instrument an override is read from. The owner of that
   migration is the CTO by its own ruling.
4. **[`1.0.0_SA_CTO` / `2.0.0_SA_COO~C`, informational] The first Dell deploy of one of the ten protected functions
   will be refused** -- the five edge functions (`auth-validator-edge`, `cache-control-injector`,
   `public-data-router`, `shared-advisor-router`, `shared-advisor-router-response`) are ones the investor-reporting and
   portal work can touch. That refusal is the intended behaviour, now live and verified; the CTO half already names
   narrowing the edge five as a candidate cell on a row from whichever seat hits it.
