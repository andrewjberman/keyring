# TO IRPT_BCKEND.TO-IB-rtf-11 -- THE DIRECTORY ENTRY READS THE PAYLOAD-2.0 EVENT SHAPE THE INTEGRATION SENDS: row S92 (ARMED, INFERRED from source, masked live by S90) -- `directory/entry.py:92-93 @9f72f4d6a4` calls `_handler.search(..., event.get('q', ''), event.get('limit', DEFAULT_LIMIT))` and `:136` calls `_handler.resolve(..., event.get('selection') or {})`, reading the TOP LEVEL of the raw event; the IRPT integrations are `payload_format_version = "2.0"` (`api/integrations.tf:57`), where the query sits under `queryStringParameters` and the body under `body` (a JSON string, possibly base64). So on the deployed path search ignores `q` and `limit` (returns the first 20 of the projection, `handler.py:179-181`) and resolve always answers UNSUPPORTED "selection matches nothing" (`:255-259`). The in-process tests pass top-level keys, which is why they never saw it. This order makes the entry read the shape the integration sends and proves it on a REAL payload-2.0 event, with the old shape as the negative control

<to_id>IRPT_BCKEND.TO-IB-rtf-11</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~1</issued_to>
<issued_by>2.0.0_SA_COO~B</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_IRPT_BCKEND~1, 2026-09-19: directory/entry.py reads the 2.0 event shape via one new helper (_event_params), used by both search() and resolve(); handler.py and every _authz/ module verified byte-identical to the cut. R68-AC1 PASSES BY OUTPUT (battery_ib_rtf_11.py, token IBR68-DIRECTORY-ENTRY-READS-PAYLOAD-2-0, rc=0); R68-AC2 recorded for the CVO, no verdict. proof-of-spec-check rc=0. Row IRPT_BCKEND-W1-S33 filed (OBSERVATION, INERT). Code and tests only; the rebuild + deploy of `irpt-directory-search` rides IB-rtf-10's second pass after this order drains (chain: rtf-11 -> rtf-10 (e)-(f) -> rtf-3's third hand). No deploy in this order.</status>

**Directive:** D9 | **Fabric:** laptop | **Round:** 6 (the CTO's round-5 analysis @81472c3a47, msg 98115) | **PRD:** `../prd/IRPT_BCKEND_PRD.md` v0.14 @b8e98d5a4d (no addendum at round 5) | **Round-5 analysis:** `../deliverables/1.0.0_SA_CTO/IRPT_BCKEND_ROUND5_ANALYSIS.md` @81472c3a47 | **L4 rulings carried:** no-source members @457cf494c6; partial projection @61627f39f9; registry deadlock @9eeb9a70a8 + @80dada6d8d | **Rulings carried:** R-40, R-42, R-44, R-45 @57bc083d45; the forward-looking-criterion bar; Rule 30; the reader-census bar and the blob-pin notation (round-5 analysis s.1, s.4) | **Decomp cell:** `IB-rtf-11` (`../decompositions/IRPT_BCKEND_DECOMP.md` v0.6, s.R6.8) | **outcome_ref:** FWD-1, FWD-2, FWD-5, FWD-11

---

## IDENTITY AND WORKTREE

- **Serial:** `0.9.0_WK_IRPT_BCKEND~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_IRPT_BCKEND~1;`.
- **Worktree:** `/c/tmp/wk-irpt-6-1e` on branch `wk-irpt_bckend-6-1e`, cut by the issuer from `HEAD` of `CLOUD` at hand-off. First act: `git rev-parse --abbrev-ref HEAD` and `test -d org && test -d .tools && echo TREE-OK`; a worktree that does not carry the paths this face names is a BLOCKING row and a stop.
- **Repo root for every path below:** the worktree; make a path absolute by prefixing `/c/tmp/wk-irpt-6-1e/`.
- **Commit:** `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~1 <0.9.0_WK_IRPT_BCKEND~1@opal.agent>" -F <msgfile> -- <paths>`, `<msgfile>` written with the Write tool. On your branch only; never push, merge, rebase, `checkout --` or `clean`.
- **Deliverables:** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/` (granted by the tree convention). Batteries are named `battery_<cell>.py`, the cell id lower-cased with underscores.
- **Python:** `py -3.12`. A recursive `grep`/`find` in Bash is DENIED by a rail hook and a denial aborts the WHOLE call; use the Read/Grep tools and keep a gated read in its own call. Capture `safe-commit.sh` output to a file, never pipe it to `tail`, never pair it with `$( )`. No deploy in this order.

---

## THE CELL

- (a) THE EVENT SHAPE, MEASURED NOT ASSUMED: read `api/integrations.tf` for every route that reaches `directory/entry.py` (`n of n` routes, payload version per route), and capture ONE REAL payload-2.0 event as the deployed integration delivers it -- from `irpt-directory-search`'s CloudWatch logs if any request body was ever logged, else by the boundary's own contract (`_authz/served.py:641` hands the compute the raw event; cite how `served.py` itself reads `queryStringParameters`/`body` for the FIRM_BINDING check at `:614-616`, which is the shape the entry must share). The captured or constructed event is committed as a fixture with its sha256 (no token, no real e-mail: the fixture carries the shape and placeholder identifiers).
- (b) THE FIX, MINIMAL: `directory/entry.py` reads `q` and `limit` from `queryStringParameters` (falling back to nothing else -- a top-level `q` on a 2.0 event is not a query) and `selection` from the parsed `body` (JSON; base64-decoded when `isBase64Encoded`; a malformed body is a POLICY refusal through the boundary's existing refusal shape, never an UNEXPECTED); `limit` bounded as `handler.py` already bounds it. ONE helper, used by both call sites, no change to `handler.py`'s contract, no change to `_authz/`. Every `directory/` test that passed a top-level `q`/`selection` is REWRITTEN to the 2.0 shape -- the test that asserted the old shape is the defect's own witness and is not kept.
- (c) THE PROOF: the `directory/` suite passes (`n of n`); a unit test over the REAL entry with the committed 2.0 fixture reads `search` honouring `q` and `limit` (a query that matches exactly one projection member returns 1, `limit=2` over a wider match returns 2) and `resolve` honouring `selection` (a selection that names a projected member resolves it); the NEGATIVE CONTROL: the pre-fix entry (read from git at `9f72f4d6a4`, run in memory) on the same fixture returns the unfiltered first-20 and UNSUPPORTED -- the false behaviour DEMONSTRATED, not described.
- (d) THE STAGING CONTRACT: `holdings/stage.py --check`-style membership for the directory root (`lambda-source-map.json`'s `irpt-directory-search` entry) still resolves every member at HEAD after the edit (`m of m`; the entry file is a member, its sha moves -- that is the point, and the manifest field is NOT hand-edited: the build re-derives it, W1-S31/S89's bar).

---

## DELIVERABLE

the entry fix and rewritten tests; the fixture; `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rtf_11.py`, `IB-rtf-11_R68-AC1_battery_output.txt`, `directory-entry-reads-payload-2-0.result.md`; the proof instance.

---

## BOUNDS

- The ONLY code touched: `infra/aws/lambda/investor-reporting/directory/entry.py`, its tests and one fixture under `directory/tests/`; `handler.py`, `_authz/`, `served.py` and every other route are NOT edited; no deploy, no manifest hand-edit, no Terraform. A defect found in `handler.py`'s own reading of the shape is a ROW, not a fix.
- **THE FORWARD-LOOKING-CRITERION BAR (round-3 analysis s.4, ADOPTED; R-68's shape):** no criterion on this face certifies what a future event WILL find or load; every claim about a run or a served artifact is bound to that artifact's CONTENT HASH (`VersionId`/`ETag`/`sha256`/`CodeSha256`/`git hash-object`) READ AT THE EVENT -- a prediction made before the event is not evidence and a battery that prints one is refused at the drain.
- **S56 (ARMED, the CVO's): EVERY line citation in this order's JUDGMENT RECORD and result carries a vintage -- `path:line @ <commit-ish>` -- a bare `:NNN` is a defect the issuer greps for at the drain (`0 of N` bare citations is the bar).** CLAUDE.md Rule 22: a citation without a vintage is not a citation.
- **S73 (the `comp-iam roles` snapshot with no vintage) is an ESTATE-INSTRUMENT defect routed elsewhere and does NOT ride this order:** a live-plane IAM read here uses `comp-iam live` or `.tools/aws iam get-role`, never `comp-iam roles`.
- **R-40 (standing bar, `1.0.0_SA_CTO` @233f5fd5e4):** every criterion whose subject is a RUN or a PRODUCED ARTIFACT records that artifact's CONTENT HASH (`git hash-object`, `sha256sum`, or the service's own digest such as `ETag`/`CodeSha256`) beside its run id in the instance, and is graded against the hash; a label, a path or a timestamp ordering is not an identity.
- **Surprises:** ONE row per premise that does not hold, path that is not where this face says, result the invocation does not produce, or capability you lack -- at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W1-S<k>` with k continuing above the file's highest `W1-S<k>` (W1-S32 today) at your worktree's HEAD (read it first; the file holds SEVERAL fenced json blocks -- append your object INSIDE THE FIRST fence's array at its end, the file's PREVAILING line endings (CRLF today, W4-S44), UTF-8 written explicitly, no json fence marker inside any row's text, `surfaced_at` a full ISO timestamp, omit `disarm_owner` on an INERT row and name a SEAT SERIAL, never a cell, when ARMED (R-42)); then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
- **THE READER-CENSUS BAR (round-5 analysis s.1, the mirror of the never-widen writer census):** FLIPPING A SHARED FLAG OR FIELD NEEDS ITS READER CENSUS -- N readers, N rules read, N printed -- before the flip is called safe; a write asks who else SETS this, a flip asks who else BELIEVES this. NON-APPLICATION: a value with exactly one reader, which the same census proves.
- **BLOB PINS ARE WRITTEN `blob <hash>` (round-5 analysis s.4):** `@<hash>` means commit-ish in this estate; a blob pinned as `@<hash>` reads like a missing file at the grader. No `memory/` path is cited on this face (S78: a fresh worktree cannot resolve one); every rule this face relies on is stated inline.

### Bounds every order carries (decomposition v0.2 s.8, verbatim)

1. **NO LIVE VENDOR CALL.** Endpoint, verbatim: *"NO LIVE VENDOR CALL is authorized by this document -- availability is not authorization; a live YCharts, Black Diamond or Orion call needs Andrew's explicit per-use word."* The same bound covers the mailbox read and a YCharts login or session capture. A cell that carries a live arm proves its MECHANISM against recorded fixtures through a transport stub with a difference control; the live arm is an express qualification read by the CTO at L10 on Andrew's per-use word, never something this order does.
2. **NO MONITOR, ALARM, SNS OR SES SEND.** Nothing in this project notifies anyone. A scheduler this project creates is the product's own trigger and is applied `DISABLED` where its first fire would be a vendor call.
3. **CROSS-FIRM, both shapes.** Per-firm prefixes + IAM conditions in the shared bucket; the FIRM's own bucket for directory and holdings data; the `FirmDestinationPolicy`; the firm fixed from the sender's domain at ingestion and immutable after; Global GRANTED to an Opal principal, never to a firm one; no new all-firm financial aggregate.
4. **Deploys (NEVER-2, NEVER-9).** `.tools/safe-apply.sh` only, from a root whose state key is this cell's; a change-management entry opened at the start (`python .tools/deploy_ledger.py open ...`) and its OPEN sentinel `org/critical_paths/.open_deploys/<slug>.json` COMMITTED IMMEDIATELY (row W3-S4's rule) before the act; the entry closed at completion and COMMITTED BEFORE the reads that grade the act; served bytes verified as `CodeSha256` against the built zip, never by filename; `aws lambda update-function-code` never; `.tools/terraform.exe` is provisioned in your worktree by the issuer -- use it by that path, never a PATH substitute (a substitute re-pins remote state); every provider cache was purged estate-wide, so `init` each root you plan with the vendored binary.
5. **Andrew's four fixed constraints are not build choices:** the BDAPI-with-Kimi runner STYLE with NO OTP branch; the firm from the sender's domain at ingestion gated to enumerated destinations; the multitenant `api/scoped/` layout; terminated clients STAY VISIBLE under entitlement. And the endpoint's: units are part of a number's meaning; unsupported positions are never silently removed; no PUT of global YCharts preferences; no vendor call in render or preview; missing history is an answer, not an empty state; the narrative states contemporaneity and never causes; model targets never masquerade as observed holdings; THE YCHARTS MECHANISM IS FIXED (v0.9: K3 capture on the dedicated host -> fenced publication -> browserless Lambda REST replay).
6. **No credential in any artifact, log, fixture or commit.** Secrets are read by NAME at runtime; a recorded fixture is scrubbed before it is committed; signed URL parameters are never logged; a `describe-secret` prints version state, never a value.
7. **No served output is touched.** The 28 existing CloudFront behaviors, the 14 pre-existing scoped routes, this project's 11 live routes and every existing bucket, table and Lambda are read, never edited, except where THIS order's cell says it CHANGES or ADDS a resource.
8. **The spec is FROZEN mid-round.** A premise that does not hold, a path that is not where this face says, a result the invocation does not produce, a capability you lack: ONE row at `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`, id `IRPT_BCKEND-W<your slot>-S<k>` (a DS lane mints `IRPT_BCKEND-D-S<k>`), per `org/surprise_channel/schemas/investigation_item.schema.json`, inside the fenced json array, appended never edited, k continuing your slot's round-1 numbering; then keep working. Never edit this face, never widen the order, never fix a neighbouring defect.
9. **Every invocation terminates.** You run each named invocation under `timeout`; rc 124 IS the recorded output, retried once at most.
10. **Every `.py` edit passes `.tools/commit-gate.sh`.** Python 3.12 (`Python312` first on PATH; bare `python` may resolve to 3.14 without PyYAML). ASCII only in production code, logs and AWS names (`OK:`/`WARN:`/`ERROR:`/`SKIP:`/`BLOCKED:`).
11. **Scratch** is `<your worktree>/.scratch/` only.
12. **NO SELF-WRAPPING HARNESS AS EVIDENCE (round-1 lesson, rows W1-S10, S24).** An arm's subject is the REAL artifact -- the real route file, the real dispatcher, the deployed function, the served object -- never a copy the battery wraps, patches or re-registers itself. A census reads the real population and prints its denominator; a `0 of 0` is printed as VACUOUS, never as a pass. Every manifest of hashes a cell writes is re-derived by its battery every run (row W3-S9).
13. **TYPED, ISSUED IDENTIFIERS AT EVERY BOUNDARY (round-1 lesson, rows W2-S9/S11, W1-S7, W3-S12).** Firm, client, relationship, account, report, export and job ids cross a function boundary as ISSUED opaque ids of a declared type; a display name, an e-mail address, a raw upstream key or a request-controlled firm token is refused at the boundary, and a refusal never echoes the refused value.

---

## ACCEPTANCE

<criterion id="R68-AC1" cell_refs="IB-rtf-11"><invocation>timeout 900 py -3.12 org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/battery_ib_rtf_11.py</invocation><expect>IBR68-DIRECTORY-ENTRY-READS-PAYLOAD-2-0</expect></criterion>
**`R68-AC1` -- PASSES BY OUTPUT:** (a) the routes and their payload versions `n of n`, the fixture's sha256; (b) the fix committed, one helper, both call sites; (c) suite `n of n`, the 2.0 fixture honoured (counts printed), the pre-fix entry's false behaviour demonstrated on the same fixture; (d) the staging membership `m of m` resolved at HEAD. The token prints only when every arm holds; the battery re-derives every count each run.

<criterion id="R68-AC2" cell_refs="IB-rtf-11" judgment="true"/>
**`R68-AC2` -- JUDGMENT, RECORDED AND NOT SELF-GRADED.** State for `3.0.0_SA_CVO`: how a suite that passed 100 percent never exercised the deployed event shape (the harness constructed its own events), and what a route's acceptance instrument must carry so the shape the integration sends is the shape the test sends -- one fixture per route captured from the integration's own contract, never hand-built. No verdict. Every line citation carries `@<commit-ish>`.

<expected_criteria>R68-AC1, R68-AC2</expected_criteria>

<placeholders>NONE</placeholders>

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-11.the-directory-entry-reads-the-payload-2-0-event-shape-the-integration-sends.md
infra/aws/lambda/investor-reporting/directory/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>


<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> v0.6, cell `IB-rtf-11` (s.R6.8 -- the mid-round addition on rows S90/S92).
<owned_cells>IB-rtf-11</owned_cells>
</decomp_ref>


<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- nothing scheduled or fired.
comp-iam: DECLARED-NOT-APPLICABLE -- code and tests only; no grant, no deploy.
comp-adversary: DECLARED-NOT-APPLICABLE at the cut; the assignee's instrument at report time.
lane: the `<paths>` block above IS the grant (RULING 1 @9ef9a40aae) plus the two tree-convention grants (`deliverables/<serial>/`, this order's own face). A path you need that is not listed is a BLOCKING row, never an override.
</preflight>


<proof_of_spec>
Criterion ids minted at cut: R68-AC1, R68-AC2. Instance at
`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtf-11.the-directory-entry-reads-the-payload-2-0-event-shape-the-integration-sends.proof_of_spec.json`
(the TASK ORDER'S OWN BASENAME stem), per `org/standards/PROOF_OF_SPEC.schema.json`: one acceptance row per id, `criterion_verbatim` the spec's words, `invocation` the exact command, `output_evidence` the verbatim deciding excerpt, `denominator` beside every count, `expect` carried from this face, and -- R-40 -- the content hash of every produced artifact the row grades, EACH PINNED TO THE COMMIT THAT CARRIED IT (commit the battery, its output and the result BEFORE the instance; `PENDING-THIS-COMMIT` is a ONE-SHOT sentinel); a blob pin is written `blob <hash>`; a judgment row under `UNVERIFIABLE-BY-INSTRUMENT` with `status_reason` naming the CVO. Validate with `py -3.12 .tools/proof-of-spec-check.py org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~1/IRPT_BCKEND.TO-IB-rtf-11.the-directory-entry-reads-the-payload-2-0-event-shape-the-integration-sends.proof_of_spec.json --governing-order org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-rtf-11.the-directory-entry-reads-the-payload-2-0-event-shape-the-integration-sends.md` BEFORE the complete flip; rc 0 AND R68-AC1 PASS-by-output, then flip this order's `<status>` to `complete` and commit instance and flip together. A FAIL row leaves the order open and is your final report on it.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape (branch tip, each criterion with its deciding output line and denominator, proof-of-spec-check rc, every row id filed with its class, anything you could not do and why).
