# AMGT_RESAPP task order -- `AMGT-bh-4` -- READ, DO NOT CHANGE: THE FUNCTION'S OVER-20-SECOND INVOCATIONS OVER THE FIRST WEEKDAY AFTER THE S3-CLIENT BUILD (`AMGT-bg-3`'s DAY-AFTER CLOSE) -- STAGED UNTIL 2026-10-13T12:40Z

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bh-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~400</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bh-4.read-the-first-weekday-of-the-s3-client-build-from-the-function-log</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- CloudWatch Logs Insights reads of ONE log group (`logs:StartQuery`, `logs:GetQueryResults`) and one function-configuration read; no write.
comp-adversary: RUN at the cut -- r99_overlay_tail_reading_check.py (the round-99 shape check, reused unchanged) reads NO at the base (no reading exists) and YES against a throwaway sample reading; its method is the round-99 reading's, which the issuer's own queries reproduced.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-400` (branch `wk-AMGT_RESAPP-400`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-400`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bh-4` (round 101, decomposition s.109): A READING, NOTHING CHANGED

The CTO's `AMGT-bg-3` close (ADDENDUM 1, msg 4262): "the day after: invocations over 20 s and 'Connection pool is full' warnings counted over a full day, against 53 and 49". The S3-client build
(`opal-amgt-scoped-api` `42z0tn68..`, applied 2026-10-12T04:17:52Z) was live for the WEEKEND tail's last hours and for Monday. The reference day (round 99) was a weekend day with a 65-hour-old
snapshot; **the window to read is the first full WEEKDAY after the build and after Monday's scheduled snapshot write: 2026-10-12T12:40Z to 2026-10-13T12:40Z** (state both ends in UTC; end the
window earlier ONLY if the function's code changed inside it, and say so: read `LastModified` at the start and at the end).

READ the function's own log group `/aws/lambda/opal-amgt-scoped-api` for that window by the round-99 method, exactly:

1. **Counts** with Logs Insights over `@type = "REPORT"`: invocations; those with `@duration > 20000`; those with `@initDuration > 0` among the over-20 s; and, over the over-20 s
   invocations' own log lines, those carrying a `Connection pool is full` warning. Also the count of invocations OVER ALL of the window carrying that warning
   (`filter @message like /Connection pool is full/ | stats count_distinct(@requestId)`).
2. **The over-20 s list** and, for those request ids ONE query of their own log lines (`filter @requestId in [<ids>] | fields @requestId, @timestamp, @message | sort @requestId, @timestamp asc | limit 10000`):
   whether a route or a security key is named; the gap from START to the first pool-full warning where there is one. Where NO line names a route or key, the route line reads `ROUTE none attributable`
   with that reason. NEVER infer a route from the duration or the hour.
3. **Beside**: `MINUTE <UTC minute> | over20=<n> | invocations=<n>` for each minute that holds an over-20 s invocation.
4. **Against the reference**: round 99's reading (53 of 32,528 over 20 s, 12 cold, 49 with a pool-full warning, 0 attributable; the file
   `deliverables/0.9.0_WK_AMGT_RESAPP~395/BF2_OVERLAY_TAIL_READING_20261011.md`): state each count beside its round-99 number AND each as a rate per 1,000 invocations. **The window's own
   invocation count differs from the reference's: a rate is graded, a raw count is not.**
5. **Why**: one short paragraph under `## Counts` stating only what the numbers show, and what they do NOT show.

Helper: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_logq.py "<query>" <hours> <rows>` is the issuer's (it prints at most the rows asked for; write your own for the over-20 s list). Logs Insights queries are asynchronous: poll
until `Complete`; a `Failed`, `Cancelled` or `Timeout` status is a finding, never a zero. Write ONE reading to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~400/BH4_FIRST_WEEKDAY_READING_20261013.md` in the shape `checks/r99_overlay_tail_reading_check.py` grades (its
docstring is the template; headings Window, Counts, Routes, Names, Beside, Sources, Surfaces, Not changed; the Counts block carries the seven counts it names).

WRITE NOTHING anywhere but the reading file and, if a premise fails, a surprise row. No invoke of the function, no other AWS call than the log calls and the one configuration read, no Bloomberg call.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W400-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (CloudWatch Logs Insights over the one log group, one function configuration read). No invoke, no deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The reading names no client, firm or account; a security key is not a client name.
5. A surface you cannot read is a finding in the reading (`NOT READ: <why>`), never a reason to guess.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~400/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bh-4"><invocation>cd C:/dev/wk-resapp-400 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_overlay_tail_reading_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~400/BH4_FIRST_WEEKDAY_READING_20261013.md"; echo "exit=$?"</invocation><expect>PASS S1 to S9 (every heading present, in order, non-empty; the window and the function's hash and time; the seven counts with both splits summing to OVER 20 s; the ROUTE lines or none attributable with a reason; NAME lines or none attributable; at least one MINUTE line; two denominated sources; two surfaces read and one not read; WRITES: none); arms passed 9 of 9; R99 OVERLAY TAIL READING SHAPE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bh-4" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~400 <0.9.0_WK_AMGT_RESAPP~400@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~400/AMGT_RESAPP.TO-AMGT-bh-4.read-the-first-weekday-of-the-s3-client-build-from-the-function-log.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's output lines;
- the COUNTS block with each count's rate per 1,000 invocations beside the round-99 reference, the ROUTE and NAME lines and the first five MINUTE lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's `AMGT-bg-3` close, arm 3 (msg 4262): the day-after count, "against 53 and 49". The reference day was a weekend with a 65-hour-old snapshot, so the comparison is confounded
by the snapshot's state; the window is therefore the first weekday after Monday's write and the comparison is a RATE. If `AMGT-bh-2` applies inside the window, the window ends at that apply (the
reading says so), because that apply changes the function. AC2 is the CVO's judgment (the counts follow from the queries, the splits sum, no route is inferred, the rate comparison is stated).
STAGED: the GO is the issuer's at or after 2026-10-13T12:40Z.

<status>pending -- GO 2026-10-13T12:4xZ by the issuer (2.0.0_SA_COO~R1): the window 2026-10-12T12:40Z to 2026-10-13T12:40Z has closed; the function's code did NOT change inside it (get-function-configuration at 12:41Z: CodeSha256 42z0tn68TZjuk8awBclnMii0k+FX2Pw2bw7iN9Xitz0=, LastModified 2026-10-12T04:18:21Z, before the window opened; AMGT-bh-2 has not applied), so the window is the full 24 hours. Reads only; worker ~400 at C:/dev/wk-resapp-400.</status>
<round>101</round>
<slot>0.9.0_WK_AMGT_RESAPP~400</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
