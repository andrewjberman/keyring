# TO NFRA_CLDGRPH.TO-CG-D-8 -- CLOSING PASS, FWD-7 EXERCISED: after the local copy is switched off, TWO MACHINES ask the SAME question inside ONE MINUTE and receive IDENTICAL answers with IDENTICAL vintage lines, with no local DB on either machine (proven); this closes CG-s-8

<to_id>NFRA_CLDGRPH.TO-CG-D-8</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~2</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>complete -- CG-x-7 EXERCISED 2026-09-09 by 0.9.0_WK_NFRA_CLDGRPH~2 on branch wk-cldgrph-2-d7, work commit d25fcb88e5, push state LOCAL (never pushed, never merged, never rebased). FWD-7 IS EXERCISED: two machines asked the fixed question 2.1 s apart and returned BYTE-IDENTICAL 58-row answers under ONE vintage (2026-09-09T12:23:34.893879+00:00, manifest 83c6e1335f43, prefix projection/2026-09-09T12:23:34.893879+00:00/), by TWO DIFFERENT TRANSPORTS -- the laptop over public HTTPS with a Secrets-Manager bearer, the gateway host i-07dccb1615503ac99 over plaintext HTTP to the in-VPC Cloud Map name. ALL FIVE CRITERIA TERMINAL: D8-AC1 ROWS_EQUAL=true with WINDOW_S=4.229 on one clock (the gateway's AWS-clock stamp falls INSIDE that window and its own date agrees to 4 ms); D8-AC2 exactly 1 distinct vintage, with the filter shown able to return 2; D8-AC3 0 in the worktree, carried BESIDE the measurement that can actually fail -- MAIN_WORKSPACE_LOCAL_DB_COUNT=0 (grep rc=1) at 2026-09-09T14:14:15Z, THIS WORKER's independent read by absolute path over a directory proven to exist and hold 69 entries with a positive control of 2, agreeing with the issuer's step-log row 20 rather than relying on it; D8-AC4 GATEWAY_LOCAL_DB_COUNT=0 AND GATEWAY_ANY_KUZU_COUNT=0 over a walk of 32,220 paths with the probe control firing; D8-AC5 RECORDED under UNVERIFIABLE-BY-INSTRUMENT with NO verdict, for 3.0.0_SA_CVO at L9. Proof instance VALID rc=0 against all five ids. TWO ROWS FILED, both OBSERVATION/INERT: W2-S28 -- the main-workspace zero is name-scoped, and an UNSCOPED read of the same directory shows three other local Kuzu stores, one a 1,166-node June copy of THIS graph by its own manifest, all already carded by 3.0.0_SA_CVO with a do-NOT-delete on two, which is a D8-AC5 reading input and no criterion's failure; W2-S29 -- D8-AC1 and D8-AC2 each re-fire the paired ask while BOUNDS caps it at two attempts, so the script ran twice, both runs are recorded whole and D8-AC2 was derived from attempt 2's own stdout with nothing discarded. READS ONLY on both machines: no write on the gateway host, no S3 write, no engine, no local graph created or opened anywhere, no code edited. NOT THIS ORDER'S AND NAMED: the D8-AC5 reading (3.0.0_SA_CVO at L9); kuzu_stitch_db (the issuer's placed manifest row at L10); the site-Z reader, still available if the gateway substitution is refused. The L8 seat reads the record. PRIOR STATUS, kept for the record: pending -- GO = the COO handing this order to slot ~2 by CONTINUING the same subagent after TO-CG-D-7 (CG-s-8) is terminal and merged and the issuer has switched off the laptop's own copy (the drain act recorded in the round-4 step log), with CLOUD merged into your branch (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~2's FIFTH and LAST order -- the last order of the run ("CG-s-8 -> CG-x-7 last", ROUND_ANALYSIS.round3.md @2dd381d969); the closing pass for FWD-7, released by CG-s-8 switched off. PREMISE RE-GROUND at hand-off: D7's proof VALID at your HEAD; if not, BLOCKING row + report. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop (+ a second machine as the second reader) · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-7; acceptance 7; R7) · **Decomp cell:** `CG-x-7` (v0.2 @`70918d5d2b` s.1b) · **Lane:** this order's deliverables only · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~2`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~2`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~2;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~2 <0.9.0_WK_NFRA_CLDGRPH~2@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/`.**
- **Surprise = ONE ROW, never a message** (id `NFRA_CLDGRPH-W2-S<k>`, continuing your W2 numbering; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** create a local graph anywhere; run an engine; write on the second machine (the SSM command is a read: `ls`, `find` bounded, `curl`); edit code; write to S3; non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find in THIS repo refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1b)

> **CG-x-7** | FWD-7 | DONE WHEN: EXERCISED -- two people on different machines have asked the same question at the same moment and received the same answer, after the local copy was switched off | the act: after CG-s-8's switch-off, two seats on two machines ask the same question inside one minute | status OPEN | lane `0.8.0_AE_CloudComp` | placement laptop + site Z as the second reader | depends_on: CG-s-8 -> switched off | **closes on:** identical answers with identical vintage lines; no local DB on either machine (proven); this closes CG-s-8

**PRD acceptance 7 (verbatim):** *"One story, no older copy. With every developer machine off, two people on two machines ask the same question at the same moment and get the same answer, and there is no local copy left that either could have read instead. (FWD-7)"*

## MEASURED BY THE ISSUER AT THE CUT -- and the ONE reading the issuer made for you

- **THE SECOND MACHINE IS THE GATEWAY HOST `i-07dccb1615503ac99`, not site Z.** The decomposition names site Z as the second reader; a worker has no bus, no skill and no session on site Z, so the second machine a worker CAN drive is the gateway EC2 host by SSM (a different machine, in the VPC, with no repository and no local graph -- exactly a machine that "has never held the graph"). The issuer states this substitution here so the CVO grades it as a judgment (D8-AC5), and the site-Z reader stays available to the CTO's round-N analysis if the substitution is refused. The gateway host answers the SAME service directly (`curl` to `http://projection.opal-globgrph.local:8181/cypher`, `Content-Type: text/plain`, the Cypher as the body -- the exact C-1 SSM shape, `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/CG-s-4.serving-service.result.md`, "Live exercise"), and the laptop reader is YOUR worktree through `comp-kuzu` (thin client -> gateway `/graph/cypher` -> the same service). Two machines, one served artifact.
- **"Inside one minute":** both asks are timestamped from the SAME clock (`date -u +%FT%TZ` on the laptop before and after; the SSM command's `ExecutionStartDateTime` from `get-command-invocation`, which is AWS's clock -- state the skew if it matters). The pointer advances about hourly; if it advances between your two asks, the vintage lines DIFFER and the arm is re-run once (the record keeps both attempts).
- **The question, fixed by the issuer:** `MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC, t` (deterministic ordering; the same question TO-CG-D-6 asked). Compare the `rows` arrays as JSON and the `vintage` strings.
- **"No local DB on either machine (proven)":** laptop = your worktree (`ls infra/aws/globgrph/ | grep -c kuzu_nessie_db` -> 0) AND the main workspace's copy, which the ISSUER deleted at the drain before continuing you (the issuer's `ls` with rc is in the round-4 step log; you quote the step-log line, you do not read the main workspace); gateway host = `sudo find / -xdev -name 'kuzu_nessie_db*' -maxdepth 6 2>/dev/null | wc -l` -> 0 by SSM (the `2>/dev/null` there discards permission noise on a find whose COUNT is the verdict; the count is printed).

## DELIVERABLE -- in this order

1. **Prove the absences** (both machines) with timestamps.
2. **THE TWO ASKS INSIDE ONE MINUTE:** `bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/two_machines.sh` (yours): timestamp T0; fire the SSM `send-command` (the gateway ask) and immediately run the laptop ask `bash .tools/comp-kuzu --json "<cypher>"` (stderr captured for its VINTAGE line); timestamp T1; poll `get-command-invocation` (bounded, at most 12 x 5 s) and print its `StandardOutputContent` whole (the service's JSON) and its `ExecutionStartDateTime`; then print `LAPTOP_VINTAGE=<vintage>`, `GATEWAY_VINTAGE=<vintage>`, `ROWS_EQUAL=<true|false>` (compare the two `rows` arrays as canonical JSON), `WINDOW_S=<T1-T0 seconds>`.
3. **The record** `CG-x-7.two-machines.result.md`: one fenced JSON block `{machine_a: "laptop worktree <path>", machine_b: "gateway i-07dccb1615503ac99", question, cypher, laptop_answer, gateway_answer, laptop_vintage, gateway_vintage, rows_equal, window_s, local_db_laptop: 0, local_db_main_workspace: "<the step-log line quoted>", local_db_gateway: 0, second_reader_substitution: "gateway host for site Z -- the issuer's reading, graded D8-AC5"}` then the raw transcript. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D8-AC1" cell_refs="CG-x-7"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/two_machines.sh | grep -E '^(ROWS_EQUAL|WINDOW_S)='</invocation><expect>ROWS_EQUAL=true[\s\S]*WINDOW_S=([0-9]|[1-5][0-9])(\.[0-9]+)?$</expect></criterion>
`D8-AC1` -- IDENTICAL ANSWERS INSIDE ONE MINUTE: the two `rows` arrays are equal and the window is under 60 s.

<criterion id="D8-AC2" cell_refs="CG-x-7"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/two_machines.sh | grep -E '^(LAPTOP|GATEWAY)_VINTAGE=' | cut -d= -f2 | sort -u | wc -l</invocation><expect>^1$</expect></criterion>
`D8-AC2` -- IDENTICAL VINTAGE LINES: exactly one distinct vintage across the two answers.

<criterion id="D8-AC3" cell_refs="CG-x-7"><invocation>ls infra/aws/globgrph/ | grep -c kuzu_nessie_db</invocation><expect>^0$</expect></criterion>
`D8-AC3` -- NO LOCAL DB ON THE LAPTOP READER (this worktree).

> ### AMENDMENT 2026-09-05 ~23:0xZ BY THE ISSUER, BEFORE THE HAND-OFF -- D8-AC3 CANNOT FAIL AS
> WRITTEN, AND THE REPORT MUST CARRY THE MEASUREMENT THAT CAN. **THE BAR DOES NOT MOVE:** D8-AC3's
> invocation and its `^0$` expect are unchanged, and there are FIVE criteria before and after.
>
> ⛔ **MEASURED BY THE ISSUER 2026-09-05 22:5xZ, WITH THE LAPTOP COPY FULLY INTACT:** the exact
> command this criterion runs (`ls infra/aws/globgrph/ | grep -c kuzu_nessie_db`) returns **0 in a
> fresh worktree TODAY**, while the main workspace at
> `C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/` holds **6 entries** of exactly
> that name. The reason is structural: `infra/aws/globgrph/.gitignore:3` ignores `kuzu_nessie_db`,
> so it is **never checked out into any worktree**. **This arm therefore passes whether or not the
> local copy is ever switched off** -- it measures the WORKTREE while its own prose says *the
> laptop reader*, and FWD-7 asks whether there is *no local copy left that either machine could
> have read instead*.
>
> **REQUIRED IN YOUR REPORT, beside D8-AC3's zero:** the same census run against the MAIN WORKSPACE
> BY ABSOLUTE PATH --
> `ls C:/Users/AndrewBerman/Desktop/ajb_workspace/infra/aws/globgrph/ | grep -c kuzu_nessie_db` --
> printed as `MAIN_WORKSPACE_LOCAL_DB_COUNT=<n>`, with the directory listing quoted if `<n>` is not
> zero. That path is OUTSIDE your worktree and this is a **READ**, which your grant does not
> restrict; you write nothing there and you delete nothing there.
>
> ⛔ **WHY IT MUST BE YOU WHO MEASURES IT: the deletion is the ISSUER'S act, and the only evidence
> the record would otherwise carry is the ISSUER'S OWN step-log line.** A producer's self-report is
> not verification of the produced state. Your count is the independent read. **If
> `MAIN_WORKSPACE_LOCAL_DB_COUNT` is non-zero, that is NOT your failure and NOT a reason to stop:
> report it, print the listing, and file a row** -- it means the issuer's drain act did not land,
> and this seat owns that.
>
> ⚠ **AND SAY WHICH ZERO IS WHICH IN THE DELIVERABLE.** D8-AC3's zero is a worktree property that
> was already true before the retirement began; `MAIN_WORKSPACE_LOCAL_DB_COUNT` is the one that
> carries FWD-7's claim. The CVO grades D8-AC5 on exactly that distinction, so do not let the two
> zeros stand side by side unlabelled.

<criterion id="D8-AC4" cell_refs="CG-x-7"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/gateway_no_db.sh</invocation><expect>GATEWAY_LOCAL_DB_COUNT=0</expect></criterion>
`D8-AC4` -- NO LOCAL DB ON THE SECOND MACHINE (`gateway_no_db.sh`, yours: the bounded SSM `find` above, its count printed as `GATEWAY_LOCAL_DB_COUNT=<n>`).

<criterion id="D8-AC5" cell_refs="CG-x-7" judgment="true"/> `D8-AC5` -- THE SECOND READER: whether the gateway host stands for "two people on two machines" as FWD-7 means it, with the issuer's substitution stated and the site-Z reader named as the alternative; and whether "every developer machine off" is met given the issuer's deletion of the main workspace's copy (the step-log line). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>D8-AC1, D8-AC2, D8-AC3, D8-AC4, D8-AC5</expected_criteria>

## SURFACES

`.tools/comp-kuzu` (READ; the laptop client) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/CG-s-4.serving-service.result.md` (READ: the SSM curl shape) · `org/missions/D0/NFRA/NFRA_CLDGRPH/ledger/STEP_LOG.2.0.0_SA_COO~A.round4.json` (READ: the issuer's switch-off line) · PRD ENDPOINT FWD-7 (READ).

## BOUNDS

- **Reads only, on both machines.** No write on the gateway host; no S3 write; no engine; no code change.
- **At most two attempts of the paired ask** (the second only if the pointer moved between the two answers of the first).
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-8.close-fwd7-two-machines.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-x-7 (s.1b; the closing pass for FWD-7; closes CG-s-8).
<owned_cells>CG-x-7</owned_cells>
Read-dependencies, NOT claimed: CG-s-8 (TO-CG-D-7, switched off before this order is handed).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria bind this face's BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- SSM `send-command` on the gateway host with the seat's existing credentials (the instrument C-1 and V-2 used); no principal, policy or grant is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D8-AC1`..`D8-AC5`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~2/NFRA_CLDGRPH.TO-CG-D-8.close-fwd7-two-machines.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D8-AC1,D8-AC2,D8-AC3,D8-AC4,D8-AC5` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D8-AC1`, `D8-AC2` and `D8-AC4` are the controls that must be able to FAIL. `D8-AC5` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE THE ASK: `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.7.0_AE_CloudOps~T/CG-s-4.serving-service.result.md --for "the exact SSM send-command and curl used from the gateway host and the response shape"`. No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-7's drain and the switch-off).**
