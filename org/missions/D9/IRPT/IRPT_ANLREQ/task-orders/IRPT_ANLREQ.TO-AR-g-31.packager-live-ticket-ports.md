# TO-AR-g-31 -- the packager's two live ticket ports: read the ticket's package, and attach (I5), as `svc-irpt-packager` (rows D2-S29, D2-W62-S2)

<to_id>IRPT_ANLREQ.TO-AR-g-31</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~66</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-31` (`decompositions/IRPT_ANLREQ_DECOMP_R3_G.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-12, AR-g-13 and AR-g-22 are merged).

---

## WORKER FACE

### Read first

`org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_G.md`, the Finding and the Cell table. Then the module
docstring of `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py` (the seven `ports`), and in
`infra/aws/lambda/ticket_center/lambda_function.py`: `get_ticket` (:1196), `package_ticket` (:1392) and the `package_principal`
entry (:104-110).

### THE CELL

`opal_packager.live_attach` and `opal_packager.live_ticket_package` are stubs today: each is one statement,
`raise PackagerRefused("PACKAGER_PRINCIPAL_UNSET")`. Make them real behind a binding, and keep today's refusal when the binding
is absent.

1. **One factory.** Add `live_ticket_ports(config, *, read_secret, http)` to `opal_packager.py`. It returns
   `{"ticket_package": f, "attach": g}`.
   - `config` is the bindings member `packager`, a dict with exactly `api_base`, `email` and `secret_name`. `None`, a non-dict,
     a missing key or an extra key gives two functions that each raise `PackagerRefused("PACKAGER_PRINCIPAL_UNSET")`.
   - `read_secret(name) -> str` and `http(method, url, headers, body_bytes) -> (status, body_bytes)` are INJECTED. The module opens
     no connection and builds no client, as its docstring already promises.
   - Keep the module-level `live_attach` and `live_ticket_package` names; they stay the refusing forms.
2. **The session.** On first use, `POST {api_base}/auth/login` with JSON `{"email": email, "password": read_secret(secret_name)}`.
   Take `accessToken` from a 200 JSON answer and send it as `Authorization: Bearer <token>` on the two calls below.
   - Any other answer refuses `PackagerRefused("PACKAGER_LOGIN_REFUSED:<status>")`.
   - The secret value and the token live in memory only. Neither appears in an exception text, a return value, a log line or
     a print.
3. **`ticket_package(ticket_id)`.** `GET {api_base}/api/scoped/tickets/{ticket_id}`. On 200 return the ticket's `package` object,
   or `None` when the ticket carries none. Read `get_ticket` to learn where `package` sits in the answer; do not guess the shape.
   Any other status refuses `PackagerRefused("TICKET_READ_REFUSED:<status>")`.
4. **`attach(ticket_id, payload)`.** `POST {api_base}/api/scoped/tickets/{ticket_id}/package` with the payload as JSON, unchanged.
   A 2xx returns the parsed answer. A 409 refuses `PackagerRefused("ATTACH_CONFLICT")`. Any other status refuses
   `PackagerRefused("ATTACH_REFUSED:<status>")`.
5. **Wiring.** `infra/aws/lambda/investor-reporting/reports/resident_installed.py` `make_packager` (:283) passes the module's refusing ports today.
   Give it one optional keyword, `ticket_ports=None`: when given, use its two functions; when `None`, behave exactly as today.
   Do not read a secret, build an HTTP client or add a bindings key in this cell: who builds `ticket_ports` from the bindings is
   the attach release's act, not yours.
6. **What you must find out and report, not assume.** Does the ticket service let `svc-irpt-packager` GET a ticket it may
   package? Read `get_ticket`'s authorization. If that principal cannot read the ticket, FILE A ROW saying so and still deliver
   steps 1 to 5: the idempotence read is then a known gap for the issuer to rule.
7. **Test.** Add `research/tests/test_packager_live_ports.py`, offline, fakes only (a fake `http` that records calls, a fake
   `read_secret`). It must prove:
   - (a) with `config` None, and with a config missing a key, both ports refuse `PACKAGER_PRINCIPAL_UNSET` and `http` is never called;
   - (b) a good config logs in ONCE, then `ticket_package` returns the package on a ticket that has one and `None` on one that has
     none, each with the bearer header;
   - (c) `attach` posts the payload bytes that `json.loads` back to the payload, to the `/package` URL, with the bearer header;
   - (d) a non-200 login, a non-200 ticket read, a 409 attach and a 500 attach each refuse by the named code;
   - (e) THE SECRET NEVER LEAKS: with a marker secret value, no exception text raised in (d) and nothing captured by `capsys`
     contains the marker or the token;
   - (f) `make_packager` with `ticket_ports` given calls the given functions; with it absent, the refusing forms.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR31-g-AC1" cell_refs="AR-g-31"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py g31</invocation><expect>^AR1-G2-G31-OK</expect></criterion>

<criterion id="AR31-g-AC2" cell_refs="AR-g-31"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar1_g2_checks.py regress</invocation><expect>^AR1-G2-REGRESS-OK</expect></criterion>

<expected_criteria>AR31-g-AC1,AR31-g-AC2</expected_criteria>

- AC1 runs `test_packager_live_ports.py`, `test_opal_packager.py` and `test_packager_i7.py`: at least 6 passed and 0 failed across
  the three. At base it FAILs (`test_packager_live_ports.py` is absent).
- AC2: no file newly red. Allow at least 600 s. The two custody test files of `ycharts/generate` are red inside the full run at
  base (row IRPT_ANLREQ-D2-S31); that is the base set, not yours to fix.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS calls, no HTTP, no installs, no secret read. Every `.py` edit passes
  `.tools/commit-gate.sh`.
- **Refusal clause.** If a criterion cannot be met as written: stop, file a row, report, and do not weaken a check.
- **Rows** are `IRPT_ANLREQ-D2-W66-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below.
  Gate: `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~66" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~66@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~66 <0.9.0_WK_IRPT_ANLREQ~66@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_live_ports.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py
infra/aws/lambda/investor-reporting/reports/resident_installed.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-31.packager-live-ticket-ports.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_G.md</decomp_doc> round 3, workstream ~G, cell `AR-g-31`.
<owned_cells>AR-g-31</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR31-g-AC1, AR31-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/IRPT_ANLREQ.TO-AR-g-31.packager-live-ticket-ports.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-31`.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR31-g-AC1,AR31-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~65/IRPT_ANLREQ.TO-AR-g-22.packager-speaks-i7-and-custody-i5prime.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- where `package` sits in `get_ticket`'s answer, and whether `svc-irpt-packager` may GET a ticket (step 6), with the lines read;
- how the session is held and where the secret and token can and cannot appear;
- the `make_packager` change;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- two functions and one optional keyword; with no `packager` binding the behaviour is today's refusal, so nothing that runs today changes. Ships only in the attach release, after the svc-irpt-packager mint pair; nothing deploys here.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is added; the credential's secret and its reader are the mint pair's legs.
comp-routes: RUN (by reading) -- I5 is POST /api/scoped/tickets/{ticketId}/package (ticket_center lambda_function.py:18, :1392); the read is GET /api/scoped/tickets/{id} (:1196). No route is added or changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; the packager runs on the I4 message, and release 4 ships without that binding.
comp-adversary: RUN -- read opal_packager.py :134-197, resident_installed.py :283-302, resident_worker.py :901-924, ticket_center :104-132 and :1392-1460. Traps: a secret or token in an exception text; a login per call; a guessed `package` location; a principal that may POST the package but not GET the ticket; changing behaviour when the binding is absent.
lane: ~G (ycharts/research/*, reports/resident_installed.py).
</preflight>

Source: CTO round-3 analysis @430d79e86d section 4 G3; rows IRPT_ANLREQ-D2-S29 and D2-W62-S2; CTO~DELL2 msg 4296.
