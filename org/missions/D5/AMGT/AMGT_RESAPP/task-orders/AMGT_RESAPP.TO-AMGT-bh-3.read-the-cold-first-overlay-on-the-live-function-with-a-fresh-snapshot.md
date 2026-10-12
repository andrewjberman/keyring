# AMGT_RESAPP task order -- `AMGT-bh-3` -- READ, DO NOT CHANGE: THE COLD FIRST OVERLAY ON THE LIVE FUNCTION WITH A FRESH SNAPSHOT -- STAGED UNTIL 2026-10-12T12:40Z

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bh-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~399</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bh-3.read-the-cold-first-overlay-on-the-live-function-with-a-fresh-snapshot</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; nothing is scheduled (the snapshot's own schedule writes it at 12:30 UTC on weekdays).
comp-iam: DECLARED-NOT-APPLICABLE -- GET-shaped direct invokes of one function, one S3 GET of the snapshot, one Logs Insights count over one log group; no write.
comp-adversary: RUN at the cut, against the literal strings below, before the Monday write (snapshot 65 hours old): r101_cold_live.py reads 'snapshot ... current False' and 'R101 COLD LIVE: NO' (ASML_NA_Equity 22.4 s with a cold container), r101_snapshot_equal.py reads 'R101 SNAPSHOT EQUAL: NOT CURRENT'; both exit 1. The same two after the Monday write are what this order reads.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-399` (branch `wk-AMGT_RESAPP-399`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-399`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bh-3` (round 101, decomposition s.109): A READING, NOTHING CHANGED

CTO~DELL1 round-100 analysis ADDENDUM 1 item (a). The issuer's GO is given AFTER 2026-10-12T12:40Z, when the scheduled writer (`cron(30 12 ? * MON-FRI *)`) has written a snapshot dated that morning.
Run, in this order, from your worktree, each exactly as the criteria name it, and put the whole of each one's output in the file `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~399/BH3_COLD_LIVE_OUTPUT_20261012.txt` under a heading `## <script name>` with the run's
UTC start time beside it:

1. `r101_snapshot_equal.py` -- the stored snapshot equals the live recompute (the first arm of the pair of the calendar rule).
2. `r101_cold_live.py` -- the cold first overlay on the LIVE function for `ASML_NA_Equity` and `ADBE_US_Equity`: the handler time, whether the container was cold, how many invocations of the
   function the preceding 15 minutes held, and the snapshot's `generated_at` and age beside them. **If the 15 minutes before its first invoke held invocations the script says NOT QUIET: that is
   a real result, not a failure to retry.** Do NOT run it twice to find a quiet moment, and do not invoke the function yourself for any other purpose in the quiet window.
3. After the two runs, in the same file, one short paragraph `## Reading` that states ONLY what the printed numbers show: the snapshot's date, the handler times, the cold flags, and what they do NOT
   show (one request pair is not a rate; the live logs of the day are `AMGT-bh-4`'s).

WRITE NOTHING but the output file and, if a premise fails, a surprise row. No other invoke, no AWS call but the ones the two scripts make, no Bloomberg call.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W399-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (one S3 GET, one Logs Insights count, two overlay invokes). No deploy, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`.
3. Standing: no push of shared branches.
4. The output names no client, firm or account; a security key is not a client name.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~399/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bh-3"><invocation>cd C:/dev/wk-resapp-399 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round101_prep/checks/r101_snapshot_equal.py" | tail -3; echo "exit=${PIPESTATUS[0]}"</invocation><expect>the last line reads `R101 SNAPSHOT EQUAL: YES` (after the Monday write the stored snapshot is current under the checkout's rule and equals the recompute) and `snapshot generated_at 2026-10-12T12:30Z` is printed above it; and exit=0. A `NO` prints each differing row's columns, which the reading reports whole.</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bh-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~399 <0.9.0_WK_AMGT_RESAPP~399@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~399/AMGT_RESAPP.TO-AMGT-bh-3.read-the-cold-first-overlay-on-the-live-function-with-a-fresh-snapshot.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- AC1's output lines and the whole `r101_cold_live.py` output;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the natural experiment: before Monday 2026-10-12 12:30Z the snapshot is 65 hours old and every cold overlay computes the coverage view live (22 to 28 s on the live function); after
the scheduled write the SAME function, unchanged, has a current snapshot under the OLD rule. If the cold overlay reads well under 20 s then, the lever is the snapshot's age and `AMGT-bh-1` is the
fix for the weekend; if it still reads 20 s or more, the snapshot is not the lever on Lambda and `AMGT-bh-2` does not go. AC2 is the CVO's judgment (the reading states only what the numbers show).
STAGED: the GO is the issuer's after 12:40Z.

<status>staged</status>
<round>101</round>
<slot>0.9.0_WK_AMGT_RESAPP~399</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
