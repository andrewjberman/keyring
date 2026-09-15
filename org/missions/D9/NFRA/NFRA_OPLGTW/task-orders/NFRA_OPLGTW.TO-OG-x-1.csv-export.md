# TO NFRA_OPLGTW.TO-OG-x-1 -- the authenticated, filtered CSV download

<to_id>NFRA_OPLGTW.TO-OG-x-1</to_id>
<project>NFRA_OPLGTW</project>
<issued_to>0.9.0_WK_NFRA_OPLGTW~5</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D9 | **Fabric:** laptop | **PRD:** `org/missions/D9/NFRA/NFRA_OPLGTW/prd/NFRA_OPLGTW_PRD.md` v0.2 @f0aa50dbc0 (ADMITTED) | **Contract:** `org/standards/NFRA_OPLGTW_CONTRACT.json` v1.0 | **Decomp cell:** `OG-x-1` | **outcome_ref:** FWD-4, FWD-6, FWD-7 | **depends_on:** `OG-d-1`, `OG-a-3`, `OG-o-1`, `OG-q-3` | **slot:** ~5, queue position 6

---

## WORKER FACE

### THE CELL

`OG-x-1` -- **the authenticated, filtered CSV download**: `infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py`
(ticket and CSV generation), `app/download_routes.py` (the page and the exchange), a static page under
`app/static/schwab_download/`, and their routes in `app/server.py`. It fills the ticket-issuing call site `OG-q-2` left in
`schwab_prepare_download`, uses `OG-a-3`'s browser login, and releases data only after `OG-o-1`'s acknowledged audit.

The PRD's C5, verbatim:
- *"Return only a Gateway HTTPS URL with its random opaque ticket in the URL fragment, no raw S3 presigned URL. A minimal
  same-origin browser script removes the fragment from history and exchanges it in an anti-CSRF, Origin-checked POST body;
  no ticket is put in a request path/query, redirect URL or referrer. If login is needed, retain only a hashed pending
  ticket bound to the secure browser session while the separate OIDC flow completes. Redact this POST body from all
  application diagnostics, use a restrictive script policy, and verify with a synthetic ticket that ALB and application
  logs contain no ticket secret. Ticket state carries hashed ticket ID, tid/oid, current grant revision, source versions,
  normalized query/projection, creation/expiry and single-use state. The browser page authenticates independently, shows
  master/date/file scope and Download CSV, and checks identity and current grant before atomically consuming the ticket at
  download start. A copied, expired, replayed, revised-policy or revoked ticket fails. A consumed ticket that fails
  midstream requires a new preparation request. Logical expiry is checked even before DynamoDB TTL deletion."*
- *"Run the same projection/filter/decimal rules as the query. Generate and validate a bounded CSV completely before
  starting its response; then reauthorize and stream without buffering it on the event loop. At most 250,000 rows and 50
  MiB UTF-8, within the export job deadline and shared source/resource caps. Over-limit exports fail and ask for narrower
  scope, never silently truncate. Include master, business date and field-definition metadata on the page on that same
  authenticated page. V1 has one downloadable artifact per ticket, the CSV; there is no second companion download that
  could reuse a consumed ticket. CSV headers identify units where necessary. Escape spreadsheet formula prefixes in text
  cells (including leading whitespace/control characters); numeric values remain numeric strings with correct signs and
  precision. Use safe filenames, attachment disposition, no-store/referrer policy and secure cookies; do not put tokens or
  data in access logs. Delete local export files on success, failure, cancellation and startup cleanup."*

Contract: `download_ticket_transport`, `download_artifacts_per_ticket` 1, `download_metadata`, `ticket_seconds` 300,
`export_rows` 250000, `export_utf8_bytes` 52428800, `disabled_operations` (`download_original`).

Write `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/DOWNLOAD_PATHS.json`: the exact page and
exchange paths this cell serves, one entry per path with its methods. `OG-i-3` reads that file to open the ALB rules.

**Read:** the PRD's "C5" and "C2" (ticket keys); the contract; `app/browser_oidc.py` (and its `BROWSER_PATHS.json`),
`app/integrations/schwab/integration.py`, `query.py`, `semantics.py`, `engine.py`, `app/schwab_audit.py`, `app/access_state.py`.

**Fixed inputs from `OG-a-3`, and the route-table rule (amended before hand-off, on `1.0.0_SA_CTO`'s ruling msg 97203;
rows `NFRA_OPLGTW-W3-S20`, `NFRA_OPLGTW-S14`).**
- The download browser's login is `OG-a-3`'s (@`06a9aec60d`): `GET /schwab/download/login` and
  `GET /schwab/download/callback`.
  - Its session and transaction cookies are scoped `Path=/schwab/download`, so your page and your exchange MUST sit
    at or under `/schwab/download`, or the session cookie never reaches them.
  - `browser_oidc.session_principal(request)` gives your routes the signed-in principal.
- `tests/test_principal_cutover.py::test_oga2_ac04` requires every served route to be classified in `ROUTE_CLASS`.
  - That file is granted to you, ENTRIES ONLY, for your own `DOWNLOAD_PATHS.json` paths.
  - Each entry carries the route's REAL guard class, as your code enforces it, never a default `"public"`. The
    public-route arm passes any route classed public, so misclassing a guarded route opens the hole `ROUTE_CLASS`
    exists to close.
  - A route whose class is genuinely unclear is a surprise row, not an entry.
  - AC28 runs the module; AC29 checks the diff.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="OGX1-AC1" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac01 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC1` (`test_ogx1_ac01`) -- `schwab_prepare_download` returns only a Gateway HTTPS URL with the ticket in its fragment, and never a presigned S3 URL.

<criterion id="OGX1-AC2" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac02 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC2` (`test_ogx1_ac02`) -- the ticket record holds a hashed ID, `tid`/`oid`, the grant revision, source versions, the normalized query and projection, creation and a 300-second expiry, and single-use state.

<criterion id="OGX1-AC3" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac03 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC3` (`test_ogx1_ac03`) -- logical expiry is checked before TTL deletion.

<criterion id="OGX1-AC4" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac04 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC4` (`test_ogx1_ac04`) -- the page script removes the fragment from history and exchanges it in an Origin-checked, CSRF-protected POST body.

<criterion id="OGX1-AC5" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac05 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC5` (`test_ogx1_ac05`) -- the ticket never appears in a request path, query string, redirect URL or referrer, by request capture.

<criterion id="OGX1-AC6" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac06 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC6` (`test_ogx1_ac06`) -- when login is needed, only a hashed pending ticket bound to the browser session is retained through `OG-a-3`'s login.

<criterion id="OGX1-AC7" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac07 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC7` (`test_ogx1_ac07`) -- a synthetic ticket appears in no application log line.

<criterion id="OGX1-AC8" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac08 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC8` (`test_ogx1_ac08`) -- the page carries a restrictive Content-Security-Policy.

<criterion id="OGX1-AC9" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac09 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC9` (`test_ogx1_ac09`) -- the page shows master, date, file scope and field definitions, and a Download CSV control.

<criterion id="OGX1-AC10" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac10 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC10` (`test_ogx1_ac10`) -- identity and the current grant are checked, then the ticket is consumed atomically at download start.

<criterion id="OGX1-AC11" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac11 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC11` (`test_ogx1_ac11`) -- (difference) a ticket copied to another principal fails, and the same ticket for its own principal succeeds (A10).

<criterion id="OGX1-AC12" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac12 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC12` (`test_ogx1_ac12`) -- an expired ticket fails.

<criterion id="OGX1-AC13" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac13 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC13` (`test_ogx1_ac13`) -- a replayed ticket fails.

<criterion id="OGX1-AC14" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac14 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC14` (`test_ogx1_ac14`) -- a ticket whose grant revision changed fails.

<criterion id="OGX1-AC15" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac15 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC15` (`test_ogx1_ac15`) -- a ticket whose grant was revoked fails.

<criterion id="OGX1-AC16" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac16 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC16` (`test_ogx1_ac16`) -- a consumed ticket that fails midstream requires a new preparation.

<criterion id="OGX1-AC17" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac17 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC17` (`test_ogx1_ac17`) -- the CSV applies the query's projection, filter and decimal rules, by parity with the same request through `schwab_query`.

<criterion id="OGX1-AC18" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac18 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC18` (`test_ogx1_ac18`) -- the CSV is generated and validated completely before the response starts.

<criterion id="OGX1-AC19" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac19 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC19` (`test_ogx1_ac19`) -- the response is reauthorized, then streamed without buffering on the event loop.

<criterion id="OGX1-AC20" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac20 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC20` (`test_ogx1_ac20`) -- an export over 250,000 rows or 50 MiB fails and asks for a narrower scope, and is never truncated.

<criterion id="OGX1-AC21" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac21 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC21` (`test_ogx1_ac21`) -- formula prefixes in text cells are escaped, leading whitespace and control characters included.

<criterion id="OGX1-AC22" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac22 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC22` (`test_ogx1_ac22`) -- numeric values stay numeric strings with correct sign and precision, and headers carry units where needed.

<criterion id="OGX1-AC23" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac23 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC23` (`test_ogx1_ac23`) -- the response has a safe filename, attachment disposition, `Cache-Control: no-store` and a referrer policy.

<criterion id="OGX1-AC24" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac24 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC24` (`test_ogx1_ac24`) -- one ticket yields one artifact, and a second download attempt fails.

<criterion id="OGX1-AC25" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac25 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC25` (`test_ogx1_ac25`) -- an original Parquet or bronze request fails for every profile, and no route serves an original (A11).

<criterion id="OGX1-AC26" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac26 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC26` (`test_ogx1_ac26`) -- local export files are gone after success, failure, cancellation and startup cleanup.

<criterion id="OGX1-AC27" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_schwab_export.py::test_ogx1_ac27 -q -p no:cacheprovider --color=no</invocation><expect>(?m)^1 passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC27` (`test_ogx1_ac27`) -- no token and no data value appears in an access log line.

<criterion id="OGX1-AC28" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 300 .venv-og/Scripts/python -m pytest infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py -q -p no:cacheprovider --color=no -m "not live"</invocation><expect>(?m)^[1-9][0-9]* passed(?![^\n]*(failed|error))</expect></criterion>
`OGX1-AC28` -- `tests/test_principal_cutover.py` passes, with this cell's routes classed in `ROUTE_CLASS` and graded by their class's arm.

<criterion id="OGX1-AC29" cell_refs="OG-x-1"><invocation>cd <WS> && timeout 120 .venv-og/Scripts/python org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/probes/og_x1.py AC29</invocation><expect>(?m)^VERDICT: PASS-OGX1-AC29(?![0-9])</expect></criterion>
`OGX1-AC29` -- (discriminating) the diff of `tests/test_principal_cutover.py` against your cut base is exactly `ROUTE_CLASS` entries for the paths in `DOWNLOAD_PATHS.json`, one per path, and no other line; the probe prints each path with its class and `VERDICT: PASS-OGX1-AC29` or `VERDICT: FAIL-OGX1-AC29 <reason>`.

<expected_criteria>OGX1-AC1, OGX1-AC2, OGX1-AC3, OGX1-AC4, OGX1-AC5, OGX1-AC6, OGX1-AC7, OGX1-AC8, OGX1-AC9, OGX1-AC10, OGX1-AC11, OGX1-AC12, OGX1-AC13, OGX1-AC14, OGX1-AC15, OGX1-AC16, OGX1-AC17, OGX1-AC18, OGX1-AC19, OGX1-AC20, OGX1-AC21, OGX1-AC22, OGX1-AC23, OGX1-AC24, OGX1-AC25, OGX1-AC26, OGX1-AC27, OGX1-AC28, OGX1-AC29</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, cut from `CLOUD` at hand-off (after `OG-q-3` and `OG-a-3` merged). Never push, merge, rebase, `checkout --` or `clean`.
- **Interpreter.** Your venv `.venv-og` (`cd <WS> && py -3.12 -m venv --system-site-packages .venv-og && .venv-og/Scripts/python -m pip install -r infra/aws/ec2/opal-gateway/requirements.txt msal moto pytest`) serves every invocation. Never commit `.venv-og/` or `.scratch/`.
- **Tests.** Each criterion names one test function in `tests/test_schwab_export.py`; write exactly that name. AC28 is a module run and AC29 a probe; `tests/test_principal_cutover.py` is yours for your `ROUTE_CLASS` entries only. Offline, moto and synthetic fixtures; browser behaviour is exercised through the ASGI test client and by reading the static script, never a real browser or Entra.
- **No original-file path.** `download_original` stays disabled for every profile; no route serves a Parquet or bronze object.
- **The known red test.** `tests/test_identity_scope.py::test_scoped_deny_by_default` fails at the cut base (row NFRA_OPLGTW-S1). Never edit it or `identity_tool_allowlist.txt`.
- **Code.** The commit gate lints with ruff for Python 3.9 syntax. `mcp==1.28.0` is not raised. The ALB is `OG-i-3`'s; nothing deploys.
- **No egress off Opal infrastructure.** No call to Claude, an Anthropic endpoint, an interactive Entra sign-in or any vendor API.
- **No secret in evidence.** Tickets in tests are synthetic.
- **Commits.** `.tools/safe-commit.sh` under your serial; every `.py` you touch passes `.tools/commit-gate.sh`.
- **Spec frozen; REFUSE what you cannot meet as written.** A criterion you cannot satisfy as written is refused and reported with its measurement -- never repaired, widened or satisfied by a route this order does not name. Anything off-spec is one surprise row, and you keep working.
- **Surprises** go to `org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `NFRA_OPLGTW-W5-S<k>`. Keep working after filing.
- **The preloaded context.** Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
infra/aws/ec2/opal-gateway/app/integrations/schwab/export.py
infra/aws/ec2/opal-gateway/app/integrations/schwab/integration.py
infra/aws/ec2/opal-gateway/app/download_routes.py
infra/aws/ec2/opal-gateway/app/static/schwab_download/
infra/aws/ec2/opal-gateway/app/server.py
infra/aws/ec2/opal-gateway/tests/test_schwab_export.py
infra/aws/ec2/opal-gateway/tests/test_principal_cutover.py
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc> v1 @8768f46770, cell `OG-x-1`, round 1 (section 3, S7).
<owned_cells>OG-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `OGX1-AC1` .. `OGX1-AC29` (29). Instance at
`org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~5/NFRA_OPLGTW.TO-OG-x-1.csv-export.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`, spec_ref.doc the PRD @f0aa50dbc0, decomp_ref.doc the
decomposition @8768f46770, decomp_ref.to_ref this order's path), validated with
`py -3.12 .tools/proof-of-spec-check.py <instance> OGX1-AC1,OGX1-AC2,OGX1-AC3,OGX1-AC4,OGX1-AC5,OGX1-AC6,OGX1-AC7,OGX1-AC8,OGX1-AC9,OGX1-AC10,OGX1-AC11,OGX1-AC12,OGX1-AC13,OGX1-AC14,OGX1-AC15,OGX1-AC16,OGX1-AC17,OGX1-AC18,OGX1-AC19,OGX1-AC20,OGX1-AC21,OGX1-AC22,OGX1-AC23,OGX1-AC24,OGX1-AC25,OGX1-AC26,OGX1-AC27,OGX1-AC28,OGX1-AC29`
BEFORE the `complete` flip. Result file `csv-export.result.md` beside it. **Flip `complete` only when every MECHANICAL
criterion PASSES by output.**
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 -- --budget 540, 5 of 5 carriers scanned (C1 230, C2 8, C3 12, C4 21, C5 334), 27 gates armed, none naming NFRA_OPLGTW. No project gate holds this cell; OG-i-3 waits on its DOWNLOAD_PATHS.json.
comp-iam: DECLARED-NOT-APPLICABLE -- this cell adds routes and a CSV writer inside the Gateway; its reads, state and audit go through OG-k-1, OG-d-1 and OG-o-1, so it adds no AWS operation, policy, principal or role of its own.
comp-adversary: RUN at L5 on the PRD v0.2 (@f0aa50dbc0) -- 4 of 4 cited commits verified; 7 cited paths, 6 stable, 1 GONE (an external RFC URL parsed as a repo path). Blindness stated: T11, filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (owned-paths-validate.py worker_grant).
</preflight>

Seating: slot ~5, queue position 6, handed after `OG-q-3` drains and `OG-a-3` merges. Round 1 of NFRA_OPLGTW, issued by
`2.0.0_SA_COO~O` (seated msg 96971, LD-0567). Decomposition v1 @8768f46770.

Amended 2026-09-15 ~19:1xZ, before hand-off, by `2.0.0_SA_COO~O` on `1.0.0_SA_CTO`'s ruling msg 97203. The changes:
- the worker face carries `OG-a-3`'s fixed download path and cookie scope (W3-S20);
- standing rule C: `tests/test_principal_cutover.py` is granted, ROUTE_CLASS entries only, with each route's real
  guard class;
- AC28 and AC29 are added.
No criterion was removed.
