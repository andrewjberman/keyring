# AMGT_RESAPP task order -- `AMGT-aw-1` -- THE COLD PATH PROFILED BY PHASE AND ITS DOMINANT PHASE CUT, NO SPEND (CTO RULING 1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-aw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~245</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; request-time code and tests only.
comp-iam: RUN by the issuer at the cut -- the cut reads the 23 names' stored `raw/bloomberg/<KEY>/.../refdata.json`; NAME the exact prefix in your report (aw-7's pair simulates it).
comp-adversary: RUN by the issuer at the cut -- r73 c51 FAILS (local, a fresh process per route): 24 and 25 model-block GetObjects on the first request, just to name rows. Deployed cold first read 7.0-8.6 s (row Z-S355).
EGRESS CLASS, declared: NONE. No vendor, SEC, ft.com or wsj.com call; stored inputs only.
</preflight>

**Your worktree:** `C:/tmp/r73-245` (branch `wk-AMGT_RESAPP-245`, cut from the issuance commit). Work and commit only there. Start every shell call with `cd /c/tmp/r73-245`: a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout.

## 1. THE ACT -- `AMGT-aw-1` (round 73, decomposition s.81)

CTO ruling 1: profile the deployed cold first request by phase, then cut the dominant cuttable phase, with no spend.
The research read (`lib/research/api/scoped_amgt.py`):
- init is a median 215 ms;
- the DOMINANT phase is `_model_block_name` (~`:1213-1245`): about 50 calls and 11.85 MB to read `NAME` for 23 ranked names whose
  crosswalk has no name, 2.5-3.0 s per cold read;
- next is the mention parquet decode, 1.2-1.6 s (`monthly_chatter.py:287-297`).

1. **Phase lines.** On the request path of `/lead-panel/rankings/*/price` and `/lead-panel/timeseries/collected/chatter`, log one
   structured line per phase through the existing `_segment_log` (~`:6065`), prefix `AMGT_PHASE`, e.g.
   `AMGT_PHASE route=<r> phase=<name> ms=<n>`. Phases: names, classification, generation read, mentions decode, compute, serialize.
   These are logs only; no served field changes.
2. **The cut.** Name the 23 from the stored Bloomberg refdata object (`raw/bloomberg/<KEY>/.../refdata.json`, field `NAME`; read
   the newest; a few KB each) instead of the whole model block, through `_clean_display_name`. Keep the model-block read as a
   fallback only when no refdata object exists.
3. **Values unchanged.** Before any edit, capture the 9 Lead Panel bodies into `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/before/`. Write
   `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/after_equal.py`, which prints `EQUAL n of 9` (ignoring `generated_at` at any depth).
4. **The phase table.** Write `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/PHASES.md`: a fresh-process local profile per route, before and after, per phase.

Run `lib/research/api/tests/` before your commit and report its last line. If one api test fails only because it reads a portal function absent at this worktree's portal ref, name it in your report and file no row; the issuer grades the suite on the shared tree. **Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing.** Rows: id form `AMGT_RESAPP-Z-W245-S<k>`, `disarm_owner` `2.0.0_SA_COO~Z`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no store write, no table, no schedule, no vendor or model call, no portal write.
2. No served value changes (AC2). Logs are added only through `_segment_log`.
3. Any reason you serve is in plain words. Do not use identity, unresolved, security key, crosswalk, dossier, landed, model block, estate, stage or input ledger.
4. Standing: no S3 delete, no push of shared branches.

## 3. SURFACES

<paths>
lib/research/api/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; timeout 1800)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-aw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round73/checks/r73_served.py" --cell c51 --where local; echo "exit=$?"</invocation><expect>model-block GetObjects on the first request read rankings 0 and chatter 0; C1 PASS; R73 C51 SERVED: YES; and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-aw-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/after_equal.py"; echo "exit=$?"</invocation><expect>EQUAL 9 of 9; and exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~245 <0.9.0_WK_AMGT_RESAPP~245@opal.agent>" -F <msgfile> -- <paths>`
(message file written with the Write tool; confirm with `git log -1`). Instance at
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~245/AMGT_RESAPP.TO-AMGT-aw-1.cold-path-cut.proof_of_spec.json`.
Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.
Report once:
- the commit hash;
- every criterion's output lines;
- the api suite's last line;
- the PHASES.md before/after table;
- the new S3 read prefix;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** CTO round-72 analysis item 1, ruling 1; rows Z-S355, Z-W242-S1 (superseded for latency by the route's stored-name source, s.81a). Deployed phases read at aw-7.

<status>pending</status>
<round>73</round>
<slot>0.9.0_WK_AMGT_RESAPP~245</slot>
<fabric>site-z</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
