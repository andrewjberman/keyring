# TO IRPT_ANLREQ.TO-AR-y-166 -- the script that submits ONE synthetic analysis request naming a ticket (BUILD ONLY; nothing is invoked live)

<to_id>IRPT_ANLREQ.TO-AR-y-166</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>YS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a script and its record in the worker's deliverables; nothing is invoked, uploaded, applied or pushed)
**Decomp cell:** `AR-y-166` (`decompositions/IRPT_ANLREQ_DECOMP_R16D_Y.md`) | **outcome_ref:** serves NFRA_TRNSPT TR-dp-24 | **depends_on:** none
**DIRECT ACT** on the CTO's word (msg 6575, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_RELAUNCH_THREE_ASKS_READ_AND_RULED_20261012.md` section 7).

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W53-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`.

### THE CELL (`AR-y-166`, inlined) -- BUILD ONLY. You call nothing live; no boto3 client is created in `--plan` or `--self-test`.

*A script that submits ONE synthetic analysis request in tenant `cottonwood`, as the project's existing synthetic filer, naming a ticket.*

**Why.** A sibling project's driven draft needs an accepted request whose record carries a `ticket_id` stated by the submitter. The
existing accepted requests carry none. The CTO ruled one new synthetic request (msg 6575). Another seat, later, runs your script once;
you only build it and prove it offline.

**Read first** (do not retype what they say; cite lines in your report):
- The shape of an earlier on-behalf upload by a direct invoke: `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/irpt_y75/y75_x1_arms.py`
  (the nine trusted headers, `x-contract-version`, the POST event shape, the filer constant `irpt-y75-testfiler-20261009@opal.invalid`,
  the synthetic CSV). Take the shape from it; re-read every contract from the code, as that script's header says it did.
- The upload door: `infra/aws/lambda/investor-reporting/intake/uploads.py` (route, required body fields, the upload token pattern) and
  `intake/upload_entry.py` / `reports/generate_installed.py` (how the POST is routed).
- The submission door: `infra/aws/lambda/investor-reporting/reports/submission.py`, the acceptance path (`acceptance.py` stores `ticket_id`
  on the record), and `docs/contracts/investor-reporting/v1/AnalysisSubmissionRequest.schema.json` (the OPTIONAL `ticket_id` and its
  pattern; the route keys in `routes.json`).

**Build `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r16/submit_synthetic_request.py`** (ASCII only), with these behaviours:
1. Arguments: `--tenant` (the only value admitted is `cottonwood`; anything else exits non-zero BEFORE any other work), `--ticket` (must
   match the schema's `ticket_id` pattern, else exit non-zero), `--plan`, `--self-test`, `--run`. `--run` is the only mode that creates a
   boto3 client; it also requires `--i-have-the-ctos-word msg-6575` (a literal) so it cannot be started by accident.
2. It builds TWO events, as the earlier script did: (i) the on-behalf template upload (the synthetic CSV `Ticker,Dollars` with two
   well-known listed tickers, a fresh upload token), then (ii) the analysis submission whose body names the ticket and every other
   member the submission door REQUIRES from the code (name each, and say where you read it). The filer is the constant above (reserved
   domain `.invalid`); no new identity is made and no users row is written.
3. `--plan`: print the two events as two JSON lines (each line starts with `{`), no network, no client. The body carries the ticket id.
4. `--run` (never run by you): read the filer's users row (a read) and STOP with a clear message if it does not list or admit
   `cottonwood`; invoke the deployed function for event (i), read the upload id from the answer, build event (ii) from it, invoke for
   event (ii); print ONLY the ids the answers carry (upload id, input id, request id) and the status codes. Print no address and no body.
5. `--self-test`: against in-memory fakes of the function and the table, show: both events validate against the published schema where
   one exists; a tenant other than cottonwood refuses; a malformed ticket id refuses; `--run` without the literal refuses; a users row that
   does not admit cottonwood stops the run before any invoke. Print `SUBMIT-SELFTEST-OK` on success.
6. The script's boto3 surface is `lambda.invoke` and READS only (`get_item`, `query`, `scan`, `get_function_configuration`). No put,
   update, delete, send, publish or create call name appears anywhere in it.
7. Write `r16/SUBMIT_SCRIPT_RECORD.json`: the script's git blob, the required members of event (ii) each with the line you read it at,
   the literal keys a successful `--run` would create BY KIND (request item, upload rows and objects, queue message, anything the
   door writes that you can read from the code), what `--run` reads, and what you could NOT read. The next seat's pair is written on it.
8. In your report: what event (ii) needs beyond the ticket id; whether the filer's users row can be read from the code or only live (say
   which); whether the door is reachable by a direct invoke or only through the portal; and anything that makes the request fail
   acceptance (for example a provider resolution the resident must finish) so the next seat knows what it will see.

### AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-12, after reading the script)

The script passes both checks and I read it. ONE gap against the CTO's ruling (msg 6575: synthetic only, no identity minted): the on-behalf
upload makes the ADVISOR the request's owner, and `resolve_advisor` accepts ANY active cottonwood user whose opaque label matches, so a real
person could end up owning the test request. Close it, in the same script:
1. After `resolve_advisor` finds the address, `--run` STOPS before ANY invoke unless that address is on a RESERVED domain: the part after the last
   at-sign, lower-cased, equal to `example.com`, `example.org` or `example.net`, or ending `.invalid`, `.test` or `.example` (the rule `count_f2.py`
   used). Print `STOP: the advisor is not a synthetic address. No invoke was made.` and never the address.
2. `--self-test` gains two arms: a resolved advisor on a real-looking domain (for example `person@firm.com` in the fake users table) stops with zero
   invokes; a reserved-domain advisor proceeds (the existing happy path). The count of arms changes; the printed token does not.
3. Add the reserved-domain rule to `SUBMIT_SCRIPT_RECORD.json` (what `--run` reads and when it stops) and say in your report that S13 is closed by it.
4. Re-run both criteria and re-validate the proof instance; commit as a new commit (do not amend). Nothing else changes.

### ACCEPTANCE

<criterion id="AR166-y-AC1" cell_refs="AR-y-166"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16d_checks.py y166-self --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y166-SELF-OK</expect></criterion>
`AR166-y-AC1`: the script exists, is ASCII, holds no write-shaped call, and its `--self-test` prints `SUBMIT-SELFTEST-OK`.

<criterion id="AR166-y-AC2" cell_refs="AR-y-166"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r16/ar16d_checks.py y166-plan --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y166-PLAN-OK</expect></criterion>
`AR166-y-AC2`: with credentials blanked, `--plan` prints exactly two POST events as JSON lines carrying the ticket id for the reserved-domain filer; a tenant other than cottonwood and a malformed ticket id each exit non-zero.

<criterion id="AR166-y-AC3J" cell_refs="AR-y-166" judgment="true"/>
`AR166-y-AC3J` (judgment, graded at L9, never by you): the two events are what the deployed door will accept, read against `uploads.py`, `submission.py`, `acceptance.py` and the schema, and `--run` can create nothing beyond the literal kinds the record lists.

<expected_criteria>AR166-y-AC1 AR166-y-AC2 AR166-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R16D_Y.md</decomp_doc>
<owned_cells>AR-y-166</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR166-y-AC1 AR166-y-AC2 AR166-y-AC3J. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-166.submit-synthetic-request-script.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-166`. `AR166-y-AC3J` is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR166-y-AC1,AR166-y-AC2,AR166-y-AC3J`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script in the worker's deliverables; no resource is changed and none is called. The script's later run is a separate order.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger is touched. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call; who may invoke the function and read the users row is the later run's order to read.
comp-adversary: RUN -- by reading the CTO's ruling (msg 6575: tenant cottonwood, existing synthetic filer, no identity minted, nothing deleted after) against the cell; the lens: a script that can write more than the ruling allows. The check refuses any write-shaped boto3 call name, the literal tenant and the literal word are required, and the self-test shows a users row that does not admit cottonwood stops the run. NOT seen: the deployed door and the filer's real users row.
lane: the worker's deliverables and one append to the project's investigation channel.
</preflight>

---

## RECORD FACE

- Cut on the CTO's word, msg 6575, as a DIRECT ACT of its OWN WORKSTREAM `YS` (a scope disjoint from workstream Y's round 16: the reader, the
  F2 arm and the counts; the spine's second-workstream rule, row IRPT_BCKEND-S179). The round-16 decomposition is frozen, so this is one cell in its
  own decomposition file; its round counter is its own. `AR166-y-AC1` and `AR166-y-AC2` base: FAIL as expected (no script).
- The SUBMISSION is not this order: when `2.0.0_SA_COO~V2` has filed the test ticket, the issuer names an executor that can reach the
  store and cuts its own order, with a never-widen pair on this script's record.
