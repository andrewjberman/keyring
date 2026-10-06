# AMGT_RESAPP task order -- `AMGT-ay-3` -- THE NEXT COLD CUT: THE FIRST CHATTER REQUEST RESOLVES NAMES WITHIN 300 MS, NO SPEND (CTO RULING 5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ay-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~259</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: DECLARED-NOT-APPLICABLE -- the same stored names, classifications and model blocks the route already reads.
comp-adversary: RUN by the issuer at the cut -- the deployed cold chatter read is 3.7-4.7 s; its largest cold phase is `names` at 1,220 ms (AE~A's phase table on 0MZWPl7n). r75 c60 base: see the issuance commit.
EGRESS CLASS, declared: NONE. No vendor, SEC or model call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r75-259` (branch `wk-AMGT_RESAPP-259`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r75-259`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-ay-3` (round 75, decomposition s.83)

CTO ruling 5. `read_monthly_chatter` (`lib/research/api/monthly_chatter.py` ~`:311`) logs `AMGT_PHASE route=chatter
phase=names` around `_display_names(covered)` (~`:86`). That function resolves each covered key's identity, reads the
classifications for every ticker, then reads model-block names for the keys still unnamed.
1. **Cut the phase.** Read once and in parallel what is now read serially. Read only what the covered keys need. Do not change a name.
2. **Bodies equal.** Before any edit, capture `/lead-panel/timeseries/collected/chatter` at days 30/90/365 into
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~259/before/`. `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~259/after_equal.py` prints `EQUAL n of 3`; drift from a snapshot landing is shown as DRIFT.
3. **Write only** `lib/research/api/monthly_chatter.py` and new modules under `lib/research/api/`. `scoped_amgt.py` is read only for
   this cell.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W259-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor, SEC or model call, no portal write.
2. No served value changes (AC2).
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/monthly_chatter.py
lib/research/api/names_read.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~259/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ay-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round75/checks/r75_served.py" --cell c60 --where local; echo "exit=$?"</invocation><expect>fresh-process names phase within 300 ms; C1 PASS; R75 C60 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ay-3"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~259/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 3 of 3; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~259 <0.9.0_WK_AMGT_RESAPP~259@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~259/AMGT_RESAPP.TO-AMGT-ay-3.names-phase-cut.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the names phase before/after (fresh process);
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-74 analysis item 4, ruling 5. The deployed cold read is measured at ay-5.

<status>pending</status>
<round>75</round>
<slot>0.9.0_WK_AMGT_RESAPP~259</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>

**ISSUER CLOSE (2.0.0_SA_COO~Z, 2026-10-06 ~10:5xZ):** CLOSED -- drained @42fd324fb3. r75 c60 local YES (the names phase logs 0 by overlap, row Z-W259-S1); the first chatter request locally 4.2-4.5 -> 3.5-4.0 s; bodies EQUAL 3 of 3.

<status>complete</status>
