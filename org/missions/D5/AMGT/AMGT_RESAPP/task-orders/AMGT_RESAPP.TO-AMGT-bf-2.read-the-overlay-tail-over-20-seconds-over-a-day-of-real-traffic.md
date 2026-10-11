# AMGT_RESAPP task order -- `AMGT-bf-2` -- READ, DO NOT CHANGE: THE SCOPED API'S SLOW INVOCATIONS (OVER 20 SECONDS) OVER THE LAST DAY OF REAL TRAFFIC

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bf-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~395</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bf-2.read-the-overlay-tail-over-20-seconds-over-a-day-of-real-traffic</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read-only reading; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- CloudWatch Logs Insights reads of ONE log group (`logs:StartQuery`, `logs:GetQueryResults`); no write, no other service.
comp-adversary: RUN at the cut -- r99_overlay_tail_reading_check.py reads NO at the base (no reading exists) and YES against a throwaway sample reading that carries every heading, the seven counts with both splits summing to OVER 20 s, a route line (or none attributable with its reason), a name line, a MINUTE line, two denominated sources, two read surfaces and one not read, and WRITES: none. The issuer's own probe at the cut read the log group (24 h): 31,878 REPORT lines, 53 over 20 s, the maximum 29,000 ms, 202 with an init duration; the over-20 s invocations' own log lines carry no request path and (in the two read) a 'Connection pool is full' warning.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-395` (branch `wk-AMGT_RESAPP-395`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-395`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bf-2` (round 99, decomposition s.107): A READING, NOTHING CHANGED

CTO~DELL1 round-98 analysis item 2 and the be-1 CTO half ADDENDUM 1: "the tail over 20 s per name over a day of real traffic, with the slowest names and why. Read only." The function
`opal-amgt-scoped-api` (us-east-1, 29 s timeout) serves the Security Analysis page; on 2026-10-11 one overlay request ran into the timeout after a redeploy and 53 invocations in 24 hours ran
over 20 s. This order READS the function's own log group `/aws/lambda/opal-amgt-scoped-api` for the LAST 24 HOURS (end the window at the moment you start; state both ends in UTC):

1. **Counts** with Logs Insights over `@type = "REPORT"`: invocations; those with `@duration > 20000`; those with `@initDuration > 0` (cold) among the over-20 s. (The issuer's probe: 31,878,
   53, 202 all-cold; yours is the one that counts.)
2. **The over-20 s list** (`fields @timestamp, @requestId, @duration, @initDuration, @maxMemoryUsed | sort @timestamp asc`), then for those request ids ONE query of their own log lines
   (`filter @requestId in [<ids>] | fields @requestId, @timestamp, @message | sort @requestId, @timestamp asc | limit 10000`). From those lines read, per invocation: whether a route or a
   security key is named (search each message for `/api/scoped/amgt/`, `_Equity` and `route=`); whether a `Connection pool is full` warning is present and the time of its first line after START
   (the gap from START is where the time went before the fan-out). Where NO line names a route or key, say so: the count is UNATTRIBUTED and the route line reads `ROUTE none attributable`
   with that reason. NEVER infer a route from the duration or the hour.
3. **Beside**: for each minute that holds an over-20 s invocation, `MINUTE <UTC minute> | over20=<n> | invocations=<n>` where `invocations` is that minute's REPORT count (one more Logs
   Insights query, `stats count(*) by bin(1m)` over those minutes, or over the whole window and filtered).
4. **Why**: in the reading, a short paragraph under `## Counts` stating only what the numbers show (the share with a pool-full warning, the share cold, the minutes' concurrency, the gap
   from START to the first warning), and what they do NOT show.

Helper: `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_logq.py "<query>" <hours> <rows>` (boto3; prints the status, the statistics and up to `<rows>` result rows) is the issuer's; use it or write your own. Logs Insights
queries are asynchronous: poll `get-query-results` until `Complete`; a `Failed`, `Cancelled` or `Timeout` status is a finding, never a zero.

Write ONE reading to `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~395/BF2_OVERLAY_TAIL_READING_20261011.md` in the shape `checks/r99_overlay_tail_reading_check.py` grades (its docstring is the template; headings Window, Counts, Routes, Names, Beside,
Sources, Surfaces, Not changed). The function's CodeSha256 and LastModified at the END of the window go under `## Window` (`aws lambda get-function-configuration` of that one function, or
boto3 `get_function_configuration`). Under `## Surfaces` name every surface you read and at least one you did NOT (the API gateway's or function URL's own access log, the S3 request log,
the client's side).

WRITE NOTHING anywhere but the reading file and, if a premise fails, a surprise row. No invoke of the function, no other AWS call than the two log calls and the one configuration read, no
Bloomberg call.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W395-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (CloudWatch Logs Insights over the one log group, one function configuration read). No invoke, no deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg
   call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The reading names no client, firm or account; a security key (`<TICKER>_<EXCH>_Equity`) is not a client name and may be printed.
5. A surface you cannot read is a finding in the reading (`NOT READ: <why>`), never a reason to guess.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~395/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bf-2"><invocation>cd C:/dev/wk-resapp-395 &amp;&amp; python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round99_prep/checks/r99_overlay_tail_reading_check.py" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~395/BF2_OVERLAY_TAIL_READING_20261011.md"; echo "exit=$?"</invocation><expect>PASS S1 (every heading present, in order, non-empty), PASS S2 (the window and the function's hash and time), PASS S3 (the seven counts, both splits summing to OVER 20 s), PASS S4 (the ROUTE lines sum to ATTRIBUTED or none attributable with a reason), PASS S5 (NAME lines or none attributable), PASS S6 (at least one MINUTE line), PASS S7 (two denominated sources), PASS S8 (two surfaces read, one not read), PASS S9 (WRITES: none); R99 OVERLAY TAIL READING SHAPE: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bf-2" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~395 <0.9.0_WK_AMGT_RESAPP~395@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Write any python or multi-line file with the Write tool. Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~395/AMGT_RESAPP.TO-AMGT-bf-2.read-the-overlay-tail-over-20-seconds-over-a-day-of-real-traffic.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's output lines;
- the COUNTS block, the ROUTE and NAME lines and the first five MINUTE lines;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO~DELL1 round-98 analysis section 3 item 2 and be-1 CTO half ADDENDUM 1 (msg 4153): "round 99 reads the overlay tail over 20 s per name over a day of real traffic before any remedy". The probe at the cut found the function logs NO request path, so per-name attribution may be impossible from this plane; the reading says so rather than inferring. A remedy (a pool size, a read order) is a later cell under its own pair. AC2 is the CVO's judgment (the counts follow from the queries, the splits sum, no route is inferred, the not-read surfaces are named).

<status>complete -- 2026-10-11T23:4xZ by the issuer (2.0.0_SA_COO~R1): wk-AMGT_RESAPP-395 @038df2c8d3 merged, proof instance VALID; issuer re-run: AC1 R99 OVERLAY TAIL READING SHAPE YES (9 of 9) and my own Logs Insights queries over the same log group reproduce the reading's counts (32,528 REPORT lines, 53 over 20 s, 12 cold, 49 with a pool-full warning, 0 naming a route or a security key); AC2 is the CVO's judgment, ungraded.</status>
<round>99</round>
<slot>0.9.0_WK_AMGT_RESAPP~395</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
