# Deploy Completion Record
**Date opened:** 2026-08-28T18:40:39.004290+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260828T185149Z
**Deploy:** ADVI_INSURE.TO-A4-AEC: INSURE as the 49F session chain's THIRD runner target -- session-trigger payload map + env var, ONE invoke-policy ARN, EventBridge bd-49f-insurance-session-daily cron(35 4) UTC
**Authored by:** 0.7.0_AE_CloudOps~K
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD commits a57461f191 (acts a+b) + f526a00753 (CVO P2 fixes) | commit hashes + measured push state | a57461f191 (acts a+b) ON ORIGIN via merge-base --is-ancestor against origin/CLOUD a57461f191; f526a00753 (CVO cert P2-i data-lookup + P2-ii both-planes stagger correction) LOCAL. git ls-remote origin refs/heads/CLOUD = a57461f1914ac36e4a9594ca8e2bac66dc096669 measured 18:49:19Z. Integrator-only branch, no push sought. | CLOSED 20260828T185106Z |
| L2 | activation | safe-apply of the SAVED -target'd plan file after 1.0.0_SA_CTO GO 78677 | apply counts == plan counts 3 add / 2 change / 0 destroy, from the apply's OWN line | safe-apply of the SAVED plan FILE (never a re-plan) after 1.0.0_SA_CTO GO 78677; HALT-GATE surfaced 5 pending base-serial messages, all reviewed, none STOP-class and none touching bd-pipeline, then HALT_ACK=1. Apply's OWN line: 'Apply complete! Resources: 3 added, 2 changed, 0 destroyed.' == plan 'Plan: 3 to add, 2 to change, 0 to destroy.' EXACTLY. Created: event rule bd-49f-insurance-session-daily, its target, its lambda permission. Changed: the session-trigger policy, the session-trigger function. | CLOSED 20260828T185106Z |
| L3 | verify | 0-diff on-target re-plan | plan reports No changes | On-target re-plan: 'No changes. Your infrastructure matches the configuration.' AND the UNTARGETED plan over the whole bd-pipeline root is ALSO 'No changes' -- so no foreign change is pending in this root (1.0.0_SA_CTO 78677 item 2 discharged) and the -target'd apply left the root fully converged. | CLOSED 20260828T185106Z |
| L4 | verify | live IAM three arms, SEPARATE invocations, ONE --resource-arns each | session-trigger role allowed on reporting-pull ARN; same role still allowed on bd-49f-runner (positive control); unrelated role implicitDeny on reporting-pull (fence real) | FIVE arms, each a SEPARATE invocation with ONE --resource-arns (the 2+-ARN false-deny trap avoided). bd-49f-session-trigger-role lambda:InvokeFunction -> opal-assets-bd49f-reporting-pull = allowed; -> bd-49f-runner = allowed (positive control, nothing lost); -> bd-49f-fees-runner = allowed (nothing lost); -> advi-49f-gold-dispatch = implicitDeny (RESOURCE-axis fence, TO form); bd-49f-keepalive-role -> opal-assets-bd49f-reporting-pull = implicitDeny (PRINCIPAL-axis fence, CTO 78677 form). Action-name trap self-discriminated: a nonexistent action can never return allowed, so the three allowed arms prove lambda:InvokeFunction is real. comp-iam gaps re-run: 14 action-plane findings estate-wide, ZERO naming bd-49f-session-trigger or opal-assets-bd49f-reporting-pull (grep count 0); NECESSARY-NOT-SUFFICIENT and stated as such -- comp-iam models (action) not (action,resource) and reports this very call as UNRESOLVABLE-RESOURCE at lambda_function.py:211, so it structurally cannot confirm or falsify this grant. The live simulate arms are the load-bearing evidence. | CLOSED 20260828T185149Z |
| L5 | verify | live read-backs of the new rule + target + env + code | describe-rule ENABLED cron(35 4); list-targets-by-rule input JSON; get-function-configuration env var + CodeSha256 matching the built artifact via the source map | aws events describe-rule bd-49f-insurance-session-daily: ScheduleExpression cron(35 4 * * ? *), State ENABLED. aws events list-targets-by-rule: one target Id=Bd49fInsuranceSessionTrigger, Arn=...:function:bd-49f-session-trigger, Input={"mode":"session-refresh","runner":"insurance"}. aws lambda get-function-configuration bd-49f-session-trigger: INSURANCE_RUNNER_FUNCTION_NAME=opal-assets-bd49f-reporting-pull present with all 7 prior env vars intact (8 total), LastModified 2026-08-28T18:43:27.000+0000, CodeSha256 YZ3FHmwtWwag53zlm6XwbyNq8331A0TZpygqatswIJs= which is BYTE-IDENTICAL to the sha256 build-and-upload printed for the artifact it uploaded (7104 B, write VERIFIED) -- deployed bytes == build input, resolved through the source map, never by filename (Rule 22a CODE layer). | CLOSED 20260828T185149Z |

## Log

- 20260828T184039Z OPENED by 0.7.0_AE_CloudOps~K with 5 leg(s)
- 20260828T185106Z LEG L1 closed: a57461f191 (acts a+b) ON ORIGIN via merge-base --is-ancestor against origin/CLOUD a57461f191; f526a00753 (CVO cert P2-i 
- 20260828T185106Z LEG L2 closed: safe-apply of the SAVED plan FILE (never a re-plan) after 1.0.0_SA_CTO GO 78677; HALT-GATE surfaced 5 pending base-seria
- 20260828T185106Z LEG L3 closed: On-target re-plan: 'No changes. Your infrastructure matches the configuration.' AND the UNTARGETED plan over the whole b
- 20260828T185149Z LEG L4 closed: FIVE arms, each a SEPARATE invocation with ONE --resource-arns (the 2+-ARN false-deny trap avoided). bd-49f-session-trig
- 20260828T185149Z LEG L5 closed: aws events describe-rule bd-49f-insurance-session-daily: ScheduleExpression cron(35 4 * * ? *), State ENABLED. aws event
- 20260828T185149Z CLOSED -- all 5 legs proven

---

## Addendum 2026-08-28T19:33Z (post-close, 0.7.0_AE_CloudOps~K) -- ordered by 1.0.0_SA_CTO 78840/78857 and 2.0.0_SA_COO 78860 item 3; interim control on record-terraform-deploy.sh's half-write class, run retroactively

**The CLOSED 5/5 verdict above is UNCHANGED by this addendum.** This is an append, never an edit
to L1's proof string: `deploy_ledger.py` has no amend-a-closed-leg verb, and a silently amended
audit record is a worse object than a disclosed gap -- but a MARKED addendum is better than both,
because the ledger is where the next reader looks and a disclosure that lives only in a broker
message scrolls.

**WHY THIS EXISTS.** After this ledger CLOSED at 18:51:49Z, the Rule-6 tag step surfaced that
`record-terraform-deploy.sh` had committed `17db393744` titled "ci: record deploy bd-pipeline @
689e1b31" while its own source-map write had SILENTLY NO-OPPED. Precisely, per 2.0.0_SA_COO 78860 (i):
the commit carried `artifact_sha256` -- but that line was ALREADY IN THE TREE from
`build-and-upload.sh` and was merely swept into the commit -- while the two fields the tool
itself writes, `last_deployed_commit` and `last_deployed_at`, DID NOT MOVE. So the sha moving
is not evidence the tool ran: it is the artifact of a different tool that did. Cause confirmed by exercise, not
inferred: `:182` selects `JSON_TOOL` by testing an absolute path first, so the bun/JS branch runs;
inside it `deriveContentCommit` shells `git -C "/cygdrive/c/..."`, which a native Windows binary
cannot resolve. Run directly under bun it THROWS -- `Command failed: git -C "/cygdrive/c/Users/
AndrewBerman/Desktop/ajb_workspace" log -1 ...`. The MSYS-argv-into-a-native-caller class; bun is a
third caller shape after Python and PowerShell. Disarm owner `0.8.0_AE_CloudComp` (1.0.0_SA_CTO
78840); obligations row 7 item (l). DISARMED != REMEDIATED.

**L1's PROOF STRING IS SILENT ON THIS**, and deliberately left so. L1 closed at 18:51:06Z; the
half-write was found afterwards, so the correction did not exist when L1 was proven. The
correction was committed at `19c0f0c53b` under this seat's author line.

**THE INTERIM CONTROL, RUN RETROACTIVELY (1.0.0_SA_CTO 78840): all THREE fields must have moved.**

| field | before | after | verdict |
|---|---|---|---|
| `artifact_sha256` | `EOOuJMrkSkfj5Tl9dYHFnFbh8c/5jAgShS/V6NCy+N4=` | `YZ3FHmwtWwag53zlm6XwbyNq8331A0TZpygqatswIJs=` | MOVED |
| `last_deployed_commit` | `f29c778648c8f7bb53682d897d57de680e7db250` | `a57461f1914ac36e4a9594ca8e2bac66dc096669` | MOVED |
| `last_deployed_at` | `2026-07-06T18:56:46Z` | `2026-08-28T18:43:27Z` | MOVED |

**THREE-FIELD VERDICT: ALL THREE MOVED.**

**TWO CORROBORATIONS, because the three-field test is a MOVEMENT test and movement to a WRONG
value would pass it:**

- **CONTENT** -- `git log -1 --format=%H -- infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py`
  returns `a57461f1914ac36e4a9594ca8e2bac66dc096669`, i.e. the recorded commit is the last one
  actually touching the built source, right BY CONTENT and not merely different from the stale
  value. (This check is 3.0.0_SA_CVO's, from 78826, re-run at this seat.)
- **LIVE** -- `aws lambda get-function-configuration --function-name bd-49f-session-trigger`
  returns `CodeSha256 = YZ3FHmwtWwag53zlm6XwbyNq8331A0TZpygqatswIJs=`, byte-identical to the map's
  `artifact_sha256`. So the Rule-22a build-input compare that a half-written record endangers now
  resolves correctly for this function.

**SCOPE OF THE HAND-CORRECTION:** ONE function entry. The payload was built and 201 other function
entries were compared field-by-field BEFORE the file was opened for write; 0 moved. Resulting diff
2 insertions / 2 deletions.

**FORWARD:** any further `record-terraform-deploy.sh` run at this seat runs the three-field check
inline and records its result in L1 at close time, so the gap disclosed here is a one-off bounded
by the interim control's own start date.

**3.0.0_SA_CVO reads this addendum as part of the (e') fire's evidence bundle, not as a reopen**
(1.0.0_SA_CTO 78857).
