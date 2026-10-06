# AMGT_RESAPP task order -- `AMGT-au-6` -- THE LEAD PANEL LOADS FROM STORED READS, NOT REQUEST-TIME COMPUTE (ANDREW-DIRECT 2026-10-05)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-au-6</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~236</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only. A fix that needs a NEW producer or served file is a row, not a build.
comp-iam: DECLARED-NOT-APPLICABLE -- reads only stores the function already reads; a NEW S3 read path is named in your report.
comp-adversary: RUN by the issuer at the cut -- r71_latency c38 on deployed, warm: collected/chatter 9.4-9.8 s at days 30/90/365; rankings trending/breakout price 3.7-4.9 s; all 9 over 2,000 ms.
EGRESS CLASS, declared: NONE.
</preflight>

**Your worktree:** `C:/tmp/r71-236` (branch `wk-AMGT_RESAPP-236`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r71-236`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-au-6` (round 71, decomposition s.79)

**Andrew, verbatim** (2026-10-05 ~15:0xZ, record
`org/tier1_exec/2.0.0_SA_COO/deliverables/ANDREW_DIRECT_20261005_150xZ_SECURITY_ANALYSIS_ALL_OPAL_EMPLOYEES_REQUIREINTERNAL_LEADPANEL_LOAD_TO_COO_Z.md`):
"I suspect that some lambdas are doing live computation when the served file should be precomputed. Specifically ... what appears in
the lead panel; the chatter/price views take almost a minute to load."

The Lead Panel reads `/api/scoped/amgt/lead-panel/timeseries/collected/chatter?days=30|90|365` and
`/lead-panel/rankings/{trending,breakout}/price` (default, `?days=90`, `?days=365`), in `lib/research/api/scoped_amgt.py`.

1. **Before any edit,** capture the nine bodies locally into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/before/` (one JSON each), and profile each route: where the
   time goes (S3 reads, objects listed, decode, per-name loops, compute). Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/PROFILE.md` with a per-phase table.
2. **Fix it so the request serves stored results:**
   - read an already-stored precomputed object where one exists (a gold table or a published file the producer writes);
   - read fewer objects and fewer columns; cache a per-container result keyed on the stored object's version;
   - never recompute at request time what a producer already stored.
   If the only real fix is a NEW producer or served file, do not build it: file ONE row naming the producer, the file and the measured
   gain, and do what is possible inside the route.
3. **The values do not change** (AC2): the nine bodies after the change equal the `before/` bodies, ignoring `generated_at`.
4. Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/after_equal.py`, which prints `EQUAL n of 9` and exits 0 only on 9 of 9.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W236-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no new producer, no schedule, no vendor or model call, no portal write.
2. No served value changes (AC2).
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-au-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round71/checks/r71_latency.py" --where local --bar-ms 6000; echo "exit=$?"</invocation><expect>every one of the 9 reads prints status [200] and a worst warm time under 6000 ms; C1 PASS; R71 C38 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-au-6"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 9 of 9; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~236 <0.9.0_WK_AMGT_RESAPP~236@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~236/AMGT_RESAPP.TO-AMGT-au-6.lead-panel-load.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the PROFILE.md before/after table;
- any new S3 read path;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** ANDREW-DIRECT 2026-10-05 ~15:0xZ via 2.0.0_SA_COO~D msg 29618. Local bar measured at the cut (see issuance). Deployed bar 2,000 ms graded at au-7.

<status>pending</status>
<round>71</round>
<slot>0.9.0_WK_AMGT_RESAPP~236</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-05 ~18:0xZ):** CLOSED -- drained @066bbc25d2. AC1: c38 local 9 of 9 under 6000 ms (warm 0.15-1.0 s). AC2: EQUAL 9 of 9. The api suite on the shared tree after all four build drains reads 612 passed. proof VALID. Row Z-W236-S1 INERT (the cold-container producer remainder). The deployed 2,000 ms bar is au-7's AC2.

<status>complete</status>
