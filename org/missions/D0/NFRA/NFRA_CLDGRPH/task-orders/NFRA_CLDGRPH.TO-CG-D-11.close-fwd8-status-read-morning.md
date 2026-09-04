# TO NFRA_CLDGRPH.TO-CG-D-11 -- CLOSING PASS, FWD-8 EXERCISED: the operator status read taken on a REAL MORNING after CG-x-2's night reads YES with a time, and taken once against a NIGHT KNOWN NOT TO HAVE RUN reads NO -- both recorded, they differ, and NOTHING was rerun to obtain either (the invocation log as the negative control)

<to_id>NFRA_CLDGRPH.TO-CG-D-11</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~3</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO = the COO handing this order to slot ~3 by CONTINUING the same subagent after TO-CG-D-5 is terminal AND TO-CG-D-9 (CG-x-2, the night) is merged into CLOUD and CLOUD into your branch (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~3's THIRD order; the closing pass for FWD-8, released by CG-s-7 DONE (TO-CG-D-4, your own first order) and CG-x-2 DONE. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-8; acceptance 8; R4) · **Decomp cell:** `CG-x-8` (v0.2 @`70918d5d2b` s.1b) · **Lane:** this order's deliverables only · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~3`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~3`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~3;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~3 <0.9.0_WK_NFRA_CLDGRPH~3@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/`.**
- **Surprise = ONE ROW, never a message** (id `NFRA_CLDGRPH-W3-S<k>`, continuing your W3 numbering; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** rerun, rebuild, derive, or provoke a stamp to obtain either reading; write to S3; edit code; an alarm/monitor (R4); non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1b)

> **CG-x-8** | FWD-8 | DONE WHEN: EXERCISED -- the answer has been read on a real morning, and a night that did not run reads differently from one that did | the act: the status read taken on a real morning after CG-x-2's night, and once against a night known not to have run | status OPEN | lane `0.8.0_AE_CloudComp` | placement laptop | depends_on: CG-s-7, CG-x-2 -> DONE | **closes on:** both readings recorded; they differ; nothing was rerun to obtain either (the invocation log as negative control)

**PRD acceptance 8 (verbatim):** *"'Did it refresh last night' is a read, not a rerun. An operator gets a plain yes or no with a time, and a missed night looks different from a completed one. (FWD-8)"*

## MEASURED BY THE ISSUER AT THE CUT -- and the ONE reading the issuer made for you

- **The read** is your own TO-CG-D-4 deliverable: `bash .tools/comp-graph status` prints `REFRESHED LAST NIGHT: YES at <built_at>` or `NO (last full: <time>)` from the pointer's manifest and the `projection/` listing, with the 02:00Z boundary printed; `COMP_GRAPH_POINTER_URI=<path>` points it at a planted pointer+manifest pair (your `plant/` under the deliverables folder, committed with D-4).
- **"A real morning":** the read taken after the nightly boundary of the calendar day you run it, with the wall clock printed (`date -u +%FT%TZ`); the night is CG-x-2's night as TO-CG-D-9 recorded it (read `NIGHT_VINTAGE` from D-9's result in `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-x-2.schedule-exercised.result.md` -- at your HEAD after the merge -- and confirm the YES reading's time matches that vintage's `built_at`, or a LATER night's if more than one has passed; say which).
- **"A NIGHT KNOWN NOT TO HAVE RUN" -- THE ISSUER'S READING:** the estate's nightly has not missed a night on the record this project holds, and provoking a miss (disabling the schedule) is a production change no worker may make. So the night that did not run is the PLANTED one from D-4 (a pointer+manifest pair whose newest `full` vintage predates the boundary by more than a day): it is "known not to have run" by construction, and the CVO grades whether the plant stands for a real missed night (D11-AC4). Keep the plant's manifest realistic: copy a REAL manifest's shape (the 2026-09-04T02:09:19 nightly's, fields intact) with the vintages shifted back 48 h, so the read exercises the same code path a real miss would.
- **"Nothing was rerun":** the invocation log for your serial (a worker writes no telemetry: `python .tools/comp-find '0.9.0_WK_NFRA_CLDGRPH~3' org/mcp/agent_telemetry --all --limit 3` -> 0 hits, the denominator printed) AND the process table around each read (`ps -ef | grep -c -E 'kuzu_nessie_load|derive_runner|projection_worker' ` -> 0 with the `grep -v grep` discipline) AND the pointer unchanged across your two reads (`s3api head-object --key projection/current.json` ETag before/after equal -- a producer may move it between reads; if it does, say so and re-read the pair once).

## DELIVERABLE -- in this order

1. **THE MORNING READ:** `morning.sh` (yours): wall clock; the pointer ETag; procs before; `bash .tools/comp-graph status` whole; procs after; prints `MORNING_READ=<the REFRESHED LAST NIGHT line>`, `PROCS=<n>`, `POINTER_ETAG_BEFORE=`, `POINTER_ETAG_AFTER=`.
2. **THE MISSED-NIGHT READ:** `missed.sh` (yours): the same with `COMP_GRAPH_POINTER_URI=org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/plant/current.json`; prints `MISSED_READ=<line>`.
3. **The record** `CG-x-8.status-read-morning.result.md`: one fenced JSON block `{morning_wall_clock, morning_read, night_vintage_from_D9, missed_read, plant_description, procs_before_after, pointer_etags, telemetry_rows_for_serial: 0}` then the two transcripts. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D11-AC1" cell_refs="CG-x-8"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/morning.sh | grep -E '^MORNING_READ='</invocation><expect>MORNING_READ=REFRESHED LAST NIGHT: YES at 20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9:.]+</expect></criterion>
`D11-AC1` -- THE REAL MORNING READS YES WITH A TIME.

<criterion id="D11-AC2" cell_refs="CG-x-8"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/missed.sh | grep -E '^MISSED_READ='</invocation><expect>MISSED_READ=REFRESHED LAST NIGHT: NO \(last full: </expect></criterion>
`D11-AC2` -- THE NIGHT THAT DID NOT RUN READS NO: the two readings differ on the deciding line.

<criterion id="D11-AC3" cell_refs="CG-x-8"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/morning.sh | grep -E '^(PROCS|POINTER_MOVED_ACROSS_READS)='</invocation><expect>PROCS=0[\s\S]*POINTER_MOVED_ACROSS_READS=false</expect></criterion>
`D11-AC3` -- NOTHING WAS RERUN: no engine process around the read, and the pointer did not move across the read (`morning.sh` compares the two ETags itself and prints `POINTER_MOVED_ACROSS_READS=<true|false>`).

<criterion id="D11-AC4" cell_refs="CG-x-8" judgment="true"/> `D11-AC4` -- WHETHER THE PLANT STANDS FOR "A NIGHT KNOWN NOT TO HAVE RUN" as FWD-8 means it (the issuer's reading: a real miss cannot be provoked without a production change; the plant exercises the same code path with a realistic manifest), and whether the morning read's time matches D-9's night. A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>D11-AC1, D11-AC2, D11-AC3, D11-AC4</expected_criteria>

## SURFACES

`.tools/comp-graph` + `org/modules/graph/graph_status_cli.py` (READ; your D-4 deliverable) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/plant/` (READ; committed with D-4) · `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-x-2.schedule-exercised.result.md` (READ: the night) · the live pointer (READ).

## BOUNDS

- **READS ONLY.** No rerun, no rebuild, no stamp, no S3 write; the plant is a local fixture.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-11.close-fwd8-status-read-morning.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-x-8 (s.1b; the closing pass for FWD-8).
<owned_cells>CG-x-8</owned_cells>
Read-dependencies, NOT claimed: CG-s-7 (TO-CG-D-4), CG-x-2 (TO-CG-D-9).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria (no alarm/monitor) bind this face's BOUNDS and R4.
comp-iam: DECLARED-NOT-APPLICABLE -- reads with the seat's existing credentials; no principal, policy or grant is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D11-AC1`..`D11-AC4`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~3/NFRA_CLDGRPH.TO-CG-D-11.close-fwd8-status-read-morning.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D11-AC1,D11-AC2,D11-AC3,D11-AC4` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D11-AC2` and `D11-AC3` are the controls that must be able to FAIL. `D11-AC4` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE THE READS: `python .tools/comp-read org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/CG-x-2.schedule-exercised.result.md --for "the NIGHT_VINTAGE and its built_at"`. No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-5's drain and TO-CG-D-9's merge).**
