# TO IRPT_BCKEND.TO-IB-s-5 -- THE FIRM DESTINATION POLICY AND THE INGESTION GATE: the firm is fixed from the sender's domain the moment a message arrives, the enumerated destinations are written down before the first request, and a new firm cannot be forgotten

<to_id>IRPT_BCKEND.TO-IB-s-5</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>staged -- assigned to slot ~1; becomes pending when the COO hands it over after IB-s-17 is terminal and merged.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-5` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-10 (own), FWD-9 (own, the binding), FWD-2 | **PRD candidate:** B5

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-1-1` on branch `wk-irpt_bckend-1-1`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-1/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** third in slot ~1, after IB-s-17. IB-s-6 (slot ~3) waits on this cell's merge.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B5 `FirmDestinationPolicy`: sender/domain-to-firm mapping, enumerated destinations, quarantine, immutable binding
- **serves:** FWD-10 (own), FWD-9 (own, the binding), FWD-2
- **brief sections consumed:** O7; IV.2 sender gate paragraph + verify-original-sender paragraph; IV.4 records paragraph
- **contracts (P=produces, C=consumes):** P `AnalysisRequest.ingestion-gate/destination-policy revision`
- **paths: reuse:** `data/firm_registry.json`
- **paths: new home:** policy document under `infra/aws/terraform/investor-reporting/`; proposed prefixes `firms/49financial/`, `firms/inflection/`, `firms/cottonwood/` in the proposed `opal-data-ycharts` bucket; a separately enumerated quarantine location; per-firm role/prefix permissions
- **fixtures / evidence:** --
- **acceptance clause draft:** a request from each firm's domain lands only in that firm's enumerated locations; a write to a second firm's location is refused; unknown, spoofed or contradictory origin never becomes a firm request; an Opal-origin mail with no target-firm rule stays unresolved; the policy has a named OWNER and a version; a new firm is a policy edit

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **OWNER of the `FirmDestinationPolicy`: `0.7.0_AE_CloudOps`** (decomposition s.2). Mechanism over name: `core/firm_destination_policy.json` is versioned (`policy_version`, `owner`, `firms[]`), and `tests/test_policy_completeness.py` FAILS LOUD when the set of enabled client firms in `data/firm_registry.json` differs from the policy's firms -- so a firm added to the registry (the ONE firm enumeration, that file's own law) obliges a policy edit that a green test cannot hide. CLAUDE.md s.5 'a new firm name is a GATE EDIT' now has a carrier.
- The policy maps `sender_domain -> firm_id` from the registry's `email_domain` (`49financial.com`, and the two ruled domains the registry carries for inflection and cottonwood -- READ them, never retype), enumerates per firm the allowed bucket prefixes (from `core/layout.json`), the metadata/queue/job namespaces and the export/artifact destinations, and names the execution roles allowed to write each. `quarantine/` is its own enumerated location with its own (narrower) grant.
- `infra/aws/lambda/investor-reporting/_gate/gate.py`: `bind_firm(sender_evidence) -> BoundRequest | Quarantined | Unresolved`; the bound firm is IMMUTABLE on the object (a later attempt to change it raises); `destination_for(bound, kind) -> key` returns only an enumerated location and REFUSES a key outside the bound firm's set; verified original-sender evidence is REQUIRED (display From alone is refused); an Opal-origin mail with no target-firm rule returns Unresolved, never a guess.
- The IAM half: per-firm prefix conditions (`s3:prefix` / resource ARNs under `firms/<id>/*`) attached in `core/` to the roles the later cells will assume by NAME (created here as role stubs with trust to Lambda, no other permissions), applied under a ledger entry in the same root as IB-s-17 -- same slot, so no second worktree ever touches this state.

---

## DELIVERABLE

`infra/aws/terraform/investor-reporting/core/firm_destination_policy.json`, `core/iam_firm_conditions.tf`, `core/roles.tf` (stubs); `infra/aws/lambda/investor-reporting/_gate/gate.py` + `tests/test_gate.py` + `tests/test_policy_completeness.py`; the ledger entry + sentinel; the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_5.py` and `.result.md`.

---

## BOUNDS

- **Do not read the mailbox, do not create a request.** Sender evidence in this cell is FIXTURES (verified-origin headers as the intake will present them); the intake is IB-s-6's.
- **Do not widen any existing role.** The role stubs are NEW roles for this project; the estate's roles are untouched.
- **A domain that is not in the registry is not a firm**, even if it looks like one; the test plants `example-firm.com` and expects Unresolved.

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

<criterion id="S5-AC1" cell_refs="IB-s-5"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_s_5.py</invocation><expect>IBS5-POLICY-BOUND</expect></criterion>
**`S5-AC1` -- PASSES BY OUTPUT -- the gate and the policy, each arm with its denominator.**
**(a) EACH FIRM LANDS ONLY IN ITS OWN LOCATIONS.** For each of the 3 registry firms, a fixture message from that firm's domain binds to that firm and `destination_for` returns keys under `firms/<id>/` only, for every destination kind; print `3 of 3` firms x `K of K` kinds.
**(b) A WRITE INTO A SECOND FIRM'S LOCATION IS REFUSED -- THE DIFFERENCE CONTROL.** With a request bound to firm A, request a destination under firm B and show the refusal; then the same call for firm A succeeds. Both printed.
**(c) UNKNOWN, SPOOFED, CONTRADICTORY, OPAL-ORIGIN.** Four fixtures: an unregistered domain, a display-From that disagrees with the verified original sender, contradictory evidence, an opalinvest.com origin with no target-firm rule -> Quarantined/Unresolved as the policy says, NEVER a firm; 4 of 4 printed.
**(d) THE BOUND FIRM IS IMMUTABLE.** After binding, an attempt to set the firm to another value RAISES; printed.
**(e) COMPLETENESS FAILS LOUD.** `test_policy_completeness.py` passes at HEAD (registry 3 == policy 3); then, in a scratch copy of the registry, plant a fourth enabled client firm and show the test FAILS naming the missing firm. Both runs printed.
**(f) THE POLICY IS VERSIONED AND OWNED; THE IAM HALF IS APPLIED.** Print `policy_version` and `owner`; `get-role` on each stub role prints its trust policy; the ledger for this slug is CLOSED and its sentinel committed (hash printed).

<criterion id="S5-AC2" cell_refs="IB-s-5"><invocation>timeout 120 .tools/terraform.exe -chdir=infra/aws/terraform/investor-reporting/core plan -no-color -input=false -lock=false</invocation><expect>No changes\. Your infrastructure matches the configuration\.</expect></criterion>
**`S5-AC2` -- THE ROOT IS CONVERGED after this cell's apply.**
Run after the apply and after the ledger closes.

<criterion id="S5-AC3" cell_refs="IB-s-5" judgment="true"/>
**`S5-AC3` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what 'verified original sender through the forwarding arrangement' can and cannot mean before the intake cell has inspected the mailbox (which header fields your fixtures assume exist); whether the owner named here is the right maintainer; and what an operator still cannot see from the policy file alone. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S5-AC1, S5-AC2, S5-AC3</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-5.firm-destination-policy-and-the-ingestion-gate.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/terraform/investor-reporting/core/
infra/aws/lambda/investor-reporting/_gate/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
org/critical_paths/change_management/
org/critical_paths/.open_deploys/irpt-bckend-s5.json
infra/aws/lambda/ci/lambda-source-map.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-5` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-5</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: RUN at the cut (20:2xZ, --budget 150) -- WITHIN BUDGET, denominator 5 of 5 carriers (C1=92 C2=6 C3=12 C4=20 C5=335), 25 gates ARMED, 0 name IRPT or any surface of this cell; the moratoria that bind here are G-20 (no monitor), G-23 (cross-firm), G-24 (vendor egress). BLIND SPOT: a ledger of gates, not prose obligations; 137 prose blocking fields unread.
comp-iam: RUN at the cut -- `comp-iam stats` + `roles`: denominator 191 roles parsed, 188 services, 307 gaps estate-wide; ZERO investor-reporting roles exist on the DESIRED plane, so this cell's role is graded at Phase 1 by `comp-iam service irpt-core` once its `.tf` exists and at Phase 2 by `comp-iam gaps` -- both recorded in the instance. BLIND SPOT: DESIRED plane only (the repo's Terraform); a GRANTED-BROAD wildcard cannot be falsified by a resource check.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S5-AC1, S5-AC2, S5-AC3. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-5.firm-destination-policy-and-the-ingestion-gate.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-s-5.firm-destination-policy-and-the-ingestion-gate.proof_of_spec.json S5-AC1,S5-AC2,S5-AC3` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
