# TO DSGN_IRPTV1.TO-IV-e-88 -- the FWD-1 trace pair REVISED to the CTO's four rulings, and the RUNNER built at a pin with offline tests -- nothing is minted, written or called

<to_id>DSGN_IRPTV1.TO-IV-e-88</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~48</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>superseded; by 1.0.0_SA_CTO~DELL2's ROUND-13 ANALYSIS @72e8e2bb59 section 2 item 1 (msg 4341): the API-runner trace is DROPPED, no runner, identity or pair is built; the worker was stopped minutes after spawn with no commit</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>13</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's rulings msg 4336 on the draft pair (IV-e-87, drained @709d1be19c) | **Decomp cell:** `IV-e-88` (decomposition v13) | **outcome_ref:** FWD-1 | **depends_on:** IV-e-87 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-48`; run everything from its root. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~48/`. Portal code is read at the DEV tip by content:
`git -C C:/dev/ajb_workspace/portal show 1cd1cf252eae0eee0d67cba4bde31630a71f975c:<path>`.

**THE NAMED CLIENT STAYS OUT (binding, by the pair's own terms):** the PRD's FWD-1 names a client and an account. Write "the named client" and "the
named account". No client name, account id, address, figure or screenshot in the runner, its tests, the packet, a record, a row, a commit or your
report. The runner takes the client's search text and the account choice as ARGUMENTS at run time and never stores or prints them.

**The cell (`IV-e-88`).** The draft pair (`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/FWD1_TRACE_READONLY_PAIR.md` and
`FWD1_TRACE_HOPS.json`) found the journey is not GET-only. The CTO ruled all four points (msg 4336) and withdrew "every request a GET":
**the trace makes the calls the page makes, no others, each named in the radius.**
1. `POST /selections`: IN. One immutable, content-addressed item per selection, named in the radius as a kept test artifact, with its key.
2. `POST /directory/resolve`: IN, as a read.
3. `GET /performance`: not out by default. Name from the portal source which route the Performance tab calls today for this firm. If it is
   `/performance`, it is IN, ONCE (FWD-1's last walk failed exactly there); the radius names the cache write and the one vendor authorization.
   If the tab calls the reporting series route, trace that.
4. API hops only; `PAGE-NOT-RENDERED` is stated. The rendered walk is a second act, asked of the laptop's `/ui-walk` once the hops read clean.

Read first: the draft pair and hops IN FULL; the precedent runner `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/`
(the lines the draft pair's section "What must hold" cites: `put_row`, `read_row`, `mint_token`, `call`, `wait_past_exp`, `cleanup`,
`data_refresh_zero_calls`, the precheck) and its tests; the precedent pair
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_TR1_THREAD_RERUN_PAIR.md`.

1. **Ruling 3, answered from the source.** Read the Performance tab's loader at the DEV tip and the firm-installed sources the draft cites, and say
   which route the tab calls for the named firm: `performance_route` {route, source: {file, line}, in_trace}. If both the reporting series routes and
   `/performance` are called, say so, and both are traced, `/performance` exactly once.
2. **The runner**, in `fwd1_trace_runner/` in your folder: a NEW script modelled on the precedent (copy what you reuse; do not import from or edit
   another seat's folder). It:
   - takes the firm token, the client search text, the account choice, the API host and the token length N as arguments; refuses N over 30;
   - writes the synthetic row, reads it back, mints ONE token with `exp` = `iat` + N minutes, memory-only;
   - runs the one-firm census before any hop, then hops H2 to H7 in the draft's order, sending ONLY the page's own requests;
   - refuses, BEFORE sending, any non-GET request whose route template is not one of exactly two: selections and directory/resolve;
   - sends `/performance` at most once per run, if ruling 3's answer puts it in the trace;
   - records per hop: hop, status, code, counts, byte_length, sha256_prefix. Never a body, a figure, an id or the search text;
   - records `PAGE-NOT-RENDERED` for the page step;
   - on every branch: waits until `exp` has passed, then deletes the row and reads it back ABSENT; then the zero-call read with its positive control;
   - makes NO network or AWS call at import, and none in its tests.
3. **Tests** beside it (pytest, offline, every client and clock injected or stubbed): a POST outside the allow-list is refused before it is sent;
   N over 30 is refused; the row is deleted only after `exp` (a delete attempted before `exp` fails the test); `/performance` is sent at most
   once; a refused hop still runs cleanup; nothing the runner writes to its trace file contains the search-text argument.
4. **Pair v2** (`FWD1_TRACE_PAIR_v2.md`): the draft's sections, revised, plus **## Rulings applied** (msg 4336, each of the four, and how the text
   changed). The blast radius names: the synthetic row; one selections item per distinct selection with its key shape, KEPT; the performance cache
   write and the one vendor authorization if `/performance` is in the trace; every other key the hops' handlers touch. The page step reads
   `PAGE-NOT-RENDERED`. "What must hold" names the runner at YOUR commit, the executor seat as proposed, and every `OWED AT SIGNING` item with its
   instrument, unchanged from the draft unless a ruling settled it. Both halves read UNSIGNED.
5. `RUNNER_RECORD.json`: {runner_file, tests_file, tests {passed, failed}, post_allow_list, exp_max_minutes, guards {...four booleans the check
   names...}, performance_route, reused_from_precedent: [{function, their_line}]}.

**No AWS call, no token, no row, no request to any deployed service, in this cell.** The runner is built and tested offline.

<criterion id="IV88-AC1" cell_refs="IV-e-88"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r13/p13_round13.py" . IV88-AC1</invocation><expect>IV88-AC1 PASS</expect></criterion>
`IV88-AC1` -- the runner's offline tests pass, its POST allow-list is exactly the two ruled routes, its token cap is 30 minutes and its four guards are tested. Base: FAIL.

<criterion id="IV88-AC2" cell_refs="IV-e-88"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r13/p13_round13.py" . IV88-AC2</invocation><expect>IV88-AC2 PASS</expect></criterion>
`IV88-AC2` -- pair v2 applies the four rulings, names the Performance route from the source, and carries two UNSIGNED halves and no client identifier. Base: FAIL.

<expected_criteria>IV88-AC1,IV88-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No AWS call, no vendor call, no secret read, no token mint, no request to a deployed service, no `bun install`, no
  download of any package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W48-S<k>`, with the real current UTC time; append as BYTES, never re-encode
  the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~48/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~48/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-88.fwd1-trace-runner-and-pair-v2.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v13 (round 13), cell `IV-e-88`.
<owned_cells>IV-e-88</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV88-AC1,IV88-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~48/DSGN_IRPTV1.TO-IV-e-88.fwd1-trace-runner-and-pair-v2.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV88-AC1,IV88-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes, each criterion's last line, which route the Performance tab calls and the line that shows it, the runner's allow-list and guards with the test that proves each, what you reused from the precedent, the radius table's rows, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- a runner that will later sign in and read the Investor Reporting DEV routes; this cell builds and tests it offline.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call here; the pair states that no seat principal gains a key grant.
comp-routes: RUN -- the runner's hops name the routes the page calls; no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: RUN -- the pair's radius names the performance cache write, if that route is in the trace.
comp-adversary: RUN -- IV88-AC1 and IV88-AC2 FAIL at base (no record). CTO rulings msg 4336.
lane: the <paths> block IS the grant.
</preflight>
