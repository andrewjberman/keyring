# TO NFRA_CLDGRPH.TO-CG-D-10 -- CLOSING PASS, FWD-4 EXERCISED: over ONE FULL REFRESH CYCLE with nobody enforcing the ceiling by hand, every served answer's age read from the service's OWN log against the schedule's ceiling -- the oldest age served <= the ceiling; the control: a planted stale artifact is NOT served (the backward-refusal seam re-run)

<to_id>NFRA_CLDGRPH.TO-CG-D-10</to_id>
<project>NFRA_CLDGRPH</project>
<issued_to>0.9.0_WK_NFRA_CLDGRPH~1</issued_to>
<issued_by>2.0.0_SA_COO~A</issued_by>
<issued_date>2026-09-04</issued_date>
<status>pending -- GO = the COO handing this order to slot ~1 by CONTINUING the same subagent after TO-CG-D-9 (CG-x-2) is terminal and merged (spine v3 L7 drain). ROUND 4 of NFRA_CLDGRPH (the ONE issuance covering every open cell, Andrew's word via CRO record @aff3bfb7bf), slot ~1's FOURTH order; the closing pass for FWD-4, released by CG-x-2 DONE and one full cycle. The cycle is READ from the record, not waited for: the serving service has been up since 2026-09-03 18:3xZ (task `c18ee8b40e4a4bf3993f8f78cc2f98a6`, startedAt epoch 1788460967), so by the time this order is handed a 24 h window containing one nightly boundary (02:00Z) is on its log. The assignee commits its own status flip after a VALID proof-of-spec instance; the L8 seat reads the record.</status>

**Directive:** D0 · **Fabric:** laptop · **PRD:** `org/missions/D0/NFRA/NFRA_CLDGRPH/prd/NFRA_CLDGRPH_PRD.md` v0.4 @`25c66d3358` (FWD-4; acceptance 4) · **Decomp cell:** `CG-x-4` (v0.2 @`70918d5d2b` s.1b) · **Lane:** this order's deliverables only · **Rule 27 seating:** `0.9.0_WK_NFRA_CLDGRPH~1`, a spine-v3 worker subagent of `2.0.0_SA_COO~A`.

---

## STANDING LAW (inlined; the worker face is your whole context)

- **Serial:** `0.9.0_WK_NFRA_CLDGRPH~1`. Every Bash call begins `export OPAL_AGENT_SERIAL=0.9.0_WK_NFRA_CLDGRPH~1;`. Commit only on your worktree branch via `bash .tools/safe-commit.sh --author "0.9.0_WK_NFRA_CLDGRPH~1 <0.9.0_WK_NFRA_CLDGRPH~1@opal.agent>" -F <msgfile> -- <files>`, `<msgfile>` written with the Write tool. Never push, merge, rebase, `checkout --` or `clean`. Push state is LOCAL and you say so.
- **Your write surface is exactly the PATHS block below plus `org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/`.**
- **Surprise = ONE ROW, never a message** (id `NFRA_CLDGRPH-W1-S<k>`, continuing your W1 numbering; restate the header denominator; never edit an existing row; keep working).
- **Every criterion invocation runs under `timeout 120`**; rc 124 IS the recorded output, retried once at most.
- **NEVER:** write the marker, the pointer or any `projection/` object; plant anything in S3 (the plant is the unit test's in-process body, `projection_server.py`'s own seam); run an engine; stop/restart a task; edit code; an alarm/monitor; non-ASCII; `2>/dev/null` on a verdict read; bare `git commit`.
- **Search rail:** `python .tools/comp-read` / `python .tools/comp-find`; raw recursive grep/find refused; a `cmd | grep` receiver is free. AWS CLI = `.tools/aws`.

## THE CELL (verbatim, decomposition v0.2 s.1b)

> **CG-x-4** | FWD-4 | DONE WHEN: EXERCISED -- a full cycle has passed with nobody enforcing the ceiling by hand and no answer served older than it | the act: over one full refresh cycle, every served answer's age is read against the schedule's ceiling | status OPEN | lane `0.7.0_AE_CloudOps` | placement laptop | depends_on: CG-x-2 -> DONE | **closes on:** the oldest age served in the cycle <= the ceiling, from the service's own log; the control: a planted stale artifact is NOT served

**PRD FWD-4 (verbatim, ENDPOINT):** *"There is a ceiling on how old any answer can be, and the ceiling belongs to the schedule, not to a person."* **Acceptance 4:** *"The ceiling holds by itself. Over a full cycle with nobody enforcing it by hand, no one is handed an answer older than the last scheduled refresh."*

## MEASURED BY THE ISSUER AT THE CUT -- the ceiling and the log, defined so the arm can fail

- **THE CEILING BELONGS TO THE SCHEDULE:** the nightly full derive at `cron(0 2 * * ? *)` (`item2a.tf:439`) plus the build-and-publish chain. So an answer's age (answer time - served `vintage`) can never lawfully exceed **24 h + the nightly chain's own duration**, and the intraday stamps only make it younger. Read the chain duration from the record: the nightly manifest's `built_at` - `vintage` (2026-09-04: 02:22:43Z - 02:09:19Z = 13 min 24 s) plus the pointer-to-swap lag (<= 60 s, the watcher interval). **CEILING_S = 86400 + (built_at - vintage of the cycle's nightly) + 60.** Print it.
- **"THE SERVICE'S OWN LOG":** CloudWatch log group `/ecs/globgrph-serving` (C-1's IAM: log writes on `/ecs/globgrph-serving:*`); the server logs every HTTP request (`projection_server.py` `log_message` -> `LOG.info("http ...")`) and every swap (the watcher's lines; `comp-read infra/aws/globgrph/projection_server.py --for "every LOG.info/LOG.warning line and what each carries: the swap, the refusals, the http access line"` -- read it first to learn the exact strings). The served vintage at any instant is the LAST swap before it; an answer at time t while vintage v is served has age t - v. Build the timeline from the swap lines (bounded: `logs filter-log-events --filter-pattern "swap"` over the 24 h window, `--limit` and pagination with `--next-token`; print the event count as the denominator), then walk the `http POST /cypher` lines in the same window and compute each answer's age against the swap timeline. Print `ANSWERS_IN_CYCLE=<n>`, `SWAPS_IN_CYCLE=<m>`, `OLDEST_AGE_SERVED_S=<max>`, `CEILING_S=<c>`, `WITHIN_CEILING=<true|false>`. If the access line does not carry enough to place an answer, say so and use the `/health` `last_swap`/`vintage` pairs you can read at the window's end plus the swap timeline -- state the method's coverage.
- **THE CYCLE:** the 24 h ending at your read, which must contain exactly one nightly boundary (02:00Z) and the nightly's swap. Print `CYCLE_START`, `CYCLE_END`, `NIGHTLY_SWAP_AT`.
- **"NOBODY ENFORCING BY HAND":** no human/seat RunTask or pointer write in the cycle -- CloudTrail `RunTask` (as in TO-CG-D-9's limb (i), the same census over the cycle window) and `PutObject` on `projection/current.json` (CloudTrail data events may not be enabled for S3 -- if the lookup returns nothing for the key, say COVERAGE UNKNOWN and use the manifests' `writer_id` values across the cycle's vintages instead: every one is `derive_runner` or `incremental_updater`, never a seat).
- **THE CONTROL (a planted stale artifact is NOT served):** the service's backward-refusal seam, already a unit test at `infra/aws/globgrph/tests/test_projection_server.py:90-188` @`8f0dff109f` (a planted backward pointer body; `LOADER_CALLS=0`; the served vintage unchanged). Re-run it at your HEAD: `python -m pytest infra/aws/globgrph/tests/test_projection_server.py -q -k "backward or refus"` -> passed. That is a plant against the READER in-process; no S3 object is planted.

## DELIVERABLE -- in this order

1. **Read the log's vocabulary** (comp-read on `projection_server.py`), then `cycle.sh` (yours): the cycle window, the swap timeline (denominator printed), the per-answer ages, the oldest, the ceiling with its arithmetic, the hands-off censuses with denominators; prints the `KEY=value` lines named above plus `HANDS_OFF_RUNTASK=<n nonpipe> of <N>`, `WRITERS_IN_CYCLE=<set of writer_id>`.
2. **The control:** the pytest run quoted whole.
3. **The record** `CG-x-4.ceiling-holds.result.md`: one fenced JSON block (the KEY=value set + the swap timeline as a list of `{at, vintage}` + the top-5 oldest answers with their times) then the transcripts. Then the proof instance, validate, flip, commit.

## ACCEPTANCE (v3 grammar: one clause per criterion; every mechanical invocation bounded)

<criterion id="D10-AC1" cell_refs="CG-x-4"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/cycle.sh | grep -E '^(OLDEST_AGE_SERVED_S|CEILING_S|WITHIN_CEILING)='</invocation><expect>OLDEST_AGE_SERVED_S=[0-9]+(\.[0-9]+)?[\s\S]*CEILING_S=8[6-9][0-9]{3}(\.[0-9]+)?[\s\S]*WITHIN_CEILING=true</expect></criterion>
`D10-AC1` -- THE OLDEST AGE SERVED IN THE CYCLE IS UNDER THE SCHEDULE'S CEILING, both numbers printed from the service's own log (the arm that can fail: one answer older than the ceiling prints `false`).

<criterion id="D10-AC2" cell_refs="CG-x-4"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/cycle.sh | grep -E '^(ANSWERS_IN_CYCLE|SWAPS_IN_CYCLE|NIGHTLY_SWAP_AT)='</invocation><expect>ANSWERS_IN_CYCLE=[1-9][0-9]*[\s\S]*SWAPS_IN_CYCLE=[1-9][0-9]*[\s\S]*NIGHTLY_SWAP_AT=20[0-9]{2}-[0-9]{2}-[0-9]{2}T0[2-3]:</expect></criterion>
`D10-AC2` -- THE CYCLE IS REAL: at least one answer and one swap on the log, and the nightly's swap inside the window at 02:xx-03:xxZ (the denominators).

<criterion id="D10-AC3" cell_refs="CG-x-4"><invocation>bash org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/cycle.sh | grep -E '^(HANDS_OFF_RUNTASK|WRITERS_IN_CYCLE)='</invocation><expect>HANDS_OFF_RUNTASK=0 of [0-9]+[\s\S]*WRITERS_IN_CYCLE=\{?('?(derive_runner|incremental_updater)'?,? ?)+\}?$</expect></criterion>
`D10-AC3` -- NOBODY ENFORCED IT BY HAND: zero non-Pipe/non-scheduler RunTasks; every vintage in the cycle written by a producer, never a seat.

<criterion id="D10-AC4" cell_refs="CG-x-4"><invocation>python -m pytest infra/aws/globgrph/tests/test_projection_server.py -q -k "backward or refus"</invocation><expect>[1-9][0-9]* passed</expect></criterion>
`D10-AC4` -- THE CONTROL: a planted stale/backward artifact is NOT served (the reader's own seam, re-run at your HEAD).

<criterion id="D10-AC5" cell_refs="CG-x-4" judgment="true"/> `D10-AC5` -- THE CEILING'S DEFINITION (24 h + the chain's duration + the watcher interval) against FWD-4's "the ceiling belongs to the schedule", and the log method's coverage (which answers could not be placed, if any). A reading act; NO verdict; graded by `3.0.0_SA_CVO` at L9.

<expected_criteria>D10-AC1, D10-AC2, D10-AC3, D10-AC4, D10-AC5</expected_criteria>

## SURFACES

`/ecs/globgrph-serving` CloudWatch log (READ) · `infra/aws/globgrph/projection_server.py` (READ: the log vocabulary, the watcher) · `infra/aws/globgrph/tests/test_projection_server.py` (READ + run) · the `projection/` manifests (READ) · CloudTrail `RunTask` (READ) · `infra/aws/terraform/globgrph/item2a.tf:439` (READ).

## BOUNDS

- **READS ONLY** on the live plane; the plant is the in-process unit test; nothing created, run, stopped or written.
- **Bounded log reads**: paginate with `--next-token`; print the event denominators.
- A spec-vs-world divergence is a ROW. Certifier != author.

<paths>
org/missions/D0/NFRA/NFRA_CLDGRPH/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D0/NFRA/NFRA_CLDGRPH/task-orders/NFRA_CLDGRPH.TO-CG-D-10.close-fwd4-ceiling-holds.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CLDGRPH/decompositions/NFRA_CLDGRPH_DECOMP.md</decomp_doc> @70918d5d2b (v0.2), cell CG-x-4 (s.1b; the closing pass for FWD-4).
<owned_cells>CG-x-4</owned_cells>
Read-dependencies, NOT claimed: CG-x-2 (TO-CG-D-9, DONE before this order is handed).
</decomp_ref>

<preflight>
comp-schedule: RUN -- 2026-09-04 06:2xZ at the cut: GATES ARMED 21 across 5 carriers (C1 21 -> 5, C2 4, C3 12, C4 20, C5 337); NEEDS-READ 138 prose fields (a reading list, never counted); the C3 moratoria bind this face's BOUNDS.
comp-iam: DECLARED-NOT-APPLICABLE -- reads with the seat's existing credentials; no principal, policy or grant is read or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- composed at L5 on the decomposition (rc 0 @07288006e5, 22/22 cited commits VERIFIED); the deliverable's validator context is the L9 seat's compose.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `D10-AC1`..`D10-AC5`. The ASSIGNEE fills a `org/standards/PROOF_OF_SPEC.schema.json` instance at
`org/missions/D0/NFRA/NFRA_CLDGRPH/deliverables/0.9.0_WK_NFRA_CLDGRPH~1/NFRA_CLDGRPH.TO-CG-D-10.close-fwd4-ceiling-holds.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> D10-AC1,D10-AC2,D10-AC3,D10-AC4,D10-AC5` BEFORE the complete flip, which the WORKER commits itself with the instance and the deliverable. `D10-AC1`, `D10-AC3` and `D10-AC4` are the controls that must be able to FAIL. `D10-AC5` is `judgment="true"`: recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; **`PASS` or `FAIL` on it is INVALID.**
</proof_of_spec>

<compiler_tools_mandate>
BEFORE THE READS: `python .tools/comp-read infra/aws/globgrph/projection_server.py --for "every LOG line the server emits -- the swap, the refusals, the http access line -- and the /health fields"`. No `.py` is edited by this order.
</compiler_tools_mandate>

**THE REPORT IS YOUR FINAL MESSAGE, ONCE, IN THE `WORKER REPORT` SHAPE.** You cannot send a message and nobody can send you one.

**GO = the hand-off (the COO continues this subagent after TO-CG-D-9's drain).**
