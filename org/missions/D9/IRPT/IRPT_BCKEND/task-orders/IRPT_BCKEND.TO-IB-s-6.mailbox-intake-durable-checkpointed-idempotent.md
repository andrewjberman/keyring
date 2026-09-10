# TO IRPT_BCKEND.TO-IB-s-6 -- MAILBOX INTAKE: Graph delta polling, attachments and receipt persisted before the checkpoint advances, restart recovery, one request per forward, the scheduler applied DISABLED

<to_id>IRPT_BCKEND.TO-IB-s-6</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~3</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~3; becomes pending when the COO hands it over after IB-s-8 is terminal and merged AND IB-s-5 (slot ~1) is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-6` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-9 (own) | **PRD candidate:** B6

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~3;`.
- **Worktree:** `/c/tmp/wk-irpt-1-3` on branch `wk-irpt_bckend-1-3`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-3/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~3 <0.9.0_WK_IRPT_BCKEND~3@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** second in slot ~3, after IB-s-8; cross-slot wait on IB-s-5's merge (the gate and the policy this cell binds through).

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B6 mailbox intake: Graph delta, attachments, checkpoint, lease, outbox, idempotency
- **serves:** FWD-9 (own)
- **brief sections consumed:** O3; IV.4 mailbox paragraph
- **contracts (P=produces, C=consumes):** P `AnalysisRequest` (original-message/attachment refs, sender evidence)
- **paths: reuse:** NONE VERIFIED -- the brief names no existing Graph/certificate mailbox implementation; the reuse source is UNRESOLVED until one is inspected (`ycharts-session-capture/index.mjs` is browser login and cookie capture and establishes no mail permission -- it belongs to B8)
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (intake handler); scheduler `cron(0/15 8-23 * * ? *)` America/New_York -- the brief's proposal, measured then declared
- **fixtures / evidence:** real forwarded-message/holdings specimens (STILL MISSING -- proof gap); mailbox `requests@opalinvest.com` forwarding into `opalbloomberg@opalinvest.com`
- **acceptance clause draft:** attachment + receipt persisted BEFORE the checkpoint advances; restart mid-attachment recovers; repeated forward = one request; new request with identical holdings = a new request; Retry-After and delta resync defined; original sender verified through the forwarding arrangement, not display From; the effective Mail.Read grant is restricted to that one mailbox and VERIFIED, never assumed from a filter; folder delta with `nextLink` pagination and a durable `deltaLink`; immutable message ids; initial cutoff, overnight catch-up, delta expiry/resync and Retry-After all defined; original MIME retained where needed to recover forwarded structure

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Reuse source UNRESOLVED (PRD v0.3), one inspect candidate (row `IRPT_BCKEND-S3`):** at Phase 1 read `infra/aws/ec2/opal-gateway/app/config.py` and the gateway's auth module for the Graph permission model it uses (app registration? certificate? delegated?), whether a grant restricted to `opalbloomberg@opalinvest.com` exists, and record it in `ib_s_6_graph_inspection.md`. The effective `Mail.Read` grant for the intake is VERIFIED by a read of the app registration's granted permissions or recorded UNVERIFIED with exactly what was read; never assumed from a filter.
- `infra/aws/lambda/investor-reporting/intake/poller.py` (Lambda `irpt-intake-poller`): folder delta with `nextLink` pagination and a durable `deltaLink` in `irpt-checkpoints`; immutable message ids; attachment retrieval `/$value`; original MIME retained where forwarded structure needs it; the ORIGINAL sender verified through the forwarding arrangement (never display From) then bound through `_gate.bind_firm` (IB-s-5); attachments + the intake receipt persisted to the bound firm's `firms/<id>/intake/...` (or `quarantine/`) BEFORE the checkpoint advances; a scan lease; a durable outbox handoff to `irpt-intake` (ids only); initial cutoff, overnight catch-up, delta expiry/resync and Retry-After defined in code and printed by the battery; idempotency: a repeated forward is ONE request, a new request with identical holdings is a NEW request (keyed on message identity, not content hash alone).
- The scheduler `cron(0/15 8-23 * * ? *)` `America/New_York` in `infra/aws/terraform/investor-reporting/intake/` applied `state = DISABLED` (the brief's proposal, declared here, not ratified; its first fire is a mailbox read, which is the qualified live arm).
- Proof is OFFLINE: recorded Graph responses (synthetic, shaped per the Graph delta/attachment API since no real forwarded specimens exist -- the gap stays named) through a transport stub; a kill injected between attachment persistence and checkpoint advance; a Retry-After response.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/intake/poller.py`, `graph_client.py`, `checkpoint.py`, `outbox.py` + `tests/` + `fixtures/graph/`; `infra/aws/terraform/investor-reporting/intake/` (`lambda.tf`, `iam.tf`, `schedule.tf` DISABLED, `main.tf` completed); the inspection record; the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_6.py` and `.result.md`.

---

## BOUNDS

- **NO LIVE MAILBOX READ.** The Graph client is exercised against the stub only; an outbound call to `graph.microsoft.com` from the battery fails arm (g). The scheduler stays DISABLED.
- **Current Silver holdings never replace what the request submitted.**
- **No universal analyst approval and no automatic outbound email** are built.
- **A message whose origin cannot be verified is quarantined, never bound.**

### Bounds every order carries (decomposition v0.1.1 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and closed at completion, the sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED; ORDER on any act that changes the world: open the entry, ACT, close the entry and COMMIT it BEFORE taking the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state).
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings.
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 existing scoped routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>`, per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.

---

## ACCEPTANCE

<criterion id="S6-AC1" cell_refs="IB-s-6"><invocation>timeout 600 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/battery_ib_s_6.py</invocation><expect>IBS6-INTAKE-DURABLE</expect></criterion>
**`S6-AC1` -- PASSES BY OUTPUT -- durability, idempotency, the gate, the scheduler disabled.**
**(a) PERSIST BEFORE CHECKPOINT -- THE DIFFERENCE CONTROL.** A kill injected after the attachment is persisted and before the checkpoint advances: on restart the same message is re-read, the attachment is NOT duplicated and the checkpoint then advances; with the kill injected AFTER the checkpoint, no re-read. Both runs printed.
**(b) DELTA, PAGINATION, RESYNC, RETRY-AFTER.** A three-page delta with `nextLink` is consumed in order; the `deltaLink` persists; an expired-delta response triggers the declared resync; a `Retry-After` response is honored (the wait is injected-clock, printed). `4 of 4`.
**(c) ONE REQUEST PER FORWARD; A NEW REQUEST FOR IDENTICAL HOLDINGS.** The same message delivered twice -> one request; a different message with byte-identical holdings -> two requests. Printed.
**(d) THE ORIGINAL SENDER, NOT DISPLAY FROM.** A fixture whose display From is a firm domain but whose verified original sender is not -> quarantine; the inverse -> bound to the firm. Printed.
**(e) LANDS ONLY WHERE THE POLICY SAYS.** Every persisted key is under the bound firm's enumerated prefixes (census of keys, `N of N`); a key outside them is impossible (the gate raised in the negative fixture).
**(f) THE INSPECTION IS RECORDED.** The Graph permission model found in the gateway, and VERIFIED / UNVERIFIED for the one-mailbox grant, printed from the record.
**(g) NOTHING LEFT THE MACHINE; THE SCHEDULER IS DISABLED; THE LEDGER CLOSED.** 0 external connections; `get-schedule --name irpt-intake-poll` prints `State: DISABLED`; `get-function-configuration irpt-intake-poller` `CodeSha256` equals the built zip's; sentinel committed (hash).

<criterion id="S6-AC2" cell_refs="IB-s-6"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/intake plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S6-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S6-AC3" cell_refs="IB-s-6" judgment="true"/>
**`S6-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: which Graph response shapes you had to SYNTHESIZE because no forwarded specimen exists, and what a real forward could carry that your fixtures do not (nested forwards, calendar items, inline images); what the gateway inspection settled and what it left open; and what 'within a short time' (FWD-9 ACCEPT) would measure as once the poller is enabled. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S6-AC1, S6-AC2, S6-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-6.mailbox-intake-durable-checkpointed-idempotent.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/intake/
infra/aws/terraform/investor-reporting/intake/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s6.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-6` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-6</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread. This cell CREATES one schedule (irpt-intake-poll) applied DISABLED; its first fire is the qualified live arm.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-intake-poller` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S6-AC1, S6-AC2, S6-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-6.mailbox-intake-durable-checkpointed-idempotent.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~3/IRPT_BCKEND.TO-IB-s-6.mailbox-intake-durable-checkpointed-idempotent.proof_of_spec.json S6-AC1,S6-AC2,S6-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
