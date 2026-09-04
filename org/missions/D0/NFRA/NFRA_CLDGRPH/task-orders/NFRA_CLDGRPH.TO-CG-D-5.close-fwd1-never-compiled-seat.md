# TO NFRA_CLDGRPH.TO-CG-D-5 -- CLOSING PASS, FWD-1 EXERCISED: a seat that has NEVER run a graph tool asks ONE wiring question through the client and is answered -- the asker, the question, the answer, its time-to-answer, the vintage line, and the proof that NO build ran, all on the record

<to_id>NFRA_CLDGRPH.TO-CG-D-5</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO = the COO handing this order to slot ~3 by CONTINUING the same subagent after TO-CG-D-3 (CG-s-6, the thin client) is terminal and merged, and after CLOUD is merged into your branch (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~3's SECOND order; the closing pass for FWD-1, released by CG-s-5 + CG-s-6 DONE. PREMISE RE-GROUND at hand-off: `infra/aws/globgrph/projection_client.py` exists at your HEAD and `bash .tools/comp-kuzu "MATCH (n) RETURN count(n) AS nodes"` answers with a VINTAGE line; if not, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-1; acceptance 1) · **Decomp cell:** `CG-x-1` (v0.2 @`70918d5d2b` s.1b) · **Lane:** this order's deliverables only (no code changes) · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~3`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~3;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~3 <0.9.0_WK_NFRA_CLDGRPH~3@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/`.**
- **Surprise = ONE ROW, never a message** (the investigation file named below; id `NFRA_CLDGRPH-W3-S<k>`, `<k>` continuing your own W3 numbering; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** run any rebuild, refresh, `kuzu_nessie_load`, `--mode`, `--force`, or any engine (the point of this order is that none is needed); edit code; write to S3; an alarm/monitor; non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free.

## THE CELL (verbatim, decomposition v0.2 s.1b)

> **CG-x-1** | FWD-1 | DONE WHEN (PRD ENDPOINT, verbatim): EXERCISED -- someone who has never run a graph tool has asked and been answered | the act: a named seat with no graph history asks one wiring question through the client; the answer, its time-to-answer and the absence of any refresh step recorded | status OPEN | lane `0.8.0_AE_CloudComp` | placement laptop | depends_on: CG-s-5, CG-s-6 -> DONE | **closes on:** the record shows the asker, the question, the answer, the vintage line, and that no build ran (process table / log negative control)

**PRD acceptance 1 (verbatim):** *"A never-compiled seat gets an answer. Someone at a seat that has never run a graph tool asks how two things are connected and gets the answer in the time an ordinary lookup takes, with no refresh step. (FWD-1)"*

## MEASURED BY THE ISSUER AT THE CUT

- **YOU are the never-compiled seat.** A spine-v3 worker starts with fresh context in a fresh worktree from CLOUD; the worktree carries no `infra/aws/globgrph/kuzu_nessie_db` (gitignored; never checked out); your serial has never run a graph tool (it did not exist before this round). The "no graph history" claim is PROVEN, not asserted: `ls infra/aws/globgrph/kuzu_nessie_db` -> absent (rc 2); `python .tools/comp-find '0.9.0_WK_NFRA_CLDGRPH~3' org/mcp/agent_telemetry --limit 3` -> 0 hits (a worker writes no telemetry; the census is the denominator).
- **The client** (TO-CG-D-3, merged before you are continued): `bash .tools/comp-kuzu "<cypher>"` -> the answer table + `VINTAGE: Built from the estate as of ... UTC.` on stderr; `--json` for a machine-readable answer. It has no refresh flag by construction (D3-AC2).
- **The wiring question, fixed by the issuer so the CVO can grade the same one on every reader:** *"Which Lambda functions does the bd data bucket trigger?"* -- Cypher: `MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE e.edge_type='TRIGGERS' AND a.node_id CONTAINS 'opal-data-bd' RETURN a.node_id AS bucket, b.node_id AS target ORDER BY target` (the graph's dialect: `node_type`/`edge_type` are PROPERTIES, per `comp-kuzu --schema`). TO-CG-D-1 (slot ~1's first order, the digest-pinned rebuild + one real cloud derive) runs in parallel with your first order and is usually merged before this one is handed: if its derive has landed, this returns the three bd-pipeline targets (bd-allocation-processor, bd-gold-trigger, bd-silver-merge); if it has not, it returns 0 rows -- and a 0-row answer is STILL an answer for FWD-1 (the seat asked and was answered, with the vintage that says which graph answered). Record which; do not chase D-1.
- **"No build ran" has two witnesses:** (a) the process table around the ask (`ps -ef | grep -c -E 'kuzu_nessie_load|kuzu_incremental_refresh|derive_runner'` before, during and after -> 0 each; the `grep -v grep` discipline); (b) the client's source has no engine (D3-AC3 at your HEAD: `python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --enumerate 'ensure_fresh|kuzu_nessie_load|import kuzu' --limit 3` -> 0 hits).

## DELIVERABLE -- in this order

1. **Prove the premise:** the three absence reads above, quoted with their rc.
2. **ASK ONCE:** `bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/ask.sh` (yours): prints `ASKER=<serial>`, `QUESTION=<the sentence>`, the process-table count BEFORE, then runs the Cypher through `comp-kuzu` under `time` (wall seconds printed as `TIME_TO_ANSWER_S=<n.nnn>`), captures stdout+stderr whole, then the process-table count AFTER. One run is the record; a second run is permitted only to record variance and is labelled so.
3. **The record** `CG-x-1.never-compiled-seat.result.md`: one fenced JSON block `{asker, question, cypher, answer_rows, vintage_line, time_to_answer_s, procs_before, procs_after, client_source_engine_hits, local_db_present}` then the raw transcript of `ask.sh` in a fenced block. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D5-AC1" cell_refs="CG-x-1"><invocation>ls -d infra/aws/globgrph/kuzu_nessie_db 2>&1; echo "rc=$?"</invocation><expect>rc=[1-9]</expect></criterion>
`D5-AC1` -- THE ASKER HOLDS NO LOCAL GRAPH: the local DB path is absent in this worktree (a non-zero rc; the `2>&1` keeps the error text in the record, it does not hide it).

<criterion id="D5-AC2" cell_refs="CG-x-1"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/ask.sh</invocation><expect>TIME_TO_ANSWER_S=[0-9]+\.[0-9]+[\s\S]*VINTAGE: Built from the estate as of</expect></criterion>
`D5-AC2` -- THE ASK IS ANSWERED, timed, with the vintage line on the answer.

<criterion id="D5-AC3" cell_refs="CG-x-1"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/ask.sh | grep -E '^PROCS_(BEFORE|AFTER)='</invocation><expect>PROCS_BEFORE=0[\s\S]*PROCS_AFTER=0</expect></criterion>
`D5-AC3` -- NO BUILD RAN: the engine process count is 0 before and after the ask (the negative control; `ask.sh` prints both lines).

<criterion id="D5-AC4" cell_refs="CG-x-1"><invocation>python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --enumerate 'ensure_fresh|kuzu_nessie_load|import kuzu|--mode' --limit 3</invocation><expect>ENUMERATE: 0 hit\(s\)</expect></criterion>
`D5-AC4` -- NO REFRESH STEP EXISTS on the path the asker used (the client's source, at your HEAD).

<criterion id="D5-AC5" cell_refs="CG-x-1" judgment="true"/> `D5-AC5` -- "IN THE TIME AN ORDINARY LOOKUP TAKES": the measured `TIME_TO_ANSWER_S` against the estate's ordinary lookups (comp-find --corpus aws measured 11.55 s at L5; a `comp-read` under 1 s), and whether a 0-row answer (if D-1 has not landed) still exercises FWD-1. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>D5-AC1, D5-AC2, D5-AC3, D5-AC4, D5-AC5</expected_criteria>

## SURFACES

`.tools/comp-kuzu` + `infra/aws/globgrph/kuzu_cli.py` + `infra/aws/globgrph/projection_client.py` (READ; the client) · `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` ENDPOINT FWD-1 (READ).

## BOUNDS

- **No code change. No engine run. No S3 write.** The record is the deliverable.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-5.close-fwd1-never-compiled-seat.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-x-1 (s.1b; the closing pass for FWD-1).
<owned_cells>CG-x-1</owned_cells>
Read-dependencies, NOT claimed: CG-s-5 (TO-CG-D-2), CG-s-6 (TO-CG-D-3), both DONE before this order is handed.
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria bind this face's BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or grant is read or changed; the client reads one secret with the seat's existing credentials.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D5-AC1`..`D5-AC5`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-D-5.close-fwd1-never-compiled-seat.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D5-AC1,D5-AC2,D5-AC3,D5-AC4,D5-AC5` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D5-AC1`, `D5-AC3` and `D5-AC4` are the controls that must be able to FAIL. `D5-AC5` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE THE ASK: `bash .tools/comp-kuzu --schema` (the dialect; read only). No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-3's drain).**
