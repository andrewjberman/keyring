# AMGT_RESAPP task order -- `AMGT-bj-3` -- READ THE OVERLAY'S HANDLER TIME OVER A DECLARED WINDOW, BEFORE AND AFTER THE FEED APPLY (A READ, NOTHING CHANGED) -- STAGED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bj-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~405</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bj-3.read-the-overlay-handler-time-over-a-declared-window-before-and-after-the-feed-apply</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a read; nothing is scheduled.
comp-iam: DECLARED-NOT-APPLICABLE -- Logs Insights reads of ONE log group and one function-configuration read; no write.
comp-adversary: RUN at the cut -- r103_window_read.py --auto-split 2026-10-13T16:17:06Z reads `R103 WINDOW READ: 2 window(s) read, 0 not read` on the live function (CodeSha256 bKCGUhXp.., LastModified 2026-10-13T16:17:06Z): the `before` window is empty by construction (it ends where it starts) and the `after` window read 740 overlays, median 489 ms, p95 779 ms, 3 over 4,000 ms (the first overlay on a container); the same instrument reads `overlays 0 (the denominator is zero)` on a window before the phase lines existed.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/dev/wk-resapp-405` (branch `wk-AMGT_RESAPP-405`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-405`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers for the wrong tree.

## 1. THE ACT -- `AMGT-bj-3` (round 103, decomposition s.111): A READING, NOTHING CHANGED

CTO~DELL1 round-102 analysis item 2: "bi-3's steady state, with a window: the warm-overlay figure is restated over a declared window (start, end, trading-calendar basis), with its denominator and
its median and 95th percentile, read from the logs." The overlay's `read_security_overlay` phase is printed once per overlay request since the apply of 2026-10-13T16:17:06Z (round 102's
`AMGT-bi-2`); `AMGT-bj-2`'s apply is the second boundary. Run the instrument ONCE, alone:

    python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_window_read.py --auto-split 2026-10-13T16:17:06Z     (the output file is org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~405/BJ3_WINDOW_READ_20261014.txt)

It reads the function's `LastModified` (the apply of `AMGT-bj-2`) and declares two windows: `before` (2026-10-13T16:17:06Z to that apply: the round-102 build, whole-table feed read) and `after`
(that apply to now). Per window it prints the start and end in UTC, the trading days the window touches (`lib.trading_calendar`), the DENOMINATOR (overlay requests), the median and the 95th
percentile of the overlay's handler-internal milliseconds, the maximum, how many are over 4,000 ms (the first overlay on a container) and what share, and the function's REPORT count and how many
carry an Init Duration. **AC1's invocation IS the run** (it writes the output file and prints its lines); run it once. Write NOTHING else; the output file is the reading.

Your report states, in prose, ONLY what the numbers show (the two medians, the two 95th percentiles, the two denominators, the share over 4,000 ms) and what they do NOT show (that the traffic in
these windows is the issuer's and the workers' own deliberate requests, not organic use: a window's median is a property of those requests).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W405-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Reads only (Logs Insights over the one log group, one function configuration read). No invoke, no deploy, no store write, no schedule, no Bloomberg, SEC or model call; no S3 delete, ever.
2. No `bun`, `npm` or `pip install`. Standing: no push of shared branches.
3. The reading names no client, firm or account.
4. A window that does not read (`NOT READ`) is a finding, never a zero.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~405/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bj-3"><invocation>cd C:/dev/wk-resapp-405 &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round103_prep/checks/r103_window_read.py" --auto-split 2026-10-13T16:17:06Z &gt; "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~405/BJ3_WINDOW_READ_20261014.txt" 2&gt;&amp;1; grep -E "^(function CodeSha256|WINDOW |R103 WINDOW READ)" "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~405/BJ3_WINDOW_READ_20261014.txt"</invocation><expect>one `function CodeSha256 ... | LastModified ...` line, a `WINDOW before` line and a `WINDOW after` line (each with its UTC start and end, the trading days, and either the overlay count with median, p95, max and the share over 4000 ms, or `overlays 0 (the denominator is zero ...)`), then `R103 WINDOW READ: 2 window(s) read, 0 not read`</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bj-3" judgment="true"/>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~405 <0.9.0_WK_AMGT_RESAPP~405@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~405/AMGT_RESAPP.TO-AMGT-bj-3.read-the-overlay-handler-time-over-a-declared-window-before-and-after-the-feed-apply.proof_of_spec.json`
with `to_id` equal to the `<to_id>` line above, character for character (AC2 is a judgment criterion: record it as the checker's grammar requires, UNVERIFIABLE-BY-INSTRUMENT, naming the CVO).
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line.
Report once:
- the commit hash;
- criterion AC1's output lines;
- the two windows' lines in full;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CVO's round-102 note (C-S113): "steady state rests on 3 warm overlays with no window; the CVO's log window holds 737 warm overlays (median 0.49 s) under a different
condition. The Saturday close must state a window and a denominator, not three requests." AC2 is the CVO's judgment (the reading states only what its numbers show; the traffic's provenance is
named). The Saturday read is the organic negative arm and is not waited on. STAGED until `AMGT-bj-2` is complete (the `before` and `after` boundary is its apply's `LastModified`).

<status>staged</status>
<status>withdrawn -- 2026-10-13T18:2xZ by the issuer (2.0.0_SA_COO~R1): DEFERRED by the CTO's ROUND_ANALYSIS.round102.md ADDENDUM 1 item 5 (msg 5021): "section 2 items 2 (the steady-state window) and 3 (the admission-table tool) are DEFERRED, since V1 comes first". No worker was seated and nothing ran. The instrument (`round103_prep/checks/r103_window_read.py`, `--auto-split`) and this order's text stay as written; it is re-cut, as a new order, when the CTO re-lists the window read. The CVO's round-102 note C-S113 (a stated window and denominator for steady state) is carried, not dropped.</status>
<round>103</round>
<slot>0.9.0_WK_AMGT_RESAPP~405</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
