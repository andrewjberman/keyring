# TO-AR-g-129 -- the resolve hop backs off a WAF challenge with a growing spacing (150, 300, 450 s: 15 minutes in all) instead of retrying it at a flat 60 s (r34f)

<to_id>IRPT_ANLREQ.TO-AR-g-129</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~263</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>42</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-129` (`decompositions/IRPT_ANLREQ_DECOMP_R42_G.md`) |
**outcome_ref:** FWD-1 run 3 (the door's resolve under a WAF challenge) | **depends_on:** nothing unmerged. Order: CTO msgs 9429 and 9447; the design draft `deliverables/2.0.0_SA_COO~G2/WAF_BACKOFF_DESIGN_20261016.md`.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~263`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-263` (branch `wk-IRPT_ANLREQ-263`), provisioned by the issuer with `infra/aws/lambda/investor-reporting`, `lib`, `.tools`, `org/standards` and the project folder on disk. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~263 <0.9.0_WK_IRPT_ANLREQ~263@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The workspace worktree may show ` M portal` and a modified `.parquet` fixture: never commit either. (A provisioner error about a portal sub-worktree does not concern you.)
- A row id has the form `IRPT_ANLREQ-D2-W263-S<k>` (take the next free `<k>`; check the channel file for `W263` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax: no `X | None`, no `match`). No non-ASCII in what you add.
- No live call, NO PUSH, no deploy, no AWS call, no network, no install. Scratch outside the product tree.
- Run each test file ON ITS OWN (`python -m pytest -q <one file>`).

- **INHERITED STATE (re-seat, issuer ruling on row W262-S1).** Worker `0.9.0_WK_IRPT_ANLREQ~262` made the product change and wrote the tests but its sparse worktree could not run them. You are re-seated on the SAME branch tip: your worktree `C:/dev/wk-irpt-anlreq-263` is a FULL checkout of branch `wk-IRPT_ANLREQ-263`, created from the tip of `wk-IRPT_ANLREQ-262` (commits `175596f205` the change and tests, `d063c6cbf2` row W262-S1, `7f0e78bcb7` worker 262's proof instance). The product change in `resident_worker.py` is correct and the issuer's build and guard arms pass on it: do NOT change it. Your job is ONLY to make the tests run and pass, and to produce your own proof. Run `python -m pytest -q <file>` on `tests/test_resolve_upload.py` first and read the failures: in the issuer's full-checkout run, 10 of the new tests fail because the real assembly calls the heartbeat (a `VisibilityTimeout=900` call) BEFORE the RETRY branch sets the back-off, so the recorded list is `[900, <delay>]`, not `[<delay>]`.
- **TEST FIX (the only edit allowed to the tests):** in `CountingQueue` and the new tests, assert on the LAST recorded visibility (`queue.timeouts[-1]`), and, where a test now says `queue.timeouts == [..]`, say `queue.timeouts[-1:] == [..]` (for the fourth receive, assert the message was deleted and that no visibility call follows the 900-s heartbeat: `queue.timeouts[-1:] in ([], [900])`). The expectations on the journal lines, the deletes and the delays 150, 300, 450 and 60 stay exactly as written above. Do not touch the existing tests of the file.

### Read first (under `C:/dev/wk-irpt-anlreq-263/infra/aws/lambda/investor-reporting/ycharts/generate/`)

- `resident_worker.py`: the constant `RESOLVE_RETRY_VISIBILITY_S` (line ~858), `RESOLVE_MAX_RECEIVES` (line ~877) and the `poll_once` function's `elif result["state"] == "RETRY":` branch (lines ~978-989), and `tests/test_resolve_upload.py` (the `Queue` double, `assembly(...)`, `broker_world.world({...})`, and `test_provider_outage_is_retry_and_the_message_stays`).

### THE CELL (`AR-g-129`, inlined)

A resolve whose lookup is refused with a WAF challenge (`code` `PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE`) is retried today with a flat `VisibilityTimeout=60` for every cause, three more times. YCharts's firewall window was measured at (122, 373] s (the comment at lines ~860-864), so the three 60 s retries all fall inside it and the row ends `RESOLVE_RETRY_EXHAUSTED`. This cell gives a WAF challenge, and only that, a growing spacing.

**`resident_worker.py`, exactly this, and nothing else in the file:**
1. Replace the single line `RESOLVE_RETRY_VISIBILITY_S = 60` with:

```
RESOLVE_RETRY_VISIBILITY_S = 60

# CTO msg 9429: a WAF challenge on the resolve hop's lookup is retried with a GROWING spacing, 150 + 300 + 450 = 900 s in all
# (the CTO's 15-minute cap; under upload_resolution.REDRIVE_SECONDS 960 and the queue's maxReceiveCount 5), because the
# YCharts firewall window measured on 2026-10-05 lies in (122, 373] s and the flat 60 s retry sits inside it.
RESOLVE_WAF_CLASS = ":WAF_CHALLENGE"
RESOLVE_WAF_BACKOFF_S = (150, 300, 450)


def _resolve_retry_visibility(code, receives):
    """The seconds a RETRY'd resolve message stays invisible: the growing WAF schedule for a code ending ":WAF_CHALLENGE",
    the flat RESOLVE_RETRY_VISIBILITY_S for every other cause."""
    if isinstance(code, str) and code.endswith(RESOLVE_WAF_CLASS) and type(receives) is int and receives >= 1:
        return RESOLVE_WAF_BACKOFF_S[min(receives, len(RESOLVE_WAF_BACKOFF_S)) - 1]
    return RESOLVE_RETRY_VISIBILITY_S
```

2. In `poll_once`, in the `else:` of the `if receives >= RESOLVE_MAX_RECEIVES:` that sits inside `elif result["state"] == "RETRY":`, replace

```
                    print("IRPT_RESIDENT_RESOLVE state=%s code=%s" % (
                        result["state"], result.get("detail", {}).get("code", "-")), flush=True)
                    sqs.change_message_visibility(QueueUrl=queue_url,
                        ReceiptHandle=envelope["ReceiptHandle"], VisibilityTimeout=RESOLVE_RETRY_VISIBILITY_S)
```

with

```
                    delay = _resolve_retry_visibility(result.get("detail", {}).get("code"), receives)
                    print("IRPT_RESIDENT_RESOLVE state=%s code=%s visibility=%d" % (
                        result["state"], result.get("detail", {}).get("code", "-"), delay), flush=True)
                    sqs.change_message_visibility(QueueUrl=queue_url,
                        ReceiptHandle=envelope["ReceiptHandle"], VisibilityTimeout=delay)
```

3. No other change: not the BUSY branch, not `_end_exhausted_resolve`, not `RESOLVE_MAX_RECEIVES`, not any other function.

**Tests**, appended to `tests/test_resolve_upload.py` (it keeps all its existing tests untouched), with these exact function names, offline and using the real `poll_once`:
- a small `CountingQueue(Queue)` double that returns `{"Attributes": {"ApproximateReceiveCount": str(n)}}` in the received message and records every `VisibilityTimeout` passed to `change_message_visibility`;
- `test_waf_challenge_retry_backs_off_150_300_450_and_names_the_delay` (parametrised over receives 1, 2, 3 and 150, 300, 450; the lookup refused with `broker_world.world({"status": 202, "waf_action": "challenge", "body": []})`; assert the recorded visibility is `[delay]`, the message is not deleted, and the journal line is `IRPT_RESIDENT_RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE visibility=<delay>`);
- `test_waf_challenge_at_the_fourth_receive_ends_the_row` (receive 4: the message is deleted and the journal says `state=ATTENTION code=RESOLVE_RETRY_EXHAUSTED`; same refused lookup);
- `test_other_retry_causes_keep_the_flat_sixty` (receives 1, 2, 3 with the existing `{"status": 503, "body": []}` outage and with `{"status": 405, "waf_action": "captcha", "body": []}`: the recorded visibility is `[60]`);
- `test_the_visibility_function_matches_only_a_code_that_ends_with_the_class` (direct calls: `_resolve_retry_visibility("PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE", 1)` is 150; a code ending `:WAF_CHALLENGE_EXTRA`, `"WAF_CHALLENGE:X"`, `None`, `7` and `""` give 60; a receive count of 0 or 1.5 gives 60);
- `test_the_waf_backoff_total_is_the_cap_and_stays_inside_the_redrive_and_the_queue_limit` (`sum(RESOLVE_WAF_BACKOFF_S) == 900`; at most `upload_resolution.REDRIVE_SECONDS`; `RESOLVE_MAX_RECEIVES < 5`).

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR129-g-AC1" cell_refs="AR-g-129"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g129_checks.py build</invocation><expect>^AR-G129-OK</expect></criterion>

<criterion id="AR129-g-AC2" cell_refs="AR-g-129"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g129_checks.py guard</invocation><expect>^AR-G129-OK</expect></criterion>

<criterion id="AR129-g-AC3" cell_refs="AR-g-129"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_g129_checks.py regress</invocation><expect>^AR-G129-REGRESS-OK</expect></criterion>

<expected_criteria>AR129-g-AC1,AR129-g-AC2,AR129-g-AC3</expected_criteria>

- AC1 imports `resident_worker` and runs the REAL `poll_once` with a recording queue: the schedule is (150, 300, 450), sums to 900, stays under `REDRIVE_SECONDS`, and `RESOLVE_MAX_RECEIVES` stays under 5; receives 1, 2, 3 of a `:WAF_CHALLENGE` RETRY set `VisibilityTimeout` 150, 300, 450 and print `visibility=<s>`; receive 4 ends the row. At base it FAILs.
- AC2 needs every other RETRY code to keep the flat 60 s at every receive through the real `poll_once`, a code that only contains `WAF_CHALLENGE` or is missing to take 60, and the BUSY class to keep its own re-send path. At base it PASSes; a fix that gives every cause the schedule, matches by substring, uses a flat 150, a total over the cap, or drops the journal delay FAILs build or guard.
- AC3 runs two test files one at a time (`tests/test_resolve_upload.py` and `tests/test_frozen_worker.py`) and needs the branch to change only `resident_worker.py`, the test file, your folder, your order and the channel file. At base it PASSes. Run it under `timeout` 590000 ms.

## BOUNDS

- **Grant.** The `<paths>` block only. No deploy, no AWS call, no HTTP, no installs.
- **Refusal clause.** If a criterion cannot be met as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py
infra/aws/lambda/investor-reporting/ycharts/generate/tests/test_resolve_upload.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~263/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-129.resolve-waf-backoff.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R42_G.md</decomp_doc> round 42, workstream ~G, cell `AR-g-129`.
<owned_cells>AR-g-129</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR129-g-AC1, AR129-g-AC2, AR129-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~263/IRPT_ANLREQ.TO-AR-g-129.resolve-waf-backoff.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-129`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put the `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each COMMITTED file with the hash of the commit that holds it: commit the product files first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR129-g-AC1,AR129-g-AC2,AR129-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~67/IRPT_ANLREQ.TO-AR-g-32.packager-own-store-precheck-no-ticket-read.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):**
- each criterion's output lines;
- the lines you changed in `resident_worker.py` with line numbers;
- commits and row ids.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- `ycharts/generate/resident_worker.py` is a member of the resident package (the r34e root, running, carries the pre-change bytes; the next resident release, r34f, carries this) and is staged into no Lambda function's source-map row. Behaviour change on the resolve hop only: a RETRY whose code ends `:WAF_CHALLENGE` is released for 150, 300 and 450 s at receives 1, 2 and 3 instead of 60 s each; the upload shows RESOLVING for up to 900 s before ending as it does today (it was about three minutes); every other cause is unchanged. No vendor call is made by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- by the issuer's reference fix in a scratch worktree (build and guard arms pass; at base build FAILs and guard PASSes; the two existing test files pass) and FIVE mutants (a flat 150; the schedule for every cause; a substring match; a total of 1200 s; no journal delay), each FAILing build or guard. Traps: the schedule applied to every cause (a 503 would wait 150 s); a loose match on the class; a total over REDRIVE_SECONDS (the client re-dispatches and doubles the lookups); a total that makes the queue dead-letter (RESOLVE_MAX_RECEIVES must stay under 5); the BUSY path disturbed; the delay not in the journal. NOT seen (blind): whether a longer spacing clears the challenge in production (the 2026-10-05 measurement is for the generation hop; SET 2 is consistent with it); denominator: 1 module, 1 branch, 9 non-WAF codes and 3 receives in the guard, 3 WAF receives plus the ending in the build.
</preflight>

- Cut on CTO msgs 9429 and 9447 and AQ2's clean lookup. Risk WORLD: the floor of an infrastructure path; source and tests only, nothing deployed. Base: `AR129-g-AC1` FAILs, `AR129-g-AC2` and `AR129-g-AC3` PASS, as expected.
- NOT claimed: that the challenge clears within 900 s every time; that the resident carries the change (the next release does).
