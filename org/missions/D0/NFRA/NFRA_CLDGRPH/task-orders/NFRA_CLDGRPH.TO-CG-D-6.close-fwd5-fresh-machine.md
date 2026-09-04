# TO NFRA_CLDGRPH.TO-CG-D-6 -- CLOSING PASS, FWD-5 EXERCISED: a MACHINE that has never held the graph -- a fresh checkout with the local DB path ABSENT, proven by `ls` BEFORE the ask -- asks and is answered on the FIRST try; the same question's answer from a laptop seat is compared at the drain by the issuer

<to_id>NFRA_CLDGRPH.TO-CG-D-6</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO = the COO handing this order to slot ~2 by CONTINUING the same subagent after TO-CG-D-3 (the thin client, your own second order) is terminal and merged and CLOUD is merged into your branch (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf; the CTO's round-3 analysis @2dd381d969 orders the closing pass CG-s-7, CG-x-1, CG-x-5, CG-x-2, CG-x-4, CG-x-8, then CG-s-8 -> CG-x-7 last), slot ~2's THIRD order; the closing pass for FWD-5, released by CG-s-5 + CG-s-6 DONE. PREMISE RE-GROUND at hand-off: `bash .tools/comp-kuzu "MATCH (n) RETURN count(n) AS nodes"` answers with a VINTAGE line from your worktree; if not, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop (the READER is a fresh checkout on this device; R12) · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-5; acceptance 5) · **Decomp cell:** `CG-x-5` (v0.3, this issuance; s.1b unchanged from v0.2 @`70918d5d2b`) · **Lane:** this order's deliverables only · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~2`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.**
- **Surprise = ONE ROW, never a message** (id `NFRA_CLDGRPH-W2-S<k>`, `<k>` continuing your own W2 numbering; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** create, copy, download or rebuild a local graph in this worktree (a fresh machine is a READER, not a builder); run any engine; edit code; write to S3; non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free.

## THE CELL (verbatim, decomposition s.1b)

> **CG-x-5** | FWD-5 | DONE WHEN: EXERCISED -- a machine that has never held the graph has asked and been answered | the act: a machine with no `kuzu_nessie_db` on disk (site Z, or a fresh checkout with the path absent, proven by an `ls`) asks and is answered on the first try | status OPEN | lane `0.8.0_AE_CloudComp` | placement laptop (the READER may be site Z; the seat is laptop) | depends_on: CG-s-5, CG-s-6 -> DONE | **closes on:** the absence of the local DB proven before the ask, then the answer; same answer as a laptop seat for the same question

**PRD acceptance 5 (verbatim):** *"A fresh machine is a reader, not a builder. A machine that has never held the database asks and gets the same answer as everyone else on its first try. (FWD-5)"*

## MEASURED BY THE ISSUER AT THE CUT

- **Your worktree IS the fresh checkout:** `git worktree add -b wk-NFRA_CLDGRPH-2 <path> CLOUD` carries no gitignored artifact, so `infra/aws/globgrph/kuzu_nessie_db` (and its `._refresh_status.json`, `.fallback.jsonl`, `.rebuild.tmp`, `.kuzu_nessie_load.lock` siblings) are ABSENT by construction. Prove it before the ask; the proof is the `ls` with its rc and a census `ls infra/aws/globgrph/ | grep -c kuzu_nessie_db` -> 0.
- **The "same answer as a laptop seat" half is the ISSUER'S at the drain**, not yours: `2.0.0_SA_COO~A` runs the identical Cypher from the main workspace (a laptop seat that still holds the local graph until CG-s-8 retires it) within the same hour and records both answers side by side in `org/missions/D0/NFRA/NFRA_CLDGRPH/ledger/STEP_LOG.2.0.0_SA_COO~A.round4.json`; the CVO grades D6-AC4 on that pair. You record YOUR answer with its vintage line; the vintage makes the two comparable (two readers of one served artifact at one vintage MUST agree; readers at different vintages are compared on the vintage line, not the rows).
- **The question, fixed by the issuer:** *"How many CloudNodes of each node_type does the estate hold?"* -- Cypher: `MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC, t` (deterministic ordering). Run it ONCE through `bash .tools/comp-kuzu --json "<cypher>"` and once in table mode; the `--json` output is the comparison object.

## DELIVERABLE -- in this order

1. **Prove the absence FIRST** (absence, then ask): `ls -la infra/aws/globgrph/ | grep -c kuzu_nessie_db` and `ls -d infra/aws/globgrph/kuzu_nessie_db; echo rc=$?` quoted with `date -u +%FT%TZ` before each.
2. **ASK ONCE, FIRST TRY:** `bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/fresh_ask.sh` (yours): timestamp, the absence reads (printed as `LOCAL_DB_BEFORE=absent|present`), then `comp-kuzu --json "<cypher>"` with stderr captured (the VINTAGE line), then the table-mode run; prints `FIRST_TRY_RC=<rc of the first json call>`; then the absence reads again (`LOCAL_DB_AFTER=`). A first-try failure is recorded as such (rc, error text) and is a criterion FAIL, never a retry-until-green.
3. **The record** `CG-x-5.fresh-machine.result.md`: one fenced JSON block `{machine: "worktree <abs path> on <hostname>", local_db_present_before: false, local_db_present_after: false, question, cypher, first_try_rc, answer_json, vintage_line, laptop_seat_comparison: "ISSUER'S AT THE DRAIN -- see the round-4 step log"}` then the raw transcript. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D6-AC1" cell_refs="CG-x-5"><invocation>ls infra/aws/globgrph/ | grep -c kuzu_nessie_db</invocation><expect>^0$</expect></criterion>
`D6-AC1` -- NO LOCAL DB ON THIS MACHINE, proven before the ask.

<criterion id="D6-AC2" cell_refs="CG-x-5"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/fresh_ask.sh</invocation><expect>FIRST_TRY_RC=0[\s\S]*VINTAGE: Built from the estate as of</expect></criterion>
`D6-AC2` -- ANSWERED ON THE FIRST TRY, with the vintage line.

<criterion id="D6-AC3" cell_refs="CG-x-5"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/fresh_ask.sh | grep -E '^LOCAL_DB_(BEFORE|AFTER)='</invocation><expect>LOCAL_DB_BEFORE=absent[\s\S]*LOCAL_DB_AFTER=absent</expect></criterion>
`D6-AC3` -- THE READER DID NOT BECOME A BUILDER: absent before, absent after.

<criterion id="D6-AC4" cell_refs="CG-x-5" judgment="true"/> `D6-AC4` -- SAME ANSWER AS A LAPTOP SEAT: your `--json` answer and its vintage line, set beside the issuer's laptop-seat answer for the identical Cypher (the round-4 step log). You record your half with NO verdict; `3.0.0_SA_CVO` grades the pair at L9.

<expected_criteria>D6-AC1, D6-AC2, D6-AC3, D6-AC4</expected_criteria>

## SURFACES

`.tools/comp-kuzu` + `infra/aws/globgrph/kuzu_cli.py` + `infra/aws/globgrph/projection_client.py` (READ; the client) · `infra/aws/globgrph/` (READ: the absence census) · PRD ENDPOINT FWD-5 (READ).

## BOUNDS

- **No local graph is created by any means; no engine; no code change; no S3 write.**
- **One first-try ask.** A failure is recorded, never retried into a pass.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-6.close-fwd5-fresh-machine.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> v0.3 (this issuance; s.1b unchanged from v0.2 @70918d5d2b), cell CG-x-5 (the closing pass for FWD-5).
<owned_cells>CG-x-5</owned_cells>
Read-dependencies, NOT claimed: CG-s-5 (TO-CG-D-2), CG-s-6 (TO-CG-D-3). Downstream, NOT yours: CG-s-8 (R7: the retirement STARTS when a fresh machine has been answered -- this order is that release; it is handed LAST).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria bind this face's BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or grant is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D6-AC1`..`D6-AC4`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-6.close-fwd5-fresh-machine.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D6-AC1,D6-AC2,D6-AC3,D6-AC4` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D6-AC1` and `D6-AC3` are the controls that must be able to FAIL. `D6-AC4` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE THE ASK: `bash .tools/comp-kuzu --schema` (read only). No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-3's drain).**
