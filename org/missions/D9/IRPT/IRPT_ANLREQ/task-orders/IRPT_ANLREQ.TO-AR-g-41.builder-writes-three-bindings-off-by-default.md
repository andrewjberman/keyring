# TO-AR-g-41 -- the builder writes the three resident bindings, off by default; the runtime builds the live ticket port from the `packager` binding

<to_id>IRPT_ANLREQ.TO-AR-g-41</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~68</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-41` (`decompositions/IRPT_ANLREQ_DECOMP_R5_G.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-31 and AR-g-32 are merged).

---

## WORKER FACE

### Read first

- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`, whole (276 lines): `main`, its arguments, and the `bindings = {...}` block.
- `infra/aws/lambda/investor-reporting/reports/resident_installed.py`: `OPTIONAL_QUEUES`, `load_bindings` (its validation of the optional queues),
  `make_packager`, and `build_resident_runtime` from "ready_url =" to the return.
- `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` `live_ticket_ports` and `TICKET_PORTS_CONFIG_KEYS`: the contract of `config`,
  `read_secret(name) -> str` and `http(method, url, headers, body_bytes) -> (status, body_bytes)`.
- `infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py` and `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_live_ports.py` for the fakes.

### THE CELL

A resident can be bound to two more queues and to the packager's principal, but nothing can turn that on: the builder
writes none of the three bindings, and the runtime never builds the live ticket port. Close both gaps. Nothing is deployed
and no release is cut.

**A. The builder** (`build_resident_package.py`).

1. A pure function, importable without running a build:
   `optional_bindings(analysis_ready_queue_url=None, commentary_ready_queue_url=None, packager=None) -> dict`.
   - All three None: returns `{}`.
   - A queue url that is not a `str` starting `https://sqs.`: `ValueError("BINDING_QUEUE_URL:<key>")`.
   - `packager` must be a dict of EXACTLY `api_base`, `email`, `secret_name`, each a non-empty string, `api_base` starting
     `https://`: else `ValueError("BINDING_PACKAGER_KEYS")`.
   - `commentary_ready_queue_url` given and `packager` None: `ValueError("BINDING_PACKAGER_REQUIRED")` (a bound queue with
     no principal refuses every message into the dead-letter queue).
   - `packager` given and `commentary_ready_queue_url` None: `ValueError("BINDING_PACKAGER_WITHOUT_QUEUE")`.
   - Otherwise returns only the members that were given, under the keys `analysis_ready_queue_url`,
     `commentary_ready_queue_url`, `packager`.
2. Three command-line flags, all optional: `--analysis-ready-queue-url URL`, `--commentary-ready-queue-url URL`, and
   `--packager api_base=<url>,email=<address>,secret_name=<name>`. `main` passes them through `optional_bindings` and
   merges the result into `bindings`; a `ValueError` ends the build with its token and writes nothing. The provenance block
   records which of the three were given, by key name only (`"optional_bindings": [...]`, sorted; absent when none).
3. **Off by default:** with none of the three flags, the bindings written are the same as before this cell for the same
   inputs: no new key at the top level and no `optional_bindings` in provenance.
4. `secret_name` is a NAME. The builder reads no secret and makes no new AWS call.

**B. The runtime** (`reports/resident_installed.py`).

5. `load_bindings` validates an optional `packager` member with the same rule as A1 and refuses
   `ResidentInstallRefused("RESIDENT_PACKAGER_BINDINGS")`; `commentary_ready_queue_url` present with no `packager` refuses
   `ResidentInstallRefused("RESIDENT_PACKAGER_REQUIRED")`.
6. `build_resident_runtime`, when the commentary-ready queue is bound, builds
   `ticket_ports = opal_packager.live_ticket_ports(bindings["packager"], read_secret=..., http=...)` and passes it to
   `make_packager`. `read_secret(name)` reads the secret's string through the injected `clients["secretsmanager"]`;
   `http` is a small function over the standard library that returns `(status, body_bytes)` for 2xx AND for an HTTP error
   status (the packager reads a 409's body), and raises only on a transport failure. Both are replaceable through
   `clients` (`clients.get("packager_http")`) so tests inject fakes. No secret value, token or header is printed, logged
   or put in an exception.
7. With no optional binding the runtime is unchanged: the same three keys, and the existing tests pass untouched.

**C. Tests**, offline: a NEW file `infra/aws/lambda/investor-reporting/reports/tests/test_resident_packager_binding.py` covering 5 (two refusals and one
accepted document), 6 (the runtime carries `packager` and `package_queue_url`; the live port's first POST goes to
`{api_base}/auth/login` through the injected `http`; `read_secret` is called with the bound name; a 409 body reaches the
packager), and 7. And builder tests in a NEW file `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/test_build_resident_bindings.py` for A1 (each refusal token, the
empty case, the full case).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR41-g-AC1" cell_refs="AR-g-41"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g41_checks.py g41</invocation><expect>^AR-G41-OK</expect></criterion>

<criterion id="AR41-g-AC2" cell_refs="AR-g-41"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g41_checks.py regress</invocation><expect>^AR-G41-REGRESS-OK</expect></criterion>

<expected_criteria>AR41-g-AC1,AR41-g-AC2</expected_criteria>

- AC1 imports the builder and asks `optional_bindings` directly for the empty case, the full case and the four refusal
  tokens, then runs the two new test files: 0 failed, at least 5 and 6 passed. At base it FAILs (no function).
- AC2 runs `reports/tests/test_resident_installed.py` (0 failed, at least 19 passed) and `ycharts/research/tests` (0 failed,
  at least 281 passed). At base it passes: it guards that nothing existing breaks.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs, no build of a real package. Every
  `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane (the builder lives
  in the base COO's folder): stop, file a row with the refusal text, report what is committed and what is not, and do not
  weaken a check or force a commit.
- **Rows** are `IRPT_ANLREQ-D2-W68-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below.
  Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~68" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~68@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~68 <0.9.0_WK_IRPT_ANLREQ~68@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/test_build_resident_bindings.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_packager_binding.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-41.builder-writes-three-bindings-off-by-default.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R5_G.md</decomp_doc> round 5, workstream ~G, cell `AR-g-41`.
<owned_cells>AR-g-41</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR41-g-AC1, AR41-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/IRPT_ANLREQ.TO-AR-g-41.builder-writes-three-bindings-off-by-default.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-41`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the
  product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR41-g-AC1,AR41-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the builder's new function and flags, with the lines;
- the runtime's new lines, and how `http` treats a 409;
- whether the builder commit was accepted or refused by the lane gate;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- 3 files read at HEAD: build_resident_package.py (276 lines, 0 occurrences of the three binding keys), reports/resident_installed.py (build_resident_runtime calls make_packager with no ticket_ports at line 392), opal_packager.py live_ticket_ports (its config and two injected callables). Both changes are off by default: a build with no new flag writes today's bindings, and a runtime with no optional binding returns today's three keys. NOT seen: the running host, which this cell does not touch. Ships only in the attach release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the secret is named, never read, by the builder; the runtime's read uses the host role's existing grant, which the attach release's pair must show.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the 2 gaps above and row IRPT_ANLREQ-D2-S29 (a bound queue with stub ports dead-letters every message). Traps: a default that turns a binding on; a secret value in a log or an exception; an http helper that raises on a 409 and so hides the conflict body the packager reads; a queue bound with no principal starting anyway; a builder flag that the runtime's validation refuses.
lane: reports/resident_installed.py (the lane AR-g-31 and AR-g-32 wrote) and the base COO's builder folder; if the lane gate refuses the builder file to a worker the issuer lands that half itself.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msgs 4971 and 4920.
