# TO IRPT_ANLREQ.TO-AR-y-266.kimi-search-qa-live-runner -- the live runner for the Kimi search QA -- real ports wired, a dry-run that calls nothing, tested offline; the live run is a later Dell order

<to_id>IRPT_ANLREQ.TO-AR-y-266</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~91</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>24</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD
**Decomp cell:** `AR-y-266` (`decompositions/IRPT_ANLREQ_DECOMP_R22G_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~91`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-91` (branch `wk-IRPT_ANLREQ-91`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~91 <0.9.0_WK_IRPT_ANLREQ~91@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W91-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-266`, inlined) -- GATE (1), THE LIVE HALF: A RUNNER A DELL LANE CAN EXECUTE. Code and tests only; NO LIVE CALL is made by this cell.

*Ruling (a') (CTO msg 7137): the proof is the QA harness passing on a fixed set written before the run (`TIMXX` plus at least 4 known funds, each suggestion schema-valid and provider-verified, 0 errors). The harness `ycharts/generate/kimi_search_qa.py` (cell `AR-y-250`, drained @6cae7c8cc9, record `0.9.0_WK_IRPT_ANLREQ~83/r22/KIMI_SEARCH_QA_HARNESS.json`) takes the `send`, `search` and `verify` ports as arguments and is tested only with fakes. The advisory (`AR-y-249`, @2fd504168f) is `KimiAdvisory(send=, telemetry=, search_capability=, search=)`; the real transports are `kimi_port.kimi_send(read_secret)` and `kimi_port.kimi_search(read_secret)`; the secret is named `astn/kimi/api-key` (name only, never its value). What does not exist yet is the REAL `verify` port (an exact provider match, the same test the resident applies to a suggestion: `state` FOUND, `reason` EXACT_PROVIDER_MATCH, no `features_needed`, a provider receipt) and the entry point that wires all three and writes the QA record. That is this cell.*

1. **Read first:** `ycharts/generate/kimi_search_qa.py` and its tests, `ycharts/generate/kimi_port.py`, `ycharts/generate/resident_worker.py` (how the resident builds its `resolver(principal, owner, symbols)` for `verify`: the provider read, what credentials it needs and where they come from), `intake/security_resolution.py` (the resolver and `check`), `intake/upload_suggestions.py` (the exact-match test), and the resident session factory `ycharts/session/resident_session.py`. Record `read` {`verify_port` (how the resident's provider read is built, with file:line: which secret or key it uses by NAME, which module calls the provider), `reuse` (what you reuse unchanged)}. **If the provider read cannot be built outside the resident process without a secret you cannot name by id, or without new infrastructure, STOP before step 2, file a BLOCKING row and write the record with `runner` absent.**
2. **The runner.** ONE new file `ycharts/generate/kimi_search_qa_live.py` (ASCII): `main(argv)` with `--dry-run` (the default) and `--live`; it builds the three real ports through the existing code (the secret read by id through a Secrets Manager client created only when `--live`; the provider verify through the same resolver construction the resident uses, reusing it, not copying it), calls the harness with the harness's own fixed case list, writes the QA record to `--out <path>` (a file OUTSIDE the repository by default; the path is printed) and prints ONLY: the receipt (or `NO RECEIPT`), the per-case verdicts (case name and ok/failed, never a returned page or snippet), the counts of search calls, chat calls and provider calls, and the elapsed seconds. `--dry-run` constructs everything, calls NOTHING (every port is a recording stub), prints what `--live` WOULD call (the endpoint hosts, the secret NAME, the case count, the cost bound) and exits 0. `--live` refuses to run unless `--i-am-a-dell-lane-under-the-signed-pair` is also given (a plain guard so it is never run by accident), and never prints a key, a header or a response body.
3. **Tests, offline.** `ycharts/generate/tests/test_kimi_search_qa_live.py` (at least 6 tests): `--dry-run` calls no port (a spy proves it) and exits 0 with the planned calls printed; `--live` without the guard flag refuses before building any real port; with fakes injected for the three ports a live-mode run writes a record whose receipt equals the harness's; a failing case prints `NO RECEIPT` and exits non-zero; no output line contains the secret name's value or any page text (a spy returns a sentinel string in a snippet and the sentinel never appears in stdout); the default `--out` is outside the repository. `before_arm`: the file does not exist at HEAD (record that). Then the `ycharts/generate/tests` files that collect (the known baseline: 4 custody failures; fitz collection errors) and `intake/tests` (365 floor).
4. **The Dell runbook.** In the record write `runbook` {`order_shape` (what the Dell CloudOps order would say: step 0 caller identity and the secret readable (head only: `describe-secret`, no value), the dry-run first and its output kept, then ONE `--live` run, the guard flag, where the QA record goes (a path under the lane's deliverables), what is committed (the QA record and the receipt, no page text), the stop conditions (any `NO RECEIPT`, any non-200 from the search endpoint, any provider error: report, do not retry with other cases)), `cost_bound` (cases times attempts times the `swap` budget plus one search call per case plus the provider calls), `egress` (hosts called: `api.moonshot.ai` and the provider's), `rollback` (nothing is written to AWS)}.
5. **Write `r22/KIMI_SEARCH_QA_LIVE_RUNNER.json`:** `read`, `runner` {`path`, `sha256`, `modes`}, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm`, `runbook`, `claim`, `not_read`.
6. **In your report:** how `verify` is built, the dry-run output, the tests, what the Dell order still needs.

### ACCEPTANCE

<criterion id="AR266-y-AC1" cell_refs="AR-y-266"><invocation>python C:/dev/wk-irpt-anlreq-91/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y266-live --root C:/dev/wk-irpt-anlreq-91</invocation><expect>Y266-LIVE-OK</expect></criterion>
`AR266-y-AC1`: the record names how the provider verify port is built (file:line), the runner file with its sha256, at least 6 passing offline tests including the dry-run-calls-nothing spy and the live guard, and a Dell runbook.

<criterion id="AR266-y-AC2J" cell_refs="AR-y-266" judgment="true"/>
`AR266-y-AC2J` (judgment, graded at L9, never by you): the dry-run calls nothing (proved by a spy), `--live` refuses without its guard, no key, header, page text or secret value is ever printed, the verify port reuses the resident's provider read (not a copy), and no live call was made.

<expected_criteria>AR266-y-AC1 AR266-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~91/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/kimi_search_qa_live.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_kimi_search_qa_live.py
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22G_Y.md</decomp_doc>
<owned_cells>AR-y-266</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~91/IRPT_ANLREQ.TO-AR-y-266.kimi-search-qa-live-runner.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-266`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR266-y-AC1,AR266-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- new source and test files in a worktree; nothing is called, released or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (a') and the QA harness record against the cell; the lens: a dry-run that is not dry, a live mode runnable by accident, a key or page text printed, a copied provider read. The order requires a spy on every port, a guard flag, and no printed secret or snippet. NOT seen: the live Kimi search endpoint, the live chat model, the live provider and the resident host (0 live items read by the issuer; 2 source records read: the harness record and the advisory record).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ruling (a') (msg 7137): the live QA is the proof; this cell builds the runner a Dell lane executes under the signed pair. The grant names both files it writes. Workstream `YR` round 24. Base: `AR266-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
