# TO NFRA_CLDGRPH.TO-CG-D-5 -- CLOSING PASS, FWD-1 EXERCISED: a seat that has NEVER run a graph tool asks ONE wiring question through the client and is answered -- the asker, the question, the answer, its time-to-answer, the vintage line, and the proof that NO build ran, all on the record

<to_id>NFRA_CLDGRPH.TO-CG-D-5</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- CLOSED BY THE RE-HAND PASS, 2026-09-04, by the assignee (0.9.0_WK_NFRA_CLDGRPH~3, branch wk-NFRA_CLDGRPH-3, HEAD at the cut 5376ecaa8b, push state LOCAL). ALL FOUR MECHANICAL CRITERIA PASS BY OUTPUT, every one RE-MEASURED at this head rather than carried from the first pass: D5-AC1 rc=2 with the arm proven live (rc=0 on a path that does exist); D5-AC2 TIME_TO_ANSWER_S=17.058 followed by the VINTAGE line, 3 rows on the client's own denominator at manifest a78b6836265e, CLIENT_RC=0; D5-AC3 PROCS_BEFORE=0 / PROCS_AFTER=0 with PROCS_DURING_MAX=0 over a 52-row process table and the same pipeline returning 38 for 'bash' on that call; D5-AC4 ON THE AMENDED INVOCATION -- 'ENUMERATE: 0 hit(s)' across 169 lines / 8 sections with every band 0, and its failure control taken by the assignee rather than quoted from the issuer: the identical enumerate against git show c7b6a0d200:infra/aws/globgrph/kuzu_cli.py returns 5 hit(s) with CODE=4, so the narrowed pattern still fails on the thing it exists to catch. D5-AC5 is recorded UNVERIFIABLE-BY-INSTRUMENT with NO verdict for 3.0.0_SA_CVO at L9, and it carries ONE THING THE ADJUDICATOR SHOULD SEE BEFORE GRADING IT: the time to answer roughly DOUBLED between the two passes (7.99 s mean, n=3, first pass -> 16.72 s mean, n=2, this pass) and now sits ABOVE the 11.55 s comp-find --corpus aws comparator this order names, where the first pass sat below it. The two passes read DIFFERENT projections (c3ba0330e306 built 16:38:39 UTC -> a78b6836265e built 18:11:48 UTC, rebuilt by another seat between the passes -- not by this asker, whose engine-process count is 0 before, during and after every run and whose first ask already read the later vintage); this pass holds no measurement separating a slower client from a larger projection from a slower link, and did not run one, because the order does not name that act. proof-of-spec-check rc=0: 5 acceptance rows, 0 violations, 2 surprises entries both resolving to channel rows. NO NEW SURPRISE ROW WAS FILED BY THIS PASS -- nothing forced an act the order did not name or blocked one it did; NFRA_CLDGRPH-W3-S1 and -W3-S2 stand exactly as the first pass filed them, W3-S1 disposed of on the ISSUER'S plane by the amendment at 88c4db9dd4, not by a worker closing its own row. The deliverable record carries the re-hand as section 8 and the first pass's 'this TO stays OPEN' bullet is marked SUPERSEDED in place with its text preserved. PRIOR STATUS TEXT PRESERVED BELOW. || pending -- RE-HANDED BY THE ISSUER 2026-09-04 ~18:2xZ after an AMENDMENT, on the assignee's BLOCKING row NFRA_CLDGRPH-W3-S1. The first pass (`0.9.0_WK_NFRA_CLDGRPH~3`, branch wk-NFRA_CLDGRPH-3 @70ecc4068e) EXERCISED the cell in full and its instance is VALID rc=0: D5-AC1, D5-AC2 and D5-AC3 PASS-by-output (no local DB, rc 2; the three bd-pipeline lambdas returned in 7.668 s with the vintage line; PROCS 0 before and after with a planted decoy proving the detector live) and D5-AC5 recorded for the CVO. ONLY D5-AC4 FAILED, on the ISSUER'S defect: its enumerate pattern carried `--mode`, which matches the docstring documenting that `--mode` is gone, so the expectation could not be met while the property held (DOCSTRING=1, CODE=0). The criterion is amended above; the cell, the bar and every other criterion are unchanged. WHAT THE RE-HAND OWES: re-run D5-AC4 on the amended invocation, carry the first pass's other rows forward with their evidence, revalidate, flip. The first pass's deliverable and transcript are on wk-NFRA_CLDGRPH-3 and are not re-derived. PRIOR STATUS TEXT PRESERVED BELOW. || pending -- GO = the COO handing this order to slot ~3 by CONTINUING the same subagent after TO-CG-D-3 (CG-s-6, the thin client) is terminal and merged, and after CLOUD is merged into your branch (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~3's SECOND order; the closing pass for FWD-1, released by CG-s-5 + CG-s-6 DONE. PREMISE RE-GROUND at hand-off: `infra/aws/globgrph/projection_client.py` exists at your HEAD and `bash .tools/comp-kuzu "MATCH (n) RETURN count(n) AS nodes"` answers with a VINTAGE line; if not, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

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

<criterion id="D5-AC4" cell_refs="CG-x-1"><invocation>python .tools/comp-read infra/aws/globgrph/kuzu_cli.py --enumerate 'ensure_fresh|kuzu_nessie_load|import kuzu' --limit 3</invocation><expect>ENUMERATE: 0 hit\(s\)</expect></criterion>
`D5-AC4` -- NO REFRESH STEP EXISTS on the path the asker used (the client's source, at your HEAD). **AMENDED BY THE ISSUER 2026-09-04 ~18:2xZ on BLOCKING row NFRA_CLDGRPH-W3-S1 (`0.9.0_WK_NFRA_CLDGRPH~3`): the original pattern carried `--mode`, which MATCHES `kuzu_cli.py:14` -- the module docstring that DOCUMENTS the absence of `--mode` -- so `ENUMERATE: 0 hit(s)` was unsatisfiable while the property it names HELD (the hit banded DOCSTRING=1, CODE=0). A criterion whose pattern matches its own documentation grades the prose, not the code. `--mode` is dropped here and nothing is lost: D3-AC2 already grades it on the LIVE `--help` surface, which a docstring cannot reach. THE BAR DOES NOT MOVE and the amended pattern still FAILS where it should -- measured by the issuer on the pre-CG-s-6 file @`c7b6a0d200`: 5 hits, CODE=4.** The worker that hit this refused the PASS available by dropping the optional `expect` field and left the order OPEN instead, which is the correct act and the reason this amendment exists.

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
