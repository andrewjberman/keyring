# TO DSGN_IRPTV1.TO-IV-e-87 -- the DRAFT never-widen pair for ONE signed-in FWD-1 trace on portal DEV under a READ-ONLY synthetic identity: the journey's hops and their requests read from the code, the identity and token bounds the CTO ruled, radius, branches, halves UNSIGNED -- it mints nothing and calls nothing

<to_id>DSGN_IRPTV1.TO-IV-e-87</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~47</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>12</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ruling msg 4198 (no closer; one signed-in FWD-1 trace cell under a read-only pair), on the state table `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~45/FWD_STATE_TABLE.json` | **Decomp cell:** `IV-e-87` (decomposition v12) | **outcome_ref:** FWD-1 | **depends_on:** IV-e-86 (drained).

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-47`; run everything from its root. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/`. The portal directory in your worktree is empty; read portal code at
the DEV tip with `git -C C:/dev/ajb_workspace/portal show 1cd1cf252eae0eee0d67cba4bde31630a71f975c:<path>` and
`git -C C:/dev/ajb_workspace/portal grep -n <pattern> 1cd1cf252eae0eee0d67cba4bde31630a71f975c -- <dir>`.

**THE CLIENT-DATA RULE (binding):** the PRD's FWD-1 names a client and an account. NEITHER enters anything you write: refer to them as "the named
client" and "the named account". No client name, account id, address, figure or screenshot in a record, the packet, a row, a commit or your report.

**The cell (`IV-e-87`).** FWD-1, the thread, has no whole signed-in trace after ten rounds (state table: APPLIED). The CTO ruled (msg 4198): one trace
cell, signed in, portal DEV, the one named client end to end, each hop recorded with what it returned, under a never-widen pair for a READ-ONLY
synthetic identity on dell2: **internal tier; the row LIST holds the one firm; a token of the run's length and at most 30 minutes; every request a
GET but the sign-in itself; the identity removed after `exp`; the trace records hop, status and counts, and no figure, account id or screenshot
enters the repository.** This cell DRAFTS that pair. A later cell runs it, after both halves sign.

Read first:
- FWD-1 in the PRD `org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md` (ENDPOINT, line ~44) and its ROUTE STRUCTURE section (~line 305);
- the precedent pair `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_TR1_THREAD_RERUN_PAIR.md` IN FULL, its CTO half
  `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_R2_TR1_THREAD_RERUN_CTO_HALF.md`, and the runner it cites
  (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~8/fwd1_runner/`): how the synthetic row is written and read back, how the
  token is minted and by whom, the cleanup order, the census before any hop, the zero-call read with its positive control;
- the earlier partial traces the state table cites for FWD-1 (its `evidence` list);
- the portal's Investor Reporting client: `src/pages/InvestorReporting/index.tsx`, `src/api/endpoints/investor-reporting.ts`, the header's client
  search and account picker, the Holdings and Performance tabs' loaders.

1. **The hops** (`FWD1_TRACE_HOPS.json`). Walk FWD-1's sentence as an ordered list of hops from "opens Investor Reporting" to the last thing the
   user reads. For EACH hop: {hop, what_the_user_does, requests: [{method, route, source: {file, line}}], records}. `requests` are the calls the
   page itself makes for that hop, read from the code at the DEV tip (route templates, never a filled id); `records` says what the run keeps for
   it, drawn only from `repo_carries` = a subset of {hop, status, counts, byte_length, sha256_prefix, code}.
   - Also `portal_commit`, `sign_in` (the requests that establish the session), `non_get_requests` (EVERY request in the hops that is not a GET).
   - **The read-only test.** The CTO's bound is "every request a GET but the sign-in itself". Several Investor Reporting reads are POSTs (the
     directory resolve is one). List EVERY non-GET request under `non_get_requests`: {method, route, is_sign_in, writes_server_side (true / false /
     NOT_ESTABLISHED), source: {file, line} of the HANDLER code that decides it}. A POST that only reads is a FINDING for the halves, who rule
     whether it is inside the pair; say so in the packet's section "What must hold". Never mark a request a sign-in to make it disappear.
   - `identity`: {tier, firm_list (the ONE firm token FWD-1's client belongs to, as the registry spells it), token_max_minutes, removed_after_exp,
     user_type}. Which clamps bind this identity on each route (the row LIST, as the precedent's census reads it) with file and line.
2. **The packet** (`FWD1_TRACE_READONLY_PAIR.md`), in the precedent's shape:
   - **## Measured at signing:** a table of what must be read at signing (live code identities of each Lambda the hops reach, the portal DEV tip
     and its CI, whether the DEV site serves that build, the synthetic row ABSENT). You fill what a repo read can fill and mark every live value
     `OWED AT SIGNING` with the instrument that reads it. You make no AWS call.
   - **## The identity:** the row key under `opal.invalid`, its fields, the token's claims and `exp` rule (run length + 5, never more than 30),
     memory-only, who mints it (the executor seat; no seat principal gains a key grant).
   - **## The act:** numbered steps: the NEVER-2 ledger and the per-worktree `.open_deploys/` read first; prechecks; write the row and read it
     back; the one-firm census before any hop; the hops in order with what each records; the page step if a browser session can be opened with
     the token and no new credential, recording canvas colour and counts only; cleanup (wait for `exp`, then delete, ConsistentRead ABSENT); the
     zero-write read with its positive control.
   - **## Blast radius:** a table, per key: what may change and the rollback. For a read-only identity the expected writes are the row itself and
     whatever a read route logs or caches; name each cache or audit write a hop's handler makes, from its code.
   - **## Branches:** every hop met; a hop refused (which code, what it means for FWD-1); a STOP before any hop; a non-GET request met.
   - **## What must hold before a run order cites this pair:** the runner and its pin, the executor seat, the open questions for the halves.
   - **## COO half** and **## CTO half**, each reading UNSIGNED.

**No AWS call, no token, no row, no request to any deployed service.** This cell reads the repository only.

<criterion id="IV87-AC1" cell_refs="IV-e-87"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r12/p12_round12.py" . IV87-AC1</invocation><expect>IV87-AC1 PASS</expect></criterion>
`IV87-AC1` -- the hops carry every request with its source line, every non-GET request is listed with what its handler writes, and the identity sits inside the ruled bounds. Base: FAIL.

<criterion id="IV87-AC2" cell_refs="IV-e-87"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r12/p12_round12.py" . IV87-AC2</invocation><expect>IV87-AC2 PASS</expect></criterion>
`IV87-AC2` -- the packet carries its sections with two UNSIGNED halves and no client identifier. Base: FAIL.

<expected_criteria>IV87-AC1,IV87-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No deploy and no push.** No AWS call, no vendor call, no secret read, no token mint, no request to a deployed service, no `bun install`, no
  download of any package, script or program.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. An edit outside the grant, a filled figure, or a client identifier in a committed file is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W47-S<k>`, with the real current UTC time.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-87.fwd1-trace-readonly-pair.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v12 (round 12), cell `IV-e-87`.
<owned_cells>IV-e-87</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV87-AC1,IV87-AC2. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~47/DSGN_IRPTV1.TO-IV-e-87.fwd1-trace-readonly-pair.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV87-AC1,IV87-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes, each criterion's last line, the hops in order with each one's requests, every non-GET request and what its handler writes, the identity, the open questions for the halves, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the packet scopes a later signed-in read of the Investor Reporting DEV routes; this cell reads the repository only.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call; the packet states that no seat principal gains a key grant.
comp-routes: RUN -- the hops name the routes the journey reads; no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: nothing is deployed; cache writes a read route makes are named in the packet's radius.
comp-adversary: RUN -- IV87-AC1 and IV87-AC2 FAIL at base (no record, no packet). CTO ruling msg 4198.
lane: the <paths> block IS the grant.
</preflight>
