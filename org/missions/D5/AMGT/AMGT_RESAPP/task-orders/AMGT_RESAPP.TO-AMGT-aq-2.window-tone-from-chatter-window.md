# AMGT_RESAPP task order -- `AMGT-aq-2` -- FWD-36 TONE: THE CHATTER ROUTE SERVES TONE AND VOTERS FROM HARVST chatter_window

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aq-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~220</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- no new write; the route reads the gold table the HARVST builder already writes (amgt/harvest/gold/chatter_window).
comp-adversary: RUN by the issuer at the cut -- r67_served c24 FAILS at the base, local and deployed: 74 of 95 rows mismatch the 636-row chatter_window on 30, 90 and 365; every row serves tone null with 'window tone is not served on this route yet'.
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r67-220` (branch `wk-AMGT_RESAPP-220`, cut from the issuance commit with `--portal-ref a730d8ce`, so the
portal fixture the api tests read is present). Work and commit only there. Start every shell call with `cd /c/tmp/r67-220`: a call that
starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aq-2` (round 67, decomposition s.75; PRD v0.37 FWD-36, tone limb)

FWD-36: chatter rows serve articles_total, voters and tone from HARVST gold, never computed at request time. HARVST now
serves `chatter_window` (`lib/research/harvest/window_tone.py`, TABLE `chatter_window`, schema GOLD_WINDOW_SCHEMA: security_key,
window_days, ..., voters, tone; tone is None iff 0 voters). Today the chatter route serves tone null with "window tone is not served on
this route yet" (`lib/research/api/rolling_windows.py` TONE_REASON).

1. **The read:** `/lead-panel/timeseries/collected/chatter?days=30|90|365` (default 30) reads the LATEST `chatter_window` part
   through the seam the route already uses for gold (`publication_gold._latest_gold_snapshot_rows_cached` with `columns=`).
   - It serves each row's `tone` and `voters` exactly as the table holds them for (security_key, window_days).
2. **0 voters:** `tone` is null and `tone_reason` is exactly "no clear tone".
3. **The old reason** "window tone is not served on this route yet" is no longer served.
   - A name with no table row serves `tone` null with a plain reason saying the window table holds no row for it.
4. **The plant test** `lib/research/api/tests/test_window_tone_route.py`:
   - a planted chatter_window serves its tone and voters;
   - 0 voters reads "no clear tone";
   - a missing row serves its reason.

Run `lib/research/api/tests/` before your commit and report its last line. **Stamp any surprise row's `surfaced_at` with `date -u
+%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W220-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. articles_total, by_month, rank and every other chatter field keep their values; only tone, voters and tone_reason change.
3. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~220/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 900)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python -m pytest -v -p no:cacheprovider lib/research/api/tests/test_window_tone_route.py; echo "exit=$?"</invocation><expect>every plant case passes (tone and voters from the table; 0 voters 'no clear tone'; a missing row with its reason); and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round67/checks/r67_served.py --cell c24 --where local; echo "exit=$?"</invocation><expect>C1 PASS on days=30, 90 and 365 (0 mismatches, 0 old reasons, 0 rows without a table row); R67 C24 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="AMGT-aq-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round64/checks/r64_served.py --cell c9 --where local; echo "exit=$?"</invocation><expect>R64 C9 SERVED: YES (the chatter windows otherwise unchanged); and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~220 <0.9.0_WK_AMGT_RESAPP~220@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~220/AMGT_RESAPP.TO-AMGT-aq-2.window-tone-from-chatter-window.proof_of_spec.json`.
Report once:
- the commit hash
- every criterion's output lines
- the api suite's last line
- the functions you changed
- any row

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-66 analysis @d76db3486c ruling 4; HARVST chatter_window (COO~H msg 29087). Served by aq-5.

<status>pending</status>
<round>67</round>
<slot>0.9.0_WK_AMGT_RESAPP~220</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-04 ~19:5xZ, drain re-entered after the site-Z crash):** CLOSED WITH AC2 FAIL.
- Worker ~220 commit `7f6ddcb942`, proof-of-spec-check VALID (rc=0). The final report was lost with the pre-crash session.
- AC1 PASS 5 of 5. AC3 PASS 4 of 4 clauses. AC2 FAIL on ONE clause: per window (30/90/365) 95 rows served, 74 match the
  table (0 mismatches, 0 old reasons), and 21 covered names have no chatter_window row.
- The route change is right: it serves the 21 their plain no-row reason (item 3). The gap is the producer's build list
  (`lib/research/harvest/window_tone.py`; 212 names, 21 covered missing), outside this cell's `<paths>`. Row
  `AMGT_RESAPP-Z-W220-S1` carries it to the round-67 analysis. Served by aq-5.

<status>complete</status>
