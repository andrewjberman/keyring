# NFRA_MCPINDEX task order -- `MX-y-2` -- the battery grades a test send PASS on the tester's own read-back, FAIL `send_unconfirmed` without one, and keeps `send_chat_message` PREVIEW-ONLY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md</decomp_doc>
<owned_cells>MX-y-2</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPINDEX.TO-MX-y-2.test-send-grading</to_id>
<issued_to>0.9.0_WK_NFRA_MCPINDEX~85</issued_to>
<issued_by>2.0.0_SA_COO~MI</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule; an edit to one existing script, one new test file and one changed test.
comp-iam: DECLARED-NOT-APPLICABLE -- local files only; no AWS call, no grant, no send.
comp-adversary: DECLARED-NOT-APPLICABLE -- the base dry-runs (AC1 and AC3 FAIL at the base; AC2 FAILs on its new arms only) and the planted variants of the fixture inside the criteria are the control.
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `MX-y-2` (round 25, workstream GATEWAY; PRD v0.19 FWD-24; CTO round-24 analysis `ledger/ROUND_ANALYSIS.round24.md` item 5, ruling (d))

Work in your own worktree (cut from `box/sitez`; every path below is relative to its root). The battery grader `workflows/gateway_battery/tool_battery.py` (merged, rounds 22 and 23) turns a recorded RESULTS file (`gateway_battery_results/1`) into per-case and per-tool verdicts. Today it grades ANY result with `sent` true as `FAIL` of class `sent`, because round 22 forbade any send. The CTO has ruled (d): ONE real test send per sender tool, to the tester's own mailbox or chat, is allowed (open call c5c2), and it is graded PASS when the tester reads the message back in their own mailbox; a send with no read-back stays FAIL, of the new class `send_unconfirmed`; `send_chat_message` stays PREVIEW-ONLY until a self-chat target is measured to exist. You EDIT the script, add one new test file, and change ONE existing test whose expectation this ruling supersedes.

**What to build.** In `workflows/gateway_battery/tool_battery.py` implement the contract below. Read the script first (`load_results`, `grade_case`, `cmd_grade`). Add `workflows/gateway_battery/tests/test_tool_battery_send.py` with at least 6 tests of your own. Change `workflows/gateway_battery/tests/test_tool_battery.py` in ONE place only: the test `test_a_send_is_a_fail_even_on_the_preview_case` asserts the old class `sent`; make it assert the new class `send_unconfirmed` (both in the tool row and in `doc["fails"]`). Every other existing test must keep passing unchanged, including `tests/test_tool_battery_route.py`.

### The contract (verbatim from the decomposition; it is the whole specification)

**Y2 TEST-SEND GRADING.** In `tool_battery.py`, a RESULT may carry `"readback": {"agrees": true|false|null, "instrument": str}` beside `"sent": true`. A result with `sent` true is PASS when `readback.agrees` is true (the tester read the message back in their own mailbox or chat), and FAIL of class `send_unconfirmed` when `readback` is absent, null or false. A result with `sent` false is graded as before. `send_chat_message` with no sent result and a preview or absent result is PREVIEW-ONLY, never FAIL for lack of a send, and the REALIZED line of the grade names it (stdout gains `PREVIEW-ONLY TOOLS:` as today; the graded file's `preview_only` lists it). A `readback` on a result with `sent` false is refused (exit 2). No other verdict or class moves; the round-22/23 fixtures grade byte-identically.

### The silences the issuer has settled (follow them)

1. `readback` is validated when it is present and not null: it must be an object whose `agrees` is `true`, `false` or `null` (a missing `agrees` reads as null) and whose `instrument` is a non-empty string; anything else is refused (exit 2, `REFUSED` on stderr, no output file), like every other malformed input. A `readback` of null beside `sent` true reads as "absent".
2. A result with `sent` true is graded BEFORE its status and its case's `expect` are looked at: `readback.agrees` true gives PASS (fail class null), anything else gives FAIL `send_unconfirmed`, whatever the status (`ok`, `preview`, ...) and whatever the case expects.
3. With `--routing`, a sent PASS is NOT routed: its case row keeps `route` null and stays PASS (a message the tester sent to themselves has no routed source). Unsent PASSes are routed as today.
4. The chat rule is by the CASE's tool name `send_chat_message`: a case of that tool whose result is absent, or unsent with status `preview`, is `PREVIEW-ONLY` (a verdict of its own, not a PASS and not a FAIL). A case of that tool with any other unsent result (`ok`, `error`, `refused`) is graded as before; a case of that tool with `sent` true takes rule 2. Every other tool with an absent result is still `FAIL` `not_run`. Name the tool in one constant.
5. Do not add a key to the graded file or an option to a subcommand: `preview_only` and the `PREVIEW-ONLY TOOLS:` line already exist and already list every tool whose verdict is PREVIEW-ONLY.

### Inputs you read (you do NOT edit them)

- The merged script and its tests `workflows/gateway_battery/tests/test_tool_battery.py` (the model for a test file: the script loaded by path, small inputs written inside the test with `tmp_path`) and `tests/test_tool_battery_route.py`.
- `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/fixtures/y2_census.json`, `y2_cases.json`, `y2_results.json`, `y2_routing.json`: the criterion AC1's fixture (5 tools: two sends with an agreeing read-back, two unsent previews, one plain read), and `y2_base_g22_*` and `y2_base_h6_*`: the baselines of the unchanged script that criterion AC2 compares byte for byte.
- The round-22 and round-23 battery fixtures under `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round22/fixtures/` and `round23/fixtures/` (criterion AC2 reads them). If any is absent in your worktree, `git sparse-checkout add` its folder.

### Steps

0. From the worktree root, `git rev-parse --show-toplevel` is your root. The worktree may lack `infra/aws/ec2/opal-gateway/app`, `workflows/atom_decomposition` and `workflows/gateway_battery`: your FIRST act is `git sparse-checkout add` of whichever is absent (the only sparse change you may make; the issuer pre-adds them).
1. Read `tool_battery.py` and `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y2_check.py` (the executable form of this section; read what each arm grades). Make the changes in the script, then the test file (at least 6 tests of your own, on small inputs written inside the test, not the issuer's fixtures), then the one changed assertion in `test_tool_battery.py`. Your tests cover at least: an agreeing read-back is PASS; no, null, false and null-agrees read-backs are `send_unconfirmed`; the chat tool with a preview or an absent result is PREVIEW-ONLY and another tool with an absent result is still `not_run`; a read-back on an unsent result is refused; a malformed read-back is refused; a sent PASS is not routed.
2. Run the three criteria in section 4 until each prints `RESULT: PASS`.

## 2. BOUNDS

1. You change only the files in `<paths>`. Do NOT edit the issuer's fixtures, checks or decomposition, `routing_table.py`, `cheatsheet.py`, `source_compare.py`, `members.yaml`, the catalog or its row files, the emitter, any file under `infra/`, the PRD, the round-22 and round-23 evidence and checks, or any other file under `workflows/`. No AWS call, no network call, no grant, no send, no deploy, no push.
2. Python 3.9, standard library only. ASCII only in code, comments, strings, output and data files. No type syntax newer than 3.9 (no `X | Y` annotations, no `match`). The commit gate runs `py_compile`, the naming gate and `ruff` for py39; it also refuses a strict `open()` without `errors=` on a file whose name or variable contains `log` or `catalog` (use `errors="replace"` where you read such a file).
3. The contract in section 1 is the whole specification. Where it is silent, do the smallest thing and say which in your report; do not widen the output.
4. The round-22 check `round22/checks/g_check.py` still holds an arm "G4 a send is a FAIL" that expects the class `sent`; that arm is SUPERSEDED by this ruling and will print FAIL after your change. Do not edit it and do not try to keep the old class: `y2.AC2` covers the same planted send (it must read FAIL with rc 1, class `send_unconfirmed`).
5. A commit through the naming gate needs a staged `.json` under this project's home if it must derive the project: your proof instance is one (commit it with, or before, the last code commit).
6. The checks are `org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y2.AC1.sh`, `.AC2.sh` and `.AC3.sh` (they run `y2_check.py` in the same folder). Do not edit any of them.
7. REFUSE a criterion you cannot meet as written, and report it with its measurement.

## 3. SURFACES

<paths>
workflows/gateway_battery/tool_battery.py
workflows/gateway_battery/tests/test_tool_battery_send.py
workflows/gateway_battery/tests/test_tool_battery.py
org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~85/**
org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/NFRA/NFRA_MCPINDEX/task-orders/NFRA_MCPINDEX.TO-MX-y-2.test-send-grading.md
</paths>

Rows go to `org/missions/D9/NFRA/NFRA_MCPINDEX/surprise-channel/investigations/INVESTIGATION_v1.md`:
- id `NFRA_MCPINDEX-Z-W85-S<k>` (`k` the next unused number of your slot);
- fabric `site-z`;
- `disarm_owner` `2.0.0_SA_COO~MI`;
- `surfaced_at` written as a full UTC timestamp (`date -u +%FT%TZ` at filing).

## 4. PROOF OF SPEC (literal; run from your worktree root, after step 2)

<proof_of_spec>
  <expected_criteria>AC1,AC2,AC3</expected_criteria>
  <criterion id="AC1" cell_refs="MX-y-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y2.AC1.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; on the fixture the sends with an agreeing read-back are PASS and the two unsent previews are PREVIEW-ONLY, the GRADE line reads PASS=3 PREVIEW-ONLY=2 FAIL=0 and the PREVIEW-ONLY TOOLS line names send_chat_message; a sent result with no, null, false or null-agrees read-back is FAIL send_unconfirmed; the chat tool with no result is still PREVIEW-ONLY while another tool with no result is not_run; a chat send without a read-back is send_unconfirmed; a sent PASS is not routed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MX-y-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y2.AC2.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line; the round-22 and round-23 h6 fixtures grade byte-identically (graded file and stdout) to the unchanged script's baselines; the round-22 planted send is FAIL rc 1 class send_unconfirmed; four malformed or misplaced read-backs are refused rc 2 with no output file; two runs give the same bytes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MX-y-2" judgment="false"><invocation>bash org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/2.0.0_SA_COO~MI/round25/checks/y2.AC3.sh; echo "exit=$?"</invocation><expect>the DENOMINATOR line (pytest rc=0, at least 28 passed) for test_tool_battery.py, test_tool_battery_route.py and test_tool_battery_send.py -- RESULT: PASS -- exit=0</expect></criterion>
  <instance_path>org/missions/D9/NFRA/NFRA_MCPINDEX/deliverables/0.9.0_WK_NFRA_MCPINDEX~85/NFRA_MCPINDEX.TO-MX-y-2.test-send-grading.proof_of_spec.json</instance_path>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

1. Write the proof instance. In its artifact rows, pin each produced file to the commit that carried it (the checker refuses `PENDING-THIS-COMMIT` for a file committed before the instance): commit the work first, then write the instance naming those commit hashes.
2. Append `<status>complete</status>` to this order file only if every criterion PASSes (if the commit gate refuses the flip, leave it and say so).
3. Commit through `.tools/safe-commit.sh` in two commits: (i) the work; (ii) the proof instance and the status flip.
4. Report once, with: what you built by part; every `RESULT:` line and `DENOMINATOR:` line of each criterion verbatim; the unit-test count; your commit shas; every place the contract was silent and what you did.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES (2.0.0_SA_COO~MI).** Round 25, workstream GATEWAY, worker ~85. Source: the CTO's round-24 analysis (`1.0.0_SA_CTO~Z`, 2026-10-20, msg 36225) item 5 and ruling (d); PRD v0.19 @7c42c0c743. Decomposition `org/missions/D9/NFRA/NFRA_MCPINDEX/decompositions/NFRA_MCPINDEX_DECOMP.round25-GATEWAY.md` (contract R25.3 Y2, frozen at the cut). Base dry-runs 2026-10-20: `y2.AC1` FAIL (1 of 12 arms ok: only the control "another tool with no result is still not_run" passes), `y2.AC2` FAIL on its new-behavior arms only (5 of 10 ok: the g22 and h6 byte-identity arms, and determinism, pass at the base; the planted send reads class `sent` and the four refusals exit 1), `y2.AC3` FAIL (test file absent). The issuer's scratch reference (a change of the merged script, the one changed assertion and eight tests, outside the repository) passes all three (AC1 12 of 12, AC2 10 of 10, AC3 30 passed); a planted mutant that ignores the read-back fails AC1 on five arms. CONTRACT CONFLICT settled by the issuer: the contract says the round-22/23 fixtures grade byte-identically, but the round-22 g4 arm "G4 a send is a FAIL" plants a `sent` result with no read-back, whose class legitimately moves from `sent` to `send_unconfirmed`; AC2 therefore compares the fixtures that carry no sent result byte for byte and grades the planted send separately. The round-22 `g4.AC1` will print one FAIL arm after this cell merges (superseded, not repaired). Gate limb that graded this order: the L6 gate at the issuance commit.

<status>issued</status>
<round>25</round>
<workstream>GATEWAY</workstream>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>complete</status>
