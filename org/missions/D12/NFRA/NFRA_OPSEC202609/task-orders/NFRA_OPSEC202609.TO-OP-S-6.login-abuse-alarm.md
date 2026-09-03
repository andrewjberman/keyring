# TO NFRA_OPSEC202609.TO-OP-S-6 -- THE LOGIN-ABUSE ALARM, AND IT IS THE PROJECT'S ONLY AUTHORISED NOTIFICATION: two alarms on the auth path reaching ONE NAMED PERSON, fired on a STAGED burst and READ by that person, because FWD-4's DONE WHEN is a human receiving it and not an alarm existing (OP-s-6, C-6)

<to_id>NFRA_OPSEC202609.TO-OP-S-6</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.7.0_AE_CloudOps~S</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-03</issued_date>
<status>staged</status>

**Directive:** D12 - **Fabric:** site-z - **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.12 @3619ebecd9** (ENDPOINT **FWD-4**; s.5 the exercise bars; C-6) - **Decomp cell:** `OP-s-6` (v0.1.10 @2fd3843047, s.1a) - **Lane:** `infra/aws/terraform/portal-auth/cloudwatch-alarms.tf`, AE lane - **Round:** 3 of NFRA_OPSEC202609. **Dispatch:** GO after `TO-OP-S-4-18` goes terminal -- one task order at a time.

---

## ⛔ THE MORATORIUM, AND EXACTLY HOW FAR THIS EXCEPTION REACHES

CLAUDE.md carries a standing veto: **never build an alert, alarm, SNS topic, SES send, notification, freshness-checker or monitor unless Andrew explicitly asks.** **He did, once, for this: FWD-4 is a commissioned endpoint outcome he confirmed at L2, and the decomposition records the exception as `moratorium exception FWD-4 ONLY`.**

>> **THE EXCEPTION IS THE TWO ALARMS IN DELIVERABLE 1 AND NOTHING ELSE.** No dashboard. No cadence or digest. No second recipient. No GuardDuty, Security Hub or Config (PRD s.5 names all three as NOT authorized). No "while we are here" alarm on a neighbouring metric. **If you find yourself adding a third alarm, you have left the exception** -- that is a ROW and a question, never a judgement call. <<

## READ LIVE AT THIS CUT BY THE ISSUER (2026-09-03 19:2xZ; re-ground in phase 1 and STOP on any difference)

- **`describe-alarms` returns 49 alarms in this account.** Reading the names: five `FIRMSEP-*` (firm separation), two Lambda-throttle, plus pipeline, CloudFront and orchestrator alarms. **NONE is on the authentication path.** That is the gap `OP-s-6` closes and the 49 is your before-denominator.
- **`list-metrics --namespace AWS/WAFV2` returns 364 metrics**, so the WAF metric plane is live and emitting -- the `AuthLoginRateLimit` rule exists on `opal-cloudfront-protection` at priority 2 with action `Block` (read live at this cut).
- **The carrier is tracked:** `git ls-files` resolves `infra/aws/terraform/portal-auth/cloudwatch-alarms.tf`.

## DELIVERABLE

1. **TWO ALARMS, DECLARED IN TERRAFORM in the carrier above, never by console:**
   - **(a)** on the WAF rule `AuthLoginRateLimit`'s **`BlockedRequests > 0`** -- the rule already exists and already blocks; this alarm is what makes a block reach a person.
   - **(b)** a **metric filter on `auth_throttled`** in the auth handler's log group, with an alarm on its metric. **Read the log group name live and name it in the proof** -- do not assume it from the function name.
2. **ONE NAMED RECIPIENT, AND THE NAME IS AN INPUT YOU DO NOT INVENT.** C-6 says one email per event to ONE named person. **This face does NOT name that person, because the issuer does not have the name.** ⛔ **DO NOT PICK ONE, DO NOT USE A ROLE ADDRESS, DO NOT USE ANDREW'S ADDRESS BY DEFAULT.** File a ROW naming the gap and send the issuer a message asking for the recipient, then **build everything else and leave the subscription as the single open leg.** A notification wired to a guessed address is worse than no notification: it reads as delivered and reaches nobody.
3. **THE DELIVERY PATH:** one SNS topic for these two alarms, subscription to the named address once you have it. **No other subscriber, no fan-out, no Lambda in the path.**
4. **THE STAGED BURST, under the `OP-x-1` probe verdict:** exercise the alarm with a deliberate burst against the login path so the rule blocks and the alarm transitions to `ALARM`. **This is the probe the verdict authorises and it stays inside the verdict's bounds: read-only elsewhere, and the burst is against the fixture identity, never a real partner human's session.** Capture the alarm's `StateTransitionedTimestamp` and the state history entry.
5. **A deploy-ledger entry** (`safe-apply`, never bare), opened before and closed after, with the module's UNSCOPED baseline quoted BEFORE the first edit and the rollback named.
6. **The proof-of-spec instance** at `../deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-6.login-abuse-alarm.proof_of_spec.json`, VALID with the expected ids BEFORE the complete flip.

## ACCEPTANCE -- criterion ids minted at cut

<criterion id="S6-AC1" cell_refs="OP-s-6"/> `S6-AC1` -- TWO ALARMS EXIST ON THE AUTH PATH AND THE COUNT MOVED: `describe-alarms` after, with the two new alarm names quoted and their `MetricName`, `Namespace`, `Threshold`, `ComparisonOperator` and `AlarmActions` pasted; the alarm count read against the **49** quoted in this face as the before. Both addresses appear in `terraform state list`. **A console-created alarm is a FAIL even if it works.**
<criterion id="S6-AC2" cell_refs="OP-s-6"/> `S6-AC2` -- THE ALARM FIRED ON A STAGED BURST, MEASURED ON THE ALARM AND NOT ON THE RULE: after the burst, `describe-alarm-history` shows a transition to `ALARM` with its timestamp, and the WAF rule's `BlockedRequests` datapoint for the same window is pasted beside it. **A blocked request is NOT the criterion; the alarm transitioning is.** NEGATIVE CONTROL: state the alarm's state BEFORE the burst, so the transition is a change and not a standing condition.
<criterion id="S6-AC3" cell_refs="OP-s-6"/> `S6-AC3` -- THE NAMED PERSON RECEIVED IT, OR THIS FILES UNCOMPUTABLE WITH THE REASON: FWD-4's DONE WHEN is that a human is reached, so the criterion is an agent-side confirmation that the message ARRIVED at the named address -- not that SNS accepted it, which is the `SENT != EMITTED != READ` trap. **If the recipient is still unnamed, this files `UNCOMPUTABLE-BY-CONSTRUCTION` citing the row from deliverable 2, and the flip waits on nothing else.** Do not substitute a self-addressed test.
<criterion id="S6-AC4" cell_refs="OP-s-6"/> `S6-AC4` -- THE MORATORIUM HELD, CENSUSED WITH ITS DENOMINATOR: a census of everything this task order created -- alarms, topics, subscriptions, metric filters, dashboards -- with the count of each, showing **exactly 2 alarms, exactly 1 topic, 0 dashboards, 0 additional subscribers, and 0 GuardDuty / Security Hub / Config resources.** The control that must be able to fail: run the same census against the whole account's dashboards and confirm the number did not change.
<criterion id="S6-AC5" cell_refs="OP-s-6"/> `S6-AC5` -- BASELINE QUOTED, 0-DIFF AFTER, NOTHING ELSE RODE: the module's UNSCOPED plan quoted BEFORE the first edit; the apply's changed-resource list enumerated with its count, containing ONLY the alarms, the topic, the subscription and the metric filter; the UNSCOPED re-plan 0-diff after; the ledger CLOSED with its proof and rollback; push state read by `ls-remote` + `is-ancestor` and stated as MEASURED.

<expected_criteria>S6-AC1, S6-AC2, S6-AC3, S6-AC4, S6-AC5</expected_criteria>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP.md</decomp_doc> @2fd3843047 (v0.1.10), cell `OP-s-6` (manifest S6; FWD-4; value EXERCISED).
<owned_cells>OP-s-6</owned_cells>
Read-dependencies, NOT claimed: `OP-s-5` (COMPLETE -- its logging is what the metric filter reads), `OP-x-1` (the probe verdict authorising the staged burst).
</decomp_ref>

<preflight>
comp-schedule: RUN 2026-09-03 19:1xZ -- GATES ARMED 21 over 5 carriers (C1 SENTINEL 21 -> 5; C2 DEPLOY-LEDGER 4 -> 4; C3 MORATORIA 12 -> 12; C4 SCOPE-GUARD 20 -> 0; C5 PROJECT-BLOCKING 336 -> 0). **The MORATORIA carrier's 12 gates are the ones that bind this face and they are meant to.** This is the ONLY task order in this project that carries a moratorium exception; it is FWD-4 ONLY, it is bounded in the section above, and the assignee re-reads those gates in phase 1 rather than taking this sentence for them.
comp-iam: DECLARED-NOT-APPLICABLE -- this face creates no role and attaches no policy. The SNS publish permission for CloudWatch alarms is a resource policy on the topic, verified on the APPLIED plane by S6-AC2's actual transition and S6-AC3's actual arrival rather than by a DESIRED-plane lens.
comp-adversary: DECLARED-NOT-APPLICABLE -- this face pins no commit-scoped claim; every factual claim in it is a LIVE AWS read taken at the cut and timestamped (49 alarms, 364 WAFV2 metrics, the rule at priority 2), which the assignee re-takes in phase 1 and STOPS on any difference.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S6-AC1`, `S6-AC2`, `S6-AC3`, `S6-AC4`, `S6-AC5`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.7.0_AE_CloudOps~S/NFRA_OPSEC202609.TO-OP-S-6.login-abuse-alarm.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S6-AC1,S6-AC2,S6-AC3,S6-AC4,S6-AC5"` BEFORE the complete flip. **The controls that must be able to FAIL: `S6-AC2`'s pre-burst alarm state, `S6-AC4`'s account-wide dashboard census, and `S6-AC5`'s unscoped re-plan.** Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before write">Re-ground the alarm census, the WAF rule's presence and the auth handler's ACTUAL log group name. Re-read the MORATORIA gates rather than trusting this face's summary of them.</phase>
  <phase id="2" when="before the apply">A broker drain, the unscoped baseline plan, the ledger entry opened.</phase>
  <phase id="3" when="after the apply">The unscoped re-plan, the alarm read on the APPLIED plane, and the ledger closed on the artifact rather than on the apply's rc.</phase>
</compiler_tools_mandate>
