# TO-AR-g-32 -- the packager pre-checks its OWN store and reads no ticket; an already-attached conflict with the same identity is done (row D2-W66-S1)

<to_id>IRPT_ANLREQ.TO-AR-g-32</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~67</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G | **Decomp cell:** `AR-g-32` (`decompositions/IRPT_ANLREQ_DECOMP_R4_G.md`) |
**outcome_ref:** FWD-1 | **depends_on:** none (AR-g-31 is merged; TCKT_VNEXT's R2-pk-2 is in the tree and live).

---

## WORKER FACE

### Read first

- `infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py`, whole (307 lines): the module docstring's numbered flow, `handle_commentary_ready`,
  `live_ticket_ports` (its `ticket_package` and `attach`), `live_ticket_package`, `live_attach`.
- `infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py` `produce_package` (search `def produce_package`): the line that retains the package
  under the logical id `"%s-package-%s" % (request_id, sha)`.
- `infra/aws/lambda/investor-reporting/reports/repository.py` `ArtifactRepository`: `_binding`, `put`, `get`, `head`, and what `put` does when the logical id
  already holds an artifact (same bytes, and different bytes).
- `infra/aws/lambda/investor-reporting/reports/resident_installed.py` `make_packager` (the ports it wires).
- `infra/aws/lambda/ticket_center/lambda_function.py` `package_ticket` (search `def package_ticket`): READ ONLY. Its 409
  answers and the `_ident` it returns.
- The tests: `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_opal_packager.py`, `test_packager_i7.py`, `test_packager_live_ports.py`.

### THE CELL

Today `handle_commentary_ready` asks the TICKET whether it already carries a package, before any render. The ticket service
refuses that read to the packager (row D2-W66-S1), and by ruling it stays refused: the packager gets no ticket read. Make the
packager idempotent against data it owns.

1. **No ticket read.** Remove the `ticket_package` port everywhere: from `handle_commentary_ready`, from `live_ticket_ports`
   (it returns the `attach` port only), from `live_ticket_package`, and from `make_packager`'s wiring. After this cell no code
   under `ycharts/research/` or `reports/resident_installed.py` issues a GET on a ticket. Update the module docstring's flow.
2. **A package id known before the render.** The package is retained under the logical id
   `<request_id>-package-<commentary sha256>` (the sha256 of the commentary ref, which the handler already holds), not under
   the sha256 of the rendered pdf. Change `produce_package` so the caller supplies that sha (a required keyword when the
   artifacts port is present); the objects-port branch (no artifacts port) keeps today's behaviour.
3. **The pre-check.** Before reading the commentary bytes and before any render, the handler asks a new injected port
   `retained_package(record, tenant, request_id, commentary_sha256) -> the I7 ref dict {"artifact_id", "sha256", "version_id"}
   of the package already retained for this request and commentary, or None`. The live port computes the artifact id from the
   repository's own binding of the owner, the family and that logical id, and asks the repository for it (`head`, or the
   read the repository offers that returns the ref without the bytes). Absent means None. Any other refusal propagates by
   name: an unreadable store is never treated as "no package".
4. **A retained package means no render.** When `retained_package` returns a ref, the handler reads no commentary bytes and
   calls no producer: it builds the same payload with that ref as `pdf_ref` and POSTs it.
5. **Two renders of one package.** If the render runs and the store already holds that logical id (a concurrent delivery),
   the handler does not fail the message on that alone: it asks `retained_package` again and uses the stored ref. Say in your
   report what `put` raises in that case and whether the stored bytes can differ from the new render.
6. **The conflict is read, not guessed.** `attach` on a 409 parses the answer's `code`:
   - `PACKAGE_ALREADY_ATTACHED` AND the answer's `package` carries the same four pointers the packager posted (`report_ref`,
     `pdf_ref`, `original_ref`, `commentary_ref`): the outcome is `ALREADY_ATTACHED`. This is done; the message is deleted.
   - `PACKAGE_ALREADY_ATTACHED` with ANY pointer different: `PackagerRefused("ATTACH_CONFLICT:PACKAGE_ALREADY_ATTACHED_OTHER")`.
   - any other `code` that is a closed token (`[A-Z][A-Z0-9_]{0,63}`): `PackagerRefused("ATTACH_CONFLICT:" + code)`.
   - no `code`, or one that is not a closed token: `PackagerRefused("ATTACH_CONFLICT")`, as today.
   Compare identity by the four pointers only; never by `attached_at` or `attached_by`.
7. `PACKAGE_TERMINAL_OUTCOMES` in `ycharts/generate/resident_worker.py` stays exactly `ATTACHED`, `ALREADY_ATTACHED`; you do
   not edit that file.
8. Tests, offline, in a NEW file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_packager_own_store.py`: (a) a retained package: no
   commentary read, no produce call, the POST carries the retained ref; (b) no retained package: render, then POST;
   (c) the handler never asks for a `ticket_package` port (ports without that key succeed); (d) 409 already-attached with the
   same four pointers is `ALREADY_ATTACHED`; (e) 409 already-attached with one pointer different is refused by the name in
   6; (f) 409 with code `PACKAGE_TICKET_COMPLETED` is refused `ATTACH_CONFLICT:PACKAGE_TICKET_COMPLETED`; (g) 409 with no
   code is `ATTACH_CONFLICT`; (h) an unreadable store propagates its refusal and renders nothing; (i) the logical id the
   producer retains under is `<request_id>-package-<commentary sha256>`. Update the three existing test files to the new
   truth; keep every other test in the folder green.

In your report, state as a READ (not an assumption) whether any package is retained under the OLD logical id form anywhere
you can read offline (a fixture, a test store), and that no host binds the packager today (`reports/resident_bindings.json`
is generated; read `make_packager`'s caller for the binding it needs).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR32-g-AC1" cell_refs="AR-g-32"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g32_checks.py g32</invocation><expect>^AR-G32-OK</expect></criterion>

<criterion id="AR32-g-AC2" cell_refs="AR-g-32"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g32_checks.py regress</invocation><expect>^AR-G32-REGRESS-OK</expect></criterion>

<expected_criteria>AR32-g-AC1,AR32-g-AC2</expected_criteria>

- AC1 reads the three source files for the removed port and the conflict code, and runs the new test file: 0 failed, at
  least 9 passed. At base it FAILs.
- AC2 runs `ycharts/research/tests` (0 failed, 0 errors, at least 259 passed; it reads 250 at base) and
  `reports/tests/test_resident_installed.py` alone (0 failed, 0 errors). At base it FAILs on the count.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs. Every `.py` edit passes
  `.tools/commit-gate.sh`. `ticket_center` is READ ONLY. This cell ships only in a later resident release under its own pair.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another project's lane: stop, file a
  row with the refusal text, report, and do not weaken a check or force a commit.
- **Rows** are `IRPT_ANLREQ-D2-W67-S<k>`. APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below.
  Each row's `surfaced_at` is the output of `date -u +%Y-%m-%dT%H:%M:%SZ` at the moment you write it; never type a time. Gate:
  `python .tools/surprise-row-gate.py --check <path>`.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_ANLREQ~67" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_ANLREQ~67@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~67 <0.9.0_WK_IRPT_ANLREQ~67@opal.agent>" -F <msgfile> -- <paths>`.
  - Write the message file with the Write tool. Do not pre-`git add`.
  - Edit byte-preserving, ASCII only. Use the native Grep/Glob/Read tools; a recursive shell grep over the repo is denied by a hook.

<paths>
infra/aws/lambda/investor-reporting/ycharts/research/opal_packager.py
infra/aws/lambda/investor-reporting/ycharts/research/opal_producer.py
infra/aws/lambda/investor-reporting/ycharts/research/tests/
infra/aws/lambda/investor-reporting/reports/resident_installed.py
infra/aws/lambda/investor-reporting/reports/tests/test_resident_installed.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R4_G.md</decomp_doc> round 4, workstream ~G, cell `AR-g-32`.
<owned_cells>AR-g-32</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR32-g-AC1, AR32-g-AC2. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-32`.
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR32-g-AC1,AR32-g-AC2` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~66/IRPT_ANLREQ.TO-AR-g-31.packager-live-ticket-ports.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the handler's new order of steps, with the lines;
- what `put` raises when the logical id is already held, and whether the stored bytes can differ from a new render;
- the read on packages retained under the old logical id form;
- which existing tests you changed and why;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- 3 files read at HEAD (opal_packager.py 307 lines, opal_producer.py produce_package, reports/repository.py ArtifactRepository) and 1 read-only (ticket_center package_ticket). The packager is bound on no host: the running resident root 37210c771a-st30 carries no commentary_ready_queue_url (V1 of TO-APPLY-st30 printed 0), so nothing calls this code in production today. NOT seen: any live store, so whether a package is already retained under the old logical id is a question the order puts to the worker as a read. Ships only in a later resident release under its own pair.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; the cell REMOVES a call the ticket service refuses.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed; one GET stops being issued.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- read package_ticket's five 409 codes and its _ident (4 pointers plus attached_at, attached_by), and opal_producer.py line 260. Traps: treating an unreadable store as no package and so rendering and posting twice; comparing identity on attached_at; calling a different package on the ticket done; leaving one GET of a ticket behind; a logical id that two different commentaries share.
lane: ycharts/research/* and reports/resident_installed.py, the lane AR-g-31 wrote.
</preflight>

Source: 1.0.0_SA_CTO~DELL2 msgs 4348 (item 4) and 4861; row IRPT_ANLREQ-D2-W66-S1.
