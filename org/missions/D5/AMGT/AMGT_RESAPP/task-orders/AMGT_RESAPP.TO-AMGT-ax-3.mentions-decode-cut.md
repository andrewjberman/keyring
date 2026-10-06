# AMGT_RESAPP task order -- `AMGT-ax-3` -- THE COLD CUT: THE FIRST CHATTER REQUEST DECODES MENTIONS WITHIN 500 MS, NO SPEND (CTO RULING 5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ax-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~254</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the same gold mention object the route already reads.
comp-adversary: RUN by the issuer at the cut -- r74 c54 FAILS (local, a fresh process): mentions decode 1,290 ms (deployed up to 3,720 ms, now the largest cold phase).
EGRESS CLASS, declared: NONE. No vendor or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r74-254` (branch `wk-AMGT_RESAPP-254`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r74-254`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ax-3` (round 74, decomposition s.82)

CTO ruling 5. `lib/research/api/monthly_chatter.py` (~`:287-297`) reads the gold `article_security_mention` snapshot
through `pool_reader._gold_latest_snapshot_rows` and decodes every row and column into Python dicts on the first request.
1. **Cut the decode.** Read only the columns the route uses (pyarrow column projection), filter to the window's months and the covered
   keys before materialising, and keep the arrow table (or numpy arrays) instead of per-row dicts where the aggregation allows.
   Do not change the counts.
2. **Bodies equal.** Before any edit, capture `/lead-panel/timeseries/collected/chatter` at days 30/90/365 into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~254/before/`.
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~254/after_equal.py` prints `EQUAL n of 3`.
3. **The phase line stays:** `AMGT_PHASE route=chatter phase=mentions decode ms=<n>` (aw-1's) measures the cut.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W254-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No served value changes (AC2).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
lib/research/coverage/pool_reader.py
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~254/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ax-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round74/checks/r74_served.py" --cell c54 --where local; echo "exit=$?"</invocation><expect>fresh-process mentions decode under 500 ms; C1 PASS; R74 C54 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ax-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~254/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 3 of 3; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~254 <0.9.0_WK_AMGT_RESAPP~254@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~254/AMGT_RESAPP.TO-AMGT-ax-3.mentions-decode-cut.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the phase before/after;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-73 analysis item 3, ruling 5. The deployed cold read is measured at ax-5.

<status>pending</status>
<round>74</round>
<slot>0.9.0_WK_AMGT_RESAPP~254</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~07:0xZ):** CLOSED -- drained @aaed0da1f7. On the shared tree, r74 c54 local YES (307 ms fresh-process mentions decode, from 1,290); api 666 passed. Worker AC2: EQUAL 3 of 3 (days30 drift from a snapshot landing noted).

<status>complete</status>
