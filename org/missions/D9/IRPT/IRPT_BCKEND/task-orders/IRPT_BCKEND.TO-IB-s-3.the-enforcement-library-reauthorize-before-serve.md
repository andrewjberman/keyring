# TO IRPT_BCKEND.TO-IB-s-3 -- THE ENFORCEMENT LIBRARY: reauthorize before serving on every handler, the key grammar, and a revoked grant refused against a warm cache

<to_id>IRPT_BCKEND.TO-IB-s-3</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>complete -- S3-AC1 PASS-by-output (IBS3-AUTHZ-LIBRARY, 5 of 5 arms; 6 of 6 swaps refused leaking 0 of 16 protected tokens, a revoked grant refused against an untouched warm cache, and a job refused at consumption); S3-AC2 RECORDED as judgment for 3.0.0_SA_CVO at L9 -- the wrapper CAN be bypassed and ships the detector that finds it, with four declared limits. Instance VALID rc=0 (7 artifact rows, 2 of 2 surprise ids resolve, alignment 1/1 cell). No deploy in this cell by the face's own words; nothing in the world changed.</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-3` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-2 (own) | **PRD candidate:** B3

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-1-2` on branch `wk-irpt_bckend-1-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** third in slot ~2, after IB-s-2. The library half of PRD candidate B3; the replay battery across every deployed route is IB-sb-3 (slot ~1, last).

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B3 authorization enforcement on every route, warm-cache revocation
- **serves:** FWD-2 (own)
- **brief sections consumed:** O1 enforcement paragraph; II.3 cache/idempotency-key paragraph
- **contracts (P=produces, C=consumes):** C `ResolvedScope`; keys per II.3
- **paths: reuse:** `infra/aws/terraform/partners-api/api-gateway.tf` (CUSTOM authorizer pattern)
- **paths: new home:** `infra/aws/terraform/investor-reporting/`
- **fixtures / evidence:** negative integration fixtures (swapped firm/advisor/account/relationship/report/PDF ids; revoked grant vs warm cache)
- **acceptance clause draft:** every negative request reveals no protected data; a cached result or artifact is reauthorized before serving; client names are never cache keys

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- `infra/aws/lambda/investor-reporting/_authz/enforce.py`: a decorator/wrapper every handler uses -- resolve scope (IB-s-2), REAUTHORIZE before serving any cached result or artifact, build keys through `_keys` (IB-s-17), and refuse when the current grant does not cover the requested object. A cache revision is not an enduring grant: the wrapper re-checks access at consumption for async jobs whose response scope was frozen at submission.
- The negative fixtures the PRD names, as unit tests against in-memory handlers: swapped firm / advisor / account / relationship / report / PDF identifiers; a revoked grant against a WARM cache (the difference control: same request served before revocation, refused after, cache untouched).
- Split rationale (decomposition s.1): this half is a shared dependency beneath every handler and must land BEFORE the handlers ship; the end-to-end replay across every DEPLOYED route can only run when the routes exist (IB-sb-3).

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/_authz/enforce.py` + `tests/test_enforce.py` (the negative fixtures); the battery `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_3.py` and `.result.md`.

---

## BOUNDS

- **Client names are never keys** -- the wrapper refuses a key component that resolves to a display name (through `_keys`).
- **No deploy in this cell.**
- **The wrapper never widens:** an object the scope does not cover is refused, never partially served.

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

<criterion id="S3-AC1" cell_refs="IB-s-3"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_3.py</invocation><expect>IBS3-AUTHZ-LIBRARY</expect></criterion>
**`S3-AC1` -- PASSES BY OUTPUT -- the library's negative fixtures, one arm each.**
**(a) SIX SWAPS, SIX REFUSALS.** Swapped firm, advisor, account, relationship, report and PDF identifiers against a wrapped in-memory handler: each refused with no protected bytes in the response (byte census printed, `6 of 6`).
**(b) REVOKED AGAINST A WARM CACHE -- THE DIFFERENCE CONTROL.** Serve a request (cache warm), revoke the grant in the fixture policy, replay the SAME request: refused; then restore the grant and replay: served from the still-warm cache. Three outcomes printed.
**(c) REAUTHORIZE AT CONSUMPTION.** An async job submitted under scope S, consumed after S is revoked: refused; printed.
**(d) KEYS THROUGH THE GRAMMAR.** Every key the wrapper builds passes `_keys`; a handler that tries to key by client name RAISES; printed.
**(e) THE FIRM-AUTHORIZED VIEWER GETS THE FIRM'S POPULATION UNDER THE SAME RULES.** Fixture printed.

<criterion id="S3-AC2" cell_refs="IB-s-3" judgment="true"/>
**`S3-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: what an in-memory handler cannot show about the real route path (the authorizer, the edge validator, API Gateway caching) that IB-sb-3 must; and whether the wrapper can be bypassed by a handler that forgets to use it -- and how a reader would detect that. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S3-AC1, S3-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-3.the-enforcement-library-reauthorize-before-serve.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_authz/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-3` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-3</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S3-AC1, S3-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-3.the-enforcement-library-reauthorize-before-serve.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-3.the-enforcement-library-reauthorize-before-serve.proof_of_spec.json S3-AC1,S3-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
