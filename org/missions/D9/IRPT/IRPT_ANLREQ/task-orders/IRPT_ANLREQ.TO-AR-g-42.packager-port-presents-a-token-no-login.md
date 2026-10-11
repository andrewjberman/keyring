# TO-AR-g-42 -- the packager's ticket port presents a token read by name and never logs in; the `packager` binding is `api_base` + `secret_name`

<to_id>IRPT_ANLREQ.TO-AR-g-42</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~69</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>6</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-42` (`decompositions/IRPT_ANLREQ_DECOMP_R6_G.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-31, AR-g-32 and AR-g-41 are merged).

---

## WORKER FACE

### Read first

- `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`: `TICKET_PORTS_CONFIG_KEYS`, `live_ticket_ports` (whole), `live_attach`, and the
  module docstring's lines about the ports.
- `infra/aws/lambda/investor-reporting/reports/resident_installed.py`: `PACKAGER_KEYS`, the `packager` validation in `load_bindings`, `_packager_http`,
  `_read_secret_string`, and the lines of `build_resident_runtime` that build `ticket_ports`.
- `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py`: `optional_bindings`, `parse_packager` and the `--packager` flag.
- The tests: `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_live_ports.py`, `infra/aws/lambda/investor-reporting/reports/tests/test_resident_packager_binding.py`,
  `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/test_build_resident_bindings.py`.
- READ ONLY, for the shape of the stored secret: `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/F10_DEPLOY/NEVER_WIDEN_PAIR_SVC_COMMENTARY_MINT.md`
  section 3: the secret's value is JSON with a `token` member, and "consumer reads .token".

### THE CELL

The packager's live port logs in: on first use it POSTs `{api_base}/auth/login` with an email and a password read from a
secret, then holds the bearer token it gets back. That is a person-shaped identity. By ruling the packager is a service
with ONE signed token in ONE secret. Re-cut the port to present that token. Nothing is minted, granted or deployed here.

1. **The binding shape, everywhere the same.** The `packager` binding is a dict of EXACTLY `api_base` and `secret_name`,
   each a non-empty string, `api_base` starting `https://`. No `email`. A binding carrying any other key (including
   `email`) is refused. Apply it in three places: `opal_packager.TICKET_PORTS_CONFIG_KEYS`, the runtime's `PACKAGER_KEYS`
   and validation (`RESIDENT_PACKAGER_BINDINGS`), and the builder's `optional_bindings` and `--packager` parse
   (`BINDING_PACKAGER_KEYS`). The `--packager` flag's form becomes `api_base=<url>,secret_name=<name>`.
2. **The port presents the token.** `live_ticket_ports(config, *, read_secret, http)` keeps its signature and returns
   `{"attach": f}`. On first use it calls `read_secret(config["secret_name"])`, parses the string as JSON, and takes its
   `token` member (a non-empty string). It then sends `Authorization: Bearer <token>` on the POST to
   `{api_base}/api/scoped/tickets/{ticket_id}/package`. The token is held in the closure only.
3. **No login call exists.** After this cell no code under `ycharts/research/` or `reports/resident_installed.py` builds a
   request to `/auth/login`, and the string `auth/login` does not appear in `opal_packager.py`.
4. **Refusals, by name, never carrying the secret or the token:**
   - the secret's string is not JSON, or has no non-empty string `token`: `PackagerRefused("PACKAGER_TOKEN_UNREADABLE")`;
   - `read_secret` raises: `PackagerRefused("PACKAGER_TOKEN_UNREADABLE:TRANSPORT")`;
   - the POST answers 401 or 403: `PackagerRefused("ATTACH_REFUSED:<status>")`, and the held token is DROPPED so the next
     message reads the secret again (a rotated token is picked up without a restart); it does not retry inside the same call;
   - the 409 handling of AR-g-32 is unchanged (`PACKAGE_ALREADY_ATTACHED` with the same four pointers is done; the other
     conflict names as they are).
5. A malformed `config` still gives the refusing port (`PACKAGER_PRINCIPAL_UNSET`), as today.
6. Tests, offline: update the three test files to the new truth and add cases for 2, 3 and each refusal of 4, including
   that after a 401 the next call reads the secret again, and that no test or code path posts to a login route. Keep every
   other test in those folders green.

In your report, state the lines that show the token never reaches an exception text, a return value, a log or a print.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR42-g-AC1" cell_refs="AR-g-42"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g42_checks.py g42</invocation><expect>^AR-G42-OK</expect></criterion>

<criterion id="AR42-g-AC2" cell_refs="AR-g-42"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g42_checks.py regress</invocation><expect>^AR-G42-REGRESS-OK</expect></criterion>

<expected_criteria>AR42-g-AC1,AR42-g-AC2</expected_criteria>

- AC1 probes the port directly with injected fakes: the token is read by the bound name, the POST carries the bearer
  token and no login is posted, a secret with no `token` is refused by name, a 401 drops the token; and it asks the builder
  and the runtime to refuse a binding that carries `email`. At base it FAILs.
- AC2 runs `ycharts/research/tests` (0 failed, at least 281 passed), `reports/tests/test_resident_installed.py` and
  `reports/tests/test_resident_packager_binding.py` (0 failed, at least 19 and 18 passed) and the builder's test file (0
  failed, at least 26 passed). At base it passes: it guards that nothing existing is lost.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs, no build of a real package, no secret
  read. `infra/aws/lambda/ticket_center/` is READ ONLY and is not in your paths. Every `.py` edit passes `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with
  the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows** are `IRPT_ANLREQ-D2-W69-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below.
  Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~69" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~69@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~69 <0.9.0_WK_IRPT_ANLREQ~69@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_packager_binding.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/build_resident_package.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/test_build_resident_bindings.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~69/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-42.packager-port-presents-a-token-no-login.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R6_G.md</decomp_doc> round 6, workstream ~G, cell `AR-g-42`.
<owned_cells>AR-g-42</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR42-g-AC1, AR42-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~69/IRPT_ANLREQ.TO-AR-g-42.packager-port-presents-a-token-no-login.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-42`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: commit the
  product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR42-g-AC1,AR42-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~68/IRPT_ANLREQ.TO-AR-g-41.builder-writes-three-bindings-off-by-default.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the port's new lines, and the lines that keep the token out of every exception, return value, log and print;
- what happens on a 401, with the lines;
- which existing tests you changed and why;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- 4 files read at HEAD: opal_packager.py live_ticket_ports (the login POST and its three-key config), reports/resident_installed.py (PACKAGER_KEYS and the port's wiring, merged @fb4aaf8fa2), build_resident_package.py (optional_bindings), and READ ONLY infra/aws/lambda/ticket_center/lambda_function.py (the package door, lines 1422-1452). The packager is bound on no host: the running root 19b02b2971-st31 carries neither queue binding (its V1 printed 0 and 0), so nothing calls this code in production. NOT seen: any secret, any token, any live call. Ships only in the attach release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change in this cell; the read grant on the host role is the mint pair's, a laptop leg.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; one call to a login route stops being built.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read the commentary token's custody rule (a JSON secret, consumer reads .token) and the package door's own admission. Traps: a token in an exception text or a log line; a stale token held forever after a rotation; a silent fallback to the login form when the secret has no token; a binding that still accepts an email; a retry loop on a 401 against a service that counts failures.
lane: ycharts/research/*, reports/resident_installed.py and the base COO's builder folder, the lanes AR-g-41 wrote.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msg 5090.
