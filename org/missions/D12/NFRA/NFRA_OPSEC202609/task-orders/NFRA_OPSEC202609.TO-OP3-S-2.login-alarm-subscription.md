# TO NFRA_OPSEC202609.TO-OP3-S-2 -- FWD-4: THE TWO LOGIN-ABUSE ALARMS CURRENTLY FIRE INTO NOTHING. Attach the recipient C-20 names, confirm it, and observe one transition END TO END (OP3-s-2, FWD-4)

<to_id>NFRA_OPSEC202609.TO-OP3-S-2</to_id>
<project>NFRA_OPSEC202609</project>
<issued_to>0.9.0_WK_NFRA_OPSEC202609~2</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged</status>

**Directive:** D12 · **Fabric:** site-z · **PRD:** `../prd/NFRA_OPSEC202609_PRD.md` **v0.14** (FWD-4; **C-20 FWD-4-RECIPIENT**) · **Decomp cell:** `OP3-s-2` (round-3 rectangle v0.3.0) · **Round:** 3.

---

## THE CELL

Row **`NFRA_OPSEC202609-Z-S151`** (GRADUATED at L9, hazard ARMED): *"FWD-4 IS GRADED COMPLETE AND CANNOT BE SATISFIED: both login-abuse alarms publish to an SNS topic WITH ZERO SUBSCRIBERS."*

The alarms exist and are correct. **They fire into a void.** The subscription is the single open leg, and until it is closed FWD-4's DONE WHEN cannot be met no matter how well the alarms are tuned.

⭐ **THE RECIPIENT IS SETTLED AND IS NOT YOURS TO CHOOSE.** Row `Z-S97` recorded FWD-4's recipient as an input this project did not hold. **PRD v0.14 `C-20 FWD-4-RECIPIENT` settles it: FWD-4's "named person" is `andrew@opalinvest.com`.** ⛔ **DO NOT guess, DO NOT default, DO NOT use a role address, DO NOT add a second recipient.**

## THE MORATORIUM IS NOT BREACHED, AND HERE IS WHY IN FULL

CLAUDE.md carries a standing bar: **never build an alert / alarm / SNS-send / notification / monitor unless Andrew explicitly asks.** It binds hard and it is not waived here.

**FWD-4 is one of the SIX NAMED EXCEPTIONS** (FWD-4/5/6/12 by commissioning word; FWD-14/15 Andrew-direct 2026-09-02). **AND THIS CELL BUILDS NOTHING NEW:** the two alarms exist, the topic exists, and the act is attaching the recipient C-20 already names so an authorised alarm stops firing into nothing.

⛔ **NOTHING BEYOND THAT.** No second recipient. No new topic. No new alarm. No new channel or cadence. **C-6's digest email remains NOT AUTHORISED and is not to be built, proposed or prepared here.** If you find yourself adding a notification this order does not name, stop and file a row.

## DELIVERABLE

1. **The subscription**, `andrew@opalinvest.com` on the topic the two alarms already publish to. Do not create a topic.
2. **CONFIRMATION**, not merely creation -- an unconfirmed email subscription is `PendingConfirmation` and delivers nothing, which is the same "attached but not reachable" shape that cost this project row `Z-S83`.
3. **One observed transition end to end**, from alarm state change to the message arriving.
4. **The proof-of-spec instance**, VALID before the `complete` flip.

## ACCEPTANCE -- criterion ids minted at cut, ONE CLAUSE EACH

<criterion id="S2-AC1" cell_refs="OP3-s-2"><invocation>`aws cloudwatch describe-alarms` filtered to the two login-abuse alarms, with their `AlarmActions` pasted.</invocation><expect>both alarms' `AlarmActions` resolve to the SAME topic ARN, and that ARN is the one acted on below.</expect></criterion> `S2-AC1` -- BOTH ALARMS' TOPIC IS IDENTIFIED FROM THE ALARMS THEMSELVES, NOT ASSUMED.

<criterion id="S2-AC2" cell_refs="OP3-s-2"><invocation>`aws sns list-subscriptions-by-topic --topic-arn <that ARN>` run BEFORE the change, output pasted.</invocation><expect>the subscription list is empty, confirming `Z-S151` on the applied plane before it is altered.</expect></criterion> `S2-AC2` -- THE ZERO-SUBSCRIBER BEFORE-STATE IS CAPTURED.

<criterion id="S2-AC3" cell_refs="OP3-s-2"><invocation>`aws sns list-subscriptions-by-topic --topic-arn <that ARN>` run AFTER, output pasted.</invocation><expect>exactly ONE subscription, protocol `email`, endpoint `andrew@opalinvest.com`.</expect></criterion> `S2-AC3` -- THE SUBSCRIBER IS EXACTLY THE ONE C-20 NAMES.

<criterion id="S2-AC4" cell_refs="OP3-s-2"><invocation>the same listing, reading the `SubscriptionArn` field.</invocation><expect>`SubscriptionArn` is a real ARN and NOT the literal string `PendingConfirmation`.</expect></criterion> `S2-AC4` -- THE SUBSCRIPTION IS CONFIRMED, NOT MERELY CREATED.

<criterion id="S2-AC5" cell_refs="OP3-s-2"><invocation>an alarm state transition (a self-targeted `set-alarm-state` is acceptable and is the safe form), with the alarm history entry pasted.</invocation><expect>the history shows the transition AND the notification action firing to that topic.</expect></criterion> `S2-AC5` -- ONE TRANSITION IS OBSERVED END TO END.

<criterion id="S2-AC6" cell_refs="OP3-s-2"><invocation>`aws cloudwatch describe-alarms` for the two alarms after, compared to `S2-AC1`'s output.</invocation><expect>thresholds, periods, metrics and actions are byte-identical to before; the only estate change is the added subscription.</expect></criterion> `S2-AC6` -- NOTHING ELSE MOVED.

<expected_criteria>S2-AC1, S2-AC2, S2-AC3, S2-AC4, S2-AC5, S2-AC6</expected_criteria>

<paths>
org/missions/D12/NFRA/NFRA_OPSEC202609/task-orders/NFRA_OPSEC202609.TO-OP3-S-2.login-alarm-subscription.md
org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~2/
org/missions/D12/NFRA/NFRA_OPSEC202609/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D12/NFRA/NFRA_OPSEC202609/prd/NFRA_OPSEC202609_PRD.md
org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/NFRA/NFRA_OPSEC202609/decompositions/NFRA_OPSEC202609_DECOMP_round3.md</decomp_doc> (v0.3.0), cell `OP3-s-2`.
<owned_cells>OP3-s-2</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN -- G-15 (the alert/monitor moratorium) BINDS and is SATISFIED by FWD-4 being one of the six named exceptions; this cell adds a subscriber to an existing authorised alarm topic and builds nothing new.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM identity policy is authored; an SNS subscription is not a principal.
comp-adversary: RUN -- the topic ARN is NOT given in this face on purpose -- `S2-AC1` derives it from the alarms themselves, because an ARN asserted by the issuer is exactly the shape that produced C-16's wrong state on this project.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `S2-AC1` .. `S2-AC6`. The worker fills a `PROOF_OF_SPEC.schema.json` instance at `org/missions/D12/NFRA/NFRA_OPSEC202609/deliverables/0.9.0_WK_NFRA_OPSEC202609~2/NFRA_OPSEC202609.TO-OP3-S-2.login-alarm-subscription.proof_of_spec.json` and validates it with `.tools/proof-of-spec-check.py <instance> "S2-AC1,S2-AC2,S2-AC3,S2-AC4,S2-AC5,S2-AC6"` BEFORE the `complete` flip. ⭐ **THE CONTROL THAT MUST BE ABLE TO FAIL IS `S2-AC4`** -- a created-but-unconfirmed subscription reads as success everywhere except delivery, and it is the ATTACHED-vs-REACHABLE distinction this project has already paid for once. Every `surprises` entry opens with a row id that resolves in the project's channel.
</proof_of_spec>

<compiler_tools_mandate>
  <phase id="1" when="before any write">Confirm the worktree: `test -d org && test -d .tools`. Then derive the topic ARN from the alarms and capture the zero-subscriber before-state. A topic that already has a subscriber is a difference from `Z-S151` -- STOP and file a row rather than proceeding.</phase>
  <phase id="2" when="the act">Subscribe, then confirm. Creation is not the deliverable.</phase>
  <phase id="3" when="after">The transition observation, the unchanged-alarms re-read, then the proof instance.</phase>
</compiler_tools_mandate>

⛔ **RUN EVERY COMP-TOOL BY ITS EXPLICIT `.tools/` PATH, NEVER THE BARE NAME** (LIMIT 4 / 4a: the bare name is a shim pinned to the MAIN checkout and censuses the wrong tree from a worktree).
