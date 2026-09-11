# TO IRPT_BCKEND.TO-IB-s-2 -- RESOLVED SCOPE: the viewer's policy, principal class and exact permitted account set, resolved from the headers the edge validator injects -- a partly permitted relationship never silently grants

<to_id>IRPT_BCKEND.TO-IB-s-2</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~2</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-10</issued_date>
<status>pending -- handed by 2.0.0_SA_COO~B at the IB-s-1 drain</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.4 @62301f71e0 | **Decomp cell:** `IB-s-2` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.1.1, s.1 + s.2) | **outcome_ref:** FWD-1 (contrib), FWD-2 (own), FWD-11 (contrib) | **PRD candidate:** B2

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~2;`.
- **Worktree:** `/c/tmp/wk-irpt-1-2` on branch `wk-irpt_bckend-1-2`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree. Every path in this face is relative to that root; make it absolute by prefixing `/c/tmp/wk-irpt-1-2/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~2 <0.9.0_WK_IRPT_BCKEND~2@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/` (granted by the tree convention; no `<paths>` entry needed).
- **Queue:** second in slot ~2, after IB-s-1.

---

## THE CELL

**The PRD row, verbatim at @62301f71e0 (the one carrier; the acceptance clause draft is the bar you build to):**

- **cell:** B2 identity resolution + permitted account set (`ResolvedScope`)
- **serves:** FWD-1 (contrib), FWD-2 (own), FWD-11 (contrib)
- **brief sections consumed:** O1; O8; IV.2 auth-validator paragraph, Global/scoped integration sources
- **contracts (P=produces, C=consumes):** P `ResolvedScope`
- **paths: reuse:** `infra/aws/lambda-edge/auth-validator-edge/index.mjs`; partner `roles.ts` x3 (vocabulary only, never grants)
- **paths: new home:** `infra/aws/lambda/investor-reporting/` (scope resolver)
- **fixtures / evidence:** 49F 201-group overlap fixture (no double-count, no manufactured primary credit); INF 79-unmapped-accounts reason list
- **acceptance clause draft:** a partly permitted relationship resolves to the exact allowed subset or an explicit unsupported scope, never the whole with rows hidden after; fingerprint identical on every downstream call

**What L5 adds (decomposition v0.1.1 s.2, s.6, s.9):**

- **Trace before you build (Phase 1, recorded in the instance):** `infra/aws/lambda-edge/auth-validator-edge/index.mjs` injects `X-User-*` headers and downstream Lambdas never parse JWTs (its own header comment, line 7); `X-Advisor-Role` is injected from the JWT claim (line 31); non-admin callers without an `advisorId` claim cannot hit advisor-scoped paths (line 188). Print the exact header names the validator injects, with line numbers, and the claim each comes from. The Opal-principal class is NOT visible in the validator's qualifiers at the cut: record how an Opal (non-firm) principal is distinguishable from that header set, or that it is NOT, as a finding -- IB-s-15 builds on your answer.
- `infra/aws/lambda/investor-reporting/_scope/resolve.py`: `resolve(headers, directory) -> ResolvedScope` validating against the schema: viewer policy, principal class (`firm-advisor` | `firm-admin` | `opal`), entitlement revision, verified request firm, the unique permitted account set + a stable fingerprint, requested vs resolved scope with a partial reason; namespaced vendor ids stay server-side (never in the returned object's browser-safe view). Consumed by every handler; the permitted-firm catalogue for Global is IB-s-15's addition to the same module.
- Fixtures: the 49F 201-group overlap (no manufactured primary credit), the INF unmapped list, a firm-authorized viewer (gets the firm population under the same rules), a browser-supplied header that the validator would never inject (refused).

**ISSUER AMENDMENT (2.0.0_SA_COO~B, 2026-09-11 ~00:2xZ, before this order was handed -- a cut defect of the issuer, surfaced on a worker's row):**
- **THE CONTRACT MUST ADMIT THE NULL IT DESCRIBES (row `IRPT_BCKEND-W2-S2`).** `_contracts/DirectoryEntry.schema.json` types `ids.relationship_id` as a bare string while its own description says an account-only entry carries null; 263 account-only 49F entries were refused by the validator on IB-s-1's first build. This order fixes the ONE token -- the property's `type` becomes `["string", "null"]` -- and updates the fixture pair: `fixtures/DirectoryEntry.valid.json` gains an account-only entry carrying `null`, `fixtures/DirectoryEntry.invalid.json` still refuses. The counterpart's typed client reads the same PRD table, whose description already names null, so the widening is compatible by construction; no other property moves. The resolver consumes the fixed schema.

---

## DELIVERABLE

`infra/aws/lambda/investor-reporting/_scope/resolve.py` + `tests/test_resolve.py` + the trace record `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/ib_s_2_validator_trace.md`; the battery `battery_ib_s_2.py` and `.result.md` in the same folder.

---

## BOUNDS

- **Headers supplied by a browser cannot become grants.** The resolver trusts only the validator-injected set you traced; anything else in the request is ignored for authorization.
- **Partner `roles.ts` files are presentation vocabulary, never grants.**
- **No deploy in this cell** -- a library consumed by the handlers; IB-s-1's handler picks it up at its next build in this slot's later orders.

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

<criterion id="S2-AC1" cell_refs="IB-s-2"><invocation>timeout 300 python org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/battery_ib_s_2.py</invocation><expect>IBS2-SCOPE-RESOLVED</expect></criterion>
**`S2-AC1` -- PASSES BY OUTPUT -- the resolver, with the trace as arm (a).**
**(a) THE TRACE IS PRINTED, WITH LINE NUMBERS.** The validator's injected header names and their source claims, read from `index.mjs` at your branch HEAD (denominator: headers found), and the Opal-principal answer (distinguishable / NOT distinguishable, with the line).
**(b) A PARTLY PERMITTED RELATIONSHIP NEVER SILENTLY GRANTS.** Fixture: a relationship with one account outside the viewer's population -> the resolved set is the exact allowed subset with `partial_reason` set, OR an explicit unsupported scope; the whole relationship is never returned. Printed.
**(c) THE FINGERPRINT IS STABLE AND DISCRIMINATING.** Same headers + same directory twice -> identical fingerprint; one account removed -> a different fingerprint. Both printed.
**(d) NO DOUBLE COUNT, EVERY GAP REASONED.** 49F overlap fixture: unique accounts preserved; INF unmapped: `N of N` with reasons.
**(e) THE DIFFERENCE CONTROL ON FORGED HEADERS.** A request carrying a browser-supplied `X-User-*` header the validator does not inject resolves to NOTHING extra: the resolved set equals the set without it. Printed.
**(f) SCHEMA-VALID, SERVER-ONLY FIELDS STAY SERVER-SIDE.** Every resolved object validates; the browser-safe view carries no vendor id (census of keys printed).
**(g) THE CONTRACT ADMITS THE NULL IT DESCRIBES -- THE DIFFERENCE CONTROL (issuer amendment, row W2-S2).** Print `ids.relationship_id`'s `type` from the schema (expect it to include `null`); an account-only fixture entry with `relationship_id: null` VALIDATES; the same entry against the pre-amendment schema text (kept as a fixture copy) is REFUSED. Both printed.

<criterion id="S2-AC2" cell_refs="IB-s-2" judgment="true"/>
**`S2-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: whether the validator's header set is sufficient to resolve a firm-admin versus an advisor versus an Opal principal, or whether IB-s-15 must add a claim upstream (name the file and the seat that owns it); and which fixture you could NOT build from real identity data and why. No verdict: the instance row carries the output under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming `3.0.0_SA_CVO` at L9.


<expected_criteria>S2-AC1, S2-AC2</expected_criteria>


<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-s-2.resolved-scope-from-the-validators-headers.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/_scope/
infra/aws/lambda/investor-reporting/_contracts/
infra/aws/lambda/investor-reporting/PATH_MANIFEST.json
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.1.1, cell `IB-s-2` (s.1 the rectangle; s.2 the L5 note; s.6 the root; s.8 the bounds).
<owned_cells>IB-s-2</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell creates, changes and fires no schedule, rule or trigger; it builds a library and runs a local battery. BLIND SPOT, stated: the cut-time run (5 of 5 carriers, 0 gates naming this project) is inherited from the issuance, not re-run here.
comp-iam: DECLARED-NOT-APPLICABLE -- nothing granted and nothing applied by this cell; no policy, role or trust document is written. BLIND SPOT: the reads this cell makes run under the launching seat's credentials, which is stated, not measured.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time on its own deliverable (a fresh cut has no prior artifact for it to read).
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). Every `infra/aws/**` and `data/assets/scripts/gold/**` path resolves to lane CLOUD_OPS_OR_ETL at HEAD and is admitted to you ONLY through this order while it is non-terminal; a path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: S2-AC1, S2-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-2.resolved-scope-from-the-validators-headers.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem, which `.tools/to-pipeline-gate.py` `check_complete_flip` globs for under `deliverables/*/`), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `python .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~2/IRPT_BCKEND.TO-IB-s-2.resolved-scope-from-the-validators-headers.proof_of_spec.json S2-AC1,S2-AC2` BEFORE the complete flip; rc 0 AND every mechanical criterion PASS-by-output, then flip this order's `<status>` to `complete` and commit instance, deliverables and flip together. A FAIL row leaves the order open and is your final report on it.

The grant is read from HEAD of your branch and only while this order is NON-TERMINAL: the issuance commit is in your ancestry at hand-off, so the flip is a modification, not an add.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages -- anything you would ask is a surprise row.
